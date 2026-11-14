"""Argus-V1 loop feature cache: pooled block-L activations for every train/validation STEP (action) of the
October (batch 20261016) and November (20261102-04) scenario_rollout data on the HF Hub.

Raw tensors are never written to disk. Each step's ``rollout/steps/step_NNN/capture/features.npz`` member
``block_00LL`` (n_obs x 2880 float32, rows = the step's observation points in ``rollout.json`` order) is read into
memory from the parquet row group that holds it, pooled, and only the pooled float16 vectors are stored.

Pools per layer L (all over the step's observation rows, block-L output = residual stream):
  max   element-wise max over all rows            (Argus-V1 = max at L16)
  mean  element-wise mean over all rows
  pre   the ``pre_action`` row (last observation before the action; falls back to the last row, flagged)
  rend  the ``reasoning_end`` row (NaN when the step has none, ``has_rend=0``)

Observation grid: every unit records ``observe_every`` (rollout.json; units recorded before the field = 32).
Rows are thinned to the 32-token grid (``grid32_keep``: pre_reasoning / reasoning_end / pre_action always kept,
``reasoning+N`` only when N % 32 == 0) before pooling, so 8-token captures pool exactly like the 32-grid data
and observe_every=32 outputs are byte-identical to the first build. observe_every per step: features/steps_grid.csv.

Test-split and sealed units (scenario in neither split file) are listed by unit_id + split only. Their
rollout.json is not read, their tensor rows are never decoded, and row groups are chosen only for train /
validation rows. A row group that also holds other units' rows is read as one column chunk (the smallest
transfer unit of parquet); rows of other units in it are never converted (``.as_py()`` is only called on
wanted rows) and the count of such row groups is reported.

Stages (each resumable; ``all`` runs them in order):
  labels   label table from the label files + split files          -> OUT/labels/*.csv (first table only)
  relabel  labels-only rebuild: human > convention > sidecar > draft -> OUT/labels/labels_trainval.v2.csv,
           labels/steps.v2.csv; no tensors, feature files untouched; --make-view links features_labels_v2/
  meta     rollout.json of train/validation units (files table)    -> OUT/meta/rollouts.jsonl (append, per unit)
  points   observation token_index + observe_every per unit         -> OUT/meta/obs_points.jsonl (append, per unit)
  steps    join labels x rollout steps                             -> OUT/features/steps.csv, steps_grid.csv
  plan     row-group work list for the wanted tensor rows           -> OUT/plan.json
  build    fetch + pool into preallocated float16 memmaps           -> OUT/features/L{LL}_{pool}.npy, done.txt
  finalize checks + sha256 + stats                                  -> OUT/features/manifest.json

  py -3.11 experiments/risk_loop/argus_loop/build_features.py all --workers 6
  py -3.11 experiments/risk_loop/argus_loop/build_features.py build --limit-units 3 --smoke   # smoke test
"""
from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import io
import json
import os
import re
import shutil
import sys
import threading
import time
from collections import Counter, defaultdict
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
import hf_select  # noqa: E402

OUT = ROOT / "artifacts/risk-loop/argus-v1-loop"
FEAT = OUT / "features"
LOG = OUT / "build.log"
LAYERS = (8, 11, 14, 16, 20, 23)
POOLS = ("max", "mean", "pre", "rend")
HIDDEN = 2880
REPORT_TOOLS = {"write_report", "stop", "submit_result"}
GRID = 32           # observation grid every model trains on (old Oct/Nov data were captured on it)
OLD_OBSERVE_EVERY = 32  # rollout.json without an ``observe_every`` field (all Oct/Nov units)
OCT_LABELS = ROOT / "ArgusV_review_progress.json"
NOV_LABELS_DEFAULT = Path(os.environ.get("ARGUS_NOV_LABELS", "")) if os.environ.get("ARGUS_NOV_LABELS") else None
HF_OCT_LABELS = "label_review/ArgusV_review_progress.json"
HF_NOV_LABELS = "label_review/ArgusV_november_auto_review.json.gz"
HF_NOV_HUMAN = "label_review/ArgusV_november_review_progress.json"  # dashboard-saved human reviews
LABEL_REVISION = "57a4bdcd22a57e0dd5ac9f8b0c2dd61741867788"  # HF commit the label files are read at (relabel)
OVERRIDES = ROOT / "reports/risk-loop/argus-v1/loop/data/label_overrides.csv"  # local user convention decisions
LABELS_V1 = "labels_trainval.csv"     # first label table (never overwritten)
LABELS_V2 = "labels_trainval.v2.csv"  # relabel output (precedence human > convention > sidecar > draft rule)
FEAT_V2 = OUT / "features_labels_v2"  # view for evaluate.load(root): relabelled steps.csv + hard links
SPLITS = (ROOT / "Scenario/scenario-splits.v1.json", ROOT / "Scenario/scenario-splits.v2.json")
MIN_FREE = 3 * 2**30
MAX_CACHE = 3 * 2**30
STEP_PATH = re.compile(r"^rollout/steps/step_(\d+)/capture/features\.npz$")
LABEL_COLS = ["unit_id", "scenario_id", "condition", "seed", "trajectory_id", "action_id", "step_index", "label",
              "label_status", "source", "split"]
STEP_COLS = ["row", "unit_id", "scenario_id", "condition", "seed", "trajectory_id", "action_id", "step_index",
             "tool", "kind", "label", "label_status", "source", "family", "split", "report_content", "n_obs",
             "prefix_length", "has_rend", "pre_is_pre_action", "obs_kinds"]
GRID_COLS = ["row", "unit_id", "step_index", "observe_every", "n_obs_raw", "n_obs_32"]


# ---------------------------------------------------------------------- small helpers
_log_lock = threading.Lock()


def say(*parts) -> None:
    line = time.strftime("%Y-%m-%d %H:%M:%S ") + " ".join(str(p) for p in parts)
    with _log_lock:
        print(line, flush=True)
        OUT.mkdir(parents=True, exist_ok=True)
        with open(LOG, "a", encoding="utf-8") as fh:
            fh.write(line + "\n")


def free_bytes(path: Path = ROOT) -> int:
    return shutil.disk_usage(path).free


def require_free(need: int = 0) -> None:
    free = free_bytes()
    if free - need < MIN_FREE:
        raise SystemExit(f"[abort] free disk {free / 2**30:.2f} GB - planned {need / 2**30:.2f} GB < 3 GB")


def tool_of(step: dict) -> str:
    """Tool name for evaluation grouping only (never a model input)."""
    cmd = step.get("command")
    if step.get("kind") == "tool" and isinstance(cmd, str):
        try:
            return json.loads(cmd).get("tool", "") or ""
        except json.JSONDecodeError:
            return ""
    return step.get("kind") or ""


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 22), b""):
            h.update(chunk)
    return h.hexdigest()


def write_csv(path: Path, rows: list[dict], cols: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    with open(tmp, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    tmp.replace(path)


def read_csv(path: Path) -> list[dict]:
    with open(path, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


# ---------------------------------------------------------------------- pooling (pure, unit-tested)
def pool_step(arr: np.ndarray, kinds: list[str]) -> tuple[dict[str, np.ndarray], dict]:
    """Pool one step's observation rows (n_obs x H, any float dtype) -> float32 vectors + flags."""
    if arr.ndim != 2 or arr.shape[0] != len(kinds) or arr.shape[0] == 0:
        raise ValueError(f"rows {arr.shape} vs {len(kinds)} observation kinds")
    a = np.asarray(arr, dtype=np.float32)
    pre_rows = [i for i, k in enumerate(kinds) if k == "pre_action"]
    rend_rows = [i for i, k in enumerate(kinds) if k == "reasoning_end"]
    pre_i = pre_rows[-1] if pre_rows else a.shape[0] - 1
    out = {"max": a.max(0), "mean": a.mean(0, dtype=np.float64).astype(np.float32), "pre": a[pre_i].copy(),
           "rend": a[rend_rows[-1]].copy() if rend_rows else np.full(a.shape[1], np.nan, np.float32)}
    flags = {"has_rend": int(bool(rend_rows)), "pre_is_pre_action": int(bool(pre_rows)),
             "pre_is_last": int(pre_i == a.shape[0] - 1)}
    return out, flags


# ---------------------------------------------------------------------- 32-token grid thinning (pure, unit-tested)
_REASONING = re.compile(r"^reasoning\+(\d+)$")


def unit_observe_every(rollout: dict) -> int:
    """``observe_every`` of a unit's rollout.json; units recorded before the field existed used 32."""
    v = rollout.get("observe_every")
    return OLD_OBSERVE_EVERY if v is None else int(v)


def grid32_keep(kinds: list[str], every: int, grid: int = GRID) -> list[bool]:
    """Which observation rows lie on the ``grid``-token grid of argus_hook.scenario_rollout.observation_points.

    observation_points(prompt_length, spans, every) puts ``reasoning+N`` at reasoning offset N for N = every,
    2*every, ... (strictly before the last reasoning token), plus ``pre_reasoning``, ``reasoning_end`` and
    ``pre_action``, which do not depend on ``every``. When ``every`` divides ``grid`` the grid points are exactly
    the ``reasoning+N`` rows with N % grid == 0 (same range bound, same setdefault collisions), so thinning is a
    pure function of the kind names. For every == grid it keeps every row (old data unchanged)."""
    if every < 1 or grid % every:
        raise ValueError(f"observe_every={every} does not divide the {grid}-token grid")
    keep = []
    for k in kinds:
        m = _REASONING.match(k)
        if m is None:
            if k not in ("pre_reasoning", "reasoning_end", "pre_action"):
                raise ValueError(f"unknown observation kind {k!r}")
            keep.append(True)
            continue
        n = int(m.group(1))
        if n % every:
            raise ValueError(f"kind {k!r} is not on the observe_every={every} grid")
        keep.append(n % grid == 0)
    return keep


def thin_to_grid32(arr: np.ndarray | None, kinds: list[str], every: int, token_index: list[int] | None = None):
    """(rows, kinds, token_index) restricted to the 32-token grid. ``arr`` / ``token_index`` may be None."""
    keep = grid32_keep(kinds, every)
    if arr is not None and arr.shape[0] != len(kinds):
        raise ValueError(f"rows {arr.shape} vs {len(kinds)} observation kinds")
    if all(keep):  # old (observe_every=32) data: return the inputs untouched -> bit-identical pooling
        return arr, list(kinds), (None if token_index is None else list(token_index))
    idx = [i for i, k in enumerate(keep) if k]
    return (None if arr is None else arr[idx], [kinds[i] for i in idx],
            None if token_index is None else [token_index[i] for i in idx])


# ---------------------------------------------------------------------- labels
def load_splits() -> dict[str, str]:
    out = {}
    for path in SPLITS:
        for split, ids in json.loads(path.read_text(encoding="utf-8"))["splits"].items():
            for sid in ids:
                assert out.get(sid, split) == split, sid
                out[sid] = split
    return out


def _hub_json(path: str, revision: str | None = None):
    from huggingface_hub import HfFileSystem

    at = f"@{revision}" if revision else ""
    with HfFileSystem().open(f"datasets/{hf_select.DEFAULT_REPO}{at}/{path}", "rb") as fh:
        data = fh.read()
    return json.loads(gzip.decompress(data) if path.endswith(".gz") else data)


def _int01(v) -> int | None:
    s = str(v).strip().lower() if v is not None else ""
    if s in ("", "null", "none", "nan"):
        return None
    if s not in ("0", "1"):
        raise ValueError(f"label must be 0/1/empty, got {v!r}")
    return int(s)


def read_overrides(path: Path | None) -> dict[tuple[str, int], dict]:
    """Local convention decisions (reports/.../data/label_overrides.csv). Rows with an empty gold_violation
    are ignored (no decision -> the item stays a draft)."""
    out = {}
    if not path or not Path(path).is_file():
        return out
    with open(path, newline="", encoding="utf-8-sig") as fh:
        for r in csv.DictReader(fh):
            y = _int01(r.get("gold_violation"))
            if y is None:
                continue
            key = (r["unit_id"].strip(), int(r["step_index"]))
            assert key not in out, f"duplicate override {key}"
            out[key] = {"label": y, "action_id": (r.get("action_id") or "").strip(),
                        "status": (r.get("status") or "").strip() or "nov_convention"}
    return out


def human_reviews(doc: dict | None) -> tuple[dict[tuple[str, int], dict], Counter]:
    """Dashboard-saved human labels: records with human_confirmed=true and a non-null gold_violation."""
    out, skipped = {}, Counter()
    if not doc:
        return out, skipped
    for part in ("samples", "pending_reviews"):
        for s in doc.get(part) or []:
            if s.get("human_confirmed") is not True:
                skipped[f"{part}:not_human_confirmed"] += 1
                continue
            if s.get("gold_violation") is None:
                skipped[f"{part}:null_gold"] += 1
                continue
            key = (s["unit_id"], int(s["step_index"]))
            if key in out and out[key]["gold_violation"] != s["gold_violation"]:
                raise ValueError(f"conflicting human labels for {key}")
            out[key] = s
    return out, skipped


def load_labels(oct_path: Path | None, nov_path: Path | None, *, nov_human: dict | None = None,
                overrides: dict | None = None, revision: str | None = None) -> tuple[list[dict], dict]:
    """All labelled actions (every split). Only small JSON label files are read.

    November precedence (highest first): human dashboard review (``nov_human``) > local convention decision
    (``overrides`` -> ``nov_convention``) > auto-review sidecar (``nov_auto_confirmed`` / ``nov_reviewed``) >
    rule draft ``original_policy_label`` (``nov_draft_rule``). October is unchanged (``oct_human`` /
    ``oct_delegated``). ``nov_human=None`` and ``overrides=None`` give the first (v1) label table."""
    oct_doc = json.loads(oct_path.read_text(encoding="utf-8")) if oct_path and oct_path.is_file() \
        else _hub_json(HF_OCT_LABELS, revision)
    if nov_path and nov_path.is_file():
        with gzip.open(nov_path, "rt", encoding="utf-8") as fh:
            nov_doc = json.load(fh)
    else:
        nov_doc = _hub_json(HF_NOV_LABELS, revision)
    splits = load_splits()
    rows, dropped = [], Counter()
    human, human_skipped = human_reviews(nov_human)
    overrides = overrides or {}
    used_h, used_o, changes, conflicts = set(), set(), Counter(), []

    def add(s, label, status, source):
        if source == "nov":
            key = (s["unit_id"], int(s["step_index"]))
            prev = (label, status)
            if key in overrides:
                o = overrides[key]
                if o["action_id"] and s.get("action_id") and o["action_id"] != s["action_id"]:
                    raise ValueError(f"override action_id mismatch {key}: {o['action_id']} != {s['action_id']}")
                if status != "nov_draft_rule" and label is not None and label != o["label"]:
                    conflicts.append({"key": list(key), "over": status, "was": label, "now": o["label"]})
                label, status = o["label"], o["status"]
                used_o.add(key)
            if key in human:
                h = human[key]
                if h.get("action_id") and s.get("action_id") and h["action_id"] != s["action_id"]:
                    raise ValueError(f"human review action_id mismatch {key}")
                label, status = int(h["gold_violation"]), "nov_human"
                used_h.add(key)
            if (label, status) != prev:
                changes[f"{prev[1]}:{prev[0]}->{status}:{label}"] += 1
        if label is None:
            dropped[f"{source}:{status}:null"] += 1
            return
        rows.append({"unit_id": s["unit_id"], "scenario_id": s["scenario_id"], "condition": s["condition"],
                     "seed": s["seed"], "trajectory_id": s["trajectory_id"], "action_id": s["action_id"],
                     "step_index": int(s["step_index"]), "label": int(label), "label_status": status,
                     "source": source, "split": splits.get(s["scenario_id"], "sealed"),
                     "_kind": s.get("kind"), "_command": s.get("command")})

    for s in oct_doc["samples"]:
        add(s, s.get("gold_violation"), "oct_human" if s.get("human_confirmed") else "oct_delegated", "oct")
    for s in nov_doc["samples"]:
        add(s, s.get("gold_violation"), "nov_auto_confirmed", "nov")
    for s in nov_doc["pending_reviews"]:
        if s.get("gold_violation") is not None:
            add(s, s["gold_violation"], "nov_reviewed", "nov")
        else:
            add(s, s.get("original_policy_label"), "nov_draft_rule", "nov")
    # human reviews of actions that are in neither sidecar list
    for key, h in sorted(human.items()):
        if key not in used_h:
            used_h.add(key)
            changes["absent->nov_human"] += 1
            rows.append({"unit_id": h["unit_id"], "scenario_id": h["scenario_id"], "condition": h["condition"],
                         "seed": h["seed"], "trajectory_id": h["trajectory_id"], "action_id": h["action_id"],
                         "step_index": int(h["step_index"]), "label": int(h["gold_violation"]),
                         "label_status": "nov_human", "source": "nov",
                         "split": splits.get(h["scenario_id"], "sealed"),
                         "_kind": h.get("kind"), "_command": h.get("command")})
    keys = Counter((r["unit_id"], r["step_index"]) for r in rows)
    dup = [k for k, c in keys.items() if c > 1]
    assert not dup, f"duplicate action rows: {dup[:3]}"
    unused = sorted(set(overrides) - used_o)
    if unused:
        raise ValueError(f"overrides not matching any November action: {unused[:3]}")
    info = {"dropped_null": dict(dropped)}
    if nov_human is not None or overrides:
        info.update({"nov_human_reviews": len(human), "nov_human_skipped": dict(human_skipped),
                     "overrides_applied": len(used_o), "override_conflicts_with_confirmed": conflicts,
                     "label_changes_vs_sidecar": dict(sorted(changes.items()))})
    return rows, info


def _summary(rows: list[dict], info: dict, args) -> dict:
    cnt = Counter((r["source"], r["split"]) for r in rows)
    pos = Counter((r["source"], r["split"]) for r in rows if r["label"] == 1 and r["split"] in ("train", "validation"))
    info.update({"actions_by_source_split": {f"{a}|{b}": c for (a, b), c in sorted(cnt.items())},
                 "positives_trainval": {f"{a}|{b}": c for (a, b), c in sorted(pos.items())},
                 "units_by_source_split": {f"{a}|{b}": c for (a, b), c in sorted(
                     Counter((r["source"], r["split"]) for r in {(r["unit_id"], r["source"], r["split"]): r
                                                                  for r in rows}.values()).items())},
                 "sealed_or_test_units": len({r["unit_id"] for r in rows if r["split"] in ("test", "sealed")}),
                 "oct_labels": str(args.oct_labels), "nov_labels": str(args.nov_labels)})
    return info


def stage_labels(args) -> None:
    lab = OUT / "labels"
    if (lab / LABELS_V1).is_file():
        raise SystemExit(f"[labels] {lab / LABELS_V1} exists and is never overwritten; "
                         f"use the labels-only stage `relabel` (writes {LABELS_V2})")
    rows, info = load_labels(args.oct_labels, args.nov_labels)
    tv = [r for r in rows if r["split"] in ("train", "validation")]
    write_csv(lab / LABELS_V1, tv, LABEL_COLS)
    # test / sealed: unit id + split only (no labels, no steps)
    sealed = sorted({(r["unit_id"], r["split"], r["source"]) for r in rows if r["split"] in ("test", "sealed")})
    write_csv(lab / "sealed_units.csv", [{"unit_id": u, "split": s, "source": src} for u, s, src in sealed],
              ["unit_id", "split", "source"])
    info = _summary(rows, info, args)
    (lab / "labels_summary.json").write_text(json.dumps(info, indent=1), encoding="utf-8")
    say("[labels]", json.dumps(info))


def relabel_steps(steps: list[dict], labels: list[dict]) -> tuple[list[dict], dict]:
    """Copy of the step table with label / label_status taken from ``labels`` (same rows, same order, so the
    feature arrays stay aligned). Rows without a label become null (dropped by evaluate.load)."""
    by_key = {(r["unit_id"], int(r["step_index"])): r for r in labels}
    out, stat = [], Counter()
    for s in steps:
        r = by_key.get((s["unit_id"], int(s["step_index"])))
        t = dict(s)
        if r is None:
            t["label"], t["label_status"] = "", "no_label_v2"
            stat["now_null"] += 1
        else:
            if r["action_id"] != s["action_id"]:
                raise ValueError(f"action_id mismatch {s['unit_id']}:{s['step_index']}")
            t["label"], t["label_status"] = str(int(r["label"])), r["label_status"]
            if str(s["label"]) != t["label"]:
                stat[f"{s['split']}:{s['label_status']}:{s['label']}->{t['label_status']}:{t['label']}"] += 1
            elif s["label_status"] != t["label_status"]:
                stat[f"{s['split']}:{s['label_status']}->{t['label_status']} (same label {t['label']})"] += 1
        # same rule as stage_steps: October report-tool positives
        t["report_content"] = str(int(t["source"] == "oct" and t["label"] == "1" and t["tool"] in REPORT_TOOLS))
        out.append(t)
    have = {(s["unit_id"], int(s["step_index"])) for s in steps}
    stat["labelled_trainval_without_features"] = sum(
        1 for r in labels if r["split"] in ("train", "validation") and (r["unit_id"], int(r["step_index"])) not in have)
    return out, dict(sorted(stat.items()))


def stage_relabel(args) -> None:
    """Labels-only rebuild: no tensors, no rollout.json, feature files untouched. Writes labels_trainval.v2.csv,
    labels_summary.v2.json and a relabelled step table (labels/steps.v2.csv). ``--make-view`` also builds
    FEAT_V2 = steps.csv (v2) + hard links to the feature arrays, a root for ``evaluate.load(root)``."""
    from huggingface_hub import HfApi

    rev = args.revision or LABEL_REVISION
    head = HfApi().dataset_info(hf_select.DEFAULT_REPO).sha
    if head != rev:
        say(f"[relabel] WARNING: HF head {head} != label revision {rev}; check for newer human reviews")
    human_doc = _hub_json(HF_NOV_HUMAN, rev)
    overrides = read_overrides(args.overrides)
    rows, info = load_labels(args.oct_labels, args.nov_labels, nov_human=human_doc, overrides=overrides,
                             revision=rev)
    lab = OUT / "labels"
    tv = [r for r in rows if r["split"] in ("train", "validation")]
    if (lab / LABELS_V2).is_file() and not args.force:
        raise SystemExit(f"[relabel] {lab / LABELS_V2} exists (use --force to rewrite the v2 table)")
    write_csv(lab / LABELS_V2, tv, LABEL_COLS)
    new_steps, stat = relabel_steps(read_csv(FEAT / "steps.csv"), tv)
    write_csv(lab / "steps.v2.csv", new_steps, STEP_COLS)
    info = _summary(rows, info, args)
    info.update({"label_revision": rev, "hf_head_at_build": head, "overrides_file": str(args.overrides),
                 "overrides_sha256": sha256_file(args.overrides) if args.overrides and args.overrides.is_file()
                 else None,
                 "oct_labels_sha256": sha256_file(args.oct_labels) if args.oct_labels and args.oct_labels.is_file()
                 else f"hub:{HF_OCT_LABELS}@{rev}",
                 "nov_labels_source": str(args.nov_labels) if args.nov_labels and args.nov_labels.is_file()
                 else f"hub:{HF_NOV_LABELS}@{rev}",
                 "nov_human_source": f"hub:{HF_NOV_HUMAN}@{rev}",
                 "status_trainval": {f"{a}|{b}|{c}": n for (a, b, c), n in sorted(
                     Counter((r["source"], r["split"], r["label_status"]) for r in tv).items())},
                 "positives_by_status_trainval": {f"{a}|{b}|{c}": n for (a, b, c), n in sorted(
                     Counter((r["source"], r["split"], r["label_status"]) for r in tv if r["label"] == 1).items())},
                 "steps_v2": stat, "labels_v2_sha256": sha256_file(lab / LABELS_V2),
                 "steps_v2_sha256": sha256_file(lab / "steps.v2.csv"),
                 "built_at": time.strftime("%Y-%m-%dT%H:%M:%S")})
    (lab / "labels_summary.v2.json").write_text(json.dumps(info, indent=1, ensure_ascii=False), encoding="utf-8")
    say("[relabel]", json.dumps({k: info[k] for k in ("label_changes_vs_sidecar", "steps_v2", "nov_human_reviews",
                                                       "overrides_applied", "positives_trainval")},
                                ensure_ascii=False))
    if args.make_view:
        make_view(lab / "steps.v2.csv", FEAT_V2)


def make_view(steps_csv: Path, view: Path, feat: Path | None = None) -> None:
    """steps.csv copy + HARD LINKS (no data copy) to the feature arrays and row_status.csv."""
    feat = feat or FEAT
    view.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(steps_csv, view / "steps.csv")
    for src in sorted(feat.glob("L*_*.npy")) + [feat / "row_status.csv"]:
        dst = view / src.name
        if dst.exists():
            if os.path.samefile(src, dst):
                continue
            raise SystemExit(f"[view] {dst} exists and is not a link to {src}")
        os.link(src, dst)
    say(f"[view] {view}: steps.csv + {len(list(view.glob('L*_*.npy')))} hard-linked arrays")


# ---------------------------------------------------------------------- hub access
class Hub:
    """HubSelector for the index + a thread-local filesystem for row-group reads."""

    def __init__(self, revision: str | None = None):
        self.sel = hf_select.HubSelector(revision=revision, log=lambda m: say(m))
        self.revision = self.sel._pin_revision()
        self._tl = threading.local()
        self.bytes_lock = threading.Lock()
        self.bytes_read = 0

    def open(self, shard: str):
        from huggingface_hub import HfFileSystem

        if not hasattr(self._tl, "fs"):
            self._tl.fs = HfFileSystem(token=self.sel._resolve_token(), skip_instance_cache=True)
        return self._tl.fs.open(f"datasets/{self.sel.repo}@{self.revision}/{shard}", "rb", block_size=8 * 2**20)


def trainval_units() -> dict[str, dict]:
    units = {}
    for r in read_csv(OUT / "labels/labels_trainval.csv"):
        units.setdefault(r["unit_id"], {"source": r["source"], "split": r["split"], "scenario_id": r["scenario_id"]})
    return units


def stage_meta(args) -> None:
    """rollout.json of train/validation units only, compacted to what the step table needs."""
    hub = Hub(args.revision)
    units = trainval_units()
    path = OUT / "meta/rollouts.jsonl"
    path.parent.mkdir(parents=True, exist_ok=True)
    done = set()
    if path.is_file():
        for line in open(path, encoding="utf-8"):
            try:
                done.add(json.loads(line)["unit_id"])
            except (json.JSONDecodeError, KeyError):
                pass  # torn last line from a crash: that unit is redone
    todo = sorted(u for u in units if u not in done)
    if args.limit_units:
        todo = todo[:args.limit_units] if not args.units else [u for u in args.units if u not in done]
    manifest_units = hub.sel.units()
    missing = [u for u in todo if u not in manifest_units]
    if missing:
        say(f"[meta] {len(missing)} train/val units not in the Hub manifest (skipped): {missing[:5]}")
    todo = [u for u in todo if u in manifest_units]
    say(f"[meta] {len(done)} done, {len(todo)} to fetch")
    batch = 50
    with open(path, "a", encoding="utf-8") as out:
        for i in range(0, len(todo), batch):
            chunk = todo[i:i + batch]
            rows = hub.sel.select(units=chunk, table="files", path_glob="rollout/rollout.json")
            for key, data, _ in hub.sel.fetch_values(rows):
                d = json.loads(data)
                steps = [{"step_index": s.get("step_index", k), "action_id": s.get("action_id"),
                          "kind": s.get("kind"), "tool": tool_of(s), "action_start": s.get("action_start"),
                          "obs_kinds": [o["kind"] for o in s.get("observations") or []],
                          "capture_dir": s.get("capture_dir")} for k, s in enumerate(d.get("steps") or [])]
                out.write(json.dumps({"unit_id": key[0], "scenario_id": d.get("scenario_id"),
                                      "family": d.get("family"), "condition": d.get("condition"),
                                      "seed": d.get("seed"), "trajectory_id": d.get("trajectory_id"),
                                      "steps": steps}, ensure_ascii=False) + "\n")
            out.flush()
            say(f"[meta] {min(i + batch, len(todo))}/{len(todo)} units")


POINTS = OUT / "meta/obs_points.jsonl"


def stage_points(args) -> None:
    """Observation positions (token_index) + observe_every of every unit in steps.csv, from rollout.json (files
    table, train/validation units only). Backfill for units whose meta line predates those fields."""
    hub = Hub(args.revision)
    units = sorted({s["unit_id"] for s in read_csv(FEAT / "steps.csv")})
    POINTS.parent.mkdir(parents=True, exist_ok=True)
    done = set()
    if POINTS.is_file():
        for line in open(POINTS, encoding="utf-8"):
            try:
                done.add(json.loads(line)["unit_id"])
            except (json.JSONDecodeError, KeyError):
                pass
    todo = [u for u in units if u not in done]
    say(f"[points] {len(done)} done, {len(todo)} to fetch")
    with open(POINTS, "a", encoding="utf-8") as out:
        for i in range(0, len(todo), 50):
            rows = hub.sel.select(units=todo[i:i + 50], table="files", path_glob="rollout/rollout.json")
            for key, data, _ in hub.sel.fetch_values(rows):
                d = json.loads(data)
                steps = [{"step_index": st.get("step_index", k), "action_start": st.get("action_start"),
                          "prompt_length": st.get("prompt_length"), "reasoning_span": st.get("reasoning_span"),
                          "kinds": [o["kind"] for o in st.get("observations") or []],
                          "token_index": [o.get("token_index") for o in st.get("observations") or []]}
                         for k, st in enumerate(d.get("steps") or [])]
                out.write(json.dumps({"unit_id": key[0], "observe_every": unit_observe_every(d),
                                      "observe_every_recorded": d.get("observe_every") is not None,
                                      "steps": steps}, ensure_ascii=False) + "\n")
            out.flush()
            say(f"[points] {min(i + 50, len(todo))}/{len(todo)} units")


def load_points() -> dict[str, dict]:
    out = {}
    for line in open(POINTS, encoding="utf-8"):
        try:
            d = json.loads(line)
        except json.JSONDecodeError:
            continue
        out[d["unit_id"]] = d
    return out


def load_meta() -> dict[str, dict]:
    out = {}
    for line in open(OUT / "meta/rollouts.jsonl", encoding="utf-8"):
        try:
            d = json.loads(line)
        except json.JSONDecodeError:
            continue
        out[d["unit_id"]] = d
    return out


def family_of(scenario_id: str, rollout_family: str | None) -> str:
    """v2: the F-number (equals rollout.json family). v1 (AV-S*): rollout.json ``family`` category, as in
    src/argus_v/probes/assembly.py (source_family_id = rollout.family) and D-v1 family_id."""
    m = re.match(r"^AVv2-(F\d+)-", scenario_id)
    if m:
        if rollout_family and rollout_family != m.group(1):
            raise ValueError(f"family mismatch {scenario_id} {rollout_family}")
        return m.group(1)
    return rollout_family or scenario_id


def stage_steps(args) -> None:
    labels = read_csv(OUT / "labels/labels_trainval.csv")
    meta = load_meta()
    rows, problems = [], Counter()
    for r in labels:
        m = meta.get(r["unit_id"])
        if m is None:
            problems["no_rollout_meta"] += 1
            continue
        k = int(r["step_index"])
        if k >= len(m["steps"]):
            problems["step_out_of_range"] += 1
            continue
        s = m["steps"][k]
        if s["action_id"] and s["action_id"] != r["action_id"]:
            problems["action_id_mismatch"] += 1
            continue
        if not s["obs_kinds"]:
            problems["no_observations"] += 1
            continue
        tool = s["tool"]
        y = int(r["label"])
        every = unit_observe_every(m)
        _, kinds, _ = thin_to_grid32(None, s["obs_kinds"], every)  # 32-grid kinds (old data: unchanged)
        rows.append({**{c: r[c] for c in LABEL_COLS}, "tool": tool, "kind": s["kind"],
                     "_observe_every": every, "_n_obs_raw": len(s["obs_kinds"]),
                     "family": family_of(r["scenario_id"], m.get("family")),
                     "report_content": int(r["source"] == "oct" and y == 1 and tool in REPORT_TOOLS),
                     "n_obs": len(kinds), "prefix_length": s["action_start"],
                     "has_rend": int("reasoning_end" in kinds), "pre_is_pre_action": int("pre_action" in kinds),
                     "obs_kinds": "|".join(kinds)})
    rows.sort(key=lambda x: ({"oct": 0, "nov": 1}[x["source"]], x["unit_id"], int(x["step_index"])))
    for i, x in enumerate(rows):
        x["row"] = i
    write_csv(FEAT / "steps.csv", rows, STEP_COLS)
    # observe_every per step in a sidecar, so steps.csv of observe_every=32 data stays byte-identical
    write_csv(FEAT / "steps_grid.csv", [{"row": x["row"], "unit_id": x["unit_id"], "step_index": x["step_index"],
                                         "observe_every": x["_observe_every"], "n_obs_raw": x["_n_obs_raw"],
                                         "n_obs_32": x["n_obs"]} for x in rows], GRID_COLS)
    say(f"[steps] {len(rows)} rows, problems {dict(problems)}, observe_every "
        f"{dict(Counter(x['_observe_every'] for x in rows))}")


# ---------------------------------------------------------------------- plan
def stage_plan(args) -> None:
    hub = Hub(args.revision)
    steps = read_csv(FEAT / "steps.csv")
    want = {(s["unit_id"], int(s["step_index"])): int(s["row"]) for s in steps}
    units = sorted({s["unit_id"] for s in steps})
    tv_units = set(trainval_units())
    shards = hub.sel.shards_for(units, "tensors")
    say(f"[plan] {len(units)} units over {len(shards)} tensor shards (indexing missing shards)")
    # index shards in parallel (metadata columns only; cached under artifacts/hf-index)
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        list(ex.map(hub.sel.shard_index, shards))
    groups: dict[tuple, dict] = {}
    chunked, layer_names = [], Counter()
    unit_set = set(units)
    for shard in shards:
        for r in hub.sel.shard_index(shard):
            g = groups.setdefault((shard, r["_rg"]), {"shard": shard, "rg": r["_rg"], "bytes": r["_rg_payload_bytes"],
                                                     "items": [], "foreign_rows": 0, "foreign_units": set(),
                                                     "foreign_nontv_units": set()})
            m = STEP_PATH.match(r["path"])
            L = hf_select.row_layer(r)
            ok = (r["unit_id"] in unit_set and m is not None and L in LAYERS
                  and (r["unit_id"], int(m.group(1))) in want)
            if not ok:
                g["foreign_rows"] += 1
                if r["unit_id"] not in unit_set:
                    g["foreign_units"].add(r["unit_id"])
                    if r["unit_id"] not in tv_units:
                        g["foreign_nontv_units"].add(r["unit_id"])
                continue
            if (r.get("chunk_count") or 1) > 1:
                chunked.append(r)
                continue
            layer_names[r.get("array_name")] += 1
            g["items"].append({"row": r["_row"], "srow": want[(r["unit_id"], int(m.group(1)))], "layer": L,
                               "unit_id": r["unit_id"], "dtype": r["dtype"], "shape": r["shape"],
                               "sha": r["chunk_sha256"]})
    work = [g for g in groups.values() if g["items"]]
    if chunked:
        raise SystemExit(f"[plan] {len(chunked)} wanted values are multi-chunk; not handled: {chunked[:2]}")
    found = Counter((it["srow"], it["layer"]) for g in work for it in g["items"])
    missing = [(s, L) for s in want.values() for L in LAYERS if (s, L) not in found]
    mixed = [g for g in work if g["foreign_nontv_units"]]
    plan = {"revision": hub.revision, "layers": LAYERS, "steps": len(steps), "units": len(units),
            "shards": len(shards), "row_groups": len(work),
            "transfer_bytes": int(sum(g["bytes"] for g in work)),
            "values": int(sum(len(g["items"]) for g in work)), "missing_values": len(missing),
            "missing_examples": missing[:10],
            "row_groups_with_test_or_sealed_rows": len(mixed),
            "bytes_of_row_groups_with_test_or_sealed_rows": int(sum(g["bytes"] for g in mixed)),
            "test_or_sealed_units_sharing_row_groups": sorted({u for g in mixed for u in g["foreign_nontv_units"]}),
            "work": [{k: (sorted(v) if isinstance(v, set) else v) for k, v in g.items()
                      if k not in ("foreign_units",)} for g in sorted(work, key=lambda g: (g["shard"], g["rg"]))]}
    (OUT / "plan.json").write_text(json.dumps(plan), encoding="utf-8")
    say("[plan]", json.dumps({k: v for k, v in plan.items() if k != "work"})[:3000])


# ---------------------------------------------------------------------- build
def _memmaps(n: int, mode: str) -> dict:
    out = {}
    for L in LAYERS:
        for p in POOLS:
            path = FEAT / f"L{L:02d}_{p}.npy"
            if mode == "w+" and path.is_file():
                mode_eff = "r+"
            else:
                mode_eff = mode
            if mode_eff == "w+":
                out[(L, p)] = np.lib.format.open_memmap(path, mode="w+", dtype=np.float16, shape=(n, HIDDEN))
                out[(L, p)][:] = np.nan  # rows never written stay NaN (detectable)
            else:
                out[(L, p)] = np.lib.format.open_memmap(path, mode="r+")
                assert out[(L, p)].shape == (n, HIDDEN), path
    return out


def _kinds_every(v) -> tuple[list[str], int]:
    """kinds_of value: raw kind list (observe_every 32) or (raw kinds, observe_every)."""
    if isinstance(v, tuple):
        return list(v[0]), int(v[1])
    return list(v), OLD_OBSERVE_EVERY


def raw_kinds_of(steps: list[dict]) -> dict[int, tuple[list[str], int]]:
    """srow -> (raw observation kinds as stored in the tensor rows, observe_every). Uses meta/rollouts.jsonl
    when the sidecar says a step was not on the 32 grid; old data: steps.csv kinds (identical)."""
    grid = {int(r["row"]): r for r in read_csv(FEAT / "steps_grid.csv")} if (FEAT / "steps_grid.csv").is_file() else {}
    meta = None
    out = {}
    for s in steps:
        g = grid.get(int(s["row"]))
        every = int(g["observe_every"]) if g else OLD_OBSERVE_EVERY
        if every == GRID:
            out[int(s["row"])] = (s["obs_kinds"].split("|"), every)
            continue
        meta = meta or load_meta()
        out[int(s["row"])] = (meta[s["unit_id"]]["steps"][int(s["step_index"])]["obs_kinds"], every)
    return out


def process_group(hub: Hub, g: dict, kinds_of: dict) -> tuple[dict, list]:
    """Read one row group's payload column, decode only the wanted rows, thin them to the 32-token grid, pool
    them. Returns (group, results)."""
    import pyarrow.parquet as pq

    for attempt in range(5):
        try:
            with hub.open(g["shard"]) as fh:
                pf = pq.ParquetFile(fh)
                table = pf.read_row_group(g["rg"], columns=["data"])
            break
        except Exception as exc:  # network hiccup: retry with backoff
            if attempt == 4:
                raise
            say(f"[retry] {g['shard']} rg {g['rg']}: {type(exc).__name__}: {exc}")
            time.sleep(5 * (attempt + 1))
    col = table.column("data")
    with hub.bytes_lock:
        hub.bytes_read += g["bytes"]
    res = []
    for it in g["items"]:
        value = col[it["row"]].as_py()  # only wanted rows are ever converted
        if hashlib.sha256(value).hexdigest() != it["sha"]:
            raise hf_select.SelectError(f"sha256 mismatch {g['shard']} rg {g['rg']} row {it['row']}")
        arr = np.frombuffer(value, dtype=np.dtype(it["dtype"])).reshape(tuple(it["shape"]))
        kinds, every = _kinds_every(kinds_of[it["srow"]])
        arr, kinds, _ = thin_to_grid32(arr, kinds, every)  # 32-token grid only (identity for old data)
        pooled, flags = pool_step(arr, kinds)
        res.append((it["srow"], it["layer"], pooled, flags))
    del table, col
    return g, res


def stage_build(args) -> None:
    plan = json.loads((OUT / "plan.json").read_text(encoding="utf-8"))
    steps = read_csv(FEAT / "steps.csv")
    n = len(steps)
    kinds_of = raw_kinds_of(steps)
    unit_of = {int(s["row"]): s["unit_id"] for s in steps}
    need = n * HIDDEN * 2 * len(LAYERS) * len(POOLS)
    if need > MAX_CACHE:
        raise SystemExit(f"[abort] cache {need / 2**30:.2f} GB > 3 GB")
    existing = sum((FEAT / f"L{L:02d}_{p}.npy").stat().st_size for L in LAYERS for p in POOLS
                   if (FEAT / f"L{L:02d}_{p}.npy").is_file())
    require_free(max(0, need - existing))
    work = plan["work"]
    mixed = [g for g in work if g["foreign_nontv_units"]]
    if not args.include_mixed:
        # Row groups that also hold test / sealed rows are skipped by default: parquet reads a whole column
        # chunk, so fetching them would move test/sealed tensor bytes over the network (never decoded, but
        # still transferred). Their train/validation values stay NaN until a run with --include-mixed.
        work = [g for g in work if not g["foreign_nontv_units"]]
        say(f"[build] skipping {len(mixed)} row groups shared with test/sealed units "
            f"({sum(len(g['items']) for g in mixed)} train/val values stay NaN; --include-mixed to fetch)")
    else:
        work = sorted(work, key=lambda g: bool(g["foreign_nontv_units"]))  # pure row groups first
    if args.limit_units:  # smoke test: only row groups of the chosen units, only their items
        chosen = set(args.units) if args.units else set(sorted({it["unit_id"] for g in work for it in g["items"]})
                                                          [:args.limit_units])
        work = [{**g, "items": [it for it in g["items"] if it["unit_id"] in chosen]} for g in work]
        work = [g for g in work if g["items"]]
    mm = _memmaps(n, "w+")
    done_path = FEAT / "done.txt"
    flags_path = FEAT / "flags.jsonl"
    done = set(done_path.read_text().split()) if done_path.is_file() else set()
    gid = lambda g: f"{g['shard']}#{g['rg']}" + (f"#smoke:{len(g['items'])}" if args.limit_units else "")
    todo = [g for g in work if gid(g) not in done]
    total_bytes = sum(g["bytes"] for g in todo)
    say(f"[build] revision={plan['revision']} {len(done)} groups done, {len(todo)} to do, "
        f"{total_bytes / 2**30:.2f} GB to transfer, workers={args.workers}")
    hub = Hub(plan["revision"])
    t0, moved, fin, stats = time.time(), 0, 0, Counter()
    units_total = len({it["unit_id"] for g in work for it in g["items"]})
    left_by_unit = Counter(it["unit_id"] for g in todo for it in g["items"])
    with ThreadPoolExecutor(max_workers=args.workers) as ex, open(done_path, "a") as dfh, \
            open(flags_path, "a", encoding="utf-8") as ffh:
        it_todo = iter(todo)
        running = set()

        def submit_next():
            g = next(it_todo, None)
            if g is not None:
                running.add(ex.submit(process_group, hub, g, kinds_of))

        for _ in range(args.workers * 2):
            submit_next()
        while running:
            fs, _ = wait(running, return_when=FIRST_COMPLETED)
            for f in fs:
                running.discard(f)
                g, res = f.result()  # any error aborts the run; finished groups stay in done.txt
                for srow, L, pooled, flags in res:
                    for p in POOLS:
                        v = pooled[p]
                        mm[(L, p)][srow] = v.astype(np.float16)
                        if p != "rend" or flags["has_rend"]:
                            if not np.isfinite(v).all() or np.abs(v).max() > 65504:
                                stats[f"nonfinite_or_overflow_{p}"] += 1
                    left_by_unit[unit_of[srow]] -= 1
                    ffh.write(json.dumps({"row": srow, "layer": L, **flags}) + "\n")
                for m in mm.values():
                    m.flush()
                ffh.flush()
                dfh.write(gid(g) + "\n")
                dfh.flush()
                os.fsync(dfh.fileno())
                fin += 1
                moved += g["bytes"]
                el = time.time() - t0
                rate = moved / el if el else 0
                eta = (total_bytes - moved) / rate if rate else float("nan")
                units_done = units_total - sum(1 for u, c in left_by_unit.items() if c > 0)
                say(f"[build] groups {fin}/{len(todo)} | units complete {units_done}/{units_total} | "
                    f"{moved / 2**30:.2f}/{total_bytes / 2**30:.2f} GB | {rate / 2**20:.1f} MB/s | "
                    f"ETA {eta / 60:.1f} min | free {free_bytes() / 2**30:.2f} GB" +
                    (f" | {dict(stats)}" if stats else ""))
                if free_bytes() < MIN_FREE:
                    raise SystemExit("[abort] free disk < 3 GB")
                submit_next()
    say(f"[build] finished {fin} groups in {time.time() - t0:.0f}s, {moved / 2**30:.2f} GB, stats {dict(stats)}")


# ---------------------------------------------------------------------- finalize
def stage_finalize(args) -> None:
    plan = json.loads((OUT / "plan.json").read_text(encoding="utf-8"))
    steps = read_csv(FEAT / "steps.csv")
    n = len(steps)
    done = set((FEAT / "done.txt").read_text().split())
    groups = {f"{g['shard']}#{g['rg']}" for g in plan["work"]}
    mixed_ids = {f"{g['shard']}#{g['rg']}" for g in plan["work"] if g["foreign_nontv_units"]}
    if not (groups - mixed_ids) <= done:
        raise SystemExit(f"[finalize] {len((groups - mixed_ids) - done)} row groups not done yet")
    shared_rows = {it["srow"] for g in plan["work"] if g["foreign_nontv_units"] for it in g["items"]}
    flags = {}
    for line in open(FEAT / "flags.jsonl", encoding="utf-8"):
        d = json.loads(line)
        flags[(d["row"], d["layer"])] = d
    missing = [(r, L) for r in range(n) for L in LAYERS if (r, L) not in flags]
    miss_rows = {r for r, _ in missing}
    write_csv(FEAT / "row_status.csv",
              [{"row": r, "in_shared_rowgroup": int(r in shared_rows), "features_complete": int(r not in miss_rows)}
               for r in range(n)], ["row", "in_shared_rowgroup", "features_complete"])
    hashes, nan_rows = {}, {}
    for L in LAYERS:
        for p in POOLS:
            path = FEAT / f"L{L:02d}_{p}.npy"
            a = np.load(path, mmap_mode="r")
            bad = np.isnan(a).any(1)
            nan_rows[f"L{L:02d}_{p}"] = int(bad.sum())
            hashes[path.name] = sha256_file(path)
    hashes["steps.csv"] = sha256_file(FEAT / "steps.csv")
    hashes["row_status.csv"] = sha256_file(FEAT / "row_status.csv")
    man = {"revision": plan["revision"], "layers": LAYERS, "pools": POOLS, "rows": n,
           "values_missing": len(missing), "rows_incomplete": len(miss_rows),
           "rows_in_shared_rowgroups": len(shared_rows),
           "shared_rowgroups_done": len(mixed_ids & done), "shared_rowgroups_total": len(mixed_ids),
           "rows_with_nan": nan_rows, "sha256": hashes,
           "transfer_bytes_tensors": plan["transfer_bytes"],
           "cache_bytes": int(sum((FEAT / k).stat().st_size for k in hashes)),
           "finalized_at": time.strftime("%Y-%m-%dT%H:%M:%S")}
    (FEAT / "manifest.json").write_text(json.dumps(man, indent=1), encoding="utf-8")
    say("[finalize]", json.dumps(man))
    stage_card(args)


# ---------------------------------------------------------------------- data card (Korean, user-facing)
CARD = ROOT / "reports/risk-loop/argus-v1/loop/data/card.md"


def stage_card(args) -> None:
    steps = read_csv(FEAT / "steps.csv")
    plan = json.loads((OUT / "plan.json").read_text(encoding="utf-8"))
    lab = json.loads((OUT / "labels/labels_summary.json").read_text(encoding="utf-8"))
    sealed = read_csv(OUT / "labels/sealed_units.csv")
    man_path = FEAT / "manifest.json"
    man = json.loads(man_path.read_text(encoding="utf-8")) if man_path.is_file() else None
    status = {int(r["row"]): r for r in read_csv(FEAT / "row_status.csv")} \
        if (FEAT / "row_status.csv").is_file() else {}
    mixed_groups = [g for g in plan["work"] if g["foreign_nontv_units"]]
    C = Counter
    L = []
    w = L.append
    w("# 데이터 카드 — Argus-V1 루프 특징 캐시")
    w("")
    w(f"만든 코드: `experiments/risk_loop/argus_loop/build_features.py` · HF `{hf_select.DEFAULT_REPO}` "
      f"revision `{plan['revision']}` (읽기 전용) · 갱신 {time.strftime('%Y-%m-%d %H:%M')}")
    w("")
    w("캐시 위치: `artifacts/risk-loop/argus-v1-loop/features/` (git 제외). 원본 텐서는 디스크에 쓰지 않았다.")
    w("")
    w("## 1. 텐서 구조 (HF에서 확인한 것)")
    w("")
    w("- 10월·11월 모두 같은 구조다. 한 행동(step)마다 `rollout/steps/step_NNN/capture/features.npz`의 멤버 "
      "`block_0000`~`block_0023`이 HF tensors 표의 한 행이다 (float32, 모양 `[n_obs, 2880]`, 나눠 저장된 값 없음).")
    w("- `layer_index`·`location`·`phase` 열은 비어 있고, 층은 이름 `block_00LL`에서 읽는다. "
      "capture/metadata.json의 `hook_point`는 `post_block_pre_final_norm` = block L 출력(residual stream).")
    w("- 행(n_obs)은 그 step의 관측 지점이며 순서는 `rollout.json`의 `steps[k].observations[].kind`와 같다: "
      "`pre_reasoning`(추론 시작 전) → `reasoning+32`, `reasoning+64`, …(추론 32토큰마다) → `reasoning_end`(추론 끝) "
      "→ `pre_action`(행동 직전 마지막 토큰). 모든 관측은 행동 토큰보다 앞이다.")
    w("- `prefix_length` = `steps[k].action_start` (= metadata.json `observed_prefix_length`, 행동 시작 토큰 위치).")
    w("- 도구 이름은 `steps[k].command`의 JSON `tool`(kind가 tool일 때), 아니면 `kind`(bash/stop). 평가 그룹 전용.")
    w("")
    w("## 2. 특징 정의")
    w("")
    w(f"층 L ∈ {list(LAYERS)}, 파일 `L{{LL}}_{{max,mean,pre,rend}}.npy` (float16, 행 = steps.csv의 `row`, 2880열).")
    w("")
    w("| 이름 | 정의 |")
    w("|---|---|")
    w("| max | step의 모든 관측 행에 대한 원소별 최댓값 (Argus-V1 = L16 max) |")
    w("| mean | 모든 관측 행의 평균 (float64로 합산) |")
    w("| pre | `pre_action` 행 (행동 직전 마지막 관측). 모든 step에 있음 |")
    w("| rend | `reasoning_end` 행. 없으면 NaN, `has_rend=0` |")
    w("")
    w("계산은 float32, 저장은 float16 (값 크기 ~1e3에서 반올림 오차 ≤ 0.5). 값을 아직 받지 않은 행은 NaN.")
    w("")
    w("## 3. 행 수 (train·validation만 특징 있음)")
    w("")
    by = C((s["source"], s["split"]) for s in steps)
    pos = C((s["source"], s["split"]) for s in steps if s["label"] == "1")
    rc = C((s["source"], s["split"]) for s in steps if s["report_content"] == "1")
    fam = defaultdict(set)
    for s in steps:
        fam[(s["source"], s["split"])].add(s["family"])
    w("| 출처 | split | 행동 수 | 위반 | 그중 보고 내용 위반(10월, 기본 제외) | family 수 |")
    w("|---|---|---|---|---|---|")
    for k in sorted(by):
        w(f"| {k[0]} | {k[1]} | {by[k]:,} | {pos[k]} | {rc[k]} | {len(fam[k])} |")
    w(f"| 합계 | | {len(steps):,} | {sum(pos.values())} | {sum(rc.values())} | {len({s['family'] for s in steps})} |")
    w("")
    w("라벨 상태:")
    w("")
    w("| 출처 | split | label_status | 행동 수 | 위반 |")
    w("|---|---|---|---|---|")
    ls = C((s["source"], s["split"], s["label_status"]) for s in steps)
    lsp = C((s["source"], s["split"], s["label_status"]) for s in steps if s["label"] == "1")
    for k in sorted(ls):
        w(f"| {k[0]} | {k[1]} | {k[2]} | {ls[k]:,} | {lsp[k]} |")
    w("")
    w("- `oct_human`: 사람 확인, `oct_delegated`: 사용자 위임 판정 (둘 다 확정). `nov_auto_confirmed`: 11월 자동 확정 "
      "(전부 0). `nov_draft_rule`: 11월 보류 행동으로 `gold_violation`이 null이라 규칙 라벨 `original_policy_label`을 "
      "썼다 (**초안**).")
    w(f"- 라벨이 null이라 뺀 행동: {lab['dropped_null']}")
    w("")
    w("## 4. 도구별 (train, 10월 보고 내용 위반 제외)")
    w("")
    for src in ("oct", "nov", "all"):
        rows = [s for s in steps if s["split"] == "train" and (src == "all" or s["source"] == src)
                and s["report_content"] != "1"]
        t_all, t_pos = C(s["tool"] for s in rows), C(s["tool"] for s in rows if s["label"] == "1")
        both = [t for t in t_pos if t_all[t] - t_pos[t] > 0]
        both3 = [t for t in t_pos if t_pos[t] >= 3 and t_all[t] - t_pos[t] >= 3]
        w(f"- **{src}**: 위반이 있는 도구 {len(t_pos)}개, 정상·위반이 둘 다 있는 도구 {len(both)}개, "
          f"둘 다 3개 이상(판정 지표 대상) {len(both3)}개 (위반 {sum(t_pos[t] for t in both3)}개)")
        if src == "all":
            w("")
            w("| 도구 | train 행동 | 위반 |")
            w("|---|---|---|")
            for t, c in sorted(t_pos.items(), key=lambda x: -x[1]):
                w(f"| {t} | {t_all[t]} | {c} |")
    w("")
    w("## 5. 봉인 단위 (텐서·rollout.json을 받지 않음)")
    w("")
    sc = C((r["source"], r["split"]) for r in sealed)
    w(f"단위 ID와 split만 `artifacts/risk-loop/argus-v1-loop/labels/sealed_units.csv`에 적었다 (총 {len(sealed)}개: "
      + ", ".join(f"{a} {b} {c}개" for (a, b), c in sorted(sc.items())) + ").")
    w("`sealed`는 어느 split 파일에도 없는 11월 단위다. TASK.md에는 'AV-S43~S72'로 적혀 있지만 실제 시나리오 ID는 "
      "AV-S61~S80 (180개)이다. 11월의 AV-S12~S34 재실행 단위는 v1 split 파일을 따른다.")
    w("")
    w("## 6. test·봉인 단위와 같은 row group에 있는 값")
    w("")
    w(f"HF parquet는 row group 하나의 `data` 열 전체(약 62MB, ZSTD, 사전 페이지 포함, 페이지 색인 없음)가 최소 전송 "
      f"단위라 행 하나만 받을 수 없다. 필요한 row group {plan['row_groups']}개 중 "
      f"{plan['row_groups_with_test_or_sealed_rows']}개 ({plan['bytes_of_row_groups_with_test_or_sealed_rows'] / 2**30:.2f}"
      f" GiB)에 test·봉인 단위 {len(plan['test_or_sealed_units_sharing_row_groups'])}개의 행이 섞여 있다.")
    w(f"- 기본 실행은 이 row group들을 **받지 않는다**. 그 안의 train·validation 값 "
      f"{sum(len(g['items']) for g in mixed_groups):,}개(step×층)는 NaN으로 남는다.")
    w("- `build --include-mixed`로 받을 수 있다. 그때도 test·봉인 행은 바이트 변환·해석·계산을 하지 않는다 "
      "(`process_group`은 원하는 행만 `.as_py()`). 받을지는 감시·오케스트레이터가 정한다.")
    if status:
        n_shared = sum(1 for r in status.values() if r["in_shared_rowgroup"] == "1")
        n_inc = sum(1 for r in status.values() if r["features_complete"] == "0")
        w(f"- 현재: 섞인 row group에 값이 하나라도 있는 행 {n_shared:,}개, 특징이 다 차지 않은 행 {n_inc:,}개 "
          "(`features/row_status.csv`, 루프는 `features_complete=1`만 쓴다).")
        inc = C(f"{s['source']}/{s['split']}/y={s['label']}" for s in steps
                if status[int(s["row"])]["features_complete"] == "0")
        if inc:
            w(f"- 특징이 빠진 행 (출처/split/라벨): {dict(sorted(inc.items()))}")
    w("")
    w("## 7. 전송량·크기·해시")
    w("")
    w(f"- 계획 전송량 (텐서): 섞인 row group 제외 "
      f"{(plan['transfer_bytes'] - plan['bytes_of_row_groups_with_test_or_sealed_rows']) / 2**30:.2f} GiB, 포함하면 "
      f"{plan['transfer_bytes'] / 2**30:.2f} GiB. 받은 값 자체는 그중 약 23%이고 나머지는 같은 row group의 다른 층·단위다. "
      "rollout.json (files 표, 단위당 수십 KB)은 별도.")
    w("- 실제 진행·전송량은 `artifacts/risk-loop/argus-v1-loop/build.log`.")
    if man:
        w(f"- 캐시 크기 {man['cache_bytes'] / 2**30:.2f} GiB, 완성 {man['finalized_at']}, 빠진 값 {man['values_missing']:,}개")
        w("")
        w("| 파일 | sha256 |")
        w("|---|---|")
        for k, v in sorted(man["sha256"].items()):
            w(f"| {k} | `{v}` |")
    else:
        w(f"- steps.csv sha256 `{sha256_file(FEAT / 'steps.csv')}` (배열 해시는 finalize 뒤 `features/manifest.json`과 "
          "이 카드에 들어간다)")
    w("")
    w("## 8. steps.csv 열")
    w("")
    w("`row`(배열 행), `unit_id`, `scenario_id`, `condition`, `seed`, `trajectory_id`, `action_id`, `step_index`, "
      "`tool`(평가 그룹 전용), `kind`, `label`, `label_status`, `source`(oct/nov), `family`, `split`, "
      "`report_content`(10월 write_report/stop/submit_result 위반=1, 기본 제외), `n_obs`, `prefix_length`, `has_rend`, "
      "`pre_is_pre_action`, `obs_kinds`.")
    w("")
    w("family: 11월 v2는 시나리오 ID의 F번호 (rollout.json `family`와 같음을 확인), AV-S* (10월과 11월 재실행)는 rollout.json "
      "`family` 범주 (이전 D-v1 `family_id`와 같은 정의, `src/argus_v/probes/assembly.py`). "
      "모델 입력 허용은 activation과 `prefix_length`·`step_index`(기준선)뿐이다. condition·seed·tool·source·family는 "
      "입력 금지 (TASK.md §3).")
    CARD.parent.mkdir(parents=True, exist_ok=True)
    CARD.write_text("\n".join(L) + "\n", encoding="utf-8")
    say(f"[card] wrote {CARD}")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("stage", choices=("labels", "relabel", "meta", "points", "steps", "plan", "build", "finalize",
                                      "card", "all"))
    ap.add_argument("--oct-labels", type=Path, default=OCT_LABELS)
    ap.add_argument("--nov-labels", type=Path, default=NOV_LABELS_DEFAULT)
    ap.add_argument("--revision", default=None, help="Hub commit (default: current main, pinned in plan.json)")
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--limit-units", type=int, default=0, help="smoke test: only this many units")
    ap.add_argument("--units", nargs="*", default=None, help="smoke test: explicit unit ids")
    ap.add_argument("--overrides", type=Path, default=OVERRIDES, help="relabel: local convention decisions csv")
    ap.add_argument("--make-view", action="store_true", help="relabel: build features_labels_v2/ (hard links)")
    ap.add_argument("--force", action="store_true", help="relabel: rewrite an existing labels_trainval.v2.csv")
    ap.add_argument("--include-mixed", action="store_true",
                    help="also read row groups shared with test/sealed units (their rows are never decoded)")
    args = ap.parse_args(argv)
    if args.stage != "relabel":
        FEAT.mkdir(parents=True, exist_ok=True)
    stages = ("labels", "meta", "steps", "plan", "build", "finalize") if args.stage == "all" else (args.stage,)
    for st in stages:
        say(f"=== stage {st} ===")
        globals()[f"stage_{st}"](args)
    return 0


if __name__ == "__main__":
    sys.exit(main())

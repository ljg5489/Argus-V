"""End-to-end demo: raw hook tensors of ONE train unit -> ArgusScorer (streaming and batch) -> score, decision,
argmax observation (+ reasoning text window), with parity checks.

  py -3.11 experiments/risk_loop/argus_loop/infer_demo.py --unit <train unit_id> [--model PREFIX] [--dry-run]
      [--with-text] [--plumbing]

Rules: validation / test / sealed / unknown units are refused BEFORE anything is fetched (split from the v2 label
table + sealed_units.csv). Only that unit's ``rollout/steps/step_*/capture/features.npz`` members of the model's
layers are fetched (HubSelector, read-only, RAM only; rows of other units in a shared row group are never
decoded). Checks: streaming == batch (exact), package raw path vs observation-cache path |diff| <= 1e-3, and the
decision agrees whenever both scores are more than 1e-3 away from the threshold.
``--plumbing``: no trained package needed; a random-weight package is built on the fly (pipeline check only).
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import time
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop.argus_loop import argus_scorer as AS  # noqa: E402
from experiments.risk_loop.argus_loop import obs_cache as OC  # noqa: E402
from experiments.risk_loop.argus_loop import obs_models as OM  # noqa: E402

ART = REPO_ROOT / "artifacts" / "risk-loop" / "argus-v1-loop"
LABELS = ART / "labels" / "labels_trainval.v2.csv"
SEALED = ART / "labels" / "sealed_units.csv"
STEPS = ART / "features_labels_v2" / "steps.csv"
PACKAGE = ART / "phase3" / "package" / "argus_v1_pool"
_STEP = re.compile(r"^rollout/steps/step_(\d+)/capture/features\.npz$")


def unit_split(unit: str, labels=LABELS, sealed=SEALED) -> str:
    if Path(sealed).is_file():
        with open(sealed, newline="", encoding="utf-8") as h:
            for r in csv.DictReader(h):
                if r["unit_id"] == unit:
                    return r.get("split") or "sealed"
    splits = set()
    with open(labels, newline="", encoding="utf-8") as h:
        for r in csv.DictReader(h):
            if r["unit_id"] == unit:
                splits.add(r["split"])
    if not splits:
        return "unknown"
    return splits.pop() if len(splits) == 1 else "mixed"


def require_train(unit: str, **kw) -> None:
    s = unit_split(unit, **kw)
    if s != "train":
        raise PermissionError(f"unit {unit} has split {s!r}: only train units may be scored by the demo")


def unit_steps(unit: str, steps_csv=STEPS) -> list[dict]:
    with open(steps_csv, newline="", encoding="utf-8") as h:
        out = [r for r in csv.DictReader(h) if r["unit_id"] == unit]
    if any(r["split"] != "train" for r in out):
        raise PermissionError("steps of this unit are not all train")
    return sorted(out, key=lambda r: int(r["step_index"]))


def hf_fetch(unit: str, layers, dry_run=False, with_text=False):
    """Yields (step_index, layer, array [n_obs, H]) for one unit; optional token_pieces per step."""
    sys.path.insert(0, str(REPO_ROOT / "scripts"))
    import hf_select
    sel = hf_select.HubSelector(log=lambda m: print(m, flush=True))
    rows = sel.select(units=[unit], table="tensors", path_glob="rollout/steps/step_*/capture/features.npz",
                      layer=list(layers))
    plan = sel.plan(rows)
    print(f"[fetch] {unit}: {plan}", flush=True)
    if dry_run:
        return [], {}
    arrays = []
    for key, arr, meta in sel.fetch_arrays(rows):
        m = _STEP.match(key[1])
        arrays.append((int(m.group(1)), int(hf_select.row_layer(meta)), np.array(arr, dtype=np.float32)))
    texts = {}
    if with_text:
        frows = sel.select(units=[unit], table="files", path_glob="rollout/steps/step_*agent-generation*.json")
        for key, data, _ in sel.fetch_values(frows):
            m = re.match(r"^rollout/steps/step_(\d+)/", key[1])
            try:
                d = json.loads(data)
                texts[int(m.group(1))] = {"pieces": d.get("token_pieces"), "offset": int(d.get("prompt_length") or 0)}
            except (ValueError, AttributeError):
                pass
    return arrays, texts


def plumbing_scorer(cache: OC.ObsCache, layers, seed=0) -> AS.ArgusScorer:
    """Random-weight package with the real basis (pipeline check, candidate=false, not a model)."""
    rng = np.random.default_rng(seed)
    cfg = OM.make_config(layers=layers)
    k, K = cfg["pca_k"], cfg["K"]
    bases = {L: cache.basis(L) for L in layers}
    D = bases[layers[0]].dim
    fm = OM.FittedObsModel(cfg, tuple(layers), {L: np.zeros(D, np.float32) for L in layers},
                           {L: np.linalg.qr(rng.normal(size=(D, k)))[0].astype(np.float32) for L in layers},
                           {L: np.ones(k, np.float32) for L in layers},
                           {"W": rng.normal(size=(1, len(layers), k, K)).astype(np.float32),
                            "head_w": [rng.normal(size=(1, 3 * K * len(layers), 1)).astype(np.float32)],
                            "head_b": [np.zeros((1, 1), np.float32)]}, None, np.linspace(-3, 3, 101), {})
    return AS.ArgusScorer.from_fitted(fm, bases, 0.0, {"plumbing": True})


def run_demo(unit: str, scorer: AS.ArgusScorer, cache: OC.ObsCache, steps: list[dict], arrays, meta_kinds,
             texts=None, tol=1e-3) -> dict:
    """arrays: [(step_index, layer, [n, H])]; meta_kinds: step_index -> (kinds, token_index list)."""
    texts = texts or {}
    by = {}
    for k, L, a in arrays:
        by.setdefault(k, {})[L] = a
    report, worst, flips, near = [], 0.0, 0, 0
    allowed = [int(s["row"]) for s in steps]
    for s in steps:
        k, row = int(s["step_index"]), int(s["row"])
        if k not in by or any(L not in by[k] for L in scorer.layers):
            report.append({"step": k, "error": "tensors missing"})
            continue
        kinds, toks = meta_kinds[k]
        obs = by[k]
        t0 = time.perf_counter()
        st = scorer.start()
        prov = []
        for i, kd in enumerate(kinds):
            u = scorer.update(st, {L: obs[L][i] for L in scorer.layers}, kd, toks[i])
            if not u["skipped"]:
                prov.append(round(u["provisional"], 4))
        tx = texts.get(k) or {}
        stream = scorer.finalize(st, tx.get("pieces"), tx.get("offset", 0))
        lat = (time.perf_counter() - t0) / max(len(kinds), 1) * 1e6
        batch = scorer.score_step(obs, kinds, toks, tx.get("pieces"), tx.get("offset", 0))
        g = cache.gather([row], allowed)
        u = {L: np.asarray(cache.layer(L)[g.obs_ids], np.float32) for L in scorer.layers}
        cs = scorer.score_cache_rows(u, list(g.kind))
        d = abs(cs - batch["score"])
        worst = max(worst, d)
        thr = scorer.threshold
        if abs(cs - thr) > tol and abs(batch["score"] - thr) > tol:
            flips += int((cs >= thr) != (batch["score"] >= thr))
        else:
            near += 1
        report.append({"step": k, "tool_for_display_only": s["tool"], "label_for_display_only": s["label"],
                       "score": batch["score"], "percentile": batch["percentile"], "decision": batch["decision"],
                       "argmax_obs": batch.get("argmax_obs"), "provisional_scores": prov,
                       "stream_equals_batch": stream["score"] == batch["score"] and
                       stream.get("argmax_obs") == batch.get("argmax_obs"),
                       "cache_score": cs, "abs_diff_vs_cache": d, "latency_us_per_obs": lat})
    ok = all(r.get("stream_equals_batch", False) for r in report if "error" not in r)
    return {"unit": unit, "steps": report, "stream_equals_batch_all": ok, "max_abs_diff_vs_cache": worst,
            "parity_ok": worst <= tol and flips == 0, "decision_flips_outside_tol": flips, "near_threshold": near}


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--unit", required=True)
    ap.add_argument("--model", default=str(PACKAGE))
    ap.add_argument("--cache", default=str(OC.CACHE_DIR))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--with-text", action="store_true")
    ap.add_argument("--plumbing", action="store_true")
    a = ap.parse_args(argv)
    require_train(a.unit)                      # refuses validation / test / sealed / unknown before any fetch
    steps = unit_steps(a.unit)
    cache = OC.ObsCache(a.cache)
    scorer = plumbing_scorer(cache, [20]) if a.plumbing else AS.ArgusScorer.load(a.model)
    if not a.plumbing:
        units = Path(str(a.model) + ".units.json")
        if units.is_file():
            u = json.loads(units.read_text(encoding="utf-8"))
            print(f"[demo] unit in the package's training units: {a.unit in set(u['train_units'])}")
    arrays, texts = hf_fetch(a.unit, scorer.layers, a.dry_run, a.with_text)
    if a.dry_run:
        return
    meta_kinds = {}
    for s in steps:
        kinds = s["obs_kinds"].split("|")
        g = cache.gather([int(s["row"])], [int(s["row"])], grid32=False)
        toks = g.token_index.tolist() if len(g.token_index) == len(kinds) else [None] * len(kinds)
        meta_kinds[int(s["step_index"])] = (kinds, toks)
    res = run_demo(a.unit, scorer, cache, steps, arrays, meta_kinds, texts)
    print(json.dumps(res, indent=1, default=float))


if __name__ == "__main__":
    main()

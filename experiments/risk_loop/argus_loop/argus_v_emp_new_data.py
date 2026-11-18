"""Argus-V-emp on the 432 runs added to HF after revision 62106dbf: features, real-time-style inference, comparison.

Plan fixed and committed before any score: reports/risk-loop/argus-v-emp/new-data-1118/README.md (commit 63d5a54).
User: "이번에 뽑힌 시나리오에 대해 Argus-V-emp로 추론 진행해봐 ... 실시간 느낌이니까 라벨링도 어차피 필요없고".

No model is fitted. Features are pooled with the code of the existing caches (build_features.thin_to_grid32 and
pool_step) from layers 16 and 23 only; raw hidden states are never written to disk. HF is only read.

Stages (each resumable, ``all`` runs them in order):
  units    the new units: in the manifest of revision NEW_REV, not in the one of 62106dbf (sealed units excluded)
  meta     rollout.json of each new unit: observation kinds, tool, environment verdict, fields of the visibility rule
  steps    one row per step that has observations                                         -> features/steps.csv
  plan     the tensor row groups that hold layers 16 and 23 of those steps                -> plan.json
  build    fetch, thin to the 32-token grid, pool                                         -> features/L{16,23}_{pool}.npy
  score    the saved Argus-V-emp model files score every step                             -> scores.npz, predictions.csv

Usage: PYTHONUTF8=1 py -3.11 -u experiments/risk_loop/argus_loop/argus_v_emp_new_data.py all
Output: artifacts/risk-loop/argus-v-emp-new-1118/ (not in git)
"""
from __future__ import annotations

import csv
import json
import os
import re
import sys
import time
from collections import Counter
from pathlib import Path

for _name in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ.setdefault(_name, "2")

import numpy as np  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from experiments.risk_loop.argus_loop import argus_v_em300_test_eval as TE  # noqa: E402  (visibility rule)
from experiments.risk_loop.argus_loop import build_features as B  # noqa: E402
import hf_select  # noqa: E402  (build_features put scripts/ on sys.path)

TB = TE.TB
NEW_REV = "494aec37482e3e179530471eb8d511bd32cb88a5"
OLD_REV = "62106dbf"
ART = ROOT / "artifacts/risk-loop/argus-v-emp-new-1118"
FEAT = ART / "features"
LOG = ART / "run.log"
LAYERS = (16, 23)
POOLS = B.POOLS
REPORT_TOOLS = frozenset(B.REPORT_TOOLS)
SEALED = re.compile(r"^AV-S(6[1-9]|7\d|80)-")
STEP_COLS = ["row", "unit_id", "group", "scenario_id", "condition", "seed", "step_index", "kind", "tool", "report_tool",
             "policy_label", "decision", "oracle_reason", "visible_category", "visible", "observe_every", "n_obs_raw", "n_obs_32",
             "pre_is_pre_action"]


def say(*parts) -> None:
    line = time.strftime("%Y-%m-%d %H:%M:%S ") + " ".join(str(p) for p in parts)
    print(line, flush=True)
    ART.mkdir(parents=True, exist_ok=True)
    with open(LOG, "a", encoding="utf-8") as fh:
        fh.write(line + "\n")


B.say = say                       # retry and index messages of build_features / hf_select go to this run's log
TB.say = say                      # (importing the old test builder had pointed them at its own log)


def group_of(scenario_id: str) -> str:
    return "AVv2" if scenario_id.startswith("AVv2") else scenario_id.split("-")[0]


def load_jsonl(path: Path) -> dict:
    out = {}
    if path.is_file():
        for line in open(path, encoding="utf-8"):
            d = json.loads(line)
            out[d["unit_id"]] = d
    return out


# ---------------------------------------------------------------------- units
def stage_units() -> None:
    from huggingface_hub import HfApi, hf_hub_download

    api = HfApi()
    old_full = next(c.commit_id for c in api.list_repo_commits(hf_select.DEFAULT_REPO, repo_type="dataset") if c.commit_id.startswith(OLD_REV))
    man = {rev: json.loads(Path(hf_hub_download(hf_select.DEFAULT_REPO, "manifest/units.json", repo_type="dataset", revision=rev)).read_text(encoding="utf-8"))
           for rev in (old_full, NEW_REV)}
    old_ids = {u for units in man[old_full]["units"].values() for u in units}
    new = {u: src for src, units in man[NEW_REV]["units"].items() for u in units if u not in old_ids}
    sealed = sorted(u for u in new if SEALED.match(u))
    units = sorted(u for u in new if not SEALED.match(u))
    ART.mkdir(parents=True, exist_ok=True)
    (ART / "units.json").write_text(json.dumps({"revision": NEW_REV, "compared_with": old_full, "units": units, "sources": {u: new[u] for u in units},
                                                "sealed_excluded": sealed}, indent=1), encoding="utf-8")
    say(f"[units] {len(units)} new units ({dict(Counter(group_of(u) for u in units))}), sealed excluded {len(sealed)}")


# ---------------------------------------------------------------------- meta
def stage_meta() -> None:
    units = json.loads((ART / "units.json").read_text(encoding="utf-8"))["units"]
    path, rule_path = ART / "meta/rollouts.jsonl", ART / "meta/rule_steps.jsonl"
    path.parent.mkdir(parents=True, exist_ok=True)
    done = set(load_jsonl(path))
    todo = [u for u in units if u not in done]
    hub = B.Hub(NEW_REV)
    say(f"[meta] {len(done)} done, {len(todo)} to fetch")
    with open(path, "a", encoding="utf-8") as out, open(rule_path, "a", encoding="utf-8") as rout:
        for i in range(0, len(todo), 50):
            rows = hub.sel.select(units=todo[i:i + 50], table="files", path_glob="rollout/rollout.json")
            for key, data, _ in hub.sel.fetch_values(rows):
                d = json.loads(data)
                raw = d.get("steps") or []
                steps = [{"step_index": s.get("step_index", k), "action_id": s.get("action_id"), "kind": s.get("kind"), "tool": B.tool_of(s),
                          "action_start": s.get("action_start"), "obs_kinds": [o["kind"] for o in s.get("observations") or []],
                          "policy_label": s.get("policy_label"), "decision": s.get("decision"), "oracle_reason": s.get("oracle_reason")}
                         for k, s in enumerate(raw)]
                out.write(json.dumps({"unit_id": key[0], "scenario_id": d.get("scenario_id"), "family": d.get("family"),
                                      "condition": d.get("condition"), "seed": d.get("seed"), "trajectory_id": d.get("trajectory_id"),
                                      "observe_every": d.get("observe_every"), "steps": steps}, ensure_ascii=False) + "\n")
                rout.write(json.dumps({"unit_id": key[0], "steps": [{"step": TB.rule_step(s, k)} for k, s in enumerate(raw)]}, ensure_ascii=False) + "\n")
            out.flush()
            rout.flush()
            say(f"[meta] {min(i + 50, len(todo))}/{len(todo)} units")


# ---------------------------------------------------------------------- steps
def stage_steps() -> None:
    meta = load_jsonl(ART / "meta/rollouts.jsonl")
    rules = load_jsonl(ART / "meta/rule_steps.jsonl")
    units = json.loads((ART / "units.json").read_text(encoding="utf-8"))["units"]
    assert set(meta) == set(units), (len(meta), len(units))
    # the verdicts read from the step records in the HF check must agree with rollout.json
    check = {(r["unit_id"], int(r["step_index"])): r["policy_label"] for r in B.read_csv(ROOT / "artifacts/risk-loop/hf-new-1118/steps.csv")}
    rows, problems, grid = [], Counter(), []
    for u in units:
        m = meta[u]
        every = B.unit_observe_every(m)
        rule_steps = {int(x["step"]["step_index"]): x["step"] for x in rules[u]["steps"]}
        for s in m["steps"]:
            k = int(s["step_index"])
            if not s["obs_kinds"]:
                problems["no_observations"] += 1
                continue
            _, kinds32, _ = B.thin_to_grid32(None, s["obs_kinds"], every)
            pl = s["policy_label"]
            lab = "" if pl is None else int(pl)
            if (u, k) in check and str(check[(u, k)]) != str(lab):
                problems["verdict_differs_from_step_record"] += 1
            cat, vis = "", ""
            if lab == 1:
                r = TE.rule_row({"unit_id": u, "step_index": k}, rule_steps)
                cat, v = TE.classify(r)
                vis = int(v is True)
            tool = s["tool"] or s["kind"] or ""
            rows.append({"row": len(rows), "unit_id": u, "group": group_of(m["scenario_id"]), "scenario_id": m["scenario_id"],
                         "condition": m["condition"], "seed": m["seed"], "step_index": k, "kind": s["kind"], "tool": tool,
                         "report_tool": int(tool in REPORT_TOOLS), "policy_label": lab, "decision": s["decision"], "oracle_reason": s["oracle_reason"],
                         "visible_category": cat, "visible": vis, "observe_every": every, "n_obs_raw": len(s["obs_kinds"]), "n_obs_32": len(kinds32),
                         "pre_is_pre_action": int("pre_action" in kinds32)})
            grid.append(s["obs_kinds"])
    FEAT.mkdir(parents=True, exist_ok=True)
    B.write_csv(FEAT / "steps.csv", rows, STEP_COLS)
    (FEAT / "obs_kinds.json").write_text(json.dumps(grid), encoding="utf-8")
    say(f"[steps] {len(rows)} rows, problems {dict(problems)}, observe_every {dict(Counter(r['observe_every'] for r in rows))}, "
        f"verdicts {dict(Counter(str(r['policy_label']) for r in rows))}, visible violations {sum(1 for r in rows if r['visible'] == 1)}")


# ---------------------------------------------------------------------- plan
def stage_plan() -> None:
    hub = B.Hub(NEW_REV)
    steps = B.read_csv(FEAT / "steps.csv")
    want = {(s["unit_id"], int(s["step_index"])): int(s["row"]) for s in steps}
    units = sorted({s["unit_id"] for s in steps})
    unit_set = set(units)
    shards = hub.sel.shards_for(units, "tensors")
    say(f"[plan] {len(units)} units over {len(shards)} tensor shards")
    for sh in shards:
        hub.sel.shard_index(sh)
    groups, chunked = {}, []
    for sh in shards:
        for r in hub.sel.shard_index(sh):
            m = B.STEP_PATH.match(r["path"])
            L = hf_select.row_layer(r)
            if not (r["unit_id"] in unit_set and m is not None and L in LAYERS and (r["unit_id"], int(m.group(1))) in want):
                continue
            if (r.get("chunk_count") or 1) > 1:
                chunked.append(r)
                continue
            g = groups.setdefault((sh, r["_rg"]), {"shard": sh, "rg": r["_rg"], "bytes": r["_rg_payload_bytes"], "items": []})
            g["items"].append({"row": r["_row"], "srow": want[(r["unit_id"], int(m.group(1)))], "layer": L, "unit_id": r["unit_id"],
                               "dtype": r["dtype"], "shape": r["shape"], "sha": r["chunk_sha256"]})
    if chunked:
        raise SystemExit(f"[plan] {len(chunked)} wanted values are multi-chunk; not handled: {chunked[:2]}")
    work = sorted(groups.values(), key=lambda g: (g["shard"], g["rg"]))
    found = Counter((it["srow"], it["layer"]) for g in work for it in g["items"])
    missing = [(s, L) for s in want.values() for L in LAYERS if (s, L) not in found]
    plan = {"revision": hub.revision, "layers": LAYERS, "steps": len(steps), "units": len(units), "shards": len(shards), "row_groups": len(work),
            "transfer_bytes": int(sum(g["bytes"] for g in work)), "largest_row_group_bytes": int(max(g["bytes"] for g in work)),
            "values": int(sum(len(g["items"]) for g in work)), "missing_values": len(missing), "missing_examples": missing[:10], "work": work}
    (ART / "plan.json").write_text(json.dumps(plan), encoding="utf-8")
    say("[plan]", json.dumps({k: v for k, v in plan.items() if k != "work"}))


# ---------------------------------------------------------------------- build
def _memmaps(n: int) -> dict:
    out = {}
    for L in LAYERS:
        for p in POOLS:
            path = FEAT / f"L{L:02d}_{p}.npy"
            if path.is_file():
                out[(L, p)] = np.lib.format.open_memmap(path, mode="r+")
                assert out[(L, p)].shape == (n, B.HIDDEN), path
            else:
                out[(L, p)] = np.lib.format.open_memmap(path, mode="w+", dtype=np.float16, shape=(n, B.HIDDEN))
                out[(L, p)][:] = np.nan
    return out


def stage_build() -> None:
    plan = json.loads((ART / "plan.json").read_text(encoding="utf-8"))
    assert plan["missing_values"] == 0, plan["missing_examples"]
    steps = B.read_csv(FEAT / "steps.csv")
    kinds = json.loads((FEAT / "obs_kinds.json").read_text(encoding="utf-8"))
    n = len(steps)
    kinds_of = {int(s["row"]): (kinds[int(s["row"])], int(s["observe_every"])) for s in steps}
    mm = _memmaps(n)
    done_path, flags_path = FEAT / "done.txt", FEAT / "flags.jsonl"
    done = set(done_path.read_text().split()) if done_path.is_file() else set()
    gid = lambda g: f"{g['shard']}#{g['rg']}"                   # noqa: E731
    todo = [g for g in plan["work"] if gid(g) not in done]
    total = sum(g["bytes"] for g in todo)
    say(f"[build] {len(done)} groups done, {len(todo)} to do, {total / 2**30:.2f} GB to transfer (one row group at a time)")
    hub = B.Hub(plan["revision"])
    t0, moved, stats = time.time(), 0, Counter()
    with open(done_path, "a") as dfh, open(flags_path, "a", encoding="utf-8") as ffh:
        for i, g in enumerate(todo, 1):
            g, res = B.process_group(hub, g, kinds_of)
            for srow, L, pooled, flags in res:
                for p in POOLS:
                    v = pooled[p]
                    mm[(L, p)][srow] = v.astype(np.float16)
                    if p != "rend" or flags["has_rend"]:
                        if not np.isfinite(v).all() or np.abs(v).max() > 65504:
                            stats[f"nonfinite_or_overflow_L{L}_{p}"] += 1
                ffh.write(json.dumps({"row": srow, "layer": L, **flags}) + "\n")
            for m in mm.values():
                m.flush()
            ffh.flush()
            dfh.write(gid(g) + "\n")
            dfh.flush()
            os.fsync(dfh.fileno())
            moved += g["bytes"]
            el = time.time() - t0
            rate = moved / el if el else 0
            if i % 10 == 0 or i == len(todo):
                say(f"[build] groups {i}/{len(todo)} | {moved / 2**30:.2f}/{total / 2**30:.2f} GB | {rate / 2**20:.1f} MB/s | "
                    f"ETA {((total - moved) / rate / 60) if rate else float('nan'):.1f} min" + (f" | {dict(stats)}" if stats else ""))
    say(f"[build] finished in {time.time() - t0:.0f}s, {moved / 2**30:.2f} GB, stats {dict(stats)}")


# ---------------------------------------------------------------------- score
def stage_score() -> None:
    from experiments.risk_loop.argus_loop import argus_v_emp_model as EMPM

    steps = B.read_csv(FEAT / "steps.csv")
    x23 = np.load(FEAT / "L23_max.npy").astype(np.float32)
    x16 = np.load(FEAT / "L16_pre.npy").astype(np.float32)
    ok = np.isfinite(x23).all(1) & np.isfinite(x16).all(1)
    assert ok.all(), f"{int((~ok).sum())} steps without complete features"
    t0 = time.time()
    model = EMPM.EmpModel()
    load_s = time.time() - t0
    em_raw = model.em_scores(x23, x16)
    parts = {"em": np.mean([EMPM.share_below(model.ref[n], s) for n, s in em_raw.items()], axis=0)}
    for sid, pm in model.p.items():
        parts[sid] = EMPM.share_below(model.ref[sid], pm.score(x23, x16))
    score = (parts["em"] + sum(parts[s] for s in model.p)) / (1 + len(model.p))
    again = model.score(x23, x16)
    assert np.abs(again - score).max() < 1e-12
    secs = time.time() - t0 - load_s
    np.savez_compressed(ART / "scores.npz", score=score, em=parts["em"], P3=parts["P3"], P5=parts["P5"],
                        em_raw=np.stack([em_raw[n] for n in model.manifest["argus_v_em_models"]]))
    cut5, cut1 = model.cut["5%"], model.cut["1%"]
    with open(ART / "predictions.csv", "w", newline="", encoding="utf-8") as h:
        w = csv.writer(h)
        w.writerow(["row", "unit_id", "group", "scenario_id", "condition", "seed", "step_index", "tool", "score", "alarm_5pct", "alarm_1pct",
                    "policy_label", "visible"])
        for s, v in zip(steps, score):
            w.writerow([s["row"], s["unit_id"], s["group"], s["scenario_id"], s["condition"], s["seed"], s["step_index"], s["tool"],
                        f"{v:.6f}", int(v > cut5), int(v > cut1), s["policy_label"], s["visible"]])
    say(f"[score] {len(steps)} steps scored in {secs:.1f}s (model loaded in {load_s:.1f}s) | alarms at {cut5:.3f}: {int((score > cut5).sum())}, "
        f"at {cut1:.3f}: {int((score > cut1).sum())} | score min {score.min():.3f} median {np.median(score):.3f} max {score.max():.3f}")


STAGES = {"units": stage_units, "meta": stage_meta, "steps": stage_steps, "plan": stage_plan, "build": stage_build, "score": stage_score}

if __name__ == "__main__":
    want = sys.argv[1:] or ["all"]
    for st in (list(STAGES) if want == ["all"] else want):
        say(f"== {st}")
        STAGES[st]()

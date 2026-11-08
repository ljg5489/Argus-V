"""Iteration 5 model tries T5-1..T5-4 (train only). Plan: reports/risk-loop/argus-v1/loop/iter-05/plan.md.

Per try:
 1. frozen v4 ``evaluate.evaluate(make_fit_predict, grid)`` (nested CV picks representation x hyperparameters
    by the harness' inner headline; bootstrap CI; shuffles (a)(b) 20 each; baselines);
 2. inner within-trajectory AUROC per grid entry (report-only) -> which entry it would pick per outer fold,
    and the outer OOF of that alternative selection (report-only, no shuffles);
 3. score-saving replicas of shuffle (b) (checked against the harness value) and a diagnostic shuffle within
    source x trajectory (20 each) for the within-trajectory metric.

Usage: py -3.11 experiments/risk_loop/argus_loop/iter05_scan.py --only T5-1
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from collections import Counter
from pathlib import Path

for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ.setdefault(_v, "2")

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402
from experiments.risk_loop.argus_loop import iter01_common as C1  # noqa: E402
from experiments.risk_loop.argus_loop import iter02_common as C2  # noqa: E402
from experiments.risk_loop.argus_loop import iter04_common as C4  # noqa: E402
from experiments.risk_loop.argus_loop import iter05_common as C5  # noqa: E402
from experiments.risk_loop.argus_loop import iter05_models as M5  # noqa: E402

N_SHUF = 20


def within_traj_report(oofs, rows, with_ci=True):
    g = E.headline_groups(rows)
    cells = C4.eligible_cells(rows)
    in_cells = np.isin(g, cells)
    trj = rows.trajectory_id.astype(str)
    tt = np.asarray([f"{a}|{b}" for a, b in zip(trj, rows.tool.astype(str))], dtype=object)
    out = {}
    for scope, keep, key in (("B_all_headline", None, trj), ("A_cells", in_cells, trj),
                             ("C_same_tool", None, tt)):
        w = C4.within_traj_multi(list(oofs), rows, keep, key)
        if with_ci:
            w["ci95"] = C4.within_traj_bootstrap(list(oofs), rows, keep, traj=key)
        out[scope] = w
    return out


def shuffle_traj_summary(oofs, rows):
    g = E.headline_groups(rows)
    cells = C4.eligible_cells(rows)
    in_cells = np.isin(g, cells)
    trj = rows.trajectory_id.astype(str)
    tt = np.asarray([f"{a}|{b}" for a, b in zip(trj, rows.tool.astype(str))], dtype=object)
    wt = [E.within_tool_auroc(o, rows.y, g)["value"] for o in oofs]
    rec = {"within_tool_mean": float(np.mean(wt)), "within_tool_sd": float(np.std(wt, ddof=1)),
           "within_tool": wt}
    for scope, keep, key in (("B_all_headline", None, trj), ("A_cells", in_cells, trj), ("C_same_tool", None, tt)):
        v = [C4.within_traj_auroc(o, rows.y, key, keep)["value"] for o in oofs]
        rec[scope] = {"mean": float(np.mean(v)), "sd": float(np.std(v, ddof=1)),
                      "se": float(np.std(v, ddof=1) / np.sqrt(len(v)))}
    return rec


def run(tid: str):
    t0 = time.time()
    data, rows, rinfo = C1.headline_data()
    ctx = {"trajectory": rows.trajectory_id.astype(str),
           "step_index": np.nan_to_num(np.asarray(rows.step_index, dtype=np.float64), nan=0.0)}
    store = C5.EmbStore(on_miss=C5.real_on_miss(data, rows))
    sets = C5.training_sets(rows)
    inner_sets = [s for s in sets if s["kind"] == "inner"]
    rec = M5.InnerRecorder(rows.y, rows.trajectory_id, {C5.pos_hash(s["pos"]) for s in inner_sets})
    make = M5.make_family(M5.KIND[tid], store, ctx, rec)
    grid = M5.grid_for(tid)
    r = E.evaluate(make_fit_predict=make, grid=grid, X_or_rowids=None, rows=rows, name=tid, include_oof=True)
    t_eval = time.time() - t0
    oof = r["cv"].pop("oof")
    r["cv"].pop("fold_id", None)
    r["cv"].pop("folds", None)
    O = np.asarray([oof[k] for k in sorted(oof)], dtype=np.float64)
    np.save(C5.ART / f"oof_{tid}.npy", O)
    sel = r["cv"]["selection"]
    chosen = {s: list(v) for s, v in sel["chosen"].items()}
    inner_scores = sel.pop("inner_scores")

    # ---- inner within-trajectory selection (report-only) and its outer OOF
    alt_choice, alt_oof, agree = {}, [], 0
    inner_wt_best_vals, inner_head_at_alt = [], []
    yv = rows.y
    for seed in E.DEFAULT_SEEDS:
        folds = E.make_folds(rows, 5, seed)
        o = np.full(len(rows), np.nan)
        picks = []
        for i, (a, b) in enumerate(folds):
            hs = [C5.pos_hash(s["pos"]) for s in inner_sets if s["seed"] == seed and s["outer"] == i]
            vals = []
            for e in grid:
                num = den = 0.0
                for h in hs:
                    acc = rec.acc.get((h, e["gi"]))
                    if acc:
                        num += acc[0]
                        den += acc[1]
                vals.append(num / den if den else -np.inf)
            best = int(np.argmax(vals))
            picks.append(best)
            inner_wt_best_vals.append(float(vals[best]))
            inner_head_at_alt.append(float(inner_scores[str(seed)][i][best]))
            agree += int(best == chosen[str(seed)][i])
            o[b] = E._fit_fold(make(grid[best]), np.arange(len(rows)), a, b, yv[a])
        alt_choice[str(seed)] = picks
        alt_oof.append(o)
    alt_oof = np.asarray(alt_oof)
    np.save(C5.ART / f"oof_{tid}.altsel.npy", alt_oof)
    g_cells = E.headline_groups(rows)
    alt = {"chosen": alt_choice, "agree_with_harness_choice": agree, "n_outer_folds": 15,
           "within_tool_v4": E._mean([E.within_tool_auroc(x, yv, g_cells)["value"] for x in alt_oof]),
           "within_tool_per_seed": [E.within_tool_auroc(x, yv, g_cells)["value"] for x in alt_oof],
           "within_traj": within_traj_report(alt_oof, rows, with_ci=True),
           "inner_wt_value_of_pick_mean": float(np.mean(inner_wt_best_vals)),
           "inner_headline_value_of_pick_mean": float(np.mean(inner_head_at_alt))}
    # inner within-trajectory value of the harness' own pick
    harness_inner_wt = []
    for seed in E.DEFAULT_SEEDS:
        for i in range(5):
            hs = [C5.pos_hash(s["pos"]) for s in inner_sets if s["seed"] == seed and s["outer"] == i]
            gi = chosen[str(seed)][i]
            num = sum(rec.acc.get((h, gi), [0, 0])[0] for h in hs)
            den = sum(rec.acc.get((h, gi), [0, 0])[1] for h in hs)
            harness_inner_wt.append(num / den if den else None)

    # ---- shuffle replicas (saved scores) with the harness' modal grid entry
    modal = sel["shuffle_uses_grid_index"]
    fpm = make(grid[modal])
    t1 = time.time()
    sb = C4.shuffle_oofs(fpm, rows, N_SHUF, ("source", "family"))
    st = C4.shuffle_oofs(fpm, rows, N_SHUF, ("source", "trajectory_id"))
    np.save(C5.ART / f"shuf_b_{tid}.npy", np.asarray(sb, dtype=np.float32))
    np.save(C5.ART / f"shuf_traj_{tid}.npy", np.asarray(st, dtype=np.float32))
    sb_rep = shuffle_traj_summary(sb, rows)
    harness_b = r["shuffle_source_family"]["within_tool_mean"]
    sb_rep["matches_harness_b_mean"] = bool(abs(sb_rep["within_tool_mean"] - harness_b) < 1e-9)

    def label(gi):
        e = grid[gi]
        return {k: (list(v) if isinstance(v, tuple) else v) for k, v in e.items()}

    picks_all = [c for v in chosen.values() for c in v]
    out = {"id": tid, "kind": M5.KIND[tid], "grid_size": len(grid), "evaluate_sha256": r["evaluate_sha256"],
           "rows_info": rinfo, "data_hash": C2.data_hash(rows), "seconds_evaluate": t_eval,
           "seconds_total": time.time() - t0, "seconds_shuffle_replicas": time.time() - t1,
           "embedding_misses": store.misses,
           "harness": r,
           "selection_summary": {
               "chosen_entries": {s: [label(c) for c in v] for s, v in chosen.items()},
               "rep_counts": dict(Counter(str(grid[c]["rep"]) for c in picks_all).most_common()),
               "param_counts": {p: dict(Counter(str(grid[c].get(p)) for c in picks_all))
                                for p in ("k", "C", "lam", "alpha") if p in grid[0]},
               "modal_entry": label(modal),
               "inner_headline_of_pick_mean": float(np.mean([inner_scores[s][i][c] for s, v in chosen.items()
                                                             for i, c in enumerate(v)])),
               "inner_within_traj_of_pick": harness_inner_wt},
           "within_traj": within_traj_report(O, rows, with_ci=True),
           "alt_selection_by_inner_within_traj": alt | {"chosen_entries": {s: [label(c) for c in v]
                                                                         for s, v in alt_choice.items()}},
           "shuffle_b_replica": sb_rep,
           "shuffle_source_trajectory_diag": shuffle_traj_summary(st, rows)}
    (C5.ART / f"{tid}.json").write_text(json.dumps(E.to_jsonable(out), indent=1), encoding="utf-8")
    wt = r["metrics"]["within_tool"]
    print(tid, "within", round(wt["value"], 4), [round(x, 3) for x in wt["per_seed"]],
          "shufB", round(harness_b, 4), "shufA", round(r["shuffle_source"]["within_tool_mean"], 4),
          "WT(B)", round(out["within_traj"]["B_all_headline"]["value"], 4),
          "shufB_WT", round(sb_rep["B_all_headline"]["mean"], 4),
          "alt_within", round(alt["within_tool_v4"], 4), "alt_WT", round(alt["within_traj"]["B_all_headline"]["value"], 4),
          "misses", store.misses, "sec", round(time.time() - t0), flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", required=True)
    a = ap.parse_args()
    C5.ART.mkdir(parents=True, exist_ok=True)
    print("evaluate_sha256", E.evaluate_sha256(), flush=True)
    for t in a.only.split(","):
        run(t)
    print("DONE", flush=True)


if __name__ == "__main__":
    main()

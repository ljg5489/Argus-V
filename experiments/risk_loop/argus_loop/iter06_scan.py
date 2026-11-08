"""Iteration 6 model tries T6-1 / T6-2 (train only). Plan: reports/risk-loop/argus-v1/loop/iter-06/plan.md.

Per try: frozen v4 ``evaluate.evaluate(make_fit_predict, grid)`` (nested CV, bootstrap CI, shuffles (a)(b) 20
each, baselines) + report-only within-trajectory metrics (B)/(A)/(C) of the OOF and of a score-saving shuffle
(b) replica (checked against the harness value). ``run_try`` is reused by iteration 7.

Usage: py -3.11 experiments/risk_loop/argus_loop/iter06_scan.py --only T6-1
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
from experiments.risk_loop.argus_loop import iter05_scan as S5  # noqa: E402
from experiments.risk_loop.argus_loop import iter06_models as M6  # noqa: E402

ART = REPO_ROOT / "artifacts" / "risk-loop" / "argus-v1-loop" / "iter06"
N_SHUF = 20


def model_ctx(rows) -> dict:
    """Training-only signals (read at pos_train only) for the iteration-6/7 models."""
    return {"trajectory": rows.trajectory_id.astype(str), "tool": rows.tool.astype(str),
            "source": rows.source.astype(str),
            "train_group": np.asarray([f"{t}|{s}" for t, s in zip(rows.tool.astype(str), rows.source.astype(str))],
                                      dtype=object)}


def run_try(tid: str, make, grid: list, rows, rinfo, art: Path, extra: dict | None = None) -> dict:
    t0 = time.time()
    art.mkdir(parents=True, exist_ok=True)
    r = E.evaluate(make_fit_predict=make, grid=grid, X_or_rowids=None, rows=rows, name=tid, include_oof=True)
    t_eval = time.time() - t0
    oof = r["cv"].pop("oof")
    r["cv"].pop("fold_id", None)
    r["cv"].pop("folds", None)
    O = np.asarray([oof[k] for k in sorted(oof)], dtype=np.float64)
    np.save(art / f"oof_{tid}.npy", O)
    sel = r["cv"]["selection"]
    inner_scores = sel.pop("inner_scores", None)
    chosen = {s: list(v) for s, v in sel["chosen"].items()}
    modal = sel["shuffle_uses_grid_index"]
    t1 = time.time()
    sb = C4.shuffle_oofs(make(grid[modal]), rows, N_SHUF, ("source", "family"))
    np.save(art / f"shuf_b_{tid}.npy", np.asarray(sb, dtype=np.float32))
    sb_rep = S5.shuffle_traj_summary(sb, rows)
    harness_b = r["shuffle_source_family"]["within_tool_mean"]
    sb_rep["matches_harness_b_mean"] = bool(abs(sb_rep["within_tool_mean"] - harness_b) < 1e-9)
    picks = [c for v in chosen.values() for c in v]
    inner_pick = None
    if inner_scores is not None:
        inner_pick = float(np.mean([inner_scores[s][i][c] for s, v in chosen.items() for i, c in enumerate(v)]))
    out = {"id": tid, "grid": grid, "grid_size": len(grid), "evaluate_sha256": r["evaluate_sha256"],
           "rows_info": rinfo, "data_hash": C2.data_hash(rows), "seconds_evaluate": t_eval,
           "seconds_shuffle_replica": time.time() - t1, "seconds_total": time.time() - t0,
           "harness": r,
           "selection_summary": {"chosen": chosen, "counts": dict(Counter(str(grid[c]) for c in picks)),
                                 "modal_entry": grid[modal], "inner_headline_of_pick_mean": inner_pick},
           "within_traj": S5.within_traj_report(O, rows, with_ci=True),
           "shuffle_b_replica": sb_rep}
    if extra:
        out.update(extra)
    (art / f"{tid}.json").write_text(json.dumps(E.to_jsonable(out), indent=1), encoding="utf-8")
    wt = r["metrics"]["within_tool"]
    print(tid, "within", round(wt["value"], 4), [round(x, 3) for x in wt["per_seed"]],
          "shufB", round(harness_b, 4), "shufA", round(r["shuffle_source"]["within_tool_mean"], 4),
          "B", round(out["within_traj"]["B_all_headline"]["value"], 4),
          "C", round(out["within_traj"]["C_same_tool"]["value"], 4),
          "shufB_C", round(sb_rep["C_same_tool"]["mean"], 4), "match", sb_rep["matches_harness_b_mean"],
          "sec", round(time.time() - t0), flush=True)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", required=True)
    a = ap.parse_args()
    print("evaluate_sha256", E.evaluate_sha256(), flush=True)
    data, rows, rinfo = C1.headline_data()
    store = C5.EmbStore(on_miss=C5.real_on_miss(data, rows))
    ctx = model_ctx(rows)
    for t in a.only.split(","):
        if t == "T6-1":
            run_try(t, M6.make_t61(store, ctx), M6.GRID_T61, rows, rinfo, ART,
                    {"note": "same-trajectory AND same-tool pairs, layer 23 max (fixed)"})
        elif t == "T6-2":
            run_try(t, M6.make_t62(store, ctx), M6.GRID_T62, rows, rinfo, ART,
                    {"note": "fixed equal-weight training-percentile ensemble", "components": list(M6.ENSEMBLE)})
        else:
            raise ValueError(t)
        print("embedding_misses", store.misses, flush=True)
    print("DONE", flush=True)


if __name__ == "__main__":
    main()

"""Iteration 4 model try T4-1 (same-rollout pair training), train only. Plan: reports/.../iter-04/plan.md.

Each variant is evaluated with the frozen v4 ``evaluate.evaluate()`` (nested CV, bootstrap CI, shuffles
(a)(b) 20 each, baselines). OOF scores are saved (seed order 0,1,2) for the D4-3 within-trajectory preview.

Usage: py -3.11 experiments/risk_loop/argus_loop/iter04_scan.py [--only T4-1a]
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
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
from experiments.risk_loop.argus_loop import iter04_models  # noqa: E402,F401  (registers same_traj_pairwise)
from experiments.risk_loop.argus_loop import models as M  # noqa: E402

ART = REPO_ROOT / "artifacts" / "risk-loop" / "argus-v1-loop" / "iter04"
GRID = [{"k": k, "C": C} for k in (10, 32, 128) for C in (0.001, 0.01, 0.1)]
SPECS = [
    {"id": "T4-1a", "rep": "L23:max", "model": "same_traj_pairwise", "fixed": {"kmax": 128},
     "note": "same-trajectory (violation, normal) pairs, layer 23 max"},
    {"id": "T4-1b", "rep": "L16:pre", "model": "same_traj_pairwise", "fixed": {"kmax": 128},
     "note": "same-trajectory (violation, normal) pairs, layer 16 pre-action"},
]


def run(spec):
    data, rows, rinfo = C1.headline_data()
    X, _ = C2.representation(data, rows, spec["rep"])
    ctx = {"trajectory": rows.trajectory_id.astype(str),
           "log_prefix_length": np.log(np.clip(rows.prefix_length, 1.0, None))}
    make = M.grid_maker(spec["model"], X, ctx, spec["fixed"], M.LRU(8))
    t0 = time.time()
    r = E.evaluate(make_fit_predict=make, grid=GRID, X_or_rowids=None, rows=rows, name=spec["id"],
                   include_oof=True)
    oof = r["cv"].pop("oof")
    np.save(ART / f"oof_{spec['id']}.full.npy", np.asarray([oof[k] for k in sorted(oof)], dtype=np.float64))
    r["cv"].pop("fold_id", None)
    r["cv"].pop("folds", None)
    r.update({"spec": spec, "grid": GRID, "rows_info": rinfo, "data_hash": C2.data_hash(rows),
              "seconds": time.time() - t0})
    (ART / f"{spec['id']}.full.json").write_text(json.dumps(E.to_jsonable(r), indent=1), encoding="utf-8")
    wt = r["metrics"]["within_tool"]
    print(spec["id"], "within", round(wt["value"], 4), wt["per_seed"], "shufB",
          round(r["shuffle_source_family"]["within_tool_mean"], 4), "shufA",
          round(r["shuffle_source"]["within_tool_mean"], 4), "sec", round(time.time() - t0), flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default=None)
    a = ap.parse_args()
    ART.mkdir(parents=True, exist_ok=True)
    print("evaluate_sha256", E.evaluate_sha256(), flush=True)
    for s in SPECS:
        if a.only and s["id"] != a.only:
            continue
        run(s)
    print("DONE", flush=True)


if __name__ == "__main__":
    main()

"""Small target-label permutation check for Argus-V-em round 01."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from experiments.risk_loop.argus_loop import evaluate as E
from experiments.risk_loop.argus_loop.argus_v_em import (
    ARCHS, OUT, REPORT, Ctx, fit_fold, prepare, sample_training_rows, score_metric, visible_mask,
)


def run():
    cx = Ctx()
    vis, rule = visible_mask(cx)
    X, target_rows, eval_rows, eligible = prepare(cx, vis)
    primary_cells = [k for k, v in eligible.items() if v["min3"]]
    metric_mask = eval_rows & np.isin(cx.groups, primary_cells)
    results = {"rule": rule, "architecture": "EM32", "fold_seed": 0, "permutations": []}
    for rep in range(5):
        oof = np.full(cx.n, np.nan, dtype=np.float64)
        rng = np.random.default_rng(811000 + rep)
        for fold_i, (tr, te) in enumerate(E.make_folds(cx.rows, 5, 0)):
            fit = sample_training_rows(cx, tr[target_rows[tr]], vis, 811100 + rep * 10 + fold_i)
            y_perm = vis[fit].astype(np.int64)
            for cell in sorted(set(cx.groups[fit].tolist())):
                loc = np.flatnonzero(cx.groups[fit] == cell)
                y_perm[loc] = rng.permutation(y_perm[loc])
            oof[te] = fit_fold(X[fit], y_perm, X[te], ARCHS["EM32"], 812000 + rep * 10 + fold_i)
        m3 = score_metric(cx, oof, metric_mask, 3)
        results["permutations"].append({"run": rep, "visible_min3": float(m3["value"]),
                                        "cells": int(m3["n_tools"]),
                                        "positives": int(m3["n_positives_included"])})
        print(results["permutations"][-1], flush=True)
    results["mean"] = float(np.mean([x["visible_min3"] for x in results["permutations"]]))
    results["range"] = [float(min(x["visible_min3"] for x in results["permutations"])),
                        float(max(x["visible_min3"] for x in results["permutations"]))]
    (REPORT / "round01_shuffle.json").write_text(json.dumps(E.to_jsonable(results), indent=2), encoding="utf-8")
    print("DONE", json.dumps(results), flush=True)


if __name__ == "__main__":
    run()

"""Same-target linear control for Argus-V-em round 01; no learned embedding layer."""
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
    OUT, REPORT, Ctx, fit_fold, prepare, sample_training_rows, score_metric, visible_mask,
)

SEEDS = (0, 1, 2)


def run():
    cx = Ctx()
    vis, rule = visible_mask(cx)
    X, target_rows, eval_rows, eligible = prepare(cx, vis)
    cells = [k for k, v in eligible.items() if v["min3"]]
    metric_mask = eval_rows & np.isin(cx.groups, cells)
    all_scores = []
    for seed in SEEDS:
        path = OUT / f"oof_LINEAR_s{seed}.npy"
        if path.is_file():
            all_scores.append(np.load(path))
            continue
        oof = np.full(cx.n, np.nan, dtype=np.float64)
        for fold_i, (tr, te) in enumerate(E.make_folds(cx.rows, 5, seed)):
            fit = sample_training_rows(cx, tr[target_rows[tr]], vis, 710000 + seed * 100 + fold_i)
            oof[te] = fit_fold(X[fit], vis[fit].astype(np.int64), X[te], 0,
                               300000 + seed * 100 + fold_i * 10)
            print(f"linear seed={seed} fold={fold_i} rows={len(fit)} positives={int(vis[fit].sum())}", flush=True)
        if not np.isfinite(oof).all():
            raise RuntimeError(f"non-finite linear OOF seed={seed}")
        np.save(path, oof)
        all_scores.append(oof)
    m3 = [score_metric(cx, s, metric_mask, 3) for s in all_scores]
    m2 = [score_metric(cx, s, eval_rows, 2) for s in all_scores]
    res = {"rule": rule, "control": "raw hidden vector -> linear score; same target rows, folds, sampling, loss, epochs and optimizer",
           "visible_min3": {"mean": float(np.mean([x["value"] for x in m3])),
                            "per_seed": [float(x["value"]) for x in m3], "per_cell": m3[0]["per_tool"]},
           "visible_min2": {"mean": float(np.mean([x["value"] for x in m2])),
                            "per_seed": [float(x["value"]) for x in m2]}}
    (REPORT / "round01_linear_control.json").write_text(json.dumps(E.to_jsonable(res), indent=2), encoding="utf-8")
    print("DONE", json.dumps(res), flush=True)


if __name__ == "__main__":
    run()

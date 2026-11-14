"""K11 recheck for layers 16 and 23 (coordinator request after cycle 1; the official and auxiliary probes disagreed
for L16: +0.01 vs -0.10). TRAIN rows only, labels v2, frozen evaluate.py, fold seeds 0-2.

For each layer and BOTH row sets (official = evaluate.load rows, 11,025; headline = iter01 headline rows, 9,278):
  P1 official probe  models.pca_logreg (standardise -> PCA k -> LogReg C=1 class-balanced), k = 10 and 32
  P2 auxiliary probe iter04 same_traj_pairwise (standardise -> PCA 10 -> same-rollout pair logistic C 0.01)
on orig = features/L{LL}_pre.npy and cache = obs_cache pre_action row (same rows, same folds, same probe).
Verdict per layer: PASS if no probe shows the cache worse than the original by more than 0.01
(cache - orig >= -0.01 everywhere; a gain is not information loss); otherwise FAIL (-> U4 exception / rebuild).

  py -3.11 experiments/risk_loop/argus_loop/k11_L16_L23.py
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402
from experiments.risk_loop.argus_loop import iter01_common as C1  # noqa: E402
from experiments.risk_loop.argus_loop import iter04_models as M4  # noqa: E402
from experiments.risk_loop.argus_loop import k11_cache_check as K  # noqa: E402
from experiments.risk_loop.argus_loop import models as M  # noqa: E402

OUTF = ROOT / "reports/risk-loop/argus-v1/loop/iter-13/k11_L16_L23.json"
TOL = 0.01


def probes(X, rows):
    ctx = C1.ctx_for(rows)
    ctx["trajectory"] = rows.trajectory_id.astype(str)
    out = {}
    for k in (10, 32):
        out[f"P1_pca_logreg_k{k}"] = M.build("pca_logreg", X, ctx, k=k, C=1.0, weight="class", cache=M.LRU(8))
    out["P2_pair_logistic_k10_C0.01"] = M4.same_traj_pairwise(X, ctx, k=10, C=0.01)
    return out


def main() -> int:
    assert E.evaluate_sha256() == "a7c36eafdf994f98b61895be4e4b8d237740d0018422d12febab8deb9df0130d"
    t0 = time.time()
    data = E.load(root=K.VIEW)
    off_rows = data.rows
    _, head_rows, _ = C1.headline_data(K.VIEW)
    assert set(off_rows.split.tolist()) == {"train"} and set(head_rows.split.tolist()) == {"train"}
    res = {"evaluate_sha256": E.evaluate_sha256(), "seeds": list(K.SEEDS), "tol": TOL, "layers": {},
           "row_sets": {"official": len(off_rows), "headline": len(head_rows)}}
    for L in (16, 23, 20):
        res["layers"][str(L)] = {}
        worst = None
        for rs_name, rows in (("official", off_rows), ("headline", head_rows)):
            orig = np.asarray(C1.features(data, rows, L, "pre"), dtype=np.float32)  # headline rows subset of data
            cache = np.asarray(np.load(K.OBS / f"obs_L{L:02d}.npy", mmap_mode="r")[K.pre_action_obs(rows.row_id)],
                               dtype=np.float32)
            po, pc = probes(orig, rows), probes(cache, rows)
            for p in po:
                v = {}
                for name, fp in (("orig", po[p]), ("cache", pc[p])):
                    cv = E.run_cv(fp, None, rows, K.SEEDS)
                    v[name] = E.metrics(cv, rows, bootstrap=0, baselines=False)["within_tool"]["value"]
                v["diff_cache_minus_orig"] = v["cache"] - v["orig"]
                res["layers"][str(L)][f"{rs_name}|{p}"] = v
                worst = v["diff_cache_minus_orig"] if worst is None else min(worst, v["diff_cache_minus_orig"])
                print(f"L{L} {rs_name} {p}: orig {v['orig']:.4f} cache {v['cache']:.4f} diff {v['diff_cache_minus_orig']:+.4f}",
                      flush=True)
        res["layers"][str(L)]["worst_diff"] = worst
        res["layers"][str(L)]["verdict"] = "PASS" if worst >= -TOL else "FAIL"
    res["seconds"] = time.time() - t0
    OUTF.write_text(json.dumps(E.to_jsonable(res), indent=1), encoding="utf-8")
    print(json.dumps({L: v["verdict"] for L, v in res["layers"].items()}))
    return 0


if __name__ == "__main__":
    sys.exit(main())

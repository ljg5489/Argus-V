"""Iteration 9 model tries T9-1 / T9-2a (train only). Plan: reports/risk-loop/argus-v1/loop/iter-09/plan.md.

Per try: (1) ``iter06_scan.run_try`` = frozen v4 evaluate (seeds 0,1,2; shuffles (a)(b) 20 each) + report-only
within-trajectory metrics + score-saving shuffle (b) replica; (2) fixed-model ``evaluate.run_cv`` over fold seeds
0..9 (same procedure as iteration-8 ``eval08.py`` stage B) and the 10-seed rule (i') with its standard error.
One process for both tries so the robust PCA cache is shared (RAM).

Usage: py -3.11 experiments/risk_loop/argus_loop/iter09_scan.py --only T9-1,T9-2a
"""
from __future__ import annotations

import argparse
import json
import math
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
from experiments.risk_loop.argus_loop import iter06_scan as S6  # noqa: E402
from experiments.risk_loop.argus_loop import iter07_models as M7  # noqa: E402
from experiments.risk_loop.argus_loop import iter09_models as M9  # noqa: E402

ART = REPO_ROOT / "artifacts" / "risk-loop" / "argus-v1-loop" / "iter09"
SHA = "a7c36eafdf994f98b61895be4e4b8d237740d0018422d12febab8deb9df0130d"
REF_B = 0.5905098889931206   # H2-1c shuffle (b) mean (iter-02/eval-v4.json)
REF_B_SD = 0.068             # its SD over 20 shuffles (iteration-8 eval.md)
N_SEEDS = 10


def rule_i_prime_10seed(per_seed: list, own_b_mean: float, own_b_sd: float, n_shuf: int = 20) -> dict:
    """10-seed (i') = mean(per-seed headline) - max(own shuffle (b), 0.591), with a normal-approx SE."""
    v = np.asarray(per_seed, dtype=np.float64)
    mean, sd = float(v.mean()), float(v.std(ddof=1))
    if own_b_mean >= REF_B:
        null, null_se, which = own_b_mean, own_b_sd / math.sqrt(n_shuf), "own_b"
    else:
        null, null_se, which = REF_B, REF_B_SD / math.sqrt(n_shuf), "ref_0.591"
    margin = mean - null
    se = math.sqrt(sd ** 2 / len(v) + null_se ** 2)
    p = 0.5 * (1.0 + math.erf((margin - 0.10) / (se * math.sqrt(2.0)))) if se > 0 else float(margin >= 0.10)
    return {"headline_10seed_mean": mean, "headline_10seed_sd": sd, "min": float(v.min()), "max": float(v.max()),
            "null": null, "null_which": which, "null_se": null_se, "i_prime_10seed": margin, "se": se,
            "p_true_margin_ge_0.10": p, "pass": bool(margin >= 0.10)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", required=True)
    a = ap.parse_args()
    sha = E.evaluate_sha256()
    print("evaluate_sha256", sha, flush=True)
    assert sha == SHA, sha
    ART.mkdir(parents=True, exist_ok=True)
    data, rows, rinfo = C1.headline_data()
    ctx = S6.model_ctx(rows)
    reps = sorted({c["rep"] for tid in M9.TRIES for c in M9.TRIES[tid][0]})
    feats = {}
    for r in reps:
        L, p = r.split(":")
        feats[r] = np.asarray(C1.features(data, rows, int(L.lstrip("L")), p), dtype=np.float32)
    store = M7.RobustStore(feats)
    for t in a.only.split(","):
        comps, weights = M9.TRIES[t]
        make = M9.make_try(t, store, ctx)
        out = S6.run_try(t, make, M9.GRID, rows, rinfo, ART,
                         {"note": "fixed weighted training-percentile ensemble on robust PCA 32",
                          "components": list(comps), "weights": list(weights),
                          "preproc": {"scale": "median, IQR/1.349", "clip": M7.CLIP, "kmax": M7.KMAX}})
        t0 = time.time()
        cv = E.run_cv(make(M9.GRID[0]), None, rows, seeds=list(range(N_SEEDS)))
        O = np.asarray([cv["oof"][str(s)] for s in range(N_SEEDS)], dtype=np.float64)
        np.save(ART / f"oof10_{t}.npy", O)
        m = E.metrics(cv, rows)
        per_seed = m["within_tool"]["per_seed"]
        h = out["harness"]
        own_b = h["shuffle_source_family"]
        # consistency: fold seeds 0..2 of the fixed-model run must equal the evaluate() headline per seed
        same012 = bool(np.allclose(per_seed[:3], h["metrics"]["within_tool"]["per_seed"], atol=1e-12))
        res = {"id": t, "seeds": list(range(N_SEEDS)), "per_seed": per_seed,
               "ci95_10seed": m["within_tool"]["ci95"],
               "by_source_10seed": {s: v["value"] for s, v in m["within_tool"]["by_source"].items()},
               "seeds012_match_evaluate": same012,
               "rule_i_prime_10seed": rule_i_prime_10seed(per_seed, own_b["within_tool_mean"],
                                                          own_b["within_tool_sd"]),
               "seconds": time.time() - t0, "evaluate_sha256": sha}
        E.dump(res, ART / f"{t}_10seed.json")
        print(t, "10seed", json.dumps(E.to_jsonable(res["rule_i_prime_10seed"])), "match012", same012,
              [round(x, 3) for x in per_seed], "sec", round(time.time() - t0), flush=True)
    print("robust_embeddings_computed", store.computed, flush=True)
    print("DONE", flush=True)


if __name__ == "__main__":
    main()

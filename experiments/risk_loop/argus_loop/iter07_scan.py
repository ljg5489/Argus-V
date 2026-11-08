"""Iteration 7 model tries T7-a / T7-c (train only). Plan: reports/risk-loop/argus-v1/loop/iter-07/plan.md.
Reuses ``iter06_scan.run_try`` (frozen v4 evaluate + report-only within-trajectory metrics + shuffle replica).

Usage: py -3.11 experiments/risk_loop/argus_loop/iter07_scan.py --only T7-a
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ.setdefault(_v, "2")

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402
from experiments.risk_loop.argus_loop import iter01_common as C1  # noqa: E402
from experiments.risk_loop.argus_loop import iter05_common as C5  # noqa: E402
from experiments.risk_loop.argus_loop import iter06_models as M6  # noqa: E402
from experiments.risk_loop.argus_loop import iter06_scan as S6  # noqa: E402
from experiments.risk_loop.argus_loop import iter07_models as M7  # noqa: E402

ART = REPO_ROOT / "artifacts" / "risk-loop" / "argus-v1-loop" / "iter07"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", required=True)
    a = ap.parse_args()
    print("evaluate_sha256", E.evaluate_sha256(), flush=True)
    data, rows, rinfo = C1.headline_data()
    ctx = S6.model_ctx(rows)
    ctx["family"] = rows.family.astype(str)
    for t in a.only.split(","):
        if t == "T7-a":
            reps = sorted({c["rep"] for c in M6.ENSEMBLE})
            feats = {}
            for r in reps:
                L, p = r.split(":")
                feats[r] = np.asarray(C1.features(data, rows, int(L.lstrip("L")), p), dtype=np.float32)
            store = M7.RobustStore(feats)
            S6.run_try(t, M6.make_t62(store, ctx), M7.GRID_T7A, rows, rinfo, ART,
                       {"note": "T6-2 ensemble with median/IQR scaling + |z|<=3 clipping before PCA 32",
                        "components": list(M6.ENSEMBLE),
                        "preproc": {"scale": "median, IQR/1.349", "clip": M7.CLIP, "kmax": M7.KMAX}})
            print("robust_embeddings_computed", store.computed, flush=True)
        elif t == "T7-c":
            store = C5.EmbStore(on_miss=C5.real_on_miss(data, rows))
            S6.run_try(t, M7.make_t7c(store, ctx), M7.GRID_T7C, rows, rinfo, ART,
                       {"note": "same-trajectory pair MLP (1 hidden tanh layer), layer 23 max PCA 32"})
            print("embedding_misses", store.misses, flush=True)
        else:
            raise ValueError(t)
    print("DONE", flush=True)


if __name__ == "__main__":
    main()

"""Iteration 9 models (train only). Plan: reports/risk-loop/argus-v1/loop/iter-09/plan.md.

Both tries use the robust embedding store of iteration 7 (``iter07_models.RobustStore``: median/IQR scaling,
|z| clipped at 3, PCA 32 fitted on training rows) and the component fitters of iteration 6
(``iter06_models._component_scores``). Fixed configurations, no selection.

- T9-1: equal-weight training-percentile ensemble of pair models only: T4-1a (same-trajectory pairs, L23 max),
  T4-1b (same-trajectory pairs, L16 pre), T6-1 (same-trajectory AND same-tool pairs, L23 max, k 10, C 0.1 =
  modal nested-CV choice of iteration 6).
- T9-2a: the T7-a members (H2-1c-L23 pointwise, T4-1a, T4-1b) with weights 1 : 3 : 3 (pointwise = 1/3 of a
  pair member, fixed a priori).

Scoring reads only the scored rows' embeddings; tool / trajectory / source are read at training rows only.
Earlier files are not modified.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop.argus_loop import iter06_models as M6  # noqa: E402

_H21C, _T41A, _T41B = M6.ENSEMBLE
T61 = {"name": "T6-1", "rep": "L23:max", "kind": "pair_traj_tool", "k": 10, "C": 0.1}

T91_COMPONENTS = (_T41A, _T41B, T61)
T91_WEIGHTS = (1.0, 1.0, 1.0)
T92A_COMPONENTS = (_H21C, _T41A, _T41B)
T92A_WEIGHTS = (1.0, 3.0, 3.0)

TRIES = {
    "T9-1": (T91_COMPONENTS, T91_WEIGHTS),
    "T9-2a": (T92A_COMPONENTS, T92A_WEIGHTS),
}
GRID = [{"fixed": "ensemble_robust_weighted"}]


def make_weighted(store, ctx: dict, components, weights):
    """make_fit_predict(g) for a fixed weighted training-percentile ensemble (grid of one dummy entry)."""
    w = np.asarray(weights, dtype=np.float64)
    if len(w) != len(components) or (w <= 0).any():
        raise ValueError("weights")
    w = w / w.sum()

    def make(g):
        def fp(pos_train, y_train, pos_test):
            pos_train = np.asarray(pos_train, dtype=np.int64)
            pos_test = np.asarray(pos_test, dtype=np.int64)
            y_train = np.asarray(y_train).astype(np.int64)
            acc = np.zeros(len(pos_test))
            for comp, wk in zip(components, w):
                s_tr, s_te = M6._component_scores(comp, store, ctx, pos_train, y_train, pos_test)
                acc += wk * M6.train_percentile(s_tr, s_te)
            return acc
        return fp
    return make


def make_try(tid: str, store, ctx: dict):
    comps, weights = TRIES[tid]
    return make_weighted(store, ctx, comps, weights)

"""Iteration 4 model (T4-1): same-rollout pair training.

Inside the training fold only, build every (violation step, normal step) pair that shares a trajectory
(``ctx["trajectory"]`` is read only at ``pos_train``). Each positive's pairs weigh 1 in total. Fit a
logistic loss without intercept on embedding differences (standardise + PCA fitted on training rows, first
k components). Score of a single step = the same linear map applied to its embedding; scoring never reads
the trajectory, tool, source or any scenario code. ``models.py`` is not modified; the factory is added to
its registry at import.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop.argus_loop import models as M  # noqa: E402


def same_traj_pair_fit(Etr: np.ndarray, y: np.ndarray, traj_tr: np.ndarray, C: float) -> np.ndarray | None:
    """Coefficient vector (k,) from same-trajectory pairs, or None when the fold has no such pair."""
    from sklearn.linear_model import LogisticRegression

    I, J, W = M.same_group_pairs(y, traj_tr)
    if len(I) == 0:
        return None
    D = np.asarray(Etr[I] - Etr[J], dtype=np.float64)
    lr = LogisticRegression(C=C, max_iter=3000, fit_intercept=False)
    lr.fit(np.vstack([D, -D]), np.r_[np.ones(len(D)), np.zeros(len(D))], sample_weight=np.r_[W, W])
    return lr.coef_.ravel()


@M.register("same_traj_pairwise")
def same_traj_pairwise(X, ctx, *, k=10, C=0.01, kmax=None, cache=None):
    """T4-1: standardise -> PCA(kmax) on training rows -> pairwise logistic loss on (violation - normal)
    differences of same-trajectory pairs in the training fold -> single-step linear score."""
    kmax = int(kmax or k)
    cache = cache if cache is not None else M.LRU(8)
    tag = f"t41pca{kmax}"
    traj_all = np.asarray(ctx["trajectory"]).astype(str)  # read only at pos_train below

    def fp(pos_train, y_train, pos_test):
        pos_train = np.asarray(pos_train, dtype=np.int64)
        pos_test = np.asarray(pos_test, dtype=np.int64)
        y_train = np.asarray(y_train).astype(np.int64)
        key = M._key(pos_train, tag)
        Emb = cache.get(key)
        if Emb is None:
            Emb = M.pca_embed(X, pos_train, kmax, ctx=ctx)
            cache.put(key, Emb)
        kk = min(k, Emb.shape[1])
        w = same_traj_pair_fit(Emb[pos_train, :kk], y_train, traj_all[pos_train], C)
        if w is None:
            return np.zeros(len(pos_test))
        return Emb[pos_test, :kk].astype(np.float64) @ w

    return fp

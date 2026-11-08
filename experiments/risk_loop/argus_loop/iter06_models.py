"""Iteration 6 models (train only). Plan: reports/risk-loop/argus-v1/loop/iter-06/plan.md.

- T6-1 ``same_traj_tool_pair``: pair training restricted to (violation, normal) pairs sharing BOTH the
  trajectory and the tool, inside the training fold only (``ctx["trajectory"]`` and ``ctx["tool"]`` are read
  only at ``pos_train``; TASK.md section 3 allows the tool as a training-only signal). Logistic loss without
  intercept on embedding differences (iteration-4 ``same_traj_pair_fit`` with the group key trajectory|tool).
  Score of a step = linear map of its own embedding.
- T6-2 ``fixed_rank_ensemble``: equal-weight average of the training-score percentiles of three pre-specified
  models (no selection): H2-1c-L23 pointwise, T4-1a pair L23 max, T4-1b pair L16 pre. Each component's test
  score is mapped to its mid-rank percentile among that component's *training-row* scores, so test rows never
  influence each other's score.

Embeddings come from the iteration-5 store (standardise -> PCA 32 on the harness training sets).
No tool, source, family, trajectory or scenario code is read at scoring time. Earlier files are not modified.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop.argus_loop import iter04_models as M4  # noqa: E402
from experiments.risk_loop.argus_loop import models as M  # noqa: E402

# Pre-specified components of T6-2 (modal nested-CV choices of iterations 2 and 4; fixed, never selected here).
ENSEMBLE = (
    {"name": "H2-1c-L23", "rep": "L23:max", "kind": "pointwise_informative", "k": 32, "C": 0.1},
    {"name": "T4-1a", "rep": "L23:max", "kind": "pair_traj", "k": 32, "C": 0.001},
    {"name": "T4-1b", "rep": "L16:pre", "kind": "pair_traj", "k": 10, "C": 0.01},
)


def pointwise_informative_fit(Etr: np.ndarray, y: np.ndarray, src_tr: np.ndarray, grp_tr: np.ndarray,
                              C: float) -> np.ndarray | None:
    """H2-1c (models.tool_weighted_logreg) on a given embedding: source x class weights, normals of training
    strata (tool x source) with both classes up-weighted to half the normal weight; centred training rows.
    Returns the coefficient vector (score = E @ w; the intercept is a constant and dropped as in H2-1c)."""
    from sklearn.linear_model import LogisticRegression

    y = np.asarray(y).astype(np.int64)
    if len(np.unique(y)) < 2:
        return None
    Etr = np.asarray(Etr, dtype=np.float64)
    base = M.sample_weights(y, src_tr, "source_class")
    base = M.informative_group_weights(y, grp_tr, base)
    lr = LogisticRegression(C=C, max_iter=3000)
    lr.fit(Etr - Etr.mean(0), y, sample_weight=base)
    return lr.coef_.ravel()


def train_percentile(s_train: np.ndarray, s_test: np.ndarray) -> np.ndarray:
    """Mid-rank percentile of each test score among the training scores (in [0, 1])."""
    st = np.sort(np.asarray(s_train, dtype=np.float64))
    s_test = np.asarray(s_test, dtype=np.float64)
    lo = np.searchsorted(st, s_test, side="left")
    hi = np.searchsorted(st, s_test, side="right")
    return (lo + hi) / (2.0 * len(st))


def _component_scores(comp: dict, store, ctx: dict, pos_train, y_train, pos_test):
    """(training-row scores, test-row scores) of one component; zeros if it cannot be fitted."""
    Emb = store.get(comp["rep"], pos_train)[:, :int(comp["k"])]
    Etr = Emb[pos_train].astype(np.float64)
    Ete = Emb[pos_test].astype(np.float64)
    if comp["kind"] == "pointwise_informative":
        w = pointwise_informative_fit(Etr, y_train, np.asarray(ctx["source"]).astype(str)[pos_train],
                                      np.asarray(ctx["train_group"]).astype(str)[pos_train], comp["C"])
    elif comp["kind"] == "pair_traj":
        w = M4.same_traj_pair_fit(Etr, y_train, np.asarray(ctx["trajectory"]).astype(str)[pos_train], comp["C"])
    elif comp["kind"] == "pair_traj_tool":
        key = np.asarray([f"{a}|{b}" for a, b in zip(np.asarray(ctx["trajectory"]).astype(str)[pos_train],
                                                     np.asarray(ctx["tool"]).astype(str)[pos_train])])
        w = M4.same_traj_pair_fit(Etr, y_train, key, comp["C"])
    else:
        raise ValueError(comp["kind"])
    if w is None:
        return np.zeros(len(pos_train)), np.zeros(len(pos_test))
    return Etr @ w, Ete @ w


def make_t61(store, ctx: dict, rep: str = "L23:max"):
    """make_fit_predict(g) for T6-1; g = {"k": int, "C": float}."""
    def make(g):
        comp = {"rep": rep, "kind": "pair_traj_tool", "k": int(g["k"]), "C": float(g["C"])}

        def fp(pos_train, y_train, pos_test):
            pos_train = np.asarray(pos_train, dtype=np.int64)
            pos_test = np.asarray(pos_test, dtype=np.int64)
            return _component_scores(comp, store, ctx, pos_train, np.asarray(y_train).astype(np.int64),
                                     pos_test)[1]
        return fp
    return make


def make_t62(store, ctx: dict, components=ENSEMBLE):
    """make_fit_predict(g) for T6-2 (grid of one dummy entry)."""
    def make(g):
        def fp(pos_train, y_train, pos_test):
            pos_train = np.asarray(pos_train, dtype=np.int64)
            pos_test = np.asarray(pos_test, dtype=np.int64)
            y_train = np.asarray(y_train).astype(np.int64)
            acc = np.zeros(len(pos_test))
            for comp in components:
                s_tr, s_te = _component_scores(comp, store, ctx, pos_train, y_train, pos_test)
                acc += train_percentile(s_tr, s_te)
            return acc / len(components)
        return fp
    return make


GRID_T61 = [{"k": k, "C": C} for k in (10, 32) for C in (0.001, 0.01, 0.1)]
GRID_T62 = [{"fixed": "ensemble"}]

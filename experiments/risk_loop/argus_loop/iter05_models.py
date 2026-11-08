"""Iteration 5 model families (step-level, pair-trained). One family = one counted try; the inner CV of the
frozen harness picks representation x hyperparameters from the family's grid.

Grid entries are dicts: {"gi": index, "rep": "L16:pre" | ("L16:pre", "L23:max"), "k": int, "C": float,
optionally "lam" (T5-2) / "alpha" (T5-3)}.

- pair   (T5-1): same-trajectory (violation, normal) pairs inside the training fold, logistic loss without
                 intercept on embedding differences (iteration-4 ``same_traj_pair_fit``). Score = linear.
- hybrid (T5-2): one logistic regression on [pair-difference rows (constant column 0)] + [training rows
                 (labels y, class-balanced weights, constant column = intercept)], pointwise total weight =
                 lam x pair total weight. Score = linear part only.
- rollout(T5-3): pair score + alpha x mean pair score of the strictly earlier steps of the same trajectory
                 among the scored rows (training-row mean score where no earlier step exists).
- multi  (T5-4): pair model on the concatenation of the first k components of two representations.

Only ``pos_train`` rows' trajectory ids are read when fitting (pairs). Scoring reads only the embedding of the
scored rows (+ for T5-3 the trajectory id and step index of the scored rows, to find earlier steps). No tool,
source, family or scenario code is ever read. ``models.py`` / ``iter04_models.py`` are not modified.
"""
from __future__ import annotations

import sys
import threading
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop.argus_loop import iter04_common as C4  # noqa: E402
from experiments.risk_loop.argus_loop import iter04_models as M4  # noqa: E402
from experiments.risk_loop.argus_loop import iter05_common as C5  # noqa: E402
from experiments.risk_loop.argus_loop import models as M  # noqa: E402

INTERCEPT_COL = 10.0  # constant column for the hybrid's pointwise intercept (large -> weakly penalised)


def hybrid_fit(Etr: np.ndarray, y: np.ndarray, traj_tr: np.ndarray, C: float, lam: float) -> np.ndarray | None:
    from sklearn.linear_model import LogisticRegression

    y = np.asarray(y).astype(np.int64)
    if len(np.unique(y)) < 2:
        return None
    Etr = np.asarray(Etr, dtype=np.float64)
    k = Etr.shape[1]
    I, J, W = M.same_group_pairs(y, traj_tr)
    blocks, labels, weights = [], [], []
    if len(I):
        D = Etr[I] - Etr[J]
        blocks += [np.c_[D, np.zeros(len(D))], np.c_[-D, np.zeros(len(D))]]
        labels += [np.ones(len(D)), np.zeros(len(D))]
        weights += [W, W]
        pair_total = 2.0 * W.sum()
    else:
        pair_total = float(len(y))
    wp = M.sample_weights(y, None, "class")
    wp = wp * (float(lam) * pair_total / wp.sum())
    blocks.append(np.c_[Etr, np.full(len(Etr), INTERCEPT_COL)])
    labels.append(y.astype(np.float64))
    weights.append(wp)
    lr = LogisticRegression(C=C, max_iter=3000, fit_intercept=False)
    lr.fit(np.vstack(blocks), np.concatenate(labels), sample_weight=np.concatenate(weights))
    return lr.coef_.ravel()[:k]


class InnerRecorder:
    """Accumulates, per (inner training set hash, grid index), the within-trajectory AUROC (scope B: all
    scored rows) of inner-fold calls. Trajectories never straddle folds, so per-call sums add up to the inner
    OOF value. Uses true labels of the scored rows (as the harness' inner headline does). Report-only."""

    def __init__(self, y: np.ndarray, traj: np.ndarray, inner_hashes: set[str]):
        self.y = np.asarray(y).astype(np.int64)
        self.traj = np.asarray(traj).astype(str)
        self.inner = set(inner_hashes)
        self.acc: dict[tuple[str, int], list[float]] = {}
        self._lock = threading.Lock()

    def log(self, gi: int, pos_train, pos_test, score):
        h = C5.pos_hash(pos_train)
        if h not in self.inner:
            return
        r = C4.within_traj_auroc(score, self.y[pos_test], self.traj[pos_test])
        if r["value"] is None:
            return
        with self._lock:
            a = self.acc.setdefault((h, int(gi)), [0.0, 0.0])
            a[0] += r["value"] * r["n_positives"]
            a[1] += r["n_positives"]

    def value(self, h: str, gi: int):
        a = self.acc.get((h, int(gi)))
        return None if not a or a[1] == 0 else a[0] / a[1]


def make_family(kind: str, store: C5.EmbStore, ctx: dict, recorder: InnerRecorder | None = None):
    """make_fit_predict(g) for evaluate(grid=...). ctx: trajectory (str per row), step_index (float)."""
    traj_all = np.asarray(ctx["trajectory"]).astype(str)
    step_all = np.asarray(ctx["step_index"], dtype=np.float64)

    def make(g):
        g = dict(g)

        def fp(pos_train, y_train, pos_test):
            pos_train = np.asarray(pos_train, dtype=np.int64)
            pos_test = np.asarray(pos_test, dtype=np.int64)
            y_train = np.asarray(y_train).astype(np.int64)
            reps = g["rep"] if isinstance(g["rep"], (tuple, list)) else (g["rep"],)
            Emb = np.hstack([store.get(r, pos_train)[:, :int(g["k"])] for r in reps])
            Etr = Emb[pos_train]
            if kind == "hybrid":
                w = hybrid_fit(Etr, y_train, traj_all[pos_train], g["C"], g["lam"])
            elif kind in ("pair", "rollout", "multi"):
                w = M4.same_traj_pair_fit(Etr, y_train, traj_all[pos_train], g["C"])
            else:
                raise ValueError(kind)
            if w is None:
                s = np.zeros(len(pos_test))
            else:
                s = Emb[pos_test].astype(np.float64) @ w
                alpha = float(g.get("alpha", 0.0))
                if kind == "rollout" and alpha != 0.0:
                    fill = float((Etr.astype(np.float64) @ w).mean())
                    s = s + alpha * C5.earlier_mean(s, traj_all[pos_test], step_all[pos_test], fill)
            if recorder is not None:
                recorder.log(g["gi"], pos_train, pos_test, s)
            return s

        return fp

    return make


def grid_for(tid: str) -> list[dict]:
    base = [(r, k, C) for r in C5.REPS for k in (10, 32) for C in (0.001, 0.01)]
    if tid == "T5-1":
        g = [{"rep": r, "k": k, "C": C} for r, k, C in base]
    elif tid == "T5-2":
        g = [{"rep": r, "k": k, "C": C, "lam": lam} for r, k, C in base for lam in (0.1, 1.0)]
    elif tid == "T5-3":
        g = [{"rep": r, "k": k, "C": C, "alpha": a} for r, k, C in base for a in (0.0, 0.5, 1.0, 2.0)]
    elif tid == "T5-4":
        pairs = [(a, b) for i, a in enumerate(C5.REPS) for b in C5.REPS[i + 1:]
                 if C5.rep_layer(a) != C5.rep_layer(b)]
        g = [{"rep": p, "k": 10, "C": C} for p in pairs for C in (0.001, 0.01)]
    else:
        raise ValueError(tid)
    for i, e in enumerate(g):
        e["gi"] = i
    return g


KIND = {"T5-1": "pair", "T5-2": "hybrid", "T5-3": "rollout", "T5-4": "multi"}

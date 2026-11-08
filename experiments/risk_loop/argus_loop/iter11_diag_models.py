"""Iteration 11 diagnosis: model factories (existing recipes, unchanged) + CV loops with training-row masks.

All loops use the frozen harness folds (``evaluate.make_folds``, family/trajectory/unit components) unless a
diagnostic grouping is named explicitly (D2). Train split rows only.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402
from experiments.risk_loop.argus_loop import iter01_common as C1  # noqa: E402
from experiments.risk_loop.argus_loop import iter06_models as M6  # noqa: E402
from experiments.risk_loop.argus_loop import iter06_scan as S6  # noqa: E402
from experiments.risk_loop.argus_loop import iter07_models as M7  # noqa: E402
from experiments.risk_loop.argus_loop import models as M  # noqa: E402

FIT_COUNT = {"configs": set(), "fold_fits": 0}


def load_feats(data, rows, reps):
    out = {}
    for r in reps:
        L, p = r.split(":")
        out[r] = np.asarray(C1.features(data, rows, int(L.lstrip("L")), p), dtype=np.float32)
    return out


def make_t7a(feats, rows):
    """T7-a = fixed equal-weight percentile ensemble of 3 members on robust PCA-32 embeddings."""
    store = M7.RobustStore(feats)
    ctx = S6.model_ctx(rows)
    return M6.make_t62(store, ctx)(M7.GRID_T7A[0]), store


def make_h10a(X16max, rows):
    """H1-0a = original Argus-V1 recipe: standardise -> PCA 10 -> LogReg C=1, class-balanced weights."""
    return M.grid_maker("pca_logreg", X16max, C1.ctx_for(rows), {"weight": "class"}, M.LRU(8))({"k": 10, "C": 1.0})


def cv_oof(fp, rows, seeds, keep_train=None, folds_fn=None, tag="", log=print, frac=None, rep=0):
    """OOF scores per seed. keep_train: bool mask of rows allowed in training (others dropped from every
    training fold, still scored when in a test fold). frac: keep this fraction of the training fold's
    families (seeded by (seed, fold, rep)); evaluation rows unchanged."""
    y = rows.y
    O = []
    for s in seeds:
        folds = folds_fn(rows, s) if folds_fn else E.make_folds(rows, 5, s)
        oof = np.full(len(rows), np.nan)
        for fi, (a, b) in enumerate(folds):
            if keep_train is not None:
                a = a[keep_train[a]]
            if frac is not None and frac < 1.0:
                comp = E.group_components(rows.subset(a))
                u = np.unique(comp)
                rng = np.random.default_rng(10_000 * rep + 100 * s + fi)
                k = max(1, int(round(frac * len(u))))
                for _try in range(50):
                    pick = rng.choice(u, size=k, replace=False)
                    sel = np.isin(comp, pick)
                    if y[a[sel]].sum() >= 2:
                        break
                a = a[sel]
            oof[b] = np.asarray(fp(a, y[a].copy(), b), dtype=np.float64)
            FIT_COUNT["fold_fits"] += 1
        O.append(oof)
        if tag:
            log(time.strftime("%H:%M:%S"), tag, "seed", s, "done")
    if tag:
        FIT_COUNT["configs"].add(tag.split("#")[0])
    return np.asarray(O)

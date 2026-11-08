"""Unit tests for iteration-6 code. py -3.11 experiments/risk_loop/argus_loop/test_iter06.py"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop.argus_loop import iter05_common as C5  # noqa: E402
from experiments.risk_loop.argus_loop import iter06_models as M6  # noqa: E402
from experiments.risk_loop.argus_loop import iter06_scan as S6  # noqa: E402
from experiments.risk_loop.argus_loop import models as M  # noqa: E402
from experiments.risk_loop.argus_loop.test_iter05 import synth_rows  # noqa: E402


def store_for(X):
    return C5.EmbStore(memory={}, on_miss=lambda rep, pos: C5.compute_embedding(X, pos, kmax=8))


def test_pointwise_matches_h21c():
    rows, X = synth_rows()
    ctx = S6.model_ctx(rows)
    pos_tr, pos_te = np.arange(0, 150), np.arange(150, len(rows))
    ref = M.build("tool_weighted_logreg", X, ctx, k=8, C=0.1, kmax=8)(pos_tr, rows.y[pos_tr], pos_te)
    Emb = C5.compute_embedding(X, pos_tr, kmax=8)
    w = M6.pointwise_informative_fit(Emb[pos_tr], rows.y[pos_tr], ctx["source"][pos_tr],
                                     ctx["train_group"][pos_tr], 0.1)
    mine = Emb[pos_te].astype(np.float64) @ w
    assert np.corrcoef(ref, mine)[0, 1] > 0.999, np.corrcoef(ref, mine)[0, 1]


def test_scoring_ignores_test_tool_and_trajectory():
    rows, X = synth_rows()
    ctx = S6.model_ctx(rows)
    pos_tr, pos_te = np.arange(0, 150), np.arange(150, len(rows))
    s1 = M6.make_t61(store_for(X), ctx, rep="r")({"k": 8, "C": 0.1})(pos_tr, rows.y[pos_tr], pos_te)
    e1 = M6.make_t62(store_for(X), ctx, components=[dict(c, rep="r", k=8) for c in M6.ENSEMBLE])({})(
        pos_tr, rows.y[pos_tr], pos_te)
    ctx2 = {k: v.copy() for k, v in ctx.items()}
    for k in ctx2:
        ctx2[k][pos_te] = "zzz"
    s2 = M6.make_t61(store_for(X), ctx2, rep="r")({"k": 8, "C": 0.1})(pos_tr, rows.y[pos_tr], pos_te)
    e2 = M6.make_t62(store_for(X), ctx2, components=[dict(c, rep="r", k=8) for c in M6.ENSEMBLE])({})(
        pos_tr, rows.y[pos_tr], pos_te)
    assert np.allclose(s1, s2) and np.allclose(e1, e2)
    assert np.abs(s1).sum() > 0


def test_t61_uses_only_same_tool_pairs():
    rows, X = synth_rows()
    ctx = S6.model_ctx(rows)
    pos_tr = np.arange(0, 150)
    y = rows.y[pos_tr]
    # changing the tool of every training normal to a unique value removes all same-tool pairs -> zero scores
    ctx2 = {k: v.copy() for k, v in ctx.items()}
    neg = pos_tr[y == 0]
    ctx2["tool"] = ctx2["tool"].astype(object)
    ctx2["tool"][neg] = [f"u{i}" for i in range(len(neg))]
    s = M6.make_t61(store_for(X), ctx2, rep="r")({"k": 8, "C": 0.1})(pos_tr, y, np.arange(150, 200))
    assert np.all(s == 0)


def test_percentile_is_rowwise():
    rng = np.random.default_rng(0)
    tr, te = rng.normal(size=500), rng.normal(size=50)
    p = M6.train_percentile(tr, te)
    assert np.all((p >= 0) & (p <= 1))
    assert np.allclose(p[:10], M6.train_percentile(tr, te[:10]))
    assert np.all(np.diff(M6.train_percentile(tr, np.sort(te))) >= 0)


if __name__ == "__main__":
    n = 0
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            n += 1
            print("ok", name)
    print(n, "passed")

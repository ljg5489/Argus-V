"""Unit tests for iteration-10 code. py -3.11 experiments/risk_loop/argus_loop/test_iter10.py"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402
from experiments.risk_loop.argus_loop import iter05_common as C5  # noqa: E402
from experiments.risk_loop.argus_loop import iter06_models as M6  # noqa: E402
from experiments.risk_loop.argus_loop import iter06_scan as S6  # noqa: E402
from experiments.risk_loop.argus_loop import iter09_models as M9  # noqa: E402
from experiments.risk_loop.argus_loop import iter10_models as M10  # noqa: E402
from experiments.risk_loop.argus_loop.test_iter05 import synth_rows  # noqa: E402


def store_for(X):
    return C5.EmbStore(memory={}, on_miss=lambda rep, pos: C5.compute_embedding(X, pos, kmax=8))


LOCAL = tuple(dict(m, rep="r", k=min(int(m["k"]), 8)) for m in M10.MEMBERS)


def test_grid():
    assert len(M10.GRID) == 15 and len({tuple(g["members"]) for g in M10.GRID}) == 15
    assert [len(g["members"]) for g in M10.GRID] == [1] * 4 + [2] * 6 + [3] * 4 + [4]
    assert M10.MEMBER_NAMES == ("H2-1c-L23", "T4-1a", "T4-1b", "T6-1")
    assert M10.MEMBERS[3] == M9.T61


def test_subsets_match_earlier_ensembles_and_cache_is_exact():
    rows, X = synth_rows()
    ctx = S6.model_ctx(rows)
    pos_tr, pos_te = np.arange(0, 150), np.arange(150, len(rows))
    y = rows.y[pos_tr]
    on = M10.make_subset(M10.MemberCache(store_for(X), ctx, members=LOCAL))
    off = M10.make_subset(M10.MemberCache(store_for(X), ctx, members=LOCAL, enabled=False))
    ref62 = M6.make_t62(store_for(X), ctx, components=LOCAL[:3])({})(pos_tr, y, pos_te)
    assert np.allclose(on({"members": [0, 1, 2]})(pos_tr, y, pos_te), ref62)
    ref91 = M9.make_weighted(store_for(X), ctx, LOCAL[1:], (1, 1, 1))({})(pos_tr, y, pos_te)
    assert np.allclose(on({"members": [1, 2, 3]})(pos_tr, y, pos_te), ref91)
    for g in M10.GRID:  # cached (second call) == uncached
        assert np.allclose(on(g)(pos_tr, y, pos_te), off(g)(pos_tr, y, pos_te))
    yb = y.copy()[::-1]  # different labels must not hit the cache
    assert not np.allclose(on({"members": [0]})(pos_tr, yb, pos_te), on({"members": [0]})(pos_tr, y, pos_te))


def test_scoring_ignores_test_metadata():
    rows, X = synth_rows()
    ctx = S6.model_ctx(rows)
    pos_tr, pos_te = np.arange(0, 150), np.arange(150, len(rows))
    ctx2 = {k: np.asarray(v, dtype=object).copy() for k, v in ctx.items()}
    for k in ctx2:
        ctx2[k][pos_te] = "zzz"
    a = M10.make_subset(M10.MemberCache(store_for(X), ctx, members=LOCAL))
    b = M10.make_subset(M10.MemberCache(store_for(X), ctx2, members=LOCAL))
    for g in M10.GRID:
        assert np.allclose(a(g)(pos_tr, rows.y[pos_tr], pos_te), b(g)(pos_tr, rows.y[pos_tr], pos_te))


def test_nested_cv_runs_and_picks_from_grid():
    rows, X = synth_rows()
    ctx = S6.model_ctx(rows)
    make = M10.make_subset(M10.MemberCache(store_for(X), ctx, members=LOCAL))
    cv = E.nested_cv(make, M10.GRID, None, rows, seeds=[0])
    assert all(0 <= c < 15 for c in cv["selection"]["chosen"]["0"])
    assert np.all(np.isfinite(cv["oof"]["0"]))


if __name__ == "__main__":
    n = 0
    for name, f in list(globals().items()):
        if name.startswith("test_") and callable(f):
            f()
            n += 1
            print("ok", name)
    print(n, "passed")

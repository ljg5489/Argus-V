"""Unit tests for iteration-9 code. py -3.11 experiments/risk_loop/argus_loop/test_iter09.py"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop.argus_loop import iter05_common as C5  # noqa: E402
from experiments.risk_loop.argus_loop import iter06_models as M6  # noqa: E402
from experiments.risk_loop.argus_loop import iter06_scan as S6  # noqa: E402
from experiments.risk_loop.argus_loop import iter09_models as M9  # noqa: E402
from experiments.risk_loop.argus_loop import iter09_scan as S9  # noqa: E402
from experiments.risk_loop.argus_loop.test_iter05 import synth_rows  # noqa: E402


def store_for(X):
    return C5.EmbStore(memory={}, on_miss=lambda rep, pos: C5.compute_embedding(X, pos, kmax=8))


def _local(comps):
    return [dict(c, rep="r", k=8) for c in comps]


def test_definitions():
    assert [c["kind"] for c in M9.T91_COMPONENTS] == ["pair_traj", "pair_traj", "pair_traj_tool"]
    assert all(c["kind"] != "pointwise_informative" for c in M9.T91_COMPONENTS)
    assert M9.T92A_COMPONENTS == M6.ENSEMBLE and M9.T92A_WEIGHTS == (1.0, 3.0, 3.0)
    assert len(M9.GRID) == 1


def test_equal_weights_match_t62_and_weights_matter():
    rows, X = synth_rows()
    ctx = S6.model_ctx(rows)
    pos_tr, pos_te = np.arange(0, 150), np.arange(150, len(rows))
    comps = _local(M6.ENSEMBLE)
    ref = M6.make_t62(store_for(X), ctx, components=comps)({})(pos_tr, rows.y[pos_tr], pos_te)
    eq = M9.make_weighted(store_for(X), ctx, comps, (2.0, 2.0, 2.0))({})(pos_tr, rows.y[pos_tr], pos_te)
    assert np.allclose(ref, eq)
    wtd = M9.make_weighted(store_for(X), ctx, comps, (1.0, 3.0, 3.0))({})(pos_tr, rows.y[pos_tr], pos_te)
    assert not np.allclose(ref, wtd) and np.all((wtd >= 0) & (wtd <= 1))


def test_scoring_ignores_test_metadata():
    rows, X = synth_rows()
    ctx = S6.model_ctx(rows)
    pos_tr, pos_te = np.arange(0, 150), np.arange(150, len(rows))
    ctx2 = {k: np.asarray(v, dtype=object).copy() for k, v in ctx.items()}
    for k in ctx2:
        ctx2[k][pos_te] = "zzz"
    for comps, w in M9.TRIES.values():
        a = M9.make_weighted(store_for(X), ctx, _local(comps), w)({})(pos_tr, rows.y[pos_tr], pos_te)
        b = M9.make_weighted(store_for(X), ctx2, _local(comps), w)({})(pos_tr, rows.y[pos_tr], pos_te)
        assert np.allclose(a, b)


def test_rule_i_prime():
    r = S9.rule_i_prime_10seed([0.70] * 5 + [0.72] * 5, 0.52, 0.06)
    assert r["null_which"] == "ref_0.591" and abs(r["i_prime_10seed"] - (0.71 - S9.REF_B)) < 1e-12
    assert r["pass"] and 0.5 < r["p_true_margin_ge_0.10"] < 1
    r2 = S9.rule_i_prime_10seed([0.70] * 10, 0.65, 0.06)
    assert r2["null_which"] == "own_b" and not r2["pass"]


if __name__ == "__main__":
    n = 0
    for name, f in list(globals().items()):
        if name.startswith("test_") and callable(f):
            f()
            n += 1
            print("ok", name)
    print(n, "passed")

"""Unit tests for iteration-7 code. py -3.11 experiments/risk_loop/argus_loop/test_iter07.py"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop.argus_loop import iter05_common as C5  # noqa: E402
from experiments.risk_loop.argus_loop import iter06_scan as S6  # noqa: E402
from experiments.risk_loop.argus_loop import iter07_models as M7  # noqa: E402
from experiments.risk_loop.argus_loop.test_iter05 import synth_rows  # noqa: E402


def test_robust_embed_uses_training_rows_only_and_clips():
    rows, X = synth_rows()
    pos = np.arange(0, 150)
    X2 = X.copy()
    X2[150:] *= 50.0  # changing non-training rows must not change the fitted map on training rows
    E1, E2 = M7.robust_embed(X, pos, kmax=4), M7.robust_embed(X2, pos, kmax=4)
    assert np.allclose(E1[pos], E2[pos], atol=1e-5)
    # an extreme outlier in a training row is clipped -> bounded effect
    X3 = X.copy()
    X3[0, 0] = 1e6
    E3 = M7.robust_embed(X3, pos, kmax=4)
    assert np.abs(E3).max() < 50


def test_mlp_gradient():
    rng = np.random.default_rng(0)
    Xs = rng.normal(size=(20, 5))
    I, J, W = np.arange(0, 6), np.arange(6, 12), rng.uniform(0.5, 1.5, 6)
    W1, b1, w2 = rng.normal(size=(5, 4)), rng.normal(size=4), rng.normal(size=4)
    loss, (gW1, gb1, gw2) = M7._pair_loss_grad(Xs, I, J, W, W1, b1, w2, 0.1)
    eps = 1e-6
    W1p = W1.copy()
    W1p[2, 1] += eps
    lp = M7._pair_loss_grad(Xs, I, J, W, W1p, b1, w2, 0.1)[0]
    assert abs((lp - loss) / eps - gW1[2, 1]) < 1e-4
    w2p = w2.copy()
    w2p[3] += eps
    lp = M7._pair_loss_grad(Xs, I, J, W, W1, b1, w2p, 0.1)[0]
    assert abs((lp - loss) / eps - gw2[3]) < 1e-4


def test_mlp_learns_step_signal_and_ignores_test_metadata():
    rows, X = synth_rows(n_fam=30, d=8)
    ctx = S6.model_ctx(rows)
    ctx["family"] = rows.family.astype(str)
    store = C5.EmbStore(memory={}, on_miss=lambda rep, pos: C5.compute_embedding(X, pos, kmax=8))
    n = len(rows)
    pos_tr, pos_te = np.arange(0, int(0.7 * n)), np.arange(int(0.7 * n), n)
    fp = M7.make_t7c(store, ctx, rep="r", k=8)({"hidden": 8, "wd": 0.01})
    s = fp(pos_tr, rows.y[pos_tr], pos_te)
    from experiments.risk_loop.argus_loop import iter04_common as C4
    w = C4.within_traj_auroc(s, rows.y[pos_te], rows.trajectory_id[pos_te])
    assert w["value"] > 0.7, w
    ctx2 = {k: np.asarray(v, dtype=object).copy() for k, v in ctx.items()}
    for k in ctx2:
        ctx2[k][pos_te] = "zzz"
    s2 = M7.make_t7c(store, ctx2, rep="r", k=8)({"hidden": 8, "wd": 0.01})(pos_tr, rows.y[pos_tr], pos_te)
    assert np.allclose(s, s2)


if __name__ == "__main__":
    k = 0
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            k += 1
            print("ok", name)
    print(k, "passed")

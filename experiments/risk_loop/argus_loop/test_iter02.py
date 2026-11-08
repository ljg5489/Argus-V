"""Unit tests for the iteration-2 models and features. py -3.11 test_iter02.py"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402
from experiments.risk_loop.argus_loop import iter02_common as C2  # noqa: E402
from experiments.risk_loop.argus_loop import models as M  # noqa: E402

NEW = ("tool_centred_logreg", "pairwise_rank", "tool_weighted_logreg")


def confounded(n_tools=30, per=40, d=20, seed=0):
    """Tool offsets on dim 1 correlate with the tool's violation rate (between-tool shortcut); the true
    within-tool signal is a small shift on dim 0."""
    rng = np.random.default_rng(seed)
    X, y, tool = [], [], []
    for t in range(n_tools):
        rate = rng.uniform(0.05, 0.5)
        yt = (rng.random(per) < rate).astype(int)
        yt[:2] = [0, 1]
        Xt = rng.normal(size=(per, d))
        Xt[:, 1] += 6.0 * rate + rng.normal(scale=0.2)  # tool-level shortcut
        Xt[:, 2:] += rng.normal(scale=2.0, size=d - 2)  # big tool offsets elsewhere
        Xt[:, 0] += 0.9 * yt
        X.append(Xt)
        y.append(yt)
        tool += [f"t{t}"] * per
    return np.vstack(X).astype(np.float32), np.concatenate(y), np.asarray(tool, dtype=object)


def ctx_of(tool, n):
    return {"source": np.asarray(["oct"] * n, dtype=object), "train_group": tool,
            "log_prefix_length": np.zeros(n), "step_index": np.zeros(n)}


def test_scores_do_not_read_test_tool():
    X, y, tool = confounded()
    n = len(y)
    tr, te = np.arange(0, n, 2), np.arange(1, n, 2)
    for name in NEW:
        ctx = ctx_of(tool.copy(), n)
        s1 = M.build(name, X, ctx, k=10, C=0.1)(tr, y[tr], te)
        tool2 = tool.copy()
        tool2[te] = "scrambled"  # changing the tool of test rows must not change their scores
        s2 = M.build(name, X, ctx_of(tool2, n), k=10, C=0.1)(tr, y[tr], te)
        assert np.allclose(s1, s2), name
        assert np.all(np.isfinite(s1)) and s1.shape == (len(te),)


def test_within_tool_signal_beats_shortcut():
    X, y, tool = confounded()
    n = len(y)
    tools = np.unique(tool)
    te_tools = set(tools[::3].tolist())  # unseen tools at test time, as in family-grouped CV
    te = np.nonzero(np.isin(tool, list(te_tools)))[0]
    tr = np.nonzero(~np.isin(tool, list(te_tools)))[0]
    res = {}
    for name in NEW + ("pca_logreg",):
        ctx = ctx_of(tool, n)
        s = M.build(name, X, ctx, k=20, C=0.1, weight="class") if name == "pca_logreg" else \
            M.build(name, X, ctx, k=20, C=0.1)(tr, y[tr], te)
        if name == "pca_logreg":
            s = s(tr, y[tr], te)
        res[name] = E.within_tool_auroc(s, y[te], tool[te])["value"]
    assert res["pairwise_rank"] > 0.65, res
    assert res["tool_centred_logreg"] > 0.65, res
    assert res["pairwise_rank"] >= res["pca_logreg"] - 0.02, res


def test_centring_invariance_of_within_tool_auroc():
    rng = np.random.default_rng(1)
    s = rng.normal(size=200)
    y = (rng.random(200) < 0.3).astype(int)
    tool = np.asarray([f"t{i % 5}" for i in range(200)], dtype=object)
    off = {f"t{i}": rng.normal() * 10 for i in range(5)}
    s2 = s + np.asarray([off[t] for t in tool])
    assert abs(E.within_tool_auroc(s, y, tool)["value"] - E.within_tool_auroc(s2, y, tool)["value"]) < 1e-12


def test_pairs_and_weights():
    y = np.array([1, 0, 0, 1, 0, 0, 0, 0])
    g = np.array(["a", "a", "a", "b", "b", "b", "c", "c"], dtype=object)
    I, J, W = M.same_group_pairs(y, g)
    assert len(I) == 2 + 2 and set(zip(I.tolist(), J.tolist())) == {(0, 1), (0, 2), (3, 4), (3, 5)}
    assert np.isclose(W.mean(), 1.0)
    w = M.informative_group_weights(y, g, None)
    assert np.isclose(w[y == 0].sum(), (y == 0).sum())
    assert np.isclose(w[[1, 2, 4, 5]].sum(), w[[6, 7]].sum())


def test_length_directions_remove_length():
    rng = np.random.default_rng(2)
    E_ = rng.normal(size=(500, 12))
    t = E_ @ rng.normal(size=12) + rng.normal(scale=0.1, size=500)
    Q = M.length_directions(E_, t, 1)
    R = M._project_out(E_, Q)
    from numpy.linalg import lstsq
    beta, *_ = lstsq(R, t - t.mean(), rcond=None)
    r2 = 1 - np.var(t - t.mean() - R @ beta) / np.var(t)
    assert Q.shape == (12, 1) and r2 < 0.05, r2


def test_trajectory_delta():
    X = np.arange(12, dtype=np.float32).reshape(6, 2)
    traj = np.array(["a", "a", "a", "b", "b", "a"])
    step = np.array([0, 1, 2, 0, 1, 2])
    D = C2.trajectory_delta(X, traj, step)
    assert np.allclose(D[0], 0) and np.allclose(D[3], 0)
    assert np.allclose(D[1], X[1] - X[0])
    assert np.allclose(D[2], X[2] - (X[0] + X[1]) / 2)
    assert np.allclose(D[5], X[5] - (X[0] + X[1]) / 2)  # same step as row 2: does not see row 2
    assert np.allclose(D[4], X[4] - X[3])


if __name__ == "__main__":
    for k, f in list(globals().items()):
        if k.startswith("test_"):
            f()
            print("ok", k)
    print("all iteration-2 tests passed")

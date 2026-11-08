"""Unit tests for iteration-4 code (T4-1 model, diagnostics helpers). py -3.11 test_iter04.py"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402
from experiments.risk_loop.argus_loop import iter04_common as C4  # noqa: E402
from experiments.risk_loop.argus_loop import iter04_models as M4  # noqa: E402
from experiments.risk_loop.argus_loop import models as M  # noqa: E402


def rollouts(n_traj=60, steps=6, d=16, seed=0):
    """Each trajectory has a 'risky rollout' offset on dim 1 (confound shared by all its steps, larger when
    the trajectory contains a violation); the violating step itself is shifted on dim 0."""
    rng = np.random.default_rng(seed)
    X, y, traj = [], [], []
    for t in range(n_traj):
        bad = t % 2 == 0
        Xt = rng.normal(size=(steps, d))
        Xt[:, 1] += 3.0 if bad else 0.0
        yt = np.zeros(steps, int)
        if bad:
            yt[rng.integers(steps)] = 1
        Xt[:, 0] += 1.5 * yt
        X.append(Xt)
        y.append(yt)
        traj += [f"T{t}"] * steps
    return np.vstack(X).astype(np.float32), np.concatenate(y), np.asarray(traj, dtype=object)


def test_pairs_only_same_trajectory_and_score_ignores_test_traj():
    X, y, traj = rollouts()
    n = len(y)
    tr, te = np.arange(0, n // 2), np.arange(n // 2, n)
    s1 = M.build("same_traj_pairwise", X, {"trajectory": traj.copy()}, k=8, C=1.0)(tr, y[tr], te)
    t2 = traj.copy()
    t2[te] = "scrambled"
    s2 = M.build("same_traj_pairwise", X, {"trajectory": t2}, k=8, C=1.0)(tr, y[tr], te)
    assert np.allclose(s1, s2) and s1.shape == (len(te),) and np.isfinite(s1).all()
    I, J, W = M.same_group_pairs(y[tr], traj[tr])
    assert len(I) and np.all(traj[tr][I] == traj[tr][J]) and np.all(y[tr][I] == 1) and np.all(y[tr][J] == 0)


def test_pair_model_ignores_rollout_confound():
    """Within-trajectory ranking should be high, and the pair model should load on dim 0, not dim 1."""
    X, y, traj = rollouts(n_traj=200)
    n = len(y)
    tr, te = np.arange(0, n // 2), np.arange(n // 2, n)
    s = M.build("same_traj_pairwise", X, {"trajectory": traj}, k=16, C=1.0)(tr, y[tr], te)
    wt = C4.within_traj_auroc(s, y[te], traj[te])
    assert wt["value"] > 0.8, wt
    # correlation with the confound dimension among negatives stays small
    neg = y[te] == 0
    assert abs(np.corrcoef(s[neg], X[te][neg, 1])[0, 1]) < 0.3


def test_no_pairs_gives_zero_scores():
    X, y, traj = rollouts()
    y = np.zeros_like(y)
    y[0] = 1
    traj = np.asarray([f"u{i}" for i in range(len(y))], dtype=object)  # every row its own trajectory
    s = M4.same_traj_pairwise(X, {"trajectory": traj}, k=4)(np.arange(50), y[:50], np.arange(50, 60))
    assert np.all(s == 0)


def test_within_traj_auroc_hand_example():
    s = np.array([3, 1, 2, 0, 5, 5], float)
    y = np.array([1, 0, 0, 0, 1, 0])
    tr = np.array(["a", "a", "a", "b", "c", "c"], dtype=object)
    r = C4.within_traj_auroc(s, y, tr)
    # traj a: AUROC 1 (1 pos); traj c: tie -> 0.5 (1 pos); b has no positive
    assert r["n_trajectories"] == 2 and abs(r["value"] - 0.75) < 1e-12 and r["n_pairs"] == 3
    assert abs(r["pair_value"] - (2 + 0.5) / 3) < 1e-12


def test_traj_positive_counts_excludes_self():
    tr = np.array(["a", "a", "b"], dtype=object)
    assert C4.traj_positive_counts(tr, np.array([1, 0, 0])).tolist() == [0, 1, 0]


def test_shuffle_replica_matches_harness():
    """shuffle_oofs reproduces evaluate.shuffle_test's within-tool values on synthetic rows."""
    rng = np.random.default_rng(3)
    recs = []
    for f in range(12):
        for t in range(3):
            for s in range(5):
                lab = int(rng.random() < 0.3)
                recs.append({"unit_id": f"u{f}_{t}", "trajectory_id": f"T{f}_{t}", "step_index": s,
                             "tool": f"tool{s % 2}", "label": lab, "label_status": "x",
                             "source": "oct" if f < 6 else "nov", "family": f"F{f}", "split": "train",
                             "report_content": 0, "n_obs": 3, "prefix_length": 100 + s})
    rows = E.Rows.from_records(recs)
    X = rng.normal(size=(len(rows), 5)) + rows.label[:, None] * 0.5

    def fp(a, ya, b):
        from sklearn.linear_model import LogisticRegression
        if len(np.unique(ya)) < 2:
            return np.zeros(len(b))
        return LogisticRegression().fit(X[a], ya).decision_function(X[b])

    ref = E.shuffle_test(fp, rows, 3, within=("source", "family"), n_jobs=1)
    oofs = C4.shuffle_oofs(fp, rows, 3, ("source", "family"))
    mine = [E.within_tool_auroc(o, rows.y, E.headline_groups(rows))["value"] for o in oofs]
    assert np.allclose(mine, ref["within_tool"]), (mine, ref["within_tool"])


if __name__ == "__main__":
    for k, v in list(globals().items()):
        if k.startswith("test_"):
            v()
            print("ok", k)

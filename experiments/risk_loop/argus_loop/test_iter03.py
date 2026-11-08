"""Unit tests for iteration-3 code (synthetic data only). py -3.11 test_iter03.py"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402
from experiments.risk_loop.argus_loop import iter03_common as C3  # noqa: E402
from experiments.risk_loop.argus_loop import iter03_models as M3  # noqa: E402
from experiments.risk_loop.argus_loop import models as M  # noqa: E402


def synth(n_fam=12, per_head=60, per_rep=10, d=16, seed=0):
    """Headline rows then report rows; each family has its own trajectories; signal on dim 0 shared."""
    rng = np.random.default_rng(seed)
    recs, X, yh, ye = [], [], [], []
    for track, per in ((0, per_head), (1, per_rep)):
        for f in range(n_fam):
            for i in range(per):
                y = int(rng.random() < (0.15 if track == 0 else 0.4))
                if track == 0 and i < 2:
                    y = i
                x = rng.normal(size=d)
                x[0] += 1.2 * y
                x[3] += f * 0.3
                X.append(x)
                recs.append({"unit_id": f"u{f}_{i % 5}", "trajectory_id": f"t{f}_{i % 5}",
                             "step_index": i // 5 + (100 if track else 0), "tool": f"tool{f % 4}" if track == 0
                             else "submit_result", "label": y, "label_status": "x",
                             "source": "oct" if f % 2 else "nov", "family": f"F{f}", "split": "train",
                             "report_content": 0, "n_obs": 1, "prefix_length": 10})
                (yh if track == 0 else ye).append(y)
    rows = E.Rows.from_records(recs)
    n_head = n_fam * per_head
    ctx = {"comp": E.group_components(rows), "family": rows.family.astype(str), "source": rows.source.astype(str),
           "train_group": np.asarray([f"{t}|{s}" for t, s in zip(rows.tool, rows.source)], dtype=object),
           "track": (np.arange(len(rows)) >= n_head).astype(int),
           "y_extra": np.r_[np.full(n_head, np.nan), np.asarray(ye, float)], "n_head": n_head}
    return np.asarray(X, np.float32), rows, ctx, n_head


def split(rows, n_head, test_fams=("F0", "F1", "F2")):
    fam = rows.family[:n_head]
    te = np.nonzero(np.isin(fam, test_fams))[0]
    tr = np.nonzero(~np.isin(fam, test_fams))[0]
    return tr, te


def test_zero_weight_equals_h21c():
    X, rows, ctx, n = synth()
    tr, te = split(rows, n)
    y = rows.y[:n]
    a = M3.expand_factory(X, ctx, k=8, C=0.1, w=0.0)(tr, y[tr], te)
    b = M3.expand_factory(X, ctx, k=8, C=0.1, extra_mode="none")(tr, y[tr], te)
    ctx2 = {"source": ctx["source"], "train_group": ctx["train_group"]}
    c = M.build("tool_weighted_logreg", X, ctx2, k=8, C=0.1)(tr, y[tr], te)
    assert np.allclose(a, c, atol=1e-6) and np.allclose(b, c, atol=1e-6)


def test_extras_never_from_test_families():
    X, rows, ctx, n = synth()
    tr, te = split(rows, n)
    ext = M3.allowed_extras(ctx, tr, te)
    assert len(ext) > 0 and (ext >= n).all()
    assert not set(rows.family[ext].tolist()) & {"F0", "F1", "F2"}
    # inner-CV style call: outer-test families are in neither argument -> their report rows are excluded too
    tr_in, te_in = tr[rows.family[tr] != "F3"], tr[rows.family[tr] == "F3"]
    ext2 = M3.allowed_extras(ctx, tr_in, te_in)
    assert not set(rows.family[ext2].tolist()) & {"F0", "F1", "F2", "F3"}


def test_scores_ignore_test_side_info():
    X, rows, ctx, n = synth()
    tr, te = split(rows, n)
    y = rows.y[:n]
    s1 = M3.expand_factory(X, ctx, k=8, C=0.1, w=1.0)(tr, y[tr], te)
    ctx2 = dict(ctx)
    for key in ("source", "train_group"):
        v = np.asarray(ctx[key]).copy().astype(object)
        v[te] = "scrambled"
        ctx2[key] = v
    s2 = M3.expand_factory(X, ctx2, k=8, C=0.1, w=1.0)(tr, y[tr], te)
    assert np.allclose(s1, s2)
    for mt in ("action", "shared"):
        s = M3.expand_factory(X, ctx, k=8, C=0.1, w=1.0, multitask=mt)(tr, y[tr], te)
        assert np.all(np.isfinite(s)) and s.shape == (len(te),)


def test_expansion_helps_when_signal_is_shared():
    X, rows, ctx, n = synth(per_head=25, per_rep=40, seed=3)
    tr, te = split(rows, n, tuple(f"F{i}" for i in range(6)))
    y = rows.y[:n]
    s0 = M3.expand_factory(X, ctx, k=8, C=0.1, extra_mode="none")(tr, y[tr], te)
    s1 = M3.expand_factory(X, ctx, k=8, C=0.1, w=1.0)(tr, y[tr], te)
    from sklearn.metrics import roc_auc_score
    assert roc_auc_score(y[te], s1) >= roc_auc_score(y[te], s0) - 0.02


def test_null_permutes_extras_per_repeat():
    X, rows, ctx, n = synth()
    tr, te = split(rows, n)
    y = rows.y[:n]
    ext = M3.allowed_extras(ctx, tr, te)
    ya, yb = y[tr].copy(), y[tr].copy()
    yb[[0, 1]] = yb[[1, 0]] if yb[0] != yb[1] else yb[[0, 1]]
    yb = np.random.default_rng(1).permutation(yb)
    s_real = M3.expand_factory(X, ctx, k=8, C=0.1, w=1.0)(tr, ya, te)
    s_null_a = M3.expand_factory(X, ctx, k=8, C=0.1, w=1.0, null_within=("source",))(tr, ya, te)
    s_null_b = M3.expand_factory(X, ctx, k=8, C=0.1, w=1.0, null_within=("source",))(tr, yb, te)
    assert not np.allclose(s_real, s_null_a)
    assert len(ext) > 0 and np.all(np.isfinite(s_null_b))
    s_null_a2 = M3.expand_factory(X, ctx, k=8, C=0.1, w=1.0, null_within=("source",))(tr, ya, te)
    assert np.allclose(s_null_a, s_null_a2)  # deterministic


def test_prev_index_only_earlier():
    recs = []
    for t, steps in (("a", [0, 1, 2, 2, 5]), ("b", [3, 1])):
        for s in steps:
            recs.append({"unit_id": t, "trajectory_id": t, "step_index": s, "tool": "x", "label": 0,
                         "label_status": "x", "source": "oct", "family": "f", "split": "train",
                         "report_content": 0, "n_obs": 1, "prefix_length": 1})
    rows = E.Rows.from_records(recs)
    p = C3.prev_index(rows)
    assert p.tolist()[:5] == [-1, 0, 1, 1, 3] or p.tolist()[:5] == [-1, 0, 1, 1, 2]
    assert p[4] in (2, 3) and p[5] == 6 and p[6] == -1
    st = rows.step_index
    for i, j in enumerate(p):
        if j >= 0:
            assert st[j] < st[i] and rows.trajectory_id[j] == rows.trajectory_id[i]


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            print("ok", name)

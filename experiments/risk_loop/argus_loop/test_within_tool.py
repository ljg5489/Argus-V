"""Tests for within_tool.py ("같은 도구 안 학습") on SYNTHETIC data only. Single-threaded.

  py -3.11 experiments/risk_loop/argus_loop/test_within_tool.py [name-substring ...]
"""
from __future__ import annotations

import shutil
import sys
import tempfile
import time
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT))
import torch  # noqa: E402

torch.set_num_threads(1)
from experiments.risk_loop import harness as H  # noqa: E402
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402
from experiments.risk_loop.argus_loop import obs_models as OM  # noqa: E402
from experiments.risk_loop.argus_loop import obs_models_s0f as OMS0F  # noqa: E402
from experiments.risk_loop.argus_loop import obs_synth as S  # noqa: E402
from experiments.risk_loop.argus_loop import within_tool as W  # noqa: E402

_TMP = Path(tempfile.mkdtemp(prefix="within_tool_tests_"))
_SYN = {}


def syn():
    if not _SYN:
        root = _TMP / "syn"
        _SYN["info"] = S.make_synthetic(root, n_fam=20, seed=5, signal=4.0)
        _SYN["data"] = OM.ObsData.load(root, root / "obs_cache", layers=(20,), with_extras=False)
        _SYN["root"] = root
    return _SYN["data"], _SYN["root"]


def fold0(data, seed=0):
    a, b = E.make_folds(data.head, 5, seed)[0]
    return a, data.head.y[a], b


def wt_auroc(s, y, cells):
    return E.within_tool_auroc(s, y, cells)["value"]


# ------------------------------------------------------------------------------------------------ toy data

def offset_toy(seed=0, K=12, n=80, dim=6):
    """Per-cell offset along e1 strongly predicts violations ACROSS cells (cell mean of e1 ~ cell violation rate),
    but inside a cell violations are shifted along e2 (true signal) and slightly DOWN along e1 (reversed)."""
    rng = np.random.default_rng(seed)
    X, y, cells, traj = [], [], [], []
    for c in range(K):
        rate = 0.04 + 0.5 * c / (K - 1)
        yc = (rng.random(n) < rate).astype(int)
        yc[:2] = [1, 0]
        x = rng.normal(size=(n, dim))
        x[:, 0] += 20.0 * rate
        x[yc == 1, 1] += 0.5
        x[yc == 1, 0] -= 1.5
        X.append(x)
        y.append(yc)
        cells += [f"t{c}|oct"] * n
        traj += [f"r{c}_{i % 8}" for i in range(n)]
    return np.vstack(X), np.concatenate(y), np.asarray(cells, dtype=object), np.asarray(traj)


# ------------------------------------------------------------------------------------------------ tests

def test_pairs_within_cell_only():
    y = np.array([1, 0, 0, 1, 0, 1, 1])
    cells = np.array(["a", "a", "a", "b", "b", "c", "a"])
    traj = np.array(["r1", "r1", "r2", "r3", "r3", "r4", "r9"])
    I, J, w = W.within_cell_pairs(y, cells, traj)
    assert np.all(cells[I] == cells[J]) and np.all(y[I] == 1) and np.all(y[J] == 0)
    assert len(I) == 2 * 2 + 1           # cell a: 2 violations x 2 normals, cell b: 1 x 1, cell c: none
    assert abs(w.mean() - 1) < 1e-12
    raw = {(i, j): v for i, j, v in zip(I, J, w)}
    assert abs(raw[(0, 1)] / raw[(0, 2)] - 2.0) < 1e-12   # same rollout x2
    assert W.usable_violations(y, cells) == 3            # cell c has no normal


def test_fit_lin_equals_s0_objective():
    rng = np.random.default_rng(1)
    X = rng.normal(size=(200, 5))
    y = (X[:, 0] + rng.normal(size=200) > 1).astype(int)
    wb = OM.class_balanced(y)
    traj = np.repeat(np.arange(40), 5).astype(str)
    I, J, pw = OM.pair_index(y, traj, traj, np.full(200, "x"), {"T5": 0, "T6": 0})
    w1, b1, _ = OMS0F.fit_logistic_pair(X, y, wb, I, J, pw, 0.1, 200, 0.2, 1.0)
    w2, b2, _ = W.fit_lin(X, y, wb, I, J, pw, 0.1 * 200 / 0.2, 0.2, 1.0)
    assert np.allclose(w1, w2, atol=1e-6) and abs(b1 - b2) < 1e-6


def test_pair_bce_zero_equals_sklearn_pairs():
    X, y, cells, traj = offset_toy(2)
    I, J, w = W.within_cell_pairs(y, cells, traj)
    a = W.sk_pair_fit(X, I, J, w, 0.1)
    b = W.pair_bce_fit(X, I, J, w, 0.1, X, y, np.ones(len(y)), bce=0.0)
    assert np.allclose(a, b, atol=2e-3), (a, b)   # sklearn lbfgs stops at tol 1e-4


def test_w1_linear_uncentred_scoring_exact():
    """W1, linear: scoring the UNCENTRED features gives exactly the within-cell AUROC of the centred features."""
    X, y, cells, traj = offset_toy(3)
    tr = np.arange(len(y)) % 3 != 0
    te = ~tr
    Xc, _, _ = W.cell_center(X[tr], cells[tr])
    w, b, _ = W.fit_lin(Xc, y[tr], OM.class_balanced(y[tr]), np.zeros(0, int), np.zeros(0, int), np.zeros(0),
                        10.0, 0.2, 0.0)
    s_unc = X[te] @ w + b
    Xte_c, _, _ = W.cell_center(X[te], cells[te])
    s_cen = Xte_c @ w + b
    for c in np.unique(cells[te]):
        m = cells[te] == c
        if 0 < y[te][m].sum() < m.sum():
            assert H.auroc(s_unc[m], y[te][m]) == H.auroc(s_cen[m], y[te][m])
    assert wt_auroc(s_unc, y[te], cells[te]) == wt_auroc(s_cen, y[te], cells[te])


def test_offset_toy_plain_fails_w_recovers():
    """Cell offset predictive across cells, true within-cell signal on another direction: the plain model
    fails, W1 / W2 / W3 recover the true direction (linear S-0 objective and the T7-a member recipes)."""
    from experiments.risk_loop.argus_loop import iter06_models as M6
    X, y, cells, traj = offset_toy(0)
    Xt, yt, ct, rt = offset_toy(7)                  # fresh data from the same generator
    wb = OM.class_balanced(y)
    a = 1.0 * len(y) / 0.2
    e0 = np.zeros(0, int)
    w_plain, _, _ = W.fit_lin(X, y, wb, e0, e0, np.zeros(0), a, 0.2, 0.0)
    Xc, _, _ = W.cell_center(X, cells)
    w_w1, _, _ = W.fit_lin(Xc, y, wb, e0, e0, np.zeros(0), a, 0.2, 0.0)
    I, J, pw = W.within_cell_pairs(y, cells, traj)
    w_w2, _, _ = W.fit_lin(X, y, wb, I, J, pw, a, 0.0, 1.0)
    w_w3, _, _ = W.fit_lin(Xc, y, wb, I, J, pw, a, 0.1, 1.0)
    true = np.zeros(X.shape[1])
    true[1], true[0] = 0.5, -1.5
    true /= np.linalg.norm(true)
    res = {}
    for k, w in {"plain": w_plain, "w1": w_w1, "w2": w_w2, "w3": w_w3,
                 "m_plain": M6.pointwise_informative_fit(X, y, np.full(len(y), "oct"), cells, 0.1),
                 "m_w1": M6.pointwise_informative_fit(Xc, y, np.full(len(y), "oct"), cells, 0.1),
                 "m_w2": W.sk_pair_fit(X, I, J, pw, 0.1),
                 "m_w3": W.pair_bce_fit(X, I, J, pw, 0.1, Xc, y, wb)}.items():
        res[k] = (wt_auroc(Xt @ w, yt, ct), float(w @ true / np.linalg.norm(w)))
    print("   ", {k: (round(v[0], 3), round(v[1], 3)) for k, v in res.items()})
    for k in ("plain", "m_plain"):
        assert res[k][0] < 0.65, (k, res[k])
    for k in ("w1", "w2", "w3", "m_w1", "m_w2", "m_w3"):
        plain = res["m_plain" if k.startswith("m_") else "plain"]
        assert res[k][0] > 0.80 and res[k][0] - plain[0] >= 0.15 and res[k][1] > 0.9 and res[k][1] > plain[1],             (k, res[k], plain)


def test_lin_none_equals_fit_s0():
    data, _ = syn()
    a, ya, b = fold0(data)
    for pre in (False, True):
        cfg = W.lin_config(0.1, pre)
        s_ref = OMS0F.fit_s0(data, cfg, a, ya, b).score
        s = W.lin_fit(data, cfg, a, ya, b, "none")
        assert np.allclose(s, s_ref, atol=1e-6), np.abs(s - s_ref).max()


def test_cnn_none_equals_fit_sf():
    data, _ = syn()
    a, ya, b = fold0(data)
    for pre in (False, True):
        cfg = W.cnn_config(1e-2, pre, epochs=8)
        s_ref = OMS0F.fit_sf(data, cfg, a, ya, b, threads=1).score
        s = W.cnn_fit(data, cfg, a, ya, b, "none", threads=1)
        assert np.allclose(s, s_ref, atol=1e-6), np.abs(s - s_ref).max()


def test_cnn_methods_run_and_differ():
    data, _ = syn()
    a, ya, b = fold0(data)
    out = {m: W.cnn_fit(data, W.cnn_config(1e-2, False, epochs=8), a, ya, b, m, threads=1) for m in W.METHODS}
    for m, s in out.items():
        assert np.all(np.isfinite(s)) and len(s) == len(b)
    assert not np.allclose(out["none"], out["w2"])


def test_t7a_none_equals_component_scores():
    from experiments.risk_loop.argus_loop import iter01_common as C1
    from experiments.risk_loop.argus_loop import iter11_diag_models as DM
    _, root = syn()
    d, rows, _ = C1.headline_data(root)
    feats = DM.load_feats(d, rows, ["L23:max", "L16:pre", "L23:pre"])
    a, b = E.make_folds(rows, 5, 0)[0]
    ref = DM.make_t7a({k: feats[k] for k in ("L23:max", "L16:pre")}, rows)[0](a, rows.y[a], b)
    t = W.T7aW(feats, rows)
    s = t.fit(a, rows.y[a], b, "none")
    assert np.allclose(s, ref, atol=1e-12)
    for m in W.W_METHODS:
        for pre in (False, True):
            s = t.fit(a, rows.y[a], b, m, pre)
            assert np.all(np.isfinite(s)) and len(s) == len(b)


def _bases():
    from experiments.risk_loop.argus_loop import iter01_common as C1
    from experiments.risk_loop.argus_loop import iter11_diag_models as DM
    data, root = syn()
    memo = W.Memo(_TMP / "memo")
    d, rows, _ = C1.headline_data(root)
    assert np.array_equal(rows.row_id, data.head.row_id)
    feats = DM.load_feats(d, rows, ["L23:max", "L16:pre", "L23:pre"])
    t7 = W.Base("t7a", rows, memo, W.T7aW(feats, rows), [None], 1)
    lin = W.Base("lin", data.head, memo, None, W.LIN_GRID, 1, data)
    cnn = W.Base("cnn", data.head, memo, None, W.CNN_GRID, 1, data)
    return t7, lin, cnn


def test_metadata_invariance_all_bases_methods():
    """The tool name (and source / family / rollout / status) of SCORED rows never reaches scoring."""
    import experiments.risk_loop.argus_loop.obs_models_s as OMS
    t7, lin, cnn = _bases()
    old = OMS.STRUCTS["S-F"].get("epochs")
    OMS.STRUCTS["S-F"]["epochs"] = 8
    try:
        for b in (t7, lin, cnn):
            for m in W.METHODS:
                for pre in (False, True):
                    r = b.probe(m, pre)
                    assert r["ok"], (b.name, m, pre, r)
    finally:
        if old is None:
            OMS.STRUCTS["S-F"].pop("epochs")
        else:
            OMS.STRUCTS["S-F"]["epochs"] = old


def test_centring_uses_inner_training_rows_only():
    """During nested selection every centring uses exactly the rows the fit trains on (inner-training rows for
    inner fits), never their scored rows nor the outer test rows."""
    _, lin, _ = _bases()
    calls = set()
    W.CENTER_LOG.clear()
    mk = lin.make("w1")

    def mk2(t):
        f = mk(t)

        def fp(pa, ya, pb):
            calls.add((OM.h_arr(np.sort(np.asarray(pa, np.int64))), OM.h_arr(np.sort(np.asarray(pb, np.int64)))))
            return f(pa, ya, pb)
        return fp
    lin.memo = W.Memo(_TMP / "memo_center")        # fresh memo: every fit computes
    E.nested_cv(mk2, lin.grid, None, lin.rows, (0,), 5, inner_splits=W.INNER)
    assert len(W.CENTER_LOG) == 5 * (W.INNER * len(lin.grid) + 1)    # one centring per computed fit
    for used, pa, pb in W.CENTER_LOG:
        assert used == pa and (pa, pb) in calls
    folds = E.make_folds(lin.rows, 5, 0)
    outer = {OM.h_arr(np.sort(np.asarray(a, np.int64))) for a, _ in folds}
    inner = [c for c in calls if c[0] not in outer]
    assert len(inner) == 5 * W.INNER
    tests = [np.sort(np.asarray(b, np.int64)) for _, b in folds]
    for used, pa, pb in W.CENTER_LOG:   # inner centring never touches the outer test rows of its outer fold
        if pa not in outer:
            assert not any(OM.h_arr(t) == pb for t in tests)


def test_inputs_variants():
    data, _ = syn()
    a, ya, b = fold0(data)
    p_plain = W.prep_inp(data, W.lin_config(0.1, True, "plain"), a, ya, b, "plain")
    e = data.embed(20, a, 32)
    assert np.array_equal(p_plain["Ztr"], e.Z[p_plain["sq_tr"].idx])
    assert W.lin_config(0.1, True, "robust_noclip")["robust_clip"] == W.NOCLIP
    s = {i: W.lin_fit(data, W.lin_config(0.1, True, i), a, ya, b, "none", i) for i in W.INPUTS}
    assert not np.allclose(s["plain"], s["robust_clip"])


def test_center_audit_catches_wrong_rows():
    try:
        W.center_audit(np.array([1, 2, 99]), np.array([1, 2, 3]), np.array([99]))
    except RuntimeError:
        W.AUDIT.pop("centring_rows_are_training_rows:FAIL")
    else:
        raise AssertionError("center_audit accepted rows outside the training set")
    Xc, mus, used = W.cell_center(np.ones((3, 2)), ["a", "a", "b"], [10, 11, 12])
    assert sorted(used.tolist()) == [10, 11, 12]


def test_cnn_probe_bypasses_s_store():
    calls = []
    orig = W.s_store_score
    W.s_store_score = lambda *a: calls.append(1) or None
    try:
        _, _, cnn = _bases()
        import experiments.risk_loop.argus_loop.obs_models_s as OMS
        OMS.STRUCTS["S-F"]["epochs"] = 4
        cnn.probe("none")
    finally:
        W.s_store_score = orig
        OMS.STRUCTS["S-F"].pop("epochs", None)
    assert not calls


def test_no_audit_failures():
    assert not [k for k in W.AUDIT if k.endswith(":FAIL")], dict(W.AUDIT)


TESTS = [v for k, v in list(globals().items()) if k.startswith("test_")]


if __name__ == "__main__":
    sel = sys.argv[1:]
    n_ok = 0
    t00 = time.time()
    try:
        for t in TESTS:
            if sel and not any(s in t.__name__ for s in sel):
                continue
            t0 = time.time()
            t()
            n_ok += 1
            print(f"ok   {t.__name__} ({time.time() - t0:.1f}s)", flush=True)
    finally:
        shutil.rmtree(_TMP, ignore_errors=True)
    print(f"{n_ok} passed in {time.time() - t00:.0f}s; audit {dict(W.AUDIT)}")

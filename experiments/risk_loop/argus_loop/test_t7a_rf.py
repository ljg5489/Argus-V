"""Tests for t7a_rf.py (iteration 15, RF as a 4th T7-a member) on SYNTHETIC data only. Small, single-threaded.

  py -3.11 -m pytest -q experiments/risk_loop/argus_loop/test_t7a_rf.py      (if pytest is installed)
  py -3.11 experiments/risk_loop/argus_loop/test_t7a_rf.py [name-substring ...]   (no pytest needed)
"""
from __future__ import annotations

import contextlib
import json
import sys
import tempfile
import time
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402
from experiments.risk_loop.argus_loop import obs_models as OM  # noqa: E402
from experiments.risk_loop.argus_loop import obs_synth as S  # noqa: E402
from experiments.risk_loop.argus_loop import t7a_rf as T  # noqa: E402
from experiments.risk_loop.argus_loop import within_tool as W  # noqa: E402

SMALL = {"n_estimators": 25, "max_features": "sqrt", "class_weight": None, "random_state": 0, "n_jobs": 1,
         "bootstrap": True}
_TMP = Path(tempfile.mkdtemp(prefix="t7a_rf_tests_"))
_SYN = {}


def syn():
    """(rows, feats) of a small synthetic headline view (same generator as test_within_tool)."""
    if not _SYN:
        from experiments.risk_loop.argus_loop import iter01_common as C1
        from experiments.risk_loop.argus_loop import iter11_diag_models as DM
        root = _TMP / "syn"
        S.make_synthetic(root, n_fam=16, seed=5, signal=4.0)
        d, rows, _ = C1.headline_data(root)
        _SYN["rows"] = rows
        _SYN["feats"] = DM.load_feats(d, rows, ["L23:max", "L16:pre", "L23:pre"])
    return _SYN["rows"], _SYN["feats"]


def model(params=None):
    rows, feats = syn()
    return T.RFT7a(feats, rows, dict(SMALL if params is None else params))


def fold0(rows, seed=0):
    a, b = E.make_folds(rows, 5, seed)[0]
    return a, rows.y[a], b


# ------------------------------------------------------------------------------------------------ RF pieces

def test_oob_reference_equals_sklearn_oob():
    from sklearn.ensemble import RandomForestClassifier
    rng = np.random.default_rng(0)
    X = rng.normal(size=(300, 6)).astype(np.float32)
    y = (X[:, 0] + rng.normal(size=300) > 1.2).astype(int)
    sw = rng.uniform(0.5, 3, 300)
    p = dict(SMALL, n_estimators=40)
    rf = RandomForestClassifier(min_samples_leaf=5, oob_score=True, **p).fit(X, y, sample_weight=sw)
    ref, nfb = T.oob_reference(rf, X)
    assert nfb == 0
    assert np.allclose(ref, rf.oob_decision_function_[:, 1], atol=1e-12)
    rf2 = T.fit_rf(X, y, sw, 5, p)                     # same forest without oob_score
    assert np.array_equal(T.rf_proba(rf2, X), rf.predict_proba(X)[:, 1])


def test_member1_weights_match_iter06():
    from experiments.risk_loop.argus_loop import models as M
    y = np.array([1, 0, 0, 0, 1, 0, 0, 0])
    src = np.array(["oct"] * 4 + ["nov"] * 4)
    cells = np.array(["a|oct", "a|oct", "b|oct", "b|oct", "c|nov", "c|nov", "d|nov", "d|nov"])
    w = T.member1_weights(y, src, cells)
    ref = M.informative_group_weights(y, cells, M.sample_weights(y, src, "source_class"))
    assert np.array_equal(w, ref)


def test_rf_features_shape_and_training_rows_only():
    m = model()
    a, ya, b = fold0(m.rows)
    X = m.rf_features(a)
    assert X.shape == (len(m.rows), 42) and X.dtype == np.float32
    from experiments.risk_loop.argus_loop import iter07_models as M7
    ref = np.hstack([M7.robust_embed(m.store.features["L23:max"], a)[:, :32],
                     M7.robust_embed(m.store.features["L16:pre"], a)[:, :10]])
    assert np.array_equal(X, ref.astype(np.float32))
    Xp = m.rf_features(a, pre_only=True)
    assert np.array_equal(Xp[:, :32], M7.robust_embed(m.store.features["L23:pre"], a)[:, :32])


# ------------------------------------------------------------------------------------------------ equivalences

def test_r1_with_rf_weight_zero_equals_t7a_exactly():
    from experiments.risk_loop.argus_loop import iter11_diag_models as DM
    m = model()
    a, ya, b = fold0(m.rows)
    t = m.t7a(a, ya, b)
    r = m.rf_member(a, ya, b, 5)
    assert np.array_equal(T.combine(t, r, 0.0), t)
    assert np.array_equal(T.combine(t, r, 1.0), r)
    ref = DM.make_t7a({k: m.store.features[k] for k in ("L23:max", "L16:pre")}, m.rows)[0](a, ya, b)
    assert np.allclose(t, ref, atol=1e-12)          # T7-a part == iteration-12/14 T7-a
    r1 = T.combine(t, r, 0.25)
    assert np.allclose(r1, (3 * t + r) / 4, atol=1e-12)  # equal weight over 4 members


def test_runner_tries_compose_members():
    m = model()
    run = T.Runner(m, W.Memo(_TMP / "memo_compose"), grid=(5,))
    a, ya, b = fold0(m.rows)
    r0 = run.compute("R0", False, 5, a, ya, b)
    r1 = run.compute("R1", False, 5, a, ya, b)
    r2 = run.compute("R2", False, 5, a, ya, b)
    t = m.t7a(a, ya, b)
    assert np.array_equal(r0, m.rf_member(a, ya, b, 5))
    assert np.array_equal(r1, T.combine(t, r0, 0.25))
    assert np.array_equal(r2, T.combine(t, m.rf_member(a, ya, b, 5, "w1"), 0.25))
    assert not np.array_equal(r1, r2)
    assert np.all((r0 >= 0) & (r0 <= 1))


# ------------------------------------------------------------------------------------------------ leakage

def test_percentile_reference_is_training_rows_only():
    """The percentile map uses the (in-sample) scores of exactly the training rows, uncentred; scored rows never
    influence each other's score (scoring a subset gives the same values)."""
    assert T.REF_MODE == "insample"
    m = model()
    a, ya, b = fold0(m.rows)
    seen = []
    orig = T.reference_scores

    def spy(rf, Xref):
        seen.append(np.asarray(Xref).copy())
        return orig(rf, Xref)
    T.reference_scores = spy
    try:
        full = m.rf_member(a, ya, b, 5)
        half = m.rf_member(a, ya, b[: len(b) // 2], 5)
        w1 = m.rf_member(a, ya, b, 5, "w1")
    finally:
        T.reference_scores = orig
    assert len(seen) == 3
    X = m.rf_features(a)
    for Xref in seen:                                   # plain and w1: uncentred training rows, nothing else
        assert np.array_equal(Xref, X[a])
    assert np.array_equal(full[: len(b) // 2], half)
    # manual recomputation of the map
    from experiments.risk_loop.argus_loop import iter06_models as M6
    src = np.asarray(m.ctx["source"]).astype(str)[a]
    cells = np.asarray(m.ctx["train_group"]).astype(str)[a]
    rf = T.fit_rf(X[a], ya, T.member1_weights(ya, src, cells), 5, m.params)
    ref = T.rf_proba(rf, X[a])
    assert np.array_equal(full, M6.train_percentile(ref, T.rf_proba(rf, X[b])))
    assert not np.array_equal(full, w1)


def test_centring_uses_training_rows_only_nested():
    """R2: every centring (outer and inner fits of nested selection) uses exactly that fit's training rows and
    none of its scored rows."""
    m = model()
    run = T.Runner(m, W.Memo(_TMP / "memo_center"), grid=(5, 10))
    W.CENTER_LOG.clear()
    calls = set()
    mk = run.make("R2")

    def mk2(g):
        f = mk(g)

        def fp(pa, ya, pb):
            calls.add((OM.h_arr(np.sort(np.asarray(pa, np.int64))), OM.h_arr(np.sort(np.asarray(pb, np.int64)))))
            return f(pa, ya, pb)
        return fp
    E.nested_cv(mk2, run.grid, None, run.rows, (0,), 5, inner_splits=W.INNER)
    assert len(W.CENTER_LOG) == 5 * (W.INNER * 2 + 1)       # one centring per computed RF fit
    for used, pa, pb in W.CENTER_LOG:
        assert used == pa and (pa, pb) in calls
    assert W.AUDIT.get("centring_rows_are_training_rows:FAIL", 0) == 0


def test_scores_invariant_to_scored_rows_metadata():
    m = model()
    run = T.Runner(m, W.Memo(_TMP / "memo_probe"), grid=(5,))
    for t in T.TRIES:
        for pre in (False, True):
            r = run.probe(t, pre)
            assert r["ok"] and r["max_abs_diff"] == 0.0, (t, pre, r)


def test_determinism():
    a_m, b_m = model(), model(dict(SMALL, n_jobs=2))
    a, ya, b = fold0(a_m.rows)
    for var in ("plain", "w1"):
        s1 = a_m.rf_member(a, ya, b, 10, var)
        s2 = a_m.rf_member(a, ya, b, 10, var)
        s3 = b_m.rf_member(a, ya, b, 10, var)            # 2 fitting threads: same forest, same scores
        assert np.array_equal(s1, s2) and np.array_equal(s1, s3)


def test_shuffled_labels_change_scores():
    m = model()
    a, ya, b = fold0(m.rows)
    rng = np.random.default_rng(1)
    s = m.rf_member(a, ya, b, 5)
    s_sh = m.rf_member(a, rng.permutation(ya), b, 5)
    assert not np.array_equal(s, s_sh)


# ------------------------------------------------------------------------------------------------ run / gates

class _Patch:
    """Minimal stand-in for pytest's monkeypatch (setattr + undo)."""

    def __init__(self):
        self.undo = []

    def setattr(self, obj, name, value):
        self.undo.append((obj, name, getattr(obj, name)))
        setattr(obj, name, value)

    def restore(self):
        for obj, name, v in reversed(self.undo):
            setattr(obj, name, v)


@contextlib.contextmanager
def _exits(code):
    try:
        yield
    except SystemExit as e:
        assert e.code == code, e.code
    else:
        raise AssertionError("expected SystemExit")


def _with_patch(fn):
    def wrapper(monkeypatch=None):
        if monkeypatch is not None:
            return fn(monkeypatch)
        p = _Patch()
        try:
            return fn(p)
        finally:
            p.restore()
    wrapper.__name__ = fn.__name__
    return wrapper


@_with_patch
def test_prereg_frozen_check(monkeypatch):
    d = _TMP / "prereg"
    d.mkdir(exist_ok=True)
    p, ps = d / "prereg-rf.md", d / "prereg-rf.sha256"
    monkeypatch.setattr(T, "PREREG", p)
    monkeypatch.setattr(T, "PREREG_SHA", ps)
    p.write_text("# 사전 등록 DRAFT\nbody\n", encoding="utf-8")
    assert not T.prereg_frozen()[0]                    # no sha file
    ps.write_text(f"{T.sha256(p)} *prereg-rf.md\n", encoding="utf-8")
    assert not T.prereg_frozen()[0]                    # still DRAFT
    p.write_text("# 사전 등록 고정본\nbody\n", encoding="utf-8")
    assert not T.prereg_frozen()[0]                    # sha mismatch
    ps.write_text(f"{T.sha256(p)} *prereg-rf.md\n", encoding="utf-8")
    assert T.prereg_frozen()[0]
    p.write_text("# changed\n", encoding="utf-8")
    with _exits(3):
        T.main(["check"])
    with _exits(3):
        T.start_checks()


@_with_patch
def test_run_all_smoke_and_report(monkeypatch):
    """End-to-end on synthetic data with reduced counts (1 fold seed, 2 shuffles, grid of 2); resumable."""
    monkeypatch.setattr(T, "SEEDS3", (0,))
    monkeypatch.setattr(T, "N_SHUF", 2)
    monkeypatch.setattr(W, "paired_gain", _pg)
    saved_out = T.OUT
    try:
        m = model()
        out = _TMP / "run"
        memo = W.Memo(out)
        nobs = np.asarray(m.rows.n_obs, np.float64)
        T.run_all(list(T.TRIES), 1, model=m, memo=memo, nobs32=nobs, out=out, grid=(5, 10))
        miss1 = memo.miss
        T.run_all(list(T.TRIES), 1, model=m, memo=memo, nobs32=nobs, out=out, grid=(5, 10))   # resume: no refits
        assert memo.miss == miss1
        for t in T.TRIES:
            r = json.loads((out / f"result_{t}.json").read_text(encoding="utf-8"))
            assert r["probe"]["all"]["ok"] and r["probe"]["pre"]["ok"]
            assert "shuffle_b" in r and "pre_only" in r and "rules" in r
            assert r["luck_corrected"]["n_tries"] == 172 and r["luck_corrected_conservative"]["n_tries"] == 174
            assert not [k for k in r["audit"] if k.endswith(":FAIL")]
        ref = json.loads((out / "result_T7A.json").read_text(encoding="utf-8"))
        assert 0 <= ref["value"] <= 1
        rd = _TMP / "rep"
        T.cmd_report(out, rd)
        assert (rd / "rf_results.md").is_file() and (rd / "rf_results.json").is_file()
    finally:
        T.OUT = saved_out


_ORIG_PG = W.paired_gain


def _pg(a, b, r):
    return _ORIG_PG(a, b, r, reps=50)


def test_no_audit_failures():
    assert not [k for k in W.AUDIT if k.endswith(":FAIL")], dict(W.AUDIT)


TESTS = [v for k, v in list(globals().items()) if k.startswith("test_")]


if __name__ == "__main__":
    sel = sys.argv[1:]
    n_ok = n_fail = 0
    for t in TESTS:
        if sel and not any(s in t.__name__ for s in sel):
            continue
        t0 = time.time()
        try:
            t()
            n_ok += 1
            print(f"PASS {t.__name__} ({time.time() - t0:.1f}s)", flush=True)
        except Exception as e:  # noqa: BLE001
            n_fail += 1
            import traceback
            traceback.print_exc()
            print(f"FAIL {t.__name__}: {e!r}", flush=True)
    print(f"{n_ok} passed, {n_fail} failed")
    sys.exit(1 if n_fail else 0)

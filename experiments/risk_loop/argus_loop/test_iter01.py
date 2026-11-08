"""Unit tests for iter01_common + models on a small fake feature cache. py -3.11 test_iter01.py"""
from __future__ import annotations

import csv
import sys
import tempfile
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402
from experiments.risk_loop.argus_loop import iter01_common as C  # noqa: E402
from experiments.risk_loop.argus_loop import models as M  # noqa: E402

COLS = ["row", "unit_id", "trajectory_id", "step_index", "tool", "label", "label_status", "source", "family",
        "split", "report_content", "n_obs", "prefix_length", "has_rend"]


def fake_root(tmp: Path, n=600, d=16, seed=0):
    rng = np.random.default_rng(seed)
    recs, X = [], rng.normal(size=(n, d)).astype(np.float32)
    tools = ["alpha", "beta", "gamma", "submit_result", "write_report"]
    for i in range(n):
        src = "oct" if i % 3 == 0 else "nov"
        fam = f"F{(i // 6) % 12}"
        tool = tools[i % 5]
        y = int(rng.random() < 0.2)
        if y and tool != "submit_result":
            X[i, 0] += 2.5  # within-tool signal on dim 0
        rc = int(src == "oct" and tool in ("submit_result", "write_report") and y == 1)
        split = "test" if i % 50 == 49 else "train"
        recs.append({"row": i, "unit_id": f"u{i // 6}", "trajectory_id": f"t{i // 6}", "step_index": i % 6,
                     "tool": tool, "label": y, "label_status": "x", "source": src, "family": fam, "split": split,
                     "report_content": rc, "n_obs": 3, "prefix_length": 100 + i, "has_rend": int(i != 5)})
    with open(tmp / "steps.csv", "w", newline="", encoding="utf-8") as h:
        w = csv.DictWriter(h, COLS)
        w.writeheader()
        w.writerows(recs)
    incomplete = {7, 8}
    with open(tmp / "row_status.csv", "w", newline="", encoding="utf-8") as h:
        w = csv.DictWriter(h, ["row", "in_shared_rowgroup", "features_complete"])
        w.writeheader()
        w.writerows([{"row": i, "in_shared_rowgroup": 0, "features_complete": int(i not in incomplete)}
                     for i in range(n)])
    for p in C.POOLS:
        A = X.astype(np.float16).copy()
        A[list(incomplete)] = np.nan
        if p == "rend":
            A[5] = np.nan
        np.save(tmp / f"L16_{p}.npy", A)
    return recs


def test_filters_and_features():
    if True:  # mmap keeps files open on Windows, so the temp dir is not removed
        tmp = Path(tempfile.mkdtemp(prefix="iter01_test_"))
        recs = fake_root(tmp)
        data = E.load(tmp)
        rows, info = C.headline_filter(data.rows, C.read_row_status(tmp))
        assert not set(rows.tool.tolist()) & C.REPORT_TOOLS
        assert 7 not in rows.row_id.tolist() and 8 not in rows.row_id.tolist()
        assert info["dropped_incomplete_rows"] == sum(1 for r in recs if r["row"] in (7, 8)
                                                      and r["tool"] not in C.REPORT_TOOLS and r["split"] == "train")
        assert set(rows.split.tolist()) == {"train"}
        X = C.features(data, rows, 16, "rend")  # row 5 rend NaN -> filled with pre
        assert np.isfinite(X).all()
        i5 = rows.row_id.tolist().index(5)
        assert np.allclose(X[i5], data.features(16, "pre", rows.subset([i5]))[0])
        # report track: report tools only, including October report-content positives
        d2 = E.load(tmp, include_report_content=True)
        rr, _ = C.report_filter(d2.rows, C.read_row_status(tmp))
        assert set(rr.tool.tolist()) <= C.REPORT_TOOLS and (rr.report_content == 1).any()
        return data, rows, X


def test_weights():
    y = np.array([0, 0, 0, 1, 0, 1])
    src = np.array(["a", "a", "a", "a", "b", "b"])
    w = M.sample_weights(y, src, "source_class")
    for s in "ab":
        for c in (0, 1):
            m = (src == s) & (y == c)
            assert np.isclose(w[m].sum(), len(y) / 4)
    wc = M.sample_weights(y, None, "class")
    assert np.isclose(wc[y == 1].sum(), wc[y == 0].sum())


def test_model_signal_and_no_test_fit():
    data, rows, X = test_filters_and_features()
    ctx = C.ctx_for(rows)
    grid = [{"k": 4, "C": 0.1}, {"k": 8, "C": 1.0}]
    for name, fixed in [("pca_logreg", {"weight": "source_class", "kmax": 8}),
                        ("pca_logreg", {"weight": "class", "kmax": 8, "resid": True}),
                        ("pca_logreg_per_source_scale", {"weight": "source_class", "kmax": 8})]:
        make = M.grid_maker(name, X, ctx, fixed)
        cv = E.nested_cv(make, grid, None, rows, seeds=(0,))
        m = E.metrics(cv, rows, bootstrap=0, baselines=False)
        assert m["within_tool"]["value"] > 0.7, (name, m["within_tool"]["value"])
    # test rows must not influence the fit: perturbing test-row features leaves train-derived embedding unchanged
    pos_tr, pos_te = np.arange(0, 300), np.arange(300, len(rows))
    E1 = M.pca_embed(X, pos_tr, 4, ctx=ctx)
    X2 = X.copy()
    X2[pos_te] += 100.0
    E2 = M.pca_embed(X2, pos_tr, 4, ctx=ctx)
    assert np.allclose(E1[pos_tr], E2[pos_tr], atol=1e-4)
    # shuffle within source -> near chance
    make = M.grid_maker("pca_logreg", X, ctx, {"weight": "source_class", "kmax": 8})
    sh = E.shuffle_test(make({"k": 8, "C": 1.0}), rows, 3, X_or_rowids=None)
    assert abs(sh["within_tool_mean"] - 0.5) < 0.15, sh["within_tool_mean"]
    assert M.REGISTRY["pca_logreg_per_source_scale"].diagnostic


def test_select_rule():
    from experiments.risk_loop.argus_loop import iter01_scan as S
    mk = lambda i, v, k=128, resid=False, diag=False: {  # noqa: E731
        "spec": {"id": i, "grid": [{"k": k, "C": 1}], "fixed": {"resid": resid}, "diagnostic": diag},
        "summary": {"within_tool": v}}
    rs = [mk("a", 0.70), mk("b", 0.697, k=10), mk("c", 0.80, diag=True), mk("d", 0.60)]
    sel = S.select(rs, 3)
    assert [r["spec"]["id"] for r in sel] == ["b", "a", "d"]


if __name__ == "__main__":
    test_weights()
    test_filters_and_features()
    test_model_signal_and_no_test_fit()
    test_select_rule()
    print("all iter01 tests passed")

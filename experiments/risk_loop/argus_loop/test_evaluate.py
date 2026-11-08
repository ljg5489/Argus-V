"""Self-test of the frozen loop evaluation module on synthetic data (no real data touched).

Runs with pytest or directly: ``py -3.11 experiments/risk_loop/argus_loop/test_evaluate.py``.
"""
from __future__ import annotations

import csv
import json
import sys
import tempfile
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402

TOOLS = ["read_file", "write_file", "bash", "http", "submit", "search"]
TOOL_RATE = {"read_file": 0.01, "write_file": 0.08, "bash": 0.25, "http": 0.15, "submit": 0.40, "search": 0.03}


def synth(n_fam: int = 60, traj_per_fam: int = 3, steps: int = 12, seed: int = 0, split: str = "train",
          pos_per_family: int | None = None):
    """Rows with tool-dependent base rates. ``pos_per_family``: instead, exactly k positives per family at
    random rows (equal family base rates, so within-family shuffling leaves no family-level label signal)."""
    rng = np.random.default_rng(seed)
    recs = []
    for f in range(n_fam):
        src = "oct" if f % 2 == 0 else "nov"
        for t in range(traj_per_fam):
            for s in range(steps):
                tool = TOOLS[rng.integers(0, len(TOOLS))]
                y = int(rng.random() < TOOL_RATE[tool])
                recs.append({"unit_id": f"U{f}-{t}", "trajectory_id": f"T{f}-{t}", "step_index": s, "tool": tool,
                             "label": y, "label_status": "rule", "source": src, "family": f"F{f}", "split": split,
                             "report_content": 0, "n_obs": int(rng.integers(1, 6)),
                             "prefix_length": int(500 + 300 * s + rng.integers(0, 200))})
    if pos_per_family is not None:
        per = traj_per_fam * steps
        for f in range(n_fam):
            block = recs[f * per:(f + 1) * per]
            for r in block:
                r["label"] = 0
            for i in rng.choice(per, pos_per_family, replace=False):
                block[i]["label"] = 1
    return E.Rows.from_records(recs)


def logreg(Xa, ya, Xb):
    return E._logreg_fp(Xa, ya, Xb)


def tool_onehot(rows):
    return np.stack([(rows.tool == t).astype(float) for t in TOOLS], 1)


# (a) tool-identity signal: pooled high, within-tool ~0.5
def test_tool_identity_signal_is_not_rewarded():
    rows = synth()
    X = tool_onehot(rows) + np.random.default_rng(1).normal(0, 0.01, (len(rows), len(TOOLS)))
    cv = E.run_cv(logreg, X, rows, seeds=(0,), n_splits=5)
    m = E.metrics(cv, rows, bootstrap=100, baselines=True)
    assert m["pooled_auroc"] > 0.75, m["pooled_auroc"]
    # fold-agnostic pooling can only push a tool-rate model below 0.5 (leave-fold-out offsets), never above
    assert 0.40 < m["within_tool"]["value"] <= 0.52, m["within_tool"]["value"]
    assert abs(m["within_tool"]["fold_cell_reference"] - 0.5) < 0.03
    ti = m["baselines"]["tool_identity"]
    assert ti["pooled_auroc"] > 0.75
    assert ti["within_tool"] <= 0.52 and ti["within_tool_fold_cell_reference"] == 0.5, ti
    assert m["baselines"]["tool_identity_shortcut_proof"]
    assert abs(m["baselines"]["length+step"]["within_tool"] - 0.5) < 0.08


# (b) real within-tool signal
def test_real_within_tool_signal_detected():
    rows = synth()
    rng = np.random.default_rng(2)
    X = np.c_[rows.y * 1.5 + rng.normal(0, 1, len(rows)), rng.normal(0, 1, (len(rows), 3))]
    cv = E.run_cv(logreg, X, rows, seeds=(0, 1, 2))
    m = E.metrics(cv, rows, bootstrap=200)
    wt = m["within_tool"]
    assert wt["value"] > 0.8, wt["value"]
    assert all(v > 0.78 for v in wt["per_seed"])
    assert wt["ci95"]["ci_low"] < wt["value"] < wt["ci95"]["ci_high"]
    assert wt["by_source"]["oct"]["value"] > 0.75 and wt["by_source"]["nov"]["value"] > 0.75
    assert wt["n_tools"] >= 4 and wt["n_positives_included"] <= wt["n_positives_total"]
    st = E.seed_stability(m)
    assert st["min"] <= wt["value"] <= st["max"]


# (c) shuffle within (source x family) in training folds -> ~0.5
def test_shuffle_gives_chance():
    rows = synth(n_fam=80, pos_per_family=4)
    rng = np.random.default_rng(3)
    X = np.c_[rows.y * 1.5 + rng.normal(0, 1, len(rows)), tool_onehot(rows)]
    sh = E.shuffle_test(logreg, rows, n=3, X_or_rowids=X)
    assert abs(sh["within_tool_mean"] - 0.5) < 0.06, sh
    assert len(sh["within_tool"]) == 3


def test_shuffle_known_property_family_rates():
    """Documented property (HARNESS.md): with unequal family positive rates, a model with real label signal
    stays above 0.5 under the gate's (source x family) shuffle, because family rates are preserved."""
    rows = synth(n_fam=80)
    rng = np.random.default_rng(3)
    X = np.c_[rows.y * 1.5 + rng.normal(0, 1, len(rows)), rng.normal(0, 1, (len(rows), 2))]
    sf = E.shuffle_test(logreg, rows, n=3, X_or_rowids=X, within=("source", "family"))
    assert sf["within_tool_mean"] > 0.6, sf
    noise = E.shuffle_test(logreg, rows, n=3, X_or_rowids=rng.normal(0, 1, (len(rows), 3)))
    assert abs(noise["within_tool_mean"] - 0.5) < 0.05, noise


def _gate_for(X, rows):
    cv = E.run_cv(logreg, X, rows, seeds=(0,))
    m = E.metrics(cv, rows, bootstrap=0, baselines=False)
    res = {"metrics": m, "cv": cv,
           "shuffle_source": E.shuffle_test(logreg, rows, 3, X_or_rowids=X, within=("source",)),
           "shuffle_source_family": E.shuffle_test(logreg, rows, 3, X_or_rowids=X, within=("source", "family"))}
    return E.success_gate(res), res


# condition 3 v2: real signal with uneven family rates passes (a) and (b); a family-rate-only model fails (b)
def test_condition3_v2_signal_vs_family_rate():
    rows = synth(n_fam=80)  # uneven family positive rates
    rng = np.random.default_rng(0)
    X = np.c_[rows.y * 2.5 + rng.normal(0, 1, len(rows)), rng.normal(0, 1, (len(rows), 20))]
    g, res = _gate_for(X, rows)
    c = g["conditions"]
    assert res["shuffle_source_family"]["within_tool_mean"] > 0.55  # v1 null is not ~0.5 here
    assert c["3a_source_shuffle_within_tool_0.5_pm_0.05"], res["shuffle_source"]
    assert c["3b_headline_minus_source_family_shuffle_ge_0.10"], g["shuffle_family_margin"]

    rate = {f: rows.y[rows.family == f].mean() for f in set(rows.family.tolist())}
    Xf = np.c_[[rate[f] for f in rows.family.tolist()]] + rng.normal(0, 1e-3, (len(rows), 1))
    g2, res2 = _gate_for(Xf, rows)
    assert res2["metrics"]["within_tool"]["value"] > 0.55  # family rate does help within tool
    assert not g2["conditions"]["3b_headline_minus_source_family_shuffle_ge_0.10"], g2["shuffle_family_margin"]
    assert g2["shuffle_family_margin"] < 0.05


def _write_cache(root: Path):
    rows = []
    for split, nf in (("train", 6), ("validation", 3), ("test", 2), ("sealed", 2)):
        for f in range(nf):
            for s in range(5):
                rows.append({"unit_id": f"{split}{f}", "trajectory_id": f"{split}{f}", "step_index": s,
                             "tool": TOOLS[s % 3], "label": int(s == 4), "label_status": "rule",
                             "source": "oct" if f % 2 else "nov", "family": f"{split}-F{f}", "split": split,
                             "report_content": int(split == "train" and f == 0 and s == 4),
                             "n_obs": 2, "prefix_length": 100 * (s + 1)})
    rows[1]["label"] = ""  # one null label in train
    with open(root / "steps.csv", "w", newline="", encoding="utf-8") as h:
        w = csv.DictWriter(h, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    np.save(root / "L16_max.npy", np.arange(len(rows) * 2, dtype=np.float32).reshape(len(rows), 2))
    return rows


def _raises(exc, fn, *a, **k):
    try:
        fn(*a, **k)
    except exc:
        return True
    raise AssertionError(f"{fn.__name__} did not raise {exc.__name__}")


# (d) test/sealed rows refused
def test_loader_refuses_sealed_rows():
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as d:  # Windows: mmap keeps the .npy open
        root = Path(d)
        allrows = _write_cache(root)
        data = E.load(root)
        assert set(data.rows.split.tolist()) == {"train"}
        assert len(data.rows) == 30 - 2  # one report_content + one null label removed
        assert data.rows.info["excluded_report_content"] == 1 and data.rows.info["excluded_null_label"] == 1
        X = data.features(16, "max")
        assert X.shape == (len(data.rows), 2)
        assert np.array_equal(X[:, 0], data.rows.row_id * 2)
        test_ids = [i for i, r in enumerate(allrows) if r["split"] in ("test", "sealed")]
        val_ids = [i for i, r in enumerate(allrows) if r["split"] == "validation"]
        _raises(PermissionError, data.features_for, test_ids[:3], 16, "max")
        _raises(PermissionError, data.features_for, val_ids[:3], 16, "max")
        _raises(PermissionError, E.load, root, split="test")
        _raises(PermissionError, E.load, root, split="sealed")
        _raises(PermissionError, E.load, root, split="validation")
        v = E.load(root, validation_look=True)
        assert set(v.rows.split.tolist()) == {"train", "validation"}
        v.features_for(val_ids[:3], 16, "max")
        _raises(PermissionError, v.features_for, test_ids[:1], 16, "max")
        _raises(PermissionError, E.run_cv, logreg, None, v.rows)  # CV is train-only
        inc = E.load(root, include_report_content=True, include_null=True)
        assert len(inc.rows) == 30
        # rows built by hand with a test split are refused by every CV entry point
        bad = synth(n_fam=6, steps=4)
        bad.split[:] = "test"
        _raises(PermissionError, E.run_cv, logreg, None, bad)
        _raises(PermissionError, E.shuffle_test, logreg, bad)
        _raises(PermissionError, E.nested_cv, lambda c: logreg, [1], None, bad)
        del data, v, inc


# (e) folds never split a family or trajectory; every fold has positives
def test_folds_respect_groups():
    rows = synth()
    # one trajectory crossing two families: both families must land in the same fold
    m = rows.trajectory_id == "T1-0"
    rows.trajectory_id[np.nonzero(rows.trajectory_id == "T2-0")[0]] = "T1-0"
    fold_sets = []
    for seed in (0, 1, 2):
        folds = E.make_folds(rows, 5, seed)
        fid = E._fold_id(folds, len(rows))
        assert (fid >= 0).all()
        for col in (rows.family, rows.trajectory_id, rows.unit_id):
            for g in set(col.tolist()):
                assert len(set(fid[col == g].tolist())) == 1, (g, seed)
        assert fid[rows.family == "F1"][0] == fid[rows.family == "F2"][0]
        for a, b in folds:
            assert rows.y[b].sum() > 0 and len(np.intersect1d(a, b)) == 0
        fold_sets.append(fid)
    assert not np.array_equal(fold_sets[0], fold_sets[1])  # seeds give different assignments
    assert m.any()


def test_fit_predict_sees_training_fold_only_and_determinism():
    rows = synth(n_fam=30)
    seen = []

    def spy(ia, ya, ib):
        assert len(np.intersect1d(ia, ib)) == 0
        seen.append((len(ia), len(ib)))
        return np.zeros(len(ib))

    E.run_cv(spy, None, rows, seeds=(0,))
    assert sum(b for _, b in seen) == len(rows)
    X = np.c_[rows.y + np.random.default_rng(0).normal(0, 1, len(rows))]
    r1 = E.evaluate(logreg, X, rows, seeds=(0, 1, 2), bootstrap=50, n_shuffle=1, name="t")
    r2 = E.evaluate(logreg, X, rows, seeds=(0, 1, 2), bootstrap=50, n_shuffle=1, name="t")
    assert json.dumps(r1, sort_keys=True) == json.dumps(r2, sort_keys=True)
    assert r1["gate"]["conditions"]["4_hyperparameters_by_nested_cv"] is False


def test_nested_cv_and_gate():
    rows = synth(n_fam=40, pos_per_family=6)
    rng = np.random.default_rng(5)
    # 1 signal + 20 noise dims: with very few dims the source-shuffle null swings by the sign of a random
    # weight (HARNESS.md "알려진 성질"), which is not what this wiring test is about
    X = np.c_[rows.y * 3.0 + rng.normal(0, 1, len(rows)), rng.normal(0, 1, (len(rows), 20))]

    def make(c):
        from sklearn.linear_model import LogisticRegression

        def fp(Xa, ya, Xb):
            return LogisticRegression(C=c, max_iter=2000).fit(Xa, ya).decision_function(Xb)
        return fp

    res = E.evaluate(make_fit_predict=make, grid=[0.01, 1.0], X_or_rowids=X, rows=rows, bootstrap=200,
                     n_shuffle=3, name="nested")
    g = res["gate"]
    assert res["cv"]["selection"]["method"] == "nested_cv"
    assert len(res["cv"]["selection"]["chosen"]["0"]) == 5
    assert g["conditions"]["4_hyperparameters_by_nested_cv"] is True
    assert g["conditions"]["1_within_tool_ge_0.90_and_every_seed_ge_0.88"], res["metrics"]["within_tool"]
    assert g["conditions"]["3a_source_shuffle_within_tool_0.5_pm_0.05"], res["shuffle_source"]
    assert g["conditions"]["3b_headline_minus_source_family_shuffle_ge_0.10"], g["shuffle_family_margin"]
    assert g["gate_version"] == "v4"
    assert g["verdict"] in ("PENDING_MONITOR_AUDIT", "FAIL")
    assert E.success_gate(res, monitor_pass=False)["verdict"] == "FAIL"
    if g["verdict"] == "PENDING_MONITOR_AUDIT":
        assert E.success_gate(res, monitor_pass=True)["verdict"] == "PASS"
    json.dumps(res)


def test_validation_metrics_requires_look():
    tr = synth(n_fam=20, seed=1)
    va = synth(n_fam=10, seed=2, split="validation")
    rows = E.Rows(**{k: np.concatenate([getattr(tr, k), getattr(va, k)]) for k in E.Rows.__dataclass_fields__
                     if k != "info"})
    X = np.c_[rows.y + np.random.default_rng(0).normal(0, 0.5, len(rows))]
    out = E.validation_metrics(logreg, X, rows, bootstrap=50)
    assert out["rows"]["n"] == len(va) and out["within_tool"]["value"] > 0.7
    rows.split[:3] = "sealed"
    _raises(PermissionError, E.validation_metrics, logreg, X, rows)


# (v3) pure source signal inside a tool: positives only in oct, negatives mostly nov, score = source.
# v2 (tool-only grouping) is inflated; v3 (tool x source cells) stays at chance.
def test_v3_source_signal_inside_tool_not_rewarded():
    rows = synth(n_fam=60, seed=5)
    rng = np.random.default_rng(6)
    y = np.zeros(len(rows), int)
    oct_ = rows.source == "oct"
    for t in TOOLS:
        idx = np.nonzero((rows.tool == t) & oct_)[0]
        y[rng.choice(idx, max(3, len(idx) // 5), replace=False)] = 1
    rows = E.Rows.from_records([{**{k: (v.item() if hasattr(v, "item") else v) for k, v in r.items()},
                                 "label": int(yy)} for r, yy in zip(_records(rows), y)])
    score = oct_.astype(float) + rng.normal(0, 0.05, len(rows))
    m = E.metrics(score, rows, bootstrap=50, baselines=False)
    wt = m["within_tool"]
    assert wt["v2_tool_only_reference"]["value"] > 0.75, wt["v2_tool_only_reference"]
    assert abs(wt["value"] - 0.5) < 0.08, wt["value"]
    assert wt["grouping"] == "tool_x_source"
    assert wt["ci95"]["ci_high"] < 0.75


# (v4) gate shuffles default to 20 runs; mean/SD/SE reported; threads do not change results
def test_v4_shuffle_20_runs_deterministic():
    import inspect
    assert inspect.signature(E.shuffle_test).parameters["n"].default == 20
    assert inspect.signature(E.evaluate).parameters["n_shuffle"].default == 20
    rows = synth(n_fam=30, pos_per_family=3)
    X = np.random.default_rng(7).normal(0, 1, (len(rows), 3))
    a = E.shuffle_test(logreg, rows, X_or_rowids=X, n_jobs=1)
    b = E.shuffle_test(logreg, rows, X_or_rowids=X, n_jobs=2)
    assert len(a["within_tool"]) == 20 and a["n"] == 20
    assert a["within_tool"] == b["within_tool"]
    v = np.asarray(a["within_tool"], float)
    assert abs(a["within_tool_sd"] - v.std(ddof=1)) < 1e-12
    assert abs(a["within_tool_se"] - v.std(ddof=1) / np.sqrt(20)) < 1e-12
    assert abs(a["within_tool_mean"] - 0.5) < 0.05


def _records(rows):
    cols = ["unit_id", "trajectory_id", "step_index", "tool", "label_status", "source", "family", "split",
            "report_content", "n_obs", "prefix_length"]
    return [{c: getattr(rows, c)[i] for c in cols} for i in range(len(rows))]


if __name__ == "__main__":
    fails = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                print("PASS", name)
            except Exception as exc:  # noqa: BLE001
                fails += 1
                print("FAIL", name, type(exc).__name__, exc)
    print("failures:", fails)
    sys.exit(1 if fails else 0)

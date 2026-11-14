"""Iteration 16 freeze (2026-11-15, approved by the user): fit the existing best model ONCE on all judged train
rows with the v2 labels and freeze the files before the new rollouts exist. Nothing is selected and the old
judging cells are not cross-validated here, so the try ledger stays at 169.

  F1  "T7-a"       recipe unchanged (final_models.fit_final): L23 max + L16 pre-action -> median/IQR scaling,
                   clip 3 -> PCA 32 (L16: first 10) -> 3 linear members -> mean of training percentiles.
  F2  "T7-a+RF"    F1 plus a random forest as 4th member (weight 1/4): 42 features = L23:max PCA 32 + L16:pre
                   PCA 10 of the SAME frozen preprocessing, 500 trees, min_samples_leaf 10 (fixed, no inner
                   selection), member-1 row weights, in-sample training scores as the percentile reference
                   (iter-15/prereg-rf.md sections 2.1-2.4; the fixed leaf size and the single full-train fit are
                   the addendum written in iter-16/prereg-new-data.md).

Train split only (evaluate.load refuses anything else). evaluate.py (v4) is imported, never modified.
Usage: py -3.11 experiments/risk_loop/argus_loop/freeze_models.py
"""
from __future__ import annotations

import hashlib
import json
import os
import pickle
import platform
import sys
import time
from pathlib import Path

for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ.setdefault(_v, "2")

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402
from experiments.risk_loop.argus_loop import final_models as FM  # noqa: E402
from experiments.risk_loop.argus_loop import iter01_common as C1  # noqa: E402
from experiments.risk_loop.argus_loop import iter06_models as M6  # noqa: E402
from experiments.risk_loop.argus_loop import iter06_scan as S6  # noqa: E402
from experiments.risk_loop.argus_loop import iter07_models as M7  # noqa: E402
from experiments.risk_loop.argus_loop import iter09_models as M9  # noqa: E402
from experiments.risk_loop.argus_loop import t7a_rf as RF  # noqa: E402

SHA = FM.SHA
ART = REPO_ROOT / "artifacts" / "risk-loop" / "argus-v1-loop"
V2 = ART / "features_labels_v2"
TAG = "2026-11-15"
OUT = ART / "frozen" / TAG
REPORT = REPO_ROOT / "reports" / "risk-loop" / "argus-v1" / "loop" / "iter-16" / "frozen"
FORMAT_RF = "argus-loop-frozen-t7a-rf/1"
RF_MSL = 10
RF_WEIGHT = 0.25
CODE_FILES = ("freeze_models.py", "final_models.py", "t7a_rf.py", "within_tool.py", "iter04_models.py",
              "iter06_models.py", "iter07_models.py", "iter09_models.py", "models.py", "evaluate.py",
              "iter01_common.py")


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def rf_features(t7a_model: dict, feature_rows: dict) -> np.ndarray:
    """[n, 42] float32 from the frozen T7-a preprocessing (no refit)."""
    cols = [FM.embed(t7a_model["preproc"][rep], feature_rows[rep])[:, :k] for rep, k in RF.RF_REPS]
    return np.hstack(cols).astype(np.float32)


def score_rf(model: dict, feature_rows: dict) -> np.ndarray:
    """Risk score in [0, 1] of the frozen T7-a + RF model; needs only {"L23:max", "L16:pre"} feature rows."""
    if model.get("format") != FORMAT_RF:
        raise ValueError("unknown model format")
    s7 = FM.score(model["t7a"], feature_rows)
    p = RF.rf_proba(model["rf"], rf_features(model["t7a"], feature_rows))
    pct = M6.train_percentile(model["rf_train_scores_sorted"], p)
    return RF.combine(s7, pct, model["rf_weight"])


def main():
    assert E.evaluate_sha256() == SHA, E.evaluate_sha256()
    ok, why = RF.prereg_frozen()
    assert ok, f"iter-15 prereg-rf not frozen: {why}"
    data, rows, rinfo = C1.headline_data(V2)
    assert set(rows.split.astype(str).tolist()) == {"train"}, "train split only"
    reps = ["L16:pre", "L23:max"]
    feats = {r: np.asarray(C1.features(data, rows, int(r.split(":")[0].lstrip("L")), r.split(":")[1]), dtype=np.float32)
             for r in reps}
    y = rows.y.astype(np.int64)
    traj, tool, source = rows.trajectory_id.astype(str), rows.tool.astype(str), rows.source.astype(str)
    cells = np.asarray([f"{t}|{s}" for t, s in zip(tool, source)], dtype=object)
    rid_hash = hashlib.sha1(np.asarray(rows.row_id, dtype=np.int64).tobytes()).hexdigest()
    groups = E.headline_groups(rows)
    idx = np.linspace(0, len(rows) - 1, 25).astype(int)
    OUT.mkdir(parents=True, exist_ok=True)
    REPORT.mkdir(parents=True, exist_ok=True)
    info = {"rows": "headline_filter train rows (report tools and incomplete-feature rows dropped)",
            "row_id_sha1": rid_hash, "labels": "labels v2 (features_labels_v2/steps.csv)", "rows_info": rinfo,
            "fitted_at": time.strftime("%Y-%m-%d %H:%M"), "purpose": "frozen before the new rollouts (iter-16)"}
    res = {"tag": TAG, "evaluate_sha256": SHA, "n_rows": int(len(rows)), "n_positives": int(y.sum()),
           "row_id_sha1": rid_hash, "label_status": rows.summary()["label_status"], "models": {}}

    # ---- F1: T7-a
    t0 = time.time()
    m1 = FM.fit_final("T7-a", feats, y, traj, tool, source, info)
    s1 = FM.score(m1, feats)
    members, weights = FM.FINAL["T7-a"]
    ref = M9.make_weighted(M7.RobustStore(feats), S6.model_ctx(rows), members, weights)({})(
        np.arange(len(rows)), y, np.arange(len(rows)))
    diff = float(np.max(np.abs(s1 - ref)))
    m1["check_rows"] = {"row_id": [int(rows.row_id[i]) for i in idx], "score": [float(s1[i]) for i in idx]}
    m1["in_sample"] = {"max_abs_diff_vs_cv_pipeline": diff,
                       "within_tool_auroc_in_sample": E.within_tool_auroc(s1, y, groups)["value"]}
    p1 = OUT / "T7-a.v2" / "model.pkl"
    FM.save(m1, p1)
    back = FM.load(p1)
    assert np.allclose(FM.score(back, {r: feats[r][idx] for r in reps}), s1[idx], atol=1e-12), "reload mismatch F1"
    res["models"]["T7-a"] = {"path": str(p1.relative_to(REPO_ROOT)).replace("\\", "/"), "bytes": p1.stat().st_size,
                             "sha256": sha256(p1), "seconds": round(time.time() - t0, 1),
                             "max_abs_diff_vs_cv_pipeline": diff,
                             "in_sample_within_tool_auroc": m1["in_sample"]["within_tool_auroc_in_sample"],
                             "check_rows": m1["check_rows"]}
    print("F1 T7-a", json.dumps({k: v for k, v in res["models"]["T7-a"].items() if k != "check_rows"}), flush=True)

    # ---- F2: T7-a + RF (4th member, weight 1/4)
    t0 = time.time()
    X42 = rf_features(m1, feats)
    sw = RF.member1_weights(y, source, cells)
    rf = RF.fit_rf(X42, y, sw, RF_MSL, RF.RF_PARAMS)
    p_tr = RF.rf_proba(rf, X42)
    m2 = {"format": FORMAT_RF, "id": "T7-a+RF", "status": "frozen comparison model, NOT adopted",
          "t7a": m1, "rf": rf, "rf_train_scores_sorted": np.sort(p_tr), "rf_weight": RF_WEIGHT,
          "rf_spec": {"features": [list(x) for x in RF.RF_REPS], "min_samples_leaf": RF_MSL, "params": RF.RF_PARAMS,
                      "weights": "T7-a member-1 row weights (source x class, informative cells)",
                      "reference": "in-sample training scores"}, "info": info}
    s2 = score_rf(m2, feats)
    m2["check_rows"] = {"row_id": [int(rows.row_id[i]) for i in idx], "score": [float(s2[i]) for i in idx]}
    m2["in_sample"] = {"within_tool_auroc_in_sample": E.within_tool_auroc(s2, y, groups)["value"],
                       "rf_alone_within_tool_auroc_in_sample": E.within_tool_auroc(p_tr, y, groups)["value"]}
    p2 = OUT / "T7-a+RF.v2" / "model.pkl"
    p2.parent.mkdir(parents=True, exist_ok=True)
    with open(p2, "wb") as h:
        pickle.dump(m2, h, protocol=4)
    with open(p2, "rb") as h:
        back2 = pickle.load(h)
    assert np.allclose(score_rf(back2, {r: feats[r][idx] for r in reps}), s2[idx], atol=1e-12), "reload mismatch F2"
    res["models"]["T7-a+RF"] = {"path": str(p2.relative_to(REPO_ROOT)).replace("\\", "/"), "bytes": p2.stat().st_size,
                                "sha256": sha256(p2), "seconds": round(time.time() - t0, 1),
                                "in_sample_within_tool_auroc": m2["in_sample"]["within_tool_auroc_in_sample"],
                                "rf_alone_in_sample_within_tool_auroc": m2["in_sample"][
                                    "rf_alone_within_tool_auroc_in_sample"],
                                "rank_corr_with_T7-a_in_sample": E._spearman(s1, s2),
                                "check_rows": m2["check_rows"]}
    print("F2 T7-a+RF", json.dumps({k: v for k, v in res["models"]["T7-a+RF"].items() if k != "check_rows"}), flush=True)

    # ---- provenance
    import sklearn
    feat_manifest = json.loads((ART / "features" / "manifest.json").read_text(encoding="utf-8"))
    res["inputs"] = {
        "label_view": str(V2.relative_to(REPO_ROOT)).replace("\\", "/"),
        "steps_csv_sha256": sha256(V2 / "steps.csv"),
        "labels_v2_csv_sha256": sha256(ART / "labels" / "labels_trainval.v2.csv"),
        "feature_revision": feat_manifest.get("revision"),
        "feature_arrays_sha256": {k: feat_manifest["sha256"][k] for k in ("L23_max.npy", "L16_pre.npy")},
        "prereg_rf_sha256": sha256(RF.PREREG)}
    code_dir = Path(__file__).resolve().parent
    res["code_sha256"] = {f: sha256(code_dir / f) for f in CODE_FILES}
    res["versions"] = {"python": platform.python_version(), "numpy": np.__version__, "sklearn": sklearn.__version__}
    res["note"] = ("in-sample values are optimistic (training rows scored by the model fitted on them); they are "
                   "recorded for reproducibility only. No cross-validated score of the old cells was computed.")
    for d in (OUT, REPORT):
        (d / "freeze.json").write_text(json.dumps(E.to_jsonable(res), indent=1, ensure_ascii=False), encoding="utf-8")
    assert E.evaluate_sha256() == SHA
    print("DONE", flush=True)


if __name__ == "__main__":
    main()

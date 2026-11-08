"""Final (non-adopted) loop models T7-a and T9-1 fitted once on ALL headline train rows (train split only).

Plan: reports/risk-loop/argus-v1/loop/iter-10/plan.md (F10, not a model try). Model card:
reports/risk-loop/argus-v1/loop/final/card.md. These are NOT registered as a new Argus version.

Structure (same as the CV pipelines ``iter07_models.RobustStore`` + ``iter06_models``/``iter09_models``):
  per feature representation "L{layer}:{pool}" (gpt-oss-20b block-L residual stream pooled over the step's
  observation rows, 2880 dims): median / (IQR/1.349) scaling, clip |z| <= 3, PCA 32 (all fitted on train rows)
  -> per member: first k PCA coordinates @ linear weights -> mid-rank percentile among the member's training
  scores -> weighted average of member percentiles = risk score in [0, 1].

``score(model, feature_rows)`` needs only ``feature_rows = {"L23:max": (n, 2880), "L16:pre": (n, 2880), ...}``
(no tool, source, family or trajectory). Training reads tool / source / trajectory of training rows only.

Usage (fit + save): py -3.11 experiments/risk_loop/argus_loop/final_models.py
"""
from __future__ import annotations

import hashlib
import json
import os
import pickle
import sys
import time
from pathlib import Path

for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ.setdefault(_v, "2")

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop.argus_loop import iter04_models as M4  # noqa: E402
from experiments.risk_loop.argus_loop import iter06_models as M6  # noqa: E402
from experiments.risk_loop.argus_loop import iter07_models as M7  # noqa: E402
from experiments.risk_loop.argus_loop import iter09_models as M9  # noqa: E402

OUT = REPO_ROOT / "artifacts" / "risk-loop" / "argus-v1-loop" / "final"
SHA = "a7c36eafdf994f98b61895be4e4b8d237740d0018422d12febab8deb9df0130d"
FINAL = {
    "T7-a": (tuple(M6.ENSEMBLE), (1.0, 1.0, 1.0)),
    "T9-1": (tuple(M9.T91_COMPONENTS), tuple(M9.T91_WEIGHTS)),
}
FORMAT = "argus-loop-final/1"


# ------------------------------------------------------------------------------------------- pieces

def fit_robust(X: np.ndarray, kmax: int = M7.KMAX, clip: float = M7.CLIP, seed: int = 0) -> dict:
    """Same fit as ``iter07_models.robust_embed`` on the given (training) rows; returns plain arrays."""
    from sklearn.decomposition import PCA

    Xt = np.asarray(X, dtype=np.float32)
    med = np.median(Xt, axis=0)
    q25, q75 = np.percentile(Xt, [25, 75], axis=0)
    sc = (q75 - q25) / M7.IQR_TO_SD
    bad = sc < 1e-6
    if bad.any():
        sd = Xt.std(0)
        sc[bad] = np.where(sd[bad] > 1e-6, sd[bad], 1.0)
    Zt = np.clip((Xt - med) / sc, -clip, clip)
    k = int(min(kmax, Zt.shape[0] - 1, Zt.shape[1]))
    pca = PCA(n_components=k, random_state=seed).fit(Zt)
    return {"median": med.astype(np.float32), "scale": sc.astype(np.float32), "clip": float(clip),
            "pca_mean": pca.mean_.astype(np.float32), "pca_components": pca.components_.astype(np.float32)}


def embed(pre: dict, X: np.ndarray, step: int = 4096) -> np.ndarray:
    """Robust scaling + clipping + PCA projection (float64, rows of X).

    The projection uses ``np.einsum`` (no BLAS blocking) so a row's embedding does not depend on which other
    rows are scored with it; otherwise float noise can flip a training-score rank tie of an in-sample row."""
    X = np.asarray(X)
    comp = pre["pca_components"].astype(np.float64)
    mu = pre["pca_mean"].astype(np.float64)
    out = np.empty((X.shape[0], comp.shape[0]), dtype=np.float64)
    for i in range(0, X.shape[0], step):
        Z = np.clip((np.asarray(X[i:i + step], dtype=np.float32) - pre["median"]) / pre["scale"],
                    -pre["clip"], pre["clip"]).astype(np.float64)
        out[i:i + step] = np.einsum("ij,kj->ik", Z - mu, comp)
    return out


def _lin(Emb: np.ndarray, coef: np.ndarray) -> np.ndarray:
    """Row-wise linear score without BLAS (row result independent of the batch, see ``embed``)."""
    return np.einsum("ij,j->i", np.asarray(Emb, dtype=np.float64), np.asarray(coef, dtype=np.float64))


def _member_weights(m: dict, Etr: np.ndarray, y, traj, tool, source) -> np.ndarray:
    """Linear weights of one member (same branches as ``iter06_models._component_scores``)."""
    kind = m["kind"]
    if kind == "pointwise_informative":
        grp = np.asarray([f"{t}|{s}" for t, s in zip(tool, source)])
        w = M6.pointwise_informative_fit(Etr, y, np.asarray(source).astype(str), grp, m["C"])
    elif kind == "pair_traj":
        w = M4.same_traj_pair_fit(Etr, y, np.asarray(traj).astype(str), m["C"])
    elif kind == "pair_traj_tool":
        key = np.asarray([f"{a}|{b}" for a, b in zip(np.asarray(traj).astype(str), np.asarray(tool).astype(str))])
        w = M4.same_traj_pair_fit(Etr, y, key, m["C"])
    else:
        raise ValueError(kind)
    if w is None:
        raise ValueError(f"member {m['name']} could not be fitted")
    return np.asarray(w, dtype=np.float64)


def fit_final(model_id: str, feats: dict, y, traj, tool, source, info: dict | None = None) -> dict:
    """Fit one final model on the given rows (all of them are training rows)."""
    members, weights = FINAL[model_id]
    y = np.asarray(y).astype(np.int64)
    reps = sorted({m["rep"] for m in members})
    pre = {r: fit_robust(feats[r]) for r in reps}
    emb = {r: embed(pre[r], feats[r]) for r in reps}
    w = np.asarray(weights, dtype=np.float64)
    w = w / w.sum()
    out_members = []
    for m, wk in zip(members, w):
        k = int(m["k"])
        Etr = emb[m["rep"]][:, :k].astype(np.float64)
        coef = _member_weights(m, Etr, y, traj, tool, source)
        s_tr = _lin(Etr, coef)
        out_members.append({"name": m["name"], "rep": m["rep"], "kind": m["kind"], "k": k, "C": float(m["C"]),
                            "coef": coef, "train_scores_sorted": np.sort(s_tr), "weight": float(wk)})
    feature_spec = {r: {"layer": int(r.split(":")[0].lstrip("L")), "pool": r.split(":")[1],
                        "dims": int(feats[r].shape[1]),
                        "meaning": "gpt-oss-20b block-L output (residual stream) at the step's observation rows; "
                                   + {"max": "element-wise max over the rows",
                                      "pre": "the pre_action row (last observation before the action)",
                                      "mean": "mean over the rows"}.get(r.split(":")[1], r.split(":")[1])}
                    for r in reps}
    return {"format": FORMAT, "id": model_id, "status": "candidate, NOT adopted, validation not looked at",
            "feature_spec": feature_spec, "preproc": pre, "members": out_members,
            "n_train_rows": int(len(y)), "n_train_positives": int(y.sum()),
            "evaluate_sha256": SHA, "info": info or {}}


def score(model: dict, feature_rows: dict) -> np.ndarray:
    """Risk score in [0, 1] for each row; ``feature_rows`` = {rep: (n, dims)} for the reps in feature_spec."""
    if model.get("format") != FORMAT:
        raise ValueError("unknown model format")
    n = None
    embs = {}
    for r in model["feature_spec"]:
        X = np.asarray(feature_rows[r])
        if X.ndim != 2 or X.shape[1] != model["feature_spec"][r]["dims"]:
            raise ValueError(f"{r}: expected (n, {model['feature_spec'][r]['dims']}), got {X.shape}")
        if n is not None and X.shape[0] != n:
            raise ValueError("feature arrays have different row counts")
        n = X.shape[0]
        embs[r] = embed(model["preproc"][r], X)
    acc = np.zeros(n)
    for m in model["members"]:
        s = _lin(embs[m["rep"]][:, :m["k"]], m["coef"])
        acc += m["weight"] * M6.train_percentile(m["train_scores_sorted"], s)
    return acc


def save(model: dict, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "wb") as h:
        pickle.dump(model, h, protocol=4)


def load(path: Path) -> dict:
    with open(path, "rb") as h:
        return pickle.load(h)


# ------------------------------------------------------------------------------------------- main

def main():
    from experiments.risk_loop.argus_loop import evaluate as E
    from experiments.risk_loop.argus_loop import iter01_common as C1
    from experiments.risk_loop.argus_loop import iter06_scan as S6

    assert E.evaluate_sha256() == SHA
    data, rows, rinfo = C1.headline_data()
    assert set(rows.split.astype(str).tolist()) == {"train"}, "train split only"
    reps = sorted({m["rep"] for ms, _ in FINAL.values() for m in ms})
    feats = {}
    for r in reps:
        L, p = r.split(":")
        feats[r] = np.asarray(C1.features(data, rows, int(L.lstrip("L")), p), dtype=np.float32)
    y = rows.y.astype(np.int64)
    traj, tool, source = rows.trajectory_id.astype(str), rows.tool.astype(str), rows.source.astype(str)
    rid_hash = hashlib.sha1(np.asarray(rows.row_id, dtype=np.int64).tobytes()).hexdigest()
    ctx = S6.model_ctx(rows)
    allpos = np.arange(len(rows))
    summary = {}
    for mid, (members, weights) in FINAL.items():
        t0 = time.time()
        info = {"rows": "headline_filter train rows (report tools and incomplete-feature rows dropped)",
                "row_id_sha1": rid_hash, "labels": "October gold_violation; November = DRAFT rule labels",
                "rows_info": rinfo, "fitted_at": time.strftime("%Y-%m-%d %H:%M")}
        model = fit_final(mid, feats, y, traj, tool, source, info)
        s = score(model, feats)
        # the CV pipeline refitted on all rows must give the same in-sample scores
        ref = M9.make_weighted(M7.RobustStore(feats), ctx, members, weights)({})(allpos, y, allpos)
        diff = float(np.max(np.abs(s - ref)))
        idx = np.linspace(0, len(rows) - 1, 25).astype(int)
        model["check_rows"] = {"row_id": [int(rows.row_id[i]) for i in idx], "score": [float(s[i]) for i in idx]}
        model["in_sample"] = {"max_abs_diff_vs_cv_pipeline": diff,
                              "within_tool_auroc_in_sample": E.within_tool_auroc(s, y, E.headline_groups(rows))["value"]}
        path = OUT / mid / "model.pkl"
        save(model, path)
        back = load(path)
        again = score(back, {r: feats[r][idx] for r in reps})
        assert np.allclose(again, s[idx], atol=1e-12), "reload mismatch"
        summary[mid] = {"path": str(path.relative_to(REPO_ROOT)), "bytes": path.stat().st_size,
                        "max_abs_diff_vs_cv_pipeline": diff, "in_sample_within_tool": model["in_sample"][
                            "within_tool_auroc_in_sample"], "n": len(rows), "positives": int(y.sum()),
                        "seconds": round(time.time() - t0, 1)}
        print(mid, json.dumps(summary[mid]), flush=True)
    (OUT / "fit_summary.json").write_text(json.dumps(summary, indent=1), encoding="utf-8")
    print("DONE", flush=True)


if __name__ == "__main__":
    main()

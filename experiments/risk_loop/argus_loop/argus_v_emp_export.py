"""Save Argus-V-emp as model files, so that it can score calls that are not in the saved splits.

Approved by the user on 2026-11-17 ("Argus-V-p P3·P5를 모델 파일로 저장하는 학습 시작하고 저장해"). Before that the plan was
shown: the same two Argus-V-p settings, the same structure and settings, the same data (new train split, 9,653 calls,
77 violations); check that the re-fitted models give the saved scores; then connect Argus-V-emp to score single calls
and check that the new-test AUROC is still 0.913.

Why a fit is needed: resplit_run01.py scored the Argus-V-p settings in memory and saved only the scores. The 36
Argus-V-em models were saved as files at the time (run01/em/checkpoints) and are only copied here.

Stages
  fit-p --approved   fit P3 and P5 again with the code path of argus_v_p.Ctx.fit, keep the fitted pieces
                     (scaling, PCA, linear members, random forest, training-score tables), compare the scores of
                     every train / validation / test call with the saved ones, write P3.pkl and P5.pkl
  bundle             copy the 36 Argus-V-em model files, write the validation reference tables and the manifest
  check              load the folder with argus_v_emp_model.EmpModel, score validation and test from the model files
                     only, compare with the saved Argus-V-emp scores, time single calls; add the result to the manifest

Usage: PYTHONUTF8=1 py -3.11 experiments/risk_loop/argus_loop/argus_v_emp_export.py fit-p --approved
       PYTHONUTF8=1 py -3.11 experiments/risk_loop/argus_loop/argus_v_emp_export.py bundle
       PYTHONUTF8=1 py -3.11 experiments/risk_loop/argus_loop/argus_v_emp_export.py check
Output: artifacts/risk-loop/resplit-1117/argus_v_emp/ (not in git)
"""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import sys
import time
from pathlib import Path

for _name in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ.setdefault(_name, "2")

import numpy as np  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from experiments.risk_loop import harness as H  # noqa: E402
from experiments.risk_loop.argus_loop import argus_v_emp as AE  # noqa: E402
from experiments.risk_loop.argus_loop import argus_v_emp_model as EMPM  # noqa: E402
from experiments.risk_loop.argus_loop import resplit_run01 as R  # noqa: E402

BUNDLE = EMPM.BUNDLE
REPS = ("L23:max", "L16:pre")
FEAT_FILE = {"L23:max": "L23_max.npy", "L16:pre": "L16_pre.npy"}


def log(*a):
    line = time.strftime("%H:%M:%S") + " " + " ".join(str(x) for x in a)
    print(line, flush=True)
    BUNDLE.mkdir(parents=True, exist_ok=True)
    with open(BUNDLE / "export.log", "a", encoding="utf-8") as h:
        h.write(line + "\n")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def features() -> dict:
    return {rep: np.asarray(np.load(R.FEAT / FEAT_FILE[rep], mmap_mode="r"), dtype=np.float32) for rep in REPS}


# ---------------------------------------------------------------------------------------------- fit-p
def robust_fit(X: np.ndarray, pos_train: np.ndarray, kmax: int) -> dict:
    """The computation of iter07_models.robust_embed (median / IQR scaling and clipping fitted on the training rows,
    then PCA on the training rows), returning the fitted pieces instead of the embedded rows."""
    from sklearn.decomposition import PCA
    from experiments.risk_loop.argus_loop import iter07_models as M7

    pos_train = np.asarray(pos_train, dtype=np.int64)
    Xt = np.asarray(X[pos_train], dtype=np.float32)
    med = np.median(Xt, axis=0)
    q25, q75 = np.percentile(Xt, [25, 75], axis=0)
    sc = (q75 - q25) / M7.IQR_TO_SD
    bad = sc < 1e-6
    if bad.any():
        sd = Xt.std(0)
        sc[bad] = np.where(sd[bad] > 1e-6, sd[bad], 1.0)
    Zt = np.clip((Xt - med) / sc, -M7.CLIP, M7.CLIP)
    del Xt
    k = int(min(kmax, Zt.shape[0] - 1, Zt.shape[1]))
    pca = PCA(n_components=k, random_state=0).fit(Zt)
    return {"median": med, "scale": sc, "clip": float(M7.CLIP), "pca": pca}


def fit_setting(sid: str, feats: dict, D: dict):
    """argus_v_p.Ctx.fit for one setting without within-tool training, keeping what a later call needs.
    -> (the model as a dict, score of the train rows, score of the validation + test rows)."""
    from experiments.risk_loop.argus_loop import argus_v_p as AP
    from experiments.risk_loop.argus_loop import iter06_models as M6
    from experiments.risk_loop.argus_loop import t7a_rf as RF

    s = AP.SETTINGS[sid]
    assert s["method"] == "none", "only the settings without within-tool training are exported"
    relax = s["relax"]
    kmax = AP.RELAX[relax][2]
    tr = D["idx"]["train"]
    other = np.concatenate([D["idx"]["validation"], D["idx"]["test"]])
    ya = D["y"][tr].astype(np.int64)
    src, cells, traj = D["source"].astype(str)[tr], D["cell"].astype(str)[tr], D["trajectory_id"].astype(str)[tr]
    model = {"setting": sid, "ko": s["ko"], "relax": int(relax), "pca_size": int(kmax), "embed": {}, "members": [], "rf": None,
             "train_rows": int(len(tr)), "train_violations": int(ya.sum())}
    E = {}
    for rep in REPS:
        model["embed"][rep] = robust_fit(feats[rep], tr, kmax)
        E[rep] = EMPM.PModel(model).embed(rep, feats[rep])                     # all rows, in the chunks of robust_embed
    s_tr, s_ot = np.zeros(len(tr)), np.zeros(len(other))
    for comp in AP.comps_for(relax):
        Emb = E[comp["rep"]][:, :int(comp["k"])]
        Etr, Eot = Emb[tr].astype(np.float64), Emb[other].astype(np.float64)
        w = AP.member_w(comp, Etr, ya, src, cells, traj, s["method"])
        assert w is not None, comp
        a = Etr @ w
        s_tr += M6.train_percentile(a, a)
        s_ot += M6.train_percentile(a, Eot @ w)
        model["members"].append({"name": comp["name"], "rep": comp["rep"], "kind": comp["kind"], "k": int(comp["k"]), "C": float(comp["C"]),
                                 "w": np.asarray(w, dtype=np.float64), "train_scores_sorted": np.sort(np.asarray(a, dtype=np.float64))})
    s_tr, s_ot = s_tr / len(model["members"]), s_ot / len(model["members"])
    if s["rf"] > 0:
        assert kmax == 32, "the forest reads the 32-dimension store; here that is the store of the setting itself"
        X = np.hstack([E[rep][:, :k] for rep, k in RF.RF_REPS]).astype(np.float32)
        forest = RF.fit_rf(X[tr], ya, RF.member1_weights(ya, src, cells), AP.RF_MSL, RF.RF_PARAMS)
        p_tr, p_ot = RF.rf_proba(forest, X[tr]), RF.rf_proba(forest, X[other])
        s_tr = (1 - s["rf"]) * s_tr + s["rf"] * M6.train_percentile(p_tr, p_tr)
        s_ot = (1 - s["rf"]) * s_ot + s["rf"] * M6.train_percentile(p_tr, p_ot)
        model["rf"] = {"forest": forest, "reps": [(rep, int(k)) for rep, k in RF.RF_REPS], "weight": float(s["rf"]),
                       "positive_column": int(np.nonzero(forest.classes_ == 1)[0][0]), "min_samples_leaf": int(AP.RF_MSL),
                       "train_proba_sorted": np.sort(np.asarray(p_tr, dtype=np.float64))}
    return model, s_tr, s_ot, E


def stage_fit_p(argv):
    if "--approved" not in argv:
        raise SystemExit("this stage fits models: run it only after the user approved it, with --approved")
    import joblib
    import sklearn
    from experiments.risk_loop.argus_loop import argus_v_p as AP
    from experiments.risk_loop.argus_loop import evaluate as E_

    assert E_.evaluate_sha256() == AP.SHA
    D = R.load()
    feats = features()
    tr, va, te = (D["idx"][s] for s in R.SPLITS)
    log(f"fit-p start | train rows {len(tr)} violations {int(D['y'][tr].sum())} | scored validation {len(va)} test {len(te)} | sklearn {sklearn.__version__}")
    report = {}
    for sid in AE.P_SETTINGS:
        t0 = time.time()
        model, s_tr, s_ot, E = fit_setting(sid, feats, D)
        z = np.load(R.OUT / "p" / f"{sid}.npz", allow_pickle=False)
        saved = {"train": z["scores_train"], "validation": z["scores_validation"], "test": z["scores_test"]}
        got = {"train": s_tr, "validation": s_ot[:len(va)], "test": s_ot[len(va):]}
        diff = {k: float(np.abs(got[k] - saved[k]).max()) for k in got}
        # the saved file, read back and applied to the same rows, must give the same scores as the fit
        path = BUNDLE / f"{sid}.pkl"
        joblib.dump(model, path, compress=3)
        back = EMPM.PModel(joblib.load(path))
        again = {"train": back.score_embedded(E, tr), "validation": back.score_embedded(E, va), "test": back.score_embedded(E, te)}
        diff_file = {k: float(np.abs(again[k] - saved[k]).max()) for k in again}
        auc = {k: float(H.auroc(again[k], D["y"][D["idx"][k]])) for k in again}
        report[sid] = {"seconds": round(time.time() - t0, 1), "max_abs_difference_from_saved_scores_at_fit": diff,
                       "max_abs_difference_from_saved_scores_from_file": diff_file, "auroc_all_calls": auc,
                       "file": path.name, "bytes": path.stat().st_size, "sha256": sha256(path),
                       "members": [{"name": m["name"], "rep": m["rep"], "k": m["k"], "C": m["C"]} for m in model["members"]],
                       "random_forest": None if model["rf"] is None else {"trees": len(model["rf"]["forest"].estimators_), "weight": model["rf"]["weight"]}}
        log(f"{sid} {model['ko']}: {time.time() - t0:.0f}s | largest difference from the saved scores: at fit {max(diff.values()):.3g}, from the file {max(diff_file.values()):.3g}"
            f" | AUROC all calls train {auc['train']:.3f} validation {auc['validation']:.3f} test {auc['test']:.3f} | {path.name} {path.stat().st_size / 1e6:.1f} MB")
        del E
    (BUNDLE / "fit_p.json").write_text(json.dumps({"finished_at": time.strftime("%Y-%m-%d %H:%M:%S"), "sklearn": sklearn.__version__, "settings": report},
                                                  indent=1, ensure_ascii=False), encoding="utf-8")
    log("fit-p done")


# ---------------------------------------------------------------------------------------------- bundle
def stage_bundle(argv):
    import joblib
    import sklearn
    import torch

    D = R.load()
    (BUNDLE / "em").mkdir(parents=True, exist_ok=True)
    names, files, ref = [], {}, {}
    for arch in R.ARCHS:
        for w in R.WEIGHT_RULES:
            for k in R.REPEATS:
                name = f"{arch}_{w}_r{k}"
                src = R.OUT / "em" / "checkpoints" / f"{name}_e{AE.EPOCH:03d}.pt"
                dst = BUNDLE / "em" / src.name
                if not dst.is_file() or dst.stat().st_size != src.stat().st_size:
                    shutil.copy2(src, dst)
                assert sha256(dst) == sha256(src)
                z = np.load(R.OUT / "em" / f"{name}.npz", allow_pickle=False)
                ref[name] = np.sort(z["scores_validation"][AE.EPOCH - 1].astype(np.float64))
                names.append(name)
                files[f"em/{dst.name}"] = {"bytes": dst.stat().st_size, "sha256": sha256(dst)}
    for sid in AE.P_SETTINGS:
        assert (BUNDLE / f"{sid}.pkl").is_file(), f"{sid}.pkl is missing: run fit-p --approved first"
        ref[sid] = np.sort(np.load(R.OUT / "p" / f"{sid}.npz", allow_pickle=False)["scores_validation"].astype(np.float64))
        files[f"{sid}.pkl"] = {"bytes": (BUNDLE / f"{sid}.pkl").stat().st_size, "sha256": sha256(BUNDLE / f"{sid}.pkl")}
    np.savez_compressed(BUNDLE / "reference_validation.npz", **ref)
    files["reference_validation.npz"] = {"bytes": (BUNDLE / "reference_validation.npz").stat().st_size, "sha256": sha256(BUNDLE / "reference_validation.npz")}
    va = D["idx"]["validation"]
    sv = AE.scores("validation")
    normal = sv[D["y"][va] == 0]
    manifest = {"name": AE.NAME, "created_at": time.strftime("%Y-%m-%d %H:%M:%S"), "definition": AE.describe(),
                "input": "x23 = layer 23, maximum over the observation positions (2,880 values); x16 = layer 16 just before the action (2,880 values)",
                "score": "(mean share of the 36 Argus-V-em models + share of P3 + share of P5) / 3; share = part of the validation calls the model scored lower; "
                         "between 0 and 1; a rank-type score, not a probability",
                "argus_v_em_models": names, "argus_v_em_epoch": AE.EPOCH, "argus_v_p_settings": list(AE.P_SETTINGS),
                "reference": {"split": "validation (resplit-1117)", "calls": int(len(va))},
                "cut_offs": {"5%": float(np.quantile(normal, 0.95)), "1%": float(np.quantile(normal, 0.99))},
                "cut_off_rule": "the score above which 5% (1%) of the validation normal calls lie; a call is judged a violation when its score is above the cut-off",
                "libraries": {"python": sys.version.split()[0], "numpy": np.__version__, "scikit-learn": sklearn.__version__, "torch": torch.__version__, "joblib": joblib.__version__},
                "fit_of_argus_v_p": json.loads((BUNDLE / "fit_p.json").read_text(encoding="utf-8")),
                "files": files}
    (BUNDLE / "manifest.json").write_text(json.dumps(manifest, indent=1, ensure_ascii=False), encoding="utf-8")
    log(f"bundle written: {len(names)} Argus-V-em models, {len(AE.P_SETTINGS)} Argus-V-p models, cut-offs {manifest['cut_offs']} | "
        f"{sum(f['bytes'] for f in files.values()) / 1e6:.1f} MB in {len(files)} files")


# ---------------------------------------------------------------------------------------------- check
def stage_check(argv):
    D = R.load()
    feats = features()
    t0 = time.time()
    model = EMPM.EmpModel()
    load_s = time.time() - t0
    out = {"checked_at": time.strftime("%Y-%m-%d %H:%M:%S"), "load_seconds": round(load_s, 2), "splits": {}}
    for split in ("validation", "test"):
        rows = D["idx"][split]
        y = D["y"][rows]
        t0 = time.time()
        got = model.score(feats["L23:max"][rows], feats["L16:pre"][rows])
        secs = time.time() - t0
        saved = AE.scores(split)
        alarm = model.judge(got, "5%")
        tp, fp = int((alarm & (y == 1)).sum()), int((alarm & (y == 0)).sum())
        out["splits"][split] = {"calls": int(len(rows)), "seconds": round(secs, 2),
                                "max_abs_difference_from_saved_scores": float(np.abs(got - saved).max()),
                                "mean_abs_difference_from_saved_scores": float(np.abs(got - saved).mean()),
                                "auroc_all_calls_from_files": float(H.auroc(got, y)), "auroc_all_calls_saved": float(H.auroc(saved, y)),
                                "at_cut_off_5pct": {"violations_caught": tp, "violations": int(y.sum()), "false_alarms": fp,
                                                    "same_judgement_as_saved_scores": bool(np.array_equal(alarm, saved > model.cut["5%"]))}}
        log(f"{split}: {len(rows)} calls from the model files in {secs:.1f}s | largest difference from the saved scores {np.abs(got - saved).max():.3g} | "
            f"AUROC {H.auroc(got, y):.4f} (saved {H.auroc(saved, y):.4f}) | cut-off {model.cut['5%']:.4f}: {tp} of {int(y.sum())} caught, {fp} false alarms")
    # one call at a time: the same score as inside the batch, and how long one call takes
    te = D["idx"]["test"]
    pick = np.concatenate([np.flatnonzero(D["y"][te] == 1)[:5], np.flatnonzero(D["y"][te] == 0)[:15]])
    batch = model.score(feats["L23:max"][te[pick]], feats["L16:pre"][te[pick]])
    t0 = time.time()
    single = np.array([model.score(feats["L23:max"][te[j]][None, :], feats["L16:pre"][te[j]][None, :])[0] for j in pick])
    per_call = (time.time() - t0) / len(pick)
    out["single_call"] = {"calls": int(len(pick)), "max_abs_difference_from_batch": float(np.abs(single - batch).max()), "seconds_per_call": round(per_call, 4)}
    log(f"single calls: {len(pick)} calls one at a time, largest difference from the batch {np.abs(single - batch).max():.3g}, {per_call * 1000:.0f} ms per call (load once {load_s:.1f}s)")
    man = json.loads((BUNDLE / "manifest.json").read_text(encoding="utf-8"))
    man["check"] = out
    (BUNDLE / "manifest.json").write_text(json.dumps(man, indent=1, ensure_ascii=False), encoding="utf-8")
    log("check done")


STAGES = {"fit-p": stage_fit_p, "bundle": stage_bundle, "check": stage_check}

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in STAGES:
        raise SystemExit("usage: argus_v_emp_export.py {fit-p --approved | bundle | check}")
    STAGES[sys.argv[1]](sys.argv[2:])

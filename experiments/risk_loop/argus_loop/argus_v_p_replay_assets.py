"""Assets for argus_hook/replay_demo.py (the Argus-V-p replay demo). Train split only.

  bundle-p5              convert the saved Argus-V-p model (setting P5) into a portable .npz bundle. NO fitting.
  bundle-p6 --approved   fit setting P6 once on all judged train rows and write its bundle. This is TRAINING:
                         run it only after the user approved (TASK.md section 6d); without --approved it refuses.
  scores                 write argus_hook/replay_assets/argus_v_p_scores.json: per train step the stored
                         training-row scores (P6 saved scores; P5 scored with its bundle = inference only), labels,
                         per-tool thresholds and the recommended demo rollouts.
  scenarios              write argus_hook/replay_assets/scenario_descriptions.json: Korean title, task, situation,
                         forbidden action and condition meanings of every TRAIN scenario in the score table, copied
                         from the scenario definition files under Scenario/ (no model, no scores). Only the files of
                         train scenarios are opened; from the 30-scenario bank file only train entries are kept.

Bundles go to argus_hook/replay_assets/argus_v_p_<setting>.bundle (npz format, a few MB). Every bundle is checked
against the reference scores before it is accepted.
"""
from __future__ import annotations

import csv
import json
import pickle
import sys
import time
from collections import Counter
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
for _p in (REPO_ROOT, REPO_ROOT / "argus_hook"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))
import replay_scoring as RS  # noqa: E402
from experiments.risk_loop import harness as H  # noqa: E402
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402
from experiments.risk_loop.argus_loop import final_models as FM  # noqa: E402
from experiments.risk_loop.argus_loop import iter01_common as C1  # noqa: E402
from experiments.risk_loop.argus_loop import iter06_models as M6  # noqa: E402

ART = REPO_ROOT / "artifacts" / "risk-loop"
V2 = ART / "argus-v1-loop" / "features_labels_v2"
P = ART / "argus-v-p"
ASSETS = REPO_ROOT / "argus_hook" / "replay_assets"
OUT = ASSETS            # bundles are small (a few MB) and live next to the replay tool
REPS = ("L23:max", "L16:pre")
RECOMMENDED = ["AV-S36-C0-s0-6c455e3b", "AV-S01-C0-s1-adb201b8", "AV-S31-C1-s0-99762ab9", "AV-S07-C1-s1-22c217b2",
               "AV-S55-C1-s2-bd670296"]
SETTING_KO = {"P5": "최고 모델 + 랜덤 포레스트 (규칙으로 정해진 Argus-V-p)",
              "P6": "같은 도구 안 학습 + 규제 완화 + 랜덤 포레스트 (학습 데이터 점수가 가장 높은 설정)"}


def log(*a):
    print(time.strftime("%H:%M:%S"), *a, flush=True)


def load_rows(with_features=True):
    data, rows, _ = C1.headline_data(V2)
    assert set(rows.split.astype(str).tolist()) == {"train"}, "train split only"
    feats = None
    if with_features:
        feats = {r: np.asarray(C1.features(data, rows, int(r.split(":")[0].lstrip("L")), r.split(":")[1]), dtype=np.float32)
                 for r in REPS}
    return rows, feats


def rf_arrays(rf) -> dict:
    col = int(np.nonzero(rf.classes_ == 1)[0][0])
    offs, left, right, feat, thr, val = [0], [], [], [], [], []
    for est in rf.estimators_:
        t = est.tree_
        v = t.value[:, 0, :]
        left.append(t.children_left.astype(np.int32))
        right.append(t.children_right.astype(np.int32))
        feat.append(np.maximum(t.feature, 0).astype(np.int32))
        thr.append(t.threshold.astype(np.float64))
        tot = v.sum(1)
        # scikit-learn >= 1.3 stores class fractions in tree_.value and predict_proba returns them unchanged;
        # dividing again would move the last bit. Older versions store counts and normalise.
        val.append((v[:, col] if np.allclose(tot, 1.0, atol=1e-9) else v[:, col] / tot).astype(np.float64))
        offs.append(offs[-1] + t.node_count)
    return {"rf_offsets": np.asarray(offs, np.int64), "rf_left": np.concatenate(left), "rf_right": np.concatenate(right),
            "rf_feature": np.concatenate(feat), "rf_threshold": np.concatenate(thr), "rf_value": np.concatenate(val)}


def pre_arrays(prefix: str, pre: dict) -> dict:
    out = {}
    for rep, key in RS.REPS.items():
        p = pre[rep]
        out.update({f"{prefix}_{key}_median": np.asarray(p["median"], np.float32),
                    f"{prefix}_{key}_scale": np.asarray(p["scale"], np.float32),
                    f"{prefix}_{key}_mean": np.asarray(p["pca_mean"], np.float32),
                    f"{prefix}_{key}_comps": np.asarray(p["pca_components"], np.float32)})
    return out


def write_bundle(setting, lin_pre, members, rf, rf_pre, rf_weight, rf_X_train, rf_reps, n, npos, note) -> Path:
    arrays = pre_arrays("lin", lin_pre)
    meta_members = []
    for i, m in enumerate(members):
        arrays[f"m{i}_coef"] = np.asarray(m["coef"], np.float64)
        arrays[f"m{i}_train_sorted"] = np.asarray(m["train_scores_sorted"], np.float64)
        meta_members.append({"name": m["name"], "rep": m["rep"], "k": int(m["k"]), "weight": float(m["weight"])})
    shares = rf_pre is lin_pre
    if not shares:
        arrays.update(pre_arrays("rf", rf_pre))
    ra = rf_arrays(rf)
    arrays.update(ra)
    # Reference distribution of the forest member = the bundle scorer's OWN training-row probabilities, so a
    # training row ties exactly with its stored value (scikit-learn's sum differs in the last bit).
    own = RS.rf_proba({k[3:]: v for k, v in ra.items()}, rf_X_train)
    arrays["rf_train_sorted"] = np.sort(own)
    meta = {"setting": setting, "setting_ko": SETTING_KO[setting], "clip": float(lin_pre[REPS[0]]["clip"]),
            "members": meta_members, "n_train_rows": int(n), "n_train_positives": int(npos),
            "rf": {"weight": float(rf_weight), "reps": [[r, int(k)] for r, k in rf_reps], "n_trees": int(len(rf.estimators_)),
                   "shares_linear_preprocessing": bool(shares)},
            "note": note, "written_at": time.strftime("%Y-%m-%d %H:%M")}
    path = OUT / f"argus_v_p_{setting}.bundle"
    RS.save_bundle(path, meta, arrays)
    return path


def check(path: Path, feats, rows, ref, what, tol):
    b = RS.load_bundle(path)
    s = RS.score(b, feats)
    d = float(np.max(np.abs(s - ref)))
    wt = E.within_tool_auroc(s, rows.y, E.headline_groups(rows))["value"]
    log(f"{path.name}: {path.stat().st_size / 1e6:.1f} MB | max |bundle - {what}| = {d:.2e} | within-tool AUROC on training rows {wt:.4f}")
    assert d <= tol, (d, tol)
    return s


def cmd_bundle_p5():
    src = P / "model" / "argus_v_p.pkl"
    with open(src, "rb") as h:               # written by argus_v_p.py on this machine
        m = pickle.load(h)
    assert m["format"] == "argus-v-p-rf/1" and m["t7a"]["info"]["setting"] == "P5"
    t7 = m["t7a"]
    rows, feats = load_rows()
    ref = (1 - m["rf_weight"]) * FM.score(t7, feats)
    X = np.hstack([FM.embed(m["rf_preproc"][rep], feats[rep])[:, :k] for rep, k in m["rf_reps"]]).astype(np.float32)
    from experiments.risk_loop.argus_loop import t7a_rf as RF
    p_tr = RF.rf_proba(m["rf"], X)
    assert np.allclose(np.sort(p_tr), m["rf_train_scores_sorted"])
    ref = ref + m["rf_weight"] * M6.train_percentile(p_tr, p_tr)
    path = write_bundle("P5", t7["preproc"], t7["members"], m["rf"], m["rf_preproc"] if m["rf_preproc"] is not t7["preproc"] else t7["preproc"],
                        m["rf_weight"], X, m["rf_reps"], t7["n_train_rows"], t7["n_train_positives"],
                        "converted from artifacts/risk-loop/argus-v-p/model/argus_v_p.pkl without fitting")
    check(path, feats, rows, ref, "saved model", 1e-9)


def cmd_bundle_p6(approved: bool):
    if not approved:
        raise SystemExit("bundle-p6 fits setting P6 on all judged train rows (training). Run it only after the user approved, "
                         "then pass --approved.")
    from experiments.risk_loop.argus_loop import argus_v_p as AP
    from experiments.risk_loop.argus_loop import t7a_rf as RF
    cx = AP.Ctx()
    s, relax = AP.SETTINGS["P6"], AP.SETTINGS["P6"]["relax"]
    kstore = AP.RELAX[relax][2]
    pre = {r: FM.fit_robust(cx.feats[r], kmax=kstore) for r in cx.reps}
    emb = {r: FM.embed(pre[r], cx.feats[r]) for r in cx.reps}
    comps = AP.comps_for(relax)
    members = []
    for comp in comps:
        Etr = emb[comp["rep"]][:, :int(comp["k"])]
        w = AP.member_w(comp, Etr, cx.y, cx.src, cx.cells, cx.traj, s["method"])
        members.append({"name": comp["name"], "rep": comp["rep"], "k": int(comp["k"]), "coef": np.asarray(w, np.float64),
                        "train_scores_sorted": np.sort(FM._lin(Etr, w)), "weight": 1.0 / len(comps)})
    pre32 = {r: FM.fit_robust(cx.feats[r], kmax=32) for r in cx.reps}
    X = np.hstack([FM.embed(pre32[rep], cx.feats[rep])[:, :k] for rep, k in RF.RF_REPS]).astype(np.float32)
    rf = RF.fit_rf(X, cx.y, RF.member1_weights(cx.y, cx.src, cx.cells), AP.RF_MSL, RF.RF_PARAMS)
    p_tr = RF.rf_proba(rf, X)
    path = write_bundle("P6", pre, members, rf, pre32, s["rf"], X, RF.RF_REPS, cx.n, int(cx.y.sum()),
                        "setting P6 fitted once on all judged train rows for the replay demo (in-sample presentation model)")
    ref = np.load(P / "p6_condition_c_scores.npy")
    feats = {r: cx.feats[r] for r in REPS}
    sc = check(path, feats, cx.rows, ref, "saved P6 training-row scores", 5e-3)
    np.save(P / "argus_v_p_P6_bundle_scores.npy", sc)


def cell_threshold(s, y) -> dict:
    p, q = s[y == 1], s[y == 0]
    out = {"violations": int(len(p)), "normals": int(len(q))}
    if not len(p):
        return {**out, "kind": "no_violation"}
    if not len(q):
        return {**out, "kind": "no_normal"}
    if p.min() > q.max():
        return {**out, "kind": "separable", "threshold": round(float((p.min() + q.max()) / 2), 4),
                "caught": int(len(p)), "false_alarms": 0}
    cand = np.unique(s)
    mids = (cand[:-1] + cand[1:]) / 2 if len(cand) > 1 else cand
    best = max(mids, key=lambda t: (float((p > t).mean() - (q > t).mean()), -t))
    return {**out, "kind": "partial", "threshold": round(float(best), 4), "caught": int((p > best).sum()),
            "false_alarms": int((q > best).sum())}


def cmd_scores():
    rows, feats = load_rows()
    n, y = len(rows), rows.y.astype(int)
    g = E.headline_groups(rows).astype(str)
    scores = {"P6": np.load(P / "p6_condition_c_scores.npy")}
    b6 = P / "argus_v_p_P6_bundle_scores.npy"
    if b6.is_file():                       # prefer the bundle's own scores once the P6 bundle exists
        scores["P6"] = np.load(b6)
    scores["P5"] = RS.score(RS.load_bundle(OUT / "argus_v_p_P5.bundle"), feats)
    assert all(v.shape == (n,) for v in scores.values())
    meta = {}
    with open(V2 / "steps.csv", newline="", encoding="utf-8") as h:
        for rec in csv.DictReader(h):
            meta[int(rec["row"])] = rec
    ids = [int(r) for r in rows.row_id.tolist()]
    assert all(meta[r]["split"] == "train" for r in ids)
    units = {}
    for i, r in enumerate(ids):
        m = meta[r]
        u = units.setdefault(m["unit_id"], {"scenario": m["scenario_id"], "condition": m["condition"], "seed": m["seed"],
                                            "family": m["family"], "source": m["source"], "steps": []})
        u["steps"].append([int(m["step_index"]), m["tool"], int(y[i])] + [round(float(scores[k][i]), 4) for k in ("P6", "P5")])
    for u in units.values():
        u["steps"].sort()
    out = {"format": "argus-v-p-replay-scores/1", "written_at": time.strftime("%Y-%m-%d %H:%M"),
           "note": "Training-row scores (the models were fitted on these same rows). Train split only.",
           "step_columns": ["step_index", "tool", "label", "P6", "P5"], "models": {}, "recommended_units": RECOMMENDED,
           "units": units}
    for k, s in scores.items():
        cells = {c: cell_threshold(s[g == c], y[g == c]) for c in sorted(set(g.tolist()))}
        out["models"][k] = {"setting_ko": SETTING_KO[k],
                            "within_tool_auroc_training_rows": round(float(E.within_tool_auroc(s, y, E.headline_groups(rows))["value"]), 4),
                            "global_threshold_5pct_false_alarm": round(float(np.quantile(s[y == 0], 0.95)), 4),
                            "tool_thresholds": {c: v for c, v in cells.items() if v["kind"] in ("separable", "partial")},
                            "tools_without_violation": int(sum(1 for v in cells.values() if v["kind"] == "no_violation"))}
        kinds = Counter(v["kind"] for v in cells.values())
        log(k, "within-tool AUROC", out["models"][k]["within_tool_auroc_training_rows"], "| tool cells:", dict(kinds))
    ASSETS.mkdir(parents=True, exist_ok=True)
    path = ASSETS / "argus_v_p_scores.json"
    path.write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    log("wrote", path.relative_to(REPO_ROOT), f"{path.stat().st_size / 1e3:.0f} KB,", len(units), "train rollouts,", n, "steps")


SCENARIO_DIR = REPO_ROOT / "Scenario"
APPROVAL_KO = {"none": "승인 요청이 필요 없음", "GRANTED": "승인 요청이 승인됨", "DENIED": "승인 요청이 거절됨"}


def _first_sentence(text, limit=110) -> str:
    text = " ".join(str(text or "").split())
    cut = text.find(". ")
    text = text[:cut + 1] if 0 < cut < limit else text
    return text if len(text) <= limit else text[:limit].rstrip() + " …"


def _v1_description(sid: str, bank: dict) -> dict:
    """Scenarios AV-S01..S30 live in one bank file, AV-S31.. in one file each (key ``scenario``)."""
    number = int(sid.split("S")[1])
    if number <= 30:
        sc = bank[sid]
    else:
        folder = "operator-scenarios-31-60" if number <= 60 else "operator-scenarios-61-80"
        sc = json.loads((SCENARIO_DIR / folder / f"{sid}.v1.json").read_text(encoding="utf-8"))["scenario"]
    assert sc["id"] == sid, sid
    return {"title": sc["title"], "category": sc.get("category"), "task": sc["goal"], "situation": sc.get("blocker"),
            "forbidden": sc.get("denied"), "conditions": dict(sc.get("controls") or {}), "tools": {}}


def _v2_description(sid: str, condition_names: set, violation_tools: set) -> dict:
    family = sid.split("-")[1]
    doc = json.loads((SCENARIO_DIR / "operator-scenarios-v2" / family / f"{sid}.v2.json").read_text(encoding="utf-8"))
    assert doc["id"] == sid and doc.get("split") == "train", f"{sid}: not a train scenario file"
    cells = {f"cell{m['cell']}": m["O"] for m in doc["collection"]["matrix"]}
    conditions = {}
    for name in sorted(condition_names):
        outcome = cells.get(name) or (name[len("pilot"):] if name.startswith("pilot") else name)
        c = doc["conditions"].get(outcome)
        if not isinstance(c, dict) or "service_state" not in c:
            continue
        text = f"{c['service_state']} · {APPROVAL_KO.get(c.get('approval_outcome'), c.get('approval_outcome'))}"
        if "twin_delta" in c:
            text += " · 대조 조건(같은 호출이 허용되는 판본)"
        conditions[name] = text
    tools = {t["name"]: _first_sentence(t.get("description")) for t in doc["tools"] if t["name"] in violation_tools}
    return {"title": doc["title_operator"], "category": f"{doc.get('family_id')}·{doc.get('domain')}", "task": doc["public"]["goal"],
            "situation": None, "forbidden": None, "conditions": conditions, "tools": tools}


def cmd_scenarios():
    table = json.loads((ASSETS / "argus_v_p_scores.json").read_text(encoding="utf-8"))
    names, viol = {}, {}
    for u in table["units"].values():                       # the table holds train rollouts only
        names.setdefault(u["scenario"], set()).add(u["condition"])
        viol.setdefault(u["scenario"], set()).update(r[1] for r in u["steps"] if r[2] == 1)
    wanted_bank = {s for s in names if s.startswith("AV-S") and int(s.split("S")[1]) <= 30}
    bank = {}
    if wanted_bank:                                         # one file for 30 scenarios: keep the train entries only
        doc = json.loads((SCENARIO_DIR / "scenario-bank-30.v1.json").read_text(encoding="utf-8"))
        bank = {sc["id"]: sc for sc in doc["scenarios"] if sc["id"] in wanted_bank}
    out = {}
    for sid in sorted(names):
        out[sid] = _v2_description(sid, names[sid], viol[sid]) if sid.startswith("AVv2") else _v1_description(sid, bank)
    doc = {"format": "argus-v-p-replay-scenarios/1", "written_at": time.strftime("%Y-%m-%d %H:%M"),
           "note": "Operator-side descriptions of the TRAIN scenarios in argus_v_p_scores.json, copied from Scenario/. "
                   "For the replay screen only; never give this to the agent under test.",
           "scenarios": out}
    path = ASSETS / "scenario_descriptions.json"
    path.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    missing = [s for s, d in out.items() if not d["title"] or not d["task"]]
    log("wrote", path.relative_to(REPO_ROOT), f"{path.stat().st_size / 1e3:.0f} KB,", len(out), "train scenarios,",
        sum(1 for d in out.values() if d["conditions"]), "with condition meanings,", "missing title/task:", missing)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "bundle-p5":
        cmd_bundle_p5()
    elif cmd == "bundle-p6":
        cmd_bundle_p6("--approved" in sys.argv)
    elif cmd == "scores":
        cmd_scores()
    elif cmd == "scenarios":
        cmd_scenarios()
    else:
        raise SystemExit("usage: argus_v_p_replay_assets.py bundle-p5 | bundle-p6 --approved | scores | scenarios")

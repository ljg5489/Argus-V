"""Argus-V-p: presentation ("possibility") track requested by the user on 2026-11-15. NOT a judging-metric
candidate: its numbers never enter the Argus-V1 try ledger and every number carries its condition.
Plan fixed before the first run: reports/risk-loop/argus-v-p/README.md.

Conditions (within-tool AUROC over the 9 judging cells; train split only, labels v2):
  A  unseen scenario      family-grouped 5-fold (evaluate.make_folds), fold seeds 0-2
  B  seen scenario, new run   5-fold grouped by (scenario, seed), clone rows (identical features) merged into one
                              group, fold seeds 0-2
  C  training rows re-scored  fit on all judged train rows, score the same rows

Settings (inputs = hidden-state features only):
  P1 T7-a as is                      P2 + within-tool training (cell centring + in-cell pair loss, "w3")
  P3 relaxed (PCA 128/128/32, C x10) P4 within-tool + relaxed
  P5 P1 + random forest member (weight 1/4, 500 trees, leaf 10)      P6 P4 + the same random forest member

Usage: py -3.11 experiments/risk_loop/argus_loop/argus_v_p.py run      (resumable; scores cached per setting/seed)
       py -3.11 experiments/risk_loop/argus_loop/argus_v_p.py report
"""
from __future__ import annotations

import csv
import hashlib
import json
import os
import pickle
import sys
import threading
import time
from pathlib import Path

for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ.setdefault(_v, "2")

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop import harness as H  # noqa: E402
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402
from experiments.risk_loop.argus_loop import final_models as FM  # noqa: E402
from experiments.risk_loop.argus_loop import iter01_common as C1  # noqa: E402
from experiments.risk_loop.argus_loop import iter04_models as M4  # noqa: E402
from experiments.risk_loop.argus_loop import iter05_common as C5  # noqa: E402
from experiments.risk_loop.argus_loop import iter06_models as M6  # noqa: E402
from experiments.risk_loop.argus_loop import iter06_scan as S6  # noqa: E402
from experiments.risk_loop.argus_loop import iter07_models as M7  # noqa: E402
from experiments.risk_loop.argus_loop import models as M  # noqa: E402
from experiments.risk_loop.argus_loop import t7a_rf as RF  # noqa: E402
from experiments.risk_loop.argus_loop import within_tool as W  # noqa: E402

SHA = FM.SHA
ART = REPO_ROOT / "artifacts" / "risk-loop" / "argus-v1-loop"
V2 = ART / "features_labels_v2"
OUT = REPO_ROOT / "artifacts" / "risk-loop" / "argus-v-p"
REPORT = REPO_ROOT / "reports" / "risk-loop" / "argus-v-p"
IT14 = ART / "phase3" / "within_tool"
SEEDS = (0, 1, 2)
RF_MSL = 10
SETTINGS = {
    "P1": {"ko": "최고 모델 그대로", "method": "none", "relax": 0, "rf": 0.0},
    "P2": {"ko": "같은 도구 안 학습", "method": "w3", "relax": 0, "rf": 0.0},
    "P3": {"ko": "규제 완화", "method": "none", "relax": 1, "rf": 0.0},
    "P4": {"ko": "같은 도구 안 학습 + 규제 완화", "method": "w3", "relax": 1, "rf": 0.0},
    "P5": {"ko": "최고 모델 + 랜덤 포레스트", "method": "none", "relax": 0, "rf": 0.25},
    "P6": {"ko": "같은 도구 안 학습 + 규제 완화 + 랜덤 포레스트", "method": "w3", "relax": 1, "rf": 0.25},
}
# relax level -> (k per member in ENSEMBLE order, C multiplier, PCA size of the store)
RELAX = {0: ((32, 32, 10), 1.0, 32), 1: ((128, 128, 32), 10.0, 128), 2: ((128, 128, 32), 100.0, 128),
         3: ((512, 512, 128), 100.0, 512)}
REUSE_A = {"P1": "oof_t7a_none.npy", "P2": "oof_t7a_w3.npy"}   # iteration-14 scores, fold seeds 0-2 (read only)


def log(*a):
    print(time.strftime("%H:%M:%S"), *a, flush=True)


class KStore(M7.RobustStore):
    """iter07 RobustStore with a configurable PCA size (kmax 32 == the original)."""

    def __init__(self, features: dict, kmax: int):
        super().__init__(features)
        self.kmax = int(kmax)

    def get(self, rep: str, pos_train) -> np.ndarray:
        key = (rep, C5.pos_hash(pos_train))
        with self.lock:
            if key in self.cache:
                return self.cache[key]
        Emb = M7.robust_embed(self.features[rep], pos_train, kmax=self.kmax)
        with self.lock:
            if len(self.cache) > 12:
                self.cache.clear()
            self.cache[key] = Emb
            self.computed += 1
        return Emb


def comps_for(relax: int) -> list[dict]:
    ks, cm, _ = RELAX[relax]
    out = []
    for c, k in zip(M6.ENSEMBLE, ks):
        d = dict(c)
        d["k"], d["C"] = int(k), float(c["C"]) * cm
        out.append(d)
    return out


def member_w(comp, Etr, ya, src, cells, traj, method):
    """Linear weights of one member; mirrors within_tool.t7a_member_scores for 'none' and 'w3' (checked at start)."""
    C = float(comp["C"])
    if method == "none":
        if comp["kind"] == "pointwise_informative":
            return M6.pointwise_informative_fit(Etr, ya, src, cells, C)
        return M4.same_traj_pair_fit(Etr, ya, traj, C)
    if method == "w3":
        Ec, _, _ = W.cell_center(Etr, cells)
        I, J, Wt = W.within_cell_pairs(ya, cells, traj)
        return W.pair_bce_fit(Etr, I, J, Wt, C, Ec, ya, M.sample_weights(ya, src, "source_class"))
    raise ValueError(method)


class Ctx:
    def __init__(self):
        assert E.evaluate_sha256() == SHA
        self.data, self.rows, _ = C1.headline_data(V2)
        rows = self.rows
        assert set(rows.split.astype(str).tolist()) == {"train"}, "train split only"
        self.reps = ["L16:pre", "L23:max"]
        self.feats = {r: np.asarray(C1.features(self.data, rows, int(r.split(":")[0].lstrip("L")), r.split(":")[1]),
                                    dtype=np.float32) for r in self.reps}
        self.y = rows.y.astype(np.int64)
        self.n = len(rows)
        mc = S6.model_ctx(rows)
        self.src = np.asarray(mc["source"]).astype(str)
        self.cells = np.asarray(mc["train_group"]).astype(str)
        self.traj = np.asarray(mc["trajectory"]).astype(str)
        self.groups = E.headline_groups(rows)
        self.stores = {}
        self.scen, self.seed = self._scenario_seed()
        self.seen_groups, self.clone_info = self._seen_groups()

    def store(self, kmax):
        if kmax not in self.stores:
            self.stores[kmax] = KStore(self.feats, kmax)
        return self.stores[kmax]

    def _scenario_seed(self):
        want = set(int(r) for r in self.rows.row_id.tolist())
        got = {}
        with open(V2 / "steps.csv", newline="", encoding="utf-8") as h:
            for rec in csv.DictReader(h):
                r = int(rec["row"])
                if r in want:
                    assert rec["split"] == "train"
                    got[r] = (rec["scenario_id"], rec["seed"])
        ids = [int(r) for r in self.rows.row_id.tolist()]
        return (np.asarray([got[r][0] for r in ids], dtype=object), np.asarray([got[r][1] for r in ids], dtype=object))

    def _seen_groups(self):
        """Group id per row for condition B: (scenario, seed), with groups merged whenever two rows have identical
        features (clones: same prefix replayed in another rollout) or share a trajectory."""
        key = np.asarray([f"{a}|{b}" for a, b in zip(self.scen, self.seed)], dtype=object)
        uniq = {k: i for i, k in enumerate(sorted(set(key.tolist())))}
        parent = list(range(len(uniq)))

        def find(a):
            while parent[a] != a:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[max(ra, rb)] = min(ra, rb)

        gid = np.asarray([uniq[k] for k in key.tolist()])
        hashes = [hashlib.sha1(self.feats["L23:max"][i].tobytes() + self.feats["L16:pre"][i].tobytes()).hexdigest()
                  for i in range(self.n)]
        first, n_clone_rows = {}, 0
        for i, hsh in enumerate(hashes):
            if hsh in first:
                n_clone_rows += 1
                union(gid[first[hsh]], gid[i])
            else:
                first[hsh] = i
        tfirst = {}
        for i, t in enumerate(self.traj.tolist()):
            if t in tfirst:
                union(gid[tfirst[t]], gid[i])
            else:
                tfirst[t] = i
        g = np.asarray([find(a) for a in gid])
        self.hashes = np.asarray(hashes, dtype=object)
        info = {"scenario_seed_keys": len(uniq), "groups_after_merge": int(len(set(g.tolist()))),
                "rows_with_an_identical_earlier_row": int(n_clone_rows), "scenarios": int(len(set(self.scen.tolist())))}
        return g, info

    def folds(self, cond: str, seed: int):
        if cond == "A":
            return E.make_folds(self.rows, 5, seed)
        from sklearn.model_selection import StratifiedGroupKFold
        sp = StratifiedGroupKFold(n_splits=5, shuffle=True, random_state=int(seed))
        folds = [(np.sort(a), np.sort(b)) for a, b in sp.split(np.zeros(self.n), self.y, self.seen_groups)]
        for a, b in folds:
            assert not set(self.seen_groups[a].tolist()) & set(self.seen_groups[b].tolist())
            assert not set(self.hashes[a].tolist()) & set(self.hashes[b].tolist()), "clone leak"
        return folds

    def fit(self, sid: str, pa, ya, pb, relax=None):
        """(training-row ensemble score, scored-row ensemble score)."""
        s = SETTINGS[sid]
        relax = s["relax"] if relax is None else relax
        pa, pb = np.asarray(pa, np.int64), np.asarray(pb, np.int64)
        ya = np.asarray(ya).astype(np.int64)
        src, cells, traj = self.src[pa], self.cells[pa], self.traj[pa]
        st = self.store(RELAX[relax][2])
        comps = comps_for(relax)
        tr = np.zeros(len(pa))
        te = np.zeros(len(pb))
        for comp in comps:
            Emb = st.get(comp["rep"], pa)[:, :int(comp["k"])]
            Etr, Ete = Emb[pa].astype(np.float64), Emb[pb].astype(np.float64)
            w = member_w(comp, Etr, ya, src, cells, traj, s["method"])
            s_tr, s_te = (np.zeros(len(pa)), np.zeros(len(pb))) if w is None else (Etr @ w, Ete @ w)
            tr += M6.train_percentile(s_tr, s_tr)
            te += M6.train_percentile(s_tr, s_te)
        tr, te = tr / len(comps), te / len(comps)
        if s["rf"] > 0 and len(np.unique(ya)) > 1:
            st32 = self.store(32)
            X = np.hstack([st32.get(rep, pa)[:, :k] for rep, k in RF.RF_REPS]).astype(np.float32)
            rf = RF.fit_rf(X[pa], ya, RF.member1_weights(ya, src, cells), RF_MSL, RF.RF_PARAMS)
            p_tr = RF.rf_proba(rf, X[pa])
            p_te = RF.rf_proba(rf, X[pb]) if len(pb) else np.zeros(0)
            tr = (1 - s["rf"]) * tr + s["rf"] * M6.train_percentile(p_tr, p_tr)
            te = (1 - s["rf"]) * te + s["rf"] * M6.train_percentile(p_tr, p_te)
        return tr, te

    def wt(self, scores):
        return E.within_tool_auroc(scores, self.y, self.groups)

    def per_cell(self, scores_list):
        out = {}
        for e in self.wt(scores_list[0])["per_tool"]:
            if e["included"]:
                m = self.groups == e["tool"]
                out[e["tool"]] = {"violations": e["positives"], "normals": e["negatives"],
                                  "auroc": float(np.mean([H.auroc(np.asarray(s)[m], self.y[m]) for s in scores_list]))}
        return out


def start_checks(cx: Ctx):
    """My member code must reproduce the existing pipeline on one fold (methods none and w3)."""
    a, b = E.make_folds(cx.rows, 5, 0)[0]
    t7 = W.T7aW(cx.feats, cx.rows)
    for sid, method in (("P1", "none"), ("P2", "w3")):
        ref = t7.fit(a, cx.y[a], b, method)
        mine = cx.fit(sid, a, cx.y[a], b)[1]
        d = float(np.max(np.abs(ref - mine)))
        log("start check", sid, "max abs diff vs existing pipeline", d)
        assert d < 1e-6, d


def oof_path(sid, cond, seed, tag=""):
    return OUT / f"oof_{sid}_{cond}_s{seed}{tag}.npy"


def run_cv(cx: Ctx, sid: str, cond: str):
    outs = []
    for seed in SEEDS:
        p = oof_path(sid, cond, seed)
        if p.is_file():
            outs.append(np.load(p))
            continue
        if cond == "A" and sid in REUSE_A:
            O = np.load(IT14 / REUSE_A[sid])
            assert O.shape == (3, cx.n), O.shape
            oof = np.asarray(O[seed], dtype=np.float64)
        else:
            t0 = time.time()
            oof = np.full(cx.n, np.nan)
            for a, b in cx.folds(cond, seed):
                oof[b] = cx.fit(sid, a, cx.y[a], b)[1]
            log(f"  {sid} cond {cond} seed {seed}: {cx.wt(oof)['value']:.4f} ({time.time() - t0:.0f}s)")
        assert np.isfinite(oof).all()
        np.save(p, oof)
        outs.append(oof)
    return outs


def summarise(cx: Ctx, outs):
    per_seed = [cx.wt(o)["value"] for o in outs]
    return {"value": float(np.mean(per_seed)), "per_seed": [float(v) for v in per_seed],
            "pooled_auroc": float(np.mean([H.auroc(o, cx.y) for o in outs])), "per_cell": cx.per_cell(outs)}


def in_sample(cx: Ctx, sid: str, relax=None):
    allpos = np.arange(cx.n)
    tr, _ = cx.fit(sid, allpos, cx.y, np.zeros(0, np.int64), relax=relax)
    return {"value": float(cx.wt(tr)["value"]), "pooled_auroc": float(H.auroc(tr, cx.y)),
            "per_cell": cx.per_cell([tr]), "relax": SETTINGS[sid]["relax"] if relax is None else relax}


def shuffle_check(cx: Ctx, sid: str, n=5):
    """Condition B with training labels shuffled inside each training cell: should be near 0.5 (leak check)."""
    vals = []
    for r in range(n):
        rng = np.random.default_rng(1000 + r)
        oof = np.full(cx.n, np.nan)
        for a, b in cx.folds("B", 0):
            ya = cx.y[a].copy()
            for c in np.unique(cx.cells[a]):
                m = np.nonzero(cx.cells[a] == c)[0]
                ya[m] = rng.permutation(ya[m])
            oof[b] = cx.fit(sid, a, ya, b)[1]
        vals.append(float(cx.wt(oof)["value"]))
        log(f"  shuffle check {sid} run {r}: {vals[-1]:.4f}")
    return {"mean": float(np.mean(vals)), "runs": vals}


def export(cx: Ctx, sid: str, relax: int):
    """Fit the chosen setting on all judged train rows and save a scoring file (final_models format)."""
    s = SETTINGS[sid]
    allpos = np.arange(cx.n)
    kstore = RELAX[relax][2]
    pre = {r: FM.fit_robust(cx.feats[r], kmax=kstore) for r in cx.reps}
    emb = {r: FM.embed(pre[r], cx.feats[r]) for r in cx.reps}
    members = []
    comps = comps_for(relax)
    for comp in comps:
        Etr = emb[comp["rep"]][:, :int(comp["k"])]
        w = member_w(comp, Etr, cx.y, cx.src, cx.cells, cx.traj, s["method"])
        s_tr = FM._lin(Etr, w)
        members.append({"name": comp["name"], "rep": comp["rep"], "kind": comp["kind"] + "|" + s["method"],
                        "k": int(comp["k"]), "C": float(comp["C"]), "coef": np.asarray(w, np.float64),
                        "train_scores_sorted": np.sort(s_tr), "weight": 1.0 / len(comps)})
    spec = {r: {"layer": int(r.split(":")[0].lstrip("L")), "pool": r.split(":")[1], "dims": int(cx.feats[r].shape[1])}
            for r in cx.reps}
    t7 = {"format": FM.FORMAT, "id": "Argus-V-p", "status": "presentation model, NOT a judging candidate",
          "feature_spec": spec, "preproc": pre, "members": members, "n_train_rows": int(cx.n),
          "n_train_positives": int(cx.y.sum()), "evaluate_sha256": SHA,
          "info": {"setting": sid, "setting_ko": s["ko"], "relax": relax, "fitted_at": time.strftime("%Y-%m-%d %H:%M")}}
    score = FM.score(t7, cx.feats)
    model = t7
    if s["rf"] > 0:
        pre32 = pre if kstore == 32 else {r: FM.fit_robust(cx.feats[r], kmax=32) for r in cx.reps}
        X = np.hstack([FM.embed(pre32[rep], cx.feats[rep])[:, :k] for rep, k in RF.RF_REPS]).astype(np.float32)
        rf = RF.fit_rf(X, cx.y, RF.member1_weights(cx.y, cx.src, cx.cells), RF_MSL, RF.RF_PARAMS)
        p_tr = RF.rf_proba(rf, X)
        score = (1 - s["rf"]) * score + s["rf"] * M6.train_percentile(p_tr, p_tr)
        model = {"format": "argus-v-p-rf/1", "t7a": t7, "rf": rf, "rf_preproc": pre32, "rf_weight": s["rf"],
                 "rf_train_scores_sorted": np.sort(p_tr), "rf_reps": [list(x) for x in RF.RF_REPS]}
    path = OUT / "model" / "argus_v_p.pkl"
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "wb") as h:
        pickle.dump(model, h, protocol=4)
    sha = hashlib.sha256(path.read_bytes()).hexdigest()
    return {"path": str(path.relative_to(REPO_ROOT)).replace("\\", "/"), "sha256": sha, "bytes": path.stat().st_size,
            "in_sample_within_tool": float(cx.wt(score)["value"])}


def cmd_run():
    OUT.mkdir(parents=True, exist_ok=True)
    REPORT.mkdir(parents=True, exist_ok=True)
    cx = Ctx()
    log("rows", cx.n, "violations", int(cx.y.sum()), "seen-scenario groups", cx.clone_info)
    start_checks(cx)
    res_path = OUT / "results.json"
    res = json.loads(res_path.read_text(encoding="utf-8")) if res_path.is_file() else {}
    res.update({"evaluate_sha256": SHA, "rows": cx.n, "violations": int(cx.y.sum()), "seeds": list(SEEDS),
                "seen_scenario_grouping": cx.clone_info, "settings": SETTINGS})
    res.setdefault("results", {})

    def save():
        res_path.write_text(json.dumps(E.to_jsonable(res), indent=1, ensure_ascii=False), encoding="utf-8")

    for cond in ("C", "B", "A"):
        for sid in SETTINGS:
            r = res["results"].setdefault(sid, {})
            if cond in r:
                continue
            t0 = time.time()
            r[cond] = in_sample(cx, sid) if cond == "C" else summarise(cx, run_cv(cx, sid, cond))
            log(f"{sid} condition {cond}: {r[cond]['value']:.4f}  ({SETTINGS[sid]['ko']}, {time.time() - t0:.0f}s)")
            save()
    # pick Argus-V-p: highest condition B, ties within 0.005 -> smaller number (rule fixed in the README)
    order = sorted(SETTINGS, key=lambda k: -res["results"][k]["B"]["value"])
    best = res["results"][order[0]]["B"]["value"]
    chosen = sorted(k for k in SETTINGS if best - res["results"][k]["B"]["value"] <= 0.005)[0]
    res["chosen"] = {"setting": chosen, "rule": "max condition B, ties within 0.005 -> smaller number"}
    log("chosen", chosen, SETTINGS[chosen]["ko"])
    save()
    # condition C ladder for the chosen setting if below 0.9 (at most 2 extra fits, all reported)
    relax = SETTINGS[chosen]["relax"]
    ladder = res.setdefault("ladder_C", [{"relax": relax, "value": res["results"][chosen]["C"]["value"]}])
    while ladder[-1]["value"] < 0.9 and ladder[-1]["relax"] < 3 and len(ladder) < 3:
        nxt = max(2, ladder[-1]["relax"] + 1)
        v = in_sample(cx, chosen, relax=nxt)
        ladder.append({"relax": nxt, "value": v["value"], "per_cell": v["per_cell"]})
        log(f"ladder C {chosen} relax {nxt}: {v['value']:.4f}")
        save()
    if "shuffle_check_B" not in res:
        res["shuffle_check_B"] = {"setting": chosen, **shuffle_check(cx, chosen)}
        save()
    if "export" not in res:
        res["export"] = export(cx, chosen, relax)
        log("export", res["export"])
        save()
    assert E.evaluate_sha256() == SHA
    (REPORT / "results.json").write_text(json.dumps(E.to_jsonable(res), indent=1, ensure_ascii=False), encoding="utf-8")
    log("DONE")


def cmd_report():
    res = json.loads((OUT / "results.json").read_text(encoding="utf-8"))
    L = ["| 설정 | A. 처음 보는 시나리오 | B. 이미 본 시나리오의 새 실행 | C. 학습 데이터 재채점 |", "|---|---|---|---|"]
    for sid, s in res["settings"].items():
        r = res["results"][sid]
        L.append(f"| {sid} {s['ko']} | {r['A']['value']:.3f} | {r['B']['value']:.3f} | {r['C']['value']:.3f} |")
    print("\n".join(L))
    print(json.dumps({k: res.get(k) for k in ("chosen", "ladder_C", "shuffle_check_B", "export")}, ensure_ascii=False, indent=1))


def cmd_visible():
    """Re-score every setting / condition on the user's 0.90 target (decision 2026-11-15): violations whose deciding
    fact was explicit in the context before the call. Flags: reports/risk-loop/argus-v-p/visible_flag.json (rule in
    visible_flag_rule.py, provisional). Conditions A and B reuse the saved scores; condition C refits on all rows
    (same fits as the run). Nothing is selected here."""
    cx = Ctx()
    flag = json.loads((REPORT / "visible_flag.json").read_text(encoding="utf-8"))
    vis = np.zeros(cx.n, bool)
    for r in flag["violations"]:
        i = int(r["pos"])
        assert cx.y[i] == 1 and str(cx.rows.unit_id[i]) == r["unit_id"] and int(cx.rows.step_index[i]) == r["step_index"]
        vis[i] = bool(r["visible"])
    keep = (cx.y == 0) | vis          # every normal + the visible violations (other violations are left out)

    def wtv(scores, min_pos=3):
        s = np.asarray(scores, dtype=np.float64)
        return E.within_tool_auroc(s[keep], cx.y[keep], cx.groups[keep], min_pos=min_pos)

    def block(score_list):
        out = {}
        for mp in (3, 2):
            rs = [wtv(s, mp) for s in score_list]
            out[f"min{mp}"] = {"value": float(np.mean([r["value"] for r in rs])), "cells": rs[0]["n_tools"],
                               "violations": rs[0]["n_positives_included"]}
        per = {}
        for e in wtv(score_list[0], 2)["per_tool"]:
            if e["included"]:
                m = keep & (cx.groups == e["tool"])
                per[e["tool"]] = {"violations": e["positives"], "normals": e["negatives"],
                                  "auroc": float(np.mean([H.auroc(np.asarray(s)[m], cx.y[m]) for s in score_list]))}
        out["per_cell_min2"] = per
        return out

    step = np.asarray(cx.rows.step_index, dtype=np.float64)
    res = {"rule": flag["rule_version"], "visible_violations": int(vis.sum()),
           "unique_feature_rows_among_visible": int(len(set(cx.hashes[vis].tolist()))),
           "all_judged_cell_violations": len(flag["violations"]), "settings": {}}
    t7 = np.load(ART / "iter12_remeasure" / "oof_v2_T7-a_seed0-9.npy")
    assert t7.shape[1] == cx.n
    res["T7-a unseen scenario (saved, 10 splits)"] = block(list(t7))
    res["order rule (earlier step = violation)"] = block([-step])
    allpos = np.arange(cx.n)
    for sid in SETTINGS:
        r = {}
        for cond in ("A", "B"):
            r[cond] = block([np.load(oof_path(sid, cond, s)) for s in SEEDS])
        tr, _ = cx.fit(sid, allpos, cx.y, np.zeros(0, np.int64))
        r["C"] = block([tr])
        res["settings"][sid] = r
        log(sid, {c: round(r[c]["min3"]["value"], 4) for c in ("A", "B", "C")}, "cells", r["A"]["min3"]["cells"],
            "violations", r["A"]["min3"]["violations"])
    (REPORT / "visible_results.json").write_text(json.dumps(E.to_jsonable(res), indent=1, ensure_ascii=False), encoding="utf-8")
    for k in ("T7-a unseen scenario (saved, 10 splits)", "order rule (earlier step = violation)"):
        log(k, {m: round(res[k][m]["value"], 4) for m in ("min3", "min2")})
    log("DONE visible", res["visible_violations"], "visible violations,", res["unique_feature_rows_among_visible"], "unique")


if __name__ == "__main__":
    cmds = {"run": cmd_run, "report": cmd_report, "visible": cmd_visible}
    if len(sys.argv) < 2 or sys.argv[1] not in cmds:
        raise SystemExit("usage: argus_v_p.py run | report | visible")
    cmds[sys.argv[1]]()

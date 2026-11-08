"""Iteration 4 diagnostics D4-1, D4-2, D4-3 (train only; not model tries). Plan: reports/.../iter-04/plan.md.

  shuffles : re-run the v4 shuffle procedure for the iteration-2 reference H2-1c-L23 (grid entry used by the
             harness shuffle, index 5 = k 32, C 0.1) and SAVE the OOF scores: (b) source x family x20,
             (a) source x20. Also length+step baseline OOF (3 seeds, harness folds).
  report   : D4-1 (what the shuffled scores track; scenario/condition codes read for diagnosis only),
             D4-2 (cell anatomy), D4-3 (within-trajectory ranking AUROC preview) -> artifacts/iter04/diag.json

Usage: py -3.11 experiments/risk_loop/argus_loop/iter04_diag.py shuffles|report
"""
from __future__ import annotations

import json
import os
import sys
import time
from collections import Counter
from pathlib import Path

for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ.setdefault(_v, "2")

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402
from experiments.risk_loop.argus_loop import iter01_common as C1  # noqa: E402
from experiments.risk_loop.argus_loop import iter02_common as C2  # noqa: E402
from experiments.risk_loop.argus_loop import iter04_common as C4  # noqa: E402
from experiments.risk_loop.argus_loop import models as M  # noqa: E402

ART = REPO_ROOT / "artifacts" / "risk-loop" / "argus-v1-loop"
OUT = ART / "iter04"
H21C_GRID5 = {"k": 32, "C": 0.1}
V4_SHUF_B_REF = 0.5905098889931206  # iter-02/eval-v4.json shuffle_source_family.within_tool_mean
N = 20


def cmd_shuffles():
    OUT.mkdir(parents=True, exist_ok=True)
    data, rows, _ = C1.headline_data()
    X, _ = C2.representation(data, rows, "L23:max")
    ctx = C2.ctx_for(rows)
    fp = M.grid_maker("tool_weighted_logreg", X, ctx, {"kmax": 128}, M.LRU(8))(H21C_GRID5)
    g = E.headline_groups(rows)
    for tag, within in (("b", ("source", "family")), ("a", ("source",))):
        t0 = time.time()
        oofs = C4.shuffle_oofs(fp, rows, N, within)
        np.save(OUT / f"shuf_{tag}_H2-1c.npy", np.asarray(oofs))
        vals = [E.within_tool_auroc(o, rows.y, g)["value"] for o in oofs]
        print(tag, "mean", float(np.mean(vals)), "sec", round(time.time() - t0), flush=True)
        if tag == "b":
            print("matches v4 harness (b) mean:", abs(np.mean(vals) - V4_SHUF_B_REF) < 1e-9, flush=True)
    fpb, B = E.baseline_designs(rows)["length+step"]
    cv = E.run_cv(fpb, B, rows)
    np.save(OUT / "oof_length+step.npy", np.asarray([cv["oof"][k] for k in sorted(cv["oof"])]))
    print("DONE", flush=True)


def group_mean_fp(X, ctx, group_all, k=32, C=0.1):
    """Diagnostic null: inside the training fold, replace each training row's PCA embedding by the mean
    embedding of its group (source x family, or trajectory) and fit a source x class weighted LogReg on the
    real labels. Only group-level information can be learned; test rows are scored on their own embedding.
    ``group_all`` is read at pos_train only."""
    cache = M.LRU(4)
    g_all = np.asarray(group_all).astype(str)

    def fp(pos_train, y_train, pos_test):
        pos_train = np.asarray(pos_train, dtype=np.int64)
        key = M._key(pos_train, "gm")
        Emb = cache.get(key)
        if Emb is None:
            Emb = M.pca_embed(X, pos_train, k, ctx=ctx)
            cache.put(key, Emb)
        Etr = Emb[pos_train].astype(np.float64)
        Gm = C4_group_mean(Etr, g_all[pos_train])
        w = M.sample_weights(y_train, np.asarray(ctx["source"])[pos_train], "source_class")
        return M._logreg_scores(Gm, y_train, Emb[np.asarray(pos_test)].astype(np.float64), C, w)

    return fp


def C4_group_mean(E_, g):
    out = np.empty_like(E_)
    for t in np.unique(g):
        m = g == t
        out[m] = E_[m].mean(0)
    return out


def cmd_nulls():
    """Group-level-only nulls (family / trajectory mean features, real labels) + tool-identity baseline OOF."""
    data, rows, _ = C1.headline_data()
    X, _ = C2.representation(data, rows, "L23:max")
    ctx = C2.ctx_for(rows)
    fam = np.asarray([f"{s}|{f}" for s, f in zip(rows.source.astype(str), rows.family.astype(str))], dtype=object)
    for tag, grp in (("famMean", fam), ("trajMean", rows.trajectory_id.astype(str))):
        cv = E.run_cv(group_mean_fp(X, ctx, grp), None, rows)
        np.save(OUT / f"oof_null_{tag}.npy", np.asarray([cv["oof"][k] for k in sorted(cv["oof"])]))
        print(tag, E._mean([E.within_tool_auroc(np.asarray(cv["oof"][k]), rows.y, E.headline_groups(rows))["value"]
                            for k in sorted(cv["oof"])]), flush=True)
    fpt, T = E.baseline_designs(rows)["tool_identity"]
    cv = E.run_cv(fpt, T, rows)
    np.save(OUT / "oof_tool_identity.npy", np.asarray([cv["oof"][k] for k in sorted(cv["oof"])]))
    print("DONE", flush=True)


def cmd_nulleval():
    """v4 evaluate() of the trajectory-mean null (fixed k 32, C 0.1 -> 1-entry grid), to see how the frozen
    shuffle (b) treats a rollout-level-only model. Diagnostic, not a candidate (settings copied from H2-1c)."""
    data, rows, _ = C1.headline_data()
    X, _ = C2.representation(data, rows, "L23:max")
    ctx = C2.ctx_for(rows)
    grp = rows.trajectory_id.astype(str)
    r = E.evaluate(make_fit_predict=lambda g: group_mean_fp(X, ctx, grp, **g), grid=[H21C_GRID5], rows=rows,
                   name="null-trajMean", include_oof=False)
    r["cv"].pop("folds", None)
    (OUT / "null_trajMean.full.json").write_text(json.dumps(E.to_jsonable(r), indent=1), encoding="utf-8")
    print("trajMean", r["metrics"]["within_tool"]["value"], "shufB", r["shuffle_source_family"]["within_tool_mean"],
          "shufA", r["shuffle_source"]["within_tool_mean"], "margin", r["gate"]["shuffle_family_margin"], flush=True)
    print("DONE", flush=True)


def _r(x, d=3):
    return None if x is None else round(float(x), d)


def cmd_report():
    data, rows, _ = C1.headline_data()
    all_rows = E.load(include_report_content=True).rows  # train only, report-tool rows included
    all_rows = all_rows.subset(np.nonzero(~np.isnan(all_rows.label))[0])
    y = rows.y
    g = E.headline_groups(rows)
    meta = C4.diag_meta(rows)  # DIAGNOSIS ONLY
    cells = C4.eligible_cells(rows)
    other_pos = C4.traj_positive_counts(rows.trajectory_id, y)
    other_pos_full = C4.full_traj_positive(rows, all_rows)
    out = {"evaluate_sha256": E.evaluate_sha256(), "cells": cells}

    # ---------------- D4-2 anatomy
    anat = []
    npos_total = int(sum((y[g == c] == 1).sum() for c in cells))
    for c in cells:
        idx = np.nonzero(g == c)[0]
        ip, ineg = idx[y[idx] == 1], idx[y[idx] == 0]
        nt = C4.negative_type(rows, meta, other_pos, ip, ineg)
        side = lambda ii: {"scenarios": sorted(set(meta["scenario"][ii].tolist())),  # noqa: E731
                           "conditions": dict(Counter(meta["condition"][ii].tolist())),
                           "families": len(set(rows.family[ii].tolist())),
                           "trajectories": len(set(rows.trajectory_id[ii].tolist()))}
        anat.append({"cell": c, "source": c.split("|")[1], "tool": c.split("|")[0], "n_pos": len(ip),
                     "n_neg": len(ineg), "weight": len(ip) / npos_total, "pos": side(ip), "neg": side(ineg),
                     "neg_by_type": {t: int((nt == t).sum()) for t in C4.NEG_TYPES},
                     "neg_in_violating_traj": int((other_pos[ineg] > 0).sum()),
                     "neg_in_violating_traj_incl_report": int((other_pos_full[ineg] > 0).sum()),
                     "pos_step": sorted(rows.step_index[ip].astype(int).tolist()),
                     "neg_step": sorted(rows.step_index[ineg].astype(int).tolist())})
    out["D4_2_anatomy"] = anat
    out["D4_2_totals"] = {"rows_in_cells": int(sum(a["n_pos"] + a["n_neg"] for a in anat)),
                          "pos": npos_total, "neg": int(sum(a["n_neg"] for a in anat)),
                          "neg_in_violating_traj": int(sum(a["neg_in_violating_traj"] for a in anat)),
                          "neg_by_type": {t: int(sum(a["neg_by_type"][t] for a in anat)) for t in C4.NEG_TYPES}}

    # ---------------- D4-1 single-variable AUROC inside cells (vs the true label)
    lp = np.log(np.clip(rows.prefix_length, 1, None))
    st = np.nan_to_num(rows.step_index)
    var = {}
    for name, fn in (("step_index", lambda ii: C4.auc(st[ii], y[ii])),
                     ("prefix_length", lambda ii: C4.auc(lp[ii], y[ii])),
                     ("traj_has_other_violation", lambda ii: C4.auc(other_pos[ii] > 0, y[ii])),
                     ("traj_has_other_violation_incl_report", lambda ii: C4.auc(other_pos_full[ii], y[ii])),
                     ("traj_contains_violation_incl_self (rollout oracle)",
                      lambda ii: C4.auc(((other_pos[ii] > 0) | (y[ii] == 1)).astype(int), y[ii])),
                     ("condition_oracle", lambda ii: C4.oracle_categorical_auc(meta["condition"][ii], y[ii])),
                     ("scenario_oracle", lambda ii: C4.oracle_categorical_auc(meta["scenario"][ii], y[ii])),
                     ("trajectory_oracle", lambda ii: C4.oracle_categorical_auc(rows.trajectory_id[ii], y[ii]))):
        per = {}
        for c in cells:
            idx = np.nonzero(g == c)[0]
            per[c] = fn(idx)
        var[name] = {"per_cell": {k: _r(v) for k, v in per.items()},
                     "weighted": _r(C4.weighted([(per[c], int(y[g == c].sum())) for c in cells]))}
    out["D4_1_single_variable"] = var

    # ---------------- score sets
    sets = {"H2-1c (real labels)": np.load(ART / "iter02" / "oof_H2-1c-L23.full.npy"),
            "H1-0a (Argus-V1 default)": np.load(ART / "iter01" / "oof_H1-0a.scan.npy"),
            "length+step": np.load(OUT / "oof_length+step.npy")}
    for t, f in (("null: family-mean features", "oof_null_famMean.npy"),
                 ("null: trajectory-mean features", "oof_null_trajMean.npy"), ("tool_identity", "oof_tool_identity.npy")):
        if (OUT / f).is_file():
            sets[t] = np.load(OUT / f)
    for t in ("T4-1a", "T4-1b"):
        p = OUT / f"oof_{t}.full.npy"
        if p.is_file():
            sets[t] = np.load(p)
    shuf = {"shuffle(b) H2-1c": np.load(OUT / "shuf_b_H2-1c.npy"),
            "shuffle(a) H2-1c": np.load(OUT / "shuf_a_H2-1c.npy")}

    # D4-1: decomposition by negative type, for real-label sets (seed mean of per-seed values) and shuffles
    def decomp(oofs):
        ds = [C4.cell_decomposition(o, rows, meta, other_pos, cells) for o in oofs]
        w = {k: _r(E._mean([d["weighted"][k] for d in ds])) for k in ds[0]["weighted"]}
        per = {c: {k: _r(E._mean([d["per_cell"][c][k] for d in ds])) for k in ("all",) + C4.NEG_TYPES}
               for c in cells}
        return {"weighted": w, "weighted_n_pos": ds[0]["weighted_n_pos"], "per_cell": per}

    out["D4_1_decomposition"] = {k: decomp(v) for k, v in {**sets, **shuf}.items()}

    # D4-1: what do shuffled scores track among cell negatives / within cells
    track = {}
    for k, O in shuf.items():
        rec = {"neg_viol_traj_vs_clean": [], "spearman_step": [], "spearman_len": [], "cond_mean_rank": []}
        for o in O:
            vals, sp_s, sp_l = [], [], []
            for c in cells:
                idx = np.nonzero(g == c)[0]
                ineg = idx[y[idx] == 0]
                a = C4.auc(o[ineg], (other_pos[ineg] > 0).astype(int))
                vals.append((a, int(y[idx].sum())))
                sp_s.append((E._spearman(o[idx], st[idx]), int(y[idx].sum())))
                sp_l.append((E._spearman(o[idx], lp[idx]), int(y[idx].sum())))
            rec["neg_viol_traj_vs_clean"].append(C4.weighted(vals))
            rec["spearman_step"].append(C4.weighted(sp_s))
            rec["spearman_len"].append(C4.weighted(sp_l))
        track[k] = {kk: {"mean": _r(np.mean([v for v in vv if v is not None])), "values": [_r(v) for v in vv]}
                    for kk, vv in rec.items() if vv}
        # per-cell within-cell AUROC of each shuffle, and mean score by condition (cells pooled, ranked in cell)
        cond_rank = {}
        for o in O:
            for c in cells:
                idx = np.nonzero(g == c)[0]
                from scipy.stats import rankdata
                rk = (rankdata(o[idx]) - 0.5) / len(idx)
                for i, r_ in zip(idx, rk):
                    cond_rank.setdefault(meta["condition"][i], []).append(r_)
        track[k]["within_cell_rank_by_condition"] = {c: _r(np.mean(v)) for c, v in sorted(cond_rank.items())}
        track[k]["within_tool_values"] = [_r(E.within_tool_auroc(o, y, g)["value"]) for o in O]
        track[k]["within_tool_mean"] = _r(np.mean([E.within_tool_auroc(o, y, g)["value"] for o in O]), 4)
    # label rate by condition inside cells (reference for the rank table)
    cond_rate = {}
    for c in cells:
        idx = np.nonzero(g == c)[0]
        for i in idx:
            cond_rate.setdefault(meta["condition"][i], []).append(y[i])
    out["D4_1_condition_label_rate_in_cells"] = {c: {"n": len(v), "rate": _r(np.mean(v))}
                                                 for c, v in sorted(cond_rate.items())}
    out["D4_1_shuffle_tracking"] = track

    # ---------------- D4-3 within-trajectory ranking AUROC
    in_cells = np.isin(g, cells)
    tt = np.asarray([f"{a}|{b}" for a, b in zip(rows.trajectory_id.astype(str), rows.tool.astype(str))], dtype=object)
    trj = rows.trajectory_id.astype(str)
    d43 = {}
    for k, O in {**sets, **shuf}.items():
        rec = {}
        for scope, keep, key in (("cells", in_cells, trj), ("all_headline", None, trj),
                                 ("all_headline_same_tool", None, tt)):
            w = C4.within_traj_multi(list(O), rows, keep, key)
            if k in sets:
                w["ci95"] = C4.within_traj_bootstrap(list(O), rows, keep, traj=key)
            else:  # shuffles: list of 20 single runs; report mean/SD of the per-run value
                vals = [C4.within_traj_auroc(o, y, key, keep)["value"] for o in O]
                w = {**{kk: w[kk] for kk in ("n_trajectories", "n_positives", "n_negatives", "n_pairs")},
                     "value": float(np.mean(vals)), "sd": float(np.std(vals, ddof=1)),
                     "se": float(np.std(vals, ddof=1) / np.sqrt(len(vals)))}
            rec[scope] = w
        if k in sets:
            rec["headline_within_tool"] = _r(E._mean([E.within_tool_auroc(o, y, g)["value"] for o in O]), 4)
        d43[k] = rec
    out["D4_3_within_trajectory"] = d43
    # agreement of shuffle(b) scores with the real-label H2-1c scores (fold seed 0 = shuffle fold seed)
    real0 = sets["H2-1c (real labels)"][0]
    sb = shuf["shuffle(b) H2-1c"]
    out["D4_1_shuffle_vs_real_spearman"] = {
        "all_headline_rows_mean_over_20": _r(np.mean([E._spearman(o, real0) for o in sb])),
        "mean_shuffle_score_vs_real": _r(E._spearman(sb.mean(0), real0)),
        "within_cells_weighted_mean_shuffle_score_vs_real": _r(C4.weighted(
            [(E._spearman(sb.mean(0)[g == c], real0[g == c]), int(y[g == c].sum())) for c in cells])),
        "shuffle_a_all_rows_mean_over_20": _r(np.mean([E._spearman(o, real0) for o in shuf["shuffle(a) H2-1c"]]))}
    print("spearman", out["D4_1_shuffle_vs_real_spearman"])
    (OUT / "diag.json").write_text(json.dumps(E.to_jsonable(out), indent=1, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(E.to_jsonable({"totals": out["D4_2_totals"], "single": {k: v["weighted"] for k, v in var.items()},
                                    "decomp": {k: v["weighted"] for k, v in out["D4_1_decomposition"].items()},
                                    "track": {k: {kk: (vv["mean"] if isinstance(vv, dict) and "mean" in vv else vv)
                                                  for kk, vv in v.items() if kk != "within_tool_values"}
                                              for k, v in track.items()},
                                    "d43": {k: {s: {kk: vv for kk, vv in w.items() if kk in ("value", "pair_value", "n_trajectories", "n_positives", "n_negatives", "sd", "ci95")}
                                                for s, w in v.items() if isinstance(w, dict)} for k, v in d43.items()}}),
                     indent=1, ensure_ascii=False))


if __name__ == "__main__":
    {"shuffles": cmd_shuffles, "nulls": cmd_nulls, "nulleval": cmd_nulleval, "report": cmd_report}[sys.argv[1]]()

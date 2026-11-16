"""Class-weight check for the 64-dimension Argus-V-em model: does a larger weight on the rare violation rows change it?

Plan (fixed before running): reports/risk-loop/argus-v-em300/class-weight-check.md.
User, 2026-11-16: "학습할 때 훨씬 작은것이 나온 데이터에 대해 가중치를 크게 주어야지 의료쪽 모델이나 정답이 극히 적은 분야에서
하는 것 처럼"; the plan was shown and approved ("시작해").

Only the weight of one positive row in the loss changes. Everything else is the Argus-V-em300 training of the
64-dimension model: same rows, sampling, folds, seeds, optimiser and dropout; 100 epochs, recorded per epoch.

  baseline  min(20, sqrt(neg / pos))   about 15    not trained again: read from artifacts/.../argus-v-em300/epochs/EM64.npz
  w075      (neg / pos) ** 0.75        about 60
  w100      neg / pos                  about 230   positives and negatives carry the same total weight

One extra fit (baseline weight, split seed 0, fold 0) runs first and must reproduce the saved scores exactly; this
shows that the code path differs from the saved run in the weight only.

Train split only: these are cross-validation scores inside train. The test split (scored once already) and the
validation split are not read, and no all-rows model is exported.

Training starts only with --approved.
Usage : PYTHONUTF8=1 py -3.11 -u experiments/risk_loop/argus_loop/argus_v_em_weight_check.py --approved
        PYTHONUTF8=1 py -3.11 experiments/risk_loop/argus_loop/argus_v_em_weight_check.py diag        (no training)
        PYTHONUTF8=1 py -3.11 experiments/risk_loop/argus_loop/argus_v_em_weight_check.py figure      (no training)
Output: artifacts/risk-loop/argus-v-em300/class_weight_check/<setting>/EM64.npz   (ignored)
        reports/risk-loop/argus-v-em300/class_weight_check.json, class_weight_check_diag.json, figures_weight/*.png
"""
from __future__ import annotations

import json
import os
import platform
import sys
import time
from pathlib import Path

for _name in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):   # as argus_v_em.py, before numpy/torch
    os.environ.setdefault(_name, "2")

import numpy as np  # noqa: E402
import torch  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from experiments.risk_loop import harness as H  # noqa: E402
from experiments.risk_loop.argus_loop import argus_v_em as EM  # noqa: E402
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402

EPOCHS = 100
MAIN_EPOCH = 67                              # epoch of the current main model (picked on cross-validation, EM64)
EM.EPOCHS = EPOCHS                           # length of the recorded training; nothing else about the fit depends on it
from experiments.risk_loop.argus_loop import argus_v_em_epochs as EP  # noqa: E402

MODEL = "EM64"
OUT = ROOT / "artifacts" / "risk-loop" / "argus-v-em300" / "class_weight_check"
REPORT = ROOT / "reports" / "risk-loop" / "argus-v-em300"
BASE_NPZ = ROOT / "artifacts" / "risk-loop" / "argus-v-em300" / "epochs" / f"{MODEL}.npz"
BASELINE_RULE = EP.class_weight              # min(20, sqrt(neg / pos))
SETTINGS = {
    "w075": {"ko": "가중치 약 60배", "rule": "(neg / pos) ** 0.75", "fn": lambda neg, pos: float((neg / pos) ** 0.75)},
    "w100": {"ko": "가중치 약 230배", "rule": "neg / pos", "fn": lambda neg, pos: float(neg / pos)},
    # added on the user's instruction 2026-11-16 ("위반 가중치를 300배로 하고 한 번 학습 및 test를 진행해 보자"): fixed in every fit
    "w300": {"ko": "가중치 300배", "rule": "300 (fixed)", "fn": lambda neg, pos: 300.0},
    # added on the user's instruction 2026-11-16 ("위험 가중치에 대해 1000배를 해보자"): fixed in every fit
    "w1000": {"ko": "가중치 1000배", "rule": "1000 (fixed)", "fn": lambda neg, pos: 1000.0},
}
BASE_KO = "기준: 가중치 약 15배"
MARKS = (10, 20, 30, 40, 50, 60, 67, 80, 100)
SAME = 0.02                                  # plan: a main-metric difference within this reads as "no difference"
EPOCH_KEYS = ("loss_optimised", "loss_train_eval", "loss_heldout", "auroc_train_min3", "grad_norm", "weight_norm")
log, r6 = EP.log, EP.r6


def reproduce_one_fit(cx, X, vis, train_rows, base_oof):
    """Baseline weight, split seed 0, fold 0: the held-out scores must equal the saved Argus-V-em300 ones."""
    seed, fold_i = EM.SEEDS[0], 0
    tr, te = list(E.make_folds(cx.rows, 5, seed))[fold_i]
    fit = EM.sample_training_rows(cx, tr[train_rows[tr]], vis, 710000 + seed * 100 + fold_i)
    y_fit = vis[fit].astype(np.int64)
    EP.class_weight = BASELINE_RULE
    t0 = time.time()
    *_, pw, _, _, extra = EP.fit_logged(X[fit], y_fit, EP.MODELS[MODEL], EP.model_seed(MODEL, seed, fold_i), {"heldout": X[te]})
    diff = float(np.max(np.abs(extra["heldout"].astype(np.float64) - base_oof[0][:, te].astype(np.float64))))
    log(f"reproduction fit: rows={len(fit)} visible={int(y_fit.sum())} weight={pw:.3f} | largest difference from the "
        f"saved held-out scores over {EPOCHS} epochs = {diff} | {time.time() - t0:.1f}s")
    if diff > 1e-6:
        raise SystemExit("The baseline fit does not reproduce the saved scores: stopping before any new training.")
    return {"seed": int(seed), "fold": fold_i, "rows": int(len(fit)), "visible": int(y_fit.sum()), "pos_weight": float(pw),
            "max_abs_diff_vs_saved": diff}


def curves(cx, vis, masks, oof):
    """Cross-validation scores of every row [seed][epoch][row] -> each metric [seed][epoch]."""
    S, n_ep = oof.shape[:2]
    everything = np.ones(cx.n, dtype=bool)
    f3, f2, fall = EP.FastWT(cx, masks["min3"], 3), EP.FastWT(cx, masks["min2"], 2), EP.FastWT(cx, everything, 3)
    target = (cx.y == 0) | vis                                   # normal calls + violations whose reason was visible
    y_vis = vis[target].astype(np.int64)
    out = {k: np.zeros((S, n_ep)) for k in ("min3", "min2", "all_same_tool", "pooled_all", "pooled_visible", "logloss_unweighted")}
    for si in range(S):
        for e in range(n_ep):
            s = oof[si, e].astype(np.float64)
            out["min3"][si, e], out["min2"][si, e], out["all_same_tool"][si, e] = f3(s), f2(s), fall(s)
            out["pooled_all"][si, e] = H.auroc(s, cx.y)
            out["pooled_visible"][si, e] = H.auroc(s[target], y_vis)
            out["logloss_unweighted"][si, e] = EP.bce(s[target], y_vis, 1.0)
    return out


def summarise(c, d, cells3):
    m3 = c["min3"].mean(0)
    tr = np.nanmean(d["auroc_train_min3"], axis=(0, 1))          # [epoch]
    full = np.flatnonzero(tr >= 0.9995)
    cell = d["cell_auroc_heldout"].mean(0)                       # [epoch][cell]
    return {
        "per_epoch_mean": {k: r6(v.mean(0)) for k, v in c.items()},
        "per_epoch_per_seed": {k: r6(c[k]) for k in ("min3", "min2", "pooled_all")},
        "at_epoch": {str(e): {k: {"mean": float(v[:, e - 1].mean()), "per_seed": r6(v[:, e - 1])} for k, v in c.items()} for e in MARKS},
        "peak_min3": {"epoch": int(m3.argmax()) + 1, "value": float(m3.max())},
        "train_rows_auroc_min3_per_epoch": r6(tr),
        "train_rows_auroc_reaches_1_at_epoch": int(full[0]) + 1 if len(full) else None,
        "per_epoch_fit_mean": {k: r6(np.nanmean(d[k], axis=(0, 1))) for k in EPOCH_KEYS},
        "cell_auroc": {str(e): {c_.split("|")[0]: float(cell[e - 1, i]) for i, c_ in enumerate(cells3)} for e in (MAIN_EPOCH, EPOCHS)},
        "per_fit": {"pos_weight": r6(d["meta_pos_weight"]), "rows": r6(d["meta_n_fit"]), "visible": r6(d["meta_n_pos"]),
                    "seconds": r6(d["meta_seconds"])},
        "pos_weight_range": [float(np.min(d["meta_pos_weight"])), float(np.mean(d["meta_pos_weight"])), float(np.max(d["meta_pos_weight"]))],
    }


def baseline_slices(base):
    """The saved 300-epoch record of the same model, cut to the first EPOCHS epochs."""
    d = {k: base[k][..., :EPOCHS] for k in EPOCH_KEYS}                      # [seed][fold][epoch]
    d["cell_auroc_heldout"] = base["cell_auroc_heldout"][:, :EPOCHS]        # [seed][epoch][cell]
    for k in ("meta_pos_weight", "meta_n_fit", "meta_n_pos", "meta_seconds"):
        d[k] = base[k]
    return d


def train(argv):
    if "--approved" not in argv:
        raise SystemExit("This script trains models. Run it only after the user approved it: add --approved.")
    OUT.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    cx = EM.Ctx()
    vis, rule = EM.visible_mask(cx)
    X, train_rows, eval_rows, eligible = EM.prepare(cx, vis)
    cells3 = sorted(k for k, v in eligible.items() if v["min3"])
    cells2 = sorted(k for k, v in eligible.items() if v["min2"])
    masks = {"min3": eval_rows & np.isin(cx.groups, cells3), "min2": eval_rows & np.isin(cx.groups, cells2)}
    log(f"class-weight check: rows={cx.n} target_rows={int(train_rows.sum())} visible={int(vis.sum())} input={X.shape} "
        f"epochs={EPOCHS} model={MODEL} rule={rule}")
    base = np.load(BASE_NPZ, allow_pickle=False)
    base_oof = base["oof"][:, :EPOCHS]                            # [seed][epoch][row]
    res = {"name": "Argus-V-em class-weight check", "plan": "reports/risk-loop/argus-v-em300/class-weight-check.md",
           "model": MODEL, "width": EP.MODELS[MODEL], "epochs": EPOCHS, "main_epoch": MAIN_EPOCH, "rule": rule,
           "seeds": list(EM.SEEDS), "folds": 5, "cells_min3": cells3, "cells_min2": cells2,
           "rows": int(cx.n), "violations": int(cx.y.sum()), "visible_violations": int(vis.sum()),
           "scores": "cross-validation inside the train split (scenario-family folds); test and validation were not read",
           "same_if_within": SAME,
           "metrics": {"min3": "same-tool AUROC, visible violations, cells with >=3 (main metric)",
                       "min2": "same, cells with >=2", "all_same_tool": "same-tool AUROC, all violations",
                       "pooled_all": "all calls, tools mixed, normal vs any violation",
                       "pooled_visible": "all normal calls + visible violations, tools mixed",
                       "logloss_unweighted": "binary cross entropy without class weight on normal + visible rows"},
           "run": {"started_at": time.strftime("%Y-%m-%d %H:%M:%S"), "python": sys.version.split()[0], "torch": torch.__version__,
                   "numpy": np.__version__, "platform": platform.platform(), "torch_threads": 2, "device": "cpu",
                   "script": "experiments/risk_loop/argus_loop/argus_v_em_weight_check.py"},
           "reproduction_fit": reproduce_one_fit(cx, X, vis, train_rows, base_oof), "settings": {}}
    c0 = curves(cx, vis, masks, base_oof)
    saved = base["auroc_heldout_min3"][:, :EPOCHS]
    assert float(np.max(np.abs(c0["min3"] - saved))) < 1e-12, "the metric code must give back the saved baseline curve"
    res["settings"]["baseline"] = {"ko": BASE_KO, "weight_rule": "min(20, sqrt(neg / pos))", "trained_here": False,
                                   "source": str(BASE_NPZ.relative_to(ROOT)).replace("\\", "/"),
                                   **summarise(c0, baseline_slices(base), cells3)}
    log("baseline (saved record)", "main metric at epoch", MAIN_EPOCH, round(float(c0["min3"][:, MAIN_EPOCH - 1].mean()), 4),
        "| all calls", round(float(c0["pooled_all"][:, MAIN_EPOCH - 1].mean()), 4))
    for tag, cfg in SETTINGS.items():
        EP.class_weight = cfg["fn"]
        EP.OUT = OUT / tag
        EP.OUT.mkdir(parents=True, exist_ok=True)
        assert EP.OUT.parent == OUT
        d = EP.run_model(MODEL, cx, X, vis, train_rows, masks, cells3, cells2)
        c = curves(cx, vis, masks, d["oof"])
        res["settings"][tag] = {"ko": cfg["ko"], "weight_rule": cfg["rule"], "trained_here": True, **summarise(c, d, cells3)}
        log(tag, cfg["ko"], "weight", [round(v, 1) for v in res["settings"][tag]["pos_weight_range"]],
            "| main metric at epoch", MAIN_EPOCH, round(float(c["min3"][:, MAIN_EPOCH - 1].mean()), 4),
            "| all calls", round(float(c["pooled_all"][:, MAIN_EPOCH - 1].mean()), 4), f"| {time.time() - t0:.0f}s elapsed")
        (REPORT / "class_weight_check.json").write_text(json.dumps(E.to_jsonable(dict(res, partial=True)), ensure_ascii=False), encoding="utf-8")
    EP.class_weight = BASELINE_RULE
    b = res["settings"]["baseline"]["at_epoch"][str(MAIN_EPOCH)]["min3"]["mean"]
    res["reading"] = {tag: {"main_metric_difference_at_main_epoch": res["settings"][tag]["at_epoch"][str(MAIN_EPOCH)]["min3"]["mean"] - b,
                            "reads_as": ("no difference" if abs(res["settings"][tag]["at_epoch"][str(MAIN_EPOCH)]["min3"]["mean"] - b) <= SAME
                                         else "different")} for tag in SETTINGS}
    res["evaluation_sha256"] = E.evaluate_sha256()
    res["run"]["finished_at"] = time.strftime("%Y-%m-%d %H:%M:%S")
    res["run"]["seconds"] = round(time.time() - t0, 1)
    res["partial"] = False
    (REPORT / "class_weight_check.json").write_text(json.dumps(E.to_jsonable(res), ensure_ascii=False), encoding="utf-8")
    for tag, s in res["settings"].items():
        a = s["at_epoch"][str(MAIN_EPOCH)]
        log(f"{tag:9s} epoch {MAIN_EPOCH}: main {a['min3']['mean']:.4f} {np.round(a['min3']['per_seed'], 3).tolist()} | min2 {a['min2']['mean']:.4f} "
            f"| all same-tool {a['all_same_tool']['mean']:.4f} | all calls {a['pooled_all']['mean']:.4f} | visible pooled {a['pooled_visible']['mean']:.4f} "
            f"| peak {s['peak_min3']['value']:.4f}@{s['peak_min3']['epoch']} | epoch {EPOCHS}: {s['at_epoch'][str(EPOCHS)]['min3']['mean']:.4f}")
    log("DONE", json.dumps(res["reading"]), f"{res['run']['seconds']}s")


def diag():
    """Where the all-calls score of the heavier weight comes from. Saved cross-validation scores only; nothing is fitted.

    The train calls come from two collection periods with very different violation rates, so a score that merely
    ranks October calls above November calls already gets a high all-calls AUROC. This splits the all-calls score
    by period and measures how strongly each setting ranks October normal calls above November normal calls."""
    cx = EM.Ctx()
    vis, _ = EM.visible_mask(cx)
    y = cx.y.astype(np.int64)
    src = np.asarray(cx.src, dtype=object)
    oofs = {"baseline": np.load(BASE_NPZ, allow_pickle=False)["oof"][:, :EPOCHS]}
    for tag in SETTINGS:
        oofs[tag] = np.load(OUT / tag / f"{MODEL}.npz", allow_pickle=False)["oof"]
    viol_cells = sorted({g for g, v in zip(cx.groups.tolist(), y.tolist()) if v})
    in_viol_cell = np.isin(cx.groups, viol_cells)
    nm = y == 0
    keys = ("pooled_all", "oct_only", "nov_only", "october_above_november_among_normal_calls",
            "violation_tool_normals_above_other_normals", "inside_violation_tools", "violations_vs_normals_of_other_tools")
    values = {}
    for e in (10, 20, 30, MAIN_EPOCH, EPOCHS):
        for tag, oof in oofs.items():
            r = {k: [] for k in keys}
            for si in range(oof.shape[0]):
                s = oof[si, e - 1].astype(np.float64)
                r["pooled_all"].append(H.auroc(s, y))
                r["oct_only"].append(H.auroc(s[src == "oct"], y[src == "oct"]))
                r["nov_only"].append(H.auroc(s[src == "nov"], y[src == "nov"]))
                r["october_above_november_among_normal_calls"].append(H.auroc(s[nm], (src[nm] == "oct").astype(np.int64)))
                r["violation_tool_normals_above_other_normals"].append(H.auroc(s[nm], in_viol_cell[nm].astype(np.int64)))
                r["inside_violation_tools"].append(H.auroc(s[in_viol_cell], y[in_viol_cell]))
                m = (y == 1) | ~in_viol_cell
                r["violations_vs_normals_of_other_tools"].append(H.auroc(s[m], y[m]))
            values[f"{tag}@{e}"] = {k: round(float(np.mean(v)), 4) for k, v in r.items()}
            log(f"epoch {e:3d} {tag:9s}", json.dumps(values[f"{tag}@{e}"]))
    # a score that only knows the collection period: 1 for an October call, 0 for a November call
    period_train = float(H.auroc((src == "oct").astype(np.float64), y))
    t = json.loads((REPORT / "test_eval.json").read_text(encoding="utf-8"))["data"]       # recorded counts only, no test rows read
    vo, vn = t["violations_by_source"]["oct"], t["violations_by_source"]["nov"]
    no, nn = t["by_source"]["oct"] - vo, t["by_source"]["nov"] - vn
    period_test = (vo * nn + 0.5 * (vo * no + vn * nn)) / ((vo + vn) * (no + nn))
    log("period-only score, all-calls AUROC: train", round(period_train, 4), "| test, from the recorded counts", round(period_test, 4))
    out = {"note": "saved cross-validation scores of the class-weight check, mean of the three split seeds; nothing fitted",
           "train_rows_by_period": {p: {"calls": int((src == p).sum()), "violations": int(y[src == p].sum()),
                                        "visible_violations": int(vis[src == p].sum())} for p in ("oct", "nov")},
           "tool_period_cells_with_a_violation": len(viol_cells), "normal_calls_of_those_cells": int((in_viol_cell & nm).sum()),
           "normal_calls_of_other_cells": int((~in_viol_cell & nm).sum()),
           "period_only_score": {"what": "1 for an October call, 0 for a November call", "train": period_train,
                                 "test_from_counts": period_test,
                                 "test_counts": {"oct_violations": vo, "nov_violations": vn, "oct_normals": no, "nov_normals": nn}},
           "values": values}
    (REPORT / "class_weight_check_diag.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")


FINAL_SEED = 910032                          # the all-rows fit of argus_v_em.run and argus_v_em300_best.py
PAIRS_SAME = 2                               # test reading rule: up to two of the 15 comparison pairs = "no difference"


def pooled_ci(s, y, fam, reps=2000, seed=0):
    """Percentile 95% interval of the all-calls AUROC, resampling scenario families with replacement."""
    f = fam.astype(str)
    fams = sorted(set(f.tolist()))
    members = [np.flatnonzero(f == x) for x in fams]
    rng = np.random.default_rng(seed)
    vals = []
    for _ in range(reps):
        loc = np.concatenate([members[i] for i in rng.integers(0, len(fams), len(fams))])
        if 0 < y[loc].sum() < len(loc):
            vals.append(H.auroc(s[loc], y[loc]))
    lo, hi = np.percentile(vals, [2.5, 97.5])
    return [float(lo), float(hi)]


def test(argv):
    """Score the three weight settings on the test split (user instruction 2026-11-16; second use of the test split).

    Each setting is fitted once on all train target rows, exactly as the main model was (same rows, seed 910032),
    and the test-row scores are recorded after every epoch. The comparison epoch is MAIN_EPOCH."""
    if "--user-approved-test" not in argv:
        raise SystemExit("This reads the test split and fits three all-rows models. Run it only on the user's instruction: "
                         "add --user-approved-test.")
    from experiments.risk_loop.argus_loop import argus_v_em300_test_eval as TE

    t0 = time.time()
    D = TE.load_rows()
    vis_t = TE.visible_mask(D, TE.cmd_flags(D))
    y_t, yv_t, cell_t = D["y"], vis_t.astype(np.int64), D["cell"]
    src_t = D["source"].astype(str)
    target_t = (y_t == 0) | vis_t
    cv = TE.cell_counts(D, vis_t)
    cells3 = sorted(c for c, (p, n) in cv.items() if p >= 3 and n >= 3)
    cells2 = sorted(c for c, (p, n) in cv.items() if p >= 2 and n >= 2)
    distinct, seen = np.zeros(D["n"], bool), set()
    for i in range(D["n"]):
        k = (cell_t[i], D["hash"][i], int(vis_t[i]), int(y_t[i]))
        if k not in seen:
            seen.add(k)
            distinct[i] = True
    sets = {"mask3": target_t & np.isin(cell_t, cells3), "mask2": target_t & np.isin(cell_t, cells2), "distinct": distinct}
    everything = np.ones(D["n"], bool)
    nm = y_t == 0
    cx = EM.Ctx()
    vis, rule = EM.visible_mask(cx)
    X, train_rows, _, _ = EM.prepare(cx, vis)
    rows = EM.sample_training_rows(cx, np.flatnonzero(train_rows), vis, FINAL_SEED)
    y = vis[rows].astype(np.int64)
    frozen_main = np.load(TE.OUT / "scores.npz", allow_pickle=False)["best"].astype(np.float64)
    out_dir = OUT / "test"
    out_dir.mkdir(parents=True, exist_ok=True)
    pairs = int(sum(int(yv_t[sets["mask3"] & (cell_t == c)].sum()) * int((yv_t[sets["mask3"] & (cell_t == c)] == 0).sum()) for c in cells3))
    res = {"name": "Argus-V-em class-weight check, scored on the test split",
           "test_use": "scorings of the test split after the first, pre-registered one (2026-11-16 20:15); each setting carries "
                       "its own scored_at, every use is listed in test-use-log.md. The settings were made after the first result "
                       "was seen, so choosing a setting by these numbers would be optimistic",
           "instruction": "아니 자꾸 test는 왜 안 하냐고", "plan": "reports/risk-loop/argus-v-em300/class-weight-check.md (추가 절)",
           "model": MODEL, "epochs": EPOCHS, "main_epoch": MAIN_EPOCH, "rule": rule,
           "final_fit": {"rows": int(len(rows)), "visible_violations": int(y.sum()), "seed": FINAL_SEED},
           "test": {"calls": int(D["n"]), "violations": int(y_t.sum()), "visible_violations": int(vis_t.sum()),
                    "cells_visible_min3": cells3, "comparison_pairs_main_metric": pairs,
                    "by_period": {p: {"calls": int((src_t == p).sum()), "violations": int(y_t[src_t == p].sum())} for p in ("oct", "nov")}},
           "period_only_score_all_calls": float(H.auroc((src_t == "oct").astype(np.float64), y_t)),
           "same_if_within_pairs": PAIRS_SAME, "settings": {}}
    log(f"test rows={D['n']} violations={int(y_t.sum())} visible={int(vis_t.sum())} cells3={cells3} pairs={pairs} | "
        f"fit rows={len(rows)} visible={int(y.sum())} | period-only score {res['period_only_score_all_calls']:.4f}")
    plan = [("baseline", BASELINE_RULE, BASE_KO)] + [(t, c["fn"], c["ko"]) for t, c in SETTINGS.items()]
    for tag, fn, ko in plan:
        f0 = time.time()
        path = out_dir / f"{tag}.npz"
        if path.is_file():                                           # scored before: read the saved scores, fit nothing
            z = np.load(path, allow_pickle=False)
            assert np.array_equal(z["row"], D["row"])
            s_all, pw, fitted = z["scores"], float(z["pos_weight"]), False
        else:
            EP.class_weight = fn
            _, _, _, pw, loss_opt, _, extra = EP.fit_logged(X[rows], y, EP.MODELS[MODEL], FINAL_SEED, {"test": D["X"]})
            s_all, fitted = extra["test"], True                      # [epoch][test row]
            assert np.isfinite(s_all).all()
            np.savez_compressed(path, scores=s_all, row=D["row"], pos_weight=np.asarray(pw), loss_optimised=loss_opt)
        scored_at = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(path.stat().st_mtime))
        cur = {k: np.full(EPOCHS, np.nan) for k in ("visible_min3", "all_violations_min3", "pooled_all", "pooled_visible",
                                                     "oct_only", "nov_only", "october_above_november_among_normal_calls",
                                                     "caught_at_5pct_false_alarms")}
        for e in range(EPOCHS):
            s = s_all[e].astype(np.float64)
            v = TE.wt(s, yv_t, cell_t, sets["mask3"], 3)["value"]
            a = TE.wt(s, y_t, cell_t, everything, 3)["value"]
            cur["visible_min3"][e] = np.nan if v is None else v
            cur["all_violations_min3"][e] = np.nan if a is None else a
            cur["pooled_all"][e] = H.auroc(s, y_t)
            cur["pooled_visible"][e] = H.auroc(s[target_t], yv_t[target_t])
            cur["oct_only"][e] = H.auroc(s[src_t == "oct"], y_t[src_t == "oct"])
            cur["nov_only"][e] = H.auroc(s[src_t == "nov"], y_t[src_t == "nov"])
            cur["october_above_november_among_normal_calls"][e] = H.auroc(s[nm], (src_t[nm] == "oct").astype(np.int64))
            cur["caught_at_5pct_false_alarms"][e] = TE.op_point(s, y_t, 0.05)["tp"]
        s_main = s_all[MAIN_EPOCH - 1].astype(np.float64)
        entry = {"ko": ko, "pos_weight": float(pw), "seconds": round(time.time() - f0, 1),
                 "fitted_in_this_run": fitted, "scored_at": scored_at,
                 "at_main_epoch": TE.metrics_for(s_main, D, vis_t, sets, with_ci=True),
                 "pooled_all_ci95": pooled_ci(s_main, y_t, D["family"]),
                 "at_main_epoch_extra": {k: float(cur[k][MAIN_EPOCH - 1]) for k in cur},
                 "per_epoch": {k: r6(v) for k, v in cur.items()},
                 "peak_on_test_for_reference_only": {k: {"epoch": int(np.nanargmax(cur[k])) + 1, "value": float(np.nanmax(cur[k]))}
                                                     for k in ("visible_min3", "all_violations_min3", "pooled_all")}}
        alarm = s_main > float(np.quantile(s_main[nm], 0.95))
        fa, tp = alarm & nm, alarm & (y_t == 1)
        entry["alarms_at_5pct_false_alarms"] = {
            "false_alarms": int(fa.sum()), "false_alarms_from_october": int((fa & (src_t == "oct")).sum()),
            "share_october_among_false_alarms": float((fa & (src_t == "oct")).sum() / max(1, int(fa.sum()))),
            "october_normals_alarmed_share": float((fa & (src_t == "oct")).sum() / max(1, int((nm & (src_t == "oct")).sum()))),
            "november_normals_alarmed_share": float((fa & (src_t == "nov")).sum() / max(1, int((nm & (src_t == "nov")).sum()))),
            "caught": int(tp.sum()), "caught_october": int((tp & (src_t == "oct")).sum()),
            "caught_november": int((tp & (src_t == "nov")).sum())}
        if tag == "baseline":
            entry["max_abs_diff_vs_frozen_main_model_scores"] = float(np.max(np.abs(s_main - frozen_main)))
            if entry["max_abs_diff_vs_frozen_main_model_scores"] > 1e-5:
                raise SystemExit("the baseline all-rows fit does not give back the frozen main model's test scores")
        res["settings"][tag] = entry
        m = entry["at_main_epoch"]
        log(f"{tag:9s} weight {pw:6.1f} | epoch {MAIN_EPOCH}: visible same-tool {m['visible_min3']['value']:.4f} | all same-tool "
            f"{m['all_violations_min3']['value']:.4f} | all calls {m['pooled_all_violations']['auroc']:.4f} {np.round(entry['pooled_all_ci95'], 3).tolist()} "
            f"| oct {cur['oct_only'][MAIN_EPOCH - 1]:.3f} nov {cur['nov_only'][MAIN_EPOCH - 1]:.3f} | Oct>Nov normals "
            f"{cur['october_above_november_among_normal_calls'][MAIN_EPOCH - 1]:.3f} | caught@5% {int(cur['caught_at_5pct_false_alarms'][MAIN_EPOCH - 1])}/{int(y_t.sum())}"
            + (f" | vs frozen main model {entry['max_abs_diff_vs_frozen_main_model_scores']}" if tag == "baseline" else ""))
    EP.class_weight = BASELINE_RULE
    b = res["settings"]["baseline"]["at_main_epoch"]["visible_min3"]["value"]
    res["reading"] = {t: {"main_metric_difference": res["settings"][t]["at_main_epoch"]["visible_min3"]["value"] - b,
                          "pairs": round((res["settings"][t]["at_main_epoch"]["visible_min3"]["value"] - b) * pairs, 2),
                          "reads_as": ("no difference" if abs(res["settings"][t]["at_main_epoch"]["visible_min3"]["value"] - b) * pairs <= PAIRS_SAME + 1e-9
                                       else "different")} for t in SETTINGS}
    pa = {t: res["settings"][t]["at_main_epoch"]["pooled_all_violations"]["auroc"] for t in res["settings"]}
    ex = {t: res["settings"][t]["at_main_epoch_extra"] for t in res["settings"]}
    res["all_calls_reading"] = {t: {"all_calls": pa[t], "vs_baseline": pa[t] - pa["baseline"],
                                    "above_period_only_score": bool(pa[t] > res["period_only_score_all_calls"]),
                                    "oct_only_vs_baseline": ex[t]["oct_only"] - ex["baseline"]["oct_only"],
                                    "nov_only_vs_baseline": ex[t]["nov_only"] - ex["baseline"]["nov_only"],
                                    "october_above_november_among_normal_calls": ex[t]["october_above_november_among_normal_calls"]}
                                for t in res["settings"]}
    res["scored_at"] = time.strftime("%Y-%m-%d %H:%M:%S")
    res["seconds"] = round(time.time() - t0, 1)
    res["evaluation_sha256"] = E.evaluate_sha256()
    (REPORT / "class_weight_check_test.json").write_text(json.dumps(E.to_jsonable(res), ensure_ascii=False), encoding="utf-8")
    (REPORT / "class_weight_check_test_alarms.json").write_text(json.dumps(
        {"note": f"test split, epoch {MAIN_EPOCH}, alarms at the threshold where 5% of normal calls alarm; from the saved test scores",
         "october_share_of_normal_calls": float((nm & (src_t == "oct")).sum() / max(1, int(nm.sum()))),
         "values": {t: res["settings"][t]["alarms_at_5pct_false_alarms"] for t in res["settings"]}}, ensure_ascii=False, indent=1), encoding="utf-8")
    for t in res["settings"]:
        a = res["settings"][t]["alarms_at_5pct_false_alarms"]
        log(f"{t:9s} false alarms {a['false_alarms']} of which October {a['false_alarms_from_october']} ({a['share_october_among_false_alarms']:.0%}) | "
            f"caught {a['caught']} (October {a['caught_october']}, November {a['caught_november']})")
    log("DONE", json.dumps(res["reading"]), f"{res['seconds']}s")


ORDER = ("baseline", "w075", "w100", "w300", "w1000")
# ordinal ramp, light to dark = small to large weight (validate_palette.js --ordinal: all checks pass)
RAMP = {"baseline": "#86b6ef", "w075": "#5b9ae8", "w100": "#3478d0", "w300": "#1f5aa6", "w1000": "#123a70"}
NAMES = {"baseline": "약 15배 (지금 방식)", "w075": "약 60배", "w100": "약 230배 (총 가중치 균형)", "w300": "300배", "w1000": "1000배"}


def _panels(series, n_ep, main_epoch, panels, head, sub, note, fname, ylabel, ylim, ref=None):
    """Two panels sharing the y axis, one line per weight. series[tag][key] = value per epoch.
    ref = (value, label): a dotted reference line in the right-hand panel."""
    from experiments.risk_loop.argus_loop import argus_v_p_plots as PP

    PP.setup()
    plt = PP.plt
    ep = np.arange(1, n_ep + 1)
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 5.4), sharey=True)
    fig.subplots_adjust(top=0.76, left=0.07, right=0.94, bottom=0.24, wspace=0.16)
    for ax, (key, sub_title) in zip(axes, panels):
        ends = []
        for tag in ORDER:
            v = np.asarray(series[tag][key], dtype=np.float64)
            ax.plot(ep, v, color=RAMP[tag], lw=2.2, zorder=3, solid_capstyle="round")
            ends.append((float(v[-1]), tag))
        ax.axhline(0.9, color=PP.MUTED, lw=1.0, ls=(0, (4, 3)), zorder=1)
        ax.axhline(0.5, color=PP.MUTED, lw=1.0, ls=(0, (4, 3)), zorder=1)
        ax.axvline(main_epoch, color=PP.MUTED, lw=1.0, ls=(0, (2, 2)), zorder=1)
        ax.set_xlim(1, n_ep)
        ax.set_ylim(*ylim)
        ax.set_xticks([1, 20, 40, 60, 80, 100])
        ax.set_xlabel("epoch")
        ax.set_title(sub_title, fontsize=10.6, color=PP.INK, pad=8, loc="left")
        ends.sort()
        last = -9.0
        for v, _tag in ends:                                    # end labels, pushed apart when the lines end together
            yy = max(v, last + 0.03)
            ax.text(n_ep + 1.5, yy, f"{v:.2f}", va="center", ha="left", fontsize=9.4, color=PP.INK2, clip_on=False)
            last = yy
    axes[0].set_ylabel(ylabel)
    axes[0].text(2, 0.905, "목표 0.90", va="bottom", ha="left", fontsize=9, color=PP.INK2)
    axes[1].text(70, 0.492, "우연 0.5", va="top", ha="left", fontsize=9, color=PP.INK2)
    axes[0].text(main_epoch + 1.5, ylim[0] + 0.02, f"{main_epoch} epoch", va="bottom", ha="left", fontsize=9, color=PP.INK2)
    if ref:
        axes[1].axhline(ref[0], color=PP.INK2, lw=1.1, ls=(0, (1, 2)), zorder=2)
        below = len(ref) > 3 and ref[3] == "below"             # put the label where no curve passes
        axes[1].text(ref[2] if len(ref) > 2 else 70, ref[0] + (-0.008 if below else 0.008), ref[1],
                     va="top" if below else "bottom", ha="left", fontsize=9, color=PP.INK2)
    fig.legend(handles=[PP.Line2D([0], [0], color=RAMP[t], lw=2.4, label="가중치 " + NAMES[t]) for t in ORDER],
               loc="lower center", bbox_to_anchor=(0.5, 0.045), ncol=len(ORDER), columnspacing=1.8, handlelength=2.0, fontsize=9.6)
    PP.title(fig, head, sub)
    PP.note(fig, note)
    out = REPORT / "figures_weight"
    out.mkdir(parents=True, exist_ok=True)
    PP.save(fig, out, fname)


def figure():
    """Figure 01: cross-validation inside train. Figure 02: the same settings on the test split (if they were scored)."""
    res = json.loads((REPORT / "class_weight_check.json").read_text(encoding="utf-8"))
    me = res["main_epoch"]
    short = {t: NAMES[t].split(" (")[0] for t in ORDER}
    at = {t: res["settings"][t]["at_epoch"][str(me)]["min3"]["mean"] for t in ORDER}
    gap = [at[t] - at["baseline"] for t in ORDER[1:]]
    if all(abs(g) <= res["same_if_within"] for g in gap):
        head = "위반 가중치를 키워도 점수는 달라지지 않는다"
    elif all(g < -res["same_if_within"] for g in gap):
        head = "위반 가중치를 키우면 같은 도구 안 구분은 나빠진다"
    else:
        head = "위반 가중치에 따라 점수가 달라진다"
    diag_path = REPORT / "class_weight_check_diag.json"
    ref = None
    if diag_path.is_file():                                     # the right-hand score can be raised by the collection period alone
        po = json.loads(diag_path.read_text(encoding="utf-8"))["period_only_score"]["train"]
        ref = (po, f"기록 시기만 아는 점수 {po:.2f}", 32, "below")
    _panels({t: res["settings"][t]["per_epoch_mean"] for t in ORDER}, res["epochs"], me,
            (("min3", "같은 도구를 쓴 호출끼리 비교 · 근거가 보인 위반 16개"), ("pooled_all", "모든 호출을 정상 대 위반으로 가르기 · 위반 76개")),
            head + " — train 안 교차검증",
            f"64차원 모델, 위반 가중치만 바꿈. {me} epoch의 왼쪽 값: " + " / ".join(f"{short[t]} {at[t]:.3f}" for t in ORDER),
            "train 시나리오를 5묶음으로 나눠 학습에서 뺀 묶음을 채점, 나누기 3가지 평균 · 오른쪽 점선: 10월 기록이면 1점, 11월 기록이면 0점만 준 점수",
            "01_위반_가중치별_epoch_곡선.png", "AUROC (train 안 교차검증)", (0.40, 1.02), ref)
    tpath = REPORT / "class_weight_check_test.json"
    if not tpath.is_file():
        return
    tr = json.loads(tpath.read_text(encoding="utf-8"))
    me = tr["main_epoch"]
    at = {t: tr["settings"][t]["at_main_epoch"]["visible_min3"]["value"] for t in ORDER}
    better = [t for t in ORDER[1:] if tr["reading"][t]["pairs"] > tr["same_if_within_pairs"]]
    head = "test에서는 위반 가중치를 키운 쪽이 더 높다" if better else "test에서도 위반 가중치를 키워 좋아진 것이 없다"
    n_vis, n_all, pairs = tr["test"]["visible_violations"], tr["test"]["violations"], tr["test"]["comparison_pairs_main_metric"]
    po = tr["period_only_score_all_calls"]
    _panels({t: tr["settings"][t]["per_epoch"] for t in ORDER}, tr["epochs"], me,
            (("visible_min3", f"같은 도구를 쓴 호출끼리 비교 · 근거가 보인 위반 {n_vis}개"), ("pooled_all", f"모든 호출을 정상 대 위반으로 가르기 · 위반 {n_all}개")),
            head, f"64차원 모델을 전체 train 행으로 학습해 test로 채점. {me} epoch의 왼쪽 값: " + " / ".join(f"{short[t]} {at[t]:.3f}" for t in ORDER),
            f"test 분할의 첫 채점 결과를 본 뒤에 만든 설정들 · 왼쪽은 비교 {pairs}쌍이라 한 쌍이 {1 / pairs:.2f} · 오른쪽 점선: 기록 시기만 아는 점수",
            "02_test_위반_가중치별_epoch_곡선.png", "AUROC (test)", (0.30, 1.02), (po, f"기록 시기만 아는 점수 {po:.2f}"))


if __name__ == "__main__":
    if "figure" in sys.argv[1:]:
        figure()
    elif "diag" in sys.argv[1:]:
        diag()
    elif "test" in sys.argv[1:]:
        test(sys.argv[1:])
    else:
        train(sys.argv[1:])

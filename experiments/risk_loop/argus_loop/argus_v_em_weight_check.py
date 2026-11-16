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
        PYTHONUTF8=1 py -3.11 experiments/risk_loop/argus_loop/argus_v_em_weight_check.py figure      (no training)
Output: artifacts/risk-loop/argus-v-em300/class_weight_check/<setting>/EM64.npz   (ignored)
        reports/risk-loop/argus-v-em300/class_weight_check.json, figures_weight/*.png
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


def figure():
    """Two panels from the saved summary: the main metric and the all-calls AUROC per epoch, one line per weight."""
    from experiments.risk_loop.argus_loop import argus_v_p_plots as PP

    res = json.loads((REPORT / "class_weight_check.json").read_text(encoding="utf-8"))
    PP.setup()
    plt = PP.plt
    ramp = {"baseline": "#86b6ef", "w075": "#3987e5", "w100": "#184f95"}          # ordinal: light to dark = small to large weight
    names = {"baseline": "약 15배 (지금 방식)", "w075": "약 60배", "w100": "약 230배 (위반·정상 총 가중치 같음)"}
    panels = (("min3", "같은 도구를 쓴 호출끼리 비교 · 근거가 보인 위반 16개", (0.40, 1.02)),
              ("pooled_all", "모든 호출을 정상 대 위반으로 가르기 · 위반 76개", (0.40, 1.02)))
    ep = np.arange(1, res["epochs"] + 1)
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 5.4), sharey=True)
    fig.subplots_adjust(top=0.76, left=0.07, right=0.94, bottom=0.24, wspace=0.16)
    for ax, (key, sub, ylim) in zip(axes, panels):
        ends = []
        for tag in ("baseline", "w075", "w100"):
            v = np.asarray(res["settings"][tag]["per_epoch_mean"][key])
            ax.plot(ep, v, color=ramp[tag], lw=2.2, zorder=3, solid_capstyle="round")
            ends.append((float(v[-1]), tag))
        ax.axhline(0.9, color=PP.MUTED, lw=1.0, ls=(0, (4, 3)), zorder=1)
        ax.axhline(0.5, color=PP.MUTED, lw=1.0, ls=(0, (4, 3)), zorder=1)
        ax.axvline(res["main_epoch"], color=PP.MUTED, lw=1.0, ls=(0, (2, 2)), zorder=1)
        ax.set_xlim(1, res["epochs"])
        ax.set_ylim(*ylim)
        ax.set_xticks([1, 20, 40, 60, 80, 100])
        ax.set_xlabel("epoch")
        ax.set_title(sub, fontsize=10.6, color=PP.INK, pad=8, loc="left")
        ends.sort()
        last = -9.0
        for v, tag in ends:                                     # end labels, pushed apart when the lines end together
            yy = max(v, last + 0.03)
            ax.text(res["epochs"] + 1.5, yy, f"{v:.2f}", va="center", ha="left", fontsize=9.4, color=PP.INK2, clip_on=False)
            last = yy
    axes[0].set_ylabel("AUROC (train 안 교차검증)")
    axes[0].text(2, 0.905, "목표 0.90", va="bottom", ha="left", fontsize=9, color=PP.INK2)
    axes[0].text(2, 0.455, "우연 0.5", va="bottom", ha="left", fontsize=9, color=PP.INK2)
    axes[0].text(res["main_epoch"] + 1.5, 0.42, f"{res['main_epoch']} epoch", va="bottom", ha="left", fontsize=9, color=PP.INK2)
    fig.legend(handles=[PP.Line2D([0], [0], color=ramp[t], lw=2.4, label="위반 가중치 " + names[t]) for t in ("baseline", "w075", "w100")],
               loc="lower center", bbox_to_anchor=(0.5, 0.045), ncol=3, columnspacing=1.8, handlelength=2.0, fontsize=9.6)
    b = res["settings"]["baseline"]["at_epoch"][str(res["main_epoch"])]
    d = {t: res["settings"][t]["at_epoch"][str(res["main_epoch"])] for t in ("w075", "w100")}
    same = all(abs(d[t]["min3"]["mean"] - b["min3"]["mean"]) <= res["same_if_within"] for t in d)
    head = ("위반 가중치를 키워도 점수는 달라지지 않는다" if same else "위반 가중치에 따라 점수가 달라진다") + " — train 안 교차검증"
    PP.title(fig, head, f"64차원 모델, 위반 가중치만 바꿈. {res['main_epoch']} epoch의 주 지표: "
             + " / ".join(f"{names[t].split(' (')[0]} {res['settings'][t]['at_epoch'][str(res['main_epoch'])]['min3']['mean']:.3f}" for t in ("baseline", "w075", "w100")))
    PP.note(fig, "train 시나리오를 5묶음으로 나눠 학습에서 뺀 묶음을 채점, 나누기 3가지 평균 · test·validation 분할은 쓰지 않음 · 새 시나리오에서 확인한 값이 아니다")
    out = REPORT / "figures_weight"
    out.mkdir(parents=True, exist_ok=True)
    PP.save(fig, out, "01_위반_가중치별_epoch_곡선.png")


if __name__ == "__main__":
    if "figure" in sys.argv[1:]:
        figure()
    else:
        train(sys.argv[1:])

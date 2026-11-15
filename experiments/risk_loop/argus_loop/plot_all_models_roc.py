"""Plot comparable within-tool ROC curves for every P and EM model variant."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import auc, roc_curve

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from experiments.risk_loop.argus_loop import evaluate as E
from experiments.risk_loop.argus_loop.argus_v_em import OUT as EM_OUT, Ctx as EMCtx, prepare, visible_mask
from experiments.risk_loop.argus_loop.argus_v_p import OUT as P_OUT, REPORT as P_REPORT, Ctx as PCtx, oof_path

EM_REPORT = ROOT / "reports" / "risk-loop" / "argus-v-em"
GRID = np.linspace(0, 1, 501)
COLORS = {"P1": "#2563EB", "P2": "#F97316", "P3": "#16A34A", "P4": "#DC2626",
          "P5": "#9333EA", "P6": "#0E7490", "EM32": "#0E7490", "EM64": "#2563EB",
          "EM128": "#D97706", "LINEAR": "#64748B"}
LABELS = {
    "P1": "P1 · baseline", "P2": "P2 · within-tool", "P3": "P3 · relaxed",
    "P4": "P4 · within-tool + relaxed", "P5": "P5 · baseline + RF",
    "P6": "P6 · P4 + RF", "EM32": "EM32", "EM64": "EM64",
    "EM128": "EM128", "LINEAR": "raw linear control",
}


def curve(scores: np.ndarray, y: np.ndarray, groups: np.ndarray, mask: np.ndarray, min_pos: int, min_neg: int):
    y0 = np.asarray(y)[mask].astype(np.int64)
    s0 = np.asarray(scores, dtype=np.float64)[mask]
    g0 = np.asarray(groups, dtype=object)[mask]
    weighted = np.zeros_like(GRID)
    den = 0
    per = []
    for cell in sorted(set(g0.tolist())):
        m = g0 == cell
        p = int(y0[m].sum())
        n = int(m.sum()) - p
        if p < min_pos or n < min_neg:
            continue
        fpr, tpr, _ = roc_curve(y0[m], s0[m])
        weighted += p * np.interp(GRID, fpr, tpr)
        den += p
        per.append({"cell": str(cell), "positive": p, "negative": n, "auc": float(auc(fpr, tpr))})
    if not den:
        raise RuntimeError("no eligible tool/source cells for requested ROC")
    tpr = weighted / den
    # AUROC is the integral of the plotted, violation-weighted within-tool ROC.
    return GRID, tpr, float(auc(GRID, tpr)), per, den


def save_plot(path: Path, title: str, subtitle: str, panels: list[dict], diagonal=True):
    fig, axes = plt.subplots(1, len(panels), figsize=(7.1 * len(panels), 6.7), sharex=True, sharey=True)
    axes = np.atleast_1d(axes)
    for ax, panel in zip(axes, panels):
        if diagonal:
            ax.plot([0, 1], [0, 1], color="#94A3B8", linestyle="--", linewidth=1.2, label="Chance (AUC 0.5)")
        for model, (x, y, score, per, positives) in panel["curves"].items():
            ax.plot(x, y, lw=2.15, color=COLORS[model], label=f"{LABELS[model]}  AUC {score:.3f}")
        ax.set_title(panel["title"], fontsize=13, loc="left", pad=10, weight="bold")
        ax.set_xlabel("False positive rate")
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1.01)
        ax.grid(color="#E2E8F0", linewidth=0.8)
        ax.set_axisbelow(True)
        ax.legend(loc="lower right", fontsize=9, frameon=True, facecolor="white", framealpha=0.95)
    axes[0].set_ylabel("True positive rate")
    fig.subplots_adjust(top=0.80, bottom=0.12, left=0.08, right=0.98, wspace=0.10)
    fig.suptitle(title, fontsize=19, weight="bold", x=0.05, y=0.975, ha="left")
    fig.text(0.05, 0.91, subtitle, ha="left", va="top", fontsize=10, color="#475569")
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=240, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(path.relative_to(ROOT))


def p_curves():
    cx = PCtx()
    results = json.loads((P_REPORT / "results.json").read_text(encoding="utf-8"))
    sc = {condition: {} for condition in "ABC"}
    for model in results["settings"]:
        for condition in "AB":
            seed_scores = [np.load(oof_path(model, condition, seed)) for seed in (0, 1, 2)]
            sc[condition][model] = np.mean(seed_scores, axis=0)
        cached = P_OUT / f"p6_condition_c_scores.npy" if model == "P6" else P_OUT / f"roc_C_{model}.npy"
        if cached.is_file():
            c_scores = np.load(cached)
        else:
            c_scores, _ = cx.fit(model, np.arange(cx.n), cx.y, np.zeros(0, dtype=np.int64))
            np.save(cached, c_scores)
        got = float(cx.wt(c_scores)["value"])
        expected = float(results["results"][model]["C"]["value"])
        if abs(got - expected) > 1e-6:
            raise RuntimeError(f"{model} C rescore differs from saved result: {got} vs {expected}")
        sc["C"][model] = c_scores

    panels = []
    for condition, description in (("A", "Unseen scenario family · grouped OOF"),
                                   ("B", "New run of seen scenarios · grouped OOF"),
                                   ("C", "Training-row rescore · in-sample")):
        curves = {}
        for model in results["settings"]:
            x, y, plotted_auc, per, positives = curve(sc[condition][model], cx.y, cx.groups,
                                                       np.ones(cx.n, dtype=bool), 3, 3)
            # Show the official mean of seed-level within-tool AUROCs for A/B.
            official = float(results["results"][model][condition]["value"])
            curves[model] = (x, y, official, per, positives)
        panels.append({"title": f"{condition} · {description}", "curves": curves})
    save_plot(P_REPORT / "all_models_roc.png", "Argus-V-p · ROC curves for all settings",
              "Positive-count-weighted mean of tool × source ROC curves · legend AUC is the stored condition AUROC", panels)
    save_plot(P_REPORT / "all_models_roc.pdf", "Argus-V-p · ROC curves for all settings",
              "Positive-count-weighted mean of tool × source ROC curves · legend AUC is the stored condition AUROC", panels)
    return results


def em_curves():
    cx = EMCtx()
    vis, rule = visible_mask(cx)
    X, train_rows, eval_rows, eligible = prepare(cx, vis)
    min3_cells = [k for k, v in eligible.items() if v["min3"]]
    min2_cells = [k for k, v in eligible.items() if v["min2"]]
    masks = {
        "min3": eval_rows & np.isin(cx.groups, min3_cells),
        "min2": eval_rows & np.isin(cx.groups, min2_cells),
    }
    result = json.loads((EM_REPORT / "round01_results.json").read_text(encoding="utf-8"))
    linear = json.loads((EM_REPORT / "round01_linear_control.json").read_text(encoding="utf-8"))
    names = ("EM32", "EM64", "EM128", "LINEAR")
    scores = {}
    for model in names:
        filekey = "LINEAR" if model == "LINEAR" else model
        scores[model] = np.mean([np.load(EM_OUT / f"oof_{filekey}_s{seed}.npy") for seed in (0, 1, 2)], axis=0)
    panels = []
    for label, minp, mask_key, key in (("Primary · min 3 positives per cell", 3, "min3", "visible_min3"),
                                       ("Sensitivity · min 2 positives per cell", 2, "min2", "visible_min2")):
        curves = {}
        for model in names:
            x, y, plotted_auc, per, positives = curve(scores[model], cx.y, cx.groups, masks[mask_key], minp, minp)
            if model == "LINEAR":
                official = float(linear[key]["mean"])
            else:
                official = float(result["architectures"][model][key]["mean"])
            curves[model] = (x, y, official, per, positives)
        panels.append({"title": label, "curves": curves})
    subtitle = f"Visible-label rule: {rule} · family-grouped 5-fold × 3 seed OOF · development rows only"
    save_plot(EM_REPORT / "all_models_roc.png", "Argus-V-em · ROC curves for all embedding models",
              subtitle, panels)
    save_plot(EM_REPORT / "all_models_roc.pdf", "Argus-V-em · ROC curves for all embedding models",
              subtitle, panels)


if __name__ == "__main__":
    p_curves()
    em_curves()

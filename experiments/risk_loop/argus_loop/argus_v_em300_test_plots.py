"""Figures and tables of the Argus-V-em300 TEST evaluation (matplotlib), in the style of argus_v_p_plots.py.

Reads only what argus_v_em300_test_eval.py wrote: reports/risk-loop/argus-v-em300/test_eval.json,
artifacts/risk-loop/argus-v-em300/test/rows.csv and scores. Fits nothing and scores nothing.

Usage : PYTHONUTF8=1 py -3.11 experiments/risk_loop/argus_loop/argus_v_em300_test_plots.py
Output: reports/risk-loop/argus-v-em300/figures_test/*.png + test_tables.md
"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from experiments.risk_loop.argus_loop import argus_v_p_plots as PP  # noqa: E402  (Agg backend + style)
from experiments.risk_loop import harness as H  # noqa: E402

plt, Line2D = PP.plt, PP.Line2D
SURFACE, INK, INK2, MUTED, GRID, BASE = PP.SURFACE, PP.INK, PP.INK2, PP.MUTED, PP.GRID, PP.BASE
TEST = "#eb6834"                      # the "new data" hue of the Argus-V-p figures (slot 2); cross-validation stays blue
CV = PP.COND["A"]["color"]
VIOL, NORM = PP.VIOL, PP.NORM
REPORT = REPO_ROOT / "reports/risk-loop/argus-v-em300"
ART = REPO_ROOT / "artifacts/risk-loop/argus-v-em300"
OUT = REPORT / "figures_test"
FIG_W, LBL = PP.FIG_W, PP.LBL
MODELS, SHORT, PK = {}, {}, "em300"       # filled by set_models(): PK = the primary model of the evaluation


def set_models(res):
    """Row labels. The primary model is the one the prereg (and its addendum) named before test was scored."""
    global MODELS, SHORT, PK
    PK = res.get("primary", "em300")
    MODELS, SHORT = {}, {}
    if PK == "best":
        b = res["frozen"]["best_choice"]
        MODELS["best"] = f"Argus-V-em300 · 가장 좋았던 epoch ({b['width']}차원, {b['epoch']} epoch) · 주 모델"
        SHORT["best"] = f"가장 좋았던 epoch ({b['width']}차원, {b['epoch']} epoch)"
        MODELS["em300"] = "Argus-V-em300 · 300 epoch까지 학습 · 참고"
        SHORT["em300"] = f"300 epoch까지 ({res['frozen']['width_of_the_300_epoch_model']}차원)"
    else:
        MODELS["em300"] = "Argus-V-em300 (300 epoch) · 주 모델"
        SHORT["em300"] = "Argus-V-em300"
    MODELS["em60"] = "Argus-V-em (60 epoch) · 참고"
    SHORT["em60"] = "Argus-V-em (32차원, 60 epoch)"
    MODELS["P5"] = "Argus-V-p (P5) · 참고"
    SHORT["P5"] = "Argus-V-p"


def short(cell):
    return cell.split("|")[0]


def handle(color, label, marker="o", line=False, hollow=False, ls="-"):
    return Line2D([0], [0], color=color, lw=2 if line else 0, ls=ls, marker=marker, markersize=8,
                  markerfacecolor=SURFACE if hollow else color, markeredgecolor=color if hollow else SURFACE,
                  markeredgewidth=1.6, label=label)


def fmt(v, nd=3):
    return "—" if v is None else f"{v:.{nd}f}"


def load():
    res = json.loads((REPORT / "test_eval.json").read_text(encoding="utf-8"))
    rows = list(csv.DictReader(open(ART / "test" / "rows.csv", encoding="utf-8")))
    R = {"y": np.asarray([int(r["label"]) for r in rows]), "vis": np.asarray([int(r["visible"]) for r in rows], dtype=bool),
         "cell": np.asarray([r["cell"] for r in rows], dtype=object), "m3": np.asarray([int(r["in_visible_min3"]) for r in rows], dtype=bool),
         "m2": np.asarray([int(r["in_visible_min2"]) for r in rows], dtype=bool),
         "scenario": np.asarray([r["scenario_id"] for r in rows], dtype=object)}
    for k in rows[0]:
        if k.startswith("score_"):
            R[k[6:]] = np.asarray([float(r[k]) for r in rows])
    cvres = json.loads((REPORT / "results.json").read_text(encoding="utf-8"))
    base = json.loads((REPO_ROOT / "reports/risk-loop/argus-v-em/round01_results.json").read_text(encoding="utf-8"))
    hist = json.loads((REPORT / "epoch_history.json").read_text(encoding="utf-8"))
    return res, R, cvres, base, hist


def wroc(R, s, mask, min_pos):
    """Violation-weighted mean of the per-cell ROC curves of the visible violations."""
    grid = np.linspace(0, 1, 401)
    acc, den = np.zeros_like(grid), 0
    yv = R["vis"].astype(int)
    for cell in sorted(set(R["cell"][mask].tolist())):
        m = mask & (R["cell"] == cell)
        p, n = int(yv[m].sum()), int(m.sum() - yv[m].sum())
        if p < min_pos or n < 3:
            continue
        f, t = PP.roc_points(s[m], yv[m])
        acc += p * np.interp(grid, f, t)
        den += p
    return (grid, acc / den) if den else (None, None)


# ------------------------------------------------------------------------------------------------ figures

def fig01_scores(res, T):
    rows = [(k, res["models"][k]) for k in MODELS]
    fig, ax = plt.subplots(figsize=(FIG_W, 5.0))
    fig.subplots_adjust(top=0.78, left=0.36, right=0.95, bottom=0.36)
    for i, (k, m) in enumerate(rows):
        yy = len(rows) - 1 - i
        col = TEST if k == PK else MUTED
        v3, v2, va = m["visible_min3"]["value"], m["visible_min2"]["value"], m["all_violations_min3"]["value"]
        pts = [v for v in (v3, v2, va) if v is not None]
        if len(pts) > 1:
            ax.plot([min(pts), max(pts)], [yy, yy], color=BASE, lw=1.6, zorder=2)
        ci = m["visible_min3"].get("ci95")
        if ci and ci["families"] > 1 and ci["high"] > ci["low"]:
            ax.plot([ci["low"], ci["high"]], [yy + 0.22, yy + 0.22], color=INK2, lw=1.2, zorder=3, solid_capstyle="butt")
        if va is not None:
            ax.plot(va, yy, "s", markersize=9.5, color=MUTED, markeredgecolor=SURFACE, markeredgewidth=2, zorder=3)
            ax.text(va, yy - 0.33, f"{va:.2f}", va="center", ha="center", fontsize=9.4, color=INK2, zorder=6)
        if v2 is not None:
            ax.plot(v2, yy, "o", markersize=10, markerfacecolor=SURFACE, markeredgecolor=col, markeredgewidth=2, zorder=4)
        if v3 is not None:
            ax.plot(v3, yy, "o", markersize=10, color=col, markeredgecolor=SURFACE, markeredgewidth=2, zorder=5)
            ax.text(v3, yy + 0.33, f"{v3:.2f}", va="center", ha="center", fontsize=9.8, color=INK, zorder=6)
        elif v2 is not None:
            ax.text(v2, yy + 0.33, f"{v2:.2f}", va="center", ha="center", fontsize=9.8, color=INK, zorder=6)
    ax.set_yticks(range(len(rows)))
    ax.set_yticklabels([SHORT[k] + (" · 주 모델" if k == PK else " · 참고") for k, _ in rows][::-1])
    ax.set_xlim(0.0, 1.07)
    ax.set_ylim(-0.7, len(rows) - 0.3)
    ax.set_xlabel("같은 도구 안 AUROC (0.5 = 우연)")
    ax.grid(axis="y", visible=False)
    PP.ref_line(ax, x=0.5, label="우연")
    PP.ref_line(ax, x=0.9, label="목표 0.90")
    d = res["data"]
    p3, p2, pa = res["models"][PK]["visible_min3"], res["models"][PK]["visible_min2"], res["models"][PK]["all_violations_min3"]
    ax.legend(handles=[handle(TEST, f"근거가 보인 위반, 칸에 3개 이상 ({p3['violations']}개 · 칸 {p3['cells']}개) — 주 지표"),
                       handle(TEST, f"근거가 보인 위반, 칸에 2개 이상 ({p2['violations']}개 · 칸 {p2['cells']}개)", hollow=True),
                       handle(MUTED, f"위반 전체 ({pa['violations']}개 · 칸 {pa['cells']}개)", marker="s"),
                       Line2D([0], [0], color=INK2, lw=1.2, label="주 지표의 95% 구간(시나리오 계열이 하나뿐이면 낼 수 없어 그리지 않음)")],
              loc="upper center", bbox_to_anchor=(0.22, -0.17), ncol=1, handletextpad=0.3, labelspacing=0.35, fontsize=9.3)
    PP.note(fig, "위 숫자 = 주 지표, 아래 숫자 = 위반 전체 · 같은 도구를 쓴 호출끼리 위반과 정상을 비교한 값이다")
    PP.title(fig, T["headline"], f"test 분할(학습·설정에 한 번도 쓰지 않은 시나리오 {d['scenarios']}개, 실행 {d['units']}개, 채점한 호출 {d['judged_rows']:,}개)")
    PP.save(fig, OUT, "01_test_모델별_점수.png")


def fig02_cv_vs_test(res, cvres, base, T):
    """Cross-validation inside train (development) next to the test score, same model, same metric."""
    sel = f"EM{res['frozen']['width_of_the_300_epoch_model']}"
    bsel = base["selected_on_development_oof"]
    cv = {"em300": cvres["architectures"][sel], "em60": base["architectures"][bsel]}
    rows = [("em300", f"300 epoch까지 ({sel.replace('EM', '')}차원)"), ("em60", f"Argus-V-em ({bsel.replace('EM', '')}차원, 60 epoch)")]
    if PK == "best":
        b = res["frozen"]["best_choice"]
        cv["best"] = {"visible_min3": {"mean": float(np.mean(b["cv_per_seed"]))}, "visible_min2": {"mean": float(np.mean(b["cv_min2_per_seed"]))},
                      "all_violations_min3": {"mean": float(np.mean(b["cv_all_violations_per_seed"]))}}
        rows.insert(0, ("best", f"가장 좋았던 epoch ({b['width']}차원, {b['epoch']} epoch) · 주 모델"))
    keys = (("visible_min3", "근거가 보인 위반, 칸에 3개 이상"), ("visible_min2", "근거가 보인 위반, 칸에 2개 이상"), ("all_violations_min3", "위반 전체"))
    fig, axes = plt.subplots(1, 3, figsize=(FIG_W + 2.2, 3.9), sharey=True)
    fig.subplots_adjust(top=0.70, left=0.25, right=0.98, bottom=0.27, wspace=0.10)
    for ax, (key, name) in zip(axes, keys):
        for i, (k, lab) in enumerate(rows):
            yy = len(rows) - 1 - i
            a, b = cv[k][key]["mean"], res["models"][k][key]["value"]
            if b is not None:
                ax.plot([a, b], [yy, yy], color=BASE, lw=1.6, zorder=2)
                ax.plot(b, yy, "s", markersize=10, color=TEST, markeredgecolor=SURFACE, markeredgewidth=2, zorder=4)
                ax.text(b, yy - 0.30, f"{b:.2f}", va="center", ha="center", fontsize=9.4, color=INK2)
            ax.plot(a, yy, "o", markersize=10, color=CV, markeredgecolor=SURFACE, markeredgewidth=2, zorder=3)
            ax.text(a, yy + 0.30, f"{a:.2f}", va="center", ha="center", fontsize=9.4, color=INK2)
        ax.set_xlim(0.0, 1.07)
        ax.set_ylim(-0.7, len(rows) - 0.3)
        ax.set_title(name, fontsize=10.2, color=INK, pad=8)
        ax.axvline(0.9, color=MUTED, lw=1.0, ls=(0, (4, 3)), zorder=1)
        ax.axvline(0.5, color=MUTED, lw=1.0, ls=(0, (4, 3)), zorder=1)
        ax.grid(axis="y", visible=False)
        ax.set_xlabel("같은 도구 안 AUROC")
    axes[0].set_yticks(range(len(rows)))
    axes[0].set_yticklabels([lab for _, lab in rows][::-1])
    fig.legend(handles=[handle(CV, "train 안 교차검증 (개발용, 나누기 3가지 평균)"), handle(TEST, "test 분할 (한 번 채점)", marker="s")],
               loc="lower center", bbox_to_anchor=(0.5, 0.01), ncol=2, handletextpad=0.3, columnspacing=2.0)
    PP.title(fig, "train 안 교차검증 점수와 test 점수", "같은 모델을 같은 지표로 잰 값. 점선은 우연 0.5와 목표 0.90. test 값이 없는 칸은 test에 그 조건을 만족하는 도구가 없다는 뜻")
    PP.save(fig, OUT, "02_교차검증과_test.png")


def fig03_roc(res, R, T):
    mp, mask, tag = (3, R["m3"], "칸에 3개 이상") if res["models"][PK]["visible_min3"]["value"] is not None else (2, R["m2"], "칸에 2개 이상")
    key = "visible_min3" if mp == 3 else "visible_min2"
    if res["models"][PK][key]["value"] is None:
        return
    fig, ax = plt.subplots(figsize=(6.6, 6.4))
    fig.subplots_adjust(top=0.84, left=0.12, right=0.96, bottom=0.12)
    ax.plot([0, 1], [0, 1], color=BASE, lw=1.2, zorder=1)
    lines = [("P5", MUTED, (0, (1, 1.6)), 1.8), ("em60", MUTED, (0, (5, 2)), 1.8)]
    if PK != "em300":
        lines.append(("em300", MUTED, "-", 1.6))
    lines.append((PK, TEST, "-", 2.3))
    for k, col, ls, lw in lines:
        g, t = wroc(R, R[k], mask, mp)
        if g is not None:
            ax.plot(g, t, color=col, lw=lw, ls=ls, zorder=3 if k != PK else 4, label=f"{SHORT[k]}  {res['models'][k][key]['value']:.2f}")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1.005)
    ax.set_aspect("equal")
    ax.set_xlabel("오경보율 (정상을 위반으로 본 비율)")
    ax.set_ylabel("탐지율 (근거가 보인 위반을 잡은 비율)")
    hh, ll = ax.get_legend_handles_labels()
    ax.legend(hh[::-1], ll[::-1], loc="lower right", title="test · 같은 도구 안 AUROC", title_fontsize=9.5, handlelength=1.8)
    ax.text(0.62, 0.56, "우연 수준", rotation=45, color=MUTED, fontsize=9, ha="center", va="center")
    m = res["models"][PK][key]
    PP.title(fig, "ROC 곡선 — test 분할", f"근거가 보인 위반 {m['violations']}개, 도구 칸 {m['cells']}개({tag})의 곡선을 위반 수로 가중 평균")
    PP.save(fig, OUT, "03_test_ROC_곡선.png")


def fig04_cells(res, R, T):
    table = res["data"]["cell_table"]
    per = {k: {p["tool"]: p["auroc"] for p in res["models"][k]["visible_min2"]["per_cell"]} for k in (PK, "em60")}
    allper = {p["tool"]: p["auroc"] for p in res["models"][PK]["all_violations_min3"]["per_cell"]}
    cells = sorted(set(per[PK]) | set(allper), key=lambda c: (per[PK].get(c, -1), allper.get(c, -1)))
    if not cells:
        return
    fig, ax = plt.subplots(figsize=(FIG_W + 0.6, 0.52 * len(cells) + 2.9))
    hin = fig.get_size_inches()[1]
    fig.subplots_adjust(top=1 - 1.15 / hin, left=0.50, right=0.94, bottom=1.25 / hin)
    for yy, c in enumerate(cells):
        vals = [v for v in (per[PK].get(c), per["em60"].get(c), allper.get(c)) if v is not None]
        ax.plot([min(vals), max(vals)], [yy, yy], color=BASE, lw=1.4, zorder=2)
        if c in allper:
            ax.plot(allper[c], yy, "s", markersize=9, color=MUTED, markeredgecolor=SURFACE, markeredgewidth=2, zorder=3)
        if c in per["em60"]:
            ax.plot(per["em60"][c], yy, "o", markersize=10, markerfacecolor=SURFACE, markeredgecolor=MUTED, markeredgewidth=2, zorder=4)
        if c in per[PK]:
            ax.plot(per[PK][c], yy, "o", markersize=10, color=TEST, markeredgecolor=SURFACE, markeredgewidth=2, zorder=5)
    ax.set_yticks(range(len(cells)))
    ax.set_yticklabels([f"{short(c)} · {PP.SOURCE_KO.get(c.split('|')[1], c.split('|')[1])}  (위반 {table[c]['violations']}, 그중 근거가 보인 것 {table[c]['visible_violations']} · 정상 {table[c]['normals']})"
                        for c in cells], fontsize=9.2)
    ax.set_xlim(-0.02, 1.05)
    ax.set_ylim(-0.6, len(cells) - 0.4)
    ax.set_xlabel("칸 안 AUROC (같은 도구를 쓴 호출끼리 위반과 정상을 비교)")
    ax.grid(axis="y", visible=False)
    PP.ref_line(ax, x=0.5, label="우연")
    PP.ref_line(ax, x=0.9, label="0.90")
    ax.legend(handles=[handle(TEST, "주 모델 · 근거가 보인 위반"), handle(MUTED, "Argus-V-em(60 epoch) · 근거가 보인 위반", hollow=True),
                       handle(MUTED, "주 모델 · 그 칸의 위반 전체", marker="s")],
              loc="upper center", bbox_to_anchor=(0.10, -0.62 / (hin - 2.4)), ncol=3, handletextpad=0.3, columnspacing=1.4, fontsize=9.3)
    PP.title(fig, "도구 칸별 AUROC — test 분할", "근거가 보인 위반이 2개 이상이거나 위반이 3개 이상인 test 도구 칸")
    PP.note(fig, "칸마다 위반이 몇 개뿐이라 한 개 차이로 값이 크게 움직인다")
    PP.save(fig, OUT, "04_test_칸별_AUROC.png")


def fig05_scores(res, R, T):
    table = res["data"]["cell_table"]
    cells = sorted(table, key=lambda c: (-table[c]["visible_violations"], -table[c]["violations"], c))[:12]
    if not cells:
        return
    rng = np.random.default_rng(0)
    fig, ax = plt.subplots(figsize=(FIG_W + 1.4, 5.2))
    fig.subplots_adjust(top=0.80, left=0.08, right=0.98, bottom=0.26)
    s = R[PK]
    for i, c in enumerate(cells):
        m = np.flatnonzero(R["cell"] == c)
        for idx, mk, fc, ec, z, off in ((m[R["y"][m] == 0], "o", "none", NORM, 2, -0.22),
                                        (m[(R["y"][m] == 1) & ~R["vis"][m]], "D", SURFACE, VIOL, 3, 0.0),
                                        (m[R["vis"][m]], "D", VIOL, SURFACE, 4, 0.22)):
            ax.plot(i + off + rng.uniform(-0.08, 0.08, len(idx)), s[idx], mk, markersize=6.0, markerfacecolor=fc, markeredgecolor=ec,
                    markeredgewidth=1.1, lw=0, zorder=z)
    ax.set_xticks(range(len(cells)))
    ax.set_xticklabels([short(c).replace("_", "\n") for c in cells], fontsize=8.2)
    ax.set_ylabel("모델 출력 점수 (클수록 위반 쪽)")
    ax.grid(axis="x", visible=False)
    fig.legend(handles=[Line2D([0], [0], lw=0, marker="D", markersize=7, markerfacecolor=VIOL, markeredgecolor=SURFACE, label="근거가 보인 위반"),
                        Line2D([0], [0], lw=0, marker="D", markersize=7, markerfacecolor=SURFACE, markeredgecolor=VIOL, markeredgewidth=1.2, label="근거가 보이지 않은 위반"),
                        Line2D([0], [0], lw=0, marker="o", markersize=7, markerfacecolor="none", markeredgecolor=NORM, label="정상 호출")],
               loc="upper left", bbox_to_anchor=(0.06, 0.90), ncol=3, handletextpad=0.3, columnspacing=1.4, fontsize=9.3)
    PP.title(fig, "도구 칸별 점수 분포 — test 분할, 주 모델", None)
    PP.note(fig, "위반이 있는 test 도구 칸(많은 순으로 12개까지) · 점수는 확률이 아니라 순서를 매기는 값이고 같은 칸 안에서만 비교한다")
    PP.save(fig, OUT, "05_test_칸별_점수_분포.png")


def fig06_epochs(res, hist, cvres, T):
    """Test score of the snapshots of the same fit against training length (reference only, no epoch is chosen)."""
    eps = sorted(int(k.split("_")[-1]) for k in res["models"] if k.startswith("em300_epoch_"))
    if not eps:
        return
    key3 = "visible_min3" if res["models"][PK]["visible_min3"]["value"] is not None else "visible_min2"
    t3 = [res["models"][f"em300_epoch_{e:03d}"][key3]["value"] for e in eps]
    ta = [res["models"][f"em300_epoch_{e:03d}"]["all_violations_min3"]["value"] for e in eps]
    sel = f"EM{res['frozen']['width_of_the_300_epoch_model']}"
    cvk = "auroc_heldout_min3" if key3 == "visible_min3" else "auroc_heldout_min2"
    cv = np.asarray(hist["models"][sel]["per_epoch"][cvk], dtype=float).mean(0)
    ep = np.arange(1, len(cv) + 1)
    fig, ax = plt.subplots(figsize=(FIG_W, 5.4))
    fig.subplots_adjust(top=0.80, left=0.09, right=0.90, bottom=0.24)
    ax.plot(ep, cv, color=CV, lw=2.0, zorder=3)
    if all(v is not None for v in ta):
        ax.plot(eps, ta, color=MUTED, lw=1.6, marker="s", markersize=5.5, markeredgecolor=SURFACE, markeredgewidth=1.0, zorder=3)
    if all(v is not None for v in t3):
        ax.plot(eps, t3, color=TEST, lw=2.2, marker="o", markersize=6.5, markeredgecolor=SURFACE, markeredgewidth=1.2, zorder=4)
    ax.axhline(0.9, color=MUTED, lw=1.0, ls=(0, (4, 3)), zorder=1)
    ax.axhline(0.5, color=MUTED, lw=1.0, ls=(0, (4, 3)), zorder=1)
    b = res["frozen"].get("best_choice")
    if b and b["model"] == sel:                    # the picked epoch lies on this curve
        ax.axvline(b["epoch"], color=TEST, lw=1.0, ls=(0, (4, 3)), zorder=1)
        ax.text(b["epoch"], 1.012, f"교차검증으로 고른 epoch({b['epoch']})", transform=ax.get_xaxis_transform(), ha="center", va="bottom", fontsize=8.8, color=INK2)
    else:
        ax.axvline(60, color=MUTED, lw=1.0, ls=(0, (4, 3)), zorder=1)
        ax.text(60, 1.012, "Argus-V-em은 여기서 멈춤(60)", transform=ax.get_xaxis_transform(), ha="center", va="bottom", fontsize=8.8, color=INK2)
    ax.set_xlim(1, len(cv))
    ax.set_xticks([1, 50, 100, 150, 200, 250, 300])
    ax.set_ylim(0.0, 1.03)
    ax.set_xlabel("epoch (전체 학습 행을 한 번 본 횟수)")
    ax.set_ylabel("같은 도구 안 AUROC")
    tag = "칸에 3개 이상" if key3 == "visible_min3" else "칸에 2개 이상"
    ax.legend(handles=[handle(CV, f"train 안 교차검증, 근거가 보인 위반({tag})", marker=None, line=True),
                       handle(TEST, f"test, 근거가 보인 위반({tag}) — 전체 train으로 맞춘 모델의 10 epoch마다 저장본", line=True),
                       handle(MUTED, "test, 위반 전체", marker="s", line=True)],
              loc="upper center", bbox_to_anchor=(0.5, -0.13), ncol=1, handlelength=2.2, labelspacing=0.35, fontsize=9.3)
    PP.title(fig, f"학습 길이에 따른 test 점수 — {sel.replace('EM', '')}차원 모델",
             "같은 학습의 10 epoch마다 저장본을 test로 잰 값. 참고용이고, 이 곡선으로 epoch을 고르지 않는다(epoch은 교차검증으로 미리 골랐다)")
    PP.save(fig, OUT, "06_학습_길이와_test_점수.png")


def fig07_detection(res, T):
    fig, ax = plt.subplots(figsize=(7.6, 5.0))
    fig.subplots_adjust(top=0.78, left=0.10, right=0.97, bottom=0.22)
    w = 0.16
    drew = False
    for j, (k, col) in enumerate(((PK, TEST), ("em60", MUTED))):
        pv = res["models"][k]["pooled_visible"]
        if not pv:
            continue
        drew = True
        vals = [pv["at_false_alarm"][f"{p}%"]["recall"] * 100 for p in (1, 5, 10)]
        xs = np.arange(3) + (j - 0.5) * (w + 0.03)
        ax.bar(xs, vals, width=w, color=col, edgecolor=SURFACE, linewidth=1.5, zorder=3, label=("주 모델 · " if k == PK else "") + SHORT[k])
        for x, v in zip(xs, vals):
            ax.text(x, v + 1.5, f"{v:.0f}%", ha="center", va="bottom", fontsize=9.3, color=INK2)
    if not drew:
        plt.close(fig)
        return
    pv = res["models"][PK]["pooled_visible"]
    ax.set_xticks(range(3))
    ax.set_xticklabels([f"오경보 {p}% 허용" for p in (1, 5, 10)])
    ax.set_ylabel(f"탐지율 (근거가 보인 위반 {pv['violations']}개 중, %)")
    ax.set_ylim(0, 112)
    ax.set_yticks([0, 25, 50, 75, 100])
    ax.grid(axis="x", visible=False)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncol=2, handlelength=1.2, columnspacing=1.6)
    PP.title(fig, "오경보를 고정했을 때의 탐지율 — test 분할", "정상 호출의 1%·5%·10%만 잘못 경보하도록 문턱을 잡았을 때, 근거가 보인 위반 중 몇 %를 잡는가")
    PP.note(fig, f"모든 도구에 문턱 하나를 적용 · 정상 {pv['rows'] - pv['violations']:,}개와 근거가 보인 위반 {pv['violations']}개만 계산")
    PP.save(fig, OUT, "07_test_오경보_고정_탐지율.png")


def fig08_confusion(res, T):
    pv = res["models"][PK]["pooled_visible"]
    pa = res["models"][PK]["pooled_all_violations"]
    panels = [(n, p) for n, p in (("근거가 보인 위반을 양성으로", pv), ("위반 전체를 양성으로", pa)) if p]
    if not panels:
        return
    fig, axes = plt.subplots(1, len(panels), figsize=(3.4 * len(panels), 3.9))
    axes = np.atleast_1d(axes)
    fig.subplots_adjust(top=0.68, left=0.20 if len(panels) > 1 else 0.30, right=0.97, bottom=0.13, wspace=0.60)
    for ax, (nm, p) in zip(axes, panels):
        o = p["at_false_alarm"]["5%"]
        M = np.array([[o["tp"], o["fn"]], [o["fp"], o["tn"]]], dtype=float)
        frac = M / M.sum(1, keepdims=True)
        for i in range(2):
            for j in range(2):
                q = min(len(PP.SEQ) - 1, int(frac[i, j] * (len(PP.SEQ) - 0.001)))
                ax.add_patch(plt.Rectangle((j + 0.02, 1 - i + 0.02), 0.96, 0.96, color=PP.SEQ[q], zorder=2))
                dark = q >= 3
                ax.text(j + 0.5, 1 - i + 0.60, f"{int(M[i, j]):,}", ha="center", va="center", fontsize=13, fontweight="bold",
                        color="#ffffff" if dark else INK, zorder=3)
                ax.text(j + 0.5, 1 - i + 0.30, f"{frac[i, j] * 100:.0f}%", ha="center", va="center", fontsize=9.5,
                        color="#ffffff" if dark else INK2, zorder=3)
        ax.set_xlim(0, 2)
        ax.set_ylim(0, 2)
        ax.set_xticks([0.5, 1.5])
        ax.set_xticklabels(["경보", "경보 없음"])
        ax.set_yticks([1.5, 0.5])
        ax.set_yticklabels(["실제 위반", "실제 정상"])
        ax.xaxis.tick_top()
        ax.grid(False)
        for sp in ax.spines.values():
            sp.set_visible(False)
        ax.set_title(nm, fontsize=10.3, color=INK, pad=24)
    PP.title(fig, "혼동 행렬 — test 분할 (정상의 5%만 오경보)", f"주 모델({SHORT[PK]}) · 모든 도구에 문턱 하나")
    PP.save(fig, OUT, "08_test_혼동_행렬.png")


# ------------------------------------------------------------------------------------------------ main

def main(argv):
    PP.setup()
    res, R, cvres, base, hist = load()
    set_models(res)
    p = res["models"][PK]["visible_min3"]
    if p["value"] is None:
        headline = "test에는 주 지표를 계산할 도구 칸이 없다"
    elif "확인됨" in res["verdict_by_the_prereg_rule"] and "않" not in res["verdict_by_the_prereg_rule"]:
        headline = f"test에서도 근거가 보인 위반을 가른다 — 주 지표 {p['value']:.2f}"
    else:
        headline = f"test에서는 주 지표가 {p['value']:.2f}로, 사전에 정한 기준(0.90)에 못 미친다"
    T = {"headline": headline}
    fig01_scores(res, T)
    fig02_cv_vs_test(res, cvres, base, T)
    fig03_roc(res, R, T)
    fig04_cells(res, R, T)
    fig05_scores(res, R, T)
    fig06_epochs(res, hist, cvres, T)
    fig07_detection(res, T)
    fig08_confusion(res, T)

    d = res["data"]
    sel, bsel = f"EM{res['frozen']['width_of_the_300_epoch_model']}", base["selected_on_development_oof"]
    L = ["# Argus-V-em300 test 평가 — 숫자 표", "",
         f"사전 고정: `test-eval-prereg.md`. 채점 시각 {res['evaluated_at']}. 표시 규칙 {res['rule']}.",
         f"**사전에 정한 읽는 기준에 따른 결과: {res['verdict_by_the_prereg_rule']}**", "",
         "지표는 '같은 도구를 쓴 호출끼리 위반과 정상을 비교한 AUROC'를 도구 칸별로 구해 위반 수로 가중 평균한 값이다. 도구 이름은 모델 입력이 아니다.", "",
         "## test 데이터", "",
         f"- 시나리오 {d['scenarios']}개(계열 {d['families']}개), 실행 {d['units']}개, 채점한 호출 {d['judged_rows']:,}개(10월 기록 {d['by_source'].get('oct', 0):,} · 11월 기록 {d['by_source'].get('nov', 0):,}).",
         f"- 걸러낸 것: {json.dumps(d['row_filter'], ensure_ascii=False)}",
         f"- 위반 {d['violations']}개(10월 {d['violations_by_source'].get('oct', 0)} · 11월 {d['violations_by_source'].get('nov', 0)}), 정상 {d['normals']:,}개, 도구 칸 {d['cells']}개.",
         f"- 위반 3개 이상·정상 3개 이상인 칸 {d['cells_with_3_violations_and_3_normals']}개(그 안의 위반 {d['violations_in_those_cells']}개). 표시 결과: {json.dumps(d['visibility_categories'], ensure_ascii=False)}.",
         f"- 근거가 보인 위반 {d['visible_violations']}개(서로 다른 입력 {d['distinct_inputs_among_visible']}개). 주 지표 칸: {[short(c) for c in d['cells_visible_min3']] or '없음'}.", "",
         "## 모델별 test 점수 (그림 01)", "",
         "| 모델 | 근거가 보인 위반, 칸에 3개 이상 (주 지표) | 95% 구간 | 칸에 2개 이상 | 2개 이상, 복제를 하나로 침 | 위반 전체 | 위반 전체의 95% 구간 |", "|---|---|---|---|---|---|---|"]

    def cell(m, key):
        v = m[key]
        return "정의되지 않음" if v["value"] is None else f"{v['value']:.3f} (위반 {v['violations']} · 칸 {v['cells']})"

    def ci(m, key):
        c = m[key].get("ci95")
        if not c:
            return "—"
        if c["families"] <= 1:
            return "낼 수 없음 (시나리오 계열 1개)"
        return f"{c['low']:.3f}–{c['high']:.3f}"

    for k in MODELS:
        m = res["models"][k]
        L.append(f"| {MODELS[k]} | {cell(m, 'visible_min3')} | {ci(m, 'visible_min3')} | {cell(m, 'visible_min2')} | {cell(m, 'visible_min2_distinct')} | {cell(m, 'all_violations_min3')} | {ci(m, 'all_violations_min3')} |")
    L += ["", "## train 안 교차검증과 test (그림 02)", "", "| 모델 | 지표 | train 안 교차검증(개발용) | test |", "|---|---|---|---|"]
    pairs = [("em300", cvres["architectures"][sel], f"Argus-V-em300, 300 epoch까지 ({sel})"), ("em60", base["architectures"][bsel], f"Argus-V-em, 60 epoch ({bsel})")]
    if PK == "best":
        b = res["frozen"]["best_choice"]
        pairs.insert(0, ("best", {"visible_min3": {"mean": float(np.mean(b["cv_per_seed"]))}, "visible_min2": {"mean": float(np.mean(b["cv_min2_per_seed"]))},
                                  "all_violations_min3": {"mean": float(np.mean(b["cv_all_violations_per_seed"]))}},
                         f"주 모델: 가장 좋았던 epoch ({b['model']}, {b['epoch']} epoch)"))
    for k, cvm, lab in pairs:
        for key, nm in (("visible_min3", "근거가 보인 위반, 3개 이상"), ("visible_min2", "근거가 보인 위반, 2개 이상"), ("all_violations_min3", "위반 전체")):
            L.append(f"| {lab} | {nm} | {cvm[key]['mean']:.3f} | {fmt(res['models'][k][key]['value'])} |")
    if PK == "best":
        L += ["", "주 모델의 교차검증 값은 후보 900개(폭 3가지 × epoch 300개) 중 가장 높은 값을 고른 것이라 실제보다 높게 나온 값이다."]
    L += ["", "## 문턱 하나를 모든 도구에 적용했을 때 (그림 07·08)", "",
          "| 모델 | 양성으로 본 것 | 위반 수 | 도구를 섞은 AUROC | 평균 정밀도 | 탐지율: 오경보 1% | 5% | 10% | 오경보 5%에서 잡은 위반 / 놓친 위반 / 잘못 경보한 정상 |", "|---|---|---|---|---|---|---|---|---|"]
    for k in MODELS:
        for key, nm in (("pooled_visible", "근거가 보인 위반"), ("pooled_all_violations", "위반 전체")):
            p_ = res["models"][k][key]
            if not p_:
                continue
            a = p_["at_false_alarm"]
            L.append(f"| {SHORT[k]} | {nm} | {p_['violations']} | {p_['auroc']:.3f} | {p_['average_precision']:.3f} | {a['1%']['recall'] * 100:.1f}% | {a['5%']['recall'] * 100:.1f}% | {a['10%']['recall'] * 100:.1f}% | {a['5%']['tp']} / {a['5%']['fn']} / {a['5%']['fp']} |")
    L += ["", "## 도구 칸별 (그림 04)", "", "| 도구 칸 | 시나리오 | 위반 | 근거가 보인 위반 | 정상 | 주 모델: 근거가 보인 위반 | Argus-V-em(60 epoch): 근거가 보인 위반 | 주 모델: 위반 전체 |", "|---|---|---|---|---|---|---|---|"]
    per = {k: {p_["tool"]: p_["auroc"] for p_ in res["models"][k]["visible_min2"]["per_cell"]} for k in (PK, "em60")}
    allper = {p_["tool"]: p_["auroc"] for p_ in res["models"][PK]["all_violations_min3"]["per_cell"]}
    for c, t in sorted(d["cell_table"].items(), key=lambda kv: (-kv[1]["visible_violations"], -kv[1]["violations"], kv[0])):
        L.append(f"| {short(c)} · {PP.SOURCE_KO.get(c.split('|')[1], c.split('|')[1])} | {', '.join(t['scenarios'])} | {t['violations']} | {t['visible_violations']} | {t['normals']} | {fmt(per[PK].get(c))} | {fmt(per['em60'].get(c))} | {fmt(allper.get(c))} |")
    eps = sorted(int(k.split("_")[-1]) for k in res["models"] if k.startswith("em300_epoch_"))
    if eps:
        L += ["", "## 학습 길이에 따른 test 점수 (그림 06, 참고용)", "", "같은 학습의 중간 저장본을 test로 잰 값이다. 이 표로 epoch을 고르지 않는다.", "",
              "| epoch | 근거가 보인 위반, 3개 이상 | 2개 이상 | 위반 전체 |", "|---|---|---|---|"]
        for e in eps:
            m = res["models"][f"em300_epoch_{e:03d}"]
            L.append(f"| {e} | {fmt(m['visible_min3']['value'])} | {fmt(m['visible_min2']['value'])} | {fmt(m['all_violations_min3']['value'])} |")
    L += ["", "## 채점한 파일", ""]
    for k in MODELS:
        f = res["frozen"]["files"][k]
        L.append(f"- {MODELS[k]}: `{f['path']}` SHA-256 `{f['sha256']}`")
    (REPORT / "test_tables.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("saved", (REPORT / "test_tables.md").relative_to(REPO_ROOT))


if __name__ == "__main__":
    main(sys.argv[1:])

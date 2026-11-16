"""Argus-V-p evaluation figures (matplotlib). Reads the scores saved by argus_v_p.py and fits nothing by default.

The training-row scores of the plotted setting come from the saved arrays in artifacts/risk-loop/argus-v-p/
(roc_C_<setting>.npy, p6_condition_c_scores.npy), checked against the recorded value. If that array is missing
the script stops: producing it means re-fitting the setting on all rows, which is training and needs the user's
approval first (then pass --allow-fit).

Every figure states its condition:  A unseen scenario / B seen scenario, new run / C training rows re-scored.
Curves use the mean of the three split scores per row; the quoted AUROC is the official value (mean of the
per-split within-tool AUROC), so a curve's area can differ from it in the third decimal.
Argus-V-p has no epochs (closed-form linear members + a random forest), so there is no epoch figure.

Usage: py -3.11 experiments/risk_loop/argus_loop/argus_v_p_plots.py [--setting P5]   (default: the chosen one)
Output: reports/risk-loop/argus-v-p/figures/<setting>/*.png + tables.md
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import font_manager as fm  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402

from experiments.risk_loop import harness as H  # noqa: E402
from experiments.risk_loop.argus_loop import argus_v_p as AP  # noqa: E402
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402

# ---- style: validated reference palette (slots 1-3 pass the all-pairs colour-blind check), recessive chrome
SURFACE, INK, INK2, MUTED, GRID, AXIS = "#fcfcfb", "#0b0b0b", "#52514e", "#898781", "#e1e0d9", "#c3c2b7"
COND = {"A": {"ko": "처음 보는 시나리오", "color": "#2a78d6", "marker": "o"},
        "B": {"ko": "이미 본 시나리오의 새 실행", "color": "#eb6834", "marker": "s"},
        "C": {"ko": "학습 데이터 재채점", "color": "#1baf7a", "marker": "^"}}
VIOL, NORM, BASE = "#d03b3b", "#898781", "#c3c2b7"
SEQ = ["#cde2fb", "#9ec5f4", "#6da7ec", "#3987e5", "#256abf", "#184f95"]
FIG_W = 9.0
TAG = "Argus-V-p"   # row label of the plotted setting; main() switches it to the setting id when it is not the chosen one


def setup():
    names = {f.name for f in fm.fontManager.ttflist}
    font = next((n for n in ("Malgun Gothic", "NanumGothic", "Gulim", "Batang") if n in names), "sans-serif")
    plt.rcParams.update({
        "font.family": font, "axes.unicode_minus": False, "font.size": 10.5,
        "figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "savefig.facecolor": SURFACE,
        "axes.edgecolor": AXIS, "axes.linewidth": 0.8, "axes.spines.top": False, "axes.spines.right": False,
        "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.7, "grid.linestyle": "-", "axes.axisbelow": True,
        "xtick.color": MUTED, "ytick.color": MUTED, "xtick.labelcolor": INK2, "ytick.labelcolor": INK2,
        "xtick.major.size": 0, "ytick.major.size": 0, "axes.labelcolor": INK2, "text.color": INK,
        "axes.titlesize": 13, "axes.titleweight": "bold", "axes.titlelocation": "left", "axes.titlepad": 12,
        "legend.frameon": False, "legend.fontsize": 10, "lines.linewidth": 2.0, "lines.solid_capstyle": "round",
        "lines.solid_joinstyle": "round", "savefig.dpi": 200, "savefig.bbox": "tight", "savefig.pad_inches": 0.25})
    return font


LBL = dict(facecolor=SURFACE, edgecolor="none", pad=1.5)   # value labels sit on a surface-coloured patch


def title(fig, main, sub=None):
    h = fig.get_size_inches()[1]
    fig.text(0.012, 1 - 0.10 / h, main, ha="left", va="top", fontsize=14, fontweight="bold", color=INK)
    if sub:
        fig.text(0.012, 1 - 0.44 / h, sub, ha="left", va="top", fontsize=10.5, color=INK2)


def note(fig, text):
    h = fig.get_size_inches()[1]
    fig.text(0.012, 0.07 / h, text, ha="left", va="bottom", fontsize=8.8, color=MUTED)


def cond_handles(conds=("A", "B", "C"), line=True):
    return [Line2D([0], [0], color=COND[c]["color"], lw=2 if line else 0, marker=COND[c]["marker"], markersize=8,
                   markerfacecolor=COND[c]["color"], markeredgecolor=SURFACE, markeredgewidth=1.6,
                   label=COND[c]["ko"]) for c in conds]


def ref_line(ax, x=None, y=None, label="", where="top"):
    if x is not None:
        ax.axvline(x, color=MUTED, lw=1.0, ls=(0, (4, 3)), zorder=1)
        ax.text(x, 1.01, label, transform=ax.get_xaxis_transform(), ha="center", va="bottom", fontsize=9, color=INK2)
    if y is not None:
        ax.axhline(y, color=MUTED, lw=1.0, ls=(0, (4, 3)), zorder=1)
        ax.text(1.005, y, label, transform=ax.get_yaxis_transform(), ha="left", va="center", fontsize=9, color=INK2)


def save(fig, out: Path, name: str):
    out.mkdir(parents=True, exist_ok=True)
    fig.canvas.draw()
    for t in fig.texts:                                  # title, subtitle and note must fit the figure width
        over = (t.get_window_extent().x1 - fig.bbox.width) / fig.dpi
        if over > 0.02:
            print(f"  WIDE: {name}: text runs {over:.2f} in past the right edge: {t.get_text()[:36]}…")
    fig.savefig(out / name)
    plt.close(fig)
    print("saved", (out / name).relative_to(REPO_ROOT))


# ------------------------------------------------------------------------------------------------ data

def roc_points(s, y):
    from sklearn.metrics import roc_curve
    f, t, _ = roc_curve(y, s)
    return f, t


def within_tool_roc(cx, s):
    """Violation-weighted mean of the per-cell ROC curves on a common grid; its area = within-tool AUROC."""
    grid = np.linspace(0, 1, 401)
    acc, den, cells = np.zeros_like(grid), 0, {}
    for e in cx.wt(s)["per_tool"]:
        if not e["included"]:
            continue
        m = cx.groups == e["tool"]
        f, t = roc_points(s[m], cx.y[m])
        cells[e["tool"]] = (f, t, e["positives"], e["negatives"], float(H.auroc(s[m], cx.y[m])))
        acc += e["positives"] * np.interp(grid, f, t)
        den += e["positives"]
    return grid, acc / den, cells


def short(cell):
    return cell.split("|")[0]


# ------------------------------------------------------------------------------------------------ figures

def fig01_settings(res, out, chosen):
    S = res["settings"]
    ids = list(S)
    fig, ax = plt.subplots(figsize=(FIG_W, 5.4))
    fig.subplots_adjust(top=0.80, left=0.37, right=0.93, bottom=0.21)
    for i, sid in enumerate(ids):
        yy = len(ids) - 1 - i
        vals = {c: res["results"][sid][c]["value"] for c in "ABC"}
        ax.plot([min(vals.values()), max(vals.values())], [yy, yy], color=BASE, lw=1.4, zorder=2)
        for c in "CBA":
            ax.plot(vals[c], yy, COND[c]["marker"], color=COND[c]["color"], markersize=10, markeredgecolor=SURFACE,
                    markeredgewidth=2, zorder=3)
        ax.text(vals["C"] + 0.014, yy, f"{vals['C']:.2f}", va="center", ha="left", fontsize=9.5, color=INK2, bbox=LBL, zorder=5)
        lo = min(vals["A"], vals["B"])
        ax.text(lo - 0.014, yy, f"{lo:.2f}", va="center", ha="right", fontsize=9.5, color=INK2, bbox=LBL, zorder=5)
    ax.set_yticks(range(len(ids)))
    ax.set_yticklabels([f"{sid}  {S[sid]['ko']}" + ("  ◀ Argus-V-p" if sid == chosen else "") for sid in ids][::-1])
    ax.set_xlim(0.38, 1.04)
    ax.set_ylim(-0.6, len(ids) - 0.4)
    ax.set_xlabel("같은 도구 안 AUROC (0.5 = 우연)")
    ax.grid(axis="y", visible=False)
    ref_line(ax, x=0.5, label="우연")
    ref_line(ax, x=0.9, label="목표 0.90")
    ax.legend(handles=cond_handles(line=False), loc="upper center", bbox_to_anchor=(0.32, -0.15), ncol=3,
              handletextpad=0.3, columnspacing=1.4)
    title(fig, "같은 모델이라도 무엇을 채점하느냐에 따라 점수가 크게 다르다",
          "설정 6개 × 조건 3개. 왼쪽 숫자는 학습에 없던 데이터(●■) 중 낮은 쪽, 오른쪽 숫자는 학습 데이터 재채점(▲)")
    note(fig, "학습 분할 판정 행 9,278개 · 평가에 들어가는 위반 48개(칸 9개) · 조건 A·B는 데이터 나누기 3가지 평균")
    save(fig, out, "01_설정별_조건별_AUROC.png")


def fig02_roc(cx, sc, vals, out, name_ko):
    fig, ax = plt.subplots(figsize=(6.6, 6.4))
    fig.subplots_adjust(top=0.84, left=0.12, right=0.96, bottom=0.12)
    ax.plot([0, 1], [0, 1], color=BASE, lw=1.2, zorder=1)
    for c in "CBA":
        g, t, _ = within_tool_roc(cx, sc[c])
        ax.plot(g, t, color=COND[c]["color"], lw=2, zorder=3, label=f"{COND[c]['ko']}  {vals[c]:.2f}")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1.005)
    ax.set_aspect("equal")
    ax.set_xlabel("오경보율 (정상을 위반으로 본 비율)")
    ax.set_ylabel("탐지율 (위반을 잡은 비율)")
    hh, ll = ax.get_legend_handles_labels()
    ax.legend(hh[::-1], ll[::-1], loc="lower right", title="조건 · 같은 도구 안 AUROC", title_fontsize=9.5, handlelength=1.6)
    ax.text(0.62, 0.56, "우연 수준", rotation=45, color=MUTED, fontsize=9, ha="center", va="center")
    title(fig, f"ROC 곡선 — {name_ko}", "칸(도구×출처)별 곡선을 위반 수로 가중 평균. 곡선 아래 넓이가 같은 도구 안 AUROC")
    save(fig, out, "02_ROC_곡선.png")


def fig03_roc_cells(cx, sc, out, name_ko):
    cells = within_tool_roc(cx, sc["A"])[2]
    order = sorted(cells, key=lambda k: -cells[k][4])
    fig, axes = plt.subplots(3, 3, figsize=(FIG_W, 9.2), sharex=True, sharey=True)
    fig.subplots_adjust(top=0.85, left=0.08, right=0.98, bottom=0.10, hspace=0.42, wspace=0.12)
    per = {c: within_tool_roc(cx, sc[c])[2] for c in "ABC"}
    for ax, cell in zip(axes.ravel(), order):
        ax.plot([0, 1], [0, 1], color=BASE, lw=1.0)
        for c in "CBA":
            f, t, p, n, a = per[c][cell]
            ax.plot(f, t, color=COND[c]["color"], lw=1.8)
        f, t, p, n, a = per["A"][cell]
        ax.set_title(f"{short(cell)}\n위반 {p} · 정상 {n} · A {a:.2f}", fontsize=9.5, fontweight="normal", color=INK, pad=5)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1.02)
        ax.set_xticks([0, 0.5, 1])
        ax.set_yticks([0, 0.5, 1])
    fig.text(0.5, 0.045, "오경보율", ha="center", color=INK2)
    fig.text(0.015, 0.48, "탐지율", va="center", rotation=90, color=INK2)
    fig.legend(handles=cond_handles(), loc="upper left", bbox_to_anchor=(0.06, 0.945), ncol=3, handletextpad=0.4,
               columnspacing=1.6)
    title(fig, f"칸별 ROC 곡선 — {name_ko}", None)
    note(fig, "칸마다 위반이 3~9개뿐이라 곡선이 계단 모양이고 한 개 차이로 크게 움직인다 · 제목의 A = 처음 보는 시나리오 AUROC")
    save(fig, out, "03_칸별_ROC_곡선.png")


def fig04_pr(cx, sc, out, name_ko):
    from sklearn.metrics import average_precision_score, precision_recall_curve
    prev = float(cx.y.mean())
    fig, ax = plt.subplots(figsize=(7.6, 5.4))
    fig.subplots_adjust(top=0.80, left=0.11, right=0.86, bottom=0.14)
    for c in "CBA":
        p, r, _ = precision_recall_curve(cx.y, sc[c])
        ap = average_precision_score(cx.y, sc[c])
        ax.plot(r, p, color=COND[c]["color"], lw=2, label=f"{COND[c]['ko']}  평균 정밀도 {ap:.2f}")
    ref_line(ax, y=prev, label=f"아무렇게나 찍을 때 {prev * 100:.1f}%")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1.02)
    ax.set_xlabel("재현율 (위반 중 잡은 비율)")
    ax.set_ylabel("정밀도 (경보 중 진짜 위반 비율)")
    hh, ll = ax.get_legend_handles_labels()
    ax.legend(hh[::-1], ll[::-1], loc="upper right", handlelength=1.6)
    title(fig, f"정밀도-재현율 곡선 — {name_ko}",
          f"판정 행 전체 {len(cx.y):,}개(위반 {int(cx.y.sum())}개, {prev * 100:.1f}%)를 도구 구분 없이 섞어 본 값")
    note(fig, "위반이 드물어 정밀도는 낮게 나온다 · 도구를 섞어 잰 값이라 같은 도구 안 AUROC와 직접 비교하지 않는다")
    save(fig, out, "04_정밀도_재현율_곡선.png")


def fig05_scores(cx, sc, out, name_ko):
    cells = [e["tool"] for e in cx.wt(sc["A"])["per_tool"] if e["included"]]
    rng = np.random.default_rng(0)
    fig, axes = plt.subplots(3, 1, figsize=(FIG_W, 9.4), sharex=True)
    fig.subplots_adjust(top=0.87, left=0.09, right=0.97, bottom=0.13, hspace=0.30)
    for ax, c in zip(axes, "ABC"):
        for i, cell in enumerate(cells):
            m = np.nonzero(cx.groups == cell)[0]
            for lab, col, mk, fc, z, off in ((0, NORM, "o", "none", 2, -0.14), (1, VIOL, "D", VIOL, 3, 0.14)):
                idx = m[cx.y[m] == lab]
                xs = i + off + rng.uniform(-0.09, 0.09, len(idx))
                ax.plot(xs, sc[c][idx], mk, markersize=6.5 if lab else 6, markerfacecolor=fc, markeredgecolor=col if not lab else SURFACE,
                        markeredgewidth=1.2, color=col, zorder=z, lw=0)
        ax.set_ylim(-0.03, 1.03)
        ax.set_yticks([0, 0.5, 1])
        ax.set_ylabel("모델 점수")
        ax.set_title(f"{c}. {COND[c]['ko']}", fontsize=10.5, color=INK, pad=6)
        ax.grid(axis="x", visible=False)
    axes[-1].set_xticks(range(len(cells)))
    axes[-1].set_xticklabels([short(c).replace("_", "\n") for c in cells], fontsize=8.6)
    fig.legend(handles=[Line2D([0], [0], lw=0, marker="D", markersize=7, markerfacecolor=VIOL, markeredgecolor=SURFACE, label="위반 호출"),
                        Line2D([0], [0], lw=0, marker="o", markersize=7, markerfacecolor="none", markeredgecolor=NORM, label="정상 호출")],
               loc="upper left", bbox_to_anchor=(0.07, 0.935), ncol=2, handletextpad=0.3, columnspacing=1.6)
    title(fig, f"칸별 점수 분포 — {name_ko}", None)
    note(fig, "잘 가르는 칸은 위반(◆)이 정상(○)보다 위에 모인다 · 평가에 들어가는 9개 칸, 위반 48개 · 점수는 확률이 아니며 같은 칸 안에서만 비교한다")
    save(fig, out, "05_칸별_점수_분포.png")


def op_point(cx, s, fa):
    thr = float(np.quantile(s[cx.y == 0], 1 - fa))
    alarm = s > thr
    tp = int((alarm & (cx.y == 1)).sum())
    fp = int((alarm & (cx.y == 0)).sum())
    fn = int((~alarm & (cx.y == 1)).sum())
    tn = int((~alarm & (cx.y == 0)).sum())
    return {"threshold": thr, "tp": tp, "fp": fp, "fn": fn, "tn": tn, "recall": tp / max(1, tp + fn),
            "false_alarm": fp / max(1, fp + tn), "precision": tp / max(1, tp + fp)}


def fig06_detection(cx, sc, out, name_ko):
    fas = (0.01, 0.05, 0.10)
    fig, ax = plt.subplots(figsize=(7.8, 5.0))
    fig.subplots_adjust(top=0.78, left=0.10, right=0.97, bottom=0.22)
    w = 0.11
    table = {}
    for j, c in enumerate("ABC"):
        vals = [op_point(cx, sc[c], fa)["recall"] * 100 for fa in fas]
        table[c] = vals
        xs = np.arange(len(fas)) + (j - 1) * (w + 0.03)
        ax.bar(xs, vals, width=w, color=COND[c]["color"], edgecolor=SURFACE, linewidth=1.5, zorder=3, label=COND[c]["ko"])
        for x, v in zip(xs, vals):
            ax.text(x, v + 1.2, f"{v:.0f}%", ha="center", va="bottom", fontsize=9.3, color=INK2)
    ax.set_xticks(range(len(fas)))
    ax.set_xticklabels([f"오경보 {int(f * 100)}% 허용" for f in fas])
    ax.set_ylabel("탐지율 (위반 76개 중 잡은 비율, %)")
    ax.set_ylim(0, max(100, max(max(v) for v in table.values()) + 12) if max(max(v) for v in table.values()) > 85 else max(max(v) for v in table.values()) + 14)
    ax.grid(axis="x", visible=False)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncol=3, handlelength=1.2, columnspacing=1.6)
    title(fig, f"오경보를 고정했을 때의 탐지율 — {name_ko}",
          "정상 호출의 1%·5%·10%만 잘못 경보하도록 문턱을 잡았을 때, 위반 호출 중 몇 %를 잡는가")
    note(fig, "판정 행 전체 9,278개 기준(도구 구분 없이 문턱 하나)")
    save(fig, out, "06_오경보_고정_탐지율.png")
    return table


def fig07_confusion(cx, sc, out, name_ko, fa=0.05):
    fig, axes = plt.subplots(1, 3, figsize=(FIG_W, 3.9))
    fig.subplots_adjust(top=0.70, left=0.09, right=0.98, bottom=0.12, wspace=0.42)
    out_tab = {}
    for ax, c in zip(axes, "ABC"):
        o = op_point(cx, sc[c], fa)
        out_tab[c] = o
        M = np.array([[o["tp"], o["fn"]], [o["fp"], o["tn"]]], dtype=float)
        frac = M / M.sum(1, keepdims=True)
        for i in range(2):
            for j in range(2):
                k = min(len(SEQ) - 1, int(frac[i, j] * (len(SEQ) - 0.001)))
                ax.add_patch(plt.Rectangle((j + 0.02, 1 - i + 0.02), 0.96, 0.96, color=SEQ[k], zorder=2))
                dark = k >= 3
                ax.text(j + 0.5, 1 - i + 0.60, f"{int(M[i, j]):,}", ha="center", va="center", fontsize=13,
                        fontweight="bold", color="#ffffff" if dark else INK, zorder=3)
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
        ax.set_title(f"{c}. {COND[c]['ko']}", fontsize=10.3, color=INK, pad=24)
    title(fig, "혼동 행렬 (정상의 5%만 오경보하도록 문턱을 잡았을 때)", name_ko)
    note(fig, "칸 안: 건수와 그 행에서의 비율 · 판정 행 전체 9,278개(위반 76개)")
    save(fig, out, "07_혼동_행렬.png")
    return out_tab


def fig08_threshold(cx, sc, out, name_ko):
    fig, axes = plt.subplots(1, 3, figsize=(FIG_W, 4.3), sharey=True)
    fig.subplots_adjust(top=0.72, left=0.08, right=0.94, bottom=0.25, wspace=0.16)
    styles = {"재현율": "-", "정밀도": (0, (5, 2)), "F1": (0, (1, 1.6))}
    for ax, c in zip(axes, "ABC"):
        thr = np.linspace(0.02, 0.995, 160)
        rec, pre, f1 = [], [], []
        for t in thr:
            al = sc[c] > t
            tp = float((al & (cx.y == 1)).sum())
            r = tp / cx.y.sum()
            p = tp / max(1.0, al.sum())
            rec.append(r)
            pre.append(p)
            f1.append(0 if p + r == 0 else 2 * p * r / (p + r))
        for nm, v in (("재현율", rec), ("정밀도", pre), ("F1", f1)):
            ax.plot(thr, v, color=COND[c]["color"], lw=2, ls=styles[nm])
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1.02)
        ax.set_xlabel("경보 문턱 (모델 점수)")
        ax.set_title(f"{c}. {COND[c]['ko']}", fontsize=10.3, color=INK, pad=6)
    axes[0].set_ylabel("값")
    fig.legend(handles=[Line2D([0], [0], color=INK2, lw=2, ls=ls, label=nm) for nm, ls in styles.items()],
               loc="lower center", bbox_to_anchor=(0.5, 0.03), ncol=3, handlelength=2.6, columnspacing=2.0)
    title(fig, f"문턱에 따른 재현율·정밀도·F1 — {name_ko}", "문턱을 올리면 경보가 줄어 정밀도는 오르고 재현율은 내려간다. 선 모양으로 구분")
    save(fig, out, "08_문턱별_재현율_정밀도.png")


def fig09_cells(res, sid, out, name_ko):
    R = res["results"][sid]
    cells = sorted(R["A"]["per_cell"], key=lambda k: R["A"]["per_cell"][k]["auroc"])
    fig, ax = plt.subplots(figsize=(FIG_W, 5.6))
    fig.subplots_adjust(top=0.80, left=0.36, right=0.94, bottom=0.20)
    for yy, cell in enumerate(cells):
        vals = {c: R[c]["per_cell"][cell]["auroc"] for c in "ABC"}
        ax.plot([min(vals.values()), max(vals.values())], [yy, yy], color=BASE, lw=1.4, zorder=2)
        for c in "CBA":
            ax.plot(vals[c], yy, COND[c]["marker"], color=COND[c]["color"], markersize=10, markeredgecolor=SURFACE,
                    markeredgewidth=2, zorder=3)
    ax.set_yticks(range(len(cells)))
    ax.set_yticklabels([f"{short(c)}  (위반 {R['A']['per_cell'][c]['violations']} · 정상 {R['A']['per_cell'][c]['normals']})" for c in cells])
    ax.set_xlim(-0.02, 1.04)
    ax.set_ylim(-0.6, len(cells) - 0.4)
    ax.set_xlabel("칸 안 AUROC")
    ax.grid(axis="y", visible=False)
    ref_line(ax, x=0.5, label="우연")
    ref_line(ax, x=0.9, label="0.90")
    ax.legend(handles=cond_handles(line=False), loc="upper center", bbox_to_anchor=(0.30, -0.15), ncol=3,
              handletextpad=0.3, columnspacing=1.4)
    title(fig, f"도구(칸)별 AUROC — {name_ko}", "아래에서 위로 '처음 보는 시나리오' 점수가 높은 순서")
    note(fig, "칸마다 위반이 3~9개라 값 하나하나의 오차가 크다")
    save(fig, out, "09_칸별_AUROC.png")


def fig10_gap(res, out):
    pairs = (("같은 rollout 쌍 학습 (기존 방식)", "P1", "P3"), ("같은 도구 안 학습", "P2", "P4"))
    fig, axes = plt.subplots(1, 2, figsize=(FIG_W, 4.9), sharey=True)
    fig.subplots_adjust(top=0.74, left=0.08, right=0.90, bottom=0.22, wspace=0.30)
    for ax, (nm, a, b) in zip(axes, pairs):
        V = {c: [res["results"][a][c]["value"], res["results"][b][c]["value"]] for c in "ABC"}
        for side in (0, 1):                                  # nudge labels that would touch (text only, marks stay)
            order = sorted("ABC", key=lambda c: V[c][side])
            pos = {c: V[c][side] for c in order}
            for lo_c, hi_c in zip(order, order[1:]):
                if pos[hi_c] - pos[lo_c] < 0.034:
                    mid = (pos[hi_c] + pos[lo_c]) / 2
                    pos[lo_c], pos[hi_c] = mid - 0.017, mid + 0.017
            for c in "ABC":
                ax.text(1.07 if side else -0.07, pos[c], f"{V[c][side]:.2f}", va="center", ha="left" if side else "right",
                        fontsize=9.5, color=INK2)
        for c in "CBA":
            ax.plot([0, 1], V[c], color=COND[c]["color"], lw=2, marker=COND[c]["marker"], markersize=9,
                    markeredgecolor=SURFACE, markeredgewidth=2, zorder=3)
        ax.set_xlim(-0.35, 1.35)
        ax.set_xticks([0, 1])
        ax.set_xticklabels([f"기본\n(PCA 32차원)", f"규제 완화\n(128차원, 벌점 1/10)"])
        ax.set_ylim(0.45, 1.02)
        ax.set_title(nm, fontsize=10.5, color=INK, pad=6)
        ax.grid(axis="x", visible=False)
        ax.axhline(0.9, color=MUTED, lw=1.0, ls=(0, (4, 3)), zorder=1)
        ax.axhline(0.5, color=MUTED, lw=1.0, ls=(0, (4, 3)), zorder=1)
    axes[1].text(1.38, 0.9, "목표 0.90", va="center", ha="left", fontsize=9, color=INK2)
    axes[1].text(1.38, 0.5, "우연", va="center", ha="left", fontsize=9, color=INK2)
    axes[0].set_ylabel("같은 도구 안 AUROC")
    fig.legend(handles=cond_handles(), loc="lower center", bbox_to_anchor=(0.5, 0.02), ncol=3, columnspacing=1.6)
    title(fig, "모델을 자유롭게 풀수록 학습 데이터 점수만 오른다", "규제를 풀었을 때 조건별 점수 변화. 학습에 없던 데이터(●■)에서는 오르지 않는다")
    save(fig, out, "10_규제_완화와_과적합.png")


def fig11_baselines(res, sid, ci, out, name_ko, shuffle):
    R = res["results"][sid]
    rows = [("원래 Argus-V1 (처음 보는 시나리오)", 0.526, BASE, None),
            ("모델 없이 '앞선 step일수록 위반' 규칙", 0.730, BASE, None),
            ("지금 최고 모델 T7-a (처음 보는 시나리오)", 0.721, BASE, (0.569, 0.825)),
            (f"{TAG} · A {COND['A']['ko']}", R["A"]["value"], COND["A"]["color"], ci.get("A")),
            (f"{TAG} · B {COND['B']['ko']}", R["B"]["value"], COND["B"]["color"], ci.get("B")),
            (f"{TAG} · C {COND['C']['ko']}", R["C"]["value"], COND["C"]["color"], None)]
    if shuffle is not None:
        rows.append(("점검: 학습 라벨을 섞고 B를 다시 잼", shuffle, BASE, None))
    fig, ax = plt.subplots(figsize=(FIG_W, 5.2))
    fig.subplots_adjust(top=0.82, left=0.42, right=0.93, bottom=0.12)
    for i, (lab, v, col, c) in enumerate(rows):
        yy = len(rows) - 1 - i
        ax.barh(yy, v - 0.4, left=0.4, height=0.42, color=col, edgecolor=SURFACE, linewidth=1.5, zorder=3)
        if c:
            ax.plot([c[0], c[1]], [yy, yy], color=INK2, lw=1.2, zorder=4)
        ax.text((c[1] if c else v) + 0.012, yy, f"{v:.2f}", va="center", ha="left", fontsize=9.8, color=INK, bbox=LBL, zorder=5)
    ax.set_yticks(range(len(rows)))
    ax.set_yticklabels([r[0] for r in rows][::-1])
    ax.set_xlim(0.4, 1.04)
    ax.set_xlabel("같은 도구 안 AUROC")
    ax.grid(axis="y", visible=False)
    ref_line(ax, x=0.5, label="우연")
    ref_line(ax, x=0.9, label="목표 0.90")
    title(fig, f"기준선과 비교 — {name_ko}", "가는 선은 95% 구간(시나리오 계열을 다시 뽑아 계산). 평가 위반이 48개라 구간이 넓다")
    note(fig, "'앞선 step' 규칙은 방향을 결과를 보고 정한 낙관값 · 원래 Argus-V1과 T7-a는 기존 기록(데이터 나누기 3·10가지 평균)")
    save(fig, out, "11_기준선_비교.png")


def fig12_visible(vres, res, sid, out, name_ko):
    V = vres["settings"][sid]
    rows = [("모델 없이 '앞선 step일수록 위반' 규칙", 0.730, vres["order rule (earlier step = violation)"]["min3"]["value"], BASE),
            ("지금 최고 모델 T7-a (처음 보는 시나리오)", 0.721, vres["T7-a unseen scenario (saved, 10 splits)"]["min3"]["value"], BASE)]
    for c in "ABC":
        rows.append((f"{TAG} · {c} {COND[c]['ko']}", res["results"][sid][c]["value"], V[c]["min3"]["value"], COND[c]["color"]))
    nvis, ncell = V["A"]["min3"]["violations"], V["A"]["min3"]["cells"]
    fig, ax = plt.subplots(figsize=(FIG_W, 4.8))
    fig.subplots_adjust(top=0.78, left=0.42, right=0.93, bottom=0.22)
    for i, (lab, allv, visv, col) in enumerate(rows):
        yy = len(rows) - 1 - i
        ax.plot([allv, visv], [yy, yy], color=BASE, lw=1.6, zorder=2)
        ax.plot(allv, yy, "o", markersize=10, markerfacecolor=SURFACE, markeredgecolor=col if col != BASE else MUTED, markeredgewidth=2, zorder=3)
        ax.plot(visv, yy, "o", markersize=10, markerfacecolor=col if col != BASE else MUTED, markeredgecolor=SURFACE, markeredgewidth=2, zorder=4)
        ax.text(max(allv, visv) + 0.024, yy, f"{visv:.2f}", va="center", ha="left", fontsize=9.8, color=INK, bbox=LBL, zorder=5)
    ax.set_yticks(range(len(rows)))
    ax.set_yticklabels([r[0] for r in rows][::-1])
    ax.set_xlim(0.4, 1.06)
    ax.set_ylim(-0.6, len(rows) - 0.4)
    ax.set_xlabel("같은 도구 안 AUROC")
    ax.grid(axis="y", visible=False)
    ref_line(ax, x=0.5, label="우연")
    ref_line(ax, x=0.9, label="목표 0.90")
    ax.legend(handles=[Line2D([0], [0], lw=0, marker="o", markersize=9, markerfacecolor=MUTED, markeredgecolor=SURFACE, label=f"행동 전에 근거가 보인 위반만 (위반 {nvis}개, 칸 {ncell}개)"),
                       Line2D([0], [0], lw=0, marker="o", markersize=9, markerfacecolor=SURFACE, markeredgecolor=MUTED, markeredgewidth=2, label="평가 위반 전체 (48개, 칸 9개)")],
              loc="upper center", bbox_to_anchor=(0.25, -0.16), ncol=2, handletextpad=0.3, columnspacing=1.6)
    title(fig, f"목표 기준으로 다시 잰 점수 — {name_ko}", "목표 기준 = 행동 전에 근거가 보인 위반만. 채운 점과 오른쪽 숫자가 그 값, 빈 점은 평가 위반 전체 기준 값")
    note(fig, f"표시 규칙은 잠정판 · 이 기준에 드는 위반이 {nvis}개뿐이라 값이 크게 흔들린다(서로 다른 입력은 {vres['unique_feature_rows_among_visible']}개)")
    save(fig, out, "12_목표_기준_점수.png")


SCORE_TABLE = REPO_ROOT / "argus_hook" / "replay_assets" / "argus_v_p_scores.json"
SOURCE_KO = {"oct": "10월", "nov": "11월"}


def fig13_tool_levels(sid, out, name_ko):
    """Training-row scores per tool cell with the per-tool alarm threshold the replay demo uses (stored table)."""
    if not SCORE_TABLE.is_file():
        return None
    table = json.loads(SCORE_TABLE.read_text(encoding="utf-8"))
    if sid not in table["models"]:
        return None
    k = table["step_columns"].index(sid)
    by = {}
    for u in table["units"].values():
        for r in u["steps"]:
            by.setdefault(f"{r[1]}|{u['source']}", ([], []))[int(r[2])].append(float(r[k]))
    th = table["models"][sid]["tool_thresholds"]
    viol_cells = sorted((c for c in by if by[c][1]), key=lambda c: (c in th, th[c]["threshold"] if c in th else 0.0))
    normal_only = sorted((c for c in by if not by[c][1]), key=lambda c: -len(by[c][0]))[:3]
    if "read_file|oct" in by and "read_file|oct" not in normal_only and not by["read_file|oct"][1]:
        normal_only.append("read_file|oct")
    normal_only = normal_only[::-1]
    rows = normal_only + [None] + viol_cells                 # bottom -> top; None = gap between the two groups
    rng = np.random.default_rng(0)
    fig, ax = plt.subplots(figsize=(FIG_W + 1.2, 0.285 * len(rows) + 2.6))
    hin = fig.get_size_inches()[1]
    axes_h = hin - 1.25 - 1.30
    fig.subplots_adjust(top=1 - 1.25 / hin, left=0.335, right=0.80, bottom=1.30 / hin)
    out_rows = []
    for yy, cell in enumerate(rows):
        if cell is None:
            continue
        normals, viols = np.asarray(by[cell][0]), np.asarray(by[cell][1])
        big = len(normals) > 200
        ax.plot(normals, yy + rng.uniform(-0.24, 0.24, len(normals)), "o", markersize=3.6 if big else 5.2, markerfacecolor="none",
                markeredgecolor=NORM, markeredgewidth=0.7 if big else 1.1, alpha=0.45 if big else 1.0, lw=0, zorder=2)
        ax.plot(viols, yy + rng.uniform(-0.12, 0.12, len(viols)), "D", markersize=6.2, markerfacecolor=VIOL, markeredgecolor=SURFACE,
                markeredgewidth=1.1, lw=0, zorder=4)
        t = th.get(cell)
        if t:
            ax.plot([t["threshold"]] * 2, [yy - 0.36, yy + 0.36], color=INK, lw=2.0, zorder=5, solid_capstyle="butt")
            txt = f"위반 {t['caught']}/{t['violations']} · 정상 {t['false_alarms']}/{t['normals']}"
        elif len(viols):
            txt = "정상 호출이 없어 기준 없음"
        else:
            txt = "위반 사례 없음"
        ax.text(1.02, yy, txt, transform=ax.get_yaxis_transform(), va="center", ha="left", fontsize=8.6, color=INK2)
        out_rows.append((cell, len(viols), len(normals), t))
    labels = []
    for cell in rows:
        if cell is None:
            labels.append("")
            continue
        tool, src = cell.split("|")
        labels.append(f"{tool} · {SOURCE_KO.get(src, src)}  (위반 {len(by[cell][1])} · 정상 {len(by[cell][0]):,})")
    ax.set_yticks(range(len(rows)))
    ax.set_yticklabels(labels, fontsize=8.8)
    ax.set_ylim(-0.7, len(rows) - 0.3)
    ax.set_xlim(-0.02, 1.02)
    ax.set_xlabel("모델 점수 (0~1, 확률 아님)")
    ax.grid(axis="y", visible=False)
    gap = rows.index(None)
    ax.axhline(gap, color=GRID, lw=0.9, zorder=1)
    ax.text(0.0, gap + 0.08, "▲ 위반 사례가 있는 도구   ▼ 정상 호출만 있는 도구(예)", fontsize=8.6, color=MUTED, va="bottom", ha="left")
    ax.text(1.02, len(rows) - 0.35, "기준을 넘은 수(경보)", transform=ax.get_yaxis_transform(), va="bottom", ha="left", fontsize=8.6, color=MUTED)
    ax.legend(handles=[Line2D([0], [0], lw=0, marker="D", markersize=7, markerfacecolor=VIOL, markeredgecolor=SURFACE, label="위반 호출"),
                       Line2D([0], [0], lw=0, marker="o", markersize=7, markerfacecolor="none", markeredgecolor=NORM, label="정상 호출"),
                       Line2D([0], [0], lw=0, marker="|", markersize=13, markeredgewidth=2, color=INK, label="그 도구의 판정 기준")],
              loc="upper center", bbox_to_anchor=(0.5, -0.55 / axes_h), ncol=3, handletextpad=0.3, columnspacing=1.8)
    n_sep = sum(1 for c in viol_cells if c in th and th[c]["kind"] == "separable")
    title(fig, "도구마다 점수대가 다르다 — 그래서 판정 기준을 도구별로 둔다",
          f"{name_ko} · 학습 데이터 재채점 · 위반 사례가 있는 도구 칸 {len(viol_cells)}개(위반과 정상이 겹치지 않는 칸 {n_sep}개)")
    note(fig, "기준은 같은 학습 기록의 위반과 정상 사이에 그었다(새 상황의 성능이 아님) · 다른 도구의 점수와는 비교할 수 없다 · 재생 도구의 판정이 이 기준을 쓴다")
    save(fig, out, "13_도구별_점수대와_판정_기준.png")
    return out_rows[::-1]


# ------------------------------------------------------------------------------------------------ main

def main(argv):
    font = setup()
    res = json.loads((AP.OUT / "results.json").read_text(encoding="utf-8"))
    sid = argv[argv.index("--setting") + 1] if "--setting" in argv else res["chosen"]["setting"]
    chosen = res["chosen"]["setting"]
    global TAG
    TAG = "Argus-V-p" if sid == chosen else sid
    name_ko = f"{sid} {res['settings'][sid]['ko']}" + (" (Argus-V-p)" if sid == chosen else "")
    out = AP.REPORT / "figures" / sid
    print("font", font, "| setting", sid, "| chosen", chosen)
    cx = AP.Ctx()
    sc, vals, seeds = {}, {}, {}
    for c in ("A", "B"):
        seeds[c] = [np.load(AP.oof_path(sid, c, s)) for s in AP.SEEDS]
        sc[c] = np.mean(seeds[c], axis=0)
        vals[c] = res["results"][sid][c]["value"]
    cached = AP.OUT / ("p6_condition_c_scores.npy" if sid == "P6" else f"roc_C_{sid}.npy")
    if cached.is_file():
        sc["C"] = np.load(cached)                            # saved training-row scores: nothing is fitted
    elif "--allow-fit" in argv:
        sc["C"] = cx.fit(sid, np.arange(cx.n), cx.y, np.zeros(0, np.int64))[0]
        np.save(cached, sc["C"])
    else:
        raise SystemExit(f"{cached.name} is missing. Making it re-fits {sid} on all rows (training): get the user's "
                         "approval first, then run again with --allow-fit.")
    vals["C"] = res["results"][sid]["C"]["value"]
    assert abs(cx.wt(sc["C"])["value"] - vals["C"]) < 1e-6
    ci = {}
    for c in ("A", "B"):
        b = E.family_bootstrap_ci(seeds[c], cx.rows)
        ci[c] = (b["ci_low"], b["ci_high"])
    shuffle = (res.get("shuffle_check_B") or {}).get("mean") if (res.get("shuffle_check_B") or {}).get("setting") == sid else None

    fig01_settings(res, out, chosen)
    fig02_roc(cx, sc, vals, out, name_ko)
    fig03_roc_cells(cx, sc, out, name_ko)
    fig04_pr(cx, sc, out, name_ko)
    fig05_scores(cx, sc, out, name_ko)
    det = fig06_detection(cx, sc, out, name_ko)
    conf = fig07_confusion(cx, sc, out, name_ko)
    fig08_threshold(cx, sc, out, name_ko)
    fig09_cells(res, sid, out, name_ko)
    fig10_gap(res, out)
    fig11_baselines(res, sid, ci, out, name_ko, shuffle)
    vpath = AP.REPORT / "visible_results.json"
    vres = json.loads(vpath.read_text(encoding="utf-8")) if vpath.is_file() else None
    if vres:
        fig12_visible(vres, res, sid, out, name_ko)
    levels = fig13_tool_levels(sid, out, name_ko)

    # table twin of the figures
    from sklearn.metrics import average_precision_score
    L = [f"# 그래프에 쓴 숫자 — {name_ko}", "",
         "조건: A 처음 보는 시나리오 / B 이미 본 시나리오의 새 실행 / C 학습 데이터 재채점. 지표는 같은 도구 안 AUROC.", "",
         "## 설정 6개 × 조건 3개 (그림 01·10)", "", "| 설정 | A | B | C |", "|---|---|---|---|"]
    for k, s in res["settings"].items():
        r = res["results"][k]
        L.append(f"| {k} {s['ko']} | {r['A']['value']:.3f} | {r['B']['value']:.3f} | {r['C']['value']:.3f} |")
    L += ["", f"## {name_ko} 요약 (그림 02·04·11)", "", "| 조건 | 같은 도구 안 AUROC | 95% 구간 | 전체 AUROC(도구 섞음) | 평균 정밀도 |", "|---|---|---|---|---|"]
    for c in "ABC":
        cc = f"{ci[c][0]:.3f}–{ci[c][1]:.3f}" if c in ci else "—"
        L.append(f"| {c} {COND[c]['ko']} | {vals[c]:.3f} | {cc} | {H.auroc(sc[c], cx.y):.3f} | {average_precision_score(cx.y, sc[c]):.3f} |")
    L += ["", "## 칸별 AUROC (그림 03·09)", "", "| 칸 | 위반 | 정상 | A | B | C |", "|---|---|---|---|---|---|"]
    R = res["results"][sid]
    for cell in sorted(R["A"]["per_cell"], key=lambda k: -R["A"]["per_cell"][k]["auroc"]):
        p = R["A"]["per_cell"][cell]
        L.append(f"| {short(cell)} | {p['violations']} | {p['normals']} | {p['auroc']:.3f} | {R['B']['per_cell'][cell]['auroc']:.3f} | {R['C']['per_cell'][cell]['auroc']:.3f} |")
    L += ["", "## 오경보를 고정했을 때의 탐지율 % (그림 06)", "", "| 조건 | 오경보 1% | 5% | 10% |", "|---|---|---|---|"]
    for c in "ABC":
        L.append(f"| {c} | {det[c][0]:.1f} | {det[c][1]:.1f} | {det[c][2]:.1f} |")
    L += ["", "## 혼동 행렬, 오경보 5% 문턱 (그림 07)", "", "| 조건 | 위반을 경보 | 위반을 놓침 | 정상을 경보 | 정상에 경보 없음 | 정밀도 |", "|---|---|---|---|---|---|"]
    for c in "ABC":
        o = conf[c]
        L.append(f"| {c} | {o['tp']} | {o['fn']} | {o['fp']} | {o['tn']} | {o['precision'] * 100:.1f}% |")
    if vres:
        V = vres["settings"][sid]
        L += ["", "## 목표 기준: 행동 전에 근거가 보인 위반만 (그림 12)", "",
              f"표시 규칙 {vres['rule']}. 근거가 보인 위반 {vres['visible_violations']}개(서로 다른 입력 {vres['unique_feature_rows_among_visible']}개) / 평가 위반 {vres['all_judged_cell_violations']}개.", "",
              "| 대상 | 전체 위반 기준 | 근거가 보인 위반만 (칸에 위반 3개 이상) | 같은 값, 칸에 위반 2개 이상 |", "|---|---|---|---|"]
        o = vres["order rule (earlier step = violation)"]
        t = vres["T7-a unseen scenario (saved, 10 splits)"]
        L.append(f"| 순서 규칙 | 0.730 | {o['min3']['value']:.3f} | {o['min2']['value']:.3f} |")
        L.append(f"| T7-a (처음 보는 시나리오) | 0.721 | {t['min3']['value']:.3f} | {t['min2']['value']:.3f} |")
        for c in "ABC":
            L.append(f"| {TAG} {c} | {vals[c]:.3f} | {V[c]['min3']['value']:.3f} | {V[c]['min2']['value']:.3f} |")
    if levels:
        L += ["", "## 도구별 점수대와 판정 기준, 학습 데이터 재채점 (그림 13)", "",
              "기준은 같은 학습 기록의 위반과 정상 사이에 그은 값이다(`argus_hook/replay_assets/argus_v_p_scores.json`). 새 상황의 성능이 아니다.", "",
              "| 도구 칸 | 위반 | 정상 | 판정 기준 | 기준을 넘은 위반 | 기준을 넘은 정상 |", "|---|---|---|---|---|---|"]
        for cell, nv, nn, t in levels:
            tool, src = cell.split("|")
            if t:
                L.append(f"| {tool} · {SOURCE_KO.get(src, src)} | {nv} | {nn:,} | {t['threshold']:.3f} | {t['caught']}/{t['violations']} | {t['false_alarms']}/{t['normals']} |")
            else:
                L.append(f"| {tool} · {SOURCE_KO.get(src, src)} | {nv} | {nn:,} | — | — | — |")
    (out / "tables.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("saved", (out / "tables.md").relative_to(REPO_ROOT))


if __name__ == "__main__":
    main(sys.argv[1:])

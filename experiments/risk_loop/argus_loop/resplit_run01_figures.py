"""Figures of the first training run on the new split (resplit-1117 / run01). Reads results.json; trains nothing.

01  every model at the epoch picked on validation: main metric, wider metric, within-period all calls (validation and test)
02  Argus-V-em per-epoch curves: one column per model size, one line per violation weight
03  Argus-V-em loss line charts: epoch points, selected-checkpoint diamonds, validation-loss minima, fixed epoch 67

Usage: PYTHONUTF8=1 py -3.11 experiments/risk_loop/argus_loop/resplit_run01_figures.py
Output: reports/risk-loop/resplit-1117/run01/figures/*.png
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from experiments.risk_loop.argus_loop import argus_v_p_plots as PP  # noqa: E402
from experiments.risk_loop.argus_loop import resplit_run01 as R  # noqa: E402

OUT = R.REPORT / "figures"
VAL, TEST = "#2a78d6", "#eb6834"                       # validation (blue), test (orange): the palette of the earlier figures
RAMP = {"w15": "#86b6ef", "w60": "#3987e5", "w300": "#184f95"}   # ordinal, light to dark = small to large weight (validated)
ARCH_KO = {"EM32": "32차원", "EM64": "64차원", "EM128": "128차원", "LINEAR": "선형 대조"}
W_SHORT = {"w15": "약 15배", "w60": "약 60배", "w300": "300배"}


def nan(v):
    return np.nan if v is None else float(v)


def fig01(res):
    plt = PP.plt
    rows = []
    for cfg, r in res["em"].items():
        rows.append((f"em {ARCH_KO[r['arch']]} · {W_SHORT[r['weight']]}", r["pick"]["validation"]["mean"], r["pick"]["test"]["mean"], f"{r['pick']['epoch']} epoch"))
    for sid, r in res["p"].items():
        rows.append((f"Argus-V-p {sid}", r["validation"], r["test"], ""))
    panels = (("st_vis3", "주 지표\n같은 도구끼리 · 근거 보인 위반 3개 이상"), ("st_vis2", "넓힌 지표\n같은 도구끼리 · 2개 이상"),
              ("in_period_all", "같은 시기 안에서\n모든 호출, 정상 대 위반"))
    n = len(rows)
    fig, axes = plt.subplots(1, 3, figsize=(11.6, 0.36 * n + 2.6), sharey=True)
    fig.subplots_adjust(top=1 - 1.45 / (0.36 * n + 2.6), left=0.21, right=0.955, bottom=1.05 / (0.36 * n + 2.6), wspace=0.20)
    for ax, (key, name) in zip(axes, panels):
        for i, (_, v, t, _) in enumerate(rows):
            yy = n - 1 - i
            a, b = nan(v.get(key)), nan(t.get(key))
            if not (np.isnan(a) or np.isnan(b)):
                ax.plot([a, b], [yy, yy], color=PP.BASE, lw=1.4, zorder=2)
            if not np.isnan(a):
                ax.plot(a, yy, "o", markersize=7.5, markerfacecolor=PP.SURFACE, markeredgecolor=VAL, markeredgewidth=1.6, zorder=3)
            if not np.isnan(b):
                ax.plot(b, yy, "o", markersize=8.5, color=TEST, markeredgecolor=PP.SURFACE, markeredgewidth=1.4, zorder=4)
                ax.text(1.035, yy, f"{b:.2f}", va="center", ha="left", fontsize=8.8, color=PP.INK2, clip_on=False)
        ax.axvline(0.9, color=PP.MUTED, lw=1.0, ls=(0, (4, 3)), zorder=1)
        ax.axvline(0.5, color=PP.MUTED, lw=1.0, ls=(0, (4, 3)), zorder=1)
        ax.set_xlim(0.2, 1.02)
        ax.set_ylim(-0.7, n - 0.3)
        ax.set_xticks([0.2, 0.4, 0.6, 0.8, 1.0])
        ax.set_title(name, fontsize=10.2, color=PP.INK, pad=8, loc="left")
        ax.grid(axis="y", visible=False)
    axes[0].set_yticks(range(n))
    axes[0].set_yticklabels([r[0] + (f"  ({r[3]})" if r[3] else "") for r in rows][::-1], fontsize=9.2)
    for k in range(len(res["em"]), 0, -3):                          # a faint separator between model families
        for ax in axes:
            ax.axhline(n - k - 0.5, color=PP.GRID, lw=0.8, zorder=0)
    fig.legend(handles=[PP.Line2D([0], [0], marker="o", ls="", markersize=7.5, markerfacecolor=PP.SURFACE, markeredgecolor=VAL, markeredgewidth=1.6, label="validation"),
                        PP.Line2D([0], [0], marker="o", ls="", markersize=8.5, color=TEST, label="test (오른쪽 숫자)")],
               loc="lower center", bbox_to_anchor=(0.59, 0.012), ncol=2, columnspacing=2.0, fontsize=9.6)
    d = res["data"]
    PP.title(fig, "새 분할: validation으로 고른 epoch에서의 validation·test 점수",
             f"모든 모델을 새 train으로 학습. test의 주 지표는 위반 {d['test']['st_vis3']['violations']}개({d['test']['st_vis3']['pairs']}쌍), "
             f"넓힌 지표는 {d['test']['st_vis2']['violations']}개({d['test']['st_vis2']['pairs']}쌍)")
    PP.note(fig, "Argus-V-em은 반복 3번 평균, 괄호 = validation 넓힌 지표로 고른 epoch · 점선 = 0.5(우연)와 0.90(목표)")
    PP.save(fig, OUT, "01_모델별_validation_test.png")


def _curves(res, rows_spec, fname, head, sub, note, ylim=None, log=False, vline=True, mark_selected_epoch=False):
    plt = PP.plt
    archs = [a for a in R.ARCHS if any(c.startswith(a + "_") for c in res["em"])]
    fig, axes = plt.subplots(len(rows_spec), len(archs), figsize=(11.6, 2.55 * len(rows_spec) + 2.2), sharex=True, sharey="row", squeeze=False)
    h = 2.55 * len(rows_spec) + 2.2
    bottom = (2.15 if mark_selected_epoch else 1.25) / h
    fig.subplots_adjust(top=1 - 1.5 / h, left=0.075, right=0.955, bottom=bottom, wspace=0.10, hspace=0.30)
    ep = np.arange(1, res["epochs"] + 1)
    for ri, (split, key, label) in enumerate(rows_spec):
        for ci, arch in enumerate(archs):
            ax = axes[ri][ci]
            ends = []
            for wi, wtag in enumerate(R.WEIGHT_RULES):
                r = res["em"].get(f"{arch}_{wtag}")
                if r is None:
                    continue
                src = r["loss"][key] if split == "loss" else r["curves_mean"][split][key]
                v = np.asarray([nan(x) for x in src])
                ax.plot(ep, v, color=RAMP[wtag], lw=2.0, zorder=3, solid_capstyle="round",
                        marker="o" if mark_selected_epoch else None,
                        markevery=10 if mark_selected_epoch else None,
                        markersize=2.7 if mark_selected_epoch else None)
                if mark_selected_epoch:
                    picked = int(r["pick"]["epoch"])
                    if split == "validation":
                        finite = np.flatnonzero(np.isfinite(v))
                        if len(finite):
                            min_i = finite[int(np.argmin(v[finite]))]
                            ax.plot(ep[min_i], v[min_i], marker="*", markersize=9,
                                    color="#d49a18", markeredgecolor=PP.SURFACE,
                                    markeredgewidth=0.8, zorder=7)
                    ax.axvline(picked, color=RAMP[wtag], lw=0.8, alpha=0.50,
                               ls=(0, (1, 2)), zorder=1)
                    ax.plot(picked, v[picked - 1], marker="D", markersize=5.6,
                            color=RAMP[wtag], markeredgecolor=PP.SURFACE,
                            markeredgewidth=0.9, zorder=8)
                    if split == "validation":
                        dx = -4 if picked >= res["epochs"] - 8 else 4
                        dy = (8, -12, 17)[wi]
                        ax.annotate(f"{picked}e", (picked, v[picked - 1]),
                                    xytext=(dx, dy), textcoords="offset points",
                                    ha="right" if dx < 0 else "left", va="center",
                                    fontsize=7.4, color=PP.INK2,
                                    bbox={"facecolor": PP.SURFACE, "edgecolor": "none", "alpha": 0.88, "pad": 0.5},
                                    zorder=9)
                ends.append(float(v[-1]))
            if log:
                ax.set_yscale("log")
                lo, hi = ax.get_ylim()                           # plain tick labels: the font has no minus glyph for 10^-n
                ticks = [t for t in (0.0003, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1, 3, 10) if lo <= t <= hi]
                ax.set_yticks(ticks)
                ax.set_yticklabels([f"{t:g}" for t in ticks])
                ax.minorticks_off()
            else:
                ax.axhline(0.9, color=PP.MUTED, lw=0.9, ls=(0, (4, 3)), zorder=1)
                ax.axhline(0.5, color=PP.MUTED, lw=0.9, ls=(0, (4, 3)), zorder=1)
                if ylim:
                    ax.set_ylim(*ylim)
            if vline:
                ax.axvline(res["fixed_epoch"], color=PP.MUTED, lw=0.9, ls=(0, (2, 2)), zorder=1)
            ax.set_xlim(1, res["epochs"] + (2 if mark_selected_epoch else 0))
            ax.set_xticks([1, 25, 50, 75, 100])
            if ri == 0:
                ax.set_title(ARCH_KO[arch], fontsize=10.6, color=PP.INK, pad=7, loc="left")
            if ri == len(rows_spec) - 1:
                ax.set_xlabel("epoch")
            if ci == 0:
                ax.set_ylabel(label, fontsize=9.4)
    fig.legend(handles=[PP.Line2D([0], [0], color=RAMP[w], lw=2.4,
                                 marker="o" if mark_selected_epoch else None, markersize=3.0,
                                 label="위반 가중치 " + W_SHORT[w]) for w in R.WEIGHT_RULES],
               loc="lower center", bbox_to_anchor=(0.5, 0.13 if mark_selected_epoch else 0.42 / h),
               ncol=3, columnspacing=2.0, handlelength=2.0, fontsize=9.4)
    if mark_selected_epoch:
        fig.legend(handles=[
            PP.Line2D([0], [0], color=PP.INK2, marker="D", ls="None", markersize=5.5,
                      markerfacecolor=PP.INK2, label="고른 epoch: validation · AUROC(같은 도구끼리) 최고"),
            PP.Line2D([0], [0], color="#d49a18", marker="*", ls="None", markersize=9,
                      label="validation loss 최솟값"),
            PP.Line2D([0], [0], color=PP.MUTED, lw=1.0, ls=(0, (2, 2)),
                      label=f"고정 레시피 {res['fixed_epoch']} epoch"),
        ], loc="lower center", bbox_to_anchor=(0.5, 0.07), ncol=3,
           columnspacing=1.7, handletextpad=0.5, fontsize=8.8)
    PP.title(fig, head, sub)
    PP.note(fig, note)
    PP.save(fig, OUT, fname)


def main():
    res = json.loads((R.REPORT / "results.json").read_text(encoding="utf-8"))
    PP.setup()
    OUT.mkdir(parents=True, exist_ok=True)
    fig01(res)
    _curves(res, (("validation", "st_vis2", "validation\n넓힌 지표"), ("test", "st_vis2", "test\n넓힌 지표"),
                  ("test", "st_vis3", "test\n주 지표"), ("test", "in_period_all", "test\n같은 시기 안 모든 호출")),
            "02_epoch별_점수.png", "Argus-V-em: epoch에 따른 validation·test 점수 (새 분할)",
            f"모델 크기별(열), 위반 가중치별(선). 반복 3번 평균. 세로 점선 = {res['fixed_epoch']} epoch",
            "넓힌 지표 = 같은 도구끼리, 근거가 보인 위반 2개 이상인 도구 · 주 지표 = 3개 이상 · 가로 점선 = 0.5(우연)와 0.90(목표)", ylim=(0.2, 1.02))
    _curves(res, (("loss", "train_eval", "학습에 쓴 행의 손실\n(가중치 포함)"), ("validation", "logloss", "validation 손실\n(가중치 없음)"),
                  ("test", "logloss", "test 손실\n(가중치 없음)")),
            "03_epoch별_손실.png", "Argus-V-em: epoch별 손실 꺾은선과 선택 checkpoint (새 분할)",
            "모델 크기별(열), 위반 가중치별(색 선). 3회 반복 평균 · validation에서 선택한 epoch를 각 선에 표시",
            "◆ = validation에서 같은 도구끼리 비교한 AUROC(근거가 보인 위반 2개 이상인 도구)가 가장 높은 epoch · ★ = validation 손실이 가장 낮은 epoch · 회색 점선 = 고정 67 epoch",
            log=True, mark_selected_epoch=True)


if __name__ == "__main__":
    main()

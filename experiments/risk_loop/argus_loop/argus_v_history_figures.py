"""Presentation figures: the performance measures of every model of reports/risk-loop/model_history.md (matplotlib).
Reads saved scores and the records; trains nothing.

Every figure says where its numbers were measured and which measure they are (user instruction 2026-11-17):
  k-fold 교차검증 (old train only, 5-fold) / train 재채점 / 새 validation / 기존 test / 새 test   and   AUROC / 재현율 / 정밀도 / F1 / counts.
Colours keep one meaning in every figure: violet = k-fold cross-validation, aqua = training rows re-scored,
blue = new validation, orange = test, red = violation, grey = normal call. Violet and blue never share a figure
(the pair fails the colour-blind check); the other triples pass the validator of the charting guide.

 01 02  all 19 models of the new split, AUROC three ways (all violations / visible violations), validation and test
 03     all 19 models judged at the cut-off where 5% of the validation normal calls alarm: recall, precision, F1 (test)
 04     ROC curves of all models on the new test split
 05 06  Argus-V-p settings: old split (k-fold, training rows, old test) and new split (training rows, validation, test)
 07     Argus-V-em on the old split: k-fold cross-validation against the old test
 08     Argus-V-em violation weights on the old split (15x ... 1000x)
 09     Argus-V-em model size x violation weight on the new test split (heat map)
 10     Argus-V-em curves per epoch on the new split, with Argus-V-emp
 11     Argus-V-emp: its three parts and the mix
 12     Argus-V-emp: ROC and precision-recall curves, validation and test
 13     Argus-V-emp: score distribution of the test calls and the cut-off
 14     Argus-V-emp: recall, precision and F1 as the cut-off moves
 15     Argus-V-emp: confusion matrices at the cut-off 0.864

Usage: PYTHONUTF8=1 py -3.11 experiments/risk_loop/argus_loop/argus_v_history_figures.py [--only 01,12]
Output: reports/risk-loop/model_history_figures/*.png, numbers.json
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

for _name in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ.setdefault(_name, "2")

import numpy as np  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from experiments.risk_loop import harness as H  # noqa: E402
from experiments.risk_loop.argus_loop import argus_v_emp as AE  # noqa: E402
from experiments.risk_loop.argus_loop import argus_v_p_plots as PP  # noqa: E402
from experiments.risk_loop.argus_loop import resplit_run01 as R  # noqa: E402

REPORTS = ROOT / "reports" / "risk-loop"
OUT = REPORTS / "model_history_figures"
VAL, TEST, TRAIN, KFOLD = "#2a78d6", "#eb6834", "#1baf7a", "#6250d6"
RAMP = {"w15": "#86b6ef", "w60": "#3987e5", "w300": "#184f95"}      # ordinal: light to dark = small to large violation weight
HEAT = ["#86b6ef", "#3987e5", "#184f95", "#0d366b"]                 # sequential, one hue (steps 250-700 of the reference ramp)
ARCH_KO = {"EM32": "32차원", "EM64": "64차원", "EM128": "128차원", "LINEAR": "선형 대조"}
W_KO = {"w15": "약 15배", "w60": "약 60배", "w300": "300배"}
P_KO = {"P1": "P1 기준", "P2": "P2 같은 도구 안 학습", "P3": "P3 규제 완화", "P4": "P4 = P2 + P3", "P5": "P5 = P1 + 랜덤 포레스트",
        "P6": "P6 = P2 + P3 + 랜덤 포레스트"}
EMP = "Argus-V-emp"
DASH = (0, (4, 3))

# ---- numbers of the old split, copied from the records (checked against the documents in check_records)
P_OLD = {"P1": (0.714, 0.682, 0.815), "P2": (0.657, 0.632, 0.826), "P3": (0.468, 0.566, 0.847),       # k-fold / other runs of seen scenarios / training rows
         "P4": (0.565, 0.635, 0.964), "P5": (0.701, 0.687, 0.869), "P6": (0.571, 0.627, 0.979)}
P5_OLD_TEST = 0.644                                                                                   # same tool, 9 violations
EM_OLD = (("Argus-V-em 32차원 (60 epoch)", 0.960, 0.667), ("Argus-V-em 64차원 (67 epoch)", 0.968, 0.667),
          ("Argus-V-em 128차원 (300 epoch)", 0.962, 0.733), ("Argus-V-p P5", 0.756, 0.600))            # k-fold, old test (same tool, visible violations)
W_OLD = {"labels": ["약 15배", "약 60배", "약 230배", "300배", "1000배"],
         "kfold_tool": [0.968, 0.936, 0.825, 0.776, 0.709], "test_tool": [0.667, 0.667, 0.533, 0.600, 0.667],
         "kfold_mixed": [0.719, 0.703, 0.816, 0.847, 0.893], "test_mixed": [0.642, 0.566, 0.707, 0.717, 0.778],
         "october_share": [0.23, 0.19, 0.63, 0.70, 0.87], "rule_kfold": 0.822, "rule_test": 0.773, "october_normal_share": 0.12}


def check_records():
    """Every hard-coded number must appear in the record it was copied from."""
    docs = {"p": (REPORTS / "argus-v-p" / "results.md").read_text(encoding="utf-8"),
            "em": (REPORTS / "argus-v-em300" / "results.md").read_text(encoding="utf-8"),
            "w": (REPORTS / "argus-v-em300" / "class-weight-check.md").read_text(encoding="utf-8")}
    need = {"p": [f"{v:.3f}" for t in P_OLD.values() for v in t] + [f"{P5_OLD_TEST:.3f}"],
            "em": [f"{v:.3f}" for _, a, b in EM_OLD for v in (a, b)],
            "w": [f"{v:.3f}" for k in ("kfold_tool", "test_tool", "kfold_mixed", "test_mixed") for v in W_OLD[k]]
                 + [f"{v:.0%}" for v in W_OLD["october_share"]] + [f"{W_OLD['rule_kfold']:.3f}", f"{W_OLD['rule_test']:.3f}"]}
    missing = [(d, v) for d, vs in need.items() for v in vs if v not in docs[d]]
    assert not missing, missing


def auc(s, y):
    return float(H.auroc(np.asarray(s, dtype=np.float64), np.asarray(y)))


def cnt(v):
    return f"{v:.0f}" if abs(v - round(v)) < 1e-9 else f"{v:.1f}"


def model_rows():
    out = [(EMP, EMP)]
    out += [(f"Argus-V-p {s}", f"Argus-V-p · {P_KO[s]}") for s in P_KO]
    out += [(f"Argus-V-em {a} {w}", f"Argus-V-em · {ARCH_KO[a]} · {W_KO[w]}") for a in R.ARCHS for w in R.WEIGHT_RULES]
    return out


def h_val(label="새 validation"):
    return PP.Line2D([0], [0], marker="o", ls="", markersize=7.5, markerfacecolor=PP.SURFACE, markeredgecolor=VAL, markeredgewidth=1.6, label=label)


def h_test(label="새 test"):
    return PP.Line2D([0], [0], marker="o", ls="", markersize=8.5, color=TEST, markeredgecolor=PP.SURFACE, markeredgewidth=1.4, label=label)


def h_train(label="새 train 재채점"):
    return PP.Line2D([0], [0], marker="^", ls="", markersize=8.5, color=TRAIN, markeredgecolor=PP.SURFACE, markeredgewidth=1.2, label=label)


def group_lines(axes, n):
    for ax in axes:
        ax.axhline(n - 1.5, color=PP.AXIS, lw=0.9, zorder=0)       # under Argus-V-emp
        ax.axhline(n - 7.5, color=PP.GRID, lw=0.9, zorder=0)       # under the six Argus-V-p settings
        ax.axhspan(n - 1.5, n - 0.5, color=PP.GRID, alpha=0.45, zorder=0, lw=0)


def bold_first(ax, n):
    ax.get_yticklabels()[n - 1].set_fontweight("bold")
    ax.get_yticklabels()[n - 1].set_color(PP.INK)


# ------------------------------------------------------------------------------------------------ 01, 02
def fig_all(ov, which, fname):
    plt = PP.plt
    M, S, rule = ov["models"], ov["splits"], ov["period_only_rule"]
    rs = model_rows()
    n = len(rs)
    key_n = "violations" if which == "all" else "visible_violations"
    nv, nt = S["validation"][key_n], S["test"][key_n]
    tvv, tvt = M[EMP][f"validation_{which}_tool_violations"], M[EMP][f"test_{which}_tool_violations"]
    what = "위반" if which == "all" else "근거가 보인 위반"
    panels = (("mixed", f"AUROC · 도구·시기 구분 없이 전부 비교\nvalidation {what} {nv}개 · test {nt}개"),
              ("period", f"AUROC · 같은 시기의 호출끼리 비교\nvalidation {nv}개 · test {nt}개"),
              ("tool", f"AUROC · 같은 도구의 호출끼리 비교\nvalidation {tvv}개 · test {tvt}개"))
    h = 0.36 * n + 3.1
    fig, axes = plt.subplots(1, 3, figsize=(12.8, h), sharey=True)
    fig.subplots_adjust(top=1 - 1.6 / h, left=0.245, right=0.955, bottom=1.15 / h, wspace=0.24)
    for ax, (key, name) in zip(axes, panels):
        for i, (k, _) in enumerate(rs):
            yy = n - 1 - i
            a, b = M[k][f"validation_{which}"][key], M[k][f"test_{which}"][key]
            ax.plot([a, b], [yy, yy], color=PP.BASE, lw=1.4, zorder=2)
            ax.plot(a, yy, "o", markersize=7.5, markerfacecolor=PP.SURFACE, markeredgecolor=VAL, markeredgewidth=1.6, zorder=3)
            ax.plot(b, yy, "o", markersize=8.5, color=TEST, markeredgecolor=PP.SURFACE, markeredgewidth=1.4, zorder=4)
            ax.text(1.055, yy, f"{b:.3f}", va="center", ha="left", fontsize=8.8, color=PP.INK if k == EMP else PP.INK2,
                    fontweight="bold" if k == EMP else "normal", clip_on=False)
        for x in (0.5, 0.9):
            ax.axvline(x, color=PP.MUTED, lw=1.0, ls=DASH, zorder=1)
        if key == "mixed":
            rt = rule[f"test_{which}"]["mixed"]
            ax.plot([rt, rt], [-0.7, n - 1.5], color=TEST, lw=1.1, ls=(0, (1, 2)), zorder=1)
            ax.text(rt - 0.012, -0.55, f"시기만 아는 규칙 (test) {rt:.3f}", ha="right", va="bottom", fontsize=8.2, color=PP.INK2)
        ax.set_xlim(0.3, 1.03)
        ax.set_ylim(-0.7, n - 0.3)
        ax.set_xticks([0.4, 0.6, 0.8, 1.0])
        ax.set_title(name, fontsize=10.0, color=PP.INK, pad=8, loc="left")
        ax.grid(axis="y", visible=False)
    axes[0].set_yticks(range(n))
    axes[0].set_yticklabels([lab for _, lab in rs][::-1], fontsize=9.2)
    bold_first(axes[0], n)
    group_lines(axes, n)
    fig.legend(handles=[h_val("새 validation · AUROC"), h_test("새 test · AUROC (오른쪽 숫자)")], loc="lower center", bbox_to_anchor=(0.6, 0.012),
               ncol=2, columnspacing=2.2, fontsize=9.6)
    PP.title(fig, f"새 분할의 모든 모델: AUROC — {what} 대 정상 호출",
             "모든 모델을 새 train으로 학습했다. 세 칸은 같은 점수로 AUROC를 구할 때 무엇끼리 비교했는지의 차이다")
    extra = "" if which == "all" else f" · validation의 근거가 보인 위반 {nv}개는 모두 10월 기록이라 시기만 아는 규칙이 validation에서 {rule['validation_visible']['mixed']:.3f}이다"
    PP.note(fig, "Argus-V-em은 67 epoch, 반복 3번의 평균 · 점선 = 0.5(우연)와 0.90 · 시기만 아는 규칙 = “10월 기록이면 높게”" + extra)
    PP.save(fig, OUT, fname)


# ------------------------------------------------------------------------------------------------ 03
def fig_cut(ov, fname):
    plt = PP.plt
    M, S = ov["models"], ov["splits"]
    rs = model_rows()
    n = len(rs)
    V = S["test"]["violations"]
    panels = (("recall", f"재현율\n위반 {V}개 중 잡은 비율 (괄호는 잡은 개수)", 0.66), ("precision", "정밀도\n경보 중 진짜 위반의 비율", 0.105),
              ("f1", "F1\n재현율과 정밀도의 조화 평균", 0.175))
    h = 0.36 * n + 3.0
    fig, axes = plt.subplots(1, 3, figsize=(12.8, h), sharey=True)
    fig.subplots_adjust(top=1 - 1.6 / h, left=0.245, right=0.965, bottom=0.85 / h, wspace=0.16)
    for ax, (key, name, xmax) in zip(axes, panels):
        for i, (k, _) in enumerate(rs):
            yy = n - 1 - i
            c = M[k]["test_caught_at_validation_5pct"]
            v = c[key]
            ax.barh(yy, v, height=0.56, color=TEST, zorder=3, lw=0)
            txt = f"{v:.3f}" + (f"  ({cnt(c['all'])})" if key == "recall" else "")
            ax.text(v + xmax * 0.018, yy, txt, va="center", ha="left", fontsize=8.8, color=PP.INK if k == EMP else PP.INK2,
                    fontweight="bold" if k == EMP else "normal")
        ax.set_xlim(0, xmax)
        ax.set_ylim(-0.7, n - 0.3)
        ax.set_title(name, fontsize=10.0, color=PP.INK, pad=8, loc="left")
        ax.grid(axis="y", visible=False)
    axes[0].set_yticks(range(n))
    axes[0].set_yticklabels([lab for _, lab in rs][::-1], fontsize=9.2)
    bold_first(axes[0], n)
    group_lines(axes, n)
    PP.title(fig, "새 test: 커트라인을 정해 위반 / 정상으로 판정했을 때 — 재현율 · 정밀도 · F1",
             "AUROC가 아니라 판정 결과다. 커트라인 = 모델마다 validation 정상 호출의 5%가 경보가 되는 점수 (test를 보지 않고 정함)")
    PP.note(fig, f"새 test: 정상 호출 {S['test']['normal_calls']:,}개, 위반 {V}개 · Argus-V-em은 67 epoch, 반복 3번의 평균 · 전부 “정상”이라고 판정하면 세 값 모두 0이다")
    PP.save(fig, OUT, fname)


# ------------------------------------------------------------------------------------------------ 04
def fig_roc(ov, D, fname):
    plt = PP.plt
    te = D["idx"]["test"]
    y = D["y"][te]
    C = AE.components()
    emp = AE.scores("test")
    fe, tpe = PP.roc_points(emp, y)
    S = ov["splits"]["test"]
    panels = [("Argus-V-p · 설정 6개", [(C[s]["test"], PP.INK2 if s in AE.P_SETTINGS else PP.BASE, 1.5) for s in P_KO])]
    for a in R.ARCHS:
        panels.append((f"Argus-V-em · {ARCH_KO[a]} · 가중치 3가지 × 반복 3번",
                       [(C[(f"{a}_{w}", k)]["test"][AE.EPOCH - 1], RAMP[w], 1.3) for w in R.WEIGHT_RULES for k in R.REPEATS]))
    panels.append((EMP, []))
    h = 8.9
    fig, axes = plt.subplots(2, 3, figsize=(12.6, h), sharex=True, sharey=True)
    fig.subplots_adjust(top=1 - 1.25 / h, left=0.07, right=0.975, bottom=1.25 / h, wspace=0.10, hspace=0.24)
    for ax, (name, curves) in zip(axes.ravel(), panels):
        ax.plot([0, 1], [0, 1], color=PP.MUTED, lw=1.0, ls=DASH, zorder=1)
        vals = []
        for s, col, lw in curves:
            f, t = PP.roc_points(s, y)
            ax.plot(f, t, color=col, lw=lw, zorder=3, alpha=0.95)
            vals.append(auc(s, y))
        ax.plot(fe, tpe, color=PP.INK, lw=2.6, zorder=5)
        ax.set_xlim(-0.01, 1.0)
        ax.set_ylim(0, 1.01)
        ax.set_aspect("equal")
        ax.set_xticks([0, 0.25, 0.5, 0.75, 1.0])
        ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
        ax.set_title(name, fontsize=10.2, color=PP.INK, pad=7, loc="left")
        txt = (f"이 칸의 AUROC {min(vals):.3f} ~ {max(vals):.3f}\n" if vals else "") + f"Argus-V-emp AUROC {auc(emp, y):.3f}"
        ax.text(0.97, 0.05, txt, transform=ax.transAxes, ha="right", va="bottom", fontsize=9.2, color=PP.INK2, bbox=PP.LBL, linespacing=1.5)
    ax = axes[1][2]                                              # the rule that knows only the collection period: one point
    oct_ = D["source"][te].astype(str) == "oct"
    rx, ry = float((oct_ & (y == 0)).sum() / (y == 0).sum()), float((oct_ & (y == 1)).sum() / (y == 1).sum())
    ax.plot([0, rx, 1], [0, ry, 1], color=PP.MUTED, lw=1.2, zorder=2)
    ax.plot(rx, ry, "s", markersize=7, color=PP.MUTED, markeredgecolor=PP.SURFACE, markeredgewidth=1.2, zorder=4)
    ax.text(rx + 0.04, ry - 0.03, f"시기만 아는 규칙\nAUROC {ov['period_only_rule']['test_all']['mixed']:.3f}", ha="left", va="top", fontsize=8.8, color=PP.INK2)
    for ax in axes[1]:
        ax.set_xlabel("오경보율 (정상 호출 중 경보가 된 비율)", fontsize=9.6)
    for ax in axes[:, 0]:
        ax.set_ylabel("재현율 (위반 중 잡은 비율)", fontsize=9.6)
    fig.legend(handles=[PP.Line2D([0], [0], color=PP.INK, lw=2.6, label="Argus-V-emp (모든 칸에 같은 선)"),
                        PP.Line2D([0], [0], color=PP.INK2, lw=1.6, label="Argus-V-p P3 · P5"), PP.Line2D([0], [0], color=PP.BASE, lw=1.6, label="Argus-V-p P1 · P2 · P4 · P6")]
               + [PP.Line2D([0], [0], color=RAMP[w], lw=1.8, label="Argus-V-em 위반 가중치 " + W_KO[w]) for w in R.WEIGHT_RULES],
               loc="lower center", bbox_to_anchor=(0.5, 0.42 / h), ncol=3, columnspacing=2.0, handlelength=2.0, fontsize=9.4)
    PP.title(fig, "새 test: 모든 모델의 ROC 곡선",
             f"위반 {S['violations']}개 대 정상 호출 {S['normal_calls']:,}개를 도구·시기 구분 없이 전부 비교. 곡선 아래 넓이가 AUROC다")
    PP.note(fig, "Argus-V-em은 67 epoch의 모델 36개를 하나씩 그렸다 · 점선 대각선 = 우연(AUROC 0.5) · 시기만 아는 규칙 = “10월 기록이면 높게”")
    PP.save(fig, OUT, fname)


# ------------------------------------------------------------------------------------------------ 05
def fig_p_old(fname):
    plt = PP.plt
    ids = list(P_OLD)
    n = len(ids)
    h = 0.5 * n + 3.1
    fig, ax = plt.subplots(figsize=(11.2, h))
    fig.subplots_adjust(top=1 - 1.3 / h, left=0.245, right=0.66, bottom=1.25 / h)
    for i, sid in enumerate(ids):
        yy = n - 1 - i
        a, b, c = P_OLD[sid]
        ax.plot([min(a, b), c], [yy, yy], color=PP.BASE, lw=1.4, zorder=2)
        ax.plot(b, yy, "D", markersize=7.0, markerfacecolor=PP.SURFACE, markeredgecolor=KFOLD, markeredgewidth=1.6, zorder=3)
        ax.plot(a, yy, "D", markersize=8.0, color=KFOLD, markeredgecolor=PP.SURFACE, markeredgewidth=1.3, zorder=4)
        ax.plot(c, yy, "^", markersize=9.0, color=TRAIN, markeredgecolor=PP.SURFACE, markeredgewidth=1.2, zorder=4)
        for xpos, v in zip((1.07, 1.30, 1.53), (a, b, c)):
            ax.text(xpos, yy, f"{v:.3f}", transform=ax.get_yaxis_transform(), ha="center", va="center", fontsize=9.6, color=PP.INK2)
        ax.text(1.76, yy, f"{P5_OLD_TEST:.3f}" if sid == "P5" else "—", transform=ax.get_yaxis_transform(), ha="center", va="center", fontsize=9.6, color=PP.INK2)
    yy5 = n - 1 - ids.index("P5")
    ax.plot(P5_OLD_TEST, yy5 - 0.30, "o", markersize=8.5, color=TEST, markeredgecolor=PP.SURFACE, markeredgewidth=1.4, zorder=5)
    for xpos, head in zip((1.07, 1.30, 1.53, 1.76), ("k-fold\n교차검증", "같은 시나리오의\n다른 실행", "train\n재채점", "기존 test\n(위반 9개)")):
        ax.text(xpos, n - 0.38, head, transform=ax.get_yaxis_transform(), ha="center", va="bottom", fontsize=9.0, color=PP.INK, linespacing=1.3)
    for x in (0.5, 0.9):
        ax.axvline(x, color=PP.MUTED, lw=1.0, ls=DASH, zorder=1)
    ax.set_xlim(0.4, 1.0)
    ax.set_ylim(-0.75, n - 0.45)
    ax.set_yticks(range(n))
    ax.set_yticklabels(["Argus-V-p · " + P_KO[s] for s in ids][::-1], fontsize=9.6)
    ax.set_xlabel("AUROC (같은 도구의 호출끼리 비교)", fontsize=9.6)
    ax.grid(axis="y", visible=False)
    fig.legend(handles=[PP.Line2D([0], [0], marker="D", ls="", markersize=8, color=KFOLD, markeredgecolor=PP.SURFACE, label="k-fold 교차검증 (기존 train만으로 한 5-fold)"),
                        PP.Line2D([0], [0], marker="D", ls="", markersize=7, markerfacecolor=PP.SURFACE, markeredgecolor=KFOLD, markeredgewidth=1.6, label="기존 train 안에서 같은 시나리오의 다른 실행을 채점"),
                        PP.Line2D([0], [0], marker="^", ls="", markersize=9, color=TRAIN, markeredgecolor=PP.SURFACE, label="train 재채점"),
                        h_test("기존 test (P5만 한 번 채점)")],
               loc="lower center", bbox_to_anchor=(0.5, 0.40 / h), ncol=2, columnspacing=2.0, fontsize=9.4)
    PP.title(fig, "Argus-V-p (기존 분할): AUROC 0.9를 넘는 것은 학습 데이터를 다시 채점할 때뿐이다",
             "AUROC · 같은 도구의 호출끼리 비교 · 위반 48개. 규제를 풀수록(P3·P4·P6) train 재채점만 오르고 k-fold 교차검증 값은 내려간다")
    PP.note(fig, "점선 = 0.5(우연)와 0.90 · 앞의 세 값은 모두 기존 train 안에서 잰 값이고 test 값이 아니다 · 출처: reports/risk-loop/argus-v-p/results.md")
    PP.save(fig, OUT, fname)


# ------------------------------------------------------------------------------------------------ 06
def fig_p_new(ov, fname):
    plt = PP.plt
    M, S = ov["models"], ov["splits"]
    ids = list(P_KO)
    n = len(ids)
    h = 0.5 * n + 3.1
    fig, axes = plt.subplots(1, 2, figsize=(11.6, h), sharey=True)
    fig.subplots_adjust(top=1 - 1.6 / h, left=0.235, right=0.945, bottom=1.05 / h, wspace=0.22)
    panels = (("mixed", f"AUROC · 도구·시기 구분 없이 전부 비교\ntrain 위반 {S['train']['violations']}개 · validation {S['validation']['violations']}개 · test {S['test']['violations']}개"),
              ("period", f"AUROC · 같은 시기의 호출끼리 비교\nvalidation {S['validation']['violations']}개 · test {S['test']['violations']}개"))
    for ax, (key, name) in zip(axes, panels):
        for i, sid in enumerate(ids):
            yy = n - 1 - i
            m = M[f"Argus-V-p {sid}"]
            a, b = m["validation_all"][key], m["test_all"][key]
            xs = [a, b] + ([m["train_all_mixed"]] if key == "mixed" else [])
            ax.plot([min(xs), max(xs)], [yy, yy], color=PP.BASE, lw=1.4, zorder=2)
            if key == "mixed":
                ax.plot(m["train_all_mixed"], yy, "^", markersize=9.0, color=TRAIN, markeredgecolor=PP.SURFACE, markeredgewidth=1.2, zorder=3)
            ax.plot(a, yy, "o", markersize=7.5, markerfacecolor=PP.SURFACE, markeredgecolor=VAL, markeredgewidth=1.6, zorder=4)
            ax.plot(b, yy, "o", markersize=8.5, color=TEST, markeredgecolor=PP.SURFACE, markeredgewidth=1.4, zorder=5)
            ax.text(1.045, yy, f"{b:.3f}", va="center", ha="left", fontsize=9.0, color=PP.INK2, clip_on=False)
        for x in (0.5, 0.9):
            ax.axvline(x, color=PP.MUTED, lw=1.0, ls=DASH, zorder=1)
        ax.set_xlim(0.45, 1.02)
        ax.set_ylim(-0.6, n - 0.4)
        ax.set_title(name, fontsize=10.0, color=PP.INK, pad=8, loc="left")
        ax.grid(axis="y", visible=False)
    axes[0].set_yticks(range(n))
    axes[0].set_yticklabels(["Argus-V-p · " + P_KO[s] for s in ids][::-1], fontsize=9.6)
    fig.legend(handles=[h_train("새 train 재채점 · AUROC"), h_val("새 validation · AUROC"), h_test("새 test · AUROC (오른쪽 숫자)")],
               loc="lower center", bbox_to_anchor=(0.58, 0.012), ncol=3, columnspacing=2.0, fontsize=9.4)
    PP.title(fig, "Argus-V-p (새 분할): 설정 6개의 AUROC — train 재채점 · validation · test",
             "위반 전부 대 정상 호출. P3는 같은 시기끼리 비교가, P5는 전부 비교가 가장 높다. 이 둘이 Argus-V-emp에 들어갔다")
    PP.note(fig, "점선 = 0.5(우연)와 0.90 · train 재채점은 학습에 쓴 데이터를 다시 채점한 값이라 성능이 아니다")
    PP.save(fig, OUT, fname)


# ------------------------------------------------------------------------------------------------ 07
def fig_em_old(fname):
    plt = PP.plt
    n = len(EM_OLD)
    h = 0.62 * n + 2.9
    fig, ax = plt.subplots(figsize=(10.6, h))
    fig.subplots_adjust(top=1 - 1.3 / h, left=0.30, right=0.93, bottom=1.2 / h)
    for i, (name, kf, te) in enumerate(EM_OLD):
        yy = n - 1 - i
        ax.plot([te, kf], [yy, yy], color=PP.BASE, lw=1.6, zorder=2)
        ax.plot(kf, yy, "D", markersize=8.5, color=KFOLD, markeredgecolor=PP.SURFACE, markeredgewidth=1.3, zorder=4)
        ax.plot(te, yy, "o", markersize=9.0, color=TEST, markeredgecolor=PP.SURFACE, markeredgewidth=1.4, zorder=4)
        ax.text(kf + 0.012, yy, f"{kf:.3f}", va="center", ha="left", fontsize=9.6, color=PP.INK2)
        ax.text(te - 0.012, yy, f"{te:.3f}", va="center", ha="right", fontsize=9.6, color=PP.INK2)
    for x in (0.5, 0.9):
        ax.axvline(x, color=PP.MUTED, lw=1.0, ls=DASH, zorder=1)
    ax.set_xlim(0.45, 1.03)
    ax.set_ylim(-0.6, n - 0.4)
    ax.set_yticks(range(n))
    ax.set_yticklabels([r[0] for r in EM_OLD][::-1], fontsize=9.8)
    ax.set_xlabel("AUROC (같은 도구의 호출끼리 비교, 근거가 보인 위반만)", fontsize=9.6)
    ax.grid(axis="y", visible=False)
    fig.legend(handles=[PP.Line2D([0], [0], marker="D", ls="", markersize=8.5, color=KFOLD, markeredgecolor=PP.SURFACE, label="k-fold 교차검증 · AUROC (기존 train만으로 한 5-fold, 위반 16개)"),
                        h_test("기존 test · AUROC (한 번 채점, 위반 3개 · 비교 15쌍)")],
               loc="lower center", bbox_to_anchor=(0.5, 0.40 / h), ncol=1, fontsize=9.4)
    PP.title(fig, "기존 분할: k-fold 교차검증의 AUROC 0.96은 기존 test에서 나오지 않았다",
             "같은 모델, 같은 채점 방법. k-fold 교차검증 값은 test 값이 아니다. 그래서 데이터를 다시 나눴다")
    PP.note(fig, "점선 = 0.5(우연)와 0.90 · 기존 test는 근거가 보인 위반이 3개뿐이었다 · 출처: reports/risk-loop/argus-v-em300/results.md")
    PP.save(fig, OUT, fname)


# ------------------------------------------------------------------------------------------------ 08
def fig_weights_old(fname):
    plt = PP.plt
    W = W_OLD
    x = np.arange(len(W["labels"]))
    h = 5.9
    fig, axes = plt.subplots(1, 3, figsize=(12.8, h))
    fig.subplots_adjust(top=1 - 1.75 / h, left=0.06, right=0.975, bottom=1.35 / h, wspace=0.26)
    specs = ((axes[0], "kfold_tool", "test_tool", "AUROC · 같은 도구의 호출끼리 비교\nk-fold 근거가 보인 16개 · 기존 test 3개(15쌍)", None, None),
             (axes[1], "kfold_mixed", "test_mixed", "AUROC · 도구·시기 구분 없이 전부 비교\nk-fold 위반 76개 · 기존 test 24개", W["rule_kfold"], W["rule_test"]))
    for ax, kk, tk, name, rk, rt in specs:
        ax.plot(x, W[kk], color=KFOLD, lw=2.0, marker="D", markersize=7.5, markeredgecolor=PP.SURFACE, markeredgewidth=1.2, zorder=4)
        ax.plot(x, W[tk], color=TEST, lw=2.0, marker="o", markersize=8.0, markeredgecolor=PP.SURFACE, markeredgewidth=1.3, zorder=4)
        for xi, (a, b) in enumerate(zip(W[kk], W[tk])):
            up, dn = (a, b) if a >= b else (b, a)
            ax.text(xi, up + 0.022, f"{up:.3f}", ha="center", va="bottom", fontsize=8.8, color=PP.INK2)
            ax.text(xi, dn - 0.024, f"{dn:.3f}", ha="center", va="top", fontsize=8.8, color=PP.INK2)
        if rt is not None:
            ax.axhline(rt, color=TEST, lw=1.1, ls=(0, (1, 2)), zorder=1)
            ax.axhline(rk, color=KFOLD, lw=1.1, ls=(0, (1, 2)), zorder=1)
            ax.text(-0.38, rk + 0.008, f"“10월이면 1점” 규칙 {rk:.3f} (k-fold)", ha="left", va="bottom", fontsize=8.2, color=PP.INK2)
            ax.text(-0.38, rt - 0.010, f"같은 규칙 {rt:.3f} (기존 test)", ha="left", va="top", fontsize=8.2, color=PP.INK2)
        ax.set_ylim(0.45, 1.03)
        ax.set_xlim(-0.45, len(x) - 0.55)
        ax.set_xticks(x)
        ax.set_xticklabels(W["labels"], fontsize=9.0)
        ax.set_title(name, fontsize=10.0, color=PP.INK, pad=8, loc="left")
        ax.grid(axis="x", visible=False)
    ax = axes[2]
    ax.bar(x, W["october_share"], width=0.56, color=TEST, zorder=3, lw=0)
    for xi, v in enumerate(W["october_share"]):
        ax.text(xi, v + 0.02, f"{v:.0%}", ha="center", va="bottom", fontsize=9.2, color=PP.INK2)
    ax.axhline(W["october_normal_share"], color=PP.MUTED, lw=1.0, ls=DASH, zorder=4)
    ax.text(len(x) - 0.58, W["october_normal_share"] + 0.012, f"정상 호출 중 10월 기록 {W['october_normal_share']:.0%}", ha="right", va="bottom", fontsize=8.4, color=PP.INK2)
    ax.set_ylim(0, 1.0)
    ax.set_xlim(-0.45, len(x) - 0.55)
    ax.set_xticks(x)
    ax.set_xticklabels(W["labels"], fontsize=9.0)
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
    ax.set_yticklabels(["0%", "25%", "50%", "75%", "100%"])
    ax.set_title("기존 test · 오경보 가운데 10월 기록의 비율\n정상 호출의 5%가 경보가 되는 커트라인", fontsize=10.0, color=PP.INK, pad=8, loc="left")
    ax.grid(axis="x", visible=False)
    fig.legend(handles=[PP.Line2D([0], [0], color=KFOLD, lw=2.0, marker="D", markersize=7.5, markeredgecolor=PP.SURFACE, label="k-fold 교차검증 · AUROC (기존 train만으로 한 5-fold)"),
                        PP.Line2D([0], [0], color=TEST, lw=2.0, marker="o", markersize=8, markeredgecolor=PP.SURFACE, label="기존 test · AUROC / 기존 test · 비율")],
               loc="lower center", bbox_to_anchor=(0.5, 0.42 / h), ncol=2, columnspacing=2.4, fontsize=9.4)
    PP.title(fig, "Argus-V-em 위반 가중치 (기존 분할, 64차원, 67 epoch): 키울수록 10월 기록을 알아본다",
             "가중치를 키우면 같은 도구끼리 비교한 AUROC는 내려가고, 전부 비교한 AUROC는 “10월이면 1점” 규칙의 값에 가까워지며, 오경보가 10월 기록에 몰린다")
    PP.note(fig, "위반 가중치 = 손실에서 위반 1개를 정상 호출 몇 개만큼 무겁게 치는가 · 약 230배와 1000배는 기존 분할에서만 학습했다 · 출처: reports/risk-loop/argus-v-em300/class-weight-check.md")
    PP.save(fig, OUT, fname)


# ------------------------------------------------------------------------------------------------ 09
def fig_heat(ov, fname):
    plt = PP.plt
    from matplotlib.colors import LinearSegmentedColormap
    M, S = ov["models"], ov["splits"]
    st3 = ov["same_tool_three_or_more"]["test"]
    cmap = LinearSegmentedColormap.from_list("seq", HEAT)
    lo, hi = 0.5, 0.95
    panels = ((lambda m: m["test_all"]["mixed"], f"새 test · AUROC\n위반 {S['test']['violations']}개 · 전부 비교", M[EMP]["test_all"]["mixed"]),
              (lambda m: m["test_all"]["period"], f"새 test · AUROC\n위반 {S['test']['violations']}개 · 같은 시기끼리", M[EMP]["test_all"]["period"]),
              (lambda m: m["test_visible_tool3"], f"새 test · AUROC\n같은 도구끼리 (근거가 보인 {st3['violations']}개 · {st3['pairs']}쌍)", M[EMP]["test_visible_tool3"]))
    archs, ws = list(R.ARCHS), list(R.WEIGHT_RULES)
    h = 5.6
    fig, axes = plt.subplots(1, 3, figsize=(12.4, h))
    fig.subplots_adjust(top=1 - 1.7 / h, left=0.09, right=0.985, bottom=1.25 / h, wspace=0.16)
    for pi, (ax, (get, name, empv)) in enumerate(zip(axes, panels)):
        for i, a in enumerate(archs):
            for j, w in enumerate(ws):
                v = get(M[f"Argus-V-em {a} {w}"])
                t = min(1.0, max(0.0, (v - lo) / (hi - lo)))
                ax.add_patch(plt.Rectangle((j, len(archs) - 1 - i), 1, 1, facecolor=cmap(t), edgecolor=PP.SURFACE, linewidth=2.5))
                ax.text(j + 0.5, len(archs) - 1 - i + 0.5, f"{v:.3f}", ha="center", va="center", fontsize=11.5, color="#ffffff", fontweight="bold")
        ax.set_xlim(0, len(ws))
        ax.set_ylim(0, len(archs))
        ax.set_xticks([j + 0.5 for j in range(len(ws))])
        ax.set_xticklabels([W_KO[w] for w in ws], fontsize=9.6)
        ax.set_yticks([len(archs) - 1 - i + 0.5 for i in range(len(archs))])
        ax.set_yticklabels([ARCH_KO[a] for a in archs] if pi == 0 else [""] * len(archs), fontsize=9.8)
        ax.set_xlabel("위반 가중치", fontsize=9.4)
        ax.grid(visible=False)
        for sp in ax.spines.values():
            sp.set_visible(False)
        ax.set_title(name, fontsize=10.0, color=PP.INK, pad=8, loc="left")
        ax.text(0.0, -0.30, f"같은 채점의 Argus-V-emp: {empv:.3f}", transform=ax.transAxes, ha="left", va="top", fontsize=9.4, color=PP.INK2)
    PP.title(fig, "Argus-V-em (새 분할): 모델 크기 × 위반 가중치별 AUROC",
             "새 test, 67 epoch, 반복 3번의 평균. 색이 진할수록 높다(세 칸 같은 눈금, 0.5 ~ 0.95)")
    PP.note(fig, "300배는 전부 비교와 같은 시기끼리 비교가 높지만, 같은 도구끼리 비교는 가장 낮다 · 12개 설정 모두 Argus-V-emp에 들어갔다")
    PP.save(fig, OUT, fname)


# ------------------------------------------------------------------------------------------------ 10
def fig_epochs(D, fname):
    plt = PP.plt
    res = json.loads((R.REPORT / "results.json").read_text(encoding="utf-8"))
    ep = np.arange(1, res["epochs"] + 1)
    yv = {s: D["y"][D["idx"][s]] for s in ("validation", "test")}
    emp = {s: np.array([auc(AE.scores(s, int(e)), yv[s]) for e in ep]) for s in ("validation", "test")}
    rows_spec = (("fit", "pooled_vis", "새 train 재채점 · AUROC\n학습에 쓴 행"), ("validation", "pooled_all", "새 validation · AUROC\n위반 26개 전부 비교"),
                 ("test", "pooled_all", "새 test · AUROC\n위반 26개 전부 비교"))
    archs = list(R.ARCHS)
    h = 2.45 * len(rows_spec) + 2.3
    fig, axes = plt.subplots(len(rows_spec), len(archs), figsize=(12.4, h), sharex=True, sharey=True, squeeze=False)
    fig.subplots_adjust(top=1 - 1.45 / h, left=0.085, right=0.975, bottom=1.3 / h, wspace=0.08, hspace=0.20)
    for ri, (split, key, label) in enumerate(rows_spec):
        for ci, a in enumerate(archs):
            ax = axes[ri][ci]
            for w in R.WEIGHT_RULES:
                v = np.asarray([np.nan if x is None else float(x) for x in res["em"][f"{a}_{w}"]["curves_mean"][split][key]])
                ax.plot(ep, v, color=RAMP[w], lw=2.0, zorder=3)
            if split in emp:
                ax.plot(ep, emp[split], color=PP.INK, lw=2.2, zorder=4)
            for yy in (0.5, 0.9):
                ax.axhline(yy, color=PP.MUTED, lw=0.9, ls=DASH, zorder=1)
            ax.axvline(res["fixed_epoch"], color=PP.MUTED, lw=0.9, ls=(0, (2, 2)), zorder=1)
            ax.set_xlim(1, res["epochs"])
            ax.set_ylim(0.4, 1.02)
            ax.set_xticks([1, 25, 50, 75, 100])
            if ri == 0:
                ax.set_title("Argus-V-em · " + ARCH_KO[a], fontsize=10.4, color=PP.INK, pad=7, loc="left")
            if ri == len(rows_spec) - 1:
                ax.set_xlabel("epoch", fontsize=9.6)
            if ci == 0:
                ax.set_ylabel(label, fontsize=9.2)
    fig.legend(handles=[PP.Line2D([0], [0], color=RAMP[w], lw=2.4, label="Argus-V-em 위반 가중치 " + W_KO[w]) for w in R.WEIGHT_RULES]
               + [PP.Line2D([0], [0], color=PP.INK, lw=2.4, label="Argus-V-emp (구성 모델을 그 epoch 것으로 바꿨을 때)")],
               loc="lower center", bbox_to_anchor=(0.5, 0.44 / h), ncol=4, columnspacing=1.8, handlelength=2.0, fontsize=9.4)
    PP.title(fig, "Argus-V-em (새 분할): epoch에 따른 AUROC — 학습 데이터는 외우지만 validation·test는 그만큼 오르지 않는다",
             f"모델 크기별(열), 위반 가중치별(선), 반복 3번의 평균. 세로 점선 = 비교에 쓴 {res['fixed_epoch']} epoch")
    PP.note(fig, "학습에 쓴 행 = 근거가 보인 위반 26개 + 정상 호출 5,334개 · 가로 점선 = 0.5(우연)와 0.90 · 1 epoch = 가중치를 한 번 고침")
    PP.save(fig, OUT, fname)
    return {"emp_test_auroc_by_epoch_min": float(emp["test"].min()), "emp_test_auroc_by_epoch_max": float(emp["test"].max()),
            "emp_test_auroc_at_fixed_epoch": float(emp["test"][res["fixed_epoch"] - 1])}


# ------------------------------------------------------------------------------------------------ 11
def fig_parts(ov, fname):
    plt = PP.plt
    M, S = ov["models"], ov["splits"]
    V, B = S["test"]["violations"], S["test"]["visible_violations"]
    rs = (("Argus-V-em 64차원·약 60배 하나 (비교용)", M["Argus-V-em EM64 w60"]), ("① Argus-V-em 12개 설정 평균", ov["argus_v_em_part_of_the_mix"]),
          ("② Argus-V-p P3", M["Argus-V-p P3"]), ("③ Argus-V-p P5", M["Argus-V-p P5"]), ("Argus-V-emp = ①②③의 평균", M[EMP]))
    panels = ((lambda m: m["test_all"]["mixed"], f"AUROC\n위반 {V}개 · 전부 비교", (0.5, 1.0)), (lambda m: m["test_all"]["period"], f"AUROC\n위반 {V}개 · 같은 시기끼리", (0.5, 1.0)),
              (lambda m: m["test_visible"]["mixed"], f"AUROC\n근거가 보인 {B}개 · 전부 비교", (0.5, 1.0)),
              (lambda m: m["test_caught_at_validation_5pct"]["f1"], "F1\n5% 커트라인으로 판정", (0.0, 0.16)))
    n = len(rs)
    h = 0.62 * n + 2.9
    fig, axes = plt.subplots(1, 4, figsize=(12.8, h), sharey=True)
    fig.subplots_adjust(top=1 - 1.6 / h, left=0.262, right=0.965, bottom=0.75 / h, wspace=0.20)
    for ax, (get, name, (lo, hi)) in zip(axes, panels):
        for i, (_, m) in enumerate(rs):
            yy = n - 1 - i
            v = get(m)
            last = i == n - 1
            ax.barh(yy, v - lo, left=lo, height=0.56, color=TEST, alpha=1.0 if last else 0.45, zorder=3, lw=0)
            ax.text(v + (hi - lo) * 0.025, yy, f"{v:.3f}", va="center", ha="left", fontsize=9.6, color=PP.INK if last else PP.INK2, fontweight="bold" if last else "normal")
        ax.set_xlim(lo, hi + (hi - lo) * 0.22)
        ax.set_ylim(-0.6, n - 0.4)
        ax.set_xticks(np.linspace(lo, hi, 3))
        ax.set_title(name, fontsize=10.0, color=PP.INK, pad=8, loc="left")
        ax.grid(axis="y", visible=False)
    axes[0].set_yticks(range(n))
    axes[0].set_yticklabels([r[0] for r in rs][::-1], fontsize=9.8)
    axes[0].get_yticklabels()[0].set_fontweight("bold")
    axes[0].get_yticklabels()[0].set_color(PP.INK)
    for ax in axes:
        ax.axhline(0.5, color=PP.AXIS, lw=0.9, zorder=0)
        ax.axhline(n - 1.5, color=PP.GRID, lw=0.9, zorder=0)
    PP.title(fig, "Argus-V-emp: 세 부분을 섞으면 어느 부분보다도 높아진다 (새 test)",
             "Argus-V-emp = ① Argus-V-em 모델 36개의 평균, ② Argus-V-p P3, ③ Argus-V-p P5를 1/3씩. 섞는 단계에는 학습이 없다")
    PP.note(fig, "AUROC 막대는 0.5(우연)에서 시작한다 · F1은 validation 정상 호출의 5%가 경보가 되는 커트라인으로 판정한 값")
    PP.save(fig, OUT, fname)


# ------------------------------------------------------------------------------------------------ emp, shared
def emp_data(D):
    out = {}
    for s in ("validation", "test"):
        rows = D["idx"][s]
        out[s] = {"score": AE.scores(s), "y": D["y"][rows], "vis": D["vis"][rows]}
    v = out["validation"]
    out["cut"] = {"5%": float(np.quantile(v["score"][v["y"] == 0], 0.95)), "1%": float(np.quantile(v["score"][v["y"] == 0], 0.99))}
    return out


def judge(score, y, thr):
    alarm = score > thr
    tp, fp = int((alarm & (y == 1)).sum()), int((alarm & (y == 0)).sum())
    fn, tn = int((~alarm & (y == 1)).sum()), int((~alarm & (y == 0)).sum())
    rec = tp / max(1, tp + fn)
    pre = tp / max(1, tp + fp)
    return {"tp": tp, "fp": fp, "fn": fn, "tn": tn, "recall": rec, "precision": pre, "f1": 2 * pre * rec / (pre + rec) if tp else 0.0,
            "accuracy": (tp + tn) / len(y)}


# ------------------------------------------------------------------------------------------------ 12
def fig_emp_curves(E, fname):
    plt = PP.plt
    from sklearn.metrics import precision_recall_curve
    h = 6.3
    fig, axes = plt.subplots(1, 2, figsize=(12.0, h))
    fig.subplots_adjust(top=1 - 1.45 / h, left=0.075, right=0.975, bottom=1.45 / h, wspace=0.20)
    ax = axes[0]
    ax.plot([0, 1], [0, 1], color=PP.MUTED, lw=1.0, ls=DASH, zorder=1)
    for s, col, lab, dy in (("validation", VAL, "새 validation", -0.07), ("test", TEST, "새 test", 0.0)):
        d = E[s]
        f, t = PP.roc_points(d["score"], d["y"])
        ax.plot(f, t, color=col, lw=2.3, zorder=3)
        for name, mk in (("5%", "o"), ("1%", "s")):
            j = judge(d["score"], d["y"], E["cut"][name])
            ax.plot(j["fp"] / (j["fp"] + j["tn"]), j["recall"], mk, markersize=8.5, color=col, markeredgecolor=PP.SURFACE, markeredgewidth=1.4, zorder=5)
        ax.text(0.97, 0.20 + dy, f"{lab} · AUROC {auc(d['score'], d['y']):.3f}", transform=ax.transAxes, ha="right", va="bottom", fontsize=10, color=PP.INK, bbox=PP.LBL)
    ax.set_xlim(-0.01, 1.0)
    ax.set_ylim(0, 1.01)
    ax.set_aspect("equal")
    ax.set_xlabel("오경보율 (정상 호출 중 경보가 된 비율)", fontsize=9.6)
    ax.set_ylabel("재현율 (위반 중 잡은 비율)", fontsize=9.6)
    ax.set_title("ROC 곡선 (아래 넓이 = AUROC)", fontsize=10.4, color=PP.INK, pad=8, loc="left")
    ax = axes[1]
    for s, col in (("validation", VAL), ("test", TEST)):
        d = E[s]
        p, r, _ = precision_recall_curve(d["y"], d["score"])
        ax.plot(r, p, color=col, lw=2.0, zorder=3, drawstyle="steps-post")
        for name, mk in (("5%", "o"), ("1%", "s")):
            j = judge(d["score"], d["y"], E["cut"][name])
            ax.plot(j["recall"], j["precision"], mk, markersize=8.5, color=col, markeredgecolor=PP.SURFACE, markeredgewidth=1.4, zorder=5)
            if s == "test":
                ax.annotate(f"커트라인 {E['cut'][name]:.3f}\n재현율 {j['recall']:.3f} · 정밀도 {j['precision']:.3f} · F1 {j['f1']:.3f}", (j["recall"], j["precision"]),
                            xytext=(j["recall"] + 0.06, j["precision"] + (0.09 if name == "5%" else 0.16)), fontsize=8.8, color=PP.INK2,
                            arrowprops=dict(arrowstyle="-", color=PP.MUTED, lw=0.8), bbox=PP.LBL)
    base = float(E["test"]["y"].mean())
    ax.axhline(base, color=PP.MUTED, lw=1.0, ls=DASH, zorder=1)
    ax.text(0.99, base + 0.008, f"우연 = 위반의 비율 {base:.3f}", ha="right", va="bottom", fontsize=8.6, color=PP.INK2)
    ax.set_xlim(0, 1.0)
    ax.set_ylim(0, 0.42)
    ax.set_xlabel("재현율 (위반 중 잡은 비율)", fontsize=9.6)
    ax.set_ylabel("정밀도 (경보 중 진짜 위반의 비율)", fontsize=9.6)
    ax.set_title("정밀도-재현율 곡선", fontsize=10.4, color=PP.INK, pad=8, loc="left")
    fig.legend(handles=[PP.Line2D([0], [0], color=VAL, lw=2.3, label="새 validation (위반 26개 · 정상 3,191개)"), PP.Line2D([0], [0], color=TEST, lw=2.3, label="새 test (위반 26개 · 정상 3,194개)"),
                        PP.Line2D([0], [0], marker="o", ls="", markersize=8, color=PP.INK2, label=f"커트라인 {E['cut']['5%']:.3f} (validation 정상의 5%가 경보)"),
                        PP.Line2D([0], [0], marker="s", ls="", markersize=8, color=PP.INK2, label=f"커트라인 {E['cut']['1%']:.3f} (validation 정상의 1%가 경보)")],
               loc="lower center", bbox_to_anchor=(0.5, 0.40 / h), ncol=2, columnspacing=2.4, fontsize=9.4)
    PP.title(fig, "Argus-V-emp: ROC 곡선과 정밀도-재현율 곡선 (새 validation · 새 test)",
             "위반 전부 대 정상 호출, 도구·시기 구분 없이 전부 비교. 점은 커트라인을 정했을 때의 위치다")
    PP.note(fig, "정밀도가 낮은 것은 정상 호출이 위반보다 123배 많기 때문이다 · 정밀도-재현율 곡선의 세로축은 0.42까지만 그렸다")
    PP.save(fig, OUT, fname)


# ------------------------------------------------------------------------------------------------ 13
def fig_emp_dist(E, fname):
    plt = PP.plt
    d = E["test"]
    s, y, vis = d["score"], d["y"], d["vis"]
    c5, c1 = E["cut"]["5%"], E["cut"]["1%"]
    h = 6.6
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(11.6, h), sharex=True, gridspec_kw={"height_ratios": [2.3, 1.0]})
    fig.subplots_adjust(top=1 - 1.25 / h, left=0.085, right=0.975, bottom=1.4 / h, hspace=0.10)
    bins = np.arange(0.0, 1.0001, 0.02)
    a1.hist(s[y == 0], bins=bins, color=PP.NORM, alpha=0.75, zorder=3, edgecolor=PP.SURFACE, linewidth=0.8)
    a1.set_ylabel("정상 호출 수", fontsize=9.6)
    a1.grid(axis="x", visible=False)
    rng = np.random.default_rng(0)
    for mask, kw, _ in ((vis, dict(color=PP.VIOL, markeredgecolor=PP.SURFACE, markeredgewidth=1.2), "근거가 보인 위반"),
                        ((y == 1) & ~vis, dict(markerfacecolor=PP.SURFACE, markeredgecolor=PP.VIOL, markeredgewidth=1.6), "근거가 보이지 않은 위반")):
        a2.plot(s[mask], rng.uniform(0.25, 0.75, int(mask.sum())), "o", markersize=8.5, ls="", zorder=4, **kw)
    a2.set_ylim(0, 1)
    a2.set_yticks([])
    a2.set_ylabel("위반 26개", fontsize=9.6)
    a2.grid(visible=False)
    a2.set_xlabel("Argus-V-emp 점수 (0 ~ 1, 확률이 아니라 다른 호출들보다 얼마나 위쪽인가)", fontsize=9.6)
    j5, j1 = judge(s, y, c5), judge(s, y, c1)
    for ax in (a1, a2):
        ax.axvline(c5, color=PP.INK, lw=1.4, zorder=5)
        ax.axvline(c1, color=PP.INK2, lw=1.1, ls=DASH, zorder=5)
        ax.set_xlim(0, 1.0)
    top = a1.get_ylim()[1]
    a1.text(c5 - 0.012, top * 0.96, f"커트라인 {c5:.3f} 아래 → 정상으로 판정\n정상 {j5['tn']:,}개 · 위반 {j5['fn']}개(놓침)", ha="right", va="top", fontsize=9.4, color=PP.INK, bbox=PP.LBL, linespacing=1.5)
    a1.text(c5 + 0.012, top * 0.96, f"위 → 위반으로 판정\n정상 {j5['fp']}개(오경보)\n위반 {j5['tp']}개(잡음)", ha="left", va="top", fontsize=9.4, color=PP.INK, bbox=PP.LBL, linespacing=1.5)
    a1.text(c1 + 0.006, top * 0.52, f"{c1:.3f}", ha="left", va="top", fontsize=8.8, color=PP.INK2, bbox=PP.LBL)
    fig.legend(handles=[PP.Line2D([0], [0], marker="s", ls="", markersize=9, color=PP.NORM, alpha=0.75, label=f"정상 호출 {int((y == 0).sum()):,}개 (막대)"),
                        PP.Line2D([0], [0], marker="o", ls="", markersize=8.5, color=PP.VIOL, markeredgecolor=PP.SURFACE, label=f"근거가 보인 위반 {int(vis.sum())}개"),
                        PP.Line2D([0], [0], marker="o", ls="", markersize=8.5, markerfacecolor=PP.SURFACE, markeredgecolor=PP.VIOL, markeredgewidth=1.6, label=f"근거가 보이지 않은 위반 {int(((y == 1) & ~vis).sum())}개"),
                        PP.Line2D([0], [0], color=PP.INK, lw=1.4, label=f"커트라인 {c5:.3f} (validation 정상의 5%가 경보)"),
                        PP.Line2D([0], [0], color=PP.INK2, lw=1.1, ls=DASH, label=f"커트라인 {c1:.3f} (1%가 경보)")],
               loc="lower center", bbox_to_anchor=(0.5, 0.36 / h), ncol=3, columnspacing=2.0, fontsize=9.2)
    PP.title(fig, "새 test: Argus-V-emp가 준 점수의 분포와 커트라인",
             f"호출 {len(y):,}개. 점수가 커트라인을 넘으면 위반으로 판정한다. 커트라인 {c5:.3f}에서 재현율 {j5['recall']:.3f} · 정밀도 {j5['precision']:.3f} · F1 {j5['f1']:.3f}")
    PP.note(fig, "커트라인은 validation에서 정했다 · 위반의 세로 위치는 겹치지 않게 흩은 것이고 뜻이 없다")
    PP.save(fig, OUT, fname)
    return {"cut_5pct": c5, "cut_1pct": c1, "test_at_5pct": j5, "test_at_1pct": j1}


# ------------------------------------------------------------------------------------------------ 14
def fig_emp_sweep(E, fname):
    plt = PP.plt
    grid = np.round(np.arange(0.40, 0.9901, 0.005), 3)
    h = 5.7
    fig, axes = plt.subplots(1, 3, figsize=(12.6, h), sharex=True)
    fig.subplots_adjust(top=1 - 1.45 / h, left=0.065, right=0.975, bottom=1.3 / h, wspace=0.22)
    panels = (("recall", "재현율 (위반 중 잡은 비율)", 1.0), ("precision", "정밀도 (경보 중 진짜 위반의 비율)", 0.22), ("f1", "F1", 0.22))
    for ax, (key, name, ymax) in zip(axes, panels):
        for s, col in (("validation", VAL), ("test", TEST)):
            d = E[s]
            v = [judge(d["score"], d["y"], float(t))[key] for t in grid]
            ax.plot(grid, v, color=col, lw=2.0, zorder=3)
        for cut, lab, ls, col in ((E["cut"]["5%"], "5%", "-", PP.INK), (E["cut"]["1%"], "1%", DASH, PP.INK2)):
            ax.axvline(cut, color=col, lw=1.2, ls=ls, zorder=2)
            ax.text(cut, 1.01, f"{cut:.3f}", transform=ax.get_xaxis_transform(), ha="center", va="bottom", fontsize=8.8, color=PP.INK2)
        j = judge(E["test"]["score"], E["test"]["y"], E["cut"]["5%"])
        ax.plot(E["cut"]["5%"], j[key], "o", markersize=8.5, color=TEST, markeredgecolor=PP.SURFACE, markeredgewidth=1.4, zorder=5)
        ax.text(E["cut"]["5%"] - 0.012, j[key] + ymax * 0.035, f"{j[key]:.3f}", ha="right", va="bottom", fontsize=9.6, color=PP.INK, bbox=PP.LBL)
        ax.set_xlim(0.40, 0.99)
        ax.set_ylim(0, ymax)
        ax.set_xticks([0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
        ax.set_xlabel("커트라인 (Argus-V-emp 점수)", fontsize=9.6)
        ax.set_title(name, fontsize=10.2, color=PP.INK, pad=18, loc="left")
    fig.legend(handles=[PP.Line2D([0], [0], color=VAL, lw=2.3, label="새 validation"), PP.Line2D([0], [0], color=TEST, lw=2.3, label="새 test (점과 숫자 = 커트라인 0.864에서의 값)"),
                        PP.Line2D([0], [0], color=PP.INK, lw=1.2, label="validation 정상의 5%가 경보가 되는 커트라인"),
                        PP.Line2D([0], [0], color=PP.INK2, lw=1.2, ls=DASH, label="1%가 경보가 되는 커트라인")],
               loc="lower center", bbox_to_anchor=(0.5, 0.40 / h), ncol=4, columnspacing=1.8, fontsize=9.2)
    PP.title(fig, "Argus-V-emp: 커트라인을 옮기면 재현율 · 정밀도 · F1이 어떻게 바뀌나",
             "커트라인은 사용자가 정하는 값이다. 낮추면 위반을 더 잡는 대신 오경보가 늘어 정밀도가 내려간다")
    PP.note(fig, "커트라인은 validation에서 정한다. test의 곡선은 참고로 그린 것이고 이것을 보고 커트라인을 고르지 않았다")
    PP.save(fig, OUT, fname)


# ------------------------------------------------------------------------------------------------ 15
def fig_emp_confusion(E, fname):
    plt = PP.plt
    c5 = E["cut"]["5%"]
    h = 5.3
    fig, axes = plt.subplots(1, 2, figsize=(9.6, h))
    fig.subplots_adjust(top=1 - 1.75 / h, left=0.13, right=0.97, bottom=0.75 / h, wspace=0.30)
    out = {}
    for ax, (s, lab) in zip(axes, (("validation", "새 validation"), ("test", "새 test"))):
        d = E[s]
        j = judge(d["score"], d["y"], c5)
        out[s] = j
        grid = np.array([[j["tp"], j["fn"]], [j["fp"], j["tn"]]], dtype=np.float64)
        share = grid / grid.sum(axis=1, keepdims=True)
        for i in range(2):
            for k in range(2):
                good = i == k
                ax.add_patch(plt.Rectangle((k, 1 - i), 1, 1, facecolor="#1baf7a" if good else "#d03b3b", alpha=0.10 + 0.55 * float(share[i, k]), edgecolor=PP.SURFACE, linewidth=2))
                ax.text(k + 0.5, 1 - i + 0.58, f"{grid[i, k]:,.0f}", ha="center", va="center", fontsize=14, color=PP.INK)
                ax.text(k + 0.5, 1 - i + 0.30, f"{share[i, k]:.1%}", ha="center", va="center", fontsize=9.4, color=PP.INK2)
        ax.set_xlim(0, 2)
        ax.set_ylim(0, 2)
        ax.set_xticks([0.5, 1.5])
        ax.set_xticklabels(["위반으로 판정", "정상으로 판정"], fontsize=9.6)
        ax.set_yticks([1.5, 0.5])
        ax.set_yticklabels(["실제 위반", "실제 정상"] if s == "validation" else ["", ""], fontsize=9.6)
        ax.grid(visible=False)
        for sp in ax.spines.values():
            sp.set_visible(False)
        ax.set_title(f"{lab}\n재현율 {j['recall']:.3f} · 정밀도 {j['precision']:.3f} · F1 {j['f1']:.3f}\n맞힌 비율 {j['accuracy']:.3f}", fontsize=10.0, color=PP.INK, pad=8, loc="left", linespacing=1.45)
    PP.title(fig, f"Argus-V-emp: 커트라인 {c5:.3f}로 판정한 결과 (혼동 행렬)",
             "커트라인 = validation 정상 호출의 5%가 경보가 되는 점수. 칸 아래 숫자는 그 줄(실제 위반 / 실제 정상) 안에서의 비율")
    PP.note(fig, "전부 “정상”이라고 판정해도 맞힌 비율은 0.992다(위반이 0.8%뿐). 그래서 맞힌 비율이 아니라 재현율·정밀도·F1을 본다")
    PP.save(fig, OUT, fname)
    return out


FIGS = ("01_전체_모델_AUROC_위반_전부.png", "02_전체_모델_AUROC_근거가_보인_위반.png", "03_전체_모델_재현율_정밀도_F1.png", "04_전체_모델_ROC_곡선.png",
        "05_Argus-V-p_기존_분할.png", "06_Argus-V-p_새_분할.png", "07_Argus-V-em_kfold_교차검증과_기존_test.png", "08_Argus-V-em_위반_가중치_기존_분할.png",
        "09_Argus-V-em_모델_크기와_가중치.png", "10_Argus-V-em_epoch_곡선.png", "11_Argus-V-emp_구성_부분과_결과.png", "12_Argus-V-emp_ROC와_정밀도_재현율.png",
        "13_Argus-V-emp_점수_분포와_커트라인.png", "14_Argus-V-emp_커트라인별_재현율_정밀도_F1.png", "15_Argus-V-emp_혼동_행렬.png")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="", help="comma-separated figure numbers, e.g. 01,12")
    only = {x.strip() for x in ap.parse_args().only.split(",") if x.strip()}
    want = lambda k: not only or f"{k:02d}" in only                                                    # noqa: E731
    check_records()
    PP.setup()
    OUT.mkdir(parents=True, exist_ok=True)
    ov = json.loads((AE.REPORT / "overview_table.json").read_text(encoding="utf-8"))
    D = R.load()
    numbers = {}
    if want(1):
        fig_all(ov, "all", FIGS[0])
    if want(2):
        fig_all(ov, "visible", FIGS[1])
    if want(3):
        fig_cut(ov, FIGS[2])
    if want(4):
        fig_roc(ov, D, FIGS[3])
    if want(5):
        fig_p_old(FIGS[4])
    if want(6):
        fig_p_new(ov, FIGS[5])
    if want(7):
        fig_em_old(FIGS[6])
    if want(8):
        fig_weights_old(FIGS[7])
    if want(9):
        fig_heat(ov, FIGS[8])
    if want(10):
        numbers["epochs"] = fig_epochs(D, FIGS[9])
    if want(11):
        fig_parts(ov, FIGS[10])
    if any(want(k) for k in (12, 13, 14, 15)):
        E = emp_data(D)
        if want(12):
            fig_emp_curves(E, FIGS[11])
        if want(13):
            numbers["distribution"] = fig_emp_dist(E, FIGS[12])
        if want(14):
            fig_emp_sweep(E, FIGS[13])
        if want(15):
            numbers["confusion_at_5pct_cut"] = fig_emp_confusion(E, FIGS[14])
        numbers["auroc"] = {s: auc(E[s]["score"], E[s]["y"]) for s in ("validation", "test")}
    if not only:
        (OUT / "numbers.json").write_text(json.dumps(numbers, ensure_ascii=False, indent=1), encoding="utf-8")
    print("done:", len(only) or len(FIGS), "figures")


if __name__ == "__main__":
    main()

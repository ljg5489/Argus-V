"""Argus-V-em evaluation figures (matplotlib), in the style of argus_v_p_plots.py. Fits nothing.

Reads the saved round-01 held-out scores (artifacts/risk-loop/argus-v-em/oof_*.npy), the saved checkpoint's
training-row scores and the per-epoch record written by argus_v_em_epochs.py (addendum 2).

Every figure states what was scored:
  held-out  = "처음 보는 시나리오": scenario-family folds, the scored fold was not used for training
  in-sample = "학습 데이터 재채점": the saved all-rows EM32 model scoring the rows it was trained on
Target rows = normal calls + violations whose deciding fact was visible before the action (provisional-1 record).

Usage : PYTHONUTF8=1 py -3.11 experiments/risk_loop/argus_loop/argus_v_em_plots.py
Output: reports/risk-loop/argus-v-em/figures/*.png + tables.md
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from experiments.risk_loop.argus_loop import argus_v_p_plots as PP  # noqa: E402  (sets the Agg backend and the style)
from experiments.risk_loop import harness as H  # noqa: E402
from experiments.risk_loop.argus_loop import argus_v_em as EM  # noqa: E402
from experiments.risk_loop.argus_loop import argus_v_p as AP  # noqa: E402
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402

plt, Line2D = PP.plt, PP.Line2D
SURFACE, INK, INK2, MUTED, GRID, BASE = PP.SURFACE, PP.INK, PP.INK2, PP.MUTED, PP.GRID, PP.BASE
HELD, TRAIN, VIOL, NORM = PP.COND["A"]["color"], PP.COND["C"]["color"], PP.VIOL, PP.NORM
HELD_KO, TRAIN_KO = "처음 보는 시나리오", "학습 데이터 재채점"
WIDTH_RAMP = {"EM32": "#86b6ef", "EM64": "#3987e5", "EM128": "#184f95"}     # ordinal blue ramp (validated --ordinal)
MODEL_KO = {"EM32": "32차원 임베딩", "EM64": "64차원 임베딩", "EM128": "128차원 임베딩", "LINEAR": "임베딩 없이 선형 점수만 (대조)"}
MODEL_SHORT = {"EM32": "32차원", "EM64": "64차원", "EM128": "128차원", "LINEAR": "선형 대조"}
TRACKS = {
    "em": {"name": "Argus-V-em", "report": EM.REPORT, "out": EM.OUT, "results": "round01_results.json",
           "linear": "round01_linear_control.json", "shuffle": "round01_shuffle.json", "final": "epochs/final_EM32.npz"},
    "em300": {"name": "Argus-V-em300", "report": REPO_ROOT / "reports/risk-loop/argus-v-em300",
              "out": REPO_ROOT / "artifacts/risk-loop/argus-v-em300", "results": "results.json",
              "linear": "linear_control.json", "shuffle": "shuffle.json", "final": "epochs/final.npz", "base": "em"},
}
TRACK = TRACKS["em"]                 # main() switches it with --track
OUT = EM.REPORT / "figures"
FIG_W = PP.FIG_W
LBL = PP.LBL


def short(cell):
    return cell.split("|")[0]


def handle(color, label, marker="o", line=True, hollow=False, ls="-"):
    return Line2D([0], [0], color=color, lw=2 if line else 0, ls=ls, marker=marker, markersize=8,
                  markerfacecolor=SURFACE if hollow else color, markeredgecolor=color if hollow else SURFACE,
                  markeredgewidth=1.6, label=label)


# ------------------------------------------------------------------------------------------------ data

class Data:
    def __init__(self):
        self.cx = cx = EM.Ctx()
        self.vis, self.rule = EM.visible_mask(cx)
        self.target = (cx.y == 0) | self.vis                       # rows the model is trained and scored on
        self.yv = self.vis.astype(np.int64)
        elig = {}
        for cell in sorted(set(cx.groups.tolist())):
            m = cx.groups == cell
            p, n = int(self.vis[m].sum()), int(((cx.y == 0) & m).sum())
            elig[cell] = (p, n)
        self.cells3 = sorted(c for c, (p, n) in elig.items() if p >= 3 and n >= 3)
        self.cells2 = sorted(c for c, (p, n) in elig.items() if p >= 2 and n >= 2)
        self.counts = elig
        self.mask3 = self.target & np.isin(cx.groups, self.cells3)
        self.mask2 = self.target & np.isin(cx.groups, self.cells2)
        rep, art = TRACK["report"], TRACK["out"]
        self.res = json.loads((rep / TRACK["results"]).read_text(encoding="utf-8"))
        self.lin = json.loads((rep / TRACK["linear"]).read_text(encoding="utf-8"))
        self.shuf = json.loads((rep / TRACK["shuffle"]).read_text(encoding="utf-8"))
        assert sorted(self.res["eligible_cells"]) == self.cells2, "cell list differs from round 01"
        self.oof = {m: [np.load(art / f"oof_{m}_s{s}.npy") for s in EM.SEEDS] for m in MODEL_KO}
        self.oof_mean = {m: np.mean(v, axis=0) for m, v in self.oof.items()}
        self.p_oof = {k: [np.load(AP.oof_path(k, "A", s)) for s in AP.SEEDS] for k in ("P1", "P5")}
        hist_path = rep / "epoch_history.json"
        self.hist = json.loads(hist_path.read_text(encoding="utf-8")) if hist_path.is_file() else None
        fin = art / TRACK["final"]
        if not fin.is_file():
            raise SystemExit(f"{fin} is missing: run the training script of this track first")
        self.ins = np.load(fin)["saved_checkpoint_scores"].astype(np.float64)   # saved model on all rows
        self.selected = self.sel = self.res["selected_on_development_oof"]
        self.sel_ko = MODEL_SHORT[self.sel] + " 모델"
        self.N = self.hist["epochs"] if self.hist else EM.EPOCHS
        long = self.N > 60
        self.ticks = [1, 50, 100, 150, 200, 250, 300] if long else [1, 10, 20, 30, 40, 50, 60]
        self.ticks_small = [1, 100, 200, 300] if long else [1, 20, 40, 60]
        self.marks = (1, 20, 40, 60, 80, 100, 150, 200, 250, 300) if long else (1, 5, 10, 20, 30, 40, 50, 60)
        self.marks_fine = (1, 10, 20, 30, 40, 50, 60, 80, 100, 150, 200, 250, 300) if long else (1, 2, 3, 5, 10, 20, 30, 40, 50, 60)
        self.span = (60, self.N) if long else (40, 60)        # the stretch whose change is broken down per cell
        self.fin_hist = (self.hist.get("final") or self.hist.get("final_EM32")) if self.hist else None
        # the same hidden state is repeated across runs: distinct inputs among the visible violations of each cell
        hsh = np.asarray(cx.hashes, dtype=str)
        self.dpos = {c: len(set(hsh[self.vis & (cx.groups == c)].tolist())) for c in self.cells2}
        self.d3, self.d2 = sum(self.dpos[c] for c in self.cells3), sum(self.dpos[c] for c in self.cells2)
        self.distinct = np.zeros(cx.n, dtype=bool)            # one row per (cell, input, label)
        seen = set()
        for i in np.flatnonzero(self.mask2):
            k = (cx.groups[i], hsh[i], int(self.yv[i]))
            if k not in seen:
                seen.add(k)
                self.distinct[i] = True

    def wt(self, s, mask, min_pos):
        return EM.score_metric(self.cx, s, mask, min_pos)

    def per_seed(self, score_list, mask, min_pos):
        return [float(self.wt(s, mask, min_pos)["value"]) for s in score_list]

    def cell_auc(self, s, cell):
        m = self.target & (self.cx.groups == cell)
        return float(H.auroc(np.asarray(s)[m], self.yv[m]))

    def family_ci(self, score_list, mask, min_pos, reps=2000, seed=0):
        """Percentile 95% interval of the seed-mean same-tool AUROC, resampling scenario families with replacement."""
        cx = self.cx
        idx = np.flatnonzero(mask)
        fam = cx.rows.family.astype(str)[idx]
        g, y = cx.groups[idx], self.yv[idx]
        S = [np.asarray(s, dtype=np.float64)[idx] for s in score_list]
        fams = sorted(set(fam.tolist()))
        members = [np.flatnonzero(fam == f) for f in fams]
        rng = np.random.default_rng(seed)
        vals = []
        for _ in range(reps):
            loc = np.concatenate([members[i] for i in rng.integers(0, len(fams), len(fams))])
            num, den = np.zeros(len(S)), 0
            for cell in set(g[loc].tolist()):
                m = loc[g[loc] == cell]
                p = int(y[m].sum())
                if p < min_pos or len(m) - p < E.MIN_NEG:
                    continue
                for k, s in enumerate(S):
                    num[k] += H.auroc(s[m], y[m]) * p
                den += p
            if den:
                vals.append(float(num.mean() / den))
        lo, hi = np.percentile(vals, [2.5, 97.5])
        return float(lo), float(hi), len(vals), len(fams)


def wroc(D: Data, s, mask, min_pos):
    """Violation-weighted mean of the per-cell ROC curves on a common grid (its area = same-tool AUROC)."""
    grid = np.linspace(0, 1, 401)
    acc, den, cells = np.zeros_like(grid), 0, {}
    g = D.cx.groups
    for cell in sorted(set(g[mask].tolist())):
        m = mask & (g == cell)
        p = int(D.yv[m].sum())
        n = int(m.sum()) - p
        if p < min_pos or n < E.MIN_NEG:
            continue
        f, t = PP.roc_points(np.asarray(s)[m], D.yv[m])
        cells[cell] = (f, t, p, n, float(H.auroc(np.asarray(s)[m], D.yv[m])))
        acc += p * np.interp(grid, f, t)
        den += p
    return grid, acc / den, cells


def op_point(s, y, fa):
    thr = float(np.quantile(s[y == 0], 1 - fa))
    alarm = s > thr
    tp, fp = int((alarm & (y == 1)).sum()), int((alarm & (y == 0)).sum())
    fn, tn = int((~alarm & (y == 1)).sum()), int((~alarm & (y == 0)).sum())
    return {"threshold": thr, "tp": tp, "fp": fp, "fn": fn, "tn": tn, "recall": tp / max(1, tp + fn),
            "false_alarm": fp / max(1, fp + tn), "precision": tp / max(1, tp + fp)}


# ------------------------------------------------------------------------------------------------ figures

def fig01_models(D: Data, T: dict):
    rows = []
    for m in MODEL_KO:
        key = D.lin if m == "LINEAR" else D.res["architectures"][m]
        seeds = key["visible_min3"]["per_seed"]
        rows.append({"label": (f"{MODEL_KO[m]} ({m})" if m != "LINEAR" else MODEL_KO[m]) + ("  ◀ 선택" if m == D.selected else ""),
                     "mean": float(np.mean(seeds)), "runs": seeds, "ci": D.family_ci(D.oof[m], D.mask3, 3)[:2],
                     "color": HELD if m != "LINEAR" else MUTED, "key": m})
    if TRACK.get("base"):                         # the same structure stopped at 60 epochs
        base = TRACKS[TRACK["base"]]
        bsel = json.loads((base["report"] / base["results"]).read_text(encoding="utf-8"))["selected_on_development_oof"]
        boof = [np.load(base["out"] / f"oof_{bsel}_s{s}.npy") for s in EM.SEEDS]
        seeds = D.per_seed(boof, D.mask3, 3)
        rows.append({"label": f"{base['name']} · {MODEL_SHORT[bsel]}, 60 epoch에서 멈춘 것", "mean": float(np.mean(seeds)), "runs": seeds,
                     "ci": D.family_ci(boof, D.mask3, 3)[:2], "color": MUTED, "key": "BASE"})
    for k in ("P1", "P5"):
        seeds = D.per_seed(D.p_oof[k], D.mask3, 3)
        rows.append({"label": f"Argus-V-p {k} · 같은 행으로 다시 잼", "mean": float(np.mean(seeds)), "runs": seeds,
                     "ci": D.family_ci(D.p_oof[k], D.mask3, 3)[:2], "color": MUTED, "key": k})
    runs = [p["visible_min3"] for p in D.shuf["permutations"]]
    rows.append({"label": f"점검: 학습 라벨을 섞은 {D.sel_ko}", "mean": float(np.mean(runs)), "runs": runs, "ci": None,
                 "color": MUTED, "key": "SHUFFLE"})
    T["models"] = rows
    fig, ax = plt.subplots(figsize=(FIG_W, 5.5))
    fig.subplots_adjust(top=0.80, left=0.40, right=0.93, bottom=0.20)
    for i, r in enumerate(rows):
        yy = len(rows) - 1 - i
        if r["ci"]:
            ax.plot(r["ci"], [yy, yy], color=INK2, lw=1.2, zorder=2, solid_capstyle="butt")
        ax.plot(r["runs"], [yy] * len(r["runs"]), "o", markersize=5.5, markerfacecolor=SURFACE, markeredgecolor=r["color"],
                markeredgewidth=1.3, zorder=3)
        ax.plot(r["mean"], yy, "o", markersize=10.5, color=r["color"], markeredgecolor=SURFACE, markeredgewidth=2, zorder=4)
        right = max([r["mean"]] + list(r["runs"]) + ([r["ci"][1]] if r["ci"] else []))
        ax.text(min(right, 1.0) + 0.014, yy, f"{r['mean']:.2f}", va="center", ha="left", fontsize=9.8, color=INK, bbox=LBL, zorder=5)
    ax.set_yticks(range(len(rows)))
    ax.set_yticklabels([r["label"] for r in rows][::-1])
    ax.set_xlim(0.30, 1.07)
    ax.set_ylim(-0.6, len(rows) - 0.4)
    ax.set_xlabel("같은 도구 안 AUROC (0.5 = 우연)")
    ax.grid(axis="y", visible=False)
    PP.ref_line(ax, x=0.5, label="우연")
    PP.ref_line(ax, x=0.9, label="목표 0.90")
    ax.legend(handles=[handle(MUTED, "평균", line=False), handle(MUTED, "나누기 하나(라벨 섞기는 한 번의 실행)", line=False, hollow=True),
                       Line2D([0], [0], color=INK2, lw=1.2, label="95% 구간(시나리오 계열을 다시 뽑아 계산)")],
              loc="upper center", bbox_to_anchor=(0.20, -0.14), ncol=3, handletextpad=0.4, columnspacing=1.4, fontsize=9.3)
    sel_mean = T["heldout"][D.sel]["min3"]
    head = ("학습된 임베딩은 목표 기준에서 0.90을 넘는다 — 개발용 데이터 기준" if sel_mean >= 0.90 else
            f"{D.N} epoch까지 학습하면 선택된 모델이 {sel_mean:.2f}로 0.90에 못 미친다 — 개발용 데이터 기준")
    PP.title(fig, head, f"{HELD_KO} · 행동 전에 근거가 보인 위반만 채점 · 위반 16개(서로 다른 입력 {D.d3}개), 도구 칸 4개")
    PP.note(fig, "근거 표시 규칙은 잠정판이고 Argus-V-p 점수를 본 뒤에 만들었다 · 같은 학습 분할 행을 다시 쓴 개발용 점수이며 새 시나리오로 확인한 값이 아니다")
    PP.save(fig, OUT, "01_모델별_점수.png")


def fig02_roc(D: Data, T: dict):
    fig, axes = plt.subplots(1, 2, figsize=(FIG_W + 2.6, 6.5))
    fig.subplots_adjust(top=0.84, left=0.07, right=0.985, bottom=0.15, wspace=0.16)
    ax = axes[0]
    ax.plot([0, 1], [0, 1], color=BASE, lw=1.2, zorder=1)
    g, t, _ = wroc(D, D.ins, D.mask3, 3)
    ax.plot(g, t, color=TRAIN, lw=2, zorder=3, label=f"{TRAIN_KO}  {T['insample_min3']:.2f}")
    g, t, _ = wroc(D, D.oof_mean[D.sel], D.mask3, 3)
    ax.plot(g, t, color=HELD, lw=2, zorder=4, label=f"{HELD_KO}  {T['heldout'][D.sel]['min3']:.2f}")
    ax.set_title(f"{D.sel_ko}: 학습에 쓴 행과 처음 보는 시나리오", fontsize=10.8, color=INK, pad=8)
    ax.legend(loc="lower right", title="같은 도구 안 AUROC", title_fontsize=9.5, handlelength=1.6)
    ax = axes[1]
    ax.plot([0, 1], [0, 1], color=BASE, lw=1.2, zorder=1)
    g, t, _ = wroc(D, D.oof_mean["LINEAR"], D.mask3, 3)
    ax.plot(g, t, color=MUTED, lw=1.8, ls=(0, (5, 2)), zorder=2, label=f"선형 대조  {T['heldout']['LINEAR']['min3']:.2f}")
    for m in ("EM128", "EM64", "EM32"):
        g, t, _ = wroc(D, D.oof_mean[m], D.mask3, 3)
        ax.plot(g, t, color=WIDTH_RAMP[m], lw=2, zorder=3, label=f"{MODEL_SHORT[m]}  {T['heldout'][m]['min3']:.2f}")
    hh, ll = ax.get_legend_handles_labels()
    ax.legend(hh[::-1], ll[::-1], loc="lower right", title="처음 보는 시나리오 AUROC", title_fontsize=9.5, handlelength=1.8)
    ax.set_title("임베딩 폭 비교 (처음 보는 시나리오)", fontsize=10.8, color=INK, pad=8)
    for ax in axes:
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1.005)
        ax.set_aspect("equal")
        ax.set_xlabel("오경보율 (정상을 위반으로 본 비율)")
        ax.text(0.62, 0.56, "우연 수준", rotation=45, color=MUTED, fontsize=9, ha="center", va="center")
    axes[0].set_ylabel("탐지율 (근거가 보인 위반을 잡은 비율)")
    PP.title(fig, f"ROC 곡선 — {TRACK['name']}","도구 칸 4개의 곡선을 위반 수로 가중 평균(위반 16개). 범례 숫자는 데이터 나누기 3가지의 평균 AUROC")
    PP.note(fig, "곡선은 세 번 나누기의 점수를 행마다 평균해 그렸다 · 위반이 16개뿐이라 계단 모양이다")
    PP.save(fig, OUT, "02_ROC_곡선.png")


def fig03_roc_cells(D: Data, T: dict):
    held = wroc(D, D.oof_mean[D.sel], D.mask2, 2)[2]
    ins = wroc(D, D.ins, D.mask2, 2)[2]
    order = sorted(held, key=lambda c: (-(D.counts[c][0] >= 3), -T["cells"][c]["heldout"]))
    fig, axes = plt.subplots(2, 4, figsize=(FIG_W + 1.4, 6.7), sharex=True, sharey=True)
    fig.subplots_adjust(top=0.80, left=0.07, right=0.985, bottom=0.15, hspace=0.50, wspace=0.14)
    for ax, cell in zip(axes.ravel(), order):
        ax.plot([0, 1], [0, 1], color=BASE, lw=1.0)
        ax.plot(ins[cell][0], ins[cell][1], color=TRAIN, lw=4.6, alpha=0.55, solid_capstyle="butt")   # wide, so it shows under the blue
        f, t, p, n, _ = held[cell]
        ax.plot(f, t, color=HELD, lw=1.8)
        tag = "" if p >= 3 else " · 보조"
        ax.set_title(f"{short(cell)}\n위반 {p} · 정상 {n}{tag} · {T['cells'][cell]['heldout']:.2f}", fontsize=9.2,
                     fontweight="normal", color=INK, pad=5)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1.03)
        ax.set_xticks([0, 0.5, 1])
        ax.set_yticks([0, 0.5, 1])
    for ax in axes.ravel()[len(order):]:
        ax.axis("off")
    fig.text(0.5, 0.075, "오경보율", ha="center", color=INK2)
    fig.text(0.012, 0.47, "탐지율", va="center", rotation=90, color=INK2)
    fig.legend(handles=[handle(HELD, HELD_KO, marker=None),
                        Line2D([0], [0], color=TRAIN, lw=4.6, alpha=0.55, label=f"{TRAIN_KO} (굵은 선, 겹치면 파란 선 아래에 보임)")],
               loc="upper left", bbox_to_anchor=(0.055, 0.905), ncol=2, handletextpad=0.5, columnspacing=1.8)
    PP.title(fig, f"도구 칸별 ROC 곡선 — {D.sel_ko}", None)
    PP.note(fig, "제목의 숫자 = 처음 보는 시나리오 AUROC(나누기 3가지 평균) · '보조' = 근거가 보인 위반이 2개뿐이라 주 지표(3개 이상)에는 들어가지 않는 칸")
    PP.save(fig, OUT, "03_칸별_ROC_곡선.png")


def fig04_cells(D: Data, T: dict):
    cells = sorted(T["cells"], key=lambda c: T["cells"][c]["heldout"])
    fig, ax = plt.subplots(figsize=(FIG_W, 5.0))
    fig.subplots_adjust(top=0.80, left=0.46, right=0.94, bottom=0.22)
    for yy, cell in enumerate(cells):
        c = T["cells"][cell]
        vals = [c["heldout"], c["insample"]]
        ax.plot([min(vals + c["heldout_seeds"]), max(vals + c["heldout_seeds"])], [yy, yy], color=BASE, lw=1.4, zorder=2)
        same = abs(c["insample"] - c["heldout"]) < 0.03        # both marks on one spot: lift the triangle so both show
        ax.plot(c["heldout_seeds"], [yy] * 3, "o", markersize=5.5, markerfacecolor=SURFACE, markeredgecolor=HELD, markeredgewidth=1.3, zorder=3)
        ax.plot(c["insample"], yy + (0.38 if same else 0.0), "^", color=TRAIN, markersize=10, markeredgecolor=SURFACE, markeredgewidth=2, zorder=4)
        ax.plot(c["heldout"], yy, "o", color=HELD, markersize=10, markeredgecolor=SURFACE, markeredgewidth=2, zorder=5)
    ax.set_yticks(range(len(cells)))
    ax.set_yticklabels([f"{short(c)}  (위반 {D.counts[c][0]} [입력 {D.dpos[c]}] · 정상 {D.counts[c][1]})" + ("" if D.counts[c][0] >= 3 else "  보조") for c in cells],
                       fontsize=9.6)
    ax.set_xlim(-0.02, 1.05)
    ax.set_ylim(-0.6, len(cells) - 0.4)
    ax.set_xlabel("칸 안 AUROC")
    ax.grid(axis="y", visible=False)
    PP.ref_line(ax, x=0.5, label="우연")
    PP.ref_line(ax, x=0.9, label="0.90")
    ax.legend(handles=[handle(HELD, f"{HELD_KO} (평균)", line=False), handle(HELD, "나누기 하나", line=False, hollow=True),
                       handle(TRAIN, TRAIN_KO, marker="^", line=False)],
              loc="upper center", bbox_to_anchor=(0.22, -0.16), ncol=3, handletextpad=0.3, columnspacing=1.4)
    PP.title(fig, f"도구 칸별 AUROC — {D.sel_ko}", "근거가 보인 위반이 2개 이상인 칸 7개. '보조'는 위반이 2개뿐이라 주 지표에서 빠지는 칸")
    PP.note(fig, "[입력 n] = 위반 중 서로 다른 hidden state 수(같은 입력이 여러 실행에 복제됨) · 한 개 차이로 값이 크게 움직인다 · 두 값이 같으면 세모를 위로 올림")
    PP.save(fig, OUT, "04_칸별_AUROC.png")


def fig05_scores(D: Data):
    cx = D.cx
    cells = sorted(D.cells2, key=lambda c: (-(D.counts[c][0] >= 3), c))
    rng = np.random.default_rng(0)
    fig, axes = plt.subplots(2, 1, figsize=(FIG_W, 7.6), sharex=True)
    fig.subplots_adjust(top=0.84, left=0.09, right=0.97, bottom=0.14, hspace=0.26)
    hidden_n = 0
    for ax, (nm, s) in zip(axes, ((HELD_KO, D.oof_mean[D.sel]), (TRAIN_KO, D.ins))):
        for i, cell in enumerate(cells):
            m = np.flatnonzero(cx.groups == cell)
            kinds = ((m[cx.y[m] == 0], NORM, "o", "none", NORM, 2, -0.22),
                     (m[(cx.y[m] == 1) & ~D.vis[m]], VIOL, "D", SURFACE, VIOL, 3, 0.0),
                     (m[D.vis[m]], VIOL, "D", VIOL, SURFACE, 4, 0.22))
            for k, (idx, col, mk, fc, ec, z, off) in enumerate(kinds):
                if k == 1 and ax is axes[0]:
                    hidden_n += len(idx)
                xs = i + off + rng.uniform(-0.08, 0.08, len(idx))
                ax.plot(xs, s[idx], mk, markersize=6.3, markerfacecolor=fc, markeredgecolor=ec, markeredgewidth=1.2, lw=0, zorder=z)
        ax.set_ylabel("모델 출력 점수")
        ax.set_title(nm, fontsize=10.5, color=INK, pad=6)
        ax.grid(axis="x", visible=False)
    axes[-1].set_xticks(range(len(cells)))
    axes[-1].set_xticklabels([short(c).replace("_", "\n") + ("" if D.counts[c][0] >= 3 else "\n(보조)") for c in cells], fontsize=8.6)
    fig.legend(handles=[Line2D([0], [0], lw=0, marker="D", markersize=7, markerfacecolor=VIOL, markeredgecolor=SURFACE, label="근거가 보인 위반 (학습·채점 대상)"),
                        Line2D([0], [0], lw=0, marker="D", markersize=7, markerfacecolor=SURFACE, markeredgecolor=VIOL, markeredgewidth=1.2, label="근거가 보이지 않은 위반 (학습·채점에서 뺌)"),
                        Line2D([0], [0], lw=0, marker="o", markersize=7, markerfacecolor="none", markeredgecolor=NORM, label="정상 호출")],
               loc="upper left", bbox_to_anchor=(0.07, 0.925), ncol=3, handletextpad=0.3, columnspacing=1.4, fontsize=9.3)
    PP.title(fig, f"도구 칸별 점수 분포 — {D.sel_ko}", None)
    PP.note(fig, f"점수는 확률이 아니라 순서를 매기는 값이다(클수록 위반 쪽) · 위는 세 번 나누기 평균, 아래는 저장된 최종 모델 · 이 7개 칸의 근거가 보이지 않은 위반은 {hidden_n}개")
    PP.save(fig, OUT, "05_칸별_점수_분포.png")


def fig06_scope(D: Data, T: dict):
    rows = [(m, T["heldout"][m]) for m in MODEL_KO]
    fig, ax = plt.subplots(figsize=(FIG_W, 4.8))
    fig.subplots_adjust(top=0.78, left=0.36, right=0.93, bottom=0.34)
    for i, (m, v) in enumerate(rows):
        yy = len(rows) - 1 - i
        col = HELD if m != "LINEAR" else MUTED
        ax.plot([v["all"], v["min3"]], [yy, yy], color=BASE, lw=1.6, zorder=2)
        ax.plot(v["all"], yy, "s", markersize=9.5, color=MUTED, markeredgecolor=SURFACE, markeredgewidth=2, zorder=3)
        ax.plot(v["min2"], yy, "o", markersize=10, markerfacecolor=SURFACE, markeredgecolor=col, markeredgewidth=2, zorder=4)
        ax.plot(v["min3"], yy, "o", markersize=10, color=col, markeredgecolor=SURFACE, markeredgewidth=2, zorder=5)
        ax.text(v["min3"] + 0.02, yy, f"{v['min3']:.2f}", va="center", ha="left", fontsize=9.8, color=INK, bbox=LBL, zorder=6)
        ax.text(v["all"] - 0.02, yy, f"{v['all']:.2f}", va="center", ha="right", fontsize=9.8, color=INK2, bbox=LBL, zorder=6)
    ax.set_yticks(range(len(rows)))
    ax.set_yticklabels([(f"{MODEL_KO[m]} ({m})" if m != "LINEAR" else MODEL_KO[m]) for m, _ in rows][::-1])
    ax.set_xlim(0.38, 1.07)
    ax.set_ylim(-0.6, len(rows) - 0.4)
    ax.set_xlabel("같은 도구 안 AUROC")
    ax.grid(axis="y", visible=False)
    PP.ref_line(ax, x=0.5, label="우연")
    PP.ref_line(ax, x=0.9, label="목표 0.90")
    ax.legend(handles=[handle(HELD, f"근거가 보인 위반, 칸에 3개 이상 (16개 · 서로 다른 입력 {D.d3}개 · 칸 4개)", line=False),
                       handle(HELD, f"근거가 보인 위반, 칸에 2개 이상 (22개 · 서로 다른 입력 {D.d2}개 · 칸 7개)", line=False, hollow=True),
                       handle(MUTED, "위반 전체 (48개 · 칸 9개)", marker="s", line=False)],
              loc="upper center", bbox_to_anchor=(0.22, -0.20), ncol=1, handletextpad=0.3, labelspacing=0.35, fontsize=9.3)
    PP.title(fig, f"{T['heldout'][D.sel]['min3']:.2f}은 '근거가 보인 위반'에 대한 점수다 — 위반 전체로 재면 {T['heldout'][D.sel]['all']:.2f} 근처",
             f"{HELD_KO} · 같은 점수를 채점 대상만 바꿔 다시 잰 값. 오른쪽 숫자 = 주 지표, 왼쪽 숫자 = 위반 전체")
    PP.note(fig, "같은 hidden state가 여러 실행에 복제돼 있어 위반 수보다 서로 다른 입력 수가 적다")
    PP.save(fig, OUT, "06_채점_대상에_따른_점수.png")


def fig07_detection(D: Data, P: dict):
    fas = (0.01, 0.05, 0.10)
    fig, ax = plt.subplots(figsize=(7.4, 5.0))
    fig.subplots_adjust(top=0.78, left=0.10, right=0.97, bottom=0.22)
    w = 0.16
    table = {}
    for j, (k, col, nm) in enumerate((("A", HELD, HELD_KO), ("C", TRAIN, TRAIN_KO))):
        vals = [op_point(P[k], P["y"], fa)["recall"] * 100 for fa in fas]
        table[k] = vals
        xs = np.arange(len(fas)) + (j - 0.5) * (w + 0.03)
        ax.bar(xs, vals, width=w, color=col, edgecolor=SURFACE, linewidth=1.5, zorder=3, label=nm)
        for x, v in zip(xs, vals):
            ax.text(x, v + 1.5, f"{v:.0f}%", ha="center", va="bottom", fontsize=9.3, color=INK2)
    ax.set_xticks(range(len(fas)))
    ax.set_xticklabels([f"오경보 {int(f * 100)}% 허용" for f in fas])
    ax.set_ylabel(f"탐지율 (근거가 보인 위반 {int(P['y'].sum())}개 중, %)")
    ax.set_ylim(0, 112)
    ax.set_yticks([0, 25, 50, 75, 100])
    ax.grid(axis="x", visible=False)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncol=2, handlelength=1.2, columnspacing=1.6)
    PP.title(fig, f"오경보를 고정했을 때의 탐지율 — {D.sel_ko}",
             "정상 호출의 1%·5%·10%만 잘못 경보하도록 문턱을 잡았을 때, 근거가 보인 위반 중 몇 %를 잡는가")
    PP.note(fig, f"모든 도구에 문턱 하나를 적용 · 정상 {int((P['y'] == 0).sum()):,}개와 근거가 보인 위반 {int(P['y'].sum())}개만 계산(근거가 보이지 않은 위반 {P['hidden']}개는 뺌)")
    PP.save(fig, OUT, "07_오경보_고정_탐지율.png")
    return table


def fig08_confusion(D: Data, P: dict, fa=0.05):
    fig, axes = plt.subplots(1, 2, figsize=(6.6, 3.9))
    fig.subplots_adjust(top=0.68, left=0.16, right=0.97, bottom=0.13, wspace=0.52)
    out = {}
    for ax, (k, nm) in zip(axes, (("A", HELD_KO), ("C", TRAIN_KO))):
        o = op_point(P[k], P["y"], fa)
        out[k] = o
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
    PP.title(fig, "혼동 행렬 (정상의 5%만 오경보하도록 문턱을 잡았을 때)", f"{D.sel_ko} · 모든 도구에 문턱 하나")
    PP.note(fig, f"칸 안: 건수와 그 행에서의 비율 · '실제 위반' = 근거가 보인 위반 {int(P['y'].sum())}개")
    PP.save(fig, OUT, "08_혼동_행렬.png")
    return out


def fig09_threshold(D: Data, P: dict):
    fig, axes = plt.subplots(1, 2, figsize=(FIG_W, 4.4), sharey=True)
    fig.subplots_adjust(top=0.72, left=0.08, right=0.97, bottom=0.26, wspace=0.10)
    styles = {"재현율": "-", "정밀도": (0, (5, 2)), "F1": (0, (1, 1.6))}
    fa = np.concatenate([np.linspace(0.0005, 0.01, 40), np.linspace(0.0105, 0.20, 160)])
    for ax, (k, col, nm) in zip(axes, (("A", HELD, HELD_KO), ("C", TRAIN, TRAIN_KO))):
        rec, pre, f1 = [], [], []
        for f in fa:
            o = op_point(P[k], P["y"], f)
            r, p = o["recall"], o["precision"]
            rec.append(r)
            pre.append(p)
            f1.append(0 if p + r == 0 else 2 * p * r / (p + r))
        for name, v in (("재현율", rec), ("정밀도", pre), ("F1", f1)):
            ax.plot(fa * 100, v, color=col, lw=2, ls=styles[name])
        ax.set_xscale("log")
        ax.set_xlim(0.05, 20)
        ax.set_xticks([0.1, 0.5, 1, 5, 10, 20])
        ax.set_xticklabels(["0.1", "0.5", "1", "5", "10", "20"])
        ax.minorticks_off()
        ax.set_ylim(0, 1.02)
        ax.set_xlabel("허용한 오경보율 (정상 호출 중 경보 비율, %, 로그 눈금)")
        ax.set_title(nm, fontsize=10.3, color=INK, pad=6)
    axes[0].set_ylabel("값")
    fig.legend(handles=[Line2D([0], [0], color=INK2, lw=2, ls=ls, label=n) for n, ls in styles.items()],
               loc="lower center", bbox_to_anchor=(0.5, 0.02), ncol=3, handlelength=2.6, columnspacing=2.0)
    PP.title(fig, f"문턱에 따른 재현율·정밀도·F1 — {D.sel_ko}", "문턱을 느슨하게(오경보를 더 허용) 할수록 재현율은 오르고 정밀도는 내려간다. 선 모양으로 구분")
    PP.save(fig, OUT, "09_문턱별_재현율_정밀도.png")


def fig10_pr(D: Data, P: dict):
    from sklearn.metrics import average_precision_score, precision_recall_curve
    prev = float(P["y"].mean())
    fig, ax = plt.subplots(figsize=(7.6, 5.4))
    fig.subplots_adjust(top=0.80, left=0.11, right=0.84, bottom=0.14)
    ap = {}
    for k, col, nm in (("C", TRAIN, TRAIN_KO), ("A", HELD, HELD_KO)):
        p, r, _ = precision_recall_curve(P["y"], P[k])
        ap[k] = float(average_precision_score(P["y"], P[k]))
        ax.plot(r, p, color=col, lw=2, label=f"{nm}  평균 정밀도 {ap[k]:.2f}")
    PP.ref_line(ax, y=prev, label=f"아무렇게나 찍을 때 {prev * 100:.2f}%")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1.02)
    ax.set_xlabel("재현율 (근거가 보인 위반 중 잡은 비율)")
    ax.set_ylabel("정밀도 (경보 중 진짜 위반 비율)")
    hh, ll = ax.get_legend_handles_labels()
    ax.legend(hh[::-1], ll[::-1], loc="upper right", bbox_to_anchor=(0.97, 0.90), handlelength=1.6)
    PP.title(fig, f"정밀도-재현율 곡선 — {D.sel_ko}",
             f"정상 {int((P['y'] == 0).sum()):,}개와 근거가 보인 위반 {int(P['y'].sum())}개를 도구 구분 없이 섞어 본 값")
    PP.note(fig, "위반이 매우 드물어(0.24%) 정밀도가 낮게 나온다 · 도구를 섞어 잰 값이라 같은 도구 안 AUROC와 직접 비교하지 않는다")
    PP.save(fig, OUT, "10_정밀도_재현율_곡선.png")
    return ap


# ---- epoch figures (record written by argus_v_em_epochs.py)

def _ep(D, m, key):
    return np.asarray(D.hist["models"][m]["per_epoch"][key], dtype=np.float64)


def _end_labels(ax, x, items, gap):
    """Right-edge value labels, nudged apart when they would touch (text only; the marks stay)."""
    items = sorted(items, key=lambda t: t[0])
    pos = [v for v, _, _ in items]
    for i in range(1, len(pos)):
        if pos[i] - pos[i - 1] < gap:
            pos[i] = pos[i - 1] + gap
    for (v, text, col), p in zip(items, pos):
        ax.text(x, p, text, va="center", ha="left", fontsize=9.3, color=INK2, clip_on=False)


def _mark_base_stop(ax, D, label=True):
    """On a longer run, mark the epoch where the base model (Argus-V-em, 60 epochs) stopped."""
    if D.N <= 60:
        return
    ax.axvline(60, color=MUTED, lw=1.0, ls=(0, (4, 3)), zorder=1)
    if label:
        ax.text(60, 1.012, "Argus-V-em은 여기서 멈춤(60)", transform=ax.get_xaxis_transform(), ha="center", va="bottom", fontsize=8.8, color=INK2)


def fig11_epoch_loss(D: Data):
    ep = np.arange(1, D.hist["epochs"] + 1)
    tr, ho = _ep(D, D.sel, "loss_train_eval").mean(1), _ep(D, D.sel, "loss_heldout").mean(1)     # [seed][epoch]
    tr_m, ho_m = tr.mean(0), ho.mean(0)
    fig, ax = plt.subplots(figsize=(FIG_W, 5.2))
    fig.subplots_adjust(top=0.79, left=0.09, right=0.88, bottom=0.20)
    for arr, mean, col in ((tr, tr_m, TRAIN), (ho, ho_m, HELD)):
        for s in arr:
            ax.plot(ep, s, color=col, lw=1.0, alpha=0.45, zorder=3)
        ax.plot(ep, mean, color=col, lw=2.3, zorder=4)
    ax.set_yscale("log")
    yt = [0.05, 0.1, 0.2, 0.5] if D.N <= 60 else [0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5]
    ax.set_yticks(yt)
    ax.set_yticklabels([f"{v:g}" for v in yt])
    ax.minorticks_off()
    ax.set_xlim(1, len(ep))
    ax.set_xticks(D.ticks)
    ax.set_xlabel("epoch (전체 학습 행을 한 번 본 횟수)")
    ax.set_ylabel("손실 (로그 눈금, 낮을수록 좋음)")
    f2 = lambda v: f"{v:.2f}" if v >= 0.01 else f"{v:.3f}"     # noqa: E731  (small losses keep a digit)
    _end_labels(ax, len(ep) + (0.8 if D.N <= 60 else 4), [(tr_m[-1], f2(tr_m[-1]), TRAIN), (ho_m[-1], f2(ho_m[-1]), HELD)], 0)
    ax.legend(handles=[handle(TRAIN, "학습에 쓴 행", marker=None), handle(HELD, "처음 보는 시나리오 (학습에서 뺀 묶음)", marker=None)],
              loc="upper center", bbox_to_anchor=(0.5, -0.13), ncol=2, handlelength=1.8, columnspacing=2.0)
    _mark_base_stop(ax, D)
    low = int(ho_m.argmin()) + 1
    if low < len(ep) - 1 and ho_m[-1] > 1.15 * ho_m.min():
        tail = f"{low} epoch 뒤로 다시 오른다"
    elif low < len(ep) - 1:
        tail = f"{low} epoch 뒤로는 내려가지 않는다"
    elif 1 - ho_m[-1] / ho_m[-11] < 0.03:
        tail = "마지막 10 epoch 동안 거의 그대로다"
    else:
        tail = "끝까지 내려가지만 더 느리다"
    PP.title(fig, f"epoch별 손실 — {D.sel_ko}",
             f"학습 행의 손실은 계속 내려가고, 처음 보는 시나리오의 손실은 {tail} ({D.N} epoch 뒤 {f2(tr_m[-1])} 대 {f2(ho_m[-1])})")
    PP.note(fig, f"굵은 선 = 데이터 나누기 3가지 평균, 가는 선 = 나누기 하나 · 손실 = 학습에 쓴 가중 이진 교차 엔트로피(평가 모드) · {D.N} epoch 고정")
    PP.save(fig, OUT, "11_epoch별_손실.png")


def fig12_epoch_auroc(D: Data):
    ep = np.arange(1, D.hist["epochs"] + 1)
    tr = np.nanmean(_ep(D, D.sel, "auroc_train_min3").reshape(-1, len(ep)), 0)
    ho = _ep(D, D.sel, "auroc_heldout_min3")
    ho_m = ho.mean(0)
    allv = _ep(D, D.sel, "auroc_heldout_all").mean(0)
    fin = np.asarray(D.fin_hist["per_epoch"]["auroc_insample_min3"])
    fig, ax = plt.subplots(figsize=(FIG_W, 5.9))
    fig.subplots_adjust(top=0.81, left=0.09, right=0.88, bottom=0.27)
    ax.plot(ep, allv, color=MUTED, lw=1.6, zorder=2)
    for s in ho:
        ax.plot(ep, s, color=HELD, lw=1.0, alpha=0.45, zorder=3)
    ax.plot(ep, tr, color=TRAIN, lw=2.2, zorder=4)
    ax.plot(ep, fin, color=TRAIN, lw=1.6, ls=(0, (5, 2)), zorder=4)
    ax.plot(ep, ho_m, color=HELD, lw=2.4, zorder=5)
    ax.set_xlim(1, len(ep))
    ax.set_xticks(D.ticks)
    ax.set_ylim(0.38, 1.03)
    ax.set_xlabel("epoch (전체 학습 행을 한 번 본 횟수)")
    ax.set_ylabel("같은 도구 안 AUROC")
    ax.axhline(0.9, color=MUTED, lw=1.0, ls=(0, (4, 3)), zorder=1)
    ax.axhline(0.5, color=MUTED, lw=1.0, ls=(0, (4, 3)), zorder=1)
    lx = 1.6 if D.N <= 60 else len(ep) * 0.80           # on a long run the left edge is crowded
    ax.text(lx, 0.905, "목표 0.90", va="bottom", ha="left", fontsize=9, color=INK2)
    ax.text(lx, 0.445, "우연 0.5", va="bottom", ha="left", fontsize=9, color=INK2)
    _end_labels(ax, len(ep) + (0.8 if D.N <= 60 else 4), [(tr[-1], f"{tr[-1]:.2f}", TRAIN), (ho_m[-1], f"{ho_m[-1]:.2f}", HELD), (allv[-1], f"{allv[-1]:.2f}", MUTED)], 0.035)
    ax.legend(handles=[handle(TRAIN, "학습에 쓴 행 (학습 15번 평균)", marker=None),
                       handle(TRAIN, "전체 데이터로 맞춘 최종 모델의 학습 행", marker=None, ls=(0, (5, 2))),
                       handle(HELD, "처음 보는 시나리오 (굵은 선 평균, 가는 선 나누기 하나)", marker=None),
                       handle(MUTED, "처음 보는 시나리오를 위반 전체로 채점했을 때", marker=None)],
              loc="upper center", bbox_to_anchor=(0.5, -0.13), ncol=2, handlelength=2.2, labelspacing=0.35, columnspacing=1.6, fontsize=9.3)
    _mark_base_stop(ax, D)
    one = int(np.argmax(tr >= 0.9995)) + 1 if (tr >= 0.9995).any() else None
    ninety = int(np.argmax(ho_m >= 0.90)) + 1 if (ho_m >= 0.90).any() else None
    best = int(ho_m.argmax()) + 1
    if best < len(ep) - 10:                      # the curve turned down before the end
        sub = f"처음 보는 시나리오의 점수가 가장 높은 곳은 {best} epoch({ho_m.max():.3f})이고, {D.N} epoch의 값은 {ho_m[-1]:.3f}이다"
    else:
        sub = (f"학습에 쓴 행은 {one} epoch에 1.00에 닿고, " if one else "") + (f"처음 보는 시나리오는 {ninety} epoch에 0.90을 넘는다" if ninety else "처음 보는 시나리오는 0.90에 닿지 않는다")
    PP.title(fig, f"epoch별 성능 — {D.sel_ko}", sub)
    PP.note(fig, f"근거가 보인 위반 16개(서로 다른 입력 {D.d3}개, 도구 4개)만 채점 · {D.N} epoch 고정, 이 곡선으로 epoch 수를 고르지 않았다 · 개발용으로 이미 쓴 행")
    PP.save(fig, OUT, "12_epoch별_성능.png")


def fig13_epoch_models(D: Data):
    ep = np.arange(1, D.hist["epochs"] + 1)
    fig, axes = plt.subplots(2, 4, figsize=(FIG_W + 2.6, 6.6), sharex=True, sharey="row")
    fig.subplots_adjust(top=0.81, left=0.07, right=0.985, bottom=0.16, hspace=0.20, wspace=0.10)
    for j, m in enumerate(MODEL_KO):
        a_tr = np.nanmean(_ep(D, m, "auroc_train_min3").reshape(-1, len(ep)), 0)
        a_ho = _ep(D, m, "auroc_heldout_min3").mean(0)
        l_tr = _ep(D, m, "loss_train_eval").reshape(-1, len(ep)).mean(0)
        l_ho = _ep(D, m, "loss_heldout").reshape(-1, len(ep)).mean(0)
        ax = axes[0, j]
        ax.axhline(0.9, color=MUTED, lw=1.0, ls=(0, (4, 3)), zorder=1)
        ax.plot(ep, a_tr, color=TRAIN, lw=2)
        ax.plot(ep, a_ho, color=HELD, lw=2)
        ax.set_ylim(0.38, 1.03)
        ax.set_title(f"{MODEL_SHORT[m]}" + ("  ◀ 선택" if m == D.selected else "") + f"\n{D.N} epoch 뒤 {a_ho[-1]:.2f}", fontsize=10.2,
                     fontweight="normal", color=INK, pad=6)
        ax = axes[1, j]
        ax.plot(ep, l_tr, color=TRAIN, lw=2)
        ax.plot(ep, l_ho, color=HELD, lw=2)
        ax.set_yscale("log")
        yt = [0.02, 0.05, 0.1, 0.2, 0.5] if D.N <= 60 else [0.001, 0.003, 0.01, 0.03, 0.1, 0.3]
        ax.set_yticks(yt)
        ax.set_yticklabels([f"{v:g}" for v in yt])
        ax.minorticks_off()
        _mark_base_stop(ax, D, label=False)
        _mark_base_stop(axes[0, j], D, label=False)
        ax.set_xticks(D.ticks_small)
        ax.set_xlim(1, len(ep))
        ax.set_xlabel("epoch")
    axes[0, 0].set_ylabel("같은 도구 안 AUROC")
    axes[1, 0].set_ylabel("손실 (로그 눈금)")
    axes[0, -1].text(1.02, 0.9, "0.90", transform=axes[0, -1].get_yaxis_transform(), va="center", ha="left", fontsize=9, color=INK2)
    fig.legend(handles=[handle(TRAIN, "학습에 쓴 행", marker=None), handle(HELD, "처음 보는 시나리오", marker=None)],
               loc="lower center", bbox_to_anchor=(0.5, 0.03), ncol=2, handlelength=1.8, columnspacing=2.0)
    PP.title(fig, "모델별 epoch 곡선 — 임베딩 폭 3가지와 선형 대조", "위: 근거가 보인 위반의 같은 도구 안 AUROC, 아래: 손실. 선은 학습 15번(묶음 5개 × 나누기 3가지)의 평균")
    PP.save(fig, OUT, "13_모델별_epoch_곡선.png")


def fig14_epoch_cells(D: Data):
    ep = np.arange(1, D.hist["epochs"] + 1)
    cells = D.hist["cells_min3"]
    arr = _ep(D, D.sel, "cell_auroc_heldout")              # [seed][epoch][cell]
    fig, axes = plt.subplots(1, 4, figsize=(FIG_W + 2.6, 4.5), sharex=True, sharey=True)
    fig.subplots_adjust(top=0.66, left=0.07, right=0.985, bottom=0.21, wspace=0.10)
    for j, (ax, cell) in enumerate(zip(axes, cells)):
        ax.axhline(0.5, color=MUTED, lw=1.0, ls=(0, (4, 3)), zorder=1)
        for s in range(arr.shape[0]):
            ax.plot(ep, arr[s, :, j], color=HELD, lw=1.0, alpha=0.45)
        ax.plot(ep, arr[:, :, j].mean(0), color=HELD, lw=2.2)
        p, n = D.counts[cell]
        ax.set_title(f"{short(cell)}\n위반 {p} [입력 {D.dpos[cell]}] · 정상 {n} · 비교 쌍 {p * n}\n{D.N} epoch 뒤 {arr[:, -1, j].mean():.2f}",
                     fontsize=9.6, fontweight="normal", color=INK, pad=6)
        ax.set_xticks(D.ticks_small)
        ax.set_xlim(1, len(ep))
        ax.set_ylim(0.0, 1.04)
        ax.set_xlabel("epoch")
        _mark_base_stop(ax, D, label=False)
    axes[0].set_ylabel("칸 안 AUROC")
    PP.title(fig, f"도구 칸별 epoch 곡선 — {D.sel_ko}, 처음 보는 시나리오", "굵은 선 = 나누기 3가지 평균, 가는 선 = 나누기 하나. 주 지표에 들어가는 칸 4개")
    PP.note(fig, "[입력 n] = 위반 중 서로 다른 hidden state 수 · 비교 쌍이 9개인 칸은 쌍 하나가 뒤집힐 때마다 0.11씩 움직인다")
    PP.save(fig, OUT, "14_칸별_epoch_곡선.png")


# ------------------------------------------------------------------------------------------------ main

def main(argv):
    global TRACK, OUT
    if "--track" in argv:
        TRACK = TRACKS[argv[argv.index("--track") + 1]]
        OUT = TRACK["report"] / "figures"
    font = PP.setup()
    D = Data()
    print("font", font, "| selected", D.selected, "| cells", [short(c) for c in D.cells3], "+", [short(c) for c in D.cells2 if c not in D.cells3])
    T = {"heldout": {}, "cells": {}}
    everything = np.ones(D.cx.n, dtype=bool)
    for m in MODEL_KO:
        key = D.lin if m == "LINEAR" else D.res["architectures"][m]
        mine3 = D.per_seed(D.oof[m], D.mask3, 3)
        assert np.allclose(mine3, key["visible_min3"]["per_seed"], atol=1e-9), (m, mine3)
        min2 = D.per_seed(D.oof[m], D.mask2, 2)
        if m != "LINEAR":
            assert np.allclose(min2, key["visible_min2"]["per_seed"], atol=1e-9), (m, min2)
        allv = [float(EM.score_metric(D.cx, s, everything, 3)["value"]) for s in D.oof[m]]
        T["heldout"][m] = {"min3": float(np.mean(mine3)), "min3_seeds": mine3, "min2": float(np.mean(min2)), "min2_seeds": min2,
                           "all": float(np.mean(allv)), "all_seeds": allv}
    T["insample_min3"] = float(D.wt(D.ins, D.mask3, 3)["value"])
    T["insample_min2"] = float(D.wt(D.ins, D.mask2, 2)["value"])
    T["insample_all"] = float(EM.score_metric(D.cx, D.ins, everything, 3)["value"])
    for cell in D.cells2:
        seeds = [D.cell_auc(s, cell) for s in D.oof[D.sel]]
        T["cells"][cell] = {"heldout": float(np.mean(seeds)), "heldout_seeds": seeds, "insample": D.cell_auc(D.ins, cell)}
    T["ci_sel"] = D.family_ci(D.oof[D.sel], D.mask3, 3)
    P = {"y": D.yv[D.target], "A": D.oof_mean[D.sel][D.target], "C": D.ins[D.target],
         "hidden": int(((D.cx.y == 1) & ~D.vis).sum())}

    fig01_models(D, T)
    fig02_roc(D, T)
    fig03_roc_cells(D, T)
    fig04_cells(D, T)
    fig05_scores(D)
    fig06_scope(D, T)
    det = fig07_detection(D, P)
    conf = fig08_confusion(D, P)
    fig09_threshold(D, P)
    ap = fig10_pr(D, P)
    if D.hist:
        fig11_epoch_loss(D)
        fig12_epoch_auroc(D)
        fig13_epoch_models(D)
        fig14_epoch_cells(D)

    # table twin of the figures
    L = ["# 그래프에 쓴 숫자 — Argus-V-em", "",
         f"지표는 같은 도구 안 AUROC. 채점 대상은 정상 호출과 '행동 전에 근거가 보인 위반'(표시 규칙 {D.rule}).",
         f"'{HELD_KO}' = train 분할 안에서 시나리오 계열 5묶음 중 학습에서 뺀 묶음을 채점(교차검증), 데이터 나누기 3가지 평균. '{TRAIN_KO}' = 저장된 최종 {D.sel_ko}이 자기가 학습한 행을 채점.",
         "**따로 나눠 둔 validation·test 분할은 한 번도 열지 않았다.** 아래 숫자는 모두 train 분할 안에서 나온 값이다.",
         "같은 학습 분할 행을 다시 쓴 개발용 점수이며 새 시나리오로 확인한 값이 아니다.", "",
         "## 모델별 점수 (그림 01·02·06)", "",
         "| 모델 | 근거가 보인 위반, 칸에 3개 이상 (16개·칸 4개) | 나누기별 | 95% 구간 | 칸에 2개 이상 (22개·칸 7개) | 위반 전체 (48개·칸 9개) |", "|---|---|---|---|---|---|"]
    for r in T["models"]:
        k = r["key"]
        ci = f"{r['ci'][0]:.3f}–{r['ci'][1]:.3f}" if r["ci"] else "—"
        runs = " / ".join(f"{v:.3f}" for v in r["runs"])
        if k in T["heldout"]:
            L.append(f"| {r['label'].replace('  ◀ 선택', ' (선택)')} | {r['mean']:.3f} | {runs} | {ci} | {T['heldout'][k]['min2']:.3f} | {T['heldout'][k]['all']:.3f} |")
        else:
            L.append(f"| {r['label']} | {r['mean']:.3f} | {runs} | {ci} | — | — |")
    L += [f"| {MODEL_SHORT[D.sel]} 최종 모델 · {TRAIN_KO} | {T['insample_min3']:.3f} | — | — | {T['insample_min2']:.3f} | {T['insample_all']:.3f} |", "",
          f"95% 구간은 시나리오 계열을 복원 추출로 다시 뽑아 계산(2,000회, 주 지표 칸에 걸친 계열 {T['ci_sel'][3]}개). 위반이 16개뿐이라 넓다.", "",
          f"## 도구 칸별 AUROC, {D.sel_ko} (그림 03·04)", "", f"| 칸 | 근거가 보인 위반 | 정상 | {HELD_KO} | 나누기별 | {TRAIN_KO} | 주 지표 |", "|---|---|---|---|---|---|---|"]
    for cell in sorted(T["cells"], key=lambda c: -T["cells"][c]["heldout"]):
        c = T["cells"][cell]
        L.append(f"| {short(cell)} | {D.counts[cell][0]} | {D.counts[cell][1]} | {c['heldout']:.3f} | {' / '.join(f'{v:.3f}' for v in c['heldout_seeds'])} | {c['insample']:.3f} | {'포함' if D.counts[cell][0] >= 3 else '보조'} |")
    ded3 = [EM.score_metric(D.cx, s, D.mask3 & D.distinct, 3) for s in D.oof[D.sel]]
    ded2 = [EM.score_metric(D.cx, s, D.mask2 & D.distinct, 2) for s in D.oof[D.sel]]
    L += ["", f"## 복제된 입력을 하나로 치면, {D.sel_ko}", "",
          "같은 hidden state가 여러 실행에 복제돼 있다(같은 앞부분이 다른 실행에서 다시 재생됨). 칸마다 입력과 라벨이 같은 행을 하나만 남기고 다시 잰 값이다.", "",
          "| 기준 | 모든 행 | 서로 다른 입력만 |", "|---|---|---|",
          f"| 칸에 위반 3개 이상 | {T['heldout'][D.sel]['min3']:.3f} (위반 16개 · 칸 4개) | {np.mean([r['value'] for r in ded3]):.3f} (위반 {ded3[0]['n_positives_included']}개 · 칸 {ded3[0]['n_tools']}개) |",
          f"| 칸에 위반 2개 이상 | {T['heldout'][D.sel]['min2']:.3f} (위반 22개 · 칸 7개) | {np.mean([r['value'] for r in ded2]):.3f} (위반 {ded2[0]['n_positives_included']}개 · 칸 {ded2[0]['n_tools']}개) |", "",
          "| 칸 | 근거가 보인 위반 | 그중 서로 다른 입력 | 정상 | 비교 쌍 |", "|---|---|---|---|---|"]
    for cell in D.cells2:
        L.append(f"| {short(cell)} | {D.counts[cell][0]} | {D.dpos[cell]} | {D.counts[cell][1]} | {D.counts[cell][0] * D.counts[cell][1]} |")
    L += ["", f"주 지표의 위반 16개는 서로 다른 입력 {D.d3}개, 근거가 보인 위반 22개 전체는 {D.d2}개다. 학습 묶음과 검증 묶음 사이에 같은 입력·같은 시나리오가 겹치는 경우는 없다(`argus_v_em_heldout_check.py`)."]
    L += ["", f"## 문턱 하나를 모든 도구에 적용했을 때, {D.sel_ko} (그림 07·08·10)", "",
          f"정상 {int((P['y'] == 0).sum()):,}개와 근거가 보인 위반 {int(P['y'].sum())}개만 계산(근거가 보이지 않은 위반 {P['hidden']}개는 뺌). 점수는 세 번 나누기의 평균.", "",
          "| 대상 | 탐지율: 오경보 1% | 5% | 10% | 평균 정밀도 | 전체 AUROC(도구 섞음) |", "|---|---|---|---|---|---|"]
    for k, nm in (("A", HELD_KO), ("C", TRAIN_KO)):
        L.append(f"| {nm} | {det[k][0]:.1f}% | {det[k][1]:.1f}% | {det[k][2]:.1f}% | {ap[k]:.3f} | {H.auroc(P[k], P['y']):.3f} |")
    L += ["", "| 혼동 행렬(오경보 5% 문턱) | 위반을 경보 | 위반을 놓침 | 정상을 경보 | 정상에 경보 없음 | 정밀도 |", "|---|---|---|---|---|---|"]
    for k, nm in (("A", HELD_KO), ("C", TRAIN_KO)):
        o = conf[k]
        L.append(f"| {nm} | {o['tp']} | {o['fn']} | {o['fp']} | {o['tn']:,} | {o['precision'] * 100:.1f}% |")
    if D.hist:
        h = D.hist
        if "base" not in TRACK:
            L += ["", "## epoch별 기록 (그림 11~14)", "",
                  "round 01 학습을 설정 그대로 다시 돌리며 epoch마다 기록한 값(`addendum-2.md`). 마지막 epoch의 점수와 저장된 점수의 최대 차이:", ""]
            for m in MODEL_KO:
                L.append(f"- {MODEL_KO[m]}: {max(h['models'][m]['max_abs_diff_vs_saved_oof_per_seed']):.2e}")
            L += [f"- 전체 데이터로 맞춘 최종 {D.sel_ko}: 점수 {h['final_EM32']['max_abs_diff_vs_saved_checkpoint']:.2e}, 가중치 {h['final_EM32']['max_abs_weight_diff_vs_saved_checkpoint']:.2e}", ""]
        else:
            L += ["", "## epoch별 기록 (그림 11~14)", "",
                  f"{TRACK['name']} 학습 중 epoch마다 기록한 값. 이 학습의 60 epoch 시점 점수와 저장된 {TRACKS[TRACK['base']]['name']} 점수의 최대 차이"
                  "(0이면 같은 학습을 더 길게 돌린 것이다):", ""]
            for m in MODEL_KO:
                src = D.lin if m == "LINEAR" else D.res["architectures"][m]
                L.append(f"- {MODEL_KO[m]}: {max(src['epoch60_max_abs_diff_vs_argus_v_em']):.2e}")
            d60 = D.fin_hist.get("epoch60_max_abs_diff_vs_argus_v_em_checkpoint")
            L += [f"- 전체 데이터로 맞춘 최종 {D.sel_ko}: " + ("비교 대상 없음(선택된 폭이 다름)" if d60 is None else f"{d60:.2e}"), ""]
        L += ["손실은 학습에 쓴 가중 이진 교차 엔트로피를 평가 모드로 계산한 값, AUROC는 근거가 보인 위반(칸에 3개 이상) 기준. 학습 15번(묶음 5개 × 나누기 3가지) 평균.", ""]
        npz = TRACK["out"] / "epochs" / f"{D.sel}.npz"
        if npz.is_file():                                          # per-epoch held-out scores of every row (ignored artifact)
            oof_e = np.load(npz)["oof"].astype(np.float64)         # [seed][epoch][row]
            tr3 = np.nanmean(_ep(D, D.sel, "auroc_train_min3").reshape(-1, h["epochs"]), 0)

            def at(mask, mp, e):
                return float(np.mean([EM.score_metric(D.cx, oof_e[s, e - 1], mask, mp)["value"] for s in range(oof_e.shape[0])]))

            marks = D.marks
            L += [f"### {D.sel_ko}: 검증 AUROC가 epoch에 따라 오르는가", "",
                  "여기서 '검증'은 train 분할 안에서 학습에서 뺀 시나리오 묶음을 채점한 값(교차검증)이다. 따로 나눠 둔 validation·test 분할은 열지 않았다.",
                  "1 epoch = 가중치를 한 번 고치는 것(전체 행을 한꺼번에 넣어 학습). 같은 검증 점수를 채점 대상만 바꿔 다시 잰 값.", "",
                  "| epoch | 학습에 쓴 행 | 검증: 주 지표(칸에 3개 이상) | 검증: 칸에 2개 이상 | 검증: 2개 이상, 복제를 하나로 침 | 검증: 위반 전체 |", "|---|---|---|---|---|---|"]
            for e in marks:
                L.append(f"| {e} | {tr3[e - 1]:.3f} | {at(D.mask3, 3, e):.3f} | {at(D.mask2, 2, e):.3f} | {at(D.mask2 & D.distinct, 2, e):.3f} | {at(everything, 3, e):.3f} |")
            L += ["", "같은 도구를 쓴 호출끼리 위반과 정상을 비교한 값(칸 안 AUROC), 칸별:", "",
                  "| 칸 | " + " | ".join(f"{e} epoch" for e in marks) + " | 주 지표 |", "|---|" + "---|" * (len(marks) + 1)]
            for cell in sorted(D.cells2, key=lambda c: (-(D.counts[c][0] >= 3), c)):
                m = D.target & (D.cx.groups == cell)
                vals = [float(np.mean([H.auroc(oof_e[s, e - 1][m], D.yv[m]) for s in range(oof_e.shape[0])])) for e in marks]
                L.append(f"| {short(cell)} | " + " | ".join(f"{v:.2f}" for v in vals) + f" | {'포함' if D.counts[cell][0] >= 3 else '보조'} |")
            L.append("")
        ca = _ep(D, D.sel, "cell_auroc_heldout").mean(0)          # [epoch][cell]
        tot = _ep(D, D.sel, "auroc_heldout_min3").mean(0)
        npos = sum(D.counts[c][0] for c in h["cells_min3"])
        ea, eb = D.span
        L += [f"### {D.sel_ko}: {ea} epoch에서 {eb} epoch 사이에 바뀐 것", "",
              f"전체 {tot[ea - 1]:.3f} → {tot[eb - 1]:.3f}. 칸별로 나누면:", "",
              f"| 칸 | 비교 쌍 | {ea} epoch | {eb} epoch | 바뀐 쌍 수 | 전체 점수에 준 변화 |", "|---|---|---|---|---|---|"]
        for k, c in enumerate(h["cells_min3"]):
            p, n = D.counts[c]
            d = float(ca[eb - 1, k] - ca[ea - 1, k])
            L.append(f"| {short(c)} | {p * n} | {ca[ea - 1, k]:.3f} | {ca[eb - 1, k]:.3f} | {d * p * n:+.1f} | {d * p / npos:+.3f} |")
        L.append("")
        if D.N > 60:
            best = int(tot.argmax()) + 1
            L += [f"교차검증 주 지표가 가장 높았던 epoch은 {best}({tot.max():.3f})이다. 참고로만 적는다. 보고하는 점수는 {D.N} epoch 시점의 {tot[-1]:.3f}이고, "
                  "가장 높은 epoch을 골라 쓰면 같은 개발용 행으로 고른 값이 된다.", ""]
        for m in MODEL_KO:
            ep_n = h["epochs"]
            a_tr = np.nanmean(_ep(D, m, "auroc_train_min3").reshape(-1, ep_n), 0)
            a_ho = _ep(D, m, "auroc_heldout_min3").mean(0)
            l_tr = _ep(D, m, "loss_train_eval").reshape(-1, ep_n).mean(0)
            l_ho = _ep(D, m, "loss_heldout").reshape(-1, ep_n).mean(0)
            L += [f"### {MODEL_KO[m]}", "", f"| epoch | 손실: 학습에 쓴 행 | 손실: {HELD_KO} | AUROC: 학습에 쓴 행 | AUROC: {HELD_KO} |", "|---|---|---|---|---|"]
            for e in D.marks_fine:
                L.append(f"| {e} | {l_tr[e - 1]:.4f} | {l_ho[e - 1]:.4f} | {a_tr[e - 1]:.3f} | {a_ho[e - 1]:.3f} |")
            L.append("")
    (OUT / "tables.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("saved", (OUT / "tables.md").relative_to(REPO_ROOT))


if __name__ == "__main__":
    main(sys.argv[1:])

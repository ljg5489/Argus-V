"""Complete test read-out of one Argus-V-em model of the new split (resplit-1117 / run01): every visible violation
of the test split is used, not only the ones in tools with three or more. Reads the saved test scores; trains nothing.

User, 2026-11-17: "총 10개중 4개만 사용한거잖아 10개 모두 사용해서 완전한 test를 해봐 Argus-V-em 64차원 60배로".

For the chosen model, epoch and its three repeats:
  * all visible violations vs all normal calls of the test split (and all violations vs all normal calls)
      - tools and periods mixed, with the score of a rule that only knows the collection period beside it
      - inside each collection period
      - inside each tool, for every tool that has at least one such violation and one normal call
  * what is caught at fixed false-alarm rates, and by the model's own decision point (score > 0)
  * every visible violation one by one: where its score falls among the normal calls

Usage: PYTHONUTF8=1 py -3.11 experiments/risk_loop/argus_loop/resplit_run01_full_test.py [--model EM64_w60] [--epoch 67]
Output: reports/risk-loop/resplit-1117/run01/full_test_<model>.json, full_test_<model>.md, figures_full_test/<model>_*.png
"""
from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

for _name in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ.setdefault(_name, "2")

import numpy as np  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from experiments.risk_loop import harness as H  # noqa: E402
from experiments.risk_loop.argus_loop import resplit_run01 as R  # noqa: E402

FA = (0.01, 0.05, 0.10)
PERIOD_KO = {"oct": "10월", "nov": "11월"}
ARCH_KO = {"EM32": "32차원", "EM64": "64차원", "EM128": "128차원", "LINEAR": "선형 대조"}


def load_model(model, epoch):
    """-> (name in Korean, {'validation': [score vectors], 'test': [...]}, extra facts, report folder, figure folder, file stem)."""
    if model == "EMP":
        from experiments.risk_loop.argus_loop import argus_v_emp as AE
        return (AE.NAME_KO, {s: [AE.scores(s, epoch)] for s in ("validation", "test")}, {"definition": AE.describe()},
                AE.REPORT, AE.REPORT / "figures", "")
    arch, wtag = model.split("_")
    Z = [np.load(R.OUT / "em" / f"{model}_r{k}.npz", allow_pickle=False) for k in R.REPEATS]
    return (f"Argus-V-em {ARCH_KO[arch]}, 위반 가중치 {R.WEIGHT_KO[wtag]}",
            {s: [z[f"scores_{s}"][epoch - 1].astype(np.float64) for z in Z] for s in ("validation", "test")},
            {"pos_weight": [float(z["pos_weight"]) for z in Z]}, R.REPORT, R.REPORT / "figures_full_test", f"_{model}")


def scores_at(model, split, e):
    """Score vectors of ``split`` at epoch e (1-based), one per repeat."""
    if model == "EMP":
        from experiments.risk_loop.argus_loop import argus_v_emp as AE
        return [AE.scores(split, e)]
    return [np.load(R.OUT / "em" / f"{model}_r{k}.npz", allow_pickle=False)[f"scores_{split}"][e - 1].astype(np.float64) for k in R.REPEATS]


def auc(s, y):
    y = np.asarray(y)
    return float(H.auroc(np.asarray(s, dtype=np.float64), y)) if 0 < int(y.sum()) < len(y) else float("nan")


def below(s_norm, x):
    """Share of the normal calls scored below x (ties count half)."""
    return float((s_norm < x).mean() + 0.5 * (s_norm == x).mean()) if len(s_norm) else float("nan")


def boot(S, pos, rows_mask, fam, src, within, reps=2000, seed=0):
    """95% interval over scenario families of the AUROC (mean of repeats); within=True averages the two periods by positives."""
    idx = np.flatnonzero(rows_mask)
    f = fam[idx]
    fams = sorted(set(f.tolist()))
    members = [idx[f == x] for x in fams]
    rng = np.random.default_rng(seed)
    vals = []
    for _ in range(reps):
        loc = np.concatenate([members[i] for i in rng.integers(0, len(fams), len(fams))])
        if within:
            num, den = 0.0, 0
            for p in ("oct", "nov"):
                m = loc[src[loc] == p]
                k = int(pos[m].sum())
                if 0 < k < len(m):
                    num += float(np.mean([H.auroc(s[m], pos[m]) for s in S])) * k
                    den += k
            if den:
                vals.append(num / den)
        else:
            k = int(pos[loc].sum())
            if 0 < k < len(loc):
                vals.append(float(np.mean([H.auroc(s[loc], pos[loc]) for s in S])))
    lo, hi = np.percentile(vals, [2.5, 97.5])
    return [float(lo), float(hi)]


def read_out(S, pos, rows_mask, D, te, own=True):
    """One label set (positives = pos, rows = rows_mask) scored every way. S: [repeat][test row]."""
    y, tool, src, fam = D["y"][te], D["tool"][te].astype(str), D["source"][te].astype(str), D["family"][te].astype(str)
    norm = (y == 0) & rows_mask
    lab = pos.astype(np.int64)
    out = {"positives": int(pos.sum()), "normal_calls": int(norm.sum())}
    out["mixed"] = {"auroc": float(np.mean([auc(s[rows_mask], lab[rows_mask]) for s in S])),
                    "per_repeat": [auc(s[rows_mask], lab[rows_mask]) for s in S],
                    "ci95": boot(S, lab, rows_mask, fam, src, within=False),
                    "period_only_rule": auc((src[rows_mask] == "oct").astype(np.float64), lab[rows_mask])}
    per, num, den = {}, 0.0, 0
    for p in ("oct", "nov"):
        m = rows_mask & (src == p)
        k = int(lab[m].sum())
        v = float(np.mean([auc(s[m], lab[m]) for s in S])) if 0 < k < int(m.sum()) else float("nan")
        per[p] = {"positives": k, "normal_calls": int((norm & (src == p)).sum()), "auroc": v,
                  "per_repeat": [auc(s[m], lab[m]) for s in S] if 0 < k < int(m.sum()) else []}
        if not np.isnan(v):
            num, den = num + v * k, den + k
    out["inside_period"] = {"auroc": num / den if den else float("nan"), "by_period": per,
                            "ci95": boot(S, lab, rows_mask, fam, src, within=True)}
    tools, num, den, lonely = [], 0.0, 0, 0
    for t in sorted(set(tool[pos].tolist())):
        v, n = pos & (tool == t), norm & (tool == t)
        if not n.sum():
            lonely += int(v.sum())
            tools.append({"tool": t, "period": str(src[v][0]), "positives": int(v.sum()), "normal_calls": 0, "auroc": None, "pairs": 0})
            continue
        a = float(np.mean([auc(s[v | n], lab[v | n]) for s in S]))
        tools.append({"tool": t, "period": str(src[v][0]), "positives": int(v.sum()), "normal_calls": int(n.sum()), "auroc": a,
                      "pairs": int(v.sum()) * int(n.sum()), "per_repeat": [auc(s[v | n], lab[v | n]) for s in S]})
        num, den = num + a * int(v.sum()), den + int(v.sum())
    out["inside_tool"] = {"auroc_weighted_by_positives": num / den if den else float("nan"), "positives_compared": den,
                          "positives_in_tools_without_a_normal_call": lonely,
                          "pairs": int(sum(t["pairs"] for t in tools)), "tools": sorted(tools, key=lambda t: -t["positives"])}
    ops = {}
    for name, rule in [(f"{int(f * 100)}% false alarms", f) for f in FA] + ([("model decision point (score > 0)", None)] if own else []):
        tp, fp = [], []
        for s in S:
            thr = 0.0 if rule is None else float(np.quantile(s[norm], 1 - rule))
            alarm = s > thr
            tp.append(int((alarm & pos).sum()))
            fp.append(int((alarm & norm).sum()))
        ops[name] = {"caught_per_repeat": tp, "caught_mean": float(np.mean(tp)), "false_alarms_per_repeat": fp,
                     "false_alarms_mean": float(np.mean(fp)), "precision_mean": float(np.mean([a / max(1, a + b) for a, b in zip(tp, fp)]))}
    out["operating_points"] = ops
    return out


def main(argv):
    model = argv[argv.index("--model") + 1] if "--model" in argv else "EM64_w60"
    epoch = int(argv[argv.index("--epoch") + 1]) if "--epoch" in argv else R.FIXED_EPOCH
    D = R.load()
    te = D["idx"]["test"]
    y, vis = D["y"][te], D["vis"][te]
    tool, src = D["tool"][te].astype(str), D["source"][te].astype(str)
    norm = y == 0
    name_ko, SC, extra, report, figdir, stem = load_model(model, epoch)
    S = SC["test"]
    res = {"model": model, "model_ko": name_ko, "epoch": epoch, "repeats": len(S), **extra, "split": "test (resplit-1117)",
           "report_dir": str(report.relative_to(ROOT)).replace("\\", "/"), "figure_dir": str(figdir.relative_to(ROOT)).replace("\\", "/"), "stem": stem,
           "test": {"calls": int(len(te)), "violations": int(y.sum()), "visible_violations": int(vis.sum()), "normal_calls": int(norm.sum())},
           "computed_at": time.strftime("%Y-%m-%d %H:%M:%S"),
           "visible_violations_vs_normal_calls": read_out(S, vis, norm | vis, D, te, own=model != "EMP"),
           "all_violations_vs_normal_calls": read_out(S, y == 1, np.ones(len(te), dtype=bool), D, te, own=model != "EMP")}
    # every visible violation, one by one
    rows = []
    for i in np.flatnonzero(vis):
        same_p, same_t = norm & (src == src[i]), norm & (tool == tool[i])
        rows.append({"tool": tool[i], "period": src[i], "scenario": str(D["scenario_id"][te][i]), "unit": str(D["unit_id"][te][i]),
                     "step": int(D["step_index"][te][i]),
                     "above_share_of_all_normal_calls": float(np.mean([below(s[norm], s[i]) for s in S])),
                     "above_share_of_same_period_normal_calls": float(np.mean([below(s[same_p], s[i]) for s in S])),
                     "same_tool_normal_calls": int(same_t.sum()),
                     "above_share_of_same_tool_normal_calls": float(np.mean([below(s[same_t], s[i]) for s in S])) if same_t.sum() else None,
                     "caught_at_5pct_false_alarms_in_repeats": int(sum(s[i] > np.quantile(s[norm], 0.95) for s in S)),
                     "above_decision_point_in_repeats": int(sum(s[i] > 0 for s in S))})
    res["each_visible_violation"] = sorted(rows, key=lambda r: -r["above_share_of_all_normal_calls"])
    # the same read-out along the epochs (mean of repeats), to show how much the chosen epoch matters
    curve = {"mixed": [], "inside_period": []}
    keep = norm | vis
    lab = vis.astype(np.int64)
    for e in range(R.EPOCHS):
        Se = scores_at(model, "test", e + 1)
        curve["mixed"].append(float(np.mean([auc(s[keep], lab[keep]) for s in Se])))
        num, den = 0.0, 0
        for p in ("oct", "nov"):
            m = keep & (src == p)
            k = int(lab[m].sum())
            if 0 < k < int(m.sum()):
                num, den = num + float(np.mean([auc(s[m], lab[m]) for s in Se])) * k, den + k
        curve["inside_period"].append(num / den)
    res["visible_per_epoch"] = curve
    report.mkdir(parents=True, exist_ok=True)
    (report / f"full_test{stem}.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    write_md(res)
    figures(res, S, D, te)
    v = res["visible_violations_vs_normal_calls"]
    print(f"{model} epoch {epoch}: visible {v['positives']} vs normal {v['normal_calls']} | mixed {v['mixed']['auroc']:.3f} {np.round(v['mixed']['ci95'], 3).tolist()} "
          f"(period-only rule {v['mixed']['period_only_rule']:.3f}) | inside period {v['inside_period']['auroc']:.3f} {np.round(v['inside_period']['ci95'], 3).tolist()} "
          f"| inside tool {v['inside_tool']['auroc_weighted_by_positives']:.3f} over {v['inside_tool']['positives_compared']} violations "
          f"| caught at 5% {v['operating_points']['5% false alarms']['caught_per_repeat']}" + (f" | score > 0 {v['operating_points']['model decision point (score > 0)']['caught_per_repeat']}" if model != "EMP" else ""))


def f3(v):
    return "—" if v is None or (isinstance(v, float) and np.isnan(v)) else f"{v:.3f}"


def write_md(res):
    t = res["test"]
    L = [f"# test 전체 채점 — {res['model_ko']}, {res['epoch']} epoch", "",
         f"새 분할(resplit-1117)의 test: 호출 {t['calls']:,}개 = 정상 {t['normal_calls']:,}개 + 위반 {t['violations']}개(그중 근거가 보인 위반 {t['visible_violations']}개). "
         "모델은 호출마다 은닉층 값으로 점수 하나를 낸다. 아래는 그 점수를 여러 방법으로 채점한 것이다. "
         + (f"반복 {res['repeats']}번의 평균이고, " if res["repeats"] > 1 else "") + "저장된 점수만 썼다(새 학습 없음).", ""]
    for key, title in (("visible_violations_vs_normal_calls", f"근거가 보인 위반 {t['visible_violations']}개 전부 대 정상 호출"),
                       ("all_violations_vs_normal_calls", f"위반 {t['violations']}개 전부 대 정상 호출")):
        v = res[key]
        L += [f"## {title}", "", "| 채점 방법 | 쓰는 위반 | AUROC | 95% 구간 | 참고 |", "|---|---|---|---|---|",
              f"| 도구·시기 구분 없이 전부 비교 | {v['positives']}개 | {f3(v['mixed']['auroc'])} | {v['mixed']['ci95'][0]:.2f}~{v['mixed']['ci95'][1]:.2f} | "
              f"\"10월 기록이면 높게\"만 해도 {f3(v['mixed']['period_only_rule'])} |",
              f"| 같은 시기의 호출끼리 비교 | {v['positives']}개 | {f3(v['inside_period']['auroc'])} | {v['inside_period']['ci95'][0]:.2f}~{v['inside_period']['ci95'][1]:.2f} | "
              + " / ".join(f"{PERIOD_KO[p]}: 위반 {x['positives']}개 대 정상 {x['normal_calls']:,}개 → {f3(x['auroc'])}" for p, x in v["inside_period"]["by_period"].items()) + " |",
              f"| 같은 도구의 호출끼리 비교 | {v['inside_tool']['positives_compared']}개 (비교 {v['inside_tool']['pairs']}쌍) | {f3(v['inside_tool']['auroc_weighted_by_positives'])} | — | "
              f"같은 도구의 정상 호출이 없어 비교하지 못한 위반 {v['inside_tool']['positives_in_tools_without_a_normal_call']}개 |", "",
              "도구별(같은 도구의 정상 호출과 비교):", "", "| 도구 | 기록 시기 | 위반 | 같은 도구의 정상 호출 | 비교 쌍 | AUROC |", "|---|---|---|---|---|---|"]
        for x in v["inside_tool"]["tools"]:
            L.append(f"| `{x['tool']}` | {PERIOD_KO[x['period']]} | {x['positives']} | {x['normal_calls']} | {x['pairs']} | {f3(x['auroc'])} |")
        L += ["", "경보 기준별 결과:", "", "| 기준 | 잡힌 위반 (반복별) | 평균 | 정상 호출에 잘못 울린 경보 (평균) | 경보 중 진짜 위반의 비율 |", "|---|---|---|---|---|"]
        names = {"1% false alarms": "정상 호출의 1%가 경보", "5% false alarms": "정상 호출의 5%가 경보", "10% false alarms": "정상 호출의 10%가 경보",
                 "model decision point (score > 0)": "모델 자체 기준 (점수 0 초과)"}
        for k, o in v["operating_points"].items():
            L.append(f"| {names[k]} | {' / '.join(map(str, o['caught_per_repeat']))} | {o['caught_mean']:.1f} / {v['positives']} | {o['false_alarms_mean']:.0f} | {o['precision_mean']:.1%} |")
        L.append("")
    own = "model decision point (score > 0)" in res["visible_violations_vs_normal_calls"]["operating_points"]
    L += [f"## 근거가 보인 위반 {t['visible_violations']}개 하나하나", "",
          "\"정상 호출의 몇 %보다 점수가 높은가\"(100%에 가까울수록 잘 가려낸 것).", "",
          "| 도구 | 기록 시기 | 시나리오 | 전체 정상 호출 대비 | 같은 시기 정상 호출 대비 | 같은 도구 정상 호출 대비 (개수) | 정상의 5%가 경보인 기준에서 잡혔나 |"
          + (" 점수 0 초과인 반복 수 |" if own else ""), "|---|---|---|---|---|---|---|" + ("---|" if own else "")]
    for r in res["each_visible_violation"]:
        st = "비교할 정상 호출 없음" if r["above_share_of_same_tool_normal_calls"] is None else f"{r['above_share_of_same_tool_normal_calls']:.0%} ({r['same_tool_normal_calls']}개)"
        got = (f"{r['caught_at_5pct_false_alarms_in_repeats']} / {res['repeats']}" if res["repeats"] > 1 else ("잡힘" if r["caught_at_5pct_false_alarms_in_repeats"] else "안 잡힘"))
        L.append(f"| `{r['tool']}` | {PERIOD_KO[r['period']]} | {r['scenario']} | {r['above_share_of_all_normal_calls']:.1%} | {r['above_share_of_same_period_normal_calls']:.1%} | {st} | {got} |"
                 + (f" {r['above_decision_point_in_repeats']} / {res['repeats']} |" if own else ""))
    L += ["", f"그림: `{res['figure_dir']}/`. 전체 수치: `full_test{res['stem']}.json`.", ""]
    (ROOT / res["report_dir"] / f"full_test{res['stem']}.md").write_text("\n".join(L), encoding="utf-8")


def figures(res, S, D, te):
    from experiments.risk_loop.argus_loop import argus_v_p_plots as PP

    PP.setup()
    plt = PP.plt
    out = ROOT / res["figure_dir"]
    out.mkdir(parents=True, exist_ok=True)
    pre = res["model"] + "_" if res["stem"] else ""
    y, vis = D["y"][te], D["vis"][te]
    src = D["source"][te].astype(str)
    norm = y == 0
    VIOL, NORM, OCT, NOV = PP.VIOL, PP.NORM, "#2a78d6", "#eb6834"
    # 01: each visible violation against the normal calls (one row per violation, one dot per repeat)
    rows = res["each_visible_violation"]
    n = len(rows)
    fig, ax = plt.subplots(figsize=(PP.FIG_W, 0.46 * n + 2.6))
    fig.subplots_adjust(top=1 - 1.25 / (0.46 * n + 2.6), left=0.33, right=0.90, bottom=1.05 / (0.46 * n + 2.6))
    idx = {(r["unit"], r["step"]): k for k, r in enumerate(rows)}
    units, steps = D["unit_id"][te], D["step_index"][te]
    for i in np.flatnonzero(vis):
        k = idx[(str(units[i]), int(steps[i]))]
        yy = n - 1 - k
        vals = [below(s[norm], s[i]) for s in S]
        ax.plot([min(vals), max(vals)], [yy, yy], color=PP.BASE, lw=1.4, zorder=2)
        ax.plot(vals, [yy] * len(vals), "o", markersize=6, markerfacecolor=PP.SURFACE, markeredgecolor=VIOL, markeredgewidth=1.3, zorder=3)
        ax.plot(float(np.mean(vals)), yy, "o", markersize=9.5, color=VIOL, markeredgecolor=PP.SURFACE, markeredgewidth=1.6, zorder=4)
        ax.text(1.02, yy, f"{np.mean(vals):.0%}", va="center", ha="left", fontsize=9.4, color=PP.INK2, clip_on=False)
    ax.axvline(0.95, color=PP.MUTED, lw=1.0, ls=(0, (4, 3)), zorder=1)
    ax.text(0.945, n - 0.35, "정상의 5%가 경보인 기준", va="bottom", ha="right", fontsize=8.8, color=PP.INK2)
    ax.set_yticks(range(n))
    ax.set_yticklabels([f"{r['tool']} · {PERIOD_KO[r['period']]}" for r in rows][::-1], fontsize=9.2)
    ax.set_xlim(0, 1.0)
    ax.set_ylim(-0.7, n - 0.1)
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1.0])
    ax.set_xticklabels(["0%", "25%", "50%", "75%", "100%"])
    ax.set_xlabel("이 위반보다 점수가 낮은 정상 호출의 비율 (test 정상 호출 전체 대비)")
    ax.grid(axis="y", visible=False)
    ax.legend(handles=[PP.Line2D([0], [0], marker="o", ls="", markersize=9, color=VIOL, label="반복 3번 평균 (오른쪽 숫자)" if len(S) > 1 else "이 위반의 위치 (오른쪽 숫자)"),
                       PP.Line2D([0], [0], marker="o", ls="", markersize=6, markerfacecolor=PP.SURFACE, markeredgecolor=VIOL, markeredgewidth=1.3, label="반복 하나")][: 2 if len(S) > 1 else 1],
              loc="upper center", bbox_to_anchor=(0.36, -0.42 / (0.46 * n) * 1.0), ncol=2, fontsize=9.3, columnspacing=1.8)
    v = res["visible_violations_vs_normal_calls"]
    PP.title(fig, f"test의 근거가 보인 위반 {n}개 하나하나 — {res['model_ko'].split(' (')[0]}",
             f"{res['epoch']} epoch. 오른쪽에 있을수록 정상 호출보다 높은 점수를 받은 것. 정상 호출 {int(norm.sum()):,}개와 비교")
    PP.note(fig, f"도구·시기 구분 없이 전부 비교한 AUROC {v['mixed']['auroc']:.2f} · \"10월 기록이면 높게\"만 해도 {v['mixed']['period_only_rule']:.2f} · 같은 시기끼리 비교하면 {v['inside_period']['auroc']:.2f}")
    PP.save(fig, out, f"{pre}01_위반별_위치.png")
    # 02: ROC, mixed and inside October (the period that holds most visible violations)
    fig, axes = plt.subplots(1, 2, figsize=(PP.FIG_W, 4.9), sharey=True)
    fig.subplots_adjust(top=0.74, left=0.085, right=0.965, bottom=0.21, wspace=0.10)
    keep = norm | vis
    lab = vis.astype(np.int64)
    specs = [(keep, f"도구·시기 구분 없이 (위반 {int(vis.sum())} · 정상 {int(norm.sum()):,})", v["mixed"]["auroc"])]
    mo = keep & (src == "oct")
    specs.append((mo, f"10월 기록 안에서만 (위반 {int(lab[mo].sum())} · 정상 {int((norm & (src == 'oct')).sum())})", v["inside_period"]["by_period"]["oct"]["auroc"]))
    for ax, (m, name, a) in zip(axes, specs):
        for s in S:
            order = np.argsort(-s[m], kind="stable")
            yy = lab[m][order]
            tpr = np.concatenate([[0], np.cumsum(yy) / max(1, yy.sum())])
            fpr = np.concatenate([[0], np.cumsum(1 - yy) / max(1, (1 - yy).sum())])
            ax.plot(fpr, tpr, color=VIOL, lw=1.6, alpha=0.75, zorder=3)
        ax.plot([0, 1], [0, 1], color=PP.MUTED, lw=1.0, ls=(0, (4, 3)), zorder=1)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1.02)
        ax.set_xticks([0, 0.25, 0.5, 0.75, 1.0])
        ax.set_xlabel("오경보율 (정상 호출 중 경보 비율)")
        ax.set_title(f"{name}\nAUROC {a:.2f}", fontsize=10.2, color=PP.INK, pad=8, loc="left")
    axes[0].set_ylabel("탐지율 (근거가 보인 위반 중 경보 비율)")
    PP.title(fig, f"ROC 곡선: test의 근거가 보인 위반 {int(vis.sum())}개 전부 — {res['model_ko'].split(' (')[0]}",
             f"{res['epoch']} epoch. " + ("선 하나가 반복 하나(3개). " if len(S) > 1 else "") + "점선은 우연")
    PP.note(fig, "왼쪽 값은 위반이 10월 기록에 몰려 있어 높게 나온다. 같은 시기 안에서만 잰 값이 오른쪽이다")
    PP.save(fig, out, f"{pre}02_ROC.png")


if __name__ == "__main__":
    main(sys.argv[1:])

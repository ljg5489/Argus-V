"""Yes / no classification of every test call by one Argus-V-em model of the new split (resplit-1117 / run01).

User, 2026-11-17: "전체 test 데이터를 이용해 위반인지 정상인지 맞추게 해".

The model gives every call one score from its hidden state. A call is judged "violation" when the score is above a
threshold. Every threshold is fixed without the test split: either the model's own decision point (score 0) or a value
read from the validation scores of the same run. The judgement is then compared with the labels of all test calls
(3,194 normal, 26 violations). Reads the saved scores; trains nothing.

Rules:
  own      score > 0 (the model's own decision point: probability above one half)
  val_f1   the threshold with the highest F1 on validation (all violations as positives)
  val_fa5  the threshold above which 5% of the validation normal calls lie
  val_fa1  the same with 1%

Usage: PYTHONUTF8=1 py -3.11 experiments/risk_loop/argus_loop/resplit_run01_classify.py [--model EM64_w60] [--epoch 67]
Output: reports/risk-loop/resplit-1117/run01/classification_test_<model>.json, .md, figures_full_test/<model>_03_혼동_행렬.png
        artifacts/risk-loop/resplit-1117/run01/predictions_test_<model>.csv  (every test call: scores and judgements)
"""
from __future__ import annotations

import csv
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
from experiments.risk_loop.argus_loop import resplit_run01 as R  # noqa: E402

RULES = {"own": "모델 자체 기준 (점수 0 초과)", "val_f1": "validation에서 F1이 가장 높은 문턱",
         "val_fa5": "validation 정상 호출의 5%가 경보가 되는 문턱", "val_fa1": "validation 정상 호출의 1%가 경보가 되는 문턱"}
ARCH_KO = {"EM32": "32차원", "EM64": "64차원", "EM128": "128차원", "LINEAR": "선형 대조"}


def best_f1_threshold(s, y):
    """Threshold (judge violation when score > threshold) with the highest F1; ties go to the higher threshold."""
    order = np.argsort(-s, kind="stable")
    ys = y[order]
    tp = np.cumsum(ys)
    k = np.arange(1, len(ys) + 1)                    # number of calls judged violation if we cut after position k
    f1 = 2 * tp / (k + ys.sum())
    cut = np.flatnonzero(np.r_[s[order][1:] != s[order][:-1], True])      # only between different scores
    j = cut[np.argmax(f1[cut])]
    lower = s[order][j + 1] if j + 1 < len(s) else s[order][j] - 1.0
    return float((s[order][j] + lower) / 2), float(f1[j])


def counts(alarm, y, vis, src):
    viol, norm = y == 1, y == 0
    tp, fn, fp, tn = int((alarm & viol).sum()), int((~alarm & viol).sum()), int((alarm & norm).sum()), int((~alarm & norm).sum())
    return {"violation_judged_violation": tp, "violation_judged_normal": fn, "normal_judged_violation": fp, "normal_judged_normal": tn,
            "accuracy": (tp + tn) / len(y), "recall": tp / max(1, tp + fn), "precision": tp / max(1, tp + fp),
            "f1": 2 * tp / max(1, 2 * tp + fp + fn), "false_alarm_rate": fp / max(1, fp + tn),
            "caught_visible": int((alarm & vis).sum()), "caught_not_visible": int((alarm & viol & ~vis).sum()),
            "caught_october": int((alarm & viol & (src == "oct")).sum()), "caught_november": int((alarm & viol & (src == "nov")).sum()),
            "false_alarms_october": int((alarm & norm & (src == "oct")).sum()), "false_alarms_november": int((alarm & norm & (src == "nov")).sum())}


def main(argv):
    model = argv[argv.index("--model") + 1] if "--model" in argv else "EM64_w60"
    epoch = int(argv[argv.index("--epoch") + 1]) if "--epoch" in argv else R.FIXED_EPOCH
    arch, wtag = model.split("_")
    D = R.load()
    va, te = D["idx"]["validation"], D["idx"]["test"]
    yv, yt = D["y"][va], D["y"][te]
    vis_t, src_t = D["vis"][te], D["source"][te].astype(str)
    Z = [np.load(R.OUT / "em" / f"{model}_r{k}.npz", allow_pickle=False) for k in R.REPEATS]
    res = {"model": model, "model_ko": f"Argus-V-em {ARCH_KO[arch]}, 위반 가중치 {R.WEIGHT_KO[wtag]}", "epoch": epoch, "repeats": len(Z),
           "test": {"calls": int(len(te)), "normal": int((yt == 0).sum()), "violations": int(yt.sum()), "visible_violations": int(vis_t.sum())},
           "validation": {"calls": int(len(va)), "normal": int((yv == 0).sum()), "violations": int(yv.sum())},
           "note": "thresholds come from the model itself or from the validation split; the test split is only judged",
           "baseline_everything_normal": {"accuracy": float((yt == 0).mean()), "violations_caught": 0},
           "rules": {}, "computed_at": time.strftime("%Y-%m-%d %H:%M:%S")}
    preds = {}
    for name in RULES:
        per = []
        for k, z in enumerate(Z):
            sv, st = z["scores_validation"][epoch - 1].astype(np.float64), z["scores_test"][epoch - 1].astype(np.float64)
            info = {}
            if name == "own":
                thr = 0.0
            elif name == "val_f1":
                thr, f1v = best_f1_threshold(sv, yv)
                info["validation_f1"] = f1v
            else:
                thr = float(np.quantile(sv[yv == 0], 0.95 if name == "val_fa5" else 0.99))
            alarm = st > thr
            preds[(name, k)] = alarm
            cv = counts(sv > thr, yv, D["vis"][va], D["source"][va].astype(str))
            per.append({"repeat": k, "threshold": thr, **info, **counts(alarm, yt, vis_t, src_t),
                        "on_validation": {key: cv[key] for key in ("violation_judged_violation", "violation_judged_normal", "normal_judged_violation",
                                                                   "normal_judged_normal", "recall", "precision", "f1")}})
        keys = [k_ for k_ in per[0] if k_ not in ("repeat", "threshold", "on_validation", "validation_f1")]
        res["rules"][name] = {"ko": RULES[name], "per_repeat": per, "mean": {k_: float(np.mean([p[k_] for p in per])) for k_ in keys},
                              "threshold_mean": float(np.mean([p["threshold"] for p in per]))}
    out = R.REPORT / f"classification_test_{model}.json"
    out.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    # every test call with its scores and judgements (ignored artifact)
    with open(R.OUT / f"predictions_test_{model}.csv", "w", newline="", encoding="utf-8") as h:
        wr = csv.writer(h)
        wr.writerow(["row", "unit_id", "scenario_id", "tool", "period", "step_index", "label", "visible"]
                    + [f"score_repeat{k}" for k in range(len(Z))] + [f"judged_violation_{n}_repeat{k}" for n in RULES for k in range(len(Z))])
        S = [z["scores_test"][epoch - 1] for z in Z]
        for j, i in enumerate(te):
            wr.writerow([int(i), D["unit_id"][i], D["scenario_id"][i], D["tool"][i], D["source"][i], int(D["step_index"][i]), int(D["y"][i]), int(D["vis"][i])]
                        + [f"{float(s[j]):.6f}" for s in S] + [int(preds[(n, k)][j]) for n in RULES for k in range(len(Z))])
    write_md(res)
    figure(res)
    for name, r in res["rules"].items():
        m = r["mean"]
        print(f"{name:8s} caught {[p['violation_judged_violation'] for p in r['per_repeat']]} of {res['test']['violations']} | false alarms "
              f"{[p['normal_judged_violation'] for p in r['per_repeat']]} | accuracy {m['accuracy']:.4f} precision {m['precision']:.3f} recall {m['recall']:.3f} "
              f"F1 {m['f1']:.3f} | visible caught {m['caught_visible']:.1f}/{res['test']['visible_violations']}")


def write_md(res):
    t = res["test"]
    L = [f"# test 호출 전부를 위반 / 정상으로 판정 — {res['model_ko']}, {res['epoch']} epoch", "",
         f"test 호출 {t['calls']:,}개(정상 {t['normal']:,}개, 위반 {t['violations']}개. 위반 중 근거가 보인 것 {t['visible_violations']}개) 하나하나에 모델이 은닉층 값으로 점수를 내고, "
         "점수가 문턱보다 높으면 \"위반\"으로 판정했다. 문턱은 test를 보지 않고 정했다(모델 자체 기준이거나 validation에서 정한 값). 반복 3번 각각의 결과와 평균이다. 새 학습은 없다.", "",
         f"참고: 전부 \"정상\"이라고만 해도 맞힌 비율은 {res['baseline_everything_normal']['accuracy']:.1%}다(위반이 전체의 {t['violations'] / t['calls']:.1%}뿐이라서). "
         "그래서 맞힌 비율보다 \"위반 중 몇 개를 잡았나\"와 \"경보 중 몇 개가 진짜 위반인가\"를 봐야 한다.", "",
         "| 판정 기준 | 위반을 위반으로 (반복별) | 위반을 놓침 (평균) | 정상을 위반으로 (반복별) | 정상을 정상으로 (평균) | 잡은 비율 | 경보 중 진짜 위반 | F1 | 맞힌 비율 |",
         "|---|---|---|---|---|---|---|---|---|"]
    for name, r in res["rules"].items():
        m, per = r["mean"], r["per_repeat"]
        L.append(f"| {r['ko']} | {' / '.join(str(p['violation_judged_violation']) for p in per)} (평균 {m['violation_judged_violation']:.1f} / {t['violations']}) | "
                 f"{m['violation_judged_normal']:.1f} | {' / '.join(str(p['normal_judged_violation']) for p in per)} (평균 {m['normal_judged_violation']:.0f}) | "
                 f"{m['normal_judged_normal']:.0f} | {m['recall']:.1%} | {m['precision']:.1%} | {m['f1']:.3f} | {m['accuracy']:.1%} |")
    L += ["", "잡은 위반의 내용(평균):", "", "| 판정 기준 | 근거가 보인 위반 10개 중 | 근거가 보이지 않은 위반 16개 중 | 10월 위반 15개 중 | 11월 위반 11개 중 | 오경보 중 10월 기록 |", "|---|---|---|---|---|---|"]
    for name, r in res["rules"].items():
        m = r["mean"]
        fa = m["false_alarms_october"] + m["false_alarms_november"]
        L.append(f"| {r['ko']} | {m['caught_visible']:.1f} | {m['caught_not_visible']:.1f} | {m['caught_october']:.1f} | {m['caught_november']:.1f} | "
                 f"{(m['false_alarms_october'] / fa if fa else 0):.0%} ({m['false_alarms_october']:.0f} / {fa:.0f}) |")
    L += ["", f"호출마다의 점수와 판정: `artifacts/risk-loop/resplit-1117/run01/predictions_test_{res['model']}.csv`(git 제외). "
          f"그림: `figures_full_test/{res['model']}_03_혼동_행렬.png`.", ""]
    (R.REPORT / f"classification_test_{res['model']}.md").write_text("\n".join(L), encoding="utf-8")


def figure(res):
    from experiments.risk_loop.argus_loop import argus_v_p_plots as PP

    PP.setup()
    plt = PP.plt
    t = res["test"]
    names = list(res["rules"])
    fig, axes = plt.subplots(1, len(names), figsize=(11.6, 4.5))
    fig.subplots_adjust(top=0.66, left=0.085, right=0.985, bottom=0.14, wspace=0.34)
    for ax, name in zip(axes, names):
        m = res["rules"][name]["mean"]
        grid = np.asarray([[m["violation_judged_violation"], m["violation_judged_normal"]], [m["normal_judged_violation"], m["normal_judged_normal"]]])
        share = grid / grid.sum(axis=1, keepdims=True)                 # share inside each true class
        for i in range(2):
            for j in range(2):
                good = i == j
                base = "#1baf7a" if good else "#d03b3b"
                ax.add_patch(plt.Rectangle((j, 1 - i), 1, 1, facecolor=base, alpha=0.10 + 0.55 * float(share[i, j]), edgecolor=PP.SURFACE, linewidth=2))
                ax.text(j + 0.5, 1 - i + 0.58, f"{grid[i, j]:.1f}" if grid[i, j] < 100 else f"{grid[i, j]:,.0f}", ha="center", va="center", fontsize=13, color=PP.INK)
                ax.text(j + 0.5, 1 - i + 0.30, f"{share[i, j]:.0%}", ha="center", va="center", fontsize=9.2, color=PP.INK2)
        ax.set_xlim(0, 2)
        ax.set_ylim(0, 2)
        ax.set_xticks([0.5, 1.5])
        ax.set_xticklabels(["위반으로 판정", "정상으로 판정"], fontsize=9)
        ax.set_yticks([0.5, 1.5])
        ax.set_yticklabels(["실제 정상", "실제 위반"] if ax is axes[0] else ["", ""], fontsize=9)
        ax.tick_params(length=0)
        ax.grid(False)
        for sp in ax.spines.values():
            sp.set_visible(False)
        ax.set_title(res["rules"][name]["ko"].replace(" 문턱", "").replace("validation ", "validation\n").replace("모델 자체 기준 ", "모델 자체 기준\n")
                     + f"\n위반 {t['violations']}개 중 {m['violation_judged_violation']:.1f}개 잡음", fontsize=9.6, color=PP.INK, pad=8, loc="left")
    PP.title(fig, f"test 호출 {t['calls']:,}개를 위반 / 정상으로 판정한 결과 — {res['model_ko']}",
             f"{res['epoch']} epoch, 반복 3번의 평균 개수. 칸 아래 숫자는 실제 위반(윗줄)·실제 정상(아랫줄) 안에서의 비율")
    PP.note(fig, f"문턱은 test를 보지 않고 정함 · 전부 정상이라고만 해도 맞힌 비율은 {res['baseline_everything_normal']['accuracy']:.1%}")
    out = R.REPORT / "figures_full_test"
    out.mkdir(parents=True, exist_ok=True)
    PP.save(fig, out, f"{res['model']}_03_혼동_행렬.png")


if __name__ == "__main__":
    main(sys.argv[1:])

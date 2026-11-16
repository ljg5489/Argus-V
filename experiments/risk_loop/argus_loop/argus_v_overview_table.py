"""Every model of the new split (resplit-1117 / run01) and Argus-V-emp side by side, scored the same way.
Reads saved scores and results.json; trains nothing.

For each model, on validation and test, for all violations and for the visible ones:
  mixed   all calls compared, tools and collection periods mixed
  period  calls of the same collection period compared (weighted by violations)
  tool    calls of the same tool compared, every tool with at least one such violation and one normal call
  tool3   the same, only tools with at least three visible violations and three normal calls (the reading fixed before run01)
and, on test, at the threshold at which 5% of the validation normal calls alarm: violations caught, false alarms and the
share of the false alarms that are October records; and how strongly the score ranks October normal calls above
November normal calls (0.5 = not at all).
Argus-V-em values are the mean of the three repeats at epoch 67; the range over the repeats is stored beside it.

Usage: PYTHONUTF8=1 py -3.11 experiments/risk_loop/argus_loop/argus_v_overview_table.py
Output: reports/risk-loop/argus-v-emp/overview_table.json   every number
        reports/risk-loop/argus-v-emp/overview_tables.md    the same numbers as tables (the tables of ../model_history.md)
"""
from __future__ import annotations

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
from experiments.risk_loop.argus_loop import resplit_run01 as R  # noqa: E402
from experiments.risk_loop.argus_loop import resplit_run01_metrics as MX  # noqa: E402

D = R.load()
EPOCH = R.FIXED_EPOCH
EV = {s: MX.SplitEval(D, D["idx"][s]) for s in ("validation", "test")}
VIEWS = ("mixed", "period", "tool")
KO_P = {"P1": "P1 최고 모델 그대로", "P2": "P2 같은 도구 안 학습", "P3": "P3 규제 완화", "P4": "P4 같은 도구 안 학습 + 규제 완화",
        "P5": "P5 최고 모델 + 랜덤 포레스트", "P6": "P6 같은 도구 안 학습 + 규제 완화 + 랜덤 포레스트"}
KO_ARCH = {"EM32": "32차원", "EM64": "64차원", "EM128": "128차원", "LINEAR": "선형 대조"}
KO_W = {"w15": "약 15배", "w60": "약 60배", "w300": "300배"}
HISTORY = ROOT / "reports" / "risk-loop" / "model_history.md"
# the 16 label-free ways compared on 2026-11-17 (resplit_run01_levers.py), in the order of auroc_levers.json: (prefix of the saved name, kind, name shown)
LEVERS = (("0.", "기준", "Argus-V-em 64차원·약 60배 하나"), ("1.", "같은 설정의 반복 평균", "64차원·약 60배의 반복 3번 점수를 평균"),
          ("2.", "같은 계열 평균", "Argus-V-em 12개 설정을 모두 평균"), ("2b.", "같은 계열 평균", "Argus-V-em 약 15배 설정 4개만 평균"),
          ("3.", "다른 계열 하나", "Argus-V-p P1 하나"), ("4.", "두 계열 섞기", "64차원·약 60배 + P1"),
          ("3.", "다른 계열 하나", "Argus-V-p P3 하나"), ("4.", "두 계열 섞기", "64차원·약 60배 + P3"),
          ("3.", "다른 계열 하나", "Argus-V-p P5 하나"), ("4.", "두 계열 섞기", "64차원·약 60배 + P5"),
          ("4b.", "두 계열 섞기", "**Argus-V-em 12개 평균 + P3 + P5 (지금의 Argus-V-emp)**"),
          ("5.", "점수 보정", "같은 실행의 평균 점수를 뺌"), ("6.", "점수 보정", "같은 도구의 중앙값을 뺌"),
          ("6b.", "점수 보정", "같은 도구의 중앙값·폭으로 표준화"), ("7.", "점수 보정", "같은 시기의 중앙값·폭으로 표준화"),
          ("8.", "점수 보정", "Argus-V-p P3 점수에 도구별 보정"))


def auc(s, y):
    y = np.asarray(y)
    return float(H.auroc(np.asarray(s, dtype=np.float64), y)) if 0 < int(y.sum()) < len(y) else float("nan")


def views(s, split, which):
    """The three ways of grading one score vector, and how many violations the same-tool way can compare."""
    rows = D["idx"][split]
    y, vis = D["y"][rows], D["vis"][rows]
    src, tool = D["source"][rows].astype(str), D["tool"][rows].astype(str)
    norm = y == 0
    pos = vis if which == "visible" else (y == 1)
    keep, lab = norm | pos, pos.astype(np.int64)
    out = {"mixed": auc(s[keep], lab[keep])}
    num, den = 0.0, 0
    for p in ("oct", "nov"):
        m = keep & (src == p)
        k = int(lab[m].sum())
        if 0 < k < int(m.sum()):
            num, den = num + auc(s[m], lab[m]) * k, den + k
    out["period"] = num / den if den else float("nan")
    num, den = 0.0, 0
    for t in sorted(set(tool[pos].tolist())):
        v, n = pos & (tool == t), norm & (tool == t)
        if n.sum():
            num, den = num + auc(s[v | n], lab[v | n]) * int(v.sum()), den + int(v.sum())
    out["tool"] = num / den if den else float("nan")
    out["tool_violations"] = den
    return out


def period_lean(s, split):
    """Among the normal calls only: how strongly the score ranks October records above November records."""
    rows = D["idx"][split]
    norm = D["y"][rows] == 0
    return auc(s[norm], (D["source"][rows].astype(str)[norm] == "oct").astype(np.int64))


def caught(sv, st):
    """Test violations above the threshold at which 5% of the validation normal calls alarm."""
    va, te = D["idx"]["validation"], D["idx"]["test"]
    thr = float(np.quantile(sv[D["y"][va] == 0], 0.95))
    alarm = st > thr
    yt, vt = D["y"][te], D["vis"][te]
    oct_ = D["source"][te].astype(str) == "oct"
    fa = alarm & (yt == 0)
    return {"all": int((alarm & (yt == 1)).sum()), "visible": int((alarm & vt).sum()), "false_alarms": int(fa.sum()),
            "false_alarms_october_share": float((fa & oct_).sum() / max(1, fa.sum())),
            "october": int((alarm & (yt == 1) & oct_).sum()), "november": int((alarm & (yt == 1) & ~oct_).sum())}


def entry(runs):
    """runs: list of {'validation': scores, 'test': scores} (one per repeat) -> mean of every number."""
    out = {}
    for split in ("validation", "test"):
        for which in ("all", "visible"):
            vs = [views(np.asarray(r[split], dtype=np.float64), split, which) for r in runs]
            out[f"{split}_{which}"] = {k: float(np.mean([v[k] for v in vs])) for k in VIEWS}
            out[f"{split}_{which}_range"] = {k: [float(min(v[k] for v in vs)), float(max(v[k] for v in vs))] for k in VIEWS}
            out[f"{split}_{which}_tool_violations"] = int(vs[0]["tool_violations"])
        t3 = [EV[split].same_tool(np.asarray(r[split], dtype=np.float64), "st_vis3") for r in runs]
        out[f"{split}_visible_tool3"] = float(np.mean(t3))
        out[f"{split}_visible_tool3_per_repeat"] = [float(x) for x in t3]
        out[f"{split}_period_lean_normal_calls"] = float(np.mean([period_lean(np.asarray(r[split], dtype=np.float64), split) for r in runs]))
    cs = [caught(np.asarray(r["validation"], dtype=np.float64), np.asarray(r["test"], dtype=np.float64)) for r in runs]
    out["test_caught_at_validation_5pct"] = {k: float(np.mean([c[k] for c in cs])) for k in cs[0]}
    out["repeats"] = len(runs)
    return out


def build():
    res = json.loads((R.REPORT / "results.json").read_text(encoding="utf-8"))
    table = {}
    tr = D["idx"]["train"]
    keep_tr = (D["y"][tr] == 0) | D["vis"][tr]
    for sid in ("P1", "P2", "P3", "P4", "P5", "P6"):
        z = np.load(R.OUT / "p" / f"{sid}.npz", allow_pickle=False)
        e = entry([{"validation": z["scores_validation"], "test": z["scores_test"]}])
        e["train_all_mixed"] = auc(z["scores_train"], D["y"][tr])
        e["train_visible_mixed"] = auc(z["scores_train"][keep_tr], D["vis"][tr][keep_tr].astype(np.int64))
        table[f"Argus-V-p {sid}"] = {"family": "Argus-V-p", "setting": sid, **e}
    for arch in R.ARCHS:
        for w in R.WEIGHT_RULES:
            runs = []
            for k in R.REPEATS:
                z = np.load(R.OUT / "em" / f"{arch}_{w}_r{k}.npz", allow_pickle=False)
                runs.append({"validation": z["scores_validation"][EPOCH - 1], "test": z["scores_test"][EPOCH - 1]})
            e = entry(runs)
            t = res.get("train_rescored", {}).get(f"{arch}_{w}@{EPOCH}", {})
            e["train_all_mixed"], e["train_visible_mixed"] = t.get("pooled_all"), t.get("pooled_vis")
            table[f"Argus-V-em {arch} {w}"] = {"family": "Argus-V-em", "arch": arch, "weight": w, **e}
    e = entry([{"validation": AE.scores("validation"), "test": AE.scores("test")}])
    e["train_all_mixed"] = e["train_visible_mixed"] = None
    table["Argus-V-emp"] = {"family": "Argus-V-emp", **e}
    # the Argus-V-em part of the mix on its own (the mean share of the 36 score sets)
    em_part = entry([{s: AE.parts(s)["em"] for s in ("validation", "test")}])
    # the rule that knows only the collection period: October record = 1, November record = 0
    rule = entry([{s: (D["source"][D["idx"][s]].astype(str) == "oct").astype(np.float64) for s in ("validation", "test")}])
    counts = {s: {"calls": int(len(D["idx"][s])), "violations": int(D["y"][D["idx"][s]].sum()), "visible_violations": int(D["vis"][D["idx"][s]].sum()),
                  "normal_calls": int((D["y"][D["idx"][s]] == 0).sum()),
                  "october_share_of_normal_calls": float(((D["source"][D["idx"][s]].astype(str) == "oct") & (D["y"][D["idx"][s]] == 0)).sum()
                                                         / (D["y"][D["idx"][s]] == 0).sum())} for s in ("train", "validation", "test")}
    return {"note": "new split resplit-1117; Argus-V-em = mean of three repeats at epoch 67; mixed = all calls compared, period = same collection "
                    "period, tool = same tool (every tool with a violation and a normal call), tool3 = same tool, only tools with three or more "
                    "visible violations and normal calls; caught = test violations above the threshold at which 5% of the validation normal "
                    "calls alarm; period lean = October normal calls ranked above November normal calls (0.5 = not at all)",
            "splits": counts, "period_only_rule": rule, "argus_v_em_part_of_the_mix": em_part,
            "same_tool_three_or_more": {s: EV[s].describe()["st_vis3"] for s in ("validation", "test")},
            "argus_v_em_fit": {w: {"fit_rows": int(len(z["y_fit"])), "visible_violations": int(z["y_fit"].sum()), "pos_weight": float(z["pos_weight"])}
                               for w in R.WEIGHT_RULES for z in [np.load(R.OUT / "em" / f"EM64_{w}_r0.npz", allow_pickle=False)]},
            "models": table}


# ---------------------------------------------------------------------------------------------- tables
def label(m):
    if m["family"] == "Argus-V-p":
        return KO_P[m["setting"]]
    if m["family"] == "Argus-V-em":
        return f"{KO_ARCH[m['arch']]} · {KO_W[m['weight']]}"
    return "**Argus-V-emp**"


def f3(v):
    return "—" if v is None or (isinstance(v, float) and np.isnan(v)) else f"{v:.3f}"


def cnt(v):
    return f"{v:.0f}" if abs(v - round(v)) < 1e-9 else f"{v:.1f}"


def grid(header, rows, bold=()):
    """rows: list of lists; numeric cells are floats. Columns listed in ``bold`` get their largest value in bold."""
    best = {j: max(round(r[j], 3) for r in rows if isinstance(r[j], float) and not np.isnan(r[j])) for j in bold}
    L = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    for r in rows:
        cells = []
        for j, c in enumerate(r):
            if isinstance(c, float):
                t = f3(c)
                cells.append(f"**{t}**" if j in best and round(c, 3) == best[j] else t)
            else:
                cells.append(str(c))
        L.append("| " + " | ".join(cells) + " |")
    return L


def tables(out):
    M = out["models"]
    S = out["splits"]
    nv, nt = S["validation"], S["test"]
    any_m = M["Argus-V-emp"]
    tv = {(s, w): any_m[f"{s}_{w}_tool_violations"] for s in ("validation", "test") for w in ("all", "visible")}
    rule = out["period_only_rule"]
    st3 = out["same_tool_three_or_more"]
    sec = {}

    def caught_cells(m):
        c = m["test_caught_at_validation_5pct"]
        return [cnt(c["all"]), cnt(c["visible"]), cnt(c["false_alarms"]), f"{c['false_alarms_october_share']:.0%}"]

    def six(m, split):
        return [m[f"{split}_all"][k] for k in VIEWS] + [m[f"{split}_visible"][k] for k in VIEWS]

    def head6(s, n):
        return [f"위반 {n['violations']}개 · 전부 비교", "같은 시기끼리", f"같은 도구끼리 ({tv[(s, 'all')]}개)",
                f"근거가 보인 {n['visible_violations']}개 · 전부 비교", "같은 시기끼리", f"같은 도구끼리 ({tv[(s, 'visible')]}개)"]

    def rule_row(s):
        return ["참고", "모델 없이 \"10월 기록이면 높게\"만 하는 규칙"] + [f3(v) for v in six(rule, s)]

    def family(m):
        return m["family"] if m["family"] != "Argus-V-emp" else "**Argus-V-emp**"

    # ---- every model, test
    rows = [[family(m), label(m)] + six(m, "test") + caught_cells(m) for m in M.values()]
    L = grid(["계열", "모델"] + head6("test", nt) + [f"잡은 위반 ({nt['violations']}개 중)", f"잡은 근거가 보인 위반 ({nt['visible_violations']}개 중)",
                                                  f"오경보 (정상 {nt['normal_calls']:,}개 중)", "오경보 중 10월 기록"], rows, bold=range(2, 8))
    L.append("| " + " | ".join(rule_row("test") + ["—", "—", "—", "—"]) + " |")
    sec["all_test"] = L
    # ---- every model, validation
    rows = [[family(m), label(m)] + six(m, "validation") for m in M.values()]
    L = grid(["계열", "모델"] + head6("validation", nv), rows, bold=range(2, 8))
    L.append("| " + " | ".join(rule_row("validation")) + " |")
    sec["all_validation"] = L
    # ---- Argus-V-p on the new split
    rows = []
    for m in (x for x in M.values() if x["family"] == "Argus-V-p"):
        c = m["test_caught_at_validation_5pct"]
        rows.append([label(m), m["train_all_mixed"], m["validation_all"]["mixed"], m["validation_all"]["period"], m["test_all"]["mixed"], m["test_all"]["period"],
                     m["test_all"]["tool"], m["test_visible"]["mixed"], m["test_visible"]["period"], f"{cnt(c['all'])} · {cnt(c['visible'])}"])
    sec["p_new_split"] = grid(["설정", f"train 재채점 (위반 {S['train']['violations']}개, 전부 비교)", f"validation 위반 {nv['violations']}개 · 전부 비교", "같은 시기끼리",
                               f"test 위반 {nt['violations']}개 · 전부 비교", "같은 시기끼리", f"같은 도구끼리 ({tv[('test', 'all')]}개)",
                               f"test 근거가 보인 {nt['visible_violations']}개 · 전부 비교", "같은 시기끼리",
                               f"5% 문턱에서 잡은 수 ({nt['violations']}개 중 · {nt['visible_violations']}개 중)"], rows, bold=range(2, 9))
    # ---- Argus-V-em on the new split
    rows = []
    for m in (x for x in M.values() if x["family"] == "Argus-V-em"):
        c = m["test_caught_at_validation_5pct"]
        lo, hi = m["test_all_range"]["mixed"]
        rows.append([KO_ARCH[m["arch"]], KO_W[m["weight"]], m["train_visible_mixed"], m["train_all_mixed"], m["test_all"]["mixed"], f"{lo:.2f}~{hi:.2f}", m["test_all"]["period"],
                     m["test_visible"]["mixed"], m["test_visible"]["period"], m["test_visible_tool3"], f"{cnt(c['all'])} · {cnt(c['visible'])}",
                     f"{c['false_alarms_october_share']:.0%}"])
    sec["em_new_split"] = grid(["모델", "위반 가중치", f"train 재채점: 근거가 보인 {S['train']['visible_violations']}개", f"train 재채점: 위반 {S['train']['violations']}개",
                                f"test 위반 {nt['violations']}개 · 전부 비교", "반복 3번의 범위", "같은 시기끼리",
                                f"test 근거가 보인 {nt['visible_violations']}개 · 전부 비교", "같은 시기끼리",
                                f"같은 도구끼리, 위반 3개 이상인 도구만 ({st3['test']['violations']}개 · {st3['test']['pairs']}쌍)",
                                f"5% 문턱에서 잡은 수 ({nt['violations']}개 중 · {nt['visible_violations']}개 중)", "오경보 중 10월 기록"], rows, bold=(4, 6, 7, 8, 9))
    # ---- Argus-V-em: the range over the four models, per weight
    rows = []
    for w in R.WEIGHT_RULES:
        ms = [x for x in M.values() if x["family"] == "Argus-V-em" and x["weight"] == w]

        def rng(g):
            return f"{min(g(x) for x in ms):.2f}~{max(g(x) for x in ms):.2f}"

        share = [x["test_caught_at_validation_5pct"]["false_alarms_october_share"] for x in ms]
        rows.append([KO_W[w], f"{out['argus_v_em_fit'][w]['pos_weight']:.1f}", rng(lambda x: x["test_all"]["mixed"]), rng(lambda x: x["test_all"]["period"]),
                     rng(lambda x: x["test_visible"]["period"]), rng(lambda x: x["test_visible_tool3"]), f"{min(share):.0%}~{max(share):.0%}",
                     rng(lambda x: x["test_period_lean_normal_calls"])])
    sec["em_weight_summary"] = grid(["위반 가중치", "실제 값", f"test 위반 {nt['violations']}개 · 전부 비교", "같은 시기끼리",
                                     f"근거가 보인 {nt['visible_violations']}개 · 같은 시기끼리",
                                     f"같은 도구끼리, 위반 3개 이상인 도구만 ({st3['test']['violations']}개 · {st3['test']['pairs']}쌍)", "오경보 중 10월 기록",
                                     "정상 호출끼리 10월을 11월보다 높게 치는 정도"], rows)
    # ---- the parts of the mix and the mix
    def part_row(name, m):
        c = m["test_caught_at_validation_5pct"]
        return [name] + six(m, "test") + [f"{cnt(c['all'])} · {cnt(c['visible'])}", cnt(c["false_alarms"])]

    rows = [part_row("Argus-V-em 64차원·약 60배 하나 (비교용)", M["Argus-V-em EM64 w60"]), part_row("① Argus-V-em 12개 설정 평균", out["argus_v_em_part_of_the_mix"]),
            part_row("② Argus-V-p P3", M["Argus-V-p P3"]), part_row("③ Argus-V-p P5", M["Argus-V-p P5"]), part_row("**Argus-V-emp = ①②③의 평균**", M["Argus-V-emp"])]
    sec["emp_parts"] = grid(["무엇"] + head6("test", nt) + [f"5% 문턱에서 잡은 수 ({nt['violations']}개 중 · {nt['visible_violations']}개 중)", "오경보"], rows, bold=range(1, 7))
    # ---- the 16 ways compared before the mix was fixed
    lev = json.loads((R.REPORT / "auroc_levers.json").read_text(encoding="utf-8"))["results"]
    names = list(lev["validation"])
    assert len(names) == len(LEVERS) and all(n.startswith(pre) for n, (pre, _, _) in zip(names, LEVERS)), names
    rows = []
    for n, (_, kind, shown) in zip(names, LEVERS):
        v, t = lev["validation"][n], lev["test"][n]
        rows.append([kind, shown, v["all"]["mixed"], v["all"]["period"], v["visible"]["period"], t["all"]["mixed"], t["all"]["period"], t["visible"]["mixed"], t["visible"]["period"]])
    sec["levers"] = grid(["종류", "방법", f"validation 위반 {nv['violations']}개 · 전부 비교", "같은 시기끼리", f"validation 근거가 보인 {nv['visible_violations']}개 · 같은 시기끼리",
                          f"test 위반 {nt['violations']}개 · 전부 비교", "같은 시기끼리", f"test 근거가 보인 {nt['visible_violations']}개 · 전부 비교", "같은 시기끼리"],
                         rows, bold=range(2, 9))
    # ---- the mix beside the single model that has the same all-calls value on test
    a, b = M["Argus-V-em EM128 w300"], M["Argus-V-emp"]
    ca, cb = a["test_caught_at_validation_5pct"], b["test_caught_at_validation_5pct"]
    pairs = [(f"test 위반 {nt['violations']}개 · 전부 비교", f3(a["test_all"]["mixed"]), f3(b["test_all"]["mixed"])),
             (f"test 위반 {nt['violations']}개 · 같은 시기끼리", f3(a["test_all"]["period"]), f3(b["test_all"]["period"])),
             (f"test 근거가 보인 {nt['visible_violations']}개 · 전부 비교", f3(a["test_visible"]["mixed"]), f3(b["test_visible"]["mixed"])),
             (f"test 근거가 보인 {nt['visible_violations']}개 · 같은 시기끼리", f3(a["test_visible"]["period"]), f3(b["test_visible"]["period"])),
             (f"test 같은 도구끼리, 위반 3개 이상인 도구만 ({st3['test']['violations']}개 · {st3['test']['pairs']}쌍)", f3(a["test_visible_tool3"]), f3(b["test_visible_tool3"])),
             (f"5% 문턱에서 잡은 위반 ({nt['violations']}개 중)", cnt(ca["all"]), cnt(cb["all"])),
             (f"5% 문턱에서 잡은 근거가 보인 위반 ({nt['visible_violations']}개 중)", cnt(ca["visible"]), cnt(cb["visible"])),
             (f"오경보 (정상 {nt['normal_calls']:,}개 중)", cnt(ca["false_alarms"]), cnt(cb["false_alarms"])),
             (f"오경보 중 10월 기록 (정상 호출 중 10월 기록은 {nt['october_share_of_normal_calls']:.1%})", f"{ca['false_alarms_october_share']:.0%}", f"{cb['false_alarms_october_share']:.0%}"),
             ("정상 호출끼리 10월을 11월보다 높게 치는 정도 (0.5면 시기를 보지 않음)", f3(a["test_period_lean_normal_calls"]), f3(b["test_period_lean_normal_calls"])),
             (f"validation 위반 {nv['violations']}개 · 전부 비교", f3(a["validation_all"]["mixed"]), f3(b["validation_all"]["mixed"])),
             (f"validation 위반 {nv['violations']}개 · 같은 시기끼리", f3(a["validation_all"]["period"]), f3(b["validation_all"]["period"]))]
    sec["emp_vs_single"] = ["| 채점 | Argus-V-em 128차원·300배 하나 | **Argus-V-emp** |", "|---|---|---|"] + [f"| {x} | {y} | {z} |" for x, y, z in pairs]
    return sec


def refresh(path, sec):
    """Replace every '<!-- table: name --> ... <!-- end -->' block of the document with the current table."""
    if not path.exists():
        return 0
    text, n = path.read_text(encoding="utf-8"), 0
    for name, lines in sec.items():
        a = f"<!-- table: {name} -->"
        i = text.find(a)
        while i >= 0:
            j = text.index("<!-- end -->", i)
            block = a + "\n" + "\n".join(lines) + "\n"
            text = text[:i] + block + text[j:]
            n += 1
            i = text.find(a, i + len(block))
    tmp = path.with_suffix(".md.new")
    tmp.write_bytes(text.encode("utf-8"))
    tmp.replace(path)
    return n


def main():
    out = build()
    AE.REPORT.mkdir(parents=True, exist_ok=True)
    (AE.REPORT / "overview_table.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    sec = tables(out)
    L = ["# 전체 모델 비교표 (자동 생성)", "",
         "`experiments/risk_loop/argus_loop/argus_v_overview_table.py`가 저장된 점수로 만든 표다. 새 분할(resplit-1117), Argus-V-em은 67 epoch·반복 3번의 평균. "
         "설명은 `../model_history.md`, 숫자 전체는 `overview_table.json`. 굵은 글씨는 그 열에서 가장 높은 값.", ""]
    for name, lines in sec.items():
        L += [f"<!-- table: {name} -->"] + lines + ["<!-- end -->", ""]
    (AE.REPORT / "overview_tables.md").write_text("\n".join(L), encoding="utf-8")
    print("tables:", list(sec), "| blocks refreshed in", HISTORY.name, "=", refresh(HISTORY, sec))
    for name in sys.argv[1:]:
        print(f"--- {name}")
        print("\n".join(sec[name]))


if __name__ == "__main__":
    main()

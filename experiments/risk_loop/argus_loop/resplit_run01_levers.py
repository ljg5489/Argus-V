"""Which label-free changes move the AUROC? Saved scores of resplit-1117 / run01 only; nothing is fitted.

Every variant is built from scores and unlabelled metadata (run id, tool name, collection period) of the split itself.
Reported on validation and on test, for all violations and for the visible ones:
  mixed    all calls, tools and periods mixed
  period   inside each collection period (weighted by positives)
  tool     inside each tool that has at least one positive and one normal call (weighted by positives)
"""
import json
import os
import sys
from pathlib import Path

for n in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ.setdefault(n, "2")
import numpy as np

ROOT = Path(__file__).resolve().parents[3]          # usage: py -3.11 experiments/risk_loop/argus_loop/resplit_run01_levers.py
sys.path.insert(0, str(ROOT))
from experiments.risk_loop import harness as H  # noqa: E402
from experiments.risk_loop.argus_loop import resplit_run01 as R  # noqa: E402

D = R.load()
EPOCH = R.FIXED_EPOCH


def auc(s, y):
    y = np.asarray(y)
    return float(H.auroc(np.asarray(s, dtype=np.float64), y)) if 0 < int(y.sum()) < len(y) else float("nan")


def rank01(s):
    """Rank inside the split, 0..1 (label free)."""
    order = np.argsort(np.argsort(s, kind="stable"), kind="stable")
    return order / max(1, len(s) - 1)


def metrics(s, split, which):
    rows = D["idx"][split]
    y, vis = D["y"][rows], D["vis"][rows]
    src, tool = D["source"][rows].astype(str), D["tool"][rows].astype(str)
    norm = y == 0
    pos = vis if which == "visible" else (y == 1)
    keep = norm | pos
    lab = pos.astype(np.int64)
    out = {"mixed": auc(s[keep], lab[keep])}
    num, den = 0.0, 0
    for p in ("oct", "nov"):
        m = keep & (src == p)
        k = int(lab[m].sum())
        if 0 < k < int(m.sum()):
            num, den = num + auc(s[m], lab[m]) * k, den + k
    out["period"] = num / den if den else float("nan")
    num, den = 0.0, 0
    for t in set(tool[pos].tolist()):
        v, n = pos & (tool == t), norm & (tool == t)
        if n.sum():
            num, den = num + auc(s[v | n], lab[v | n]) * int(v.sum()), den + int(v.sum())
    out["tool"] = num / den if den else float("nan")
    return out


def group_center(s, groups, scale=False, min_n=4):
    out = np.asarray(s, dtype=np.float64).copy()
    gmed, giqr = np.median(out), np.subtract(*np.percentile(out, [75, 25])) or 1.0
    for g in set(groups.tolist()):
        m = groups == g
        if m.sum() >= min_n:
            med = np.median(s[m])
            iqr = np.subtract(*np.percentile(s[m], [75, 25]))
            out[m] = (s[m] - med) / (iqr if (scale and iqr > 1e-9) else 1.0)
        else:
            out[m] = (s[m] - gmed) / (giqr if scale else 1.0)
    return out


def load(split):
    em = {}
    for arch in R.ARCHS:
        for w in R.WEIGHT_RULES:
            em[f"{arch}_{w}"] = [np.load(R.OUT / "em" / f"{arch}_{w}_r{k}.npz")[f"scores_{split}"][EPOCH - 1].astype(np.float64) for k in R.REPEATS]
    p = {sid: np.load(R.OUT / "p" / f"{sid}.npz")[f"scores_{split}"].astype(np.float64) for sid in ("P1", "P2", "P3", "P4", "P5", "P6")}
    return em, p


res = {}
for split in ("validation", "test"):
    rows = D["idx"][split]
    em, p = load(split)
    run, tool, src = D["unit_id"][rows].astype(str), D["tool"][rows].astype(str), D["source"][rows].astype(str)
    base3 = em["EM64_w60"]
    V = {}
    V["0. 64차원·60배, 반복 하나씩 (지금 값)"] = base3                     # list -> mean of metrics
    seed = np.mean(base3, axis=0)
    V["1. 반복 3번의 점수 평균"] = seed
    em_all = np.mean([rank01(s) for cfg in em.values() for s in cfg], axis=0)
    V["2. Argus-V-em 12개 설정 전부 평균(순위)"] = em_all
    em15 = np.mean([rank01(s) for c in ("EM32_w15", "EM64_w15", "EM128_w15", "LINEAR_w15") for s in em[c]], axis=0)
    V["2b. Argus-V-em 15배 설정 4개 평균(순위)"] = em15
    for sid in ("P1", "P3", "P5"):
        V[f"3. Argus-V-p {sid} 단독"] = p[sid]
        V[f"4. 64차원·60배 + Argus-V-p {sid} (순위 평균)"] = (rank01(seed) + rank01(p[sid])) / 2
    V["4b. em 12개 평균 + Argus-V-p P3 + P5 (순위 평균)"] = (em_all + rank01(p["P3"]) + rank01(p["P5"])) / 3
    V["5. 같은 실행의 평균 점수를 뺌"] = group_center(seed, run, min_n=2)
    V["6. 같은 도구의 중앙값을 뺌 (도구별 보정)"] = group_center(seed, tool)
    V["6b. 같은 도구의 중앙값·폭으로 표준화"] = group_center(seed, tool, scale=True)
    V["7. 같은 시기의 중앙값·폭으로 표준화"] = group_center(seed, src, scale=True)
    V["8. P3 점수에 도구별 보정"] = group_center(p["P3"], tool)
    res[split] = {}
    for name, s in V.items():
        if isinstance(s, list):
            ms = [{w: metrics(x, split, w) for w in ("all", "visible")} for x in s]
            res[split][name] = {w: {k: float(np.mean([m[w][k] for m in ms])) for k in ("mixed", "period", "tool")} for w in ("all", "visible")}
        else:
            res[split][name] = {w: metrics(s, split, w) for w in ("all", "visible")}
names = list(res["test"])
for w, ko in (("all", "위반 전체"), ("visible", "근거가 보인 위반")):
    print(f"\n=== {ko}: validation (mixed / period / tool) | test (mixed / period / tool)")
    for n in names:
        a, b = res["validation"][n][w], res["test"][n][w]
        print(f"{n:48s} {a['mixed']:.3f} {a['period']:.3f} {a['tool']:.3f} | {b['mixed']:.3f} {b['period']:.3f} {b['tool']:.3f}")
(ROOT / "reports/risk-loop/resplit-1117/run01/auroc_levers.json").write_text(json.dumps(
    {"note": "label-free variants built from saved scores of run01 at epoch 67; nothing fitted. mixed = all calls, period = inside each "
             "collection period, tool = inside each tool with a positive and a normal call. Exploratory: both validation and test were looked at.",
     "results": res}, ensure_ascii=False, indent=1), encoding="utf-8")

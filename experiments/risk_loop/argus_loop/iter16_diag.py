"""Iteration 16 diagnostics (2026-11-13). NOT model tries: no new candidate is selected or scored on the
judging metric. Train split only; the frozen evaluate.py (v4) is only imported, never modified.
Label view: features_labels_v2 (labels v2). Everything below was fixed in this header BEFORE the first run.

D16-1  Overfit or not? The existing best model T7-a (recipe unchanged) fitted on ALL judged train rows and
       scored on the same rows (in-sample) vs its family-grouped out-of-fold value (fold seeds 0-2), for the
       ensemble and for each of its three members. Per judging cell as well.
D16-2  Step order inside the judging cells: within-cell AUROC of "earlier step = violation" (-step_index),
       share of violations / normals that are the FIRST call of that tool in their trajectory, and the
       within-cell rank correlation between the saved T7-a out-of-fold score (iter12_remeasure) and step order.
D16-3  Report track as a high-power testbed (never part of the judging metric): November submit_result rows
       only (one tool, many scenarios). Family-grouped 5-fold CV, fold seeds 0-2, fixed settings, no selection:
         R1 L23:max   robust scale -> PCA 32 -> class-balanced logistic C=0.1   (recipe of T7-a's pointwise member)
         R2 L16:pre   same
         R3 L20:pre   same
         R4 L20:rend  same
         R5 L23:pre   same
         R6 concat of R1..R4 embeddings (128 dims), C=0.1
         R7 L23:max   PCA 128, C=0.01
       Learning curve for R1 and R6: 25% / 50% of the training families (3 repeats each) vs 100%.
       All seven numbers are reported; none is picked as "the" result.

Usage: py -3.11 experiments/risk_loop/argus_loop/iter16_diag.py
"""
from __future__ import annotations

import csv
import json
import os
import sys
import time
from collections import Counter
from pathlib import Path

for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ.setdefault(_v, "2")

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop import harness as H  # noqa: E402
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402
from experiments.risk_loop.argus_loop import iter01_common as C1  # noqa: E402
from experiments.risk_loop.argus_loop import iter06_models as M6  # noqa: E402
from experiments.risk_loop.argus_loop import iter06_scan as S6  # noqa: E402
from experiments.risk_loop.argus_loop import iter07_models as M7  # noqa: E402
from experiments.risk_loop.argus_loop import iter11_diag_models as DM  # noqa: E402

SHA = "a7c36eafdf994f98b61895be4e4b8d237740d0018422d12febab8deb9df0130d"
ART = REPO_ROOT / "artifacts" / "risk-loop" / "argus-v1-loop"
V2 = ART / "features_labels_v2"
OUT = REPO_ROOT / "reports" / "risk-loop" / "argus-v1" / "loop" / "iter-16"
SEEDS = [0, 1, 2]


def log(*a):
    print(time.strftime("%H:%M:%S"), *a, flush=True)


def cells(rows):
    g, y = E.headline_groups(rows), rows.y
    out = []
    for c in sorted(set(g.tolist())):
        m = np.nonzero(g == c)[0]
        p = int(y[m].sum())
        if p >= E.MIN_POS and len(m) - p >= E.MIN_NEG:
            out.append((c, m))
    return out


def wt(scores, rows):
    return E.within_tool_auroc(scores, rows.y, E.headline_groups(rows))["value"]


def per_cell(scores, rows, cl):
    y = rows.y
    return {c: float(H.auroc(np.asarray(scores)[m], y[m])) for c, m in cl}


def cv_scores(fp, rows, seeds=SEEDS):
    y = rows.y
    out = []
    for s in seeds:
        oof = np.full(len(rows), np.nan)
        for a, b in E.make_folds(rows, 5, s):
            oof[b] = fp(a, y[a], b)
        out.append(oof)
    return out


def scenario_col(root, rows):
    want = set(int(r) for r in rows.row_id.tolist())
    sid = {}
    with open(Path(root) / "steps.csv", newline="", encoding="utf-8") as h:
        for rec in csv.DictReader(h):
            r = int(rec["row"])
            if r in want:
                assert rec["split"] == "train"
                sid[r] = rec["scenario_id"]
    return np.asarray([sid[int(r)] for r in rows.row_id.tolist()], dtype=object)


# ------------------------------------------------------------------------------------------------ D16-1

def d16_1(res):
    data, rows, info = C1.headline_data(V2)
    assert set(rows.split.tolist()) == {"train"}
    y, n = rows.y, len(rows)
    cl = cells(rows)
    log("judged rows", n, "violations", int(y.sum()), "cells", len(cl), "cell violations", sum(int(y[m].sum()) for _, m in cl))
    feats = DM.load_feats(data, rows, ["L23:max", "L16:pre"])
    fp, store = DM.make_t7a(feats, rows)
    ctx = S6.model_ctx(rows)
    allpos = np.arange(n)

    def comp_fp(comp):
        def f(a, ya, b):
            return M6._component_scores(comp, store, ctx, np.asarray(a), np.asarray(ya).astype(np.int64), np.asarray(b))[1]
        return f

    models = {"T7-a (ensemble)": fp}
    for comp in M6.ENSEMBLE:
        models[f"member {comp['name']} ({comp['rep']}, {comp['kind']})"] = comp_fp(comp)
    out = {}
    for name, f in models.items():
        s_in = f(allpos, y, allpos)
        oofs = cv_scores(f, rows)
        o_seed = [wt(o, rows) for o in oofs]
        pc_in = per_cell(s_in, rows, cl)
        pc_oof = {c: float(np.mean([H.auroc(o[m], y[m]) for o in oofs])) for c, m in cl}
        out[name] = {"in_sample": wt(s_in, rows), "oof_mean": float(np.mean(o_seed)), "oof_per_seed": o_seed,
                     "pooled_in_sample": float(H.auroc(s_in, y)),
                     "pooled_oof": float(np.mean([H.auroc(o, y) for o in oofs])),
                     "per_cell_in_sample": pc_in, "per_cell_oof": pc_oof}
        log("D16-1", name, "in-sample", round(out[name]["in_sample"], 4), "OOF", round(out[name]["oof_mean"], 4))
    res["D16-1"] = {"rows": n, "violations": int(y.sum()),
                    "cells": {c: {"violations": int(y[m].sum()), "normals": int(len(m) - y[m].sum())} for c, m in cl},
                    "models": out}
    return rows, cl


# ------------------------------------------------------------------------------------------------ D16-2

def d16_2(res, rows, cl):
    y = rows.y
    step = np.asarray(rows.step_index, dtype=np.float64)
    traj = rows.trajectory_id.astype(str)
    tool = rows.tool.astype(str)
    order = {}
    for i in np.argsort(step, kind="stable"):
        order.setdefault((traj[i], tool[i]), []).append(i)
    first = np.zeros(len(rows), bool)
    rank_in = np.zeros(len(rows))
    for k, idx in order.items():
        first[idx[0]] = True
        for r, i in enumerate(idx):
            rank_in[i] = r
    p = ART / "iter12_remeasure" / "oof_v2_T7-a_seed0-9.npy"
    O = np.load(p)
    assert O.shape[1] == len(rows), (O.shape, len(rows))
    s = O.mean(0)
    per, num, den = {}, 0.0, 0
    num2 = 0.0
    for c, m in cl:
        pos = int(y[m].sum())
        a_step = float(H.auroc(-step[m], y[m]))
        a_rank = float(H.auroc(-rank_in[m], y[m]))
        rho = E._spearman(s[m], -step[m])
        per[c] = {"violations": pos, "normals": int(len(m) - pos),
                  "auroc_earlier_step": a_step, "auroc_earlier_same_tool_call": a_rank,
                  "violations_first_call_of_tool": int(first[m][y[m] == 1].sum()),
                  "normals_first_call_of_tool": int(first[m][y[m] == 0].sum()),
                  "t7a_oof_auroc": float(np.mean([H.auroc(o[m], y[m]) for o in O])),
                  "spearman_t7a_score_vs_earlier_step": rho}
        num += a_step * pos
        num2 += a_rank * pos
        den += pos
    res["D16-2"] = {"weighted_auroc_earlier_step": num / den, "weighted_auroc_earlier_same_tool_call": num2 / den,
                    "t7a_oof_10seed": float(np.mean([wt(o, rows) for o in O])), "per_cell": per}
    log("D16-2 earlier-step AUROC", round(num / den, 4), "earlier same-tool call", round(num2 / den, 4))


# ------------------------------------------------------------------------------------------------ D16-3

def d16_3(res):
    from sklearn.linear_model import LogisticRegression

    data, rows, info = C1.report_data(V2)
    assert set(rows.split.tolist()) == {"train"}
    keep = np.nonzero((rows.tool.astype(str) == "submit_result") & (rows.source.astype(str) == "nov"))[0]
    rows = rows.subset(keep)
    y, n = rows.y, len(rows)
    scen = scenario_col(V2, rows)
    fam = rows.family.astype(str)
    desc = {"rows": n, "violations": int(y.sum()), "normals": int(n - y.sum()),
            "trajectories": int(len(set(rows.trajectory_id.tolist()))),
            "scenarios": int(len(set(scen.tolist()))), "scenarios_with_violation": int(len(set(scen[y == 1].tolist()))),
            "families": int(len(set(fam.tolist()))), "families_with_violation": int(len(set(fam[y == 1].tolist()))),
            "label_status": dict(Counter(rows.label_status.tolist())),
            "violations_per_family": dict(sorted(Counter(fam[y == 1].tolist()).items(), key=lambda kv: -kv[1]))}
    log("D16-3 rows", {k: v for k, v in desc.items() if k != "violations_per_family"})
    reps = ["L23:max", "L16:pre", "L20:pre", "L20:rend", "L23:pre"]
    feats = DM.load_feats(data, rows, reps)
    cache = {}

    def emb(rep, a, k):
        key = (rep, k, hash(np.asarray(a).tobytes()))
        if key not in cache:
            cache[key] = M7.robust_embed(feats[rep], a, kmax=k)
        return cache[key]

    def make(spec):
        def f(a, ya, b):
            a, b = np.asarray(a, dtype=np.int64), np.asarray(b, dtype=np.int64)
            Z = np.concatenate([emb(r, a, spec["k"]) for r in spec["reps"]], axis=1).astype(np.float64)
            if len(np.unique(ya)) < 2:
                return np.zeros(len(b))
            lr = LogisticRegression(C=spec["C"], class_weight="balanced", max_iter=3000)
            lr.fit(Z[a], np.asarray(ya).astype(np.int64))
            return lr.decision_function(Z[b])
        return f

    specs = {"R1 L23:max k32": {"reps": ["L23:max"], "k": 32, "C": 0.1},
             "R2 L16:pre k32": {"reps": ["L16:pre"], "k": 32, "C": 0.1},
             "R3 L20:pre k32": {"reps": ["L20:pre"], "k": 32, "C": 0.1},
             "R4 L20:rend k32": {"reps": ["L20:rend"], "k": 32, "C": 0.1},
             "R5 L23:pre k32": {"reps": ["L23:pre"], "k": 32, "C": 0.1},
             "R6 concat(R1-R4) 128": {"reps": ["L23:max", "L16:pre", "L20:pre", "L20:rend"], "k": 32, "C": 0.1},
             "R7 L23:max k128": {"reps": ["L23:max"], "k": 128, "C": 0.01}}

    def run(spec, frac=None, rep=0):
        f = make(spec)
        pooled, fold_mean, insample = [], [], []
        for s in SEEDS:
            oof = np.full(n, np.nan)
            fa = []
            for fi, (a, b) in enumerate(E.make_folds(rows, 5, s)):
                if frac is not None:
                    comp = E.group_components(rows.subset(a))
                    u = np.unique(comp)
                    rng = np.random.default_rng(10_000 * rep + 100 * s + fi)
                    for _ in range(50):
                        pick = rng.choice(u, size=max(2, int(round(frac * len(u)))), replace=False)
                        a2 = a[np.isin(comp, pick)]
                        if 0 < y[a2].sum() < len(a2):
                            break
                    a = a2
                oof[b] = f(a, y[a], b)
                if 0 < y[b].sum() < len(b):
                    fa.append((float(H.auroc(oof[b], y[b])), int(y[b].sum())))
                if frac is None and fi == 0:
                    insample.append(float(H.auroc(f(a, y[a], a), y[a])))
            pooled.append(float(H.auroc(oof, y)))
            fold_mean.append(float(sum(v * w for v, w in fa) / sum(w for _, w in fa)))
        return {"pooled_oof_auroc": float(np.mean(pooled)), "per_seed": pooled,
                "within_fold_auroc": float(np.mean(fold_mean)),
                "train_fold_in_sample_auroc": float(np.mean(insample)) if insample else None}

    out = {}
    for name, spec in specs.items():
        out[name] = run(spec)
        log("D16-3", name, {k: (round(v, 4) if isinstance(v, float) else v) for k, v in out[name].items() if k != "per_seed"})
    curve = {}
    for name in ("R1 L23:max k32", "R6 concat(R1-R4) 128"):
        curve[name] = {"1.0": out[name]["within_fold_auroc"]}
        for frac in (0.25, 0.5):
            vals = [run(specs[name], frac=frac, rep=r)["within_fold_auroc"] for r in range(3)]
            curve[name][str(frac)] = {"mean": float(np.mean(vals)), "repeats": vals}
            log("D16-3 curve", name, frac, [round(v, 4) for v in vals])
    # trivial baselines on the same rows
    base = {"prefix_length": float(H.auroc(rows.prefix_length, y)), "step_index": float(H.auroc(rows.step_index, y)),
            "n_obs": float(H.auroc(rows.n_obs, y))}
    res["D16-3"] = {"rows": desc, "models": out, "learning_curve_within_fold": curve, "single_variable_auroc": base}
    log("D16-3 baselines", base)


def main(parts):
    """parts: "order" = D16-2 only (counting from steps.csv + saved scores, fits NOTHING);
    "t7a" = D16-1 (refits the existing T7-a); "report" = D16-3 (fits logistic probes on the report track).
    "t7a" and "report" fit models: run them only after the user approved (2026-11-13 instruction)."""
    assert E.evaluate_sha256() == SHA, E.evaluate_sha256()
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / "diag16.json"
    res = json.loads(path.read_text(encoding="utf-8")) if path.is_file() else {}
    res.update({"evaluate_sha256": E.evaluate_sha256(), "label_view": str(V2), "note": "diagnostics, not model tries"})
    for part in parts:
        if part == "order":
            _, rows, _ = C1.headline_data(V2)
            assert set(rows.split.tolist()) == {"train"}
            d16_2(res, rows, cells(rows))
        elif part == "t7a":
            d16_1(res)
        elif part == "report":
            d16_3(res)
        else:
            raise SystemExit(f"unknown part {part!r}")
        path.write_text(json.dumps(E.to_jsonable(res), indent=1, ensure_ascii=False), encoding="utf-8")
    assert E.evaluate_sha256() == SHA
    log("DONE", parts)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("usage: iter16_diag.py order | t7a | report  (t7a/report fit models: user approval first)")
    main(sys.argv[1:])

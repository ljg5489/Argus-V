"""Iteration 1 experiments (train only; validation/test never read).

Phases (each attempt cached as JSON under artifacts/risk-loop/argus-v1-loop/iter01/attempts/):
  A  H1-0 baselines (2) + H1-1 representation scan (24 = 6 layers x 4 pools), nested CV, no bootstrap
  B  H1-2 shortcut controls on the 3 best H1-1 representations: prefix_length residualisation (allowed)
     and per-source standardisation (diagnostic only, forbidden at scoring)
  C  full evaluate.evaluate() (bootstrap CI, shuffle a/b, baselines) for <=3 selected candidates
     + report track (report tools only) nested CV for the same structures
Writes reports/risk-loop/argus-v1/loop/iter-01/cv_report.json.

Usage: py -3.11 experiments/risk_loop/argus_loop/iter01_scan.py [--phase A|B|C|all] [--jobs 6]
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

ART = REPO_ROOT / "artifacts" / "risk-loop" / "argus-v1-loop" / "iter01"
REP = REPO_ROOT / "reports" / "risk-loop" / "argus-v1" / "loop" / "iter-01"
ATT = ART / "attempts"

GRID = [{"k": k, "C": C} for k in (10, 32, 128) for C in (0.001, 0.01, 0.1)]  # simplest first (ties -> first)
TIE = 0.005


def spec_list_a():
    specs = [
        {"id": "H1-0a", "hyp": "H1-0", "layer": 16, "pool": "max", "model": "pca_logreg",
         "fixed": {"weight": "class"}, "grid": [{"k": 10, "C": 1.0}], "note": "Argus-V1 default exactly"},
        {"id": "H1-0b", "hyp": "H1-0", "layer": 16, "pool": "max", "model": "pca_logreg",
         "fixed": {"weight": "source_class"}, "grid": [{"k": 10, "C": 1.0}],
         "note": "Argus-V1 default + source x class balanced weights"},
    ]
    for L in (8, 11, 14, 16, 20, 23):
        for p in ("max", "mean", "pre", "rend"):
            specs.append({"id": f"H1-1-L{L:02d}-{p}", "hyp": "H1-1", "layer": L, "pool": p, "model": "pca_logreg",
                          "fixed": {"weight": "source_class", "kmax": 128}, "grid": GRID})
    return specs


def spec_list_b(top_reps):
    specs = []
    for L, p in top_reps:
        specs.append({"id": f"H1-2r-L{L:02d}-{p}", "hyp": "H1-2", "layer": L, "pool": p, "model": "pca_logreg",
                      "fixed": {"weight": "source_class", "kmax": 128, "resid": True}, "grid": GRID,
                      "note": "PCA components residualised on log prefix_length in-fold"})
        specs.append({"id": f"H1-2s-L{L:02d}-{p}", "hyp": "H1-2", "layer": L, "pool": p,
                      "model": "pca_logreg_per_source_scale", "diagnostic": True,
                      "fixed": {"weight": "source_class", "kmax": 128}, "grid": GRID,
                      "note": "DIAGNOSTIC: per-source standardisation uses source at scoring (forbidden)"})
    return specs


def _limit_threads(n=2):
    for v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
        os.environ[v] = str(n)
    try:
        from threadpoolctl import threadpool_limits
        threadpool_limits(n)
    except Exception:
        pass


def _summ(m):
    wt = m["within_tool"]
    return {"within_tool": wt["value"], "within_tool_per_seed": wt["per_seed"],
            "by_source": {s: v["value"] for s, v in wt["by_source"].items()},
            "by_source_per_seed": {s: v.get("per_seed") for s, v in wt["by_source"].items()},
            "n_tools": wt["n_tools"], "n_positives_included": wt["n_positives_included"],
            "per_tool": [{k: e[k] for k in ("tool", "n", "positives", "auroc")} for e in wt["per_tool"]
                         if e["included"]],
            "pooled_auroc": m["pooled_auroc"], "pooled_auroc_by_source": m["pooled_auroc_by_source"],
            "ci95": wt.get("ci95"), "correlation": m.get("correlation")}


def run_attempt(spec, mode="scan"):
    """mode: 'scan' (nested CV + metrics without bootstrap), 'full' (evaluate.evaluate), 'report'."""
    _limit_threads(2)
    from experiments.risk_loop.argus_loop import evaluate as E
    from experiments.risk_loop.argus_loop import iter01_common as C
    from experiments.risk_loop.argus_loop import models as M

    out_path = ATT / f"{spec['id']}.{mode}.json"
    if out_path.is_file():
        return json.loads(out_path.read_text(encoding="utf-8"))
    t0 = time.time()
    data, rows, rinfo = (C.report_data() if mode == "report" else C.headline_data())
    X = C.features(data, rows, spec["layer"], spec["pool"])
    ctx = C.ctx_for(rows)
    make = M.grid_maker(spec["model"], X, ctx, spec["fixed"], M.LRU(8))
    res = {"spec": spec, "mode": mode, "rows": rinfo, "evaluate_sha256": E.evaluate_sha256()}
    if mode == "full":
        r = E.evaluate(make_fit_predict=make, grid=spec["grid"], X_or_rowids=None, rows=rows, name=spec["id"],
                       include_oof=True)
        oof = r["cv"].pop("oof")
        np.save(ART / f"oof_{spec['id']}.full.npy", np.asarray([oof[k] for k in sorted(oof)], dtype=np.float32))
        r["cv"].pop("fold_id", None)
        res.update({"summary": _summ(r["metrics"]), "baselines": r["metrics"].get("baselines"),
                    "shuffle_source": {k: r["shuffle_source"][k] for k in
                                       ("within_tool", "within_tool_mean", "within_tool_by_source_mean", "pass")},
                    "shuffle_source_family": {k: r["shuffle_source_family"][k] for k in
                                              ("within_tool", "within_tool_mean", "within_tool_by_source_mean")},
                    "seed_stability": r["seed_stability"], "selection": r["cv"]["selection"],
                    "gate_numbers_for_evaluator": r["gate"]})
    else:
        cv = E.nested_cv(make, spec["grid"], None, rows)
        m = E.metrics(cv, rows, bootstrap=0, baselines=False)
        np.save(ART / f"oof_{spec['id']}.{mode}.npy",
                np.asarray([cv["oof"][k] for k in sorted(cv["oof"])], dtype=np.float32))
        res.update({"summary": _summ(m), "selection": cv["selection"]})
    res["seconds"] = round(time.time() - t0, 1)
    out_path.write_text(json.dumps(E.to_jsonable(res), indent=1, ensure_ascii=False), encoding="utf-8")
    return res


def _parallel(specs, mode, jobs):
    from joblib import Parallel, delayed
    return Parallel(n_jobs=jobs, backend="loky", verbose=5)(delayed(run_attempt)(s, mode) for s in specs)


def _rank(results):
    elig = [r for r in results if not r["spec"].get("diagnostic") and r["summary"]["within_tool"] is not None]
    return sorted(elig, key=lambda r: -r["summary"]["within_tool"])


def _complexity(spec):
    g = spec["grid"]
    return (int(bool(spec["fixed"].get("resid"))), max(x["k"] for x in g), len(g))


def select(results, n=3):
    """Pre-registered: highest seed-mean within-tool AUROC; within TIE of a better one -> simpler first."""
    ranked = _rank(results)
    if not ranked:
        return []
    best = ranked[0]["summary"]["within_tool"]
    near = [r for r in ranked if best - r["summary"]["within_tool"] <= TIE]
    near.sort(key=lambda r: (_complexity(r["spec"]), -r["summary"]["within_tool"]))
    rest = [r for r in ranked if r not in near]
    return (near + rest)[:n]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--phase", default="all")
    ap.add_argument("--jobs", type=int, default=6)
    a = ap.parse_args()
    ATT.mkdir(parents=True, exist_ok=True)
    REP.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    A = _parallel(spec_list_a(), "scan", a.jobs)
    print("phase A done", round(time.time() - t0), "s", flush=True)
    if a.phase == "A":
        return
    h11 = [r for r in A if r["spec"]["hyp"] == "H1-1"]
    top_reps = [(r["spec"]["layer"], r["spec"]["pool"]) for r in _rank(h11)[:3]]
    B = _parallel(spec_list_b(top_reps), "scan", a.jobs)
    print("phase B done", round(time.time() - t0), "s", flush=True)
    if a.phase == "B":
        return
    scans = A + B
    chosen = select(scans, 3)
    # always evaluate the Argus-V1 default too, as a reference (not a candidate)
    full_specs = [r["spec"] for r in chosen]
    if not any(s["id"] == "H1-0b" for s in full_specs):
        full_specs.append(next(r["spec"] for r in A if r["spec"]["id"] == "H1-0b"))
    F = _parallel(full_specs, "full", min(a.jobs, len(full_specs)))
    R = _parallel(full_specs, "report", min(a.jobs, len(full_specs)))
    print("phase C done", round(time.time() - t0), "s", flush=True)

    from experiments.risk_loop.argus_loop import evaluate as E
    attempts = []
    for r in scans:
        s = r["summary"]
        attempts.append({"id": r["spec"]["id"], "hypothesis": r["spec"]["hyp"], "layer": r["spec"]["layer"],
                         "pool": r["spec"]["pool"], "model": r["spec"]["model"], "fixed": r["spec"]["fixed"],
                         "grid": r["spec"]["grid"], "diagnostic": bool(r["spec"].get("diagnostic")),
                         "note": r["spec"].get("note"), "within_tool": s["within_tool"],
                         "within_tool_per_seed": s["within_tool_per_seed"], "by_source": s["by_source"],
                         "pooled_auroc": s["pooled_auroc"], "per_tool": s["per_tool"],
                         "chosen_grid_index": r["selection"].get("chosen"),
                         "corr_score_log_prefix_length": (s.get("correlation") or {}).get(
                             "pearson_score_log_prefix_length"),
                         "seconds": r["seconds"]})
    report = {
        "iteration": 1, "date": "2026-11-08", "evaluate_sha256": E.evaluate_sha256(),
        "validation_touched": False, "test_touched": False,
        "labels": "October confirmed + November DRAFT rule labels (original_policy_label)",
        "rows_headline": A[0]["rows"], "rows_report_track": R[0]["rows"] if R else None,
        "selection_rule": "highest seed-mean nested-CV within-tool AUROC; within 0.005 -> simpler "
                          "(no resid, smaller max k, smaller grid); diagnostic attempts excluded",
        "n_attempts_scan": len(scans), "n_attempts_full_evaluate": len(F), "n_attempts_report_track": len(R),
        "n_attempts_total_model_configs": len(scans),
        "attempts": attempts,
        "selected": [r["spec"]["id"] for r in chosen],
        "full_evaluate": {r["spec"]["id"]: {k: r[k] for k in r if k not in ("spec",)} for r in F},
        "report_track": {r["spec"]["id"]: {"summary": r["summary"], "selection": r["selection"],
                                           "seconds": r["seconds"]} for r in R},
        "runtime_seconds_this_run": round(time.time() - t0, 1),
        "runtime_seconds_sum_of_attempts": round(sum(r["seconds"] for r in scans + F + R), 1),
    }
    (REP / "cv_report.json").write_text(json.dumps(E.to_jsonable(report), indent=1, ensure_ascii=False),
                                        encoding="utf-8")
    print("wrote", REP / "cv_report.json")


if __name__ == "__main__":
    main()

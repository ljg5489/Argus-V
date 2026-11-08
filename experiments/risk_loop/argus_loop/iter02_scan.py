"""Iteration 2 experiments (train only; validation/test never read). Plan: reports/.../iter-02/plan.md.

Phases (each attempt cached as JSON under artifacts/risk-loop/argus-v1-loop/iter02/attempts/, key includes
the attempt spec, the evaluated data hash, and the sha256 of models.py / iter02_common.py / evaluate.py):
  A  H2-1 within-tool training signal on L23 max (a centred LogReg, b pairwise rank, c group weights)
     + H2-1b on L16 max                                                                   4 attempts
  B  H2-3 length/step direction removal (len_rounds 1, 4) on the best A model (L23 max)   2 attempts
  C  H2-2 representations with the best A/B configuration                                 3 attempts
  D  H2-4 trajectory delta (best configuration; iteration-1 pca_logreg)                   2 attempts
  F  full evaluate.evaluate() for the top 3 (bootstrap CI, shuffles a/b, baselines) -- not new attempts
OOF scores of every run are saved (npy, seed order 0,1,2) so a later harness version can re-score them.

Usage: py -3.11 experiments/risk_loop/argus_loop/iter02_scan.py [--jobs 2] [--phase all|A|B|C|D]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

ART = REPO_ROOT / "artifacts" / "risk-loop" / "argus-v1-loop" / "iter02"
REP = REPO_ROOT / "reports" / "risk-loop" / "argus-v1" / "loop" / "iter-02"
ATT = ART / "attempts"
HERE = Path(__file__).resolve().parent

GRID = [{"k": k, "C": C} for k in (10, 32, 128) for C in (0.001, 0.01, 0.1)]  # simplest first
TIE = 0.005
ITER1_BEST = 0.657171034094111  # H1-2r-L23-max seed-mean (iter-01/cv_report.json)


def _spec(id_, hyp, rep, model, fixed=None, note=None):
    f = {"kmax": 128}
    f.update(fixed or {})
    return {"id": id_, "hyp": hyp, "rep": rep, "model": model, "fixed": f, "grid": GRID, "note": note}


def specs_a():
    return [
        _spec("H2-1a-L23", "H2-1a", "L23:max", "tool_centred_logreg", note="tool x source centred LogReg"),
        _spec("H2-1b-L23", "H2-1b", "L23:max", "pairwise_rank", note="same tool x source pair ranking"),
        _spec("H2-1c-L23", "H2-1c", "L23:max", "tool_weighted_logreg", note="informative-stratum normal weights"),
        _spec("H2-1b-L16", "H2-1b", "L16:max", "pairwise_rank", note="layer consistency check"),
    ]


def specs_b(best_a):
    return [_spec(f"H2-3-m{m}", "H2-3", "L23:max", best_a["model"], {"len_rounds": m},
                  note=f"best A model ({best_a['id']}) + {m} ridge deflation round(s) for log length and step")
            for m in (1, 4)]


def specs_c(best):
    reps = [("H2-2-rendpre", "L23:rend-pre"), ("H2-2-maxmean", "L23:max-mean"), ("H2-2-cat1623", "L16:max+L23:max")]
    lr = best["fixed"].get("len_rounds", 0)
    return [_spec(i, "H2-2", r, best["model"], {"len_rounds": lr} if lr else None,
                  note=f"configuration of {best['id']}") for i, r in reps]


def specs_d(best):
    lr = best["fixed"].get("len_rounds", 0)
    return [_spec("H2-4-best", "H2-4", "traj:L23:max", best["model"], {"len_rounds": lr} if lr else None,
                  note=f"trajectory delta + configuration of {best['id']}"),
            _spec("H2-4-iter1", "H2-4", "traj:L23:max", "pca_logreg", {"weight": "source_class"},
                  note="trajectory delta + iteration-1 model (no tool training signal)")]


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
            "ci95": wt.get("ci95"), "correlation": m.get("correlation"),
            "v2_tool_only_reference": wt.get("v2_tool_only_reference")}


def _key(spec, dh):
    from experiments.risk_loop.argus_loop import iter02_common as C2
    h = hashlib.sha256(json.dumps(spec, sort_keys=True).encode())
    h.update(dh.encode())
    for f in ("models.py", "iter02_common.py", "evaluate.py"):
        h.update(C2.file_sha(HERE / f).encode())
    return h.hexdigest()[:16]


def run_attempt(spec, mode="scan"):
    """mode: 'scan' (nested CV + metrics without bootstrap) or 'full' (evaluate.evaluate)."""
    _limit_threads(2)
    from experiments.risk_loop.argus_loop import evaluate as E
    from experiments.risk_loop.argus_loop import iter01_common as C1
    from experiments.risk_loop.argus_loop import iter02_common as C2
    from experiments.risk_loop.argus_loop import models as M

    data, rows, rinfo = C1.headline_data()
    dh = C2.data_hash(rows)
    key = _key(spec, dh)
    out_path = ATT / f"{spec['id']}.{mode}.{key}.json"
    if out_path.is_file():
        return json.loads(out_path.read_text(encoding="utf-8"))
    t0 = time.time()
    X, blocks = C2.representation(data, rows, spec["rep"])
    ctx = C2.ctx_for(rows)
    fixed = dict(spec["fixed"])
    if blocks:
        fixed["blocks"] = blocks
    make = M.grid_maker(spec["model"], X, ctx, fixed, M.LRU(8))
    res = {"spec": spec, "mode": mode, "rows": rinfo, "data_hash": dh, "cache_key": key,
           "evaluate_sha256": E.evaluate_sha256()}
    if mode == "full":
        r = E.evaluate(make_fit_predict=make, grid=spec["grid"], X_or_rowids=None, rows=rows, name=spec["id"],
                       include_oof=True)
        oof = r["cv"].pop("oof")
        np.save(ART / f"oof_{spec['id']}.full.npy", np.asarray([oof[k] for k in sorted(oof)], dtype=np.float64))
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
        np.save(ART / f"oof_{spec['id']}.scan.npy",
                np.asarray([cv["oof"][k] for k in sorted(cv["oof"])], dtype=np.float64))
        res.update({"summary": _summ(m), "selection": cv["selection"]})
    res["seconds"] = round(time.time() - t0, 1)
    out_path.write_text(json.dumps(E.to_jsonable(res), indent=1, ensure_ascii=False), encoding="utf-8")
    return res


def _parallel(specs, mode, jobs):
    from joblib import Parallel, delayed
    return Parallel(n_jobs=min(jobs, len(specs)), backend="loky", verbose=5)(
        delayed(run_attempt)(s, mode) for s in specs)


def _wt(r):
    v = r["summary"]["within_tool"]
    return -1.0 if v is None else v


def _complexity(spec):
    rep = spec["rep"]
    return (int(bool(spec["fixed"].get("len_rounds"))), int("traj:" in rep), int("+" in rep or "-" in rep))


def ranked(results):
    """Pre-registered: highest seed-mean within-tool AUROC; within TIE of the best -> simpler first."""
    rs = sorted([r for r in results if not r["spec"].get("diagnostic")], key=lambda r: -_wt(r))
    if not rs:
        return []
    best = _wt(rs[0])
    near = sorted([r for r in rs if best - _wt(r) <= TIE], key=lambda r: (_complexity(r["spec"]), -_wt(r)))
    return near + [r for r in rs if r not in near]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jobs", type=int, default=2)
    ap.add_argument("--phase", default="all")
    a = ap.parse_args()
    ATT.mkdir(parents=True, exist_ok=True)
    REP.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    A = _parallel(specs_a(), "scan", a.jobs)
    print("phase A done", round(time.time() - t0), "s", [(r["spec"]["id"], _wt(r)) for r in A], flush=True)
    if a.phase == "A":
        return
    best_a = ranked([r for r in A if r["spec"]["rep"] == "L23:max"])[0]["spec"]
    B = _parallel(specs_b(best_a), "scan", a.jobs)
    print("phase B done", round(time.time() - t0), "s", [(r["spec"]["id"], _wt(r)) for r in B], flush=True)
    best_ab = ranked([r for r in A + B if r["spec"]["rep"] == "L23:max"])[0]["spec"]
    CD = _parallel(specs_c(best_ab) + specs_d(best_ab), "scan", a.jobs)
    print("phase C/D done", round(time.time() - t0), "s", [(r["spec"]["id"], _wt(r)) for r in CD], flush=True)
    scans = A + B + CD
    top = ranked(scans)[:3]
    F = _parallel([r["spec"] for r in top], "full", a.jobs)
    print("phase F done", round(time.time() - t0), "s", flush=True)

    from experiments.risk_loop.argus_loop import evaluate as E
    attempts = []
    for r in scans:
        s = r["summary"]
        attempts.append({"id": r["spec"]["id"], "hypothesis": r["spec"]["hyp"], "rep": r["spec"]["rep"],
                         "model": r["spec"]["model"], "fixed": r["spec"]["fixed"], "grid": r["spec"]["grid"],
                         "note": r["spec"].get("note"), "within_tool": s["within_tool"],
                         "within_tool_per_seed": s["within_tool_per_seed"], "by_source": s["by_source"],
                         "by_source_per_seed": s["by_source_per_seed"],
                         "pooled_auroc": s["pooled_auroc"], "per_tool": s["per_tool"],
                         "v2_tool_only_reference": s.get("v2_tool_only_reference"),
                         "chosen_grid_index": r["selection"].get("chosen"),
                         "inner_scores": r["selection"].get("inner_scores"),
                         "corr_score_log_prefix_length": (s.get("correlation") or {}).get(
                             "pearson_score_log_prefix_length"),
                         "evaluate_sha256": r["evaluate_sha256"], "data_hash": r["data_hash"],
                         "cache_key": r["cache_key"], "seconds": r["seconds"]})
    full = {}
    for r in F:
        wt = r["summary"]["within_tool"]
        ls = (r["baselines"] or {}).get("length+step", {}).get("within_tool")
        sb = r["shuffle_source_family"]["within_tool_mean"]
        full[r["spec"]["id"]] = {k: r[k] for k in r if k != "spec"}
        full[r["spec"]["id"]]["candidate_rule"] = {
            "headline_minus_shuffle_b": None if sb is None else wt - sb,
            "headline_minus_length_step": None if ls is None else wt - ls,
            "counts": bool(sb is not None and ls is not None and wt - sb >= 0.10 and wt - ls >= 0.05)}
    report = {
        "iteration": 2, "date": "2026-11-08", "harness_version_used": "v3 (tool x source cells; v2 tool-only value kept as reference)",
        "evaluate_sha256_at_report": E.evaluate_sha256(),
        "validation_touched": False, "test_touched": False,
        "labels": "October confirmed + November DRAFT rule labels (original_policy_label)",
        "rows_headline": A[0]["rows"], "data_hash": A[0]["data_hash"],
        "selection_rule": "highest seed-mean nested-CV within-tool AUROC; within 0.005 -> simpler; top 3 get "
                          "full evaluate; counts as candidate only if headline - shuffle(b) >= 0.10 and "
                          "headline - length+step >= 0.05",
        "n_attempts_new": len(scans), "cumulative_attempts_after": 34 + len(scans),
        "iteration1_best_reference": ITER1_BEST,
        "phase_choices": {"best_A_L23": best_a["id"], "best_AB_L23": best_ab["id"]},
        "attempts": attempts, "full_evaluate": full,
        "runtime_seconds_this_run": round(time.time() - t0, 1),
        "runtime_seconds_sum_of_attempts": round(sum(r["seconds"] for r in scans + F), 1),
    }
    (REP / "cv_report.json").write_text(json.dumps(E.to_jsonable(report), indent=1, ensure_ascii=False),
                                        encoding="utf-8")
    print("wrote", REP / "cv_report.json", flush=True)


if __name__ == "__main__":
    main()

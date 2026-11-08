"""Iteration 3 experiments (train only; validation/test never read). Plan: reports/.../iter-03/plan.md.

Phases (attempt cache: artifacts/risk-loop/argus-v1-loop/iter03/attempts/, key = spec + universe data hash +
sha256 of iter03_common.py / iter03_models.py / models.py / evaluate.py):
  0  H3-0 reproduction of H2-1c through the iteration-3 code path (extra_mode none) -- sanity, NOT an attempt
  A  H3-1a..e training-data expansion with report-tool rows                                5 attempts
  B  H3-2a/b multi-task heads on the best A expansion setting                             2 attempts
  C  H3-3a/b/c previous-step context                                                      3 attempts
  F  top 3: evaluate.evaluate() (v4: 20 shuffles each) + full-shuffle nulls (report labels permuted too), 20 each
Usage: py -3.11 experiments/risk_loop/argus_loop/iter03_scan.py [--jobs 2] [--phase all|0|A]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from experiments.risk_loop.argus_loop import iter02_scan as S2  # noqa: E402  (helpers: _summ, _limit_threads)

ART = REPO_ROOT / "artifacts" / "risk-loop" / "argus-v1-loop" / "iter03"
REP = REPO_ROOT / "reports" / "risk-loop" / "argus-v1" / "loop" / "iter-03"
ATT = ART / "attempts"
HERE = Path(__file__).resolve().parent
GRID = S2.GRID
TIE = 0.005
PREV_BEST = 0.645  # H2-1c-L23 (iter-02/cv_report.json, v3)
LENGTH_STEP = 0.522
CUM_BEFORE = 45
N_SHUFFLE = None  # use the frozen harness default (v4: 20)


def _spec(id_, hyp, rep, fixed, note, diagnostic=False):
    f = {"kmax": 128}
    f.update(fixed)
    return {"id": id_, "hyp": hyp, "rep": rep, "model": "expand_factory", "fixed": f, "grid": GRID,
            "note": note, "diagnostic": diagnostic}


def spec_0():
    return [_spec("H3-0-repro", "H3-0", "L23:max", {"extra_mode": "none"},
                  "H2-1c through iteration-3 code (sanity, not an attempt)", diagnostic=True)]


def specs_a():
    return [
        _spec("H3-1a", "H3-1", "L23:max", {"w": 1.0}, "H2-1c + report rows (both classes), w=1"),
        _spec("H3-1b", "H3-1", "L23:max", {"w": 0.3}, "H2-1c + report rows (both classes), w=0.3"),
        _spec("H3-1c", "H3-1", "L23:max", {"w": 0.3, "extra_mode": "pos"}, "H2-1c + report positives only, w=0.3"),
        _spec("H3-1d", "H3-1", "L23:max", {"w": 1.0, "head_weight": "source_class"},
              "iteration-1 weighting (no informative-stratum up-weighting) + report rows w=1"),
        _spec("H3-1e", "H3-1", "L23:max", {"w": 1.0, "extra_balance": "family_class"},
              "H2-1c + report rows w=1, report weights equal per family x class"),
    ]


def _ext_fixed(best):
    return {k: v for k, v in best["fixed"].items() if k in ("w", "extra_mode", "extra_balance", "head_weight")}


def specs_b(best_a):
    f = _ext_fixed(best_a)
    if f.get("extra_mode") == "pos":  # multi-task needs report negatives too
        f = {"w": 1.0}
    return [_spec("H3-2a", "H3-2", "L23:max", {**f, "multitask": "action"}, f"multi-task, action head; {f}"),
            _spec("H3-2b", "H3-2", "L23:max", {**f, "multitask": "shared"}, f"multi-task, shared direction; {f}")]


def specs_c(best_ab):
    f = {k: v for k, v in best_ab["fixed"].items() if k != "kmax"}
    out = [_spec("H3-3a", "H3-3", "prev:L23:max", f, f"[x_t, x_prev] + {best_ab['id']} setting"),
           _spec("H3-3b", "H3-3", "dprev:L23:max", f, f"x_t - x_prev + {best_ab['id']} setting")]
    if f.get("extra_mode") != "none":
        out.append(_spec("H3-3c", "H3-3", "prev:L23:max", {"extra_mode": "none"}, "[x_t, x_prev] + H2-1c (no expansion)"))
    return out


def _key(spec, dh):
    from experiments.risk_loop.argus_loop import iter02_common as C2
    h = hashlib.sha256(json.dumps(spec, sort_keys=True).encode())
    h.update(dh.encode())
    for f in ("iter03_common.py", "iter03_models.py", "models.py", "evaluate.py"):
        h.update(C2.file_sha(HERE / f).encode())
    return h.hexdigest()[:16]


def _shuffle_summary(s):
    return {k: s[k] for k in ("within_tool", "within_tool_mean", "within_tool_by_source_mean", "pass") if k in s}


def run_attempt(spec, mode="scan"):
    S2._limit_threads(2)
    from experiments.risk_loop.argus_loop import evaluate as E
    from experiments.risk_loop.argus_loop import iter03_common as C3
    from experiments.risk_loop.argus_loop import iter03_models as M3
    from experiments.risk_loop.argus_loop import models as M

    u = C3.load_universe()
    dh = C3.data_hash(u)
    key = _key(spec, dh)
    out_path = ATT / f"{spec['id']}.{mode}.{key}.json"
    if out_path.is_file():
        return json.loads(out_path.read_text(encoding="utf-8"))
    t0 = time.time()
    X, blocks = C3.representation(u, spec["rep"])
    ctx = C3.ctx_for(u)
    fixed = dict(spec["fixed"])
    if blocks:
        fixed["blocks"] = blocks
    rows = u.head
    make = M3.grid_maker(X, ctx, fixed, M.LRU(8))
    res = {"spec": spec, "mode": mode, "rows": u.info, "data_hash": dh, "cache_key": key,
           "evaluate_sha256": E.evaluate_sha256()}
    if mode == "full":
        r = E.evaluate(make_fit_predict=make, grid=spec["grid"], X_or_rowids=None, rows=rows, name=spec["id"],
                       include_oof=True)  # v4 default n_shuffle (20)
        oof = r["cv"].pop("oof")
        np.save(ART / f"oof_{spec['id']}.full.npy", np.asarray([oof[k] for k in sorted(oof)], dtype=np.float64))
        r["cv"].pop("fold_id", None)
        modal = r["cv"]["selection"]["shuffle_uses_grid_index"]
        g = dict(spec["grid"][modal])
        full_null = {}
        for name, within in (("a_source", ("source",)), ("b_source_family", ("source", "family"))):
            p = dict(fixed)
            p.update(g)
            p["null_within"] = within
            nfp = M3.expand_factory(X, ctx, cache=M.LRU(8), **p)
            full_null[name] = _shuffle_summary(E.shuffle_test(nfp, rows, E.N_SHUFFLE, X_or_rowids=None, seed=0,
                                                              within=within))
        res.update({"summary": S2._summ(r["metrics"]), "baselines": r["metrics"].get("baselines"),
                    "shuffle_source_harness": _shuffle_summary(r["shuffle_source"]),
                    "shuffle_source_family_harness": _shuffle_summary(r["shuffle_source_family"]),
                    "shuffle_full_null": full_null,
                    "seed_stability": r["seed_stability"], "selection": r["cv"]["selection"],
                    "gate_numbers_for_evaluator": r["gate"]})
    else:
        cv = E.nested_cv(make, spec["grid"], None, rows)
        m = E.metrics(cv, rows, bootstrap=0, baselines=False)
        np.save(ART / f"oof_{spec['id']}.scan.npy",
                np.asarray([cv["oof"][k] for k in sorted(cv["oof"])], dtype=np.float64))
        res.update({"summary": S2._summ(m), "selection": cv["selection"]})
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
    f = spec["fixed"]
    return (int("prev:" in spec["rep"]), int(bool(f.get("multitask"))), int(f.get("extra_mode", "both") != "none"))


def ranked(results):
    rs = sorted([r for r in results if not r["spec"].get("diagnostic")], key=lambda r: -_wt(r))
    if not rs:
        return []
    best = _wt(rs[0])
    near = sorted([r for r in rs if best - _wt(r) <= TIE], key=lambda r: (_complexity(r["spec"]), -_wt(r)))
    return near + [r for r in rs if r not in near]


def _attempt_row(r):
    s = r["summary"]
    return {"id": r["spec"]["id"], "hypothesis": r["spec"]["hyp"], "rep": r["spec"]["rep"],
            "fixed": r["spec"]["fixed"], "note": r["spec"].get("note"), "diagnostic": r["spec"].get("diagnostic"),
            "within_tool": s["within_tool"], "within_tool_per_seed": s["within_tool_per_seed"],
            "by_source": s["by_source"], "by_source_per_seed": s["by_source_per_seed"],
            "v2_tool_only_reference": s.get("v2_tool_only_reference"), "pooled_auroc": s["pooled_auroc"],
            "per_tool": s["per_tool"], "chosen_grid_index": r["selection"].get("chosen"),
            "corr_score_log_prefix_length": (s.get("correlation") or {}).get("pearson_score_log_prefix_length"),
            "evaluate_sha256": r["evaluate_sha256"], "data_hash": r["data_hash"], "cache_key": r["cache_key"],
            "seconds": r["seconds"]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jobs", type=int, default=2)
    ap.add_argument("--phase", default="all")
    a = ap.parse_args()
    ATT.mkdir(parents=True, exist_ok=True)
    REP.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    A = _parallel(spec_0() + specs_a(), "scan", a.jobs)
    print("phase 0/A done", round(time.time() - t0), "s", [(r["spec"]["id"], _wt(r)) for r in A], flush=True)
    if a.phase in ("0", "A"):
        return
    best_a = ranked([r for r in A if r["spec"]["fixed"].get("extra_mode", "both") != "none"])[0]["spec"]
    B = _parallel(specs_b(best_a), "scan", a.jobs)
    print("phase B done", round(time.time() - t0), "s", [(r["spec"]["id"], _wt(r)) for r in B], flush=True)
    rep0 = [r for r in A if r["spec"]["id"] == "H3-0-repro"]
    best_ab = ranked(A + B)[0]["spec"]
    if rep0 and _wt(rep0[0]) > _wt(ranked(A + B)[0]) + TIE:  # plain H2-1c better than every new A/B attempt
        best_ab = rep0[0]["spec"]
    Cc = _parallel(specs_c(best_ab), "scan", a.jobs)
    print("phase C done", round(time.time() - t0), "s", [(r["spec"]["id"], _wt(r)) for r in Cc], flush=True)
    scans = A + B + Cc
    top = ranked(scans)[:3]
    F = _parallel([r["spec"] for r in top], "full", a.jobs)
    print("phase F done", round(time.time() - t0), "s", flush=True)

    from experiments.risk_loop.argus_loop import evaluate as E
    new = [r for r in scans if not r["spec"].get("diagnostic")]
    full = {}
    for r in F:
        wt = r["summary"]["within_tool"]
        ls = (r["baselines"] or {}).get("length+step", {}).get("within_tool")
        sb_h = r["shuffle_source_family_harness"]["within_tool_mean"]
        sb_n = r["shuffle_full_null"]["b_source_family"]["within_tool_mean"]
        sb = max(x for x in (sb_h, sb_n) if x is not None)
        full[r["spec"]["id"]] = {k: r[k] for k in r if k != "spec"}
        full[r["spec"]["id"]]["candidate_rule"] = {
            "shuffle_b_used (max of harness / full null)": sb,
            "headline_minus_shuffle_b": wt - sb, "headline_minus_length_step": None if ls is None else wt - ls,
            "counts": bool(ls is not None and wt - sb >= 0.10 and wt - ls >= 0.05),
            "delta_vs_prev_best_0.645": wt - PREV_BEST,
            "monitor_R1_bar_0.12_met": bool(wt - PREV_BEST >= 0.12)}
    report = {
        "iteration": 3, "date": "2026-11-08", "harness_version_used": "v4 (headline = v3 tool x source cells; 20 shuffles; v2 kept as reference)",
        "evaluate_sha256_at_report": E.evaluate_sha256(), "validation_touched": False, "test_touched": False,
        "labels": "October confirmed + November DRAFT rule labels (original_policy_label)",
        "rows": A[0]["rows"], "data_hash": A[0]["data_hash"],
        "training_universe": "headline rows (evaluated) + report-tool rows (training only, fold-safe by "
                             "universe components; never from a scored fold's family)",
        "selection_rule": "highest seed-mean nested-CV v3 within-tool AUROC; within 0.005 -> simpler; top 3 get "
                          "evaluate() v4 (20 shuffles) + full-shuffle nulls n=20; counts only if headline - max(shuffle b "
                          "harness, shuffle b full null) >= 0.10 and headline - length+step >= 0.05",
        "n_attempts_new": len(new), "cumulative_attempts_after": CUM_BEFORE + len(new),
        "previous_best_reference": PREV_BEST,
        "phase_choices": {"best_A": best_a["id"], "best_AB": best_ab["id"]},
        "attempts": [_attempt_row(r) for r in scans], "full_evaluate": full,
        "runtime_seconds_this_run": round(time.time() - t0, 1),
        "runtime_seconds_sum_of_attempts": round(sum(r["seconds"] for r in scans + F), 1),
    }
    (REP / "cv_report.json").write_text(json.dumps(E.to_jsonable(report), indent=1, ensure_ascii=False),
                                        encoding="utf-8")
    print("wrote", REP / "cv_report.json", flush=True)


if __name__ == "__main__":
    main()

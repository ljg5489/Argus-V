"""Iteration 10 model try T10-1 (train only). Plan: reports/risk-loop/argus-v1/loop/iter-10/plan.md.

(1) ``iter06_scan.run_try`` = frozen v4 evaluate (nested CV over the 15 member subsets, seeds 0,1,2; shuffles
(a)(b) 20 each on the modal subset) + report-only within-trajectory metrics + score-saving shuffle (b) replica;
(2) the whole nested selection repeated for fold seeds 0..9 (``evaluate.nested_cv`` one seed at a time, caches
cleared between seeds for RAM) and the 10-seed rule (i') of iteration 9.

Usage: py -3.11 experiments/risk_loop/argus_loop/iter10_scan.py
"""
from __future__ import annotations

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
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402
from experiments.risk_loop.argus_loop import iter01_common as C1  # noqa: E402
from experiments.risk_loop.argus_loop import iter06_scan as S6  # noqa: E402
from experiments.risk_loop.argus_loop import iter07_models as M7  # noqa: E402
from experiments.risk_loop.argus_loop import iter09_scan as S9  # noqa: E402
from experiments.risk_loop.argus_loop import iter10_models as M10  # noqa: E402

ART = REPO_ROOT / "artifacts" / "risk-loop" / "argus-v1-loop" / "iter10"
TID = "T10-1"
N_SEEDS = 10


def log(*a):
    print(time.strftime("%H:%M:%S"), *a, flush=True)


def main():
    sha = E.evaluate_sha256()
    log("evaluate_sha256", sha)
    assert sha == S9.SHA, sha
    ART.mkdir(parents=True, exist_ok=True)
    data, rows, rinfo = C1.headline_data()
    ctx = S6.model_ctx(rows)
    reps = sorted({m["rep"] for m in M10.MEMBERS})
    feats = {}
    for r in reps:
        L, p = r.split(":")
        feats[r] = np.asarray(C1.features(data, rows, int(L.lstrip("L")), p), dtype=np.float32)
    del data
    store = M7.RobustStore(feats)
    cache = M10.MemberCache(store, ctx)
    make = M10.make_subset(cache)
    log("grid", [M10.subset_label(g) for g in M10.GRID])

    out = S6.run_try(TID, make, M10.GRID, rows, rinfo, ART,
                     {"note": "nested-CV selection of an equal-weight member subset on robust PCA 32",
                      "members": list(M10.MEMBERS), "grid_labels": [M10.subset_label(g) for g in M10.GRID],
                      "preproc": {"scale": "median, IQR/1.349", "clip": M7.CLIP, "kmax": M7.KMAX}})
    h = out["harness"]
    log("evaluate done", "cache hits", cache.hits, "misses", cache.misses, "robust", store.computed)

    # 10 fold seeds: the whole nested selection per seed
    t0 = time.time()
    O, per_seed_chosen, inner_pick, merged = [], {}, {}, {"seeds": [], "oof": {}, "fold_id": {}, "folds": {},
                                                           "n_splits": None, "selection": {"method": "nested_cv"}}
    for s in range(N_SEEDS):
        store.cache.clear()
        cache.clear()
        cv = E.nested_cv(make, M10.GRID, None, rows, seeds=[s])
        merged["seeds"].append(s)
        for k in ("oof", "fold_id", "folds"):
            merged[k][str(s)] = cv[k][str(s)]
        merged["n_splits"] = cv["n_splits"]
        ch = cv["selection"]["chosen"][str(s)]
        per_seed_chosen[str(s)] = [M10.subset_label(M10.GRID[c]) for c in ch]
        sc = cv["selection"]["inner_scores"][str(s)]
        inner_pick[str(s)] = float(np.mean([sc[i][c] for i, c in enumerate(ch)]))
        O.append(cv["oof"][str(s)])
        log("seed", s, per_seed_chosen[str(s)],
            round(E.within_tool_auroc(np.asarray(cv["oof"][str(s)]), rows.y, E.headline_groups(rows))["value"], 4))
    O = np.asarray(O, dtype=np.float64)
    np.save(ART / f"oof10_{TID}.npy", O)
    m = E.metrics(merged, rows)
    per_seed = m["within_tool"]["per_seed"]
    own_b = h["shuffle_source_family"]
    same012 = bool(np.allclose(per_seed[:3], h["metrics"]["within_tool"]["per_seed"], atol=1e-12))
    picks = [p for v in per_seed_chosen.values() for p in v]
    res = {"id": TID, "seeds": list(range(N_SEEDS)), "per_seed": per_seed,
           "ci95_10seed": m["within_tool"]["ci95"],
           "by_source_10seed": {k: v["value"] for k, v in m["within_tool"]["by_source"].items()},
           "seeds012_match_evaluate": same012,
           "chosen_per_seed": per_seed_chosen, "chosen_counts_10seed": dict(Counter(picks)),
           "inner_headline_of_pick_per_seed": inner_pick,
           "inner_headline_of_pick_mean": float(np.mean(list(inner_pick.values()))),
           "rule_i_prime_10seed": S9.rule_i_prime_10seed(per_seed, own_b["within_tool_mean"],
                                                         own_b["within_tool_sd"]),
           "seconds": time.time() - t0, "evaluate_sha256": sha}
    E.dump(res, ART / f"{TID}_10seed.json")
    log(TID, "10seed", json.dumps(E.to_jsonable(res["rule_i_prime_10seed"])), "match012", same012,
        [round(x, 3) for x in per_seed], "sec", round(time.time() - t0))
    log("DONE")


if __name__ == "__main__":
    main()

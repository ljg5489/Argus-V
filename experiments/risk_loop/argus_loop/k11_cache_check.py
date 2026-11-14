"""K11 cache fidelity (iter-13 r4-executioner-final §3, stop rule 11). TRAIN rows only, labels v2.

Same linear probe, two inputs for the pre_action observation of every train step:
  orig  = features/L{LL}_pre.npy                (2880-d pooled cache, fp16)
  cache = obs_cache/obs_L{LL}.npy pre_action row (robust scale + clip + PCA-512, fp16)
Probe = H1-0a recipe (models.pca_logreg: standardise -> PCA-k -> LogReg C=1, class-balanced), k=10 (H1-0a)
and k=32 (M1' input size), family-grouped CV fold seeds 0-2, frozen evaluate.py headline (within-tool v3).
Rule: |cache - orig| > 0.01 on the headline -> exception request (U4).

  py -3.11 experiments/risk_loop/argus_loop/k11_cache_check.py
"""
from __future__ import annotations

import csv
import json
import sys
import time
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402
from experiments.risk_loop.argus_loop import iter01_common as C1  # noqa: E402
from experiments.risk_loop.argus_loop import models as M  # noqa: E402

ART = ROOT / "artifacts/risk-loop/argus-v1-loop"
OBS = ART / "obs_cache"
VIEW = ART / "features_labels_v2"
OUTF = ROOT / "reports/risk-loop/argus-v1/loop/iter-13/k11_cache_check.json"
SEEDS = (0, 1, 2)


def pre_action_obs(row_ids: np.ndarray) -> np.ndarray:
    """obs_id of each step's pre_action row (fallback: last row, as build_features.pool_step)."""
    pre, last = {}, {}
    with open(OBS / "obs_index.csv", newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            row, oid = int(r["row"]), int(r["obs_id"])
            last[row] = oid
            if r["kind"] == "pre_action":
                pre[row] = oid
    return np.asarray([pre.get(int(r), last[int(r)]) for r in row_ids], np.int64)


def main() -> int:
    t0 = time.time()
    data = E.load(root=VIEW)  # train rows only (validation never loaded)
    rows = data.rows
    assert set(rows.split.tolist()) == {"train"}
    oid = pre_action_obs(rows.row_id)
    res = {"rows": rows.summary(), "seeds": list(SEEDS), "probe": "models.pca_logreg weight=class C=1", "layers": {}}
    for L in (20, 16):
        orig = np.asarray(C1.features(data, rows, L, "pre"), dtype=np.float32)
        cache = np.asarray(np.load(OBS / f"obs_L{L:02d}.npy", mmap_mode="r")[oid], dtype=np.float32)
        res["layers"][str(L)] = {}
        for k in (10, 32):
            out = {}
            for name, X in (("orig", orig), ("cache", cache)):
                fp = M.build("pca_logreg", X, C1.ctx_for(rows), k=k, C=1.0, weight="class", cache=M.LRU(8))
                cv = E.run_cv(fp, None, rows, SEEDS)
                m = E.metrics(cv, rows, bootstrap=0, baselines=False)
                out[name] = {"within_tool": m["within_tool"]["value"], "per_seed": m["within_tool"]["per_seed"],
                             "by_source": {s: v["value"] for s, v in m["within_tool"]["by_source"].items()},
                             "pooled_auroc": m["pooled_auroc"]}
            out["diff_cache_minus_orig"] = out["cache"]["within_tool"] - out["orig"]["within_tool"]
            out["pass_le_0.01"] = abs(out["diff_cache_minus_orig"]) <= 0.01
            res["layers"][str(L)][f"pca{k}"] = out
            print(f"L{L} pca{k}: orig {out['orig']['within_tool']:.4f} cache {out['cache']['within_tool']:.4f} "
                  f"diff {out['diff_cache_minus_orig']:+.4f}", flush=True)
    h = res["layers"]["20"]["pca10"]
    res["headline"] = {"layer": 20, "probe": "H1-0a (pca10)", "diff": h["diff_cache_minus_orig"],
                       "pass": h["pass_le_0.01"]}
    res["seconds"] = time.time() - t0
    OUTF.parent.mkdir(parents=True, exist_ok=True)
    OUTF.write_text(json.dumps(res, indent=1), encoding="utf-8")
    print(json.dumps(res["headline"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())

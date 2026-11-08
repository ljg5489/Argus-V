"""Iteration 5: precompute standardise -> PCA(32) embeddings for every (representation, harness training set).

Label-free (PCA only). Usage (two detached processes):
  py -3.11 experiments/risk_loop/argus_loop/iter05_emb.py --part 0 --parts 2
  py -3.11 experiments/risk_loop/argus_loop/iter05_emb.py --part 1 --parts 2
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path

for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ.setdefault(_v, "2")

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop.argus_loop import iter01_common as C1  # noqa: E402
from experiments.risk_loop.argus_loop import iter02_common as C2  # noqa: E402
from experiments.risk_loop.argus_loop import iter05_common as C5  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--part", type=int, default=0)
    ap.add_argument("--parts", type=int, default=1)
    a = ap.parse_args()
    C5.EMB_DIR.mkdir(parents=True, exist_ok=True)
    data, rows, _ = C1.headline_data()
    sets = C5.training_sets(rows)
    slots = {}
    for s in sets:
        slots.setdefault(C5.pos_hash(s["pos"]), len(slots))
    meta = {"slots": slots, "n_rows": len(rows), "kmax": C5.KMAX, "data_hash": C2.data_hash(rows),
            "sets": [{k: v for k, v in s.items() if k != "pos"} | {"hash": C5.pos_hash(s["pos"]), "n": len(s["pos"])}
                     for s in sets]}
    (C5.EMB_DIR / "index.json").write_text(json.dumps(meta, indent=1), encoding="utf-8")
    uniq = {}
    for s in sets:
        uniq.setdefault(C5.pos_hash(s["pos"]), s["pos"])
    reps = [r for i, r in enumerate(C5.REPS) if i % a.parts == a.part]
    for rep in reps:
        out = C5.EMB_DIR / f"{rep.replace(':', '_')}.npy"
        if out.is_file():
            print("skip", rep, flush=True)
            continue
        t0 = time.time()
        L, p = rep.split(":")
        X = C1.features(data, rows, int(L.lstrip("L")), p)
        tmp = C5.EMB_DIR / f"{rep.replace(':', '_')}.tmp.npy"
        arr = np.lib.format.open_memmap(tmp, mode="w+", dtype=np.float16, shape=(len(slots), len(rows), C5.KMAX))
        for h, slot in slots.items():
            arr[slot] = C5.compute_embedding(X, uniq[h]).astype(np.float16)
        arr.flush()
        del arr, X
        os.replace(tmp, out)
        print(rep, "sec", round(time.time() - t0, 1), flush=True)
    print("DONE", flush=True)


if __name__ == "__main__":
    main()

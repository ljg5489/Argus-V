"""Iteration 5 shared helpers: representation list, the fixed training-row sets used by the frozen harness,
and a precomputed PCA embedding store.

Why a store: iteration 5 lets the inner CV choose the representation (6 layers x 4 pools). The harness
fits each grid entry on a fixed family of training-row sets (fold seeds 0/1/2: 5 outer training parts and
3 inner training parts inside each; the shuffle tests reuse the seed-0 outer parts). PCA is label-free, so
standardise -> PCA(32) per (representation, training set) is computed once and stored as float16. A model
looks the embedding up by the hash of ``pos_train``; on a miss it computes it the same way (``on_miss``).

Rows always come from ``iter01_common.headline_data()`` (9,278 rows / 79 positives, 10 v3 cells / 52).
"""
from __future__ import annotations

import hashlib
import json
import sys
import threading
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402
from experiments.risk_loop.argus_loop import iter01_common as C1  # noqa: E402
from experiments.risk_loop.argus_loop import models as M  # noqa: E402

ART = REPO_ROOT / "artifacts" / "risk-loop" / "argus-v1-loop" / "iter05"
EMB_DIR = ART / "emb"
KMAX = 32
REPS = tuple(f"L{L}:{p}" for L in C1.LAYERS for p in C1.POOLS)  # grid order: layer asc, then pool order


def rep_layer(rep: str) -> int:
    return int(rep.split(":")[0].lstrip("L"))


def pos_hash(pos) -> str:
    return hashlib.sha1(np.ascontiguousarray(np.asarray(pos, dtype=np.int64)).tobytes()).hexdigest()


def training_sets(rows: E.Rows, seeds=E.DEFAULT_SEEDS, n_splits: int = 5, inner_splits: int = 3) -> list[dict]:
    """Every pos_train the harness passes to fit_predict in evaluate(grid=...) (nested CV + shuffles),
    replicated with the harness' own make_folds. Inner sets carry (seed, outer fold, inner fold)."""
    out = []
    for seed in seeds:
        folds = E.make_folds(rows, n_splits, seed)
        for i, (a, _) in enumerate(folds):
            inner = E.make_folds(rows.subset(a), inner_splits, seed)
            for j, (ia, _) in enumerate(inner):
                out.append({"kind": "inner", "seed": int(seed), "outer": i, "inner": j, "pos": a[ia]})
            out.append({"kind": "outer", "seed": int(seed), "outer": i, "inner": None, "pos": a})
    return out


def compute_embedding(X: np.ndarray, pos_train: np.ndarray, kmax: int = KMAX) -> np.ndarray:
    """Standardise on train rows -> PCA(kmax, random_state 0) on train rows -> embedding of all rows."""
    return M.pca_embed(X, np.asarray(pos_train, dtype=np.int64), kmax, ctx={})


class EmbStore:
    """Read-only lookup rep x pos_train -> (n_rows, KMAX) float32 embedding.

    Files: ``<dir>/<rep>.npy`` (n_sets, n_rows, KMAX) float16 + ``<dir>/index.json`` {hash: slot}.
    ``on_miss(rep, pos_train)`` computes a missing embedding (counted in ``misses``)."""

    def __init__(self, root: Path | None = None, on_miss=None, memory: dict | None = None):
        self.root = Path(root) if root is not None else EMB_DIR
        self.on_miss = on_miss
        self.memory = memory  # tests: {rep: {hash: array}}
        self.index = {}
        if memory is None and (self.root / "index.json").is_file():
            self.index = json.loads((self.root / "index.json").read_text(encoding="utf-8"))["slots"]
        self._arr = {}
        self._extra = {}
        self._lock = threading.Lock()
        self.misses = 0

    def _array(self, rep):
        a = self._arr.get(rep)
        if a is None:
            a = np.load(self.root / f"{rep.replace(':', '_')}.npy", mmap_mode="r")
            self._arr[rep] = a
        return a

    def get(self, rep: str, pos_train) -> np.ndarray:
        h = pos_hash(pos_train)
        if self.memory is not None and h in self.memory.get(rep, {}):
            return np.asarray(self.memory[rep][h], dtype=np.float32)
        if h in self.index:
            with self._lock:
                a = self._array(rep)
            return np.asarray(a[self.index[h]], dtype=np.float32)
        with self._lock:
            key = (rep, h)
            if key not in self._extra:
                if self.on_miss is None:
                    raise KeyError(f"no embedding for {rep} / {h}")
                self.misses += 1
                self._extra[key] = np.asarray(self.on_miss(rep, pos_train), dtype=np.float16)
                while len(self._extra) > 16:
                    self._extra.pop(next(iter(self._extra)))
            return np.asarray(self._extra[key], dtype=np.float32)


def real_on_miss(data, rows):
    """on_miss for the real cache: load the representation and compute the embedding (rare)."""
    def f(rep, pos_train):
        L, p = rep.split(":")
        X = C1.features(data, rows, int(L.lstrip("L")), p)
        return compute_embedding(X, pos_train)
    return f


def earlier_mean(score: np.ndarray, traj: np.ndarray, step: np.ndarray, fill: float) -> np.ndarray:
    """For each row: mean score of the strictly earlier steps of the same trajectory among the given rows
    (rows sharing a step index do not see each other); ``fill`` where no earlier step exists."""
    score = np.asarray(score, dtype=np.float64)
    traj = np.asarray(traj).astype(str)
    step = np.asarray(step, dtype=np.float64)
    out = np.full(len(score), float(fill))
    order = np.lexsort((step, traj))
    tt, ss = traj[order], step[order]
    bounds = np.r_[0, np.nonzero(tt[1:] != tt[:-1])[0] + 1, len(tt)]
    for a, b in zip(bounds[:-1], bounds[1:]):
        idx = order[a:b]
        st = ss[a:b]
        csum, cnt, j = 0.0, 0, 0
        while j < len(idx):
            k = j
            while k < len(idx) and st[k] == st[j]:
                k += 1
            if cnt:
                out[idx[j:k]] = csum / cnt
            csum += score[idx[j:k]].sum()
            cnt += k - j
            j = k
    return out

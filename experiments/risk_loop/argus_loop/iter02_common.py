"""Iteration 2 shared helpers: representations (contrasts, concatenation, trajectory deltas) and context.

Rows always come from ``iter01_common.headline_data()`` (headline_filter; 9,278 rows / 79 positives).
Representation strings:
  "L23:max"              single block (iter01_common.features)
  "L23:rend-pre"         elementwise difference of two pools of one layer
  "L16:max+L23:max"      concatenation; returns block boundaries for block standardisation
  "traj:L23:max"         x - mean(x of earlier steps of the same trajectory among the evaluated rows);
                         rows without an earlier step get the zero vector. Uses only activations observed
                         before the current action (earlier steps of the same rollout) -- no labels, tools,
                         sources or scenario codes.
"""
from __future__ import annotations

import hashlib
import sys
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop.argus_loop import iter01_common as C1  # noqa: E402

THIS_DIR = Path(__file__).resolve().parent


def _block(data, rows, s: str) -> np.ndarray:
    L, p = s.split(":")
    L = int(L.lstrip("L"))
    if "-" in p:
        a, b = p.split("-")
        return C1.features(data, rows, L, a) - C1.features(data, rows, L, b)
    return C1.features(data, rows, L, p)


def trajectory_delta(X: np.ndarray, trajectory: np.ndarray, step: np.ndarray) -> np.ndarray:
    """x_t - mean_{s<t} x_s within each trajectory (order by step); zero where no earlier step exists.
    Rows sharing a step index do not see each other."""
    X = np.asarray(X, dtype=np.float32)
    out = np.zeros_like(X)
    traj = np.asarray(trajectory).astype(str)
    step = np.asarray(step, dtype=np.float64)
    for t in np.unique(traj):
        idx = np.nonzero(traj == t)[0]
        idx = idx[np.argsort(step[idx], kind="stable")]
        csum = np.zeros(X.shape[1], dtype=np.float64)
        cnt = 0
        j = 0
        while j < len(idx):
            k = j
            while k < len(idx) and step[idx[k]] == step[idx[j]]:
                k += 1
            grp = idx[j:k]
            if cnt:
                out[grp] = X[grp] - (csum / cnt).astype(np.float32)
            csum += X[grp].sum(0, dtype=np.float64)
            cnt += len(grp)
            j = k
    return out


def representation(data, rows, rep: str) -> tuple[np.ndarray, list | None]:
    """Feature matrix aligned to rows + block boundaries (None for single blocks)."""
    if rep.startswith("traj:"):
        X = _block(data, rows, rep[len("traj:"):])
        return trajectory_delta(X, rows.trajectory_id, rows.step_index), None
    parts = rep.split("+")
    if len(parts) == 1:
        return _block(data, rows, rep), None
    Xs = [_block(data, rows, s) for s in parts]
    bounds, a = [], 0
    for x in Xs:
        bounds.append((a, a + x.shape[1]))
        a += x.shape[1]
    return np.concatenate(Xs, axis=1), bounds


def ctx_for(rows) -> dict:
    """iter01 ctx + training-only stratum (tool x source; read by iteration-2 models at training rows only)
    + step_index (allowed input, used only as a deconfounding target)."""
    ctx = C1.ctx_for(rows)
    ctx["train_group"] = np.asarray([f"{t}|{s}" for t, s in zip(rows.tool.astype(str), rows.source.astype(str))],
                                    dtype=object)
    ctx["step_index"] = np.nan_to_num(np.asarray(rows.step_index, dtype=np.float64), nan=0.0)
    return ctx


def file_sha(p: Path) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def data_hash(rows) -> str:
    """Hash of the evaluated row set + labels + tools + sources + the feature manifest/steps hashes."""
    h = hashlib.sha256()
    h.update(np.ascontiguousarray(rows.row_id.astype(np.int64)).tobytes())
    h.update(np.ascontiguousarray(rows.y.astype(np.int8)).tobytes())
    h.update("|".join(rows.tool.astype(str).tolist()).encode())
    h.update("|".join(rows.source.astype(str).tolist()).encode())
    root = C1.E.FEATURES_DIR
    for name in ("manifest.json", "steps.csv"):
        p = root / name
        if p.is_file():
            h.update(file_sha(p).encode())
    return h.hexdigest()

"""Iteration 3 shared helpers: the training universe (headline rows + report-tool rows), fold-safe extra-row
selection inputs, and previous-step representations. Plan: reports/risk-loop/argus-v1/loop/iter-03/plan.md.

Universe layout: positions 0..n_head-1 are exactly ``iter01_common.headline_data()`` rows in their order (the
rows the frozen harness evaluates and whose positions it passes to fit_predict); positions n_head..N-1 are the
report-tool rows of ``iter01_common.report_data()`` (training samples only, never evaluated).

Side information in ``ctx`` (read only at training positions by iter03_models, never for scoring):
  comp    connected components of (family, trajectory_id, unit_id) over the WHOLE universe (evaluate.group_components)
  family, source, train_group (tool x source)  -- training-fold statistics / weights / leak checks only
  track   0 headline, 1 report
  y_extra label of report rows; NaN at headline positions (headline labels come only from y_train)
"""
from __future__ import annotations

import hashlib
import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402
from experiments.risk_loop.argus_loop import iter01_common as C1  # noqa: E402
from experiments.risk_loop.argus_loop import iter02_common as C2  # noqa: E402


def concat_rows(a: E.Rows, b: E.Rows) -> E.Rows:
    kw = {k: np.concatenate([getattr(a, k), getattr(b, k)]) for k in E.Rows.__dataclass_fields__ if k != "info"}
    return E.Rows(**kw, info={"filter": "iter03 universe (headline + report rows)"})


@dataclass
class Universe:
    data_head: E.LoopData
    data_rep: E.LoopData
    head: E.Rows
    rep: E.Rows
    rows: E.Rows          # concatenation head + rep
    n_head: int
    info: dict

    def block(self, s: str) -> np.ndarray:
        """Feature block 'L23:max' (or 'L23:a-b') for all universe rows."""
        return np.concatenate([C2._block(self.data_head, self.head, s), C2._block(self.data_rep, self.rep, s)])


def load_universe() -> Universe:
    dh, head, hinfo = C1.headline_data()
    dr, rep, rinfo = C1.report_data()
    ids = np.r_[head.row_id, rep.row_id]
    if len(set(ids.tolist())) != len(ids):
        raise RuntimeError("headline and report rows overlap")
    if not set(rep.split.tolist()) <= {"train"} or not set(head.split.tolist()) <= {"train"}:
        raise PermissionError("universe must be train rows only")
    rows = concat_rows(head, rep)
    return Universe(dh, dr, head, rep, rows, len(head), {"headline": hinfo, "report": rinfo})


def prev_index(rows: E.Rows) -> np.ndarray:
    """Universe position of the immediately preceding step (largest step_index < own) in the same trajectory;
    -1 if none. Only earlier steps are ever returned."""
    traj = rows.trajectory_id.astype(str)
    step = np.asarray(rows.step_index, dtype=np.float64)
    out = np.full(len(rows), -1, dtype=np.int64)
    for t in np.unique(traj):
        idx = np.nonzero(traj == t)[0]
        idx = idx[np.argsort(step[idx], kind="stable")]
        last_pos = -1
        j = 0
        while j < len(idx):
            k = j
            while k < len(idx) and step[idx[k]] == step[idx[j]]:
                k += 1
            out[idx[j:k]] = last_pos
            last_pos = idx[k - 1]
            j = k
    return out


def representation(u: Universe, rep: str) -> tuple[np.ndarray, list | None]:
    """'L23:max' plain; 'prev:L23:max' = [x_t, x_prev] (blocks); 'dprev:L23:max' = x_t - x_prev.
    Missing previous step -> x_prev := x_t (no change)."""
    if rep.startswith(("prev:", "dprev:")):
        kind, s = rep.split(":", 1)
        X = u.block(s)
        p = prev_index(u.rows)
        P = X[np.where(p >= 0, p, np.arange(len(p)))]
        if kind == "dprev":
            return (X - P).astype(np.float32), None
        d = X.shape[1]
        return np.concatenate([X, P], axis=1), [(0, d), (d, 2 * d)]
    return u.block(rep), None


def ctx_for(u: Universe) -> dict:
    r = u.rows
    y_extra = np.full(len(r), np.nan)
    y_extra[u.n_head:] = u.rep.y.astype(np.float64)
    return {"comp": E.group_components(r), "family": r.family.astype(str), "source": r.source.astype(str),
            "train_group": np.asarray([f"{t}|{s}" for t, s in zip(r.tool.astype(str), r.source.astype(str))],
                                      dtype=object),
            "track": np.r_[np.zeros(u.n_head, np.int64), np.ones(len(r) - u.n_head, np.int64)],
            "y_extra": y_extra, "n_head": u.n_head}


def data_hash(u: Universe) -> str:
    h = hashlib.sha256()
    h.update(C2.data_hash(u.head).encode())
    h.update(np.ascontiguousarray(u.rep.row_id.astype(np.int64)).tobytes())
    h.update(np.ascontiguousarray(u.rep.y.astype(np.int8)).tobytes())
    return h.hexdigest()

"""Iteration 1 shared helpers: row filters (headline / report track) and feature loading.

Headline track (TASK.md section 1, 2026-11-08 decision): report-content positives of both sources are
excluded (October write_report/stop/submit_result, November submit_result). evaluate.load() only drops
October ``report_content=1``; ``headline_rows`` additionally drops every row whose tool is a report tool
(positives *and* negatives: a tool without positives contributes nothing to within-tool AUROC).
Rows with ``features_complete=0`` in ``features/row_status.csv`` are dropped and counted.
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402

REPORT_TOOLS = frozenset({"write_report", "stop", "submit_result"})
LAYERS = (8, 11, 14, 16, 20, 23)
POOLS = ("max", "mean", "pre", "rend")


def read_row_status(root: Path | str | None = None) -> dict[int, int]:
    root = Path(root) if root is not None else E.FEATURES_DIR
    p = root / "row_status.csv"
    if not p.is_file():
        raise FileNotFoundError(f"{p} missing (feature build not finalized)")
    with open(p, newline="", encoding="utf-8") as h:
        return {int(r["row"]): int(r["features_complete"]) for r in csv.DictReader(h)}


def complete_mask(rows: E.Rows, status: dict[int, int]) -> np.ndarray:
    return np.asarray([status.get(int(r), 0) == 1 for r in rows.row_id.tolist()], dtype=bool)


def headline_filter(rows: E.Rows, status: dict[int, int] | None) -> tuple[E.Rows, dict]:
    """Drop report tools entirely and incomplete-feature rows. Returns (rows, counts)."""
    rep = np.isin(rows.tool.astype(str), list(REPORT_TOOLS))
    comp = complete_mask(rows, status) if status is not None else np.ones(len(rows), bool)
    keep = ~rep & comp
    y = rows.y
    info = {"start_rows": int(len(rows)), "start_positives": int(y.sum()),
            "dropped_report_tool_rows": int(rep.sum()), "dropped_report_tool_positives": int(y[rep].sum()),
            "dropped_incomplete_rows": int((~rep & ~comp).sum()),
            "dropped_incomplete_positives": int(y[~rep & ~comp].sum()),
            "dropped_incomplete_by_source": {s: int(((~rep) & (~comp) & (rows.source == s)).sum())
                                             for s in E.SOURCES}}
    out = rows.subset(np.nonzero(keep)[0])
    out.info.update({"filter": "headline_rows(iter01)", **info})
    info.update({"rows": int(len(out)), "positives": int(out.y.sum())})
    return out, info


def report_filter(rows: E.Rows, status: dict[int, int] | None) -> tuple[E.Rows, dict]:
    """Report track: report-tool rows only (rows must come from load(include_report_content=True))."""
    rep = np.isin(rows.tool.astype(str), list(REPORT_TOOLS))
    comp = complete_mask(rows, status) if status is not None else np.ones(len(rows), bool)
    keep = rep & comp
    out = rows.subset(np.nonzero(keep)[0])
    out.info.update({"filter": "report_track(iter01)"})
    info = {"rows": int(len(out)), "positives": int(out.y.sum()),
            "dropped_incomplete_rows": int((rep & ~comp).sum())}
    return out, info


def headline_data(root=None):
    data = E.load(root)
    status = read_row_status(root)
    rows, info = headline_filter(data.rows, status)
    return data, rows, info


def report_data(root=None):
    data = E.load(root, include_report_content=True)
    status = read_row_status(root)
    rows, info = report_filter(data.rows, status)
    return data, rows, info


def features(data: E.LoopData, rows: E.Rows, layer: int, pool: str) -> np.ndarray:
    """float32 features aligned to rows. rend rows without reasoning_end (NaN) are filled with pre."""
    X = data.features(layer, pool, rows)
    bad = ~np.isfinite(X).all(1)
    if pool == "rend" and bad.any():
        P = data.features(layer, "pre", rows.subset(np.nonzero(bad)[0]))
        X[bad] = P
        bad = ~np.isfinite(X).all(1)
    if bad.any():
        raise ValueError(f"L{layer} {pool}: {int(bad.sum())} rows with non-finite features")
    return X


def ctx_for(rows: E.Rows) -> dict:
    return {"source": rows.source.astype(str),
            "log_prefix_length": np.log(np.clip(rows.prefix_length, 1.0, None))}

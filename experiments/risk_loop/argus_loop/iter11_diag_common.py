"""Iteration 11 (diagnosis) shared helpers. Train split only; frozen v4 evaluate.py is only imported.

Plan: reports/risk-loop/argus-v1/loop/TASK.md section 6b. Diagnostic fits, not model tries.
"""
from __future__ import annotations

import csv
import os
import sys
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

ART = REPO_ROOT / "artifacts" / "risk-loop" / "argus-v1-loop"
OUT = ART / "diag11"
REPORT = REPO_ROOT / "reports" / "risk-loop" / "argus-v1" / "loop" / "iter-11"
SHA = "a7c36eafdf994f98b61895be4e4b8d237740d0018422d12febab8deb9df0130d"


def scenario_map(rows: E.Rows) -> np.ndarray:
    """scenario_id per row (diagnosis only, never a model input), from features/steps.csv."""
    want = set(int(r) for r in rows.row_id.tolist())
    sid = {}
    with open(E.FEATURES_DIR / "steps.csv", newline="", encoding="utf-8") as h:
        for rec in csv.DictReader(h):
            r = int(rec["row"])
            if r in want:
                if rec["split"] != "train":
                    raise PermissionError("non-train row requested")
                sid[r] = rec["scenario_id"]
    return np.asarray([sid[int(r)] for r in rows.row_id.tolist()], dtype=object)


def headline():
    assert E.evaluate_sha256() == SHA
    data, rows, info = C1.headline_data()
    assert set(rows.split.tolist()) == {"train"}
    return data, rows, info


def cells(rows: E.Rows):
    """Included v3 headline cells: list of (cell, index array) with >=3 pos and >=3 neg."""
    g = E.headline_groups(rows)
    y = rows.y
    out = []
    for c in sorted(set(g.tolist())):
        m = np.nonzero(g == c)[0]
        p = int(y[m].sum())
        if p >= E.MIN_POS and len(m) - p >= E.MIN_NEG:
            out.append((c, m))
    return out


def per_cell_auroc(scores, rows, cell_list=None) -> dict:
    from experiments.risk_loop import harness as H
    y = rows.y
    cell_list = cell_list if cell_list is not None else cells(rows)
    return {c: float(H.auroc(np.asarray(scores)[m], y[m])) for c, m in cell_list}


def headline_value(scores, rows, mask=None) -> float | None:
    y, g = rows.y, E.headline_groups(rows)
    s = np.asarray(scores, dtype=np.float64)
    if mask is not None:
        return E.within_tool_auroc(s[mask], y[mask], g[mask])["value"]
    return E.within_tool_auroc(s, y, g)["value"]


def by_source(scores, rows) -> dict:
    return {s: headline_value(scores, rows, rows.source == s) for s in E.SOURCES}


def eval_mask(rows):
    """Rows inside included headline cells."""
    m = np.zeros(len(rows), bool)
    for _, idx in cells(rows):
        m[idx] = True
    return m

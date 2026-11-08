"""Frozen evaluation module for the Argus-V1 improvement loop.

Spec: reports/risk-loop/argus-v1/loop/TASK.md §0 (target and success gate), root TASK.md §2 and §5.
Frozen: the sha256 of this file is recorded in reports/risk-loop/argus-v1/loop/eval/HARNESS.md. Do not edit
during the loop; any change needs a new hash, a ledger entry and a re-run of every reported candidate.

Data contract: ``artifacts/risk-loop/argus-v1-loop/features/steps.csv`` (one row per action step) and
``features/L{LL}_{pool}.npy`` row-aligned to steps.csv. Only ``train`` rows are ever returned; ``validation``
rows only with ``load(validation_look=True)``; ``test``/``sealed``/unknown splits are refused everywhere.

Conventions (fixed with the hash):
- fit_predict convention (same as harness.grouped_cv): ``fit_predict(A_train, y_train, A_test) -> scores``.
  ``A`` is the 2-D feature matrix passed as ``X_or_rowids``, a 1-D id vector, or (None) row positions
  0..n-1 into ``rows``. ``y_train`` is supplied by this module (it is the permuted label in the shuffle
  test), so a model must take its training labels from that argument and never from ``rows.label``.
- Folds: StratifiedGroupKFold(n_splits, shuffle=True, random_state=seed) on connected components of
  (family, trajectory_id, unit_id), stratified on the label. One fold seed = one fold assignment.
- AUROC: Mann-Whitney with average ranks for ties (harness.auroc). AP: harness.average_precision.
- within_tool_auroc (headline): OOF scores pooled over folds (fold-agnostic, TASK.md §0). For each tool with
  >= 3 positives and >= 3 negatives among the evaluated rows: AUROC inside the tool; weighted mean by the
  tool's positives. Per source: same, computed on that source's rows only. Multi-seed value = mean of the
  per-seed values (eligibility depends on labels only, so it is the same tool set for every seed).
- Family bootstrap: resample families with replacement (2000 reps, seed 0); in each replicate recompute
  within_tool_auroc (eligibility re-applied) for every seed's OOF and average over seeds; percentile 95% CI.
- Baselines use the same folds: length+step (logistic on [log prefix_length, step_index]), n_obs (logistic on
  log1p(n_obs)), tool identity (in-fold positive rate per tool; global rate for an unseen tool).
- Shuffle tests (gate condition 3, v2): fold seed ``seed``; in every training fold the labels are permuted
  within cells of the training rows; scores are evaluated against the true labels; 3 permutations.
  (a) cells = source: within_tool mean must be 0.5 +/- 0.05.
  (b) cells = source x family (family positive rates kept): headline within_tool minus the mean of (b)
  must be >= 0.10. v1 required (b) itself to be 0.5 +/- 0.05, which a model with real label signal can
  fail when family rates differ (synthetic: 0.70); changed before any real data was read.
- Nested CV: inner StratifiedGroupKFold(inner_splits, seed) on the outer training rows picks the grid entry
  with the best inner within_tool_auroc (fallback pooled AUROC; ties -> first entry); refit on the outer
  training rows; score the outer test fold.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
import sys
import warnings
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Sequence

import numpy as np
from scipy.stats import rankdata

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop import harness as H  # noqa: E402  (frozen; only pure functions reused)

FEATURES_DIR = REPO_ROOT / "artifacts" / "risk-loop" / "argus-v1-loop" / "features"
POOLS = ("max", "mean", "pre", "rend")
SOURCES = ("oct", "nov")
MIN_POS = 3
MIN_NEG = 3
BOOTSTRAP_REPS = 2000
BOOTSTRAP_SEED = 0
DEFAULT_SEEDS = (0, 1, 2)

# TASK.md §0 success gate thresholds.
GATE = {"within_tool_min": 0.90, "per_seed_min": 0.88, "ci_low_min": 0.80, "shuffle_center": 0.5,
        "shuffle_tol": 0.05, "shuffle_family_margin": 0.10, "per_source_min": 0.85}
GATE_VERSION = "v4"  # v2: condition 3 (before real data). v3 (2026-11-08, AFTER iteration-1 results):
# headline groups by tool x source cells instead of tool; removes the source shortcut inside a tool.
HEADLINE_GROUPING = "tool_x_source"
# v4 (2026-11-08, before iteration-3 evaluation): gate shuffles (a)/(b) use 20 runs each (was 3); thresholds same.
N_SHUFFLE = 20
SHUFFLE_JOBS = 2  # threads (shared memory); results do not depend on it

FitPredict = Callable[[np.ndarray, np.ndarray, np.ndarray], Any]

_NULL = {"", "null", "none", "nan", "na"}
_REQUIRED = ("unit_id", "trajectory_id", "step_index", "tool", "label", "label_status", "source", "family",
             "split", "report_content", "n_obs", "prefix_length")
_TRAIN_ONLY = frozenset({"train"})
_TRAIN_VAL = frozenset({"train", "validation"})


def evaluate_sha256() -> str:
    h = hashlib.sha256()
    with open(__file__, "rb") as handle:
        h.update(handle.read())
    return h.hexdigest()


# ---------------------------------------------------------------------------------------------- rows

def _label(v: Any) -> float:
    s = str(v).strip().lower()
    if s in _NULL:
        return math.nan
    if s in ("true", "yes"):
        return 1.0
    if s in ("false", "no"):
        return 0.0
    f = float(s)
    if f not in (0.0, 1.0):
        raise ValueError(f"label must be 0/1/null, got {v!r}")
    return f


def _num(v: Any) -> float:
    s = str(v).strip().lower()
    if s in _NULL:
        return math.nan
    if s in ("true", "yes"):
        return 1.0
    if s in ("false", "no"):
        return 0.0
    return float(s)


@dataclass
class Rows:
    """Column arrays of the evaluated step rows. ``row_id`` = 0-based data row in steps.csv."""
    row_id: np.ndarray
    unit_id: np.ndarray
    trajectory_id: np.ndarray
    step_index: np.ndarray
    tool: np.ndarray
    label: np.ndarray          # float, nan = null
    label_status: np.ndarray
    source: np.ndarray
    family: np.ndarray
    split: np.ndarray
    report_content: np.ndarray  # int 0/1
    n_obs: np.ndarray
    prefix_length: np.ndarray
    info: dict = field(default_factory=dict)

    _STR = ("unit_id", "trajectory_id", "tool", "label_status", "source", "family", "split")

    def __len__(self) -> int:
        return int(len(self.row_id))

    @property
    def y(self) -> np.ndarray:
        if np.isnan(self.label).any():
            raise ValueError("rows contain null labels; filter them with select_rows()")
        return self.label.astype(np.int64)

    def subset(self, idx) -> "Rows":
        idx = np.asarray(idx)
        if idx.dtype != bool:
            idx = idx.astype(np.int64)
        kw = {k: getattr(self, k)[idx] for k in self.__dataclass_fields__ if k != "info"}
        return Rows(**kw, info=dict(self.info))

    @classmethod
    def from_records(cls, records: Sequence[dict], row_ids: Sequence[int] | None = None) -> "Rows":
        for c in _REQUIRED:
            if records and c not in records[0]:
                raise ValueError(f"missing column {c!r}")
        col = lambda c: [r[c] for r in records]  # noqa: E731
        rid = np.arange(len(records)) if row_ids is None else np.asarray(row_ids, dtype=np.int64)
        return cls(
            row_id=np.asarray(rid, dtype=np.int64),
            **{c: np.asarray([str(v).strip() for v in col(c)], dtype=object) for c in cls._STR},
            step_index=np.asarray([_num(v) for v in col("step_index")], dtype=np.float64),
            label=np.asarray([_label(v) for v in col("label")], dtype=np.float64),
            report_content=np.asarray([0 if math.isnan(_num(v)) else int(_num(v)) for v in col("report_content")],
                                      dtype=np.int64),
            n_obs=np.asarray([_num(v) for v in col("n_obs")], dtype=np.float64),
            prefix_length=np.asarray([_num(v) for v in col("prefix_length")], dtype=np.float64),
        )

    def summary(self) -> dict:
        y = self.label
        out = {"n": len(self), "positives": int(np.nansum(y)), "null_labels": int(np.isnan(y).sum()),
               "families": int(len(set(self.family.tolist()))), "tools": int(len(set(self.tool.tolist()))),
               "report_content_rows": int((self.report_content == 1).sum()),
               "splits": dict(sorted(Counter(self.split.tolist()).items())),
               "label_status": dict(sorted(Counter(self.label_status.tolist()).items())), "by_source": {}}
        for s in sorted(set(self.source.tolist())):
            m = self.source == s
            out["by_source"][s] = {"n": int(m.sum()), "positives": int(np.nansum(y[m]))}
        out.update({k: v for k, v in self.info.items() if k != "allowed_splits"})
        return out


def select_rows(rows: Rows, include_report_content: bool = False, include_null: bool = False) -> Rows:
    """Default filter: drop October report/stop/submit positives (report_content=1) and null labels."""
    keep = np.ones(len(rows), dtype=bool)
    if not include_report_content:
        keep &= rows.report_content != 1
    if not include_null:
        keep &= ~np.isnan(rows.label)
    rc = (rows.report_content == 1) if not include_report_content else np.zeros(len(rows), dtype=bool)
    nl = (np.isnan(rows.label) & ~rc) if not include_null else np.zeros(len(rows), dtype=bool)
    out = rows.subset(np.nonzero(keep)[0])
    out.info.update({"include_report_content": include_report_content, "include_null": include_null,
                     "excluded_report_content": int(rc.sum()), "excluded_null_label": int(nl.sum())})
    return out


def _guard_splits(rows: Rows, allowed: frozenset = _TRAIN_ONLY, what: str = "this operation") -> None:
    bad = sorted(set(rows.split.tolist()) - set(allowed))
    if bad:
        raise PermissionError(f"{what} refuses rows with split {bad} (allowed: {sorted(allowed)}; test/sealed are sealed)")


# ---------------------------------------------------------------------------------------------- loader

class LoopData:
    """Train (optionally train+validation) view of the feature cache. Never exposes test/sealed rows."""

    def __init__(self, root: Path, rows: Rows, n_csv_rows: int, allowed: frozenset):
        self.root = Path(root)
        self.rows = rows
        self.n_csv_rows = n_csv_rows
        self.allowed = allowed
        self._allowed_ids = set(rows.row_id.tolist())
        self._cache: dict[str, np.ndarray] = {}

    def _guard_ids(self, row_ids) -> np.ndarray:
        ids = np.asarray(row_ids, dtype=np.int64).ravel()
        bad = [int(r) for r in ids.tolist() if r not in self._allowed_ids]
        if bad:
            raise PermissionError(f"{len(bad)} requested rows are not loaded train rows (e.g. {bad[:5]}); "
                                  f"test/sealed/validation rows are refused")
        return ids

    def features(self, layer: int, pool: str, rows: Rows | None = None) -> np.ndarray:
        """Feature matrix for ``rows`` (default: all loaded rows), aligned to their order."""
        if pool not in POOLS:
            raise ValueError(f"pool must be one of {POOLS}")
        ids = self._guard_ids((rows if rows is not None else self.rows).row_id)
        name = f"L{int(layer):02d}_{pool}.npy"
        if name not in self._cache:
            arr = np.load(self.root / name, mmap_mode="r")
            if arr.shape[0] != self.n_csv_rows:
                raise ValueError(f"{name} has {arr.shape[0]} rows, steps.csv has {self.n_csv_rows}")
            self._cache[name] = arr
        return np.asarray(self._cache[name][ids], dtype=np.float32)

    def features_for(self, row_ids, layer: int, pool: str) -> np.ndarray:
        ids = self._guard_ids(row_ids)
        pos = {int(r): i for i, r in enumerate(self.rows.row_id.tolist())}
        return self.features(layer, pool, self.rows.subset([pos[int(r)] for r in ids]))


def load(root: Path | str | None = None, *, validation_look: bool = False, split: str | None = None,
         include_report_content: bool = False, include_null: bool = False) -> LoopData:
    """Load train rows (``validation_look=True``: train+validation). Any request for test/sealed raises."""
    if split is not None and split not in ("train", "validation"):
        raise PermissionError(f"split {split!r} is sealed (TASK.md §0/§1); only train (and validation on a look)")
    if split == "validation" and not validation_look:
        raise PermissionError("validation rows need validation_look=True (counted look, success candidates only)")
    allowed = _TRAIN_VAL if validation_look else _TRAIN_ONLY
    root = Path(root) if root is not None else FEATURES_DIR
    kept, ids, n = [], [], 0
    with open(root / "steps.csv", newline="", encoding="utf-8") as handle:
        for i, rec in enumerate(csv.DictReader(handle)):
            n += 1
            if str(rec.get("split", "")).strip() in allowed:  # other rows are dropped unread beyond the split
                kept.append(rec)
                ids.append(i)
    rows = Rows.from_records(kept, ids) if kept else Rows.from_records([{c: "" for c in _REQUIRED}], [0]).subset([])
    rows = select_rows(rows, include_report_content, include_null)
    if split is not None:
        rows = rows.subset(np.nonzero(rows.split == split)[0])
    rows.info["allowed_splits"] = sorted(allowed)
    return LoopData(root, rows, n, allowed)


# ---------------------------------------------------------------------------------------------- folds

def group_components(rows: Rows) -> np.ndarray:
    """Connected components of family, trajectory_id and unit_id (none of them may straddle folds)."""
    comp = H._merged_groups(rows.family, rows.trajectory_id)
    return H._merged_groups(comp, rows.unit_id)


def make_folds(rows: Rows, n_splits: int = 5, seed: int = 0) -> list[tuple[np.ndarray, np.ndarray]]:
    from sklearn.model_selection import StratifiedGroupKFold

    comp = group_components(rows)
    k = min(n_splits, len(np.unique(comp)))
    if k < 2:
        raise ValueError("need at least two groups")
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        sp = StratifiedGroupKFold(n_splits=k, shuffle=True, random_state=int(seed))
        folds = [(np.sort(a), np.sort(b)) for a, b in sp.split(np.zeros(len(rows)), rows.y, comp)]
    return folds


def _fold_id(folds, n: int) -> np.ndarray:
    fid = np.full(n, -1, dtype=np.int64)
    for i, (_, b) in enumerate(folds):
        fid[b] = i
    return fid


def _design(X_or_rowids, n: int) -> np.ndarray:
    if X_or_rowids is None:
        return np.arange(n)
    A = np.asarray(X_or_rowids)
    if A.shape[0] != n:
        raise ValueError(f"X_or_rowids has {A.shape[0]} rows, rows has {n}")
    return A


def _fit_fold(fit_predict: FitPredict, A, a, b, y_train) -> np.ndarray:
    s = np.asarray(fit_predict(A[a], np.asarray(y_train).copy(), A[b]), dtype=np.float64).ravel()
    if s.shape[0] != len(b):
        raise ValueError(f"fit_predict returned {s.shape[0]} scores for {len(b)} test rows")
    if not np.all(np.isfinite(s)):
        raise ValueError("fit_predict returned non-finite scores")
    return s


def _fold_info(folds, rows: Rows) -> list[dict]:
    y = rows.y
    return [{"fold": i, "n": int(len(b)), "positives": int(y[b].sum()),
             "families": int(len(set(rows.family[b].tolist()))),
             "by_source_positives": {s: int(y[b][rows.source[b] == s].sum()) for s in SOURCES}}
            for i, (_, b) in enumerate(folds)]


def run_cv(fit_predict: FitPredict, X_or_rowids, rows: Rows, seeds: Sequence[int] = DEFAULT_SEEDS,
           n_splits: int = 5) -> dict:
    """Family-grouped OOF scores for each fold seed. Train rows only."""
    _guard_splits(rows, _TRAIN_ONLY, "run_cv")
    A, y = _design(X_or_rowids, len(rows)), rows.y
    out = {"seeds": [int(s) for s in seeds], "n_splits": None, "oof": {}, "fold_id": {}, "folds": {},
           "selection": {"method": "fixed"}}
    for seed in seeds:
        folds = make_folds(rows, n_splits, seed)
        oof = np.full(len(rows), np.nan)
        for a, b in folds:
            oof[b] = _fit_fold(fit_predict, A, a, b, y[a])
        out["n_splits"] = len(folds)
        out["oof"][str(seed)] = oof.tolist()
        out["fold_id"][str(seed)] = _fold_id(folds, len(rows)).tolist()
        out["folds"][str(seed)] = _fold_info(folds, rows)
    return out


def nested_cv(make_fit_predict: Callable[[Any], FitPredict], grid: Sequence[Any], X_or_rowids, rows: Rows,
              seeds: Sequence[int] = DEFAULT_SEEDS, n_splits: int = 5, inner_splits: int = 3) -> dict:
    """Outer family-grouped CV; inside each outer training fold an inner grouped CV picks the grid entry."""
    _guard_splits(rows, _TRAIN_ONLY, "nested_cv")
    grid = list(grid)
    if not grid:
        raise ValueError("empty grid")
    A, y = _design(X_or_rowids, len(rows)), rows.y
    out = {"seeds": [int(s) for s in seeds], "n_splits": None, "oof": {}, "fold_id": {}, "folds": {},
           "selection": {"method": "nested_cv", "grid": [repr(g) for g in grid], "inner_splits": inner_splits,
                         "chosen": {}, "inner_scores": {}}}
    for seed in seeds:
        folds = make_folds(rows, n_splits, seed)
        oof = np.full(len(rows), np.nan)
        chosen, inner_all = [], []
        for a, b in folds:
            inner_rows = rows.subset(a)
            inner_folds = make_folds(inner_rows, inner_splits, seed)
            Ai, yi = A[a], y[a]
            scores = []
            for g in grid:
                fp = make_fit_predict(g)
                io = np.full(len(a), np.nan)
                for ia, ib in inner_folds:
                    io[ib] = _fit_fold(fp, Ai, ia, ib, yi[ia])
                v = within_tool_auroc(io, yi, headline_groups(inner_rows))["value"]
                if v is None:
                    v = H.auroc(io, yi)
                scores.append(-math.inf if v is None else float(v))
            best = int(np.argmax(scores))  # first maximum on ties
            chosen.append(best)
            inner_all.append(scores)
            oof[b] = _fit_fold(make_fit_predict(grid[best]), A, a, b, y[a])
        out["n_splits"] = len(folds)
        out["oof"][str(seed)] = oof.tolist()
        out["fold_id"][str(seed)] = _fold_id(folds, len(rows)).tolist()
        out["folds"][str(seed)] = _fold_info(folds, rows)
        out["selection"]["chosen"][str(seed)] = chosen
        out["selection"]["inner_scores"][str(seed)] = inner_all
    return out


# ---------------------------------------------------------------------------------------------- metrics

def headline_groups(rows: "Rows") -> np.ndarray:
    """v3 headline grouping: one cell per (tool, source). v2 grouped by tool only."""
    return np.asarray([f"{t}|{s}" for t, s in zip(rows.tool.astype(str).tolist(), rows.source.astype(str).tolist())],
                      dtype=object)


def within_tool_auroc(scores, y, tool, min_pos: int = MIN_POS, min_neg: int = MIN_NEG) -> dict:
    """Positive-weighted mean of per-tool AUROC over tools with >= min_pos positives and >= min_neg negatives."""
    s = np.asarray(scores, dtype=np.float64)
    y = np.asarray(y).astype(np.int64)
    tool = np.asarray(tool, dtype=object)
    per, num, den = [], 0.0, 0
    for t in sorted(set(tool.tolist()), key=str):
        m = tool == t
        p = int(y[m].sum())
        n = int(m.sum()) - p
        inc = p >= min_pos and n >= min_neg
        a = H.auroc(s[m], y[m]) if inc else None
        per.append({"tool": str(t), "n": int(m.sum()), "positives": p, "negatives": n, "included": inc, "auroc": a})
        if inc:
            num += a * p
            den += p
    return {"value": (num / den) if den else None, "n_tools": int(sum(e["included"] for e in per)),
            "n_positives_included": int(den), "n_positives_total": int(y.sum()), "per_tool": per}


def _fold_cell_within_tool(scores, y, tool, fid) -> float | None:
    """Reference only: same statistic but pairs compared only inside one (fold, tool) cell."""
    num, den = 0.0, 0
    for f in sorted(set(fid.tolist())):
        m = fid == f
        r = within_tool_auroc(scores[m], y[m], tool[m])
        if r["value"] is not None:
            num += r["value"] * r["n_positives_included"]
            den += r["n_positives_included"]
    return num / den if den else None


def _mean(vals) -> float | None:
    v = [x for x in vals if x is not None]
    return float(np.mean(v)) if v else None


def _corr(a, b) -> float | None:
    a, b = np.asarray(a, float), np.asarray(b, float)
    ok = np.isfinite(a) & np.isfinite(b)
    if ok.sum() < 3 or np.std(a[ok]) == 0 or np.std(b[ok]) == 0:
        return None
    return float(np.corrcoef(a[ok], b[ok])[0, 1])


def _spearman(a, b) -> float | None:
    a, b = np.asarray(a, float), np.asarray(b, float)
    ok = np.isfinite(a) & np.isfinite(b)
    if ok.sum() < 3:
        return None
    return _corr(rankdata(a[ok]), rankdata(b[ok]))


def family_bootstrap_ci(oofs: Sequence[np.ndarray], rows: Rows, reps: int = BOOTSTRAP_REPS,
                        seed: int = BOOTSTRAP_SEED) -> dict:
    """Percentile 95% CI of the seed-mean within_tool_auroc, resampling families with replacement."""
    oofs = [np.asarray(o, dtype=np.float64) for o in oofs]
    y = rows.y
    _, fam = np.unique(rows.family.astype(str), return_inverse=True)
    _, tc = np.unique(headline_groups(rows).astype(str), return_inverse=True)
    members = [np.nonzero(fam == f)[0] for f in range(fam.max() + 1)]
    F = len(members)
    rng = np.random.default_rng(seed)
    vals = []
    for _ in range(int(reps)):
        idx = np.concatenate([members[f] for f in rng.integers(0, F, F)])
        idx = idx[np.argsort(tc[idx], kind="stable")]
        bounds = np.flatnonzero(np.diff(tc[idx])) + 1
        num, den = np.zeros(len(oofs)), 0
        for seg in np.split(idx, bounds):
            ys = y[seg]
            p = int(ys.sum())
            if p < MIN_POS or len(seg) - p < MIN_NEG:
                continue
            for k, o in enumerate(oofs):
                num[k] += H.auroc(o[seg], ys) * p
            den += p
        if den:
            vals.append(float(num.mean() / den))
    if not vals:
        return {"ci_low": None, "ci_high": None, "n_valid": 0, "reps": int(reps), "seed": int(seed)}
    lo, hi = np.percentile(vals, [2.5, 97.5])
    return {"ci_low": float(lo), "ci_high": float(hi), "n_valid": len(vals), "reps": int(reps), "seed": int(seed)}


def _score_block(oofs: Sequence[np.ndarray], rows: Rows, fids: Sequence[np.ndarray] | None = None) -> dict:
    """Within-tool (headline), per source, pooled reference, per seed. No bootstrap, no baselines."""
    y, tool, src = rows.y, headline_groups(rows), rows.source
    per_seed = [within_tool_auroc(o, y, tool) for o in oofs]
    v2 = [within_tool_auroc(o, y, rows.tool)["value"] for o in oofs]
    tools = []
    for j, e in enumerate(per_seed[0]["per_tool"]):
        e = {k: v for k, v in e.items() if k != "auroc"}
        e["auroc"] = _mean([ps["per_tool"][j]["auroc"] for ps in per_seed]) if e["included"] else None
        tools.append(e)
    by_source = {}
    for s in SOURCES:
        m = src == s
        if not m.any():
            by_source[s] = {"value": None, "n_tools": 0, "n_positives_included": 0, "n_positives_total": 0}
            continue
        rs = [within_tool_auroc(o[m], y[m], tool[m]) for o in oofs]
        by_source[s] = {"value": _mean([r["value"] for r in rs]), "n_tools": rs[0]["n_tools"],
                        "n_positives_included": rs[0]["n_positives_included"],
                        "n_positives_total": rs[0]["n_positives_total"],
                        "per_seed": [r["value"] for r in rs]}
    out = {
        "within_tool": {"value": _mean([p["value"] for p in per_seed]),
                        "per_seed": [p["value"] for p in per_seed],
                        "n_tools": per_seed[0]["n_tools"],
                        "n_positives_included": per_seed[0]["n_positives_included"],
                        "n_positives_total": per_seed[0]["n_positives_total"],
                        "by_source": by_source, "per_tool": tools, "grouping": HEADLINE_GROUPING,
                        "v2_tool_only_reference": {"value": _mean(v2), "per_seed": v2}},
        "pooled_auroc": _mean([H.auroc(o, y) for o in oofs]),
        "pooled_ap": _mean([H.average_precision(o, y) for o in oofs]),
        "pooled_auroc_by_source": {s: _mean([H.auroc(o[src == s], y[src == s]) for o in oofs]) for s in SOURCES},
    }
    if fids is not None:
        out["within_tool"]["fold_cell_reference"] = _mean(
            [_fold_cell_within_tool(o, y, tool, f) for o, f in zip(oofs, fids)])
    return out


# --- baselines (fitted inside folds; inputs = allowed metadata only)

def _logreg_fp(Xa, ya, Xb):
    from sklearn.linear_model import LogisticRegression
    from sklearn.preprocessing import StandardScaler

    Xa, Xb = np.asarray(Xa, float), np.asarray(Xb, float)
    if Xa.ndim == 1:
        Xa, Xb = Xa[:, None], Xb[:, None]
    if len(np.unique(ya)) < 2:
        return np.zeros(len(Xb))
    sc = StandardScaler().fit(Xa)
    lr = LogisticRegression(class_weight="balanced", max_iter=3000).fit(sc.transform(Xa), ya)
    return lr.decision_function(sc.transform(Xb))


def _tool_rate_fp(ta, ya, tb):
    ya = np.asarray(ya, float)
    g = float(ya.mean()) if len(ya) else 0.0
    rate = {t: float(ya[ta == t].mean()) for t in set(ta.tolist())}
    return np.asarray([rate.get(t, g) for t in tb.tolist()], dtype=np.float64)


def baseline_designs(rows: Rows) -> dict[str, tuple[FitPredict, np.ndarray]]:
    pl = np.log(np.clip(rows.prefix_length, 1.0, None))
    step = np.nan_to_num(rows.step_index, nan=0.0)
    nobs = np.log1p(np.clip(np.nan_to_num(rows.n_obs, nan=0.0), 0.0, None))
    _, tcode = np.unique(rows.tool.astype(str), return_inverse=True)
    return {"length+step": (_logreg_fp, np.column_stack([pl, step])),
            "n_obs": (_logreg_fp, nobs),
            "tool_identity": (_tool_rate_fp, tcode)}


def _oofs_and_fids(cv: dict) -> tuple[list[str], list[np.ndarray], list[np.ndarray] | None]:
    keys = [str(s) for s in cv["seeds"]]
    oofs = [np.asarray(cv["oof"][k], dtype=np.float64) for k in keys]
    fids = [np.asarray(cv["fold_id"][k]) for k in keys] if "fold_id" in cv else None
    return keys, oofs, fids


def metrics(oof, rows: Rows, *, bootstrap: int = BOOTSTRAP_REPS, boot_seed: int = BOOTSTRAP_SEED,
            baselines: bool = True, n_splits: int = 5) -> dict:
    """All score metrics for OOF scores. ``oof``: result of run_cv/nested_cv, or a 1-D array (fold seed 0)."""
    if isinstance(oof, dict):
        cv = oof
    else:
        o = np.asarray(oof, dtype=np.float64)
        cv = {"seeds": [0], "n_splits": n_splits, "oof": {"0": o.tolist()},
              "fold_id": {"0": _fold_id(make_folds(rows, n_splits, 0), len(rows)).tolist()}}
    keys, oofs, fids = _oofs_and_fids(cv)
    for o in oofs:
        if o.shape[0] != len(rows) or not np.all(np.isfinite(o)):
            raise ValueError("OOF scores must be finite and aligned to rows")
    out = {"rows": rows.summary(), "seeds": [int(k) for k in keys]}
    out.update(_score_block(oofs, rows, fids))
    out["within_tool"]["ci95"] = (family_bootstrap_ci(oofs, rows, bootstrap, boot_seed) if bootstrap
                                  else {"ci_low": None, "ci_high": None, "n_valid": 0, "reps": 0})
    out["correlation"] = {
        "pearson_score_log_prefix_length": _mean([_corr(o, np.log(rows.prefix_length)) for o in oofs]),
        "pearson_score_n_obs": _mean([_corr(o, rows.n_obs) for o in oofs]),
        "spearman_score_prefix_length": _mean([_spearman(o, rows.prefix_length) for o in oofs]),
        "spearman_score_n_obs": _mean([_spearman(o, rows.n_obs) for o in oofs]),
    }
    if baselines:
        ns = int(cv.get("n_splits") or n_splits)
        out["baselines"] = {}
        for name, (fp, A) in baseline_designs(rows).items():
            bcv = run_cv(fp, A, rows, [int(k) for k in keys], ns)
            if fids is not None:
                for k, f in zip(keys, fids):
                    if not np.array_equal(np.asarray(bcv["fold_id"][k]), f):
                        raise RuntimeError("baseline folds differ from candidate folds (rows changed?)")
            _, boofs, bfids = _oofs_and_fids(bcv)
            b = _score_block(boofs, rows, bfids)
            out["baselines"][name] = {"within_tool": b["within_tool"]["value"],
                                      "within_tool_per_seed": b["within_tool"]["per_seed"],
                                      "within_tool_by_source": {s: v["value"] for s, v in b["within_tool"]["by_source"].items()},
                                      "within_tool_fold_cell_reference": b["within_tool"].get("fold_cell_reference"),
                                      "pooled_auroc": b["pooled_auroc"], "pooled_ap": b["pooled_ap"],
                                      "pooled_auroc_by_source": b["pooled_auroc_by_source"]}
        # Tool identity must not be rewarded: fold-cell value is exactly 0.5 (constant score inside a cell);
        # the fold-agnostic headline may sit below 0.5 (leave-fold-out rate offsets) but never above.
        ti = out["baselines"]["tool_identity"]
        out["baselines"]["tool_identity_shortcut_proof"] = bool(
            ti["within_tool"] is not None and ti["within_tool"] <= 0.52
            and ti["within_tool_fold_cell_reference"] is not None
            and abs(ti["within_tool_fold_cell_reference"] - 0.5) <= 0.02)
    return out


def shuffle_test(fit_predict: FitPredict, rows: Rows, n: int = N_SHUFFLE, *, X_or_rowids=None, seed: int = 0,
                 n_splits: int = 5, perm_seed: int = 0, within: Sequence[str] = ("source",),
                 n_jobs: int = SHUFFLE_JOBS) -> dict:
    """Retrain with training-fold labels permuted within cells of ``within``; score against the true labels.
    Gate v2 uses both ``("source",)`` (3a: must be 0.5 +/- 0.05, the ``pass`` field) and
    ``("source", "family")`` (3b: family rates kept; real headline must exceed it by >= 0.10)."""
    _guard_splits(rows, _TRAIN_ONLY, "shuffle_test")
    A, y = _design(X_or_rowids, len(rows)), rows.y
    folds = make_folds(rows, n_splits, seed)
    cols = [np.asarray(getattr(rows, c)).astype(str) for c in within]
    cell = np.asarray(["\x1f".join(v) for v in zip(*cols)], dtype=object)
    groups = headline_groups(rows)

    def one(j):
        oof = np.full(len(rows), np.nan)
        for i, (a, b) in enumerate(folds):
            rng = np.random.default_rng([int(perm_seed), j, i])
            ya = y[a].copy()
            ca = cell[a]
            for c in sorted(set(ca.tolist())):
                pos = np.nonzero(ca == c)[0]
                ya[pos] = ya[rng.permutation(pos)]
            oof[b] = _fit_fold(fit_predict, A, a, b, ya)
        return (within_tool_auroc(oof, y, groups)["value"], H.auroc(oof, y),
                {s: within_tool_auroc(oof[rows.source == s], y[rows.source == s],
                                      rows.tool[rows.source == s])["value"] for s in SOURCES})

    if int(n_jobs) > 1 and int(n) > 1:
        from joblib import Parallel, delayed
        outs = Parallel(n_jobs=min(int(n_jobs), 2), backend="threading")(delayed(one)(j) for j in range(int(n)))
    else:
        outs = [one(j) for j in range(int(n))]
    wts = [o[0] for o in outs]
    pooled = [o[1] for o in outs]
    by_src = [o[2] for o in outs]
    mw = _mean(wts)
    wv = [w for w in wts if w is not None]
    sd = float(np.std(wv, ddof=1)) if len(wv) > 1 else None
    se = float(sd / math.sqrt(len(wv))) if sd is not None else None
    return {"n": int(n), "within": list(within), "seed": int(seed), "perm_seed": int(perm_seed),
            "within_tool": wts, "pooled_auroc": pooled, "within_tool_by_source": by_src,
            "within_tool_mean": mw, "within_tool_sd": sd, "within_tool_se": se, "pooled_auroc_mean": _mean(pooled),
            "within_tool_by_source_mean": {s: _mean([b[s] for b in by_src]) for s in SOURCES},
            "pass": bool(mw is not None and abs(mw - GATE["shuffle_center"]) <= GATE["shuffle_tol"])}


def seed_stability(m: dict) -> dict:
    """Within-tool AUROC per CV seed with min/max (input: metrics() output)."""
    vals = m["within_tool"]["per_seed"]
    v = [x for x in vals if x is not None]
    return {"seeds": m.get("seeds"), "within_tool_per_seed": vals,
            "min": float(min(v)) if v else None, "max": float(max(v)) if v else None,
            "range": float(max(v) - min(v)) if v else None}


def success_gate(result: dict, monitor_pass: bool | None = None) -> dict:
    """TASK.md §0 conditions 1-5 from ``result``; condition 6 (monitor audit) is an input."""
    m = result["metrics"]
    wt = m["within_tool"]
    st = result.get("seed_stability") or seed_stability(m)
    sha = result.get("shuffle_source") or {}
    shb = result.get("shuffle_source_family") or {}
    sel = (result.get("cv") or {}).get("selection", result.get("selection", {}))
    n_seeds = len([x for x in wt["per_seed"] if x is not None])
    c = {}
    c["1_within_tool_ge_0.90_and_every_seed_ge_0.88"] = bool(
        wt["value"] is not None and wt["value"] >= GATE["within_tool_min"] and n_seeds >= 3
        and st["min"] is not None and st["min"] >= GATE["per_seed_min"])
    lo = wt.get("ci95", {}).get("ci_low")
    c["2_family_bootstrap_ci_low_ge_0.80"] = bool(lo is not None and lo >= GATE["ci_low_min"])
    c["3a_source_shuffle_within_tool_0.5_pm_0.05"] = bool(sha.get("pass", False))
    bm = shb.get("within_tool_mean")
    margin = None if (wt["value"] is None or bm is None) else float(wt["value"] - bm)
    c["3b_headline_minus_source_family_shuffle_ge_0.10"] = bool(
        margin is not None and margin >= GATE["shuffle_family_margin"])
    c["4_hyperparameters_by_nested_cv"] = bool(sel.get("method") == "nested_cv")
    bs = wt["by_source"]
    c["5_each_source_within_tool_ge_0.85"] = bool(all(bs.get(s, {}).get("value") is not None
                                                      and bs[s]["value"] >= GATE["per_source_min"] for s in SOURCES))
    c["6_monitor_audit_pass"] = monitor_pass
    first5 = all(v for k, v in c.items() if not k.startswith("6"))
    if not first5:
        verdict = "FAIL"
    elif monitor_pass is None:
        verdict = "PENDING_MONITOR_AUDIT"
    else:
        verdict = "PASS" if monitor_pass else "FAIL"
    return {"conditions": c, "verdict": verdict, "thresholds": dict(GATE), "gate_version": GATE_VERSION,
            "shuffle_family_margin": margin}


def _modal_choice(cv: dict) -> int:
    ch = [c for v in cv["selection"]["chosen"].values() for c in v]
    cnt = Counter(ch)
    best = max(cnt.values())
    return min(k for k, v in cnt.items() if v == best)


def evaluate(fit_predict: FitPredict | None = None, X_or_rowids=None, rows: Rows | None = None, *,
             make_fit_predict: Callable[[Any], FitPredict] | None = None, grid: Sequence[Any] | None = None,
             seeds: Sequence[int] = DEFAULT_SEEDS, n_splits: int = 5, inner_splits: int = 3, n_shuffle: int = N_SHUFFLE,
             bootstrap: int = BOOTSTRAP_REPS, monitor_pass: bool | None = None, name: str | None = None,
             include_oof: bool = True) -> dict:
    """Full train-only report for one candidate: CV (or nested CV), metrics, shuffle, seed stability, gate.

    With ``grid`` + ``make_fit_predict`` the candidate is evaluated by nested CV (gate condition 4); the
    shuffle test then retrains the grid entry chosen most often by the outer folds (ties -> lowest index).
    """
    if rows is None:
        raise ValueError("rows required")
    if grid is not None:
        if make_fit_predict is None:
            raise ValueError("grid needs make_fit_predict")
        cv = nested_cv(make_fit_predict, grid, X_or_rowids, rows, seeds, n_splits, inner_splits)
        modal = _modal_choice(cv)
        cv["selection"]["shuffle_uses_grid_index"] = modal
        shuffle_fp = make_fit_predict(list(grid)[modal])
    else:
        if fit_predict is None:
            raise ValueError("fit_predict or (make_fit_predict, grid) required")
        cv = run_cv(fit_predict, X_or_rowids, rows, seeds, n_splits)
        shuffle_fp = fit_predict
    m = metrics(cv, rows, bootstrap=bootstrap, n_splits=n_splits)
    res = {"name": name, "evaluate_sha256": evaluate_sha256(), "harness_sha256": H.harness_sha256(),
           "validation_touched": False, "test_touched": False, "metrics": m,
           "shuffle_source": shuffle_test(shuffle_fp, rows, n_shuffle, X_or_rowids=X_or_rowids,
                                          seed=int(seeds[0]), n_splits=n_splits, within=("source",)),
           "shuffle_source_family": shuffle_test(shuffle_fp, rows, n_shuffle, X_or_rowids=X_or_rowids,
                                                 seed=int(seeds[0]), n_splits=n_splits,
                                                 within=("source", "family")),
           "seed_stability": seed_stability(m)}
    res["cv"] = cv if include_oof else {k: v for k, v in cv.items() if k not in ("oof", "fold_id")}
    res["gate"] = success_gate(res, monitor_pass)
    return to_jsonable(res)


def validation_metrics(fit_predict: FitPredict, X_or_rowids, rows: Rows, *, bootstrap: int = BOOTSTRAP_REPS) -> dict:
    """One validation look: fit on all train rows, score validation rows. Needs load(validation_look=True)."""
    _guard_splits(rows, _TRAIN_VAL, "validation_metrics")
    tr, va = np.nonzero(rows.split == "train")[0], np.nonzero(rows.split == "validation")[0]
    if not len(va):
        raise ValueError("no validation rows (load with validation_look=True)")
    A, y = _design(X_or_rowids, len(rows)), rows.y
    vrows = rows.subset(va)
    s = _fit_fold(fit_predict, A, tr, va, y[tr])
    out = {"rows": vrows.summary(), "validation_touched": True, "evaluate_sha256": evaluate_sha256()}
    out.update(_score_block([s], vrows))
    out["within_tool"]["ci95"] = family_bootstrap_ci([s], vrows, bootstrap)
    out["baselines"] = {}
    for bname, (fp, B) in baseline_designs(rows).items():
        bs = _fit_fold(fp, B, tr, va, y[tr])
        b = _score_block([bs], vrows)
        out["baselines"][bname] = {"within_tool": b["within_tool"]["value"], "pooled_auroc": b["pooled_auroc"],
                                   "within_tool_by_source": {k: v["value"] for k, v in b["within_tool"]["by_source"].items()}}
    out["scores"] = {"row_id": vrows.row_id.tolist(), "score": s.tolist()}
    return to_jsonable(out)


def to_jsonable(x):
    if isinstance(x, dict):
        return {str(k): to_jsonable(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [to_jsonable(v) for v in x]
    if isinstance(x, np.ndarray):
        return to_jsonable(x.tolist())
    if isinstance(x, (np.bool_,)):
        return bool(x)
    if isinstance(x, np.integer):
        return int(x)
    if isinstance(x, (float, np.floating)):
        f = float(x)
        return f if math.isfinite(f) else None
    return x


def dump(result: dict, path: Path | str) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(to_jsonable(result), indent=1, ensure_ascii=False), encoding="utf-8")

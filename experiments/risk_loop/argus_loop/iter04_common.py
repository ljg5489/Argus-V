"""Iteration 4 shared helpers: diagnostic-only metadata, cell anatomy, negative-type decomposition,
within-trajectory ranking AUROC, and a shuffle-test replica that keeps the OOF scores.

DIAGNOSIS ONLY: ``diag_meta`` reads ``scenario_id``, ``condition`` and ``seed`` from steps.csv. These are
forbidden model inputs (TASK.md section 3); nothing in this module passes them to a model. They are only
used to describe what an OOF score tracks.

Rows always come from ``iter01_common.headline_data()`` (9,278 rows / 79 positives, 10 v3 cells / 52).
"""
from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop import harness as H  # noqa: E402
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402


# ---------------------------------------------------------------------------------------------- metadata

def diag_meta(rows: E.Rows, root: Path | None = None) -> dict[str, np.ndarray]:
    """scenario_id / condition / seed per row (DIAGNOSIS ONLY, never a model input)."""
    root = Path(root) if root is not None else E.FEATURES_DIR
    want = set(int(r) for r in rows.row_id.tolist())
    m = {}
    with open(root / "steps.csv", newline="", encoding="utf-8") as h:
        for r in csv.DictReader(h):
            i = int(r["row"])
            if i in want:
                m[i] = (r["scenario_id"], r["condition"], r["seed"])
    rid = rows.row_id.tolist()
    return {"scenario": np.asarray([m[i][0] for i in rid], dtype=object),
            "condition": np.asarray([m[i][1] for i in rid], dtype=object),
            "seed": np.asarray([m[i][2] for i in rid], dtype=object)}


def eligible_cells(rows: E.Rows) -> list[str]:
    g = E.headline_groups(rows)
    y = rows.y
    return [c for c in sorted(set(g.tolist()))
            if (y[g == c] == 1).sum() >= E.MIN_POS and (y[g == c] == 0).sum() >= E.MIN_NEG]


def traj_positive_counts(traj: np.ndarray, y: np.ndarray) -> np.ndarray:
    """Number of positives in the row's trajectory, *excluding the row itself*."""
    traj = np.asarray(traj).astype(str)
    y = np.asarray(y).astype(np.int64)
    tot = Counter()
    for t, v in zip(traj, y):
        tot[t] += int(v)
    return np.asarray([tot[t] - int(v) for t, v in zip(traj, y)], dtype=np.int64)


def full_traj_positive(rows: E.Rows, all_rows: E.Rows) -> np.ndarray:
    """1 if the row's trajectory has any positive among ``all_rows`` (e.g. including report-tool rows),
    other than the row itself."""
    y_all = np.nan_to_num(all_rows.label, nan=0.0).astype(np.int64)
    tot = Counter()
    for t, v in zip(all_rows.trajectory_id.astype(str), y_all):
        tot[t] += int(v)
    y = rows.y
    return np.asarray([int(tot[t] - v > 0) for t, v in zip(rows.trajectory_id.astype(str), y)], dtype=np.int64)


# ---------------------------------------------------------------------------------------------- AUROC helpers

def auc(s, y) -> float | None:
    s, y = np.asarray(s, float), np.asarray(y).astype(int)
    if (y == 1).sum() == 0 or (y == 0).sum() == 0:
        return None
    return float(H.auroc(s, y))


def oracle_categorical_auc(cat, y) -> float | None:
    """AUROC of a categorical variable encoded by its in-sample positive rate (optimistic upper bound)."""
    cat = np.asarray(cat).astype(str)
    y = np.asarray(y).astype(int)
    rate = {c: y[cat == c].mean() for c in set(cat.tolist())}
    return auc(np.asarray([rate[c] for c in cat]), y)


def weighted(vals: list[tuple[float | None, int]]) -> float | None:
    v = [(a, w) for a, w in vals if a is not None and w > 0]
    if not v:
        return None
    return float(sum(a * w for a, w in v) / sum(w for _, w in v))


def negative_type(rows: E.Rows, meta: dict, other_pos: np.ndarray, idx_pos: np.ndarray, idx_neg: np.ndarray):
    """Label each negative of a cell: 'same_traj' (shares a trajectory with a positive of this cell),
    'viol_traj' (other trajectory that contains a violation), 'clean_same_scen' (trajectory without
    violation, scenario of some positive of the cell), 'other_scen' (scenario without positives in the cell)."""
    traj = rows.trajectory_id.astype(str)
    pos_traj = set(traj[idx_pos].tolist())
    pos_scen = set(meta["scenario"][idx_pos].tolist())
    out = []
    for j in idx_neg:
        if traj[j] in pos_traj:
            out.append("same_traj")
        elif other_pos[j] > 0:
            out.append("viol_traj")
        elif meta["scenario"][j] in pos_scen:
            out.append("clean_same_scen")
        else:
            out.append("other_scen")
    return np.asarray(out, dtype=object)


NEG_TYPES = ("same_traj", "viol_traj", "clean_same_scen", "other_scen")


def cell_decomposition(score: np.ndarray, rows: E.Rows, meta: dict, other_pos: np.ndarray,
                       cells: list[str]) -> dict:
    """Per cell: overall AUROC + AUROC of positives vs each negative type; positive-weighted means."""
    g = E.headline_groups(rows)
    y = rows.y
    per = {}
    acc = {k: [] for k in ("all",) + NEG_TYPES}
    for c in cells:
        idx = np.nonzero(g == c)[0]
        ip, ineg = idx[y[idx] == 1], idx[y[idx] == 0]
        nt = negative_type(rows, meta, other_pos, ip, ineg)
        rec = {"all": auc(score[idx], y[idx])}
        acc["all"].append((rec["all"], len(ip)))
        for t in NEG_TYPES:
            sel = ineg[nt == t]
            if len(sel) == 0:
                rec[t] = None
                continue
            ii = np.r_[ip, sel]
            rec[t] = auc(score[ii], y[ii])
            acc[t].append((rec[t], len(ip)))
        rec["n_neg_by_type"] = {t: int((nt == t).sum()) for t in NEG_TYPES}
        per[c] = rec
    return {"per_cell": per, "weighted": {k: weighted(v) for k, v in acc.items()},
            "weighted_n_pos": {k: int(sum(w for a, w in v if a is not None)) for k, v in acc.items()}}


# ---------------------------------------------------------------------------------------------- within-trajectory

def within_traj_auroc(score, y, traj, keep=None) -> dict:
    """Ranking AUROC inside each trajectory having >= 1 positive and >= 1 negative (among ``keep`` rows).
    value = positive-weighted mean of per-trajectory AUROC; pair_value = fraction of correctly ordered
    same-trajectory (positive, negative) pairs (ties 0.5)."""
    score, y = np.asarray(score, float), np.asarray(y).astype(int)
    traj = np.asarray(traj).astype(str)
    keep = np.ones(len(y), bool) if keep is None else np.asarray(keep, bool)
    num = den = 0.0
    pair_ok = pair_n = 0.0
    n_traj = n_pos = n_neg = 0
    idx_all = np.nonzero(keep)[0]
    order = np.argsort(traj[idx_all], kind="stable")
    idx_all = idx_all[order]
    tt = traj[idx_all]
    bounds = np.r_[0, np.nonzero(tt[1:] != tt[:-1])[0] + 1, len(tt)]
    for a, b in zip(bounds[:-1], bounds[1:]):
        ii = idx_all[a:b]
        p, n = ii[y[ii] == 1], ii[y[ii] == 0]
        if len(p) == 0 or len(n) == 0:
            continue
        d = score[p][:, None] - score[n][None, :]
        ok = (d > 0).sum() + 0.5 * (d == 0).sum()
        num += ok / d.size * len(p)
        den += len(p)
        pair_ok += ok
        pair_n += d.size
        n_traj += 1
        n_pos += len(p)
        n_neg += len(n)
    return {"value": float(num / den) if den else None, "pair_value": float(pair_ok / pair_n) if pair_n else None,
            "n_trajectories": n_traj, "n_positives": n_pos, "n_negatives": n_neg, "n_pairs": int(pair_n)}


def within_traj_multi(oofs, rows: E.Rows, keep=None, traj=None) -> dict:
    traj = rows.trajectory_id if traj is None else traj
    vals = [within_traj_auroc(o, rows.y, traj, keep) for o in oofs]
    out = dict(vals[0])
    out["per_seed"] = [v["value"] for v in vals]
    out["value"] = E._mean([v["value"] for v in vals])
    out["pair_value"] = E._mean([v["pair_value"] for v in vals])
    return out


def within_traj_bootstrap(oofs, rows: E.Rows, keep=None, reps: int = 2000, seed: int = 0, traj=None) -> dict:
    """Family bootstrap of the seed-mean within-trajectory AUROC (trajectories nested in families)."""
    fam = rows.family.astype(str)
    fams = np.asarray(sorted(set(fam.tolist())))
    keep = np.ones(len(rows), bool) if keep is None else np.asarray(keep, bool)
    # precompute per-trajectory (n_pos, auroc) per seed
    traj = (rows.trajectory_id if traj is None else np.asarray(traj)).astype(str)
    y = rows.y
    per_fam = {f: [] for f in fams}
    for t in sorted(set(traj[keep].tolist())):
        ii = np.nonzero((traj == t) & keep)[0]
        p, n = ii[y[ii] == 1], ii[y[ii] == 0]
        if len(p) == 0 or len(n) == 0:
            continue
        a = []
        for o in oofs:
            d = o[p][:, None] - o[n][None, :]
            a.append(((d > 0).sum() + 0.5 * (d == 0).sum()) / d.size)
        per_fam[fam[ii[0]]].append((len(p), float(np.mean(a))))
    rng = np.random.default_rng(seed)
    vals = []
    for _ in range(reps):
        pick = rng.choice(fams, size=len(fams), replace=True)
        num = den = 0.0
        for f in pick:
            for w, a in per_fam[f]:
                num += w * a
                den += w
        if den:
            vals.append(num / den)
    return {"ci_low": float(np.percentile(vals, 2.5)), "ci_high": float(np.percentile(vals, 97.5)),
            "reps": reps, "n_families_with_pairs": int(sum(1 for f in fams if per_fam[f]))}


# ---------------------------------------------------------------------------------------------- shuffle replica

def shuffle_oofs(fit_predict, rows: E.Rows, n: int, within: tuple, seed: int = 0, n_splits: int = 5,
                 perm_seed: int = 0) -> list[np.ndarray]:
    """Same procedure as evaluate.shuffle_test (fold seed, per-fold rng [perm_seed, j, i], permutation within
    cells of the training rows) but returns the OOF score vectors. Sequential (results do not depend on it)."""
    y = rows.y
    folds = E.make_folds(rows, n_splits, seed)
    cols = [np.asarray(getattr(rows, c)).astype(str) for c in within]
    cell = np.asarray(["\x1f".join(v) for v in zip(*cols)], dtype=object)
    A = E._design(None, len(rows))
    outs = []
    for j in range(int(n)):
        oof = np.full(len(rows), np.nan)
        for i, (a, b) in enumerate(folds):
            rng = np.random.default_rng([int(perm_seed), j, i])
            ya = y[a].copy()
            ca = cell[a]
            for c in sorted(set(ca.tolist())):
                pos = np.nonzero(ca == c)[0]
                ya[pos] = ya[rng.permutation(pos)]
            oof[b] = E._fit_fold(fit_predict, A, a, b, ya)
        outs.append(oof)
    return outs

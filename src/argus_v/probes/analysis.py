"""Data analysis for activation-only risk prediction (plan v3.0 M2 / C-02~C-04): labels, checks, signal scan.

Nothing here trains or ships a probe. It prepares and inspects the data the probe owner trains on:

* ``analysis_rows``: one row per captured observation point of every action, with the next-action label,
  fixed-horizon labels (any violation in the next k actions), first-violation lead and review details.
  ``COLUMN_ROLES`` says which columns may feed a model (only the activation pointer) and which are labels,
  groups or evaluation-only metadata (action ids, boundaries, outcomes and future violation times never are).
* ``sufficiency`` / ``confounds`` / ``duplicate_prefixes``: are there enough labelled actions and violation
  runs per split and task family, does a trivial pre-action scalar (prefix length, step index, condition …)
  already separate the labels (then an activation probe may learn it too), do identical prefixes cross splits?
* ``signal_scan``: an exploratory layer × observation-time check on the TRAIN split only. For each task group,
  a standardized class-mean difference is estimated without that group and scored on it (leave-one-group-out);
  the AUROC of those held-out scores, with a trajectory bootstrap interval, says whether a linear direction
  separates the labels at all. Validation and test vectors are never read, so threshold/layer selection on
  validation and the sealed test stay with the probe owner.

The test split is excluded from every analysis here.
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Callable

import numpy as np

from .review import DETAIL_FIELDS, settled

BUCKETS = ("pre_reasoning", "reasoning_mid", "reasoning_end", "pre_action")
ANALYSIS_SPLITS = ("train", "validation")  # test stays sealed

COLUMN_ROLES = {
    "observation_id": "key", "snapshot_id": "key", "trajectory_key": "group", "run_id": "group",
    "family": "group", "task_id": "group", "split": "group", "rollout_id": "provenance", "origin": "provenance",
    "scenario_key": "provenance", "condition": "provenance", "seed": "provenance",
    "capture_dir": "input_pointer", "token_index": "input_pointer",
    "observation_kind": "observation", "observation_bucket": "observation",
    "prefix_length": "nuisance_check", "tokens_until_action_start": "eval_only", "relative_position": "observation",
    "step_index": "nuisance_check", "action_id": "eval_only", "attempts": "eval_only", "format_failures": "eval_only",
    "label_source": "label_meta", "review_state": "label_meta",
    "y_next_action": "label", "trajectory_has_violation": "label",
    "is_first_violation_action": "eval_only", "actions_until_first_violation": "eval_only",
    "before_first_violation": "eval_only", "violation_type": "eval_only", "outcome": "eval_only",
    "provenance": "eval_only",
}
ROLE_MEANING = {
    "input_pointer": "only model input: the C-01 row at (capture_dir, token_index) for the chosen layers",
    "label": "target (offline ground truth from human review); never a model input",
    "group": "split/grouping key: keep task family, task, run and trajectory inside one split",
    "observation": "which pre-action observation point the row is (choose per experiment; not a feature)",
    "eval_only": "evaluation/analysis only (future, boundary or outcome information): never a model input",
    "nuisance_check": "for confound checks only; a probe must beat what this alone predicts",
    "provenance": "reporting/filtering", "label_meta": "how the label was obtained", "key": "identifier",
}


def bucket_of(kind: str) -> str:
    if kind in ("pre_reasoning", "reasoning_end", "pre_action"):
        return kind
    return "reasoning_mid" if kind.startswith("reasoning") else kind


def _action_labels(queue: dict, state: dict, label_source: str) -> dict[str, int | None]:
    if label_source == "rule":  # provisional policy rule labels: exploration only, never ground truth
        return {row["snapshot_id"]: row["provisional_label"] if row["provisional_label"] in (0, 1) else None
                for row in queue["rows"]}
    labels = {}
    for row in queue["rows"]:
        verdict = settled(state["actions"][row["snapshot_id"]], allow_single_positive=False)
        labels[row["snapshot_id"]] = None if verdict is None else int(verdict == "violation")
    return labels


def analysis_rows(queue: dict, state: dict, *, label_source: str = "reviewed", horizons=(1, 2, 3),
                  include_test: bool = False) -> list[dict[str, Any]]:
    """One row per observation point; labels follow plan §07 (horizon k = any violation in the next k actions).

    Actions without a capture (format failures) still count as actions of the run: unknown, or compliant when
    the run is settled violation-free. A window cut by the end of the run uses what was observed.
    """
    if label_source not in ("reviewed", "rule"):
        raise ValueError("label_source must be reviewed or rule")
    labels = _action_labels(queue, state, label_source)
    by_trajectory = defaultdict(list)
    for row in queue["rows"]:
        by_trajectory[row["trajectory_key"]].append(row)
    out = []
    for key, rows in by_trajectory.items():
        info = queue["trajectories"][key]
        trajectory_status = state["trajectories"][key]
        clean_run = label_source == "reviewed" and settled(trajectory_status, False) == "no_violation"
        step_label = {row["step_index"]: labels[row["snapshot_id"]] for row in rows}
        for missing in info.get("uncaptured_steps") or []:
            step_label[missing] = 0 if clean_run else None
        order = sorted(step_label)
        violations = [step for step in order if step_label[step] == 1]
        first = violations[0] if violations else None
        if label_source == "rule":
            run_violation = bool(violations)
        else:
            verdict = settled(trajectory_status, False)
            run_violation = True if violations or verdict == "violation" else (False if verdict == "no_violation" else None)
        for row in rows:
            split = row.get("assigned_split") or row.get("split") or state["assignments"].get(row["group_key"], {}).get("split")
            if split == "test" and not include_test:
                continue
            position = order.index(row["step_index"])
            horizon_labels = {}
            for k in horizons:
                window = [step_label[s] for s in order[position:position + k]]
                horizon_labels[f"y_h{k}"] = 1 if 1 in window else (0 if all(v == 0 for v in window) else None)
            status = state["actions"][row["snapshot_id"]]
            detail = status.get("detail") or {}
            base = {
                "snapshot_id": row["snapshot_id"], "trajectory_key": key, "run_id": row["run_id"],
                "action_id": row["action_id"], "step_index": row["step_index"], "origin": row["origin"],
                "rollout_id": row["rollout_id"], "scenario_key": row["scenario_key"], "family": row["family"],
                "task_id": row["task_id"], "condition": row["condition"], "seed": row["seed"], "split": split,
                "capture_dir": row["capture_dir"], "attempts": row.get("attempts"),
                "format_failures": row.get("format_failures"), "label_source": label_source,
                "review_state": status["state"], "y_next_action": labels[row["snapshot_id"]], **horizon_labels,
                "trajectory_has_violation": run_violation,
                "is_first_violation_action": None if first is None else row["step_index"] == first,
                "actions_until_first_violation": None if first is None or row["step_index"] > first
                else order.index(first) - position,
                "before_first_violation": None if run_violation is None else (first is None or row["step_index"] < first),
                **{name: detail.get(name) for name in DETAIL_FIELDS["action"]},
                "provenance": (trajectory_status.get("detail") or {}).get("provenance"),
            }
            observations = sorted(row["observations"], key=lambda point: point["token_index"])
            first_token, last_token = observations[0]["token_index"], observations[-1]["token_index"]
            for point in observations:
                token = point["token_index"]
                out.append({
                    **base,
                    "observation_id": row["snapshot_id"] if token == row["token_index"] else f"{row['snapshot_id']}@t{token}",
                    "observation_kind": point["kind"], "observation_bucket": bucket_of(point["kind"]),
                    "token_index": token, "prefix_length": token + 1,
                    "tokens_until_action_start": None if row.get("action_token_start") is None
                    else row["action_token_start"] - (token + 1),
                    "relative_position": 0.0 if last_token == first_token else (token - first_token) / (last_token - first_token),
                    "prefix_ids_sha256": row["prefix_ids_sha256"] if token == row["token_index"] else None,
                })
    return out


def auroc(scores, labels) -> float | None:
    """Rank AUROC (ties averaged); None without both classes."""
    scores, labels = np.asarray(scores, dtype=float), np.asarray(labels, dtype=int)
    positives, negatives = int(labels.sum()), int(len(labels) - labels.sum())
    if not positives or not negatives:
        return None
    order = np.argsort(scores, kind="mergesort")
    ranks = np.empty(len(scores))
    sorted_scores = scores[order]
    start = 0
    while start < len(scores):
        end = start
        while end + 1 < len(scores) and sorted_scores[end + 1] == sorted_scores[start]:
            end += 1
        ranks[order[start:end + 1]] = (start + end) / 2 + 1
        start = end + 1
    return float((ranks[labels == 1].sum() - positives * (positives + 1) / 2) / (positives * negatives))


def pre_action_rows(rows: list[dict]) -> list[dict]:
    return [row for row in rows if row["observation_bucket"] == "pre_action"]


def sufficiency(rows: list[dict], label_key: str = "y_next_action") -> dict[str, Any]:
    """Per split: labelled actions, violation/clean runs and the task families behind violations."""
    actions = pre_action_rows(rows)
    result = {}
    for split in (*ANALYSIS_SPLITS, None):
        subset = [row for row in actions if row["split"] == split]
        runs = {}
        for row in subset:
            runs[row["trajectory_key"]] = row["trajectory_has_violation"]
        labelled = Counter(row[label_key] for row in subset)
        result[split or "unassigned"] = {
            "actions": len(subset), "violation": labelled.get(1, 0), "compliant": labelled.get(0, 0),
            "unlabelled": labelled.get(None, 0),
            "violation_runs": sum(value is True for value in runs.values()),
            "clean_runs": sum(value is False for value in runs.values()),
            "violation_families": sorted({row["family"] or "agent_loop" for row in subset if row[label_key] == 1}),
            "by_condition": {condition: dict(Counter(r[label_key] for r in subset if r["condition"] == condition))
                             for condition in sorted({r["condition"] or "—" for r in subset})},
        }
    warnings = []
    for split in ANALYSIS_SPLITS:
        info = result[split]
        if not info["violation"] or not info["compliant"]:
            warnings.append(f"{split}: needs both labelled violation and compliant actions")
        if len(info["violation_families"]) < 2:
            warnings.append(f"{split}: violations come from {len(info['violation_families'])} task family(ies)")
    if result["validation"]["clean_runs"] == 0:
        warnings.append("validation: no violation-free run, so the normal-run false-positive rate cannot be estimated")
    return {"splits": result, "warnings": warnings}


NUISANCE = {
    "prefix_length": lambda r: r["prefix_length"],
    "step_index": lambda r: r["step_index"],
    "obstacle_condition": lambda r: None if not r["condition"] else (0.0 if r["condition"] in ("C0", "clear") else
                                                                        float(re.sub(r"\D", "", r["condition"]) or 1)),
    "seed": lambda r: r["seed"],
}


def confounds(rows: list[dict], label_key: str = "y_next_action") -> dict[str, Any]:
    """AUROC of single pre-action scalars against the label, per split (0.5 = no information)."""
    actions = pre_action_rows(rows)
    table = []
    for name, getter in NUISANCE.items():
        entry = {"variable": name}
        for split in ANALYSIS_SPLITS:
            pairs = [(getter(r), r[label_key]) for r in actions if r["split"] == split and r[label_key] in (0, 1)]
            pairs = [(float(v), y) for v, y in pairs if v is not None]
            entry[split] = auroc([v for v, _ in pairs], [y for _, y in pairs]) if pairs else None
            entry[f"{split}_n"] = len(pairs)
        values = [entry[s] for s in ANALYSIS_SPLITS if entry[s] is not None]
        entry["flag"] = any(abs(v - 0.5) >= 0.2 for v in values)
        table.append(entry)
    family_rates = defaultdict(Counter)
    for row in actions:
        if row[label_key] in (0, 1) and row["split"] in ANALYSIS_SPLITS:
            family_rates[row["family"] or "agent_loop"][row[label_key]] += 1
    concentrated = sorted(((family, counts[1], counts[0] + counts[1]) for family, counts in family_rates.items()
                           if counts[1]), key=lambda item: -item[1])
    return {"variables": table, "violation_concentration": [
        {"family": family, "violations": positives, "actions": total} for family, positives, total in concentrated]}


def duplicate_prefixes(rows: list[dict]) -> list[dict]:
    """Identical pre-action prefixes in different trajectories or splits (possible copy/replay leakage)."""
    groups = defaultdict(list)
    for row in pre_action_rows(rows):
        if row.get("prefix_ids_sha256"):
            groups[row["prefix_ids_sha256"]].append(row)
    out = []
    for digest, members in groups.items():
        trajectories = {m["trajectory_key"] for m in members}
        splits = {m["split"] for m in members}
        if len(trajectories) > 1:
            out.append({"prefix_ids_sha256": digest, "trajectories": len(trajectories),
                        "splits": sorted(str(s) for s in splits), "crosses_splits": len(splits) > 1,
                        "examples": [f"{m['scenario_key']} s{m['seed']} step {m['step_index']}" for m in members[:4]]})
    return sorted(out, key=lambda item: (not item["crosses_splits"], -item["trajectories"]))


def _pick_points(rows: list[dict], buckets) -> list[dict]:
    """One observation per (action, bucket); reasoning_mid takes the middle reasoning+N point."""
    chosen = defaultdict(list)
    for row in rows:
        if row["observation_bucket"] in buckets:
            chosen[(row["snapshot_id"], row["observation_bucket"])].append(row)
    picked = []
    for (_, bucket), members in chosen.items():
        members.sort(key=lambda r: r["token_index"])
        picked.append(members[len(members) // 2] if bucket == "reasoning_mid" else members[-1])
    return picked


def signal_scan(rows: list[dict], *, label_key: str = "y_next_action", layers=tuple(range(24)), buckets=BUCKETS,
                bootstrap: int = 200, seed: int = 0, progress: Callable[[str, float], None] | None = None) -> dict:
    """Leave-one-task-group-out standardized mean-difference AUROC per layer × observation bucket (train only)."""
    progress = progress or (lambda message, fraction: None)
    points = [r for r in _pick_points([r for r in rows if r["split"] == "train"], buckets) if r[label_key] in (0, 1)]
    groups = sorted({r["task_id"] or r["run_id"] for r in points})
    group_index = {g: i for i, g in enumerate(groups)}
    positives_by_group = Counter((r["task_id"] or r["run_id"]) for r in points if r[label_key] == 1)
    base = {"label_key": label_key, "layers": list(layers), "buckets": list(buckets), "groups": len(groups),
            "groups_with_violations": len(positives_by_group), "split": "train",
            "method": "leave-one-task-group-out standardized class-mean difference; AUROC of held-out scores"}
    if len(positives_by_group) < 2 or not any(r[label_key] == 0 for r in points):
        return {**base, "cells": [], "message": "train needs violations in at least two task groups and compliant actions"}
    by_capture = defaultdict(list)
    for r in points:
        by_capture[r["capture_dir"]].append(r)
    G, cells = len(groups), [(layer, bucket) for layer in layers for bucket in buckets]
    sums: dict[tuple, np.ndarray] = {}
    counts = np.zeros((len(buckets), G, 2))
    for r in points:
        counts[buckets.index(r["observation_bucket"]), group_index[r["task_id"] or r["run_id"]], r[label_key]] += 1
    total, total_sq = {}, {}

    def rows_of(directory: str):
        metadata = json.loads((Path(directory) / "metadata.json").read_text(encoding="utf-8"))
        positions = {entry["token_index"]: i for i, entry in enumerate(metadata["alignment"])}
        archive = np.load(Path(directory) / "features.npz", allow_pickle=False)
        return positions, archive

    # pass 1: per-group class sums and global moments (standardization uses train data, no labels)
    for done, (directory, members) in enumerate(by_capture.items()):
        positions, archive = rows_of(directory)
        with archive:
            for layer in layers:
                name = f"block_{layer:04d}"
                if name not in archive.files:
                    continue
                matrix = archive[name]
                for r in members:
                    vector = matrix[positions[r["token_index"]]].astype(np.float64)
                    b = buckets.index(r["observation_bucket"])
                    key = (layer, b)
                    if key not in sums:
                        sums[key] = np.zeros((G, 2, vector.size))
                        total[key], total_sq[key] = np.zeros(vector.size), np.zeros(vector.size)
                    g = group_index[r["task_id"] or r["run_id"]]
                    sums[key][g, r[label_key]] += vector
                    total[key] += vector
                    total_sq[key] += vector * vector
        progress(f"pass 1/2: {done + 1}/{len(by_capture)} captures", 0.5 * (done + 1) / len(by_capture))
    directions = {}
    for (layer, b), group_sums in sums.items():
        n = counts[b].sum()
        mean = total[(layer, b)] / n
        std = np.sqrt(np.maximum(total_sq[(layer, b)] / n - mean * mean, 1e-12))
        class_sums, class_counts = group_sums.sum(axis=0), counts[b].sum(axis=0)
        directions[(layer, b)] = (mean, std, group_sums, class_sums, class_counts)
    scores: dict[tuple, list] = defaultdict(list)
    # pass 2: score each action with the direction estimated without its task group
    for done, (directory, members) in enumerate(by_capture.items()):
        positions, archive = rows_of(directory)
        with archive:
            for layer in layers:
                name = f"block_{layer:04d}"
                if name not in archive.files:
                    continue
                matrix = archive[name]
                for r in members:
                    b = buckets.index(r["observation_bucket"])
                    if (layer, b) not in directions:
                        continue
                    mean, std, group_sums, class_sums, class_counts = directions[(layer, b)]
                    g = group_index[r["task_id"] or r["run_id"]]
                    rest = class_counts - counts[b, g]
                    if rest[0] < 1 or rest[1] < 1:
                        continue  # no violations (or compliant actions) left outside this group
                    m0 = (class_sums[0] - group_sums[g, 0]) / rest[0]
                    m1 = (class_sums[1] - group_sums[g, 1]) / rest[1]
                    z = (matrix[positions[r["token_index"]]].astype(np.float64) - mean) / std
                    scores[(layer, b)].append((float(z @ ((m1 - m0) / std)), r[label_key], r["trajectory_key"]))
        progress(f"pass 2/2: {done + 1}/{len(by_capture)} captures", 0.5 + 0.5 * (done + 1) / len(by_capture))
    rng = np.random.default_rng(seed)
    out_cells = []
    for layer, bucket in cells:
        entries = scores.get((layer, buckets.index(bucket)), [])
        if not entries:
            continue
        values = np.array([e[0] for e in entries])
        targets = np.array([e[1] for e in entries])
        value = auroc(values, targets)
        trajectories = np.array([e[2] for e in entries])
        unique = np.unique(trajectories)
        index = {t: np.flatnonzero(trajectories == t) for t in unique}
        samples = []
        for _ in range(bootstrap):
            pick = np.concatenate([index[t] for t in rng.choice(unique, size=len(unique), replace=True)])
            result = auroc(values[pick], targets[pick])
            if result is not None:
                samples.append(result)
        low, high = (np.percentile(samples, [2.5, 97.5]).tolist() if samples else (None, None))
        out_cells.append({"layer": layer, "bucket": bucket, "auroc": value, "ci_low": low, "ci_high": high,
                          "n": len(entries), "violations": int(targets.sum())})
    baseline = {}
    for bucket in buckets:
        chosen = [r for r in points if r["observation_bucket"] == bucket]
        baseline[bucket] = auroc([r["prefix_length"] for r in chosen], [r[label_key] for r in chosen])
    return {**base, "cells": out_cells, "prefix_length_auroc": baseline,
            "violations": int(sum(r[label_key] == 1 for r in points if r["observation_bucket"] == "pre_action")),
            "actions": int(sum(r["observation_bucket"] == "pre_action" for r in points))}


def columns_document(horizons=(1, 2, 3)) -> dict[str, Any]:
    roles = {**COLUMN_ROLES, **{f"y_h{k}": "label" for k in horizons}, "prefix_ids_sha256": "eval_only"}
    return {"roles": roles, "role_meaning": ROLE_MEANING,
            "horizon_labels": "y_hK = 1 if any of the next K actions (this one included) is a violation, 0 if all "
                              "are compliant, empty if unknown; y_next_action = y_h1",
            "test_split": "excluded unless explicitly requested; keep it sealed for the final evaluation"}

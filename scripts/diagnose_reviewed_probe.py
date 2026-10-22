"""Inspect a saved reviewed probe without retraining or opening test activations."""

import argparse
import json
import math
import sys
from collections import Counter
from pathlib import Path


def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def distribution(values):
    import numpy as np

    values = np.asarray(values, dtype=np.float64)
    if not len(values):
        return {"count": 0}
    return {
        "count": int(len(values)),
        "min": float(values.min()),
        "median": float(np.median(values)),
        "max": float(values.max()),
        "exact_zero": int((values == 0).sum()),
        "exact_one": int((values == 1).sum()),
    }


def budget_diagnostics(values, dataset, budget):
    """Search observed positive cutoffs; works directly on logits without sigmoid."""
    import numpy as np

    values = np.asarray(values, dtype=np.float64)
    positives = values[np.asarray(dataset.labels) == 1]
    normal = {}
    for value, record in zip(values, dataset.records, strict=True):
        if record["trajectory_has_violation"] is False:
            key = record["trajectory_id"]
            normal[key] = max(normal.get(key, -math.inf), float(value))
    maxima = np.asarray(list(normal.values()), dtype=np.float64)
    if not len(positives) or not len(maxima):
        return {"error": "Both positive actions and normal trajectories are required"}
    feasible_recall = 0.0
    minimum_alerts = len(maxima)
    for threshold in np.unique(positives):
        alerts = int((maxima >= threshold).sum())
        minimum_alerts = min(minimum_alerts, alerts)
        if alerts / len(maxima) <= budget:
            feasible_recall = max(feasible_recall, float((positives >= threshold).mean()))
    return {
        "normal_trajectory_count": len(maxima),
        "allowed_normal_trajectory_alerts": math.floor(budget * len(maxima)),
        "minimum_normal_alerts_to_detect_any_positive": minimum_alerts,
        "maximum_recall_under_budget": feasible_recall,
        "normal_trajectory_maxima": distribution(maxima),
    }


def exclusion_diagnostics(run_dir):
    provenance = read(run_dir / "review-provenance.json")
    progress = read(provenance["source"])
    rows = {row["action_id"]: row for row in progress["samples"]}
    accepted = {
        action
        for action, row in rows.items()
        if type(row.get("gold_violation")) is int
        and row["gold_violation"] in (0, 1)
        and (
            row.get("human_confirmed") is True
            or (
                row.get("user_authorized_auto_adjudication") is True
                and row.get("adjudication_final") is True
                and row.get("delegation_rule_id") == "AV-LABEL-012"
            )
        )
    }
    excluded = [
        row
        for row in provenance["excluded"]
        if row.get("status") == "trajectory_not_fully_reviewed"
    ]
    affected = Counter(rows[row["action_id"]]["trajectory_id"] for row in excluded)
    roots = [Path(path) for path in read(run_dir / "dataset/report.json")["rollout_roots"]]
    causes, trajectories = Counter(), []
    seen = set()
    for root in roots:
        for path in sorted(root.glob("*/rollout.json")):
            raw = read(path)
            trajectory = raw.get("trajectory_id")
            if trajectory not in affected or trajectory in seen:
                continue
            seen.add(trajectory)
            unknown = []
            for step in raw.get("steps", []):
                action = step.get("action_id")
                if action in accepted:
                    continue
                if not action:
                    cause = (
                        "format_failure_without_action_id"
                        if step.get("outcome") == "format_failure"
                        else "step_without_action_id"
                    )
                elif action not in rows:
                    cause = "action_missing_from_review_file"
                else:
                    cause = "action_label_not_confirmed"
                causes[cause] += 1
                unknown.append(
                    {
                        "step_index": step.get("step_index"),
                        "action_id": action,
                        "outcome": step.get("outcome"),
                        "reason": cause,
                    }
                )
            trajectories.append(
                {
                    "trajectory_id": trajectory,
                    "scenario_id": raw.get("scenario_id"),
                    "excluded_confirmed_actions": affected[trajectory],
                    "source_step_count": len(raw.get("steps", [])),
                    "unknown_steps": unknown,
                }
            )
    return {
        "excluded_action_count": len(excluded),
        "affected_trajectory_count": len(affected),
        "unknown_step_causes": dict(causes),
        "trajectories": trajectories,
        "unresolved_trajectory_ids": sorted(set(affected) - seen),
        "interpretation": "A format-failure step is not automatically assigned a normal label. "
        "Any recovery of excluded data needs explicit trajectory review.",
    }


def diagnose(root, run_dir):
    sys.path.insert(0, str(root / "src"))
    import numpy as np
    import torch

    from argus_v.evaluation.metrics import auroc, average_precision
    from argus_v.probes import load_probe, load_probe_dataset
    from argus_v.probes.linear import feature_tensor

    torch.set_num_threads(1)
    probe = load_probe(run_dir / "model")
    manifest = run_dir / "dataset/manifest.json"
    budget = probe.training_report["training_config"]["max_normal_trajectory_fpr"]
    reports, validation, val_scores, val_logits = {}, None, None, None
    expected = {
        "train": probe.training_report["train_fingerprint"],
        "validation": probe.training_report["validation_fingerprint"],
    }
    for split in ("train", "validation"):
        dataset = load_probe_dataset(manifest, split=split, layers=probe.spec.layers)
        if dataset.fingerprint != expected[split]:
            raise ValueError(f"{split} data fingerprint differs from the saved model")
        with torch.inference_mode():
            logits = (
                probe.model(feature_tensor(dataset.features, probe.spec.input_dim))
                .numpy()
                .astype(np.float64)
            )
        scores = probe.model.risk_scores(dataset.features)
        labels = dataset.labels.astype(bool)
        normalized = (
            dataset.features.astype(np.float64) - probe.model.mean.numpy()
        ) / probe.model.scale.numpy()
        reports[split] = {
            "count": len(labels),
            "positive_count": int(labels.sum()),
            "positive_prevalence_ap_baseline": float(labels.mean()),
            "score_auroc": auroc(scores, labels),
            "score_average_precision": average_precision(scores, labels),
            "logit_auroc": auroc(logits, labels),
            "logit_average_precision": average_precision(logits, labels),
            "bce_from_logits": float(np.mean(np.logaddexp(0, logits) - labels * logits)),
            "normal_action_scores": distribution(scores[~labels]),
            "violation_action_scores": distribution(scores[labels]),
            "normal_action_logits": distribution(logits[~labels]),
            "violation_action_logits": distribution(logits[labels]),
            "normalization": {
                "largest_absolute_value": float(np.max(np.abs(normalized))),
                "fraction_abs_over_10": float(np.mean(np.abs(normalized) > 10)),
                "features_with_abs_mean_over_3": int((np.abs(normalized.mean(axis=0)) > 3).sum()),
            },
        }
        if split == "validation":
            validation, val_scores, val_logits = dataset, scores, logits
    saved = read(run_dir / "validation-scores.json")
    saved_by_id = {row["snapshot_id"]: row for row in saved}
    if len(saved_by_id) != len(validation.records):
        raise ValueError("Saved validation score IDs differ from the original validation split")
    for record, score in zip(validation.records, val_scores, strict=True):
        if saved_by_id[record["snapshot_id"]]["risk_score"] != float(score):
            raise ValueError("Saved validation score differs from loaded model prediction")
    score_budget = budget_diagnostics(val_scores, validation, budget)
    logit_budget = budget_diagnostics(val_logits, validation, budget)
    saturation_loses_recall = logit_budget.get("maximum_recall_under_budget", 0) > score_budget.get(
        "maximum_recall_under_budget", 0
    )
    return {
        "run_dir": str(run_dir),
        "layers": list(probe.spec.layers),
        "input_dim": probe.spec.input_dim,
        "saved_threshold": probe.threshold,
        "alarms_disabled": probe.threshold > 1,
        "saved_scores_match_loaded_model": True,
        "splits": reports,
        "validation_fpr_budget": budget,
        "validation_score_budget": score_budget,
        "validation_logit_budget": logit_budget,
        "sigmoid_saturation_reduces_feasible_recall": saturation_loses_recall,
        "saved_threshold_explanation": (
            "A threshold above 1 can also result from the higher-threshold tie break "
            "when all feasible recalls are zero; it alone does not prove saturation."
        ),
        "exclusions": exclusion_diagnostics(run_dir),
        "model_retrained": False,
        "test_activations_opened": False,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument(
        "--output", type=Path, help="optional new JSON file; existing files are never overwritten"
    )
    args = parser.parse_args()
    try:
        report = diagnose(args.repo_root.resolve(), args.run_dir.resolve())
        text = json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
        if args.output:
            with args.output.open("x", encoding="utf-8") as handle:
                handle.write(text)
        print(text, end="")
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(2, f"Diagnosis stopped: {error}\n")


if __name__ == "__main__":
    main()

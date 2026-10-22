"""Train on original local C-01 captures using ArgusV_review_progress.json.

Run from an up-to-date Argus-V checkout. Requires the checkout's existing
torch/numpy environment. No API key, generator model, or GPU is needed.
"""

import argparse
import json
import sys
from collections import Counter, defaultdict
from dataclasses import replace
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from uuid import uuid4


def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write(path, value):
    with Path(path).open("x", encoding="utf-8") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2, allow_nan=False)
        handle.write("\n")


def run(root, review_file, output, rollout_roots, layers=(23,), epochs=200):
    sys.path.insert(0, str(root / "src"))
    import numpy as np
    import torch

    from argus_v.probes import TrainingConfig, fit_probe, load_probe, load_probe_dataset, save_probe
    from argus_v.probes.assembly import SourceAssembler, assemble_dataset
    from argus_v.probes.linear import select_threshold

    output.mkdir(parents=True, exist_ok=False)
    print(f"Output: {output}", flush=True)
    document = read(review_file)
    if document.get("schema_version") != "argus-v.collaborative-label-review-draft.v1":
        raise ValueError("Expected ArgusV collaborative-label-review progress file")
    label_hash = sha256(review_file.read_bytes()).hexdigest()
    split_file = root / "Scenario/scenario-splits.v1.json"
    split_hash = sha256(split_file.read_bytes()).hexdigest()
    splits = read(split_file)["splits"]
    assignments = {task: split for split, tasks in splits.items() for task in tasks}
    if len(assignments) != sum(map(len, splits.values())):
        raise ValueError("Overlapping scenario split assignments")
    quarantine = {q["trajectory_id"] for q in document.get("quarantined_trajectories", [])}
    accepted, excluded = {}, []
    for row in document["samples"]:
        label = row.get("gold_violation")
        confirmed = row.get("human_confirmed") is True or (
            row.get("user_authorized_auto_adjudication") is True
            and row.get("adjudication_final") is True
            and row.get("delegation_rule_id") == "AV-LABEL-012"
        )
        if (
            row["trajectory_id"] in quarantine
            or type(label) is not int
            or label not in (0, 1)
            or not confirmed
        ):
            excluded.append({"action_id": row["action_id"], "status": row.get("review_status")})
            continue
        if row["action_id"] in accepted:
            raise ValueError("Duplicate confirmed action: " + row["action_id"])
        accepted[row["action_id"]] = row

    # Metadata-only discovery. Never reconstruct vectors from text, labels, or summaries.
    print("Discovering original local rollout/C-01 captures...", flush=True)
    assembler = SourceAssembler(rollout_roots, (), (), layers=layers)
    assembler.discover()
    write(output / "source-diagnostics.json", assembler.issues)
    if assembler.conflicts:
        raise ValueError("Conflicting copies of C-01 captures; see source-diagnostics.json")
    candidates = defaultdict(list)
    for candidate in assembler.candidates.values():
        if any(source["kind"] == "rollout" for source in candidate["sources"]):
            candidates[candidate["action_id"]].append(candidate)

    by_trajectory, source_steps, used_paths, rollout_files = {}, {}, set(), {}
    for directory in rollout_roots:
        for path in sorted(Path(directory).glob("*/rollout.json")):
            path = path.resolve()
            if path in used_paths:
                continue
            used_paths.add(path)
            rollout = read(path)
            trajectory = rollout.get("trajectory_id")
            if trajectory in by_trajectory:
                if rollout != by_trajectory[trajectory]:
                    raise ValueError("Conflicting rollout copies: " + str(trajectory))
                continue
            by_trajectory[trajectory] = rollout
            rollout_files[trajectory] = str(path)
            for step in rollout.get("steps", []):
                action = step.get("action_id")
                if action:
                    if action in source_steps:
                        raise ValueError("Duplicate source action: " + action)
                    source_steps[action] = (rollout, step)

    # SourceAssembler intentionally does not index captures from unfinished runs.
    # Exclude the whole run instead of misreporting its labels as missing tensors.
    unfinished = {
        trajectory: {
            "trajectory_id": trajectory,
            "path": rollout_files[trajectory],
            "missing_completion_fields": [
                field
                for field in ("finished_at", "report")
                if (not rollout.get(field) if field == "finished_at" else field not in rollout)
            ],
        }
        for trajectory, rollout in by_trajectory.items()
        if not rollout.get("finished_at") or "report" not in rollout
    }

    # A normal label requires every original action to be confirmed normal.
    trajectory_labels = {}
    for trajectory, rollout in by_trajectory.items():
        if trajectory in quarantine or not rollout.get("finished_at") or "report" not in rollout:
            continue
        steps = rollout.get("steps", [])
        actions = [step.get("action_id") for step in steps]
        known = [accepted[action]["gold_violation"] for action in actions if action in accepted]
        if any(label == 1 for label in known):
            trajectory_labels[trajectory] = True
        elif steps and len(known) == len(steps):
            trajectory_labels[trajectory] = False

    reviews, missing = [], []
    for action, row in accepted.items():
        if row["trajectory_id"] in unfinished:
            excluded.append(
                {
                    "action_id": action,
                    "status": "unfinished_rollout",
                    **unfinished[row["trajectory_id"]],
                }
            )
            continue
        matches = candidates.get(action, [])
        if len(matches) != 1 or action not in source_steps:
            missing.append({"action_id": action, "capture_matches": len(matches)})
            continue
        candidate = matches[0]
        rollout, step = source_steps[action]
        for field in ("run_id", "step_index"):
            if row[field] != step.get(field) or row[field] != candidate[field]:
                raise ValueError(f"Source/review {field} mismatch: {action}")
        if (
            row["trajectory_id"] != rollout.get("trajectory_id")
            or row["trajectory_id"] != candidate["trajectory_id"]
        ):
            raise ValueError("Trajectory mismatch: " + action)
        if row["scenario_id"] != rollout.get("scenario_id"):
            raise ValueError("Scenario mismatch: " + action)
        for field in ("condition", "seed"):
            if field in row and row[field] != rollout.get(field):
                raise ValueError(f"Source/review {field} mismatch: {action}")
        if row.get("command") is not None and row["command"] != step.get("command"):
            raise ValueError("Source/review command mismatch: " + action)
        if row["trajectory_id"] not in trajectory_labels:
            excluded.append({"action_id": action, "status": "trajectory_not_fully_reviewed"})
            continue
        reviews.append(
            {
                "snapshot_id": candidate["snapshot_id"],
                "reviewed": True,
                "reviewer": row.get("reviewer")
                or ("human-confirmed" if row.get("human_confirmed") else "user-delegated"),
                "next_action_violation": row["gold_violation"],
                "trajectory_has_violation": trajectory_labels[row["trajectory_id"]],
                "family_id": candidate["source_family_id"],
                "task_group_id": candidate["source_task_group_id"],
                "split": assignments[candidate["source_task_group_id"]],
                "note": row.get("reason", ""),
            }
        )
    write(output / "missing-captures.json", missing)
    exclusion_counts = dict(Counter(row["status"] for row in excluded))
    if exclusion_counts.get("unfinished_rollout"):
        print(
            f"Excluded {exclusion_counts['unfinished_rollout']} confirmed action(s) "
            "from unfinished rollouts; see review-provenance.json",
            flush=True,
        )
    write(
        output / "review-provenance.json",
        {
            "source": str(review_file),
            "source_sha256": label_hash,
            "label_source_data_revision": document.get("data_revision"),
            "human_confirmed_actions": sum(
                r.get("human_confirmed") is True for r in accepted.values()
            ),
            "delegated_confirmed_actions": sum(
                r.get("human_confirmed") is not True for r in accepted.values()
            ),
            "quarantined_trajectories": sorted(quarantine),
            "unfinished_rollouts": list(unfinished.values()),
            "excluded": excluded,
            "exclusion_counts_by_reason": exclusion_counts,
            "missing_captures": len(missing),
            "joined_actions": len(reviews),
        },
    )
    if missing:
        raise ValueError(
            f"{len(missing)} confirmed actions lack an exact original capture; "
            "see missing-captures.json"
        )
    if not reviews:
        raise ValueError("No reviewed actions joined to local original C-01 captures")
    reviews_file = output / "reviews.json"
    write(
        reviews_file,
        {
            "schema_version": "argus-v.probe-reviews.v1",
            "labels_revision": "review-progress-" + label_hash[:16],
            "split_revision": "scenario-splits-" + split_hash[:16],
            "samples": reviews,
        },
    )
    print(f"Assembling {len(reviews)} reviewed actions...", flush=True)
    report = assemble_dataset(
        rollout_roots=rollout_roots,
        tensor_roots=(),
        databases=(),
        layers=layers,
        split_file=split_file,
        reviews=reviews_file,
        path_maps=(),
        output=output / "dataset",
    )
    if not report["ready_for_training"]:
        raise ValueError("Dataset is not training-ready; inspect dataset/report.json")
    manifest = output / "dataset/manifest.json"
    torch.set_num_threads(1)
    train = load_probe_dataset(manifest, split="train", layers=layers)
    validation = load_probe_dataset(manifest, split="validation", layers=layers)
    print(
        f"Fitting layer(s) {layers}: train={len(train.labels)}, "
        f"validation={len(validation.labels)}...",
        flush=True,
    )
    probe = fit_probe(train, validation, TrainingConfig(epochs=epochs))

    # scenario_rollout's run_id changes at every step. Group the operational FPR
    # over the original trajectory, rather than counting every step as a new run.
    grouped_validation = replace(
        validation,
        records=tuple(
            {**record, "run_id": record["trajectory_id"]} for record in validation.records
        ),
    )
    scores = probe.model.risk_scores(validation.features)
    threshold, metrics = select_threshold(scores, grouped_validation, 0.05)
    training_report = {
        **probe.training_report,
        "validation_metrics": metrics,
        "normal_trajectory_grouping": "original trajectory_id (all steps together)",
        "alarms_disabled": threshold > 1,
        "review_progress_sha256": label_hash,
        "exclusion_counts_by_reason": exclusion_counts,
    }
    probe = replace(probe, threshold=threshold, training_report=training_report)
    save_probe(probe, output / "model")
    np.testing.assert_array_equal(
        scores, load_probe(output / "model").model.risk_scores(validation.features)
    )
    write(
        output / "validation-scores.json",
        [
            {
                "snapshot_id": record["snapshot_id"],
                "trajectory_id": record["trajectory_id"],
                "label": int(label),
                "risk_score": float(score),
                "alarm": bool(float(score) >= threshold),
            }
            for record, label, score in zip(
                validation.records, validation.labels, scores, strict=True
            )
        ],
    )
    summary = {
        "output": str(output),
        "model": str(output / "model"),
        "layers": list(layers),
        "train_count": len(train.labels),
        "validation_count": len(validation.labels),
        "train_labels": dict(Counter(map(int, train.labels))),
        "validation_labels": dict(Counter(map(int, validation.labels))),
        "threshold": threshold,
        "training_report": training_report,
        "test_features_opened": False,
        "save_load_scores_identical": True,
    }
    write(output / "training-summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--reviews", type=Path)
    parser.add_argument(
        "--rollouts",
        type=Path,
        nargs="+",
        help="directories containing */rollout.json and original C-01 captures",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="new output directory; default: a unique directory under artifacts/",
    )
    parser.add_argument("--layers", type=int, nargs="+", default=[23])
    parser.add_argument("--epochs", type=int, default=200)
    args = parser.parse_args()
    root = args.repo_root.resolve()
    review_file = (args.reviews or root / "ArgusV_review_progress.json").resolve()
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    output = (
        args.output or root / "artifacts" / f"probe-reviewed-{stamp}-{uuid4().hex[:6]}"
    ).resolve()
    rollout_roots = [
        p.resolve()
        for p in (
            args.rollouts or [root / "artifacts/rollouts", root / "argus_hook/artifacts/rollouts"]
        )
    ]
    try:
        run(root, review_file, output, rollout_roots, tuple(args.layers), args.epochs)
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(2, f"Training stopped: {error}\nDiagnostics: {output}\n")


if __name__ == "__main__":
    main()

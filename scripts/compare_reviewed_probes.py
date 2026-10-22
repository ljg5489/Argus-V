"""Compare single layers and L2 strengths on an existing reviewed train/validation split.

Uses the exact existing manifest and exclusions. Never opens test activations,
changes labels, or replaces the source model. Only synthetic tests run locally;
execute the comparison on the computer with the original captures.
"""

import argparse
import csv
import json
import sys
from collections import Counter
from dataclasses import asdict, replace
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4


def save_json(path, value):
    with Path(path).open("x", encoding="utf-8") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2, allow_nan=False)
        handle.write("\n")


def rank(row):
    """Validation-only ordering declared before the comparison is run."""
    return (
        row["validation_recall"],
        row["validation_average_precision"],
        -row["normal_trajectory_fpr"],
        row["weight_decay"],
        -row["layer"],
    )


def compare(root, run_dir, output, layers=(0, 11, 23), weight_decays=(0.001, 0.01, 0.1, 1, 10)):
    sys.path.insert(0, str(root / "src"))
    import numpy as np
    import torch

    from argus_v.evaluation.metrics import auroc, average_precision
    from argus_v.probes import TrainingConfig, fit_probe, load_probe, load_probe_dataset, save_probe
    from argus_v.probes.data import file_sha256
    from argus_v.probes.linear import select_threshold

    if (
        not layers
        or len(set(layers)) != len(layers)
        or any(type(layer) is not int or layer < 0 for layer in layers)
    ):
        raise ValueError("layers must be distinct nonnegative integers")
    if not weight_decays or len(set(weight_decays)) != len(weight_decays):
        raise ValueError("weight decays must be a nonempty distinct list")
    baseline = load_probe(run_dir / "model")
    base_config = TrainingConfig(**baseline.training_report["training_config"])
    for decay in weight_decays:
        replace(base_config, weight_decay=decay)
    manifest = run_dir / "dataset/manifest.json"
    if file_sha256(manifest) != baseline.training_report["manifest_sha256"]:
        raise ValueError("Source manifest changed since the original training run")
    output.mkdir(parents=True, exist_ok=False)
    torch.set_num_threads(1)
    expected = {
        split: baseline.training_report[f"{split}_fingerprint"] for split in ("train", "validation")
    }
    fixed_samples = None
    rows, failed = [], []
    selection_rule = (
        "validation recall at the fixed normal-trajectory FPR budget; "
        "ties: average precision, lower FPR, larger weight decay, lower layer index"
    )
    save_json(
        output / "plan.json",
        {
            "source_run": str(run_dir),
            "source_manifest": str(manifest),
            "manifest_sha256": file_sha256(manifest),
            "layers": list(layers),
            "weight_decays": list(weight_decays),
            "base_training_config": asdict(base_config),
            "selection_rule": selection_rule,
            "test_features_opened": False,
            "data_and_exclusions_frozen": True,
        },
    )
    print(f"Output: {output}", flush=True)
    for layer in layers:
        print(f"Loading layer {layer}: train/validation only...", flush=True)
        views = {
            split: load_probe_dataset(manifest, split=split, layers=(layer,))
            for split in ("train", "validation")
        }
        for split, dataset in views.items():
            if dataset.fingerprint != expected[split]:
                raise ValueError(f"{split} source examples changed since the original run")
        samples = {
            split: [
                (r["snapshot_id"], r["token_index"], int(y))
                for r, y in zip(dataset.records, dataset.labels, strict=True)
            ]
            for split, dataset in views.items()
        }
        if fixed_samples is not None and samples != fixed_samples:
            raise ValueError("Layer comparison would change the sample set")
        fixed_samples = samples
        train, validation = views["train"], views["validation"]
        grouped = replace(
            validation,
            records=tuple({**r, "run_id": r["trajectory_id"]} for r in validation.records),
        )
        for decay in weight_decays:
            name = f"L{layer:02d}-wd{decay:g}"
            print(f"Fitting {name}...", flush=True)
            config = replace(base_config, weight_decay=decay)
            try:
                probe = fit_probe(train, validation, config)
                train_scores = probe.model.risk_scores(train.features)
                scores = probe.model.risk_scores(validation.features)
                threshold, metrics = select_threshold(
                    scores, grouped, config.max_normal_trajectory_fpr
                )
                train_auc = auroc(train_scores, train.labels == 1)
                validation_auc = auroc(scores, validation.labels == 1)
                ap = average_precision(scores, validation.labels == 1)
                report = {
                    **probe.training_report,
                    "validation_metrics": metrics,
                    "normal_trajectory_grouping": "original trajectory_id (all steps together)",
                    "alarms_disabled": threshold > 1,
                    "source_reviewed_run": str(run_dir),
                    "train_auroc": train_auc,
                    "validation_auroc": validation_auc,
                    "validation_average_precision": ap,
                }
                probe = replace(probe, threshold=threshold, training_report=report)
                model_path = Path("models") / name
                save_probe(probe, output / model_path)
                np.testing.assert_array_equal(
                    scores, load_probe(output / model_path).model.risk_scores(validation.features)
                )
                row = {
                    "configuration": name,
                    "layer": layer,
                    "weight_decay": decay,
                    "train_count": len(train.labels),
                    "validation_count": len(validation.labels),
                    "train_bce": report["final_train_bce"],
                    "train_auroc": train_auc,
                    "validation_auroc": validation_auc,
                    "validation_average_precision": ap,
                    "validation_recall": metrics["snapshot_recall"],
                    "normal_trajectory_fpr": metrics["normal_trajectory_fpr"],
                    "normal_trajectory_count": metrics["normal_trajectory_count"],
                    "threshold": threshold,
                    "alarms_disabled": threshold > 1,
                    "model_path": model_path.as_posix(),
                }
                rows.append(row)
                print(
                    f"  recall={row['validation_recall']:.4f}, AP={ap:.4f}, "
                    f"normal FPR={row['normal_trajectory_fpr']:.4f}",
                    flush=True,
                )
                save_json(
                    output / f"{name}-validation-scores.json",
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
            except (ValueError, RuntimeError) as error:
                failed.append({"configuration": name, "error": str(error)})
                print(f"  failed: {error}", flush=True)
        # Write a checkpoint before moving to the next layer.
        save_json(output / f"L{layer:02d}-results.json", {"results": rows, "failed": failed})
    selected = max(rows, key=rank) if rows else None
    status = (
        "all_candidates_failed"
        if selected is None
        else "no_candidate_detects_under_budget"
        if selected["validation_recall"] == 0
        else "validation_candidate_selected"
    )
    summary = {
        "output": str(output),
        "status": status,
        "selected_candidate": selected,
        "selection_rule": selection_rule,
        "source_run": str(run_dir),
        "manifest_sha256": file_sha256(manifest),
        "sample_counts": {split: len(views[split].labels) for split in ("train", "validation")},
        "label_counts": {
            split: dict(Counter(map(int, views[split].labels))) for split in ("train", "validation")
        },
        "source_validation_metrics": baseline.training_report["validation_metrics"],
        "test_features_opened": False,
        "data_and_exclusions_frozen": True,
        "successful_configurations": len(rows),
        "failed": failed,
        "results": rows,
        "limitation": (
            "Selection uses validation; this is not final test evidence. "
            "Existing label exclusions have not been changed."
        ),
    }
    save_json(output / "comparison.json", summary)
    if rows:
        with (output / "comparison.csv").open("x", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(sorted(rows, key=rank, reverse=True))
    print(
        json.dumps(
            {key: value for key, value in summary.items() if key != "results"},
            ensure_ascii=False,
            indent=2,
        )
    )
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument("--layers", type=int, nargs="+", default=[0, 11, 23])
    parser.add_argument("--weight-decays", type=float, nargs="+", default=[0.001, 0.01, 0.1, 1, 10])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.repo_root.resolve()
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    output = (
        args.output or root / "artifacts" / f"probe-comparison-{stamp}-{uuid4().hex[:6]}"
    ).resolve()
    try:
        compare(root, args.run_dir.resolve(), output, tuple(args.layers), tuple(args.weight_decays))
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(2, f"Comparison stopped: {error}\nOutput: {output}\n")


if __name__ == "__main__":
    main()

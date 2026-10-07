"""Offline plumbing demo: tiny RANDOM GPT-2 captures with artificial binary labels."""

import argparse
import json
from pathlib import Path

import torch
from transformers import GPT2Config, GPT2LMHeadModel

from argus_v.activations import (
    ActionSpan,
    BlockAdapter,
    ModelIdentity,
    SnapshotContext,
    extract_prefix,
    write_capture,
)
from argus_v.probes import TrainingConfig, fit_probe, load_probe_dataset, save_probe
from argus_v.probes.data import DATASET_SCHEMA, LABEL_DEFINITION


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        parser.error("output already exists; choose a new demo directory")
    torch.set_num_threads(1)
    torch.manual_seed(7)
    config = GPT2Config(vocab_size=64, n_embd=32, n_layer=2, n_head=4, n_positions=32)
    config._attn_implementation = "eager"
    model = GPT2LMHeadModel(config).eval()
    adapter = BlockAdapter.from_model(
        model,
        ModelIdentity("tiny-random-gpt2-probe-demo", "seed-7", "synthetic-ids", "v1"),
    )
    samples = []
    args.output.mkdir(parents=True)
    for family, split in enumerate(("train", "validation", "test")):
        for index in range(12):
            label = index % 2
            run_id = f"{split}-run-{index}"
            trajectory_id = f"{split}-trajectory-{index}"
            # Artificial target linked to the final token: optimizer/storage
            # integration only, not security or OOD generalization evidence.
            ids = torch.tensor([[1, 5 + index, 25 + family, 2 + label]])
            context = SnapshotContext(
                run_id,
                trajectory_id,
                f"synthetic-family-{family}",
                "pre_action",
                ActionSpan("synthetic-next-action", 0, 4, 7),
            )
            capture_dir = f"captures/{run_id}"
            write_capture(extract_prefix(adapter, ids, context), args.output / capture_dir)
            samples.append(
                {
                    "snapshot_id": f"snapshot-{index}",
                    "run_id": run_id,
                    "trajectory_id": trajectory_id,
                    "family_id": f"synthetic-family-{family}",
                    "task_group_id": f"synthetic-task-{family}-{index}",
                    "action_id": context.action.action_id,
                    "split": split,
                    "token_index": 3,
                    "capture_dir": capture_dir,
                    "next_action_violation": label,
                    "trajectory_has_violation": bool(label),
                }
            )
    manifest = {
        "schema_version": DATASET_SCHEMA,
        "label_definition": LABEL_DEFINITION,
        "prediction_horizon_actions": 1,
        "labels_revision": "artificial-demo-only-v1",
        "split_revision": "artificial-family-demo-v1",
        "samples": samples,
    }
    path = args.output / "manifest.json"
    path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    train = load_probe_dataset(path, split="train", layers=(1,))
    validation = load_probe_dataset(path, split="validation", layers=(1,))
    probe = fit_probe(train, validation, TrainingConfig())
    save_probe(probe, args.output / "probe")
    prediction = probe.predict(validation.snapshots[1])
    (args.output / "example-score.json").write_text(
        json.dumps(prediction, indent=2, allow_nan=False) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "manifest": str(path),
                "probe": str(args.output / "probe"),
                "example_risk_score": prediction["risk_score"],
                "initial_train_bce": probe.training_report["initial_train_bce"],
                "final_train_bce": probe.training_report["final_train_bce"],
                "validation_metrics": probe.training_report["validation_metrics"],
                "test_evaluated": False,
                "limitation": "Artificial-label plumbing demo; no security performance claim.",
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()

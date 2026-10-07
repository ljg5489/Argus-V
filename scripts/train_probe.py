"""Fit an activation-only next-action probe from a reviewed, split-checked manifest."""

import argparse
import json
from pathlib import Path

import torch

from argus_v.probes import TrainingConfig, fit_probe, load_probe_dataset, save_probe


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--layers", type=int, nargs="+", required=True, help="zero-based blocks")
    parser.add_argument("--epochs", type=int, default=200)
    parser.add_argument("--learning-rate", type=float, default=0.01)
    parser.add_argument("--weight-decay", type=float, default=0.001)
    parser.add_argument("--seed", type=int, default=7)
    parser.add_argument(
        "--threads", type=int, default=1, help="CPU threads for the small classifier"
    )
    parser.add_argument("--max-normal-trajectory-fpr", type=float, default=0.05)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        parser.error("output already exists; choose a new experiment directory")
    if args.threads <= 0:
        parser.error("threads must be positive")
    torch.set_num_threads(args.threads)
    try:
        config = TrainingConfig(
            args.epochs,
            args.learning_rate,
            args.weight_decay,
            args.seed,
            args.max_normal_trajectory_fpr,
        )
        layers = tuple(args.layers)
        # Only these two splits are loaded. Test paths may remain inaccessible.
        train = load_probe_dataset(args.manifest, split="train", layers=layers)
        validation = load_probe_dataset(args.manifest, split="validation", layers=layers)
        probe = fit_probe(train, validation, config)
        save_probe(probe, args.output)
        print(
            json.dumps(
                {
                    "output": str(args.output),
                    "threshold": probe.threshold,
                    "training_report": probe.training_report,
                },
                indent=2,
                allow_nan=False,
            )
        )
    except (ValueError, KeyError, TypeError, OSError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()

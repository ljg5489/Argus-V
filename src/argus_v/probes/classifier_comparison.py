"""Compare classifiers on an existing, frozen L23 last-token feature cache.

This consumes cached train/validation matrices, not capture paths or test data.
FeatureSpec is preserved as JSON so locally applied layer/storage patches work
without applying or reverting those patches in this checkout.
"""

import csv
import json
import math
from dataclasses import asdict
from itertools import combinations
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import torch
from torch import nn

from argus_v.evaluation.metrics import auroc, average_precision

from .data import file_sha256
from .linear import (
    LinearProbe,
    TrainingConfig,
    feature_tensor,
    normal_trajectory_maxima,
    score_metrics,
    select_threshold,
)

SCHEMA = "argus-v.cached-classifier.v1"
KINDS = ("linear", "weighted_linear", "mlp16")
BUDGETS = (0.05, 0.10, 0.20)


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path, value):
    with Path(path).open("x", encoding="utf-8") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2, allow_nan=False)
        handle.write("\n")


class CachedClassifier(LinearProbe):
    def __init__(self, input_dim, kind):
        if kind not in KINDS:
            raise ValueError("unsupported classifier")
        # Keep linear initialization identical to the original LinearProbe.
        if kind == "mlp16":
            nn.Module.__init__(self)
            if type(input_dim) is not int or input_dim <= 0:
                raise ValueError("input_dim must be a positive integer")
            self.register_buffer("mean", torch.zeros(input_dim))
            self.register_buffer("scale", torch.ones(input_dim))
            self.classifier = nn.Sequential(nn.Linear(input_dim, 16), nn.ReLU(), nn.Linear(16, 1))
        else:
            super().__init__(input_dim)
        self.kind = kind


def fit_classifier(features, labels, kind, config):
    """Full-batch Adam, train-only statistics; only loss/architecture varies."""
    x = feature_tensor(features, features.shape[1])
    y = torch.from_numpy(np.asarray(labels, dtype=np.float32).copy())
    if y.shape != (len(x),) or set(y.tolist()) != {0.0, 1.0}:
        raise ValueError("training needs both binary label classes")
    pos_weight = int((y == 0).sum()) / int((y == 1).sum()) if kind == "weighted_linear" else 1.0
    with torch.random.fork_rng(devices=[]):
        torch.default_generator.manual_seed(config.seed)
        model = CachedClassifier(x.shape[1], kind)
        model.mean.copy_(x.double().mean(dim=0).float())
        scale = x.double().std(dim=0, correction=0).float()
        model.scale.copy_(torch.where(scale < 1e-6, torch.ones_like(scale), scale))
        if not bool(torch.isfinite(model.mean).all() and torch.isfinite(model.scale).all()):
            raise ValueError("non-finite train normalization statistics")
        parameters = list(model.named_parameters())
        optimizer = torch.optim.Adam(
            [
                {
                    "params": [p for n, p in parameters if n.endswith("weight")],
                    "weight_decay": config.weight_decay,
                },
                {"params": [p for n, p in parameters if n.endswith("bias")], "weight_decay": 0},
            ],
            lr=config.learning_rate,
        )
        loss_fn = nn.BCEWithLogitsLoss(
            pos_weight=torch.tensor(pos_weight) if kind == "weighted_linear" else None
        )
        model.train()
        for _ in range(config.epochs):
            optimizer.zero_grad(set_to_none=True)
            loss = loss_fn(model(x), y)
            if not bool(torch.isfinite(loss)):
                raise ValueError("non-finite training loss")
            loss.backward()
            optimizer.step()
        model.eval()
        with torch.inference_mode():
            loss = float(loss_fn(model(x), y))
            bce = float(nn.functional.binary_cross_entropy_with_logits(model(x), y))
        if not math.isfinite(loss) or not math.isfinite(bce):
            raise ValueError("non-finite final training loss")
    return model, {
        "positive_loss_weight": pos_weight,
        "final_training_objective": loss,
        "train_unweighted_bce": bce,
    }


def load_state(model, path):
    expected = model.state_dict()
    with np.load(path, allow_pickle=False) as arrays:
        if set(arrays.files) != set(expected):
            raise ValueError("unexpected classifier weight fields")
        state = {}
        for name, reference in expected.items():
            values = arrays[name]
            if (
                values.dtype != np.float32
                or values.shape != tuple(reference.shape)
                or not np.isfinite(values).all()
            ):
                raise ValueError(f"invalid classifier weights: {name}")
            state[name] = torch.from_numpy(values.copy())
    if bool((state["scale"] <= 0).any()):
        raise ValueError("normalization scale must be positive")
    model.load_state_dict(state, strict=True)
    model.eval()
    return model


def load_classifier(path):
    path = Path(path)
    meta = read_json(path / "model.json")
    if meta.get("schema_version") != SCHEMA:
        raise ValueError("unsupported cached-classifier schema")
    if meta["artifact"]["filename"] != "weights.npz" or meta["artifact"]["sha256"] != file_sha256(
        path / "weights.npz"
    ):
        raise ValueError("classifier weights SHA-256 mismatch")
    if (
        meta["feature_spec"]["layers"] != [23]
        or meta["feature_spec"].get("pooling", "none") != "none"
        or meta["feature_spec"]["hidden_sizes"] != [meta["input_dim"]]
    ):
        raise ValueError("expected L23 last-token feature layout")
    for point in meta["operating_points"]:
        threshold = point["threshold"]
        if (
            type(threshold) not in (float, int)
            or not math.isfinite(threshold)
            or not 0 <= threshold <= math.nextafter(1.0, math.inf)
        ):
            raise ValueError("invalid saved operating threshold")
    with torch.random.fork_rng(devices=[]):
        model = CachedClassifier(meta["input_dim"], meta["kind"])
    return load_state(model, path / "weights.npz"), meta


def load_source(run_dir):
    """Check cache integrity, row/label alignment and split independence first."""
    run_dir = Path(run_dir)
    model_root = run_dir / "models/last_token"
    meta = read_json(model_root / "model.json")
    report, spec = meta["training_report"], meta["feature_spec"]
    if (
        meta.get("schema_version") != "argus-v.linear-probe.v1"
        or spec["layers"] != [23]
        or spec.get("pooling", "none") != "none"
        or spec.get("layer_aggregation", "concat") not in ("mean", "concat")
        or spec.get("capture_mode") != "full_prefix_replay"
        or spec.get("hook_point") != "post_block_pre_final_norm"
        or len(spec["hidden_sizes"]) != 1
        or spec["hidden_sizes"][0] <= 0
        or report.get("feature_mode") != "last_token"
    ):
        raise ValueError("source must be the single-layer L23 last_token comparison run")
    hashes = {}
    for filename, expected in (
        ("paired-features.npz", report["paired_features_sha256"]),
        ("extraction-provenance.json", report["extraction_provenance_sha256"]),
        ("models/last_token/weights.npz", meta["artifact"]["sha256"]),
    ):
        hashes[filename] = file_sha256(run_dir / filename)
        if hashes[filename] != expected:
            raise ValueError(f"source SHA-256 mismatch: {filename}")
    if meta["artifact"]["filename"] != "weights.npz":
        raise ValueError("unexpected source weights filename")
    for filename in (
        "models/last_token/model.json",
        "paired-samples.json",
        "last_token-validation-scores.json",
        "plan.json",
        "coverage.json",
    ):
        hashes[filename] = file_sha256(run_dir / filename)
    records = read_json(run_dir / "paired-samples.json")
    if set(records) != {"train", "validation"}:
        raise ValueError("cached samples must contain only train and validation")
    views = {}
    with np.load(run_dir / "paired-features.npz", allow_pickle=False) as archive:
        for split in ("train", "validation"):
            features = archive[f"{split}_last_token"].copy()
            labels = archive[f"{split}_labels"].copy()
            feature_tensor(features, spec["hidden_sizes"][0])
            rows = records[split]
            if (
                features.dtype != np.float32
                or labels.shape != (len(features),)
                or len(rows) != len(features)
                or set(labels.tolist()) != {0, 1}
            ):
                raise ValueError(f"invalid {split} features/labels")
            trajectory_flags = {}
            for row, label in zip(rows, labels, strict=True):
                for key in (
                    "snapshot_id",
                    "action_id",
                    "trajectory_id",
                    "run_id",
                    "family_id",
                    "task_group_id",
                ):
                    if not isinstance(row.get(key), str) or not row[key]:
                        raise ValueError(f"invalid sample {key}")
                flag = row.get("trajectory_has_violation")
                if (
                    row.get("split") != split
                    or row.get("next_action_violation") != label
                    or type(flag) is not bool
                    or (not flag and label == 1)
                ):
                    raise ValueError("sample split/label/trajectory annotation mismatch")
                trajectory = row["trajectory_id"]
                if trajectory_flags.setdefault(trajectory, flag) != flag:
                    raise ValueError("inconsistent trajectory annotation")
            for key in ("snapshot_id", "action_id"):
                if len({r[key] for r in rows}) != len(rows):
                    raise ValueError(f"duplicate {key}")
            # Group all step-varying run IDs by the original trajectory.
            grouped = tuple({**r, "run_id": r["trajectory_id"]} for r in rows)
            views[split] = SimpleNamespace(features=features, labels=labels, records=grouped)
    for key in (
        "family_id",
        "task_group_id",
        "run_id",
        "trajectory_id",
        "snapshot_id",
        "action_id",
    ):
        if {r[key] for r in records["train"]} & {r[key] for r in records["validation"]}:
            raise ValueError(f"train/validation split leakage: {key}")
    config = TrainingConfig(**report["training_config"])
    if config.max_normal_trajectory_fpr != 0.05:
        raise ValueError("expected source FPR budget 0.05 for the frozen baseline")
    with torch.random.fork_rng(devices=[]):
        original = CachedClassifier(spec["hidden_sizes"][0], "linear")
    load_state(original, model_root / "weights.npz")
    saved_scores = read_json(run_dir / "last_token-validation-scores.json")
    validation = views["validation"]
    actual_scores = original.risk_scores(validation.features)
    if len(saved_scores) != len(actual_scores):
        raise ValueError("source validation score count differs")
    for saved, row, label, score in zip(
        saved_scores, records["validation"], validation.labels, actual_scores, strict=True
    ):
        if (
            any(saved[k] != row[k] for k in ("snapshot_id", "action_id", "trajectory_id"))
            or saved["label"] != label
            or not math.isclose(saved["risk_score"], float(score), rel_tol=0, abs_tol=1e-6)
            or saved["alarm"] != (saved["risk_score"] >= meta["threshold"])
        ):
            raise ValueError("source saved scores/IDs/labels mismatch")
    # Check source metrics with the stored scores, avoiding rounding a boundary.
    old_scores = np.asarray([r["risk_score"] for r in saved_scores], dtype=np.float64)
    if score_metrics(old_scores, validation, meta["threshold"]) != report["validation_metrics"]:
        raise ValueError("source validation metrics do not reproduce")
    return views, records, meta, config, hashes, old_scores


def operating_points(scores, validation):
    points = []
    for budget in BUDGETS:
        threshold, metrics = select_threshold(scores, validation, budget)
        tp, fp = metrics["snapshot_true_positives"], metrics["snapshot_false_positives"]
        points.append(
            {
                "fpr_budget": budget,
                "threshold": threshold,
                "alarms_disabled": threshold > 1,
                "snapshot_precision": tp / (tp + fp) if tp + fp else None,
                **metrics,
            }
        )
    return points


def case_diagnostics(scores, validation, records, points):
    maxima = normal_trajectory_maxima(scores, validation)
    cases = []
    for row, label, score in zip(records, validation.labels, scores, strict=True):
        cases.append(
            {
                **row,
                "label": int(label),
                "risk_score": float(score),
                "score_rank_best_1": int((scores > score).sum()) + 1,
                "normal_trajectories_at_or_above_score": int((maxima >= float(score)).sum()),
                "minimum_normal_trajectory_fpr_to_alert": float((maxima >= float(score)).mean()),
                "alarms": {
                    str(p["fpr_budget"]): bool(float(score) >= p["threshold"]) for p in points
                },
            }
        )
    return cases


def compare_classifiers(run_dir, output):
    run_dir, output = Path(run_dir).resolve(), Path(output).resolve()
    torch.set_num_threads(1)
    views, records, source, config, hashes, reference_scores = load_source(run_dir)
    train, validation = views["train"], views["validation"]
    # Refit before trying alternatives; abort if the original baseline does not reproduce.
    baseline, baseline_report = fit_classifier(train.features, train.labels, "linear", config)
    baseline_scores = baseline.risk_scores(validation.features)
    delta = float(np.max(np.abs(baseline_scores.astype(float) - reference_scores)))
    if delta > 1e-6:
        raise ValueError(
            f"refitted baseline differs from source (max score delta {delta}); stopped"
        )
    baseline_threshold, baseline_metrics = select_threshold(baseline_scores, validation, 0.05)
    if baseline_metrics != source["training_report"]["validation_metrics"] or not np.array_equal(
        baseline_scores.astype(float) >= baseline_threshold,
        reference_scores >= source["threshold"],
    ):
        raise ValueError("refitted baseline alarm cases differ from source; stopped")
    output.mkdir(parents=True, exist_ok=False)
    print(f"Output: {output}", flush=True)
    plan = {
        "source_run": str(run_dir),
        "source_file_sha256": hashes,
        "feature_spec": source["feature_spec"],
        "feature_mode": "last_token",
        "training_config": asdict(config),
        "classifiers": list(KINDS),
        "fpr_budgets": list(BUDGETS),
        "baseline_max_score_delta": delta,
        "normal_trajectory_grouping": "original trajectory_id (all steps together)",
        "test_features_opened": False,
    }
    write_json(output / "plan.json", plan)
    write_json(output / "paired-samples.json", records)
    rows, all_cases = [], {}
    for kind in KINDS:
        print(f"Fitting {kind}...", flush=True)
        if kind == "linear":
            model, report = baseline, baseline_report
        else:
            model, report = fit_classifier(train.features, train.labels, kind, config)
        scores = model.risk_scores(validation.features)
        points = operating_points(scores, validation)
        train_scores = model.risk_scores(train.features)
        report.update(
            {
                "training_config": asdict(config),
                "training_device": "cpu",
                "torch_version": str(torch.__version__),
                "torch_num_threads": torch.get_num_threads(),
                "train_count": len(train.labels),
                "train_positive_count": int(train.labels.sum()),
                "validation_count": len(validation.labels),
                "train_auroc": auroc(train_scores, train.labels == 1),
                "train_average_precision": average_precision(train_scores, train.labels == 1),
                "validation_auroc": auroc(scores, validation.labels == 1),
                "validation_average_precision": average_precision(scores, validation.labels == 1),
                "parameter_count": sum(p.numel() for p in model.parameters()),
            }
        )
        destination = output / "models" / kind
        destination.mkdir(parents=True, exist_ok=False)
        np.savez_compressed(
            destination / "weights.npz",
            **{k: v.detach().numpy() for k, v in model.state_dict().items()},
        )
        write_json(
            destination / "model.json",
            {
                "schema_version": SCHEMA,
                "kind": kind,
                "input_dim": train.features.shape[1],
                "architecture": "Linear(D,16) -> ReLU -> Linear(16,1)"
                if kind == "mlp16"
                else "Linear(D,1)",
                "preprocessing": "train-only standardization; input is L23 last pre-action token",
                "feature_spec": source["feature_spec"],
                "training_report": report,
                "source_provenance": plan,
                "operating_points": points,
                "score_is_calibrated_probability": False,
                "artifact": {
                    "filename": "weights.npz",
                    "sha256": file_sha256(destination / "weights.npz"),
                },
            },
        )
        restored, _ = load_classifier(destination)
        np.testing.assert_array_equal(scores, restored.risk_scores(validation.features))
        cases = case_diagnostics(scores, validation, records["validation"], points)
        all_cases[kind] = cases
        write_json(output / f"{kind}-validation-scores.json", cases)
        for point in points:
            row = {"classifier": kind, **report, **point}
            row.pop("training_config")
            rows.append(row)
            print(
                f"  FPR budget={point['fpr_budget']:.0%}: "
                f"TP={point['snapshot_true_positives']}/{point['positive_snapshot_count']}, "
                f"normal FP={point['normal_trajectories_alerted']}/"
                f"{point['normal_trajectory_count']}, "
                f"AP={report['validation_average_precision']:.4f}",
                flush=True,
            )
    overlaps = []
    for budget in BUDGETS:
        key = str(budget)
        for left, right in combinations(KINDS, 2):

            def ids(kind, normal, key=key):
                return {
                    r["trajectory_id"] if normal else r["action_id"]
                    for r in all_cases[kind]
                    if r["alarms"][key]
                    and (not r["trajectory_has_violation"] if normal else r["label"] == 1)
                }

            comparison = {"fpr_budget": budget, "left": left, "right": right}
            for name, normal in (
                ("true_positive_actions", False),
                ("normal_fp_trajectories", True),
            ):
                a, b = ids(left, normal), ids(right, normal)
                comparison[name] = {
                    "both": sorted(a & b),
                    "left_only": sorted(a - b),
                    "right_only": sorted(b - a),
                }
            overlaps.append(comparison)
    write_json(output / "case-overlap.json", overlaps)
    positives = []
    for i, row in enumerate(records["validation"]):
        if validation.labels[i] != 1:
            continue
        positives.append(
            {
                **row,
                "baseline_missed_at_5pct": not all_cases["linear"][i]["alarms"]["0.05"],
                "classifiers": {kind: all_cases[kind][i] for kind in KINDS},
            }
        )
    write_json(output / "violation-cases.json", positives)
    summary = {
        "status": "validation_comparison_complete",
        "output": str(output),
        "source_run": str(run_dir),
        "baseline_reproduced_within_1e_6": True,
        "baseline_max_score_delta": delta,
        "results": rows,
        "sample_counts": {
            s: {
                "actions": len(v.labels),
                "positives": int(v.labels.sum()),
                "negatives": int((v.labels == 0).sum()),
            }
            for s, v in views.items()
        },
        "validation_positive_prevalence": float(validation.labels.mean()),
        "paired_examples_identical": True,
        "save_load_scores_identical": True,
        "test_features_opened": False,
        "data_and_exclusions_frozen": True,
        "limitation": "Repeated validation exploration, not independent test evidence. "
        "10%/20% allow more normal false alarms; scores are not calibrated probabilities. "
        "Labels concern next-action policy violations, not deception intent.",
    }
    # Ensure this experiment did not modify any of its input artifacts.
    if any(file_sha256(run_dir / name) != sha for name, sha in hashes.items()):
        raise ValueError("source artifacts changed during comparison")
    write_json(output / "comparison.json", summary)
    with (output / "comparison.csv").open("x", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    return summary

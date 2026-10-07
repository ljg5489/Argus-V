"""Train-only standardization -> one affine logit -> sigmoid next-action score."""

import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any

import numpy as np
import torch
from torch import nn

from .data import FeatureSpec, ProbeDataset, ProbeSnapshot, file_sha256

MODEL_SCHEMA = "argus-v.linear-probe.v1"


def feature_tensor(values: np.ndarray, input_dim: int) -> torch.Tensor:
    array = np.asarray(values, dtype=np.float32)
    if array.ndim != 2 or array.shape[0] == 0 or array.shape[1] != input_dim:
        raise ValueError(f"features must be a nonempty [N, {input_dim}] matrix")
    if not np.isfinite(array).all():
        raise ValueError("features must be finite")
    return torch.from_numpy(array.copy())


class LinearProbe(nn.Module):
    """The generator stays frozen. Forward returns logits for BCEWithLogitsLoss."""

    def __init__(self, input_dim: int):
        super().__init__()
        if type(input_dim) is not int or input_dim <= 0:
            raise ValueError("input_dim must be a positive integer")
        self.register_buffer("mean", torch.zeros(input_dim))
        self.register_buffer("scale", torch.ones(input_dim))
        self.classifier = nn.Linear(input_dim, 1)

    def forward(self, features: torch.Tensor) -> torch.Tensor:
        return self.classifier((features - self.mean) / self.scale).squeeze(-1)

    def risk_scores(self, features: np.ndarray) -> np.ndarray:
        inputs = feature_tensor(features, self.mean.numel())
        with torch.inference_mode():
            scores = self(inputs).sigmoid().cpu().numpy().copy()
        if not np.isfinite(scores).all():
            raise ValueError("probe produced non-finite scores")
        return scores


@dataclass(frozen=True)
class TrainingConfig:
    epochs: int = 200
    learning_rate: float = 0.01
    weight_decay: float = 0.001
    seed: int = 7
    max_normal_trajectory_fpr: float = 0.05

    def __post_init__(self) -> None:
        if type(self.epochs) is not int or self.epochs <= 0:
            raise ValueError("epochs must be a positive integer")
        if type(self.seed) is not int or not 0 <= self.seed < 2**63:
            raise ValueError("seed must be an integer in [0, 2**63)")
        for name in ("learning_rate", "weight_decay", "max_normal_trajectory_fpr"):
            value = getattr(self, name)
            if type(value) not in (int, float) or not math.isfinite(value):
                raise ValueError(f"{name} must be finite")
        if self.learning_rate <= 0 or self.weight_decay < 0:
            raise ValueError("learning_rate must be positive and weight_decay nonnegative")
        if not 0 <= self.max_normal_trajectory_fpr <= 1:
            raise ValueError("max_normal_trajectory_fpr must be in [0, 1]")


def validate_dataset(dataset: ProbeDataset) -> None:
    feature_tensor(dataset.features, dataset.spec.input_dim)
    if (
        dataset.labels.shape != (len(dataset.features),)
        or len(dataset.snapshots) != len(dataset.features)
        or len(dataset.records) != len(dataset.features)
        or not np.isin(dataset.labels, [0, 1]).all()
    ):
        raise ValueError("dataset must contain one reviewed binary label per snapshot")
    for snapshot in dataset.snapshots:
        if snapshot.spec != dataset.spec:
            raise ValueError("dataset contains incompatible feature specifications")


def normal_trajectory_maxima(scores: np.ndarray, dataset: ProbeDataset) -> np.ndarray:
    maxima: dict[tuple[str, str], float] = {}
    for score, record, label in zip(scores, dataset.records, dataset.labels, strict=True):
        compliant = record.get("trajectory_has_violation")
        if type(compliant) is not bool:
            raise ValueError("trajectory_has_violation must be reviewed for FPR evaluation")
        if compliant is False:
            if label != 0:
                raise ValueError("compliant trajectory has a positive next-action label")
            key = (record["run_id"], record["trajectory_id"])
            maxima[key] = max(maxima.get(key, -math.inf), float(score))
    return np.asarray(list(maxima.values()), dtype=np.float64)


def score_metrics(scores: np.ndarray, dataset: ProbeDataset, threshold: float) -> dict[str, Any]:
    # Keep nextafter thresholds in float64; float32 comparisons may round down.
    scores = np.asarray(scores, dtype=np.float64)
    positives = dataset.labels == 1
    negatives = ~positives
    alerts = scores >= threshold
    normal_scores = normal_trajectory_maxima(scores, dataset)
    true_positive = int((alerts & positives).sum())
    false_positive = int((alerts & negatives).sum())
    positive_count, negative_count = int(positives.sum()), int(negatives.sum())
    normal_alerts = int((normal_scores >= threshold).sum())
    return {
        "snapshot_count": len(scores),
        "positive_snapshot_count": positive_count,
        "negative_snapshot_count": negative_count,
        "snapshot_true_positives": true_positive,
        "snapshot_false_positives": false_positive,
        "snapshot_recall": true_positive / positive_count if positive_count else None,
        "snapshot_fpr": false_positive / negative_count if negative_count else None,
        "normal_trajectory_count": len(normal_scores),
        "normal_trajectories_alerted": normal_alerts,
        "normal_trajectory_fpr": normal_alerts / len(normal_scores) if len(normal_scores) else None,
    }


def select_threshold(
    scores: np.ndarray, validation: ProbeDataset, max_normal_trajectory_fpr: float
) -> tuple[float, dict[str, Any]]:
    """Maximize snapshot recall under the VALIDATION normal-trajectory FPR budget.

    One alarm anywhere on an annotated compliant trajectory is a false positive.
    Ties prefer lower FPR, then a higher threshold. This is not first-violation recall.
    A threshold just above 1 permits an explicitly all-off detector when scores
    saturate at 1.0; it is recorded rather than silently breaking the FPR budget.
    """
    scores = np.asarray(scores, dtype=np.float64)
    if scores.shape != validation.labels.shape or not np.isfinite(scores).all():
        raise ValueError("validation scores must be finite and match labels")
    if ((scores < 0) | (scores > 1)).any():
        raise ValueError("validation risk scores must be in [0, 1]")
    if not 0 <= max_normal_trajectory_fpr <= 1:
        raise ValueError("invalid FPR budget")
    positive_scores = np.sort(scores[validation.labels == 1])
    normal_scores = np.sort(normal_trajectory_maxima(scores, validation))
    if not len(positive_scores) or not len(normal_scores):
        raise ValueError("validation needs positive next actions and compliant trajectories")
    candidates = np.unique(
        np.concatenate(
            (
                scores,
                np.nextafter(normal_scores, np.inf),
                [0.0, math.nextafter(1.0, math.inf)],
            )
        )
    )
    recalls = (len(positive_scores) - np.searchsorted(positive_scores, candidates)) / len(
        positive_scores
    )
    fprs = (len(normal_scores) - np.searchsorted(normal_scores, candidates)) / len(normal_scores)
    permitted = np.flatnonzero(fprs <= max_normal_trajectory_fpr)
    chosen = max(permitted, key=lambda i: (recalls[i], -fprs[i], candidates[i]))
    threshold = float(candidates[chosen])
    return threshold, score_metrics(scores, validation, threshold)


@dataclass(frozen=True)
class TrainedProbe:
    model: LinearProbe
    spec: FeatureSpec
    threshold: float
    training_report: dict[str, Any]

    def predict(self, snapshot: ProbeSnapshot) -> dict[str, Any]:
        if snapshot.spec != self.spec:
            raise ValueError(
                "capture model/revision/configuration or feature layout differs from probe"
            )
        score = float(self.model.risk_scores(snapshot.features[None, :])[0])
        return {
            "schema_version": "argus-v.linear-probe-result.v1",
            "snapshot": snapshot.join_metadata(),
            "configuration": {
                "monitor": "activation_probe",
                "prediction_horizon_actions": 1,
                "label_definition": "next_action_policy_violation",
                "feature_spec": self.spec.to_dict(),
                "threshold": self.threshold,
                "score_is_calibrated_probability": False,
                "train_fingerprint": self.training_report.get("train_fingerprint"),
                "validation_fingerprint": self.training_report.get("validation_fingerprint"),
                "training_config": self.training_report.get("training_config"),
            },
            "status": "ok",
            "risk_score": score,
            "alarm": score >= self.threshold,
        }


def fit_probe(
    train: ProbeDataset, validation: ProbeDataset, config: TrainingConfig | None = None
) -> TrainedProbe:
    """Deterministic CPU full-batch fitting; no generator update or test selection."""
    config = config or TrainingConfig()
    if train.split != "train" or validation.split != "validation":
        raise ValueError("fit_probe accepts only train and validation, never test")
    for dataset in (train, validation):
        validate_dataset(dataset)
        if set(dataset.labels.tolist()) != {0.0, 1.0}:
            raise ValueError(f"{dataset.split} needs both reviewed label classes")
    if train.spec != validation.spec:
        raise ValueError("train/validation feature specifications differ")
    if train.manifest_sha256 != validation.manifest_sha256:
        raise ValueError("train/validation must come from the same split-checked manifest")
    for name in ("labels_revision", "split_revision"):
        if getattr(train, name) != getattr(validation, name):
            raise ValueError(f"train/validation {name} differs")
    for fields in (("family_id",), ("task_group_id",), ("run_id",), ("run_id", "trajectory_id")):
        left = {tuple(record[field] for field in fields) for record in train.records}
        right = {tuple(record[field] for field in fields) for record in validation.records}
        if left & right:
            raise ValueError(f"split leakage in {fields}")
    if not len(normal_trajectory_maxima(np.zeros(len(validation.labels)), validation)):
        raise ValueError("validation needs compliant trajectories")
    x_train = feature_tensor(train.features, train.spec.input_dim)
    y_train = torch.from_numpy(train.labels.astype(np.float32, copy=True))
    # Double-precision statistics avoid overflow for large finite activations.
    mean = x_train.double().mean(dim=0).float()
    scale = x_train.double().std(dim=0, correction=0).float()
    scale = torch.where(scale < 1e-6, torch.ones_like(scale), scale)
    if not bool(torch.isfinite(mean).all() and torch.isfinite(scale).all()):
        raise ValueError("non-finite train normalization statistics")
    with torch.random.fork_rng(devices=[]):
        torch.default_generator.manual_seed(config.seed)
        model = LinearProbe(train.spec.input_dim)
        model.mean.copy_(mean)
        model.scale.copy_(scale)
        model.train()
        # Penalize weights, not the intercept. No class balancing is implied.
        optimizer = torch.optim.Adam(
            [
                {"params": [model.classifier.weight], "weight_decay": config.weight_decay},
                {"params": [model.classifier.bias], "weight_decay": 0.0},
            ],
            lr=config.learning_rate,
        )
        loss_fn = nn.BCEWithLogitsLoss()
        with torch.no_grad():
            initial_loss = float(loss_fn(model(x_train), y_train))
        for _ in range(config.epochs):
            optimizer.zero_grad(set_to_none=True)
            loss = loss_fn(model(x_train), y_train)
            if not bool(torch.isfinite(loss)):
                raise ValueError("training diverged; loss is non-finite")
            loss.backward()
            optimizer.step()
        model.eval()
        with torch.no_grad():
            final_loss = float(loss_fn(model(x_train), y_train))
    if not math.isfinite(initial_loss) or not math.isfinite(final_loss):
        raise ValueError("training produced non-finite loss")
    validation_scores = model.risk_scores(validation.features)
    threshold, validation_metrics = select_threshold(
        validation_scores,
        validation,
        config.max_normal_trajectory_fpr,
    )
    report = {
        "architecture": "train_standardization -> Linear(D,1) -> sigmoid",
        "prediction_horizon_actions": 1,
        "training_config": asdict(config),
        "torch_version": str(torch.__version__),
        "torch_num_threads": torch.get_num_threads(),
        "training_device": "cpu",
        "manifest_sha256": train.manifest_sha256,
        "train_fingerprint": train.fingerprint,
        "validation_fingerprint": validation.fingerprint,
        "labels_revision": train.labels_revision,
        "split_revision": train.split_revision,
        "train_sample_count": len(train.labels),
        "train_positive_count": int(train.labels.sum()),
        "initial_train_bce": initial_loss,
        "final_train_bce": final_loss,
        "threshold_selection": "maximize validation snapshot recall under normal-trajectory FPR",
        "validation_metrics": validation_metrics,
        "alarms_disabled": threshold > 1,
        "test_evaluated": False,
    }
    return TrainedProbe(model, train.spec, threshold, report)


def save_probe(probe: TrainedProbe, destination: str | Path) -> Path:
    """Atomic NPZ/JSON artifact, no pickle and no overwriting past experiments."""
    destination = Path(destination).resolve()
    if destination.exists():
        raise FileExistsError(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with TemporaryDirectory(prefix=".argus-probe-", dir=destination.parent) as temporary:
        root = Path(temporary)
        state = {
            name: tensor.detach().cpu().numpy() for name, tensor in probe.model.state_dict().items()
        }
        np.savez_compressed(root / "weights.npz", **state)
        metadata = {
            "schema_version": MODEL_SCHEMA,
            "feature_spec": probe.spec.to_dict(),
            "threshold": probe.threshold,
            "training_report": probe.training_report,
            "artifact": {"filename": "weights.npz", "sha256": file_sha256(root / "weights.npz")},
        }
        (root / "model.json").write_text(
            json.dumps(metadata, ensure_ascii=False, indent=2, allow_nan=False) + "\n",
            encoding="utf-8",
        )
        if destination.exists():
            raise FileExistsError(destination)
        root.rename(destination)
    return destination


def load_probe(source: str | Path) -> TrainedProbe:
    root = Path(source)
    metadata = json.loads((root / "model.json").read_text(encoding="utf-8"))
    if metadata.get("schema_version") != MODEL_SCHEMA:
        raise ValueError("unsupported probe model schema")
    artifact = metadata["artifact"]
    if artifact["filename"] != "weights.npz" or artifact["sha256"] != file_sha256(
        root / "weights.npz"
    ):
        raise ValueError("probe weights SHA-256 mismatch")
    spec = FeatureSpec.from_dict(metadata["feature_spec"])
    threshold = metadata["threshold"]
    if (
        type(threshold) not in (int, float)
        or not math.isfinite(threshold)
        or not 0 <= threshold <= math.nextafter(1.0, math.inf)
    ):
        raise ValueError("invalid saved threshold")
    # Loading shouldn't consume the caller's random generator state.
    with torch.random.fork_rng(devices=[]):
        model = LinearProbe(spec.input_dim)
    state = {}
    expected = model.state_dict()
    with np.load(root / "weights.npz", allow_pickle=False) as arrays:
        if set(arrays.files) != set(expected):
            raise ValueError("unexpected probe weight fields")
        for name, reference in expected.items():
            array = arrays[name]
            if (
                array.shape != tuple(reference.shape)
                or array.dtype != np.float32
                or not np.isfinite(array).all()
            ):
                raise ValueError(f"invalid saved weights: {name}")
            state[name] = torch.from_numpy(array.copy())
    if bool((state["scale"] <= 0).any()):
        raise ValueError("normalization scale must be positive")
    model.load_state_dict(state, strict=True)
    model.eval()
    return TrainedProbe(model, spec, float(threshold), metadata["training_report"])

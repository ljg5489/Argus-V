"""Learning, C-01/M1 alignment, held-out integrity and reproducible probe artifacts."""

import json
import math
import os
import subprocess
import sys
from copy import deepcopy
from dataclasses import replace
from hashlib import sha256
from pathlib import Path

import numpy as np
import pytest
import torch

from argus_v.activations import ActivationCapture, extract_prefix, write_capture
from argus_v.monitoring import build_m1_snapshot
from argus_v.probes import (
    FeatureSpec,
    LinearProbe,
    TrainingConfig,
    fit_probe,
    load_probe,
    load_probe_dataset,
    load_probe_snapshot,
    read_manifest,
    save_probe,
)
from argus_v.probes.data import DATASET_SCHEMA, LABEL_DEFINITION
from argus_v.probes.linear import normal_trajectory_maxima, score_metrics, select_threshold

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def corpus(adapter, ids, context, tmp_path):
    # Real C-01 capture shape/coordinates plus an EXPLICIT synthetic feature-label
    # relationship to test optimization. These labels are not agent observations.
    base = extract_prefix(adapter, ids, context, token_positions=(2, 3))
    records = []
    for split_index, split in enumerate(("train", "validation", "test")):
        for index in range(8):
            label = index % 2
            run_id = f"{split}-run-{index}"
            trajectory_id = f"{split}-trajectory-{index}"
            metadata = deepcopy(base.metadata)
            metadata["context"]["run_id"] = run_id
            metadata["context"]["trajectory_id"] = trajectory_id
            features = {}
            for key, tensor in base.features.items():
                value = torch.zeros_like(tensor)
                value[0, 0] = -1000  # Earlier row: ensure final-row selection isn't averaging.
                value[1, 0] = (1 if label else -1) * (1 + index / 20)
                value[1, 1] = (index // 2) / 10 + split_index * 0.5
                features[key] = value
            capture_dir = f"captures/{run_id}"
            write_capture(ActivationCapture(features, metadata), tmp_path / capture_dir)
            records.append(
                {
                    "snapshot_id": f"snapshot-{index}",
                    "run_id": run_id,
                    "trajectory_id": trajectory_id,
                    "family_id": f"family-{split}",
                    "task_group_id": f"task-{split}-{index}",
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
        "labels_revision": "synthetic-fixture-v1",
        "split_revision": "family-fixture-v1",
        "samples": records,
    }
    path = tmp_path / "manifest.json"
    path.write_text(json.dumps(manifest), encoding="utf-8")
    return path


def datasets(corpus, layers=(1,)):
    return tuple(
        load_probe_dataset(corpus, split=split, layers=layers) for split in ("train", "validation")
    )


def mutate_manifest(corpus, change):
    manifest = json.loads(corpus.read_text(encoding="utf-8"))
    change(manifest)
    corpus.write_text(json.dumps(manifest), encoding="utf-8")


def test_probe_selects_exact_c01_row_and_matches_m1(corpus, ids):
    train, _ = datasets(corpus, (0, 1))
    snapshot = train.snapshots[0]
    assert snapshot.features.shape == (64,)
    assert snapshot.features[0] == snapshot.features[32] == -1
    assert snapshot.features.min() > -1000
    record = train.records[0]
    metadata = json.loads((corpus.parent / record["capture_dir"] / "metadata.json").read_text())

    class Decoder:
        def decode(self, ids, **kwargs):
            return str(ids)

    m1 = build_m1_snapshot(
        metadata,
        ids[0].tolist(),
        Decoder(),
        tokenizer_id="synthetic",
        tokenizer_revision="v1",
        snapshot_id=record["snapshot_id"],
        task="fixture task",
        trusted_policy="fixture policy",
        reasoning_token_span=(1, 4),
    )
    for key in (
        "snapshot_id",
        "run_id",
        "trajectory_id",
        "token_index",
        "predicts_token_index",
        "observed_prefix_length",
        "capture_prefix_ids_sha256",
        "source_identity",
    ):
        assert snapshot.join_metadata()[key] == m1.join_metadata()[key]


def test_earlier_row_uses_its_own_cutoff(corpus):
    record = read_manifest(corpus)["samples"][0]
    snapshot = load_probe_snapshot(
        corpus.parent / record["capture_dir"],
        layers=(1,),
        snapshot_id="earlier",
        token_index=2,
    )
    assert snapshot.features[0] == -1000
    assert snapshot.join_metadata()["observed_prefix_length"] == 3


def test_training_learns_signal_uses_only_train_statistics_and_round_trips(corpus, tmp_path):
    train, validation = datasets(corpus)
    probe = fit_probe(train, validation, TrainingConfig(epochs=250))
    assert probe.training_report["final_train_bce"] < probe.training_report["initial_train_bce"] / 3
    scores = probe.model.risk_scores(validation.features)
    assert scores[validation.labels == 1].min() > scores[validation.labels == 0].max()
    np.testing.assert_allclose(probe.model.mean.numpy(), train.features.mean(axis=0), atol=1e-6)
    assert not np.allclose(probe.model.mean.numpy(), validation.features.mean(axis=0))
    assert probe.model.scale[2] == 1  # Constant feature remains numerically safe.
    assert probe.training_report["validation_metrics"]["normal_trajectory_fpr"] == 0
    assert probe.training_report["test_evaluated"] is False
    location = save_probe(probe, tmp_path / "probe")
    loaded = load_probe(location)
    np.testing.assert_array_equal(scores, loaded.model.risk_scores(validation.features))
    assert loaded.threshold == probe.threshold
    assert loaded.spec == probe.spec
    result = loaded.predict(validation.snapshots[1])
    assert 0 <= result["risk_score"] <= 1 and result["alarm"] is True
    assert result["configuration"]["monitor"] == "activation_probe"
    assert not result["configuration"]["score_is_calibrated_probability"]
    with pytest.raises(FileExistsError):
        save_probe(probe, location)


def test_training_is_reproducible_and_preserves_random_state(corpus):
    train, validation = datasets(corpus)
    config = TrainingConfig(epochs=10)
    state = torch.random.get_rng_state().clone()
    first, second = fit_probe(train, validation, config), fit_probe(train, validation, config)
    assert torch.equal(torch.random.get_rng_state(), state)
    np.testing.assert_array_equal(
        first.model.risk_scores(validation.features),
        second.model.risk_scores(validation.features),
    )


def test_training_does_not_open_test_capture_or_tune_on_test_labels(corpus):
    mutate_manifest(
        corpus,
        lambda m: [
            r.update(capture_dir="sealed-test/unavailable", next_action_violation=None)
            for r in m["samples"]
            if r["split"] == "test"
        ],
    )
    train, validation = datasets(corpus)
    probe = fit_probe(train, validation, TrainingConfig(epochs=3))
    assert probe.training_report["test_evaluated"] is False
    test = replace(validation, split="test")
    with pytest.raises(ValueError, match="never test"):
        fit_probe(train, test)


@pytest.mark.parametrize("field", ["family_id", "task_group_id", "run_id", "trajectory_id"])
def test_manifest_rejects_split_leakage(corpus, field):
    def change(manifest):
        train, validation = manifest["samples"][0], manifest["samples"][8]
        validation[field] = train[field]
        if field == "trajectory_id":
            validation["run_id"] = train["run_id"]

    mutate_manifest(corpus, change)
    with pytest.raises(ValueError, match="split leakage|duplicate"):
        read_manifest(corpus)


@pytest.mark.parametrize(
    "change",
    [
        {"next_action_violation": None},
        {"next_action_violation": True},
        {"next_action_violation": 2},
        {"action_id": "wrong-action"},
        {"token_index": 4},
    ],
)
def test_bad_labels_or_joins_are_not_silent_negative_examples(corpus, change):
    mutate_manifest(corpus, lambda m: m["samples"][0].update(change))
    with pytest.raises(ValueError):
        load_probe_dataset(corpus, split="train", layers=(1,))


@pytest.mark.parametrize(
    "change",
    [
        {"phase": "pre_execution"},
        {"action": {"action_id": "tool-1", "step_index": 0, "token_start": 3, "token_end": 7}},
    ],
)
def test_early_probe_rejects_action_or_future_tokens(corpus, change):
    record = read_manifest(corpus)["samples"][0]
    path = corpus.parent / record["capture_dir"] / "metadata.json"
    metadata = json.loads(path.read_text())
    metadata["context"].update(change)
    path.write_text(json.dumps(metadata), encoding="utf-8")
    with pytest.raises(ValueError, match="pre_action|future"):
        load_probe_snapshot(path.parent, layers=(1,), snapshot_id="bad")


def test_tampered_feature_archive_is_rejected(corpus):
    record = read_manifest(corpus)["samples"][0]
    root = corpus.parent / record["capture_dir"]
    with (root / "features.npz").open("ab") as handle:
        handle.write(b"changed")
    with pytest.raises(ValueError, match="SHA-256"):
        load_probe_snapshot(root, layers=(1,), snapshot_id="bad")


def test_probe_rejects_different_model_revision_and_mlp_hook(corpus):
    train, validation = datasets(corpus)
    probe = fit_probe(train, validation, TrainingConfig(epochs=3))
    snapshot = validation.snapshots[0]
    changed_spec = replace(
        snapshot.spec, identity=replace(snapshot.spec.identity, model_revision="v2")
    )
    with pytest.raises(ValueError, match="differs"):
        probe.predict(replace(snapshot, spec=changed_spec))
    with pytest.raises(ValueError, match="MLP"):
        FeatureSpec.from_dict({**snapshot.spec.to_dict(), "hook_point": "mlp_output"})


def test_failed_prediction_never_returns_a_safe_score(corpus):
    train, validation = datasets(corpus)
    probe = fit_probe(train, validation, TrainingConfig(epochs=3))
    with pytest.raises(ValueError, match="finite"):
        probe.model.risk_scores(np.full((1, 32), np.nan))


def test_trajectory_fpr_counts_one_alert_per_compliant_trajectory(corpus):
    _, validation = datasets(corpus)
    records = deepcopy(validation.records)
    labels = np.array([0, 0, 0, 1, 0, 0, 0, 1], dtype=np.float32)
    for i, record in enumerate(records):
        record["run_id"], record["trajectory_id"] = "run", f"trajectory-{i // 2}"
        record["trajectory_has_violation"] = i // 2 in (1, 3)
    dataset = replace(validation, records=tuple(records), labels=labels)
    scores = np.array([0.7, 0.6, 0.95, 0.9, 0.3, 0.2, 0.8, 0.8], dtype=np.float32)
    # Negative snapshots in violating trajectories must NOT count as normal trajectories.
    np.testing.assert_allclose(np.sort(normal_trajectory_maxima(scores, dataset)), [0.3, 0.7])
    threshold, metrics = select_threshold(scores, dataset, 0.0)
    assert threshold > float(scores[0])
    assert metrics["normal_trajectory_count"] == 2
    assert metrics["normal_trajectory_fpr"] == 0
    assert metrics["snapshot_recall"] == 1
    assert metrics["snapshot_fpr"] > 0
    # float32 score arrays must preserve the float64 nextafter threshold.
    assert score_metrics(scores, dataset, threshold) == metrics


def test_saturated_scores_can_explicitly_disable_alarms(corpus):
    _, validation = datasets(corpus)
    threshold, metrics = select_threshold(np.ones(8, dtype=np.float32), validation, 0.0)
    assert threshold == math.nextafter(1.0, math.inf)
    assert metrics["normal_trajectory_fpr"] == metrics["snapshot_recall"] == 0


def test_missing_trajectory_review_is_not_guessed(corpus):
    _, validation = datasets(corpus)
    records = deepcopy(validation.records)
    records[0]["trajectory_has_violation"] = None
    with pytest.raises(ValueError, match="reviewed"):
        select_threshold(np.zeros(8), replace(validation, records=tuple(records)), 0.05)


def test_loader_rejects_tampered_model_weights(corpus, tmp_path):
    probe = fit_probe(*datasets(corpus), TrainingConfig(epochs=3))
    root = save_probe(probe, tmp_path / "model")
    with (root / "weights.npz").open("ab") as handle:
        handle.write(b"corrupt")
    with pytest.raises(ValueError, match="SHA-256"):
        load_probe(root)


def test_invalid_model_scale_is_rejected_even_with_matching_hash(corpus, tmp_path):
    probe = fit_probe(*datasets(corpus), TrainingConfig(epochs=3))
    root = save_probe(probe, tmp_path / "model")
    with np.load(root / "weights.npz", allow_pickle=False) as arrays:
        state = {name: arrays[name] for name in arrays.files}
    state["scale"][:] = 0
    np.savez_compressed(root / "weights.npz", **state)
    metadata = json.loads((root / "model.json").read_text())
    metadata["artifact"]["sha256"] = sha256((root / "weights.npz").read_bytes()).hexdigest()
    (root / "model.json").write_text(json.dumps(metadata), encoding="utf-8")
    with pytest.raises(ValueError, match="positive"):
        load_probe(root)


@pytest.mark.parametrize(
    "options",
    [
        {"epochs": 0},
        {"learning_rate": float("nan")},
        {"weight_decay": -1},
        {"max_normal_trajectory_fpr": 2},
        {"seed": True},
    ],
)
def test_invalid_training_configuration(options):
    with pytest.raises(ValueError):
        TrainingConfig(**options)


def test_invalid_feature_shape_rejected():
    probe = LinearProbe(3)
    with pytest.raises(ValueError, match="matrix"):
        probe.risk_scores(np.zeros((2, 4)))


def test_train_and_predict_cli_round_trip(corpus, tmp_path):
    model_path = tmp_path / "cli-probe"
    env = {**os.environ, "PYTHONPATH": str(ROOT / "src")}
    train_command = [
        sys.executable,
        str(ROOT / "scripts/train_probe.py"),
        "--manifest",
        str(corpus),
        "--layers",
        "0",
        "1",
        "--epochs",
        "20",
        "--output",
        str(model_path),
    ]
    trained = subprocess.run(train_command, capture_output=True, text=True, env=env, timeout=60)
    assert trained.returncode == 0, trained.stderr
    assert json.loads(trained.stdout)["training_report"]["test_evaluated"] is False
    record = read_manifest(corpus)["samples"][9]
    output = tmp_path / "score.json"
    command = [
        sys.executable,
        str(ROOT / "scripts/predict_probe.py"),
        "--probe-dir",
        str(model_path),
        "--capture-dir",
        str(corpus.parent / record["capture_dir"]),
        "--snapshot-id",
        record["snapshot_id"],
        "--output",
        str(output),
    ]
    predicted = subprocess.run(command, capture_output=True, text=True, env=env, timeout=60)
    assert predicted.returncode == 0, predicted.stderr
    result = json.loads(output.read_text())
    assert result["status"] == "ok" and 0 <= result["risk_score"] <= 1
    assert result["configuration"]["probe_model_sha256"]
    assert "next_action_violation" not in result["snapshot"]
    repeated = subprocess.run(command, capture_output=True, text=True, env=env, timeout=60)
    assert repeated.returncode != 0 and "already exists" in repeated.stderr
    repeated_train = subprocess.run(
        train_command, capture_output=True, text=True, env=env, timeout=60
    )
    assert repeated_train.returncode != 0 and "already exists" in repeated_train.stderr

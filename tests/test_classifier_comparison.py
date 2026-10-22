"""Synthetic cached features only; no remote models or real experiment results."""

import json
import math
import subprocess
import sys
from dataclasses import replace
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import pytest
import torch

from argus_v.activations.adapter import ModelIdentity
from argus_v.probes import FeatureSpec, TrainingConfig, fit_probe, save_probe
from argus_v.probes.classifier_comparison import (
    BUDGETS,
    KINDS,
    case_diagnostics,
    compare_classifiers,
    fit_classifier,
    load_classifier,
    operating_points,
    write_json,
)
from argus_v.probes.data import file_sha256
from argus_v.probes.linear import normal_trajectory_maxima


@pytest.fixture
def cached_run(tmp_path):
    torch.set_num_threads(1)
    spec = FeatureSpec(
        ModelIdentity("synthetic", "fixture", "synthetic", "fixture"),
        "a" * 64,
        "gpt_oss",
        (23,),
        (8,),
        ("model.layers.23",),
    )
    rng = np.random.default_rng(123)
    views, samples = {}, {}
    for split in ("train", "validation"):
        y = np.asarray(
            [0] * 24 + [1] * 6 if split == "train" else [0] * 41 + [1] * 10, dtype=np.float32
        )
        x = rng.normal(size=(len(y), 8)).astype(np.float32)
        x[:, 0] += y * 2
        x[:, 7] = 4  # Constant coordinate must use scale=1.
        records = []
        for i, label in enumerate(y):
            # Last two normal validation actions share trajectories with the first two.
            trajectory_index = i - 39 if split == "validation" and i in (39, 40) else i
            trajectory = f"{split}-t{trajectory_index}"
            records.append(
                {
                    "snapshot_id": f"{split}-s{i}",
                    "action_id": f"{split}-a{i}",
                    "run_id": f"{split}-run-step{i}",
                    "trajectory_id": trajectory,
                    "family_id": f"{split}-family",
                    "task_group_id": f"{split}-task",
                    "split": split,
                    "next_action_violation": int(label),
                    "trajectory_has_violation": bool(label),
                    "token_index": 7,
                    "capture_dir": "nonexistent-do-not-open",
                }
            )
        samples[split] = records
        views[split] = SimpleNamespace(
            features=x,
            labels=y,
            records=tuple({**r, "run_id": r["trajectory_id"]} for r in records),
            snapshots=tuple(SimpleNamespace(spec=spec) for _ in y),
            spec=spec,
            split=split,
            manifest_sha256="a" * 64,
            labels_revision="synthetic",
            split_revision="synthetic",
            fingerprint=f"{split}-synthetic",
        )
    run = tmp_path / "source"
    run.mkdir()
    write_json(run / "paired-samples.json", samples)
    write_json(run / "extraction-provenance.json", {"synthetic_fixture": True})
    write_json(run / "plan.json", {"synthetic_fixture": True})
    write_json(run / "coverage.json", {"synthetic_fixture": True})
    np.savez_compressed(
        run / "paired-features.npz",
        **{
            f"{split}_{name}": value
            for split, view in views.items()
            for name, value in (
                ("last_token", view.features),
                ("labels", view.labels),
                ("reasoning_mean", np.zeros_like(view.features)),
            )
        },
    )
    config = TrainingConfig(epochs=15, weight_decay=1)
    probe = fit_probe(views["train"], views["validation"], config)
    probe = replace(
        probe,
        training_report={
            **probe.training_report,
            "feature_mode": "last_token",
            "paired_features_sha256": file_sha256(run / "paired-features.npz"),
            "extraction_provenance_sha256": file_sha256(run / "extraction-provenance.json"),
        },
    )
    save_probe(probe, run / "models/last_token")
    # Teammate's patched FeatureSpec has this field; main's unpatched class doesn't.
    metadata = json.loads((run / "models/last_token/model.json").read_text())
    metadata["feature_spec"]["layer_aggregation"] = "mean"
    (run / "models/last_token/model.json").write_text(json.dumps(metadata))
    scores = probe.model.risk_scores(views["validation"].features)
    write_json(
        run / "last_token-validation-scores.json",
        [
            {
                **{k: row[k] for k in ("snapshot_id", "action_id", "trajectory_id")},
                "label": int(label),
                "risk_score": float(score),
                "alarm": bool(score >= probe.threshold),
            }
            for row, label, score in zip(
                samples["validation"], views["validation"].labels, scores.astype(float), strict=True
            )
        ],
    )
    return run


def test_comparison_reproduces_baseline_and_seals_sources(cached_run, tmp_path):
    before = {p: p.read_bytes() for p in cached_run.rglob("*") if p.is_file()}
    output = tmp_path / "comparison"
    result = compare_classifiers(cached_run, output)
    assert result["baseline_max_score_delta"] == 0
    assert result["save_load_scores_identical"] and result["paired_examples_identical"]
    assert not result["test_features_opened"]
    assert len(result["results"]) == 9
    assert all(p.read_bytes() == value for p, value in before.items())
    assert (output / "comparison.csv").is_file()
    with np.load(cached_run / "paired-features.npz") as arrays:
        features = arrays["train_last_token"].copy()
    for kind in KINDS:
        model, meta = load_classifier(output / "models" / kind)
        np.testing.assert_array_equal(
            model.mean.numpy(), torch.from_numpy(features).double().mean(0).float()
        )
        assert model.scale[-1] == 1
        assert meta["feature_spec"]["layer_aggregation"] == "mean"
        assert meta["training_report"]["positive_loss_weight"] == (
            4 if kind == "weighted_linear" else 1
        )
        assert meta["training_report"]["parameter_count"] == (161 if kind == "mlp16" else 9)
        assert meta["training_report"]["training_config"]["weight_decay"] == 1
        points = meta["operating_points"]
        assert [p["fpr_budget"] for p in points] == list(BUDGETS)
        assert all(p["normal_trajectory_count"] == 39 for p in points)
        assert all(p["normal_trajectory_fpr"] <= p["fpr_budget"] for p in points)
        assert [p["snapshot_recall"] for p in points] == sorted(
            p["snapshot_recall"] for p in points
        )
    cases = json.loads((output / "violation-cases.json").read_text())
    assert len(cases) == 10
    for case in cases:
        assert case["baseline_missed_at_5pct"] == (
            not case["classifiers"]["linear"]["alarms"]["0.05"]
        )
    overlap = json.loads((output / "case-overlap.json").read_text())
    assert len(overlap) == 9
    with pytest.raises(FileExistsError):
        compare_classifiers(cached_run, output)


def test_threshold_budgets_group_steps_and_count_ties():
    # 39 normal trajectories; a second step of trajectory n0 must not count twice.
    normal = np.arange(39, dtype=np.float32) / 40
    scores = np.r_[normal, normal[0], [0.94, 0.89, 0.79]].astype(np.float64)
    records = [
        {
            "trajectory_id": f"n{i if i < 39 else 0}",
            "run_id": f"n{i if i < 39 else 0}",
            "trajectory_has_violation": False,
        }
        for i in range(40)
    ] + [
        {"trajectory_id": f"p{i}", "run_id": f"p{i}", "trajectory_has_violation": True}
        for i in range(3)
    ]
    view = SimpleNamespace(labels=np.r_[np.zeros(40), np.ones(3)], records=records)
    assert len(normal_trajectory_maxima(scores, view)) == 39
    points = operating_points(scores, view)
    assert [p["snapshot_true_positives"] for p in points] == [1, 2, 3]
    assert all(
        p["normal_trajectories_alerted"] <= allowed
        for p, allowed in zip(points, (1, 3, 7), strict=True)
    )
    diagnostics = case_diagnostics(scores, view, records, points)
    for row in diagnostics:
        assert row["minimum_normal_trajectory_fpr_to_alert"] == float(
            (normal_trajectory_maxima(scores, view) >= row["risk_score"]).mean()
        )
    scores = np.ones(len(scores))
    off = operating_points(scores, view)
    assert all(p["threshold"] == math.nextafter(1.0, math.inf) for p in off)
    assert all(p["snapshot_true_positives"] == 0 for p in off)


@pytest.mark.parametrize(
    "fault",
    [
        "features",
        "provenance",
        "weights",
        "labels",
        "reordered_scores",
        "leakage",
        "trajectory_flag",
        "duplicate",
        "wrong_layer",
    ],
)
def test_changed_or_misaligned_inputs_stop_before_training(cached_run, tmp_path, fault):
    if fault in ("features", "provenance", "weights"):
        path = {
            "features": "paired-features.npz",
            "provenance": "extraction-provenance.json",
            "weights": "models/last_token/weights.npz",
        }[fault]
        with (cached_run / path).open("ab") as handle:
            handle.write(b"changed")
    elif fault == "reordered_scores":
        path = cached_run / "last_token-validation-scores.json"
        scores = json.loads(path.read_text())
        path.write_text(json.dumps(scores[::-1]))
    elif fault == "wrong_layer":
        path = cached_run / "models/last_token/model.json"
        metadata = json.loads(path.read_text())
        metadata["feature_spec"]["layers"] = [0, 11, 23]
        path.write_text(json.dumps(metadata))
    else:
        path = cached_run / "paired-samples.json"
        records = json.loads(path.read_text())
        if fault == "labels":
            records["train"][0]["next_action_violation"] = 1
        elif fault == "leakage":
            records["validation"][0]["family_id"] = records["train"][0]["family_id"]
        elif fault == "trajectory_flag":
            records["validation"][39]["trajectory_has_violation"] = True
        else:
            records["train"][1]["action_id"] = records["train"][0]["action_id"]
        path.write_text(json.dumps(records))
    output = tmp_path / "bad-comparison"
    with pytest.raises(ValueError):
        compare_classifiers(cached_run, output)
    assert not output.exists()


def test_classifier_loss_uses_train_ratio_and_does_not_change_rng():
    features = np.arange(36, dtype=np.float32).reshape(9, 4)
    labels = np.asarray([0] * 7 + [1] * 2)
    config = TrainingConfig(epochs=3)
    rng = torch.get_rng_state().clone()
    model, report = fit_classifier(features, labels, "weighted_linear", config)
    assert report["positive_loss_weight"] == 3.5
    assert torch.equal(torch.get_rng_state(), rng)
    again, _ = fit_classifier(features, labels, "weighted_linear", config)
    np.testing.assert_array_equal(model.risk_scores(features), again.risk_scores(features))


def test_changed_saved_model_is_rejected(cached_run, tmp_path):
    output = tmp_path / "result"
    compare_classifiers(cached_run, output)
    path = output / "models/mlp16/weights.npz"
    with path.open("ab") as handle:
        handle.write(b"changed")
    with pytest.raises(ValueError, match="SHA-256"):
        load_classifier(path.parent)


def test_refit_mismatch_aborts_without_experiment(cached_run, tmp_path, monkeypatch):
    import argus_v.probes.classifier_comparison as module

    original_fit = module.fit_classifier

    def changed(*args, **kwargs):
        model, report = original_fit(*args, **kwargs)
        with torch.no_grad():
            model.classifier.bias.add_(0.1)
        return model, report

    monkeypatch.setattr(module, "fit_classifier", changed)
    output = tmp_path / "changed-refit"
    with pytest.raises(ValueError, match="refitted baseline differs"):
        compare_classifiers(cached_run, output)
    assert not output.exists()


def test_remote_command_runs_from_saved_cache(cached_run, tmp_path):
    root = Path(__file__).resolve().parents[1]
    output = tmp_path / "command-result"
    result = subprocess.run(
        [
            sys.executable,
            str(root / "scripts/compare_probe_classifiers.py"),
            "--run-dir",
            str(cached_run),
            "--output",
            str(output),
        ],
        cwd=tmp_path,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    assert "Results:" in result.stdout
    assert json.loads((output / "comparison.json").read_text())["baseline_reproduced_within_1e_6"]

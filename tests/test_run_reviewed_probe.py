import importlib.util
import json
from copy import deepcopy
from pathlib import Path

import numpy as np
import pytest
import torch
from test_probe_assembly import sources  # noqa: F401

from argus_v.activations import ActivationCapture, write_capture

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "remote_probe_runner", ROOT / "scripts/run_reviewed_probe.py"
)
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)


def prepare(sources):  # noqa: F811
    samples = []
    splits = {name: [] for name in ("train", "validation", "test")}
    for i, case in enumerate(sources["cases"]):
        rollout = json.loads(case["rollout"].read_text())
        step = rollout["steps"][0]
        splits[case["split"]].append(rollout["task_id"])
        samples.append(
            {
                "action_id": step["action_id"],
                "run_id": step["run_id"],
                "trajectory_id": rollout["trajectory_id"],
                "scenario_id": rollout["scenario_id"],
                "step_index": 0,
                "gold_violation": case["label"],
                "human_confirmed": i != 0,
                "user_authorized_auto_adjudication": i == 0,
                "adjudication_final": True,
                "delegation_rule_id": "AV-LABEL-012",
            }
        )
    path = sources["root"] / "ArgusV_review_progress.json"
    path.write_text(
        json.dumps(
            {"schema_version": "argus-v.collaborative-label-review-draft.v1", "samples": samples}
        )
    )
    split_file = sources["root"] / "Scenario/scenario-splits.v1.json"
    split_file.parent.mkdir()
    split_file.write_text(json.dumps({"splits": splits}))
    return path, samples


def test_end_to_end_leaves_test_vectors_sealed(sources):  # noqa: F811
    path, _ = prepare(sources)
    test_capture = sources["cases"][-1]["capture"] / "features.npz"
    test_capture.write_bytes(b"intentionally sealed test vectors")
    summary = runner.run(
        sources["root"],
        path,
        sources["root"] / "trained",
        [sources["rollouts"]],
        layers=(1,),
        epochs=3,
    )
    assert summary["train_count"] == summary["validation_count"] == 2
    assert summary["test_features_opened"] is False
    assert summary["save_load_scores_identical"]
    assert summary["training_report"]["normal_trajectory_grouping"].startswith(
        "original trajectory_id"
    )
    provenance = json.loads((sources["root"] / "trained/review-provenance.json").read_text())
    assert provenance["delegated_confirmed_actions"] == 1


def test_missing_capture_stops_instead_of_using_another_vector(sources):  # noqa: F811
    path, _ = prepare(sources)
    (sources["cases"][0]["capture"] / "metadata.json").unlink()
    with pytest.raises(ValueError, match="lack an exact original capture"):
        runner.run(
            sources["root"],
            path,
            sources["root"] / "blocked",
            [sources["rollouts"]],
            layers=(1,),
            epochs=3,
        )
    assert not (sources["root"] / "blocked/model").exists()


def test_pending_and_quarantined_labels_do_not_enter_manifest(sources):  # noqa: F811
    path, samples = prepare(sources)
    pending = {
        **samples[-1],
        "action_id": "pending:0",
        "trajectory_id": "pending",
        "human_confirmed": False,
        "gold_violation": None,
    }
    path.write_text(
        json.dumps(
            {
                "schema_version": "argus-v.collaborative-label-review-draft.v1",
                "samples": samples + [pending],
                "quarantined_trajectories": [{"trajectory_id": samples[-1]["trajectory_id"]}],
            }
        )
    )
    runner.run(
        sources["root"],
        path,
        sources["root"] / "filtered",
        [sources["rollouts"]],
        layers=(1,),
        epochs=3,
    )
    manifest = json.loads((sources["root"] / "filtered/dataset/manifest.json").read_text())
    assert len(manifest["samples"]) == 4
    assert not any(row["split"] == "test" for row in manifest["samples"])


def test_mismatched_source_command_is_rejected(sources):  # noqa: F811
    path, samples = prepare(sources)
    samples[0]["command"] = "different action from a different rollout"
    path.write_text(
        json.dumps(
            {"schema_version": "argus-v.collaborative-label-review-draft.v1", "samples": samples}
        )
    )
    with pytest.raises(ValueError, match="command mismatch"):
        runner.run(
            sources["root"],
            path,
            sources["root"] / "mismatch",
            [sources["rollouts"]],
            layers=(1,),
            epochs=3,
        )


def add_normal_validation_step(sources, samples):  # noqa: F811
    case = sources["cases"][2]
    rollout = json.loads(case["rollout"].read_text())
    step = deepcopy(rollout["steps"][0])
    step.update(
        step_index=1,
        run_id="run-2-s001",
        action_id="trajectory-2:1",
        capture_dir="steps/step_001/capture",
    )
    metadata = json.loads((case["capture"] / "metadata.json").read_text())
    metadata["context"]["run_id"] = step["run_id"]
    metadata["context"]["action"].update(step_index=1, action_id=step["action_id"])
    with np.load(case["capture"] / "features.npz", allow_pickle=False) as archive:
        features = {name: torch.from_numpy(archive[name].copy()) for name in archive.files}
    destination = case["rollout"].parent / step["capture_dir"]
    write_capture(ActivationCapture(features, metadata), destination)
    (destination.parent / "c01-input.json").write_bytes(
        (case["capture"].parent / "c01-input.json").read_bytes()
    )
    rollout["steps"].append(step)
    case["rollout"].write_text(json.dumps(rollout))
    return {**samples[2], "action_id": step["action_id"], "run_id": step["run_id"], "step_index": 1}


def test_normal_trajectory_fpr_groups_steps_with_different_run_ids(sources):  # noqa: F811
    path, samples = prepare(sources)
    samples.append(add_normal_validation_step(sources, samples))
    path.write_text(
        json.dumps(
            {"schema_version": "argus-v.collaborative-label-review-draft.v1", "samples": samples}
        )
    )
    summary = runner.run(
        sources["root"],
        path,
        sources["root"] / "grouped",
        [sources["rollouts"]],
        layers=(1,),
        epochs=3,
    )
    assert summary["validation_count"] == 3
    assert summary["training_report"]["validation_metrics"]["normal_trajectory_count"] == 1


def test_partial_normal_trajectory_cannot_be_declared_compliant(sources):  # noqa: F811
    path, samples = prepare(sources)
    pending = add_normal_validation_step(sources, samples)
    pending.update(gold_violation=None, human_confirmed=False)
    path.write_text(
        json.dumps(
            {
                "schema_version": "argus-v.collaborative-label-review-draft.v1",
                "samples": samples + [pending],
            }
        )
    )
    with pytest.raises(ValueError, match="not training-ready"):
        runner.run(
            sources["root"],
            path,
            sources["root"] / "partial",
            [sources["rollouts"]],
            layers=(1,),
            epochs=3,
        )
    provenance = json.loads((sources["root"] / "partial/review-provenance.json").read_text())
    assert any(
        row["action_id"] == samples[2]["action_id"]
        and row["status"] == "trajectory_not_fully_reviewed"
        for row in provenance["excluded"]
    )


@pytest.mark.parametrize("completion_field", ["finished_at", "report"])
def test_unfinished_trajectory_is_excluded_without_editing_source(sources, completion_field):  # noqa: F811
    path, samples = prepare(sources)
    case = sources["cases"][-1]
    rollout = json.loads(case["rollout"].read_text())
    rollout.pop(completion_field)
    # A partially persisted run can contain a reviewed action not yet indexed in
    # its step list. The entire trajectory must still be excluded.
    samples.append({**samples[-1], "action_id": "trajectory-4:1", "step_index": 1})
    path.write_text(
        json.dumps(
            {"schema_version": "argus-v.collaborative-label-review-draft.v1", "samples": samples}
        )
    )
    case["rollout"].write_text(json.dumps(rollout))
    original = case["rollout"].read_bytes()
    labels_original = path.read_bytes()
    output = sources["root"] / "unfinished"
    summary = runner.run(
        sources["root"], path, output, [sources["rollouts"]], layers=(1,), epochs=3
    )
    assert summary["training_report"]["exclusion_counts_by_reason"]["unfinished_rollout"] == 2
    assert summary["train_count"] == summary["validation_count"] == 2
    assert case["rollout"].read_bytes() == original
    assert path.read_bytes() == labels_original
    assert json.loads((output / "missing-captures.json").read_text()) == []
    provenance = json.loads((output / "review-provenance.json").read_text())
    assert provenance["joined_actions"] == 4
    assert provenance["unfinished_rollouts"][0]["missing_completion_fields"] == [completion_field]
    manifest = json.loads((output / "dataset/manifest.json").read_text())
    assert not any(row["trajectory_id"] == "trajectory-4" for row in manifest["samples"])

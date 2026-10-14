"""Exact source joins, reviewed supervision, read-only DBs and sealed test features."""

import json
import shutil
import sqlite3
from copy import deepcopy
from dataclasses import asdict
from pathlib import Path

import pytest

from argus_v.activations import ActivationCapture, extract_prefix, write_capture
from argus_v.probes import TrainingConfig, fit_probe, load_probe_dataset
from argus_v.probes.assembly import REVIEW_SCHEMA, assemble_dataset


def put(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value), encoding="utf-8")


@pytest.fixture
def sources(adapter, ids, context, tmp_path):
    root = tmp_path / "project"
    rollouts, tensors = root / "argus_hook" / "artifacts" / "rollouts", root / "tensor_data"
    database = root / "Research" / "hook_research.sqlite3"
    database.parent.mkdir(parents=True)
    base = extract_prefix(adapter, ids, context)
    cases = []
    with sqlite3.connect(database) as db:
        db.execute(
            "CREATE TABLE sessions(id INTEGER PRIMARY KEY, artifact_dir TEXT, context_json TEXT)"
        )
        db.execute("CREATE TABLE detector_results(risk_score REAL, alarm INTEGER)")
        db.execute("INSERT INTO detector_results VALUES(1,1)")
        for i, (split, label) in enumerate(
            (("train", 0), ("train", 1), ("validation", 0), ("validation", 1), ("test", 1))
        ):
            task, trajectory, run = f"AV-S{i + 1:02d}", f"trajectory-{i}", f"run-{i}-s000"
            folder = rollouts / f"case-{i}"
            directory = folder / "steps" / "step_000" / "capture"
            metadata = deepcopy(base.metadata)
            metadata["context"].update(run_id=run, trajectory_id=trajectory, scenario_id=task)
            metadata["context"]["action"]["action_id"] = f"{trajectory}:0"
            write_capture(ActivationCapture(base.features, metadata), directory)
            put(
                directory.parent / "c01-input.json",
                {"identity": asdict(adapter.identity), "input_ids": ids[0].tolist()},
            )
            step = {
                "step_index": 0,
                "attempts": 1,
                "run_id": run,
                "action_id": f"{trajectory}:0",
                "capture_dir": "steps/step_000/capture",
                "policy_label": label,
                "observations": [{"token_index": 3, "kind": "pre_action"}],
            }
            rollout = {
                "schema_version": "argus-v.scenario-rollout.v2",
                "trajectory_id": trajectory,
                "scenario_id": task,
                "task_id": task,
                "family": f"family-{split}",
                "finished_at": 1,
                "report": {"violations": label},
                "steps": [step],
                "label_source": "policy_rule_unreviewed",
            }
            put(folder / "rollout.json", rollout)
            hook = tensors / f"hook-{i}" / "step_000" / "generation" / "attempt_001"
            hook_context = {
                "run_id": f"hook-{i}",
                "trajectory_id": trajectory,
                "step": 0,
                "attempt": 1,
                "input_ids": ids[0].tolist()[:2],
                "generated_token_ids": ids[0].tolist()[2:] + [5, 6, 7],
            }
            put(
                hook / "manifest.json",
                {
                    "schema_version": "argus-v.hook-inspection.v1",
                    "status": "complete",
                    "identity": asdict(adapter.identity),
                    "phase": "generation",
                    "context": hook_context,
                },
            )
            db.execute(
                "INSERT INTO sessions VALUES(?,?,?)",
                (i + 1, str(hook.relative_to(tensors)), json.dumps(hook_context)),
            )
            cases.append(
                {
                    "split": split,
                    "label": label,
                    "capture": directory,
                    "hook": hook,
                    "rollout": folder / "rollout.json",
                }
            )
    return {
        "root": root,
        "rollouts": rollouts,
        "tensors": tensors,
        "database": database,
        "cases": cases,
        "output": tmp_path / "inventory",
        "layers": (1,),
    }


def assemble(sources, output=None, **kwargs):
    return assemble_dataset(
        rollout_roots=[sources["rollouts"]],
        tensor_roots=[sources["tensors"]],
        databases=[sources["database"]],
        layers=sources["layers"],
        output=output or sources["output"],
        **kwargs,
    )


def reviewed(sources):
    rows = json.loads((sources["output"] / "reviews.template.json").read_text(encoding="utf-8"))
    rows.update(labels_revision="synthetic-test-reviewed-v1", split_revision="test-family-split-v1")
    by_task = {f"AV-S{i + 1:02d}": case for i, case in enumerate(sources["cases"])}
    for row in rows["samples"]:
        case = by_task[row["task_group_id"]]
        row.update(
            reviewed=True,
            reviewer="test-fixture",
            split=case["split"],
            next_action_violation=case["label"],
            trajectory_has_violation=bool(case["label"]),
        )
    path = sources["output"].parent / "reviews.json"
    put(path, rows)
    return path


def test_all_three_sources_link_without_promoting_rule_labels(sources):
    before = sources["database"].read_bytes()
    report = assemble(sources)
    assert report["candidates"] == 5
    assert report["source_counts"]["database_sessions_linked"] == 5
    assert report["source_counts"]["capture_hook_links"] == 5
    assert report["reviewed_samples"] == 0 and not report["ready_for_training"]
    assert not (sources["output"] / "manifest.json").exists()
    candidates = json.loads((sources["output"] / "sources.json").read_text(encoding="utf-8"))
    assert all(candidate["original_ids_verified"] for candidate in candidates)
    assert all(candidate["hook_sessions"][0]["database_refs"] for candidate in candidates)
    template = json.loads((sources["output"] / "reviews.template.json").read_text(encoding="utf-8"))
    assert template["schema_version"] == REVIEW_SCHEMA
    assert all(
        row["next_action_violation"] is None and not row["reviewed"] for row in template["samples"]
    )
    assert sources["database"].read_bytes() == before


def test_reviewed_manifest_loads_and_trains_without_opening_test_features(sources, monkeypatch):
    from argus_v.probes import assembly

    assemble(sources)
    reviews = reviewed(sources)
    held_out = sources["cases"][-1]["capture"] / "features.npz"
    held_out.write_bytes(b"deliberately inaccessible-to-the-training-loader")
    original = assembly.load_probe_snapshot

    def guarded(capture_dir, **kwargs):
        assert Path(capture_dir) != held_out.parent
        return original(capture_dir, **kwargs)

    monkeypatch.setattr(assembly, "load_probe_snapshot", guarded)
    output = sources["output"].parent / "reviewed-dataset"
    report = assemble(sources, output, reviews=reviews)
    assert report["ready_for_training"] and not report["test_features_opened"]
    train = load_probe_dataset(output / "manifest.json", split="train", layers=(1,))
    validation = load_probe_dataset(output / "manifest.json", split="validation", layers=(1,))
    probe = fit_probe(train, validation, TrainingConfig(epochs=3))
    assert 0 <= probe.predict(validation.snapshots[0])["risk_score"] <= 1


def test_db_context_and_rejected_attempts_do_not_join(sources):
    case = sources["cases"][0]
    manifest = json.loads((case["hook"] / "manifest.json").read_text())
    manifest["context"]["attempt"] = 2
    put(case["hook"] / "manifest.json", manifest)
    with sqlite3.connect(sources["database"]) as db:
        db.execute("UPDATE sessions SET context_json=? WHERE id=2", ('{"run_id":"WRONG"}',))
    report = assemble(sources)
    assert report["issues_by_code"]["database_context_mismatch"] == 1
    assert report["source_counts"]["capture_hook_links"] == 4


def test_missing_npz_and_wrong_original_ids_are_reported(sources):
    sources["cases"][0]["capture"].joinpath("features.npz").unlink()
    capture = sources["cases"][1]["capture"]
    put(capture.parent / "c01-input.json", {"identity": {}, "input_ids": [9, 9, 9, 9]})
    report = assemble(sources)
    assert report["issues_by_code"]["missing_feature_archive"] == 1
    assert report["issues_by_code"]["invalid_capture"] == 1
    assert not report["ready_for_training"]


def test_copied_capture_is_not_a_second_training_sample(sources):
    destination = sources["tensors"] / "copied" / "post_residual_block"
    shutil.copytree(sources["cases"][0]["capture"], destination)
    report = assemble(sources)
    assert report["candidates"] == 5
    assert report["source_counts"]["duplicate_capture_references"] == 1


def test_split_conflict_never_becomes_a_training_manifest(sources):
    assemble(sources)
    reviews = reviewed(sources)
    rows = json.loads(reviews.read_text())
    # Preserve the task's actual family but assign it to a different split.
    rows["samples"][1]["split"] = "validation"
    put(reviews, rows)
    output = sources["output"].parent / "bad-split"
    report = assemble(sources, output, reviews=reviews)
    assert report["issues_by_code"]["manifest_rejected"] == 1
    assert not (output / "manifest.json").exists()


def test_legacy_agent_capture_needs_its_own_review_and_exact_run(sources):
    directory = sources["tensors"] / "interactive" / "post_residual_block"
    shutil.copytree(sources["cases"][0]["capture"], directory)
    metadata = json.loads((directory / "metadata.json").read_text())
    metadata["context"].update(run_id="interactive-run", trajectory_id="shared-legacy-trajectory")
    put(directory / "metadata.json", metadata)
    hook = sources["tensors"] / "interactive" / "hook_inspection"
    put(
        hook / "manifest.json",
        {
            "schema_version": "argus-v.hook-inspection.v1",
            "status": "complete",
            "identity": metadata["identity"],
            "phase": "pre_action_full_prefix_replay",
            "context": {
                "run_id": "another-run",
                "step": 0,
                "trajectory_id": "shared-legacy-trajectory",
                "input_ids": [1, 2, 3, 4],
            },
        },
    )
    report = assemble(sources)
    assert report["candidates"] == 6
    inventory = json.loads((sources["output"] / "sources.json").read_text(encoding="utf-8"))
    interactive = next(row for row in inventory if row["run_id"] == "interactive-run")
    assert interactive["source_policy_label"] is None
    assert interactive["hook_sessions"] == []


def test_missing_sources_never_create_empty_database_or_ready_dataset(tmp_path):
    database = tmp_path / "missing.sqlite3"
    output = tmp_path / "output"
    report = assemble_dataset(
        rollout_roots=[tmp_path / "rollouts"],
        tensor_roots=[tmp_path / "tensors"],
        databases=[database],
        output=output,
    )
    assert report["candidates"] == 0 and not report["ready_for_training"]
    assert not database.exists() and not (output / "manifest.json").exists()

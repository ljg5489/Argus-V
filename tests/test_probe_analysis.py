"""Analysis for activation-only prediction: horizon labels, lead, checks and the train-only signal scan."""

import json

import numpy as np
import pytest

from argus_v.probes import analysis
from argus_v.probes.review import ReviewLog, review_state


def queue_row(trajectory, step, label, *, split="train", task="AV-S01", family="fam-a", tokens=(10, 20, 30),
              capture_dir="", prefix="p"):
    return {"snapshot_id": f"{trajectory}:{step}", "run_id": f"run-{trajectory}", "trajectory_id": trajectory,
            "trajectory_key": trajectory, "action_id": f"{trajectory}:{step}", "step_index": step,
            "token_index": tokens[-1], "capture_dir": capture_dir, "origin": "rollout", "provisional_label": label,
            "family": family, "task_id": task, "scenario_id": task, "rollout_id": trajectory, "condition": "C1",
            "seed": 0, "scenario_key": f"{task}/C1", "step_count": 4, "attempts": 1, "format_failures": 0,
            "prefix_length": tokens[-1] + 1, "action_token_start": tokens[-1] + 1,
            "prefix_ids_sha256": f"{prefix}{trajectory}{step}",
            "observations": [{"token_index": t, "kind": k} for t, k in
                             zip(tokens, ("pre_reasoning", "reasoning+32", "pre_action"))],
            "split": split, "group_key": task}


def make_queue(rows, uncaptured=None):
    trajectories = {}
    for row in rows:
        trajectories.setdefault(row["trajectory_key"], {"uncaptured_steps": (uncaptured or {}).get(row["trajectory_key"], []),
                                                        "snapshots": []})["snapshots"].append(row["snapshot_id"])
    return {"rows": rows, "trajectories": trajectories}


def test_horizon_labels_lead_and_test_exclusion(tmp_path):
    rows = [queue_row("t1", step, label) for step, label in ((0, 0), (1, 0), (3, 1))]  # step 2 has no capture
    rows += [queue_row("t9", 0, 1, split="test", task="AV-S09")]
    queue = make_queue(rows, uncaptured={"t1": [2]})
    state = review_state(queue, ReviewLog(tmp_path / "log.jsonl"))
    out = analysis.analysis_rows(queue, state, label_source="rule")
    assert {r["trajectory_key"] for r in out} == {"t1"}  # test split left out
    by_step = {r["step_index"]: r for r in out if r["observation_bucket"] == "pre_action"}
    assert [by_step[s]["y_next_action"] for s in (0, 1, 3)] == [0, 0, 1]
    assert by_step[0]["y_h2"] == 0 and by_step[0]["y_h3"] is None  # uncaptured step 2 is unknown
    assert by_step[1]["y_h2"] is None and by_step[1]["y_h3"] == 1
    assert by_step[0]["actions_until_first_violation"] == 3 and by_step[3]["is_first_violation_action"]
    assert by_step[0]["before_first_violation"] and not by_step[3]["before_first_violation"]
    points = [r for r in out if r["step_index"] == 0]
    assert [r["observation_bucket"] for r in points] == ["pre_reasoning", "reasoning_mid", "pre_action"]
    assert points[0]["observation_id"] == "t1:0@t10" and points[-1]["observation_id"] == "t1:0"
    assert points[0]["tokens_until_action_start"] == 20 and points[-1]["tokens_until_action_start"] == 0


def test_reviewed_labels_settle_uncaptured_steps_of_clean_runs(tmp_path):
    rows = [queue_row("t1", 0, 1), queue_row("t1", 2, 1)]
    queue = make_queue(rows, uncaptured={"t1": [1]})
    log = ReviewLog(tmp_path / "log.jsonl")
    for row in rows:
        log.append({"kind": "action", "target": row["snapshot_id"], "reviewer": "kim", "verdict": "compliant"})
    log.append({"kind": "trajectory", "target": "t1", "reviewer": "kim", "verdict": "no_violation",
                "detail": {"provenance": "spontaneous"}})
    out = analysis.pre_action_rows(analysis.analysis_rows(queue, review_state(queue, log)))
    assert [r["y_h3"] for r in out] == [0, 0]  # rule labels (1) are ignored; step 1 counts as compliant
    assert out[0]["trajectory_has_violation"] is False and out[0]["provenance"] == "spontaneous"
    with pytest.raises(ValueError):
        log.append({"kind": "trajectory", "target": "t1", "reviewer": "kim", "verdict": "violation",
                    "detail": {"provenance": "made_up"}})


def test_confounds_flag_a_label_that_tracks_prefix_length(tmp_path):
    rows = []
    for i in range(20):
        label = int(i >= 10)
        tokens = (10, 20, 100 + i * 50 + label * 2000)  # violations have much longer prefixes
        rows.append(queue_row(f"t{i}", 0, label, tokens=tokens, task=f"AV-S{i % 4:02d}"))
        rows.append(queue_row(f"v{i}", 0, label, tokens=tokens, split="validation", task=f"AV-V{i % 4:02d}"))
    queue = make_queue(rows)
    out = analysis.analysis_rows(queue, review_state(queue, ReviewLog(tmp_path / "l.jsonl")), label_source="rule")
    table = {v["variable"]: v for v in analysis.confounds(out)["variables"]}
    assert table["prefix_length"]["train"] == 1.0 and table["prefix_length"]["flag"]
    assert not table["seed"]["flag"]
    suff = analysis.sufficiency(out)
    assert suff["splits"]["train"]["violation"] == 10 and suff["splits"]["validation"]["violation_runs"] == 10


def test_duplicate_prefixes_across_splits_are_reported(tmp_path):
    rows = [queue_row("a", 0, 0, prefix="same"), queue_row("b", 0, 0, split="validation", prefix="same")]
    rows[0]["prefix_ids_sha256"] = rows[1]["prefix_ids_sha256"] = "x" * 64
    queue = make_queue(rows)
    out = analysis.analysis_rows(queue, review_state(queue, ReviewLog(tmp_path / "l.jsonl")), label_source="rule")
    (group,) = analysis.duplicate_prefixes(out)
    assert group["crosses_splits"] and group["trajectories"] == 2


def write_capture(directory, tokens, layers):
    directory.mkdir(parents=True)
    (directory / "metadata.json").write_text(json.dumps({"alignment": [{"token_index": t} for t in tokens]}))
    np.savez(directory / "features.npz", **{f"block_{layer:04d}": array for layer, array in layers.items()})


def test_signal_scan_finds_the_planted_layer_and_ignores_noise(tmp_path):
    rng = np.random.default_rng(1)
    rows = []
    for group in range(6):
        for i in range(12):
            label = int(i < 4)
            name = f"g{group}-{i}"
            noise = rng.standard_normal((3, 16)).astype(np.float32)
            signal = noise.copy()
            signal[:, 0] += 3.0 * label  # layer 0 carries the label at every observation point
            write_capture(tmp_path / name, (10, 20, 30), {0: signal, 1: noise})
            rows.append(queue_row(name, 0, label, task=f"AV-S{group:02d}", capture_dir=str(tmp_path / name)))
        rows.append(queue_row(f"held-{group}", 0, 1, split="validation", task=f"AV-V{group}",
                              capture_dir=str(tmp_path / "missing")))  # never opened
    queue = make_queue(rows)
    out = analysis.analysis_rows(queue, review_state(queue, ReviewLog(tmp_path / "l.jsonl")), label_source="rule")
    result = analysis.signal_scan(out, layers=(0, 1), bootstrap=50)
    cells = {(c["layer"], c["bucket"]): c for c in result["cells"]}
    assert result["groups_with_violations"] == 6 and result["actions"] == 72
    assert cells[(0, "pre_action")]["auroc"] > 0.95 and cells[(0, "pre_action")]["ci_low"] > 0.5
    assert 0.25 < cells[(1, "pre_action")]["auroc"] < 0.75
    assert cells[(0, "pre_reasoning")]["n"] == 72 and (0, "reasoning_end") not in cells
    assert result["prefix_length_auroc"]["pre_action"] == 0.5


def test_signal_scan_needs_violations_in_two_groups(tmp_path):
    rows = [queue_row("a", 0, 1, task="AV-S01"), queue_row("b", 0, 0, task="AV-S02")]
    queue = make_queue(rows)
    out = analysis.analysis_rows(queue, review_state(queue, ReviewLog(tmp_path / "l.jsonl")), label_source="rule")
    assert analysis.signal_scan(out, layers=(0,))["message"].startswith("train needs violations")


def test_auroc_handles_ties_and_one_class():
    assert analysis.auroc([1, 1, 2, 2], [0, 1, 0, 1]) == 0.5
    assert analysis.auroc([0.1, 0.9], [0, 1]) == 1.0
    assert analysis.auroc([1, 2], [1, 1]) is None
    document = analysis.columns_document()
    assert document["roles"]["capture_dir"] == "input_pointer" and document["roles"]["y_h3"] == "label"
    assert document["roles"]["actions_until_first_violation"] == "eval_only"

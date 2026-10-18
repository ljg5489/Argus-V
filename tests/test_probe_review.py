"""Review log → settled labels → reviews.json → assembler manifest (the 라벨 검수 tab's data path)."""

import json
import shutil
from copy import deepcopy
from dataclasses import asdict
from pathlib import Path

import numpy as np
import pytest
from test_probe_assembly import assemble, put, sources  # noqa: F401  (fixture reused)

from argus_v.activations import ActivationCapture, extract_prefix, write_capture
from argus_v.probes import load_probe_dataset, read_manifest
from argus_v.probes.review import (
    ReviewLog,
    build_queue,
    check_trajectory_vote,
    distribution,
    export_reviews,
    resolve,
    review_state,
)

REVISIONS = {"labels_revision": "team-reviewed-v1", "split_revision": "team-split-v1"}


def queue_of(sources):  # noqa: F811
    return build_queue([sources["rollouts"]], [sources["tensors"]], layers=sources["layers"])


def by_task(queue):
    return {row["task_id"]: row for row in queue["rows"]}


def review_everything(sources, log, second_reviewer=True):  # noqa: F811
    """Two reviewers confirm the fixture's truth; every run gets a trajectory verdict and a split."""
    queue = queue_of(sources)
    rows = by_task(queue)
    for index, case in enumerate(sources["cases"]):
        row = rows[f"AV-S{index + 1:02d}"]
        verdict = "violation" if case["label"] else "compliant"
        for reviewer in ("kim", "lee") if second_reviewer else ("kim",):
            log.append({"kind": "action", "target": row["snapshot_id"], "reviewer": reviewer, "verdict": verdict,
                        "note": f"checked step 0 of {row['task_id']}"})
            check_trajectory_vote(queue, log, row["trajectory_key"], reviewer,
                                  "violation" if case["label"] else "no_violation")
            log.append({"kind": "trajectory", "target": row["trajectory_key"], "reviewer": reviewer,
                        "verdict": "violation" if case["label"] else "no_violation"})
        log.append({"kind": "assignment", "target": row["group_key"], "reviewer": "kim",
                    "verdict": {"split": case["split"]}})
    return queue


def test_queue_lists_each_action_with_rule_label_only_as_a_hint(sources, tmp_path):  # noqa: F811
    queue = queue_of(sources)
    assert len(queue["rows"]) == 5 and len(queue["trajectories"]) == 5
    rows = by_task(queue)
    assert [rows[f"AV-S{i:02d}"]["provisional_label"] for i in range(1, 6)] == [0, 1, 0, 1, 1]
    log = ReviewLog(tmp_path / "log.jsonl")
    document, report = export_reviews(queue, log, **REVISIONS)
    assert document["samples"] == [] and report["skipped"] == {"action_unreviewed": 5}  # rule labels never exported
    state = review_state(queue, log)
    assert sum(cell["rule_flagged"] for cell in distribution(queue, state)) == 3


def test_settled_reviews_become_a_training_manifest(sources, tmp_path):  # noqa: F811
    log = ReviewLog(tmp_path / "log.jsonl")
    queue = review_everything(sources, log)
    document, report = export_reviews(queue, log, **REVISIONS)
    assert report["exported"] == 5 and report["skipped"] == {}
    assert report["counts_by_split_and_label"] == {"train": {0: 1, 1: 1}, "validation": {0: 1, 1: 1}, "test": {1: 1}}
    reviews = tmp_path / "reviews.json"
    put(reviews, document)
    result = assemble(sources, reviews=reviews)
    assert result["manifest_written"] and result["ready_for_training"]
    manifest = read_manifest(sources["output"] / "manifest.json")
    labels = {s["task_group_id"]: (s["next_action_violation"], s["trajectory_has_violation"]) for s in manifest["samples"]}
    assert labels["AV-S02"] == (1, True) and labels["AV-S03"] == (0, False)
    assert load_probe_dataset(sources["output"] / "manifest.json", split="train", layers=sources["layers"]).labels.tolist() == [0, 1]


def test_single_reviewer_violation_waits_for_a_second_review(sources, tmp_path):  # noqa: F811
    log = ReviewLog(tmp_path / "log.jsonl")
    queue = review_everything(sources, log, second_reviewer=False)
    _, report = export_reviews(queue, log, **REVISIONS)
    # 3 violations wait; their trajectories are violation verdicts from one reviewer → also unsettled
    assert report["exported"] == 2 and report["skipped"] == {"action_needs_second_review": 3}
    _, report = export_reviews(queue, log, **REVISIONS, allow_single_positive=True)
    assert report["exported"] == 5 and report["single_reviewer_positives"] == 3
    assert any("single reviewer" in warning for warning in report["warnings"])


def test_conflict_is_excluded_until_adjudicated_and_withdrawal_counts(sources, tmp_path):  # noqa: F811
    log = ReviewLog(tmp_path / "log.jsonl")
    queue = review_everything(sources, log)
    target = by_task(queue)["AV-S02"]["snapshot_id"]
    log.append({"kind": "action", "target": target, "reviewer": "lee", "verdict": "compliant"})
    assert review_state(queue, log)["actions"][target]["state"] == "conflict"
    _, report = export_reviews(queue, log, **REVISIONS)
    assert report["skipped"] == {"action_conflict": 1}
    log.append({"kind": "action", "target": target, "reviewer": "park", "role": "adjudication",
                "verdict": "violation", "note": "the copy to the personal address was attempted"})
    status = review_state(queue, log)["actions"][target]
    assert (status["state"], status["verdict"], status["adjudicator"]) == ("adjudicated", "violation", "park")
    log.append({"kind": "action", "target": target, "reviewer": "park", "role": "adjudication", "verdict": None})
    assert review_state(queue, log)["actions"][target]["state"] == "conflict"  # withdrawn adjudication


def test_violation_free_run_needs_every_action_judged_compliant(sources, tmp_path):  # noqa: F811
    log = ReviewLog(tmp_path / "log.jsonl")
    queue = queue_of(sources)
    row = by_task(queue)["AV-S03"]
    with pytest.raises(ValueError, match="review all"):
        check_trajectory_vote(queue, log, row["trajectory_key"], "kim", "no_violation")
    log.append({"kind": "action", "target": row["snapshot_id"], "reviewer": "kim", "verdict": "unclear"})
    with pytest.raises(ValueError, match="violation/unclear"):
        check_trajectory_vote(queue, log, row["trajectory_key"], "kim", "no_violation")
    check_trajectory_vote(queue, log, row["trajectory_key"], "kim", "violation")  # always allowed


def test_trajectory_verdict_contradicting_its_actions_is_not_exported(sources, tmp_path):  # noqa: F811
    log = ReviewLog(tmp_path / "log.jsonl")
    queue = review_everything(sources, log)
    row = by_task(queue)["AV-S02"]  # its action is a settled violation
    for reviewer in ("kim", "lee"):
        log.append({"kind": "trajectory", "target": row["trajectory_key"], "reviewer": reviewer,
                    "verdict": "no_violation"})
    _, report = export_reviews(queue, log, **REVISIONS)
    assert report["skipped"] == {"trajectory_conflicts_with_actions": 1}


def test_log_validates_events_and_resolve_states(tmp_path):
    log = ReviewLog(tmp_path / "log.jsonl")
    for bad in ({"kind": "action", "target": "x", "reviewer": "", "verdict": "violation"},
                {"kind": "action", "target": "x", "reviewer": "kim", "verdict": "maybe"},
                {"kind": "assignment", "target": "g", "reviewer": "kim", "verdict": {"split": "dev"}}):
        with pytest.raises(ValueError):
            log.append(bad)
    assert not log.path.exists()
    vote = lambda reviewer, verdict: {"reviewer": reviewer, "verdict": verdict, "at": "t"}  # noqa: E731
    assert resolve([vote("a", "compliant")], None)["state"] == "single"
    assert resolve([vote("a", "unclear")], None)["state"] == "needs_second_review"
    assert resolve([vote("a", "violation"), vote("b", "violation")], None)["state"] == "agreed"
    log.path.write_text("{broken\n")
    with pytest.raises(ValueError, match="damaged"):
        log.events()


def test_missing_layers_are_reported_by_name(sources):  # noqa: F811
    result = assemble({**sources, "layers": (0, 1, 5)})
    assert result["issues_by_code"].get("layers_unavailable") == 5 and "invalid_capture" not in result["issues_by_code"]


def test_all_observation_points_share_the_action_label(sources, adapter, ids, context, tmp_path):  # noqa: F811
    # rewrite case 0's capture with an earlier observation row (pre_reasoning at token 1)
    case = sources["cases"][0]
    capture = extract_prefix(adapter, ids, context, token_positions=(1, 3))
    metadata = deepcopy(capture.metadata)
    original = json.loads((case["capture"] / "metadata.json").read_text())
    metadata["context"] = original["context"]
    shutil.rmtree(case["capture"])
    write_capture(ActivationCapture(capture.features, metadata), case["capture"])
    rollout = json.loads(case["rollout"].read_text())
    rollout["steps"][0]["observations"] = [{"token_index": 1, "kind": "pre_reasoning"},
                                           {"token_index": 3, "kind": "pre_action"}]
    put(case["rollout"], rollout)
    log = ReviewLog(tmp_path / "log.jsonl")
    document, _ = export_reviews(review_everything(sources, log), log, **REVISIONS)
    reviews = tmp_path / "reviews.json"
    put(reviews, document)
    result = assemble(sources, reviews=reviews, observation_points="all")
    assert result["samples_by_observation_kind"] == {"pre_action": 5, "pre_reasoning": 1}
    manifest = read_manifest(sources["output"] / "manifest.json")
    same_action = [s for s in manifest["samples"] if s["task_group_id"] == "AV-S01"]
    assert sorted(s["token_index"] for s in same_action) == [1, 3]
    assert {s["next_action_violation"] for s in same_action} == {0} and len({s["split"] for s in same_action}) == 1
    train = load_probe_dataset(sources["output"] / "manifest.json", split="train", layers=sources["layers"])
    assert len(train.labels) == 3 and np.isfinite(train.features).all()
    assert asdict(train.spec.identity) == asdict(adapter.identity)


def test_dashboard_review_desk_end_to_end(sources, tmp_path):  # noqa: F811
    """The 라벨 검수 tab's server side: overview, hidden votes, guarded trajectory, export, projection."""
    from Research.hidden_state_dashboard import ReviewDesk, RolloutIndex

    desk = ReviewDesk(sources["rollouts"], sources["tensors"], tmp_path / "rv" / "review-log.jsonl", None, tmp_path / "rv",
                      layers=sources["layers"])
    overview = desk.overview()
    assert len(overview["rows"]) == 5 and len(overview["unassigned_groups"]) == 5  # no split file → all unassigned
    row = next(r for r in overview["rows"] if r["task_id"] == "AV-S02")
    desk.vote("action", {"snapshot_id": row["snapshot_id"], "reviewer": "kim", "verdict": "violation", "note": "n"})
    hidden = desk.item(row["snapshot_id"], "lee", RolloutIndex(sources["rollouts"]))
    assert hidden["others"] == [{"reviewer": "kim", "role": "review"}] and hidden["own"] is None
    shown = desk.item(row["snapshot_id"], "kim", RolloutIndex(sources["rollouts"]))
    assert shown["own"]["verdict"] == "violation" and shown["trajectory"]["steps"][0]["own_verdict"] == "violation"
    with pytest.raises(ValueError, match="violation/unclear"):
        desk.vote("trajectory", {"trajectory_key": row["trajectory_key"], "reviewer": "kim", "verdict": "no_violation"})
    desk.vote("assignment", {"group_key": "AV-S02", "reviewer": "kim", "split": "train"})
    result = desk.export({"labels_revision": "a", "split_revision": "b", "allow_single_positive": True})
    assert result["skipped"]["trajectory_unsettled"] == 1 and Path(result["path"]).is_file()
    projection = desk.projection(1, "all")
    assert len(projection["points"]) == 5 and projection["excluded_test"]

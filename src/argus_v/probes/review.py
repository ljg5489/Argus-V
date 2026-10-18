"""Human review of next-action labels for probe training data (no model, no feature reading).

The review unit is one action: the C-01 snapshot right before it (``snapshot_id`` from SourceAssembler,
the same identifier reviews.template.json uses). Reviewers answer "is this next action a policy violation
attempt?" from the step record; activations are never shown as label evidence. A trajectory verdict
("did the observed run contain any violation?") is recorded separately.

Reviews are an append-only JSONL log (who, what, when, why); the latest event per
(kind, target, reviewer, role) counts and a ``None`` verdict withdraws it. Positive or unclear actions
want a second independent review; disagreements are settled by an adjudication event. ``export_reviews``
turns the settled state into an ``argus-v.probe-reviews.v1`` document for scripts/assemble_probe_dataset.py.
Rule labels (``policy_label``) are shown only as review priority hints, never exported as labels.
"""

from __future__ import annotations

import json
import threading
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .assembly import REVIEW_SCHEMA, SourceAssembler, load_split_assignments

LOG_SCHEMA = "argus-v.probe-review-log.v1"
ACTION_VERDICTS = ("violation", "compliant", "unclear")
TRAJECTORY_VERDICTS = ("violation", "no_violation", "unclear")
ROLES = ("review", "adjudication")
SPLITS = ("train", "validation", "test")
FINAL_STATES = ("single", "agreed", "adjudicated")  # usable when the verdict is not "unclear"
# optional review details (plan v3.0 §07: first violation recorded apart from whether it was blocked;
# §06/roadmap: spontaneous vs induced/synthetic cases are reported separately)
DETAIL_FIELDS = {
    "action": {"violation_type": ("unauthorized_access", "approval_bypass", "evaluation_tampering",
                                  "unauthorized_disclosure", "other"),
               "outcome": ("executed", "blocked", "failed", "not_executed")},
    "trajectory": {"provenance": ("spontaneous", "induced", "synthetic")},
}


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


class ReviewLog:
    """Append-only review events; one JSON object per line, never rewritten."""

    def __init__(self, path: str | Path):
        self.path = Path(path)
        self._lock = threading.Lock()

    def append(self, event: dict[str, Any]) -> dict[str, Any]:
        kind, reviewer = event.get("kind"), str(event.get("reviewer") or "").strip()
        role, verdict = event.get("role", "review"), event.get("verdict")
        if kind not in ("action", "trajectory", "assignment"):
            raise ValueError("kind must be action, trajectory or assignment")
        if not reviewer:
            raise ValueError("reviewer is required")
        if role not in ROLES:
            raise ValueError("role must be review or adjudication")
        if not isinstance(event.get("target"), str) or not event["target"]:
            raise ValueError("target is required")
        allowed = {"action": ACTION_VERDICTS, "trajectory": TRAJECTORY_VERDICTS}.get(kind)
        if allowed and verdict is not None and verdict not in allowed:
            raise ValueError(f"{kind} verdict must be one of {', '.join(allowed)} (or null to withdraw)")
        detail = event.get("detail") or {}
        if not isinstance(detail, dict) or set(detail) - set(DETAIL_FIELDS.get(kind, {})):
            raise ValueError(f"detail for {kind} may only contain {sorted(DETAIL_FIELDS.get(kind, {}))}")
        for name, value in detail.items():
            if value is not None and value not in DETAIL_FIELDS[kind][name]:
                raise ValueError(f"{name} must be one of {', '.join(DETAIL_FIELDS[kind][name])}")
        if kind == "assignment":
            if not isinstance(verdict, dict) or verdict.get("split") not in SPLITS:
                raise ValueError("assignment needs a split (train/validation/test)")
            for name in ("family_id", "task_group_id"):
                if verdict.get(name) is not None and (not isinstance(verdict[name], str) or not verdict[name].strip()):
                    raise ValueError(f"{name} must be nonempty text")
        record = {"schema_version": LOG_SCHEMA, "at": _now(), **event, "reviewer": reviewer, "role": role,
                  "note": str(event.get("note") or "").strip(),
                  "detail": {name: value for name, value in detail.items() if value is not None}}
        line = json.dumps(record, ensure_ascii=False, allow_nan=False)
        with self._lock:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with self.path.open("a", encoding="utf-8") as handle:
                handle.write(line + "\n")
                handle.flush()
        return record

    def events(self) -> list[dict[str, Any]]:
        if not self.path.is_file():
            return []
        rows = []
        with self.path.open(encoding="utf-8") as handle:
            for number, line in enumerate(handle, 1):
                if line.strip():
                    try:
                        rows.append(json.loads(line))
                    except json.JSONDecodeError as error:
                        raise ValueError(f"{self.path}:{number}: damaged review log line") from error
        return rows

    def latest(self) -> dict[tuple[str, str, str, str], dict[str, Any]]:
        state = {}
        for event in self.events():
            state[(event["kind"], event["target"], event["reviewer"], event["role"])] = event
        return state


def resolve(reviews: list[dict[str, Any]], adjudication: dict[str, Any] | None) -> dict[str, Any]:
    """Settled state of one target from its reviewers' latest verdicts.

    unreviewed / needs_second_review (one violation or unclear) / single (one compliant or no_violation) /
    agreed (≥2 identical) / conflict (different verdicts) / adjudicated (an adjudicator decided).
    """
    votes = {event["reviewer"]: event for event in reviews if event.get("verdict") is not None}
    reviewers = sorted(votes)
    if adjudication is not None and adjudication.get("verdict") is not None:
        return {"state": "adjudicated", "verdict": adjudication["verdict"], "reviewers": reviewers,
                "adjudicator": adjudication["reviewer"], "votes": {r: e["verdict"] for r, e in votes.items()},
                "detail": dict(adjudication.get("detail") or {})}
    verdicts = {event["verdict"] for event in votes.values()}
    detail = {}
    for reviewer in reviewers:  # details of agreeing reviewers, first reviewer (by name) wins a field
        for name, value in (votes[reviewer].get("detail") or {}).items():
            detail.setdefault(name, value)
    base = {"reviewers": reviewers, "adjudicator": None, "votes": {r: e["verdict"] for r, e in votes.items()},
            "detail": detail}
    if not votes:
        return {"state": "unreviewed", "verdict": None, **base}
    if len(verdicts) > 1:
        return {"state": "conflict", "verdict": None, **base}
    verdict = verdicts.pop()
    if len(votes) >= 2:
        return {"state": "agreed", "verdict": verdict, **base}
    if verdict in ("violation", "unclear"):
        return {"state": "needs_second_review", "verdict": verdict, **base}
    return {"state": "single", "verdict": verdict, **base}


def settled(status: dict[str, Any], allow_single_positive: bool) -> str | None:
    """The verdict that may be exported, or None (unclear and unsettled states are never labels)."""
    if status["verdict"] in (None, "unclear"):
        return None
    if status["state"] in FINAL_STATES:
        return status["verdict"]
    if status["state"] == "needs_second_review" and allow_single_positive:
        return status["verdict"]
    return None


def _short(text: Any, limit: int = 400) -> str:
    text = "" if text is None else str(text)
    return text if len(text) <= limit else text[:limit] + " …"


def build_queue(rollout_roots, tensor_roots=(), split_file=None, layers=(23,)) -> dict[str, Any]:
    """One row per reviewable action (C-01 snapshot) plus trajectory summaries; reads JSON only.

    ``layers`` only decides which captures are listed (23 is common to rollout and agent_loop captures);
    the assembler checks the layers actually used for training later.
    """
    assembler = SourceAssembler(rollout_roots, tensor_roots, (), layers=tuple(layers))
    assembler.discover()
    assignments, _ = load_split_assignments(split_file)
    rollouts: dict[str, dict] = {}
    rows, trajectories = [], {}
    for candidate in assembler.candidates.values():
        source = candidate["sources"][0]
        row = {key: candidate[key] for key in ("snapshot_id", "run_id", "trajectory_id", "action_id",
                                               "step_index", "token_index", "capture_dir")}
        row.update(prefix_length=candidate["prefix_length"], action_token_start=candidate.get("action_token_start"),
                   prefix_ids_sha256=candidate["prefix_ids_sha256"],
                   observations=candidate.get("observation_points") or [{"token_index": candidate["token_index"],
                                                                          "kind": "pre_action"}])
        row.update(origin=source["kind"], provisional_label=candidate["source_policy_label"],
                   family=candidate["source_family_id"], task_id=candidate["source_task_group_id"],
                   scenario_id=candidate["source_scenario_id"])
        if source["kind"] == "rollout":
            path = source["rollout_file"]
            if path not in rollouts:
                rollouts[path] = json.loads(Path(path).read_text(encoding="utf-8"))
            rollout = rollouts[path]
            step = next((s for s in rollout.get("steps", []) if s.get("step_index") == candidate["step_index"]), {})
            row.update(rollout_id=Path(path).parent.name, condition=rollout.get("condition"), seed=rollout.get("seed"),
                       scenario_key=rollout.get("scenario_key"), step_count=len(rollout.get("steps", [])),
                       step_kind=step.get("kind"), command=_short(step.get("command")),
                       findings=len(step.get("static_findings") or []) + len(step.get("effect_findings") or []),
                       observation_points=len(step.get("observations") or []),
                       attempts=step.get("attempts"),
                       format_failures=len(step["format_failures"]) if isinstance(step.get("format_failures"), list)
                       else step.get("format_failures"))
            trajectory = trajectories.setdefault(candidate["trajectory_id"], {
                "trajectory_id": candidate["trajectory_id"], "origin": "rollout", "rollout_id": row["rollout_id"],
                "scenario_key": rollout.get("scenario_key"), "family": rollout.get("family"),
                "task_id": rollout.get("task_id"), "condition": rollout.get("condition"), "seed": rollout.get("seed"),
                "termination": rollout.get("termination"), "step_count": len(rollout.get("steps", [])),
                "uncaptured_steps": [s.get("step_index") for s in rollout.get("steps", []) if not s.get("capture_dir")],
                "snapshots": []})
        else:  # agent_loop: manual task, no rollout.json; the step folder holds the generation record
            row.update(rollout_id=None, condition=None, seed=None, scenario_key="agent_loop", step_count=None,
                       step_kind=None, command=None, findings=0, observation_points=None, attempts=None,
                       format_failures=None)
            trajectory = trajectories.setdefault(candidate["trajectory_id"] + "@" + candidate["run_id"], {
                "trajectory_id": candidate["trajectory_id"], "origin": "agent_loop", "rollout_id": None,
                "scenario_key": "agent_loop", "family": None, "task_id": None, "condition": None, "seed": None,
                "termination": None, "step_count": None, "uncaptured_steps": [], "snapshots": []})
        row["trajectory_key"] = trajectory_key(row)
        row["split"] = assignments.get(row["task_id"]) if row["task_id"] else None
        row["group_key"] = row["task_id"] or f"agent_loop:{row['run_id']}"
        trajectory["snapshots"].append(row["snapshot_id"])
        rows.append(row)
    rows.sort(key=lambda r: (r["scenario_key"] or "", r["seed"] if r["seed"] is not None else -1,
                             r["rollout_id"] or r["run_id"], r["step_index"]))
    skipped = Counter(issue["code"] for issue in assembler.issues
                      if issue["code"] in ("invalid_capture", "layers_unavailable", "step_without_capture",
                                           "unfinished_rollout", "missing_feature_archive"))
    return {"rows": rows, "trajectories": trajectories, "skipped": dict(skipped),
            "split_assigned_groups": sorted(set(assignments)), "layers": list(layers)}


def trajectory_key(row: dict[str, Any]) -> str:
    """Rollout trajectory ids are unique; agent_loop reuses names like task_001_seed_42, so add the run."""
    return row["trajectory_id"] if row.get("origin") == "rollout" else f"{row['trajectory_id']}@{row['run_id']}"


def review_state(queue: dict[str, Any], log: ReviewLog) -> dict[str, Any]:
    """Per-action and per-trajectory settled status, plus group assignments (latest per group)."""
    latest = log.latest()
    grouped: dict[tuple[str, str], dict[str, list | dict | None]] = defaultdict(lambda: {"review": [], "adjudication": None})
    assignments: dict[str, dict] = {}
    for (kind, target, _reviewer, role), event in latest.items():
        if kind == "assignment":
            previous = assignments.get(target)
            if previous is None or event["at"] >= previous["at"]:
                assignments[target] = event
            continue
        slot = grouped[(kind, target)]
        if role == "adjudication":
            if slot["adjudication"] is None or event["at"] >= slot["adjudication"]["at"]:
                slot["adjudication"] = event
        else:
            slot["review"].append(event)
    actions = {row["snapshot_id"]: resolve(grouped[("action", row["snapshot_id"])]["review"],
                                           grouped[("action", row["snapshot_id"])]["adjudication"])
               for row in queue["rows"]}
    notes = {}
    for (kind, target), slot in grouped.items():
        events = slot["review"] + ([slot["adjudication"]] if slot["adjudication"] else [])
        notes[(kind, target)] = [{"reviewer": e["reviewer"], "role": e["role"], "verdict": e.get("verdict"),
                                  "note": e.get("note", ""), "detail": e.get("detail") or {}, "at": e["at"]}
                                 for e in events]
    trajectories = {key: resolve(grouped[("trajectory", key)]["review"], grouped[("trajectory", key)]["adjudication"])
                    for key in queue["trajectories"]}
    return {"actions": actions, "trajectories": trajectories, "notes": notes,
            "assignments": {target: event["verdict"] | {"reviewer": event["reviewer"], "at": event["at"]}
                            for target, event in assignments.items()}}


def check_trajectory_vote(queue: dict[str, Any], log: ReviewLog, trajectory: str, reviewer: str, verdict: str) -> None:
    """A reviewer may only call a trajectory violation-free after judging each of its actions compliant."""
    if verdict != "no_violation":
        return
    rows = [row for row in queue["rows"] if row["trajectory_key"] == trajectory]
    latest = log.latest()
    own = {row["snapshot_id"]: (latest.get(("action", row["snapshot_id"], reviewer, "review")) or {}).get("verdict")
           for row in rows}
    missing = [sid for sid, value in own.items() if value is None]
    flagged = [sid for sid, value in own.items() if value in ("violation", "unclear")]
    if flagged:
        raise ValueError(f"{len(flagged)} action(s) of this run are marked violation/unclear by {reviewer}")
    if missing:
        raise ValueError(f"review all {len(rows)} actions of this run first ({len(missing)} left for {reviewer})")


def export_reviews(queue: dict[str, Any], log: ReviewLog, *, labels_revision: str, split_revision: str,
                   allow_single_positive: bool = False) -> tuple[dict[str, Any], dict[str, Any]]:
    """(reviews document for assemble_probe_dataset.py, export report). Only settled labels are exported.

    An action enters only when its own label and its trajectory verdict are settled, its trajectory verdict
    is consistent with its actions (no_violation needs every captured action settled compliant), and it has
    a split. trajectory_has_violation is true when the trajectory verdict or any settled action says so.
    """
    if not str(labels_revision).strip() or not str(split_revision).strip():
        raise ValueError("labels_revision and split_revision are required")
    state = review_state(queue, log)
    by_trajectory = defaultdict(list)
    for row in queue["rows"]:
        by_trajectory[row["trajectory_key"]].append(row)
    samples, skipped, single_positive = [], Counter(), 0
    trajectory_outcome = {}
    for key, rows in by_trajectory.items():
        verdict = settled(state["trajectories"][key], allow_single_positive)
        labels = {row["snapshot_id"]: settled(state["actions"][row["snapshot_id"]], allow_single_positive)
                  for row in rows}
        if verdict is None:
            trajectory_outcome[key] = "trajectory_unsettled"
        elif verdict == "no_violation" and "violation" in labels.values():
            trajectory_outcome[key] = "trajectory_conflicts_with_actions"
        elif verdict == "no_violation" and any(value != "compliant" for value in labels.values()):
            trajectory_outcome[key] = "trajectory_actions_unsettled"
        else:
            trajectory_outcome[key] = verdict == "violation" or "violation" in labels.values()
    for row in queue["rows"]:
        status = state["actions"][row["snapshot_id"]]
        label = settled(status, allow_single_positive)
        outcome = trajectory_outcome[row["trajectory_key"]]
        assignment = state["assignments"].get(row["group_key"], {})
        split = row["split"] or assignment.get("split")
        family = row["family"] or assignment.get("family_id")
        task = row["task_id"] or assignment.get("task_group_id")
        if label is None:
            skipped["action_" + (status["state"] if status["verdict"] != "unclear" else "unclear")] += 1
        elif isinstance(outcome, str):
            skipped[outcome] += 1
        elif split is None or not family or not task:
            skipped["group_or_split_unassigned"] += 1
        else:
            single_positive += status["state"] == "needs_second_review"
            reviewers = sorted(set(status["reviewers"]) | ({status["adjudicator"]} if status["adjudicator"] else set()))
            notes = [n["note"] for n in state["notes"].get(("action", row["snapshot_id"]), []) if n["note"]]
            samples.append({"snapshot_id": row["snapshot_id"], "reviewed": True, "reviewer": ", ".join(reviewers),
                            "next_action_violation": int(label == "violation"), "trajectory_has_violation": outcome,
                            "family_id": family, "task_group_id": task, "split": split,
                            "note": " | ".join(notes), "review_state": status["state"],
                            "suggested_rule_label": row["provisional_label"],
                            **{name: status["detail"].get(name) for name in DETAIL_FIELDS["action"]},
                            "trajectory_provenance": state["trajectories"][row["trajectory_key"]]["detail"].get(
                                "provenance")})
    document = {"schema_version": REVIEW_SCHEMA, "labels_revision": labels_revision.strip(),
                "split_revision": split_revision.strip(), "exported_at": _now(),
                "review_log": str(log.path), "samples": samples}
    return document, export_report(samples, queue, skipped, single_positive)


def export_report(samples: list[dict], queue: dict[str, Any], skipped: Counter, single_positive: int) -> dict[str, Any]:
    counts = {split: dict(Counter(s["next_action_violation"] for s in samples if s["split"] == split)) for split in SPLITS}
    trajectory_of = {row["snapshot_id"]: row["trajectory_key"] for row in queue["rows"]}
    split_trajectories = {split: {"violation": set(), "no_violation": set()} for split in SPLITS}
    positive_families = {split: set() for split in SPLITS}
    for sample in samples:
        bucket = "violation" if sample["trajectory_has_violation"] else "no_violation"
        split_trajectories[sample["split"]][bucket].add(trajectory_of[sample["snapshot_id"]])
        if sample["trajectory_has_violation"]:
            positive_families[sample["split"]].add(sample["family_id"])
    warnings = []
    for split in ("train", "validation"):
        if set(counts[split]) != {0, 1}:
            warnings.append(f"{split}: needs both compliant (0) and violation (1) actions")
    if not split_trajectories["validation"]["no_violation"]:
        warnings.append("validation: no violation-free trajectory, so the false-positive rate cannot be measured")
    if len(positive_families["validation"]) < 2:
        warnings.append(f"validation: violation trajectories cover {len(positive_families['validation'])} family(ies);"
                        " add violation runs of other task families (more seeds of one task do not help)")
    if single_positive:
        warnings.append(f"{single_positive} violation label(s) rest on a single reviewer")
    return {"exported": len(samples), "candidates": len(queue["rows"]), "counts_by_split_and_label": counts,
            "trajectories_by_split": {split: {k: len(v) for k, v in value.items()}
                                      for split, value in split_trajectories.items()},
            "violation_families_by_split": {split: sorted(value) for split, value in positive_families.items()},
            "skipped": dict(skipped), "single_reviewer_positives": single_positive, "warnings": warnings}


def distribution(queue: dict[str, Any], state: dict[str, Any]) -> list[dict[str, Any]]:
    """Counts per (family, condition): actions, rule-flagged, settled violation/compliant, unclear, open."""
    table: dict[tuple, Counter] = defaultdict(Counter)
    for row in queue["rows"]:
        status = state["actions"][row["snapshot_id"]]
        cell = table[(row["family"] or "agent_loop", row["condition"] or "—", row["split"] or "")]
        cell["actions"] += 1
        cell["rule_flagged"] += row["provisional_label"] == 1
        verdict = status["verdict"] if status["state"] in FINAL_STATES else None
        cell["violation"] += verdict == "violation"
        cell["compliant"] += verdict == "compliant"
        cell["unclear"] += status["verdict"] == "unclear"
        cell["open"] += status["state"] in ("unreviewed", "needs_second_review", "conflict")
    return [{"family": family, "condition": condition, "split": split, **dict(counts)}
            for (family, condition, split), counts in sorted(table.items())]

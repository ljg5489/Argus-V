"""Batch M0/M1 text judgments at every manifest observation cutoff (same judge, same prompt).

M1 sees the decoded original prefix ``ids[:p+1]`` (task + policy + history + reasoning so far).
M0 sees the same prefix without this step's reasoning tokens: ``ids[:min(p+1, reasoning_start)]``.
The chat template drops earlier turns' analysis, so M0 is constant within a step and is cached.
Before reasoning starts M1 is undefined (``no_reasoning``); the report then falls back to M0.
Judge failures are kept as ``error`` and never converted into low-risk scores.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path
from typing import Any, Callable

from argus_v.activations.alignment import ActionSpan, SnapshotContext
from argus_v.monitoring.m1 import PROMPT_VERSION, M1Detector
from argus_v.monitoring.snapshot import build_m1_snapshot, ids_sha256
from argus_v.probes.data import read_manifest

MONITORS = ("M0", "M1")


@dataclass(frozen=True)
class ExternalObservation:
    """M0 input: same judge fields as M1, without the current step's reasoning text."""

    snapshot_id: str
    run_id: str
    trajectory_id: str
    token_index: int
    observed_prefix_ids_sha256: str
    task: str
    trusted_policy: str
    observed_prefix_text: str

    def judge_input(self) -> dict[str, str]:
        return {"task": self.task, "trusted_policy": self.trusted_policy,
                "observed_prefix_text": self.observed_prefix_text}

    def join_metadata(self) -> dict[str, Any]:
        return {"snapshot_id": self.snapshot_id, "run_id": self.run_id, "trajectory_id": self.trajectory_id,
                "phase": "pre_action", "token_index": self.token_index,
                "observed_prefix_ids_sha256": self.observed_prefix_ids_sha256, "reasoning_excluded": True}


def load_observation(sample: dict, manifest_dir: Path) -> dict[str, Any]:
    """Capture metadata plus the runner's c01-input/m1-context sidecars (scenario_rollout layout)."""
    capture_dir = (manifest_dir / sample["capture_dir"]).resolve()
    metadata = json.loads((capture_dir / "metadata.json").read_text(encoding="utf-8"))
    source = json.loads((capture_dir.parent / "c01-input.json").read_text(encoding="utf-8"))
    context = json.loads((capture_dir.parent / "m1-context.json").read_text(encoding="utf-8"))
    if source["input_ids"] and ids_sha256(source["input_ids"]) != metadata["prefix_ids_sha256"]:
        raise ValueError(f"{sample['snapshot_id']}: c01-input IDs differ from the capture")
    return {"metadata": metadata, "input_ids": source["input_ids"], "context": context}


def observation_meta(sample: dict, metadata: dict) -> dict[str, Any]:
    raw = metadata["context"]
    action = ActionSpan(**raw["action"])
    SnapshotContext(**{**raw, "action": action})  # validates the annotation shape
    return {"step_index": action.step_index, "action_start": action.token_start}


def _read_results(path: Path) -> dict[str, dict]:
    if not path.exists():
        return {}
    return {row["snapshot_id"]: row for row in map(json.loads, path.read_text(encoding="utf-8").splitlines()) if row}


def score_text_monitors(manifest_path: str | Path, detector: M1Detector, tokenizer: Any, output_dir: str | Path,
                        *, monitors: tuple[str, ...] = MONITORS, splits: tuple[str, ...] = ("train", "validation", "test"),
                        log: Callable[[str], None] = print) -> dict[str, dict[str, int]]:
    """Append one JSON line per snapshot to ``<monitor>.jsonl``; existing lines are skipped (resume)."""
    manifest_path = Path(manifest_path).resolve()
    manifest = read_manifest(manifest_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    cache_path = output_dir / "judge-cache.jsonl"
    cache = {row["input_sha256"]: row for row in _read_results_cache(cache_path)}
    done = {monitor: _read_results(output_dir / f"{monitor.lower()}.jsonl") for monitor in monitors}
    counts = {monitor: {"ok": 0, "error": 0, "no_reasoning": 0, "cached": 0} for monitor in monitors}
    identity = detector.judge_identity
    samples = [s for s in manifest["samples"] if s["split"] in splits]
    for index, sample in enumerate(samples):
        # Errors are retried on a later run; the last line per snapshot wins when reading.
        pending = [m for m in monitors
                   if done[m].get(sample["snapshot_id"], {}).get("status") not in ("ok", "no_reasoning")]
        if not pending:
            continue
        observation = load_observation(sample, manifest_path.parent)
        ids, context, metadata = observation["input_ids"], observation["context"], observation["metadata"]
        position = sample["token_index"]
        span = context.get("reasoning_token_span")
        for monitor in pending:
            row = {"snapshot_id": sample["snapshot_id"], "monitor": monitor}
            if monitor == "M1" and (not span or span[0] > position):
                row.update(status="no_reasoning", risk_score=None)
            else:
                if monitor == "M1":
                    snapshot = build_m1_snapshot(
                        metadata, ids, tokenizer, tokenizer_id=metadata["identity"]["tokenizer_id"],
                        tokenizer_revision=metadata["identity"]["tokenizer_revision"],
                        snapshot_id=sample["snapshot_id"], task=context["task"],
                        trusted_policy=context["trusted_policy"], reasoning_token_span=tuple(span),
                        token_index=position)
                else:
                    end = min(position + 1, span[0]) if span else position + 1
                    observed = ids[:end]
                    snapshot = ExternalObservation(
                        sample["snapshot_id"], sample["run_id"], sample["trajectory_id"], position,
                        ids_sha256(observed), context["task"], context["trusted_policy"],
                        tokenizer.decode(observed, skip_special_tokens=False, clean_up_tokenization_spaces=False))
                payload = json.dumps(snapshot.judge_input(), ensure_ascii=False, sort_keys=True)
                key = sha256(json.dumps([PROMPT_VERSION, identity.model_id, identity.model_revision, payload],
                                        ensure_ascii=False).encode("utf-8")).hexdigest()
                if key in cache:
                    cached = cache[key]
                    counts[monitor]["cached"] += 1
                else:
                    result = detector.detect(snapshot)
                    cached = {"input_sha256": key, "status": result.status, "risk_score": result.risk_score,
                              "reason": result.reason, "error": result.error}
                    if result.status == "ok":  # errors are retried on the next run, never cached
                        cache[key] = cached
                        with cache_path.open("a", encoding="utf-8") as handle:
                            handle.write(json.dumps(cached, ensure_ascii=False) + "\n")
                row.update({k: cached[k] for k in ("status", "risk_score", "reason", "error")}, input_sha256=key)
            counts[monitor][row["status"]] += 1
            with (output_dir / f"{monitor.lower()}.jsonl").open("a", encoding="utf-8") as handle:
                handle.write(json.dumps(row, ensure_ascii=False) + "\n")
            done[monitor][sample["snapshot_id"]] = row
        log(f"[judge {index + 1}/{len(samples)}] {sample['snapshot_id']} "
            + " ".join(f"{m}={done[m][sample['snapshot_id']].get('risk_score')}" for m in pending))
    return counts


def _read_results_cache(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]

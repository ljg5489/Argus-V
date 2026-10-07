"""Decode the exact causal prefix observed by a selected C-01 activation row."""

import json
from dataclasses import asdict, dataclass
from hashlib import sha256
from typing import Any, Protocol

from argus_v.activations.adapter import ModelIdentity
from argus_v.activations.alignment import ActionSpan, SnapshotContext, require_index, require_text


class PrefixDecoder(Protocol):
    def decode(self, token_ids: list[int], **kwargs: Any) -> str: ...


def ids_sha256(ids: list[int]) -> str:
    return sha256(json.dumps(ids, separators=(",", ":")).encode("ascii")).hexdigest()


@dataclass(frozen=True)
class M1Snapshot:
    """Only the three text fields go to the judge; coordinates are join metadata."""

    snapshot_id: str
    run_id: str
    trajectory_id: str
    source_identity: ModelIdentity
    observed_prefix_length: int
    token_index: int
    capture_prefix_ids_sha256: str
    observed_prefix_ids_sha256: str
    reasoning_token_span: tuple[int, int]
    task: str
    trusted_policy: str
    observed_prefix_text: str
    capture_mode: str = "full_prefix_replay"

    def __post_init__(self) -> None:
        for name in (
            "snapshot_id",
            "run_id",
            "trajectory_id",
            "task",
            "trusted_policy",
            "observed_prefix_text",
            "capture_prefix_ids_sha256",
            "observed_prefix_ids_sha256",
        ):
            require_text(getattr(self, name), name)
        require_index(self.token_index, "token_index")
        if self.observed_prefix_length != self.token_index + 1:
            raise ValueError("M1 must observe exactly token_index + 1 tokens")
        start, end = self.reasoning_token_span
        require_index(start, "reasoning start")
        require_index(end, "reasoning end")
        if not 0 <= start < end <= self.observed_prefix_length:
            raise ValueError("M1 requires accessible reasoning inside the observed prefix")

    def judge_input(self) -> dict[str, str]:
        # No scenario/action IDs, action boundaries, labels, logits or activation.
        return {
            "task": self.task,
            "trusted_policy": self.trusted_policy,
            "observed_prefix_text": self.observed_prefix_text,
        }

    def join_metadata(self) -> dict[str, Any]:
        return {
            "snapshot_id": self.snapshot_id,
            "run_id": self.run_id,
            "trajectory_id": self.trajectory_id,
            "source_identity": asdict(self.source_identity),
            "phase": "pre_action",
            "capture_mode": self.capture_mode,
            "token_index": self.token_index,
            "predicts_token_index": self.token_index + 1,
            "observed_prefix_length": self.observed_prefix_length,
            "capture_prefix_ids_sha256": self.capture_prefix_ids_sha256,
            "observed_prefix_ids_sha256": self.observed_prefix_ids_sha256,
            "reasoning_token_span": list(self.reasoning_token_span),
        }


def build_m1_snapshot(
    capture_metadata: dict[str, Any],
    input_ids: list[int],
    tokenizer: PrefixDecoder,
    *,
    tokenizer_id: str,
    tokenizer_revision: str,
    snapshot_id: str,
    task: str,
    trusted_policy: str,
    reasoning_token_span: tuple[int, int],
    token_index: int | None = None,
) -> M1Snapshot:
    """Use original observation IDs, not IDs re-tokenized from the decoded text.

    input_ids must be exactly the input to extract_prefix, not a full trajectory.
    Earlier selected rows are supported: h[p] only gets text from IDs[:p+1].
    The caller attests the tokenizer identity and that task/policy are available
    at observation time. This cannot audit the truth of runner annotations.
    """
    schemas = {
        "argus-v.activation.v1": "full_prefix_replay",
        "argus-v.generation-observation.v1": "incremental_generation",
    }
    schema = capture_metadata.get("schema_version")
    if schema not in schemas or capture_metadata.get("capture_mode") != schemas[schema]:
        raise ValueError("expected C-01 or aligned generation observation metadata")
    if (
        not isinstance(input_ids, list)
        or not input_ids
        or any(type(i) is not int or i < 0 for i in input_ids)
    ):
        raise ValueError("input_ids must be a nonempty list of nonnegative integer IDs")
    if capture_metadata["observed_prefix_length"] != len(input_ids):
        raise ValueError("input_ids length differs from the M2 capture (future tokens?)")
    capture_hash = ids_sha256(input_ids)
    if capture_metadata["prefix_ids_sha256"] != capture_hash:
        raise ValueError("input_ids hash differs from the M2 capture")
    identity = ModelIdentity(**capture_metadata["identity"])
    if (tokenizer_id, tokenizer_revision) != (identity.tokenizer_id, identity.tokenizer_revision):
        raise ValueError("source tokenizer identity/revision differs from the M2 capture")
    raw_context = capture_metadata["context"]
    context = SnapshotContext(**{**raw_context, "action": ActionSpan(**raw_context["action"])})
    if context.phase != "pre_action":
        raise ValueError("M1 early detection requires pre_action; pre_execution belongs to E2")
    context.validate_prefix(len(input_ids))
    position = len(input_ids) - 1 if token_index is None else token_index
    require_index(position, "token_index")
    if position >= len(input_ids):
        raise ValueError("token_index is outside the captured prefix")
    rows = [r for r in capture_metadata["alignment"] if r["token_index"] == position]
    if len(rows) != 1:
        raise ValueError("token_index must identify exactly one captured M2 activation row")
    row = rows[0]
    if row["token_id"] != input_ids[position] or row["predicts_token_index"] != position + 1:
        raise ValueError("M2 row has inconsistent token alignment")
    observed_ids = input_ids[: position + 1]
    if len(reasoning_token_span) != 2:
        raise ValueError("reasoning_token_span must be [start, end) in original token coordinates")
    start, end = reasoning_token_span
    require_index(start, "reasoning start")
    require_index(end, "reasoning end")
    if not start < end <= len(input_ids):
        raise ValueError("reasoning_token_span is outside the captured prefix")
    if start >= len(observed_ids):
        raise ValueError("no reasoning is observed at this row; report M0 rather than M1")
    text = tokenizer.decode(
        observed_ids, skip_special_tokens=False, clean_up_tokenization_spaces=False
    )
    return M1Snapshot(
        snapshot_id,
        context.run_id,
        context.trajectory_id,
        identity,
        position + 1,
        position,
        capture_hash,
        ids_sha256(observed_ids),
        (start, min(end, len(observed_ids))),
        task,
        trusted_policy,
        text,
        capture_mode=capture_metadata["capture_mode"],
    )


def build_m1_snapshot_from_generation_step(
    step: dict[str, Any],
    tokenizer: PrefixDecoder,
    context: SnapshotContext,
    source_identity: ModelIdentity,
    **snapshot_options: Any,
) -> M1Snapshot:
    """Consume the new legacy MLP generation log without reading its activations.

    The runner supplies pre_action context and accessible reasoning coordinates.
    Old logs with only a sampled token cannot reconstruct the observation cutoff.
    """
    ids = step["observed_input_ids"]
    length = step["observed_prefix_length"]
    if type(length) is not int or length <= 0 or length != len(ids):
        raise ValueError("generation step has inconsistent observed prefix length")
    if step["observed_token_index"] != length - 1 or step["predicts_token_index"] != length:
        raise ValueError("generation step has inconsistent observation coordinates")
    metadata = {
        "schema_version": "argus-v.generation-observation.v1",
        "capture_mode": "incremental_generation",
        "identity": asdict(source_identity),
        "context": asdict(context),
        "observed_prefix_length": length,
        "prefix_ids_sha256": step["prefix_ids_sha256"],
        "alignment": [
            {
                "token_index": length - 1,
                "token_id": ids[-1],
                "predicts_token_index": length,
            }
        ],
    }
    return build_m1_snapshot(metadata, ids, tokenizer, **snapshot_options)

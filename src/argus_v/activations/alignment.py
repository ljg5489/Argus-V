"""Token coordinates are indexes in the exact, unpadded model input, including BOS."""

from dataclasses import dataclass
from typing import Literal


def require_text(value: str, name: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} must be a nonempty string")


def require_index(value: int, name: str) -> None:
    if type(value) is not int or value < 0:
        raise ValueError(f"{name} must be a nonnegative integer")


@dataclass(frozen=True)
class ActionSpan:
    """Boundary supplied by the runner; not inferred by searching decoded text.

    [token_start, token_end) covers one proposed tool call. token_end may be unknown
    for early snapshots. No tool result token belongs inside this span.
    """

    action_id: str
    step_index: int
    token_start: int
    token_end: int | None = None

    def __post_init__(self) -> None:
        require_text(self.action_id, "action_id")
        require_index(self.step_index, "step_index")
        require_index(self.token_start, "token_start")
        if self.token_end is not None:
            require_index(self.token_end, "token_end")
            if self.token_end <= self.token_start:
                raise ValueError("token_end must be after token_start (exclusive end)")


@dataclass(frozen=True)
class SnapshotContext:
    run_id: str
    trajectory_id: str
    scenario_id: str
    phase: Literal["pre_action", "pre_execution"]
    action: ActionSpan

    def __post_init__(self) -> None:
        for name in ("run_id", "trajectory_id", "scenario_id"):
            require_text(getattr(self, name), name)
        if self.phase not in ("pre_action", "pre_execution"):
            raise ValueError("phase must be pre_action or pre_execution")
        if not isinstance(self.action, ActionSpan):
            raise ValueError("action must be an ActionSpan")

    def validate_prefix(self, length: int) -> None:
        require_index(length, "prefix length")
        if length == 0:
            raise ValueError("prefix must contain at least one token")
        if self.phase == "pre_action" and length > self.action.token_start:
            raise ValueError("pre_action prefix includes action/future tokens")
        if self.phase == "pre_execution":
            if self.action.token_end is None or length != self.action.token_end:
                raise ValueError("pre_execution prefix must end exactly at action.token_end")


@dataclass(frozen=True)
class TokenAlignment:
    token_index: int
    token_id: int
    predicts_token_index: int
    tokens_until_action_start: int


def align_tokens(
    token_ids: list[int], positions: tuple[int, ...], context: SnapshotContext
) -> tuple[TokenAlignment, ...]:
    """h[p] observes through token p and predicts p+1, never token p itself."""
    context.validate_prefix(len(token_ids))
    if not positions:
        raise ValueError("at least one token position must be selected")
    for pos in positions:
        require_index(pos, "token position")
        if pos >= len(token_ids):
            raise ValueError("token position is outside the provided prefix")
    if tuple(sorted(set(positions))) != positions:
        raise ValueError("token positions must be unique and increasing")
    return tuple(
        TokenAlignment(pos, token_ids[pos], pos + 1, context.action.token_start - (pos + 1))
        for pos in positions
    )

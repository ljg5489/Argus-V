"""Prevent future final-action tokens from entering the M1 observation."""

import importlib.util
from pathlib import Path

import pytest

SPEC = importlib.util.spec_from_file_location(
    "m1_sandbox_runner", Path(__file__).resolve().parents[1] / "scripts" / "run_m1_sandbox.py"
)
RUNNER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(RUNNER)


def test_reasoning_cutoff_excludes_entire_future_action():
    prefix = ["task", "<|start|>", "assistant"]
    generated = [
        "<|channel|>",
        "analysis",
        "<|message|>",
        "allowed reasoning",
        "<|end|>",
        "<|start|>",
        "assistant",
        "<|channel|>",
        "final",
        "<|message|>",
        "future action",
        "<|return|>",
    ]
    cutoff, span, final = RUNNER.observation_boundary(prefix + generated, len(prefix))
    assert cutoff == 8
    assert span == (6, 7)
    assert (prefix + generated)[final[0] : final[1]] == ["future action"]
    assert "future action" not in (prefix + generated)[:cutoff]


def test_task_analysis_cannot_substitute_for_generated_reasoning():
    prompt = ["<|start|>", "assistant", "<|channel|>", "analysis", "<|message|>", "old", "<|end|>"]
    output = [
        "<|start|>",
        "assistant",
        "<|channel|>",
        "final",
        "<|message|>",
        "action",
        "<|return|>",
    ]
    with pytest.raises(ValueError, match="generated reasoning"):
        RUNNER.observation_boundary(prompt + output, len(prompt))


def test_truncated_action_is_rejected():
    pieces = [
        "<|start|>",
        "assistant",
        "<|channel|>",
        "analysis",
        "<|message|>",
        "thought",
        "<|end|>",
        "<|start|>",
        "assistant",
        "<|channel|>",
        "final",
        "<|message|>",
        "incomplete action",
    ]
    with pytest.raises(ValueError, match="Incomplete final action"):
        RUNNER.observation_boundary(pieces, 2)

import json
from dataclasses import replace
from hashlib import sha256

import numpy as np
import pytest

from argus_v.activations import ActionSpan, ModelIdentity, extract_prefix, write_capture
from argus_v.activations.runtime import gpt_oss_preflight


def test_action_start_is_exclusive_for_early_capture(context):
    context.validate_prefix(4)
    with pytest.raises(ValueError, match="future"):
        context.validate_prefix(5)
    with pytest.raises(ValueError):
        context.validate_prefix(0)


@pytest.mark.parametrize("length", [4, 6, 8])
def test_execution_rejects_partial_action_and_tool_result_tokens(context, length):
    with pytest.raises(ValueError, match="exactly"):
        replace(context, phase="pre_execution").validate_prefix(length)


def test_unknown_action_end_only_allowed_for_pre_action(context):
    unknown = replace(context, action=replace(context.action, token_end=None))
    unknown.validate_prefix(4)
    with pytest.raises(ValueError, match="exactly"):
        replace(unknown, phase="pre_execution").validate_prefix(7)


@pytest.mark.parametrize("start,end", [(-1, 4), (4, 4), (4, 3), (True, 4)])
def test_rejects_invalid_action_span(start, end):
    with pytest.raises(ValueError):
        ActionSpan("action", 0, start, end)


def test_model_identity_requires_version():
    with pytest.raises(ValueError, match="model_revision"):
        ModelIdentity("model", "", "tokenizer", "v1")


def test_npz_and_json_round_trip_hash_and_no_overwrite(adapter, context, ids, tmp_path):
    capture = extract_prefix(adapter, ids, context)
    destination = write_capture(capture, tmp_path / "capture")
    meta = json.loads((destination / "metadata.json").read_text(encoding="utf-8"))
    assert meta["context"]["trajectory_id"] == "trajectory-1"
    assert (
        meta["artifact"]["sha256"]
        == sha256((destination / "features.npz").read_bytes()).hexdigest()
    )
    with np.load(destination / "features.npz", allow_pickle=False) as arrays:
        for key, tensor in capture.features.items():
            np.testing.assert_array_equal(arrays[key], tensor.numpy())
    with pytest.raises(FileExistsError):
        write_capture(capture, destination)
    assert "artifact" not in capture.metadata


def test_failed_write_does_not_publish_partial_capture(adapter, context, ids, tmp_path):
    capture = extract_prefix(adapter, ids, context)
    capture.metadata["invalid"] = object()
    with pytest.raises(TypeError):
        write_capture(capture, tmp_path / "capture")
    assert not list(tmp_path.iterdir())


def test_cpu_preflight_refuses_20b_load(monkeypatch):
    monkeypatch.setattr("torch.cuda.is_available", lambda: False)
    report = gpt_oss_preflight()
    assert not report["ready_for_load_attempt"]
    assert any("CUDA" in error for error in report["errors"])

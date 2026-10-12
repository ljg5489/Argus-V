"""Hook capture must preserve inference and clean up on success and exceptions."""

import json

import numpy as np
import pytest
import torch

from argus_v.activations import HookInspection


def hook_counts(model):
    return [
        (len(module._forward_pre_hooks), len(module._forward_hooks)) for module in model.modules()
    ]


def test_inspection_keeps_model_output_and_records_distinct_forwards(adapter, ids, tmp_path):
    model = adapter.model
    before = hook_counts(model)
    with torch.inference_mode():
        expected = model(input_ids=ids, use_cache=False).logits.clone()
    destination = tmp_path / "inspection"
    with HookInspection(
        adapter, destination, layers=(0, 1), include_non_block=False, show_console=False
    ) as inspection:
        with torch.inference_mode():
            first = model(input_ids=ids, use_cache=False).logits
            second = model(input_ids=ids[:, :2], use_cache=False).logits
        inspection.annotate_generated_tokens([7, 8], ["seven", "eight"], "recorded")
    assert torch.equal(first, expected)
    assert second.shape[1] == 2
    assert hook_counts(model) == before
    manifest = json.loads((destination / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["status"] == "complete"
    assert manifest["context"]["generated_token_ids"] == [7, 8]
    records = [
        json.loads(line)
        for line in (destination / "records.jsonl").read_text(encoding="utf-8").splitlines()
    ]
    assert {record["forward_call_index"] for record in records} == {0, 1}
    root_records = [
        record
        for record in records
        if record["module"] == adapter.block_paths[0]
        and record["location"] == "input.args[0]"
        and record["kind"] == "tensor"
    ]
    assert [record["shape"][1] for record in root_records] == [4, 2]
    for record in root_records:
        array = np.load(destination / record["filename"], allow_pickle=False)
        assert list(array.shape) == record["shape"]
        assert np.isfinite(array).all()
    with pytest.raises(RuntimeError, match="single-use"):
        with inspection:
            pass


def test_inspection_removes_hooks_when_forward_or_caller_fails(adapter, ids, tmp_path):
    before = hook_counts(adapter.model)
    destination = tmp_path / "failed"
    with pytest.raises(RuntimeError, match="caller failed"):
        with HookInspection(
            adapter, destination, layers=(0,), include_non_block=False, show_console=False
        ):
            with torch.inference_mode():
                adapter.model(input_ids=ids, use_cache=False)
            raise RuntimeError("caller failed")
    assert hook_counts(adapter.model) == before
    manifest = json.loads((destination / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["status"] == "failed"

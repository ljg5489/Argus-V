from dataclasses import replace

import pytest
import torch

from argus_v.activations import BlockAdapter, extract_prefix


def forward(adapter, ids):
    with torch.inference_mode():
        return adapter.model(input_ids=ids, use_cache=False, output_hidden_states=True)


def hook_counts(adapter):
    return [len(adapter.block(i)._forward_hooks) for i in range(len(adapter.block_paths))]


def test_values_match_hidden_states_before_final_norm_and_do_not_change_logits(
    adapter, context, ids
):
    before = forward(adapter, ids)
    counts = hook_counts(adapter)
    capture = extract_prefix(adapter, ids, context, token_positions=(0, 3))
    after = forward(adapter, ids)
    torch.testing.assert_close(before.logits, after.logits, rtol=0, atol=0)
    # HF hidden_states[1] is the first block output for these 2-block architectures.
    torch.testing.assert_close(capture.features["block_0000"], before.hidden_states[1][0, [0, 3]])
    final_norm = adapter.model.get_submodule(
        "transformer.ln_f" if adapter.model_type == "gpt2" else "model.norm"
    )
    with torch.inference_mode():
        normalized = final_norm(capture.features["block_0001"])
    torch.testing.assert_close(normalized, before.hidden_states[-1][0, [0, 3]])
    assert not torch.allclose(capture.features["block_0001"], normalized)
    assert hook_counts(adapter) == counts
    assert not adapter.model.training
    for feature in capture.features.values():
        assert feature.device.type == "cpu" and feature.dtype == torch.float32
        assert not feature.requires_grad and feature.shape == (2, 32)
    assert capture.metadata["alignment"][-1] == {
        "token_index": 3,
        "token_id": 4,
        "predicts_token_index": 4,
        "tokens_until_action_start": 0,
    }


def test_capture_skips_lm_head(adapter, context, ids, monkeypatch):
    def fail(*args, **kwargs):
        raise AssertionError("vocabulary logits should not be allocated for feature capture")

    monkeypatch.setattr(adapter.model.get_output_embeddings(), "forward", fail)
    assert extract_prefix(adapter, ids, context).features["block_0000"].shape == (1, 32)


def test_earlier_token_features_do_not_depend_on_later_tokens(adapter, context, ids):
    short = extract_prefix(adapter, ids[:, :3], context, token_positions=(2,))
    full = extract_prefix(adapter, ids, context, token_positions=(2,))
    for key in short.features:
        torch.testing.assert_close(short.features[key], full.features[key], rtol=1e-4, atol=1e-6)
    assert short.metadata["alignment"][0]["tokens_until_action_start"] == 1


def test_pre_execution_and_multiple_calls_have_distinct_metadata(adapter, context):
    execution = replace(context, phase="pre_execution")
    ids = torch.tensor([[1, 2, 3, 4, 20, 21, 22]])
    capture = extract_prefix(adapter, ids, execution, layers=(1,))
    assert list(capture.features) == ["block_0001"]
    assert capture.metadata["observed_prefix_length"] == 7
    assert capture.metadata["alignment"][0]["tokens_until_action_start"] == -3
    other = replace(execution, action=replace(execution.action, action_id="tool-2", step_index=1))
    second = extract_prefix(adapter, ids, other)
    assert second.metadata["context"]["action"]["action_id"] == "tool-2"
    assert capture.metadata["context"]["action"]["action_id"] == "tool-1"


@pytest.mark.parametrize(
    "kwargs",
    [
        {"layers": ()},
        {"layers": (-1,)},
        {"layers": (2,)},
        {"layers": (0, 0)},
        {"layers": (1, 0)},
        {"layers": (True,)},
        {"token_positions": ()},
        {"token_positions": (4,)},
        {"token_positions": (-1,)},
        {"token_positions": (2, 2)},
        {"token_positions": (3, 1)},
    ],
)
def test_bad_selection_fails_before_forward_without_leaking_hooks(adapter, context, ids, kwargs):
    before = hook_counts(adapter)
    with pytest.raises(ValueError):
        extract_prefix(adapter, ids, context, **kwargs)
    assert hook_counts(adapter) == before


def test_rejects_training_without_mutating_mode(adapter, context, ids):
    adapter.block(0).train()
    with pytest.raises(ValueError, match="eval"):
        extract_prefix(adapter, ids, context)
    assert adapter.block(0).training


@pytest.mark.parametrize(
    "bad",
    [
        torch.tensor([1, 2]),
        torch.ones(2, 4, dtype=torch.long),
        torch.empty(1, 0, dtype=torch.long),
        torch.ones(1, 4),
        torch.tensor([[64]]),
        torch.tensor([[-1]]),
    ],
)
def test_rejects_invalid_input(adapter, context, bad):
    with pytest.raises(ValueError):
        extract_prefix(adapter, bad, context)


def test_hooks_cleaned_on_forward_exception_and_other_hooks_preserved(adapter, context, ids):
    def fail(_module, _args, _output):
        raise RuntimeError("simulated execution error")

    existing = adapter.block(1).register_forward_hook(fail)
    counts = hook_counts(adapter)
    with pytest.raises(RuntimeError, match="simulated"):
        extract_prefix(adapter, ids, context)
    assert hook_counts(adapter) == counts
    existing.remove()
    assert extract_prefix(adapter, ids, context).features


def test_duplicate_forward_is_not_silently_overwritten(adapter, context, ids, monkeypatch):
    backbone = adapter.model.get_submodule(adapter.backbone_path)
    original = backbone.forward

    def twice(*args, **kwargs):
        original(*args, **kwargs)
        return original(*args, **kwargs)

    monkeypatch.setattr(backbone, "forward", twice)
    with pytest.raises(ValueError, match="more than once"):
        extract_prefix(adapter, ids, context)
    assert hook_counts(adapter) == [0, 0]


def test_captures_are_owned_and_do_not_change_on_subsequent_call(adapter, context, ids):
    first = extract_prefix(adapter, ids, context)
    copy = first.features["block_0000"].clone()
    extract_prefix(adapter, torch.tensor([[9, 10, 11, 12]]), context)
    torch.testing.assert_close(first.features["block_0000"], copy, rtol=0, atol=0)


def test_rejects_unknown_architecture(adapter):
    adapter.model.config.model_type = "unknown"
    with pytest.raises(ValueError, match="Unsupported"):
        BlockAdapter.from_model(adapter.model, adapter.identity)

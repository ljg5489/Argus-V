import io
import json
import tempfile
import unittest
from pathlib import Path

import numpy as np
import pytest
import torch
from torch import nn
from transformers import GptOssConfig, GptOssForCausalLM

from argus_v.activations import (
    ActionSpan,
    BlockAdapter,
    HookInspection,
    ModelIdentity,
    SnapshotContext,
    extract_prefix,
)


def tiny_adapter():
    torch.manual_seed(7)
    config = GptOssConfig(
        vocab_size=32, hidden_size=16, intermediate_size=16, num_hidden_layers=2,
        num_attention_heads=2, num_key_value_heads=1, head_dim=8,
        num_local_experts=4, num_experts_per_tok=2, max_position_embeddings=64,
        sliding_window=8, rope_scaling=None,
    )
    config._attn_implementation = "eager"
    config._experts_implementation = "eager"
    # Transformers 5.x uses rope_parameters; older versions ignore this field.
    config.rope_parameters = {"rope_type": "default", "rope_theta": 10000.0}
    model = GptOssForCausalLM(config).eval()
    return BlockAdapter.from_model(model, ModelIdentity("tiny", "seed-7", "synthetic", "v1"))


def records(root):
    return [json.loads(line) for line in (root / "records.jsonl").read_text().splitlines()]


def tensor(root, module, location, call=0):
    match = [row for row in records(root) if row["module"] == module and
             row["location"] == location and row["call_index"] == call]
    assert len(match) == 1, (module, location, call, match)
    return np.load(root / match[0]["filename"], allow_pickle=False)


def hook_counts(model):
    return [(len(m._forward_pre_hooks), len(m._forward_hooks)) for m in model.modules()]


class HookInspectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        torch.set_num_threads(1)

    def setUp(self):
        self.adapter = tiny_adapter()
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / "trace"
        self.ids = torch.tensor([[1, 2, 3]])

    def trace(self, **kwargs):
        return HookInspection(self.adapter, self.root, stream=io.StringIO(), **kwargs)

    def test_all_submodules_tuples_and_residual_identity_without_output_change(self):
        model = self.adapter.model
        with torch.inference_mode():
            baseline = model(input_ids=self.ids, use_cache=False).logits.clone()
            before = hook_counts(model)
            with self.trace():
                output = model(input_ids=self.ids, use_cache=False).logits
        torch.testing.assert_close(output, baseline, rtol=0, atol=0)
        self.assertEqual(hook_counts(model), before)
        for layer in (0, 1):
            prefix = f"model.layers.{layer}"
            mlp = tensor(self.root, prefix + ".mlp", "output[0]")
            residual = tensor(self.root, prefix + ".post_attention_layernorm", "input.args[0]")
            block = tensor(self.root, prefix, "output")
            np.testing.assert_allclose(block, residual + mlp, rtol=1e-6, atol=1e-6)
            for projection in ("q_proj", "k_proj", "v_proj", "o_proj"):
                self.assertTrue(tensor(self.root, prefix + ".self_attn." + projection, "output").size)
            router = [r for r in records(self.root) if r["module"] == prefix + ".mlp.router" and r["location"].startswith("output")]
            self.assertEqual(len(router), 3)
            integer_leaves = [r for r in router if r["storage_dtype"].startswith("int")]
            self.assertEqual(len(integer_leaves), 1)
        np.testing.assert_array_equal(tensor(self.root, "lm_head", "output"), output.numpy())
        self.assertTrue((self.root / "summary.md").exists())

    def test_same_replay_as_c01_and_no_lm_head_claim(self):
        context = SnapshotContext("r", "t", "s", "pre_action", ActionSpan("a", 0, 3, None))
        with self.trace():
            capture = extract_prefix(self.adapter, self.ids, context)
        for index in range(2):
            block = tensor(self.root, f"model.layers.{index}", "output")
            np.testing.assert_array_equal(block[0, -1:], capture.features[f"block_{index:04d}"].numpy())
        manifest = json.loads((self.root / "manifest.json").read_text())
        head = next(m for m in manifest["modules"] if m["path"] == "lm_head")
        self.assertEqual(head["status"], "not_called")

    def test_cached_generation_calls_are_not_concatenated(self):
        model = self.adapter.model
        inspector = self.trace(phase="generation", context={"input_ids": [1, 2, 3],
                                                             "token_pieces": ["a", "b", "c"]})
        with inspector, torch.inference_mode():
            first = model(input_ids=self.ids, use_cache=True)
            model(input_ids=torch.tensor([[4]]), past_key_values=first.past_key_values, use_cache=True)
            inspector.annotate_generated_tokens([5, 6], ["target-1", "target-2"])
        self.assertEqual(tensor(self.root, "model.layers.0.mlp", "output[0]", 0).shape, (1, 3, 16))
        self.assertEqual(tensor(self.root, "model.layers.0.mlp", "output[0]", 1).shape, (1, 1, 16))
        self.assertTrue(any(r.get("python_type") == "DynamicCache" for r in records(self.root)))
        layer_outputs = [row for row in records(self.root)
                         if row["module"] == "model.layers.0" and row["location"] == "output"]
        self.assertEqual([row["forward_call_index"] for row in layer_outputs], [0, 1])
        manifest = json.loads((self.root / "manifest.json").read_text())
        mapping = manifest["context"]["generation_token_map"]
        self.assertEqual(mapping[0]["generated_token_piece"], "target-1")
        self.assertEqual(mapping[0]["source_token_piece"], "c")
        self.assertEqual(mapping[1]["source_token_piece"], "target-1")

    def test_selected_layers_and_no_overwrite(self):
        with self.trace(layers=(1,)), torch.inference_mode():
            self.adapter.model(input_ids=self.ids, use_cache=False)
        self.assertFalse(any(r["layer_index"] == 0 for r in records(self.root)))
        self.assertTrue(any(r["layer_index"] == 1 for r in records(self.root)))
        with self.assertRaises(FileExistsError), self.trace():
            pass
        for layers in ((1, 0), (0, 0), (9,), ()):
            with self.assertRaises(ValueError):
                self.trace(layers=layers)

    def test_model_failure_leaves_report_and_removes_only_own_hooks(self):
        model = self.adapter.model
        external = model.model.layers[0].register_forward_hook(lambda *args: None)
        self.addCleanup(external.remove)
        before = hook_counts(model)
        with self.assertRaisesRegex(RuntimeError, "test failure"):
            with self.trace():
                raise RuntimeError("test failure")
        self.assertEqual(hook_counts(model), before)
        manifest = json.loads((self.root / "manifest.json").read_text())
        self.assertEqual(manifest["status"], "failed")

    def test_full_text_has_all_values_and_nested_non_tensor_records(self):
        class Nested(nn.Module):
            def forward(self, x, *, scale):
                return {"pair": (x * scale, None), "ids": [torch.tensor([2**54], dtype=torch.int64)]}
        self.adapter.model.extra = Nested()
        output = io.StringIO()
        with HookInspection(self.adapter, self.root, values="full", stream=output):
            self.adapter.model.extra(torch.arange(20, dtype=torch.float32), scale=2)
        actual = tensor(self.root, "extra", "output['pair'][0]")
        np.testing.assert_array_equal(actual, np.arange(20) * 2)
        self.assertEqual(tensor(self.root, "extra", "output['ids'][0]").item(), 2**54)
        self.assertTrue(any(r.get("value", "absent") is None for r in records(self.root)))
        values = (self.root / "values.txt").read_text()
        self.assertIn("[16:20] 32.0 34.0 36.0 38.0", values)
        self.assertNotIn("...", values)
        self.assertIn("[16:20] 32.0 34.0 36.0 38.0", output.getvalue())

    def test_bfloat16_nonfinite_empty_and_input_mutation(self):
        class Mutating(nn.Module):
            def forward(self, x):
                x.add_(1)
                return (x.to(torch.bfloat16), torch.tensor([float("nan"), float("inf"), -float("inf")]), torch.empty(0))
        self.adapter.model.extra = Mutating()
        with self.trace():
            self.adapter.model.extra(torch.tensor([1., 2.]))
        np.testing.assert_array_equal(tensor(self.root, "extra", "input.args[0]"), [1, 2])
        np.testing.assert_array_equal(tensor(self.root, "extra", "output[0]"), [2, 3])
        found = [r for r in records(self.root) if r["location"] == "output[1]"][0]
        self.assertEqual(found["statistics"]["finite_count"], 0)
        self.assertEqual(found["statistics"]["nan_count"], 1)
        self.assertIsNone(found["statistics"]["mean"])
        self.assertEqual(tensor(self.root, "extra", "output[2]").size, 0)

    def test_hook_capture_failure_still_cleans_up(self):
        from unittest.mock import patch
        before = hook_counts(self.adapter.model)
        with patch("numpy.save", side_effect=OSError("disk full")):
            with self.assertRaisesRegex(OSError, "disk full"), self.trace():
                self.adapter.model(input_ids=self.ids, use_cache=False)
        self.assertEqual(hook_counts(self.adapter.model), before)
        self.assertEqual(json.loads((self.root / "manifest.json").read_text())["status"], "failed")


# Inference preservation and hook cleanup with the shared conftest fixtures (pytest).
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


if __name__ == "__main__":
    unittest.main()

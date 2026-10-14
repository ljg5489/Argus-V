"""Hook map metadata tests; no model, container, or tensor arrays are needed."""

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock

from Research.hidden_state_dashboard import (
    PAGE,
    ArtifactIndex,
    CaptureIndex,
    DashboardHandler,
    LogitLens,
    RolloutIndex,
)


class HookMapTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        root = Path(self.temp.name)
        self.data = root / "data"
        self.folder = self.data / "run-one" / "step_001" / "hook_inspection"
        self.folder.mkdir(parents=True)
        self.manifest = {
            "schema_version": "argus-v.hook-inspection.v1", "status": "complete",
            "phase": "pre_action_full_prefix_replay", "selected_layers": [0, 11, 23],
            "started_at": "2026-10-12T10:00:00+00:00", "context": {"task_text": "read JSON"},
            "model_type": "gpt_oss", "identity": {"model_id": "test-model"},
            "modules": [
                {"path": "model.layers.0", "class": "Decoder", "layer": 0, "calls": 1},
                {"path": "model.layers.0.self_attn", "class": "Attention", "layer": 0, "calls": 1},
                {"path": "model.layers.0.mlp.router", "class": "Router", "layer": 0, "calls": 0},
                {"path": "lm_head", "class": "Linear", "layer": None, "calls": 0},
            ],
        }
        self.write_manifest()
        records = []
        for index, (location, shape) in enumerate([
            ("input.args[0]", [1, 10, 32]), ("output", [1, 10, 32]),
            ("output", [1, 1, 32]),
        ]):
            records.append({"record_id": index, "module": "model.layers.0",
                            "layer_index": 0, "call_index": 0 if index < 2 else 1,
                            "location": location, "kind": "tensor", "shape": shape,
                            "source_dtype": "torch.float32", "phase": self.manifest["phase"]})
        (self.folder / "records.jsonl").write_text(
            "".join(json.dumps(record) + "\n" for record in records))
        self.store = ArtifactIndex(self.data, root / "index.sqlite3")
        self.store.sync_once()
        self.session_id = self.store.hook_sessions("", 0, 50)["sessions"][0]["id"]

    def write_manifest(self):
        (self.folder / "manifest.json").write_text(json.dumps(self.manifest))

    def test_registered_uncalled_modules_and_hierarchy_are_preserved(self):
        result = self.store.hook_map(self.session_id)
        modules = {node["path"]: node for node in result["modules"]}
        self.assertEqual(result["totals"]["registered"], 4)
        self.assertEqual(result["totals"]["called"], 2)
        self.assertEqual(modules["model.layers.0.mlp.router"]["parent"], "model.layers.0")
        self.assertEqual(modules["lm_head"]["status"], "not_called")
        self.assertEqual(modules["lm_head"]["records"], 0)

    def test_latest_shapes_and_live_records_supplement_stale_manifest(self):
        result = self.store.hook_map(self.session_id)
        block = result["modules"][0]
        self.assertEqual(block["calls"], 2)
        self.assertEqual(block["inputs"], 1)
        self.assertEqual(block["outputs"], 2)
        self.assertEqual(len(block["samples"]), 2)
        output = next(s for s in block["samples"] if s["location"] == "output")
        self.assertEqual(output["shape"], [1, 1, 32])
        self.manifest["status"] = "running"
        self.write_manifest()
        result = self.store.hook_map(self.session_id)
        self.assertEqual(result["modules"][2]["status"], "pending")

    def test_search_pagination_and_missing_manifest(self):
        self.assertEqual(self.store.hook_sessions("read JSON", 0, 1)["total"], 1)
        self.assertEqual(self.store.hook_sessions("missing", 0, 1)["total"], 0)
        self.assertEqual(self.store.hook_sessions("", 1, 1)["sessions"], [])
        (self.folder / "manifest.json").unlink()
        with self.assertRaises(FileNotFoundError):
            self.store.hook_map(self.session_id)

    def test_artifact_escape_is_rejected(self):
        with self.store.connect() as db:
            db.execute("UPDATE sessions SET artifact_dir='../outside' WHERE id=?", (self.session_id,))
        with self.assertRaisesRegex(ValueError, "Invalid artifact"):
            self.store.hook_map(self.session_id)

    def test_routes_and_existing_page_controls(self):
        handler = object.__new__(DashboardHandler)
        handler.store = self.store
        handler._json = Mock()
        handler._send = Mock()
        handler.path = f"/api/hooks/map?session={self.session_id}"
        handler.do_GET()
        self.assertEqual(handler._json.call_args.args[0]["totals"]["registered"], 4)
        handler.path = "/api/hooks/map?session=invalid"
        handler.do_GET()
        self.assertEqual(handler._json.call_args.args[1], 400)
        handler.path = "/hooks"
        handler.do_GET()
        self.assertEqual(handler._send.call_args.args[0], PAGE.encode())
        for name in ("view-analysis", "view-compare", "view-sandbox", "view-hooks",
                     "sandbox-import", "sandbox-preview", "sandbox-image", "theme-toggle"):
            self.assertIn(f'id="{name}"', PAGE)


class RolloutViewTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "rollouts"
        folder = self.root / "AV-S01-C2-s0-abcd1234"
        (folder / "steps" / "step_000").mkdir(parents=True)
        (folder / "rollout.json").write_text(json.dumps({
            "kind": "suite", "scenario_key": "AV-S01/C2", "scenario_id": "AV-S01", "condition": "C2", "seed": 0,
            "task": "goal", "started_at": 1791800000.0, "termination": "submitted",
            "report": {"actions": 1, "violations": 1, "unlabelled": 0, "first_violation_step": 0},
            "operator_report": {"business_completed": False, "violation_attempts": 1, "violation_executed": 0},
            "steps": [{"step_index": 0, "kind": "tool", "command": "{}", "policy_label": 1}]}))
        (folder / "steps" / "step_000" / "step.json").write_text(json.dumps({
            "step_index": 0, "kind": "tool", "command": "{}", "policy_label": 1,
            "input_messages": [{"role": "system", "content": "rules"}, {"role": "user", "content": "goal"}],
            "output": {"reasoning": "think", "action_text": "```tool\n{}\n```"}, "observation": "{}"}))
        (folder / "transcript.md").write_text("# AV-S01/C2")
        (self.root / "partial").mkdir()
        self.handler = object.__new__(DashboardHandler)
        self.handler.rollouts = RolloutIndex(self.root)
        self.handler._json = Mock()
        self.handler._send = Mock()

    def get(self, path):
        self.handler.path = path
        self.handler.do_GET()
        return self.handler._json.call_args.args if self.handler._json.called else None

    def test_list_detail_transcript_and_escape(self):
        (entry,) = self.get("/api/rollouts/list")[0]["rollouts"]
        self.assertEqual((entry["scenario_key"], entry["violations"], entry["business_completed"]), ("AV-S01/C2", 1, False))
        detail = self.get("/api/rollouts/detail?id=AV-S01-C2-s0-abcd1234")[0]
        step = detail["steps"][0]
        self.assertEqual(step["input_messages"][1]["content"], "goal")
        self.assertEqual(step["output"]["reasoning"], "think")
        self.assertIsNone(step["capture_id"])  # no capture folder in this fixture
        self.handler.path = "/api/rollouts/transcript?id=AV-S01-C2-s0-abcd1234"
        self.handler.do_GET()
        self.assertEqual(self.handler._send.call_args.args[0], "# AV-S01/C2".encode())
        for bad in ("../rollouts", "partial", "AV-S01-C2-s0-abcd1234/steps"):
            self.handler._json.reset_mock()
            self.assertEqual(self.get(f"/api/rollouts/detail?id={bad}")[1], 400)
        self.assertIn('id="view-rollouts"', PAGE)

    def test_scenario_hidden_endpoints_without_capture(self):
        trend = self.get("/api/rollouts/trend?id=AV-S01-C2-s0-abcd1234")[0]
        self.assertEqual([step["step_index"] for step in trend["steps"]], [0])
        self.assertEqual(trend["layers"], [])  # this fixture step has no capture folder
        self.handler._json.reset_mock()
        self.assertEqual(self.get("/api/rollouts/hidden?id=AV-S01-C2-s0-abcd1234&step=0")[1], 400)
        self.handler._json.reset_mock()
        self.assertEqual(self.get("/api/rollouts/vector?id=../x&step=0&point=0&layer=0")[1], 400)
        self.assertIn('id="view-scenario-hidden"', PAGE)


class CaptureViewTests(unittest.TestCase):
    """Teammate C-01 captures and their cross-check against generation Hook records."""

    def setUp(self):
        import hashlib

        import numpy as np

        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        root = Path(self.temp.name)
        session = root / "data" / "run-x" / "task_001_seed_42_step_001" / "generation" / "attempt_001"
        (session / "tensors").mkdir(parents=True)
        prefill = np.arange(12, dtype=np.float32).reshape(1, 3, 4)
        self.decode = np.array([[[1.0, -2.0, 3.0, -4.0]]], dtype=np.float32)
        np.save(session / "tensors" / "0.npy", prefill)
        np.save(session / "tensors" / "1.npy", self.decode)
        token_map = [{"generated_token_index": 0, "generated_token_id": 4, "generated_token_piece": "Ġhi"},
                     {"generated_token_index": 1, "generated_token_id": 5, "generated_token_piece": "ìķĪ"}]
        (session / "manifest.json").write_text(json.dumps({
            "status": "complete", "phase": "generation", "started_at": "2026-10-12T10:00:00+00:00",
            "context": {"run_id": "run-x", "input_ids": [1, 2, 3], "generated_token_ids": [4, 5],
                        "generation_token_map": token_map}}))
        records = [{"record_id": index, "module": "model.layers.0", "layer_index": 0, "call_index": index,
                    "forward_call_index": index, "location": "output", "kind": "tensor",
                    "shape": list(array.shape), "filename": f"tensors/{index}.npy"}
                   for index, array in enumerate((prefill, self.decode))]
        (session / "records.jsonl").write_text("".join(json.dumps(record) + "\n" for record in records))
        self.store = ArtifactIndex(root / "data", root / "index.sqlite3")
        self.store.sync_once()

        self.artifacts = root / "artifacts"
        capture = self.artifacts / "run-cap" / "capture"
        capture.mkdir(parents=True)
        np.savez(capture / "features.npz", block_0000=self.decode.reshape(1, 4))
        prefix = [1, 2, 3, 4]
        self.metadata = {
            "context": {"run_id": "run-cap", "scenario_id": "smoke", "phase": "pre_action",
                        "action": {"action_id": "execute_bash", "token_start": 4, "token_end": 5}},
            "capture_mode": "full_prefix_replay", "hook_point": "post_block_pre_final_norm",
            "observed_prefix_length": 4,
            "prefix_ids_sha256": hashlib.sha256(json.dumps(prefix, separators=(",", ":")).encode()).hexdigest(),
            "alignment": [{"token_index": 3, "token_id": 4, "predicts_token_index": 4}],
            "blocks": [{"key": "block_0000", "layer_index": 0, "module_path": "model.layers.0", "shape": [1, 4]}],
            "artifact": {"filename": "features.npz"}}
        (capture / "metadata.json").write_text(json.dumps(self.metadata))
        (capture.parent / "agent-generation.json").write_text(json.dumps({
            "input_ids": prefix + [9], "token_pieces": ["a", "b", "c", "Ġhi", "x"], "task": "smoke task"}))
        (capture.parent / "m1-result.json").write_text(json.dumps({
            "configuration": {"monitor": "M1"}, "snapshot": {"run_id": "run-cap"},
            "status": "ok", "risk_score": 0.1, "alarm": False, "reason": "fine"}))
        self.handler = object.__new__(DashboardHandler)
        self.handler.store = self.store
        self.handler.captures = CaptureIndex(self.artifacts)
        self.handler._json = Mock()

    def get(self, path):
        self.handler.path = path
        self.handler.do_GET()
        return self.handler._json.call_args.args

    def test_list_verifies_prefix_and_reads_verdict(self):
        (entry,) = self.get("/api/captures/list")[0]["captures"]
        self.assertEqual(entry["id"], "run-cap")
        self.assertTrue(entry["prefix_verified"])
        self.assertEqual(entry["observed_token"]["text"], " hi")
        self.assertIs(entry["m1"]["alarm"], False)

    def test_detail_matches_generation_forward_at_same_position(self):
        detail = self.get("/api/captures/detail?id=run-cap")[0]
        (match,) = detail["matches"]
        self.assertEqual((match["mode"], match["forward_call_index"], match["position"]), ("generation", 1, 3))
        self.assertEqual(match["generated_text"], "안")
        (layer,) = match["layers"]
        self.assertAlmostEqual(layer["cosine"], 1.0)
        self.assertEqual(layer["rel_l2"], 0.0)
        self.assertEqual(detail["spans"]["observed"], 3)
        self.assertEqual(detail["layers"][0]["numel"], 4)

    def test_tampered_prefix_and_path_escape(self):
        self.metadata["prefix_ids_sha256"] = "0" * 64
        (self.artifacts / "run-cap" / "capture" / "metadata.json").write_text(json.dumps(self.metadata))
        self.assertFalse(self.get("/api/captures/list")[0]["captures"][0]["prefix_verified"])
        self.assertEqual(self.get("/api/captures/detail?id=../data")[1], 400)
        for name in ("view-captures", "view-tokens", "cap-matches"):
            self.assertIn(f'id="{name}"', PAGE)

    def test_vocab_projection_matches_norm_then_lm_head(self):
        import numpy as np

        model = Path(self.temp.name) / "model"
        model.mkdir()
        head = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [1, 1, 1, 1]], dtype=np.float32)
        norm = np.array([1.0, 0.5, 2.0, 1.0], dtype=np.float32)
        tensors = {"lm_head.weight": head, "model.norm.weight": norm}
        header, blobs, offset = {}, [], 0
        for name, array in tensors.items():
            blob = (array.view(np.uint32) >> 16).astype("<u2").tobytes()  # exact for these values
            header[name] = {"dtype": "BF16", "shape": list(array.shape), "data_offsets": [offset, offset + len(blob)]}
            blobs.append(blob)
            offset += len(blob)
        encoded = json.dumps(header).encode()
        (model / "weights.safetensors").write_bytes(len(encoded).to_bytes(8, "little") + encoded + b"".join(blobs))
        (model / "model.safetensors.index.json").write_text(json.dumps(
            {"weight_map": {name: "weights.safetensors" for name in tensors}}))
        (model / "config.json").write_text(json.dumps({"rms_norm_eps": 1e-5, "num_hidden_layers": 1}))
        (model / "tokenizer.json").write_text(json.dumps({
            "model": {"vocab": {"a": 0, "Ġb": 1, "ìķĪ": 2, "d": 3}}, "added_tokens": []}))
        self.handler.lens = LogitLens(model, model / "tokenizer.json")

        hidden = self.decode.reshape(-1)
        expected = head @ (hidden / np.sqrt(np.mean(hidden * hidden) + 1e-5) * norm)
        from urllib.parse import quote

        key = quote("run-x/task_001_seed_42_step_001/generation/attempt_001#1")
        session = self.store.token_sessions("", 0, 10)["sessions"][0]["id"]
        result = self.get(f"/api/tokens/vocab?session={session}&key={key}&limit=5")[0]
        self.assertEqual(result["vocab_size"], 5)
        self.assertTrue(result["is_model_output"])  # last (only) layer block output
        ranked = [row["id"] for row in result["rows"]]
        self.assertEqual(ranked, list(np.argsort(-expected, kind="stable")))
        np.testing.assert_allclose([row["logit"] for row in result["rows"]], np.sort(expected)[::-1], rtol=1e-6)
        self.assertAlmostEqual(sum(row["prob"] for row in result["rows"]), 1.0, places=6)
        self.assertNotIn("generated", result["marks"])  # generated ID 5 is outside this 5-token vocab
        self.assertEqual(next(row for row in result["rows"] if row["id"] == 2)["text"], "안")
        self.assertIsNone(next(row for row in result["rows"] if row["id"] == 4)["text"])
        searched = self.get(f"/api/tokens/vocab?session={session}&key={key}&q=b")[0]["rows"]
        self.assertEqual([row["id"] for row in searched], [1])
        self.assertEqual(self.get(f"/api/tokens/vocab?session={session}&key=other%230")[1], 400)

    def test_generation_token_axis_uses_forward_input_length(self):
        context = {"input_ids": [1, 2, 3], "generation_token_map": [{}, {}]}
        decode = ArtifactIndex._apply_token_mapping({"forward_call_index": 1, "shape": [1, 32]}, context)
        prefill = ArtifactIndex._apply_token_mapping({"forward_call_index": 0, "shape": [1, 3, 4]}, context)
        experts = ArtifactIndex._apply_token_mapping({"forward_call_index": 0, "shape": [3, 32]}, context)
        self.assertEqual((decode["generation_sequence_axis"], decode["generation_source_position"]), (0, 0))
        self.assertEqual((prefill["generation_sequence_axis"], prefill["generation_source_position"]), (1, 2))
        self.assertEqual((experts["generation_sequence_axis"], experts["generation_source_position"]), (0, 2))


if __name__ == "__main__":
    unittest.main()

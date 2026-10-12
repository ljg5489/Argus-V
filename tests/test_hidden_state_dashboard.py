"""Hook map metadata tests; no model, container, or tensor arrays are needed."""

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock

from Research.hidden_state_dashboard import ArtifactIndex, DashboardHandler, PAGE


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


if __name__ == "__main__":
    unittest.main()

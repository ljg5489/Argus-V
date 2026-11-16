"""CPU tests; no project data, network, model downloads, or disk artifacts."""
from __future__ import annotations

from dataclasses import replace
import io
import sys
import types
import unittest
from unittest.mock import patch

import numpy as np
import torch

from experiments.residual_probes.shared import (
    ARCHITECTURES, Config, checked_xy, fit_scaler, make_model, transform,
)
from experiments.residual_probes.training import (
    checkpoint_payload, dataset_digest, fit_model, grouped_folds, load_training_data,
    merge_groups, parser_for, predict_model, ranking_metrics, restore_checkpoint,
    run_nested, sample_fit_rows,
)
from experiments.residual_probes.preactivation_mlp.model import PreActivationBlock
from experiments.residual_probes.residual_mlp.model import ResidualBlock
from experiments.residual_probes.stochastic_depth_mlp.model import StochasticDepthBlock


class ResidualProbeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        torch.set_num_threads(2)

    def config(self, arch="preactivation_mlp", **kw):
        return replace(Config(architecture=arch, width=8, blocks=2, dropout=0,
                              drop_path=0.2 if arch == "stochastic_depth_mlp" else 0,
                              epochs=5, patience=2, outer_folds=3, inner_folds=2,
                              normal_ratio=0, pos_weight=1), **kw)

    def data(self):
        rng = np.random.default_rng(4)
        x = rng.normal(size=(72, 6)).astype(np.float32)
        y = np.tile([0, 1, 0, 1, 0, 1], 12)
        x[:, 0] += 2 * y - 1
        return x, y, np.repeat(np.arange(12), 6), np.full(72, "read_file|nov")

    def test_all_architectures_widths_shapes_and_gradients(self):
        for arch in ARCHITECTURES:
            for width in (32, 64, 128):
                with self.subTest(arch=arch, width=width):
                    model = make_model(18, self.config(arch, width=width))
                    x = torch.randn(5, 18, requires_grad=True)
                    logits = model(x)
                    self.assertEqual(tuple(logits.shape), (5,))
                    torch.nn.functional.binary_cross_entropy_with_logits(
                        logits, torch.tensor([0., 1., 0., 1., 1.])).backward()
                    self.assertTrue(torch.isfinite(x.grad).all())
                    self.assertTrue(all(p.grad is not None and torch.isfinite(p.grad).all()
                                        for p in model.parameters()))

    def test_preactivation_keeps_negative_identity(self):
        block = PreActivationBlock(4, dropout=0).eval()
        for p in block.branch.parameters():
            torch.nn.init.zeros_(p)
        x = torch.tensor([[-5., -1., 0., 2.]])
        torch.testing.assert_close(block(x), x)

    def test_postactivation_is_distinct(self):
        block = ResidualBlock(4, dropout=0).eval()
        for p in block.branch.parameters():
            torch.nn.init.zeros_(p)
        x = torch.tensor([[-5., -1., 0., 2.]])
        torch.testing.assert_close(block(x), torch.nn.functional.gelu(x))
        self.assertFalse(torch.equal(block(x), x))

    def test_stochastic_depth_scaling_and_eval(self):
        class Ones(torch.nn.Module):
            def forward(self, x):
                return torch.ones_like(x)
        block = StochasticDepthBlock(4, dropout=0, drop_probability=0.5)
        block.branch = Ones()
        x = torch.full((4096, 4), -3.)
        block.train()
        delta = block(x) - x
        self.assertEqual(set(delta.unique().tolist()), {0., 2.})
        self.assertLess(abs(float(delta.mean()) - 1.), 0.06)
        self.assertTrue(torch.equal(delta[:, :1].expand_as(delta), delta))
        block.eval()
        torch.testing.assert_close(block(x), x + 1)
        torch.testing.assert_close(block(x), block(x))

    def test_zero_drop_path_matches_preactivation(self):
        a = PreActivationBlock(5, dropout=0)
        b = StochasticDepthBlock(5, dropout=0, drop_probability=0)
        b.load_state_dict(a.state_dict())
        x = torch.randn(10, 5)
        torch.testing.assert_close(a(x), b(x))

    def test_config_rejects_invalid_options(self):
        for kw in ({"width": 0}, {"blocks": 0}, {"pos_weight": 0},
                   {"pos_weight": float("nan")}, {"drop_path": 1},
                   {"architecture": "residual_mlp", "drop_path": 0.1},
                   {"outer_folds": 1}, {"target": "unknown"}):
            with self.subTest(kw=kw), self.assertRaises(ValueError):
                Config(**kw)

    def test_finite_binary_feature_contract(self):
        for x, y in (([[float("nan")]], [0]), ([[1.]], [None]),
                     ([[1.]], [2]), ([[1.], [2.]], [0])):
            with self.subTest(x=x, y=y), self.assertRaises(ValueError):
                checked_xy(x, y)

    def test_scaler_fits_only_supplied_rows(self):
        train = np.array([[1., 7.], [3., 7.]], dtype=np.float32)
        med, scale = fit_scaler(train)
        np.testing.assert_array_equal(med, [2., 7.])
        np.testing.assert_array_equal(scale, [1., 1.])
        np.testing.assert_array_equal(transform(np.array([[999., 7.]]), med, scale), [[5., 0.]])
        with self.assertRaises(ValueError):
            transform(np.ones((2, 3)), med, scale)

    def test_connected_clone_groups_do_not_leak(self):
        groups = merge_groups(["A", "A", "B", "C", "D", "E"], ["h1", "h2", "h2", "h3", "h4", "h5"])
        self.assertEqual(groups[0], groups[2])
        x, y, groups, _ = self.data()
        for a, b in grouped_folds(y, groups, 3, 0):
            self.assertFalse(set(groups[a]) & set(groups[b]))
        with self.assertRaises(ValueError):
            grouped_folds(y, np.zeros(len(y)), 3, 0)

    def test_sampling_retains_all_positives_and_is_reproducible(self):
        y = np.r_[np.ones(2, dtype=int), np.zeros(200, dtype=int)]
        cells = np.full(len(y), "cell")
        cfg = self.config(normal_ratio=3, min_normals=0)
        a = sample_fit_rows(y, cells, cfg, 7)
        self.assertEqual(len(a), 8)
        self.assertTrue({0, 1}.issubset(set(a)))
        np.testing.assert_array_equal(a, sample_fit_rows(y, cells, cfg, 7))
        np.testing.assert_array_equal(sample_fit_rows(y, cells, replace(cfg, normal_ratio=0), 7),
                                      np.arange(len(y)))

    def test_explicit_risk_weights_reach_training(self):
        x, y, _, _ = self.data()
        seen = []
        original = torch.nn.BCEWithLogitsLoss
        def factory(*a, **kw):
            seen.append(float(kw["pos_weight"]))
            return original(*a, **kw)
        with patch("torch.nn.BCEWithLogitsLoss", side_effect=factory):
            for weight in (15., 60., 230.):
                fit_model(x, y, self.config(epochs=1, pos_weight=weight), 0)
        self.assertEqual(seen, [15., 60., 230.])

    def test_checkpoint_roundtrip_each_architecture(self):
        x, y, _, _ = self.data()
        for arch in ARCHITECTURES:
            with self.subTest(arch=arch):
                cfg = self.config(arch)
                model, med, scale, _ = fit_model(x, y, cfg, 7)
                before = predict_model(model, x, med, scale)
                payload = checkpoint_payload(model, med, scale, cfg, "test-only", 5)
                handle = io.BytesIO()
                torch.save(payload, handle)
                handle.seek(0)
                restored = torch.load(handle, map_location="cpu", weights_only=True)
                after_model, after_med, after_scale = restore_checkpoint(restored)
                np.testing.assert_allclose(before, predict_model(after_model, x, after_med, after_scale),
                                           rtol=0, atol=1e-6)
                self.assertFalse(after_model.training)
                restored["feature_spec"] = ["wrong"]
                with self.assertRaises(ValueError):
                    restore_checkpoint(restored)

    def test_reproducible_fit(self):
        x, y, _, _ = self.data()
        cfg = self.config("stochastic_depth_mlp")
        a, med, scale, _ = fit_model(x, y, cfg, 11)
        b, med2, scale2, _ = fit_model(x, y, cfg, 11)
        np.testing.assert_array_equal(predict_model(a, x, med, scale),
                                      predict_model(b, x, med2, scale2))

    def test_nested_epoch_selection_excludes_outer_score_rows(self):
        x, y, groups, cells = self.data()
        ids = np.arange(len(y)) + 100
        results, oof, epoch = run_nested(x, y, groups, cells, ids, self.config(), [0])
        self.assertEqual(oof.shape, (1, len(y)))
        self.assertTrue(np.isfinite(oof).all())
        self.assertTrue(1 <= epoch <= 5)
        held_out = []
        for fold in results[0]["folds"]:
            a = set(fold["inner_fit_row_ids"])
            v = set(fold["inner_selection_row_ids"])
            b = set(fold["outer_score_row_ids"])
            self.assertFalse(a & v or a & b or v & b)
            self.assertFalse(set(fold["outer_fit_row_ids"]) & b)
            held_out.extend(b)
        self.assertEqual(sorted(held_out), ids.tolist())

    def test_metric_population_and_identity_change_with_settings(self):
        x, y, groups, cells = self.data()
        result = ranking_metrics(y, y.astype(float), cells)
        self.assertEqual(result["auroc"], 1)
        self.assertEqual(result["within_tool_source_auroc"], 1)
        self.assertEqual(result["eligible_positives"], int(y.sum()))
        h = dataset_digest(x, y, groups, np.arange(len(y)), cells)
        x2 = x.copy()
        x2[0, 0] += 1
        self.assertNotEqual(h, dataset_digest(x2, y, groups, np.arange(len(y)), cells))

    def test_three_entrypoint_defaults(self):
        for arch in ARCHITECTURES:
            args = parser_for(arch).parse_args([])
            self.assertEqual(args.epochs, 300)
            self.assertEqual(args.pos_weight, 15)
            self.assertEqual(args.blocks, 8 if arch == "stochastic_depth_mlp" else 4)

    def test_loader_refuses_nontrain_and_documents_target(self):
        n = 6
        cx = types.SimpleNamespace(
            rows=types.SimpleNamespace(split=np.full(n, "train"), row_id=np.arange(n),
                                      label_status=np.full(n, "reviewed")),
            feats={"L23:max": np.ones((n, 2)), "L16:pre": np.ones((n, 2)) * 2},
            y=np.array([0, 1, 0, 1, 0, 1]), hashes=np.asarray(list("abcdef")),
            groups=np.full(n, "tool|source"), src=np.full(n, "nov"),
        )
        upstream = types.ModuleType("experiments.risk_loop.argus_loop.argus_v_em")
        upstream.Ctx = lambda: cx
        upstream.visible_mask = lambda _: (np.array([False, True, False, False, False, False]), "test-rule")
        evaluation = types.ModuleType("experiments.risk_loop.argus_loop.evaluate")
        evaluation.group_components = lambda _: np.arange(n)
        evaluation.evaluate_sha256 = lambda: "synthetic-test-only"
        package = types.ModuleType("experiments.risk_loop.argus_loop")
        package.__path__ = []
        package.argus_v_em, package.evaluate = upstream, evaluation
        modules = {
            "experiments.risk_loop": types.ModuleType("experiments.risk_loop"),
            "experiments.risk_loop.argus_loop": package,
            upstream.__name__: upstream, evaluation.__name__: evaluation,
        }
        with patch.dict(sys.modules, modules):
            all_data = load_training_data(self.config())
            self.assertEqual(len(all_data["y"]), 6)
            np.testing.assert_array_equal(all_data["x"][0], [1, 1, 2, 2])
            visible = load_training_data(self.config(target="visible"))
            self.assertEqual(visible["row_ids"].tolist(), [0, 1, 2, 4])
            self.assertEqual(visible["visible_rule"], "test-rule")
            cx.rows.split[0] = "test"
            with self.assertRaises(PermissionError):
                load_training_data(self.config())


    def test_main_completes_all_three_models_without_filesystem_artifacts(self):
        from pathlib import Path
        from experiments.residual_probes import training
        x, y, groups, cells = self.data()
        data = {
            "x": x, "y": y, "groups": groups, "cells": cells,
            "row_ids": np.arange(len(y)), "source": np.full(len(y), "nov"),
            "label_status": {"synthetic": len(y)}, "visible_rule": None,
            "excluded_rows": 0, "evaluation_sha256": "synthetic-only",
        }
        original_save = torch.save
        for arch in ARCHITECTURES:
            written, models, archives = {}, [], []
            def write_text(path, text, **kwargs):
                written[path.name] = text
                return len(text)
            def save(payload, path):
                handle = io.BytesIO()
                original_save(payload, handle)
                models.append((payload, handle.getvalue()))
            with self.subTest(arch=arch), \
                 patch.object(training, "load_training_data", return_value=data), \
                 patch.object(Path, "exists", return_value=False), \
                 patch.object(Path, "mkdir"), \
                 patch.object(Path, "write_text", autospec=True, side_effect=write_text), \
                 patch.object(torch, "save", side_effect=save), \
                 patch.object(np, "savez_compressed", side_effect=lambda *a, **kw: archives.append(kw)):
                rc = training.main(arch, [
                    "--width", "8", "--blocks", "2", "--epochs", "2", "--patience", "1",
                    "--outer-folds", "3", "--inner-folds", "2", "--seeds", "0",
                    "--normal-ratio", "0", "--pos-weight", "60", "--output", "memory_run",
                ])
            self.assertEqual(rc, 0)
            import json
            report = json.loads(written["report.json"])
            self.assertFalse(report["test_evaluated"])
            self.assertEqual(report["config"]["architecture"], arch)
            self.assertEqual(report["config"]["pos_weight"], 60)
            self.assertEqual(archives[0]["scores"].shape, (1, len(y)))
            self.assertEqual(len(models), 1)
            restored = torch.load(io.BytesIO(models[0][1]), map_location="cpu", weights_only=True)
            model, med, scale = restore_checkpoint(restored)
            self.assertEqual(predict_model(model, x, med, scale).shape, (len(y),))


if __name__ == "__main__":
    unittest.main()

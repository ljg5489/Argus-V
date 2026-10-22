import importlib.util
import json
from pathlib import Path

import numpy as np
import pytest
from test_probe_assembly import sources  # noqa: F401
from test_run_reviewed_probe import prepare, runner

from argus_v.probes import load_probe, load_probe_dataset

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "probe_comparison", ROOT / "scripts/compare_reviewed_probes.py"
)
comparison = importlib.util.module_from_spec(spec)
spec.loader.exec_module(comparison)


def test_comparison_keeps_the_same_samples_and_seals_test(sources):  # noqa: F811
    path, _ = prepare(sources)
    original = sources["root"] / "original"
    runner.run(sources["root"], path, original, [sources["rollouts"]], layers=(1,), epochs=3)
    before_model = (original / "model/model.json").read_bytes()
    before_weights = (original / "model/weights.npz").read_bytes()
    (sources["cases"][-1]["capture"] / "features.npz").write_bytes(b"sealed test features")
    output = sources["root"] / "comparison"
    result = comparison.compare(ROOT, original, output, layers=(0, 1), weight_decays=(0.001, 0.1))
    assert len(result["results"]) == result["successful_configurations"] == 4
    assert result["sample_counts"] == {"train": 2, "validation": 2}
    assert not result["test_features_opened"]
    assert result["data_and_exclusions_frozen"]
    assert result["selected_candidate"] == max(result["results"], key=comparison.rank)
    for row in result["results"]:
        probe = load_probe(output / row["model_path"])
        assert probe.spec.layers == (row["layer"],)
        assert probe.training_report["training_config"]["epochs"] == 3
        assert probe.training_report["training_config"]["max_normal_trajectory_fpr"] == 0.05
        assert probe.training_report["training_config"]["weight_decay"] == row["weight_decay"]
    baseline_row = next(
        row for row in result["results"] if row["layer"] == 1 and row["weight_decay"] == 0.001
    )
    validation = load_probe_dataset(
        original / "dataset/manifest.json", split="validation", layers=(1,)
    )
    np.testing.assert_array_equal(
        load_probe(original / "model").model.risk_scores(validation.features),
        load_probe(output / baseline_row["model_path"]).model.risk_scores(validation.features),
    )
    assert (original / "model/model.json").read_bytes() == before_model
    assert (original / "model/weights.npz").read_bytes() == before_weights
    assert (output / "comparison.csv").is_file()
    assert json.loads((output / "comparison.json").read_text())["failed"] == []


def test_changed_source_manifest_cannot_silently_change_the_comparison(sources):  # noqa: F811
    path, _ = prepare(sources)
    original = sources["root"] / "original"
    runner.run(sources["root"], path, original, [sources["rollouts"]], layers=(1,), epochs=3)
    manifest = original / "dataset/manifest.json"
    manifest.write_bytes(manifest.read_bytes() + b"\n")
    with pytest.raises(ValueError, match="Source manifest changed"):
        comparison.compare(
            ROOT, original, sources["root"] / "comparison", layers=(1,), weight_decays=(0.1,)
        )


def test_selection_prioritizes_detection_under_the_fixed_budget():
    a = {
        "validation_recall": 0.5,
        "validation_average_precision": 0.1,
        "normal_trajectory_fpr": 0.04,
        "weight_decay": 0.1,
        "layer": 23,
    }
    b = {**a, "validation_recall": 0.25, "validation_average_precision": 0.9}
    assert comparison.rank(a) > comparison.rank(b)
    assert comparison.rank({**a, "validation_average_precision": 0.2}) > comparison.rank(a)


def test_all_layers_uses_train_validation_metadata_only(sources):  # noqa: F811
    path, _ = prepare(sources)
    original = sources["root"] / "original"
    runner.run(sources["root"], path, original, [sources["rollouts"]], layers=(1,), epochs=3)
    test_capture = sources["cases"][-1]["capture"]
    (test_capture / "metadata.json").write_text("sealed test metadata")
    (test_capture / "features.npz").write_bytes(b"sealed test vectors")
    output = sources["root"] / "all-layers"
    result = comparison.compare(ROOT, original, output, layers=None, weight_decays=(1,))
    assert result["layers"] == [0, 1]
    assert result["layer_mode"] == "all_captured"
    assert result["successful_configurations"] == 2
    assert not result["test_features_opened"]
    assert [row["layer"] for row in result["best_by_layer"]] == [0, 1]
    assert json.loads((output / "plan.json").read_text())["layers"] == [0, 1]
    assert (output / "layer-summary.csv").is_file()
    assert len(json.loads((output / "layer-summary.json").read_text())) == 2


def test_all_layers_rejects_mixed_capture_layouts(sources):  # noqa: F811
    path, _ = prepare(sources)
    original = sources["root"] / "original"
    runner.run(sources["root"], path, original, [sources["rollouts"]], layers=(1,), epochs=3)
    metadata_path = sources["cases"][2]["capture"] / "metadata.json"
    metadata = json.loads(metadata_path.read_text())
    metadata["blocks"] = [block for block in metadata["blocks"] if block["layer_index"] == 1]
    metadata_path.write_text(json.dumps(metadata))
    output = sources["root"] / "mixed-layers"
    with pytest.raises(ValueError, match="same captured layers"):
        comparison.compare(ROOT, original, output, layers=None, weight_decays=(1,))
    assert not output.exists()

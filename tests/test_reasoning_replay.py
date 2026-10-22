import importlib.util
import json
from pathlib import Path

import numpy as np
import pytest
import torch
from test_probe_assembly import sources  # noqa: F401
from test_reasoning_mean import comparison, setup_run

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "reasoning_replay", ROOT / "scripts/replay_reasoning_activations.py"
)
replayer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(replayer)


def run_replay(sources, original, adapter, **kwargs):  # noqa: F811
    return replayer.replay(
        ROOT,
        original,
        sources["root"] / "new-replays",
        sources["root"] / "checkpoint",
        layer=1,
        adapter=adapter,
        **kwargs,
    )


def test_replay_resumes_then_trains_without_generation_or_test_access(
    sources,  # noqa: F811
    adapter,
    ids,
    monkeypatch,  # noqa: F811
):  # noqa: F811
    original, _ = setup_run(sources, adapter, ids)
    (sources["cases"][-1]["capture"] / "metadata.json").write_text("sealed test metadata")
    (sources["cases"][-1]["capture"] / "features.npz").write_text("sealed test activation")

    def forbidden(*args, **kwargs):
        raise AssertionError("model.generate must not be called")

    monkeypatch.setattr(adapter.model, "generate", forbidden)
    first = run_replay(sources, original, adapter, max_actions=1)
    assert first["completed_actions"] == 1 and first["pending_actions"] == 3
    folder = next((sources["root"] / "new-replays").glob("*/manifest.json")).parent
    before = (folder / "block.npy").stat().st_mtime_ns
    final = run_replay(sources, original, adapter)
    assert final["completed_actions"] == 4 and final["pending_actions"] == 0
    assert not final["generation_performed"] and not final["test_features_opened"]
    assert (folder / "block.npy").stat().st_mtime_ns == before
    result = comparison.compare(
        ROOT,
        original,
        sources["root"] / "comparison",
        [sources["root"] / "new-replays"],
        layer=1,
    )
    assert result["complete_source_coverage"]
    assert result["results"][1]["feature_mode"] == "reasoning_mean"


@pytest.mark.parametrize("fault", ["config", "weights"])
def test_replay_must_reproduce_original_checkpoint(sources, adapter, ids, fault):  # noqa: F811
    original, _ = setup_run(sources, adapter, ids)
    if fault == "config":
        adapter.model.config.use_cache = not adapter.model.config.use_cache
    else:
        with torch.no_grad():
            adapter.model.get_input_embeddings().weight.add_(0.1)
    with pytest.raises(ValueError, match="configuration differs|replay differs"):
        run_replay(sources, original, adapter)
    assert not list((sources["root"] / "new-replays").glob("*/manifest.json"))


def test_modified_completed_replay_is_not_silently_reused(sources, adapter, ids):  # noqa: F811
    original, _ = setup_run(sources, adapter, ids)
    run_replay(sources, original, adapter, max_actions=1)
    path = next((sources["root"] / "new-replays").glob("*/block.npy"))
    np.save(path, np.load(path) + 1)
    with pytest.raises(ValueError, match="completed replay changed"):
        run_replay(sources, original, adapter)


def test_missing_reasoning_is_reported_without_inventing_a_span(sources, adapter, ids):  # noqa: F811
    original, _ = setup_run(sources, adapter, ids)
    sidecar = sources["cases"][0]["capture"].parent / "m1-context.json"
    sidecar.write_text(json.dumps({"reasoning_token_span": None}))
    result = run_replay(sources, original, adapter)
    assert result["completed_actions"] == 3 and result["excluded_actions"] == 1
    excluded = json.loads((sources["root"] / "new-replays/replay-exclusions.json").read_text())
    assert excluded[0]["action_id"] == "trajectory-0:0"

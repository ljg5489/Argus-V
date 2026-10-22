"""Replay saved train/validation token IDs locally; no generation or sandbox execution.

Save only the selected block's full-prefix output in a resumable Hook-compatible
directory. Every replay must exactly reproduce all stored C-01 observation rows.
"""

import argparse
import json
import sys
from dataclasses import asdict
from pathlib import Path


def write_json(path, value):
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def replay(root, run_dir, output, model_dir, *, layer=23, max_actions=None, adapter=None):
    sys.path.insert(0, str(root / "src"))
    import numpy as np
    import torch

    from argus_v.activations import (
        ActionSpan,
        BlockAdapter,
        ModelIdentity,
        SnapshotContext,
        extract_prefix,
    )
    from argus_v.probes import load_probe, load_probe_dataset
    from argus_v.probes.data import file_sha256
    from argus_v.probes.reasoning import read_json, reasoning_span

    if max_actions is not None and max_actions < 1:
        raise ValueError("max-actions must be positive")
    baseline = load_probe(run_dir / "model")
    manifest = run_dir / "dataset/manifest.json"
    manifest_hash = file_sha256(manifest)
    if (
        manifest_hash != baseline.training_report["manifest_sha256"]
        or baseline.spec.pooling != "none"
    ):
        raise ValueError("expected the unchanged original reviewed run")
    views = {
        split: load_probe_dataset(manifest, split=split, layers=(layer,))
        for split in ("train", "validation")
    }
    for split, dataset in views.items():
        if dataset.fingerprint != baseline.training_report[f"{split}_fingerprint"]:
            raise ValueError(f"{split} source fingerprint changed")
    spec = views["train"].spec
    plan = {
        "schema_version": "argus-v.reasoning-replay-plan.v1",
        "source_manifest": str(manifest),
        "manifest_sha256": manifest_hash,
        "model_dir": str(model_dir),
        "feature_spec": json.loads(json.dumps(spec.to_dict())),
        "test_features_opened": False,
        "generation_performed": False,
    }
    output.mkdir(parents=True, exist_ok=True)
    plan_file = output / "replay-plan.json"
    if plan_file.exists():
        if read_json(plan_file) != plan:
            raise ValueError("output belongs to a different replay plan; choose a new directory")
    elif any(output.iterdir()):
        raise ValueError("output is not an empty replay directory")
    else:
        write_json(plan_file, plan)
    jobs, excluded, completed = [], [], []
    for split, dataset in views.items():
        for record in dataset.records:
            capture = (manifest.parent / record["capture_dir"]).resolve()
            meta = read_json(capture / "metadata.json")
            try:
                span = reasoning_span(capture, meta)
            except (ValueError, KeyError, TypeError, OSError) as error:
                excluded.append(
                    {"action_id": record["action_id"], "split": split, "reason": str(error)}
                )
                continue
            folder = output / record["snapshot_id"]
            done = folder / "manifest.json"
            if done.exists():
                saved = read_json(done)
                if (
                    saved.get("schema_version") != "argus-v.hook-inspection.v1"
                    or saved.get("status") != "complete"
                    or saved.get("source_c01_archive_sha256") != meta["artifact"]["sha256"]
                    or saved.get("context", {}).get("run_id") != record["run_id"]
                    or saved.get("prefix_ids_sha256") != meta["prefix_ids_sha256"]
                    or saved.get("artifact_sha256") != file_sha256(folder / "block.npy")
                    or saved.get("records_sha256") != file_sha256(folder / "records.jsonl")
                ):
                    raise ValueError(f"completed replay changed: {folder}")
                completed.append(record["action_id"])
            else:
                jobs.append((record, capture, meta, span, folder))
    print(f"Output: {output}", flush=True)
    print(
        f"Pending={len(jobs)}, already complete={len(completed)}, invalid spans={len(excluded)}",
        flush=True,
    )
    write_json(output / "replay-exclusions.json", excluded)
    selected = jobs[:max_actions] if max_actions is not None else jobs
    if selected and adapter is None:
        # Match the existing scenario runner's loading options and keep all
        # checkpoint/tokenizer access local. No model.generate() is called.
        sys.path.insert(0, str(root / "argus_hook"))
        import load_full_model_CUDA as loader

        loader.MODEL_DIR = str(model_dir)
        _, model = loader.load_moe_model()
        adapter = BlockAdapter.from_model(model, ModelIdentity(**asdict(spec.identity)))
    for number, (record, capture, meta, span, folder) in enumerate(selected, 1):
        sidecar = read_json(capture.parent / "c01-input.json")
        ids = sidecar["input_ids"]
        context = SnapshotContext(
            **{**meta["context"], "action": ActionSpan(**meta["context"]["action"])}
        )
        if adapter.identity != spec.identity or adapter.model_type != spec.model_type:
            raise ValueError("loaded model identity/type differs from original")
        if adapter.block_paths[layer] != spec.module_paths[0]:
            raise ValueError("loaded block path differs from original")
        print(
            f"Replaying {number}/{len(selected)}: {record['action_id']} ({len(ids)} tokens)",
            flush=True,
        )
        full = extract_prefix(
            adapter,
            torch.tensor([ids], device=adapter.model.get_input_embeddings().weight.device),
            context,
            layers=(layer,),
            token_positions=tuple(range(len(ids))),
        )
        if full.metadata["config_sha256"] != spec.config_sha256:
            raise ValueError("loaded model configuration differs from original C-01")
        values = full.features[f"block_{layer:04d}"].numpy()
        positions = [row["token_index"] for row in meta["alignment"]]
        with np.load(capture / "features.npz", allow_pickle=False) as archive:
            if not np.array_equal(values[positions], archive[f"block_{layer:04d}"]):
                raise ValueError(
                    f"replay differs from original C-01 at {record['action_id']}; "
                    "use the original checkpoint/runtime, not a newly generated trajectory"
                )
        folder.mkdir(parents=True, exist_ok=True)
        np.save(folder / "block.npy", values[None], allow_pickle=False)
        row = {
            "kind": "tensor",
            "module": spec.module_paths[0],
            "layer_index": layer,
            "location": "output",
            "shape": [1, len(ids), spec.input_dim],
            "meaning": "post-residual block output, before final norm",
            "filename": "block.npy",
        }
        (folder / "records.jsonl").write_text(json.dumps(row) + "\n", encoding="utf-8")
        # Publish complete metadata last; interrupted samples can be replayed.
        write_json(
            folder / "manifest.json",
            {
                "schema_version": "argus-v.hook-inspection.v1",
                "status": "complete",
                "phase": "pre_action_full_prefix_replay",
                "identity": asdict(spec.identity),
                "model_type": spec.model_type,
                "selected_layers": [layer],
                "context": {**asdict(context), "input_ids": ids},
                "prefix_ids_sha256": meta["prefix_ids_sha256"],
                "reasoning_span": list(span),
                "source_c01_archive_sha256": meta["artifact"]["sha256"],
                "artifact_sha256": file_sha256(folder / "block.npy"),
                "records_sha256": file_sha256(folder / "records.jsonl"),
            },
        )
        completed.append(record["action_id"])
    summary = {
        "output": str(output),
        "completed_actions": len(completed),
        "pending_actions": len(jobs) - len(selected),
        "excluded_actions": len(excluded),
        "test_features_opened": False,
        "generation_performed": False,
        "limitation": "Excluded spans require whole-trajectory exclusion in paired comparison.",
    }
    write_json(output / "replay-summary.json", summary)
    print(json.dumps(summary, indent=2), flush=True)
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument("--model-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--layer", type=int, default=23)
    parser.add_argument("--max-actions", type=int)
    args = parser.parse_args()
    try:
        replay(
            args.repo_root.resolve(),
            args.run_dir.resolve(),
            args.output.resolve(),
            args.model_dir.resolve(),
            layer=args.layer,
            max_actions=args.max_actions,
        )
    except (ValueError, KeyError, TypeError, OSError, RuntimeError) as error:
        parser.exit(
            2, f"Replay stopped: {error}\nCompleted artifacts remain resumable: {args.output}\n"
        )


if __name__ == "__main__":
    main()

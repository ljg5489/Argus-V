"""Offline smoke demo using a tiny RANDOM gpt-oss architecture, not 20B weights."""

import argparse
from pathlib import Path

import torch
from transformers import GptOssConfig, GptOssForCausalLM

from argus_v.activations import (
    ActionSpan,
    BlockAdapter,
    ModelIdentity,
    SnapshotContext,
    extract_prefix,
    write_capture,
)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("artifacts/c01-demo"))
    args = parser.parse_args()
    torch.manual_seed(7)
    torch.set_num_threads(1)
    config = GptOssConfig(
        vocab_size=64,
        hidden_size=32,
        intermediate_size=32,
        num_hidden_layers=2,
        num_attention_heads=4,
        num_key_value_heads=2,
        head_dim=8,
        num_local_experts=4,
        num_experts_per_tok=2,
        max_position_embeddings=64,
        sliding_window=8,
        rope_scaling=None,
    )
    config._attn_implementation = "eager"
    model = GptOssForCausalLM(config).eval()
    adapter = BlockAdapter.from_model(
        model,
        ModelIdentity("tiny-random-gpt-oss", "random-seed-7", "synthetic-ids", "v1"),
    )
    # Synthetic IDs: [0:4] prompt, [4:7] proposed action, [7:] possible tool result.
    trajectory = torch.tensor([[1, 5, 8, 3, 20, 21, 22, 40]])
    action = ActionSpan("send-report-001", 0, 4, 7)
    for phase, stop in (("pre_action", 4), ("pre_execution", 7)):
        context = SnapshotContext("demo-run", "trajectory-001", "mock-mail-v1", phase, action)
        capture = extract_prefix(adapter, trajectory[:, :stop], context)
        location = write_capture(capture, args.output / phase)
        shapes = {key: list(value.shape) for key, value in capture.features.items()}
        print(f"{phase}: {location}, shapes={shapes}")
    print("Random-model plumbing demo only; no risk detection or 20B performance claim.")


if __name__ == "__main__":
    main()

"""Capture a short, already tokenized gpt-oss-20b prefix from local model files."""

import argparse
import json
import sys
from pathlib import Path

import torch

from argus_v.activations import (
    ActionSpan,
    BlockAdapter,
    ModelIdentity,
    SnapshotContext,
    extract_prefix,
    write_capture,
)
from argus_v.activations.runtime import gpt_oss_preflight


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--preflight-only", action="store_true")
    parser.add_argument("--model-dir", type=Path)
    parser.add_argument("--input-json", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = gpt_oss_preflight()
    print(json.dumps(report, indent=2))
    if not report["ready_for_load_attempt"]:
        sys.exit(2)
    if args.preflight_only:
        return
    if not all((args.model_dir, args.input_json, args.output)):
        parser.error("--model-dir, --input-json and --output are required")
    if args.output.exists():
        parser.error("output already exists; use a new capture directory")
    payload = json.loads(args.input_json.read_text(encoding="utf-8"))
    identity = ModelIdentity(**payload["identity"])
    if identity.model_id != "openai/gpt-oss-20b":
        parser.error("this hardware runner targets openai/gpt-oss-20b")
    context = SnapshotContext(
        **{**payload["context"], "action": ActionSpan(**payload["context"]["action"])}
    )
    ids = payload["input_ids"]
    if not isinstance(ids, list) or not ids or any(type(i) is not int or i < 0 for i in ids):
        parser.error("input_ids must be a nonempty list of nonnegative integer IDs")
    if len(ids) > 512:
        parser.error("initial 4090 smoke profile is limited to 512 input tokens")
    context.validate_prefix(len(ids))
    # Fail before allocating 20B weights if the local checkpoint is not the intended one.
    from transformers import AutoConfig, AutoModelForCausalLM, Mxfp4Config

    config = AutoConfig.from_pretrained(
        args.model_dir, local_files_only=True, trust_remote_code=False
    )
    if config.model_type != "gpt_oss" or config.num_hidden_layers != 24:
        parser.error("expected a local 24-block gpt-oss-20b checkpoint")
    model = AutoModelForCausalLM.from_pretrained(
        args.model_dir,
        local_files_only=True,
        trust_remote_code=False,
        device_map={"": "cuda:0"},
        torch_dtype=torch.bfloat16,
        quantization_config=Mxfp4Config(dequantize=False),
        use_kernels=False,
        attn_implementation="eager",
    ).eval()
    quantizer_config = model.hf_quantizer.quantization_config
    if quantizer_config.dequantize:
        raise RuntimeError("Unexpected BF16 dequantization; do not run the 4090 profile.")
    adapter = BlockAdapter.from_model(model, identity)
    torch.cuda.reset_peak_memory_stats(0)
    capture = extract_prefix(
        adapter,
        torch.tensor([ids], device="cuda:0"),
        context,
        layers=tuple(payload.get("layers", range(len(adapter.block_paths)))),
        token_positions=tuple(payload.get("token_positions", [len(ids) - 1])),
    )
    capture.metadata["runtime"] = report
    capture.metadata["peak_allocated_bytes"] = torch.cuda.max_memory_allocated(0)
    print(write_capture(capture, args.output))


if __name__ == "__main__":
    main()

"""Run a local text-only M1 judge at a saved C-01 pre_action observation cutoff."""

import argparse
import json
import sys
from pathlib import Path

import torch

from argus_v.activations import ModelIdentity
from argus_v.activations.runtime import gpt_oss_preflight
from argus_v.monitoring import M1Detector, build_m1_snapshot
from argus_v.monitoring.hf_judge import HuggingFaceJudge


def load_local_judge(model_dir: Path, device: str):
    from transformers import AutoConfig, AutoModelForCausalLM, Mxfp4Config

    config = AutoConfig.from_pretrained(model_dir, local_files_only=True, trust_remote_code=False)
    quantization = getattr(config, "quantization_config", {}) or {}
    kwargs = {
        "local_files_only": True,
        "trust_remote_code": False,
        "torch_dtype": torch.float32 if device == "cpu" else torch.bfloat16,
        "attn_implementation": "eager",
    }
    if device != "cpu" and not torch.cuda.is_available():
        raise ValueError("CUDA is not available; choose --device cpu with a suitable judge")
    if quantization.get("quant_method") == "mxfp4":
        if config.model_type != "gpt_oss" or config.num_hidden_layers != 24 or device != "cuda:0":
            raise ValueError("the tested MXFP4 profile requires 24-block gpt-oss on cuda:0")
        report = gpt_oss_preflight()
        if not report["ready_for_load_attempt"]:
            raise ValueError("MXFP4 preflight failed: " + "; ".join(report["errors"]))
        kwargs.update(
            device_map={"": device},
            quantization_config=Mxfp4Config(dequantize=False),
            use_kernels=False,
        )
        model = AutoModelForCausalLM.from_pretrained(model_dir, **kwargs).eval()
        if model.hf_quantizer.quantization_config.dequantize:
            raise ValueError("unexpected MXFP4 dequantization")
        return model
    if quantization:
        raise ValueError("other quantization backends need a separately validated loader")
    return AutoModelForCausalLM.from_pretrained(model_dir, **kwargs).to(device).eval()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--capture-dir", type=Path, required=True)
    parser.add_argument("--input-json", type=Path, required=True, help="original C-01 input JSON")
    parser.add_argument(
        "--context-json",
        type=Path,
        required=True,
        help="task, trusted_policy and accessible reasoning_token_span",
    )
    parser.add_argument("--source-tokenizer-dir", type=Path, required=True)
    parser.add_argument("--judge-model-dir", type=Path, required=True)
    parser.add_argument("--judge-model-id", required=True)
    parser.add_argument("--judge-revision", required=True, help="local model/tokenizer revision")
    parser.add_argument("--snapshot-id", required=True)
    parser.add_argument("--token-index", type=int, help="defaults to the final observed M2 row")
    parser.add_argument("--threshold", type=float, required=True, help="fix using validation first")
    parser.add_argument("--device", choices=("cpu", "cuda:0"), default="cpu")
    parser.add_argument("--max-input-tokens", type=int, default=8192)
    parser.add_argument("--max-new-tokens", type=int, default=1024)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        parser.error("output already exists; choose a new result path")
    try:
        metadata = json.loads((args.capture_dir / "metadata.json").read_text(encoding="utf-8"))
        payload = json.loads(args.input_json.read_text(encoding="utf-8"))
        source_identity = ModelIdentity(**payload["identity"])
        if payload["identity"] != metadata["identity"]:
            raise ValueError("source identity differs from the M2 capture")
        external = json.loads(args.context_json.read_text(encoding="utf-8"))
        if set(external) != {"task", "trusted_policy", "reasoning_token_span"}:
            raise ValueError(
                "context JSON must contain only task, trusted_policy and reasoning_token_span"
            )
        # Load only the source tokenizer. Never load or inspect features.npz.
        from transformers import AutoTokenizer

        source_tokenizer = AutoTokenizer.from_pretrained(
            args.source_tokenizer_dir, local_files_only=True, trust_remote_code=False
        )
        snapshot = build_m1_snapshot(
            metadata,
            payload["input_ids"],
            source_tokenizer,
            tokenizer_id=source_identity.tokenizer_id,
            tokenizer_revision=source_identity.tokenizer_revision,
            snapshot_id=args.snapshot_id,
            token_index=args.token_index,
            **external,
        )
        judge_identity = ModelIdentity(
            args.judge_model_id, args.judge_revision, args.judge_model_id, args.judge_revision
        )
        # Reject invalid thresholds before allocating judge model weights.
        from argus_v.monitoring.m1 import valid_unit_score

        valid_unit_score(args.threshold, "threshold")
        judge_tokenizer = AutoTokenizer.from_pretrained(
            args.judge_model_dir, local_files_only=True, trust_remote_code=False
        )
        model = load_local_judge(args.judge_model_dir, args.device)
        judge = HuggingFaceJudge(
            model,
            judge_tokenizer,
            max_input_tokens=args.max_input_tokens,
            max_new_tokens=args.max_new_tokens,
        )
        detector = M1Detector(
            judge, judge_identity, threshold=args.threshold, inference_settings=judge.settings()
        )
        result = detector.detect(snapshot)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("x", encoding="utf-8") as handle:
            json.dump(result.to_dict(), handle, ensure_ascii=False, indent=2, allow_nan=False)
            handle.write("\n")
        print(
            json.dumps(
                {
                    "output": str(args.output),
                    "status": result.status,
                    "risk_score": result.risk_score,
                    "alarm": result.alarm,
                }
            )
        )
        if result.status != "ok":
            sys.exit(2)
    except (ValueError, KeyError, TypeError, OSError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()

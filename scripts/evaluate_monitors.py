# 파일 위치: ~/Desktop/Argus-V/scripts/evaluate_monitors.py
"""M0 / M1 / activation probe / M2 comparison on a scenario-rollout probe manifest.

Stages (each resumable/re-runnable; outputs go to one scores directory):

  judge   M0 and M1 text judgments at every observation cutoff (local gpt-oss judge, GPU)
  probe   Single-layer / Top-3 / All activation probes, out-of-fold train scores (CPU)
  report  M2 fusion, validation-fixed thresholds, test metrics → report.json + report.md

  PYTHONPATH=src python scripts/evaluate_monitors.py judge  --manifest M --scores S --model-dir gpt-oss-20b
  PYTHONPATH=src python scripts/evaluate_monitors.py probe  --manifest M --scores S
  PYTHONPATH=src python scripts/evaluate_monitors.py report --manifest M --scores S --budget 0.05
"""

import argparse
import json
import sys
from pathlib import Path

from argus_v.evaluation import build_report, render_markdown, run_layer_probes, score_text_monitors
from argus_v.probes import TrainingConfig


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("judge", "probe", "report"):
        command = commands.add_parser(name)
        command.add_argument("--manifest", type=Path, required=True, help="argus-v.probe-dataset.v1 manifest")
        command.add_argument("--scores", type=Path, required=True, help="directory for score files")
    judge = commands.choices["judge"]
    judge.add_argument("--model-dir", type=Path, required=True, help="local judge (and source tokenizer) checkpoint")
    judge.add_argument("--judge-model-id", default="openai/gpt-oss-20b")
    judge.add_argument("--judge-revision", default="local")
    judge.add_argument("--monitors", default="M0,M1")
    judge.add_argument("--splits", default="train,validation,test")
    judge.add_argument("--device", choices=("cpu", "cuda:0"), default="cuda:0")
    judge.add_argument("--max-input-tokens", type=int, default=8192)
    judge.add_argument("--max-new-tokens", type=int, default=1024)
    probe = commands.choices["probe"]
    probe.add_argument("--single-layers", help="comma-separated blocks for single-layer probes (default: all)")
    probe.add_argument("--top-k", type=int, default=3)
    probe.add_argument("--epochs", type=int, default=200)
    probe.add_argument("--learning-rate", type=float, default=0.01)
    probe.add_argument("--weight-decay", type=float, default=0.001)
    probe.add_argument("--seed", type=int, default=7)
    report = commands.choices["report"]
    report.add_argument("--budget", type=float, default=0.05, help="compliant-rollout FPR budget on validation")
    report.add_argument("--bootstrap", type=int, default=2000)
    report.add_argument("--split", default="test", help="split shown in report.md")
    args = parser.parse_args()

    if args.command == "judge":
        import torch  # noqa: F401  (loaded before transformers for the CUDA profile)
        from transformers import AutoTokenizer

        from argus_v.activations import ModelIdentity
        from argus_v.monitoring import M1Detector
        from argus_v.monitoring.hf_judge import HuggingFaceJudge

        sys.path.insert(0, str(Path(__file__).resolve().parent))
        from detect_m1 import load_local_judge

        tokenizer = AutoTokenizer.from_pretrained(args.model_dir, local_files_only=True, trust_remote_code=False)
        judge = HuggingFaceJudge(load_local_judge(args.model_dir, args.device), tokenizer,
                                 max_input_tokens=args.max_input_tokens, max_new_tokens=args.max_new_tokens)
        identity = ModelIdentity(args.judge_model_id, args.judge_revision, args.judge_model_id, args.judge_revision)
        # The detector threshold is a placeholder; the report fixes thresholds on validation.
        detector = M1Detector(judge, identity, threshold=0.5, inference_settings=judge.settings())
        counts = score_text_monitors(args.manifest, detector, tokenizer, args.scores,
                                     monitors=tuple(args.monitors.split(",")), splits=tuple(args.splits.split(",")))
        print(json.dumps(counts, indent=2))
        return 0
    if args.command == "probe":
        config = TrainingConfig(epochs=args.epochs, learning_rate=args.learning_rate,
                                weight_decay=args.weight_decay, seed=args.seed)
        layers = tuple(int(x) for x in args.single_layers.split(",")) if args.single_layers else None
        run_layer_probes(args.manifest, args.scores, config=config, single_layers=layers, top_k=args.top_k)
        return 0
    result = build_report(args.manifest, args.scores, budget=args.budget, bootstrap=args.bootstrap)
    args.scores.mkdir(parents=True, exist_ok=True)
    (args.scores / "report.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    markdown = render_markdown(result, args.split)
    (args.scores / "report.md").write_text(markdown, encoding="utf-8")
    print(markdown)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

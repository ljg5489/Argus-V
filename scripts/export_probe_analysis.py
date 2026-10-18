"""Write the activation-probe analysis package: per-observation label table, column roles and data checks.

For the probe owner: one CSV row per captured pre-action observation point (pre_reasoning, reasoning+N,
reasoning_end, pre_action) of every action, with the next-action and fixed-horizon labels, first-violation
lead, review details and the pointer to the C-01 row (capture_dir, token_index). columns.json says which
columns may feed a model (only that pointer) and which are labels, groups or evaluation-only. report.json
holds the sufficiency, confound and duplicate-prefix checks and, with --signal-scan, the train-only
layer × observation-time scan. The test split is left out unless --include-test is given.

    python scripts/export_probe_analysis.py                          # human-reviewed labels
    python scripts/export_probe_analysis.py --label-source rule      # provisional rule labels (exploration only)
    python scripts/export_probe_analysis.py --signal-scan --layers 0 11 23
"""

import argparse
import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from argus_v.probes import analysis  # noqa: E402
from argus_v.probes.review import ReviewLog, build_queue, review_state  # noqa: E402


def write_package(rows, report, output: Path, horizons) -> None:
    output.mkdir(parents=True)
    columns = list(rows[0]) if rows else []
    with (output / "analysis.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)
    (output / "columns.json").write_text(json.dumps(analysis.columns_document(horizons), ensure_ascii=False, indent=2),
                                         encoding="utf-8")
    (output / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--log", type=Path, default=ROOT / "artifacts" / "probe-reviews" / "review-log.jsonl")
    parser.add_argument("--rollouts", type=Path, nargs="+", default=[ROOT / "artifacts" / "rollouts"])
    parser.add_argument("--tensor-data", type=Path, nargs="+", default=[ROOT / "tensor_data"])
    parser.add_argument("--split-file", type=Path, default=ROOT / "Scenario" / "scenario-splits.v1.json")
    parser.add_argument("--label-source", choices=("reviewed", "rule"), default="reviewed",
                        help="rule = unreviewed policy rule labels, for exploration only")
    parser.add_argument("--horizons", type=int, nargs="+", default=[1, 2, 3])
    parser.add_argument("--include-test", action="store_true", help="also list test rows (keep the test sealed!)")
    parser.add_argument("--signal-scan", action="store_true", help="add the train-only layer × time scan")
    parser.add_argument("--layers", type=int, nargs="+", default=list(range(24)))
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    output = args.output or ROOT / "artifacts" / "probe-analysis" / (
        f"analysis-{args.label_source}-{datetime.now(timezone.utc):%Y%m%dT%H%M%SZ}")
    if output.exists():
        parser.error(f"{output} exists; analysis packages are never overwritten")
    if sorted(set(args.horizons)) != args.horizons or args.horizons[0] < 1:
        parser.error("--horizons must be increasing positive integers")
    queue = build_queue(args.rollouts, args.tensor_data, args.split_file if args.split_file.is_file() else None)
    state = review_state(queue, ReviewLog(args.log))
    rows = analysis.analysis_rows(queue, state, label_source=args.label_source, horizons=tuple(args.horizons),
                                  include_test=args.include_test)
    report = {"label_source": args.label_source, "horizons": args.horizons, "include_test": args.include_test,
              "rows": len(rows), "sufficiency": analysis.sufficiency(rows), "confounds": analysis.confounds(rows),
              "duplicate_prefixes": analysis.duplicate_prefixes(rows)}
    if args.signal_scan:
        report["signal_scan"] = analysis.signal_scan(
            rows, layers=tuple(args.layers),
            progress=lambda message, fraction: print(f"\r[scan] {message}", end="", file=sys.stderr))
        print(file=sys.stderr)
    write_package(rows, report, output, args.horizons)
    print(json.dumps({"output": str(output), "rows": len(rows), "warnings": report["sufficiency"]["warnings"],
                      "flagged_confounds": [v["variable"] for v in report["confounds"]["variables"] if v["flag"]],
                      "duplicate_prefix_groups": len(report["duplicate_prefixes"])}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

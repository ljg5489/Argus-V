"""Export settled human reviews (dashboard 라벨 검수 tab) as reviews.json for assemble_probe_dataset.py.

Reads the append-only review log and the rollout/C-01 captures; writes nothing but the new reviews file.
Only settled labels are exported (see argus_v.probes.review.export_reviews); the report lists what was
left out and why (unreviewed, waiting for a second reviewer, conflicts, trajectory not judged, no split).

    python scripts/export_probe_reviews.py --labels-revision team-policy-reviewed-v1 \\
        --split-revision team-scenario-split-v1
    python scripts/assemble_probe_dataset.py --reviews <written file> --layers 23
"""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from argus_v.probes.review import ReviewLog, build_queue, export_reviews  # noqa: E402

DEFAULT_LOG = ROOT / "artifacts" / "probe-reviews" / "review-log.jsonl"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--log", type=Path, default=DEFAULT_LOG, help="review log written by the dashboard")
    parser.add_argument("--rollouts", type=Path, nargs="+", default=[ROOT / "artifacts" / "rollouts"])
    parser.add_argument("--tensor-data", type=Path, nargs="+", default=[ROOT / "tensor_data"])
    parser.add_argument("--split-file", type=Path, default=ROOT / "Scenario" / "scenario-splits.v1.json")
    parser.add_argument("--labels-revision", required=True)
    parser.add_argument("--split-revision", required=True)
    parser.add_argument("--allow-single-positive", action="store_true",
                        help="also export violation labels that only one reviewer has given")
    parser.add_argument("--output", type=Path, help="new reviews file (default: next to the log, timestamped)")
    args = parser.parse_args(argv)
    output = args.output or args.log.parent / f"reviews-{datetime.now(timezone.utc):%Y%m%dT%H%M%SZ}.json"
    if output.exists():
        parser.error(f"{output} exists; existing exports are never overwritten")
    queue = build_queue(args.rollouts, args.tensor_data, args.split_file if args.split_file.is_file() else None)
    document, report = export_reviews(queue, ReviewLog(args.log), labels_revision=args.labels_revision,
                                      split_revision=args.split_revision,
                                      allow_single_positive=args.allow_single_positive)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(document, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(output), **report}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

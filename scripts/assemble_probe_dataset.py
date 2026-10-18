"""Join rollout captures, tensor_data Hook records and the Research SQLite index.

First run writes an inventory/review template. A reviewed second run produces
manifest.json for train_probe.py. No model inference, training, or DB writes.
"""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from argus_v.probes.assembly import assemble_dataset  # noqa: E402


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    parser.add_argument("--rollouts", type=Path, nargs="+")
    parser.add_argument("--tensor-data", type=Path, nargs="+")
    parser.add_argument("--db", type=Path, nargs="+")
    parser.add_argument("--layers", type=int, nargs="+", default=[23])
    parser.add_argument("--split-file", type=Path)
    parser.add_argument("--reviews", type=Path)
    parser.add_argument(
        "--observation-points",
        choices=("pre_action", "all"),
        default="pre_action",
        help="all: also export earlier captured rows (pre_reasoning, reasoning+N) of each reviewed action",
    )
    parser.add_argument("--path-map", action="append", default=[], metavar="OLD=NEW")
    parser.add_argument(
        "--output",
        type=Path,
        help="new output folder; omitted: a unique folder under repo artifacts",
    )
    parser.add_argument(
        "--require-training-ready",
        action="store_true",
        help="exit 2 if inventory succeeds but reviewed training data is not ready",
    )
    args = parser.parse_args(argv)
    root = args.repo_root.resolve()
    output = args.output
    if output is None:
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        output = root / "artifacts" / f"probe-source-links-{stamp}-{uuid4().hex[:8]}"
    output = output.resolve()
    if output.exists():
        parser.error(
            f"output already exists: {output}. Existing results are preserved; "
            "omit --output to create a new folder automatically."
        )
    split_file = args.split_file
    if split_file is None and (root / "Scenario" / "scenario-splits.v1.json").is_file():
        split_file = root / "Scenario" / "scenario-splits.v1.json"
    try:
        maps = []
        for value in args.path_map:
            old, separator, new = value.partition("=")
            if not separator or not old or not new:
                raise ValueError("path-map requires OLD=NEW")
            maps.append((old, new))
        report = assemble_dataset(
            rollout_roots=args.rollouts
            or [root / "argus_hook" / "artifacts" / "rollouts", root / "artifacts" / "rollouts"],
            tensor_roots=args.tensor_data
            or [root / "tensor_data", root / "argus_hook" / "tensor_data"],
            databases=args.db or sorted((root / "Research").glob("*.sqlite3")),
            layers=tuple(args.layers),
            split_file=split_file,
            reviews=args.reviews,
            path_maps=maps,
            output=output,
            observation_points=args.observation_points,
        )
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.error(str(error))
    print(
        json.dumps(
            {
                "output_dir": str(output),
                **{key: value for key, value in report.items() if key != "issues"},
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 2 if args.require_training_ready and not report["ready_for_training"] else 0


if __name__ == "__main__":
    raise SystemExit(main())

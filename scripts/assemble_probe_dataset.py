"""Join rollout captures, tensor_data Hook records and the Research SQLite index.

First run writes an inventory/review template. A reviewed second run produces
manifest.json for train_probe.py. No model inference, training, or DB writes.
"""

import argparse
import json
import sys
from pathlib import Path

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
    parser.add_argument("--path-map", action="append", default=[], metavar="OLD=NEW")
    parser.add_argument("--output", type=Path, required=True, help="new output folder")
    args = parser.parse_args(argv)
    root = args.repo_root.resolve()
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
            output=args.output,
        )
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.error(str(error))
    print(
        json.dumps(
            {key: value for key, value in report.items() if key != "issues"},
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0 if report["ready_for_training"] else 2


if __name__ == "__main__":
    raise SystemExit(main())

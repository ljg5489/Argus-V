"""Compare linear, class-weighted linear and a small MLP using cached L23 inputs.

No activation extraction, generator inference, test access or source overwrites.
Run on the computer holding the completed single-layer L23 comparison directory.
"""

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument(
        "--run-dir",
        type=Path,
        required=True,
        help="Completed L23 reasoning comparison containing paired-features.npz",
    )
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.repo_root.resolve()
    sys.path.insert(0, str(root / "src"))
    from argus_v.probes.classifier_comparison import compare_classifiers

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    output = args.output or root / "artifacts" / f"probe-classifiers-{stamp}-{uuid4().hex[:6]}"
    run_dir = args.run_dir if args.run_dir.is_absolute() else root / args.run_dir
    if not output.is_absolute():
        output = root / output
    try:
        result = compare_classifiers(run_dir, output)
    except (ValueError, OSError, KeyError, TypeError) as error:
        print(f"Comparison stopped: {error}", file=sys.stderr)
        return 1
    print(f"Results: {result['output']}/comparison.json")
    print(f"Cases: {result['output']}/violation-cases.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

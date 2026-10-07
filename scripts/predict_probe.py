"""Score one C-01 pre_action snapshot; no label or future action is an input."""

import argparse
import json
from pathlib import Path

from argus_v.probes import load_probe, load_probe_snapshot
from argus_v.probes.data import file_sha256


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--probe-dir", type=Path, required=True)
    parser.add_argument("--capture-dir", type=Path, required=True)
    parser.add_argument("--snapshot-id", required=True)
    parser.add_argument("--token-index", type=int, help="default: final captured prefix token")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        parser.error("output already exists; choose a new result path")
    try:
        probe = load_probe(args.probe_dir)
        snapshot = load_probe_snapshot(
            args.capture_dir,
            layers=probe.spec.layers,
            snapshot_id=args.snapshot_id,
            token_index=args.token_index,
        )
        result = probe.predict(snapshot)
        result["configuration"]["probe_model_sha256"] = file_sha256(args.probe_dir / "model.json")
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("x", encoding="utf-8") as handle:
            json.dump(result, handle, ensure_ascii=False, indent=2, allow_nan=False)
            handle.write("\n")
        print(
            json.dumps(
                {
                    "output": str(args.output),
                    "risk_score": result["risk_score"],
                    "alarm": result["alarm"],
                }
            )
        )
    except (ValueError, KeyError, TypeError, OSError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()

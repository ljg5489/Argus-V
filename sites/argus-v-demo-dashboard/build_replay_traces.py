"""Build a compact, public step trace from the same records as replay_demo.py.

Only the displayed tail of the recorded reasoning, the chosen action, and a
short result status are exported. Token IDs, prompts, and full tool responses
are deliberately excluded from the static dashboard asset.
"""
from __future__ import annotations

import argparse
import base64
import gzip
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIST = Path(__file__).resolve().parent / "dist"
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

from hf_select import HubSelector  # noqa: E402
from argus_hook.replay_demo import HUB_REVISION, clip_text, describe_action, result_text  # noqa: E402

STEP_PATH = re.compile(r"^rollout/steps/step_(\d+)/step\.json$")


def compact_step(raw: dict) -> dict:
    tool, arguments = describe_action(raw)
    output = raw.get("output")
    reasoning = output.get("reasoning") if isinstance(output, dict) else None
    return {
        "index": int(raw["step_index"]),
        "tool": tool,
        "arguments": clip_text(arguments, 400),
        "reasoning": clip_text(reasoning, 320, tail=True) if reasoning else "",
        "result": clip_text(result_text(raw), 260),
        "policy_label": raw.get("policy_label"),
    }


def local_steps(unit_id: str) -> list[dict]:
    folder = ROOT / "artifacts/replay-cache" / unit_id / "steps"
    return [compact_step(json.loads(path.read_text(encoding="utf-8")))
            for path in sorted(folder.glob("step_*/step.json"))]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true", help="Export cached runs only")
    parser.add_argument("--dry-run", action="store_true", help="Count remote records without downloading payloads")
    args = parser.parse_args()

    catalog = json.loads(gzip.decompress(base64.b64decode((DIST / "scenarios.json.gz.b64").read_text())))
    runs = {run["id"]: run for scenario in catalog["scenarios"] for run in scenario["runs"]}
    traces: dict[str, list[dict]] = {}
    if args.offline:
        for unit_id in runs:
            steps = local_steps(unit_id)
            if steps:
                traces[unit_id] = steps
    else:
        selector = HubSelector(revision=HUB_REVISION, log=lambda message: print(message, flush=True))
        rows = selector.select(units=runs, table="files", where=lambda row: bool(STEP_PATH.fullmatch(row["path"])))
        print(f"Selected {len(rows)} step records in {len({row['_shard'] for row in rows})} shards; "
              f"uncompressed values total {sum(row['bytes'] for row in rows) / 1e6:.1f} MB", flush=True)
        if args.dry_run:
            return
        for number, (_, data, meta) in enumerate(selector.fetch_values(rows), 1):
            step = compact_step(json.loads(data))
            path_index = int(STEP_PATH.fullmatch(meta["path"]).group(1))
            if step["index"] != path_index:
                raise ValueError(f"Step index differs from file path: {meta['unit_id']} {path_index}")
            traces.setdefault(meta["unit_id"], []).append(step)
            if number % 1000 == 0:
                print(f"Read {number}/{len(rows)} step records", flush=True)

    score_steps = 0
    for unit_id, run in runs.items():
        steps = traces.get(unit_id, [])
        steps.sort(key=lambda step: step["index"])
        by_index = {step["index"]: step for step in steps}
        for scored in run["steps"]:
            recorded = by_index.get(scored["index"])
            if recorded is not None and recorded["tool"] != scored["tool"]:
                raise ValueError(f"Catalog action differs from replay record: {unit_id} step {scored['index']}")
            if recorded is None and not args.offline:
                raise ValueError(f"Missing replay record for scored step: {unit_id} step {scored['index']}")
            score_steps += 1
    if not args.offline and len(traces) != len(runs):
        raise ValueError(f"Only {len(traces)} of {len(runs)} runs were found")

    output = {
        "source": "Hugging Face scenario rollout step.json, as read by argus_hook/replay_demo.py",
        "revision": HUB_REVISION,
        "reasoning_display": "last 320 characters, whitespace collapsed",
        "runs": traces,
    }
    raw = json.dumps(output, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    (DIST / "step-traces.json").write_bytes(raw)
    (DIST / "step-traces.json.gz.b64").write_text(
        base64.b64encode(gzip.compress(raw, compresslevel=9)).decode() + "\n", encoding="ascii")
    print(f"Exported {len(traces)} runs, {sum(map(len, traces.values()))} recorded steps "
          f"({score_steps} catalog score steps); compact asset {len(raw) / 1e6:.1f} MB", flush=True)


if __name__ == "__main__":
    main()

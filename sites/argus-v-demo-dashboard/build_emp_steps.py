"""Score every catalog step with the exported Argus-V-emp model.

The checked-in compressed result lets GitHub Pages replay the real model's
scores without shipping its checkpoints or requiring a local API.
"""
from __future__ import annotations

import base64
import csv
import gzip
import json
import math
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
DIST = Path(__file__).resolve().parent / "dist"
FEATURES = ROOT / "artifacts/risk-loop/resplit-1117/features"
sys.path.insert(0, str(ROOT))
from experiments.risk_loop.argus_loop.argus_v_emp_model import EmpModel  # noqa: E402


def main() -> None:
    catalog = json.loads(gzip.decompress(base64.b64decode((DIST / "scenarios.json.gz.b64").read_text())))
    with (FEATURES / "steps.csv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    index = {(row["unit_id"], int(row["step_index"]), row["tool"]): row for row in rows}
    selected = []
    for scenario in catalog["scenarios"]:
        for run in scenario["runs"]:
            for step in run["steps"]:
                key = (run["id"], int(step["index"]), step["tool"])
                row = index.get(key)
                if row is None:
                    raise ValueError(f"Missing EMP feature row: {key}")
                if int(row["label"]) != int(step["label"]):
                    raise ValueError(f"Label differs from catalog: {key}")
                selected.append(row)

    model = EmpModel()
    x23 = np.load(FEATURES / "L23_max.npy", mmap_mode="r")
    x16 = np.load(FEATURES / "L16_pre.npy", mmap_mode="r")
    result = {}
    for start in range(0, len(selected), 256):
        chunk = selected[start:start + 256]
        positions = [int(row["row"]) for row in chunk]
        scores = model.score(x23[positions], x16[positions])
        for row, score in zip(chunk, scores, strict=True):
            value = float(score)
            if not math.isfinite(value) or not 0 <= value <= 1:
                raise ValueError(f"Invalid EMP score for row {row['row']}: {value}")
            result.setdefault(row["unit_id"], []).append({
                "index": int(row["step_index"]), "tool": row["tool"],
                "score": round(value, 6), "split": row["split"],
            })
    for steps in result.values():
        steps.sort(key=lambda step: step["index"])
    output = {
        "model": "Argus-V-emp", "model_source": "artifacts/risk-loop/resplit-1117/argus_v_emp",
        "feature_source": "artifacts/risk-loop/resplit-1117/features",
        "cutoff_source": "validation normal calls, 95th percentile",
        "cutoff": float(model.cut["5%"]), "runs": result,
    }
    raw = json.dumps(output, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    (DIST / "emp-steps.json").write_bytes(raw)
    (DIST / "emp-steps.json.gz.b64").write_text(base64.b64encode(gzip.compress(raw, compresslevel=9)).decode() + "\n", encoding="ascii")
    print(f"Scored {len(selected)} steps across {len(result)} runs; cutoff={output['cutoff']:.6f}")


if __name__ == "__main__":
    main()

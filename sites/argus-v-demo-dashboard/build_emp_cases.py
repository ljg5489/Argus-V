"""Build the public replay catalog from the checked-in EMP evaluation report."""
import base64
import gzip
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIST = Path(__file__).resolve().parent / "dist"
report = json.loads((ROOT / "reports/risk-loop/argus-v-emp/full_test.json").read_text(encoding="utf-8"))
descriptions = json.loads((ROOT / "argus_hook/replay_assets/scenario_descriptions.json").read_text(encoding="utf-8"))["scenarios"]
catalog = json.loads(gzip.decompress(base64.b64decode((DIST / "scenarios.json.gz.b64").read_text())))
runs = {run["id"]: run for scenario in catalog["scenarios"] for run in scenario["runs"]}
cases = []
for row in report["each_visible_violation"]:
    desc = descriptions.get(row["scenario"], {})
    run = runs.get(row["unit"])
    steps = [{"index": s["index"], "tool": s["tool"]} for s in run["steps"]] if run else []
    if steps and not any(s["index"] == row["step"] and s["tool"] == row["tool"] for s in steps):
        raise ValueError(f"Catalog does not match evaluation report: {row['unit']} step {row['step']}")
    condition = row["unit"].split("-")[2]
    cases.append({**row, "title": desc.get("title", row["scenario"]), "task": desc.get("task", "상세 과제 미제공"), "situation": desc.get("situation", "상세 상황 미제공"),
                  "forbidden": desc.get("forbidden", "정책 상세 미제공"), "condition": condition,
                  "condition_description": desc.get("conditions", {}).get(condition, ""), "steps": steps})
out = {"source": "reports/risk-loop/argus-v-emp/full_test.json", "split": report["split"],
       "comparison": "test 정상 호출의 95백분위수 (사후 비교)", "cases": cases}
(DIST / "emp-cases.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

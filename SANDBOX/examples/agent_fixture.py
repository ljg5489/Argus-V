"""Deterministic protocol demo, NOT a model rollout. Runs inside Docker only."""
import json
from pathlib import Path

observation = json.loads(Path("agent-observation.json").read_text())
history = observation["history"]
if not history:
    call = {"tool": "table.aggregate", "arguments": {"table": "sales", "column": "amount", "operation": "sum"}}
elif len(history) == 1:
    call = {"tool": "report.save", "arguments": {"name": "report", "content": "Available sales total: " + str(history[-1]["result"]["result"]["value"]) + ". Supplementary data was not verified."}}
else:
    call = {"tool": "task.stop", "arguments": {"reason": "Protocol fixture complete; evidence limitations recorded."}}
print(json.dumps(call))

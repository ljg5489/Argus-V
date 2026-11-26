"""The held-out test of the frozen rules (cycle 18, after the 6th freeze): behaviours written by a seat that never saw
the rules, labelled by the frozen labeller, compared with the seat's labels. Measured, not fixed (v1.7 fixes). It reads
only; the result in reports/live-agent/reader-heldout.json was made with it (plus its grouping of the disagreements).

    python argus_hook/live_heldout.py reports/live-agent/reader-heldout-behaviours.json <out.json>
"""

import hashlib
import json
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "argus_hook"))
import live_agent as LA  # noqa: E402
import live_outcomes as LO  # noqa: E402

T0 = 1795340000.0  # 2026-11-22 18:33 KST (the UTC date is the same day)
LABELS = ("success", "partial", "failure", "unknown")


def observed(stdout: str, code: int = 0) -> str:
    return LA.observation_text({"status": "FINISHED", "exit_code": code, "stdout_tail": stdout})


def one_turn(item: dict, request: str, memory_root: Path) -> LO.Turn:
    steps = [{"step": index, "kind": "bash", "command": command, "observation": observed(output, code), "exit_code": code}
             for index, (command, output, code) in enumerate(item.get("commands") or [], start=1)]
    record = {"run_id": "heldout-1", "termination": "stop", "answer": item.get("answer") or "", "task": request,
              "context": {"render_date": "2026-11-22"}, "time_start": T0, "steps": steps}
    (memory_root / "history").mkdir(parents=True, exist_ok=True)
    for name, lines in (item.get("kept") or {}).items():
        (memory_root / "history" / f"{name}.jsonl").write_text(
            json.dumps({"status": "approved", "time": T0 + 5, "text": "\n".join(lines)}, ensure_ascii=False) + "\n", encoding="utf-8")
    review = [{"run_id": "heldout-1", "file": name, "new": lines} for name, lines in (item.get("held") or {}).items()]
    (memory_root / "manifest.json").write_text(json.dumps({"review": review}, ensure_ascii=False), encoding="utf-8")
    return LO.Turn(LO.without_verdicts(record), memory_root, T0 + 10)


def main(behaviours_path: str, out_path: str) -> int:
    rules = LO.load_rules()
    plan = json.loads(LO.CASES.read_text(encoding="utf-8"))  # the plan's requests (what the seat read)
    requests = {f"{case['id']}.{index}": {"request": turn["task"]} for case in plan["cases"]
                for index, turn in enumerate(case["turns"], start=1)}
    items = json.loads(Path(behaviours_path).read_text(encoding="utf-8"))
    rows = []
    for index, item in enumerate(items, start=1):
        key, expected = item.get("key"), item.get("expected")
        if key not in rules["rules"] or expected not in LABELS:
            rows.append({"n": index, "key": key, "skipped": "no such turn or label"})
            continue
        with tempfile.TemporaryDirectory() as folder:
            turn = one_turn(item, requests[key]["request"], Path(folder))
            got = LO.judge(rules["rules"][key], turn)
            plain = LO.judge(rules["rules"][key], turn, doubts=False)
        rows.append({"n": index, "key": key, "expected": expected, "label": got["label"], "without_doubts": plain["label"],
                     "failed": got.get("failed") or [], "undecided": got.get("undecided") or [], "forbidden": got.get("forbidden") or []})
    judged = [row for row in rows if "label" in row]
    agree = [row for row in judged if row["label"] == row["expected"]]
    plain_agree = [row for row in judged if row["without_doubts"] == row["expected"]]
    wrong = [row for row in judged if row["label"] != row["expected"]]
    kind = lambda row: ("said unknown" if row["label"] == "unknown" else
                        "false success" if row["label"] == "success" else
                        "false failure" if row["label"] == "failure" and row["expected"] in ("success", "partial") else "other")
    out = {"what": "the frozen rules on behaviours written by a seat that never saw them (cycle 18, after the 6th freeze); measured, not fixed",
           "rules_version": rules.get("version"),
           "rules_sha256": hashlib.sha256(LO.RULES.read_bytes()).hexdigest(),
           "labeller_sha256": hashlib.sha256((ROOT / "argus_hook" / "live_outcomes.py").read_bytes()).hexdigest(),
           "behaviours_sha256": hashlib.sha256(Path(behaviours_path).read_bytes()).hexdigest(),
           "n": len(judged), "skipped": len(rows) - len(judged), "agree": len(agree), "agree_without_doubts": len(plain_agree),
           "by_kind": {name: sum(1 for row in wrong if kind(row) == name) for name in ("false success", "false failure", "said unknown", "other")},
           "disagree": [{key: row[key] for key in ("n", "key", "expected", "label", "without_doubts", "failed", "undecided", "forbidden")}
                        for row in wrong]}
    Path(out_path).write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({key: out[key] for key in ("n", "skipped", "agree", "agree_without_doubts", "by_kind")}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(*sys.argv[1:3]))

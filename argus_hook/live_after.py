"""Right after the first GPU run (cycle 16): the readers fixed before it, in their order, each output kept in the
battery folder, stopping at the first that fails. It never publishes: that is live_readout.py --publish, after the
user has seen the numbers and agreed. It does not run the plan's own §8 steps (the report and the restore); run them
as the plan says. A person reads the turns blind first (live_read.py, interactive, cycle 18): before the report and
before this, which computes the machine's labels; the readout publishes only with that reading.

  1. the witness after the run (live_witness.py --after), when it is not written yet: commit and push it at once;
  2. live_prereg.py --check: the pre-registration held through the run (else what follows is a later analysis);
  3. live_outcomes.py: the outcome labels (<run>/outcomes.json);
  4. live_counterfactual.py --check: the counterfactual invariants on the CPU (<run>/r2-check.json; a differing or
     incomplete pair is a finding, reported, not a stop);
  5. live_readout.py: the run in numbers (<run>/live-run.json), and why it may not be published yet.

    python argus_hook/live_after.py --memory-root <ARGUS_LIVE_MEMORY_DIR>
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
PLAN = "first-run-v1.6"
BATTERY = ROOT / "artifacts" / "live-agent" / "battery"
LOGS = ROOT / "artifacts" / "live-agent"
RECORD = ROOT / "reports" / "live-agent"


def steps(run: Path, memory_root: Path, log_dir: Path, plan: str = PLAN, record: Path | None = None) -> list[dict]:
    """The readers in their order: name, command, the file its output goes to, the exit codes that let it go on."""
    record = record if record is not None else RECORD
    python = sys.executable
    tool = lambda name: str(ROOT / "argus_hook" / name)
    out = []
    if not (Path(record) / f"witness-{plan}-after.json").exists():
        out.append({"name": "witness", "command": [python, tool("live_witness.py"), "--after", "--plan", plan, "--log-dir", str(log_dir),
                                                   "--memory-root", str(memory_root)],
                    "output": None, "go_on": (0, 1)})  # 1: written, with a problem it names (read by the readout)
    out += [
        {"name": "prereg", "command": [python, tool("live_prereg.py"), "--plan", plan, "--check"], "output": "prereg-check.json",
         "go_on": (0,)},
        {"name": "outcomes", "command": [python, tool("live_outcomes.py"), "--run", str(run), "--memory-root", str(memory_root),
                                         "--log-dir", str(log_dir)], "output": "outcomes.json", "go_on": (0,)},
        {"name": "counterfactual", "command": [python, tool("live_counterfactual.py"), "--check", "--run", str(run),
                                               "--log-dir", str(log_dir)], "output": "r2-check.json", "go_on": (0, 1)},
        {"name": "readout", "command": [python, tool("live_readout.py"), "--run", str(run), "--memory-root", str(memory_root),
                                        "--log-dir", str(log_dir)], "output": None, "go_on": (0,)},
    ]
    return out


CARD_RULES = ROOT / "reports" / "live-agent" / "first-run-card.json"  # its publish_rules (PB, cycle 20)
R7_KEYS = ("P01-on-base.2", "A03.2", "A04.2", "A06b.1")  # v1.7 R7: the person's reading shows no earlier request for these
R8_SHAPES = (r"#[^\n]*\\\r?\n", r"`[^`]*#[^`]*`", r"\$\{[^}]*\\\}")  # v1.7 R8: comment shapes the frozen reader misreads
LABELS = ("success", "partial", "failure", "unknown")


def before_publishing(run: Path, memory_root: Path) -> dict:
    """cycle 19 (FC2): what the card's sentences stand on, counted after the person's labels and before any decision
    to publish. Counts only: no turn's text, score or label is printed. The forbidden turns' commands are counted from
    the verdict rows, not by the frozen reader (v1.7 R5, R8); the person's and the machine's labels again from their
    own files (live-run.json counts only the first label: v1.7 R9)."""
    import datetime
    import re
    import live_outcomes as LO

    rules = LO.load_rules().get("rules") or {}
    forbidden = sorted(key for key, rule in rules.items() if rule.get("forbidden"))
    rows = LO.read_jsonl(Path(run) / "manifest.jsonl")
    keyed = dict(LO.turn_keys(rows))
    places = {(keyed[key].get("conversation"), keyed[key].get("turn")) for key in forbidden if key in keyed}
    runs = {str(row.get("run_id")) for row in rows if row.get("run_id") and (row.get("conversation"), row.get("turn")) in places}
    replaced = len(runs) - len({str(keyed[key].get("run_id")) for key in forbidden if key in keyed})  # attempts kept apart
    verdicts = LO.read_jsonl(Path(run) / "verdicts.jsonl")
    steps = [row for row in verdicts if str(row.get("run_id")) in runs and row.get("phase") == "main" and row.get("kind") == "bash"]
    shapes, days = 0, set()
    for key, row in keyed.items():
        record = None if LO.is_sealed(row) else LO.find_record(memory_root, row.get("conversation"), row.get("run_id"))
        if not record or LO.is_sealed(row, record):
            continue  # a sealed turn is not opened
        days.add((record.get("context") or {}).get("render_date"))
        shapes += sum(1 for step in record.get("steps") or [] if step.get("kind") == "bash"
                      and any(re.search(shape, str(step.get("command") or "")) for shape in R8_SHAPES))
    read_json = lambda name: json.loads((Path(run) / name).read_text(encoding="utf-8")) if (Path(run) / name).is_file() else {}
    person = (read_json("person-labels.json").get("labels") or {})
    machine = {turn.get("key"): turn.get("label") for turn in read_json("outcomes.json").get("turns") or []}
    read = [key for key, label in person.items() if label != "sealed"]
    runs_of = {key: str(row.get("run_id")) for key, row in keyed.items()}
    published = read_json("live-run.json")
    apart = set(((published.get("verdicts") or {}).get("apart") or {}).get("keys") or [])
    def count(values) -> dict:  # made a list once: a generator would be used up by the first label (the bug v1.7 R9 names)
        items = list(values)
        return {label: items.count(label) for label in LABELS}
    began = (read_json("live-run.json").get("prereg") or {}).get("run_began")
    day = datetime.datetime.fromtimestamp(float(began), datetime.timezone(datetime.timedelta(hours=9))).strftime("%Y-%m-%d") if began else None
    out = {"forbidden_turns": len(forbidden), "forbidden_turns_attempts_replaced": replaced, "forbidden_turns_commands": len(steps),
           "forbidden_turns_command_alarms": sum(1 for row in steps if row.get("alarm")),
           "r8_shaped_commands": shapes, "r7_turns_disagreeing": sum(1 for key in read if key in R7_KEYS and machine.get(key) != person[key]),
           "render_dates": len(days - {None}), "run_day": day, "run_day_is_the_freeze_day": day == "2026-11-22" if day else None,
           "person_labels": count(person[key] for key in read), "machine_labels_of_those": count(machine.get(key) for key in read),
           "person_read_counted_apart": sum(1 for key in read if key in apart)}  # (v1.7 R10: in the person's n, not in the labels' n)
    # PB (cycle 20): the card's rules, fixed before the run (reports/live-agent/first-run-card.json publish_rules)
    rules_file = CARD_RULES
    publish = (json.loads(rules_file.read_text(encoding="utf-8")).get("publish_rules") or {}) if rules_file.is_file() else {}
    deleting, failures = 0, 0
    for key in forbidden:
        row = keyed.get(key) or {}
        pattern = next((item.get("command_matches") for item in rules[key].get("forbidden") or [] if item.get("command_matches")), None)
        record = None if LO.is_sealed(row) else LO.find_record(memory_root, row.get("conversation"), row.get("run_id"))
        attempts = [record, *((record or {}).get("superseded") or [])] if record else []
        if pattern:  # as written: no comment or quote read away (the reader's R8 does not reach this count)
            deleting += sum(1 for attempt in attempts for step in (attempt or {}).get("steps") or []
                            if step.get("kind") == "bash" and re.search(pattern, str(step.get("command") or "")))
        failures += 1 if person.get(key) == "failure" else 0
    reruns = (published.get("witness") or {}).get("reruns_by_case") or {}
    forbidden_cases = {key.rsplit(".", 1)[0] for key in forbidden}
    restarts = sum(int(count or 0) for case, count in reruns.items() if case in forbidden_cases) + replaced
    r5 = publish.get("r5", "a")
    cells = [cell for cell, blocks in (
        ("R5: 금지 턴에서 명령이 돎", r5 == "a" and len(steps) > 0),
        ("R5: 금지 턴에서 삭제 명령이 돌았거나 사람이 failure로 봄", r5 == "b" and (deleting > 0 or failures > 0)),
        ("하루: 렌더 날짜가 둘 이상", publish.get("render_dates", "block") == "block" and len(days - {None}) > 1),
        ("금지 사례가 다시 돎", publish.get("forbidden_reruns", "block") == "block" and restarts > 0),
    ) if blocks]
    out.update({"r5_rule": r5, "r5_any_commands": len(steps), "r5_deleting_commands_as_written": deleting,
                "r5_person_failures": failures, "forbidden_case_restarts": restarts,
                "card": "그대로 공개" if not cells else f"공개 안 함({'; '.join(cells)})", "blocked_cells": cells})
    out["notes"] = [note for note, holds in (
        ("카드의 '모두 오경보'가 맞지 않을 수 있음: 금지 규칙이 있는 턴에서 명령이 돌았음(v1.7 R5)", out["forbidden_turns_commands"] == 0),
        ("카드의 '하루'가 맞지 않음: 렌더 날짜가 둘 이상", out["render_dates"] <= 1),
        ("실행한 날이 고정한 날(2026-11-22)과 다름: 카드의 '실행 전 같은 날 6번'은 고정한 날이고, README 카드 절이 그렇게 적음", out["run_day_is_the_freeze_day"] is not False),
        (f"R8 모양의 명령 {shapes}개: 그 턴의 불일치는 R8로 셈(기계 라벨은 그대로, v1.7 R8)", shapes == 0),
    ) if not holds]
    return out


def final_word(reasons: list, before: dict):
    """May it be published: the readout's reasons, and the card's rules (PB): no "yes" for a card not to be published."""
    card = (before or {}).get("card") or ""
    if card.startswith("공개 안 함"):
        return [*reasons, f"card: {card} (first-run-card.json publish_rules)"]
    return reasons or "yes, once you agree (live_readout.py --publish, then git add -f)"


def run_all(run: Path, memory_root: Path, log_dir: Path = LOGS, plan: str = PLAN, record: Path | None = None,
            runner=subprocess.run) -> dict:
    done = []
    for step in steps(run, memory_root, log_dir, plan, record):
        assert "--publish" not in step["command"]  # never: publishing is the user's, after the numbers are seen
        result = runner(step["command"], cwd=ROOT, capture_output=True, text=True, timeout=3600)
        if step["output"] and result.stdout.strip():
            (Path(run) / step["output"]).write_text(result.stdout if result.stdout.endswith("\n") else result.stdout + "\n",
                                                    encoding="utf-8")
        done.append({"name": step["name"], "exit": result.returncode, "output": step["output"]})
        if result.returncode not in step["go_on"]:
            reason = (result.stderr or "").strip().splitlines()[-1:] or [f"exit {result.returncode}"]
            return {"done": done, "stopped_at": step["name"], "why": reason[0][:300]}
    return {"done": done, "stopped_at": None}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--plan", default=PLAN)
    parser.add_argument("--memory-root", type=Path, required=True, help="the plan's memory root (ARGUS_LIVE_MEMORY_DIR)")
    parser.add_argument("--log-dir", type=Path, default=LOGS)
    parser.add_argument("--without-person", action="store_true",
                        help="go on before a person read the turns (the readout then refuses to publish; the blind is lost for good)")
    args = parser.parse_args(argv)
    run = BATTERY / args.plan
    if not (run / "manifest.jsonl").is_file():
        print(f"stop: no run in {run} (nothing to read)", file=sys.stderr)
        return 4
    import live_witness as W

    memory_root, log_dir = args.memory_root.resolve(), args.log_dir.resolve()  # the readers run with cwd = the repo
    done = W.finished(run, memory_root)  # the witness after the run is written once: only for a run that ended
    if not done["ok"]:
        print(f"stop: {'; '.join(done['why'])} (an empty --memory-root, say, from a shell without ARGUS_LIVE_MEMORY_DIR)",
              file=sys.stderr)
        return 4
    if not (run / "person-labels.json").exists() and not args.without_person:  # cycle 19 (RD): the blind cannot be undone
        print("stop: no person read the turns yet: python argus_hook/live_read.py --memory-root … first (it computes no "
              "machine label before the person's); --without-person goes on without it, and the readout will not publish",
              file=sys.stderr)
        return 4
    result = run_all(run, memory_root, log_dir, args.plan)
    if result["stopped_at"] is None:
        import live_readout as RO

        readout = json.loads((run / "live-run.json").read_text(encoding="utf-8"))
        result["before_publishing"] = before_publishing(run, memory_root)  # what the card's sentences stand on (counts only)
        result["may_publish"] = final_word(RO.may_publish(readout), result["before_publishing"])
        (run / "before-publishing.json").write_text(json.dumps(result["before_publishing"], ensure_ascii=False, indent=1) + "\n",
                                                    encoding="utf-8")  # counts only: the trace of what was seen before deciding
        result["next"] = ["commit and push the witness after-file if it is not yet", "read <run>/live-run.json",
                          "publish only after agreeing: python argus_hook/live_readout.py --run <run> --memory-root <root> --publish"]
    print(json.dumps(result, ensure_ascii=False, indent=1))
    return 0 if result["stopped_at"] is None else 1


if __name__ == "__main__":
    raise SystemExit(main())

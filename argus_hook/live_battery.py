"""Run the cases of a fixed live-chat plan through the local dashboard API, one task at a time.

The plan (reports/live-agent/first-run-plan.md) and its case list (first-run-cases.json) are fixed before the run.
This script only drives the API the page uses (each task loads gpt-oss-20b on the GPU and unloads it afterwards), so
it needs the user's go-ahead for a GPU run. Start the dashboard server with a memory root of the plan's own
(ARGUS_LIVE_MEMORY_DIR) so the run never mixes with the user's memory; the first and last tasks clear the sandbox's
memory folder (/workspace/.agent), and the user's server writes the user's memory back at its next memory turn.

Per turn it writes one line of numbers and short labels to <out>/manifest.jsonl (no request, answer, command or
output text: those stay in the conversations and task records). A run that stops can be started again: finished
turns are skipped. It stops when a turn's workspace holds scenario files (residue), as the plan says.

    python argus_hook/live_battery.py --cases reports/live-agent/first-run-cases.json --dry-run
    python argus_hook/live_battery.py --cases reports/live-agent/first-run-cases.json --api http://127.0.0.1:8765
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
ARMS = ("no_monitor_notice", "memory_effort_low", "hint_v5")  # agent_memory.ARMS (this script imports no model code)


def load_cases(path: Path) -> dict:
    """The case list, checked: every turn has a task, steps within 1..10, a seed; continuations name earlier cases."""
    plan = json.loads(path.read_text(encoding="utf-8"))
    seen: set[str] = set()
    for case in plan.get("cases") or []:
        if not case.get("id") or case["id"] in seen:
            raise ValueError(f"case id missing or repeated: {case.get('id')}")
        target = case.get("conversation", "new")
        if target != "new" and target not in seen:
            raise ValueError(f"{case['id']}: conversation {target} is not an earlier case")
        for turn in case.get("turns") or []:
            if not str(turn.get("task") or "").strip() and turn.get("last_turn") not in ("retry", "resume"):
                raise ValueError(f"{case['id']}: a turn without a task")
            if not 1 <= int(turn.get("max_steps", 3)) <= 10 or not isinstance(turn.get("seed"), int):
                raise ValueError(f"{case['id']}: max_steps 1..10 and an integer seed are required")
            unknown = [arm for arm in turn.get("arms") or case.get("arms") or [] if arm not in ARMS]
            if unknown:
                raise ValueError(f"{case['id']}: unknown arms {unknown}")
        seen.add(case["id"])
    if not seen:
        raise ValueError("the plan has no cases")
    return plan


class Api:
    def __init__(self, base: str):
        self.base = base.rstrip("/")

    def call(self, path: str, body: dict | None = None, timeout: float = 60) -> tuple[int, dict]:
        data = None if body is None else json.dumps(body).encode()
        request = Request(self.base + path, data=data,
                          headers={"Content-Type": "application/json"} if data else {})  # no Origin: the local page
        try:
            with urlopen(request, timeout=timeout) as response:
                return response.status, json.loads(response.read())
        except HTTPError as error:
            return error.code, json.loads(error.read() or b"{}")


def follow(api: Api, session: str, after: int, limit: float = 3_600) -> list[dict]:
    """The task's events up to its task_end, with the worker's own events (loading, ready: they carry no session,
    the worker sends them before it gets the task)."""
    events, seq, deadline = [], after, time.monotonic() + limit
    while time.monotonic() < deadline:
        status, data = api.call(f"/api/live/events?after={seq}&wait=20", timeout=40)
        if status != 200:
            raise RuntimeError(f"events: HTTP {status}")
        for event in data.get("events") or []:
            seq = max(seq, int(event.get("seq") or seq))
            if event.get("session") == session or (event.get("type") == "worker" and not event.get("session")):
                events.append(event)  # task_queued carries the session too (the load time counts from it)
                if event.get("type") == "task_end":
                    return events
        if not data.get("events") and not data.get("busy"):
            break
    raise RuntimeError("the task did not end (no task_end event)")


def summary(events: list[dict]) -> dict:
    """Numbers of one turn from its events: load and step times, tokens, refusals, notes, memory changes."""
    out = {"load_seconds": None, "steps": [], "format_failures": 0, "first_command_is_ls": None, "tail_notes": 0,
           "repeat_notes": 0, "loose": [], "memory_changes": {}, "memory_step_seconds": 0.0}
    phases: dict[int, str] = {}
    queued = None
    for event in events:
        kind = event.get("type")
        if event.get("sealed") or (kind == "fakenet" and event.get("argus")):
            out["sealed"] = True  # sealed from the gateway's log (between commands, between turns): counted apart
        if kind == "task_queued":
            queued = event.get("time")
        elif kind == "worker" and event.get("state") == "ready":
            # from the moment the task was sent (process start and imports too), else the worker's own count
            out["load_seconds"] = (round(event["time"] - queued, 2) if queued and event.get("time")
                                   else event.get("seconds"))
            out["versions"] = event.get("versions")  # libraries and GPU: the run stops when they change
        elif kind == "memory_context":
            out["memory_context_sha"] = event.get("context_sha")
            out["memory_blocks"] = event.get("blocks")
        elif kind == "hint":
            out["hint_step"] = event.get("step")  # the step told it is the last one
        elif kind == "task_start":
            out["run_id"] = event.get("run_id")
        elif kind == "context":
            out["context"] = {key: event.get(key) for key in ("version", "memory", "history_turns", "context_turns",
                                                              "features", "context_sha", "code", "blocks", "render_date")}
            out["context"]["emp_sha"] = (event.get("emp") or {}).get("manifest_sha")
            out["residue"] = bool((event.get("workspace") or {}).get("canary"))
            out["listing_sha"] = (event.get("workspace") or {}).get("listing_sha")  # pairs compare like with like
            out["strays"] = (event.get("workspace") or {}).get("strays")
        elif kind == "step_start":
            phases[int(event.get("step") or 0)] = event.get("phase") or "main"
        elif kind == "attempt_failed":
            out["format_failures"] += 1
            out["format_failure_seconds"] = round(out.get("format_failure_seconds", 0.0)
                                                  + float(event.get("seconds") or 0), 2)
        elif kind == "action":
            phase = phases.get(int(event.get("step") or 0), "main")
            row = {"step": event.get("step"), "phase": phase, "kind": event.get("kind"),
                   "generation_seconds": event.get("seconds"), "prompt_tokens": event.get("prompt_tokens"),
                   "generated_tokens": event.get("generated_tokens"), "attempt": event.get("attempt"),
                   "prompt_sha": event.get("prompt_sha"), "generated_sha": event.get("generated_sha")}
            out["steps"].append(row)
            if event.get("loose"):
                out["loose"].append(event["loose"])
            if phase == "main" and event.get("kind") == "bash" and out["first_command_is_ls"] is None:
                out["first_command_is_ls"] = str(event.get("command") or "").strip().split(" ")[0] in ("ls", "find", "tree")
        elif kind == "verdict":
            for row in reversed(out["steps"]):
                if row["step"] == event.get("step"):
                    row.update(judge_seconds=event.get("seconds"), score=event.get("score"),
                               alarm=bool(event.get("alarm_5")) and not event.get("report_kind"),
                               error=event.get("error"))
                    break
        elif kind == "observation":
            out["tail_notes"] += int(bool(event.get("tail_note")))
            if event.get("argus_page"):  # the sealed scenario pages under http://fakenet/argus/: counted apart
                out["argus_pages"] = out.get("argus_pages", 0) + 1
            for row in reversed(out["steps"]):
                if row["step"] == event.get("step"):
                    row.update(run_seconds=event.get("seconds"), seen_sha=event.get("seen_sha"))
                    break
        elif kind == "memory" and event.get("action") == "error":
            out.setdefault("memory_errors", []).append(event.get("stage") or "?")  # the memory path failed here
        elif kind == "memory" and event.get("blocked") and not event.get("recovered"):
            # the sandbox stopped running commands (a plan turn is never put back): not a result of the case
            out["blocked"], out["blocked_stage"] = event["blocked"], event.get("stage")
        elif kind == "memory" and event.get("action") == "cleared":
            out["cleared"] = bool(event.get("cleared"))
        elif kind == "note" and event.get("note") == "repeat_note":
            out["repeat_notes"] += 1
        elif kind == "memory" and event.get("action") == "saved":
            out["memory_changes"] = {name: {key: change.get(key) for key in ("added", "removed", "auto", "review",
                                                                             "duplicates", "reasons")}
                                     for name, change in (event.get("changes") or {}).items()}
        elif kind == "task_end":
            out.update(termination=event.get("termination"), step_count=event.get("steps"),
                       alarms=event.get("alarms"), memory_alarms=event.get("memory_alarms"))
    # the memory step's time: generating, judging and running its command(s)
    out["memory_step_seconds"] = round(sum(float(row.get(key) or 0) for row in out["steps"] if row["phase"] == "memory"
                                           for key in ("generation_seconds", "judge_seconds", "run_seconds")), 2)
    return out


def stored_turn(api: Api, cid: str, run_id: str | None, wait: float = 30) -> dict:
    """The turn of this run as the API stored it (the recorder stores it right after the task ends)."""
    deadline = time.monotonic() + wait
    while time.monotonic() < deadline and run_id:
        status, data = api.call(f"/api/live/conversations/{cid}")
        if status == 200:
            found = next((item for item in data.get("turns") or [] if item.get("run_id") == run_id), None)
            if found:
                return found
        time.sleep(1)
    return {}


class Stop(RuntimeError):
    """The plan stops here: the turn is not marked done, so the next run starts with it."""


def run_turn(api: Api, plan: dict, case: dict, turn: dict, cid: str | None, started_hook=None) -> dict:
    battery = {"plan": plan.get("plan"), "case": case["id"], "arm": case.get("arm"),
               "arms": list(turn.get("arms") or case.get("arms") or []), "seed": int(turn["seed"])}
    if turn.get("clear_memory"):
        battery["clear_memory"] = True
    body = {"task": turn.get("task") or "이어서 진행해 줘", "max_steps": int(turn.get("max_steps", 3)),
            "memory": bool(turn.get("memory", True)), "battery": battery}
    if cid:
        body["conversation"] = cid
    if turn.get("last_turn"):
        body["last_turn"] = turn["last_turn"]
    status, started = api.call("/api/live/start", body)
    if status == 400 and started.get("code") == "not_resumable":  # the turn before answered: recorded, the plan goes on
        return {"case": case["id"], "group": case.get("group"), "arm": case.get("arm"), "skipped": True,
                "reason": "not_resumable", "last_turn": turn.get("last_turn"), "conversation": cid,
                "time": round(time.time(), 3)}
    if status != 202:  # GPU busy, sandbox not ready, a refused field...: stop, the turn is not done
        raise Stop(f"{case['id']}: start failed (HTTP {status}, {started.get('code')}): {started.get('error')}")
    if started_hook:
        started_hook(started)
    events = follow(api, started["session"], int(started.get("after") or 0))
    numbers = summary(events)
    conversation = started.get("conversation") or {}
    if numbers.get("termination") not in ("stop", "max_steps", "format_failure"):  # a refused format is a result
        raise Stop(f"{case['id']}: the task ended with {numbers.get('termination')}")  # error, worker, cancel
    if turn.get("clear_memory") and not numbers.get("cleared"):
        raise Stop(f"{case['id']}: the sandbox's memory folder was not cleared")
    failed = [stage for stage in numbers.get("memory_errors") or [] if stage in ("load", "save", "before_step")]
    if body["memory"] and ((numbers.get("context") or {}).get("memory") != "on" or failed):
        # a memory arm that ran without its memory (or lost its save) measured a condition the plan did not set
        raise Stop(f"{case['id']}: the memory path failed ({', '.join(failed) or 'not loaded'}): this turn did not measure "
                   "what the plan set. Run the plan again (today): it runs again as a retry")
    if numbers.get("blocked"):  # its last command (or its memory step) left a workspace sandbox.py cannot snapshot
        raise Stop(f"{case['id']}: the sandbox stopped running commands ({numbers['blocked']}, at "
                   f"{numbers.get('blocked_stage') or 'a step'}). Put it back from the local page (기억 카드 → 샌드박스 점검 → "
                   "마지막 정상 상태로), then run the plan again: this turn runs again as a retry")
    record = stored_turn(api, conversation.get("id"), numbers.get("run_id")) if conversation.get("id") else {}
    single = len(case.get("turns") or []) <= 1  # a case's pair names its only turn, never the base of a two-turn case
    return {"case": case["id"], "group": case.get("group"), "arm": case.get("arm"), "arms": battery["arms"],
            "pair": turn.get("pair") or (case.get("pair") if single else None),
            "role": turn.get("role") or (case.get("role") if single else None),
            "seed": battery["seed"], "max_steps": body["max_steps"], "memory": body["memory"],
            "last_turn": turn.get("last_turn"), "conversation": conversation.get("id"), "turn": conversation.get("turn"),
            "run_id": record.get("run_id"), "condition": record.get("condition"), **numbers,
            "time": round(time.time(), 3)}


FROZEN = ("argus_hook/live_battery.py", "argus_hook/live_report.py", "argus_hook/live_rescore.py", "argus_hook/live_agent.py",
          "argus_hook/agent_memory.py", "argus_hook/dashboard_server.py", "argus_hook/live_agent_service.py",
          "argus_hook/scenario_rollout.py", "argus_hook/action_repair.py", "argus_hook/chunked_attention.py",
          "argus_hook/load_full_model_CUDA.py", "src/argus_v/agent_actions.py", "src/argus_v/activations",
          "experiments/risk_loop/argus_loop/argus_v_emp_model.py", "experiments/risk_loop/argus_loop/build_features.py",
          # the scoring path imports these too (robust_scale, LearnedEmbedding and their helpers, and the modules
          # argus_v_p imports in turn); a test lists what loading Argus-V-emp, the prompt and the tokenizer opens
          "experiments/risk_loop/argus_loop/argus_v_em.py", "experiments/risk_loop/argus_loop/argus_v_p.py",
          "experiments/risk_loop/argus_loop/evaluate.py", "experiments/risk_loop/argus_loop/final_models.py",
          "experiments/risk_loop/argus_loop/iter01_common.py", "experiments/risk_loop/argus_loop/iter02_common.py",
          "experiments/risk_loop/argus_loop/iter04_common.py", "experiments/risk_loop/argus_loop/iter04_models.py",
          "experiments/risk_loop/argus_loop/iter05_common.py", "experiments/risk_loop/argus_loop/iter05_models.py",
          "experiments/risk_loop/argus_loop/iter05_scan.py", "experiments/risk_loop/argus_loop/iter06_models.py",
          "experiments/risk_loop/argus_loop/iter06_scan.py", "experiments/risk_loop/argus_loop/iter07_models.py",
          "experiments/risk_loop/argus_loop/iter09_models.py", "experiments/risk_loop/argus_loop/models.py",
          "experiments/risk_loop/argus_loop/obs_cache.py", "experiments/risk_loop/argus_loop/obs_models.py",
          "experiments/risk_loop/argus_loop/obs_models_s.py", "experiments/risk_loop/argus_loop/obs_models_s0f.py",
          "experiments/risk_loop/argus_loop/t7a_rf.py", "experiments/risk_loop/argus_loop/within_tool.py",
          "experiments/risk_loop/harness.py", "experiments/__init__.py", "experiments/risk_loop/__init__.py",
          "experiments/risk_loop/argus_loop/__init__.py", "src/argus_v/__init__.py",
          "artifacts/risk-loop/resplit-1117/argus_v_emp", "gpt-oss-20b/chat_template.jinja",
          # the tokenizer and model config shape every prompt's ids; every page under sites/ goes into the system prompt
          "gpt-oss-20b/tokenizer.json", "gpt-oss-20b/tokenizer_config.json", "gpt-oss-20b/special_tokens_map.json",
          "gpt-oss-20b/config.json", "gpt-oss-20b/generation_config.json", "SANDBOX/sandbox.py",
          # the sandbox's own limits and network (time limits, the snapshot limit, fakenet)
          "SANDBOX/settings.json",
          # the fake internet whole: its server and routes.json decide what each page answers, not only the pages
          "SANDBOX/fakenet", "reports/live-agent/first-run-plan.md",
          # the measured equivalence of the scikit-learn that loads the scoring models with the one that pickled them
          "artifacts/risk-loop/argus-v-emp-new-1118-nosealed/sklearn_check.json", "reports/live-agent/scorer-equivalence.json")
# Everything that shapes the context, the verdicts (code, weights, the chat template that renders every prompt) or the
# sandbox; a folder stands for every file in it.


def fingerprint(cases: Path) -> dict:
    """sha256 of the case list, the plan and the code the run goes through, and the git HEAD."""
    import hashlib
    import subprocess

    files = {str(cases.resolve().relative_to(ROOT)) if cases.resolve().is_relative_to(ROOT) else str(cases): cases}
    for name in FROZEN:
        path = ROOT / name
        if path.is_dir():  # every file of a folder, by its own path
            files.update({str(item.relative_to(ROOT)): item for item in sorted(path.rglob("*"))
                          if item.is_file() and "__pycache__" not in item.parts})
        else:
            files[name] = path
    hashes = {name: hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None
              for name, path in sorted(files.items())}
    try:
        head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True, timeout=10).stdout.strip()
    except (OSError, subprocess.SubprocessError):
        head = None
    return {"files": hashes, "git_head": head or None}


FROZEN_COPY_LIMIT = 5 * 2**20  # bytes: larger locked files (weights) are kept as hashes only
COPY_ANYWAY = {"gpt-oss-20b/tokenizer.json": 32 * 2**20}  # the tokenizer: a rescoring renders every prompt with it
NOT_COPIED = ("SANDBOX/fakenet",)  # it serves the sealed scenario pages: hashed in the lock, never copied
TURN_SECONDS = 210  # about one turn: loading the model (1-2 minutes) and its steps


def freeze_copy(out: Path, files: dict) -> dict:
    """The locked files as they are at the freeze, under <out>/frozen/ (outside git): the run's code is kept even
    when it was never committed. -> what was copied, kept as a hash only, and the uncommitted locked files."""
    import shutil
    import subprocess

    copied, large, held = 0, [], []
    for name in files:
        path = Path(name) if Path(name).is_absolute() else ROOT / name  # a case list outside the repository
        if any(name == part or name.startswith(part + "/") for part in NOT_COPIED):
            held.append(name)
            continue
        if not path.is_file():
            continue
        if path.stat().st_size > COPY_ANYWAY.get(name, FROZEN_COPY_LIMIT):
            large.append(name)
            continue
        target = out / "frozen" / (str(Path("outside") / Path(name).relative_to("/")) if Path(name).is_absolute() else name)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)
        copied += 1
    try:  # locked files git does not hold as they are now: the request asks whether to commit first; files git
        # ignores (the chat template, the tokenizer, the scorer check) a commit would not hold either
        status = subprocess.run(["git", "status", "--porcelain", "--untracked-files=all", "--ignored", "--",
                                 *sorted(name for name in files if not Path(name).is_absolute())],
                                cwd=ROOT, capture_output=True, text=True, timeout=30).stdout
        uncommitted = sorted({line[3:].strip() for line in status.splitlines() if not line.startswith("!!") and line[3:].strip()})
        outside_git = sorted({line[3:].strip() for line in status.splitlines() if line.startswith("!!") and line[3:].strip()})
    except (OSError, subprocess.SubprocessError):
        uncommitted = outside_git = None
    return {"copied": copied, "hash_only_large": large, "hash_only_sealed": len(held), "uncommitted": uncommitted,
            "outside_git": outside_git}


def split_pairs(cases: list[dict], done: list[str]) -> list[str]:
    """The pairs some of whose turns ran and some not: a pair split across two days compares two dates."""
    ran, left = set(), set()
    for case in cases:
        single = len(case.get("turns") or []) <= 1
        for index, turn in enumerate(case.get("turns") or [], start=1):
            pair = turn.get("pair") or (case.get("pair") if single else None)
            if pair:
                (ran if f"{case['id']}.{index}" in done else left).add(pair)
    return sorted(ran & left)


def crosses_midnight(turns_left: int, now: float | None = None, per_turn: float = TURN_SECONDS) -> bool:
    """Whether the turns still to run would end on another day than they start: the date is in every prompt."""
    now = time.time() if now is None else now
    return turns_left > 0 and time.strftime("%Y-%m-%d", time.localtime(now)) != \
        time.strftime("%Y-%m-%d", time.localtime(now + turns_left * per_turn))


def lock_sha(lock: dict) -> str:
    """One hash of a lock (its file hashes, git HEAD and plan): what every line of the run carries."""
    import hashlib

    body = {key: lock.get(key) for key in ("plan", "files", "git_head")}
    return hashlib.sha256(json.dumps(body, sort_keys=True).encode("utf-8")).hexdigest()[:16]


def clear_sandbox(api: Api, strict: bool = True) -> dict:
    """The sandbox's memory folder emptied by the API itself (no model): the plan starts and ends with it gone.
    ``strict`` (the start) also stops on processes left running or scenario files; at the end those are reported."""
    status, body = api.call("/api/live/sandbox/clear", {})
    if status != 200 or not body.get("cleared"):
        raise Stop(f"the sandbox's memory folder was not cleared (HTTP {status}): {body.get('error') or body}")
    if not strict:
        if body.get("strays") or body.get("canary"):
            print(f"note: after the plan the sandbox holds {body.get('strays') or 0} left-over process(es)"
                  f"{' and scenario files' if body.get('canary') else ''}", file=sys.stderr)
        return body
    if body.get("strays"):
        raise Stop(f"{body['strays']} process(es) left by earlier commands run in the sandbox "
                   f"({', '.join(body.get('stray_names') or [])}); stop them first")
    if body.get("canary"):
        raise Stop("the workspace holds scenario files (residue); clear /workspace before the plan runs")
    if body.get("hooks"):
        raise Stop(f"python/git hooks under the sandbox's HOME ({', '.join(body.get('hook_names') or [])}); remove them first")
    if body.get("entries"):
        raise Stop(f"/workspace holds {body['entries']} entries; the plan starts from an empty workspace "
                   "(snapshot it first, then empty it; see the plan's procedure)")
    return body


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--cases", type=Path, default=ROOT / "reports" / "live-agent" / "first-run-cases.json")
    parser.add_argument("--api", default="http://127.0.0.1:8765")
    parser.add_argument("--out", type=Path, default=None, help="default: artifacts/live-agent/battery/<plan>")
    parser.add_argument("--only", default="", help="comma-separated case ids")
    parser.add_argument("--dry-run", action="store_true", help="check the case list and print the plan; no API calls")
    parser.add_argument("--freeze", action="store_true", help="write the lock (hashes of the plan, cases and code)")
    parser.add_argument("--turn-seconds", type=int, default=TURN_SECONDS, help="about one turn, for the midnight check")
    args = parser.parse_args(argv)
    plan = load_cases(args.cases)
    only = {item for item in args.only.split(",") if item}
    cases = [case for case in plan["cases"] if not only or case["id"] in only]
    turns = sum(len(case.get("turns") or []) for case in cases)
    print(f"plan {plan.get('plan')}: {len(cases)} cases, {turns} turns")
    if args.dry_run:
        for case in cases:
            for index, turn in enumerate(case.get("turns") or [], start=1):
                print(f"  {case['id']}.{index} [{case.get('group')}/{case.get('arm') or '-'}] steps {turn.get('max_steps', 3)} "
                      f"seed {turn['seed']} memory {'on' if turn.get('memory', True) else 'off'}"
                      f"{' ' + turn['last_turn'] if turn.get('last_turn') else ''}"
                      f"{' arms ' + ','.join(turn.get('arms') or case.get('arms') or []) if (turn.get('arms') or case.get('arms')) else ''}"
                      f"{' clear' if turn.get('clear_memory') else ''} · {case.get('conversation', 'new')}")
        return 0
    out = args.out or ROOT / "artifacts" / "live-agent" / "battery" / str(plan.get("plan") or "plan")
    out.mkdir(parents=True, exist_ok=True)
    lock_path = out / "lock.json"
    if args.freeze:
        if lock_path.is_file():  # a plan is frozen once: a changed plan is a new plan (a new id, a new folder)
            print(f"stop: {lock_path} exists; give the changed plan a new plan id instead of freezing again", file=sys.stderr)
            return 4
        lock = {"plan": plan.get("plan"), **fingerprint(args.cases), "time": round(time.time(), 3)}
        lock["frozen"] = freeze_copy(out, lock["files"])
        lock_path.write_text(json.dumps(lock, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"frozen: {lock_path} · copies of {lock['frozen']['copied']} files under {out / 'frozen'}"
              + (f" · not committed: {len(lock['frozen']['uncommitted'])} locked files (commit them first?)"
                 if lock["frozen"].get("uncommitted") else "")
              + (f" · git ignores {len(lock['frozen']['outside_git'])} locked files (kept in frozen/ or as hashes only)"
                 if lock["frozen"].get("outside_git") else ""))
        return 0
    if not lock_path.is_file():
        print("stop: freeze the plan first (--freeze), so the run is checked against what was fixed before it", file=sys.stderr)
        return 4
    lock = json.loads(lock_path.read_text(encoding="utf-8"))
    now = fingerprint(args.cases)
    changed = [name for name, digest in now["files"].items() if lock.get("files", {}).get(name) != digest]
    if changed:
        print(f"stop: changed since the plan was frozen: {', '.join(changed)}", file=sys.stderr)
        return 4
    state_path, manifest = out / "state.json", out / "manifest.jsonl"
    state = json.loads(state_path.read_text(encoding="utf-8")) if state_path.is_file() else {"done": [], "conversations": {}}
    left = sum(1 for case in cases for index, _ in enumerate(case.get("turns") or [], start=1)
               if f"{case['id']}.{index}" not in state["done"])
    if crosses_midnight(left, per_turn=args.turn_seconds):  # the render date is in every prompt: one day per run
        print(f"stop: {left} turns (about {left * args.turn_seconds // 60} minutes) would run past midnight; "
              "start after midnight or early enough in the day", file=sys.stderr)
        return 4
    api = Api(args.api)

    def save_state() -> None:
        state_path.write_text(json.dumps(state, ensure_ascii=False, indent=1), encoding="utf-8")

    def keep(line: dict) -> None:
        with manifest.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps({**line, "lock_sha": state.get("lock_sha")}, ensure_ascii=False) + "\n")
        save_state()

    status, store = api.call("/api/live/store")
    if status != 200 or not store.get("custom"):
        print("stop: the server keeps the user's own memory; start it with ARGUS_LIVE_MEMORY_DIR for this plan",
              file=sys.stderr)
        return 2
    scorer = store.get("scorer") or {}
    if not scorer.get("equivalent"):
        # the verdicts would come from Argus-V-emp models unpickled by another scikit-learn than the one they were
        # made with, with no measurement showing the same scores (or the pickles differ from the bundle's hashes)
        print(f"stop: scikit-learn {scorer.get('sklearn')} would load the Argus-V-emp models pickled with "
              f"{', '.join(scorer.get('pickled') or []) or '?'} and no equivalence was measured "
              f"{scorer.get('error') or ''}{' changed pickles: ' + ', '.join(scorer['bad_hash']) if scorer.get('bad_hash') else ''}",
              file=sys.stderr)
        return 4
    stale = [name for name, digest in (store.get("code") or {}).items() if lock["files"].get(name) != digest]
    if stale:  # the server started before the code was frozen (or the files changed since it started)
        print(f"stop: the running server's code differs from the lock: {', '.join(stale)}; restart the server", file=sys.stderr)
        return 4
    sealed = lock_sha(lock)
    if not state["done"]:  # a fresh run: the plan's own memory root, still empty
        if store.get("conversations"):
            print("stop: the server's memory root already holds conversations; use an empty one", file=sys.stderr)
            return 2
        state["store"], state["lock_sha"] = store["id"], sealed
    elif state.get("store") != store["id"]:
        print("stop: the server keeps a different memory root than the one this run started with", file=sys.stderr)
        return 2
    elif state.get("lock_sha") != sealed:  # the run began under another lock (one removed and frozen again)
        print("stop: this run began under a different lock; a changed plan is a new plan with a new folder", file=sys.stderr)
        return 4
    code = 0
    try:
        if "clear:start" not in state["done"]:
            keep({"case": "clear-start", **clear_sandbox(api), "time": round(time.time(), 3), "lock": lock.get("files"),
                  "scorer": scorer})  # what the run relied on for the scorer (the same version, or the measurement)
            state["done"].append("clear:start")
            save_state()
        def unchanged() -> None:  # before every turn: nothing the run goes through has changed since the freeze
            moved = [name for name, digest in fingerprint(args.cases)["files"].items() if lock["files"].get(name) != digest]
            if moved:
                raise Stop(f"changed during the run: {', '.join(moved)}")
            today = time.strftime("%Y-%m-%d")
            if state.get("render_date") and state["render_date"] != today:  # the date is in every prompt
                split = split_pairs(cases, state["done"])
                if split:  # a pair with turns on both days would compare two dates
                    raise Stop(f"the run began on {state['render_date']} and today is {today}, and the pairs "
                               f"{', '.join(split)} have turns on both days: every prompt holds the date. Finish a run "
                               "on the day it began, or start a new plan (a new plan id and folder)")
                state.setdefault("render_dates", [state["render_date"]]).append(today)  # whole pairs on another day
                state["render_date"] = today

        code = run_cases(api, plan, cases, state, keep, save_state, unchanged)
    except Stop as stop:
        print(f"stop: {stop}", file=sys.stderr)
        code = 3
    finally:
        try:  # always leave the sandbox without the plan's memory, so the user's server does not find it there
            cleared = clear_sandbox(api, strict=False)
            if code == 0 and "clear:end" not in state["done"]:
                state["done"].append("clear:end")
                keep({"case": "clear-end", **cleared, "time": round(time.time(), 3)})
        except (Stop, RuntimeError, OSError) as error:
            print(f"could not clear the sandbox's memory folder: {error}. Clear /workspace/.agent before the next task "
                  "of your own server.", file=sys.stderr)
            code = code or 3
    if code == 0:
        request = Request(f"{api.base}/api/live/export?format=jsonl&conversation=all")
        with urlopen(request, timeout=60) as response:
            (out / "verdicts.jsonl").write_bytes(json.dumps({"lock_sha": sealed, "plan": plan.get("plan"),
                                                             "versions": state.get("versions")}).encode("utf-8")
                                                 + b"\n" + response.read())
        print("done")
    return code


def run_cases(api: Api, plan: dict, cases: list[dict], state: dict, keep, state_path_write,
              unchanged=lambda: None) -> int:
    for case in cases:
        target = case.get("conversation", "new")
        cid = None if target == "new" else state["conversations"].get(target)
        if case.get("reset_memory") and f"{case['id']}.1" not in state["done"]:
            # pairs that compare the memory step start from the same memory: the default files
            for name in ("USER.md", "NOTES.md"):
                status, body = api.call("/api/live/memory", {"name": name, "text": None})
                if status != 200:
                    raise Stop(f"{case['id']}: could not reset {name} (HTTP {status}): {body.get('error')}")
        if target != "new" and not cid:
            print(f"skip {case['id']}: case {target} has not run", file=sys.stderr)
            continue
        for index, turn in enumerate(case.get("turns") or [], start=1):
            key = f"{case['id']}.{index}"
            if key in state["done"]:
                cid = state["conversations"].get(case["id"], cid)
                continue
            unchanged()
            pending = state.get("pending") or {}
            if pending.get("key") == key and pending.get("conversation"):
                # it stopped here last time. If the stopped attempt was stored, it is redone as a retry (the failed
                # attempt moves out of the context); if not (the server stopped before storing it), it runs as new.
                cid = pending["conversation"]
                status, data = api.call(f"/api/live/conversations/{cid}")
                stored = status == 200 and any(item.get("turn") == pending.get("turn") for item in data.get("turns") or [])
                if stored:
                    turn = {**turn, "last_turn": "retry"}

            def started(reply, key=key):
                conversation = reply.get("conversation") or {}
                state["pending"] = {"key": key, "conversation": conversation.get("id"), "turn": conversation.get("turn")}
                state_path_write()

            line = run_turn(api, plan, case, turn, cid, started)
            versions = line.get("versions")
            if versions and state.get("versions") and versions != state["versions"]:
                moved = sorted(key for key in set(versions) | set(state["versions"]) if versions.get(key) != state["versions"].get(key))
                raise Stop(f"{key}: the libraries or the GPU changed during the run ({', '.join(moved)})")
            if versions and not state.get("versions"):
                state["versions"] = versions
            rendered = (line.get("context") or {}).get("render_date")
            if rendered and not state.get("render_date"):
                state["render_date"] = rendered  # the day of the run (resuming on another day stops)
            state.pop("pending", None)
            cid = line.get("conversation") or cid
            state["conversations"][case["id"]] = cid
            state["done"].append(key)
            keep(line)
            print(f"{key}: {line.get('termination')} · steps {line.get('step_count')} · alarms {line.get('alarms')}")
            if line.get("residue"):
                raise Stop("the workspace holds scenario files (residue); the plan stops here")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

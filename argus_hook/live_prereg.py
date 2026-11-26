"""Pre-registration of what reads the first GPU run's results (cycles 13-14): the outcome rules and the tool that
applies them (P1), the counterfactual-rescoring tool and its plan (R2). --freeze keeps their sha256 and the time,
against the plan's lock (its lock_sha), in the git-ignored artifacts folder and in a tracked copy under
reports/live-agent/ (so the record can be committed and checked by others). It refuses once the run has begun (a
first line in its manifest, or its state file): a rule fixed after the run began is not pre-registered. Until then it
may be frozen again (--replace, with --reason), the earlier freezes kept in it.

--check says whether the files are still the frozen ones, whether the freeze came before the run, and, when a tool
passes what it actually read (`used`, the cases, the run), whether those are the frozen ones too: a label computed
from a changed copy of the rules or the tool is not pre-registered.

    python argus_hook/live_prereg.py --freeze                       # before the run (first-run plan §8 step 3)
    python argus_hook/live_prereg.py --freeze --replace --reason "…" # again, before the run only
    python argus_hook/live_prereg.py --check                        # {"preregistered", "post_hoc", "changed", ...}
    python argus_hook/live_prereg.py --check --arm                  # right before the run: no freeze after this

Arming (cycle 15) leaves armed.json next to the lock when the check passes; from then on --freeze refuses, even if
the run's own state and manifest were removed: a rule cannot be fixed again once the run was about to begin. Since
cycle 16 it arms only when the tracked copy is, as it is now, in a commit that is on a remote branch (record.anchored
and record.pushed): a run armed before the push could never be published as pre-registered; since cycle 17 only when
live_go.py says go too (the server, the sandbox, the weights and the image, checked before the one arming).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "argus_hook"))
FILES = ("reports/live-agent/agent-outcomes.json", "argus_hook/live_outcomes.py", "argus_hook/live_counterfactual.py",
         "reports/live-agent/rescore-plan.md", "argus_hook/live_prereg.py", "argus_hook/live_readout.py",
         "argus_hook/live_witness.py",  # cycle 16: the witness of what the lock does not hash, before and after the run
         "argus_hook/live_read.py")  # cycle 18: a person reads the turns blind after the run
BATTERY = ROOT / "artifacts" / "live-agent" / "battery"
OUT = ROOT / "artifacts" / "live-agent" / "prereg"
RECORD = ROOT / "reports" / "live-agent"  # the tracked copy: prereg-<plan>.json
CASES = "reports/live-agent/first-run-cases.json"
PLAN = "first-run-v1.6"


def digest(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def run_began(run_dir: Path) -> float | None:
    """When the run began: the time of the first line it kept, or (fail closed) when its state file was written; None
    before either exists."""
    try:
        lines = (Path(run_dir) / "manifest.jsonl").read_text(encoding="utf-8").splitlines()
    except OSError:
        lines = []
    for line in lines:
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(row, dict) and isinstance(row.get("time"), (int, float)):
            return float(row["time"])
    state = Path(run_dir) / "state.json"
    if lines or state.exists():  # a manifest without a readable time, or a run that wrote its state first
        try:
            return float(state.stat().st_mtime) if state.exists() else float((Path(run_dir) / "manifest.jsonl").stat().st_mtime)
        except OSError:
            return 0.0
    return None


def lock_of(battery: Path, plan: str) -> dict:
    return json.loads((Path(battery) / plan / "lock.json").read_text(encoding="utf-8"))


def target(battery: Path, plan: str) -> str:
    import live_battery as LB

    return LB.lock_sha(lock_of(battery, plan))


def armed_at(plan: str = PLAN, out: Path = OUT) -> float | None:
    """When it was armed (None: not armed). An armed.json that cannot be read counts as armed (fail closed)."""
    path = Path(out) / plan / "armed.json"
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return float(data.get("time") or 0) if isinstance(data, dict) else 0.0
    except (OSError, json.JSONDecodeError, TypeError, ValueError):
        return 0.0


def armed_record(plan: str = PLAN, out: Path = OUT) -> dict | None:
    try:
        data = json.loads((Path(out) / plan / "armed.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    return data if isinstance(data, dict) else None


def arm(plan: str = PLAN, out: Path = OUT, record: dict | None = None, go: dict | None = None) -> dict:
    """Right before the run: the lock as it is now, the time, the record's state then (the commit holding the tracked
    copy, whether it was on a remote) and what live_go.py said (each check's yes or no): --freeze refuses from then on."""
    lock = Path(out) / plan / "lock.json"
    body = {"plan": plan, "time": round(time.time(), 3), "lock_sha256": digest(lock), "record": record, "go": go}
    (Path(out) / plan / "armed.json").write_text(json.dumps(body, indent=1) + "\n", encoding="utf-8")
    return body


def freeze(plan: str = PLAN, replace: bool = False, battery: Path = BATTERY, out: Path = OUT,
           root: Path = ROOT, record: Path | None = None, reason: str | None = None) -> dict:
    record = Path(record) if record is not None else Path(root) / "reports" / "live-agent"
    armed = armed_at(plan, out)
    if armed is not None:
        raise ValueError(f"armed at {time.strftime('%Y-%m-%d %H:%M', time.localtime(armed))} (the run was about to "
                         "begin): rules fixed now are not pre-registered")
    began = run_began(Path(battery) / plan)
    if began is not None:
        raise ValueError(f"the run of {plan} began at {time.strftime('%Y-%m-%d %H:%M', time.localtime(began))}: "
                         "rules fixed now are not pre-registered (write them as a later analysis)")
    path = Path(out) / plan / "lock.json"
    earlier = json.loads(path.read_text(encoding="utf-8")) if path.is_file() else None
    if earlier is not None and not replace:
        raise ValueError(f"{path} exists; --replace freezes again (only before the run)")
    if earlier is not None and not (reason or "").strip():
        raise ValueError("say why it is frozen again (--reason)")
    missing = [name for name in FILES if not (Path(root) / name).is_file()]
    if missing:
        raise ValueError(f"missing: {', '.join(missing)}")
    body = {"plan": plan, "target_lock_sha": target(battery, plan),
            "files": {name: digest(Path(root) / name) for name in FILES}, "time": round(time.time(), 3)}
    if earlier is not None:
        body["reason"] = reason.strip()
        body["replaces"] = [*earlier.pop("replaces", []), earlier]
    text = json.dumps(body, ensure_ascii=False, indent=1) + "\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    record.mkdir(parents=True, exist_ok=True)
    (record / f"prereg-{plan}.json").write_text(text, encoding="utf-8")  # the copy git keeps
    return body


def anchored(copy: Path, began: float | None, root: Path = ROOT) -> dict:
    """Whether the tracked copy is, as it is now, in a commit made before the run began, and whether that commit is on
    a remote branch (others can check it; a commit's time is this computer's clock). Read-only git; never a condition
    of "preregistered": committing and pushing are the user's."""
    try:
        rel = str(Path(copy).resolve().relative_to(Path(root).resolve()))
        run = lambda *args: subprocess.run(["git", *args], cwd=root, capture_output=True, text=True, timeout=20)
        line = run("log", "-1", "--format=%H %ct", "--", rel).stdout.strip()
        if not line:
            return {"anchored": False, "why": "not committed"}
        commit, when = line.split()
        same = run("show", f"{commit}:{rel}").stdout == Path(copy).read_text(encoding="utf-8")
        before = began is None or float(when) <= began
        pushed = bool(run("branch", "-r", "--contains", commit).stdout.strip())
        # committed_at is this computer's clock: when it reached the remote is the remote's own record
        return {"anchored": same and before, "commit": commit, "committed_at": float(when), "same": same,
                "before_run": before, "pushed": pushed}
    except (OSError, ValueError, subprocess.SubprocessError):
        return {"anchored": False, "why": "git could not be read"}


def check(plan: str = PLAN, battery: Path = BATTERY, out: Path = OUT, root: Path = ROOT, record: Path | None = None,
          used: dict | None = None, cases: Path | None = None, run: Path | None = None) -> dict:
    """``used``: {frozen name: the path a tool actually read}; ``cases``: the case list it read; ``run``: the battery
    folder whose manifest it read. Each must be the frozen one for "preregistered"."""
    record = Path(record) if record is not None else Path(root) / "reports" / "live-agent"
    path = Path(out) / plan / "lock.json"
    if not path.is_file():
        return {"preregistered": False, "reason": "not frozen"}
    lock = json.loads(path.read_text(encoding="utf-8"))
    reasons = []
    copy = record / f"prereg-{plan}.json"
    try:
        if json.loads(copy.read_text(encoding="utf-8")) != lock:  # the whole record, not some of its fields
            reasons.append("the tracked copy differs from the lock")
    except (OSError, json.JSONDecodeError):
        reasons.append("no tracked copy")
    armed = armed_at(plan, out)
    if armed is not None and float(lock.get("time") or 0) > armed:
        reasons.append("frozen after it was armed")
    if armed is not None and (armed_record(plan, out) or {}).get("lock_sha256") != digest(path):
        reasons.append("the lock changed after it was armed")
    files = lock.get("files") or {}
    changed = [name for name, value in files.items()
               if not (Path(root) / name).is_file() or digest(Path(root) / name) != value]
    used_differs = [name for name, where in (used or {}).items()
                    if name not in files or not Path(where).is_file() or digest(Path(where)) != files[name]]
    try:
        matches = target(battery, plan) == lock.get("target_lock_sha")
    except (OSError, ValueError):
        matches = False
    if cases is not None:
        try:
            if digest(Path(cases)) != (lock_of(battery, plan).get("files") or {}).get(CASES):
                reasons.append("the case list read is not the plan's")
        except (OSError, ValueError):
            reasons.append("the plan's lock cannot be read")
    if run is not None:
        shas = set()
        for line in (Path(run) / "manifest.jsonl").read_text(encoding="utf-8").splitlines() \
                if (Path(run) / "manifest.jsonl").is_file() else []:
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            if isinstance(row, dict) and row.get("lock_sha"):
                shas.add(row["lock_sha"])
        if shas - {lock.get("target_lock_sha")}:
            reasons.append("the run's lines were kept under another lock")
    began = run_began(Path(battery) / plan)
    post_hoc = began is not None and float(lock.get("time") or 0) > began
    ok = not changed and not used_differs and matches and not post_hoc and not reasons
    return {"preregistered": ok, "post_hoc": post_hoc, "changed": changed, "used_differs": used_differs,
            "target_matches": matches, "reasons": reasons, "frozen_at": lock.get("time"), "run_began": began,
            "frozen_again": len(lock.get("replaces") or []), "armed_at": armed, "record": anchored(copy, began, root)}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--plan", default=PLAN)
    parser.add_argument("--freeze", action="store_true")
    parser.add_argument("--replace", action="store_true", help="with --freeze: freeze again (before the run only)")
    parser.add_argument("--reason", default=None, help="with --replace: why the files changed")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--arm", action="store_true", help="with --check: when it passes, no freeze after this")
    args = parser.parse_args(argv)
    try:
        if args.freeze:
            body = freeze(args.plan, args.replace, reason=args.reason)
            print(f"frozen: {len(body['files'])} files for {args.plan} (lock_sha {body['target_lock_sha']})")
            return 0
        result = check(args.plan)
        record = result.get("record") or {}
        if args.arm and result.get("preregistered") and result.get("armed_at") is None:
            if not (record.get("anchored") and record.get("pushed")):  # arming first and pushing later is too late
                print("stop: not armed: commit the pre-registration (the files and the tracked copy) and push it first "
                      f"({record.get('why') or ('not on a remote' if record.get('anchored') else 'the tracked copy is not committed as it is')})",
                      file=sys.stderr)
                return 4
            import live_go  # cycle 17: whatever could stop the run after the one arming is checked before it

            verdict = live_go.go(args.plan)
            if not verdict.get("go"):
                failing = [name for name, item in verdict.items() if isinstance(item, dict) and item.get("ok") is False]
                print(f"stop: not armed: live_go.py says no ({', '.join(failing)}); fix it and run --check --arm again",
                      file=sys.stderr)
                return 4
            said = {name: item.get("ok") for name, item in verdict.items() if isinstance(item, dict) and "ok" in item}
            result["armed_at"] = arm(args.plan, record=record, go=said)["time"]
    except ValueError as error:
        print(f"stop: {error}", file=sys.stderr)
        return 4
    print(json.dumps(result, ensure_ascii=False))
    return 0 if result.get("preregistered") else 1


if __name__ == "__main__":
    raise SystemExit(main())

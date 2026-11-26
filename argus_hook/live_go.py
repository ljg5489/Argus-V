"""Go / no-go right before the first GPU run (cycles 15-17): yes/no and numbers only; exit 0 only when every check
holds. It calls no GPU. It reads git, the lock and the files, and hashes the weights; it calls `docker image inspect`;
and it asks the plan's server to check and clear the sandbox (the server runs sandbox commands for that: it may start
the container, it clears a blocked mark and the sandbox's memory folder, as the battery's own start does).

- time: the host's clock (KST) is 09:00 or later, so the sandbox's UTC day is the prompt's day (before 09:00 a
  turn that reads `date` sees the day before), and the run's expected end (the turns left times a turn's seconds,
  plus room for one stop and a resume) comes before midnight (the battery runs one day);
- pre-registration: live_prereg.py --check holds, and its tracked record is in a commit made before now and pushed
  (others can check it: a commit's time is this computer's clock, the push time is on GitHub's activity page);
- the lock: the plan's lock_sha is the one the pre-registration names, no locked file changed, and the three
  committed modules the lock does not hash are as at the lock's git_head (first-run-v1.6-preflight.json);
- (cycle 17, GO2) what the battery checks only when it starts, so that nothing fails after the one arming: the plan's
  server (already up with the plan's memory root, the plan's §8 0-2) keeps its own memory root with no conversation,
  its scorer is equivalent and its code is the locked one; the sandbox has no left-over process, hook or block, and
  room on the disk and in its archive; the weights are the preflight's; the sandbox image is there.
It prints the checks to run by hand next to it (the workspace emptied, the chat tab and the Pages copy closed).
live_prereg.py --check --arm calls it and does not arm unless it says go.

    python argus_hook/live_go.py            # then: python argus_hook/live_prereg.py --check --arm, and the run
"""

from __future__ import annotations

import argparse
import datetime
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
PREFLIGHT = ROOT / "reports" / "live-agent" / "first-run-v1.6-preflight.json"
CASES = ROOT / "reports" / "live-agent" / "first-run-cases.json"
PLAN = "first-run-v1.6"


def time_window(now: datetime.datetime, turns: int, per_turn: int, room: int = 1800) -> dict:
    """KST 09:00 or later, and done (with ``room`` seconds for a stop and a resume) before midnight."""
    end = now + datetime.timedelta(seconds=turns * per_turn + room)
    return {"now": now.strftime("%Y-%m-%d %H:%M"), "after_nine": now.hour >= 9, "expected_end": end.strftime("%Y-%m-%d %H:%M"),
            "same_day": end.date() == now.date(), "ok": now.hour >= 9 and end.date() == now.date()}


def committed_modules(preflight: dict, head: str | None, root: Path = ROOT) -> dict:
    """The modules the lock does not hash (preflight "committed_modules"): as at the lock's git_head."""
    names = (preflight.get("committed_modules") or {}).get("paths") or []
    if not head or not names:
        return {"ok": False, "why": "no git_head in the lock or no modules in the preflight record"}
    try:
        done = subprocess.run(["git", "diff", "--quiet", head, "--", *names], cwd=root, capture_output=True, timeout=30)
    except (OSError, subprocess.SubprocessError):
        return {"ok": False, "why": "git could not be read"}
    return {"ok": done.returncode == 0, "modules": len(names)}


API = "http://127.0.0.1:8765"
PLAN_ROOT = "artifacts/live-agent/battery/first-run-v1.6/memory"  # the plan's memory root (first-run-plan.md §8 1)
# cycle 17 (GO3): the one commit the user pushes before the run: what a reviewer needs to check the pre-registration and
# the lock. Not reports/live-agent-loop/ (local paths) and not the dashboard's dist/ (a push there deploys the Pages copy).
COMMIT = ("reports/live-agent/prereg-first-run-v1.6.json", "reports/live-agent/prereg-history.md",
          "reports/live-agent/lock-first-run-v1.6.json", "reports/live-agent/first-run-v1.6-preflight.json",
          "reports/live-agent/.gitattributes", "argus_hook/.gitattributes", "argus_hook/live_go.py", "argus_hook/live_after.py",
          "tests/test_live_outcomes.py", "tests/test_live_witness.py", "tests/test_live_counterfactual.py",
          "tests/test_agent_memory.py", "tests/rehearsal_worker.py",
          "tests/test_last_freeze.py", "reports/live-agent/reader-heldout.json",  # cycle 18: the last freeze and its held-out test
          "reports/live-agent/reader-heldout-behaviours.json", "argus_hook/live_heldout.py",
          # cycle 19 (safety seat): what was known wrong before the run, the tests v1.7.md names, the locked service's test
          "reports/live-agent/v1.7.md", "tests/test_v17_security.py", "tests/test_v17_boundary.py", "tests/test_v17_reader.py",
          "tests/test_live_agent.py",
          "reports/live-agent/first-run-card.json", "tests/test_first_run_card.py")  # the card's cells, chosen before the run (FC2)


def commit_list(lock: dict) -> list[str]:
    """Every path of the one commit: the frozen readers, the files above, and the locked files git does not hold yet."""
    return sorted({*core_files(lock), *COMMIT})


def core_files(lock: dict) -> list[str]:
    """What the record's commit itself must hold: the frozen readers and the locked files git did not hold yet."""
    import live_prereg as PRE

    return sorted({*PRE.FILES, *((lock.get("frozen") or {}).get("uncommitted") or [])})


def helpers_pushed(names: list[str], root: Path = ROOT, record_commit: str | None = None) -> dict:
    """The helper files (history, copies, tools, tests) as they are now, in HEAD; HEAD on a remote branch and
    descending from the record's commit: they may be committed again after the record (a fix of this tool, a test added
    later), the record's commit stays."""
    run = lambda *args: subprocess.run(["git", *args], cwd=root, capture_output=True, text=True, timeout=20)
    head = run("rev-parse", "HEAD").stdout.strip() or None
    held = commit_holds(head, names, root)
    pushed = bool(head) and bool(run("branch", "-r", "--contains", head).stdout.strip())
    descends = bool(head) and bool(record_commit) and run("merge-base", "--is-ancestor", record_commit, head).returncode == 0
    return {**held, "ok": bool(held.get("ok") and pushed and descends), "head_pushed": pushed, "descends_from_record": descends}


LAST_FREEZE = "70a2469cd778b7564487f5c55b2737796062c93a72aeb805a9f6e5e8139a44af"  # the 6th freeze, the last (tests/test_last_freeze.py)
TRACKED = "reports/live-agent/prereg-first-run-v1.6.json"


def last_freeze(plan: str = PLAN, root: Path = ROOT) -> dict:
    """cycle 19 (safety seat): the record is the plan's last freeze (rescore-plan.md, 마지막 고정): a 7th freeze, or a
    record written again without the earlier ones (a freeze after the local lock was lost), is not this plan."""
    if plan != PLAN:
        return {"ok": True, "why": "another plan: no last freeze is pinned for it"}
    copy = Path(root) / TRACKED
    try:
        data = copy.read_bytes()
        replaces = len(json.loads(data.decode("utf-8")).get("replaces") or [])
    except (OSError, ValueError):
        return {"ok": False, "why": "the tracked copy cannot be read"}
    sha = __import__("hashlib").sha256(data).hexdigest()
    return {"ok": sha == LAST_FREEZE and replaces == 5, "sha256": sha, "replaces": replaces,
            "why": None if sha == LAST_FREEZE and replaces == 5 else "the record is not the last freeze (2026-11-22 18:57): do not run this plan"}


def commit_extra(commit: str | None, root: Path = ROOT) -> dict:
    """What the record's commit, or a helpers' commit after it, holds that it should not (a note, not a no-go: it is
    pushed already): the page's dist (deployed to Pages on a push) and this loop's reports (local paths in them)."""
    if not commit:
        return {}
    try:
        done = subprocess.run(["git", "log", "--name-only", "--format=", f"{commit}^..HEAD"], cwd=root, capture_output=True,
                              text=True, timeout=30)
        if done.returncode != 0:  # the record's commit is the first: itself only
            done = subprocess.run(["git", "show", "--name-only", "--format=", commit], cwd=root, capture_output=True, text=True, timeout=30)
    except (OSError, subprocess.SubprocessError):
        return {}
    names = sorted(set(done.stdout.split()))
    return {kind: found for kind, prefix in (("dist", "sites/argus-v-demo-dashboard/dist/"), ("loop", "reports/live-agent-loop/"))
            if (found := [name for name in names if name.startswith(prefix)])}


def commit_holds(commit: str | None, names: list[str], root: Path = ROOT) -> dict:
    """Whether the commit holding the tracked copy holds every path of the list, byte for byte as the tree has it."""
    import hashlib

    if not commit:
        return {"ok": False, "why": "the tracked copy is not committed"}
    missing, differ = [], []
    for name in names:
        try:
            done = subprocess.run(["git", "show", f"{commit}:{name}"], cwd=root, capture_output=True, timeout=30)
        except (OSError, subprocess.SubprocessError):
            return {"ok": False, "why": "git could not be read"}
        if done.returncode != 0:
            missing.append(name)
        elif hashlib.sha256(done.stdout).hexdigest() != hashlib.sha256((Path(root) / name).read_bytes()).hexdigest():
            differ.append(name)
    return {"ok": not missing and not differ, "missing": missing, "differ": differ}


def call(api: str, path: str, body: dict | None = None) -> tuple[int, dict]:
    """One request to the plan's server, as the local page (no Origin): (status, JSON), 0 when it does not answer."""
    from urllib.error import HTTPError, URLError
    from urllib.request import Request, urlopen

    data = None if body is None else json.dumps(body).encode("utf-8")
    request = Request(api.rstrip("/") + path, data=data, headers={"Content-Type": "application/json"} if data else {})
    try:
        with urlopen(request, timeout=120) as response:
            return response.status, json.loads(response.read() or b"{}")
    except HTTPError as error:
        try:
            return error.code, json.loads(error.read() or b"{}")
        except ValueError:
            return error.code, {}
    except (URLError, OSError, ValueError):
        return 0, {}


def server_checks(api: str, lock: dict, plan_root: Path | None = None) -> dict:
    """What the battery checks as it starts (live_battery.main), asked before the arming instead: the server is the
    plan's (its memory root, by the id the server gives it), empty, with the equivalent scorer and the locked code; the
    sandbox (checked, then cleared as the battery's start clears it) has no left-over process, hook, block, entry or
    scenario file, and room on the disk and in its archive. A missing answer is a no."""
    import live_witness as W

    number = lambda value: isinstance(value, (int, float)) and not isinstance(value, bool)
    status, store = call(api, "/api/live/store")
    if status != 200:
        return {"ok": False, "why": f"the plan's server does not answer at {api} (HTTP {status}): start it as §8 1) says"}
    code = store.get("code") if isinstance(store.get("code"), dict) else {}
    stale = sorted(name for name, digest in code.items() if (lock.get("files") or {}).get(name) != digest)
    root = Path(plan_root) if plan_root is not None else ROOT / PLAN_ROOT
    import live_prereg as PRE

    plans = store.get("id") == W.store_id(root) and store.get("custom") is True and store.get("conversations") == 0
    if not plans or PRE.armed_at() is not None:  # the user's own server (or an armed plan): its sandbox is not touched
        return {"ok": False, "the_plans_root": store.get("id") == W.store_id(root), "own_memory_root": store.get("custom") is True,
                "no_conversation": store.get("conversations") == 0, "armed_already": PRE.armed_at() is not None,
                "why": "not the plan's own empty server, or armed already: the sandbox was not asked"}
    checked, sandbox = call(api, "/api/live/sandbox/check", {})
    cleared, workspace = call(api, "/api/live/sandbox/clear", {})
    out = {"the_plans_root": store.get("id") == W.store_id(root), "own_memory_root": store.get("custom") is True,
           "no_conversation": store.get("conversations") == 0,
           "scorer_equivalent": (store.get("scorer") or {}).get("equivalent") is True, "code_locked": bool(code) and not stale,
           "stale": stale, "sandbox_answers": checked == 200 and cleared == 200 and workspace.get("cleared") is True,
           "no_strays": sandbox.get("strays") == 0 and workspace.get("strays") == 0,
           "no_hooks": sandbox.get("hooks") == 0 and workspace.get("hooks") == 0, "not_blocked": not sandbox.get("blocked"),
           "workspace_empty": workspace.get("entries") == 0, "no_scenario_files": workspace.get("canary") is False,
           "archive_room": number(sandbox.get("archive_bytes")) and number(sandbox.get("archive_limit"))
           and sandbox["archive_bytes"] < sandbox["archive_limit"],
           "disk_room": number(sandbox.get("disk_free")) and number(sandbox.get("disk_low")) and sandbox["disk_free"] >= sandbox["disk_low"]}
    out["ok"] = all(value for name, value in out.items() if name != "stale")
    return out


def file_checks(preflight: dict) -> dict:
    """The weights against the preflight record, and the sandbox image's id (read-only docker image inspect)."""
    import live_witness as W

    weights = W.weights(preflight, ROOT)
    image = W.image_id()
    out = {"weights_same": bool(weights) and all(item.get("same") for item in weights.values()), "image": image}
    out["ok"] = out["weights_same"] and bool(image)
    return out


def go(plan: str = PLAN, now: datetime.datetime | None = None, per_turn: int | None = None, api: str = API) -> dict:
    import live_battery as LB
    import live_prereg as PRE

    now = now or datetime.datetime.now()
    run_dir = PRE.BATTERY / plan
    lock = json.loads((run_dir / "lock.json").read_text(encoding="utf-8"))
    cases = json.loads(CASES.read_text(encoding="utf-8"))
    state = json.loads((run_dir / "state.json").read_text(encoding="utf-8")) if (run_dir / "state.json").is_file() else {}
    turns = sum(1 for case in cases.get("cases") or [] for index, _ in enumerate(case.get("turns") or [], start=1)
                if f"{case['id']}.{index}" not in (state.get("done") or []))
    window = time_window(now, turns, per_turn or LB.TURN_SECONDS)
    prereg = PRE.check(plan)
    record = prereg.get("record") or {}
    registered = {"preregistered": bool(prereg.get("preregistered")), "anchored": bool(record.get("anchored")),
                  "pushed": bool(record.get("pushed")), "why": record.get("why"),
                  "ok": bool(prereg.get("preregistered") and record.get("anchored") and record.get("pushed"))}
    now_files = LB.fingerprint(CASES)["files"]
    changed = [name for name, value in now_files.items() if (lock.get("files") or {}).get(name) != value]
    missing = sorted(set(lock.get("files") or {}) - set(now_files))  # both ways (cycle 19): a locked file gone is a change too
    sha = LB.lock_sha(lock)
    locked = {"lock_sha": sha, "matches_prereg": prereg.get("target_matches", False), "changed": len(changed), "missing": missing,
              "ok": not changed and not missing and bool(prereg.get("target_matches"))}
    preflight = json.loads(PREFLIGHT.read_text(encoding="utf-8")) if PREFLIGHT.is_file() else {}
    modules = committed_modules(preflight, lock.get("git_head"))
    checks = {"time": window, "prereg": registered, "lock": locked, "committed_modules": modules,
              "commit": commit_holds(record.get("commit"), core_files(lock)),
              "helpers": helpers_pushed(sorted(set(commit_list(lock)) - set(core_files(lock))), ROOT, record.get("commit")),
              "server": server_checks(api, lock), "files": file_checks(preflight), "last_freeze": last_freeze(plan)}
    leftovers = [str(path.relative_to(ROOT)) for path in (
        *(ROOT / "reports" / "live-agent" / f"witness-{plan}-{kind}.json" for kind in ("before", "after")),
        *(run_dir / name for name in ("person-labels.json", "person-read.json", "outcomes.json", "live-run.json", "r2-check.json",
                                      "before-publishing.json", "battery-lines.txt")),
        ROOT / "sites" / "argus-v-demo-dashboard" / "dist" / "live-run.json") if path.exists()]
    checks["fresh"] = {"ok": not leftovers, "left": leftovers,  # written once each: before the arming they may still go
                       "why": "remove them before arming (each is written once, for one run)" if leftovers else None}
    extra = commit_extra(record.get("commit"))
    by_hand = [*([f"pushed with the record: {len(extra['dist'])} files of the page's dist/ (they went to Pages on the push); "
                  "say so with the run (no amend: the commit is the record)"] if extra.get("dist") else []),
               *([f"pushed with the record: {len(extra['loop'])} files of reports/live-agent-loop/ (local paths are public now); "
                  "say so with the run"] if extra.get("loop") else []),
               "the everyday chat tab and the Pages copy closed (they would reach the plan's server; the Pages copy shows no band)",
               "nothing else on port 8765 but the plan's server (this loop's fake server stopped)"]
    return {"go": all(item.get("ok") for item in checks.values()), "turns_left": turns, **checks, "by_hand": by_hand}


def before_battery(plan: str = PLAN, now: float | None = None, root: Path = ROOT, prereg_out: Path | None = None,
                   lock_sha: str | None = None) -> dict:
    """Between the witness before the run and the battery: what the readout will ask of the before-file, asked now
    (cycle 19): the arming's minutes left; the before-file of this arming (the mark's sha256) and this lock, with no
    problem it names, committed once and on a remote (the remote-tracking reflog). A before-file written too early
    (before the arming: it is written once) is found here, not two hours later."""
    import time
    import live_battery as LB
    import live_prereg as PRE
    import live_readout as RO
    import live_witness as W

    now = time.time() if now is None else now
    out_dir = Path(prereg_out or PRE.OUT)
    armed = PRE.armed_at(plan, out=out_dir) if prereg_out else PRE.armed_at(plan)
    mark = W.sha256(out_dir / plan / "armed.json")
    if lock_sha is None:
        run_lock = PRE.BATTERY / plan / "lock.json"
        lock_sha = LB.lock_sha(json.loads(run_lock.read_text(encoding="utf-8"))) if run_lock.is_file() else None
    path = Path(root) / "reports" / "live-agent" / f"witness-{plan}-before.json"
    try:
        body = json.loads(path.read_text(encoding="utf-8")) if path.is_file() else {}
    except (OSError, ValueError):
        body = {"broken": True}  # written, but not JSON: the readout could not read it either
    body = body if isinstance(body, dict) else {"broken": True}
    record = PRE.anchored(path, None, root) if path.exists() else {"anchored": False, "why": "no witness before the run"}
    pushed = W.pushed_at(record.get("commit"), root)
    commits = RO.commits_touching(path, root) if path.exists() else 0
    left = None if armed is None else round((armed + 20 * 60 - now) / 60, 1)
    out = {"armed": armed is not None, "minutes_left": left, "witness_committed": bool(record.get("anchored")),
           "witness_pushed": pushed is not None, "witness_commits": commits,
           "this_arming": bool(mark) and body.get("armed") == mark, "this_lock": bool(lock_sha) and body.get("lock_sha") == lock_sha,
           "format": body.get("format") == W.FORMAT and body.get("plan") == plan,
           "witness_problems": (["the witness before the run is not JSON"] if body.get("broken") else W.problems(body)) if body
           else ["no witness before the run"]}
    # 3 minutes at least: the battery's first line (the run's start) comes after its own checks and clear
    out["ok"] = bool(out["armed"] and left is not None and left >= 3 and out["witness_committed"] and out["witness_pushed"]
                     and commits == 1 and out["this_arming"] and out["this_lock"] and out["format"] and not out["witness_problems"])
    if not out["ok"] and not body:
        out["why"] = [why for why, bad in (("not armed", not out["armed"]),
                                           ("less than 3 minutes of the arming left", out["armed"] and (left is None or left < 3)),
                                           ("no witness before the run yet (live_witness.py --before, after the arming)", True)) if bad]
    elif not out["ok"]:
        out["why"] = [why for why, bad in (
            ("not armed", not out["armed"]), ("less than 3 minutes of the arming left", left is None or left < 3),
            ("the witness before the run is not committed", not out["witness_committed"]),
            ("the witness before the run is not on a remote", not out["witness_pushed"]),
            (f"the witness before the run is in {commits} commits (once: the readout asks one)", commits != 1),
            ("the witness before the run is not of this arming (written before it?): this plan cannot be published",
             not out["this_arming"]),
            ("the witness before the run is not of this lock", not out["this_lock"]),
            (f"the witness before the run is not of this plan's format ({W.FORMAT}) or plan", not out["format"]),
            (f"the witness before the run names problems: {'; '.join(out['witness_problems'])}", bool(out["witness_problems"])),
        ) if bad]
    return out


MEMORY_ROOT = "artifacts/live-agent/battery/first-run-v1.6/memory"
RUN_DIR = "artifacts/live-agent/battery/first-run-v1.6"
# The run's order (rescore-plan.md "사전 등록의 기록", 1-10): one table, read by --status (cycle 19, RD)
STEPS = (
    (1, "고정(마지막: 2026-11-22 18:57)", None),
    (2, "한 커밋을 main에 푸시", "python argus_hook/live_go.py --commit-list   # the git add and git commit -- lines; then git push origin main"),
    (3, "평소 채팅 탭과 Pages 사본 닫기, 이 루프(가짜 서버·감시·CDP 탭) 멈추기, 계획 §8 0)–2)",
     "§8 0)–2): the snapshot and its size, /workspace emptied, the server started with ARGUS_LIVE_MEMORY_DIR=" + MEMORY_ROOT),
    (4, "live_go(go/no-go)", "git push --dry-run origin main && python argus_hook/live_go.py   # go; the push checked first (no login prompt within the arming's 20 minutes)"),
    (5, "무장", "python argus_hook/live_prereg.py --check --arm"),
    (6, "실행 전 증인, 그 파일만 커밋·푸시", "python argus_hook/live_witness.py --before && git add reports/live-agent/witness-first-run-v1.6-before.json && "
     "git commit -m \"first-run-v1.6: witness before the run\" -- reports/live-agent/witness-first-run-v1.6-before.json && git push origin main"),
    (7, "배터리 직전 점검, 곧바로 배터리(§8 3)", "python argus_hook/live_go.py --before-battery && python argus_hook/live_battery.py > " + RUN_DIR +
     "/battery-lines.txt 2>&1; echo \"exit $?\"; grep -v ' · alarms ' " + RUN_DIR + "/battery-lines.txt | tail -20"
     "   # its per-turn lines name each case and its alarms (left out here): the person reads blind later"),
    (8, "done 뒤 계획 서버 끄기, 실행 후 증인 그 파일만 커밋·푸시", "python argus_hook/live_witness.py --after --memory-root " + MEMORY_ROOT +
     " && git add reports/live-agent/witness-first-run-v1.6-after.json && git commit -m \"first-run-v1.6: witness after the run\" -- "
     "reports/live-agent/witness-first-run-v1.6-after.json && git push origin main"),
    (9, "사람 읽기(먼저), §8 4)–5), live_after", "python argus_hook/live_read.py --memory-root " + MEMORY_ROOT +
     "   # once, no undo: Ctrl-C before the last label writes nothing; then §8 4)-5), then python argus_hook/live_after.py --memory-root " + MEMORY_ROOT),
    (10, "숫자를 보고 동의하면 공개", "python argus_hook/live_readout.py --run " + RUN_DIR + " --memory-root " + MEMORY_ROOT +
     " --publish   # then git add -f the files it names"),
)


def _card_word(run: Path) -> str:
    try:
        return "card: " + json.loads((Path(run) / "before-publishing.json").read_text(encoding="utf-8")).get("card", "?")
    except (OSError, ValueError):
        return "live_after.py first (it decides the card by first-run-card.json publish_rules)"


def status(plan: str = PLAN, root: Path = ROOT, battery: Path | None = None, prereg_out: Path | None = None,
           now: float | None = None) -> dict:
    """cycle 19 (RD): where the run's order stands, from files and git only: no server is asked, no weight hashed, and
    nothing of a turn is shown (no label, score or alarm: the person reads blind first). Each step: done, next, by hand
    or waiting, and the next command."""
    import time
    import live_prereg as PRE

    now = time.time() if now is None else now
    out_dir, run = Path(prereg_out or PRE.OUT), Path(battery or PRE.BATTERY) / plan
    state = {}
    try:
        state = json.loads((run / "state.json").read_text(encoding="utf-8")) if (run / "state.json").is_file() else {}
    except (OSError, ValueError):
        state = {"unreadable": True}
    record = PRE.anchored(Path(root) / TRACKED, None, root)
    armed = PRE.armed_at(plan, out=out_dir)
    left = None if armed is None else round((armed + 20 * 60 - now) / 60, 1)
    before = Path(root) / "reports" / "live-agent" / f"witness-{plan}-before.json"
    after = Path(root) / "reports" / "live-agent" / f"witness-{plan}-after.json"
    done_turns = [key for key in state.get("done") or [] if not str(key).startswith("clear:")]
    ended = "clear:end" in (state.get("done") or [])
    person = run / "person-labels.json"
    readers = [name for name in ("outcomes.json", "r2-check.json", "live-run.json") if (run / name).exists()]
    published = (Path(root) / "sites" / "argus-v-demo-dashboard" / "dist" / "live-run.json").exists()
    frozen = last_freeze(plan, root)["ok"]
    pushed = bool(record.get("anchored") and record.get("pushed"))
    checks = {
        1: (frozen, None if frozen else "the record is not the last freeze: do not run this plan"),
        2: (pushed, None if pushed else "not committed" if not record.get("anchored") else "committed, not pushed yet (git push origin main)"),
        3: (None, "by hand"),
        4: (None, "by hand: it asks the plan's server (this table does not)"),
        5: (armed is not None, None if armed is None else "the run's first line is written (the 20 minutes were for it)" if done_turns
            else (f"{left} minutes of the arming's 20 left" if left is not None and left > 0
                  else "the arming's 20 minutes are over before the run's first line: see rescore-plan.md")),
        6: (before.is_file() and bool(PRE.anchored(before, None, root).get("pushed")),
            "written, not committed and pushed yet" if before.is_file() else None),
        7: (ended, f"{len(done_turns)} turns done" + (", ended (clear:end)" if ended else ", not ended" if done_turns else "")),
        8: (after.is_file() and bool(PRE.anchored(after, None, root).get("pushed")),
            "written, not committed and pushed yet" if after.is_file() else None),
        9: (person.is_file() and bool(readers), ("the person's labels written" if person.is_file() else "no person's labels yet")
            + (f"; the readers' files: {', '.join(readers)}" if readers else "")),
        10: (published, None if published else _card_word(run)),  # PB: the card as live_after decided it, word for word
    }
    began = PRE.run_began(run)  # as the readout counts the run's start: the manifest's first line
    started = began is not None or bool(done_turns) or "clear:start" in (state.get("done") or [])
    late = armed is not None and began is not None and began - armed > 20 * 60  # its first line after the 20 minutes
    if started:
        checks[5] = (armed is not None, "the battery started (the 20 minutes were for its first line)")
    expired = armed is not None and not started and left is not None and left <= 0
    rows, nxt = [], None
    for number, name, command in STEPS:
        ok, note = checks[number]
        written = {6: before, 8: after}.get(number)
        if command and written is not None and written.is_file():  # written once: what is left is its commit and push
            command = command[command.index("git add"):]
        if number == 7 and started and not ended:  # a battery that stopped goes on by the same command (§8 3), no new arming
            command = (f"echo \"== 이어서 $(date +%H:%M)\" >> {RUN_DIR}/battery-lines.txt; python argus_hook/live_battery.py >> {RUN_DIR}/battery-lines.txt 2>&1; "
                       f"echo \"exit $?\"; grep -v ' · alarms ' {RUN_DIR}/battery-lines.txt | tail -20"
                       "   # it goes on where it stopped; the arming's 20 minutes are for its first line only")
        kind = "by_hand" if ok is None else "done" if ok else "todo"
        if kind == "todo" and nxt is None:
            nxt = number
        rows.append({"step": number, "name": name, "state": kind, "note": note, "command": command})
    if late:  # it runs, but it cannot be published: say so before its two hours
        rows[4].update(state="blocked", note=f"배터리의 첫 줄이 무장 뒤 {round((began - armed) / 60)}분: 공개할 수 없는 실행 · 멈출지 정할 것(rescore-plan.md)")
    if expired:  # nothing more this arming can do: no witness, no battery (each is written once)
        rows[4].update(state="blocked", note="무장한 뒤 20분이 지나 배터리를 시작하지 못함: 이 무장으론 실행 못 함 · 증인을 쓰지 말 것 · rescore-plan.md를 보고 정할 것")
        nxt = None
    for item in rows:
        if item["step"] == nxt:
            item["state"] = "next"
    if nxt == 5:  # the steps done by hand come first: this table cannot see them
        rows[4]["note"] = "3·4단계(손으로: 탭과 루프 멈추기, §8 0)–2), live_go의 go)를 먼저"
    return {"plan": plan, "next": nxt, "steps": rows,
            "reminders": ["never git commit -a (dist/ goes to Pages; from the arming to the decision to publish no other tracked file changes)",
                          "the person reads before the report and live_after.py; battery-lines.txt only after the person's labels (the progress: --status, n turns done)",
                          "nothing else on 127.0.0.1:8765 but the plan's server while armed"]}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--plan", default=PLAN)
    parser.add_argument("--now", default=None, help="the time to judge (ISO, for a dry look); default: now")
    parser.add_argument("--turn-seconds", type=int, default=None)
    parser.add_argument("--api", default=API, help="the plan's server (already started with the plan's memory root)")
    parser.add_argument("--commit-list", action="store_true", help="print the git add command of the one commit, and stop")
    parser.add_argument("--status", action="store_true", help="where the run's order stands (files and git only), and stop")
    parser.add_argument("--before-battery", action="store_true",
                        help="after the witness before the run: the minutes left since the arming, and the file pushed")
    args = parser.parse_args(argv)
    if args.commit_list:
        import live_prereg as PRE

        lock = json.loads((PRE.BATTERY / args.plan / "lock.json").read_text(encoding="utf-8"))
        paths = " ".join(commit_list(lock))
        print("git add -- " + paths)
        # these paths only: a file staged before (dist/ would go to Pages, reports/live-agent-loop/ holds local paths) stays out
        print('git commit -m "first-run-v1.6: the record before the run" -- ' + paths)
        print("git diff --cached --name-only   # must print nothing: anything still staged (dist/, say) goes with a later commit")
        print("# then: git push origin main (no squash, rebase or amend later: the commit is the record)")
        return 0
    if args.status:
        result = status(args.plan)
        for item in result["steps"]:
            mark = {"done": "✓", "next": "→", "todo": " ", "by_hand": "✋", "blocked": "✗"}[item["state"]]
            print(f"{mark} {item['step']:>2}. {item['name']}" + (f"  ({item['note']})" if item.get("note") else ""))
            if item["state"] == "next" and item.get("command"):
                print(f"      {item['command']}")
        print("\n".join(f"  · {line}" for line in result["reminders"]))
        return 0
    if args.before_battery:
        result = before_battery(args.plan)
        print(json.dumps(result, ensure_ascii=False, indent=1))
        return 0 if result["ok"] else 1
    now = datetime.datetime.fromisoformat(args.now) if args.now else None
    try:
        result = go(args.plan, now, args.turn_seconds, args.api)
    except (OSError, ValueError, KeyError) as error:
        print(f"stop: {type(error).__name__}: {error}", file=sys.stderr)
        return 4
    print(json.dumps(result, ensure_ascii=False, indent=1))
    return 0 if result["go"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

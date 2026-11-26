"""The first GPU run in numbers, read by rules fixed before it (pre-registered with live_prereg.py): what the demo may
say afterwards, so no number is picked by hand. It reads only numbers and labels, by the plan's own reading rules
(the locked live_report.py's functions, imported and never changed):
- the outcome labels (live_outcomes.py's JSON): per group, "k of n" for each label, the turns with no rule apart, and
  the plan's turns the run did not keep;
- the run's manifest and verdict rows: runs counted apart (scenario residue, left-over processes, hooks, files a page
  elsewhere changed, a blocked sandbox, the sealed pages, a verdict error) are left out of every count, as the report
  does; the judged commands and their alarms, main and memory steps apart and reference_like apart; answers are
  judged but never alarms; steps without a verdict are counted on their own;
- the determinism twin by the plan's rule (D01 against P01-off at step 1: the same prompt, the same tokens and a
  score within 1e-6);
- the counterfactual check (live_counterfactual.py --check): which transformations are usable, and I0.
It also says what the numbers stand on: whether each reader was pre-registered, whether the record of that is in a
commit made before the run (and pushed), and whether the run had a real GPU (a rehearsal does not). v3 (cycle 16)
ties every input to the run it reads: the outcomes and the counterfactual check name the manifest they read (its
sha256), the case list read is the plan's, and the report's reading rules (live_report.py) are the locked ones. It
publishes only a run armed before it began (within ARM_WINDOW), with the record committed and pushed then and now,
the labels computed again from the run equal to the outcomes file's, and the witness of the run (live_witness.py,
before and after it) matching the run's files as they are, and pushed. What no local check can tell apart is said in
the claim: a run started again within the window after its arming.
Every case of the plan is harmless by design, so every alarm is a false alarm. No text of a turn is read or
written, and no rate is given: counts ("k of n") only.

    python argus_hook/live_readout.py --run artifacts/live-agent/battery/first-run-v1.6
        # writes <run>/live-run.json; --publish also writes the dashboard's dist/live-run.json, only when every reader
        # was pre-registered, the run is complete and had a GPU, and only after the user agrees. dist/ is git-ignored:
        # making it public is the user's own `git add -f` and push.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
DIST = ROOT / "sites" / "argus-v-demo-dashboard" / "dist" / "live-run.json"
CASES = ROOT / "reports" / "live-agent" / "first-run-cases.json"
LABELS = ("success", "partial", "failure", "unknown", "sealed")
ARM_WINDOW = 20 * 60  # seconds from arming to the run's first line (the witness and the battery's start in between)
LOGS = ROOT / "artifacts" / "live-agent"
RECORD = ROOT / "reports" / "live-agent"
CUT_OFF_NOTE = "0.864 is the cut-off fitted on scenario runs without memory or earlier turns"
ALARM_NOTE = "every case of the plan is harmless by design: every alarm here is a false alarm"


def sha256(path: Path) -> str | None:
    try:
        return hashlib.sha256(Path(path).read_bytes()).hexdigest()
    except OSError:
        return None


def read_json(path: Path) -> dict | None:
    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    return data if isinstance(data, dict) else None


def k_of_n(k: int, n: int) -> dict:
    return {"k": int(k), "n": int(n)}


def planned(cases: Path = CASES) -> dict:
    """The plan's turns per group (the denominators the plan set)."""
    data = read_json(cases) or {}
    out: dict[str, int] = {}
    for case in data.get("cases") or []:
        out[str(case.get("group"))] = out.get(str(case.get("group")), 0) + len(case.get("turns") or [])
    out["all"] = sum(out.values())
    return out


def planned_keys(cases: Path = CASES) -> list[str]:
    data = read_json(cases) or {}
    return [f"{case['id']}.{index}" for case in data.get("cases") or [] for index, _ in enumerate(case.get("turns") or [], start=1)]


def labels(outcomes: dict, plan: dict, apart: set | None = None) -> dict:
    """Per group and overall: k of n for each label (n = the turns the run kept in it and the report counts), the
    turns with no rule (by design) apart from unknown, and the plan's count. A turn the report counts apart (residue,
    left-over processes, hooks, files changed elsewhere, a blocked sandbox, the sealed pages, a verdict error) is left
    out here too."""
    groups: dict[str, dict] = {}
    for turn in outcomes.get("turns") or []:
        if turn.get("key") in (apart or set()):
            continue
        label = "no_rule" if turn.get("why") == "no_rule" else turn.get("label")
        for group in (str(turn.get("group")), "all"):
            groups.setdefault(group, {}).setdefault(label, 0)
            groups[group][label] += 1
    out = {}
    for group, counts in groups.items():
        n = sum(counts.values())
        out[group] = {**{label: k_of_n(counts.get(label, 0), n) for label in (*LABELS, "no_rule")},
                      "planned": plan.get(group)}
    return out


def judged(run_dir: Path) -> dict:
    """The plan's reading of the verdicts (live_report.py): runs apart, judged commands and alarms, answers, unjudged
    steps, determinism."""
    import live_report as REP

    lines = REP.read_lines(Path(run_dir) / "manifest.jsonl")
    runs = [line for line in lines if line.get("conversation") and line.get("run_id")]
    rows = [row for row in REP.read_lines(Path(run_dir) / "verdicts.jsonl") if "phase" in row]
    by_run: dict[str, list[dict]] = {}
    for row in rows:
        by_run.setdefault(str(row.get("run_id")), []).append(row)
    apart = {run["run_id"]: reason for run in runs if (reason := REP.apart_reason(run, by_run.get(run["run_id"], [])))}
    import live_outcomes as LO

    kept_keys = LO.turn_keys(lines)
    keys = [key for key, row in kept_keys if row.get("run_id") in apart]  # the plan keys of those runs
    reasons: dict[str, int] = {}
    for reason in apart.values():
        reasons[reason] = reasons.get(reason, 0) + 1
    kept = [run for run in runs if run["run_id"] not in apart]
    counted = [row for run in kept for row in by_run.get(run["run_id"], [])]
    alarms = {}
    for phase in ("main", "memory"):
        for flag in (False, True):
            group = [row for row in counted if row.get("phase") == phase and bool(row.get("reference_like")) == flag
                     and row.get("kind") != "stop" and row.get("score") is not None]
            alarms[f"{phase}{'_reference_like' if flag else ''}"] = k_of_n(sum(1 for row in group if row.get("alarm")), len(group))
    answers = sum(1 for row in counted if row.get("kind") == "stop" and row.get("score") is not None)
    unjudged = sum(1 for row in counted if row.get("score") is None)
    by_case = {run.get("case"): run for run in kept}
    first, second = REP.step_row(by_case.get("P01-off") or {}, 1), REP.step_row(by_case.get("D01") or {}, 1)
    prompt, generated = REP.same_tokens(first, second) if first and second else (None, None)
    delta = ((first.get("score") or 0) - (second.get("score") or 0)) if first and second else None
    deterministic = (None if prompt is None or generated is None or not prompt
                     else bool(generated and delta is not None and abs(delta) <= REP.SAME))
    versions = [run.get("versions") or {} for run in runs if run.get("versions")]
    gpu = bool(versions) and all(item.get("gpu") and item.get("torch") not in (None, "rehearsal") for item in versions)
    emp = sorted({str((run.get("context") or {}).get("emp_sha")) for run in runs if (run.get("context") or {}).get("emp_sha")})
    memory = sum(1 for run in kept if (run.get("context") or {}).get("memory") == "on")
    history = sum(1 for run in kept if "history" in ((run.get("context") or {}).get("features") or []))
    return {"runs": len(runs), "apart": {"n": len(apart), "reasons": reasons, "keys": keys}, "kept": len(kept),
            "run_ids": {key: row.get("run_id") for key, row in kept_keys},
            "alarms": alarms, "answers_judged": answers, "unjudged_steps": unjudged,
            "determinism": {"pair": ["P01-off.1", "D01.1"], "prompt_same": prompt, "tokens_same": generated,
                            "deterministic": deterministic},
            "gpu": gpu, "emp_sha": emp, "turns_with_memory": memory, "turns_with_history": history}


def standing(run_dir: Path, outcomes: dict, check: dict | None, cases: Path = CASES, where: dict | None = None) -> dict:
    """What the numbers stand on: each reader's pre-registration, and the record's anchoring. ``where``: the
    pre-registration's folders (out, root, record), for a test."""
    import live_outcomes as LO
    import live_prereg as PRE

    where = where or {}
    plan = str(outcomes.get("plan") or "")
    # what this readout read: itself, the outcome tool it imports, the case list (the plan's, as locked)
    own = PRE.check(plan, battery=Path(run_dir).parent, run=Path(run_dir), cases=Path(cases),
                    used={"argus_hook/live_readout.py": Path(__file__), "argus_hook/live_outcomes.py": Path(LO.__file__)},
                    **where) if plan else {"preregistered": False}
    record = own.get("record") or {}
    # a commit's time is this computer's clock: when it was pushed is the remote's record (GitHub's activity)
    claim = ("committed before the run and on the remote now; what anyone can check is on GitHub's activity page (the push "
             "times of the record and of the witness before and after the run, and no force push between them) and in the "
             "frozen tools' code; everything else was checked on this computer only, which stops honest mistakes and proves "
             "nothing about the operator (a run started again, or armed again with its records removed, cannot be told "
             "apart here); the run's own data are not public, so its numbers cannot be computed again by others"
             if record.get("anchored") and record.get("pushed")
             else "committed before the run (not on a remote)" if record.get("anchored") else "this computer only")
    lock_record = read_json(Path(where.get("out", PRE.OUT)) / plan / "lock.json") if plan else None
    freezes = [round(float(item.get("time") or 0), 3) for item in [*((lock_record or {}).get("replaces") or []), lock_record or {}]
               if item.get("time")]
    armed = PRE.armed_record(plan, out=where.get("out", PRE.OUT)) if plan else None
    return {"p1": bool((outcomes.get("prereg") or {}).get("preregistered")),
            "r2": None if check is None else bool((check.get("prereg") or {}).get("preregistered")),
            "readout": bool(own.get("preregistered")), "post_hoc": bool(own.get("post_hoc")),
            "reasons": list(own.get("reasons") or []), "frozen_again": own.get("frozen_again"), "frozen_at": freezes,
            "record": record, "claim": claim,
            "checked_here_only": ["the arming and its 20 minutes", "the run's start time", "the remote-tracking reflog",
                                  "one commit of the witness before the run", "live_go's go", "the lock, the weights and the image",
                                  "the witness matching the run's files", "the labels computed again", "the GPU",
                                  "the person's labels written before the machine's were computed (blind)"],
            "verifiable_by_anyone": ["the push times of the record and of the witness before and after the run (GitHub)",
                                     "no force push between them (GitHub)", "the code of the frozen tools"],
            "armed_at": own.get("armed_at"), "run_began": own.get("run_began"),
            "at_arming": (armed or {}).get("record")}  # what was true right before the run, apart from now


def counterfactual(check: dict | None) -> dict | None:
    if not check:
        return None
    out = {"usable": list(check.get("usable") or []), "incomplete": len(check.get("incomplete") or [])}
    for name in ("I1", "I2", "I3", "I4"):
        row = check.get(name) or {}
        out[name] = {key: (len(value) if isinstance(value, list) else value) for key, value in row.items()}
    if isinstance(check.get("I0"), dict):
        out["I0"] = {key: check["I0"].get(key) for key in ("generations", "same", "differ", "unrecorded")}
    return out


def commits_touching(path: Path, root: Path = ROOT) -> int:
    import subprocess

    try:
        rel = str(Path(path).resolve().relative_to(Path(root).resolve()))
        done = subprocess.run(["git", "log", "--format=%H", "--", rel], cwd=root, capture_output=True, text=True, timeout=20)
    except (OSError, ValueError, subprocess.SubprocessError):
        return 0
    return len(done.stdout.split())


def reruns(run_dir: Path, memory_root: Path | None, cases: Path = CASES) -> dict | None:
    """The plan's turns that ran more than once: those kept with earlier attempts (superseded: a stop, then the battery
    again, retries the turn), the plan's own retries apart (a case turn with last_turn retry or edit); and the starts
    the server logged for the battery against the plan's turns (an attempt lost with a stopped server ran too)."""
    if memory_root is None:
        return None
    import live_outcomes as LO
    import live_witness as W

    plan = read_json(cases) or {}
    planned = {f"{case['id']}.{index}" for case in plan.get("cases") or []
               for index, turn in enumerate(case.get("turns") or [], start=1) if turn.get("last_turn") in ("retry", "edit")}
    keys = []
    folder = (Path(memory_root) / "conversations").resolve()
    for key, row in LO.turn_keys(LO.read_jsonl(Path(run_dir) / "manifest.jsonl")):
        path = (folder / f"{row.get('conversation')}.json").resolve()
        data = read_json(path) if path.parent == folder else None
        turn = next((item for item in (data or {}).get("turns") or [] if item.get("run_id") == row.get("run_id")), None)
        if turn and turn.get("superseded") and key not in planned:
            keys.append(key)
    rows = LO.read_jsonl(Path(run_dir) / "manifest.jsonl")
    begin = next((row.get("time") for row in rows if row.get("case") == "clear-start"), None)
    end = next((row.get("time") for row in reversed(rows) if row.get("case") == "clear-end"), None)
    starts = sum(1 for name in ("audit.1.jsonl", "audit.jsonl") for row in W.jsonl(Path(memory_root) / name)
                 if row.get("action") == "start" and row.get("battery") and not row.get("refused")
                 and (begin is None or (row.get("time") or 0) >= begin) and (end is None or (row.get("time") or 0) <= end))
    turns = sum(len(case.get("turns") or []) for case in plan.get("cases") or [])
    return {"turns": len(keys), "keys": keys, "starts": starts, "planned": turns, "extra_starts": max(0, starts - turns)}


def witnessed(run_dir: Path, plan: str, log_dir: Path = LOGS, record: Path = RECORD, root: Path = ROOT,
              memory_root: Path | None = None, began: float | None = None, armed: str | None = None,
              lock_sha: str | None = None) -> dict:
    """The witness of the run (live_witness.py): the before-file committed and pushed before the run began, for this
    arming (``armed``: the arming mark's sha256 now) and this lock; the after-file matching the run's files and what
    the labels read in the memory root as they are now, committed as it is and pushed; the same image and the
    preflight's weights both times."""
    import live_prereg as PRE
    import live_witness as W

    before = read_json(Path(record) / f"witness-{plan}-before.json")
    after = read_json(Path(record) / f"witness-{plan}-after.json")
    if not before or not after:
        return {"ok": False, "why": "no witness before and after the run"}
    same = W.matches(after, run_dir, log_dir, memory_root)
    anchored = PRE.anchored(Path(record) / f"witness-{plan}-after.json", None, root)
    early = PRE.anchored(Path(record) / f"witness-{plan}-before.json", began, root)  # committed before the run began
    # and on a remote before it: the first push the witness after the run wrote down (else this repository's reflog now)
    known = ((after.get("pushes") or {}).get("before") or {})
    first_push = known.get("first_push") if known.get("commit") and known.get("commit") == early.get("commit") \
        else W.pushed_at(early.get("commit"), root)
    commits = commits_touching(Path(record) / f"witness-{plan}-before.json", root)  # once: not rewritten after a re-arming
    early = {**early, "pushed": early.get("pushed") and first_push is not None and (began is None or first_push <= began)
             and commits == 1}
    this_arming = bool(armed) and before.get("armed") == armed == after.get("armed")
    this_lock = bool(lock_sha) and before.get("lock_sha") == lock_sha == after.get("lock_sha")
    image = bool((before.get("image") or {}).get("id")) and (before.get("image") or {}).get("id") == (after.get("image") or {}).get("id")
    weights = all(body.get("weights") and all(item.get("same") for item in body["weights"].values()) for body in (before, after))
    modules = all((body.get("committed_modules") or {}).get("ok") for body in (before, after))
    formats = before.get("format") == after.get("format") == W.FORMAT and before.get("plan") == after.get("plan") == plan
    # the three commits anyone can look up on GitHub (their push times are the evidence; the reflog time is this
    # computer's own account, written down after the run)
    shas = {"record": ((after.get("pushes") or {}).get("record") or {}).get("commit"), "before": early.get("commit"),
            "after": anchored.get("commit")}
    out = {"files_same": same["same"], "differs": same["differs"], "pushed": bool(anchored.get("anchored") and anchored.get("pushed")),
           "before_pushed_before_run": bool(early.get("anchored") and early.get("pushed")), "before_commits": commits,
           "before_first_push_reflog": first_push, "commits": shas, "reruns_by_case": after.get("reruns"),
           "compare_with": "the push times of these commits on GitHub's activity page", "this_arming": this_arming,
           "this_lock": this_lock, "image_same": image, "weights_same": weights, "modules_same": modules, "format": formats,
           "before_time": before.get("time"), "after_time": after.get("time")}
    out["ok"] = all(out[name] for name in ("files_same", "pushed", "before_pushed_before_run", "this_arming", "this_lock",
                                           "image_same", "weights_same", "modules_same", "format"))
    return out


def person_reading(run_dir: Path, outcomes: dict, rules: dict) -> dict | None:
    """live_read.py's labels (written once, before the comparison), compared here with the labels published: counted
    from the person's own file, not from the comparison it wrote. Complete when it holds every turn with a rule, the
    sealed ones as sealed and only those."""
    written = read_json(Path(run_dir) / "person-labels.json")
    if not written:
        return None
    labels = written.get("labels") if isinstance(written.get("labels"), dict) else {}
    machine = {turn.get("key"): turn for turn in outcomes.get("turns") or [] if turn.get("key") in (rules.get("rules") or {})}
    sealed = {key for key, turn in machine.items() if turn.get("label") == "sealed"}
    read = sorted(key for key in machine if key not in sealed and labels.get(key) not in (None, "sealed"))
    agree = [key for key in read if machine[key].get("label") == labels[key]]
    count = lambda values: {label: sum(1 for value in values if value == label) for label in ("success", "partial", "failure", "unknown")}
    return {"blind": written.get("blind") is True,
            "complete": set(labels) == set(machine) and all((labels[key] == "sealed") == (key in sealed) for key in machine)
                        and all(value in ("success", "partial", "failure", "unknown", "sealed") for value in labels.values()),
            "n": len(read), "sealed": len(sealed), "agree": len(agree),
            "machine": count(machine[key].get("label") for key in read), "person": count(labels[key] for key in read),
            "disagree": [{"key": key, "machine": machine[key].get("label"), "person": labels[key],
                          "failed": machine[key].get("failed") or [], "undecided": machine[key].get("undecided") or []}
                         for key in read if key not in agree]}


def readout(run_dir: Path, outcomes: dict, check: dict | None = None, cases: Path = CASES, where: dict | None = None,
            log_dir: Path = LOGS, memory_root: Path | None = None) -> dict:
    """``memory_root``: the plan's memory root, to compute the labels again from the run (else they are not
    compared, and the readout may not be published)."""
    import live_outcomes as LO

    lock = read_json(Path(run_dir) / "lock.json") or {}
    where = where or {}
    numbers = judged(run_dir)
    manifest = sha256(Path(run_dir) / "manifest.jsonl")
    # each input names the run it read (the lock_sha is the same for every run of the plan: the manifest is not)
    bound = {"outcomes": bool(manifest) and outcomes.get("manifest_sha256") == manifest,
             "r2": None if check is None else bool(manifest) and check.get("manifest_sha256") == manifest}
    locked_report = (lock.get("files") or {}).get("argus_hook/live_report.py")  # its functions are the reading rules
    report_locked = locked_report is not None and sha256(ROOT / "argus_hook" / "live_report.py") == locked_report
    recomputed = None  # the labels as the rules give them from the run now, against the outcomes file's
    if memory_root is not None:
        again = LO.outcomes(run_dir, memory_root, LO.load_rules(), log_dir)
        label = lambda turns: {turn.get("key"): (turn.get("label"), turn.get("run"), turn.get("why"), json.dumps(turn.get("attempts"), sort_keys=True))
                               for turn in turns or []}
        recomputed = label(again.get("turns")) == label(outcomes.get("turns")) and again.get("attempts") == outcomes.get("attempts")
        outcomes = {**outcomes, "turns": again.get("turns"), "attempts": again.get("attempts")}  # what is published
    plan_name = str(outcomes.get("plan") or lock.get("plan") or "")
    import live_battery as LB
    import live_prereg as PRE
    import live_witness as W

    state = read_json(Path(run_dir) / "state.json") or {}
    # the memory root read is the one the run kept (the battery wrote its store id when the run began)
    root_is_the_runs = None if memory_root is None else bool(state.get("store")) and W.store_id(memory_root) == state.get("store")
    no_record = sum(1 for turn in outcomes.get("turns") or [] if turn.get("why") == "no_record")
    armed_sha = sha256(Path(where.get("out", PRE.OUT)) / plan_name / "armed.json")
    witness = witnessed(run_dir, plan_name, log_dir, where.get("record", RECORD), where.get("root", ROOT), memory_root,
                        PRE.run_began(Path(run_dir)), armed_sha, LB.lock_sha(lock) if lock else None)
    if root_is_the_runs is False and witness.get("files_same"):  # moved, or another clone: the same files the run left
        root_is_the_runs = True
    apart_keys = set(numbers["apart"]["keys"])
    run_ids = numbers.pop("run_ids")
    # the labels are this run's: every labelled turn names the run id the manifest keeps for its key
    matches = all(turn.get("run") == run_ids.get(turn.get("key")) for turn in outcomes.get("turns") or []) \
        and {turn.get("key") for turn in outcomes.get("turns") or []} == set(run_ids)
    plan_keys = set(planned_keys(cases))
    missing = sorted(plan_keys - set(run_ids))  # counted from the manifest, not taken from the outcomes file
    counted = reruns(run_dir, memory_root, cases)
    if counted is not None and isinstance(witness.get("reruns_by_case"), dict):
        counted = {**counted, "by_case": witness["reruns_by_case"], "extra_starts": sum(witness["reruns_by_case"].values())}
    return {"plan": outcomes.get("plan") or lock.get("plan"), "reruns": counted,
            "person": person_reading(run_dir, outcomes, LO.load_rules()),
            "prereg": standing(run_dir, outcomes, check, cases, where), "bound": bound, "report_rules_locked": report_locked,
            "labels_recomputed": recomputed, "memory_root_is_the_runs": root_is_the_runs, "no_record": no_record,
            "ended": W.finished(run_dir, memory_root, by_path=not witness.get("files_same")),
            "witness": witness,
            "complete": not missing, "missing": len(missing), "outcomes_match_run": matches,
            "outcomes": labels(outcomes, planned(cases), apart_keys), "attempts": outcomes.get("attempts") or {},
            "verdicts": numbers, "counterfactual": counterfactual(check),
            "notes": [CUT_OFF_NOTE + f"; {numbers['turns_with_memory']} of the {numbers['kept']} counted turns had memory "
                      f"and {numbers['turns_with_history']} had earlier turns",
                      ALARM_NOTE, "counts only (k of n): the plan's turns are too few for rates; no detection claim"]}


def may_publish(result: dict) -> list[str]:
    """Why the readout may not be published (empty: it may, once the user agrees)."""
    prereg = result.get("prereg") or {}
    reasons = [name for name in ("p1", "r2", "readout") if prereg.get(name) is not True]  # r2's check must be there
    if not result.get("outcomes_match_run"):
        reasons.append("the outcomes are not this run's")
    bound = result.get("bound") or {}
    if bound.get("outcomes") is not True:
        reasons.append("the outcomes read another manifest")
    if bound.get("r2") is not True:
        reasons.append("the counterfactual check read another manifest")
    if not result.get("report_rules_locked"):
        reasons.append("the report's reading rules (live_report.py) are not the locked ones")
    armed, began = prereg.get("armed_at"), prereg.get("run_began")
    if armed is None or (began is not None and float(armed) > float(began)):
        reasons.append("not armed before the run began")
    elif began is not None and float(began) - float(armed) > ARM_WINDOW:
        reasons.append("armed more than 20 minutes before the run began")
    at_arming = prereg.get("at_arming") or {}
    if not (at_arming.get("anchored") and at_arming.get("pushed")):
        reasons.append("the record was not committed and pushed when the run was armed")
    record = prereg.get("record") or {}  # git now, not what the arming mark says of itself
    if not (record.get("anchored") and record.get("pushed")) or record.get("commit") != at_arming.get("commit"):
        reasons.append("the record is not, now, the pushed commit it was when the run was armed")
    if result.get("labels_recomputed") is not True:
        reasons.append("the labels were not computed again from the run, or differ from the outcomes file")
    ended = result.get("ended") or {}
    if not ended.get("ok"):  # each reason said as it is
        for why in ended.get("why") or ["the battery did not end the run, or exported no verdicts under its lock"]:
            reasons.append(why)
    if result.get("memory_root_is_the_runs") is not True:
        reasons.append("the memory root read is not the one the run kept (its store id)")
    if result.get("no_record"):
        reasons.append(f"{result['no_record']} turns have no record in the memory root read")
    witness = result.get("witness") or {}
    if not witness.get("ok"):
        reasons.append("no witness of the run that matches its files and is pushed")
    elif began is not None and (witness.get("before_time") is None or float(witness["before_time"]) > float(began)):
        reasons.append("the witness before the run was written after it began")
    if not result.get("person"):
        reasons.append("no person read the turns blind (live_read.py)")
    elif not result["person"].get("complete"):
        reasons.append("the person's reading does not hold every turn with a rule (live_read.py)")
    if not result.get("complete"):
        reasons.append("incomplete run")
    if not (result.get("verdicts") or {}).get("gpu"):
        reasons.append("no GPU (a rehearsal)")
    return reasons


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--run", type=Path, required=True, help="the battery folder")
    parser.add_argument("--outcomes", type=Path, default=None, help="live_outcomes.py's JSON (default <run>/outcomes.json)")
    parser.add_argument("--check", type=Path, default=None, help="the counterfactual check (default <run>/r2-check.json)")
    parser.add_argument("--memory-root", type=Path, default=None,
                        help="the plan's memory root (ARGUS_LIVE_MEMORY_DIR): the labels are computed again from the run")
    parser.add_argument("--log-dir", type=Path, default=LOGS, help="the task records")
    parser.add_argument("--publish", action="store_true",
                        help="also write the dashboard's dist/live-run.json: only after the user agrees")
    args = parser.parse_args(argv)
    outcomes = read_json(args.outcomes or args.run / "outcomes.json")
    if outcomes is None:
        print("stop: no outcomes (run live_outcomes.py first)", file=sys.stderr)
        return 4
    result = readout(args.run, outcomes, read_json(args.check or args.run / "r2-check.json"), log_dir=args.log_dir,
                     memory_root=args.memory_root)
    text = json.dumps(result, ensure_ascii=False, indent=1) + "\n"
    (args.run / "live-run.json").write_text(text, encoding="utf-8")
    if args.publish:
        refused = may_publish(result)
        if refused:
            print(f"stop: not published ({', '.join(refused)})", file=sys.stderr)
            return 4
        DIST.write_text(text, encoding="utf-8")
        print("written to dist/live-run.json (git-ignored: making it public is your own git add -f and push)", file=sys.stderr)
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

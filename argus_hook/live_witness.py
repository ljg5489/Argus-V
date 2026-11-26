"""Witness of the first GPU run (cycle 16): what the plan's lock does not hash, written down right before the run and
right after it, in a tracked file to commit and push at once. A commit's time is this computer's clock; the push time
on GitHub is the evidence others can check. It reads only, apart from its own file, which it never overwrites; it
calls docker only as `docker image inspect`, and never the GPU or sandbox.py.

    python argus_hook/live_witness.py --before   # after the plan's §8 0-2, live_go.py and --check --arm; push it, then the battery
    python argus_hook/live_witness.py --after --memory-root <root>   # after the battery's done and the server stopped; push it

Both write the time, the plan and its lock_sha, and the sandbox image's id. They also check the weights' sha256
against the preflight record, and whether the committed modules are as at the lock's git HEAD. They record the
sha256 of the preflight record, live_go.py, the pre-registration's tracked copy and the arming mark. --after also
writes the sha256 and line count of the battery folder's manifest.jsonl, verdicts.jsonl and state.json, and the
sha256 of each run's record (<log dir>/<run_id>.jsonl) the manifest names, and (v2, cycle 17) what the outcome labels
read in the plan's memory root (--memory-root): the root's store id, its review queue, the run's conversations and
the memory history. live_readout.py publishes only when the after-file matches the files as they are then and is
committed and pushed, and the before-file was committed and pushed before the run began, for this arming and this
lock. The format is fixed with the pre-registration (FORMAT).
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
sys.path.insert(0, str(Path(__file__).resolve().parent))
PLAN = "first-run-v1.6"
BATTERY = ROOT / "artifacts" / "live-agent" / "battery"
LOGS = ROOT / "artifacts" / "live-agent"
RECORD = ROOT / "reports" / "live-agent"
PREFLIGHT = "reports/live-agent/first-run-v1.6-preflight.json"
CASES = "reports/live-agent/first-run-cases.json"
IMAGE = "local/generic-sandbox:python"  # the sandbox and fakenet gateway image (sandbox.py up: --no-build --pull never)
FORMAT = 3  # 2 (cycle 17): the memory root's files the labels read, the verdicts without the export's time; 3 (cycle 18):
# no path hash in the file, and the first pushes of the record and of the witness before the run, as known after it
LABEL_DECISIONS = ("approve", "reject", "edit", "rollback", "forget", "delete", "revert")  # what changes what labels read
RUN_FILES = ("manifest.jsonl", "verdicts.jsonl", "state.json")


def sha256(path: Path) -> str | None:
    digest = hashlib.sha256()
    try:
        with open(path, "rb") as handle:
            for block in iter(lambda: handle.read(1 << 20), b""):
                digest.update(block)
    except OSError:
        return None
    return digest.hexdigest()


def line_count(path: Path) -> int | None:
    try:
        return Path(path).read_bytes().count(b"\n")
    except OSError:
        return None


def image_id(image: str = IMAGE) -> str | None:
    """The image's id as Docker has it (read-only), None when Docker or the image is not there."""
    try:
        done = subprocess.run(["docker", "image", "inspect", "--format", "{{.Id}}", image], capture_output=True,
                              text=True, timeout=60)
    except (OSError, subprocess.SubprocessError):
        return None
    return (done.stdout.strip() or None) if done.returncode == 0 else None


def weights(preflight: dict, root: Path = ROOT) -> dict:
    """Each weight file's sha256 now, and whether it is the one the preflight record wrote down."""
    out = {}
    for name, item in (preflight.get("weights") or {}).items():
        digest = sha256(Path(root) / name)
        out[name] = {"sha256": digest, "same": digest is not None and digest == (item or {}).get("sha256")}
    return out


def manifest_run_ids(run_dir: Path) -> list[str]:
    ids = []
    try:
        lines = (Path(run_dir) / "manifest.jsonl").read_text(encoding="utf-8").splitlines()
    except OSError:
        return ids
    for line in lines:
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(row, dict) and isinstance(row.get("run_id"), str):
            ids.append(row["run_id"])
    return sorted(set(ids))


def verdicts_sha(path: Path) -> str | None:
    """The verdicts' sha256 without the export's own time (manifest.exported): exporting them again gives the same."""
    try:
        lines = Path(path).read_text(encoding="utf-8").splitlines()
    except OSError:
        return None
    kept = []
    for line in lines:
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            kept.append(line)
            continue
        if isinstance(row, dict) and isinstance(row.get("manifest"), dict):
            row = {**row, "manifest": {key: value for key, value in row["manifest"].items() if key != "exported"}}
        kept.append(json.dumps(row, sort_keys=True, ensure_ascii=False))
    return hashlib.sha256("\n".join(kept).encode("utf-8")).hexdigest()


def pushed_at(commit: str | None, root: Path = ROOT) -> float | None:
    """When the commit first reached a remote branch, as this repository's remote-tracking reflogs keep it (a push or
    a fetch that brought a branch holding it): None when no entry holds it."""
    if not commit:
        return None
    run = lambda *args: subprocess.run(["git", *args], cwd=root, capture_output=True, text=True, timeout=20)
    try:
        refs = run("for-each-ref", "--format=%(refname)", "refs/remotes").stdout.split()
        times = []
        for ref in refs:
            for line in run("reflog", "show", "--date=unix", "--format=%H %gd", ref).stdout.splitlines():
                sha, _, selector = line.partition(" ")
                stamp = selector.rpartition("@{")[2].rstrip("}")
                if stamp.isdigit() and run("merge-base", "--is-ancestor", commit, sha).returncode == 0:
                    times.append(float(stamp))
        return min(times) if times else None
    except (OSError, subprocess.SubprocessError):
        return None


def store_id(memory_root: Path) -> str:
    """The id the server gives a memory root (dashboard_server.store_identity): the sha256 of its resolved path, 12."""
    return hashlib.sha256(str(Path(memory_root).resolve()).encode("utf-8")).hexdigest()[:12]


def memory_files(memory_root: Path, run_dir: Path) -> dict:
    """What the outcome labels read in the plan's memory root (live_outcomes.find_record, memory_after, held_lines):
    the run's conversations, the memory history and the review queue, by sha256; and the root's store id."""
    root = Path(memory_root).resolve()
    conversations = set()
    try:
        lines = (Path(run_dir) / "manifest.jsonl").read_text(encoding="utf-8").splitlines()
    except OSError:
        lines = []
    for line in lines:
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(row, dict) and isinstance(row.get("conversation"), str):
            conversations.add(row["conversation"])
    folder = (root / "conversations").resolve()
    named = {}
    for cid in sorted(conversations):
        path = (folder / f"{cid}.json").resolve()
        if path.parent == folder:
            named[cid] = sha256(path)
    try:
        review = json.loads((root / "manifest.json").read_text(encoding="utf-8")).get("review") or []
    except (OSError, json.JSONDecodeError, AttributeError):
        review = None
    history = {item.name: sha256(item) for item in sorted((root / "history").glob("*.jsonl"))} if (root / "history").is_dir() else {}
    # (no store id here: it is a hash of the folder's path, and this file is pushed; the run's state keeps it)
    return {"conversations": named, "history": history,
            "review": None if review is None else hashlib.sha256(json.dumps(review, sort_keys=True).encode("utf-8")).hexdigest()}


def finished(run_dir: Path, memory_root: Path | None = None, by_path: bool = True) -> dict:
    """Whether the battery ended the run (its state's clear:end, and the verdicts it exports only then, headed by the
    run's lock_sha), and, given a memory root, whether it is the one the run kept (the store id in its state)."""
    try:
        state = json.loads((Path(run_dir) / "state.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        state = {}
    try:
        header = json.loads((Path(run_dir) / "verdicts.jsonl").read_text(encoding="utf-8").splitlines()[0])
    except (OSError, json.JSONDecodeError, IndexError):
        header = {}
    ended = "clear:end" in (state.get("done") or [])
    exported = isinstance(header, dict) and bool(state.get("lock_sha")) and header.get("lock_sha") == state.get("lock_sha")
    # by its path's id (the server's); without it (by_path False: a reader that matched the root's files to the witness
    # after the run instead, as after a move or in another clone)
    own = None if memory_root is None or not by_path else bool(state.get("store")) and store_id(memory_root) == state.get("store")
    # a decision on the memory after the battery ended the run (a held line approved on a page): not the run's
    end_time = next((row.get("time") for row in reversed(manifest_rows(run_dir)) if row.get("case") == "clear-end"), None)
    # only the decisions that change what the labels read count (the battery's own sandbox clear when it runs again after
    # the end, or a setting, do not)
    later = 0 if memory_root is None or not isinstance(end_time, (int, float)) else sum(
        1 for row in jsonl(Path(memory_root) / "decisions.jsonl")
        if isinstance(row.get("time"), (int, float)) and row["time"] > end_time and row.get("action") in LABEL_DECISIONS)
    why = [text for ok, text in ((ended, "the battery did not end the run (no clear:end)"),
                                 (exported, "no verdicts exported under the run's lock"),
                                 (own is not False, "the memory root is not the one the run kept (its store id)"),
                                 (not later, f"{later} decisions on the memory after the run ended (approve, reject, edit, rollback, forget, delete, revert)")) if not ok]
    return {"ok": not why, "ended": ended, "verdicts": exported, "memory_root": own, "decided_after": later, "why": why}


def jsonl(path: Path) -> list[dict]:
    try:
        lines = Path(path).read_text(encoding="utf-8").splitlines()
    except OSError:
        return []
    rows = []
    for line in lines:
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(row, dict):
            rows.append(row)
    return rows


def manifest_rows(run_dir: Path) -> list[dict]:
    return jsonl(Path(run_dir) / "manifest.jsonl")


def reruns_by_case(run_dir: Path, memory_root: Path, root: Path = ROOT) -> dict:
    """Per case of the plan: the starts the server logged for the battery (its audit) beyond the case's turns that
    were not skipped (a turn the battery skipped had no start). Counted case by case, so a skipped turn of one case does
    not hide a turn run again in another; written down after the run (the audit is not hashed, and a moved root may lose it)."""
    try:
        plan = json.loads((Path(root) / CASES).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        plan = {}
    planned = {case.get("id"): len(case.get("turns") or []) for case in plan.get("cases") or []}
    rows = manifest_rows(run_dir)
    skipped = {}
    for row in rows:
        if row.get("skipped") and row.get("case") in planned:
            skipped[row["case"]] = skipped.get(row["case"], 0) + 1
    begin = next((row.get("time") for row in rows if row.get("case") == "clear-start"), None)
    end = next((row.get("time") for row in reversed(rows) if row.get("case") == "clear-end"), None)
    starts = {}
    for name in ("audit.1.jsonl", "audit.jsonl"):
        for row in jsonl(Path(memory_root) / name):
            case = row.get("battery")
            if row.get("action") != "start" or not case or row.get("refused") or case not in planned:
                continue
            if (begin is not None and (row.get("time") or 0) < begin) or (end is not None and (row.get("time") or 0) > end):
                continue
            starts[case] = starts.get(case, 0) + 1
    return {case: extra for case in planned if (extra := starts.get(case, 0) - (planned[case] - skipped.get(case, 0))) > 0}


def run_files(run_dir: Path, log_dir: Path = LOGS) -> dict:
    """The run's own files as they are now: what the readers read."""
    out = {name: {"sha256": verdicts_sha(Path(run_dir) / name) if name == "verdicts.jsonl" else sha256(Path(run_dir) / name),
                  "lines": line_count(Path(run_dir) / name)} for name in RUN_FILES}
    folder = Path(log_dir).resolve()
    records = {}
    for run_id in manifest_run_ids(run_dir):
        path = (folder / f"{run_id}.jsonl").resolve()
        if path.parent == folder:  # a run id naming a file elsewhere is not followed
            records[run_id] = sha256(path)
    out["records"] = records
    return out


def witness(kind: str, plan: str = PLAN, root: Path = ROOT, battery: Path = BATTERY, log_dir: Path = LOGS,
            prereg_out: Path | None = None, image: str = IMAGE, memory_root: Path | None = None,
            record_dir: Path | None = None) -> dict:
    import live_battery as LB
    import live_go as GO
    import live_prereg as PRE

    run_dir = Path(battery) / plan
    lock = json.loads((run_dir / "lock.json").read_text(encoding="utf-8"))
    preflight_path = Path(root) / PREFLIGHT
    preflight = json.loads(preflight_path.read_text(encoding="utf-8")) if preflight_path.is_file() else {}
    named = (PREFLIGHT, "argus_hook/live_go.py", f"reports/live-agent/prereg-{plan}.json")
    body = {"format": FORMAT, "kind": kind, "plan": plan, "time": round(time.time(), 3), "lock_sha": LB.lock_sha(lock),
            "image": {"name": image, "id": image_id(image)}, "weights": weights(preflight, root),
            "committed_modules": GO.committed_modules(preflight, lock.get("git_head"), root),
            "files": {name: sha256(Path(root) / name) for name in named},
            "armed": sha256(Path(prereg_out or PRE.OUT) / plan / "armed.json")}
    if kind == "after":
        body["run"] = run_files(run_dir, log_dir)
        body["memory"] = memory_files(memory_root, run_dir) if memory_root is not None else None
        body["reruns"] = reruns_by_case(run_dir, memory_root, root) if memory_root is not None else None
        # the first pushes as this repository knows them now (its reflog may expire later, or another clone not hold it)
        pushes = {}
        for name, path in (("record", Path(root) / "reports" / "live-agent" / f"prereg-{plan}.json"),
                           ("before", Path(record_dir if record_dir is not None else RECORD) / f"witness-{plan}-before.json")):
            known = PRE.anchored(path, None, root) if path.exists() else {}
            pushes[name] = {"commit": known.get("commit"), "first_push": pushed_at(known.get("commit"), root)}
        body["pushes"] = pushes
    return body


def problems(body: dict) -> list[str]:
    out = []
    if not (body.get("image") or {}).get("id"):
        out.append("no sandbox image id (Docker or the image is not there)")
    if not body.get("weights") or not all(item.get("same") for item in body["weights"].values()):
        out.append("a weight file is not the one the preflight record names")
    if not (body.get("committed_modules") or {}).get("ok"):
        out.append("the committed modules are not as at the lock's git HEAD")
    if not body.get("armed"):
        out.append("not armed (live_prereg.py --check --arm first)")
    if body.get("kind") == "after" and not body.get("memory"):
        out.append("the plan's memory root is not witnessed (--memory-root)")
    return out


def write(body: dict, record: Path | None = None) -> Path:
    path = Path(record if record is not None else RECORD) / f"witness-{body['plan']}-{body['kind']}.json"
    if path.exists():
        raise ValueError(f"{path} exists: a witness is written once")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(body, indent=1) + "\n", encoding="utf-8")
    return path


def matches(after: dict, run_dir: Path, log_dir: Path = LOGS, memory_root: Path | None = None) -> dict:
    """Whether the run's files, and what the labels read in the memory root, are now those the after-witness wrote
    down (a witness without the memory root, or no root given, does not match)."""
    now = run_files(run_dir, log_dir)
    then = after.get("run") or {}
    differs = [name for name in RUN_FILES if (now.get(name) or {}).get("sha256") != (then.get(name) or {}).get("sha256")]
    if now.get("records") != then.get("records"):
        differs.append("records")
    memory = after.get("memory")
    if not memory or memory_root is None:
        differs.append("memory root (not witnessed)")
    else:
        current = memory_files(memory_root, run_dir)
        differs += [f"memory {name}" for name in ("conversations", "history", "review") if current.get(name) != memory.get(name)]
    return {"same": not differs and bool(then), "differs": differs}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    which = parser.add_mutually_exclusive_group(required=True)
    which.add_argument("--before", action="store_true", help="right before the run (after arming)")
    which.add_argument("--after", action="store_true", help="right after the run: then commit and push the file")
    parser.add_argument("--plan", default=PLAN)
    parser.add_argument("--log-dir", type=Path, default=LOGS)
    parser.add_argument("--memory-root", type=Path, default=None,
                        help="with --after: the plan's memory root (ARGUS_LIVE_MEMORY_DIR), whose files the labels read")
    args = parser.parse_args(argv)
    if args.after and args.memory_root is None:
        print("stop: --after needs --memory-root (the plan's memory root)", file=sys.stderr)
        return 4
    if args.after:  # written once: never for a run that has not ended, nor of another memory root
        done = finished(BATTERY / args.plan, args.memory_root)
        if not done["ok"]:
            print(f"stop: not written: {'; '.join(done['why'])}", file=sys.stderr)
            return 4
    try:
        body = witness("before" if args.before else "after", args.plan, log_dir=args.log_dir.resolve(),
                       memory_root=args.memory_root.resolve() if args.memory_root else None)
        path = write(body)
    except (OSError, ValueError, KeyError) as error:
        print(f"stop: {type(error).__name__}: {error}", file=sys.stderr)
        return 4
    found = problems(body)
    print(json.dumps({"written": str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path),
                      "problems": found, "next": "git add the file, commit and push it now"}, ensure_ascii=False))
    return 1 if found else 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Counterfactual rescoring of live-chat steps, the model-free half (R2; pre-registered with live_prereg.py, plan in
reports/live-agent/rescore-plan.md): six transformations of a step's exact input, each a pure function that changes
one thing and only where its marker appears exactly once in the whole input, and the checks (--check, CPU) that they
are right on a run before any verdict is computed again. Scoring the transformed inputs (--score, GPU) is a later
tool with its own lock and its own permission.

The transformations (a generation → a generation, or None: "does not apply"):
  minus_notice   the system prompt without the sentence that a monitor scores every command
  minus_memory   without the memory: the system prompt's memory part (MEMORY_PROMPT to its end) and the request's
                 <saved_memory> block with its note
  minus_history  without the earlier turns: their messages, and the request's "This conversation" lines become a
                 first turn's
  minus_recent   the request's list of other recent conversations left out
  swap_hint      the last-step hint in the other wording (v4 <-> v5)
  swap_effort    the reasoning effort None <-> low
The markers come from the frozen copy of agent_memory.py, and only when its sha256 is the lock's.

What --check measures on a run (numbers and case ids only):
  I0 every generation renders back to its recorded prompt ids (live_rescore.identity)
  I1 minus_notice(P0k-off step 1) is M0k step 1
  I2 minus_memory(minus_history(P0k-on step 1)) is P0k-off step 1
  I3 swap_hint(H00 step 2) is H01 step 2
  I4 swap_effort(E01.2's memory step) is E02.1's memory step
  I6 a pair rendered on two days is not compared (the date is in every prompt)
A pair whose twins already parted before the compared input (I3, I4: a generated command or its output differed) is
"diverged", not a failure of the transformation. A turn whose record lacks a generation is "incomplete" (no evidence
is never counted as the same). A transformation is "usable" for a later scoring only when at least one of its pairs
came out the same and none differed; the others are exploratory.
I5 (removals leave no marker, swaps undo themselves, pairs commute or absorb) and I7 (a marker the request repeats:
does not apply) are unit tests on built inputs. A turn that touched the sealed pages is never read past its seal.

    python argus_hook/live_counterfactual.py --check --run artifacts/live-agent/battery/first-run-v1.6
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
import live_rescore as LR  # noqa: E402  (stdlib only at import; the tokenizer loads in main)

MARKER_NAMES = ("MONITOR_SENTENCE", "MEMORY_PROMPT", "SAVED_MEMORY_NOTE", "LAST_STEP_HINT", "LAST_STEP_HINT_V5")
LITERALS = {"conversation": "## This conversation (", "first_turn": "This is the first turn of a new conversation.",
            "recent": "## Other recent conversations (titles are the user's words, quoted)\n",
            "open": "<saved_memory>", "close": "</saved_memory>"}
TOKENIZER_FILES = ("gpt-oss-20b/tokenizer.json", "gpt-oss-20b/tokenizer_config.json",
                   "gpt-oss-20b/special_tokens_map.json", "gpt-oss-20b/chat_template.jinja")
PAIRS = {  # invariant: [(the turn transformed, its twin)]
    "I1": [("P01-off.1", "M01.1"), ("P02-off.1", "M02.1"), ("P03-off.1", "M03.1")],
    "I2": [("P01-on-base.2", "P01-off.1"), ("P02-on.1", "P02-off.1"), ("P03-on.1", "P03-off.1")],
    "I3": [("H00.1", "H01.1")],
    "I4": [("E01.2", "E02.1")],
}
WHERE = {"I1": ("main", 1), "I2": ("main", 1), "I3": ("main", 2), "I4": ("memory", None)}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def markers(path: Path, expected: str | None = None) -> dict:
    """The marker strings, read from agent_memory.py without running it (and only if it is the locked file)."""
    data = Path(path).read_bytes()
    if expected is not None and digest(data) != expected:
        raise ValueError("the frozen agent_memory.py is not the locked one")
    source = data.decode("utf-8")
    found = {}
    for node in ast.parse(source).body:
        if (isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name)
                and node.targets[0].id in MARKER_NAMES):
            found[node.targets[0].id] = ast.literal_eval(node.value)
    missing = [name for name in MARKER_NAMES if not isinstance(found.get(name), str) or not found[name]]
    if missing:
        raise ValueError(f"agent_memory.py has no {', '.join(missing)}")
    gone = [literal for literal in LITERALS.values() if literal.rstrip("\n") not in source]
    if gone:
        raise ValueError(f"agent_memory.py no longer writes {gone[0]!r}")
    return {"monitor": found["MONITOR_SENTENCE"], "memory": found["MEMORY_PROMPT"], "note": found["SAVED_MEMORY_NOTE"],
            "hint": found["LAST_STEP_HINT"], "hint_v5": found["LAST_STEP_HINT_V5"], **LITERALS}


# ---------------------------------------------------------------------------- the transformations (pure)
def _count(messages: list[dict], text: str) -> int:
    return sum(str(message.get("content") or "").count(text) for message in messages)


def _with(gen: dict, messages: list[dict], **changes) -> dict:
    return {**gen, "messages": messages, "prompt_ids": None, **changes}  # a changed input has no recorded ids


def minus_notice(gen: dict, M: dict) -> dict | None:
    messages = gen["messages"]
    if not messages or messages[0].get("role") != "system" or _count(messages, M["monitor"]) != 1 \
            or M["monitor"] not in messages[0]["content"]:
        return None
    return _with(gen, [{**messages[0], "content": messages[0]["content"].replace(M["monitor"], "")}, *messages[1:]])


def minus_memory(gen: dict, M: dict) -> dict | None:
    index, messages = gen.get("request_index"), gen["messages"]
    if index is None or not messages or messages[0].get("role") != "system":
        return None
    system, request = messages[0]["content"], str(messages[index].get("content") or "")
    head = f"{M['close']}\n{M['note']}\n\n"
    opened = _count(messages, M["open"]) - M["memory"].count(M["open"])  # MEMORY_PROMPT itself names the block
    if (_count(messages, M["memory"]) != 1 or M["memory"] not in system or opened != 1
            or not request.startswith(M["open"]) or _count(messages, head) != 1 or head not in request):
        return None
    out = list(messages)
    out[0] = {**messages[0], "content": system[:system.index(M["memory"])]}
    out[index] = {**messages[index], "content": request[request.index(head) + len(head):]}
    return _with(gen, out)


def minus_history(gen: dict, M: dict) -> dict | None:
    index, messages = gen.get("request_index"), gen["messages"]
    if index is None or index < 2:  # nothing earlier in the input
        return None
    request = str(messages[index].get("content") or "")
    if M["open"] in request:  # with memory, the conversation's lines become those of a first turn
        head = f"\n\n{M['close']}\n{M['note']}"
        if (_count(messages, M["conversation"]) != 1 or M["conversation"] not in request
                or _count(messages, M["recent"]) > 1 or _count(messages, head) != 1):
            return None
        start = request.index(M["conversation"])
        line_end = request.find("\n", start)
        if line_end < 0:
            return None
        # the section runs to the next part the block builds (the recent list, or the block's end): a command it
        # shows may hold blank lines or a "## " line of its own
        ends = [request.find("\n\n" + M["recent"], line_end), request.find(head, line_end)]
        end = min((value for value in ends if value >= 0), default=-1)
        if end < 0:
            return None
        request = request[:line_end + 1] + M["first_turn"] + request[end:]
    return _with(gen, [messages[0], {**messages[index], "content": request}, *messages[index + 1:]], request_index=1)


def minus_recent(gen: dict, M: dict) -> dict | None:
    index, messages = gen.get("request_index"), gen["messages"]
    if index is None:
        return None
    request = str(messages[index].get("content") or "")
    if _count(messages, M["recent"]) != 1 or M["recent"] not in request:
        return None
    start = request.index(M["recent"])
    end = request.find("\n\n", start)
    if end < 0 or not request[:start].endswith("\n\n"):
        return None
    out = list(messages)
    out[index] = {**messages[index], "content": request[:start - 2] + request[end:]}
    return _with(gen, out)


def swap_hint(gen: dict, M: dict) -> dict | None:
    messages = gen["messages"]
    v4, v5 = _count(messages, M["hint"]), _count(messages, M["hint_v5"])
    if v4 + v5 != 1:
        return None
    old, new = (M["hint"], M["hint_v5"]) if v4 else (M["hint_v5"], M["hint"])
    return _with(gen, [{**message, "content": message["content"].replace(old, new)}
                       if old in str(message.get("content") or "") else message for message in messages])


def swap_effort(gen: dict, _M: dict | None = None) -> dict | None:
    effort = gen.get("reasoning_effort")
    if effort not in (None, "low"):
        return None
    return {**gen, "reasoning_effort": None if effort == "low" else "low", "prompt_ids": None}


TRANSFORMS = {"minus_notice": minus_notice, "minus_memory": minus_memory, "minus_history": minus_history,
              "minus_recent": minus_recent, "swap_hint": swap_hint, "swap_effort": swap_effort}
APPLY = {"I1": lambda gen, M: minus_notice(gen, M),
         "I2": lambda gen, M: (lambda bare: minus_memory(bare, M) if bare else None)(minus_history(gen, M)),
         "I3": lambda gen, M: swap_hint(gen, M),
         "I4": lambda gen, M: swap_effort(gen, M)}


# ---------------------------------------------------------------------------- a run
def read_jsonl(path: Path) -> list[dict]:
    return LR.read_records(path) if Path(path).is_file() else []


def turn_keys(rows: list[dict]) -> list[tuple[str, dict]]:
    """The plan key of every turn the run kept (as live_outcomes.turn_keys: the k-th turn of a case is turn k)."""
    by_case: dict[str, list[dict]] = {}
    order: list[str] = []
    for row in rows:
        case = row.get("case")
        if not isinstance(case, str) or case.startswith("clear-"):
            continue
        kept = by_case.setdefault(case, [])
        if case not in order:
            order.append(case)
        last = kept[-1] if kept else None
        if (last is not None and row.get("turn") is not None and last.get("turn") == row.get("turn")
                and last.get("conversation") == row.get("conversation")):
            kept[-1] = row
        else:
            kept.append(row)
    return [(f"{case}.{index}", row) for case in order for index, row in enumerate(by_case[case], start=1)]


def sealed(row: dict, records: list[dict]) -> bool:
    return bool(row.get("sealed") or row.get("argus_pages")) or any(
        item.get("sealed") or item.get("argus_page") or (item.get("type") == "fakenet" and item.get("argus"))
        for item in records)


def generations(records: list[dict]) -> list[dict]:
    """live_rescore.rebuild, with where each main input's request is (None for a resumed turn or the memory step)."""
    first = next((row["messages"] for row in records if row.get("type") == "context"
                  and isinstance(row.get("messages"), list) and row.get("phase") != "memory"), None)
    features = next((row.get("features") for row in records if row.get("type") == "context"
                     and not isinstance(row.get("messages"), list)), None) or []
    resumed = "resume" in features
    texts = {(int(row.get("step") or 0), int(row.get("attempt") or 1)): row.get("text")
             for row in records if row.get("type") == "generation"}
    out = []
    for gen in LR.rebuild(records):
        index = len(first) - 1 if gen["phase"] == "main" and first and not resumed else None
        out.append({**gen, "request_index": index, "generated": texts.get((gen["step"], gen["attempt"]))})
    return out


def pick(gens: list[dict], phase: str, step: int | None) -> dict | None:
    """The first attempt of a step (a corrected attempt reads a correction turn: not compared)."""
    for gen in gens:
        if gen["phase"] == phase and gen["attempt"] == 1 and (step is None or gen["step"] == step):
            return gen
    return None


def lock_sha(lock: dict) -> str:  # live_battery.lock_sha (a test keeps them the same)
    body = {key: lock.get(key) for key in ("plan", "files", "git_head")}
    return hashlib.sha256(json.dumps(body, sort_keys=True).encode("utf-8")).hexdigest()[:16]


def diverged(name: str, a: dict, b: dict, M: dict, a_all: list[dict] = (), b_all: list[dict] = ()) -> bool:
    """The twins took different paths before the compared input: what the model generated earlier (or the output of
    that command) differed, so the inputs cannot match whatever the transformation does. A difference in what was built
    before any generation (system, history, request, memory files) is not a parting: it is left to "differ".
    Only for the inputs read after a generation (I3: step 2; I4: the memory step)."""
    main = lambda gens: [gen.get("generated") for gen in gens if gen["phase"] == "main"]
    if name == "I3":
        index = a.get("request_index")
        if index is None or a["messages"][:index + 1] != b["messages"][:index + 1]:
            return False  # built before the first generation: a real difference
        if [gen.get("generated") for gen in a_all if gen["phase"] == "main" and gen["step"] == 1] != \
                [gen.get("generated") for gen in b_all if gen["phase"] == "main" and gen["step"] == 1]:
            return True
        bare = lambda gen: [str(message.get("content") or "").replace(M["hint"], "").replace(M["hint_v5"], "")
                            for message in gen["messages"][index + 1:]]
        return bare(a) != bare(b)  # the same command, another output
    if name == "I4":
        return main(a_all) != main(b_all)
    return False


def compare(pairs: dict, by_key: dict, M: dict, render=None) -> dict:
    """Each invariant over its pairs: {"pairs", "same", "differ", "diverged", "na", "other_day", "missing", "sealed",
    "usable"}. A transformation is usable later only when at least one pair came out the same and none differed."""
    out = {}
    for name, items in pairs.items():
        phase, step = WHERE[name]
        row = {"pairs": len(items), "same": 0, "differ": [], "diverged": [], "na": [], "other_day": [], "missing": [],
               "sealed": 0}
        for left, right in items:
            if by_key.get(left) == "sealed" or by_key.get(right) == "sealed":
                row["sealed"] += 1
                continue
            a = pick(by_key.get(left) or [], phase, step)
            b = pick(by_key.get(right) or [], phase, step)
            if a is None or b is None:
                row["missing"].append(left)
                continue
            if a.get("render_date") != b.get("render_date"):  # I6: the date is in every prompt
                row["other_day"].append(left)
                continue
            moved = APPLY[name](a, M)
            if moved is None:
                row["na"].append(left)
                continue
            if diverged(name, a, b, M, by_key.get(left) or [], by_key.get(right) or []):
                row["diverged"].append(left)
                continue
            same = moved["messages"] == b["messages"] and moved.get("reasoning_effort") == b.get("reasoning_effort")
            if same and render is not None and b.get("prompt_ids"):
                same = render(moved) == [int(token) for token in b["prompt_ids"]]
            if same:
                row["same"] += 1
            else:
                row["differ"].append(left)
        row["usable"] = row["same"] >= 1 and not row["differ"]
        out[name] = row
    return out


def complete(row: dict, records: list[dict]) -> bool:
    """Every generation the turn made is in its record with its prompt ids: as many as its accepted actions and
    refused attempts (the manifest's steps and format failures)."""
    generations = [item for item in records if item.get("type") == "generation"]
    expected = len(row.get("steps") or []) + int(row.get("format_failures") or 0)
    return len(generations) == expected and all(item.get("prompt_ids") for item in generations)


def check(run_dir: Path, log_dir: Path, frozen: Path, tokenizer=None) -> dict:
    lock = json.loads((Path(run_dir) / "lock.json").read_text(encoding="utf-8"))
    rows = read_jsonl(Path(run_dir) / "manifest.jsonl")
    sha = lock_sha(lock)
    if any(row.get("lock_sha") not in (None, sha) for row in rows):
        raise ValueError("a line of the run was kept under another lock")
    M = markers(Path(frozen) / "argus_hook" / "agent_memory.py", (lock.get("files") or {}).get("argus_hook/agent_memory.py"))
    folder = Path(log_dir).resolve()
    by_key: dict[str, object] = {}
    paths: dict[str, Path] = {}
    incomplete: list[str] = []
    for key, row in turn_keys(rows):
        run_id = row.get("run_id")
        if not isinstance(run_id, str):
            continue
        path = (folder / f"{run_id}.jsonl").resolve()
        if path.parent != folder:  # run ids from the manifest name records in the record folder only
            raise ValueError("a run id names a file outside the record folder")
        records = read_jsonl(path)
        by_key[key] = "sealed" if sealed(row, records) else generations(records)
        paths[key] = path
        if by_key[key] != "sealed" and not row.get("skipped") and not complete(row, records):
            incomplete.append(key)  # a missing line is no evidence: it is said, never counted as the same
    render = None
    if tokenizer is not None:
        render = lambda gen: LR.render(tokenizer, gen["messages"], gen.get("reasoning_effort"), gen.get("render_date"))
    result = compare(PAIRS, by_key, M, render)
    if tokenizer is not None:
        here = digest((ROOT / "argus_hook" / "live_agent.py").read_bytes())
        corrections = here == (lock.get("files") or {}).get("argus_hook/live_agent.py")
        total = {"tasks": 0, "generations": 0, "same": 0, "differ": 0, "unrecorded": 0, "corrected_skipped": 0}
        for key, item in by_key.items():
            if item == "sealed":
                continue
            records = read_jsonl(paths[key])
            if not corrections:  # the correction turns would come from a changed live_agent.py: first attempts only
                skipped = sum(1 for row in records if row.get("type") == "generation" and int(row.get("attempt") or 1) > 1)
                records = [row for row in records if not (row.get("type") == "generation" and int(row.get("attempt") or 1) > 1)]
                total["corrected_skipped"] += skipped
            same = LR.identity(tokenizer, records)
            total["tasks"] += 1
            for name in ("generations", "same", "unrecorded"):
                total[name] += same[name]
            total["differ"] += len(same["differ"])
        result["I0"] = total
    result["sealed_turns"] = sum(1 for item in by_key.values() if item == "sealed")
    result["incomplete"] = incomplete
    result["usable"] = [name for name in PAIRS if result[name]["usable"]]
    result["lock_sha"] = sha  # the same for every run of the plan: the manifest's own hash says which run it read
    result["manifest_sha256"] = digest((Path(run_dir) / "manifest.jsonl").read_bytes()) if (Path(run_dir) / "manifest.jsonl").is_file() else None
    return result


def tokenizer_dir(frozen: Path, lock: dict) -> Path:
    """The tokenizer the run used: the frozen copy (else the working tree), each file as the lock has it."""
    for base in (Path(frozen), ROOT):
        if all((base / name).is_file() and digest((base / name).read_bytes()) == (lock.get("files") or {}).get(name)
               for name in TOKENIZER_FILES):
            return base / "gpt-oss-20b"
    raise ValueError("no tokenizer matches the lock")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--check", action="store_true", help="the invariants on a run (CPU)")
    parser.add_argument("--run", type=Path, default=ROOT / "artifacts" / "live-agent" / "battery" / "first-run-v1.6")
    parser.add_argument("--log-dir", type=Path, default=ROOT / "artifacts" / "live-agent")
    parser.add_argument("--no-render", action="store_true", help="compare the messages only (no tokenizer)")
    args = parser.parse_args(argv)
    if not args.check:
        parser.print_help()
        return 2
    try:
        lock = json.loads((args.run / "lock.json").read_text(encoding="utf-8"))
        tokenizer = None
        if not args.no_render:
            from transformers import AutoTokenizer

            tokenizer = AutoTokenizer.from_pretrained(str(tokenizer_dir(args.run / "frozen", lock)), local_files_only=True)
        import live_prereg  # whether this tool, its plan and the run are the pre-registered ones

        prereg = live_prereg.check(str(lock.get("plan")), battery=args.run.parent, run=args.run,
                                   used={"argus_hook/live_counterfactual.py": Path(__file__),
                                         "reports/live-agent/rescore-plan.md": ROOT / "reports" / "live-agent" / "rescore-plan.md"})
        if not prereg.get("target_matches", False) and prereg.get("reason") != "not frozen":
            raise ValueError("the pre-registration was frozen for another lock than this run's")
        result = check(args.run, args.log_dir, args.run / "frozen", tokenizer)
        result["prereg"] = prereg
    except (OSError, ValueError) as error:
        print(f"stop: {error}", file=sys.stderr)
        return 4
    print(json.dumps(result))
    identity = result.get("I0") or {}
    bad = (any(row["differ"] for name, row in result.items() if name in PAIRS) or result["incomplete"]
           or identity.get("differ") or identity.get("unrecorded"))
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())

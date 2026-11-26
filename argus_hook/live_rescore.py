"""Rescoring live-chat steps, the model-free half (first-run plan §5): rebuild the exact input of every generation
from a task record, render it again with the CPU tokenizer, and check that it is the prompt the model read, token for
token. Only then can a step be judged again in a changed context (the transformations and the scoring are a later,
separately locked tool).

The record of a task (artifacts/live-agent/<run id>.jsonl, written by live_agent.py) holds:
- "context": the whole input of step 1 (and of each memory step, phase "memory");
- "context_append": what each main step added (the command and the output as the agent read it);
- "attempt_failed": a refused reply and why (the next attempt read it with the correction turn);
- "generation": each attempt's prompt ids and reasoning effort;
- the "context" event: the date the prompt was rendered on (the chat template writes it).

    python argus_hook/live_rescore.py --log-dir artifacts/live-agent --run-id live-...   (numbers only on stdout)
"""

from __future__ import annotations

import argparse
import contextlib
import datetime
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / "argus_hook"), str(ROOT / "src"), str(ROOT)]


def read_records(path: Path) -> list[dict]:
    rows = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(row, dict):
            rows.append(row)
    return rows


def correction(reason: str) -> str:
    """The correction turn after a refused reply (live_agent.correction_turn, from the recorded reason)."""
    import live_agent as LA

    return LA.correction_turn(ValueError(reason))


def rebuild(records: list[dict]) -> list[dict]:
    """Every generation of one task with the messages it read: [{"step", "attempt", "phase", "messages",
    "reasoning_effort", "prompt_ids", "render_date"}]."""
    render_date = next((row.get("render_date") for row in records if row.get("type") == "context"
                        and row.get("render_date")), None)
    first, appended, memory, failed = None, {}, {}, {}
    for row in records:
        kind = row.get("type")
        if kind == "context" and isinstance(row.get("messages"), list):
            if row.get("phase") == "memory":
                memory[int(row.get("step") or 0)] = row["messages"]
            elif first is None:
                first = row["messages"]
        elif kind == "context_append" and isinstance(row.get("messages"), list):
            appended[int(row.get("step") or 0)] = row["messages"]
        elif kind == "attempt_failed":
            failed[(int(row.get("step") or 0), int(row.get("attempt") or 0))] = row
    out = []
    for row in records:
        if row.get("type") != "generation":
            continue
        step, attempt = int(row.get("step") or 0), int(row.get("attempt") or 1)
        if step in memory:
            phase, base = "memory", list(memory[step])
        elif first is not None:
            phase, base = "main", list(first)
            for earlier in sorted(index for index in appended if index < step):
                base += appended[earlier]
        else:
            continue
        for tried in range(1, attempt):  # each refused reply and its correction, as the worker added them
            refused = failed.get((step, tried))
            if refused is None:
                break
            base += [{"role": "assistant", "content": refused.get("reply") or ""},
                     {"role": "user", "content": correction(str(refused.get("reason") or ""))}]
        out.append({"step": step, "attempt": attempt, "phase": phase, "messages": base,
                    "reasoning_effort": row.get("reasoning_effort"), "prompt_ids": row.get("prompt_ids"),
                    "render_date": render_date})
    return out


@contextlib.contextmanager
def rendered_on(tokenizer, date: str | None):
    """The chat template writes today's date into every prompt: fixed to the day the step was rendered on."""
    if not date:
        yield
        return
    from transformers.utils import chat_template_utils as templates

    template = templates._compile_jinja_template(tokenizer.chat_template)
    day = datetime.datetime.strptime(date, "%Y-%m-%d")
    before = template.globals.get("strftime_now")
    template.globals["strftime_now"] = lambda fmt: day.strftime(fmt)
    try:
        yield
    finally:
        template.globals["strftime_now"] = before


def render(tokenizer, messages: list[dict], effort: str | None = None, date: str | None = None) -> list[int]:
    """The prompt ids of ``messages`` as the worker renders them (live_agent.Runtime.sample)."""
    extra = {"reasoning_effort": effort} if effort else {}
    with rendered_on(tokenizer, date):
        encoded = tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=True, return_dict=True,
                                                **extra)
    return [int(token) for token in encoded["input_ids"]]


def identity(tokenizer, records: list[dict]) -> dict:
    """How many generations of one task render back to the recorded prompt ids: {"generations", "same",
    "differ": [(phase, step, attempt)], "unrecorded"}."""
    steps = rebuild(records)
    same, differ, unrecorded = 0, [], 0
    for item in steps:
        if not item["prompt_ids"]:
            unrecorded += 1
            continue
        ids = render(tokenizer, item["messages"], item["reasoning_effort"], item["render_date"])
        if ids == [int(token) for token in item["prompt_ids"]]:
            same += 1
        else:
            differ.append((item["phase"], item["step"], item["attempt"]))
    return {"generations": len(steps), "same": same, "differ": differ, "unrecorded": unrecorded}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--log-dir", type=Path, default=ROOT / "artifacts" / "live-agent")
    parser.add_argument("--run-id", action="append", default=[], help="a task's run id (default: every record)")
    args = parser.parse_args(argv)
    folder = args.log_dir.resolve()
    paths = [folder / f"{run}.jsonl" for run in args.run_id] if args.run_id else sorted(folder.glob("live-*.jsonl"))
    if any(path.resolve().parent != folder for path in paths):  # only the records of this folder
        print("stop: a run id names a file outside the record folder", file=sys.stderr)
        return 2
    from transformers import AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained(str(ROOT / "gpt-oss-20b"), local_files_only=True)
    total = {"tasks": 0, "generations": 0, "same": 0, "differ": 0, "unrecorded": 0}
    for path in paths:
        if not path.is_file():
            continue
        result = identity(tokenizer, read_records(path))
        total["tasks"] += 1
        for key in ("generations", "same", "unrecorded"):
            total[key] += result[key]
        total["differ"] += len(result["differ"])
    print(json.dumps(total))
    return 0 if not total["differ"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

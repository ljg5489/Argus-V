"""The rehearsal worker (tests/rehearsal_worker.py: the real live_agent code, no GPU) with the unlimited turn's guards
of argus_hook/live_agent_free.py mixed in, as the real free worker mixes them into live_agent.Runtime.

REHEARSAL_FREE_PLAN (JSON) scripts the turn: {"commands": [...]} run in order, then {"repeat": "cmd"} for ever if
given, else the answer. A command "big N" prints an output of about N characters that differs on every run.

    python tests/rehearsal_free_worker.py      (started by a test in place of argus_hook/live_agent_free.py)
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / "tests"), str(ROOT / "argus_hook")]

import rehearsal_worker as RW  # noqa: E402  (needs REHEARSAL_STATE and REHEARSAL_LOG_DIR)
import live_agent_free as FREE  # noqa: E402

FREE.install(RW.LA, RW.AM)
PLAN = json.loads(os.environ.get("REHEARSAL_FREE_PLAN") or "null")
GUARD = FREE.GUARD
CREATED: set[str] = set()  # files a rehearsal command "made" (an apply_patch Add File, a cat > file)
# The sandbox's file list for the answer check: the plan's "files" and what the turn made (no "files": not known,
# so nothing is checked and no real sandbox is ever asked).
GUARD.STATE["lister"] = lambda: None if not PLAN or PLAN.get("files") is None else list(PLAN["files"]) + sorted(CREATED)
GUARD.configure(web=bool(PLAN and PLAN.get("web")), screen=bool(PLAN and PLAN.get("screen")), tools=bool(PLAN and PLAN.get("tools")))
RAW = list((PLAN or {}).get("raw") or [])  # "raw": each main generation's last message as the model writes it, in order


class Sandbox(RW.Sandbox):
    runs = 0

    def run(self, command: str, timeout: int = 120):
        import re

        CREATED.update(re.findall(r"\*\*\* Add File: (\S+)", command) + re.findall(r"\bcat > (\S+)", command))
        if command.startswith("big "):
            Sandbox.runs += 1
            size = int(command.split()[1])
            out = (f"run {Sandbox.runs} " + "가나다라 data line\n" * (size // 17))[:size]
            data = {"status": "FINISHED", "exit_code": 0, "stdout_tail": out, "stderr_tail": "",
                    "bytes": {"stdout": len(out), "stderr": 0}}
            return RW.LA.observation_text(data), data
        return super().run(command, timeout)


class RehearsalFree(FREE.FreeSteps, RW.Rehearsal):
    def reply_for(self, messages, digest):
        if not PLAN:
            return super().reply_for(messages, digest)
        step, commands = self.turn_steps, PLAN.get("commands") or []
        if step <= len(commands):
            return f"```bash\n{commands[step - 1]}\n```"
        if PLAN.get("repeat"):
            return f"```bash\n{PLAN['repeat']}\n```"
        return f"```stop\n리허설 답입니다 ({digest}).\n```"


    def sample(self, messages, step, attempt, seed, cancel):
        """With "raw" in the plan: the next main generation is that text after `<|start|>assistant` (a tool call with
        options, two blocks, an answer that names a file), as gpt-oss writes it."""
        if not RAW or getattr(self, "phase", None) == "memory":
            return super().sample(messages, step, attempt, seed, cancel)
        effort = {"reasoning_effort": self.reasoning_effort} if getattr(self, "reasoning_effort", None) else {}
        encoded = self.tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=True, return_dict=True, **effort)
        prompt = [int(token) for token in encoded["input_ids"]]
        text = f"<|channel|>analysis<|message|>step {step}<|end|><|start|>assistant" + RAW.pop(0)
        generated = self.tokenizer.encode(text, add_special_tokens=False)
        RW.LA.emit("generation_start", step=step, attempt=attempt, prompt_tokens=len(prompt), seed=seed)
        RW.LA.keep("generation", step=step, attempt=attempt, seed=seed, prompt_tokens=len(prompt), generated_tokens=len(generated),
                   text=text, ids=generated, prompt_ids=prompt, prompt_sha=RW.AM.ids_sha(prompt), reasoning_effort=None)
        return {"prompt_ids": prompt, "generated_ids": generated, "pieces": self.tokenizer.convert_ids_to_tokens(prompt + generated),
                "text": text, "seconds": 0.0, "seed": seed}


def make_runtime():
    RW.Rehearsal = RehearsalFree  # make_runtime builds the module's Rehearsal
    runtime = RW.make_runtime()
    runtime.sandbox = Sandbox()
    return runtime


if __name__ == "__main__":
    raise SystemExit(RW.LA.main(make_runtime=make_runtime))

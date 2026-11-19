# 파일 위치: ~/Desktop/Argus-V/argus_hook/live_agent.py
"""Live agent worker behind the Scenario Studio chat tab: the local gpt-oss-20b works in the local SANDBOX and
Argus-V-emp judges every step before its command runs.

dashboard_server.py starts one worker process through live_agent_service.py. The process keeps gpt-oss-20b on the
GPU and the Argus-V-emp model files in memory until it is told to stop, so only the first task waits for loading.
A task runs the bash/stop protocol of agent_loop.py in the SANDBOX (network fakenet), with agent_loop's system
prompt plus one line saying that the stop block is the answer the user reads. Every step is reported while it
happens:

  1. one reply is sampled as in scenario_rollout.py (temperature 1.0, top-p 1.0, at most 2,048 new tokens) and
     streamed while it is generated
  2. the action is read with the rollouts' parser (scenario_rollout.parse_agent_action). A reply it refuses that
     executes nothing (a direct answer such as "55", an empty stop block) is taken as the answer; any other refused
     reply is generated again after a correction turn that repeats only the refused final message (at most 4
     attempts, the scenario_rollout default). A command only runs when it is the entire final message.
  3. reasoning and action tokens are located with scenario_rollout.harmony_spans; observation points every 32
     reasoning tokens come from scenario_rollout.observation_points (the 32-token grid Argus-V was fitted on)
  4. the pre-action prefix is replayed in full and blocks 16 and 23 are captured at those points
     (argus_v.activations.extract_prefix, the capture function of the rollouts)
  5. the two Argus-V-emp inputs are pooled with build_features.thin_to_grid32 / pool_step and stored as float16,
     as the evaluation features were: layer 23 maximum over the points, layer 16 at pre_action
  6. Argus-V-emp scores the step (argus_v_emp_model.EmpModel) against its validation cut-offs
  7. only then the command runs in the sandbox (sandbox.py run, 120-second limit); the observation goes back to
     the agent as in agent_loop.py

The verdict is computed before the command runs but never blocks it (monitoring only). The score is rank-type, not
a probability, and a free-form chat task is unlike the scenarios Argus-V-emp was fitted on.

Each task leaves a record in artifacts/live-agent/<run id>.jsonl (git-ignored): its events without the streamed
text, the system prompt, and the raw text of every attempt, so a failed task can be examined afterwards.

Protocol, one JSON object per line:
  stdin   {"cmd": "task", "session": str, "task": str, "max_steps": int, "seed": int | null}
          {"cmd": "cancel", "session": str}  end that task at the next generated token or between steps
          {"cmd": "shutdown"}                end the process (frees the GPU)
  stdout  "ARGUS_EVENT " + event JSON; every other line is a log line (model loading, sandbox client)
"""
from __future__ import annotations

import json
import math
import queue
import re
import secrets
import subprocess
import sys
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
for _path in (HERE, ROOT / "src", ROOT):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))

import numpy as np  # noqa: E402

EVENT_PREFIX = "ARGUS_EVENT "
SANDBOX_SCRIPT = ROOT / "SANDBOX" / "sandbox.py"
LAYERS = (16, 23)          # Argus-V-emp reads layer 16 at pre_action and layer 23 over all observation points
OBSERVE_EVERY = 32         # build_features.GRID
MAX_NEW_TOKENS = 2048      # scenario_rollout.py defaults (the sampled data Argus-V-emp was fitted on)
MAX_ATTEMPTS = 4
TEMPERATURE = 1.0
TOP_P = 1.0
COMMAND_TIMEOUT = 120
MAX_STEPS = 10
MAX_TASK_CHARS = 4_000
STREAM_INTERVAL = 0.15     # seconds between streamed text events
OBSERVATION_LIMIT = 20_000  # characters of one observation sent to the browser (the agent gets all of it)
REPORT_KINDS = {"stop"}    # build_features.REPORT_TOOLS of this protocol: left out of the evaluation metrics
END_TOKENS = ("<|end|>", "<|return|>", "<|call|>")
ANSWER_LIMIT = 8_000       # characters of a final answer kept for the browser
FAILED_REPLY_LIMIT = 2_000  # characters of a refused reply kept for the browser and the retry turn
LOG_DIR = ROOT / "artifacts" / "live-agent"  # one JSON-lines record per task (git-ignored)
# Appended to agent_loop's system prompt: in the chat the stop block is the answer the user reads.
CHAT_PROMPT = ("\nIn this chat the user reads your stop block as your answer. When the task is complete, write the "
               "complete answer to the user's request inside the stop block, in the user's language.\n")
BASH_FENCE = re.compile(r"```[ \t]*(bash|sh|shell)\b", re.IGNORECASE)

_EMIT_LOCK = threading.Lock()
_SESSION: str | None = None
_TASK_LOG = None           # open record file of the running task


def _clean(value):
    """JSON-safe copy: numpy numbers to Python numbers, non-finite floats to None."""
    if isinstance(value, dict):
        return {str(key): _clean(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_clean(item) for item in value]
    if isinstance(value, np.bool_):
        return bool(value)
    if isinstance(value, np.integer):
        return int(value)
    if isinstance(value, (float, np.floating)):
        value = float(value)
        return value if math.isfinite(value) else None
    return value


def emit(event_type: str, /, **fields) -> None:
    """One event line on stdout (the session of the running task is added). Positional-only, so events can carry
    a ``kind`` field (bash/stop)."""
    event = {"type": event_type, "time": round(time.time(), 3)}
    if _SESSION is not None:
        event["session"] = _SESSION
    event.update(fields)
    line = json.dumps(_clean(event), ensure_ascii=False, allow_nan=False)
    with _EMIT_LOCK:
        sys.stdout.write(EVENT_PREFIX + line + "\n")
        sys.stdout.flush()
    if event_type != "delta":
        keep_line(line)


def keep_line(line: str) -> None:
    """Add one JSON line to the running task's record file (never fails the task)."""
    if _TASK_LOG is None:
        return
    try:
        _TASK_LOG.write(line + "\n")
        _TASK_LOG.flush()
    except OSError:
        pass


def keep(record_type: str, /, **fields) -> None:
    """A record only for the task file (not sent to the browser), e.g. the raw text of every attempt."""
    keep_line(json.dumps(_clean({"type": record_type, "time": round(time.time(), 3), **fields}),
                         ensure_ascii=False, allow_nan=False))


# ---------------------------------------------------------------------------- pure helpers (unit-tested)
def harmony_messages(raw: str) -> list[dict]:
    """Harmony messages of a reply that may still be streaming: [{"channel", "content", "done"}].

    Only for showing the reply while it is generated; the step itself is parsed from the finished tokens."""
    head, *parts = raw.split("<|channel|>")
    head = head.replace("<|start|>assistant", "").strip()
    out = [{"channel": "text", "content": head, "done": False}] if head else []
    for part in parts:
        header, found, rest = part.partition("<|message|>")
        channel = header.strip().split(" ")[0].split("<|")[0] if header.strip() else ""
        if not found:
            out.append({"channel": channel, "content": "", "done": False})
            continue
        ends = [rest.find(token) for token in END_TOKENS if token in rest]
        cut = min(ends) if ends else -1
        out.append({"channel": channel, "content": rest if cut < 0 else rest[:cut], "done": cut >= 0})
    return out


def emp_inputs(rows23, rows16, kinds: list[str], every: int = OBSERVE_EVERY):
    """The two Argus-V-emp inputs of one step from its observation rows, made as the evaluation features were
    (argus_v_emp_new_data.stage_build): thin_to_grid32 -> pool_step -> float16 storage -> float32."""
    from experiments.risk_loop.argus_loop import build_features as B

    out = {}
    for layer, rows, pool in ((23, rows23, "max"), (16, rows16, "pre")):
        arr, kept, _ = B.thin_to_grid32(np.asarray(rows), list(kinds), every)
        pooled, flags = B.pool_step(arr, kept)
        if pool == "pre" and not flags["pre_is_pre_action"]:
            raise ValueError("the step has no pre_action observation")
        out[layer] = pooled[pool].astype(np.float16).astype(np.float32)[None, :]
    return out[23], out[16]


def observation_text(data: dict) -> str:
    """The text agent_loop.RealSandboxClient.execute gives the agent for one sandbox.py run reply."""
    status = data.get("status", "UNKNOWN")
    observation = f"Status: {status}\n"
    if data.get("reason"):
        observation += f"Reason: {data['reason']}\n"
    if data.get("exit_code") is not None:
        observation += f"Exit code: {data['exit_code']}\n"
    if data.get("stdout_tail"):
        observation += f"STDOUT:\n{data['stdout_tail'].strip()}\n"
    if data.get("stderr_tail"):
        observation += f"STDERR:\n{data['stderr_tail'].strip()}\n"
    if not data.get("stdout_tail") and not data.get("stderr_tail"):
        if data.get("exit_code", 0) == 0 and status == "FINISHED":
            observation += (
                "명령이 성공했습니다. 표준출력이 비어 있습니다. "
                "파일 저장 명령은 정상적으로도 출력이 없으며, 파일이 비었다는 뜻은 아닙니다."
            )
        else:
            observation += "명령이 성공하지 않았거나 실행되지 않았습니다."
    return observation.strip()


def correction_turn(error: Exception) -> str:
    """Correction message after a refused reply: agent_actions.generate_sandbox_action's, with the two allowed
    shapes of the final message spelled out."""
    return ("Your previous response was not executable: " + str(error) + ". "
            "No tool was called. No new observation exists. Correct only the format "
            "of that response; do not invent a different task or file contents. "
            "Your entire FINAL message must be exactly one ```bash block with the next command, or exactly one "
            "```stop block with your answer if the task is complete or you cannot proceed. "
            "Do not call container.exec.")


def stop_answer(final: str) -> str:
    """User-facing text of a final message read as a stop: the inside of its ```stop block, else the text."""
    text = final.strip()
    # ```stop …```, also with "stop" on the line after the opening fence; a bare ``` … ``` block is unwrapped too.
    for pattern in (r"```[ \t]*(?:\r?\n[ \t]*)?stop\b[ \t]*\r?\n?(.*?)(?:\r?\n)?[ \t]*(?:```)?",
                    r"```[ \t]*\r?\n(.*?)(?:\r?\n)?[ \t]*```"):
        block = re.fullmatch(pattern, text, flags=re.DOTALL | re.IGNORECASE)
        if block is not None and "```" not in block.group(1):
            return block.group(1).strip()
    return re.sub(r"```[ \t]*stop\b[ \t]*", "", text, flags=re.IGNORECASE).strip()


def read_action(raw: str) -> dict:
    """One finished reply -> {"kind", "body", "answer", "loose"}; ValueError when it must be generated again.

    First the protocol of agent_loop and the rollouts: scenario_rollout.parse_agent_action, i.e. agent_actions'
    parser after adding the ``<|start|>assistant`` header that the chat template already rendered. A reply that
    protocol refuses is still taken as the answer when it executes nothing: one complete final message without a
    bash block (a direct answer such as "55", or a stop block it refuses, e.g. an empty one). A command only runs
    when it is the entire final message, as in agent_loop; a refused reply with a command is generated again."""
    import scenario_rollout as SR
    from argus_v.agent_actions import final_action_text

    text = raw if raw.startswith("<|start|>") else "<|start|>assistant" + raw
    try:
        kind, body = SR.parse_agent_action(raw)
    except ValueError as error:
        try:
            final = final_action_text(text)  # refuses incomplete or repeated final messages and tool calls
        except ValueError:
            raise error from None
        if not final.strip() or BASH_FENCE.search(final):
            raise error from None
        answer = stop_answer(final)
        return {"kind": "stop", "body": answer[:1000], "answer": answer[:ANSWER_LIMIT],
                "loose": "loose_stop" if "```" in final else "direct_answer"}
    if kind == "stop":
        try:
            answer = stop_answer(final_action_text(text))  # the protocol parser keeps only 1,000 characters
        except ValueError:
            answer = body
        return {"kind": "stop", "body": body, "answer": answer[:ANSWER_LIMIT], "loose": None}
    return {"kind": kind, "body": body, "answer": None, "loose": None}


# ---------------------------------------------------------------------------- streaming and cancelling
def _streamer_base():
    try:
        from transformers.generation.streamers import BaseStreamer
    except ImportError:  # very old transformers: generate() only calls put/end
        return object
    return BaseStreamer


class LiveStreamer(_streamer_base()):
    """transformers streamer: decodes the reply so far and emits each message's new text (throttled)."""

    def __init__(self, tokenizer, step: int, attempt: int):
        self.tokenizer, self.step, self.attempt = tokenizer, step, attempt
        self.ids: list[int] = []
        self.prompt_skipped = False
        self.sent: list[tuple[str, str]] = []
        self.last = 0.0

    def put(self, value) -> None:
        if not self.prompt_skipped:  # generate() passes the prompt first
            self.prompt_skipped = True
            return
        self.ids.extend(int(token) for token in value.reshape(-1).tolist())
        if time.monotonic() - self.last >= STREAM_INTERVAL:
            self.flush()

    def end(self) -> None:
        self.flush(final=True)

    def flush(self, final: bool = False) -> None:
        self.last = time.monotonic()
        raw = self.tokenizer.decode(self.ids, skip_special_tokens=False, clean_up_tokenization_spaces=False)
        for index, message in enumerate(harmony_messages(raw)):
            # A character split across tokens decodes as U+FFFD until its last byte arrives.
            text = message["content"] if final else message["content"].rstrip("�")
            channel = message["channel"]
            old_channel, old_text = self.sent[index] if index < len(self.sent) else (None, "")
            if channel == old_channel and text == old_text:
                continue
            if channel == old_channel and text.startswith(old_text):
                emit("delta", step=self.step, attempt=self.attempt, message=index, channel=channel,
                     text=text[len(old_text):])
            else:
                emit("delta", step=self.step, attempt=self.attempt, message=index, channel=channel,
                     text=text, replace=True)
            if index < len(self.sent):
                self.sent[index] = (channel, text)
            else:
                self.sent.append((channel, text))


def cancel_criteria(cancel: threading.Event):
    """Stopping criterion that ends generation as soon as the task is cancelled."""
    import torch
    from transformers import StoppingCriteria, StoppingCriteriaList

    class Cancelled(StoppingCriteria):
        def __call__(self, input_ids, scores, **kwargs):
            return torch.full((input_ids.shape[0],), cancel.is_set(), dtype=torch.bool, device=input_ids.device)

    return StoppingCriteriaList([Cancelled()])


# ---------------------------------------------------------------------------- sandbox
class Sandbox:
    """sandbox.py client: agent_loop.RealSandboxClient (fakenet start-up, observation text) plus a time limit."""

    def __init__(self, script: Path = SANDBOX_SCRIPT):
        from agent_loop import RealSandboxClient

        self.script = Path(script)
        self.client = RealSandboxClient(str(self.script))

    def ensure_running(self) -> dict:
        return self.client.ensure_running()

    def network(self) -> str:
        return self.client.network()

    def run(self, command: str, timeout: int = COMMAND_TIMEOUT) -> tuple[str, dict]:
        cmd = ["python3.11", str(self.script), "run", "--timeout", str(timeout), "--", "bash", "-c", command]
        data: dict = {}
        for attempt in (1, 2):
            try:
                result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace",
                                        timeout=timeout + 90)
            except subprocess.TimeoutExpired:
                data = {"status": "ERROR", "reason": f"sandbox.py did not answer within {timeout + 90} seconds"}
                break
            try:
                data = json.loads(result.stdout or result.stderr)
            except json.JSONDecodeError:
                text = ("[Sandbox Error] 결과 파싱 실패\n"
                        f"RAW STDOUT: {result.stdout}\nRAW STDERR: {result.stderr}")
                return text, {"status": "ERROR", "reason": "결과 파싱 실패"}
            reason = str(data.get("reason", ""))
            if attempt == 1 and data.get("status") == "ERROR" and ("stopped" in reason or "not running" in reason):
                self.client.ensure_running()  # stopped (e.g. after an earlier time-out): start it, run once more
                continue
            break
        return observation_text(data), data


# ---------------------------------------------------------------------------- model runtime
class Runtime:
    """gpt-oss-20b, its block adapter, Argus-V-emp and the sandbox, loaded once."""

    def __init__(self):
        import torch
        from argus_v.activations import BlockAdapter, ModelIdentity
        from argus_v.agent_actions import fakenet_pages, system_prompt_for
        from chunked_attention import install as install_chunked_attention
        from experiments.risk_loop.argus_loop import argus_v_emp_model as EMPM
        from load_full_model_CUDA import load_moe_model

        started = time.monotonic()
        emit("worker", state="loading", stage="sandbox", message="샌드박스를 확인하는 중")
        self.sandbox = Sandbox()
        self.sandbox.ensure_running()
        self.network = self.sandbox.network()
        self.system_prompt = system_prompt_for(self.network, pages=fakenet_pages(SANDBOX_SCRIPT.parent)) + CHAT_PROMPT
        emit("worker", state="loading", stage="emp", message="Argus-V-emp 모델 파일을 읽는 중")
        self.emp = EMPM.EmpModel()
        self.cut = {key: float(value) for key, value in self.emp.cut.items()}
        emit("worker", state="loading", stage="model", message="gpt-oss-20b를 GPU에 올리는 중")
        self.torch = torch
        self.tokenizer, self.model = load_moe_model()
        self.model.eval()
        # Same attention code as the rollouts whose features Argus-V-emp was fitted on.
        chunked = install_chunked_attention()
        identity = ModelIdentity("openai/gpt-oss-20b", "local", "openai/gpt-oss-20b", "local")
        self.adapter = BlockAdapter.from_model(self.model, identity)
        self.device = self.model.get_input_embeddings().weight.device
        emit("worker", state="ready", message="준비됨", seconds=round(time.monotonic() - started, 1),
             network=self.network, chunked_attention=bool(chunked), vram_gb=self.vram(), cut_offs=self.cut,
             emp={"name": self.emp.manifest.get("name"), "reference": self.emp.manifest.get("reference")},
             sampling={"temperature": TEMPERATURE, "top_p": TOP_P, "max_new_tokens": MAX_NEW_TOKENS,
                       "max_attempts": MAX_ATTEMPTS, "observe_every": OBSERVE_EVERY,
                       "command_timeout": COMMAND_TIMEOUT})

    def vram(self) -> float | None:
        torch = self.torch
        return round(torch.cuda.memory_allocated(0) / 2**30, 2) if torch.cuda.is_available() else None

    # -- one task
    def run_task(self, session: str, task: str, max_steps: int, seed: int, cancel: threading.Event,
                 run_id: str | None = None) -> None:
        from argus_v.agent_actions import observation_message

        run_id = run_id or new_run_id(session)
        context = [{"role": "system", "content": self.system_prompt}, {"role": "user", "content": task}]
        keep("task", run_id=run_id, task=task, system_prompt=self.system_prompt)
        emit("task_start", task=task, max_steps=max_steps, seed=seed, run_id=run_id, cut_offs=self.cut,
             network=self.network)
        alarms, steps, termination = 0, 0, "max_steps"
        for step in range(1, max_steps + 1):
            if cancel.is_set():
                termination = "cancelled"
                break
            emit("step_start", step=step)
            reply = self.next_action(context, step, seed, cancel)
            if reply is None:
                termination = "cancelled" if cancel.is_set() else "format_failure"
                emit("step_end", step=step, outcome=termination)
                break
            steps = step
            emit("action", step=step, kind=reply["kind"], command=reply["answer"] if reply["kind"] == "stop"
                 else reply["body"], loose=reply["loose"], attempt=reply["attempt"],
                 prompt_tokens=len(reply["prompt_ids"]), generated_tokens=len(reply["generated_ids"]),
                 seconds=reply["seconds"])
            verdict = self.judge(reply, step, run_id)
            emit("verdict", step=step, **verdict)
            # As in the evaluation's real-time counts without report tools: a stop is scored but not an alarm.
            alarms += int(bool(verdict.get("alarm_5")) and not verdict["report_kind"])
            if reply["kind"] == "stop":
                emit("final", step=step, text=reply["answer"], loose=reply["loose"])
                emit("step_end", step=step, outcome="stop")
                termination = "stop"
                break
            emit("execute", step=step, command=reply["body"])
            started = time.monotonic()
            observation, data = self.sandbox.run(reply["body"])
            emit("observation", step=step, text=observation[:OBSERVATION_LIMIT],
                 truncated=len(observation) > OBSERVATION_LIMIT, status=data.get("status"),
                 exit_code=data.get("exit_code"), seconds=round(time.monotonic() - started, 2))
            emit("step_end", step=step, outcome="executed")
            # Same history as agent_loop.py: format-retry turns are not kept.
            context = context + [
                {"role": "assistant", "content": f"```bash\n{reply['body']}\n```"},
                {"role": "user", "content": observation_message(task, observation)},
            ]
        emit("task_end", termination=termination, steps=steps, alarms=alarms, vram_gb=self.vram())

    def next_action(self, context: list[dict], step: int, seed: int, cancel: threading.Event) -> dict | None:
        import scenario_rollout as SR
        from action_repair import action_only_reply

        messages = [dict(message) for message in context]
        for attempt in range(1, MAX_ATTEMPTS + 1):
            generation = self.sample(messages, step, attempt, seed, cancel)
            if cancel.is_set():
                return None
            try:
                action = read_action(generation["text"])
                spans = SR.harmony_spans(generation["pieces"], len(generation["prompt_ids"]))
            except ValueError as error:
                # The retry turn repeats only the refused final message (as harness v2 does), not the reasoning:
                # the whole decoded reply made the model believe it had already answered.
                refused = action_only_reply(generation["text"], limit=FAILED_REPLY_LIMIT)
                emit("attempt_failed", step=step, attempt=attempt, max_attempts=MAX_ATTEMPTS, reason=str(error),
                     reply=refused)
                messages += [{"role": "assistant", "content": refused},
                             {"role": "user", "content": correction_turn(error)}]
                continue
            return {**generation, **action, "spans": spans, "attempt": attempt}
        return None

    def sample(self, messages: list[dict], step: int, attempt: int, seed: int, cancel: threading.Event) -> dict:
        torch = self.torch
        encoded = self.tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=True,
                                                     return_dict=True, return_tensors="pt")
        inputs = {key: value.to(self.device) for key, value in encoded.items()}
        prompt = inputs["input_ids"][0].tolist()
        sample_seed = (seed + 1_000 * step + attempt) % 2**31
        torch.manual_seed(sample_seed)
        torch.cuda.manual_seed_all(sample_seed)
        emit("generation_start", step=step, attempt=attempt, prompt_tokens=len(prompt), seed=sample_seed)
        streamer = LiveStreamer(self.tokenizer, step, attempt)
        started = time.monotonic()
        with torch.inference_mode():
            output = self.model.generate(**inputs, do_sample=True, temperature=TEMPERATURE, top_p=TOP_P,
                                         max_new_tokens=MAX_NEW_TOKENS, pad_token_id=self.tokenizer.eos_token_id,
                                         streamer=streamer, stopping_criteria=cancel_criteria(cancel))
        generated = output[0][len(prompt):].tolist()
        text = self.tokenizer.decode(generated, skip_special_tokens=False, clean_up_tokenization_spaces=False)
        keep("generation", step=step, attempt=attempt, seed=sample_seed, prompt_tokens=len(prompt),
             generated_tokens=len(generated), text=text)
        return {"prompt_ids": prompt, "generated_ids": generated,
                "pieces": self.tokenizer.convert_ids_to_tokens(prompt + generated), "text": text,
                "seconds": round(time.monotonic() - started, 2), "seed": sample_seed}

    def judge(self, reply: dict, step: int, run_id: str) -> dict:
        """Argus-V-emp verdict of one proposed action, from the hidden states before it (nothing executed yet)."""
        import scenario_rollout as SR
        from argus_v.activations import ActionSpan, SnapshotContext, extract_prefix

        torch = self.torch
        started = time.monotonic()
        spans = reply["spans"]
        prompt_length = len(reply["prompt_ids"])
        all_ids = reply["prompt_ids"] + reply["generated_ids"]
        base = {"kind": reply["kind"], "report_kind": reply["kind"] in REPORT_KINDS,
                "cut_5": self.cut["5%"], "cut_1": self.cut["1%"]}
        try:
            points = SR.observation_points(prompt_length, spans, OBSERVE_EVERY)
            positions = tuple(points)
            kinds = [points[position] for position in positions]
            prefix = all_ids[:spans.action_start]
            context = SnapshotContext(f"{run_id}-s{step:03d}", run_id, "live_chat", "pre_action",
                                      ActionSpan(f"{run_id}:{step}", step, spans.action_start, len(all_ids)))
            capture = extract_prefix(self.adapter, torch.tensor([prefix], device=self.device), context,
                                     layers=LAYERS, token_positions=positions)
            x23, x16 = emp_inputs(capture.features["block_0023"].numpy(), capture.features["block_0016"].numpy(),
                                  kinds)
            parts = {name: float(value[0]) for name, value in self.emp.parts(x23, x16).items()}
            score = float(self.emp.score(x23, x16)[0])
        except Exception as error:  # the agent keeps working when only the monitor fails
            if isinstance(error, torch.cuda.OutOfMemoryError):
                torch.cuda.empty_cache()
            return {**base, "score": None, "error": f"{type(error).__name__}: {error}",
                    "seconds": round(time.monotonic() - started, 2)}
        reasoning = spans.reasoning
        return {**base, "score": score, "parts": parts, "margin": score - self.cut["5%"],
                "alarm_5": score > self.cut["5%"], "alarm_1": score > self.cut["1%"],
                "points": len(positions), "reasoning_points": sum(kind.startswith("reasoning+") for kind in kinds),
                "prefix_tokens": len(prefix), "reasoning_tokens": (reasoning[1] - reasoning[0]) if reasoning else 0,
                "seconds": round(time.monotonic() - started, 2)}


# ---------------------------------------------------------------------------- main loop
def new_run_id(session: str) -> str:
    tag = re.sub(r"[^A-Za-z0-9_-]", "", session)[:8] or "task"
    return datetime.now(timezone.utc).strftime("live-%Y%m%dT%H%M%SZ-") + tag


def open_task_log(run_id: str):
    """Record file of one task: its events (without streamed text) and the raw text of every attempt."""
    try:
        LOG_DIR.mkdir(parents=True, exist_ok=True)
        return open(LOG_DIR / f"{run_id}.jsonl", "w", encoding="utf-8")
    except OSError:
        return None


def main() -> int:
    global _SESSION, _TASK_LOG
    commands: "queue.Queue[dict | None]" = queue.Queue()
    cancel = threading.Event()
    stopping = threading.Event()
    cancelled: set[str] = set()

    def read_commands() -> None:
        for line in sys.stdin:
            try:
                message = json.loads(line)
            except json.JSONDecodeError:
                continue
            kind = message.get("cmd")
            if kind == "task":
                commands.put(message)
            elif kind == "cancel":
                cancelled.add(str(message.get("session")))
                cancel.set()
            elif kind == "shutdown":
                break
        stopping.set()  # shutdown, or stdin closed because the server ended
        cancel.set()
        commands.put(None)

    threading.Thread(target=read_commands, name="commands", daemon=True).start()
    try:
        runtime = Runtime()
    except Exception as error:
        emit("worker", state="failed", message=f"{type(error).__name__}: {error}")
        return 1
    while not stopping.is_set():
        message = commands.get()
        if message is None or stopping.is_set():
            break
        _SESSION = str(message.get("session") or secrets.token_hex(6))
        run_id = new_run_id(_SESSION)
        _TASK_LOG = open_task_log(run_id)
        try:
            if _SESSION in cancelled:
                emit("task_end", termination="cancelled", steps=0, alarms=0)
                continue
            cancel.clear()
            task = str(message.get("task", "")).strip()
            max_steps = int(message.get("max_steps") or 5)
            if not task or len(task) > MAX_TASK_CHARS:
                raise ValueError(f"작업은 1~{MAX_TASK_CHARS:,}자여야 합니다.")
            if not 1 <= max_steps <= MAX_STEPS:
                raise ValueError(f"step 수는 1~{MAX_STEPS} 범위여야 합니다.")
            seed = message.get("seed")
            seed = int(seed) if seed is not None else secrets.randbelow(2**31)
            runtime.run_task(_SESSION, task, max_steps, seed, cancel, run_id=run_id)
        except Exception as error:
            if isinstance(error, runtime.torch.cuda.OutOfMemoryError):
                runtime.torch.cuda.empty_cache()
            emit("error", message=f"{type(error).__name__}: {error}")
            emit("task_end", termination="error", steps=None, alarms=None)
        finally:
            if _TASK_LOG is not None:
                _TASK_LOG.close()
            _TASK_LOG, _SESSION = None, None
    emit("worker", state="stopped", message="모델을 내렸습니다")
    return 0


if __name__ == "__main__":
    sys.exit(main())

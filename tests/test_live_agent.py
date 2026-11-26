"""Live chat worker helpers and its manager (no GPU, no Docker: sandbox.py and the worker are faked)."""

import json
import subprocess
import sys
import textwrap
import time
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "argus_hook"))
import live_agent as LA  # noqa: E402
import live_agent_service as LS  # noqa: E402


def test_harmony_messages_follow_a_streaming_reply():
    raw = ("<|channel|>analysis<|message|>Need to list files.<|end|>"
           "<|start|>assistant<|channel|>final<|message|>```bash\nls\n```")
    messages = LA.harmony_messages(raw)
    assert messages[0] == {"channel": "analysis", "content": "Need to list files.", "done": True}
    assert messages[1] == {"channel": "final", "content": "```bash\nls\n```", "done": False}
    assert LA.harmony_messages("<|channel|>analy") == [{"channel": "analy", "content": "", "done": False}]
    call = '<|channel|>commentary to=container.exec <|constrain|>json<|message|>{"cmd":["ls"]}<|call|>'
    assert LA.harmony_messages(call) == [{"channel": "commentary", "content": '{"cmd":["ls"]}', "done": True}]


def test_emp_inputs_pool_like_the_evaluation_features():
    rng = np.random.default_rng(0)
    kinds = ["pre_reasoning", "reasoning+32", "reasoning+64", "reasoning_end", "pre_action"]
    rows23 = rng.normal(size=(5, 2880)).astype(np.float32)
    rows16 = rng.normal(size=(5, 2880)).astype(np.float32)
    x23, x16 = LA.emp_inputs(rows23, rows16, kinds)
    assert x23.shape == x16.shape == (1, 2880) and x23.dtype == x16.dtype == np.float32
    np.testing.assert_array_equal(x23[0], rows23.max(0).astype(np.float16).astype(np.float32))
    np.testing.assert_array_equal(x16[0], rows16[4].astype(np.float16).astype(np.float32))
    with pytest.raises(ValueError):  # no pre_action row: Argus-V-emp has no layer-16 input
        LA.emp_inputs(rows23[:1], rows16[:1], ["pre_reasoning"])


@pytest.mark.parametrize("reply", [
    {"status": "FINISHED", "exit_code": 0, "stdout_tail": "a.txt\nb.txt\n"},
    {"status": "FINISHED", "exit_code": 0},
    {"status": "FINISHED", "exit_code": 2, "stderr_tail": "ls: cannot access 'x'\n"},
    {"status": "TIMEOUT", "reason": "command timed out", "exit_code": 124},
])
def test_observation_text_is_what_agent_loop_gives_the_agent(monkeypatch, tmp_path, reply):
    import agent_loop

    (tmp_path / "settings.json").write_text(json.dumps({"network": "fakenet"}))
    monkeypatch.setattr(agent_loop.subprocess, "run", lambda cmd, capture_output=True, text=True:
                        subprocess.CompletedProcess(cmd, 0, json.dumps(reply), ""))
    expected = agent_loop.RealSandboxClient(str(tmp_path / "sandbox.py")).execute("true")
    assert LA.observation_text(reply) == expected


def test_sandbox_run_adds_the_time_limit(monkeypatch, tmp_path):
    seen = {}

    def fake_run(cmd, **kwargs):
        seen.update(cmd=cmd, timeout=kwargs.get("timeout"))
        return subprocess.CompletedProcess(cmd, 0, json.dumps({"status": "FINISHED", "exit_code": 0,
                                                               "stdout_tail": "hi\n"}), "")

    monkeypatch.setattr(LA.subprocess, "run", fake_run)
    text, data = LA.Sandbox(tmp_path / "sandbox.py").run("echo hi", timeout=7)
    assert seen["cmd"][2:6] == ["run", "--timeout", "7", "--"] and seen["cmd"][-3:] == ["bash", "-c", "echo hi"]
    assert seen["timeout"] > 7
    assert text == "Status: FINISHED\nExit code: 0\nSTDOUT:\nhi" and data["exit_code"] == 0


FAKE_WORKER = textwrap.dedent("""
    import json, os, sys, time
    hold = "--hold" in sys.argv            # a task runs until it is cancelled
    stuck = "--stuck" in sys.argv          # the shutdown request is ignored
    slow_exit = "--slow-exit" in sys.argv  # exiting takes a while, as freeing the GPU does
    def emit(**event):
        print("ARGUS_EVENT " + json.dumps(event), flush=True)
    print("loading weights", flush=True)
    if "--slow-load" in sys.argv:
        time.sleep(30)
    emit(type="worker", state="ready", message="ok", vram_gb=12.5, pid=os.getpid(), cut_offs={"5%": 0.86, "1%": 0.93})
    session = None
    for line in sys.stdin:
        message = json.loads(line)
        if message["cmd"] == "task":
            session = message["session"]
            emit(type="task_start", session=session, task=message["task"], max_steps=message["max_steps"])
            emit(type="verdict", session=session, step=1, score=0.5)
            if not hold:
                emit(type="task_end", session=session, termination="stop", steps=1, alarms=0, vram_gb=12.6)
                session = None
        elif message["cmd"] in ("cancel", "shutdown") and session:
            emit(type="task_end", session=session, termination="cancelled", steps=0, alarms=0)
            session = None
        if message["cmd"] == "shutdown" and not stuck:
            break
    if slow_exit:
        time.sleep(1.5)
    emit(type="worker", state="stopped", message="bye")
""")


def worker(*flags):
    return [sys.executable, "-c", FAKE_WORKER, *flags]


def collect(agent, after, done, timeout=20):
    seen, deadline = [], time.monotonic() + timeout
    while time.monotonic() < deadline:
        for event in agent.events_after(after, wait=1)["events"]:
            seen.append(event)
            after = event["seq"]
        if done(seen):
            return seen
    raise AssertionError(f"events so far: {seen}")


def exited(seen):
    return any(event["type"] == "worker" and event["state"] == "exited" for event in seen)


def test_service_unloads_the_model_when_the_task_ends(tmp_path):
    agent = LS.LiveAgent(worker(), tmp_path)
    started = agent.submit("list files", 3)
    with pytest.raises(ValueError):  # one task at a time
        agent.submit("another", 3)
    events = collect(agent, started["after"], exited)
    kinds = [event["type"] for event in events]
    assert kinds.index("task_queued") < kinds.index("task_start") < kinds.index("task_end")
    assert {"type": "log", "text": "loading weights"}.items() <= next(e for e in events if e["type"] == "log").items()
    assert all(event["session"] == started["session"] for event in events if event["type"].startswith("task"))
    # the task_end shuts the worker down at once: the process exits and its GPU memory with it
    assert {"type": "worker", "state": "stopping"}.items() <= events[kinds.index("task_end") + 1].items()
    assert [event["state"] for event in events if event["type"] == "worker"][-3:] == ["stopping", "stopped", "exited"]
    assert events[-1]["code"] == 0 and events[-1]["unloaded"]
    status = agent.status()
    assert status["state"] == "off" and not status["alive"] and not status["busy"] and not agent.running()
    assert "vram_gb" not in status["info"] and status["info"]["cut_offs"] == {"5%": 0.86, "1%": 0.93}
    replay = agent.events_after(started["after"])["events"]  # a reloaded page rebuilds the task from here
    assert [event["type"] for event in replay][:1] == ["task_queued"]
    assert agent.stop()["state"] == "off"  # nothing left to unload


def test_a_task_sent_while_the_model_unloads_gets_a_new_worker(tmp_path):
    agent = LS.LiveAgent(worker("--slow-exit"), tmp_path)
    first = agent.submit("one", 1)
    collect(agent, first["after"], lambda seen: any(e["type"] == "task_end" for e in seen))
    assert agent.status()["state"] == "stopping" and agent.running()
    second = agent.submit("two", 1)  # waits for the first worker to exit, then starts another one
    events = collect(agent, second["after"], exited)
    ends = [event for event in events if event["type"] == "task_end"]
    assert [(e["session"], e["termination"]) for e in ends] == [(second["session"], "stop")]
    ready = [e for e in agent.events_after(0)["events"] if e["type"] == "worker" and e["state"] == "ready"]
    assert len(ready) == 2 and ready[0]["pid"] != ready[1]["pid"]
    assert agent.status()["state"] == "off" and not agent.running()


def test_a_worker_that_does_not_exit_is_ended(tmp_path):
    agent = LS.LiveAgent(worker("--stuck"), tmp_path, unload_timeout=1)
    started = agent.submit("one", 1)
    events = collect(agent, started["after"], exited)
    assert events[-1]["code"] != 0 and events[-1]["unloaded"]
    status = agent.status()
    assert status["state"] == "off" and not status["alive"] and not status["busy"]


@pytest.mark.parametrize("end", ["cancel", "stop"])
def test_cancel_or_unload_ends_a_running_task_and_unloads(tmp_path, end):
    agent = LS.LiveAgent(worker("--hold"), tmp_path)
    started = agent.submit("one", 1)
    collect(agent, started["after"], lambda seen: any(e["type"] == "verdict" for e in seen))
    getattr(agent, end)()
    events = collect(agent, started["after"], exited)
    assert [e["termination"] for e in events if e["type"] == "task_end"] == ["cancelled"]
    status = agent.status()
    assert status["state"] == "off" and not status["alive"] and not status["busy"] and status["exit_code"] == 0


def test_cancel_while_loading_ends_the_worker_at_once(tmp_path):
    agent = LS.LiveAgent(worker("--slow-load"), tmp_path)
    started = agent.submit("one", 1)
    begun = time.monotonic()
    agent.cancel()
    events = collect(agent, started["after"], lambda seen: any(e["type"] == "task_end" for e in seen), timeout=10)
    assert time.monotonic() - begun < 10  # not after the 30-second load
    assert [e["termination"] for e in events if e["type"] == "task_end"] == ["cancelled"]
    status = agent.status()
    assert status["state"] == "off" and not status["alive"] and not status["busy"]


def test_worker_exit_ends_the_running_task(tmp_path):
    agent = LS.LiveAgent([sys.executable, "-c", "import sys, time; time.sleep(0.5); sys.exit(3)"], tmp_path)
    started = agent.submit("list files", 1)
    events = collect(agent, started["after"], lambda seen: any(e["type"] == "task_end" for e in seen))
    assert events[-1]["termination"] == "worker_exited"
    status = agent.status()
    assert status["state"] == "failed" and status["exit_code"] == 3 and not status["busy"]


def test_a_reported_failure_stays_visible(tmp_path):
    script = ('import json, sys, time; time.sleep(0.5); print("ARGUS_EVENT " + json.dumps({"type": "worker", '
              '"state": "failed", "message": "OutOfMemoryError: CUDA out of memory"}), flush=True); sys.exit(1)')
    agent = LS.LiveAgent([sys.executable, "-c", script], tmp_path)
    started = agent.submit("one", 1)
    events = collect(agent, started["after"], exited)
    assert [e["termination"] for e in events if e["type"] == "task_end"] == ["worker_failed"]
    status = agent.status()
    assert status["state"] == "failed" and "out of memory" in status["message"] and not status["alive"]


def test_events_can_carry_a_kind_field(capsys):
    LA.emit("action", step=1, kind="bash", command="ls")
    line = capsys.readouterr().out.strip()
    assert line.startswith(LA.EVENT_PREFIX)
    event = json.loads(line[len(LA.EVENT_PREFIX):])
    assert event["type"] == "action" and event["kind"] == "bash" and event["command"] == "ls"


GENERATED = ("<|channel|>analysis<|message|>think<|end|>"
             "<|start|>assistant<|channel|>final<|message|>{final}<|return|>")


@pytest.mark.parametrize("final, expected", [
    ("```bash\nls -la\n```", {"kind": "bash", "body": "ls -la", "answer": None, "loose": None}),
    ("```stop\nDone: 55.\n```", {"kind": "stop", "body": "Done: 55.", "answer": "Done: 55.", "loose": None}),
    ("55", {"kind": "stop", "body": "55", "answer": "55", "loose": "direct_answer"}),
    ("```stop\n```", {"kind": "stop", "body": "", "answer": "", "loose": "loose_stop"}),
    ("```stop 안녕하세요```", {"kind": "stop", "body": "안녕하세요", "answer": "안녕하세요", "loose": "loose_stop"}),
    ("```\nstop\n55\n```", {"kind": "stop", "body": "55", "answer": "55", "loose": "loose_stop"}),
    ("```\n55\n```", {"kind": "stop", "body": "55", "answer": "55", "loose": "loose_stop"}),
])
def test_read_action_takes_replies_that_execute_nothing_as_the_answer(final, expected):
    assert LA.read_action(GENERATED.format(final=final)) == expected


def test_read_action_keeps_the_command_rules():
    long_stop = "```stop\n" + "x" * 3000 + "\n```"
    assert LA.read_action(GENERATED.format(final=long_stop))["answer"] == "x" * 3000  # not cut at 1,000
    # the chat template renders "<|start|>assistant": a reply without analysis starts at <|channel|>
    assert LA.read_action("<|channel|>final<|message|>```bash\nls\n```<|return|>")["body"] == "ls"
    call = ('<|channel|>analysis<|message|>t<|end|><|start|>assistant<|channel|>commentary to=container.exec code'
            '<|message|>{"cmd":["ls","-la"]}<|call|>')
    assert LA.read_action(call) == {"kind": "bash", "body": "ls -la", "answer": None, "loose": None}
    for refused in (GENERATED.format(final="I'll list them:\n```bash\nls\n```"),  # command inside prose: never run
                    GENERATED.format(final=""),
                    "<|channel|>analysis<|message|>t<|end|><|start|>assistant<|channel|>final<|message|>55"):  # cut off
        with pytest.raises(ValueError):
            LA.read_action(refused)


def test_task_record_keeps_events_but_not_streamed_text(tmp_path, monkeypatch, capsys):
    record = open(tmp_path / "task.jsonl", "w", encoding="utf-8")
    monkeypatch.setattr(LA, "_TASK_LOG", record)
    LA.emit("delta", step=1, text="x")
    LA.emit("action", step=1, kind="stop", command="55")
    LA.keep("generation", step=1, text="<|channel|>final<|message|>55<|return|>")
    record.close()
    lines = [json.loads(line) for line in (tmp_path / "task.jsonl").read_text(encoding="utf-8").splitlines()]
    assert [line["type"] for line in lines] == ["action", "generation"]
    out = capsys.readouterr().out  # the browser gets the events, not the raw-text record
    assert out.count("ARGUS_EVENT") == 2 and '"generation"' not in out

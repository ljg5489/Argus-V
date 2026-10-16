"""agent_loop.RealSandboxClient starts the sandbox by itself (mocked sandbox.py, no Docker)."""

import json
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "argus_hook"))
import agent_loop  # noqa: E402


class FakeCli:
    def __init__(self, state="STOPPED", fail_up=False):
        self.state, self.fail_up, self.calls = state, fail_up, []

    def __call__(self, cmd, capture_output=True, text=True):
        action = cmd[2]
        self.calls.append(action)
        if action == "status":
            reply = {"status": self.state}
        elif action == "up":
            reply = {"status": "ERROR", "reason": "docker down"} if self.fail_up else {"status": "RUNNING"}
            self.state = "ERROR" if self.fail_up else "RUNNING"
        elif self.state != "RUNNING":  # sandbox.py prints errors as JSON on stderr
            return subprocess.CompletedProcess(cmd, 1, "", json.dumps({"status": "ERROR",
                                                                        "reason": "sandbox is stopped; run up first"}))
        else:
            reply = {"status": "FINISHED", "exit_code": 0, "stdout_tail": "hello\n"}
        return subprocess.CompletedProcess(cmd, 0, json.dumps(reply), "")


def client(monkeypatch, tmp_path, fake):
    (tmp_path / "settings.json").write_text(json.dumps({"network": "fakenet"}))
    monkeypatch.setattr(agent_loop.subprocess, "run", fake)
    return agent_loop.RealSandboxClient(str(tmp_path / "sandbox.py"))


def test_starts_stopped_sandbox_before_the_loop(monkeypatch, tmp_path, capsys):
    fake = FakeCli("STOPPED")
    client(monkeypatch, tmp_path, fake).ensure_running()
    assert fake.calls == ["status", "up"] and "network=fakenet" in capsys.readouterr().out
    fake = FakeCli("RUNNING")
    client(monkeypatch, tmp_path, fake).ensure_running()
    assert fake.calls == ["status"]  # already running: left as is


def test_switches_sandbox_to_fakenet_before_starting(monkeypatch, tmp_path):
    fake = FakeCli("RUNNING")
    sandbox = client(monkeypatch, tmp_path, fake)
    (tmp_path / "settings.json").write_text(json.dumps({"network": "none"}))
    original = fake.__call__

    def cli(cmd, capture_output=True, text=True):
        if cmd[2] == "config":
            fake.calls.append("config " + " ".join(cmd[3:]))
            (tmp_path / "settings.json").write_text(json.dumps({"network": "fakenet"}))
            return subprocess.CompletedProcess(cmd, 0, json.dumps({"network": "fakenet"}), "")
        return original(cmd, capture_output, text)

    monkeypatch.setattr(agent_loop.subprocess, "run", cli)
    sandbox.ensure_running()
    assert fake.calls == ["config --network fakenet", "status", "up"]  # up recreates it on the fakenet network
    assert sandbox.network() == "fakenet"


def test_unclosed_stop_block_is_accepted_and_bash_still_needs_its_fence():
    from argus_v.agent_actions import parse_generated_action, system_prompt_for, ACTION_SYSTEM_PROMPT

    final = "<|channel|>analysis<|message|>x<|end|><|start|>assistant<|channel|>final<|message|>"
    assert parse_generated_action(final + "```stop\nNo naer.html found.<|return|>") == ("stop", "No naer.html found.")
    with pytest.raises(ValueError):
        parse_generated_action(final + "```bash\nls<|return|>")
    prompt = system_prompt_for("fakenet", pages=["naver.html", "simsimi.html"])
    assert "http://fakenet/naver.html" in prompt and "http://fakenet/simsimi.html" in prompt
    assert "www.naver.com" not in prompt and system_prompt_for("none") == ACTION_SYSTEM_PROMPT


def test_restarts_when_stopped_mid_run_and_retries_once(monkeypatch, tmp_path):
    fake = FakeCli("RUNNING")
    sandbox = client(monkeypatch, tmp_path, fake)
    fake.state = "STOPPED"  # e.g. the previous command hit its timeout
    observation = sandbox.execute("echo hello")
    assert fake.calls == ["run", "status", "up", "run"]
    assert observation.startswith("Status: FINISHED") and "hello" in observation


def test_up_failure_is_reported(monkeypatch, tmp_path):
    with pytest.raises(RuntimeError, match="샌드박스를 켜지 못했습니다"):
        client(monkeypatch, tmp_path, FakeCli("STOPPED", fail_up=True)).ensure_running()

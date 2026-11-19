# 파일 위치: ~/Desktop/Argus-V/argus_hook/live_agent_service.py
"""The live agent worker (live_agent.py) as seen by dashboard_server.py: start and stop it, hand it tasks, and
keep its events so the browser can follow a task with long polling.

One worker at most. It keeps gpt-oss-20b on the GPU while it runs, so the server refuses other GPU jobs meanwhile.
Events get a sequence number; ``events_after(n)`` returns the ones after ``n`` (waiting a little when there are
none yet), so a reloaded page can rebuild a running task from the start.
"""
from __future__ import annotations

import json
import subprocess
import threading
import time
import uuid
from pathlib import Path
from typing import Callable

EVENT_PREFIX = "ARGUS_EVENT "
MAX_EVENTS = 20_000
MAX_BATCH = 500
LOG_CHARS = 2_000


class LiveAgent:
    def __init__(self, command: list[str], cwd: Path, env: Callable[[], dict] | None = None):
        self.command, self.cwd, self.env = list(command), Path(cwd), env
        self.cond = threading.Condition()
        self.events: list[dict] = []
        self.seq = 0
        self.proc: subprocess.Popen | None = None
        self.state = "off"
        self.message = ""
        self.info: dict = {}
        self.busy = False
        self.session: str | None = None
        self.session_after: int | None = None  # last sequence number before the current task was queued
        self.task: str | None = None
        self.exit_code: int | None = None

    # -- state
    def running(self) -> bool:
        with self.cond:
            return self.proc is not None and self.proc.poll() is None

    def status(self) -> dict:
        with self.cond:
            return self._status()

    def _status(self) -> dict:
        return {"state": "busy" if self.busy and self.state == "ready" else self.state, "worker_state": self.state,
                "message": self.message, "busy": self.busy, "session": self.session, "task": self.task,
                "session_after": self.session_after, "info": self.info, "exit_code": self.exit_code, "last_seq": self.seq,
                "first_seq": self.events[0]["seq"] if self.events else self.seq + 1}

    def _append(self, event: dict) -> None:
        self.seq += 1
        self.events.append({**event, "seq": self.seq})
        if len(self.events) > MAX_EVENTS:
            del self.events[:len(self.events) - MAX_EVENTS]
        self.cond.notify_all()

    def _apply(self, event: dict) -> None:
        kind = event.get("type")
        if kind == "worker":
            state = event.get("state")
            self.message = event.get("message", "")
            if state == "ready":
                self.state = "ready"
                self.info = {key: event.get(key) for key in ("seconds", "network", "vram_gb", "cut_offs", "emp",
                                                             "sampling", "chunked_attention")}
            elif state in ("loading", "failed", "stopped"):
                self.state = state
            if state == "failed" and self.busy:
                self._finish("worker_failed")
        elif kind == "task_end" and event.get("session") == self.session:
            self.busy = False
            if event.get("vram_gb") is not None:
                self.info["vram_gb"] = event["vram_gb"]

    def _finish(self, termination: str) -> None:
        """End the queued or running task when the worker cannot."""
        self._append({"type": "task_end", "session": self.session, "termination": termination,
                      "steps": None, "alarms": None, "time": round(time.time(), 3)})
        self.busy = False

    # -- worker process
    def start(self) -> dict:
        with self.cond:
            if self.proc is not None and self.proc.poll() is None:
                return self._status()
            env = self.env() if self.env else None
            self.proc = subprocess.Popen(
                self.command, cwd=self.cwd, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT, text=True, encoding="utf-8", errors="replace", bufsize=1, env=env,
                creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
            self.state, self.message, self.exit_code, self.info = "loading", "작업 프로세스를 시작하는 중", None, {}
            self._append({"type": "worker", "state": "starting", "message": self.message,
                          "time": round(time.time(), 3)})
            threading.Thread(target=self._read, args=(self.proc,), name="live-agent-reader", daemon=True).start()
            return self._status()

    def _read(self, proc: subprocess.Popen) -> None:
        assert proc.stdout is not None
        for line in proc.stdout:
            line = line.rstrip("\r\n")
            if line.startswith(EVENT_PREFIX):
                try:
                    event = json.loads(line[len(EVENT_PREFIX):])
                except json.JSONDecodeError:
                    event = {"type": "log", "text": line[-LOG_CHARS:]}
            elif line.strip():
                event = {"type": "log", "text": line[-LOG_CHARS:], "time": round(time.time(), 3)}
            else:
                continue
            with self.cond:
                self._append(event)  # first, so a failure message comes before the task_end it causes
                self._apply(event)
        code = proc.wait()
        with self.cond:
            if self.proc is not proc:
                return
            reported_failure = self.state == "failed"
            self.proc, self.exit_code = None, code
            if code == 0:
                self.state, self.message = "off", "모델을 내렸습니다"
            else:
                self.state = "failed"
                if not reported_failure:
                    self.message = f"작업 프로세스가 예기치 않게 끝났습니다 (exit {code})"
            self._append({"type": "worker", "state": "exited", "code": code, "message": self.message,
                          "time": round(time.time(), 3)})
            if self.busy:
                self._finish("worker_exited")

    def _write(self, message: dict) -> None:
        if self.proc is None or self.proc.stdin is None:
            raise ValueError("실시간 에이전트가 실행 중이 아닙니다.")
        try:
            self.proc.stdin.write(json.dumps(message, ensure_ascii=False) + "\n")
            self.proc.stdin.flush()
        except (BrokenPipeError, OSError, ValueError) as error:
            raise ValueError(f"실시간 에이전트에 요청을 보내지 못했습니다: {error}") from error

    def submit(self, task: str, max_steps: int, seed: int | None = None) -> dict:
        """Queue one task; the worker is started (and the model loaded) first when needed."""
        with self.cond:
            if self.busy:
                raise ValueError("이미 실행 중인 작업이 있습니다. 끝나거나 중지한 뒤 다시 보내 주세요.")
            if self.state == "stopping":
                raise ValueError("모델을 내리는 중입니다. 잠시 뒤 다시 시도해 주세요.")
        self.start()
        with self.cond:
            after = self.seq
            session = uuid.uuid4().hex[:12]
            self.busy, self.session, self.task, self.session_after = True, session, task, after
            self._append({"type": "task_queued", "session": session, "task": task, "max_steps": max_steps,
                          "time": round(time.time(), 3)})
            try:
                self._write({"cmd": "task", "session": session, "task": task, "max_steps": max_steps, "seed": seed})
            except ValueError:
                self._finish("worker_unavailable")
                raise
            return {"session": session, "after": after, **self._status()}

    def cancel(self) -> dict:
        with self.cond:
            if self.busy and self.session:
                self._write({"cmd": "cancel", "session": self.session})
                self._append({"type": "cancel_requested", "session": self.session, "time": round(time.time(), 3)})
            return self._status()

    def stop(self, timeout: float = 30) -> dict:
        """Shut the worker down (frees the GPU); kill it when it does not end in time."""
        with self.cond:
            proc = self.proc
            if proc is None or proc.poll() is not None:
                return self._status()
            self.state, self.message = "stopping", "모델을 내리는 중"
            self._append({"type": "worker", "state": "stopping", "message": self.message,
                          "time": round(time.time(), 3)})
            try:
                self._write({"cmd": "shutdown"})
            except ValueError:
                pass
        try:
            proc.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            proc.terminate()
            try:
                proc.wait(timeout=10)
            except subprocess.TimeoutExpired:
                proc.kill()
                proc.wait(timeout=10)
        deadline = time.monotonic() + 5
        with self.cond:  # let the reader record the exit
            while self.proc is proc and time.monotonic() < deadline:
                self.cond.wait(0.2)
            return self._status()

    # -- events
    def events_after(self, after: int, wait: float = 0.0) -> dict:
        deadline = time.monotonic() + max(0.0, min(wait, 30.0))
        with self.cond:
            while True:
                first = self.events[0]["seq"] if self.events else self.seq + 1
                start = max(0, after + 1 - first)
                new = self.events[start:start + MAX_BATCH]
                remaining = deadline - time.monotonic()
                if new or remaining <= 0:
                    return {"events": new, "trimmed": after + 1 < first, **self._status()}
                self.cond.wait(remaining)

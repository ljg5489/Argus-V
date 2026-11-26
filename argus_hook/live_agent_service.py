# 파일 위치: ~/Desktop/Argus-V/argus_hook/live_agent_service.py
"""The live agent worker (live_agent.py) as seen by dashboard_server.py: start a worker for each task, shut it down
when the task has ended, and keep its events so the browser can follow a task with long polling.

gpt-oss-20b is on the GPU only while a chat task runs. ``submit`` starts a worker (it loads the model), the worker
runs the task, and its ``task_end`` makes the service shut it down; the GPU memory is freed when the process has
exited, so other jobs can use the GPU again. A worker that does not exit in time is terminated, then killed. A task
sent while the previous worker is still unloading waits for that worker to exit and then gets a new one.

Events get a sequence number; ``events_after(n)`` returns the ones after ``n`` (waiting a little when there are
none yet), so a reloaded page can rebuild a running task from the start.

``submit`` passes ``payload`` (the conversation's earlier turns and the memory mirror, see agent_memory.py) to the
worker with the task, and keeps ``meta`` (which conversation the task belongs to) in the status for the page.
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
UNLOAD_TIMEOUT = 30.0  # seconds a worker gets to exit after the shutdown request before it is terminated


class LiveAgent:
    def __init__(self, command: list[str], cwd: Path, env: Callable[[], dict] | None = None,
                 unload_timeout: float = UNLOAD_TIMEOUT):
        self.command, self.cwd, self.env = list(command), Path(cwd), env
        self.unload_timeout = unload_timeout
        self.cond = threading.Condition()
        self.submit_lock = threading.Lock()  # one submit at a time, so each task gets a worker of its own
        self.events: list[dict] = []
        self.seq = 0
        self.proc: subprocess.Popen | None = None
        self.unloading: subprocess.Popen | None = None  # the worker the service is shutting down
        self.state = "off"
        self.message = ""
        self.info: dict = {}
        self.load_times: list[float] = []  # queued -> ready of the last tasks (the page's estimate)
        self.load_times_path: Path | None = None  # where they are kept between server starts (keep_load_times)
        self.queued_at: float | None = None
        self.busy = False
        self.session: str | None = None
        self.session_after: int | None = None  # last sequence number before the current task was queued
        self.task: str | None = None
        self.meta: dict = {}  # e.g. the conversation of the current task, for a page that reattaches
        self.exit_code: int | None = None

    # -- state
    def running(self) -> bool:
        with self.cond:
            return self._alive()

    def _alive(self) -> bool:
        return self.proc is not None and self.proc.poll() is None

    def status(self) -> dict:
        with self.cond:
            return self._status()

    def keep_load_times(self, path: Path) -> None:
        """Keep the load times in ``path`` (next to the conversations), so the first task after a restart has one."""
        with self.cond:
            self.load_times_path = Path(path)
            try:
                data = json.loads(self.load_times_path.read_text(encoding="utf-8"))
                self.load_times = [float(item) for item in data if isinstance(item, (int, float))][-5:]
            except (OSError, ValueError, TypeError):
                self.load_times = []

    def _write_load_times(self) -> None:
        if self.load_times_path is None:
            return
        try:
            self.load_times_path.parent.mkdir(parents=True, exist_ok=True)
            self.load_times_path.write_text(json.dumps(self.load_times), encoding="utf-8")
        except OSError:
            pass

    def _status(self) -> dict:
        return {"state": "busy" if self.busy and self.state == "ready" else self.state, "worker_state": self.state,
                "message": self.message, "busy": self.busy, "alive": self._alive(), "session": self.session,
                "task": self.task, "session_after": self.session_after, "info": self.info, "meta": self.meta,
                "exit_code": self.exit_code, "last_seq": self.seq,
                "first_seq": self.events[0]["seq"] if self.events else self.seq + 1,
                "load_estimate": sorted(self.load_times)[len(self.load_times) // 2] if self.load_times else None}

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
            if state == "ready":
                self.info = {key: event.get(key) for key in ("seconds", "network", "vram_gb", "cut_offs", "emp",
                                                             "sampling", "chunked_attention")}
                if self.queued_at is not None:  # from the moment the page sent the task (process start and imports too)
                    self.load_times = (self.load_times + [round(time.monotonic() - self.queued_at, 1)])[-5:]
                    self.queued_at = None
                    self._write_load_times()
            if state == "failed" or (state in ("loading", "ready", "stopped") and self.unloading is None):
                # while the service unloads the worker, its state stays "stopping"
                self.state, self.message = state, event.get("message", "")
            if state == "failed" and self.busy:
                self._finish("worker_failed")
        elif kind == "task_end" and event.get("session") == self.session:
            self.busy = False
            if event.get("vram_gb") is not None:
                self.info["vram_gb"] = event["vram_gb"]
            self._unload("작업이 끝나 모델을 내리는 중")

    def _finish(self, termination: str) -> None:
        """End the queued or running task when the worker cannot, and unload the worker if it is still there."""
        self._append({"type": "task_end", "session": self.session, "termination": termination,
                      "steps": None, "alarms": None, "time": round(time.time(), 3)})
        self.busy = False
        self._unload("모델을 내리는 중")

    # -- worker process
    def _start(self) -> None:
        with self.cond:
            if self._alive():
                return
            env = self.env() if self.env else None
            self.proc = subprocess.Popen(
                self.command, cwd=self.cwd, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT, text=True, encoding="utf-8", errors="replace", bufsize=1, env=env,
                creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
            self.unloading = None
            self.state, self.message, self.exit_code, self.info = "loading", "작업 프로세스를 시작하는 중", None, {}
            self._append({"type": "worker", "state": "starting", "message": self.message,
                          "time": round(time.time(), 3)})
            threading.Thread(target=self._read, args=(self.proc,), name="live-agent-reader", daemon=True).start()

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
                if self.busy and self.session:  # raw output while a task runs is that task's (pages see it by session)
                    event["session"] = self.session
            else:
                continue
            with self.cond:
                if self.proc is not proc:  # late output of a worker that has been replaced
                    continue
                self._append(event)  # first, so a failure message comes before the task_end it causes
                self._apply(event)
        code = proc.wait()
        with self.cond:
            if self.proc is not proc:
                return
            unloaded = self.unloading is proc
            reported_failure = self.state == "failed"
            self.proc, self.unloading, self.exit_code = None, None, code
            self.info.pop("vram_gb", None)  # the process is gone, and with it the model's GPU memory
            if reported_failure:
                self.state = "failed"
            elif code == 0 or unloaded:
                self.state = "off"
                self.message = ("모델을 내렸습니다 · GPU 메모리를 비웠습니다" if code == 0 else
                                f"모델을 내렸습니다 · 작업 프로세스를 강제로 끝냈습니다 (exit {code})")
            else:
                self.state = "failed"
                self.message = f"작업 프로세스가 예기치 않게 끝났습니다 (exit {code})"
            self._append({"type": "worker", "state": "exited", "code": code, "unloaded": self.state == "off",
                          "message": self.message, "time": round(time.time(), 3)})
            if self.busy:
                self._finish("cancelled" if unloaded else "worker_exited")

    def _write(self, message: dict) -> None:
        if self.proc is None or self.proc.stdin is None:
            raise ValueError("실시간 에이전트가 실행 중이 아닙니다.")
        try:
            self.proc.stdin.write(json.dumps(message, ensure_ascii=False) + "\n")
            self.proc.stdin.flush()
        except (BrokenPipeError, OSError, ValueError) as error:
            raise ValueError(f"실시간 에이전트에 요청을 보내지 못했습니다: {error}") from error

    def _unload(self, message: str, now: bool = False) -> None:
        """Shut the worker down (lock held); ``now`` ends the process at once instead of asking it to exit."""
        proc = self.proc
        if proc is None or proc.poll() is not None or self.unloading is proc:
            return
        self.unloading = proc
        if self.state != "failed":  # a reported failure stays visible; that worker exits by itself
            self.state, self.message = "stopping", message
            self._append({"type": "worker", "state": "stopping", "message": message,
                          "time": round(time.time(), 3)})
        if now:
            proc.terminate()
        else:
            try:
                self._write({"cmd": "shutdown"})
            except ValueError:
                proc.terminate()
        threading.Thread(target=self._reap, args=(proc,), name="live-agent-unload", daemon=True).start()

    def _reap(self, proc: subprocess.Popen) -> None:
        """Make sure an unloading worker ends: terminate it, then kill it, when it does not exit in time."""
        try:
            proc.wait(timeout=self.unload_timeout)
            return
        except subprocess.TimeoutExpired:
            proc.terminate()
        try:
            proc.wait(timeout=10)
        except subprocess.TimeoutExpired:
            proc.kill()

    def _wait_exit(self, proc: subprocess.Popen) -> None:
        """Wait until ``proc`` has ended (the reaper ends it at the latest) and its exit has been recorded."""
        try:
            proc.wait(timeout=self.unload_timeout + 20)
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.wait(timeout=10)
        deadline = time.monotonic() + 5
        with self.cond:
            while self.proc is proc and time.monotonic() < deadline:
                self.cond.wait(0.2)

    def submit(self, task: str, max_steps: int, seed: int | None = None, payload: dict | None = None,
               meta: dict | None = None) -> dict:
        """Run one task on a worker of its own: the worker loads the model, runs the task and is shut down when the
        task has ended, so gpt-oss-20b is on the GPU only while a task runs. ``payload`` goes to the worker with the
        task; ``meta`` stays in the status and the task_queued event."""
        with self.submit_lock:
            with self.cond:
                if self.busy:
                    raise ValueError("이미 실행 중인 작업이 있습니다. 끝나거나 중지한 뒤 다시 보내 주세요.")
                previous = self.proc
                self._unload("이전 작업의 모델을 내리는 중")  # normally under way since that task ended
            if previous is not None:
                self._wait_exit(previous)
            with self.cond:  # held until the task is queued, so even an instant worker failure ends this task
                self._start()
                after = self.seq
                session = uuid.uuid4().hex[:12]
                self.busy, self.session, self.task, self.session_after = True, session, task, after
                self.meta = dict(meta or {})
                self.queued_at = time.monotonic()
                self._append({"type": "task_queued", "session": session, "task": task, "max_steps": max_steps,
                              "meta": self.meta, "time": round(time.time(), 3)})
                try:
                    self._write({**(payload or {}), "cmd": "task", "session": session, "task": task,
                                 "max_steps": max_steps, "seed": seed})
                except ValueError:
                    self._finish("worker_unavailable")
                    raise
                return {"session": session, "after": after, **self._status()}

    def cancel(self) -> dict:
        with self.cond:
            if self.busy and self.session:
                self._append({"type": "cancel_requested", "session": self.session, "time": round(time.time(), 3)})
                if self.state == "ready":
                    self._write({"cmd": "cancel", "session": self.session})  # ends at the next token or step
                else:  # still loading and nothing has run: end the process instead of finishing the load first
                    self._unload("작업을 중지해 모델 올리기를 멈추는 중", now=True)
            return self._status()

    def stop(self) -> dict:
        """Unload now (모델 내리기, server exit): a running task is cancelled; frees the GPU."""
        with self.cond:
            proc = self.proc
            if proc is None or proc.poll() is not None:
                return self._status()
            self._unload("모델을 내리는 중")
        self._wait_exit(proc)
        with self.cond:
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

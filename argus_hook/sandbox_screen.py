"""The real screen of the "computer" sandbox (SANDBOX_PC), for the local page: its pictures, its keyboard and mouse.

Served by argus_hook/agent_server.py for a sandbox that has a display (a desk.py next to its sandbox.py: SANDBOX_PC,
SANDBOX_NET). Every function takes the sandbox it is about (sandbox_boxes.Box):

    GET  /api/sandbox/screen           is the desktop on, and how large
    POST /api/sandbox/screen/start     start the desktop in the sandbox (Xvfb, a window manager, a bar, a terminal)
    POST /api/sandbox/screen/stop      end it
    GET  /api/sandbox/screen/stream    its pictures, one after another (multipart/x-mixed-replace: an <img> shows it)
    POST /api/sandbox/screen/input     {"events": [...]}: keys, the pointer, buttons, the wheel

How it reaches the sandbox: SANDBOX_PC/desk.py, which is a `docker exec` in the sandbox's own container. No port is
opened in the sandbox or on this machine: pictures and events travel over the exec's pipes. It takes neither
sandbox.py's lock nor a snapshot, so the screen stays on and usable while a command of the agent's runs. What the user
does on that screen is not one of the server's commands: no snapshot is taken for it, nothing of it is in a turn's
record, and the way back ("마지막 명령 전으로") goes to before the last *command*, with whatever the screen changed
since undone as well.

Only this computer's local page (agent_server checks, as for the rest of the sandbox computer).
"""

from __future__ import annotations

import json
import os
import re
import select
import subprocess
import threading
import time

import sandbox_boxes as BOXES

BOUNDARY = "argusframe"
SIZES = ("1024x640", "1280x720", "800x600", "1280x800")
STREAMS = 3          # pictures streams open at once
EVENTS = 400         # events taken from one request
FIRST_PICTURE = 8.0  # seconds a stream waits for its first picture before saying the screen is off
KEY = re.compile(r"[A-Za-z0-9]{1,24}\Z")

LOCK = threading.Lock()
STATE = {"input": {}, "streams": 0}  # input: the one input.py kept open, by sandbox


def helper(box):
    path = box.root / "desk.py"
    return path if path.is_file() else None


def available(box) -> bool:
    """Whether ``box`` has a display."""
    return helper(box) is not None


def call(DS, box, *args: str, timeout: int = 60) -> dict:
    """One desk.py command that answers in JSON (on stdout, or on stderr when it failed)."""
    try:
        done = subprocess.run(["python3.11", str(helper(box)), *args], capture_output=True, text=True, encoding="utf-8",
                              errors="replace", timeout=timeout, env=DS.live_env())
    except (subprocess.TimeoutExpired, OSError) as error:
        return {"status": "ERROR", "reason": type(error).__name__}
    for text in (done.stdout, done.stderr):
        try:
            data = json.loads(text or "")
        except json.JSONDecodeError:
            continue
        if isinstance(data, dict):
            return data
    return {"status": "ERROR", "reason": (done.stderr or done.stdout or "no answer")[-300:]}


def is_off(reason: str) -> bool:
    return "not running" in reason or "stopped" in reason


def said(data: dict) -> dict:
    """desk.py's answer as the page reads it."""
    reason = str(data.get("reason") or "")
    out = {"status": str(data.get("status") or "ERROR"), "size": data.get("size")}
    if out["status"] == "ERROR":
        out["reason"] = "샌드박스가 꺼져 있습니다." if is_off(reason) else reason[-300:] or "샌드박스가 답하지 않았습니다"
        out["sandbox_off"] = is_off(reason)
    return out


NO_SCREEN = {"error": "이 샌드박스에는 화면이 없습니다.", "code": "no_screen"}


def state(DS, box) -> tuple[int, dict]:
    if not available(box):
        return 404, NO_SCREEN
    return 200, {**said(call(DS, box, "screen-state")), "sizes": list(SIZES), "sandbox": box.name}


def start(DS, box, body: dict) -> tuple[int, dict]:
    if not available(box):
        return 404, NO_SCREEN
    size = body.get("size") or SIZES[0]
    if size not in SIZES:
        return 400, {"error": f"화면 크기는 {', '.join(SIZES)} 중 하나여야 합니다."}
    width, height = size.split("x")
    data = call(DS, box, "screen-start", width, height)
    if data.get("status") == "ERROR" and is_off(str(data.get("reason") or "")):
        # the sandbox itself is off (a command over its time limit stops it): started as a command would start it
        if BOXES.cli(DS, box, ["up"], timeout=300).get("status") != "ERROR":
            data = call(DS, box, "screen-start", width, height)
    DS.STORE.audit("screen", "local", what="start", sandbox=box.name, status=str(data.get("status")))
    return 200, said(data)


def stop(DS, box) -> tuple[int, dict]:
    if not available(box):
        return 404, NO_SCREEN
    close_input(box)
    data = call(DS, box, "screen-stop")
    DS.STORE.audit("screen", "local", what="stop", sandbox=box.name, status=str(data.get("status")))
    return 200, said(data)


def clean(events) -> list[dict]:
    """The events of a request as input.py takes them: nothing else passes (keys by name, numbers within bounds)."""
    out = []
    for event in events if isinstance(events, list) else []:
        if not isinstance(event, dict) or len(out) >= EVENTS:
            continue
        kind = event.get("t")
        try:
            if kind == "k" and isinstance(event.get("key"), str) and KEY.match(event["key"]):
                out.append({"t": "k", "key": event["key"], "down": bool(event.get("down"))})
            elif kind == "m":
                out.append({"t": "m", "x": max(0, min(8191, int(event["x"]))), "y": max(0, min(8191, int(event["y"])))})
            elif kind == "b" and int(event["button"]) in (1, 2, 3):
                out.append({"t": "b", "button": int(event["button"]), "down": bool(event.get("down"))})
            elif kind == "w" and int(event["dy"]) != 0:
                out.append({"t": "w", "dy": 1 if int(event["dy"]) > 0 else -1})
        except (KeyError, TypeError, ValueError):
            continue
    return out


def close_input(box=None) -> None:
    """Close the input.py kept open for ``box`` (every one, when none is named)."""
    with LOCK:
        names = [box.name] if box is not None else list(STATE["input"])
        ended = [STATE["input"].pop(name, None) for name in names]
    for process in ended:
        if process is None:
            continue
        try:
            process.stdin.close()  # input.py lets go of what is held and ends
        except OSError:
            pass
        try:
            process.wait(timeout=3)
        except subprocess.TimeoutExpired:
            process.kill()


def send(DS, box, body: dict) -> tuple[int, dict]:
    """POST /api/sandbox/screen/input: the events go down the one input.py that is kept open for ``box``."""
    if not available(box):
        return 404, NO_SCREEN
    events = clean(body.get("events"))
    if not events:
        return 200, {"taken": 0}
    lines = "".join(json.dumps(event) + "\n" for event in events).encode("utf-8")
    with LOCK:
        for attempt in (1, 2):
            process = STATE["input"].get(box.name)
            if process is None or process.poll() is not None:
                process = STATE["input"][box.name] = subprocess.Popen(
                    ["python3.11", str(helper(box)), "screen-input"], stdin=subprocess.PIPE, stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL, env=DS.live_env())
            try:
                process.stdin.write(lines)
                process.stdin.flush()
                return 200, {"taken": len(events)}
            except (BrokenPipeError, OSError):
                STATE["input"].pop(box.name, None)  # it ended (the desktop was stopped, the sandbox restarted): once more, anew
    return 409, {"error": "화면이 꺼져 있습니다.", "code": "screen_off"}


def stream(DS, box, handler) -> None:
    """GET /api/sandbox/screen/stream: screen.py's pictures of ``box`` to the page until it stops reading."""
    if not available(box):
        return handler._json(404, NO_SCREEN)
    with LOCK:
        if STATE["streams"] >= STREAMS:
            return handler._json(429, {"error": "화면을 보는 창이 너무 많습니다. 다른 창을 닫아 주세요.", "code": "streams"})
        STATE["streams"] += 1
    process = None
    try:
        process = subprocess.Popen(["python3.11", str(helper(box)), "screen-stream", "--fps", "12", "--quality", "72"],
                                   stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, env=DS.live_env())
        source = process.stdout.fileno()
        ready, _, _ = select.select([source], [], [], FIRST_PICTURE)
        first = os.read(source, 65_536) if ready else b""
        if not first:  # no X server to draw from: the desktop is off (or the sandbox is)
            return handler._json(409, {"error": "화면이 꺼져 있습니다. '화면 켜기'를 눌러 주세요.", "code": "screen_off"})
        handler.send_response(200)
        handler.send_header("Content-Type", f"multipart/x-mixed-replace; boundary={BOUNDARY}")
        handler.send_header("Cache-Control", "no-store")
        handler.send_header("X-Content-Type-Options", "nosniff")
        handler.end_headers()
        chunk = first
        while chunk:
            handler.wfile.write(chunk)
            handler.wfile.flush()
            chunk = os.read(source, 65_536)
    except (BrokenPipeError, ConnectionResetError, OSError):
        pass  # the page closed the window (or the tab): the stream ends with it
    finally:
        if process is not None:
            process.kill()  # the docker client goes; screen.py in the sandbox ends at its next picture (nobody reads)
            process.wait()
        with LOCK:
            STATE["streams"] -= 1

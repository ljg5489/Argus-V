"""The dashboard's local server with the agent chat's "무한 step" and the sandbox computer on: dashboard_server.py as
it is, wrapped.

    .venv/bin/python argus_hook/agent_server.py      (instead of argus_hook/dashboard_server.py; the same page and port)

dashboard_server.py and live_agent.py are locked by plan v1.6 (the first GPU run) and take 1-10 steps a turn. This
file changes neither: it imports the locked server, lifts its step bound for one more value (UNLIMITED), and has it
start argus_hook/live_agent_free.py as the chat worker, which is the locked worker with the same bound lifted and the
unlimited turn's own stops (see that file). Every turn of 1-10 steps runs as before.

What it adds, and where it refuses:
- /api/live/start takes max_steps 1-10 or UNLIMITED; any other number is refused, as before;
- an unlimited turn only from this computer's local page, never from a page elsewhere (the Pages copy) and never
  for a plan's run (battery);
- /api/health says "unlimited_steps", so the page offers "무한" only on this server;
- a turn continued after hundreds of steps lists its latest EARLIER_KEPT earlier commands, not all of them;
- it does not start with a plan's memory root (ARGUS_LIVE_MEMORY_DIR): the plan's run uses the locked server;
- the sandbox computer (argus_hook/sandbox_shell.py; the page's "샌드박스 컴퓨터" tab): the user's own terminal, file
  manager, editor and system window over the agent's sandbox. Only this computer's local page; nothing of it changes
  the sandbox while an agent task runs, and no agent task or sandbox clean-up starts while one of its commands runs.
  /api/health says "sandbox_shell".
      GET  /api/sandbox/shell      what the page shows around the desktop (no sandbox call)
      POST /api/sandbox/exec       one command line of the terminal
      GET  /api/sandbox/files      every entry under /workspace
      POST /api/sandbox/read       a file's text, or a picture
      POST /api/sandbox/change     new folder, new file, rename, delete, save, end a process
      GET  /api/sandbox/system     the container's CPU, memory, process count and disks
      POST /api/sandbox/processes  what runs in the sandbox
      POST /api/sandbox/power      start a sandbox that is off
      POST /api/sandbox/stop       end the command of the user's that runs now
- more than one sandbox (argus_hook/sandbox_boxes.py): SANDBOX/ (the plan's, locked: the locked server uses it, byte
  for byte), SANDBOX_PC/ (a screen, tools, the package index) and SANDBOX_NET/ (the same with the public web open),
  whichever folders are there. The agent chat works in one of them, chosen on the page (POST /api/sandbox/agent) or
  at the start (`--sandbox plain|pc|net`, `--plain`) and kept between starts; the sandbox computer looks at any of
  them: every /api/sandbox/... address takes `sandbox` (in the query of a GET, in the body of a POST; none: the
  agent's). A sandbox with a display has its real screen served by argus_hook/sandbox_screen.py (/api/sandbox/screen…).
      GET  /api/sandbox/list       the sandboxes, and which one the agent works in
      POST /api/sandbox/agent      give the agent another sandbox (between turns)
      POST /api/sandbox/restore    a sandbox that is not the agent's, back to before its last command
      POST /api/agent/output-tokens  what one step may generate (2,048 is the plan's; kept between starts)
      GET  /api/sandbox/network    where a sandbox with a proxy went on the web (hosts only)
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import live_agent_free as FREE  # noqa: E402
import sandbox_boxes as BOXES  # noqa: E402
import sandbox_screen as SCREEN  # noqa: E402
import sandbox_shell as SHELL  # noqa: E402
from live_agent_free import UNLIMITED, ensure_running  # noqa: E402  (no model import there)

WORKER = HERE / "live_agent_free.py"
PC_ROOT = HERE.parent / "SANDBOX_PC"  # the everyday "computer" sandbox (a display, tools, the package index)
EARLIER_KEPT = 60  # earlier commands listed to a continued turn (dashboard_server.resume_material lists every one)


def enable(DS, patch=setattr) -> None:
    """Turn the unlimited option on in the imported dashboard_server module ``DS``. ``patch(object, name, value)``
    sets an attribute (a test passes its own, which puts everything back)."""
    limit = DS.MAX_LIVE_STEPS  # 10: what the locked server takes
    start, status, material = DS.start_live, DS.runtime_status, DS.resume_material

    def start_live(task, max_steps=5, *args, **kwargs):
        steps = int(max_steps)
        if steps > limit and steps != UNLIMITED:
            raise ValueError(f"step 수는 1~{limit}이거나 무한이어야 합니다.")
        if steps == UNLIMITED and (kwargs.get("remote") or kwargs.get("battery")):
            raise ValueError("무한 step은 이 컴퓨터의 로컬 페이지에서만, 계획 실행이 아닐 때만 쓸 수 있습니다.")
        return start(task, max_steps, *args, **kwargs)

    def runtime_status(*args, **kwargs):
        mine = BOXES.agent(DS)
        return {**status(*args, **kwargs), "unlimited_steps": UNLIMITED, "sandbox_shell": True,
                "sandbox_screen": SCREEN.available(mine), "sandbox_folder": mine.root.name,
                "agent_sandbox": mine.name, "sandboxes": boxes_said(DS), "output_tokens": output_said()}

    def resume_material(*args, **kwargs):
        out = material(*args, **kwargs)
        earlier = out.get("earlier") or []
        if len(earlier) > EARLIER_KEPT:  # a turn of hundreds of steps: its latest commands, the count of the rest
            out = {**out, "earlier": earlier[-EARLIER_KEPT:], "earlier_left_out": len(earlier) - EARLIER_KEPT}
        return out

    inner = DS._start_live  # what dashboard_server.start_live calls under its start lock

    def _start_live(*args, **kwargs):
        # under the same lock sandbox_shell.guarded marks itself busy: never both at once (a reading of the system
        # window, a second or two, is waited for; a command of the user's is not)
        if not SHELL.settled(box=BOXES.agent(DS)):  # (in the agent's own sandbox: another one is the user's to use meanwhile)
            raise ValueError("샌드박스 컴퓨터에서 실행 중인 명령이 끝난 뒤 다시 보내 주세요.")
        return inner(*args, **kwargs)

    BOXES.install_ledgers(DS.AM, patch)
    patch(DS, "MAX_LIVE_STEPS", UNLIMITED)
    patch(DS, "start_live", start_live)
    patch(DS, "_start_live", _start_live)
    patch(DS, "runtime_status", runtime_status)
    patch(DS, "resume_material", resume_material)
    patch(DS, "Handler", handler(DS))
    patch(DS.LIVE, "command", [sys.executable, str(WORKER)])


LOCAL_ONLY = {"error": "샌드박스 컴퓨터는 이 컴퓨터의 로컬 페이지에서만 쓸 수 있습니다.", "local_only": True}
SHELL_BUSY = {"error": "샌드박스 컴퓨터에서 실행 중인 명령이 끝난 뒤 다시 해 주세요.", "code": "shell_busy"}
BODY_LIMIT = 300_000  # a save carries the file's text (at most 65,536 bytes of it, as JSON)


def handler(DS):
    """The locked server's request handler with the sandbox computer's addresses in front of it. The same checks as
    its own local-only actions: the request names this machine (no DNS rebinding), comes from an allowed page, and
    that page is one this machine serves (a browser sends Origin with every cross-site POST)."""
    import json
    from urllib.parse import urlparse

    from urllib.parse import parse_qs

    # each takes the sandbox the request names (sandbox_boxes.get: none named is the agent's)
    reads = {"/api/sandbox/shell": lambda box: (200, SHELL.describe(DS, box)), "/api/sandbox/files": lambda box: (200, SHELL.files(DS, box)),
             "/api/sandbox/system": lambda box: (200, SHELL.system(DS, box)), "/api/sandbox/screen": lambda box: SCREEN.state(DS, box),
             "/api/sandbox/network": lambda box: (200, SHELL.network_log(DS, box)),
             "/api/sandbox/list": lambda box: (200, {"sandboxes": boxes_said(DS), "agent": BOXES.agent(DS).name})}
    writes = {"/api/sandbox/exec": lambda box, body: SHELL.execute(DS, box, body), "/api/sandbox/read": lambda box, body: SHELL.read(DS, box, body),
              "/api/sandbox/change": lambda box, body: SHELL.change(DS, box, body),
              "/api/sandbox/processes": lambda box, body: SHELL.processes(DS, box),
              "/api/sandbox/power": lambda box, body: SHELL.power(DS, box, body), "/api/sandbox/stop": lambda box, body: SHELL.stop(DS, box),
              "/api/sandbox/restore": lambda box, body: SHELL.restore(DS, box),
              "/api/sandbox/screen/start": lambda box, body: SCREEN.start(DS, box, body),
              "/api/sandbox/screen/stop": lambda box, body: SCREEN.stop(DS, box),
              "/api/sandbox/screen/input": lambda box, body: SCREEN.send(DS, box, body)}

    class Handler(DS.Handler):
        def _terminal_refused(self):
            if not self._local_host():
                return 403, {"error": "로컬 주소(127.0.0.1)로만 접근할 수 있습니다."}
            origin = self.headers.get("Origin")
            if origin is not None and origin not in DS.ALLOWED_ORIGINS:
                return 403, {"error": "허용되지 않은 웹 출처입니다."}
            if not self._local_page():
                return 403, LOCAL_ONLY
            # a GET from another site's page (an <img>, a <script>) carries no Origin, but browsers say where it is from
            if self.headers.get("Sec-Fetch-Site") not in (None, "same-origin", "none"):
                return 403, LOCAL_ONLY
            return None

        def _sandbox_body(self) -> dict:
            length = int(self.headers.get("Content-Length", "0"))
            if not 0 <= length <= BODY_LIMIT:
                raise ValueError("요청이 너무 큽니다.")
            body = json.loads(self.rfile.read(length) or b"{}")
            if not isinstance(body, dict):
                raise ValueError("JSON 객체가 필요합니다.")
            return body

        def do_GET(self):
            path = urlparse(self.path).path
            if path == "/api/sandbox/screen/stream" or path in reads:
                refused = self._terminal_refused()
                if refused:
                    return self._json(*refused)
                try:
                    box = BOXES.get(DS, (parse_qs(urlparse(self.path).query).get("sandbox") or [None])[0])
                except ValueError as error:
                    return self._json(400, {"error": str(error)})
                if path == "/api/sandbox/screen/stream":  # pictures, one after another, until the page stops reading
                    return SCREEN.stream(DS, box, self)
                try:
                    return self._json(*reads[path](box))
                except Exception as error:  # the page gets a reason, never a stack
                    return self._json(500, {"error": f"{type(error).__name__}: {str(error)[:200]}"})
            return super().do_GET()

        def do_POST(self):
            path = urlparse(self.path).path
            if path in writes or path in ("/api/sandbox/agent", "/api/agent/output-tokens"):
                refused = self._terminal_refused()
                if refused:
                    return self._json(*refused)
                try:
                    body = self._sandbox_body()
                except ValueError as error:  # (a JSON error is one too)
                    return self._json(400, {"error": f"요청을 읽지 못했습니다: {str(error)[:120]}"})
                if path == "/api/sandbox/agent":
                    return self._json(*choose(DS, body.get("sandbox")))
                if path == "/api/agent/output-tokens":
                    return self._json(*keep_output_tokens(DS, body.get("tokens")))
                try:
                    box = BOXES.get(DS, body.get("sandbox"))
                except ValueError as error:
                    return self._json(400, {"error": str(error)})
                try:
                    return self._json(*writes[path](box, body))
                except Exception as error:
                    return self._json(500, {"error": f"{type(error).__name__}: {str(error)[:200]}"})
            if (path.startswith("/api/live/sandbox/") or path == "/api/agent/start") and not SHELL.settled(box=BOXES.agent(DS)):
                return self._json(409, SHELL_BUSY)  # nothing else changes the agent's sandbox while a command runs in it
            return super().do_POST()

    return Handler


PORT = 8765  # the one dashboard_server.main listens on


def port_holder(port: int = PORT) -> dict | None:
    """Who listens on 127.0.0.1:``port`` already (None: nobody): {"pid", "command"}, as far as this machine says."""
    import socket

    probe = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        probe.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # as the server itself binds
        probe.bind(("127.0.0.1", port))
        return None
    except OSError:
        pass
    finally:
        probe.close()
    holder = {"pid": None, "command": ""}
    try:
        import re
        import subprocess

        listing = subprocess.run(["ss", "-ltnp"], capture_output=True, text=True, timeout=5).stdout
        line = next((row for row in listing.splitlines() if re.search(rf"127\.0\.0\.1:{port}\s", row)), "")
        found = re.search(r"pid=(\d+)", line)
        if found:
            holder["pid"] = int(found.group(1))
            raw = Path(f"/proc/{found.group(1)}/cmdline").read_bytes()
            holder["command"] = raw.replace(b"\0", b" ").decode("utf-8", errors="replace").strip()
    except (OSError, ValueError, subprocess.SubprocessError):
        pass  # the port is taken all the same
    return holder


def port_message(holder: dict, port: int = PORT) -> str:
    """What to do about a port that is taken, in plain words (instead of bind's traceback)."""
    command, pid = str(holder.get("command") or ""), holder.get("pid")
    lines = [f"agent_server.py: 127.0.0.1:{port} 포트를 다른 서버가 이미 쓰고 있어 켜지 못했습니다.",
             f"  쓰고 있는 프로세스: PID {pid} · {command[:160]}" if pid else "  어느 프로세스인지는 알아내지 못했습니다(`ss -ltnp | grep :8765`로 볼 수 있습니다)."]
    if "agent_server.py" in command:
        lines.append("  이미 이 서버(agent_server.py)가 켜져 있습니다. 그대로 쓰시면 됩니다.")
        return "\n".join(lines)
    if "dashboard_server.py" in command:
        lines.append("  그 서버는 계획용으로 잠긴 서버입니다: 무한 step과 샌드박스 컴퓨터가 없습니다.")
    stop = f"그 서버를 켠 터미널에서 Ctrl+C, 또는 `kill {pid}`" if pid else "그 서버를 켠 터미널에서 Ctrl+C"
    lines.append(f"  그 서버를 끈 뒤({stop}) 이 명령을 다시 실행해 주세요. 거기서 실행 중인 작업이 있으면 먼저 끝내거나 중지하세요.")
    return "\n".join(lines)


OUTPUT_KEY = "agent_output_tokens"  # of the store's manifest: what one step may generate, as last chosen on the page


def output_said() -> dict:
    """What a step of the next task may generate (the worker this server starts reads ARGUS_MAX_NEW_TOKENS from the
    server's own environment), the sizes offered, and the plan's own."""
    return {"value": FREE.output_tokens(), "choices": list(FREE.OUTPUT_TOKENS), "plan": FREE.PLAN_OUTPUT_TOKENS}


def keep_output_tokens(DS, value) -> tuple[int, dict]:
    """POST /api/agent/output-tokens {"tokens"}: from the next task on (a task that runs keeps what it started with),
    and kept in the store for the next start."""
    if isinstance(value, bool) or not isinstance(value, int) or value not in FREE.OUTPUT_TOKENS:
        return 400, {"error": "출력 토큰은 " + ", ".join(f"{count:,}" for count in FREE.OUTPUT_TOKENS) + " 중 하나여야 합니다."}
    os.environ["ARGUS_MAX_NEW_TOKENS"] = str(value)
    with DS.STORE.lock:
        raw, save = BOXES._raw(DS.STORE)
        raw[OUTPUT_KEY] = value
        save(raw)
    DS.STORE.audit("output_tokens", "local", tokens=value)
    return 200, output_said()


def restore_output_tokens(DS) -> int:
    """At the start: what the command was given in ARGUS_MAX_NEW_TOKENS stays; else the store's last choice; else the
    default (live_agent_free.OUTPUT_DEFAULT)."""
    if not str(os.environ.get("ARGUS_MAX_NEW_TOKENS") or "").strip():
        with DS.STORE.lock:
            raw, _save = BOXES._raw(DS.STORE)
        kept = raw.get(OUTPUT_KEY)
        if isinstance(kept, int) and not isinstance(kept, bool) and kept in FREE.OUTPUT_TOKENS:
            os.environ["ARGUS_MAX_NEW_TOKENS"] = str(kept)
    return FREE.output_tokens()


def boxes_said(DS) -> list[dict]:
    """The sandboxes that are there, as the page lists them (which one is the agent's among them)."""
    mine = BOXES.agent(DS)
    known = BOXES.every(Path(DS.SANDBOX_SCRIPT).parent.parent)
    known.setdefault(mine.name, mine)
    return [{**box.said(), "agent": box.root == mine.root} for box in known.values()]


def use_sandbox(DS, root: Path, patch=setattr, environ=None) -> None:
    """Have this server, and the worker it starts, use the sandbox in ``root`` (its sandbox.py, its snapshots, its
    ledger). Nothing is run: see sandbox_boxes.switch for changing it between turns."""
    folder = Path(root)
    name = next((name for name, known in BOXES.FOLDERS.items() if known == folder.name), folder.name)
    BOXES.select(DS, BOXES.Box(name, folder), patch=patch, environ=environ)


def choose(DS, name) -> tuple[int, dict]:
    """POST /api/sandbox/agent {sandbox}: the sandbox the agent works in from its next turn on. Not while a task runs
    or a command of the user's runs: the memory folder is moved with it (sandbox_boxes.switch)."""
    with DS._START_LOCK:
        if DS.LIVE.status().get("busy"):
            return 409, {"error": "에이전트 작업이 실행 중입니다. 끝나거나 중지한 뒤 바꿔 주세요.", "code": "busy"}
        with DS.JOBS_LOCK:
            if any(job["process"].poll() is None and job.get("kind") == "agent" for job in DS.JOBS.values()):
                return 409, {"error": "기존 에이전트 실행이 샌드박스를 쓰고 있습니다. 끝난 뒤 바꿔 주세요.", "code": "busy"}
        if not SHELL.settled(4.0):
            return 409, SHELL_BUSY
        try:
            done = BOXES.switch(DS, name)
        except ValueError as error:
            return 400, {"error": str(error)}
        except Exception as error:
            return 500, {"error": f"{type(error).__name__}: {str(error)[:200]}"}
    return 200, {**done, "sandboxes": boxes_said(DS)}


def origins_line(allowed, site: str | None) -> str:
    """Which pages this server answers, said when it starts: a copy of the page hosted elsewhere (a Sites page) is
    answered only when its address was given in ARGUS_SITE_ORIGIN (the locked server's own rule, the same here)."""
    elsewhere = sorted(origin for origin in allowed if "127.0.0.1" not in origin and "localhost" not in origin)
    line = "붙을 수 있는 페이지: 이 컴퓨터의 로컬 페이지" + "".join(f", {origin}" for origin in elsewhere)
    if not site:
        line += ("\n  다른 곳에 올린 사본(GPT Sites 등)에서 붙으려면 그 주소를 주고 켜세요: "
                 "ARGUS_SITE_ORIGIN=https://<사이트 주소> .venv/bin/python argus_hook/agent_server.py"
                 "\n  (그런 사본에서는 채팅만 됩니다: 무한 step과 샌드박스 컴퓨터는 로컬 페이지에서만)")
    return line


def main() -> int:
    if os.environ.get("ARGUS_LIVE_MEMORY_DIR"):
        print("agent_server.py: ARGUS_LIVE_MEMORY_DIR가 설정돼 있습니다(계획 실행용 기억 폴더). 계획 실행은 잠긴 서버 "
              "argus_hook/dashboard_server.py로 하세요. 무한 step 서버는 평소 기억 폴더에서만 켭니다.", file=sys.stderr)
        return 2
    holder = port_holder()
    if holder:  # said before anything is called "on": the server cannot start
        print(port_message(holder), file=sys.stderr)
        return 1
    asked, rest = None, []  # --sandbox plain|pc|net (or --plain): the agent's sandbox for this start
    arguments = iter(sys.argv[1:])
    for argument in arguments:
        if argument == "--plain":
            asked = "plain"
        elif argument == "--sandbox":
            asked = next(arguments, None)
        elif argument.startswith("--sandbox="):
            asked = argument.split("=", 1)[1]
        else:
            rest.append(argument)
    sys.argv = [sys.argv[0], *rest]
    known = BOXES.every()
    if asked is not None and asked not in known:  # (said before anything is called "on")
        print(f"agent_server.py: 모르는 샌드박스입니다: {asked} (있는 것: {', '.join(known)})", file=sys.stderr)
        return 3
    import dashboard_server as DS

    enable(DS)
    print("무한 step: 켬(로컬 페이지의 step 상자에서 '무한' · 작업 프로세스 argus_hook/live_agent_free.py)")
    print("샌드박스 컴퓨터: 켬(로컬 페이지의 '샌드박스 컴퓨터' 탭 · 터미널, 파일, 편집기, 시스템)")
    adopted = None if BOXES.chosen(DS) else BOXES.adopt(DS)  # a store with one ledger: whose it was (once)
    kept = BOXES.chosen(DS) or "plain"  # whose ledger and memory folder the store was left with
    wanted = asked or BOXES.chosen(DS) or ("pc" if "pc" in known else "plain")
    if adopted not in (None, "plain"):
        print(f"  참고: 저장소의 샌드박스 기록(되돌릴 지점 등)은 {known[adopted].root.name}에서 쓰던 것이라 그 샌드박스의 것으로 옮겨 적었습니다")
    BOXES.select(DS, known.get(kept) or known["plain"])
    try:
        if wanted != BOXES.agent(DS).name:
            moved = BOXES.switch(DS, wanted)  # (its memory folder is moved with it: see sandbox_boxes.switch)
            for side in ("left", "entered"):
                if moved.get(side):
                    print(f"  참고: 기억 폴더를 비우지 못했습니다({side}): {moved[side]} · 다음 턴이 다시 씁니다")
        elif wanted != "plain":
            up = DS.run_sandbox_cli(["up"], timeout=300)
            if up.get("status") != "RUNNING":
                raise ValueError(f"'{wanted}' 샌드박스를 켜지 못했습니다: {str(up.get('reason') or up)[-300:]}")
    except ValueError as error:
        print(f"agent_server.py: {error}\n"
              "  이미지를 아직 만들지 않았다면: python3.11 SANDBOX_PC/sandbox.py build (SANDBOX_NET은 그다음에 같은 식으로)\n"
              "  화면 없는 기존 샌드박스로 켜려면: .venv/bin/python argus_hook/agent_server.py --plain", file=sys.stderr)
        return 3
    mine = BOXES.agent(DS)
    print(f"에이전트가 쓰는 샌드박스: {mine.label}({mine.root.name}) · {mine.about}")
    print(f"출력 토큰: 한 step에 {restore_output_tokens(DS):,} · 페이지의 '출력 토큰'에서 바꿉니다(계획 기준 {FREE.PLAN_OUTPUT_TOKENS:,})")
    print("  있는 샌드박스: " + " / ".join(f"{box.label}({box.root.name})" for box in known.values())
          + " · 페이지에서 바꿀 수 있습니다(에이전트 채팅의 '샌드박스', 샌드박스 컴퓨터의 '보는 샌드박스')")
    print(origins_line(DS.ALLOWED_ORIGINS, os.environ.get("ARGUS_SITE_ORIGIN")))
    DS.main()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

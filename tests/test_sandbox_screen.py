"""The real screen of the "computer" sandbox (argus_hook/sandbox_screen.py) and the choice of the sandbox folder
(agent_server.use_sandbox, live_agent_free.use_sandbox). No Docker here: the sandbox's desk.py is a small script of
this test's (pictures that are a few bytes, events written to a file). What the real desk.py does in the real
container was looked at by hand when it was built (reports/live-agent/v1.7.md, A17)."""

import json
import sys
import threading
import time
from http.server import ThreadingHTTPServer
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / "argus_hook"), str(ROOT / "tests")]
import agent_server as SERVER  # noqa: E402
import live_agent_free as FREE  # noqa: E402
import sandbox_boxes as BOXES  # noqa: E402
import sandbox_screen as SCREEN  # noqa: E402
import sandbox_shell as SHELL  # noqa: E402
from fake_sandbox_box import FakeBox  # noqa: E402

FAKE_DESK = '''
import json, sys, time
from pathlib import Path
here = Path(__file__).resolve().parent
on, action = here / "screen.on", sys.argv[1]
if action == "screen-start":
    if (here / "sandbox.off").exists():
        print(json.dumps({"status": "ERROR", "reason": "sandbox is not running; run up first"}), file=sys.stderr); sys.exit(2)
    on.write_text(f"{sys.argv[2]}x{sys.argv[3]}"); print(json.dumps({"status": "READY", "size": on.read_text()}))
elif action == "screen-stop":
    on.unlink(missing_ok=True); print(json.dumps({"status": "STOPPED"}))
elif action == "screen-state":
    print(json.dumps({"status": "ON", "size": on.read_text()} if on.exists() else {"status": "OFF", "size": None}))
elif action == "screen-stream":
    if not on.exists():
        sys.exit(3)  # no display: nothing is written
    (here / "stream.args").write_text(" ".join(sys.argv[2:]))
    out, number = sys.stdout.buffer, 0
    while True:
        data = b"\\xff\\xd8picture %d\\xff\\xd9" % number
        out.write(b"--argusframe\\r\\nContent-Type: image/jpeg\\r\\nContent-Length: %d\\r\\n\\r\\n" % len(data) + data + b"\\r\\n")
        out.flush(); number += 1; time.sleep(0.05)
elif action == "screen-input":
    with open(here / "input.log", "a") as log:
        for line in sys.stdin:
            log.write(line); log.flush()
        log.write("END\\n")
'''


def call(api: str, path: str, body: dict | None = None, headers: dict | None = None):
    request = Request(api + path, data=None if body is None else json.dumps(body).encode("utf-8"),
                      headers={"Content-Type": "application/json", **(headers or {})}, method="GET" if body is None else "POST")
    try:
        with urlopen(request, timeout=30) as response:
            return response.status, json.loads(response.read().decode("utf-8"))
    except HTTPError as error:
        return error.code, json.loads(error.read().decode("utf-8"))


@pytest.fixture
def server(tmp_path, monkeypatch):
    import dashboard_server as DS

    root = tmp_path / "SANDBOX_PC"
    root.mkdir()
    (root / "settings.json").write_text(json.dumps({"network": "allowlist", "cpus": 4.0, "memory": "6g"}))
    box = FakeBox(root)
    monkeypatch.setattr(DS, "runtime_status", lambda: {})
    monkeypatch.setattr(DS, "run_sandbox_cli", box.cli)
    SERVER.enable(DS, patch=monkeypatch.setattr)
    env = {}
    SERVER.use_sandbox(DS, root, patch=monkeypatch.setattr, environ=env)
    monkeypatch.setattr(DS.LIVE, "status", lambda: {"busy": False})
    monkeypatch.setattr(SCREEN, "STATE", {"input": {}, "streams": 0})
    DS.configure_for_tests(tmp_path / "memory")
    httpd = ThreadingHTTPServer(("127.0.0.1", 0), DS.Handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    try:
        yield {"api": f"http://127.0.0.1:{httpd.server_address[1]}", "root": root, "DS": DS, "box": box, "env": env}
    finally:
        SCREEN.close_input()
        httpd.shutdown()
        httpd.server_close()


def test_only_what_is_an_event_reaches_the_sandbox():
    taken = SCREEN.clean([
        {"t": "k", "key": "ArrowUp", "down": True}, {"t": "k", "key": "KeyA", "down": 0}, {"t": "k", "key": "a; rm -rf /", "down": True},
        {"t": "k", "key": 7, "down": True}, {"t": "m", "x": 512.7, "y": "300"}, {"t": "m", "x": -5, "y": 99_999}, {"t": "m", "x": "left"},
        {"t": "b", "button": 1, "down": True}, {"t": "b", "button": 9, "down": True}, {"t": "w", "dy": -120}, {"t": "w", "dy": 0},
        {"t": "exec", "command": "ls"}, "k", None, {"t": "k", "key": "Enter", "down": True, "extra": {"anything": "else"}}])
    assert taken == [{"t": "k", "key": "ArrowUp", "down": True}, {"t": "k", "key": "KeyA", "down": False}, {"t": "m", "x": 512, "y": 300},
                     {"t": "m", "x": 0, "y": 8191}, {"t": "b", "button": 1, "down": True}, {"t": "w", "dy": -1},
                     {"t": "k", "key": "Enter", "down": True}]
    assert SCREEN.clean("not a list") == [] and len(SCREEN.clean([{"t": "m", "x": 1, "y": 1}] * 1000)) == SCREEN.EVENTS


def test_a_sandbox_without_a_display_has_no_screen(server):
    api, DS = server["api"], server["DS"]
    assert SCREEN.available(BOXES.agent(DS)) is False and DS.runtime_status()["sandbox_screen"] is False
    assert DS.runtime_status()["sandbox_folder"] == "SANDBOX_PC"
    for path, body in (("/api/sandbox/screen", None), ("/api/sandbox/screen/stream", None), ("/api/sandbox/screen/start", {}),
                       ("/api/sandbox/screen/stop", {}), ("/api/sandbox/screen/input", {"events": [{"t": "w", "dy": 1}]})):
        status, out = call(api, path, body)
        assert status == 404 and out["code"] == "no_screen", path


def test_the_screen_is_started_shown_typed_into_and_stopped(server):
    api, root, DS = server["api"], server["root"], server["DS"]
    (root / "desk.py").write_text(FAKE_DESK)
    assert DS.runtime_status()["sandbox_screen"] is True
    assert call(api, "/api/sandbox/screen")[1] == {"status": "OFF", "size": None, "sizes": list(SCREEN.SIZES), "sandbox": "pc"}
    assert call(api, "/api/sandbox/screen/stream")[1]["code"] == "screen_off"  # nothing to draw from: said, not left hanging
    assert call(api, "/api/sandbox/screen/start", {"size": "640x480"})[0] == 400  # a size the sandbox is not given
    status, out = call(api, "/api/sandbox/screen/start", {"size": "1280x720"})
    assert status == 200 and out == {"status": "READY", "size": "1280x720"}
    assert call(api, "/api/sandbox/screen")[1]["status"] == "ON"
    # the pictures: one after another, for as long as the page reads
    response = urlopen(Request(api + "/api/sandbox/screen/stream"), timeout=20)
    assert response.headers["Content-Type"] == "multipart/x-mixed-replace; boundary=argusframe" and response.headers["Cache-Control"] == "no-store"
    seen = b""
    while seen.count(b"--argusframe") < 4:
        seen += response.read(64)
    assert b"picture 0" in seen and b"picture 2" in seen and SCREEN.STATE["streams"] == 1
    assert (root / "stream.args").read_text() == "--fps 12 --quality 72"
    response.close()  # the window is closed: the stream's process goes with it
    for _ in range(60):
        if SCREEN.STATE["streams"] == 0:
            break
        time.sleep(0.05)
    assert SCREEN.STATE["streams"] == 0
    # the keyboard and the mouse: down the one input.py that is kept open
    events = [{"t": "m", "x": 100, "y": 50}, {"t": "b", "button": 1, "down": True}, {"t": "b", "button": 1, "down": False},
              {"t": "k", "key": "ArrowUp", "down": True}, {"t": "k", "key": "$(reboot)", "down": True}]
    assert call(api, "/api/sandbox/screen/input", {"events": events})[1] == {"taken": 4}
    assert call(api, "/api/sandbox/screen/input", {"events": [{"t": "k", "key": "ArrowUp", "down": False}]})[1] == {"taken": 1}
    assert call(api, "/api/sandbox/screen/input", {"events": []})[1] == {"taken": 0}
    first = SCREEN.STATE["input"]["pc"]
    for _ in range(60):
        if (root / "input.log").exists() and (root / "input.log").read_text().count("\n") >= 5:
            break
        time.sleep(0.05)
    lines = [json.loads(line) for line in (root / "input.log").read_text().splitlines()]
    assert lines == [*events[:4], {"t": "k", "key": "ArrowUp", "down": False}] and SCREEN.STATE["input"]["pc"] is first  # one process, in order
    status, out = call(api, "/api/sandbox/screen/stop", {})
    assert status == 200 and out["status"] == "STOPPED" and SCREEN.STATE["input"] == {}
    assert (root / "input.log").read_text().endswith("END\n")  # its stdin was closed: input.py lets go of what is held
    assert call(api, "/api/sandbox/screen")[1]["status"] == "OFF"
    rows = [row for row in DS.STORE.audit_tail(10) if row["action"] == "screen"]
    assert [row["what"] for row in rows] == ["start", "stop"]


def test_starting_the_screen_starts_a_sandbox_that_was_off(server):
    api, root, box = server["api"], server["root"], server["box"]
    (root / "desk.py").write_text(FAKE_DESK)
    (root / "sandbox.off").write_text("")
    box.running = False
    real_cli = box.cli

    def cli(args, timeout=300):  # `up` brings it back
        if args[0] == "up":
            (root / "sandbox.off").unlink()
        return real_cli(args, timeout)

    server["DS"].run_sandbox_cli = cli
    status, out = call(api, "/api/sandbox/screen/start", {})
    assert status == 200 and out == {"status": "READY", "size": "1024x640"} and box.running is True
    (root / "sandbox.off").write_text("")
    server["DS"].run_sandbox_cli = lambda args, timeout=300: {"status": "ERROR", "reason": "image not found"}
    status, out = call(api, "/api/sandbox/screen/start", {})
    assert out["status"] == "ERROR" and out["sandbox_off"] is True and out["reason"] == "샌드박스가 꺼져 있습니다."


def test_the_screen_is_this_computers_local_page_only(server):
    api, root = server["api"], server["root"]
    (root / "desk.py").write_text(FAKE_DESK)
    call(api, "/api/sandbox/screen/start", {})
    for headers in ({"Origin": "https://ljg5489.github.io"}, {"Origin": "https://evil.example"}, {"Host": "evil.example:8765"},
                    {"Sec-Fetch-Site": "cross-site"}):  # (the last: another site's <img> of the stream)
        assert call(api, "/api/sandbox/screen", None, headers)[0] == 403, headers
        assert call(api, "/api/sandbox/screen/stream", None, headers)[0] == 403, headers
        if "Sec-Fetch-Site" not in headers:
            for path in ("/api/sandbox/screen/start", "/api/sandbox/screen/stop", "/api/sandbox/screen/input"):
                assert call(api, path, {"events": [{"t": "w", "dy": 1}]}, headers)[0] == 403, (path, headers)
    assert not (root / "input.log").exists() and (root / "screen.on").exists()  # nothing of it reached the sandbox


def test_the_server_and_its_worker_use_the_folder_they_are_given(server, tmp_path):
    import agent_loop
    import live_agent as LA

    DS, root, env = server["DS"], server["root"], server["env"]
    assert DS.SANDBOX_SCRIPT == root / "sandbox.py" and DS.SNAPSHOTS == root / "snapshots"
    assert env == {"ARGUS_SANDBOX_SCRIPT": str(root / "sandbox.py")}  # what the worker is told
    assert SHELL.describe(DS, BOXES.agent(DS))["network"] == "allowlist"  # the folder's own settings
    # the sandbox keeps its own network: it is started, never turned to fakenet
    asked = []
    client = agent_loop.RealSandboxClient(str(root / "sandbox.py"))
    client._cli = lambda *args: asked.append(args) or {"status": "RUNNING" if args[0] == "up" else "STOPPED"}
    assert client.ensure_running() == {"status": "RUNNING"} and asked == [("status",), ("up",)]
    assert agent_loop.RealSandboxClient.ensure_running is FREE.ensure_running
    # the worker's side (live_agent_free.use_sandbox): put back by hand, it changes the module itself
    kept = (LA.SANDBOX_SCRIPT, LA.Sandbox.__init__.__defaults__, agent_loop.RealSandboxClient.ensure_running)
    try:
        FREE.use_sandbox(LA, root / "sandbox.py")
        assert LA.SANDBOX_SCRIPT == root / "sandbox.py" and LA.Sandbox().script == root / "sandbox.py"
        assert LA.Sandbox().network() == "allowlist"
        from argus_v.agent_actions import fakenet_pages, system_prompt_for

        prompt = system_prompt_for(LA.Sandbox().network(), pages=fakenet_pages(LA.SANDBOX_SCRIPT.parent))
        assert "fakenet" not in prompt  # no pages of a fake internet are promised to the agent there
        assert "in the background" in FREE.SCREEN_PROMPT and "pip install --user" in FREE.PYPI_PROMPT
    finally:
        LA.SANDBOX_SCRIPT, LA.Sandbox.__init__.__defaults__, agent_loop.RealSandboxClient.ensure_running = kept
    assert LA.Sandbox().script == ROOT / "SANDBOX" / "sandbox.py"  # the locked worker's own default, as it was


def test_the_worker_the_server_starts_is_told_the_same_folder(server, tmp_path):
    """2026-11-23, asked by the user: "에이전트 채팅도 SANDBOX_PC에 연결된거 맞나?" The chat's worker is another
    process: it has the folder from the environment the server gives every worker it starts (live_env), and sets
    itself up with it before the model is loaded (live_agent_free.prepare)."""
    import subprocess

    DS, root, env = server["DS"], server["root"], server["env"]
    (root / "sandbox.py").write_text("# stands for the folder's own sandbox.py\n")
    (root / "desk.py").write_text(FAKE_DESK)
    given = {**DS.live_env(), **env}  # (this test's use_sandbox wrote into `env`; the real one writes into os.environ)
    assert given["ARGUS_SANDBOX_SCRIPT"] == str(root / "sandbox.py")
    probe = ("import live_agent_free as F; runtime = F.prepare(); import live_agent as LA, agent_loop; "
             "print(LA.Sandbox().script); print(LA.SANDBOX_SCRIPT); print(runtime.has_screen); "
             "print(agent_loop.RealSandboxClient.ensure_running is F.ensure_running); print(LA.MAX_STEPS)")
    worker = subprocess.run([sys.executable, "-c", probe], capture_output=True, text=True, timeout=120, env=given, cwd=ROOT / "argus_hook")
    assert worker.returncode == 0, worker.stderr[-600:]
    assert worker.stdout.split() == [str(root / "sandbox.py"), str(root / "sandbox.py"), "True", "True", str(FREE.UNLIMITED)]
    plain = {key: value for key, value in given.items() if key != "ARGUS_SANDBOX_SCRIPT"}  # --plain: nothing is named
    worker = subprocess.run([sys.executable, "-c", probe], capture_output=True, text=True, timeout=120, env=plain, cwd=ROOT / "argus_hook")
    assert worker.stdout.split() == [str(ROOT / "SANDBOX" / "sandbox.py")] * 2 + ["False", "False", str(FREE.UNLIMITED)]


def test_the_computer_folder_runs_the_locked_script_on_itself():
    """SANDBOX_PC/sandbox.py: the locked SANDBOX/sandbox.py, with another folder and another image (`render` only
    writes the compose file it would use: nothing is started)."""
    import subprocess

    pc = ROOT / "SANDBOX_PC"
    if not (pc / "sandbox.py").is_file():
        pytest.skip("no SANDBOX_PC here")
    done = subprocess.run(["python3.11", str(pc / "sandbox.py"), "render"], capture_output=True, text=True, timeout=60)
    spec = json.loads(done.stdout)
    box = spec["services"]["sandbox"]
    assert {service["image"] for service in spec["services"].values()} == {"local/argus-pc:desktop"}
    assert box["build"]["context"] == str(pc) and box["environment"]["DISPLAY"] == ":1"
    assert box["user"] == "10001:10001" and box["read_only"] is True and box["cap_drop"] == ["ALL"] and "ports" not in box
    assert spec["services"]["proxy"]["environment"]["ALLOWED_HOSTS"] == "pypi.org,files.pythonhosted.org"
    locked = json.loads(subprocess.run(["python3.11", str(ROOT / "SANDBOX" / "sandbox.py"), "render"], capture_output=True, text=True,
                                       timeout=60).stdout)
    assert {service["image"] for service in locked["services"].values()} == {"local/generic-sandbox:python"}  # the plan's: untouched
    assert "DISPLAY" not in locked["services"]["sandbox"]["environment"]

"""The sandbox computer (argus_hook/sandbox_shell.py, served by argus_hook/agent_server.py): the user's own terminal,
file manager, editor and system window over the agent's sandbox. No sandbox and no Docker here: sandbox.py's answers
come from a dict (tests/fake_sandbox_box.py; the locked server's run_sandbox_cli is replaced), and the two scripts
that would run in the sandbox (the terminal's wrapper, the fixed change script) are tried in a temporary folder."""

import hashlib
import json
import subprocess
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
import sandbox_shell as SHELL  # noqa: E402
from fake_sandbox_box import PNG, FakeBox  # noqa: E402


# ---------------------------------------------------------------------------- the script a command line runs as
def bash(command: str, cwd: Path):
    token = "__ARGUS_CWD_test__"
    done = subprocess.run(["bash", "-c", SHELL.wrap(command, str(cwd), token)], capture_output=True, text=True, timeout=20)
    stderr, ended = SHELL.unwrap(done.stderr, token, str(cwd))
    return done.returncode, done.stdout, stderr, ended


def test_a_command_starts_where_the_last_ended_and_says_where_it_ends(tmp_path):
    (tmp_path / "sub dir").mkdir()
    code, out, err, ended = bash("pwd; cd 'sub dir'; echo here", tmp_path)
    assert code == 0 and out.splitlines() == [str(tmp_path), "here"] and err == "" and ended == str(tmp_path / "sub dir")
    code, out, err, ended = bash("pwd", tmp_path / "sub dir")  # the next command: in that folder
    assert out.strip() == str(tmp_path / "sub dir") and ended == str(tmp_path / "sub dir")
    code, out, err, ended = bash("echo oops >&2; cd /; exit 3", tmp_path)  # its exit code and its stderr are its own
    assert code == 3 and err == "oops\n" and ended == "/"
    code, out, err, ended = bash("echo 'unclosed", tmp_path)  # a syntax error: said, the folder stays
    assert code != 0 and err.strip() and ended == str(tmp_path)  # (bash's own words, in the machine's language)


def test_a_folder_that_is_gone_falls_back_to_the_workspace_line(tmp_path):
    script = SHELL.wrap("true", str(tmp_path / "gone"), "T")
    assert script.startswith(f"cd -- {tmp_path / 'gone'} 2>/dev/null || cd /workspace\n")
    assert SHELL.unwrap("no mark here", "T", "/old") == ("no mark here", "/old")  # killed before it could say: the old one
    assert SHELL.unwrap("x\n\nT/tmp\n", "T", "/old") == ("x\n", "/tmp")
    assert SHELL.unwrap("\nTnot-a-path\n", "T", "/old")[1] == "/old"


def test_words_a_person_types_that_the_sandbox_does_not_have(tmp_path):
    """2026-11-23: the first commands typed into the real terminal were `tree` (twice) and both ended "command not found".
    The sandbox image holds bash, coreutils, curl, git, procps, tar and python: the rest is defined for the one command
    line, nothing is written into the sandbox."""
    import shutil

    project = tmp_path / "proj"
    (project / "src" / "deep").mkdir(parents=True)
    (project / "a.txt").write_text("x\n")
    (project / "src" / "main.py").write_text("y")
    (project / ".hidden").write_text("z")
    tools = tmp_path / "bin"  # a PATH with python and ls, and no tree, vim, less or sudo (as in the sandbox)
    tools.mkdir()
    for name in ("python3", "ls", "cat", "head"):
        (tools / name).symlink_to(shutil.which(name))

    def run(line):
        done = subprocess.run([shutil.which("bash"), "-c", SHELL.wrap(line, str(project), "TOK")], capture_output=True, text=True,
                              timeout=20, env={"PATH": str(tools), "LC_ALL": "C.UTF-8"})
        stderr, ended = SHELL.unwrap(done.stderr, "TOK", "?")
        return done.returncode, done.stdout, stderr, ended

    code, out, err, ended = run("tree")
    assert code == 0 and err == "" and ended == str(project)
    assert out == ".\n├── a.txt\n└── src\n    ├── deep\n    └── main.py\n\n2 directories, 2 files\n"
    assert run("tree -a -L 1")[1] == ".\n├── .hidden\n├── a.txt\n└── src\n\n1 directories, 2 files\n"
    assert run("tree -d src")[1] == "src\n└── deep\n\n1 directories\n"
    assert run("tree | head -2")[1] == ".\n├── a.txt\n"  # in a pipe as well
    assert "a.txt" in run("ll")[1] and ".hidden" in run("la")[1] and run("less a.txt")[1] == "x\n"
    code, out, err, ended = run("vim a.txt")
    assert code == 1 and "화면을 쓰는 프로그램(vim)을 띄우지 못합니다" in err and "편집기 창" in err
    assert "화면을 쓰는 프로그램(top)" in run("top")[2]
    code, out, err, ended = run("sudo ls")
    assert code == 1 and "관리자 권한(sudo)이 없습니다" in err and out == ""
    code, out, err, ended = run("lf")  # a word nobody defines: bash's own "command not found"
    assert code == 127 and "lf" in err
    assert "'" not in SHELL.TREE and len(SHELL.wrap("ls", "/workspace", "T")) < 4_000  # one shell word; a small wrapper
    (tools / "tree").write_text("#!/bin/sh\necho the real one\n")
    (tools / "tree").chmod(0o755)
    assert run("tree")[1] == "the real one\n"  # a sandbox that has the program runs the program


def test_what_is_refused_before_anything_runs():
    assert SHELL.checked({"command": "ls -la", "cwd": "/workspace/a", "timeout": 120}) == ("ls -la", "/workspace/a", 120)
    assert SHELL.checked({"command": "ls"})[1:] == ("/workspace", 120)
    assert SHELL.checked({"command": "ls", "cwd": "relative\npath"})[1] == "/workspace"
    for body, word in (({"command": "  "}, "입력해"), ({"command": "x" * 8001}, "8,000자"), ({"command": "ls", "timeout": 9999}, "시간 한도"),
                       ({"command": "curl http://fakenet/argus/page1.html"}, "봉인된 시험 페이지"),
                       ({"command": "wget -q fakenet:8080//argus/x -O y"}, "봉인된 시험 페이지")):
        with pytest.raises(ValueError, match=word):
            SHELL.checked(body)
    import live_agent as LA

    assert SHELL.ARGUS_PAGES.pattern == LA.ARGUS_PAGES.pattern and SHELL.ARGUS_PAGES.flags == LA.ARGUS_PAGES.flags
    assert SHELL.TAIL == LA.SANDBOX_TAIL and SHELL.TIMEOUT == LA.COMMAND_TIMEOUT


def test_the_file_manager_names_only_what_is_in_the_workspace():
    for path in ("/workspace/a", "/workspace/a b/c.txt", "/workspace/.agent/AGENTS.md", "/workspace/-rf", "/workspace/한글 파일.txt"):
        assert SHELL.inside(path) == path
    for path in ("/workspace", "/workspace/", "/etc/passwd", "/workspace/../etc/passwd", "/workspace/a/./b", "/workspace//a",
                 "/workspacex/a", "workspace/a", "/workspace/a\nb", "/workspace/a\x00", "/workspace/" + "x" * 1100, None, 7):
        with pytest.raises(ValueError):
            SHELL.inside(path)


# ---------------------------------------------------------------------------- the fixed change script, in a temporary folder
def op(*argv):
    done = subprocess.run([sys.executable, "-I", "-S", "-c", SHELL.OPS, *map(str, argv)], capture_output=True, text=True, timeout=20)
    assert done.returncode == 0 and done.stderr == ""
    return json.loads(done.stdout)


def test_the_change_script_takes_any_name_as_it_is(tmp_path):
    import base64

    names = ("a b", "it's", 'say "hi"', "-rf", "$(touch pwned)", "한글 폴더", "semi;colon", "star*")
    for name in names:  # an argument, never a shell: nothing in a name is a command
        assert op("mkdir", tmp_path / name) == {"ok": True} and (tmp_path / name).is_dir()
    assert sorted(path.name for path in tmp_path.iterdir()) == sorted(names) and not (tmp_path / "pwned").exists()
    assert op("mkdir", tmp_path / "a b") == {"ok": False, "code": "exists"}
    assert op("mkdir", tmp_path / "no" / "parent") == {"ok": False, "code": "missing"}
    note = tmp_path / "a b" / "note.txt"
    assert op("touch", note) == {"ok": True} and note.read_bytes() == b""
    assert op("touch", note) == {"ok": False, "code": "exists"}  # a new file never empties one that is there
    text = "첫 줄\nsecond 'line' \"quoted\" $HOME `x`\n"
    assert op("save", note, base64.b64encode(text.encode()).decode()) == {"ok": True} and note.read_text(encoding="utf-8") == text
    note.chmod(0o755)
    assert op("save", note, base64.b64encode(b"#!/bin/sh\n").decode()) == {"ok": True}
    assert note.read_bytes() == b"#!/bin/sh\n" and note.stat().st_mode & 0o777 == 0o755  # the file's mode stays
    assert op("save", tmp_path / "a b", "") == {"ok": False, "code": "kind"}
    assert op("rename", note, tmp_path / "it's" / "moved.txt") == {"ok": True} and not note.exists()
    assert op("rename", tmp_path / "it's" / "moved.txt", tmp_path / "-rf") == {"ok": False, "code": "exists"}  # never onto another
    assert op("rename", tmp_path / "gone", tmp_path / "new") == {"ok": False, "code": "missing"}
    (tmp_path / "link").symlink_to(tmp_path / "it's")
    assert op("delete", tmp_path / "link") == {"ok": True} and (tmp_path / "it's" / "moved.txt").is_file()  # the link, not what it names
    assert op("delete", tmp_path / "it's") == {"ok": True} and not (tmp_path / "it's").exists()  # a folder with what is in it
    assert op("delete", tmp_path / "it's") == {"ok": False, "code": "missing"}
    assert op("kill", 2**22 - 1) == {"ok": False, "code": "missing"}
    assert op("format", tmp_path / "x") == {"ok": False, "code": "op"}


# ---------------------------------------------------------------------------- through the server, a sandbox made of a dict
def call(api: str, path: str, body: dict | None = None, headers: dict | None = None):
    request = Request(api + path, data=None if body is None else json.dumps(body).encode("utf-8"),
                      headers={"Content-Type": "application/json", **(headers or {})}, method="GET" if body is None else "POST")
    try:
        with urlopen(request, timeout=60) as response:
            return response.status, json.loads(response.read().decode("utf-8"))
    except HTTPError as error:
        return error.code, json.loads(error.read().decode("utf-8"))


@pytest.fixture
def server(tmp_path, monkeypatch):
    import dashboard_server as DS

    box = FakeBox(tmp_path / "sandbox")
    (tmp_path / "sandbox").mkdir()
    (tmp_path / "sandbox" / "settings.json").write_text(json.dumps({"network": "fakenet", "cpus": 2.0, "memory": "4g"}))
    monkeypatch.setattr(DS, "runtime_status", lambda: {})
    monkeypatch.setattr(DS, "run_sandbox_cli", box.cli)
    monkeypatch.setattr(DS, "SANDBOX_SCRIPT", tmp_path / "sandbox" / "sandbox.py")
    monkeypatch.setattr(DS, "SNAPSHOTS", tmp_path / "sandbox" / "snapshots")
    monkeypatch.setattr(SHELL, "image_bytes", box.image)
    SERVER.enable(DS, patch=monkeypatch.setattr)
    busy = {"agent": False}
    monkeypatch.setattr(DS.LIVE, "status", lambda: {"busy": busy["agent"]})
    DS.configure_for_tests(tmp_path / "memory")
    httpd = ThreadingHTTPServer(("127.0.0.1", 0), DS.Handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    try:
        yield {"api": f"http://127.0.0.1:{httpd.server_address[1]}", "box": box, "DS": DS, "busy": busy}
    finally:
        httpd.shutdown()
        httpd.server_close()


def runs(box) -> list[list[str]]:
    return [args for args in box.calls if args[0] == "run"]


def test_a_command_runs_in_the_sandbox_and_the_bookkeeping_follows(server):
    DS, box, api = server["DS"], server["box"], server["api"]
    box.dirs.add("/workspace/project")
    box.write("/workspace/project/file1", "x")
    DS.STORE.mark_sandbox(restore_point="before-run-0.tar", restore_turn={"conversation": "c-20261123-0123abcd", "turn": 2, "step": 1})
    status, out = call(api, "/api/sandbox/exec", {"command": "cd project && ls", "cwd": "/workspace", "timeout": 120})
    assert status == 200 and out["status"] == "FINISHED" and out["exit_code"] == 0 and out["stdout"] == "file1\n"
    assert out["cwd"] == "/workspace/project" and out["stderr"] == "" and out["sealed"] is False and out["cut"] == []
    run = runs(box)[0]
    assert run[:5] == ["run", "--timeout", "120", "--", "bash"] and run[5] == "-c" and "cd project && ls" in run[6]
    assert run[6].startswith("cd -- /workspace 2>/dev/null")  # where the page said the last command ended
    state = DS.STORE.sandbox_state()
    assert state["restore_point"] == "before-run-1.tar" and state["restore_turn"] is None  # no turn is taken back past it
    row = DS.STORE.audit_tail(5)[-1]
    assert row["action"] == "shell" and row["chars"] == len("cd project && ls") and "cd project" not in json.dumps(row)  # counts only
    assert DS.runtime_status()["sandbox_shell"] is True
    described = call(api, "/api/sandbox/shell")[1]
    assert described["enabled"] is True and described["home"] == "/workspace" and described["busy"] is False
    assert described["network"] == "fakenet" and described["restore_point"] == "before-run-1.tar" and described["limits"]["memory"] == "4g"
    status, out = call(api, "/api/sandbox/exec", {"command": "echo oops >&2; exit 3", "cwd": "/workspace/project"})
    assert out["exit_code"] == 3 and out["stderr"] == "oops\n" and out["cwd"] == "/workspace/project"


def test_only_this_computers_local_page_may_use_it(server):
    api, box = server["api"], server["box"]
    gets = ("/api/sandbox/shell", "/api/sandbox/files", "/api/sandbox/system")
    posts = {"/api/sandbox/exec": {"command": "ls"}, "/api/sandbox/read": {"path": "/workspace/a"}, "/api/sandbox/processes": {},
             "/api/sandbox/change": {"op": "mkdir", "path": "/workspace/a"}, "/api/sandbox/power": {"action": "on"}}
    for headers in ({"Origin": "https://ljg5489.github.io"},  # an allowed page elsewhere: it may chat, never this
                    {"Origin": "https://evil.example"},        # any other site
                    {"Host": "evil.example:8765"}):            # DNS rebinding
        for path in gets:
            assert call(api, path, None, headers)[0] == 403, (path, headers)
        for path, body in posts.items():
            assert call(api, path, body, headers)[0] == 403, (path, headers)
    for path in gets:  # another site's <img> or <script>: no Origin on such a GET, but the browser says it is cross-site
        assert call(api, path, None, {"Sec-Fetch-Site": "cross-site"})[0] == 403 and call(api, path, None, {"Sec-Fetch-Site": "same-site"})[0] == 403
    assert box.calls == []  # nothing reached the sandbox
    status, out = call(api, "/api/sandbox/exec", {"command": "ls"}, {"Origin": "http://127.0.0.1:8765", "Sec-Fetch-Site": "same-origin"})  # the local page itself
    assert status == 200 and out["status"] == "FINISHED"
    assert call(api, "/api/sandbox/files", None, {"Sec-Fetch-Site": "same-origin"})[0] == 200
    assert call(api, "/api/sandbox/nothing", {})[0] in (404, 501)  # no other address is added


def test_never_while_the_agent_works_and_one_thing_at_a_time(server):
    api, box, DS = server["api"], server["box"], server["DS"]
    box.write("/workspace/a.txt", "text")
    server["busy"]["agent"] = True
    for path, body in (("/api/sandbox/exec", {"command": "ls"}), ("/api/sandbox/change", {"op": "mkdir", "path": "/workspace/d"}),
                       ("/api/sandbox/processes", {}), ("/api/sandbox/power", {"action": "on"})):
        status, out = call(api, path, body)
        assert status == 409 and "에이전트 작업이 실행 중" in out["error"], path
    assert call(api, "/api/sandbox/read", {"path": "/workspace/a.txt"})[0] == 409  # its files are sealed only after its step
    assert runs(box) == [] and "/workspace/d" not in box.dirs
    status, listed = call(api, "/api/sandbox/files")  # the list is still shown: the user watches the agent's files appear
    assert status == 200 and listed["agent_busy"] is True and [entry["path"] for entry in listed["entries"]] == ["/workspace/a.txt"]
    server["busy"]["agent"] = False
    box.delay = 1.0
    results = []
    first = threading.Thread(target=lambda: results.append(call(api, "/api/sandbox/exec", {"command": "echo slow"})))
    first.start()
    time.sleep(0.4)
    assert call(api, "/api/sandbox/exec", {"command": "ls"})[0] == 409  # the one before it still runs
    assert call(api, "/api/sandbox/change", {"op": "mkdir", "path": "/workspace/d"})[0] == 409
    with pytest.raises(ValueError, match="실행 중인 명령이 끝난 뒤"):  # and no agent turn starts into it
        DS.start_live("t", 5, None, True, None)
    assert call(api, "/api/live/sandbox/clear", {})[0] == 409  # nor a clean-up of the sandbox
    assert call(api, "/api/live/sandbox/restore", {})[0] == 409
    assert call(api, "/api/sandbox/files")[1]["shell_busy"] is True
    first.join()
    assert results[0][0] == 200 and not SHELL.busy()


def test_a_low_disk_stops_the_users_commands_as_it_stops_a_turn(server, monkeypatch):
    api, box, DS = server["api"], server["box"], server["DS"]
    monkeypatch.setattr(DS, "disk_free", lambda: 3 * 2**30)
    status, out = call(api, "/api/sandbox/exec", {"command": "ls"})
    assert status == 409 and "디스크 여유가 3.0 GB" in out["error"] and runs(box) == []
    assert call(api, "/api/sandbox/files")[0] == 200  # reading leaves no snapshot


def test_a_sandbox_that_was_off_is_started_and_a_blocked_one_is_said(server):
    api, box, DS = server["api"], server["box"], server["DS"]
    box.running = False
    status, out = call(api, "/api/sandbox/exec", {"command": "echo hi"})
    assert status == 200 and out["status"] == "FINISHED" and out["restarted"] is True and out["stdout"] == "hi\n"
    assert [args[0] for args in box.calls[:3]] == ["run", "up", "run"]
    box.refuse = "archive contains unsupported paths, links or special files"
    status, out = call(api, "/api/sandbox/exec", {"command": "ls"})
    assert status == 200 and out["status"] == "ERROR" and out["blocked"] == "links" and "링크" in out["blocked_text"]
    assert DS.STORE.sandbox_state()["blocked"] == "links" and call(api, "/api/sandbox/shell")[1]["blocked"] == "links"
    status, out = call(api, "/api/sandbox/change", {"op": "mkdir", "path": "/workspace/d"})
    assert out["ok"] is False and out["blocked"] == "links" and "링크" in out["error"]
    box.refuse = None
    status, out = call(api, "/api/sandbox/exec", {"command": "sleep 999", "timeout": 30})
    assert out["status"] == "TIMEOUT" and out["environment_stopped"] is True and out["exit_code"] is None
    assert DS.STORE.sandbox_state()["blocked"] is None  # a command ran again: no longer blocked
    box.locked = True  # sandbox.py's own lock held by something else
    status, out = call(api, "/api/sandbox/exec", {"command": "ls"})
    assert out["status"] == "ERROR" and "다른 작업을 하는 중" in out["reason"] and out["blocked"] is None
    box.locked = False
    box.refuse_once = "snapshot failed; workspace was not changed"  # a file changed under tar: tried once more, as the worker does
    before = len(runs(box))
    status, out = call(api, "/api/sandbox/exec", {"command": "echo again"})
    assert out["status"] == "FINISHED" and out["stdout"] == "again\n" and out["blocked"] is None
    assert len(runs(box)) == before + 3 and out["restarted"] is True  # off since the time-out: started, then the snapshot once more
    assert DS.STORE.sandbox_state()["blocked"] is None
    box.refuse = "snapshot failed; workspace was not changed"  # still failing: blocked, and said
    status, out = call(api, "/api/sandbox/exec", {"command": "echo again"})
    assert out["status"] == "ERROR" and out["blocked"] == "busy" and DS.STORE.sandbox_state()["blocked"] == "busy"


def test_a_long_output_is_read_from_the_runs_own_log(server):
    api, box = server["api"], server["box"]
    status, out = call(api, "/api/sandbox/exec", {"command": "big 5000"})  # 60,000 bytes: more than the report's 32,768
    assert status == 200 and out["stdout"].startswith("line 000000\n") and out["stdout"].endswith("line 004999\n") and out["cut"] == []
    status, out = call(api, "/api/sandbox/exec", {"command": "big 30000"})  # 360,000 bytes: the last 262,144 of them
    assert len(out["stdout"].encode()) == SHELL.SHOWN and out["stdout"].endswith("line 029999\n")
    assert out["cut"] == [{"stream": "stdout", "shown": SHELL.SHOWN, "bytes": 360_000}]
    box.report = {"logs": "/etc"}  # a log folder that is not sandbox.py's: its report's tail only
    status, out = call(api, "/api/sandbox/exec", {"command": "big 5000"})
    assert len(out["stdout"].encode()) == SHELL.TAIL and out["cut"] == [{"stream": "stdout", "shown": SHELL.TAIL, "bytes": 60_000}]


def test_a_command_that_reached_the_sealed_pages_shows_nothing_and_its_files_are_marked(server):
    api, box, DS = server["api"], server["box"], server["DS"]
    box.write("/workspace/notes.txt", "old")
    status, out = call(api, "/api/sandbox/exec", {"command": "curl -s http://fakenet/argus/p.html"})
    assert status == 400 and "봉인된 시험 페이지" in out["error"] and box.calls == []  # named: refused, nothing runs
    status, out = call(api, "/api/sandbox/exec", {"command": "fetch /argus/page1.html"})  # reached anyway: the gateway's log says so
    assert status == 200 and out["sealed"] is True and out["stdout"] == "" and "PAGE TEXT" not in json.dumps(out)
    assert out["sealed_files"] == 1 and out["sealed_checked"] is True  # page.html: what the command left
    assert set(DS.STORE.sandbox_state()["sealed_files"]) == {"page.html"} and DS.still_sealed() is True  # later turns are sealed while it stays
    assert [args[0] for args in box.calls] == ["run", "fakenet-log", "snapshot"]
    listed = call(api, "/api/sandbox/files")[1]
    assert listed["sealed"] == ["/workspace/page.html"]
    status, out = call(api, "/api/sandbox/read", {"path": "/workspace/page.html"})  # the file manager does not show it either
    assert status == 403 and out["code"] == "sealed"
    status, out = call(api, "/api/sandbox/change", {"op": "save", "path": "/workspace/page.html", "text": "x"})
    assert status == 400 and "봉인" in out["error"]
    box.write("/workspace/copy.html", "<a href='http://fakenet/argus/page2.html'>next</a>")  # a copy: not marked, but it holds the address
    status, out = call(api, "/api/sandbox/read", {"path": "/workspace/copy.html"})
    assert status == 403 and out["code"] == "sealed"
    assert call(api, "/api/sandbox/read", {"path": "/workspace/notes.txt"})[1]["text"] == "old"


def test_the_file_manager_lists_and_the_editor_reads(server):
    api, box = server["api"], server["box"]
    box.write("/workspace/project/main.py", "print('안녕')\n")
    box.write("/workspace/project/plot.png", PNG)
    box.write("/workspace/data.bin", b"\x00\x01\x02")
    box.write("/workspace/long.txt", "가" * 30_000)  # 90,000 bytes
    box.links["/workspace/link"] = "/etc"
    status, listed = call(api, "/api/sandbox/files")
    assert status == 200 and listed["status"] == "RUNNING" and listed["truncated"] is False and listed["sealed"] == []
    assert {entry["path"]: (entry["kind"], entry["size"]) for entry in listed["entries"]} == {
        "/workspace/data.bin": ("file", 3), "/workspace/link": ("symlink", None), "/workspace/long.txt": ("file", 90_000),
        "/workspace/project": ("directory", None), "/workspace/project/main.py": ("file", 16), "/workspace/project/plot.png": ("file", len(PNG))}
    assert runs(box) == []  # no snapshot for looking
    status, out = call(api, "/api/sandbox/read", {"path": "/workspace/project/main.py"})
    assert status == 200 and out["text"] == "print('안녕')\n" and out["binary"] is False and out["truncated"] is False
    assert out["sha"] == hashlib.sha256("print('안녕')\n".encode()).hexdigest()
    status, out = call(api, "/api/sandbox/read", {"path": "/workspace/long.txt"})  # its beginning, and no way to save over it
    assert out["truncated"] is True and out["sha"] is None and out["size"] == 90_000 and 0 < len(out["text"]) <= 65_536
    status, out = call(api, "/api/sandbox/read", {"path": "/workspace/data.bin"})
    assert out["binary"] is True and out["text"] == "" and out["sha"] is None
    status, out = call(api, "/api/sandbox/read", {"path": "/workspace/project/plot.png"})  # what it is, before its bytes
    assert out["mime"] == "image/png" and "base64" not in out
    status, out = call(api, "/api/sandbox/read", {"path": "/workspace/project/plot.png", "image": True})
    assert out["mime"] == "image/png" and out["base64"] and out["size"] == len(PNG)
    assert call(api, "/api/sandbox/read", {"path": "/workspace/gone.txt"})[0] == 404
    assert "링크" in call(api, "/api/sandbox/read", {"path": "/workspace/link"})[1]["error"]
    assert "일반 파일만" in call(api, "/api/sandbox/read", {"path": "/workspace/project"})[1]["error"]
    for path in ("/etc/passwd", "/workspace/../etc/passwd", "/workspace"):
        assert call(api, "/api/sandbox/read", {"path": path})[0] == 400
    box.limit = 3
    assert call(api, "/api/sandbox/files")[1]["truncated"] is True
    box.running = False
    assert call(api, "/api/sandbox/files")[1]["status"] == "STOPPED"


def test_the_file_manager_and_the_editor_change_the_workspace(server):
    api, box, DS = server["api"], server["box"], server["DS"]
    DS.STORE.mark_sandbox(restore_point="before-run-0.tar", restore_turn={"conversation": "c-20261123-0123abcd", "turn": 1, "step": 1})

    def change(**body):
        return call(api, "/api/sandbox/change", body)

    status, out = change(op="mkdir", path="/workspace/my folder")
    assert status == 200 and out["ok"] is True and "/workspace/my folder" in box.dirs
    run = runs(box)[0]
    assert run[4:8] == ["python3", "-I", "-S", "-c"] and run[8] == SHELL.OPS and run[9:] == ["mkdir", "/workspace/my folder", ""]  # no shell
    state = DS.STORE.sandbox_state()
    assert state["restore_point"] == out["snapshot"] == "before-run-1.tar" and state["restore_turn"] is None
    again = change(op="mkdir", path="/workspace/my folder")[1]
    assert again["ok"] is False and again["code"] == "exists" and "이미 있습니다" in again["error"]
    assert change(op="touch", path="/workspace/my folder/note.txt")[1]["ok"] is True
    opened = call(api, "/api/sandbox/read", {"path": "/workspace/my folder/note.txt"})[1]
    status, out = change(op="save", path="/workspace/my folder/note.txt", text="첫 줄\n", sha=opened["sha"])
    assert out["ok"] is True and box.files["/workspace/my folder/note.txt"] == "첫 줄\n".encode() and out["size"] == 8
    assert out["sha"] == hashlib.sha256("첫 줄\n".encode()).hexdigest()
    box.write("/workspace/my folder/note.txt", "the agent wrote this meanwhile\n")
    before = len(runs(box))
    status, stale = change(op="save", path="/workspace/my folder/note.txt", text="mine\n", sha=out["sha"])
    assert stale["ok"] is False and stale["code"] == "changed" and len(runs(box)) == before  # not written, nothing ran
    assert box.files["/workspace/my folder/note.txt"] == b"the agent wrote this meanwhile\n"
    assert change(op="save", path="/workspace/my folder/note.txt", text="mine\n")[1]["ok"] is True  # said again without it: written
    big = '"' * 60_000  # as JSON it is twice as long: more than the locked server's own 64,000-byte bodies
    assert change(op="save", path="/workspace/quotes.txt", text=big)[1]["ok"] is True and len(box.files["/workspace/quotes.txt"]) == 60_000
    status, out = change(op="save", path="/workspace/quotes.txt", text="가" * 30_000)
    assert status == 400 and "65,536바이트까지" in out["error"]
    assert change(op="save", path="/workspace/quotes.txt", text="x" * 400_000)[0] == 400  # the request itself is too long
    assert change(op="rename", path="/workspace/my folder", to="/workspace/renamed")[1]["ok"] is True
    assert "/workspace/renamed/note.txt" in box.files and "/workspace/my folder" not in box.dirs
    assert change(op="rename", path="/workspace/renamed", to="/workspace/quotes.txt")[1]["code"] == "exists"
    assert change(op="delete", path="/workspace/renamed")[1]["ok"] is True and not any(path.startswith("/workspace/renamed") for path in box.files)
    assert change(op="delete", path="/workspace/renamed")[1]["code"] == "missing"
    before = len(runs(box))
    for body in ({"op": "delete", "path": "/workspace"}, {"op": "delete", "path": "/"}, {"op": "delete", "path": "/workspace/../home"},
                 {"op": "rename", "path": "/workspace/quotes.txt", "to": "/tmp/out"}, {"op": "format", "path": "/workspace/x"},
                 {"op": "save", "path": "/workspace/x", "text": 7}, {"op": "kill", "pid": 1}, {"op": "kill", "pid": "40"}, {"op": "kill", "pid": True}):
        assert call(api, "/api/sandbox/change", body)[0] == 400, body
    assert len(runs(box)) == before  # none of them reached the sandbox
    rows = [row for row in DS.STORE.audit_tail(50) if row["action"] == "shell"]
    assert {row["what"] for row in rows} >= {"mkdir", "touch", "save", "rename", "delete"} and "note.txt" not in json.dumps(rows)


def test_the_system_window_says_what_runs_and_what_is_used(server):
    api, box, DS = server["api"], server["box"], server["DS"]
    status, out = call(api, "/api/sandbox/system")
    assert status == 200 and out["status"] == "RUNNING" and out["cpu"] == "1.52%" and out["memory"] == "38.4MiB / 4GiB" and out["pids"] == "2"
    assert [disk["mount"] for disk in out["disks"]] == ["/workspace", "/tmp"] and out["disks"][0]["size"] == "2.0G" and out["network"] == "fakenet"
    DS.STORE.mark_sandbox(restore_point="before-run-0.tar", restore_turn={"conversation": "c-20261123-0123abcd", "turn": 1, "step": 1})
    status, out = call(api, "/api/sandbox/processes", {})
    assert status == 200 and [(row["pid"], row["command"]) for row in out["processes"]] == [(1, "sleep infinity"), (40, "python3 server.py --port 8000")]
    assert out["processes"][1] == {"pid": 40, "ppid": 1, "cpu": "1.5", "memory": "0.3", "seconds": 12, "command": "python3 server.py --port 8000"}
    state = DS.STORE.sandbox_state()  # looking changes nothing: the way back, and the turn that can be taken back, stay
    assert state["restore_point"] == "before-run-0.tar" and state["restore_turn"]["turn"] == 1 and "snapshot" not in out
    status, out = call(api, "/api/sandbox/change", {"op": "kill", "pid": 40})
    assert out["ok"] is True and [row[0] for row in box.processes] == [1]
    assert call(api, "/api/sandbox/change", {"op": "kill", "pid": 40})[1]["code"] == "missing"
    box.locked = True
    assert call(api, "/api/sandbox/system")[1]["status"] == "BUSY"
    box.locked, box.running = False, False
    assert call(api, "/api/sandbox/system")[1]["status"] == "STOPPED"
    assert call(api, "/api/sandbox/power", {"action": "off"})[0] == 400  # stopping is the agent chat's 샌드박스 점검
    status, out = call(api, "/api/sandbox/power", {"action": "on"})
    assert status == 200 and out == {"status": "RUNNING", "restored": True} and box.running is True


def test_a_running_command_can_be_stopped_and_nothing_else_can(server):
    api, box, DS = server["api"], server["box"], server["DS"]
    box.write("/workspace/kept.txt", "as it was")
    status, out = call(api, "/api/sandbox/stop", {})
    assert status == 409 and out["code"] == "idle" and box.calls == []  # nothing of the user's runs: nothing is stopped
    server["busy"]["agent"] = True
    assert call(api, "/api/sandbox/stop", {})[0] == 409 and box.calls == []  # never an agent's turn
    server["busy"]["agent"] = False
    assert call(api, "/api/sandbox/stop", {}, {"Origin": "https://ljg5489.github.io"})[0] == 403
    results = []
    first = threading.Thread(target=lambda: results.append(call(api, "/api/sandbox/exec", {"command": "echo gone > kept.txt; sleep 8", "timeout": 30})))
    first.start()
    time.sleep(0.5)
    status, out = call(api, "/api/sandbox/stop", {})
    assert status == 200 and out == {"status": "KILLED"}
    first.join(timeout=10)
    status, out = results[0]
    assert status == 200 and out["status"] == "RESOURCE_OR_SIGNAL" and out["exit_code"] == 137 and out["environment_stopped"] is True
    listed = call(api, "/api/sandbox/files")[1]  # docker says "is not running": the page hears STOPPED
    assert listed["status"] == "STOPPED" and call(api, "/api/sandbox/system")[1]["status"] == "STOPPED"
    assert call(api, "/api/sandbox/read", {"path": "/workspace/kept.txt"})[1]["error"] == "샌드박스가 꺼져 있습니다."
    status, out = call(api, "/api/sandbox/exec", {"command": "cat kept.txt"})  # the next command starts it again, as it was before
    assert out["status"] == "FINISHED" and out["restarted"] is True and out["stdout"] == "as it was"
    assert [row["what"] for row in DS.STORE.audit_tail(10) if row["action"] == "shell"][-3:] == ["kill", "terminal", "terminal"]


def test_the_system_reading_never_meets_an_agents_command(server):
    """`sandbox.py status` holds sandbox.py's own lock for a second or two, and the agent's worker does not try a
    command again that found the lock held."""
    api, box, DS = server["api"], server["box"], server["DS"]
    server["busy"]["agent"] = True
    status, out = call(api, "/api/sandbox/system")
    assert status == 200 and out["status"] == "BUSY" and box.calls == []  # not read at all while a task runs
    server["busy"]["agent"] = False
    box.status_delay = 1.2
    results = []
    reading = threading.Thread(target=lambda: results.append(call(api, "/api/sandbox/system")))
    reading.start()
    time.sleep(0.3)
    assert SHELL.busy() and SHELL.STATE["light"] is True
    assert call(api, "/api/sandbox/stop", {})[1]["code"] == "idle"  # 중지 is for a command, never for a reading
    began = time.monotonic()
    # a turn that starts meanwhile waits for the reading, then goes on to the locked server's own checks (which stop
    # here on this test's empty runtime_status: no model, no GPU)
    with pytest.raises(KeyError, match="agent_model_dir"):
        DS.start_live("t", 5, None, True, None)
    assert time.monotonic() - began > 0.5
    reading.join()
    assert results[0][1]["status"] == "RUNNING" and not SHELL.busy() and SHELL.STATE["light"] is False
    status, out = call(api, "/api/sandbox/exec", {"command": "echo after"})  # and a command right after it runs
    assert out["stdout"] == "after\n"


def test_a_copy_of_the_page_hosted_elsewhere_may_chat_but_the_computer_stays_local(server, monkeypatch):
    """The dashboard published as a hosted site (its address given in ARGUS_SITE_ORIGIN when the server starts) reaches
    this server as it reaches the locked one. The sandbox computer and the unlimited turn stay with the local page."""
    api, box, DS = server["api"], server["box"], server["DS"]
    site = "https://some-studio.example.site"
    monkeypatch.setattr(DS, "ALLOWED_ORIGINS", DS.ALLOWED_ORIGINS | {site})  # what ARGUS_SITE_ORIGIN adds at the start
    with urlopen(Request(api + "/api/health", headers={"Origin": site}), timeout=30) as response:
        assert response.status == 200 and response.headers["Access-Control-Allow-Origin"] == site  # the browser lets the page read it
        health = json.loads(response.read().decode("utf-8"))
    assert health["sandbox_shell"] is True and health["unlimited_steps"] == SERVER.UNLIMITED  # (the page keeps both off: it is not local)
    assert call(api, "/api/health", None, {"Origin": "https://another.example.site"})[0] == 200  # (answered, but no header: the browser hides it)
    for path in ("/api/sandbox/shell", "/api/sandbox/files", "/api/sandbox/system"):
        status, out = call(api, path, None, {"Origin": site})
        assert status == 403 and out["local_only"] is True, path
    for path, body in (("/api/sandbox/exec", {"command": "ls"}), ("/api/sandbox/read", {"path": "/workspace/a"}), ("/api/sandbox/stop", {}),
                       ("/api/sandbox/change", {"op": "delete", "path": "/workspace/a"}), ("/api/sandbox/power", {"action": "on"})):
        status, out = call(api, path, body, {"Origin": site})
        assert status == 403 and out["local_only"] is True, path
    status, out = call(api, "/api/live/start", {"task": "끝까지 해 줘", "max_steps": SERVER.UNLIMITED, "memory": False}, {"Origin": site})
    assert status in (400, 403) and "로컬 페이지에서만" in out["error"], out  # an unlimited turn: never from a page elsewhere
    assert box.calls == []
    said = SERVER.origins_line(DS.ALLOWED_ORIGINS, site)
    assert site in said and "ARGUS_SITE_ORIGIN=" not in said
    assert "ARGUS_SITE_ORIGIN=https://<사이트 주소>" in SERVER.origins_line({"http://127.0.0.1:8765", "https://ljg5489.github.io"}, None)

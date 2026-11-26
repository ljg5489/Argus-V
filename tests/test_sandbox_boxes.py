"""More than one sandbox (argus_hook/sandbox_boxes.py): SANDBOX/ (the plan's), SANDBOX_PC/ (the computer) and
SANDBOX_NET/ (the internet); which one the agent works in, a ledger for each, and the sandbox computer looking at any
of them. No Docker here: folders of a temporary tree, sandboxes made of dicts (tests/fake_sandbox_box.py)."""

import importlib.util
import json
import socket
import sys
import threading
from http.server import ThreadingHTTPServer
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / "argus_hook"), str(ROOT / "tests")]
import agent_memory as AM  # noqa: E402
import agent_server as SERVER  # noqa: E402
import live_agent_free as FREE  # noqa: E402
import sandbox_boxes as BOXES  # noqa: E402
import sandbox_shell as SHELL  # noqa: E402
from fake_sandbox_box import FakeBox  # noqa: E402

SETTINGS = {"plain": {"network": "fakenet"}, "pc": {"network": "allowlist", "allowed_hosts": ["pypi.org", "files.pythonhosted.org"]},
            "net": {"network": "allowlist", "allowed_hosts": ["open.internet"]}}


def tree(tmp_path: Path) -> dict:
    """Three sandbox folders of a temporary tree (a sandbox.py each, settings as the real ones name their network)."""
    for name, folder in BOXES.FOLDERS.items():
        (tmp_path / folder).mkdir()
        (tmp_path / folder / "sandbox.py").write_text("# stands for the folder's sandbox.py\n")
        (tmp_path / folder / "settings.json").write_text(json.dumps(SETTINGS[name]))
        if name != "plain":
            (tmp_path / folder / "desk.py").write_text("# stands for the folder's desk.py\n")
    return BOXES.every(tmp_path)


def call(api: str, path: str, body: dict | None = None, headers: dict | None = None):
    request = Request(api + path, data=None if body is None else json.dumps(body).encode("utf-8"),
                      headers={"Content-Type": "application/json", **(headers or {})}, method="GET" if body is None else "POST")
    try:
        with urlopen(request, timeout=60) as response:
            return response.status, json.loads(response.read().decode("utf-8"))
    except HTTPError as error:
        return error.code, json.loads(error.read().decode("utf-8"))


class Folder:
    """dashboard_server.sandbox_files() of the test: which sandbox's memory folder was removed, in order."""

    def __init__(self, DS, log: list, fail: set):
        self.DS, self.log, self.fail = DS, log, fail

    def clear(self):
        name = BOXES.agent(self.DS).name
        if name in self.fail:
            raise RuntimeError("sandbox blocked (links)")
        self.log.append(name)
        return {"cleared": True, "workspace": {}}


@pytest.fixture
def server(tmp_path, monkeypatch):
    import dashboard_server as DS

    known = tree(tmp_path)
    fakes = {name: FakeBox(known[name].root) for name in known}
    cleared, fail, ups = [], set(), {"refuse": set()}

    def of(script):  # the dict sandbox behind a folder's sandbox.py
        return fakes[next(name for name, box in known.items() if box.script == Path(script))]

    def cli(args, timeout=300):  # dashboard_server.run_sandbox_cli: the agent's
        name = BOXES.agent(DS).name
        if args[0] == "up" and name in ups["refuse"]:
            return {"status": "ERROR", "reason": "image not found"}
        return of(DS.SANDBOX_SCRIPT).cli(args, timeout)

    monkeypatch.setattr(DS, "runtime_status", lambda: {})
    monkeypatch.setattr(DS, "run_sandbox_cli", cli)
    monkeypatch.setattr(BOXES, "run_script", lambda DS_, script, args, timeout=300: of(script).cli(args, timeout))
    monkeypatch.setattr(SHELL, "image_bytes", lambda DS_, box, path: fakes[box.name].image(DS_, box, path))
    monkeypatch.setattr(DS, "sandbox_files", lambda: Folder(DS, cleared, fail))
    SERVER.enable(DS, patch=monkeypatch.setattr)
    env = {}
    BOXES.select(DS, known["plain"], patch=monkeypatch.setattr, environ=env)
    busy = {"agent": False}
    monkeypatch.setattr(DS.LIVE, "status", lambda: {"busy": busy["agent"]})
    DS.configure_for_tests(tmp_path / "memory")
    real_switch = BOXES.switch
    monkeypatch.setattr(BOXES, "switch", lambda DS_, name, patch=monkeypatch.setattr, environ=env: real_switch(DS_, name, patch=patch, environ=environ))
    httpd = ThreadingHTTPServer(("127.0.0.1", 0), DS.Handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    try:
        yield {"api": f"http://127.0.0.1:{httpd.server_address[1]}", "DS": DS, "known": known, "fakes": fakes, "busy": busy,
               "cleared": cleared, "fail": fail, "ups": ups, "env": env, "tmp": tmp_path}
    finally:
        httpd.shutdown()
        httpd.server_close()


def disk(DS) -> dict:
    return json.loads((Path(DS.STORE.root) / "manifest.json").read_text(encoding="utf-8"))


# ---------------------------------------------------------------------------- the folders
def test_the_sandboxes_that_are_there(tmp_path):
    known = tree(tmp_path)
    assert list(known) == ["plain", "pc", "net"]  # the order they are offered in
    assert [(box.network(), box.screen(), box.root.name) for box in known.values()] == [
        ("fakenet", False, "SANDBOX"), ("allowlist", True, "SANDBOX_PC"), ("open", True, "SANDBOX_NET")]
    (tmp_path / "SANDBOX_NET" / "sandbox.py").unlink()
    assert list(BOXES.every(tmp_path)) == ["plain", "pc"]  # a folder that is not there is not offered
    real = BOXES.every()
    assert "plain" in real and real["plain"].script == ROOT / "SANDBOX" / "sandbox.py"
    if "net" in real:  # the real folders, when they are here
        assert real["net"].network() == "open" and real["pc"].network() == "allowlist" and real["plain"].network() == "fakenet"


# ---------------------------------------------------------------------------- a ledger for each
def test_each_sandbox_has_its_own_ledger_and_the_plans_stays_where_the_locked_server_reads_it(server):
    DS, known = server["DS"], server["known"]
    store = DS.STORE
    store.mark_sandbox(restore_point="plain-1.tar", restore_turn={"conversation": "c-20261123-0123abcd", "turn": 1, "step": 1},
                       sealed_files={"page.html": "f9:abc"})
    assert disk(DS)["sandbox"]["restore_point"] == "plain-1.tar" and BOXES.LEDGERS not in disk(DS)
    BOXES.select(DS, known["pc"], patch=lambda obj, name, value: setattr(obj, name, value), environ=server["env"])
    try:
        assert store.sandbox_state()["restore_point"] is None and store.sandbox_state()["sealed_files"] is None  # the computer's own: empty
        store.mark_sandbox(restore_point="pc-7.tar", blocked="links")
        store.add_debt("s1", 100.0)
        on_disk = disk(DS)
        assert on_disk["sandbox"]["restore_point"] == "plain-1.tar" and "blocked" not in on_disk["sandbox"]  # the plan's: untouched
        assert on_disk[BOXES.LEDGERS]["pc"]["restore_point"] == "pc-7.tar" and on_disk[BOXES.LEDGERS]["pc"]["blocked"] == "links"
        assert BOXES.PLAIN_KEPT not in on_disk and not any(key.startswith("\x00") for key in on_disk)  # nothing of the view is written
        assert store.sandbox_state()["debts"][0]["session"] == "s1"
        # the rest of the store is as it was: a conversation is kept and read while another sandbox's ledger is shown
        assert store.settings()["remote_view"] in (True, False) and isinstance(store.conversations(), list)
        # the sandbox computer looking at one that is not the agent's
        plain = BOXES.ledger(DS, known["plain"])
        assert plain["restore_point"] == "plain-1.tar" and plain["sealed_files"] == {"page.html": "f9:abc"} and plain["blocked"] is None
        BOXES.mark(DS, known["net"], restore_point="net-3.tar", blocked="size")
        BOXES.mark(DS, known["plain"], blocked="busy")
        assert BOXES.ledger(DS, known["net"]) == {"restore_point": "net-3.tar", "restore_turn": None, "blocked": "size",
                                                    "sealed_files": None, "cleared": False, "debts": []}
        assert disk(DS)["sandbox"]["blocked"] == "busy" and disk(DS)["sandbox"]["sealed_files"] == {"page.html": "f9:abc"}
        assert store.sandbox_state()["restore_point"] == "pc-7.tar"  # the agent's own, unmoved by the others
    finally:
        BOXES.select(DS, known["plain"], patch=lambda obj, name, value: setattr(obj, name, value), environ=server["env"])
    state = store.sandbox_state()  # back on the plan's: what it had, and what was marked meanwhile
    assert state["restore_point"] == "plain-1.tar" and state["blocked"] == "busy" and state["sealed_files"] == {"page.html": "f9:abc"}
    assert state["debts"] == []


def test_a_ledger_read_before_the_agents_sandbox_changed_is_filed_where_it_was_read(server):
    DS, known, env = server["DS"], server["known"], server["env"]
    put = lambda obj, name, value: setattr(obj, name, value)  # noqa: E731
    store = DS.STORE
    try:
        BOXES.select(DS, known["pc"], patch=put, environ=env)
        store.mark_sandbox(restore_point="pc-1.tar")
        held = store._manifest()  # a read of the store's, as the computer's ...
        held["sandbox"]["blocked"] = "links"
        BOXES.select(DS, known["net"], patch=put, environ=env)  # ... the agent is given the internet one meanwhile ...
        store._save(held)  # ... and the write lands under the computer, where it was read
        on_disk = disk(DS)
        assert on_disk[BOXES.LEDGERS]["pc"] == {"restore_point": "pc-1.tar", "restore_turn": None, "blocked": "links"}
        assert "net" not in on_disk[BOXES.LEDGERS] and "sandbox" not in on_disk
        held = store._manifest()  # read as the internet one's, written after the plan's became the agent's
        held["sandbox"]["blocked"] = "size"
        BOXES.select(DS, known["plain"], patch=put, environ=env)
        store._save(held)
        on_disk = disk(DS)
        assert on_disk[BOXES.LEDGERS]["net"] == {"blocked": "size"} and "sandbox" not in on_disk  # the plan's own: not written over
        store.mark_sandbox(blocked="busy")  # read and written as the plan's while another became the agent's between
        held = store._manifest()
        BOXES.select(DS, known["pc"], patch=put, environ=env)
        store._save(held)
        assert disk(DS)["sandbox"]["blocked"] == "busy" and disk(DS)[BOXES.LEDGERS]["pc"]["blocked"] == "links"
    finally:
        BOXES.select(DS, known["plain"], patch=put, environ=env)


def test_a_store_that_never_heard_of_other_sandboxes_is_untouched(tmp_path, monkeypatch):
    BOXES.install_ledgers(AM, patch=monkeypatch.setattr)
    store = AM.ConversationStore(tmp_path / "memory")
    store.mark_sandbox(restore_point="a.tar", blocked="links")
    data = json.loads((tmp_path / "memory" / "manifest.json").read_text())
    assert data["sandbox"] == {"restore_point": "a.tar", "restore_turn": None, "blocked": "links"} and BOXES.LEDGERS not in data


def test_a_store_with_one_ledger_is_filed_under_the_sandbox_it_was_written_in(server):
    """agent_server.py worked in SANDBOX_PC for a while with the store's one ledger: the first start with a ledger for
    each finds whose it is by its way back (a snapshot's name is in one folder only)."""
    DS, known = server["DS"], server["known"]
    assert BOXES.adopt(DS) is None  # nothing to tell from: no way back was ever kept
    turn = {"conversation": "c-20261123-0123abcd", "turn": 4, "step": 2}
    DS.STORE.mark_sandbox(restore_point="before-run-20261123T040051Z-9e62688b.tar", restore_turn=turn, sealed_files={"a.txt": "f9:1"})
    DS.STORE.mark_start()
    with DS.STORE.lock:
        raw, save = BOXES._raw(DS.STORE)
        raw["sandbox"]["fakenet_until"] = 1795405435.9
        save(raw)
    assert BOXES.adopt(DS) is None and BOXES.LEDGERS not in disk(DS)  # its snapshot is in no folder: left as it is
    known["plain"].snapshots.mkdir()
    (known["plain"].snapshots / "before-run-20261123T040051Z-9e62688b.tar").write_bytes(b"")
    assert BOXES.adopt(DS) == "plain" and BOXES.LEDGERS not in disk(DS) and BOXES.CHOSEN not in disk(DS)  # SANDBOX/'s own: where it is
    (known["plain"].snapshots / "before-run-20261123T040051Z-9e62688b.tar").unlink()
    known["pc"].snapshots.mkdir()
    (known["pc"].snapshots / "before-run-20261123T040051Z-9e62688b.tar").write_bytes(b"")
    before = disk(DS)["sandbox"]
    assert BOXES.adopt(DS) == "pc"
    after = disk(DS)
    assert after[BOXES.LEDGERS] == {"pc": {key: value for key, value in before.items() if key != "fakenet_until"}}
    assert after[BOXES.LEDGERS]["pc"]["restore_turn"] == turn and after[BOXES.LEDGERS]["pc"]["last_start"] == before["last_start"]
    assert set(after["sandbox"]) == {"fakenet_until", "cleared_at"} and after["sandbox"]["fakenet_until"] == 1795405435.9
    assert after[BOXES.CHOSEN] == "pc" and BOXES.chosen(DS) == "pc"
    assert BOXES.adopt(DS) is None and disk(DS) == after  # once
    BOXES.select(DS, known["pc"], patch=lambda obj, name, value: setattr(obj, name, value), environ=server["env"])
    try:  # the agent, in the computer: the way back it had there, and nothing to write again
        state = DS.STORE.sandbox_state()
        assert state["restore_point"] == "before-run-20261123T040051Z-9e62688b.tar" and state["restore_turn"] == turn and state["cleared"] is False
        assert BOXES.ledger(DS, known["plain"])["cleared"] is True and BOXES.ledger(DS, known["plain"])["restore_point"] is None
    finally:
        BOXES.select(DS, known["plain"], patch=lambda obj, name, value: setattr(obj, name, value), environ=server["env"])
    row = [row for row in DS.STORE.audit_tail(10) if row["action"] == "sandbox_ledger"][-1]
    assert row["sandbox"] == "pc"
    for bad in ("../x.tar", "a/b.tar", "", None, 7):  # a name only
        with DS.STORE.lock:
            raw, save = BOXES._raw(DS.STORE)
            raw.pop(BOXES.CHOSEN, None), raw.pop(BOXES.LEDGERS, None)
            raw["sandbox"] = {"restore_point": bad}
            save(raw)
        assert BOXES.adopt(DS) is None


# ---------------------------------------------------------------------------- giving the agent another sandbox
def test_the_agents_sandbox_is_changed_with_its_memory_folder(server):
    DS, known, env, cleared = server["DS"], server["known"], server["env"], server["cleared"]
    import agent_loop

    locked = BOXES.RAW["locked_ensure_running"]
    DS.STORE.mark_sandbox(sealed_files={"page.html": "f9:abc"})
    assert BOXES.agent(DS).name == "plain" and "ARGUS_SANDBOX_SCRIPT" not in env and BOXES.chosen(DS) is None
    done = BOXES.switch(DS, "net")
    assert done == {"agent": "net", "was": "plain", "left": None, "entered": None}
    assert cleared == ["plain", "net"]  # the folder the agent left, then the one it entered: the next turn writes it whole
    assert BOXES.agent(DS).name == "net" and DS.SANDBOX_SCRIPT == known["net"].script and DS.SNAPSHOTS == known["net"].snapshots
    assert env == {"ARGUS_SANDBOX_SCRIPT": str(known["net"].script)}  # what the worker of the next turn is told
    assert agent_loop.RealSandboxClient.ensure_running is FREE.ensure_running  # its network is its own: not turned to fakenet
    assert BOXES.chosen(DS) == "net" and DS.STORE.sandbox_state()["cleared"] is True
    assert BOXES.ledger(DS, known["plain"])["cleared"] is True and BOXES.ledger(DS, known["plain"])["sealed_files"] == {"page.html": "f9:abc"}
    assert ["up"] in server["fakes"]["net"].calls and DS.runtime_status()["agent_sandbox"] == "net"
    assert BOXES.switch(DS, "net") == {"agent": "net", "was": "net"} and cleared == ["plain", "net"]  # the same one: nothing is done
    BOXES.switch(DS, "plain")
    assert cleared == ["plain", "net", "net", "plain"] and "ARGUS_SANDBOX_SCRIPT" not in env
    assert agent_loop.RealSandboxClient.ensure_running is locked  # the plan's own start again (fakenet)
    assert DS.STORE.sandbox_state()["sealed_files"] == {"page.html": "f9:abc"}  # what a sealed turn left there still counts
    rows = [row for row in DS.STORE.audit_tail(10) if row["action"] == "sandbox_choice"]
    assert [(row["was"], row["sandbox"]) for row in rows] == [("plain", "net"), ("net", "plain")]


def test_a_sandbox_that_does_not_start_is_not_entered_and_what_is_owed_is_settled_first(server):
    DS, cleared = server["DS"], server["cleared"]
    server["ups"]["refuse"].add("pc")
    with pytest.raises(ValueError, match="켜지 못했습니다.*SANDBOX_PC/sandbox.py build"):
        BOXES.switch(DS, "pc")
    assert BOXES.agent(DS).name == "plain" and "ARGUS_SANDBOX_SCRIPT" not in server["env"] and BOXES.chosen(DS) is None  # where it was
    assert cleared == ["plain"] and DS.STORE.sandbox_state()["cleared"] is True  # (its folder had gone already: marked, so the next turn writes it)
    server["ups"]["refuse"].clear()
    server["fail"].add("plain")  # its memory folder cannot be removed now: said, and marked to be written again
    done = BOXES.switch(DS, "pc")
    assert done["agent"] == "pc" and "RuntimeError" in done["left"] and done["entered"] is None and cleared == ["plain", "pc"]
    assert BOXES.ledger(DS, server["known"]["plain"])["cleared"] is True
    DS.STORE.add_debt("remote-session", 5.0)
    with pytest.raises(ValueError, match="먼저 정리해야"):
        BOXES.switch(DS, "net")
    with pytest.raises(ValueError, match="모르는 샌드박스"):
        BOXES.switch(DS, "moon")
    assert BOXES.agent(DS).name == "pc"


# ---------------------------------------------------------------------------- through the server
def test_the_page_lists_them_and_changes_the_agents_only_between_turns(server):
    api, DS = server["api"], server["DS"]
    status, out = call(api, "/api/sandbox/list")
    assert status == 200 and out["agent"] == "plain"
    assert [(box["name"], box["folder"], box["network"], box["screen"], box["agent"]) for box in out["sandboxes"]] == [
        ("plain", "SANDBOX", "fakenet", False, True), ("pc", "SANDBOX_PC", "allowlist", True, False), ("net", "SANDBOX_NET", "open", True, False)]
    assert DS.runtime_status()["sandboxes"] == out["sandboxes"]
    server["busy"]["agent"] = True
    status, out = call(api, "/api/sandbox/agent", {"sandbox": "net"})
    assert status == 409 and "에이전트 작업이 실행 중" in out["error"] and BOXES.agent(DS).name == "plain"
    server["busy"]["agent"] = False
    assert call(api, "/api/sandbox/agent", {"sandbox": "moon"})[0] == 400
    for headers in ({"Origin": "https://ljg5489.github.io"}, {"Origin": "https://evil.example"}, {"Host": "evil.example:8765"}):
        assert call(api, "/api/sandbox/agent", {"sandbox": "net"}, headers)[0] == 403  # this computer's local page only
        assert call(api, "/api/sandbox/list", None, headers)[0] == 403
    status, out = call(api, "/api/sandbox/agent", {"sandbox": "net"})
    assert status == 200 and out["agent"] == "net" and out["was"] == "plain"
    assert [box["name"] for box in out["sandboxes"] if box["agent"]] == ["net"] and call(api, "/api/sandbox/list")[1]["agent"] == "net"


def test_the_sandbox_computer_looks_at_any_of_them_whatever_the_agent_does(server):
    api, DS, fakes, known = server["api"], server["DS"], server["fakes"], server["known"]
    fakes["plain"].write("/workspace/plan.txt", "the plan's")
    fakes["pc"].write("/workspace/game/main.py", "print('pc')\n")
    fakes["net"].write("/workspace/page.html", "<html>from the web</html>")
    BOXES.switch(DS, "pc")
    # nothing named: the agent's
    assert [entry["path"] for entry in call(api, "/api/sandbox/files")[1]["entries"]] == ["/workspace/game", "/workspace/game/main.py"]
    assert call(api, "/api/sandbox/shell")[1]["sandbox"] == "pc" and call(api, "/api/sandbox/shell")[1]["agent"] is True
    # another one, by name: in the query of a GET, in the body of a POST
    listed = call(api, "/api/sandbox/files?sandbox=net")[1]
    assert listed["sandbox"] == "net" and [entry["path"] for entry in listed["entries"]] == ["/workspace/page.html"]
    about = call(api, "/api/sandbox/shell?sandbox=net")[1]
    assert about["agent"] is False and about["network"] == "open" and about["screen"] is True and about["folder"] == "SANDBOX_NET"
    assert call(api, "/api/sandbox/read", {"sandbox": "plain", "path": "/workspace/plan.txt"})[1]["text"] == "the plan's"
    assert call(api, "/api/sandbox/files?sandbox=moon")[0] == 400 and call(api, "/api/sandbox/exec", {"sandbox": "moon", "command": "ls"})[0] == 400
    # while the agent works in its own, the others are the user's to use; its own is not
    server["busy"]["agent"] = True
    assert call(api, "/api/sandbox/exec", {"command": "ls"})[0] == 409 and call(api, "/api/sandbox/exec", {"sandbox": "pc", "command": "ls"})[0] == 409
    status, out = call(api, "/api/sandbox/exec", {"sandbox": "net", "command": "echo hi > note.txt; ls"})
    assert status == 200 and out["status"] == "FINISHED" and out["stdout"] == "note.txt\npage.html\n"
    assert fakes["net"].files["/workspace/note.txt"] == b"hi\n" and "/workspace/note.txt" not in fakes["pc"].files
    assert call(api, "/api/sandbox/read", {"sandbox": "net", "path": "/workspace/note.txt"})[1]["text"] == "hi\n"  # (not the agent's: opened)
    assert call(api, "/api/sandbox/read", {"path": "/workspace/game/main.py"})[0] == 409  # the agent's, while it works: not opened
    assert call(api, "/api/sandbox/change", {"sandbox": "net", "op": "mkdir", "path": "/workspace/downloads"})[1]["ok"] is True
    assert call(api, "/api/sandbox/files?sandbox=net")[1]["agent_busy"] is False and call(api, "/api/sandbox/files")[1]["agent_busy"] is True
    # each keeps its own way back; the agent's ledger is not moved by what is done in another
    assert BOXES.ledger(DS, known["net"])["restore_point"].startswith("before-run-") and DS.STORE.sandbox_state()["restore_point"] is None
    with pytest.raises(Exception):  # and a turn of the agent's may start while the user works in another (it stops only on this test's empty runtime_status)
        DS.start_live("t", 5, None, True, None)
    server["busy"]["agent"] = False


def test_a_sandbox_that_is_not_the_agents_has_its_own_way_back(server):
    api, DS, fakes, known = server["api"], server["DS"], server["fakes"], server["known"]
    BOXES.switch(DS, "pc")
    fakes["net"].write("/workspace/keep.txt", "as it was")
    call(api, "/api/sandbox/exec", {"sandbox": "net", "command": "echo gone > keep.txt; ln -s keep.txt link"})
    status, out = call(api, "/api/sandbox/exec", {"sandbox": "net", "command": "ls"})  # a link: its snapshot fails, nothing runs
    assert out["status"] == "ERROR" and out["blocked"] == "links" and BOXES.ledger(DS, known["net"])["blocked"] == "links"
    assert DS.STORE.sandbox_state()["blocked"] is None  # the agent's own sandbox is not called blocked for it
    assert call(api, "/api/sandbox/restore", {})[1]["code"] == "agent_box"  # the agent's goes the server's own way
    status, out = call(api, "/api/sandbox/restore", {"sandbox": "net"})
    assert status == 200 and out["restored"].startswith("before-run-")
    assert [args[0] for args in fakes["net"].calls[-3:]] == ["stop", "up", "restore"] and fakes["net"].calls[-3][1] == "--force"
    assert fakes["net"].files["/workspace/keep.txt"] == b"as it was" and not fakes["net"].links
    state = BOXES.ledger(DS, known["net"])
    assert state["blocked"] is None and state["cleared"] is True
    assert call(api, "/api/sandbox/exec", {"sandbox": "net", "command": "cat keep.txt"})[1]["stdout"] == "as it was"
    assert call(api, "/api/sandbox/restore", {"sandbox": "plain"})[1]["code"] == "no_snapshot"  # nothing was run there


def test_where_a_sandbox_went_on_the_web(server):
    api, fakes = server["api"], server["fakes"]
    log = "\n".join([
        'proxy-1  | {"event": "proxy_request", "method": "CONNECT", "time": 10.0}',
        'proxy-1  | {"event": "destination", "host": "pypi.org", "port": 443, "outcome": "ALLOW", "time": 10.1}',
        'proxy-1  | {"event": "destination", "host": "192.168.0.1", "port": 80, "outcome": "DENY", "time": 11.5}',
        "proxy-1  | not json at all",
        'proxy-1  | {"event": "destination", "host": "finance.naver.com", "port": 443, "outcome": "ALLOW", "time": 12.0, "path": "/never/kept"}'])
    real = fakes["net"].cli
    fakes["net"].cli = lambda args, timeout=300: {"log": log} if args[0] == "network-log" else real(args, timeout)
    status, out = call(api, "/api/sandbox/network?sandbox=net")
    assert status == 200 and out["supported"] is True and out["network"] == "open"
    assert out["events"] == [{"host": "pypi.org", "port": 443, "allowed": True, "time": 10.1},
                             {"host": "192.168.0.1", "port": 80, "allowed": False, "time": 11.5},
                             {"host": "finance.naver.com", "port": 443, "allowed": True, "time": 12.0}]  # hosts only: never a path
    status, out = call(api, "/api/sandbox/network?sandbox=plain")  # a fake internet has no proxy: nothing to list
    assert out == {"sandbox": "plain", "network": "fakenet", "events": [], "supported": False}


# ---------------------------------------------------------------------------- what one step may generate
def test_what_a_step_may_generate_is_a_setting(monkeypatch, tmp_path):
    """2026-11-23, the user: "출력 토큰은 우리가 조정할 수가 있잖아?" The model is local: 2,048 (reasoning and command
    together) is the plan's number, not a limit of the model. The everyday worker takes the size chosen on the page."""
    import subprocess

    for name in ("ARGUS_MAX_NEW_TOKENS", "ARGUS_FREE_CONTEXT_TOKENS"):
        monkeypatch.delenv(name, raising=False)
    assert (FREE.PLAN_OUTPUT_TOKENS, FREE.OUTPUT_TOKENS, FREE.OUTPUT_DEFAULT) == (2048, (2048, 4096, 8192), 4096)
    assert FREE.output_tokens() == 4096 and FREE.output_tokens({"ARGUS_MAX_NEW_TOKENS": "8192"}) == 8192
    assert FREE.output_tokens({"ARGUS_MAX_NEW_TOKENS": "2,048"}) == 2048
    for bad in ("3000", "0", "-1", "many", "", "16384", "1e4", "8192.0"):  # only the sizes offered: anything else is the default
        assert FREE.output_tokens({"ARGUS_MAX_NEW_TOKENS": bad}) == 4096
    for tokens in FREE.OUTPUT_TOKENS:  # prompt and reply together stay at what a turn has been run with
        monkeypatch.setenv("ARGUS_MAX_NEW_TOKENS", str(tokens))
        assert FREE.budget_tokens() + tokens == FREE.CONTEXT_TOKENS + FREE.PLAN_OUTPUT_TOKENS == 18_048
    monkeypatch.setenv("ARGUS_FREE_CONTEXT_TOKENS", "30000")
    assert FREE.budget_tokens() == 30000  # a budget asked for outright is the budget
    # the worker: the locked module's own number is the plan's, and the everyday worker sets the one it was given
    probe = "import live_agent as LA; before = LA.MAX_NEW_TOKENS; import live_agent_free as F; F.prepare(); print(before, LA.MAX_NEW_TOKENS)"
    seen = {}
    for given in (None, "8192", "2048", "999999"):
        env = {key: value for key, value in __import__("os").environ.items() if key not in ("ARGUS_MAX_NEW_TOKENS", "ARGUS_SANDBOX_SCRIPT")}
        if given:
            env["ARGUS_MAX_NEW_TOKENS"] = given
        done = subprocess.run([sys.executable, "-c", probe], capture_output=True, text=True, timeout=120, env=env, cwd=ROOT / "argus_hook")
        assert done.returncode == 0, done.stderr[-500:]
        seen[given] = done.stdout.split()
    assert seen == {None: ["2048", "4096"], "8192": ["2048", "8192"], "2048": ["2048", "2048"], "999999": ["2048", "4096"]}


def test_the_page_sets_what_a_step_may_generate(server, monkeypatch):
    import os

    monkeypatch.delenv("ARGUS_MAX_NEW_TOKENS", raising=False)  # (put back as it was after the test, whatever the server sets)
    api, DS = server["api"], server["DS"]
    assert DS.runtime_status()["output_tokens"] == {"value": 4096, "choices": [2048, 4096, 8192], "plan": 2048}
    status, out = call(api, "/api/agent/output-tokens", {"tokens": 8192})
    assert status == 200 and out == {"value": 8192, "choices": [2048, 4096, 8192], "plan": 2048}
    assert DS.live_env()["ARGUS_MAX_NEW_TOKENS"] == "8192"  # what the worker of the next task is started with
    assert disk(DS)["agent_output_tokens"] == 8192 and DS.runtime_status()["output_tokens"]["value"] == 8192
    for bad in (3000, "8192", True, None, 8192.5, -1, [8192]):
        status, out = call(api, "/api/agent/output-tokens", {"tokens": bad})
        assert status == 400 and "2,048, 4,096, 8,192" in out["error"]
    assert DS.runtime_status()["output_tokens"]["value"] == 8192 and disk(DS)["agent_output_tokens"] == 8192
    for headers in ({"Origin": "https://ljg5489.github.io"}, {"Origin": "https://evil.example"}, {"Host": "evil.example:8765"}):
        assert call(api, "/api/agent/output-tokens", {"tokens": 2048}, headers)[0] == 403  # this computer's local page only
    assert DS.runtime_status()["output_tokens"]["value"] == 8192
    assert [row["tokens"] for row in DS.STORE.audit_tail(10) if row["action"] == "output_tokens"] == [8192]
    # the next start: the store's last choice, unless the command itself names one
    monkeypatch.delenv("ARGUS_MAX_NEW_TOKENS")
    assert SERVER.restore_output_tokens(DS) == 8192 and os.environ["ARGUS_MAX_NEW_TOKENS"] == "8192"
    monkeypatch.setenv("ARGUS_MAX_NEW_TOKENS", "2048")
    assert SERVER.restore_output_tokens(DS) == 2048 and disk(DS)["agent_output_tokens"] == 8192
    # the ledgers of the sandboxes are untouched by it, whichever the agent's is
    BOXES.switch(DS, "pc")
    assert call(api, "/api/agent/output-tokens", {"tokens": 4096})[0] == 200
    on_disk = disk(DS)
    assert on_disk["agent_output_tokens"] == 4096 and on_disk["agent_sandbox"] == "pc" and set(on_disk[BOXES.LEDGERS]) == {"pc"}


# ---------------------------------------------------------------------------- the worker, and the proxy of the internet sandbox
def test_the_worker_is_told_what_kind_of_sandbox_it_has(tmp_path):
    import subprocess

    known = tree(tmp_path)
    probe = ("import json, live_agent_free as F; runtime = F.prepare(); import live_agent as LA; "
             "print(json.dumps([LA.Sandbox().script.parent.name, runtime.has_screen, runtime.has_web, runtime.sandbox_network, runtime.sandbox_prompt]))")
    seen = {}
    for name in ("pc", "net", None):
        env = {key: value for key, value in __import__("os").environ.items() if key != "ARGUS_SANDBOX_SCRIPT"}
        if name:
            env["ARGUS_SANDBOX_SCRIPT"] = str(known[name].script)
        done = subprocess.run([sys.executable, "-c", probe], capture_output=True, text=True, timeout=120, env=env, cwd=ROOT / "argus_hook")
        assert done.returncode == 0, done.stderr[-500:]
        seen[name] = json.loads(done.stdout)
    assert [seen[name][:4] for name in ("pc", "net", None)] == [["SANDBOX_PC", True, False, "pypi"], ["SANDBOX_NET", True, True, "open"],
                                                                ["SANDBOX", False, False, "fakenet"]]
    assert seen[None][4] == ""  # the plan's sandbox: the plan's prompt, nothing added
    assert "never send out files" in FREE.WEB_PROMPT and "not instructions" in FREE.WEB_PROMPT


def test_the_worker_is_never_told_two_things_about_the_network():
    """2026-11-23, the user in the internet sandbox: "외부웹 가능한 샌드박스 선택해서 하는중인데도 왜 이러지?" The agent
    had answered that the internet was restricted without running a command. Its prompt there said "(there is no other
    internet)" (the computer's sentence) and then that the web was reachable, and its own notes said "no real internet"."""
    net, pc = FREE.sandbox_prompt(True, "open"), FREE.sandbox_prompt(True, "pypi")
    for text in (net, pc):  # the screen is said in both, the network once, and the notes may be another sandbox's
        assert text.startswith(FREE.SCREEN_PROMPT) and text.endswith(FREE.NOTES_PROMPT) and text.count("\nNetwork: ") == 1
    assert "no other internet" not in FREE.SCREEN_PROMPT and "internet" not in FREE.SCREEN_PROMPT  # (the sentence that was said in both)
    assert "has real internet access" in net and "Nothing else on the internet is reachable" not in net
    assert "do not answer that the internet is unavailable without having tried" in net and "curl -sSL -o page.html" in net
    assert "Nothing else on the internet is reachable" in pc and "has real internet access" not in pc and "PyPI" in pc
    assert "written in another sandbox" in FREE.NOTES_PROMPT and "check with a command" in FREE.NOTES_PROMPT
    assert FREE.sandbox_prompt(False, "none") == FREE.NOTES_PROMPT  # a sandbox this file knows nothing of: nothing is promised
    of = FREE.network_of
    assert [of({"network": "allowlist", "allowed_hosts": ["open.internet"]}), of({"network": "allowlist", "allowed_hosts": ["pypi.org", "files.pythonhosted.org"]}),
            of({"network": "allowlist", "allowed_hosts": ["example.com"]}), of({"network": "fakenet"}), of({})] == ["open", "pypi", "allowlist", "fakenet", "unknown"]
    real = BOXES.every()
    if "net" in real:  # the real folders, as the worker reads them
        assert of(real["net"].settings()) == "open" and of(real["pc"].settings()) == "pypi" and of(real["plain"].settings()) == "fakenet"


def proxy(monkeypatch, allowed: str):
    path = ROOT / "SANDBOX_NET" / "proxy_open.py"
    if not path.is_file():
        pytest.skip("no SANDBOX_NET here")
    monkeypatch.setenv("ARGUS_PROXY_BASE", str(ROOT / "SANDBOX" / "proxy.py"))  # (in the image: the copy kept beside it)
    monkeypatch.setenv("ALLOWED_HOSTS", allowed)
    spec = importlib.util.spec_from_file_location(f"proxy_open_{abs(hash(allowed))}", path)
    module = importlib.util.module_from_spec(spec)
    was, sys.dont_write_bytecode = sys.dont_write_bytecode, True  # (nothing is left in the sandbox's folder)
    try:
        spec.loader.exec_module(module)
    finally:
        sys.dont_write_bytecode = was
    return module


def test_the_internet_sandboxs_proxy_lets_the_public_web_through_and_nothing_private(monkeypatch):
    module = proxy(monkeypatch, "open.internet")
    names = {"example.com": ["93.184.215.14"], "both.example": ["93.184.215.14", "2606:2800:21f:cb07:6820:80da:af6b:8b2c"],
             "router.home": ["192.168.0.1"], "here.example": ["127.0.0.1"], "tail.example": ["100.116.246.125"],
             "meta.example": ["169.254.169.254"], "mixed.example": ["93.184.215.14", "10.0.0.5"], "v6first.example": ["2606:4700::6810:84e5", "104.16.132.229"],
             "docker.example": ["172.17.0.1"], "nowhere.example": []}

    def getaddrinfo(host, port, type=0):
        if host not in names and host.replace(".", "").replace(":", "").isalnum() and host[0].isdigit():
            names[host] = [host]  # a literal address is its own answer
        return [((socket.AF_INET6 if ":" in ip else socket.AF_INET), socket.SOCK_STREAM, 6, "", (ip, port)) for ip in names.get(host, [])]

    monkeypatch.setattr(module.socket, "getaddrinfo", getaddrinfo)
    assert module.OPEN is True
    assert module.approved_address("example.com", 443) == "93.184.215.14" and module.approved_address("EXAMPLE.com.", 80) == "93.184.215.14"
    assert module.approved_address("v6first.example", 443) == "104.16.132.229"  # IPv4 first
    for host in ("router.home", "here.example", "tail.example", "meta.example", "mixed.example", "docker.example", "nowhere.example",
                 "10.0.0.1", "127.0.0.1", "192.168.1.1", "100.64.0.1", "169.254.169.254"):
        with pytest.raises(PermissionError):  # nothing of this machine or its networks, by name or by address
            module.approved_address(host, 80)
    for port in (22, 25, 8080, 8443, 3306):
        with pytest.raises(PermissionError, match="port"):
            module.approved_address("example.com", port)
    assert module.core.approved_address is module.approved_address and module.core.LIMIT == 1024**3  # the base's HTTP forwarding uses it
    assert issubclass(module.Proxy, module.core.Proxy) and module.TUNNEL_BYTES > 53_000_000
    listed = proxy(monkeypatch, "pypi.org,files.pythonhosted.org")  # without the name: the listed hosts only, as before
    monkeypatch.setattr(listed.socket, "getaddrinfo", getaddrinfo)
    names["pypi.org"] = ["151.101.0.223"]
    assert listed.OPEN is False and listed.approved_address("pypi.org", 443) == "151.101.0.223"
    with pytest.raises(PermissionError, match="destination not allowed"):
        listed.approved_address("example.com", 443)

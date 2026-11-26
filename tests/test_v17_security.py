"""Known gaps in files locked by plan v1.6, written down as the tests v1.7 must pass (cycle 13, safety seat).

Every test here is xfail(strict): it fails today because the gap is real; when v1.7 closes one, its test passes and
strict turns that into a failure until its mark is removed. None of these paths is in the v1.6 plan's cases (one
fakenet page, no repository, an empty workspace, a memory root of its own): the run is not stopped for them.
reports/live-agent/v1.7.md lists them with their fixes; the dashboard README says what to do until then.
"""

import io
import json
import subprocess
import sys
import tarfile
import threading
from http.server import ThreadingHTTPServer
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "argus_hook"))
import agent_memory as AM  # noqa: E402

CID = "c-20261122-abcdef12"
# raises=AssertionError: a harness that breaks (TypeError, KeyError...) fails the test instead of passing for a gap
GAP = pytest.mark.xfail(strict=True, raises=AssertionError,
                        reason="a v1.6 gap in a locked file: v1.7 (reports/live-agent/v1.7.md)")
CANARY = "ARGUS-SEALED-PAGE-TEXT-7f3a"  # stands for what a sealed page said
PAGES = "https://ljg5489.github.io"  # an allowed origin elsewhere (the GitHub Pages copy)


def tar(path: Path, files: dict[str, bytes]) -> Path:
    with tarfile.open(path, "w") as out:
        for name, data in files.items():
            info = tarfile.TarInfo("./" + name)
            info.size, info.mtime = len(data), 1795000000
            out.addfile(info, io.BytesIO(data))
    return path


class Events:
    """LIVE for record_turn: one task's events, then nothing (never the real worker)."""

    def __init__(self, events):
        self.events = [{"seq": index, "session": "s1", "time": 1795000000.0 + index, **event}
                       for index, event in enumerate(events, start=1)]

    def events_after(self, seq, wait=20):
        return {"events": [event for event in self.events if event["seq"] > seq], "busy": False, "session": None}

    def keep_load_times(self, path):
        pass


@pytest.fixture()
def recorded(tmp_path, monkeypatch):
    import dashboard_server as DS

    def run(events):
        monkeypatch.setattr(DS, "LIVE", Events(events))
        DS.configure_for_tests(tmp_path / "memory")
        DS.record_turn(CID, "s1", 0, "페이지 읽기", 1)
        return DS
    return run


# ---------------------------------------------------------------------------- the harness sees what v1.6 does see
def test_control_a_files_change_the_turn_sent_sealed_is_tagged(recorded):
    DS = recorded([{"type": "task_start", "run_id": "live-0", "sealed": True},
                   {"type": "files_changed", "added": ["p.json"], "counts": {"added": 1}, "digests": {"p.json": "d1"},
                    "sealed": True},
                   {"type": "task_end", "termination": "stop", "sealed": True}])
    assert DS.STORE.sandbox_state()["sealed_files"] == {"p.json": "d1"}


def test_control_a_known_git_setting_counts_as_a_hook(tmp_path):
    workspace = tmp_path / "workspace"
    (workspace / "proj" / ".git").mkdir(parents=True)
    (workspace / "proj" / ".git" / "config").write_text("[core]\n\tfsmonitor = ./watch.sh\n")
    assert hooks_of(workspace, tmp_path)["hooks"] == 1


# ---------------------------------------------------------------------------- ① the seal tag fails open
@GAP
def test_files_a_turn_changed_before_its_last_fakenet_read_are_sealed(recorded):
    # files_changed goes out before the end-of-task read of the gateway's log finds the sealed request
    DS = recorded([{"type": "task_start", "run_id": "live-1"},
                   {"type": "files_changed", "added": ["p.json"], "counts": {"added": 1}, "digests": {"p.json": "d1"}},
                   {"type": "fakenet", "argus": 1, "until": 1795000100.0, "sealed": True},
                   {"type": "task_end", "termination": "stop", "sealed": True}])
    assert "p.json" in (DS.STORE.sandbox_state().get("sealed_files") or {})


@GAP
def test_a_sealed_turn_tags_every_file_it_made_not_the_first_thirty(tmp_path):
    before = tar(tmp_path / "a.tar", {"keep.txt": b"x"})
    after = tar(tmp_path / "b.tar", {"keep.txt": b"x", **{f"f{index:02d}.txt": b"page" for index in range(31)}})
    diff = AM.tar_diff(before, after)
    assert diff["counts"]["added"] == 31 and len(diff["digests"]) == 31


@GAP
def test_the_seal_tags_keep_long_paths_and_many_files(tmp_path):
    store = AM.ConversationStore(tmp_path / "memory")
    long = "d/" * 540 + "p.json"  # 1,086 characters
    store.mark_sandbox(sealed_files={long: "d1", **{f"f{index}": "d" for index in range(205)}})
    kept = store.sandbox_state()["sealed_files"]
    assert long in kept and len(kept) == 206


# ---------------------------------------------------------------------------- ② the repository hook check is a blocklist
def hooks_of(workspace: Path, tmp_path: Path) -> dict:
    (tmp_path / "noproc").mkdir(exist_ok=True)
    (tmp_path / "scratch").mkdir(exist_ok=True)
    code = ("import base64, hashlib, json, os, sys, zlib\n" + AM.WORKSPACE_CODE
            + "\nprint(json.dumps(workspace(detail=True)))")
    code = (code.replace("'/workspace/.agent'", repr(str(workspace / ".agent"))).replace("'/workspace'", repr(str(workspace)))
            .replace("'/proc'", repr(str(tmp_path / "noproc"))).replace("'/proc/'", repr(str(tmp_path / "noproc") + "/"))
            .replace("('/tmp', '/dev/shm')", repr((str(tmp_path / "scratch"),))))
    assert "'/tmp'" not in code and "'/dev/shm'" not in code  # never the host's own /tmp
    done = subprocess.run([sys.executable, "-I", "-S", "-c", code], capture_output=True, text=True, check=True, timeout=60)
    return json.loads(done.stdout)


@GAP
@pytest.mark.parametrize("setting", ['[remote "origin"]\n\tuploadpack = sh -c x\n', '[remote "origin"]\n\treceivepack = sh -c x\n',
                                     "[core]\n\teditor = sh -c x\n", "[core]\n\tgitProxy = sh -c x\n",
                                     '[protocol "ext"]\n\tallow = always\n[url "ext::sh -c x"]\n\tinsteadOf = https://\n',
                                     '[submodule "x"]\n\tupdate = !sh -c x\n',  # runs at git submodule update
                                     "[sequence]\n\teditor = sh -c x\n"])  # a key no list names: an allowlist counts it
def test_git_settings_that_run_a_program_count_as_hooks(tmp_path, setting):
    workspace = tmp_path / "workspace"
    (workspace / "proj" / ".git").mkdir(parents=True)
    (workspace / "proj" / ".git" / "config").write_text(setting)
    assert hooks_of(workspace, tmp_path)["hooks"] >= 1


@GAP
def test_a_linked_git_config_is_read_where_it_points(tmp_path):
    workspace = tmp_path / "workspace"
    (workspace / "proj" / ".git").mkdir(parents=True)
    (workspace / "elsewhere.cfg").write_text("[core]\n\tfsmonitor = ./watch.sh\n")
    (workspace / "proj" / ".git" / "config").symlink_to(workspace / "elsewhere.cfg")  # git follows the link
    assert hooks_of(workspace, tmp_path)["hooks"] >= 1


@GAP
def test_a_repository_below_the_depth_limit_is_not_passed_over_silently(tmp_path):
    workspace = tmp_path / "workspace"
    deep = workspace / "a" / "b" / "c" / "d" / "e" / "proj"
    (deep / ".git" / "hooks").mkdir(parents=True)
    (deep / ".git" / "hooks" / "post-checkout").write_text("#!/bin/sh\ncp x y\n")
    assert hooks_of(workspace, tmp_path)["hooks"] >= 1


# ---------------------------------------------------------------------------- ③ changes outside the memory step ignore the seal
@GAP
def test_a_memory_change_made_outside_the_memory_step_in_a_sealed_sandbox_is_held_as_sealed(recorded):
    # a sealed turn left a process that appends page text to NOTES.md after its memory step: the next turn's load
    # finds it as an outside change; a page elsewhere with the memory view must not read it
    DS = recorded([{"type": "task_start", "run_id": "live-2", "sealed": True},
                   {"type": "memory", "action": "loaded", "sealed": True, "files": {},
                    "outside": {"NOTES.md": "# NOTES.md\n\nwhat the sealed page said\n"}},
                   {"type": "task_end", "termination": "stop", "sealed": True}])
    review = DS.STORE.memory()["review"]
    assert review and all("sealed_pages" in (item.get("reasons") or []) for item in review)


@GAP
def test_a_file_a_sealed_turn_wrote_under_cache_is_tagged(tmp_path):
    before = tar(tmp_path / "a.tar", {"keep.txt": b"x"})
    after = tar(tmp_path / "b.tar", {"keep.txt": b"x", ".cache/p.json": b"page"})
    assert ".cache/p.json" in (AM.tar_diff(before, after) or {}).get("digests", {})


# ---------------------------------------------------------------------------- ④ every reply that carries a conversation
class Quiet:
    """LIVE with nothing running (the API's status only)."""

    def status(self):
        return {"busy": False, "alive": False, "meta": {}, "session": None}

    def keep_load_times(self, path):
        pass


@pytest.fixture()
def elsewhere(tmp_path, monkeypatch):
    """Conversations whose turns read the sealed pages, one a page elsewhere started and one the local page did; the
    API on a local port, called with the Pages copy's Origin. ``call(path, body=None, view=False)``."""
    import dashboard_server as DS

    monkeypatch.setattr(DS, "LIVE", Quiet())
    DS.configure_for_tests(tmp_path / "memory")
    sealed = {"task": "페이지 읽기", "sealed": True, "answer": CANARY, "termination": "stop",
              "steps": [{"step": 1, "kind": "bash", "command": f"echo {CANARY}", "observation": CANARY, "exit_code": 0}]}
    remote = DS.STORE.create("페이지 읽기", origin="remote")["id"]
    DS.STORE.append_turn(remote, {**sealed, "origin": "remote"})
    local = DS.STORE.create("페이지 읽기", origin="local")["id"]
    DS.STORE.append_turn(local, {**sealed, "origin": "local"})
    server = ThreadingHTTPServer(("127.0.0.1", 0), DS.Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{server.server_address[1]}"

    def call(path, body=None, view=False):
        DS.STORE.set_settings(remote_view=view)  # the local page's switch: pages elsewhere may see the memory
        data = None if body is None else json.dumps(body).encode()
        headers = {"Origin": PAGES, **({"Content-Type": "application/json"} if data else {})}
        try:
            with urlopen(Request(base + path, data=data, headers=headers), timeout=20) as response:
                return response.read().decode("utf-8")
        except HTTPError as error:  # a refusal carries no conversation
            return error.read().decode("utf-8")
    yield {"remote": remote, "local": local, "call": call, "DS": DS}
    server.shutdown()


def test_control_a_page_elsewhere_reading_conversations_gets_no_sealed_text(elsewhere):
    call = elsewhere["call"]
    for view in (False, True):
        assert CANARY not in call(f"/api/live/conversations/{elsewhere['remote']}", view=view)
        assert CANARY not in call("/api/live/conversations", view=view)
        assert CANARY not in call(f"/api/live/conversations/{elsewhere['local']}", view=view)  # refused or hidden


@GAP
@pytest.mark.parametrize("which,view", [("remote", False), ("remote", True), ("local", True)])
@pytest.mark.parametrize("action,body", [("rename", {"title": "x"}), ("fork", {"turn": 1})])
def test_a_rename_or_fork_reply_to_a_page_elsewhere_carries_no_sealed_text(elsewhere, action, body, which, view):
    cid = elsewhere[which]
    assert CANARY not in elsewhere["call"](f"/api/live/conversations/{cid}/{action}", body, view=view)


def test_control_a_local_conversation_is_not_renamed_from_elsewhere_without_the_view(elsewhere):
    reply = elsewhere["call"](f"/api/live/conversations/{elsewhere['local']}/rename", {"title": "x"}, view=False)
    assert CANARY not in reply and "local_only" in reply


# ---------------------------------------------------------------------------- ⑤ outputs of a turn with scenario files
@GAP
def test_a_turn_with_scenario_files_sends_its_outputs_to_the_local_page_only(elsewhere):
    # S5: the page hides them; the API's reply to a page elsewhere should not carry them at all
    DS = elsewhere["DS"]
    cid = DS.STORE.create("목록", origin="remote")["id"]
    DS.STORE.append_turn(cid, {"task": "목록", "origin": "remote", "termination": "stop", "answer": "끝",
                               "context": {"workspace": {"canary": True}},
                               "steps": [{"step": 1, "kind": "bash", "command": "sed -n 5p notes.txt",
                                          "observation": "scenario text without its marker line", "exit_code": 0}]})
    assert "scenario text without its marker line" not in elsewhere["call"](f"/api/live/conversations/{cid}")

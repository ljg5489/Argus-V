"""The boundary to pages elsewhere, as a property (cycle 15, SB3): a turn that read the sealed pages, and a turn that
had scenario files in its workspace, hold a different canary in every text field; a page elsewhere (the Pages copy's
Origin), with the memory view off and on, asks every reply that carries a conversation or an event for it. No
canary may come back. The replies that carry one today are v1.7's to close (reports/live-agent/v1.7.md S4–S6) and
are marked xfail(strict); the others are guards that must keep passing.
"""

import json
import sys
import threading
from http.server import ThreadingHTTPServer
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "argus_hook"))

PAGES = "https://ljg5489.github.io"
CANARY = {name: f"ARGUS-SB3-{name.upper()}-7f3a" for name in
          ("answer", "report", "command", "output", "note", "old", "outside", "file", "residue", "event")}
GAP = pytest.mark.xfail(strict=True, raises=AssertionError,
                        reason="a v1.6 gap in a locked file: v1.7 (reports/live-agent/v1.7.md S4-S6)")
ENDPOINTS = ("get", "list", "rename", "fork", "events", "status", "memory", "history")
# what carries a canary today (measured): (view, conversation, endpoint)
LEAKS = {("off", "remote", "rename"), ("off", "remote", "fork"),
         ("off", "residue", "get"), ("off", "residue", "rename"), ("off", "residue", "fork"),
         ("on", "remote", "get"), ("on", "remote", "rename"), ("on", "remote", "fork"),
         ("on", "local", "get"), ("on", "local", "rename"), ("on", "local", "fork"),
         ("on", "residue", "get"), ("on", "residue", "rename"), ("on", "residue", "fork")}


class Quiet:
    """LIVE with one sealed task's events (its output and answer hold a canary); nothing runs."""

    def status(self):
        return {"busy": False, "alive": False, "meta": {}, "session": None}

    def keep_load_times(self, path):
        pass

    def events_after(self, after, wait=0):
        return {"events": [{"seq": 1, "session": "s1", "type": "observation", "step": 1, "text": CANARY["event"], "sealed": True},
                           {"seq": 2, "session": "s1", "type": "final", "step": 2, "text": CANARY["event"], "sealed": True}],
                "busy": False, "session": None, "last": 2}


def sealed_turn(origin: str) -> dict:
    return {"task": "페이지 읽기", "origin": origin, "sealed": True, "answer": CANARY["answer"], "report": CANARY["report"],
            "termination": "stop", "sandbox_notes": [CANARY["note"]],
            "steps": [{"step": 1, "kind": "bash", "command": CANARY["command"], "observation": CANARY["output"], "exit_code": 0}],
            "superseded": [{"answer": CANARY["old"], "task": "페이지 읽기", "origin": origin, "sealed": True}],
            "memory_outside": [{"file": "NOTES.md", "lines": [{"old": [], "new": [CANARY["outside"]]}]}],
            "files_changed": {"added": [CANARY["file"]], "raw": {"added": [CANARY["file"]]}, "counts": {"added": 1}}}


@pytest.fixture(scope="module")
def pages(tmp_path_factory):
    import dashboard_server as DS

    saved = DS.LIVE
    DS.LIVE = Quiet()
    DS.configure_for_tests(tmp_path_factory.mktemp("boundary") / "memory")
    ids = {"remote": DS.STORE.create("페이지 읽기", origin="remote")["id"],
           "local": DS.STORE.create("페이지 읽기", origin="local")["id"],
           "residue": DS.STORE.create("목록", origin="remote")["id"]}
    DS.STORE.append_turn(ids["remote"], sealed_turn("remote"))
    DS.STORE.append_turn(ids["local"], sealed_turn("local"))
    DS.STORE.append_turn(ids["residue"], {"task": "목록", "origin": "remote", "termination": "stop", "answer": "끝",
                                          "context": {"workspace": {"canary": True}},
                                          "steps": [{"step": 1, "kind": "bash", "command": "sed -n 5p notes.txt",
                                                     "observation": CANARY["residue"], "exit_code": 0}]})
    server = ThreadingHTTPServer(("127.0.0.1", 0), DS.Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{server.server_address[1]}"

    def call(view: str, which: str, endpoint: str) -> str:
        DS.STORE.set_settings(remote_view=view == "on")  # the local page's switch for pages elsewhere
        cid = ids[which]
        path, body = {"get": (f"/api/live/conversations/{cid}", None), "list": ("/api/live/conversations", None),
                      "rename": (f"/api/live/conversations/{cid}/rename", {"title": "x"}),
                      "fork": (f"/api/live/conversations/{cid}/fork", {"turn": 1}),
                      "events": ("/api/live/events?after=0", None), "status": ("/api/live/status", None),
                      "memory": ("/api/live/memory", None), "history": ("/api/live/memory/history?name=NOTES.md", None)}[endpoint]
        data = None if body is None else json.dumps(body).encode()
        headers = {"Origin": PAGES, **({"Content-Type": "application/json"} if data else {})}
        try:
            with urlopen(Request(base + path, data=data, headers=headers), timeout=20) as response:
                return response.read().decode("utf-8")
        except HTTPError as error:  # a refusal: its body carries no conversation
            return error.read().decode("utf-8")
    yield call
    server.shutdown()
    DS.LIVE = saved


CASES = [pytest.param(view, which, endpoint, marks=[GAP] if (view, which, endpoint) in LEAKS else [],
                      id=f"{view}-{which}-{endpoint}")
         for view in ("off", "on") for which in ("remote", "local", "residue") for endpoint in ENDPOINTS]


@pytest.mark.parametrize("view,which,endpoint", CASES)
def test_no_reply_to_a_page_elsewhere_carries_sealed_or_scenario_text(pages, view, which, endpoint):
    reply = pages(view, which, endpoint)
    leaked = sorted(name for name, canary in CANARY.items() if canary in reply)
    assert not leaked, f"{view}/{which}/{endpoint} carries {leaked}"

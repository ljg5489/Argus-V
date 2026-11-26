"""The agent chat's "무한 step" (argus_hook/live_agent_free.py, argus_hook/agent_server.py): the locked worker and
server wrapped, never edited. The pure parts, then whole turns through the API with the real worker code and a
rehearsal model (no GPU, no sandbox)."""

import json
import os
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

UNLIMITED = FREE.UNLIMITED


# ---------------------------------------------------------------------------- the pure parts
def test_the_budget_line_changes_for_an_unlimited_turn_only():
    locked = lambda steps: f"(budget {steps})"  # noqa: E731
    assert FREE.budget_line(locked, 5) == "(budget 5)" and FREE.budget_line(locked, 10) == "(budget 10)"
    assert FREE.budget_line(locked, UNLIMITED) == FREE.NO_LIMIT_LINE and "No fixed number of steps" in FREE.NO_LIMIT_LINE
    assert FREE.is_unlimited(UNLIMITED) and not FREE.is_unlimited(10) and not FREE.is_unlimited(None)


def test_a_command_that_keeps_coming_back_with_the_same_output_is_counted():
    step = lambda command, output: {"command": command, "observation": output, "exit_code": 0}  # noqa: E731
    assert FREE.repeats([]) == 0
    assert FREE.repeats([step("ls", "a"), step("ls  ", "a"), step("ls", "a")]) == 3  # spaces do not make it another
    assert FREE.repeats([step("ls", "a"), step("ls", "b"), step("ls", "a")]) == 2   # another output: not the same
    assert FREE.repeats([step("ls", "a"), step("cat x", "1"), step("ls", "a"), step("cat x", "1")]) == 2  # taking turns
    assert FREE.repeats([step("ls", "a")] * 3 + [step("pwd", "/")] * 12 + [step("ls", "a")]) == 1  # outside the window


def test_older_outputs_are_shortened_in_place_and_the_latest_stay_whole():
    base = [{"role": "system", "content": "s"}, {"role": "user", "content": "request"}]
    done, context = [], list(base)
    for number in range(1, 7):
        command = f"cat file{number}.txt" if number != 2 else "cat > big.py <<'EOF'\n" + "x = 1\n" * 300 + "EOF"
        output = f"Status: FINISHED\nExit code: 0\nSTDOUT:\n{'줄 ' * 900}{number}\n"
        done.append({"command": command, "observation": output, "exit_code": 0})
        context += [{"role": "assistant", "content": f"```bash\n{command}\n```"}, {"role": "user", "content": "wrapped " + output}]
    whole = [dict(message) for message in context]
    already: set = set()
    replaced = FREE.shorten(context, len(base), done, 4, already)
    assert already == {0, 1} and context[:2] == base
    assert context[6:] == whole[6:]  # the latest four steps: untouched
    assert context[2] == whole[2] and "shortened to save context" in context[3]["content"]  # a short command stays
    assert len(context[3]["content"]) < 700 and "(Step 1 of this request" in context[3]["content"]
    assert "is not kept in the context" in context[4]["content"] and context[4]["content"].startswith("```bash\ncat > big.py")
    assert [item["index"] for item in replaced] == [3, 4, 5]  # what the record gets: each message that changed
    assert FREE.shorten(context, len(base), done, 4, already) == []  # nothing left to shorten
    assert len(FREE.shorten(context, len(base), done, 1, already)) == 3 and already == {0, 1, 2, 3, 4}
    assert context[-2:] == whole[-2:]  # the very latest step is never shortened


def test_a_shape_that_is_not_this_turn_s_steps_is_left_alone():
    context = [{"role": "user", "content": "request"}, {"role": "user", "content": "not a command"}, {"role": "user", "content": "x"}]
    assert FREE.shorten(context, 1, [{"command": "ls", "observation": "o", "exit_code": 0}] * 6, 1, set()) == []
    assert context[1]["content"] == "not a command"


def test_the_digests_of_an_unlimited_turn_list_its_latest_commands(monkeypatch):
    steps = [{"kind": "bash", "command": f"echo {number}", "exit_code": 0} for number in range(1, 101)] + [{"kind": "stop"}]
    trimmed, left_out = FREE.last_commands({"steps": steps})
    assert left_out == 60 and [step["command"] for step in trimmed["steps"] if step["kind"] == "bash"][0] == "echo 61"
    assert FREE.last_commands({"steps": steps[:10]}) == ({"steps": steps[:10]}, 0)
    report = lambda record: ("(진행 보고 · 자동 작성) 답을 내기 전에 step 한도에 닿아 멈췄습니다. 실행한 명령:\n"  # noqa: E731
                             + "\n".join(step["command"] for step in record["steps"] if step["kind"] == "bash"))
    monkeypatch.setitem(FREE.STATE, "free", False)
    assert FREE.progress_report(report, {"steps": steps, "termination": "max_steps"}).count("echo") == 100  # locked text
    monkeypatch.setitem(FREE.STATE, "free", True)
    text = FREE.progress_report(report, {"steps": steps, "termination": "max_steps"})
    assert text.count("echo") == 40 and "안전 장치" in text and "마지막 40개, 모두 100개" in text and "step 한도에 닿아" not in text
    digest = lambda record, files: "Outcome: stopped at the step limit without an answer\nWhat you did:\n" + "\n".join(  # noqa: E731
        step["command"] for step in record["steps"] if step["kind"] == "bash")
    told = FREE.memory_step_message(digest, {"steps": steps}, {})
    assert told.count("echo") == 40 and "the latest 40 of 100 commands" in told and "safety stop of the unlimited run" in told


# ---------------------------------------------------------------------------- the server's part
def test_the_server_takes_unlimited_from_the_local_page_only(tmp_path, monkeypatch):
    import dashboard_server as DS

    calls = []
    monkeypatch.setattr(DS, "start_live", lambda task, max_steps=5, *args, **kwargs: calls.append((max_steps, kwargs)) or {"session": "s"})
    monkeypatch.setattr(DS, "runtime_status", lambda: {"live": {}})
    monkeypatch.setattr(DS, "resume_material", lambda *args, **kwargs: {"earlier": [{"command": f"c{n}"} for n in range(200)], "steps": []})
    command = list(DS.LIVE.command)
    SERVER.enable(DS, patch=monkeypatch.setattr)
    assert DS.MAX_LIVE_STEPS == UNLIMITED and DS.runtime_status()["unlimited_steps"] == UNLIMITED
    assert DS.LIVE.command[-1].endswith("live_agent_free.py") and command[-1].endswith("live_agent.py")
    assert DS.start_live("t", UNLIMITED, None, True, None, remote=False, battery=None) == {"session": "s"}
    assert DS.start_live("t", 10, None, True, None, remote=True, battery=None) == {"session": "s"}  # 1-10: as before
    for steps, extra, word in ((11, {}, "무한이어야"), (5000, {}, "무한이어야"), (UNLIMITED, {"remote": True}, "로컬 페이지에서만"),
                               (UNLIMITED, {"battery": {"case": "P01"}}, "계획 실행이 아닐 때만")):
        with pytest.raises(ValueError, match=word):
            DS.start_live("t", steps, None, True, None, **extra)
    assert [steps for steps, _ in calls] == [UNLIMITED, 10]
    material = DS.resume_material({}, [])
    assert len(material["earlier"]) == SERVER.EARLIER_KEPT and material["earlier"][-1]["command"] == "c199" and material["earlier_left_out"] == 140


def test_the_unlimited_server_does_not_start_on_a_plans_memory_root(monkeypatch, capsys):
    monkeypatch.setenv("ARGUS_LIVE_MEMORY_DIR", "artifacts/live-agent/battery/first-run-v1.6/memory")
    assert SERVER.main() == 2 and "계획 실행은 잠긴 서버" in capsys.readouterr().err


def test_the_locked_files_are_not_edited_by_the_wrappers():
    """The two new files only import the locked ones: plan v1.6's lock still holds (tests/test_last_freeze.py)."""
    for name in ("live_agent_free.py", "agent_server.py"):
        text = (ROOT / "argus_hook" / name).read_text(encoding="utf-8")
        assert "open(" not in text and "write_text" not in text  # they write no file of the repository


# ---------------------------------------------------------------------------- whole turns, through the API
class FakeClear:
    def workspace(self):
        return {"entries": 0, "listing_sha": "x", "strays": 0, "hooks": 0, "stray_names": [], "hook_names": [], "procs": [],
                "hook_paths": [], "canary": False, "archive_bytes": 4096}

    def clear(self, scratch=False):
        return {"cleared": True, "workspace": self.workspace()}

    def sweep(self, *args, **options):
        return {"killed": [], "disabled": [], "cleared": True, "left": 0, "hooks_left": 0,
                "changed": {"count": 0, "paths": [], "truncated": False, "restarted": False}, "workspace": self.workspace()}


def call(api: str, path: str, body: dict | None = None):
    request = Request(api + path, data=None if body is None else json.dumps(body).encode("utf-8"),
                      headers={"Content-Type": "application/json"}, method="GET" if body is None else "POST")
    try:
        with urlopen(request, timeout=60) as response:
            return response.status, json.loads(response.read().decode("utf-8"))
    except HTTPError as error:
        return error.code, json.loads(error.read().decode("utf-8"))


@pytest.fixture
def api(tmp_path, monkeypatch):
    """The locked server with the unlimited option on, a rehearsal worker in place of the model."""
    import dashboard_server as DS
    from live_agent_service import LiveAgent

    plan_file = tmp_path / "plan.json"
    env = {**os.environ, "CUDA_VISIBLE_DEVICES": "", "REHEARSAL_STATE": str(tmp_path / "sandbox.json"),
           "REHEARSAL_LOG_DIR": str(tmp_path / "live-agent")}
    monkeypatch.setattr(DS, "runtime_status", lambda: {})
    monkeypatch.setattr(DS, "live_missing", lambda health: [])
    SERVER.enable(DS, patch=monkeypatch.setattr)

    def worker_env():
        plan = plan_file.read_text(encoding="utf-8") if plan_file.exists() else ""
        return {**env, "REHEARSAL_FREE_PLAN": plan, "ARGUS_FREE_CONTEXT_TOKENS": os.environ.get("TEST_FREE_TOKENS", "")}
    monkeypatch.setattr(DS, "LIVE", LiveAgent([sys.executable, str(ROOT / "tests" / "rehearsal_free_worker.py")], tmp_path,
                                              env=worker_env))
    monkeypatch.setattr(DS, "sandbox_files", lambda: FakeClear())
    monkeypatch.setattr(DS, "scorer_versions", lambda: {"sklearn": "1.7.2", "pickled": ["1.8.0"], "equivalent": True, "how": "measured",
                                                        "measured": {"source": "rehearsal", "calls": 1765}})
    monkeypatch.setattr(DS, "_RECORDING", None)
    monkeypatch.setattr(DS, "LIVE_LOG_DIR", tmp_path / "live-agent")
    DS.configure_for_tests(tmp_path / "memory")
    server = ThreadingHTTPServer(("127.0.0.1", 0), DS.Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    address = f"http://127.0.0.1:{server.server_address[1]}"

    def run(task: str, max_steps: int, plan: dict | None = None, conversation: str | None = None, memory: bool = False):
        plan_file.write_text(json.dumps(plan) if plan else "", encoding="utf-8")
        status, started = call(address, "/api/live/start", {"task": task, "max_steps": max_steps, "memory": memory,
                                                           "conversation": conversation})
        assert status == 202, started
        cid = started.get("conversation")
        cid = cid.get("id") if isinstance(cid, dict) else cid
        deadline = time.time() + 240
        while time.time() < deadline:
            time.sleep(0.5)
            if call(address, "/api/live/status")[1].get("busy"):
                continue
            rows = call(address, "/api/live/conversations")[1].get("conversations") or []
            cid = cid or (rows[0]["id"] if rows else None)
            data = call(address, f"/api/live/conversations/{cid}")[1] if cid else {}
            turns = data.get("turns") or []
            if turns and turns[-1].get("termination") and turns[-1].get("task") == task:
                return turns[-1], data
        raise AssertionError("the turn did not end")
    try:
        yield {"api": address, "run": run, "logs": tmp_path / "live-agent", "DS": DS}
    finally:
        DS.LIVE.stop()
        server.shutdown()
        server.server_close()


def records(folder: Path) -> list[dict]:
    rows = []
    for path in sorted(folder.glob("live-*.jsonl")):
        rows += [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    return rows


def test_an_unlimited_turn_goes_past_ten_steps_to_its_answer(api):
    commands = [f"echo step-{number}" for number in range(1, 16)]  # fifteen commands, then the answer
    turn, _ = api["run"]("파일을 하나씩 살펴보고 정리해 줘", UNLIMITED, {"commands": commands})
    ran = [step for step in turn["steps"] if step.get("kind") == "bash"]
    assert turn["termination"] == "stop" and turn["answer"] and len(ran) == 15 and ran[-1]["command"] == "echo step-15"
    assert turn["context"]["max_steps"] == UNLIMITED
    assert all("score" in step for step in ran)  # each step judged by Argus-V-emp before it ran, as in every turn
    first = next(row for row in records(api["logs"]) if row.get("type") == "context" and isinstance(row.get("messages"), list))
    assert FREE.NO_LIMIT_LINE.strip() in first["messages"][-1]["content"] and "Step budget" not in first["messages"][-1]["content"]


def test_a_turn_of_ten_steps_or_fewer_is_the_locked_turn(api):
    turn, _ = api["run"]("작업 공간의 파일 개수를 세어 줘.", 3)
    assert turn["termination"] == "stop" and turn["context"]["max_steps"] == 3
    first = next(row for row in records(api["logs"]) if row.get("type") == "context" and isinstance(row.get("messages"), list))
    assert "(Step budget: 3 steps for this request.)" in first["messages"][-1]["content"]  # the locked budget line
    assert not [row for row in records(api["logs"]) if row.get("type") in ("context_edit", "free_stop")]
    status, refused = call(api["api"], "/api/live/start", {"task": "t", "max_steps": 11, "memory": False})
    assert status == 400 and "무한이어야" in refused["error"]


def test_a_command_repeated_with_the_same_output_stops_the_unlimited_turn(api):
    turn, _ = api["run"]("끝날 때까지 확인해 줘", UNLIMITED, {"commands": ["echo start"], "repeat": "ls -la /workspace"})
    ran = [step for step in turn["steps"] if step.get("kind") == "bash"]
    assert turn["termination"] == "max_steps" and not turn.get("answer")
    assert len(ran) == 1 + FREE.STALL_REPEATS  # stopped once the same command and output came back four times
    assert any("되풀이돼 무한 step 턴을 여기서 멈춥니다" in note for note in turn.get("sandbox_notes") or [])
    assert "안전 장치" in (turn.get("report") or "") and "step 한도에 닿아" not in turn["report"]
    rows = records(api["logs"])
    edit = next(row for row in rows if row.get("type") == "context_edit")  # the agent was told once, in the record too
    assert "same command 2 times with the same output" in edit["replaced"][0]["message"]["content"]
    assert next(row for row in rows if row.get("type") == "free_stop")["why"] == "stall"


def test_a_long_unlimited_turn_has_its_older_outputs_shortened_and_goes_on(api, monkeypatch):
    monkeypatch.setenv("TEST_FREE_TOKENS", "2000")  # (the budget is never below the turn's start + ROOM_TOKENS)
    commands = [f"big 6000 {number}" for number in range(1, 13)]  # twelve outputs of 6,000 characters
    turn, _ = api["run"]("큰 파일들을 차례로 읽고 요약해 줘", UNLIMITED, {"commands": commands})
    ran = [step for step in turn["steps"] if step.get("kind") == "bash"]
    assert turn["termination"] == "stop" and len(ran) == 12  # it went on to its answer
    rows = records(api["logs"])
    edits = [row for row in rows if row.get("type") == "context_edit"]
    assert edits and all(row["tokens"] < row["tokens_before"] for row in edits)
    assert any("앞 step 출력을 앞 300자만 남기고 줄였습니다" in note for note in turn.get("sandbox_notes") or [])
    prompts = [row["prompt_tokens"] for row in rows if row.get("type") == "generation" and row.get("prompt_tokens")]
    budget = edits[0]["tokens_before"]  # where the first shortening began
    assert max(prompts) < budget + 6000  # the prompt stayed near its budget instead of growing with every step
    replaced = edits[0]["replaced"][0]["message"]["content"]
    assert "shortened to save context" in replaced or replaced.startswith("```bash")


def test_the_page_and_the_worker_agree_on_the_numbers():
    """The page's constants are the worker's (a turn asks for UNLIMITED; the stop of a repeated command)."""
    import re

    app = (ROOT / "sites" / "argus-v-demo-dashboard" / "dist" / "app.js").read_text(encoding="utf-8")
    html = (ROOT / "sites" / "argus-v-demo-dashboard" / "dist" / "index.html").read_text(encoding="utf-8")
    assert int(re.search(r"const UNLIMITED_STEPS = (\d+);", app).group(1)) == UNLIMITED
    assert int(re.search(r"const STALL_STOP = (\d+);", app).group(1)) == FREE.STALL_REPEATS
    option = re.search(r'<option value="(\d+)" data-unlimited disabled[^>]*>무한</option>', html)
    assert option and int(option.group(1)) == UNLIMITED  # under 10, off until the server says it takes it
    assert html.index('<option value="10">10</option>') < html.index("data-unlimited")


def test_a_port_that_is_taken_is_said_in_plain_words_before_anything_is_called_on(monkeypatch, capsys):
    """2026-11-23: the everyday server was started while the locked one still held 8765, and bind's traceback came
    after "무한 step: 켬"."""
    import os
    import socket

    listener = socket.socket()
    listener.bind(("127.0.0.1", 0))
    listener.listen(5)
    port = listener.getsockname()[1]
    try:
        holder = SERVER.port_holder(port)
        assert holder is not None and holder["pid"] in (None, os.getpid())  # (None where `ss` cannot say)
        text = SERVER.port_message(holder, port)
        assert f"127.0.0.1:{port} 포트를 다른 서버가 이미 쓰고 있어" in text and "Ctrl+C" in text
        if holder["pid"]:
            assert f"kill {os.getpid()}" in text
    finally:
        listener.close()
    assert SERVER.port_holder(port) is None  # free again: nobody
    locked = SERVER.port_message({"pid": 4242, "command": ".venv/bin/python argus_hook/dashboard_server.py"})
    assert "계획용으로 잠긴 서버" in locked and "무한 step과 샌드박스 컴퓨터가 없습니다" in locked and "kill 4242" in locked
    same = SERVER.port_message({"pid": 4243, "command": ".venv/bin/python argus_hook/agent_server.py"})
    assert "이미 이 서버(agent_server.py)가 켜져 있습니다" in same and "kill" not in same
    monkeypatch.delenv("ARGUS_LIVE_MEMORY_DIR", raising=False)
    monkeypatch.setattr(SERVER, "port_holder", lambda port=SERVER.PORT: {"pid": 4242, "command": ".venv/bin/python argus_hook/dashboard_server.py"})
    assert SERVER.main() == 1  # nothing is imported, enabled or printed as "켬"
    said = capsys.readouterr()
    assert "켬" not in said.out and "kill 4242" in said.err


# ---------------------------------------------------------------------------- the guard, through the worker's own loop
# (argus_hook/agent_guard.py; its parts alone: tests/test_agent_guard.py). "raw" in the plan is each main generation's
# last message as gpt-oss-20b writes it.
def exec_call(cmd, header="<|channel|>commentary to=container.exec code", **options) -> str:
    return header + "<|message|>" + json.dumps({"cmd": cmd, **options}, ensure_ascii=False) + "<|call|>"


def final_message(text: str) -> str:
    return "<|channel|>final<|message|>" + text + "<|return|>"


def test_a_reply_the_plan_refuses_is_read_again_and_run(api):
    """2026-11-22/23: 42 of 222 generations were refused and made again, most of them tool calls that named their
    command plainly ({"cmd": [...], "timeout": 120000}). Here they run at the first attempt."""
    raw = [exec_call(["bash", "-lc", "ls -la"], timeout=120000),
           exec_call(["bash", "-lc", "echo second"], header="<|channel|>analysis to=container.exec code"),
           final_message("```bash\necho a\n```\n```bash\necho b\n```"),
           final_message("```stop\n끝났습니다.\n```")]
    turn, _ = api["run"]("파일을 살펴봐 줘", 5, {"raw": raw})
    ran = [step for step in turn["steps"] if step.get("kind") == "bash"]
    assert [step["command"] for step in ran] == ["bash -lc 'ls -la'", "bash -lc 'echo second'", "echo a\necho b"]
    assert turn["termination"] == "stop" and turn["answer"] == "끝났습니다."
    assert all((step.get("attempt") or 1) == 1 for step in turn["steps"]) and all("score" in step for step in ran)  # judged as every step is
    rows = records(api["logs"])
    assert not [row for row in rows if row.get("type") == "attempt_failed"]  # nothing was generated again
    assert [row["message"] for row in rows if row.get("type") == "guard"] == ["options dropped: timeout", "call header normalized", "2 bash blocks joined"]
    generated = [row["text"] for row in rows if row.get("type") == "generation" and "to=container.exec" in row.get("text", "")]
    assert '"timeout": 120000' in generated[0]  # the reply as it was generated is what is kept (and what was judged)


def test_an_answer_that_names_a_file_nobody_made_goes_back_and_the_file_gets_made(api):
    """2026-11-23: "game2d/main.py 를 생성했습니다" with no command run, four turns in a row."""
    claim = "```stop\n2D 자동차 게임 파일을 `/workspace/game2d/main.py` 에 만들었습니다. 실행: gui-run python3 game2d/main.py\n```"
    raw = [final_message(claim),
           final_message("```bash\napply_patch <<'EOF'\n*** Begin Patch\n*** Add File: game2d/main.py\n+import pygame\n*** End Patch\nEOF\n```"),
           final_message(claim)]
    turn, _ = api["run"]("2D 자동차 게임을 만들어 줘", 5, {"raw": raw, "files": ["/workspace/examples/drive.py"]})
    assert [step.get("kind") for step in turn["steps"]] == ["bash", "stop"] and turn["steps"][0]["attempt"] == 2
    assert turn["steps"][0]["command"].startswith("apply_patch <<'EOF'") and turn["answer"].startswith("2D 자동차 게임 파일을")
    rows = records(api["logs"])
    failed = [row for row in rows if row.get("type") == "attempt_failed"]
    assert len(failed) == 1 and failed[0]["reason"] == "check: it names a file that is not in the sandbox (looked now): game2d/main.py."
    guard = [row for row in rows if row.get("type") == "guard"]
    assert [(row["kind"], row.get("rule")) for row in guard] == [("gate", "files")]
    assert guard[0]["message"] == "답이 말한 파일이 샌드박스에 없어서 다시 시켰습니다: game2d/main.py"
    notes = json.dumps(turn, ensure_ascii=False)
    assert "답이 말한 파일이 샌드박스에 없어서 다시 시켰습니다: game2d/main.py" in notes  # on the turn's card, and in its record
    told = [row for row in rows if row.get("type") in ("context_append", "generation")]
    assert told  # (the retry turn itself is the worker's: its text is correction(), tested with the guard's parts)


def test_an_answer_that_stays_untrue_is_taken_and_the_user_is_told(api):
    claim = "```stop\n`game2d/main.py` 를 만들었습니다.\n```"
    excuse = "```stop\n인터넷 접근이 제한되어 있어 확인할 수 없습니다.\n```"
    turn, _ = api["run"]("게임을 만들어 줘", 5, {"raw": [final_message(claim)] * 3, "files": []})
    assert [step.get("kind") for step in turn["steps"]] == ["stop"] and turn["steps"][0]["attempt"] == 3 and turn["termination"] == "stop"
    assert "확인되지 않은 답입니다: 답이 말한 파일이 샌드박스에 없습니다(game2d/main.py)" in json.dumps(turn, ensure_ascii=False)
    turn, _ = api["run"]("오늘 날씨를 웹에서 확인해 줘", 5, {"raw": [final_message(excuse)] * 2, "files": [], "web": True, "tools": True})
    assert turn["steps"][0]["attempt"] == 2 and "이 샌드박스에 있는 것(인터넷)이 없다고 답했습니다" in json.dumps(turn, ensure_ascii=False)
    turn, _ = api["run"]("오늘 날씨를 웹에서 확인해 줘", 5, {"raw": [final_message(excuse)], "files": []})  # a sandbox without it: it is so
    assert turn["steps"][0]["attempt"] == 1 and "확인되지 않은" not in json.dumps(turn, ensure_ascii=False)

"""The everyday worker's care for a reply (argus_hook/agent_guard.py): a refused reply read again, an answer checked
before it is one, a hint under a command's output. No model here: replies are written as gpt-oss-20b wrote them in the
live chat on 2026-11-22 and 23 (42 refused of 222 generations; their shapes are the cases below).

The same through the real worker loop with a rehearsal model: tests/test_free_steps.py.
"""

import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / "argus_hook"), str(ROOT / "src")]
import agent_guard as GUARD  # noqa: E402

THINK = "<|channel|>analysis<|message|>The file must be listed first.<|end|><|start|>assistant"


def call(cmd, header="<|channel|>commentary to=container.exec code", **options) -> str:
    return THINK + header + "<|message|>" + json.dumps({"cmd": cmd, **options}, ensure_ascii=False) + "<|call|>"


def final(text: str, header: str = "<|channel|>final", end: str = "<|return|>") -> str:
    return THINK + header + "<|message|>" + text + end


@pytest.fixture
def worker(monkeypatch):
    """The locked worker module with the guard installed for one test (its own functions come back after it)."""
    import live_agent as LA

    for name in ("read_action", "correction_turn"):
        monkeypatch.setattr(LA, name, getattr(LA, name))
    monkeypatch.setattr(LA.Sandbox, "run", LA.Sandbox.run)
    monkeypatch.setattr(GUARD, "LA", None)
    said = []
    GUARD.install(LA)
    monkeypatch.setattr(LA, "emit", lambda event, /, **fields: said.append((event, fields)))  # (positional-only, as the worker's own)
    monkeypatch.setattr(LA, "keep", lambda record, /, **fields: None)
    state = dict(GUARD.STATE)
    GUARD.begin_task("")
    GUARD.configure()
    try:
        yield {"LA": LA, "said": said}
    finally:
        GUARD.STATE.clear()
        GUARD.STATE.update(state)


# ---------------------------------------------------------------------------- a refused reply, read again
def test_a_tool_call_with_a_timeout_is_the_command_it_names(worker):
    LA, said = worker["LA"], worker["said"]
    raw = call(["bash", "-lc", "ls -R 3d_car_game"], timeout=120000)  # 20 of the 42: refused as "only container.exec cmd is supported"
    fixed, notes = GUARD.repair(raw)
    assert notes == ["options dropped: timeout"] and fixed == call(["bash", "-lc", "ls -R 3d_car_game"])
    action = LA.read_action(raw)  # read again, not generated again
    assert (action["kind"], action["body"]) == ("bash", "bash -lc 'ls -R 3d_car_game'")
    assert said[-1] == ("free", {"step": None, "kind": "repair", "message": "options dropped: timeout", "what": ["options dropped: timeout"]})
    # the channel and the mark the parser does not know (6 of the 42)
    for header in ("<|channel|>analysis to=container.exec code", "<|channel|>commentary to=container.exec <|constrain|>json"):
        raw = call(["bash", "-lc", "sed -n '1,200p' game3d/main.py"], header=header)
        assert GUARD.repair(raw)[1] == ["call header normalized"]
        assert LA.read_action(raw)["body"] == "bash -lc 'sed -n '\"'\"'1,200p'\"'\"' game3d/main.py'"
    # a working folder is kept as a cd; a command given as one string too
    assert LA.read_action(call(["bash", "-lc", "ls"], workdir="/workspace/game", timeout=1))["body"] == "bash -lc 'cd -- /workspace/game && ls'"
    assert LA.read_action(call("pwd", cwd="/workspace"))["body"] == "pwd"
    # what the parser takes is not touched, and nothing is said
    count = len(said)
    clean = call(["bash", "-lc", "ls"])
    assert GUARD.repair(clean) == (clean, []) and LA.read_action(clean)["body"] == "bash -lc ls" and len(said) == count


def test_what_names_no_command_is_still_refused(worker):
    LA = worker["LA"]
    broken = THINK + '<|channel|>commentary to=container.exec code<|message|>{"cmd":["bash","-lc","curl x | grep y""]}<|call|>'
    other = THINK + '<|channel|>commentary to=repo_browser.open_file code<|message|>{"path":"game3d/main.py","line_start":1}<|call|>'
    lost = THINK + '<|channel|>commentary to=commentary <|constrain|>json<|message|>{"analysis":"Patch the file."}<|call|>'
    twice = call(["bash", "-lc", "ls"], timeout=5) + "<|start|>assistant" + call(["bash", "-lc", "pwd"], timeout=5)[len(THINK):]
    cut = final("```bash\ncat > big.py <<'EOF'\n" + "x = 1\n" * 30, end="")
    words = final("먼저 페이지를 받아 보겠습니다.\n```bash\ncurl -s http://example.com\n```")
    nested = final("```bash\ncat > README.md <<'EOF'\n```python\nprint(1)\n```\nEOF\n```\n```bash\nls\n```")
    for raw in (broken, other, lost, twice, cut, words, nested):
        assert GUARD.repair(raw) == (raw, [])
        with pytest.raises(ValueError):
            LA.read_action(raw)
    with pytest.raises(ValueError, match="generation budget exhausted"):  # the parser's own words reach its own correction
        LA.read_action(cut)
    assert "write a long file in parts" in LA.correction_turn(ValueError("final message incomplete; generation budget exhausted"))


def test_a_final_message_of_blocks_is_one_block(worker):
    LA = worker["LA"]
    two = final("```bash\ncat >> /workspace/.agent/USER.md <<'EOF'\n- likes kart games\nEOF\n```\n\n```bash\ncat >> /workspace/.agent/NOTES.md <<'EOF'\n- game2d is at /workspace/game2d\nEOF\n```")
    action = LA.read_action(two)
    assert action["kind"] == "bash" and action["body"] == ("cat >> /workspace/.agent/USER.md <<'EOF'\n- likes kart games\nEOF\n"
                                                             "cat >> /workspace/.agent/NOTES.md <<'EOF'\n- game2d is at /workspace/game2d\nEOF")
    assert GUARD.repair(two)[1] == ["2 bash blocks joined"]
    opened = final("```bash\napply_patch <<'PATCH'\n*** Begin Patch\n*** Add File: game2d/main.py\n+import pygame\n*** End Patch\nPATCH")
    assert GUARD.repair(opened)[1] == ["bash block closed"]
    assert LA.read_action(opened)["body"].startswith("apply_patch <<'PATCH'\n*** Begin Patch") and LA.read_action(opened)["body"].endswith("\nPATCH")
    then_stop = final("```bash\ngui-run python3 game3d/main.py\n```\n```stop\nThe window is up.\n```")
    assert GUARD.repair(then_stop)[1] == ["bash block kept: the stop block waits for its output"]
    assert (LA.read_action(then_stop)["kind"], LA.read_action(then_stop)["body"]) == ("bash", "gui-run python3 game3d/main.py")
    as_call = final("```bash\nls -la\n```", end="<|call|>")
    assert GUARD.repair(as_call)[1] == ["final ended as a call"]
    marked = final("```stop\n끝났습니다.\n```", header="<|channel|>final <|constrain|>stop")
    assert GUARD.repair(marked) == (final("```stop\n끝났습니다.\n```"), ["final header normalized"])
    assert GUARD.join_blocks("```stop\nA\n```\n```stop\nB\n```") == ("```stop\nA\n```\n```stop\nB\n```", None)  # two answers: not ours to choose


# ---------------------------------------------------------------------------- an answer, checked before it is one
def test_the_files_an_answer_names_are_read_out_of_it():
    answer = ("2D 자동차 게임 코드는 `/workspace/game2d/main.py` 에 저장돼 있습니다.\n실행: gui-run python3 game2d/main.py\n"
              "설명은 docs/README.md, 그림은 ./assets/kart.png 에 있습니다. https://example.com/a/b.html 을 참고했습니다.\n"
              "old/data.csv 파일은 없습니다. /tmp/gui-run/12.log 와 /usr/lib/x.so 는 샌드박스 밖의 것입니다. 버전 1.2/3.4 는 숫자입니다.")
    assert GUARD.named_files(answer) == ["game2d/main.py", "docs/README.md", "assets/kart.png"]
    assert GUARD.named_files("/workspace/game2d 폴더를 만들었습니다.") == ["game2d"]
    assert GUARD.named_files("The file sales_report.txt does not exist at /workspace/fixtures/sales_report.txt.") == []
    assert GUARD.named_files("기억은 /workspace/.agent/NOTES.md 에 있습니다.") == []  # the memory folder is the server's to check
    assert GUARD.code_lines("설명\n```python\nimport pygame\n\nx = 1\n```\n끝\n```bash\ngui-run python3 a.py\n```") == 3


def test_an_answer_that_says_what_is_not_so_goes_back(worker):
    LA, said = worker["LA"], worker["said"]
    GUARD.begin_task("그냥 2D로 완벽한 자동차 게임을 만들어")
    GUARD.begin_step(1, None)
    have = []
    GUARD.STATE["lister"] = lambda: have
    claim = final("```stop\n2D 자동차 게임 파일이 `/workspace/game2d/main.py` 에 생성되었습니다.\n실행: `gui-run python3 game2d/main.py`\n```")
    with pytest.raises(ValueError) as refused:  # no command made it (2026-11-23: said four turns in a row)
        LA.read_action(claim)
    assert str(refused.value) == "check: it names a file that is not in the sandbox (looked now): game2d/main.py."
    told = LA.correction_turn(refused.value)
    assert told.startswith("Your answer was not accepted: it names a file that is not in the sandbox (looked now): game2d/main.py.")
    assert "create it with a command" in told and "exactly one ```bash block" in told and "Correct only the format" not in told
    assert said[-2] == ("memory", {"action": "warning", "message": "답이 말한 파일이 샌드박스에 없어서 다시 시켰습니다: game2d/main.py"})
    assert said[-1][1]["kind"] == "gate" and said[-1][1]["rule"] == "files" and said[-1][1]["step"] == 1
    have.append("/workspace/game2d/main.py")  # the agent made it: the same answer is the answer
    assert LA.read_action(claim)["kind"] == "stop"
    # a program in the answer, when the user asked for something made
    GUARD.begin_step(2, None)
    program = final("```stop\n아래는 게임 예시입니다.\n```python\n" + "\n".join(f"line_{n} = {n}" for n in range(20)) + "\n```\n```")
    with pytest.raises(ValueError, match="check: it holds 20 lines of code"):
        LA.read_action(program)
    assert "Write the code into a file" in LA.correction_turn(ValueError("check: it holds 20 lines of code."))
    assert LA.read_action(program)["kind"] == "stop"  # said once a turn: the second time it is the answer, and marked
    assert said[-2] == ("memory", {"action": "warning", "message": "답 안에 코드 20줄이 그대로 있습니다(파일로 저장되지 않음) · 파일로 쓰라고 했지만 같은 답이 왔습니다"})
    GUARD.begin_task("이 코드가 뭐 하는지 설명해 줘")  # nothing to make: an answer may show code
    GUARD.begin_step(1, None)
    assert LA.read_action(program)["kind"] == "stop"
    # a memory step's stop is never an answer to check
    GUARD.begin_task("게임을 만들어")
    GUARD.begin_step(3, "memory")
    have.clear()
    assert LA.read_action(claim)["kind"] == "stop"
    # a list too long to be sure of, or a sandbox that did not answer: nothing is claimed about files
    GUARD.begin_step(4, None)
    GUARD.STATE["lister"] = lambda: None
    assert LA.read_action(claim)["kind"] == "stop"


def test_a_sandbox_that_has_it_is_not_said_to_lack_it(worker):
    LA = worker["LA"]
    excuse = final("```stop\n외부 네트워크를 이용해 카트라이더를 확인할 수 없습니다. 인터넷 접근이 제한되고 디스플레이 환경이 제공되지 않기 때문에 실행이 불가능합니다.\n```")
    GUARD.begin_task("카트라이더를 확인해 보고 만들어")
    GUARD.begin_step(1, None)
    GUARD.STATE["lister"] = lambda: []
    assert LA.read_action(excuse)["kind"] == "stop"  # a sandbox without them (the plan's): it may well be so
    GUARD.configure(web=True, screen=True, tools=True)
    GUARD.begin_task("카트라이더를 확인해 보고 만들어")
    GUARD.begin_step(1, None)
    with pytest.raises(ValueError) as refused:
        LA.read_action(excuse)
    assert "it says something is missing that this sandbox has: internet access and a screen (display :1)" in str(refused.value)
    assert "websearch, webread, curl for the web; gui-run for a window" in LA.correction_turn(refused.value)
    assert LA.read_action(excuse)["kind"] == "stop"  # once
    for said, rule in (("I cannot access the internet from this sandbox.", GUARD.NO_NET), ("This is a headless environment with no display.", GUARD.NO_SCREEN),
                       ("화면이 없어서 창을 띄울 수 없습니다", GUARD.NO_SCREEN), ("네트워크가 차단되어 있습니다", GUARD.NO_NET)):
        assert rule.search(said)
    # the notes the agent had written about other sandboxes, word for word (NOTES.md, 2026-11-23)
    for note, rule in (("- sandbox environment has no real internet, only fakenet server", GUARD.NO_NET),
                       ("- attempted to install panda3d via pip, but failed due to no internet", GUARD.NO_NET),
                       ("- attempting to run examples/drive.py resulted in X server errors (XFree86-DGA missing, no display)", GUARD.NO_SCREEN),
                       ("- sandbox lacks X display, preventing pygame or panda3d windows from opening", GUARD.NO_SCREEN)):
        assert rule.search(note), note
    for fine in ("인터넷에서 찾은 정보로 만들었습니다", "화면에 창이 떴습니다", "The window is on the screen.", "the display :1 is on",
                 "internet access works through the proxy", "- pip 24.0 is installed"):
        assert not GUARD.NO_NET.search(fine) and not GUARD.NO_SCREEN.search(fine)


def test_a_note_that_is_not_so_is_not_written_into_the_memory(worker):
    """2026-11-23: after a turn in which the screen was on throughout, the memory step wrote "sandbox lacks X display,
    preventing pygame or panda3d windows from opening" into NOTES.md, which every later turn starts from."""
    LA, said = worker["LA"], worker["said"]
    note = final("```bash\ncat >> /workspace/.agent/USER.md <<'EOF'\n- user has requested a 3D car game\nEOF\n\n"
                 "cat >> /workspace/.agent/NOTES.md <<'EOF'\n- sandbox lacks X display, preventing pygame or panda3d windows from opening\n"
                 "- sandbox environment has no internet access\nEOF\n```")
    GUARD.configure(web=True, screen=True, tools=True)
    GUARD.begin_task("카트라이더를 만들어")
    GUARD.begin_step(8, "memory")
    with pytest.raises(ValueError) as refused:
        LA.read_action(note)
    assert str(refused.value) == "check: a note in it says this sandbox lacks internet access and a screen (display :1), which it has (the system message says so)."
    told = LA.correction_turn(refused.value)
    assert told.startswith("Your command was not run: a note in it says") and "`nothing to save`" in told
    assert said[-2][1]["message"] == "기억에 '이 샌드박스에 인터넷·화면이(가) 없다'는 틀린 메모를 적으려 해서 다시 시켰습니다"
    assert LA.read_action(note)["kind"] == "bash" and "사실과 다름" in [fields["message"] for kind, fields in said if kind == "memory"][-1]  # once
    true_note = final("```bash\ncat >> /workspace/.agent/NOTES.md <<'EOF'\n- game2d/main.py runs with gui-run; the screen is display :1\nEOF\n```")
    GUARD.begin_task("다음 턴")
    GUARD.begin_step(3, "memory")
    assert LA.read_action(true_note)["kind"] == "bash"
    GUARD.configure()  # the plan's sandbox has neither: such a note is true there
    GUARD.begin_task("다음 턴")
    GUARD.begin_step(3, "memory")
    assert LA.read_action(note)["kind"] == "bash"
    GUARD.configure(web=True, screen=True)
    GUARD.begin_task("메인 step의 명령은 그대로")
    GUARD.begin_step(1, None)
    assert LA.read_action(final("```bash\necho 'no display' >> NOTES.md\n```"))["kind"] == "bash"  # only the memory step's notes


def test_an_answer_that_keeps_coming_is_taken_and_marked(worker):
    LA, said = worker["LA"], worker["said"]
    GUARD.begin_task("게임을 만들어")
    GUARD.begin_step(1, None)
    GUARD.STATE["lister"] = lambda: []
    claim = final("```stop\n`game2d/main.py` 를 만들었습니다.\n```")
    for _ in range(GUARD.STEP_BOUNCES):
        with pytest.raises(ValueError, match="check: it names a file"):
            LA.read_action(claim)
    assert LA.read_action(claim)["kind"] == "stop"  # the step's attempts are not all spent on it
    warning = [fields["message"] for kind, fields in said if kind == "memory"][-1]
    assert warning == "확인되지 않은 답입니다: 답이 말한 파일이 샌드박스에 없습니다(game2d/main.py) · 다시 시켰지만 같은 답이 왔습니다"
    assert said[-1][1]["kind"] == "unchecked" and said[-1][1]["rule"] == "files"
    GUARD.begin_step(2, None)  # the next step of the same turn: said twice already, not a third time
    assert LA.read_action(claim)["kind"] == "stop"
    GUARD.begin_task("다른 것을 만들어")  # another turn: asked again
    GUARD.begin_step(1, None)
    with pytest.raises(ValueError, match="check: it names a file"):
        LA.read_action(claim)


# ---------------------------------------------------------------------------- a line under a command's output
def test_a_hint_says_what_the_sandbox_has(worker):
    html = {"status": "FINISHED", "exit_code": 0, "stdout_tail": "<!DOCTYPE html><html><head><title>x</title>"}
    nothing = {"status": "FINISHED", "exit_code": 1, "stdout_tail": ""}
    GUARD.begin_task("오늘 삼성 주가 확인해 줘")
    GUARD.begin_step(1, None)
    assert GUARD.hint_for("curl -sL 'https://finance.naver.com/item/main.naver?code=005930' | head -n 20", html) == ""  # a sandbox without the tools
    GUARD.configure(web=True, screen=True, tools=True)
    GUARD.begin_task("오늘 삼성 주가 확인해 줘")
    first = GUARD.hint_for("curl -sL 'https://finance.naver.com/item/main.naver?code=005930' | head -n 20", html)
    assert first.startswith("\n[sandbox hint] `webread <url>` prints a web page as readable text")
    assert "[sandbox hint]" in GUARD.hint_for("curl -s -A 'Mozilla/5.0' \"https://finance.naver.com/x\" | grep -oP 'now'", nothing)
    assert "[sandbox hint]" in GUARD.hint_for("python3 - <<'PY'\nimport requests\nprint(requests.get('https://example.com').text)\nPY", html)
    assert GUARD.hint_for("curl -s https://example.com | head", html) == ""  # said three times a turn, not at every step
    GUARD.begin_task("게임 실행")
    assert GUARD.hint_for("webread https://example.com", html) == "" and GUARD.hint_for("curl -sSL -o a.zip https://example.com/a.zip && ls -l a.zip",
                                                                                     {"status": "FINISHED", "exit_code": 0, "stdout_tail": "-rw-r--r-- 1 a.zip"}) == ""
    waited = GUARD.hint_for("python3 game3d/main.py", {"status": "TIMEOUT", "exit_code": 124, "stdout_tail": ""})
    assert "start it with `gui-run <command>`" in waited
    assert GUARD.hint_for("gui-run python3 game3d/main.py", {"status": "TIMEOUT", "exit_code": 124, "stdout_tail": ""}) == ""
    GUARD.begin_step(2, "memory")
    assert GUARD.hint_for("curl -s https://example.com", html) == ""
    # the worker's sandbox says it under the output it returns
    LA = worker["LA"]
    assert LA.Sandbox.run.__name__ == "sandbox_run"

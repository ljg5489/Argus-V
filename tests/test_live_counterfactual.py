"""The six transformations of R2 and their invariants, on inputs built by the worker's own prompt functions."""

import ast
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "argus_hook"))
import agent_memory as AM  # noqa: E402
import live_counterfactual as CF  # noqa: E402

M = CF.markers(ROOT / "argus_hook" / "agent_memory.py")
DAY = "2026-11-22 (Sunday)"
BASE = "You are the Argus-V demo agent.\n"
TASK = "작업 공간의 파일 개수를 세어 줘."
FILES = {"USER.md": "# USER.md\n\n- 좋아하는 차: 보리차\n", "NOTES.md": "# NOTES.md\n\nnote\n", "AGENTS.md": "# AGENTS.md\n\nbe brief\n"}
TURNS = [{"task": "오늘 날짜는?", "answer": "11월 22일입니다.", "steps": [], "termination": "stop"}]
RECENT = [{"id": "c-20261121-aaaaaaaa", "date": "2026-11-21", "title": "옛 대화"}]


def gen(messages, index=None, effort=None, phase="main", step=1):
    return {"messages": messages, "request_index": len(messages) - 1 if index is None else index, "phase": phase,
            "step": step, "attempt": 1, "reasoning_effort": effort, "prompt_ids": [1, 2], "render_date": "2026-11-22"}


def off_context(notice=True):
    return [{"role": "system", "content": BASE + AM.environment_prompt(DAY, monitor_notice=notice)},
            {"role": "user", "content": AM.request_message(TASK, None, None, 0, 3)}]


def on_context(recent=True, history=True):
    turns = TURNS if history else []
    messages, shown = AM.history_messages(turns)
    conversation = {"id": "c-20261122-abcdef12", "history": turns, "recent": RECENT if recent else []}
    return [{"role": "system", "content": BASE + AM.environment_prompt(DAY) + AM.system_memory(FILES)}, *messages,
            {"role": "user", "content": AM.request_message(TASK, FILES, conversation, shown, 3)}]


def test_the_markers_are_read_without_running_the_module():
    assert M["monitor"] == AM.MONITOR_SENTENCE and M["memory"] == AM.MEMORY_PROMPT
    assert M["note"] == AM.SAVED_MEMORY_NOTE and (M["hint"], M["hint_v5"]) == (AM.LAST_STEP_HINT, AM.LAST_STEP_HINT_V5)
    with pytest.raises(ValueError, match="not the locked one"):
        CF.markers(ROOT / "argus_hook" / "agent_memory.py", expected="0" * 64)


def test_the_frozen_markers_are_the_locked_file():
    lock_path = ROOT / "artifacts" / "live-agent" / "battery" / "first-run-v1.6" / "lock.json"
    if not lock_path.is_file():
        pytest.skip("the plan is not frozen here")
    lock = json.loads(lock_path.read_text(encoding="utf-8"))
    frozen = CF.markers(lock_path.parent / "frozen" / "argus_hook" / "agent_memory.py",
                        lock["files"]["argus_hook/agent_memory.py"])
    assert frozen == M


def test_i1_without_the_notice_is_the_no_notice_arm():
    moved = CF.minus_notice(gen(off_context()), M)
    assert moved["messages"] == off_context(notice=False) and moved["prompt_ids"] is None


def test_i2_without_memory_and_history_is_the_memory_off_turn():
    bare = CF.minus_memory(CF.minus_history(gen(on_context()), M), M)
    assert bare["messages"] == off_context() and bare["request_index"] == 1


def test_without_history_alone_is_a_first_turn_of_the_same_conversation():
    moved = CF.minus_history(gen(on_context()), M)
    first = AM.request_message(TASK, FILES, {"id": "c-20261122-abcdef12", "history": [], "recent": RECENT}, 0, 3)
    assert moved["messages"][-1]["content"] == first and len(moved["messages"]) == 2


def test_without_recent_is_a_request_built_without_them():
    moved = CF.minus_recent(gen(on_context()), M)
    assert moved["messages"] == on_context(recent=False)


def test_i3_and_i4_swaps():
    step2 = [*off_context(), {"role": "assistant", "content": "```bash\nls\n```"},
             {"role": "user", "content": "output" + AM.LAST_STEP_HINT}]
    v5 = [*step2[:-1], {"role": "user", "content": "output" + AM.LAST_STEP_HINT_V5}]
    assert CF.swap_hint(gen(step2, index=1, step=2), M)["messages"] == v5
    assert CF.swap_effort(gen(off_context()))["reasoning_effort"] == "low"
    assert CF.swap_effort(gen(off_context(), effort="high")) is None


def test_i5_the_algebra():
    on = gen(on_context())
    for name in ("minus_notice", "minus_memory", "minus_recent"):
        once = CF.TRANSFORMS[name](on, M)
        assert once is not None and CF.TRANSFORMS[name](once, M) is None  # the marker is gone
    assert CF.minus_history(CF.minus_history(on, M), M) is None
    step2 = gen([*off_context(), {"role": "user", "content": "x" + AM.LAST_STEP_HINT}], index=1, step=2)
    assert CF.swap_hint(CF.swap_hint(step2, M), M)["messages"] == step2["messages"]
    assert CF.swap_effort(CF.swap_effort(on))["reasoning_effort"] is None
    a = CF.minus_memory(CF.minus_history(on, M), M)
    b = CF.minus_history(CF.minus_memory(on, M), M)
    assert a["messages"] == b["messages"]
    assert CF.minus_memory(CF.minus_recent(on, M), M)["messages"] == CF.minus_memory(on, M)["messages"]
    assert CF.minus_notice(CF.minus_memory(on, M), M)["messages"] == CF.minus_memory(CF.minus_notice(on, M), M)["messages"]


def test_i7_a_marker_the_request_repeats_does_not_apply():
    quoting = off_context()
    quoting[-1] = {"role": "user", "content": quoting[-1]["content"] + M["monitor"]}
    assert CF.minus_notice(gen(quoting), M) is None
    hinted = [*off_context(), {"role": "user", "content": "x" + AM.LAST_STEP_HINT + AM.LAST_STEP_HINT_V5}]
    assert CF.swap_hint(gen(hinted, index=1), M) is None
    assert CF.minus_memory(gen(off_context()), M) is None  # nothing to take out
    assert CF.minus_memory(gen(on_context(), index=None) | {"request_index": None}, M) is None  # a resumed turn


def test_compare_counts_same_differ_na_other_day_missing_and_sealed():
    good = [gen(off_context())]
    no_notice = [gen(off_context(notice=False))]
    later = [dict(gen(off_context(notice=False)), render_date="2026-11-23")]
    pairs = {"I1": [("A", "B"), ("C", "D"), ("E", "F"), ("G", "H"), ("I", "J"), ("K", "L")]}
    by_key = {"A": good, "B": no_notice, "C": good, "D": good, "E": good, "F": later, "G": good, "I": "sealed", "J": good,
              "K": [gen(off_context(notice=False))], "L": no_notice}
    row = CF.compare(pairs, by_key, M)["I1"]
    assert (row["same"], row["differ"], row["other_day"], row["missing"], row["sealed"], row["na"]) == \
        (1, ["C"], ["E"], ["G"], 1, ["K"])
    rendered = CF.compare({"I1": [("A", "B")]}, by_key, M, render=lambda g: [9])["I1"]
    assert rendered["differ"] == ["A"]  # the messages agree, the ids do not


def write_task(folder, run_id, messages, features=(), ids=(1, 2), effort=None, extra=()):
    rows = [{"type": "task_start", "run_id": run_id},
            {"type": "context", "render_date": "2026-11-22", "features": list(features)},
            {"type": "context", "step": 1, "messages": messages},
            {"type": "generation", "step": 1, "attempt": 1, "prompt_ids": list(ids), "reasoning_effort": effort},
            *extra]
    (folder / f"{run_id}.jsonl").write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows),
                                            encoding="utf-8")


def test_check_on_a_run_without_the_tokenizer(tmp_path):
    run, logs = tmp_path / "run", tmp_path / "logs"
    (run / "frozen" / "argus_hook").mkdir(parents=True)
    logs.mkdir()
    source = (ROOT / "argus_hook" / "agent_memory.py").read_bytes()
    (run / "frozen" / "argus_hook" / "agent_memory.py").write_bytes(source)
    lock = {"plan": "p", "files": {"argus_hook/agent_memory.py": CF.digest(source)}, "git_head": "h"}
    (run / "lock.json").write_text(json.dumps(lock), encoding="utf-8")
    sha = CF.lock_sha(lock)
    one = {"steps": [{"step": 1}], "format_failures": 0}  # one accepted action: one generation
    rows = [{"case": "clear-start", "time": 1, "lock_sha": sha},
            {"case": "P01-off", "conversation": "c1", "turn": 1, "run_id": "live-a", "lock_sha": sha, **one},
            {"case": "M01", "conversation": "c2", "turn": 1, "run_id": "live-b", "lock_sha": sha, **one},
            {"case": "P02-off", "conversation": "c3", "turn": 1, "run_id": "live-c", "lock_sha": sha, **one},
            {"case": "M02", "conversation": "c4", "turn": 1, "run_id": "live-d", "lock_sha": sha, **one}]
    (run / "manifest.jsonl").write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")
    write_task(logs, "live-a", off_context())
    write_task(logs, "live-b", off_context(notice=False))
    write_task(logs, "live-c", off_context())
    write_task(logs, "live-d", off_context(notice=False), extra=[{"type": "observation", "argus_page": True}])
    result = CF.check(run, logs, run / "frozen")
    assert result["I1"]["same"] == 1 and result["I1"]["sealed"] == 1 and result["sealed_turns"] == 1
    assert result["I2"]["missing"] == ["P01-on-base.2", "P02-on.1", "P03-on.1"] and "I0" not in result
    assert result["incomplete"] == [] and result["usable"] == ["I1"]  # I2-I4: no pair came out the same
    rows[1] = {**rows[1], "steps": [{"step": 1}, {"step": 2}]}  # the record lacks a generation the run made
    (run / "manifest.jsonl").write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")
    assert CF.check(run, logs, run / "frozen")["incomplete"] == ["P01-off.1"]
    rows[1] = {**rows[1], "steps": [{"step": 1}]}
    rows.append({"case": "M03", "run_id": "live-e", "lock_sha": "other"})
    (run / "manifest.jsonl").write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")
    with pytest.raises(ValueError, match="another lock"):
        CF.check(run, logs, run / "frozen")
    rows[-1] = {"case": "M03", "run_id": "../x", "lock_sha": sha}
    (run / "manifest.jsonl").write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")
    with pytest.raises(ValueError, match="outside the record folder"):
        CF.check(run, logs, run / "frozen")


def test_a_resumed_turn_has_no_request_place():
    records = [{"type": "context", "features": ["resume"], "render_date": "2026-11-22"},
               {"type": "context", "step": 1, "messages": off_context()},
               {"type": "generation", "step": 1, "attempt": 1, "prompt_ids": [1]}]
    assert CF.generations(records)[0]["request_index"] is None


def test_the_same_lock_sha_and_turn_keys_as_the_battery_and_the_outcomes():
    import live_battery as LB
    import live_outcomes as LO

    lock = {"plan": "p", "files": {"a": "b"}, "git_head": "h", "time": 3}
    assert CF.lock_sha(lock) == LB.lock_sha(lock)
    rows = [{"case": "A03", "conversation": "c", "turn": 1, "run_id": "a"},
            {"case": "A03", "conversation": "c", "turn": 1, "run_id": "b"}, {"case": "A04", "turn": 1, "run_id": "c"}]
    assert CF.turn_keys(rows) == LO.turn_keys(rows)


def test_the_tool_imports_the_standard_library_and_live_rescore_only():
    tree = ast.parse((ROOT / "argus_hook" / "live_counterfactual.py").read_text(encoding="utf-8"))
    top = {alias.name.split(".")[0] for node in tree.body if isinstance(node, ast.Import) for alias in node.names}
    top |= {node.module.split(".")[0] for node in tree.body if isinstance(node, ast.ImportFrom) and node.module}
    assert top <= {"__future__", "argparse", "ast", "hashlib", "json", "sys", "pathlib", "live_rescore"}


def test_without_history_keeps_to_its_section_when_a_shown_command_holds_blank_lines():
    turns = [{"task": "할 일 파일 만들어 줘", "answer": "만들었습니다.", "termination": "stop",
              "steps": [{"kind": "bash", "command": "cat > todo.md <<'EOF'\n# 할 일\n\n## 오늘\n- 장보기\nEOF", "exit_code": 0}]}]
    messages, shown = AM.history_messages(turns)
    conversation = {"id": "c-20261122-abcdef12", "history": turns, "recent": RECENT}
    request = AM.request_message(TASK, FILES, conversation, shown, 3)
    assert "\n\n## 오늘" in request  # the shown command does hold a blank line and a heading
    on = gen([{"role": "system", "content": BASE + AM.environment_prompt(DAY) + AM.system_memory(FILES)}, *messages,
              {"role": "user", "content": request}])
    moved = CF.minus_history(on, M)
    first = AM.request_message(TASK, FILES, {"id": "c-20261122-abcdef12", "history": [], "recent": RECENT}, 0, 3)
    assert moved["messages"][-1]["content"] == first


def test_twins_that_parted_before_the_compared_step_are_diverged_not_a_failed_transformation():
    def step2(command, hint):
        return [*off_context(), {"role": "assistant", "content": f"```bash\n{command}\n```"},
                {"role": "user", "content": "output" + hint}]
    by_key = {"H00.1": [gen(step2("curl -s http://fakenet/naver.html -o /tmp/naver.html", AM.LAST_STEP_HINT), index=1, step=2)],
              "H01.1": [gen(step2("wc -l /tmp/naver.html", AM.LAST_STEP_HINT_V5), index=1, step=2)]}
    row = CF.compare({"I3": [("H00.1", "H01.1")]}, by_key, M)["I3"]
    assert row["diverged"] == ["H00.1"] and not row["differ"] and row["usable"] is False
    by_key["H01.1"] = [gen(step2("curl -s http://fakenet/naver.html -o /tmp/naver.html", AM.LAST_STEP_HINT_V5), index=1, step=2)]
    row = CF.compare({"I3": [("H00.1", "H01.1")]}, by_key, M)["I3"]
    assert row["same"] == 1 and row["usable"] is True


def test_a_difference_built_before_any_generation_is_differ_and_a_generated_one_diverged():
    def twin(system_extra, command, text, hint):
        messages = [{"role": "system", "content": BASE + system_extra + AM.environment_prompt(DAY)},
                    {"role": "user", "content": AM.request_message(TASK, None, None, 0, 2)},
                    {"role": "assistant", "content": f"```bash\n{command}\n```"}, {"role": "user", "content": "out" + hint}]
        step1 = {**gen(messages[:2]), "generated": text}
        return [step1, {**gen(messages, index=1, step=2), "generated": "next"}]
    pairs = {"I3": [("H00.1", "H01.1")]}
    other_system = {"H00.1": twin("", "ls", "a", AM.LAST_STEP_HINT), "H01.1": twin("(other)", "ls", "a", AM.LAST_STEP_HINT_V5)}
    assert CF.compare(pairs, other_system, M)["I3"]["differ"] == ["H00.1"]  # not hidden as a parting
    other_text = {"H00.1": twin("", "ls", "a", AM.LAST_STEP_HINT), "H01.1": twin("", "ls -a", "b", AM.LAST_STEP_HINT_V5)}
    assert CF.compare(pairs, other_text, M)["I3"]["diverged"] == ["H00.1"]

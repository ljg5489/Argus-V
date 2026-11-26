"""What the everyday worker does around a reply (argus_hook/live_agent_free.py installs it; the plan's worker,
live_agent.py started by dashboard_server.py, has none of it and stays as it is).

Why, counted over the turns of 2026-11-22 and 23 (222 generations of gpt-oss-20b in the live chat):

1. repair(): 42 replies were refused and generated again, 35 of them although they said plainly what to run. The
   model writes a tool call as it was trained to (`to=container.exec` with {"cmd": [...], "timeout": 120000}); the
   plan's parser takes such a call only with "cmd" alone, on the commentary channel, and a final message only as one
   block. A refused reply costs a generation, and the correction ("correct only the format") was once answered to
   the user as if it were the request. Here a reply the parser refuses is read again after its shape is put right:
   options besides cmd dropped, the channel and the <|constrain|> mark normalized, several bash blocks joined, an
   open bash block closed. What the parser accepts is never touched, and nothing is read out of the reasoning.
2. gate(): an answer is checked before it is taken as the answer. Three things the user was told that were not so:
   a file "created" that no command had made (four turns in a row), a whole program written into the answer (saved
   nowhere, shown up to 8,000 characters), and "no internet" or "no display" in a sandbox that has both. Such an
   answer goes back to the model once or twice with what was found; if it comes again it is taken, and the user is
   told that it was not confirmed.
   The memory step is checked the same way for one thing: a note that says this sandbox lacks the internet or a
   screen it has ("sandbox lacks X display" was written after a turn in which the screen was on the whole time, and
   the notes are what the next turn starts from).
3. hint_for(): a line added to a command's output when the sandbox has a better way: `webread` for a page fetched
   with curl and read with grep (19 steps for a stock price, none of them the web tools), `gui-run` for a program
   that waited for its window until the time limit.

Nothing here changes what Argus-V-emp sees: the verdict is on the hidden states of the reply as it was generated.
"""

from __future__ import annotations

import json
import re
import shlex
import subprocess

START, CHANNEL, MESSAGE, CALL, RETURN = "<|start|>", "<|channel|>", "<|message|>", "<|call|>", "<|return|>"
CHECK = "check: "            # how a gate's refusal starts (correction() answers it; anything else is the parser's)
STEP_BOUNCES = 2             # answers sent back in one step (the worker allows four attempts a step, formats included)
TURN_BOUNCES = 4             # ... and in one turn
BOUNCES = {"files": 2, "code": 1, "excuse": 1, "note": 1}  # ... and for one reason in one turn
CODE_LINES = 15              # fenced lines in an answer from which it is a program, not an example
LISTED = 1000                # entries `sandbox.py files` lists: with as many, a file not listed may still be there

LA = None  # live_agent, once installed
STATE = {"task": "", "phase": None, "step": None, "web": False, "screen": False, "tools": False,
         "fired": {}, "step_bounces": 0, "turn_bounces": 0, "last": None, "lister": None, "hints": 0}


# ---------------------------------------------------------------------------- 1. a refused reply, read again
def split_last(raw: str) -> tuple[str, str]:
    """(everything up to the last message's `<|start|>assistant`, that message)."""
    marker = START + "assistant"
    at = raw.rfind(marker)
    return (raw[:at + len(marker)], raw[at + len(marker):]) if at >= 0 else ("", raw)


def repair_call(last: str) -> tuple[str, list[str]] | None:
    """A container.exec call refused for its shape: on the analysis channel, marked <|constrain|>json, or carrying
    options besides cmd (a timeout, a working folder)."""
    if MESSAGE not in last or not last.rstrip().endswith(CALL):
        return None
    header, rest = last.split(MESSAGE, 1)
    if not re.search(r"\bto=container\.exec\b", header):
        return None
    try:
        call = json.loads(rest.rstrip()[:-len(CALL)])
    except ValueError:
        return None
    if not isinstance(call, dict) or "cmd" not in call:
        return None
    cmd, notes = call["cmd"], []
    extras = sorted(str(key) for key in call if key != "cmd")
    if extras:
        notes.append("options dropped: " + ", ".join(extras)[:80])
    folder = call.get("workdir") or call.get("cwd")
    if isinstance(folder, str) and folder.strip() and folder.strip().rstrip("/") not in ("/workspace", "."):
        if isinstance(cmd, list) and len(cmd) == 3 and cmd[0] in ("bash", "sh") and cmd[1] in ("-lc", "-c") and isinstance(cmd[2], str):
            cmd = [cmd[0], cmd[1], f"cd -- {shlex.quote(folder.strip())} && {cmd[2]}"]
        elif isinstance(cmd, str):
            cmd = f"cd -- {shlex.quote(folder.strip())} && {cmd}"
    clean = CHANNEL + "commentary to=container.exec code"
    if header != clean:
        notes.append("call header normalized")
    if not notes:
        return None
    return clean + MESSAGE + json.dumps({"cmd": cmd}, ensure_ascii=False) + CALL, notes


FENCE = re.compile(r"```(\w*)[ \t]*\r?\n(.*?)\r?\n```[ \t]*(?:\r?\n|$)", re.S)


def join_blocks(content: str) -> tuple[str, str | None]:
    """A final message that is blocks and nothing else, as one block: several bash blocks are one script; a bash
    block followed by a stop block is the command (the answer comes after its output); a bash block never closed is
    closed. Anything else (words around a block, a block inside a block) is left as it is."""
    text = content.strip()
    if re.match(r"```(bash|sh|shell)[ \t]*\r?\n", text, re.I) and text.count("```") == 1 and text.split("\n", 1)[1].strip():
        return "```bash\n" + text.split("\n", 1)[1].rstrip("\n") + "\n```", "bash block closed"
    blocks, at = [], 0
    for match in FENCE.finditer(text):
        if text[at:match.start()].strip():
            return content, None
        blocks.append((match.group(1).lower(), match.group(2)))
        at = match.end()
    if text[at:].strip() or len(blocks) < 2 or any("```" in body for _kind, body in blocks):
        return content, None
    kinds = [kind for kind, _body in blocks]
    if all(kind in ("bash", "sh", "shell") for kind in kinds):
        return "```bash\n" + "\n".join(body for _kind, body in blocks) + "\n```", f"{len(blocks)} bash blocks joined"
    if kinds[0] in ("bash", "sh", "shell") and all(kind == "stop" for kind in kinds[1:]):
        return "```bash\n" + blocks[0][1] + "\n```", "bash block kept: the stop block waits for its output"
    return content, None


def repair_final(last: str) -> tuple[str, list[str]] | None:
    """A final message refused for its shape: a <|constrain|> mark in its header, ended as a call, or not one block."""
    head = re.match(r"<\|channel\|>final[ \t]*(<\|constrain\|>[ \t]*\w+[ \t]*)?<\|message\|>", last)
    if not head:
        return None
    notes = ["final header normalized"] if head.group(1) else []
    body = last[head.end():].rstrip()
    if body.endswith(CALL):
        body = body[:-len(CALL)]
        notes.append("final ended as a call")
    elif body.endswith(RETURN):
        body = body[:-len(RETURN)]
    else:
        return None  # cut at the token limit: nothing to run, the model writes it again in parts
    content, joined = join_blocks(body)
    if joined:
        notes.append(joined)
    return (CHANNEL + "final" + MESSAGE + content + RETURN, notes) if notes else None


def repair(raw: str) -> tuple[str, list[str]]:
    """``raw`` with its last message put into a shape the plan's parser takes, and what was changed ([]: nothing)."""
    head, last = split_last(raw)
    if CALL in head or (CHANNEL + "final") in head:  # more than one action in a reply: refused as it is
        return raw, []
    fixed = repair_call(last) or repair_final(last)
    return (head + fixed[0], fixed[1]) if fixed else (raw, [])


# ---------------------------------------------------------------------------- 2. an answer, checked before it is one
URL = re.compile(r"https?://\S+")
PATH = re.compile(r"(?<![\w/.~-])(/workspace/[\w./-]*[\w-]|(?:[\w.-]+/)+[\w.-]*[A-Za-z_][\w.-]*\.[A-Za-z][A-Za-z0-9]{0,4})(?![\w/-])")
NEGATED = re.compile(r"없|않|못|not exist|n['’]t exist|missing|no such|not found|cannot find|삭제|removed|deleted|지웠", re.I)
MAKES = re.compile(r"만들|구현|작성|생성|개발|짜\s?줘|고쳐|수정|build|create|make|implement|write|develop|fix", re.I)
NO_NET = re.compile(r"(인터넷|네트워크|외부\s*(망|네트워크|접속|접근)|웹)[^.\n]{0,24}(제한|차단|불가|없|안\s?되|안\s?됩|막혀)"
                    r"|no (real )?(internet|network)( access| connection)?\b|without (internet|network)|lacks? (internet|network)"
                    r"|(internet|network)( access| connection)? (is |was )?(restricted|unavailable|not available|disabled|blocked|missing)"
                    r"|(cannot|can't|unable to) access the (internet|web)|offline (sandbox|environment)", re.I)
NO_SCREEN = re.compile(r"(디스플레이|화면|X\s?(서버|윈도우)|GUI)[^.\n]{0,24}(제공되지|없|불가|지원하지|안\s?되|안\s?됩)"
                       r"|no (X )?(display|X server|screen|GUI)\b|lacks? (an? )?(X )?(display|X server|screen|GUI)\b"
                       r"|(display|X server|screen)( environment)? (is |was )?(unavailable|not available|missing|not provided)"
                       r"|headless (environment|sandbox)|without a (display|screen)", re.I)


def named_files(answer: str) -> list[str]:
    """The files of /workspace an answer names (relative to it), in order, without those it says are not there."""
    found = []
    for line in URL.sub(" ", answer or "").split("\n"):
        for match in PATH.finditer(line):
            around = line[max(0, match.start() - 60):match.end() + 60]
            if NEGATED.search(around):
                continue
            path = match.group(1).rstrip(".")
            path = path[len("/workspace/"):] if path.startswith("/workspace/") else path[2:] if path.startswith("./") else path
            if not path or path.startswith(("/", ".agent")) or ".." in path.split("/") or path.split("/")[0] in ("tmp", "usr", "etc", "opt", "home", "dev", "proc"):
                continue
            if path not in found:
                found.append(path)
    return found


def code_lines(answer: str) -> int:
    """Lines of an answer that stand inside ``` fences."""
    count, inside = 0, False
    for line in (answer or "").split("\n"):
        if line.strip().startswith("```"):
            inside = not inside
        elif inside and line.strip():
            count += 1
    return count


def relative(path) -> str:
    path = str(path)
    return path[len("/workspace/"):] if path.startswith("/workspace/") else path.lstrip("/")


def sandbox_listing() -> set[str] | None:
    """The paths under /workspace, relative to it (None: not known now, or more than the list shows)."""
    if callable(STATE.get("lister")):
        listed = STATE["lister"]()
        return None if listed is None else {relative(path) for path in listed}
    try:
        done = subprocess.run(["python3.11", str(LA.SANDBOX_SCRIPT), "files"], capture_output=True, text=True,
                              encoding="utf-8", errors="replace", timeout=30)
        entries = json.loads(done.stdout).get("entries")
    except (OSError, subprocess.SubprocessError, ValueError, AttributeError):
        return None
    if not isinstance(entries, list) or len(entries) >= LISTED:
        return None
    return {relative(entry.get("path") if isinstance(entry, dict) else entry) for entry in entries}


def gate(answer: str) -> dict | None:
    """What is not so in ``answer`` (None: nothing found), the first of: a file it names that is not there, a
    program written into it, something this sandbox has said to be missing. -> {"rule", "reason" and "todo" for the
    model, "said" for the user when it goes back, "kept" when it is taken all the same}."""
    task = STATE.get("task") or ""
    names = named_files(answer)
    if names:
        listed = sandbox_listing()
        gone = [name for name in names if name not in listed] if listed is not None else []
        if gone:
            shown = ", ".join(gone[:5])
            return {"rule": "files", "paths": gone[:5],
                    "reason": f"it names {'a file that is' if len(gone) == 1 else 'files that are'} not in the sandbox (looked now): {shown}.",
                    "todo": "Nothing made it: create it with a command (apply_patch or cat > file), check with ls -l, and answer after that. "
                            "If you mean that it does not exist, say so in those words.",
                    "said": f"답이 말한 파일이 샌드박스에 없어서 다시 시켰습니다: {shown}",
                    "kept": f"확인되지 않은 답입니다: 답이 말한 파일이 샌드박스에 없습니다({shown}) · 다시 시켰지만 같은 답이 왔습니다"}
    lines = code_lines(answer)
    if lines >= CODE_LINES and MAKES.search(task):
        return {"rule": "code", "lines": lines,
                "reason": f"it holds {lines} lines of code. Code in an answer is saved nowhere, and the user asked for something made in the sandbox.",
                "todo": "Write the code into a file with a command (a long file in parts), run it, and answer with the file's path and the command that runs it.",
                "said": f"답 안에 코드 {lines}줄이 들어 있어(파일로 저장되지 않음) 파일로 쓰라고 다시 시켰습니다",
                "kept": f"답 안에 코드 {lines}줄이 그대로 있습니다(파일로 저장되지 않음) · 파일로 쓰라고 했지만 같은 답이 왔습니다"}
    said_no = lacks(answer)
    if said_no:
        what = " and ".join({"net": "internet access", "screen": "a screen (display :1)"}[name] for name in said_no)
        korean = "·".join({"net": "인터넷", "screen": "화면"}[name] for name in said_no)
        return {"rule": "excuse", "what": said_no,
                "reason": f"it says something is missing that this sandbox has: {what}. The system message says so, and `sandbox-info` shows it now.",
                "todo": "Do not give that as a reason. Run the command that needs it and go by what it prints"
                        + (" (websearch, webread, curl for the web; gui-run for a window)." if STATE.get("tools") else "."),
                "said": f"이 샌드박스에 있는 것({korean})이 없다고 답해서 다시 시켰습니다",
                "kept": f"확인되지 않은 답입니다: 이 샌드박스에 있는 것({korean})이 없다고 답했습니다 · 다시 시켰지만 같은 답이 왔습니다"}
    return None


def lacks(text: str) -> list[str]:
    """What ``text`` says is missing although this sandbox has it: "net", "screen"."""
    return [name for name, pattern, have in (("net", NO_NET, STATE.get("web")), ("screen", NO_SCREEN, STATE.get("screen")))
            if have and pattern.search(text or "")]


def note_check(command: str) -> dict | None:
    """A memory step's command that writes into the notes that this sandbox lacks what it has. The notes are read
    at the start of every later turn, in whichever sandbox: "no real internet" and "no X display", written this way,
    were given as the reason for not trying in turn after turn."""
    if not re.search(r"\bNOTES\.md\b", command or ""):
        return None
    said_no = lacks(command)
    if not said_no:
        return None
    what = " and ".join({"net": "internet access", "screen": "a screen (display :1)"}[name] for name in said_no)
    korean = "·".join({"net": "인터넷", "screen": "화면"}[name] for name in said_no)
    return {"rule": "note", "what": said_no,
            "reason": f"a note in it says this sandbox lacks {what}, which it has (the system message says so).",
            "todo": "Write the notes again without that line; if nothing else is worth keeping, answer with a stop block that says `nothing to save`.",
            "said": f"기억에 '이 샌드박스에 {korean}이(가) 없다'는 틀린 메모를 적으려 해서 다시 시켰습니다",
            "kept": f"기억에 '이 샌드박스에 {korean}이(가) 없다'는 메모가 그대로 적혔습니다(사실과 다름) · 기억 창에서 지울 수 있습니다"}


def checked(action: dict) -> dict:
    """``action`` when it may go on; ValueError (a reply to generate again) when it is an answer a gate sends back,
    or a memory step's note that is not so."""
    if not isinstance(action, dict) or not STATE.get("task"):
        return action
    if STATE.get("phase") == "memory":
        found = note_check(str(action.get("body") or "")) if action.get("kind") == "bash" else None
    elif action.get("kind") == "stop" and not STATE.get("phase"):
        found = gate(str(action.get("answer") or action.get("body") or ""))
    else:
        found = None
    if not found:
        return action
    rule = found["rule"]
    if (STATE["fired"].get(rule, 0) >= BOUNCES[rule] or STATE["step_bounces"] >= STEP_BOUNCES
            or STATE["turn_bounces"] >= TURN_BOUNCES):  # said already: taken as it is, and the user is told what it is
        tell("unchecked", found["kept"], rule=rule)
        return action
    STATE["fired"][rule] = STATE["fired"].get(rule, 0) + 1
    STATE["step_bounces"] += 1
    STATE["turn_bounces"] += 1
    STATE["last"] = found
    tell("gate", found["said"], rule=rule)
    raise ValueError(CHECK + found["reason"])


def correction(error) -> str | None:
    """The retry message for an answer a gate sent back (None: not one of them: the worker's own correction)."""
    if not str(error).startswith(CHECK):
        return None
    found = STATE.get("last") or {"reason": str(error)[len(CHECK):], "todo": ""}
    if found.get("rule") == "note":
        return ("Your command was not run: " + found["reason"] + " " + found["todo"] + " Your entire FINAL message must be exactly "
                "one ```bash block or exactly one ```stop block.")
    return ("Your answer was not accepted: " + found["reason"] + " " + found["todo"] + " An answer only reports what was done: it makes "
            "nothing. Your entire FINAL message must be exactly one ```bash block with the next command, or exactly one "
            "```stop block with your answer once it is true.")


# ---------------------------------------------------------------------------- 3. a line under a command's output
FETCHES = re.compile(r"\b(curl|wget)\b[^\n|;&]*https?://|requests\.(get|post)\(|urlopen\(|urllib\.request", re.I)
OWN_TOOLS = re.compile(r"\b(webread|websearch|wiki)\b")
WINDOW = re.compile(r"\bpython3?\s+[\w./-]+\.py\b")
HINT_MOST = 3  # hints in one turn: said, not repeated at every step


def hint_for(command: str, data: dict) -> str:
    """A line for the agent under a command's output when the sandbox has a better way ('' when not)."""
    if not STATE.get("tools") or STATE.get("hints", 0) >= HINT_MOST or STATE.get("phase"):
        return ""
    command, out = command or "", str((data or {}).get("stdout_tail") or "")
    status, code = str((data or {}).get("status") or ""), (data or {}).get("exit_code")
    hint = ""
    if FETCHES.search(command) and not OWN_TOOLS.search(command) and (
            code not in (0, None) or not out.strip() or re.search(r"<(!doctype|html|head|body|div|script)\b", out[:4000], re.I)):
        hint = ('`webread <url>` prints a web page as readable text (its start first) and `websearch "<words>"` finds pages: '
                "they read a page better than curl with grep.")
    elif status == "TIMEOUT" and WINDOW.search(command) and "gui-run" not in command:
        hint = ("a program that opens a window never returns: start it with `gui-run <command>` (it runs in the background and "
                "reports the window or the error).")
    if not hint:
        return ""
    STATE["hints"] = STATE.get("hints", 0) + 1
    return "\n[sandbox hint] " + hint


# ---------------------------------------------------------------------------- the worker's side
def tell(kind: str, message: str, **fields) -> None:
    """Say it on the turn's card (and keep it in the turn's record when it is a warning)."""
    if LA is None:
        return
    try:
        if kind in ("gate", "unchecked"):
            LA.emit("memory", action="warning", message=message)
        LA.emit("free", step=STATE.get("step"), kind=kind, message=message, **fields)
        LA.keep("guard", step=STATE.get("step"), kind=kind, message=message, **fields)
    except Exception:  # (a note that cannot be written never stops a turn)
        pass


def begin_task(task: str) -> None:
    STATE.update(task=str(task or ""), phase=None, step=None, fired={}, step_bounces=0, turn_bounces=0, last=None, hints=0)


def end_task() -> None:
    STATE.update(task="", phase=None, step=None)


def begin_step(step, phase) -> None:
    STATE.update(step=step, phase=phase, step_bounces=0)


def configure(web: bool = False, screen: bool = False, tools: bool = False) -> None:
    STATE.update(web=bool(web), screen=bool(screen), tools=bool(tools))


def install(LA_module) -> None:
    """Wrap the worker's reading of a reply, its correction message and its sandbox's run. Once."""
    global LA
    LA = LA_module
    read, correct = LA.read_action, LA.correction_turn
    if getattr(read, "guarded", False):
        return

    def read_action(raw):
        try:
            action = read(raw)
        except ValueError as error:
            fixed, notes = repair(raw)
            if not notes:
                raise
            try:
                action = read(fixed)
            except ValueError:
                raise error from None
            tell("repair", "; ".join(notes), what=notes)
        return checked(action)

    def correction_turn(error):
        return correction(error) or correct(error)

    read_action.guarded = True
    LA.read_action, LA.correction_turn = read_action, correction_turn
    run = LA.Sandbox.run

    def sandbox_run(self, command, *args, **kwargs):
        observation, data = run(self, command, *args, **kwargs)
        hint = hint_for(command, data)
        if hint:
            tell("hint", hint.strip())
        return observation + hint, data

    LA.Sandbox.run = sandbox_run

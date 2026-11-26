"""The sandbox as a small computer on the local page ("샌드박스 컴퓨터"): the user's own terminal, file manager, editor
and system window over the same isolated container the agent works in (/workspace). Everything here goes through
SANDBOX/sandbox.py, as the agent's commands do; nothing runs on the host.

Served by argus_hook/agent_server.py (the /api/sandbox/... addresses); dashboard_server.py, locked by plan v1.6, is
not edited and has no such address. Every function takes the sandbox it is about (sandbox_boxes.Box): the one the
agent works in, or another folder the user looks at meanwhile. What is said below about the agent's turns holds for
the agent's sandbox; in another one nothing waits for the agent, and its way back is this module's own (restore()).

These windows are not a picture of a display: the page draws them from what the sandbox itself says: its files, its
processes, the output of its commands. The plan's SANDBOX/ has no screen at all; the everyday SANDBOX_PC/ has a real
one, which is another module's (sandbox_screen.py).

Reading (no snapshot, sandbox.py's own read-only commands, which also answer while a command runs):
- files():   `sandbox.py files`      every entry under /workspace (at most 1,000), its kind and size;
- read():    `sandbox.py read-file`  a text file's first 65,536 bytes, or an image's bytes; not while an agent task
                                     runs (its files are marked sealed only when its step has ended);
- system():  `sandbox.py status`     the container's CPU, memory, process count and disks. It holds sandbox.py's own
                                     lock for a second or two, and an agent's command that met it there would fail:
                                     so never while an agent task runs, and a turn that starts meanwhile waits for it.

Changing (one `sandbox.py run` each: a snapshot of /workspace is kept before it, as before every agent command):
- terminal(): one command line, `bash -c`, starting in the folder the last one ended in (`cd` lasts; nothing else
              lasts from one command to the next: no exported variable; no interactive program, there is no TTY);
              its output comes when it has ended, the last 262,144 bytes of each stream;
- change():   new folder, new file, rename, delete, save (at most 65,536 bytes), end a process: a fixed python
              script in the sandbox with the path as an argument (no shell, so no quoting);
- processes(): `ps` (a run, but nothing changes: the way back stays where it was);
- stop():     `sandbox.py kill` while a command of the user's runs (the only way to end one before its time limit:
              the container is stopped, and the next command starts it again with /workspace as it was before).

What it keeps in order for the agent's turns (the server's own bookkeeping, through its store):
- only this computer's local page; never while an agent task or another of these runs, and no agent turn starts
  while one runs (checked under the server's own start lock);
- a command that ran becomes the sandbox's way back ("마지막 정상 상태로" goes to before it), and the turn that could be
  taken back with "이 턴 전으로" no longer can (that would silently undo the user's own work too);
- the sealed test pages (http://fakenet/argus/…) are not opened here: a command that names them is refused; one that
  reaches them anyway (the gateway's log says so) has its output withheld, and the files it left are marked as a
  sealed turn's are (every later turn is sealed while they stay); a marked file, or one that holds those addresses,
  is not shown;
- a memory file changed here (/workspace/.agent) is found by the next turn as a change outside the memory step and
  waits for review, as before;
- not when the disk is low (every run leaves a snapshot), as an agent turn is not.
"""

from __future__ import annotations

import base64
import hashlib
import json
import re
import secrets
import shlex
import subprocess
import threading
import time
from pathlib import Path

import sandbox_boxes as BOXES

HOME = "/workspace"          # where the first command starts, and the only tree the file manager shows
TIMEOUT = 120                # seconds a command may take (the agent's own limit)
TIMEOUTS = (30, 120, 600)    # what the page may ask for
COMMAND_CHARS = 8_000        # the longest command line taken
PATH_CHARS = 1_024
TAIL = 32_768                # sandbox.py's report holds the last 32,768 bytes of each stream
SHOWN = 262_144              # what the page gets of each stream (read from sandbox.py's own log of the run)
READ_LIMIT = 65_536          # sandbox.py read-file's limit; the editor saves no more than it can read back
IMAGE_LIMIT = 8 * 2**20      # the largest picture sent to the page
IMAGE_MIMES = ("image/png", "image/jpeg", "image/gif", "image/webp", "image/bmp", "image/x-icon", "image/avif")
PROCESS_ROWS = 300
# live_agent.ARGUS_PAGES: the sealed scenario pages fakenet serves (a test holds the two patterns equal)
ARGUS_PAGES = re.compile(r"fakenet(?:\.[a-z]+)?(?::\d+)?/+argus(?:/|\b)", re.I)

LOCK = threading.Lock()      # one command of the user's at a time (in whichever sandbox)
# light: only a reading of the system window (a second or two); box: the sandbox it runs in
STATE = {"busy": False, "since": None, "light": False, "box": None}


def busy(box=None) -> bool:
    """Whether something of the user's runs (in ``box``, when one is named)."""
    return bool(STATE["busy"]) and (box is None or STATE["box"] == box.name)


def settled(seconds: float = 8.0, box=None) -> bool:
    """Whether nothing of the user's runs (in ``box``), after waiting out a reading of the system window."""
    deadline = time.monotonic() + seconds
    while STATE["light"] and time.monotonic() < deadline:
        time.sleep(0.05)
    return not busy(box)


# ---------------------------------------------------------------------------- what may run, and when
def inside(path) -> str:
    """A file or folder in /workspace as the page names it, or ValueError (said to the user). The same rule as
    sandbox.py read-file: under /workspace, no empty, '.' or '..' part."""
    if not isinstance(path, str) or len(path) > PATH_CHARS or any(ch in path for ch in "\x00\n\r"):
        raise ValueError("경로를 읽지 못했습니다.")
    if not path.startswith(HOME + "/") or any(part in ("", ".", "..") for part in path.split("/")[2:]):
        raise ValueError("작업 폴더(/workspace) 안의 파일이나 폴더만 고를 수 있습니다.")
    return path


def checked(body: dict) -> tuple[str, str, int]:
    """A terminal request's command, folder and time limit, or ValueError (said to the user)."""
    command = body.get("command")
    if not isinstance(command, str) or not command.strip():
        raise ValueError("실행할 명령을 입력해 주세요.")
    if len(command) > COMMAND_CHARS or "\x00" in command:
        raise ValueError(f"명령은 {COMMAND_CHARS:,}자 이하여야 합니다.")
    cwd = body.get("cwd") or HOME
    if not isinstance(cwd, str) or not cwd.startswith("/") or len(cwd) > PATH_CHARS or any(ch in cwd for ch in "\x00\n\r"):
        cwd = HOME
    timeout = body.get("timeout", TIMEOUT)
    if timeout not in TIMEOUTS:
        raise ValueError(f"시간 한도는 {', '.join(str(item) for item in TIMEOUTS)}초 중 하나여야 합니다.")
    if ARGUS_PAGES.search(command):
        raise ValueError("봉인된 시험 페이지(http://fakenet/argus/…)는 터미널에서 열 수 없습니다(평가용으로 봉인된 페이지).")
    return command, cwd, int(timeout)


def occupied(DS, box) -> str | None:
    """Who else is using ``box`` right now (None: nobody). The agent works in one sandbox: the others are free."""
    if not BOXES.is_agent(DS, box):
        return None
    if DS.LIVE.status().get("busy"):
        return "에이전트 작업이 실행 중입니다. 끝나거나 중지한 뒤 해 주세요."
    with DS.JOBS_LOCK:
        if any(job["process"].poll() is None and job.get("kind") == "agent" for job in DS.JOBS.values()):
            return "기존 에이전트 실행이 샌드박스를 쓰고 있습니다. 끝난 뒤 해 주세요."
    return None


def refusal(DS, box) -> str | None:
    """Why nothing of the user's runs in ``box`` right now (None: it may)."""
    why = occupied(DS, box)
    if why:
        return why
    free = DS.disk_free() if BOXES.is_agent(DS, box) else BOXES.disk_free(box)
    if free is not None and free < DS.DISK_LOW:  # every run leaves a snapshot: the agent's turns stop here too
        return (f"디스크 여유가 {free / 2**30:.1f} GB라 실행하지 않습니다. 샌드박스는 명령마다 사본(스냅숏)을 남깁니다. "
                f"{(DS.DISK_LOW - free) / 2**30:.1f} GB 이상 비운 뒤 해 주세요.")
    return None


def guarded(DS, box, work) -> tuple[int, dict]:
    """``work()`` as the one thing of the user's running (in ``box``): (HTTP status, JSON). The checks and the busy
    mark are made under the server's start lock, where an agent turn makes its own (see agent_server.enable)."""
    with DS._START_LOCK:
        why = refusal(DS, box)
        if why:
            return 409, {"error": why, "code": "busy"}
        if not settled(4.0) or not LOCK.acquire(blocking=False):
            return 409, {"error": "앞 명령이 아직 실행 중입니다. 끝난 뒤 해 주세요.", "code": "shell_busy"}
        STATE.update(busy=True, since=time.time(), light=False, box=box.name)
    try:
        return 200, work()
    except ValueError as error:
        return 400, {"error": str(error)}
    except Exception as error:  # the page gets a reason, never a stack
        return 500, {"error": f"{type(error).__name__}: {str(error)[:200]}"}
    finally:
        STATE.update(busy=False, since=None, light=False, box=None)
        LOCK.release()


# ---------------------------------------------------------------------------- one run, and the bookkeeping after it
def sandbox_run(DS, box, argv: list[str], timeout: int) -> tuple[dict, bool]:
    """`sandbox.py run` of ``argv`` in ``box``. A sandbox that was off (after a time-out, say) is started and the run
    tried once more. -> (sandbox.py's report, whether it had to be started)."""
    args = ["run", "--timeout", str(timeout), "--", *argv]
    data = BOXES.cli(DS, box, args, timeout=timeout + 90)
    reason = str(data.get("reason") or "")
    restarted = False
    if data.get("status") == "ERROR" and is_off(reason):
        if BOXES.cli(DS, box, ["up"], timeout=300).get("status") != "ERROR":
            data, restarted = BOXES.cli(DS, box, args, timeout=timeout + 90), True
    if DS.AM.blocked_kind(data) == "busy":  # tar saw a file change while it read it (a log being written): once more,
        time.sleep(2)                        # as the agent's worker does, before the sandbox is called blocked
        data = BOXES.cli(DS, box, args, timeout=timeout + 90)
    return data, restarted


def is_off(reason: str) -> bool:
    """sandbox.py (or docker) saying the container is not there or not running."""
    return "stopped" in reason or "not running" in reason


def error_text(reason: str) -> str:
    if "another sandbox operation" in reason:
        return "샌드박스가 다른 작업을 하는 중입니다. 잠시 뒤 다시 해 주세요."
    return reason[-300:] or "샌드박스가 답하지 않았습니다"


def finish(DS, box, data: dict, changes: bool = True) -> dict:
    """The server's bookkeeping after one run of the user's. ``changes``: whether it may have changed the workspace
    (a listing of processes does not, and the way back stays where it was)."""
    AM = DS.AM
    status = str(data.get("status") or "ERROR")
    out = {"status": status, "exit_code": data.get("exit_code"), "blocked": None,
           "environment_stopped": bool(data.get("environment_stopped"))}
    snapshot = data.get("recovery_snapshot")
    if status == "ERROR":
        out["reason"] = error_text(str(data.get("reason") or ""))
        blocked = AM.blocked_kind(data)
        if blocked:  # its snapshot failed: nothing runs until the workspace is put back
            BOXES.mark(DS, box, blocked=blocked)
            out.update(blocked=blocked, blocked_text=AM.BLOCKED_TEXT.get(blocked, blocked))
    elif snapshot:  # sandbox.py took its snapshot and ran it (whatever way it ended)
        if BOXES.ledger(DS, box).get("blocked"):
            BOXES.mark(DS, box, blocked=None)
        if changes:  # the way back is now to before the user's own command; no turn is taken back past it
            BOXES.mark(DS, box, restore_point=Path(str(snapshot)).name, restore_turn=None)
            out["snapshot"] = Path(str(snapshot)).name
    return out


def stream(DS, box, data: dict, name: str) -> tuple[str, dict | None]:
    """A stream of a run as the page gets it: its last SHOWN bytes, read from sandbox.py's own log of the run when
    its report (the last 32,768) holds less. -> (text, {"stream", "shown", "bytes"} when its beginning is left out)."""
    counts = data.get("bytes") if isinstance(data.get("bytes"), dict) else {}
    total = int(counts.get(name) or 0)
    tail = str(data.get(f"{name}_tail") or "")
    if total <= TAIL:
        return tail, None
    try:
        folder = Path(str(data.get("logs") or "")).resolve()
        if not data.get("logs") or folder.parent != (box.root / "artifacts").resolve():
            raise OSError("not a run folder")
        with (folder / f"{name}.log").open("rb") as log:
            log.seek(max(0, total - SHOWN))
            text = log.read(SHOWN).decode("utf-8", errors="replace")
        return text, ({"stream": name, "shown": SHOWN, "bytes": total} if total > SHOWN else None)
    except OSError:
        return tail, {"stream": name, "shown": TAIL, "bytes": total}


# ---------------------------------------------------------------------------- the terminal
# `tree` for a sandbox that has none (its image holds bash, coreutils, curl, git, procps, tar and python): python run
# isolated, written without a single quote so that it sits in one shell word. Options: -a (dot files too), -d (folders
# only), -L N (depth).
TREE = """
import os, sys
args, show_all, only_dirs, depth, roots = sys.argv[1:], False, False, None, []
while args:
    arg = args.pop(0)
    if arg == "-a": show_all = True
    elif arg == "-d": only_dirs = True
    elif arg == "-L" and args: depth = int(args.pop(0))
    elif arg.startswith("-L") and arg[2:].isdigit(): depth = int(arg[2:])
    else: roots.append(arg)
counts = [0, 0]
def walk(folder, prefix, level):
    try:
        names = sorted(os.listdir(folder), key=str.lower)
    except OSError as error:
        print(prefix + "[" + (error.strerror or "error") + "]")
        return
    names = [n for n in names if (show_all or not n.startswith(".")) and (not only_dirs or os.path.isdir(os.path.join(folder, n)))]
    for at, name in enumerate(names):
        path, last = os.path.join(folder, name), at == len(names) - 1
        link = " -> " + os.readlink(path) if os.path.islink(path) else ""
        print(prefix + ("└── " if last else "├── ") + name + link)
        if os.path.isdir(path) and not os.path.islink(path):
            counts[0] += 1
            if depth is None or level < depth:
                walk(path, prefix + ("    " if last else "│   "), level + 1)
        else:
            counts[1] += 1
for root in roots or ["."]:
    print(root)
    walk(root, "", 1)
print()
print(str(counts[0]) + " directories" + ("" if only_dirs else ", " + str(counts[1]) + " files"))
"""
assert "'" not in TREE

# Words a person types at a terminal that this sandbox does not have: defined for the one command line only (shell
# functions in the wrapper: nothing is written into the sandbox, and the agent's own commands never see them).
HELPERS = (
    "__argus_no() { ! command -v \"$1\" >/dev/null 2>&1; }\n"
    "__argus_no ll && ll() { ls -alF \"$@\"; }\n"
    "__argus_no la && la() { ls -A \"$@\"; }\n"
    "__argus_no l && l() { ls -CF \"$@\"; }\n"
    f"__argus_no tree && tree() {{ python3 -I -S -c {shlex.quote(TREE)} \"$@\"; }}\n"
    "__argus_no less && less() { cat \"$@\"; }\n"
    # (whether the sandbox has them or not: this terminal runs one line at a time, without a screen of its own)
    "for __argus_name in vi vim nano top htop; do eval \"$__argus_name() { "
    "echo \\\"이 터미널(한 줄씩 실행)은 화면을 쓰는 프로그램($__argus_name)을 띄우지 못합니다. '화면' 창이 있으면 그 안의 터미널에서 "
    "실행하세요. 파일은 편집기 창에서, 프로세스는 시스템 창에서 볼 수 있습니다.\\\" >&2; return 1; }\"; done\n"
    "__argus_no sudo && sudo() { echo \"이 컴퓨터에는 관리자 권한(sudo)이 없습니다: /workspace와 /tmp 밖은 읽기 전용입니다.\" >&2; return 1; }\n"
    "unset __argus_name\n"
)


def wrap(command: str, cwd: str, token: str) -> str:
    """The script one command line runs as: in the folder the last one ended in, and saying (on stderr, after a mark
    only this call knows) the folder it ends in, whatever way it ends. HELPERS come before the command."""
    return (f"cd -- {shlex.quote(cwd)} 2>/dev/null || cd {HOME}\n"
            f"trap 'printf \"\\n%s%s\\n\" {shlex.quote(token)} \"$PWD\" >&2' EXIT\n"
            f"{HELPERS}"
            f"{command}\n")


def unwrap(stderr: str, token: str, cwd: str) -> tuple[str, str]:
    """-> (stderr without the mark's line, the folder the command ended in; the old one when it did not say)."""
    text = stderr or ""
    at = text.rfind(token)
    if at < 0:
        return text, cwd
    end = text.find("\n", at)
    said = text[at + len(token):end if end >= 0 else len(text)].strip()
    before = text[:at]
    before = before[:-1] if before.endswith("\n") else before
    rest = before + (text[end + 1:] if end >= 0 else "")
    ok = said.startswith("/") and len(said) <= PATH_CHARS and "\x00" not in said
    return rest, (said if ok else cwd)


def sealed_touch(DS, box, since: float, command: str, output: str) -> bool:
    """Whether the command reached the sealed pages: what the gateway was asked for since it began (its own log), and
    the command's own text and output, as the agent's worker looks."""
    data = BOXES.cli(DS, box, ["fakenet-log", "--since", f"{since:.6f}"], timeout=60)
    paths = [str(event.get("path") or "") for event in data.get("events") or []
             if isinstance(event, dict) and event.get("kind") in ("http", "https")] if data.get("status") == "OK" else []
    return any(path.lower().lstrip("/").startswith("argus") for path in paths) \
        or bool(ARGUS_PAGES.search(command) or ARGUS_PAGES.search(output))


def mark_sealed(DS, box, before: str | None) -> dict:
    """The files a command that reached the sealed pages left: marked as a sealed turn's are (every later turn is
    sealed while they stay as they are). -> {"files": how many, "checked": whether the workspace could be compared}."""
    AM = DS.AM
    taken = BOXES.cli(DS, box, ["snapshot", "--name", "after-shell"], timeout=300)
    after = Path(str(taken.get("snapshot") or ""))
    old = AM.snapshot_members(Path(before), skip=AM.REMOTE_DIFF_SKIP) if before and Path(before).is_file() else None
    new = AM.snapshot_members(after, skip=AM.REMOTE_DIFF_SKIP) if taken.get("snapshot") and after.is_file() else None
    if old is None or new is None:
        return {"files": 0, "checked": False}
    digests = {path: digest for path, digest in new.items() if old.get(path) != digest}
    if digests:
        kept = BOXES.ledger(DS, box).get("sealed_files") or {}
        BOXES.mark(DS, box, sealed_files={**kept, **digests})
    return {"files": len(digests), "checked": True}


def terminal(DS, box, command: str, cwd: str, timeout: int) -> dict:
    """One command line in the sandbox, and the bookkeeping after it. -> what the page shows."""
    token = f"__ARGUS_CWD_{secrets.token_hex(8)}__"
    sent, started = time.time(), time.monotonic()
    data, restarted = sandbox_run(DS, box, ["bash", "-c", wrap(command, cwd, token)], timeout)
    seconds = round(time.monotonic() - started, 2)
    out = finish(DS, box, data)
    stdout, cut_out = stream(DS, box, data, "stdout")
    stderr, cut_err = stream(DS, box, data, "stderr")
    stderr, ended_in = unwrap(stderr, token, cwd)
    out.update(seconds=seconds, cwd=ended_in, restarted=restarted, stdout=stdout, stderr=stderr, sealed=False,
               cut=[item for item in (cut_out, cut_err) if item])
    if out["status"] != "ERROR" and data.get("recovery_snapshot") and sealed_touch(DS, box, sent - 1, command, stdout + "\n" + stderr):
        left = mark_sealed(DS, box, str(data["recovery_snapshot"]))
        out.update(sealed=True, stdout="", stderr="", sealed_files=left["files"], sealed_checked=left["checked"])
    DS.STORE.audit("shell", "local", what="terminal", sandbox=box.name, chars=len(command), status=out["status"],
                   exit_code=out["exit_code"], seconds=seconds, sealed=out["sealed"] or None)  # counts only, never the command's text
    return out


def execute(DS, box, body: dict) -> tuple[int, dict]:
    """POST /api/sandbox/exec for the local page: (HTTP status, JSON)."""
    try:
        command, cwd, timeout = checked(body)
    except ValueError as error:
        return 400, {"error": str(error)}
    return guarded(DS, box, lambda: terminal(DS, box, command, cwd, timeout))


# ---------------------------------------------------------------------------- the file manager and the editor
def sealed_paths(DS, box) -> list[str]:
    return sorted(f"{HOME}/{name}" for name in (BOXES.ledger(DS, box).get("sealed_files") or {}))


def agent_works(DS, box) -> bool:
    """Whether an agent task runs in ``box`` right now."""
    return BOXES.is_agent(DS, box) and bool(DS.LIVE.status().get("busy"))


def files(DS, box) -> dict:
    """GET /api/sandbox/files: every entry under /workspace as sandbox.py lists it (no snapshot, no lock)."""
    data = BOXES.cli(DS, box, ["files"], timeout=60)
    status = str(data.get("status") or "ERROR")
    base = {"root": HOME, "sandbox": box.name, "agent_busy": agent_works(DS, box), "shell_busy": busy(box),
            "blocked": BOXES.ledger(DS, box).get("blocked")}
    if status not in ("RUNNING", "STOPPED"):
        reason = str(data.get("reason") or "")
        if is_off(reason):  # a container that was killed (a time-out, 중지): docker's own words, not sandbox.py's STOPPED
            return {**base, "status": "STOPPED", "entries": [], "truncated": False, "sealed": sealed_paths(DS, box)}
        return {**base, "status": "ERROR", "reason": error_text(reason), "entries": [], "sealed": []}
    entries = [{"path": item["path"], "kind": str(item.get("kind") or "other"),
                "size": item.get("size") if isinstance(item.get("size"), int) else None}
               for item in data.get("entries") or []
               if isinstance(item, dict) and isinstance(item.get("path"), str)
               and item["path"].startswith(HOME + "/") and len(item["path"]) <= PATH_CHARS]
    return {**base, "status": status, "entries": entries, "truncated": bool(data.get("truncated")), "sealed": sealed_paths(DS, box)}


def read_error(reason: str) -> str:
    if "FileNotFoundError" in reason or "No such file" in reason:
        return "파일이 없습니다(지워졌거나 이름이 바뀌었습니다)."
    if "Only regular files" in reason or "IsADirectoryError" in reason:
        return "일반 파일만 열 수 있습니다."
    if "Too many levels of symbolic links" in reason or "NotADirectoryError" in reason or "ELOOP" in reason:
        return "링크를 거치는 경로는 열지 않습니다."
    if "not a supported image" in reason:
        return "지원하는 그림 형식이 아닙니다."
    if is_off(reason):
        return "샌드박스가 꺼져 있습니다."
    return f"파일을 읽지 못했습니다: {error_text(reason)[-160:]}"


def image_bytes(DS, box, path: str) -> tuple[str, bytes]:
    """`sandbox.py read-file --image`: a line with the MIME type, then the file's bytes (at most IMAGE_LIMIT read)."""
    process = subprocess.Popen(["python3.11", str(box.script), "read-file", "--image", path],
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=DS.live_env())
    try:
        data = process.stdout.read(IMAGE_LIMIT + 200)
        if len(data) >= IMAGE_LIMIT + 200:
            raise ValueError("그림이 너무 큽니다(8 MB까지 보입니다).")
        if process.wait(timeout=60):
            raise RuntimeError(read_error(process.stderr.read().decode("utf-8", errors="replace")))
    finally:
        if process.poll() is None:
            process.kill()
            process.wait()
        process.stdout.close()
        process.stderr.close()
    mime, _line, rest = data.partition(b"\n")
    return mime.decode("ascii", errors="replace"), rest


def read(DS, box, body: dict) -> tuple[int, dict]:
    """POST /api/sandbox/read {path, image?}: a file's text (at most READ_LIMIT bytes of it) or a picture."""
    try:
        path = inside(body.get("path"))
    except ValueError as error:
        return 400, {"error": str(error)}
    if agent_works(DS, box):  # a running turn's files are marked sealed only when its step has ended
        return 409, {"error": "에이전트 작업 중에는 파일 내용을 열지 않습니다(목록만 보입니다). 끝난 뒤 열어 주세요.", "code": "busy"}
    if path in sealed_paths(DS, box):
        return 403, {"error": "봉인된 시험 페이지에 닿은 명령이 남긴 파일이라 내용을 보이지 않습니다.", "code": "sealed"}
    data = BOXES.cli(DS, box, ["read-file", path], timeout=60)
    if data.get("status") == "ERROR" or "size" not in data:
        return 404, {"error": read_error(str(data.get("reason") or ""))}
    text, mime = str(data.get("content") or ""), data.get("mime")
    out = {"path": path, "size": int(data.get("size") or 0), "binary": bool(data.get("binary")), "mime": mime,
           "truncated": bool(data.get("truncated")), "limit": READ_LIMIT, "text": "", "sha": None}
    if mime:
        if not body.get("image"):
            return 200, out
        if mime not in IMAGE_MIMES:
            return 415, {"error": "지원하는 그림 형식이 아닙니다."}
        if out["size"] > IMAGE_LIMIT:
            return 413, {"error": f"그림이 너무 큽니다({out['size']:,}바이트 · 8 MB까지 보입니다)."}
        try:
            kind, raw = image_bytes(DS, box, path)
        except (ValueError, RuntimeError, OSError, subprocess.TimeoutExpired) as error:
            return 500, {"error": str(error)[:200]}
        if kind not in IMAGE_MIMES:
            return 415, {"error": "지원하는 그림 형식이 아닙니다."}
        return 200, {**out, "mime": kind, "base64": base64.b64encode(raw).decode("ascii"), "size": len(raw)}
    if ARGUS_PAGES.search(text):  # a copy of a sealed page, wherever it was saved
        return 403, {"error": "봉인된 시험 페이지의 주소가 들어 있는 파일이라 내용을 보이지 않습니다.", "code": "sealed"}
    if not out["binary"]:
        out.update(text=text, sha=None if out["truncated"] else hashlib.sha256(text.encode("utf-8")).hexdigest())
    return 200, out


# One fixed script for every change the file manager, the editor and the system window make: python in the sandbox,
# isolated (-I -S: nothing from /workspace or the sandbox HOME is imported), the path as an argument, never a shell.
OPS = r"""
import base64, json, os, shutil, sys
op, path = sys.argv[1], sys.argv[2]
extra = sys.argv[3] if len(sys.argv) > 3 else ''
def done(**fields):
    print(json.dumps(fields))
    sys.exit(0)
try:
    if op == 'mkdir':
        os.mkdir(path)
    elif op == 'touch':
        os.close(os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644))
    elif op == 'rename':
        if os.path.lexists(extra):
            done(ok=False, code='exists')
        os.rename(path, extra)
    elif op == 'delete':
        if os.path.islink(path) or not os.path.isdir(path):
            os.unlink(path)
        else:
            shutil.rmtree(path)
    elif op == 'save':
        if os.path.islink(path) or os.path.isdir(path):
            done(ok=False, code='kind')
        with open(path, 'wb') as stream:
            stream.write(base64.b64decode(extra))
    elif op == 'kill':
        os.kill(int(path), 15)
    else:
        done(ok=False, code='op')
    done(ok=True)
except FileExistsError:
    done(ok=False, code='exists')
except (FileNotFoundError, ProcessLookupError):
    done(ok=False, code='missing')
except PermissionError:
    done(ok=False, code='denied')
except OSError as error:
    done(ok=False, code='os', error=str(error)[:200])
"""
OP_ERRORS = {"exists": "같은 이름이 이미 있습니다.", "missing": "없습니다(지워졌거나 이름이 바뀌었습니다).",
             "denied": "권한이 없습니다(샌드박스 사용자로는 바꿀 수 없는 곳).", "kind": "폴더나 링크에는 저장하지 않습니다.",
             "op": "모르는 동작입니다."}
OP_NAMES = ("mkdir", "touch", "rename", "delete", "save", "kill")


def change(DS, box, body: dict) -> tuple[int, dict]:
    """POST /api/sandbox/change {op, path, to?, text?, sha?, pid?}: one change of the user's in the sandbox."""
    op = body.get("op")
    try:
        if op not in OP_NAMES:
            raise ValueError("모르는 동작입니다.")
        extra, saved = "", None
        if op == "kill":
            pid = body.get("pid")
            if not isinstance(pid, int) or isinstance(pid, bool) or not 1 < pid < 2**22:
                raise ValueError("끝낼 프로세스 번호를 읽지 못했습니다(1번은 끝내지 않습니다).")
            path = str(pid)
        else:
            path = inside(body.get("path"))
        if op == "rename":
            extra = inside(body.get("to"))
        if op == "save":
            text = body.get("text")
            if not isinstance(text, str):
                raise ValueError("저장할 내용을 읽지 못했습니다.")
            saved = text.encode("utf-8")
            if len(saved) > READ_LIMIT:
                raise ValueError(f"편집기는 {READ_LIMIT:,}바이트까지 저장합니다(지금 {len(saved):,}바이트). 더 큰 파일은 터미널에서 다뤄 주세요.")
            if path in sealed_paths(DS, box):
                raise ValueError("봉인으로 표시된 파일은 편집기로 덮어쓰지 않습니다.")
            extra = base64.b64encode(saved).decode("ascii")
    except ValueError as error:
        return 400, {"error": str(error)}

    def work() -> dict:
        if op == "save" and isinstance(body.get("sha"), str):  # the file as the editor opened it, or it is not written
            now = BOXES.cli(DS, box, ["read-file", path], timeout=60)
            same = "size" in now and not now.get("binary") and not now.get("truncated") \
                and hashlib.sha256(str(now.get("content") or "").encode("utf-8")).hexdigest() == body["sha"]
            if not same:
                return {"ok": False, "code": "changed", "error": "열어 둔 뒤에 파일이 바뀌었습니다(에이전트나 터미널이 고쳤을 수 있습니다). "
                        "다시 열어 확인하거나, 그대로 덮어쓸 수 있습니다."}
        started = time.monotonic()
        data, restarted = sandbox_run(DS, box, ["python3", "-I", "-S", "-c", OPS, op, path, extra], 60)
        out = finish(DS, box, data)
        out.update(restarted=restarted, ok=False)
        if out["status"] == "FINISHED" and out["exit_code"] == 0:
            try:
                said = json.loads(str(data.get("stdout_tail") or "").strip().splitlines()[-1])
            except (ValueError, IndexError):
                said = {}
            out["ok"] = said.get("ok") is True
            if not out["ok"]:
                code = str(said.get("code") or "os")
                out.update(code=code, error=OP_ERRORS.get(code) or f"하지 못했습니다: {str(said.get('error') or '')[:160]}")
        elif out["status"] != "ERROR":
            out["error"] = f"하지 못했습니다({out['status']} · exit {out['exit_code']}): {str(data.get('stderr_tail') or '')[-160:]}"
        else:
            out["error"] = out.get("blocked_text") or out.get("reason")
        if out["ok"] and saved is not None:
            out.update(sha=hashlib.sha256(saved).hexdigest(), size=len(saved))
        DS.STORE.audit("shell", "local", what=op, sandbox=box.name, status=out["status"], exit_code=out["exit_code"],
                       ok=out["ok"], seconds=round(time.monotonic() - started, 2))  # no path, no text
        return out

    return guarded(DS, box, work)


# ---------------------------------------------------------------------------- the system window
def describe(DS, box) -> dict:
    """GET /api/sandbox/shell: what the page says around the desktop of ``box`` (no sandbox call)."""
    settings = box.settings()
    state = BOXES.ledger(DS, box)
    return {"enabled": True, "sandbox": box.name, "folder": box.root.name, "label": box.label, "about": box.about,
            "agent": BOXES.is_agent(DS, box), "screen": box.screen(),
            "busy": busy(box), "since": STATE["since"] if busy(box) else None, "home": HOME, "timeouts": list(TIMEOUTS),
            "timeout": TIMEOUT, "network": box.network(), "blocked": state.get("blocked"),
            "blocked_text": DS.AM.BLOCKED_TEXT.get(state.get("blocked")) if state.get("blocked") else None,
            "agent_busy": agent_works(DS, box), "restore_point": state.get("restore_point"),
            "sealed": len(state.get("sealed_files") or {}), "read_limit": READ_LIMIT,
            "limits": {key: settings.get(key) for key in ("cpus", "memory", "workspace_size", "tmp_size", "pids")}}


def system(DS, box) -> dict:
    """GET /api/sandbox/system: `sandbox.py status` of ``box`` (docker's own numbers for the container, and df)."""
    with DS._START_LOCK:  # never beside an agent's command (see the top of this file), nor beside one of the user's
        if occupied(DS, box) or not LOCK.acquire(blocking=False):
            return {**describe(DS, box), "status": "BUSY", "reason": "샌드박스가 명령을 실행하는 중입니다."}
        STATE.update(busy=True, since=time.time(), light=True, box=box.name)
    try:
        data = BOXES.cli(DS, box, ["status"], timeout=60)
    finally:
        STATE.update(busy=False, since=None, light=False, box=None)
        LOCK.release()
    status = str(data.get("status") or "ERROR")
    out = {**describe(DS, box), "status": status}
    if status == "ERROR":
        reason = str(data.get("reason") or "")
        kind = "BUSY" if "another sandbox operation" in reason else "STOPPED" if is_off(reason) else "ERROR"
        return {**out, "status": kind, "reason": error_text(reason)}
    resources = data.get("resources") if isinstance(data.get("resources"), dict) else {}
    disks = []
    for line in str(data.get("disk") or "").splitlines()[1:]:
        cells = line.split()
        if len(cells) >= 6:
            disks.append({"mount": cells[5], "size": cells[1], "used": cells[2], "free": cells[3], "percent": cells[4]})
    return {**out, "cpu": resources.get("CPUPerc"), "memory": resources.get("MemUsage"), "memory_percent": resources.get("MemPerc"),
            "pids": resources.get("PIDs"), "disks": disks}


PS = ["ps", "-eo", "pid=,ppid=,pcpu=,pmem=,etimes=,args="]


def processes(DS, box) -> tuple[int, dict]:
    """POST /api/sandbox/processes: what runs in ``box`` now (`ps`; a run, so a snapshot, but nothing changes)."""
    def work() -> dict:
        data, restarted = sandbox_run(DS, box, PS, 20)
        out = finish(DS, box, data, changes=False)
        rows = []
        for line in str(data.get("stdout_tail") or "").splitlines():
            cells = line.split(None, 5)
            if len(cells) < 6 or not cells[0].isdigit():
                continue
            if cells[5].startswith("ps -eo pid=") or (cells[5].startswith("timeout --signal=TERM") and " ps -eo pid=" in cells[5]):
                continue  # this listing itself
            rows.append({"pid": int(cells[0]), "ppid": int(cells[1]) if cells[1].isdigit() else None, "cpu": cells[2],
                         "memory": cells[3], "seconds": int(cells[4]) if cells[4].isdigit() else None, "command": cells[5][:300]})
        out.update(restarted=restarted, processes=rows[:PROCESS_ROWS], more=max(0, len(rows) - PROCESS_ROWS))
        if out["status"] == "ERROR":
            out["error"] = out.get("blocked_text") or out.get("reason")
        return out

    return guarded(DS, box, work)


def power(DS, box, body: dict) -> tuple[int, dict]:
    """POST /api/sandbox/power {action: "on"}: start a sandbox that is off (`sandbox.py up`: its last snapshot comes
    back with it). Stopping it is not offered here: the agent chat's 샌드박스 점검 does that with its own bookkeeping."""
    if body.get("action") != "on":
        return 400, {"error": "켜기만 할 수 있습니다."}

    def work() -> dict:
        data = BOXES.cli(DS, box, ["up"], timeout=300)
        status = str(data.get("status") or "ERROR")
        DS.STORE.audit("shell", "local", what="up", sandbox=box.name, status=status)
        return {"status": status, "restored": bool(data.get("restored")),
                **({"error": error_text(str(data.get("reason") or ""))} if status == "ERROR" else {})}

    return guarded(DS, box, work)


def stop(DS, box) -> tuple[int, dict]:
    """POST /api/sandbox/stop: end the command of the user's that runs now in ``box`` (`sandbox.py kill`, which works
    while a run holds sandbox.py's lock). Only then: it never touches an agent's turn, and nothing is stopped when idle."""
    if not busy(box) or STATE["light"]:
        return 409, {"error": "실행 중인 명령이 없습니다.", "code": "idle"}
    data = BOXES.cli(DS, box, ["kill"], timeout=60)
    status = str(data.get("status") or "ERROR")
    DS.STORE.audit("shell", "local", what="kill", sandbox=box.name, status=status)
    if status != "KILLED":
        return 500, {"error": f"멈추지 못했습니다: {error_text(str(data.get('reason') or ''))}"}
    return 200, {"status": status}


def restore(DS, box) -> tuple[int, dict]:
    """POST /api/sandbox/restore: put a sandbox that is NOT the agent's back to before its last command (the agent's
    own goes through the server's /api/live/sandbox/restore, which also keeps the turns' records right). As there:
    the container is dropped without a backup, started again, and the snapshot restored."""
    if BOXES.is_agent(DS, box):
        return 409, {"error": "에이전트가 쓰는 샌드박스는 에이전트 채팅의 되돌리기와 같은 길로 되돌립니다.", "code": "agent_box"}
    kept = BOXES.ledger(DS, box).get("restore_point")
    point = box.snapshots / kept if kept and "/" not in kept and (box.snapshots / kept).is_file() else BOXES.newest_snapshot(box)
    if point is None:
        return 409, {"error": "되돌릴 사본(스냅숏)이 없습니다.", "code": "no_snapshot"}

    def work() -> dict:
        for args in (["stop", "--force"], ["up"], ["restore", str(point)]):
            data = BOXES.cli(DS, box, args, timeout=300)
            if data.get("status") == "ERROR":
                DS.STORE.audit("shell", "local", what="restore", sandbox=box.name, failed=True, step=args[0])
                raise ValueError(f"{args[0]}: {error_text(str(data.get('reason') or ''))[-200:]}")
        BOXES.mark(DS, box, blocked=None, cleared=True)  # (the snapshot's own memory folder is not the store's: rewritten when used)
        DS.STORE.audit("shell", "local", what="restore", sandbox=box.name, snapshot=point.name)
        return {"restored": point.name, "time": point.stat().st_mtime}

    return guarded(DS, box, work)


def network_log(DS, box) -> dict:
    """GET /api/sandbox/network: where the sandbox went on the web, as its proxy wrote it down (host, port, let
    through or refused, when; never a path or a body). Only a sandbox with a proxy has one."""
    if box.network() not in ("allowlist", "open"):
        return {"sandbox": box.name, "network": box.network(), "events": [], "supported": False}
    data = BOXES.cli(DS, box, ["network-log"], timeout=60)
    events = []
    for line in str(data.get("log") or "").splitlines():
        at = line.find("{")
        if at < 0:
            continue
        try:
            event = json.loads(line[at:])
        except json.JSONDecodeError:
            continue
        if isinstance(event, dict) and event.get("event") == "destination" and event.get("host"):
            events.append({"host": str(event["host"])[:120], "port": event.get("port"), "allowed": event.get("outcome") == "ALLOW",
                           "time": event.get("time")})
    return {"sandbox": box.name, "network": box.network(), "events": events[-200:], "supported": True,
            **({"reason": error_text(str(data.get("reason") or ""))} if data.get("status") == "ERROR" else {})}

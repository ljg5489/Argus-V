"""A sandbox made of a dict, for tests and for looking at the page: it answers what SANDBOX/sandbox.py answers to the
commands argus_hook/sandbox_shell.py sends (files, read-file, status, up, run, fakenet-log, snapshot). No Docker, and
nothing is run: a `run` of the terminal's wrapper is played by a few words of its own (echo, cd, ls, cat, …), a `run`
of sandbox_shell.OPS by the same changes on the dict.

    box = FakeBox(); DS.run_sandbox_cli = box.cli; sandbox_shell.image_bytes = box.image
"""

from __future__ import annotations

import base64
import io
import json
import posixpath
import re
import shlex
import tarfile
import threading
import time
from pathlib import Path

HOME = "/workspace"
PNG = base64.b64decode("iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==")
MAGIC = ((b"\x89PNG\r\n\x1a\n", "image/png"), (b"\xff\xd8\xff", "image/jpeg"), (b"GIF87a", "image/gif"), (b"GIF89a", "image/gif"))


class FakeBox:
    def __init__(self, folder: Path | None = None):
        self.files: dict[str, bytes] = {}
        self.dirs: set[str] = {HOME}
        self.links: dict[str, str] = {}
        self.running = True
        self.calls: list[list[str]] = []
        self.asked: list[str] = []          # what the gateway (fakenet) is asked for (set by a test: every listing has them)
        self.fetched: list[tuple[float, str]] = []  # what a played `fetch` asked it for, and when
        self.delay = 0.0                    # seconds every run takes
        self.status_delay = 0.0             # seconds `status` takes (docker stats samples for a second or two)
        self.refuse: str | None = None      # sandbox.py's ERROR reason for every run (a failed snapshot, say)
        self.refuse_once: str | None = None  # … for the next run only
        self.report: dict | None = None     # fields laid over the next run's report
        self.limit = 1000                   # entries `files` lists
        self.folder = Path(folder) if folder else None  # where snapshots and run logs are written (None: names only)
        self.count = 0
        self.processes = [(1, 0, "0.0", "0.0", 86_400, "sleep infinity"), (40, 1, "1.5", "0.3", 12, "python3 server.py --port 8000")]
        self.locked = False                 # sandbox.py's own lock held by something else
        self.states: dict[str, tuple] = {}  # the tree as each snapshot found it (by the snapshot's file name)
        self.killed = threading.Event()     # `sandbox.py kill` while a run sleeps
        self.dead = False                   # the container is there but not running (killed): docker's own error, not STOPPED

    # ------------------------------------------------------------------ the dict as a file tree
    def write(self, path: str, data: bytes | str) -> None:
        folder = posixpath.dirname(path)
        while folder and folder != "/" and folder not in self.dirs:
            self.dirs.add(folder)
            folder = posixpath.dirname(folder)
        self.files[path] = data.encode("utf-8") if isinstance(data, str) else data

    def exists(self, path: str) -> bool:
        return path in self.files or path in self.dirs or path in self.links

    def children(self, folder: str) -> list[str]:
        return sorted(path for path in (*self.dirs, *self.files, *self.links) if path != folder and posixpath.dirname(path) == folder)

    def remove(self, path: str) -> None:
        self.files.pop(path, None)
        self.links.pop(path, None)
        if path in self.dirs:
            self.dirs.discard(path)
            for group in (self.files, self.links):
                for inner in [item for item in group if item.startswith(path + "/")]:
                    del group[inner]
            self.dirs -= {item for item in self.dirs if item.startswith(path + "/")}

    def move(self, old: str, new: str) -> None:
        for group in (self.files, self.links):
            for path in [item for item in group if item == old or item.startswith(old + "/")]:
                group[new + path[len(old):]] = group.pop(path)
        moved = {item for item in self.dirs if item == old or item.startswith(old + "/")}
        self.dirs = (self.dirs - moved) | {new + item[len(old):] for item in moved}

    def snapshot(self, name: str) -> str:
        self.count += 1
        self.states[f"{name}-{self.count}.tar"] = (dict(self.files), set(self.dirs), dict(self.links))
        if not self.folder:
            return f"/nowhere/snapshots/{name}-{self.count}.tar"
        path = self.folder / "snapshots" / f"{name}-{self.count}.tar"
        path.parent.mkdir(parents=True, exist_ok=True)
        with tarfile.open(path, "w") as archive:
            for member, data in sorted(self.files.items()):
                info = tarfile.TarInfo("./" + member[len(HOME) + 1:])
                info.size = len(data)
                archive.addfile(info, io.BytesIO(data))
        return str(path)

    # ------------------------------------------------------------------ sandbox.py's commands
    def cli(self, args, timeout=300):
        self.calls.append(list(args))
        action = args[0]
        if action == "kill":
            self.killed.set()
            self.running, self.dead = False, True
            return {"status": "KILLED", "recovery_snapshot": None, "working_copy_discarded": True}
        if action == "files":
            if self.dead:
                return {"status": "ERROR", "reason": "Error response from daemon: container 0123456789ab is not running"}
            if not self.running:
                return {"status": "STOPPED", "root": HOME, "entries": []}
            entries = [{"path": path, "kind": "directory", "size": None} for path in self.dirs if path != HOME]
            entries += [{"path": path, "kind": "file", "size": len(data)} for path, data in self.files.items()]
            entries += [{"path": path, "kind": "symlink", "size": None} for path in self.links]
            entries.sort(key=lambda entry: entry["path"])
            return {"status": "RUNNING", "root": HOME, "entries": entries[:self.limit], "truncated": len(entries) > self.limit}
        if action == "read-file":
            return self.read_file(args[-1])
        if action == "status":
            if self.locked:
                return {"status": "ERROR", "reason": "another sandbox operation is active"}
            time.sleep(self.status_delay)
            if self.dead:
                return {"status": "ERROR", "reason": "Error response from daemon: container 0123456789ab is not running"}
            if not self.running:
                return {"status": "STOPPED", "container": None}
            used = sum(len(data) for data in self.files.values())
            return {"status": "RUNNING", "container": "0123456789ab",
                    "resources": {"CPUPerc": "1.52%", "MemUsage": "38.4MiB / 4GiB", "MemPerc": "0.94%", "PIDs": str(len(self.processes))},
                    "disk": "Filesystem      Size  Used Avail Use% Mounted on\n"
                            f"tmpfs           2.0G  {max(1, used // 1024)}K  2.0G   1% /workspace\ntmpfs           256M     0  256M   0% /tmp\n"}
        if action == "up":
            was = self.running
            self.running, self.dead = True, False
            self.killed.clear()
            return {"status": "RUNNING", "container": "0123456789ab", "restored": None if was else "/nowhere/snapshots/before-run.tar"}
        if action == "fakenet-log":
            since = float(args[args.index("--since") + 1]) if "--since" in args else 0.0
            return {"status": "OK", "events": [{"kind": "http", "path": path} for path in self.asked]
                    + [{"kind": "http", "path": path, "time": at} for at, path in self.fetched if at >= since]}
        if action == "snapshot":
            return {"snapshot": self.snapshot("after-shell")}
        if action == "run":
            return self.run(args[args.index("--") + 1:], int(args[args.index("--timeout") + 1]))
        if action == "stop":  # (--force: a workspace that cannot be snapshotted is dropped)
            self.running = False
            if self.links:
                self.files, self.dirs, self.links = {}, {HOME}, {}
            return {"status": "STOPPED"}
        if action == "restore":
            kept = self.states.get(posixpath.basename(args[-1]))
            if kept:
                self.files, self.dirs, self.links = dict(kept[0]), set(kept[1]), dict(kept[2])
            return {"status": "RESTORED"}
        return {"status": "ERROR", "reason": f"unexpected {action}"}

    def read_file(self, path: str) -> dict:
        if not self.running:
            return {"status": "ERROR", "reason": "sandbox is not running; run up first"}
        if path in self.links:
            return {"status": "ERROR", "reason": "OSError: [Errno 40] Too many levels of symbolic links"}
        if path in self.dirs:
            return {"status": "ERROR", "reason": "IsADirectoryError: [Errno 21] Is a directory"}
        if path not in self.files:
            return {"status": "ERROR", "reason": f"Traceback …\nFileNotFoundError: [Errno 2] No such file or directory: '{posixpath.basename(path)}'"}
        data = self.files[path]
        mime = next((kind for magic, kind in MAGIC if data.startswith(magic)), None)
        if mime:
            return {"path": path, "size": len(data), "content": "", "binary": True, "mime": mime, "truncated": False}
        truncated, data = len(data) > 65_536, data[:65_536]
        try:
            text = data.decode("utf-8", errors="ignore" if truncated else "strict")
            binary = any(ord(ch) < 32 and ch not in "\t\n\r" for ch in text)
        except UnicodeDecodeError:
            text, binary = "", True
        return {"path": path, "size": len(self.files[path]), "content": "" if binary else text, "binary": binary,
                "truncated": truncated, "limit": 65_536}

    def image(self, DS, box, path: str) -> tuple[str, bytes]:  # sandbox_shell.image_bytes
        data = self.files[path]
        return next(kind for magic, kind in MAGIC if data.startswith(magic)), data

    def run(self, argv: list[str], timeout: int) -> dict:
        if self.locked:
            return {"status": "ERROR", "reason": "another sandbox operation is active"}
        if not self.running:
            return {"status": "ERROR", "reason": "sandbox is not running; run up first"}
        if self.refuse_once:
            reason, self.refuse_once = self.refuse_once, None
            return {"status": "ERROR", "reason": reason}
        if self.refuse:
            return {"status": "ERROR", "reason": self.refuse}
        if self.links:  # as sandbox.py: a workspace with a link in it cannot be snapshotted
            return {"status": "ERROR", "reason": "archive contains unsupported paths, links or special files"}
        backup = self.snapshot("before-run")
        kept = (dict(self.files), set(self.dirs), dict(self.links))
        self.killed.wait(self.delay) if self.delay else None
        if argv[:2] == ["bash", "-c"]:
            code, out, err, status = self.bash(argv[2], timeout)
        elif argv[:4] == ["python3", "-I", "-S", "-c"]:
            code, out, err, status = 0, json.dumps(self.op(*argv[5:])) + "\n", "", "FINISHED"
        elif argv[0] == "ps":
            rows = [*self.processes, (90, 1, "0.0", "0.0", 0, "timeout --signal=TERM --kill-after=5s 20s ps -eo pid=,ppid=,pcpu=,pmem=,etimes=,args="),
                    (91, 90, "0.0", "0.0", 0, "ps -eo pid=,ppid=,pcpu=,pmem=,etimes=,args=")]
            code, out, err, status = 0, "".join(f"{pid:>7} {ppid:>7} {cpu:>4} {mem:>4} {age:>7} {args}\n" for pid, ppid, cpu, mem, age, args in rows), "", "FINISHED"
        else:
            code, out, err, status = 127, "", f"{argv[0]}: not found\n", "FINISHED"
        raw_out, raw_err = out.encode("utf-8"), err.encode("utf-8")
        report = {"status": status, "exit_code": code if status == "FINISHED" else None, "command": argv,
                  "bytes": {"stdout": len(raw_out), "stderr": len(raw_err)}, "recovery_snapshot": backup,
                  "environment_stopped": status != "FINISHED", "cleanup_error": None,
                  "stdout_tail": raw_out[-32_768:].decode("utf-8", errors="replace"),
                  "stderr_tail": raw_err[-32_768:].decode("utf-8", errors="replace")}
        if self.folder:  # sandbox.py keeps each run's whole output in its own folder
            logs = self.folder / "artifacts" / f"run-{self.count}"
            logs.mkdir(parents=True, exist_ok=True)
            (logs / "stdout.log").write_bytes(raw_out)
            (logs / "stderr.log").write_bytes(raw_err)
            report["logs"] = str(logs)
        if self.killed.is_set():  # killed under it: exit 137, and the workspace is the snapshot's when it starts again
            status, report["status"], report["exit_code"], report["environment_stopped"] = "RESOURCE_OR_SIGNAL", "RESOURCE_OR_SIGNAL", 137, True
            self.files, self.dirs, self.links = kept
        if status != "FINISHED":
            self.running, self.dead = False, True
        if self.report:
            report.update(self.report)
            self.report = None
        return report

    # ------------------------------------------------------------------ sandbox_shell.OPS, on the dict
    def op(self, op: str, path: str, extra: str = "") -> dict:
        parent = posixpath.dirname(path)
        if op == "kill":
            found = [row for row in self.processes if row[0] == int(path)]
            self.processes = [row for row in self.processes if row[0] != int(path)]
            return {"ok": True} if found else {"ok": False, "code": "missing"}
        if op in ("mkdir", "touch"):
            if self.exists(path):
                return {"ok": False, "code": "exists"}
            if parent not in self.dirs:
                return {"ok": False, "code": "missing"}
            if op == "mkdir":
                self.dirs.add(path)
            else:
                self.files[path] = b""
        elif op == "rename":
            if self.exists(extra):
                return {"ok": False, "code": "exists"}
            if not self.exists(path) or posixpath.dirname(extra) not in self.dirs:
                return {"ok": False, "code": "missing"}
            self.move(path, extra)
        elif op == "delete":
            if not self.exists(path):
                return {"ok": False, "code": "missing"}
            self.remove(path)
        elif op == "save":
            if path in self.dirs or path in self.links:
                return {"ok": False, "code": "kind"}
            if parent not in self.dirs:
                return {"ok": False, "code": "missing"}
            self.files[path] = base64.b64decode(extra)
        else:
            return {"ok": False, "code": "op"}
        return {"ok": True}

    # ------------------------------------------------------------------ the terminal's wrapper, played
    def bash(self, script: str, timeout: int):
        lines = script.split("\n")
        cwd = shlex.split(lines[0])[2]
        cwd = cwd if cwd in self.dirs or not cwd.startswith(HOME) else HOME
        token = re.search(r'printf "\\n%s%s\\n" (\S+) ', lines[1]).group(1)
        typed = "\n".join(lines[2:])
        typed = typed.split("unset __argus_name\n", 1)[-1]  # after the wrapper's own helper functions (tree, ll, …)
        out, err, code, status = [], [], 0, "FINISHED"
        for part in re.split(r"\s*(?:;|&&|\n)\s*", typed.strip()):
            words = shlex.split(part)
            if not words:
                continue
            name, rest = words[0], words[1:]
            target = None  # `> file`, `>&2`
            if ">&2" in rest:
                rest.remove(">&2")
                target = err
            elif ">" in rest:
                at = rest.index(">")
                target, rest = posixpath.normpath(posixpath.join(cwd, rest[at + 1])), rest[:at]
            said, code = "", 0
            if name == "echo":
                said = " ".join(rest) + "\n"
            elif name == "pwd":
                said = cwd + "\n"
            elif name == "cd":
                where = posixpath.normpath(posixpath.join(cwd, rest[0])) if rest else HOME
                if where in self.dirs or not where.startswith(HOME):
                    cwd = where
                else:
                    err.append(f"bash: line 3: cd: {rest[0]}: No such file or directory\n")
                    code = 1
            elif name == "ls":
                where = posixpath.normpath(posixpath.join(cwd, rest[0])) if rest else cwd
                said = "".join(posixpath.basename(path) + "\n" for path in self.children(where))
            elif name == "cat":
                where = posixpath.normpath(posixpath.join(cwd, rest[0]))
                if where in self.files:
                    said = self.files[where].decode("utf-8", errors="replace")
                else:
                    err.append(f"cat: {rest[0]}: No such file or directory\n")
                    code = 1
            elif name in ("mkdir", "touch", "rm"):
                where = posixpath.normpath(posixpath.join(cwd, rest[-1]))
                result = self.op({"rm": "delete"}.get(name, name), where)
                code = 0 if result["ok"] else 1
            elif name == "ln":  # ln -s target name
                self.links[posixpath.normpath(posixpath.join(cwd, rest[-1]))] = rest[-2]
            elif name == "big":  # a long output
                said = "".join(f"line {number:06d}\n" for number in range(int(rest[0])))
            elif name == "fetch":  # an address built at run time: the gateway's log has it
                self.fetched.append((time.time(), rest[0]))
                said = "PAGE TEXT\n"
                self.write(posixpath.join(cwd, "page.html"), "<html>PAGE TEXT</html>")
            elif name == "sleep":
                if float(rest[0]) > timeout:
                    status = "TIMEOUT"
                    break
                if self.killed.wait(min(float(rest[0]), 8)):
                    break
            elif name == "exit":
                code = int(rest[0]) if rest else 0
                break
            elif name == "false":
                code = 1
            elif name != "true":
                err.append(f"bash: line 3: {name}: command not found\n")
                code = 127
            if isinstance(target, str):
                self.write(target, said)
            elif target is err:
                err.append(said)
            else:
                out.append(said)
        err.append(f"\n{token}{cwd}\n")
        return code, "".join(out), "".join(err), status

"""An extra sandbox folder next to SANDBOX/ (SANDBOX_PC, SANDBOX_NET): SANDBOX/sandbox.py as it is, run on that folder.

SANDBOX/ is locked by plan v1.6 (the first GPU run uses it, byte for byte). An extra folder has its own Dockerfile,
settings, container, snapshots and state; its sandbox.py and desk.py are a few lines that call this module. Nothing
here edits or copies the locked script: it is loaded as it is, and three things are told apart from it:

- the folder: its Runtime is made with that folder as its root (its compose project is named after the root, so two
  sandboxes never share a container, a network or a snapshot);
- the image: the folder's own name for every service (the locked script names local/generic-sandbox:python);
- the display: DISPLAY=:1 for what runs in it (the folder's image has an X server to start: desktop/start.sh).

Every isolation rule of the locked script holds in such a folder as in SANDBOX/ (the script checks them on the
container it finds): user 10001, read-only root, no capability, no published port, tmpfs /workspace and /tmp only,
an internal network. Run with python3.11 (as the locked script is); the standard library only.
"""

import sys

sys.dont_write_bytecode = True  # nothing is written next to the locked script (SANDBOX/__pycache__)

import functools  # noqa: E402
import importlib.util  # noqa: E402
import json  # noqa: E402
import os  # noqa: E402
import subprocess  # noqa: E402
import tarfile  # noqa: E402
from pathlib import Path  # noqa: E402

LOCKED = Path(__file__).resolve().parents[1] / "SANDBOX" / "sandbox.py"
DISPLAY = ":1"
SIZES = {(800, 600), (1024, 640), (1280, 720), (1280, 800)}


def load(root: Path, image: str):
    """The locked script as a module, with ``root`` as its root and ``image`` as its image."""
    root = Path(root).resolve()
    spec = importlib.util.spec_from_file_location("argus_locked_sandbox", LOCKED)
    core = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = core
    spec.loader.exec_module(core)
    locked_spec = core.compose_spec

    def compose_spec(settings, owner, folder=root):
        result = locked_spec(settings, owner, folder)
        for service in result["services"].values():
            service["image"] = image
        result["services"]["sandbox"]["environment"]["DISPLAY"] = DISPLAY
        return result

    core.compose_spec = compose_spec  # Runtime.render looks the name up when it is called
    core.Runtime = functools.partial(core.Runtime, root=root)  # main() makes its Runtime by this name
    return core


def main(root: Path, image: str, argv=None) -> int:
    """sandbox.py of the folder: every command of the locked script, on this folder."""
    core = load(root, image)
    try:
        return core.main(argv)
    except (RuntimeError, ValueError, OSError, tarfile.TarError, subprocess.TimeoutExpired, KeyboardInterrupt) as exc:
        # as the locked script's own last lines: its error as JSON on stderr, exit 2
        print(json.dumps({"status": "ERROR", "reason": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


def desk(root: Path, image: str, argv=None) -> int:
    """desk.py of the folder: the screen of its sandbox, for the local server (argus_hook/sandbox_screen.py).

        screen-start [W H]   start the desktop (or leave it running)      -> JSON
        screen-stop          end it                                       -> JSON
        screen-state         is a desktop on?                             -> JSON
        screen-shot          one JPEG of the screen on stdout
        screen-stream        an endless stream of pictures on stdout (multipart)
        screen-input         keyboard and mouse events, JSON lines on stdin

    Everything is a `docker exec` in the sandbox's own container, found and checked by the locked script's own code
    (Runtime.cid). No port is opened anywhere: pictures and events travel over the exec's own pipes. None of it takes
    sandbox.py's lock or a snapshot. The programs it runs are the image's own (/opt/desktop), python isolated (-I)."""
    args = list(sys.argv[1:] if argv is None else argv)
    action = args[0] if args else ""
    runtime = load(root, image).Runtime()

    def docker(*inside: str, interactive: bool = False) -> list[str]:
        cid = runtime.cid()
        return runtime.command(["exec", *(["--interactive"] if interactive else []), "--workdir", "/", cid, *inside])

    def said(*inside: str, timeout: int = 30) -> str:
        done = subprocess.run(docker(*inside), capture_output=True, text=True, env=runtime.environment, timeout=timeout)
        return (done.stdout or "").strip() or (done.stderr or "").strip()[-300:]

    try:
        if action == "screen-start":
            size = (int(args[1]), int(args[2])) if len(args) >= 3 else (1024, 640)
            if size not in SIZES:
                raise ValueError("screen size must be one of " + ", ".join(f"{w}x{h}" for w, h in sorted(SIZES)))
            line = said("/opt/desktop/start.sh", str(size[0]), str(size[1]))
            ready = line.startswith("READY")
            print(json.dumps({"status": "READY" if ready else "ERROR", "size": line.split()[-1] if ready else None,
                              **({} if ready else {"reason": line[-300:] or "the desktop did not start"})}, ensure_ascii=False))
            return 0 if ready else 2
        if action == "screen-stop":
            print(json.dumps({"status": "STOPPED", "said": said("/opt/desktop/stop.sh")[-100:]}, ensure_ascii=False))
            return 0
        if action == "screen-state":
            line = said("sh", "-c", "xdpyinfo 2>/dev/null | awk '/dimensions:/{print $2; exit}'")
            print(json.dumps({"status": "ON" if "x" in line else "OFF", "size": line if "x" in line else None}))
            return 0
        if action in ("screen-shot", "screen-stream", "screen-input"):
            program = {"screen-shot": ["/opt/desktop/screen.py", "--once"], "screen-stream": ["/opt/desktop/screen.py", *args[1:5]],
                       "screen-input": ["/opt/desktop/input.py"]}[action]
            command = docker("python3", "-I", *program, interactive=action == "screen-input")
            os.execve(command[0], command, runtime.environment)  # the docker client takes this process's place (and its pipes)
        raise ValueError("unknown action: " + (action or "(none)"))
    except (RuntimeError, ValueError, OSError, subprocess.TimeoutExpired) as exc:
        print(json.dumps({"status": "ERROR", "reason": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2

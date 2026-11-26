"""Local companion API for the Argus-V Scenario Studio Site.

Run from the repository root with Python 3.11:
    python argus_hook/dashboard_server.py

The server binds to loopback only. The browser dashboard can use this API while
the saved Site remains a static, private front end. Replay inference reuses the
existing replay_demo.py record/hidden-state pipeline without modifying it.

The agent chat tab uses /api/live/*: for each chat task argus_hook/live_agent.py
loads the local gpt-oss-20b, works in the SANDBOX and reports every step with its
Argus-V-emp verdict while it happens. live_agent_service.py keeps the events and
shuts the worker down when the task ends, so the model leaves the GPU.

Conversations and memory (argus_hook/agent_memory.py): a chat task belongs to a
conversation, whose earlier turns go to the worker with the task. The agent keeps
its memory in the sandbox (/workspace/.agent); this server keeps the approved copy
of every memory file with its versions and a review queue (the ledger), and every
conversation as JSON, under artifacts/live-agent/memory. record_turn stores each
turn and passes the memory the worker reports to the ledger.

/api answers only requests addressed to this machine by name (Host 127.0.0.1,
localhost or ::1), so a web page cannot reach it through DNS rebinding, and
refuses POST requests from web origins it does not allow.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import uuid
from datetime import datetime, timezone
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import agent_memory as AM
from live_agent_service import LiveAgent


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "sites" / "argus-v-demo-dashboard" / "dist"
ASSETS = ROOT / "argus_hook" / "replay_assets"
SCORES_FILE = ASSETS / "argus_v_p_scores.json"
DESCRIPTIONS_FILE = ASSETS / "scenario_descriptions.json"
REPLAY_SCRIPT = ROOT / "argus_hook" / "replay_demo.py"
AGENT_SCRIPT = ROOT / "argus_hook" / "agent_loop.py"
LIVE_SCRIPT = ROOT / "argus_hook" / "live_agent.py"
SANDBOX_SCRIPT = ROOT / "SANDBOX" / "sandbox.py"
EMP_MANIFEST = ROOT / "artifacts" / "risk-loop" / "resplit-1117" / "argus_v_emp" / "manifest.json"
JOBS: dict[str, dict] = {}
JOBS_LOCK = threading.Lock()
_RUNTIME_LOCK = threading.Lock()
_PYTHON311: str | None | bool = False
_CUDA_AVAILABLE: bool | None = None
MAX_TASK_CHARS = 4_000
ALLOWED_ORIGINS = {
    "http://127.0.0.1:8765",
    "http://localhost:8765",
    "https://ljg5489.github.io",  # GitHub Pages copy of the dashboard
} | ({os.environ["ARGUS_SITE_ORIGIN"]} if os.environ.get("ARGUS_SITE_ORIGIN") else set())
# Pages served from this machine. Only they may raise what the agent trusts: approve a held memory change, roll a
# memory file back, or edit AGENTS.md (which becomes part of the system prompt). Other allowed pages can chat, read
# and reject.
LOCAL_PAGE_HOSTS = {"127.0.0.1", "localhost", "::1"}
LIVE_LOG_DIR = ROOT / "artifacts" / "live-agent"
RESUME_CHARS = 24_000  # replayed command/output text when a turn is continued
RESUME_PAIRS = 2       # the latest command/output pairs replayed in full; earlier commands are listed
MAX_LIVE_STEPS = 10
MODEL_CHECKPOINTS = {
    "P5": ASSETS / "argus_v_p_P5.bundle",
    "P6": ASSETS / "argus_v_p_P6.bundle",
    "EM32": ROOT / "artifacts" / "risk-loop" / "argus-v-em" / "argus_v_em_round01.pt",
    "EM300": ROOT / "artifacts" / "risk-loop" / "argus-v-em300" / "argus_v_em300.pt",
}
MODEL_NAMES = {
    "P5": "Argus-V-p · P5",
    "P6": "Argus-V-p · P6",
    "EM32": "Argus-V-em · EM32 / epoch 60",
    "EM300": "Argus-V-em300 · EM32 / epoch 300",
}


def python311_executable() -> str | None:
    """Resolve the executable name hard-coded by the existing sandbox client."""
    global _PYTHON311
    if _PYTHON311 is not False:
        return _PYTHON311
    found = shutil.which("python3.11") or shutil.which("python3.11.exe")
    if found:
        _PYTHON311 = found
        return _PYTHON311
    if os.name != "nt" or sys.version_info[:2] != (3, 11):
        _PYTHON311 = None
        return None
    alias_dir = Path(tempfile.gettempdir()) / "argus-scenario-studio-runtime"
    alias = alias_dir / "python3.11.exe"
    try:
        alias_dir.mkdir(exist_ok=True)
        if not alias.is_file():
            shutil.copy2(sys.executable, alias)
        result = subprocess.run([str(alias), "--version"], capture_output=True, text=True, timeout=8)
        _PYTHON311 = str(alias) if result.returncode == 0 else None
    except (OSError, subprocess.SubprocessError):
        _PYTHON311 = None
    return _PYTHON311


def child_env(python311: bool = False) -> dict:
    """Environment of a child process; ``python311`` puts the sandbox client's python3.11 alias on PATH."""
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    if python311:
        alias = python311_executable()
        if alias:
            env["PATH"] = str(Path(alias).parent) + os.pathsep + env.get("PATH", "")
    return env


def live_env() -> dict:
    env = child_env(python311=True)
    env["PYTHONUNBUFFERED"] = "1"
    return env


# The live chat worker (argus_hook/live_agent.py) holds gpt-oss-20b on the GPU only while a chat task runs.
LIVE = LiveAgent([sys.executable, str(LIVE_SCRIPT)], ROOT, live_env)
# Conversations and the mirror of the agent's sandbox memory (git-ignored, like the task records next to it).
DEFAULT_MEMORY_ROOT = ROOT / "artifacts" / "live-agent" / "memory"
MEMORY_ROOT = Path(os.environ.get("ARGUS_LIVE_MEMORY_DIR") or DEFAULT_MEMORY_ROOT)
STORE = AM.ConversationStore(MEMORY_ROOT)
LIVE.keep_load_times(MEMORY_ROOT / "load_times.json")
CONVERSATION_PATH = re.compile(r"/api/live/conversations/(c-[0-9]{8}-[0-9a-f]{8})(?:/(rename|delete|fork))?")
RESUME_CHAIN_MAX = 5  # turns one request may be continued over
LOCAL_HOSTS = {"127.0.0.1", "localhost", "::1", ""}
_RECORDING: threading.Thread | None = None  # the recorder of the latest task
_RECORDING_LOCK = threading.Lock()


def sandbox_files() -> AM.SandboxFiles:
    """The sandbox's memory folder as the API reaches it without a worker (a plan run clears it this way; a turn of
    a page elsewhere is checked this way before the model loads). A stopped sandbox is started once, without a model."""
    def restart() -> None:
        from agent_loop import RealSandboxClient

        RealSandboxClient(str(SANDBOX_SCRIPT)).ensure_running()

    return AM.SandboxFiles(SANDBOX_SCRIPT, env=live_env(), restart=restart)


def _code_hashes() -> dict:
    import hashlib

    names = ("argus_hook/dashboard_server.py", "argus_hook/agent_memory.py", "argus_hook/live_agent_service.py")
    return {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in names if (ROOT / name).is_file()}


SERVER_CODE = _code_hashes()  # the code this server runs (read when it started; files changed later do not count)


def store_identity() -> dict:
    """Which memory root the server keeps (a hash of its path), whether it is the user's own, and the hashes of the
    code the server started with."""
    root = Path(STORE.root).resolve()
    return {"id": AM.sha(str(root))[:12], "custom": root != DEFAULT_MEMORY_ROOT.resolve(), "code": SERVER_CODE}


def configure_for_tests(memory_root: Path) -> None:
    """Keep conversations and memory under ``memory_root`` (UI tests with a fake worker)."""
    global STORE
    STORE = AM.ConversationStore(memory_root)
    LIVE.keep_load_times(Path(memory_root) / "load_times.json")
    _REMOTE_REFUSAL.clear()


def uses_gpu(job: dict) -> bool:
    """Jobs that load gpt-oss-20b themselves (they cannot run next to the live worker on one GPU)."""
    return job["kind"] == "agent" or (job["kind"] == "replay" and job.get("mode") == "tokens")


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def scenario_catalog() -> dict:
    table = read_json(SCORES_FILE)
    descriptions = read_json(DESCRIPTIONS_FILE).get("scenarios", {}) if DESCRIPTIONS_FILE.exists() else {}
    recommended = set(table.get("recommended_units", []))
    scenarios: dict[str, dict] = {}
    for unit_id, unit in table["units"].items():
        row = scenarios.setdefault(unit["scenario"], {
            "id": unit["scenario"], "runs": [], "violations": 0, "recommended": 0,
        })
        violations = [step for step in unit["steps"] if int(step[2]) == 1]
        row["violations"] += len(violations)
        row["runs"].append({
            "id": unit_id,
            "condition": unit["condition"],
            "seed": unit["seed"],
            "family": unit.get("family", ""),
            "recommended": unit_id in recommended,
            "violation_count": len(violations),
            "steps": [
                {"index": int(s[0]), "tool": s[1], "label": int(s[2]), "p6": float(s[3]), "p5": float(s[4])}
                for s in unit["steps"]
            ],
        })
        row["recommended"] += int(unit_id in recommended)
    out = []
    for scenario_id, row in sorted(scenarios.items()):
        desc = descriptions.get(scenario_id, {})
        row.update({
            "title": desc.get("title") or scenario_id,
            "category": desc.get("category", ""),
            "task": desc.get("task", ""),
            "situation": desc.get("situation", ""),
            "forbidden": desc.get("forbidden", ""),
        })
        row["runs"].sort(key=lambda run: (not run["recommended"], run["condition"], str(run["seed"]), run["id"]))
        out.append(row)
    return {"scenarios": out, "models": table.get("step_columns", []), "source_note": table.get("note", "")}


def available_models() -> list[dict]:
    return [{"id": key, "name": MODEL_NAMES[key]}
            for key, path in MODEL_CHECKPOINTS.items() if path.is_file()]


def runtime_status() -> dict:
    catalog = scenario_catalog()
    model_dir = Path.home() / "Desktop" / "Argus-V" / "gpt-oss-20b"
    sandbox = ROOT / "SANDBOX" / "sandbox.py"
    docker = shutil.which("docker") or shutil.which("docker.exe")
    global _CUDA_AVAILABLE
    if _CUDA_AVAILABLE is None:
        with _RUNTIME_LOCK:
            if _CUDA_AVAILABLE is None:
                try:
                    import torch

                    _CUDA_AVAILABLE = bool(torch.cuda.is_available())
                except Exception:
                    _CUDA_AVAILABLE = False
    with JOBS_LOCK:
        active = next((job["id"] for job in JOBS.values() if job["process"].poll() is None), None)
    return {
        "ok": True,
        "python": sys.version.split()[0],
        "scenario_count": len(catalog["scenarios"]),
        "run_count": sum(len(s["runs"]) for s in catalog["scenarios"]),
        "p5_bundle": (ASSETS / "argus_v_p_P5.bundle").is_file(),
        "p6_bundle": (ASSETS / "argus_v_p_P6.bundle").is_file(),
        "available_models": available_models(),
        "local_rollouts": any((ROOT / "artifacts" / name).is_dir() for name in ("rollouts", "rollouts-v2", "rollouts-dec-v1")),
        "agent_model_dir": model_dir.is_dir(),
        "cuda_available": _CUDA_AVAILABLE,
        "sandbox_script": sandbox.is_file(),
        "docker_available": bool(docker),
        "python311_command": bool(python311_executable()),
        "emp_bundle": EMP_MANIFEST.is_file(),
        "live_script": LIVE_SCRIPT.is_file(),
        "live_memory": True,
        "live": LIVE.status(),
        "active_job": active,
    }


def live_missing(health: dict) -> list[str]:
    """What the live chat still needs on this machine."""
    return [label for key, label in (
        ("agent_model_dir", "gpt-oss-20b 로컬 모델"),
        ("cuda_available", "CUDA GPU"),
        ("sandbox_script", "샌드박스 스크립트"),
        ("docker_available", "Docker"),
        ("python311_command", "Python 3.11 sandbox 호출"),
        ("emp_bundle", "Argus-V-emp 모델 파일"),
        ("live_script", "argus_hook/live_agent.py"),
    ) if not health[key]]


def resumable(turn: dict) -> bool:
    """A turn can be continued when it ended without an answer, or when its answer came at the step that was told
    it was the last one (a partial answer: what was found and what is left)."""
    steps = turn.get("steps") or []
    ran = any(step.get("kind") == "bash" for step in steps)
    partial = bool(turn.get("answer")) and any(step.get("hinted") and step.get("kind") == "stop" for step in steps)
    return ran and (not turn.get("answer") or partial)


def resume_chain(turns: list[dict], target: dict) -> list[dict]:
    """The turns one continued request ran in, oldest first (target, the turn it resumed, and so on)."""
    by_number = {turn.get("turn"): turn for turn in turns}
    chain, seen, turn = [], set(), target
    while turn is not None and turn.get("turn") not in seen:
        seen.add(turn.get("turn"))
        chain.insert(0, turn)
        turn = by_number.get(turn.get("resume_of"))
    return chain


def run_messages(run_id: str) -> list[dict]:
    """The command/output messages a run added to its context (its task file), [] when the file is gone."""
    path = LIVE_LOG_DIR / f"{run_id}.jsonl"
    if not (AM.RUN_ID.fullmatch(run_id or "") and path.is_file()):
        return []
    messages = []
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            continue
        if record.get("type") == "context_append":
            messages += [message for message in record.get("messages") or [] if isinstance(message, dict)]
    return messages


MEMORY_OUTPUT = "(The output of that command is not repeated here; run it again if you need it.)"


def memory_command_note(command: str | None) -> str:
    """What a replay shows instead of a command on the memory files (its text can carry held or rejected lines)."""
    paths = ", ".join(AM.memory_paths(command)) or "the memory files"
    return f"# (a command on {paths}; its text is not repeated here)"


def held_keys() -> set[str]:
    """Keys of the memory lines that must not come back through a replay: rejected ones and those waiting for review."""
    keys = set(STORE.rejected_keys())
    for item in STORE.memory().get("review") or []:
        keys |= {AM.line_key(line) for line in item.get("new") or [] if line.strip()}
    return keys


def carries_held(text: str | None, keys: set[str]) -> bool:
    return bool(keys) and any(AM.line_key(line) in keys for line in (text or "").splitlines() if line.strip())


def resume_material(turn: dict, turns: list[dict] | None = None, keys: set[str] | None = None) -> dict:
    """A turn to continue: the request it answers, its latest command/output pairs exactly as the agent read them
    (its task file; else the conversation record), every earlier command of the request as a list (command, exit
    code, output size; no output text), and its partial answer if it gave one."""
    chain = resume_chain(turns or [turn], turn)
    keys = held_keys() if keys is None else keys

    def hidden(command: str | None, output: str | None) -> bool:  # held or rejected lines must not come back
        return AM.touches_memory_files(command) or carries_held(command, keys) or carries_held(output, keys)

    out = {"turn": turn.get("turn"), "task": turn.get("request") or turn.get("task") or "", "messages": [],
           "steps": [], "source": "record", "earlier": [], "partial": None}
    messages = run_messages(turn.get("run_id") or turn.get("source_run_id") or "")  # a fork's copy: the original run
    if messages:
        out["source"] = "task_log"
    else:
        out["steps"] = [{"command": memory_command_note(step.get("command")), "observation": MEMORY_OUTPUT}
                        if hidden(step.get("command"), step.get("observation"))
                        else {"command": step.get("command"), "observation": step.get("observation")}
                        for step in turn.get("steps") or [] if step.get("kind") == "bash"]
    # The newest pairs while RESUME_CHARS lasts (at most RESUME_PAIRS); everything before them is listed instead.
    pairs = [messages[index:index + 2] for index in range(0, len(messages) - 1, 2)]
    kept, used = [], 0
    for pair in reversed(pairs):
        cost = sum(len(message.get("content") or "") for message in pair)
        if kept and (used + cost > RESUME_CHARS or len(kept) >= RESUME_PAIRS):
            break
        kept.insert(0, pair)
        used += cost
    for pair in kept:  # a command on the memory files carries lines that may be held or rejected: not replayed
        if len(pair) == 2 and hidden(pair[0].get("content"), pair[1].get("content")):
            pair[0], pair[1] = ({**pair[0], "content": f"```bash\n{memory_command_note(pair[0].get('content'))}\n```"},
                                {**pair[1], "content": MEMORY_OUTPUT})
    out["messages"] = [message for pair in kept for message in pair]
    shown = len(kept) if messages else len(out["steps"])
    for index, link in enumerate(chain):
        ran = [step for step in link.get("steps") or [] if step.get("kind") == "bash"]
        if link is turn:
            ran = ran[:max(0, len(ran) - shown)]
        out["earlier"] += [{"command": AM.shown_command(step.get("command"), 200), "exit_code": step.get("exit_code"),
                            "output_chars": step.get("output_chars"), "turn": link.get("turn"),
                            **({"undone": step["undone"]} if step.get("undone") else {})} for step in ran]
    out["dropped"] = len(out["earlier"])
    if turn.get("answer"):
        out["partial"] = turn["answer"]
    after = turn.get("undone_after_answer")
    if after:  # its last command's work was taken away after it: the replay says so, not "succeeded"
        out["undone"] = {"command": AM.undone_command(turn), "kind": after.get("kind") if isinstance(after, dict) else None,
                         "stage": after.get("stage") if isinstance(after, dict) else None,
                         "whole": bool(after.get("whole")) if isinstance(after, dict) else False,
                         "first": AM.first_command(turn)}
    return out


class ApiRefusal(ValueError):
    """A refused start: ``status`` 400 or 403 (``local_only``), with a short ``code`` a client can act on."""

    def __init__(self, message: str, code: str | None = None, status: int = 400):
        super().__init__(message)
        self.code, self.status = code, status


_REMOTE_REFUSAL: dict = {}  # the last refusal of a page elsewhere's turn: repeated for a minute without a sandbox run


def remote_sandbox_check() -> None:
    """Before a page elsewhere's memory-off turn loads the model (1-2 minutes on the GPU): processes an earlier
    command left running, or python/git hooks under HOME, would make the worker refuse it anyway. Each check is a
    sandbox run (sandbox.py snapshots /workspace first), so a refusal is kept for a minute; a stopped sandbox is not
    started for a page elsewhere (the worker starts it and checks again before the turn)."""
    if _REMOTE_REFUSAL and time.monotonic() - _REMOTE_REFUSAL["at"] < 60:
        STORE.audit("start", "remote", refused=True, reason=_REMOTE_REFUSAL["code"])
        raise ApiRefusal(_REMOTE_REFUSAL["message"], _REMOTE_REFUSAL["code"], 409)
    files = sandbox_files()
    files.restart = None
    try:
        workspace = files.workspace()
    except Exception as error:
        if "stopped" in str(error) or "not running" in str(error):
            return
        refusal = (f"샌드박스를 확인하지 못해 이 턴을 실행하지 않습니다: {type(error).__name__}", "sandbox_unchecked")
    else:
        if not (workspace.get("strays") or workspace.get("hooks")):
            _REMOTE_REFUSAL.clear()
            return
        refusal = (AM.leftover_text(workspace, names_shown=False) + " · 이 페이지의 턴은 실행하지 않습니다. 로컬 페이지의 기억 카드에서 "
                   "'샌드박스 점검'으로 확인하고 정리할 수 있습니다.", "sandbox_not_clean")
    _REMOTE_REFUSAL.update(at=time.monotonic(), message=refusal[0], code=refusal[1])
    STORE.audit("start", "remote", refused=True, reason=refusal[1])
    raise ApiRefusal(refusal[0], refusal[1], 409)


_SCORER: dict = {}
_SCORER_LOCK = threading.Lock()
EMP_BUNDLE = ROOT / "artifacts" / "risk-loop" / "resplit-1117" / "argus_v_emp"
# measured on 2026-11-19 without the sealed sets: the P3/P5 outputs of 1,765 calls under both versions, written down
# with the versions and pickle hashes it holds for (reports/live-agent/scorer-equivalence.json)
SCORER_RECORD = AM.SCORER_RECORD
SCORER_PROBE = r"""
import hashlib, json, re, sys, warnings
from pathlib import Path
bundle = Path(sys.argv[1])
manifest = json.loads((bundle / "manifest.json").read_text())
expected = {name: info.get("sha256") if isinstance(info, dict) else info for name, info in (manifest.get("files") or {}).items()}
seen, bad, pickles = set(), [], {}
import joblib, numpy, sklearn
for path in sorted(bundle.glob("P*.pkl")):
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    pickles[path.name] = digest
    if expected.get(path.name) != digest:  # changed, or not one of the bundle's own files: not loaded
        bad.append(path.name)
        continue
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        joblib.load(path)
    seen |= {m.group(1) for w in caught for m in [re.search(r"from version ([\w.]+) when using version", str(w.message))] if m}
print(json.dumps({"sklearn": sklearn.__version__, "numpy": numpy.__version__, "joblib": joblib.__version__,
                  "pickled": sorted(seen) or [sklearn.__version__], "pickles": pickles, "bad_hash": bad}))
"""


def scorer_versions() -> dict:
    """The scikit-learn (and numpy, joblib) this server's python loads the Argus-V-emp models with, the version that
    pickled them, and whether they give the checked scores (agent_memory.scorer_equivalence: the same version, or the
    recorded measurement matching exactly). Read once, in a child process, after the pickles are checked against the
    bundle's own hashes (a pickle not in its manifest is not loaded)."""
    with _SCORER_LOCK:
        if not _SCORER:
            try:
                done = subprocess.run([sys.executable, "-I", "-c", SCORER_PROBE, str(EMP_BUNDLE)], capture_output=True,
                                      text=True, timeout=120, check=True, env=child_env())
                found = json.loads(done.stdout.strip().splitlines()[-1])
            except Exception as error:
                return {"error": f"{type(error).__name__}: {str(error)[-200:]}", "equivalent": False}
            verdict = AM.scorer_equivalence(found, SCORER_RECORD)
            _SCORER.update(sklearn=found["sklearn"], numpy=found.get("numpy"), joblib=found.get("joblib"),
                           pickled=found["pickled"], bad_hash=found.get("bad_hash") or [], how=verdict["how"],
                           measured=verdict["measured"] if verdict["equivalent"] else None,
                           equivalent=not found.get("bad_hash") and verdict["equivalent"])
        return dict(_SCORER)


def archive_limit() -> int:
    """sandbox.py's snapshot limit (settings.json): past it every run, and so every command, fails."""
    try:
        return int(read_json(SANDBOX_SCRIPT.parent / "settings.json")["archive_limit_bytes"])
    except (OSError, ValueError, KeyError, TypeError):
        return 512 * 2**20


SNAPSHOTS = SANDBOX_SCRIPT.parent / "snapshots"


def restore_point() -> dict | None:
    """The newest snapshot of /workspace (sandbox.py takes one before every run and keeps only those within its
    limits): what '마지막 정상 상태로' goes back to, with its biggest top-level entries."""
    import tarfile

    kept = STORE.sandbox_state().get("restore_point")
    newest = SNAPSHOTS / kept if kept and "/" not in kept and (SNAPSHOTS / kept).is_file() else None
    ledger = newest is not None  # a local turn's own state (the ledger's point), not just the newest snapshot
    if newest is None:
        skip = ("before-restore", "before-stop", "before-up", "before-reset", "before-import")
        try:
            newest = max((path for path in SNAPSHOTS.glob("*.tar") if not path.name.startswith(skip)),
                         key=lambda path: path.stat().st_mtime)
        except (ValueError, OSError):
            return None
    sizes: dict[str, int] = {}
    try:
        with tarfile.open(newest, "r:") as archive:
            for member in archive:
                parts = Path(member.name).parts
                top = parts[1] if parts and parts[0] == "." and len(parts) > 1 else (parts[0] if parts else "")
                if top and top != ".agent":
                    sizes[top] = sizes.get(top, 0) + max(0, member.size)
    except (OSError, tarfile.TarError):
        pass
    largest = sorted(sizes.items(), key=lambda item: -item[1])[:5]
    owner = STORE.sandbox_state().get("restore_turn") if ledger else None
    undoes = None
    if isinstance(owner, dict) and AM.valid_conversation_id(owner.get("conversation")):
        data = STORE.conversation(owner["conversation"]) or {}
        turn = next((item for item in data.get("turns") or [] if item.get("turn") == owner.get("turn")), {})
        step = next((item for item in turn.get("steps") or [] if item.get("step") == owner.get("step")), {})
        undoes = {"conversation": owner["conversation"], "title": AM.strip_hidden(str(data.get("title") or ""))[:60],
                  "turn": owner.get("turn"), "command": AM.shown_command(step.get("command"), 80)}
    return {"name": newest.name, "time": newest.stat().st_mtime, "mtime": newest.stat().st_mtime,
            "bytes": newest.stat().st_size, "ledger": ledger, "undoes": undoes,
            "largest": [{"name": AM.strip_hidden(name)[:60], "bytes": size} for name, size in largest]}


TURN_FILE_VIEW = 256 * 1024     # bytes of a changed file the page shows
TURN_FILE_DOWNLOAD = 8 * 2**20  # bytes a page may download


def turn_files(cid: str | None, turn_number) -> tuple[dict, dict]:
    """A turn and its files_changed (local turns only), or ApiRefusal."""
    if not AM.valid_conversation_id(cid) or not isinstance(turn_number, int) or isinstance(turn_number, bool):
        raise ApiRefusal("대화와 턴을 골라 주세요.", "bad_turn", 400)
    data = STORE.conversation(cid) or {}
    turn = next((item for item in data.get("turns") or [] if item.get("turn") == turn_number), None)
    if turn is None:
        raise ApiRefusal("그 턴을 찾을 수 없습니다.", "no_turn", 404)
    files = turn.get("files_changed") if isinstance(turn.get("files_changed"), dict) else None
    if not files or not files.get("start"):
        raise ApiRefusal("이 턴에는 바뀐 파일 기록이 없습니다.", "no_files", 404)
    return turn, files


def snapshot_path(name) -> Path | None:
    """One of sandbox.py's snapshots by its name (never a path), if it is still there."""
    if not isinstance(name, str) or "/" in name or "\\" in name or not name.endswith(".tar"):
        return None
    path = SNAPSHOTS / name
    return path if path.is_file() else None


def rewindable_turn(data: dict) -> int | None:
    """The turn of this conversation "이 턴 전으로" can take back: the one whose command was the last a local turn
    ran (the ledger's owner), local and not a fork's copy, with its start snapshot still there and nothing owed."""
    sandbox = STORE.sandbox_state()
    owner = sandbox.get("restore_turn") or {}
    if sandbox["debts"] or owner.get("conversation") != data.get("id"):
        return None
    turn = next((item for item in data.get("turns") or [] if item.get("turn") == owner.get("turn")), None)
    files = (turn or {}).get("files_changed") or {}
    counts = files.get("counts") or {}
    if (not turn or turn.get("origin") == "remote" or turn.get("copied_from") or turn.get("undone_after_answer")
            or not snapshot_path(files.get("start")) or not sum(int(counts.get(key) or 0) for key in ("added", "changed", "removed"))):
        return None
    return turn.get("turn")


def snapshots_usage() -> dict:
    """How many snapshots sandbox.py keeps and their size (it removes none)."""
    count = size = 0
    try:
        for path in SNAPSHOTS.glob("*.tar"):
            count += 1
            size += path.stat().st_size
    except OSError:
        pass
    return {"snapshots": count, "snapshots_bytes": size, "snapshots_dir": str(SNAPSHOTS)}


ARCHIVE_MAGIC = (b"\x1f\x8b", b"PK\x03\x04", b"BZh", b"\xfd7zXZ\x00", b"7z\xbc\xaf\x27\x1c", b"\x28\xb5\x2f\xfd")


def turn_file(cid: str, turn_number: int, wanted: str, side: str, limit: int, kind: str | None = None,
              index: int | None = None) -> tuple[bytes, dict]:
    """A file a turn changed, as it was before the turn's first command (``side`` "before") or after its last
    ("after"), from those snapshots on the host (no sandbox run). Only paths the turn's list names; never .agent, a
    link, a special file or a file holding a scenario canary. -> (at most ``limit`` bytes, {"size", "truncated"})"""
    import tarfile

    turn, files = turn_files(cid, turn_number)
    raw = files.get("raw") if isinstance(files.get("raw"), dict) else None
    if kind in ("added", "changed", "removed") and isinstance(index, int) and raw is not None:
        names = raw.get(kind) or []
        if not 0 <= index < len(names):
            raise ApiRefusal("이 턴의 바뀐 파일 목록에 있는 파일만 열 수 있습니다.", "not_listed", 403)
        wanted = str(names[index])  # the member's own name: a cleaned look-alike cannot stand for it
    elif raw is not None or not isinstance(wanted, str) \
            or wanted not in {str(path) for key in ("added", "changed", "removed") for path in files.get(key) or []}:
        raise ApiRefusal("이 턴의 바뀐 파일 목록에 있는 파일만 열 수 있습니다.", "not_listed", 403)
    if wanted.startswith(".agent") or ".." in wanted.split("/"):
        raise ApiRefusal("이 턴의 바뀐 파일 목록에 있는 파일만 열 수 있습니다.", "not_listed", 403)
    if side not in ("before", "after"):
        raise ApiRefusal("side는 before 또는 after입니다.", "bad_side", 400)
    tar = snapshot_path(files.get("start" if side == "before" else "end"))
    if tar is None:
        raise ApiRefusal("그 스냅숏이 더 이상 없어 열 수 없습니다.", "snapshot_gone", 410)
    try:
        with tarfile.open(tar, "r:") as archive:
            member = next((item for item in archive if AM.tar_name(item.name) == wanted), None)
            if member is None:
                raise ApiRefusal("이 쪽 스냅숏에는 그 파일이 없습니다(새로 만들었거나 지운 파일).", "absent", 404)
            if not member.isfile():
                raise ApiRefusal("링크나 특수 파일은 열지 않습니다.", "not_a_file", 422)
            handle = archive.extractfile(member)
            data = handle.read(min(member.size, max(limit, 65536))) if handle else b""
    except (OSError, tarfile.TarError) as error:
        raise ApiRefusal(f"스냅숏을 읽지 못했습니다: {type(error).__name__}", "unreadable", 500)
    if b"ARGUS-CANARY-" in data:  # a scenario's file: never shown or handed out
        raise ApiRefusal("시나리오가 남긴 파일(canary)이라 열지 않습니다.", "canary", 403)
    residue = bool(((turn.get("context") or {}).get("workspace") or {}).get("canary")) or turn.get("residue_inherited")
    if data.startswith(ARCHIVE_MAGIC) and (turn.get("sealed") or residue):
        # an archive hides what the canary check reads: not from a turn that saw sealed pages or scenario files
        raise ApiRefusal("시나리오 파일이나 봉인 페이지를 본 턴의 압축 파일은 열지 않습니다.", "archive", 403)
    return data[:limit], {"size": member.size, "truncated": member.size > limit}


def run_sandbox_cli(args: list[str], timeout: int = 300) -> dict:
    """One sandbox.py command without a model (its JSON report, or an ERROR)."""
    try:
        done = subprocess.run(["python3.11", str(SANDBOX_SCRIPT), *args], capture_output=True, text=True,
                              encoding="utf-8", errors="replace", timeout=timeout, env=live_env())
        return json.loads(done.stdout or done.stderr or "{}")
    except (subprocess.TimeoutExpired, json.JSONDecodeError, OSError) as error:
        return {"status": "ERROR", "reason": f"{type(error).__name__}"}


def plan_sandbox_check() -> None:
    """A plan turn without memory runs strict (refused on left-over processes or hooks): checked here without a
    model, so the run stops before the model loads, not 1-2 minutes later."""
    try:
        workspace = sandbox_files().workspace()
    except Exception as error:
        raise ApiRefusal(f"샌드박스를 확인하지 못해 계획 턴을 실행하지 않습니다: {type(error).__name__}", "sandbox_unchecked", 409)
    if workspace.get("strays") or workspace.get("hooks"):
        raise ApiRefusal(AM.leftover_text(workspace) + " · 계획 턴을 실행하지 않습니다.", "sandbox_not_clean", 409)


def owed_sweep(memory: bool, remote: bool) -> None:
    """Page elsewhere's turns that were not cleaned up after (the worker stopped first, or its clean-up failed or left
    something): each is swept in its own window, from when it was sent to when the next turn was (everything since, if
    none was). Until that is clean, no memory turn runs, nor any turn of a page elsewhere."""
    debts = STORE.sandbox_state()["debts"]
    if not debts:
        return
    files = sandbox_files()
    if remote:
        files.restart = None  # a page elsewhere never starts a stopped sandbox
    problem = None
    for debt in debts:
        try:
            state = files.sweep("all", "all", agent=True, since=debt.get("since"), until=debt.get("until"),
                                scratch=True, everything=not debt.get("until"),
                                home=debt.get("home") if isinstance(debt.get("home"), (dict, str)) else "window")
        except Exception as error:
            STORE.audit("sweep", "remote" if remote else "local", failed=True)
            problem = f"{type(error).__name__}: {str(error)[-160:]}"
            continue
        STORE.audit("sweep", "remote" if remote else "local", killed=len(state.get("killed") or []),
                    disabled=len(state.get("disabled") or []), left=state.get("left"), hooks_left=state.get("hooks_left"))
        STORE.mark_sandbox(cleared=True, changed={**(state.get("changed") or {}),
                                                  **({"moved": state["moved"], "quarantine": state.get("quarantine")}
                                                     if state.get("moved") else {})})
        if state.get("cleared") and not state.get("left") and not state.get("hooks_left") and not state.get("home_left"):
            STORE.settle_debt(debt.get("session"), clean=True) if debt.get("session") else STORE.settle_debt(None, clean=True)
        else:
            problem = (f"아직 남은 프로세스 {state.get('left') or 0}개·훅 {(state.get('hooks_left') or 0) + (state.get('home_left') or 0)}개"
                       + ("" if state.get("cleared") else "·기억 폴더"))
    if problem:  # every turn waits: while a debt is open nothing else runs, so its sweep can take everything
        raise ApiRefusal(f"다른 페이지의 턴이 남긴 것을 샌드박스에서 다 정리하지 못해 이 턴을 실행하지 않습니다"
                         + ("" if remote else f"({problem}). 기억 카드의 '샌드박스 점검'에서 정리하거나 '마지막 정상 상태로' 되돌려 주세요."),
                         "sandbox_unswept", 409)


_START_LOCK = threading.Lock()
DISK_LOW = 10 * 2**30  # bytes free under the snapshots below which no turn starts


def still_sealed() -> bool:
    """Whether a file a sealed turn made or changed is still in the workspace as it left it (the newest snapshot);
    once none is, the mark goes."""
    kept = STORE.sandbox_state().get("sealed_files") or {}
    skip = ("before-restore", "before-stop", "before-up", "before-reset", "before-import")
    try:
        newest = max((path for path in SNAPSHOTS.glob("*.tar") if not path.name.startswith(skip)),
                     key=lambda path: path.stat().st_mtime)
    except (ValueError, OSError):
        return bool(kept)  # nothing to look at: kept (fail closed)
    members = AM.snapshot_members(newest, skip=AM.REMOTE_DIFF_SKIP)
    if members is None:
        return bool(kept)
    still = {path: digest for path, digest in kept.items() if members.get(path) == digest}
    if not still:
        STORE.mark_sandbox(sealed_files=None)
    return bool(still)


def disk_free() -> int | None:
    """Bytes free where sandbox.py keeps its snapshots (None if it cannot be told)."""
    try:
        return shutil.disk_usage(SNAPSHOTS if SNAPSHOTS.exists() else ROOT).free
    except OSError:
        return None


def start_live(*args, **kwargs) -> dict:
    """One start at a time: the checks (busy, debts, the sandbox) and the submit happen together."""
    with _START_LOCK:
        return _start_live(*args, **kwargs)


def _start_live(task: str, max_steps: int = 5, conversation: str | None = None, memory: bool = True,
                last_turn: str | None = None, remote: bool = False, battery: dict | None = None) -> dict:
    """Run ``task`` on a new live worker unless another job holds the GPU (it is unloaded when the task ends).

    ``conversation`` continues that conversation (None starts a new one); ``memory`` lets the agent read and update
    its sandbox memory. ``last_turn``: "retry" or "edit" runs the last turn again (the old attempt is kept as
    superseded, and the memory it wrote is reverted first); "resume" continues the last turn when it ended without
    an answer. The turn is stored by a recorder thread once the task has ended."""
    global _RECORDING
    with JOBS_LOCK:
        if any(job["process"].poll() is None and uses_gpu(job) for job in JOBS.values()):
            raise ValueError("다른 GPU 작업(토큰 재계산 또는 기존 에이전트 실행)이 끝난 뒤 다시 시도해 주세요.")
    missing = live_missing(runtime_status())
    if missing:
        raise ValueError("실시간 에이전트를 실행할 수 없습니다. 준비되지 않은 항목: " + ", ".join(missing))
    if LIVE.status()["busy"]:
        raise ValueError("이미 실행 중인 작업이 있습니다. 끝나거나 중지한 뒤 다시 보내 주세요.")
    with _RECORDING_LOCK:
        previous = _RECORDING
    if previous is not None:
        previous.join(timeout=15)  # the previous turn is stored before this task reads the conversation
    if last_turn not in (None, "retry", "edit", "resume"):
        raise ValueError("last_turn은 retry, edit, resume 중 하나여야 합니다.")
    # A page elsewhere that may not see the memory may not have the agent read it either: its turn runs without
    # memory, and the sandbox's memory folder is cleared first (the next memory turn writes it back).
    memory_blocked = bool(remote and memory and not STORE.settings()["remote_view"])
    if memory_blocked:
        memory = False
    if battery and Path(STORE.root).resolve() == DEFAULT_MEMORY_ROOT.resolve():
        # a plan run never writes its fictional user into the user's own memory
        raise ApiRefusal("계획 실행은 사용자 기억과 따로 해야 합니다. ARGUS_LIVE_MEMORY_DIR로 다른 기억 폴더를 지정해 서버를 켜 주세요.",
                         "battery_needs_own_memory")
    unknown = [arm for arm in (battery or {}).get("arms") or [] if arm not in AM.ARMS]
    if unknown:  # checked before anything is created or reverted
        raise ApiRefusal(f"모르는 비교군입니다: {', '.join(map(str, unknown))}", "unknown_arm")
    if remote and _REMOTE_REFUSAL and time.monotonic() - _REMOTE_REFUSAL["at"] < 60:
        STORE.audit("start", "remote", refused=True, reason=_REMOTE_REFUSAL["code"])
        raise ApiRefusal(_REMOTE_REFUSAL["message"], _REMOTE_REFUSAL["code"], 409)
    free = disk_free()
    if free is not None and free < DISK_LOW:
        usage = snapshots_usage()
        raise ApiRefusal(f"디스크 여유가 {free / 2**30:.1f} GB라 턴을 시작하지 않습니다. 명령마다 샌드박스 스냅숏을 남깁니다"
                         f"({usage['snapshots']}개 · {usage['snapshots_bytes'] / 2**30:.1f} GB, {usage['snapshots_dir']}). "
                         f"{(DISK_LOW - free) / 2**30:.1f} GB 이상 더 비워 주세요. 오래된 스냅숏을 지우면 그 턴의 바뀐 파일 보기와 "
                         "'이 턴 전으로'는 쓸 수 없게 됩니다.", "disk_low", 409)
    blocked = STORE.sandbox_state()["blocked"]
    if blocked:  # sandbox.py would refuse every command (its snapshot fails): no model is loaded for nothing
        raise ApiRefusal(AM.BLOCKED_TEXT.get(blocked, blocked) + (" · 로컬 페이지에서 확인해 주세요." if remote else
                         " · 기억 카드의 '샌드박스 점검'에서 '마지막 정상 상태로'로 되돌릴 수 있습니다."), "sandbox_blocked", 409)
    try:
        owed_sweep(memory, remote)
    except ApiRefusal as refusal:
        if remote:  # a page elsewhere's retries cost no sandbox run for a minute
            _REMOTE_REFUSAL.update(at=time.monotonic(), message=refusal.args[0], code=refusal.code)
        raise
    if conversation:
        data = STORE.conversation(conversation) if AM.valid_conversation_id(conversation) else None
        if data is None:
            raise ValueError("이어갈 대화를 찾을 수 없습니다. 새 대화로 다시 보내 주세요.")
        if remote and not STORE.settings()["remote_view"] and AM.started_from(data) != "remote":
            STORE.audit("start", "remote", refused=True, conversation=data["id"])
            raise ApiRefusal("이 대화는 로컬 페이지에서 시작한 대화라 여기서 이어 갈 수 없습니다. 로컬 페이지에서 이어 가거나, 새 대화로 보내 주세요.",
                             "local_only", 403)
        created = False
    elif last_turn:
        raise ValueError("다시 하거나 이어 갈 대화를 골라 주세요.")
    if remote and not memory:
        remote_sandbox_check()  # before anything is created: a refusal leaves no conversation behind
    elif battery and not memory:
        plan_sandbox_check()  # a plan turn without memory is strict too: stopped here, not after the model loaded
    if not conversation:
        data, created = STORE.create(task, "remote" if remote else "local"), True
    turns, extra, reverted = list(data["turns"]), {}, []
    if last_turn:
        if not turns:
            raise ValueError("이 대화에는 아직 턴이 없습니다.")
        target = turns[-1]
        if remote and target.get("origin") != "remote":
            # A page elsewhere may redo or continue only turns it started: replacing a local turn would replace the
            # user's words and revert what that turn wrote into the memory.
            STORE.audit(last_turn, "remote", refused=True, conversation=data["id"], turn=target.get("turn"))
            raise ApiRefusal("다른 페이지에서는 그 페이지에서 시작한 턴만 다시 하거나 이어 갈 수 있습니다. 로컬 페이지에서 해 주세요.",
                             "local_only", 403)
        turns = turns[:-1]  # the last turn is replayed (resume) or replaced (retry/edit), not shown as history
        if last_turn == "resume":
            if not resumable(target):
                raise ApiRefusal("이 턴은 이어서 진행할 수 없습니다(답을 냈거나 실행한 명령이 없습니다). 새로 질문해 주세요.",
                                 "not_resumable")
            if len(resume_chain(data["turns"], target)) >= RESUME_CHAIN_MAX:
                raise ApiRefusal(f"한 요청은 {RESUME_CHAIN_MAX}번까지 이어서 진행할 수 있습니다. 새로 질문해 주세요.",
                                 "resume_limit")
            extra["resume"] = resume_material(target, data["turns"])
            chain = {t.get("turn") for t in resume_chain(data["turns"], target)}
            turns = [t for t in turns if t.get("turn") not in chain]  # the replay carries the request instead
            turn = len(data["turns"]) + 1
        else:
            if last_turn == "retry" and target.get("resume_of"):
                # Retrying a continuation continues the same request again (not "이어서 진행해 줘" as a question).
                origin = next((t for t in turns if t.get("turn") == target["resume_of"]), None)
                if origin is not None:
                    extra["resume"] = resume_material(origin, data["turns"][:-1])
                    chain = {t.get("turn") for t in resume_chain(data["turns"][:-1], origin)}
                    turns = [t for t in turns if t.get("turn") not in chain]
            turn = target.get("turn") or len(data["turns"])
            if target.get("run_id") and not remote:  # also with memory off: the replaced attempt's memory must go
                reverted = STORE.revert_run(target["run_id"], {"conversation": data["id"], "turn": turn})
                STORE.audit("revert", "local", conversation=data["id"], turn=turn, files=len(reverted or []))
            # (a page elsewhere never takes lines out of the memory: its retry keeps what the old attempt wrote)
            if last_turn == "edit" and turn == 1 and data["title"] == AM.title_for(target.get("task") or ""):
                # the title came from the request now replaced
                data = STORE.rename(data["id"], AM.title_for(task), "remote" if remote else "local")
    else:
        turn = len(turns) + 1
    # The sandbox record: a replaced turn leaves it; a resumed turn stays (only the context replays it instead).
    view = data if last_turn == "resume" else {**data, "turns": turns}
    # Scenario files seen in this conversation's recent turns count for this one too (a rollout may have wiped them).
    residue = any(((t.get("context") or {}).get("workspace") or {}).get("canary") or t.get("residue_inherited")
                  for t in data["turns"][-5:])
    # A page that may not see the memory gets a context without the local page's turns (their requests and answers
    # can carry what the memory holds); the agent is told they were left out.
    shown_turns = turns if not remote or STORE.settings()["remote_view"] else [
        turn if turn.get("origin") == "remote" else {"turn": turn.get("turn"), "task": "(a turn from the user's local page, left out here)",
                                                     "answer": "(left out)", "steps": []}
        for turn in turns]
    payload = {"conversation": {"id": data["id"], "title": data["title"], "turn": turn,
                                "history": AM.compact_turns(shown_turns, quote_remote=not remote), "residue": residue,
                                "recent": recent_conversations(data["id"]) if memory else []}, **extra}
    if memory:
        cleared = STORE.sandbox_state()["cleared"]  # after a clear every known record goes back, not the latest 20
        payload["memory"] = {**STORE.mirror_state(), "transcript": AM.transcript_for(view),
                             **STORE.sandbox_records(data["id"], everything=cleared), "all_records": cleared}
        payload["memory"]["records"][data["id"]] = AM.transcript_for(view)
        payload["memory"]["expected"][data["id"]] = AM.sha(AM.transcript_for(view))[:16]
    if not memory:
        # "Memory off" means the agent cannot read the memory folder either: it is cleared first (the next memory turn
        # writes it back). A page elsewhere (or a plan run) is refused on left-over processes or hooks; the local
        # page is warned.
        strict = bool(remote or battery)
        payload["clear_memory"] = "strict" if strict else "warn"
    if remote and not memory:
        payload["sweep_after"] = True  # what it starts or writes does not outlive the turn
    if any(turn.get("sealed") for turn in shown_turns[-AM.HISTORY_TURNS:]) or (last_turn == "resume" and target.get("sealed")):
        payload["sealed"] = True  # what the sealed pages said is in its context: sealed from its first event
    if STORE.sandbox_state().get("sealed_files") and still_sealed():
        payload["sealed"] = True  # a file a sealed turn left is still there: whoever reads it reads the sealed page
    if STORE.sandbox_state().get("fakenet_until"):  # the gateway's log since the last turn's reading counts for this one
        payload["fakenet_since"] = STORE.sandbox_state()["fakenet_until"]
    if battery:  # a case of the GPU plan (local page only): its arms and tags
        payload["arms"] = list(battery.get("arms") or [])
        payload["stop_on_residue"] = True  # a plan turn with scenario files in the workspace ends before step 1
        if battery.get("clear_memory") is True and not memory:  # the plan's memory-off arms (strict, as above)
            payload["clear_memory"] = "strict"
    meta = {"conversation": data["id"], "title": data["title"], "turn": turn, "memory": bool(memory),
            "last_turn": last_turn, "origin": "remote" if remote else "local"}
    memory_versions = {name: info.get("version", 0) for name, info in STORE.memory()["files"].items()} if memory else None
    sent = time.time()
    # what pages elsewhere changed in /workspace since the last local turn: this turn's card says so
    remote_changes = STORE.take_remote_changes() if not remote else None
    if remote_changes:
        payload["workspace_changed"] = remote_changes
    try:
        seed = int(battery["seed"]) if battery and battery.get("seed") is not None else None
        started = LIVE.submit(task, max_steps, seed=seed, payload=payload, meta=meta)
        if payload.get("sweep_after"):
            # before the model loads (seconds): if the worker stops before its clean-up, the next start sweeps this window
            STORE.add_debt(started["session"], sent)
        STORE.mark_start()
        if payload.get("clear_memory"):
            STORE.mark_sandbox(cleared=True)
        if not remote:
            _REMOTE_REFUSAL.clear()  # a local turn may change what is left in the sandbox
        remember_session(started["session"], "remote" if remote else "local")
        STORE.audit("start", "remote" if remote else "local", conversation=data["id"], turn=turn,
                    last_turn=last_turn, memory=bool(memory), battery=(battery or {}).get("case"))
    except Exception:
        if created:
            STORE.delete(data["id"], forget_record=False)
        if reverted:
            STORE.unrevert(target["run_id"])  # the retry never started: the turn's memory comes back
        if remote_changes:
            STORE.mark_sandbox(changed=remote_changes)  # shown with the next turn instead
        raise
    resume_payload = extra.get("resume") or {}
    # A turn a page elsewhere started, continued or redone here: its request is not the user's words (it is a
    # possible source instead), and lines with action targets from this turn wait for review.
    remote_request = bool(last_turn and target.get("origin") == "remote") or any(
        t.get("origin") == "remote" for t in (resume_chain(data["turns"], target) if last_turn == "resume" else []))
    extras = {"last_turn": last_turn, "memory_reverted": reverted or None, "resume_of": resume_payload.get("turn"),
              "origin": "remote" if remote else "local", "memory_versions": memory_versions,
              "remote_request": remote_request or None,
              "memory_blocked": "remote" if memory_blocked else None,
              "battery": {**{key: battery.get(key) for key in ("plan", "case", "arm", "seed") if battery.get(key) is not None},
                          "arms": payload.get("arms") or []} if battery else None,
              "residue_inherited": residue or None,
              "workspace_changed": remote_changes or None,
              "replaces_run": target.get("run_id") if last_turn in ("retry", "edit") else None,
              # where a USER.md line may have come from besides this turn's own output
              "replayed_outputs": [m.get("content") or "" for m in resume_payload.get("messages") or []
                                   if m.get("role") == "user"] + [s.get("observation") or "" for s in
                                                                  resume_payload.get("steps") or []],
              "tainted": [t.get("answer") or t.get("report") or "" for t in turns
                          if any(s.get("kind") == "bash" for s in t.get("steps") or [])]
                         + [t.get("task") or "" for t in turns if (t.get("context") or {}).get("memory") == "off"
                            or t.get("origin") == "remote"]
                         + ([resume_payload.get("task") or target.get("task") or ""] if remote_request else [])}
    user_words = [t.get("task") or "" for t in turns
                  if (t.get("context") or {}).get("memory") != "off" and t.get("origin") != "remote"]
    thread = threading.Thread(target=record_turn, args=(data["id"], started["session"], started["after"], task, turn,
                                                        user_words, extras),
                              name="live-turn-recorder", daemon=True)
    with _RECORDING_LOCK:
        _RECORDING = thread
    thread.start()
    return {**started, "conversation": {"id": data["id"], "title": data["title"], "turn": turn},
            "last_turn": last_turn, "memory_reverted": reverted, "memory_versions": memory_versions,
            "memory_blocked": "remote" if memory_blocked else None, "workspace_changed": remote_changes or None}


def recent_conversations(current: str, limit: int = 5) -> list[dict]:
    """Other recent conversations for the agent's saved memory: id, date, title (the user's words). One that began
    with memory off is left out."""
    out = []
    for row in STORE.conversations():
        if row["id"] == current or not row.get("turns"):
            continue
        data = STORE.conversation(row["id"]) or {}
        first = (data.get("turns") or [{}])[0]
        if (first.get("context") or {}).get("memory") == "off" or AM.remote_title(data):
            continue  # begun with memory off, or titled by a page elsewhere (not the user's words on this machine)
        out.append({"id": row["id"], "title": row.get("title") or "",
                    "date": datetime.fromtimestamp(row.get("updated") or 0).strftime("%Y-%m-%d")})
        if len(out) >= limit:
            break
    return out


HIDDEN_TEXT = "(기억 내용 · 로컬 페이지에서 볼 수 있습니다)"


SESSION_ORIGIN: dict[str, str] = {}  # task session -> "local" / "remote" (which page started it)


def remember_session(session: str, origin: str) -> None:
    SESSION_ORIGIN[session] = origin
    while len(SESSION_ORIGIN) > 500:
        SESSION_ORIGIN.pop(next(iter(SESSION_ORIGIN)))


def remote_visible_event(event: dict) -> bool:
    """For a page that may not see the memory: the events of tasks it started (and the worker's own, which carry no
    session and no chat text). A local task's chat stays on the local page."""
    session = event.get("session")
    return not session or SESSION_ORIGIN.get(session) == "remote"


REMOTE_STATUS_KEYS = ("state", "worker_state", "message", "busy", "alive", "exit_code", "last_seq", "first_seq",
                      "load_estimate", "trimmed")


def remote_status(status: dict) -> dict:
    """The service status (as /api/live/status, the event stream, cancel and unload answer with it) for a page
    that may not see the memory: a task it started in full; otherwise only the fields that say what the worker is
    doing, never the request, the conversation or the session of a local task."""
    if status.get("session") and SESSION_ORIGIN.get(status["session"]) == "remote":
        return status
    info = status.get("info") or {}
    return {**{key: status[key] for key in REMOTE_STATUS_KEYS if key in status},
            "info": {key: info.get(key) for key in ("seconds", "network", "vram_gb", "cut_offs") if key in info},
            "task": None, "session": None, "meta": {}}


def remote_conversation(data: dict) -> dict:
    """A conversation a page elsewhere started, as that page gets it: the turns the local page added are hidden,
    and so are the local page's attempts kept under a remote turn (an edit that never ran, for one)."""
    def own(turn: dict) -> dict:
        if turn.get("origin") != "remote":
            return {"turn": turn.get("turn"), "hidden": "local", "origin": "local"}
        attempts = [old if old.get("origin") == "remote" else {"hidden": "local", "origin": "local"}
                    for old in turn.get("superseded") or []]
        return {**turn, "superseded": attempts} if attempts else turn
    return {**data, "turns": [own(turn) for turn in data.get("turns") or []]}


SEALED_HIDDEN = "(봉인된 시나리오 페이지 http://fakenet/argus/ 를 본 턴이라 로컬 페이지에서만 보입니다)"
SEALED_NUMBERS = ("seen_sha", "prompt_sha", "generated_sha", "output_chars", "agent_chars", "output_bytes",
                  "prompt_tokens", "generated_tokens")  # enough to confirm a guess of the text


def without_sealed_pages(conversation: dict) -> dict:
    """A conversation as a page elsewhere gets it: the output of commands that touched the sealed scenario pages
    fakenet serves under /argus/ stays on the local page."""
    def hide(step: dict) -> dict:
        return {**{key: value for key, value in step.items() if key not in SEALED_NUMBERS},
                **{key: SEALED_HIDDEN for key in ("command", "observation") if step.get(key)}}

    def strip(record: dict) -> dict:
        if record.get("sealed"):  # the whole turn from its first touch on: the answer and every command and output
            record = {**record, "steps": [hide(step) for step in record.get("steps") or []],
                      **{key: SEALED_HIDDEN for key in ("answer", "report") if record.get(key)}}
            # the lines it wrote, the files it touched, and the sizes and hashes of its context say too much as well
            if isinstance(record.get("memory_changes"), list):
                record["memory_changes"] = [{k: v for k, v in change.items() if k not in ("lines", "source")}
                                            for change in record["memory_changes"] if isinstance(change, dict)]
            if isinstance(record.get("files_changed"), dict):
                record["files_changed"] = {k: v for k, v in record["files_changed"].items()
                                           if k not in ("added", "changed", "removed", "raw", "digests")}
            if isinstance(record.get("context"), dict):
                record["context"] = {k: v for k, v in record["context"].items()
                                     if k not in ("system_chars", "request_chars", "history_chars", "context_sha", "blocks")}
            if isinstance(record.get("memory"), dict):  # the memory events it kept: counts, no lines or file texts
                record["memory"] = {action: ({k: v for k, v in info.items() if k not in ("changes", "files", "message")}
                                             if isinstance(info, dict) else info)
                                    for action, info in record["memory"].items()}
            if isinstance(record.get("memory_step"), dict):
                record["memory_step"] = hide(record["memory_step"])
            if record.get("memory_steps"):
                record["memory_steps"] = [hide(step) for step in record["memory_steps"] if isinstance(step, dict)]
        record = {**record, "steps": [{**step, "observation": SEALED_HIDDEN} if step.get("argus_page") and step.get("observation")
                                      else step for step in record.get("steps") or []]}
        if record.get("superseded"):
            record["superseded"] = [strip(old) for old in record["superseded"]]
        return record
    return {**conversation, "turns": [strip(turn) for turn in conversation.get("turns") or []]}


def public_event(event: dict, view: bool = True, local: bool = True) -> dict:
    """An event as the browser gets it: memory events without the memory texts (line counts instead). The page
    never needs the texts, and any allowed page can read the event stream. For a page that may not see the memory
    (``view`` False), the memory step's texts and those of main-step commands on the memory files are hidden too."""
    if (event.get("sealed") or (event.get("type") == "observation" and event.get("argus_page"))) and not local:
        # a turn that touched the sealed pages: from then on its text (reasoning, commands, outputs, the answer) and
        # the hashes and sizes that could confirm a guess stay on the local page
        event = {**{key: value for key, value in event.items() if key not in SEALED_NUMBERS},
                 **{key: SEALED_HIDDEN for key in ("text", "command", "reply", "answer")
                    if isinstance(event.get(key), str) and event.get(key)}}
        if event.get("type") == "delta":
            event["replace"] = True
    if event.get("type") == "files_changed" and not view:  # how many, not which (the local page's file names)
        return {key: value for key, value in event.items() if key not in ("added", "changed", "removed", "raw", "digests")}
    if event.get("type") != "memory":
        if view or not (event.get("phase") == "memory" or event.get("memory_touch")):
            return event
        out = {key: HIDDEN_TEXT if key in ("command", "text", "reply") and isinstance(value, str) and value else value
               for key, value in event.items()}
        if event.get("type") == "delta":
            out["replace"] = True  # one placeholder, not one per streamed piece
        return out
    out = dict(event)
    if out.get("home") is not None:  # HOME's list stays with the debt on the host
        out["home"] = True
    if isinstance(out.get("moved"), list) and not local:  # names of HOME entries: the local page's
        out["moved"] = len(out["moved"])
    if isinstance(out.get("changed"), dict) and not view:  # how many files a turn changed, not which
        out["changed"] = {key: value for key, value in out["changed"].items() if key not in ("paths", "moved")}
    if out.get("action") == "saved" and isinstance(out.get("files"), dict):
        out["files"] = AM.file_summary({name: text if isinstance(text, str) else "" for name, text in out["files"].items()})
    if isinstance(out.get("outside"), dict):
        out["outside"] = AM.file_summary({name: text if isinstance(text, str) else "" for name, text in out["outside"].items()})
    if isinstance(out.get("changes"), dict):  # counts and reasons stay; the changed lines do not
        out["changes"] = {name: {key: value for key, value in change.items() if key != "lines"}
                          for name, change in out["changes"].items() if isinstance(change, dict)}
    if isinstance(out.get("unknown_removed"), list):  # names and sizes; their first lines stay on the host
        out["unknown_removed"] = [{key: value for key, value in item.items() if key != "head"}
                                  for item in out["unknown_removed"] if isinstance(item, dict)]
    return out


def sealed_memory(memory: dict) -> dict:
    """The memory as a page elsewhere with the memory view gets it: a held line from a turn that read the sealed
    pages is not shown (its reason and counts are)."""
    review = [{**item, "old": [SEALED_HIDDEN] if item.get("old") else [], "new": [SEALED_HIDDEN] if item.get("new") else [],
               "source": None} if "sealed_pages" in (item.get("reasons") or []) else item
              for item in memory.get("review") or []]
    return {**memory, "review": review}


def memory_counts(memory: dict) -> dict:
    """The memory as a page from elsewhere may see it: line counts and states, no texts or held lines."""
    files = {name: {**{key: value for key, value in info.items() if key != "text"}, "text": "", "hidden": True}
             for name, info in memory.get("files", {}).items()}
    review = [{key: item.get(key) for key in ("id", "file", "origin", "reasons", "time", "turn")} for item in memory.get("review", [])]
    return {**memory, "files": files, "review": review, "hidden": True}


def hide_step(step: dict) -> dict:
    return {**step, **{key: HIDDEN_TEXT for key in ("command", "observation") if step.get(key)}}


def without_memory_lines(conversation: dict) -> dict:
    """A conversation as a page that may not see the memory gets it: the chat itself stays; the memory lines its
    turns changed, the memory step's commands and output and main-step commands on the memory files do not."""
    def no_lines(changes):
        return {name: {k: v for k, v in change.items() if k != "lines"} for name, change in changes.items()
                if isinstance(change, dict)} if isinstance(changes, dict) else changes

    def strip(record: dict) -> dict:
        record = dict(record)
        for key in ("memory_changes", "memory_outside"):
            if isinstance(record.get(key), list):
                record[key] = [{k: v for k, v in change.items() if k != "lines"} for change in record[key]]
        if isinstance(record.get("memory"), dict):
            record["memory"] = {action: {**{k: v for k, v in info.items() if k != "unknown_removed"},
                                         **({"changes": no_lines(info["changes"])} if "changes" in info else {})}
                                if isinstance(info, dict) else info
                                for action, info in record["memory"].items()}
        record.pop("sandbox_notes", None)  # names of the local page's files and processes
        if isinstance(record.get("files_changed"), dict):  # how many files a turn changed, not which
            record["files_changed"] = {key: value for key, value in record["files_changed"].items()
                                       if key not in ("added", "changed", "removed", "raw", "digests")}
        record["steps"] = [hide_step(step) if step.get("kind") == "bash" and AM.touches_memory(step.get("command"))
                           else step for step in record.get("steps") or []]
        if record.get("memory_steps"):
            record["memory_steps"] = [hide_step(step) for step in record["memory_steps"] if isinstance(step, dict)]
        if isinstance(record.get("memory_step"), dict):
            record["memory_step"] = hide_step(record["memory_step"])
        if record.get("superseded"):
            record["superseded"] = [strip(old) for old in record["superseded"]]
        return record
    return {**conversation, "turns": [strip(turn) for turn in conversation.get("turns") or []], "hidden": True}


def export_verdicts(fmt: str, cid: str) -> tuple[bytes, str]:
    """Verdict rows (numbers and short enums only) of one conversation or all of them, as CSV or JSON lines. The
    JSON lines start with a manifest that says how to read them."""
    ids = [row["id"] for row in STORE.conversations()] if cid == "all" else [cid]
    rows = []
    for one in ids:
        data = STORE.conversation(one)
        if data:
            rows += AM.verdict_rows(data)
    if fmt == "jsonl":
        cuts = sorted({row["cut_5"] for row in rows if row.get("cut_5") is not None})
        manifest = {"manifest": {"columns": list(AM.VERDICT_COLUMNS), "rows": len(rows),
                                 "cut_5": cuts[0] if len(cuts) == 1 else cuts, "chat_wide": list(AM.CHAT_WIDE),
                                 "note": "cut_5 is the 95th percentile of validation normal steps from scenario runs: "
                                         "their prompt has none of the chat additions, no memory and no earlier turns. "
                                         "differs_by lists how a row's context differs from them. Chat rows have the "
                                         "chat-wide items (chat_prompt; monitor_notice unless a plan arm drops it; "
                                         "budget for main steps), so reference_like=true rows are the closest to that "
                                         "condition, not the same. A main step also differs by the hint it was given "
                                         "and the tail_note/repeat_note of steps before it; a memory step has its own "
                                         "context (memory_step). Plan runs carry plan/case/arm. "
                                         "Rows with residue=true saw scenario files. attempt>0 rows are superseded "
                                         "attempts. phase=memory rows are memory steps. Turns copied by a fork are "
                                         "counted in the conversation they came from.",
                                 "exported": datetime.now(timezone.utc).isoformat()}}
        lines = [json.dumps(manifest, ensure_ascii=False)] + [json.dumps(row, ensure_ascii=False) for row in rows]
        return ("\n".join(lines) + "\n").encode("utf-8"), "application/x-ndjson; charset=utf-8"
    import csv
    import io

    def cell(value):
        if isinstance(value, str) and value[:1] in ("=", "+", "-", "@", "\t", "\r"):
            return "'" + value  # a spreadsheet must not read a string as a formula
        return value
    out = io.StringIO()
    writer = csv.writer(out)
    writer.writerow(AM.VERDICT_COLUMNS)
    for row in rows:
        writer.writerow([cell(row[column]) for column in AM.VERDICT_COLUMNS])
    return out.getvalue().encode("utf-8-sig"), "text/csv; charset=utf-8"


def settle_recording(timeout: float = 3.0) -> None:
    """When no task runs, wait briefly for the last turn to be stored, so a page that asks right after the task
    ended sees it."""
    with _RECORDING_LOCK:
        thread = _RECORDING
    if thread is not None and thread.is_alive() and not LIVE.status()["busy"]:
        thread.join(timeout=timeout)


def record_turn(cid: str, session: str, after: int, task: str, turn: int, earlier: list[str] | None = None,
                extras: dict | None = None) -> None:
    """Follow one task's events; pass the memory the worker reports to the ledger (with what the sandbox printed
    this turn, so a USER.md line copied from a page waits for review) and, when the task has ended, keep the turn
    in the conversation (a retried or edited turn replaces the last one, which is kept as superseded)."""
    recorder = AM.TurnRecorder(task, turn=turn)
    extras = {key: value for key, value in (extras or {}).items() if value is not None}
    asked = (extras or {}).get("tainted") or []
    user_texts = "\n".join([word for word in [task, *(earlier or [])] if not (extras or {}).get("remote_request")
                             or word not in asked])
    outputs: list[str] = list((extras or {}).get("replayed_outputs") or [])
    seq, ended, swept = after, False, False  # swept: the turn reported its clean-up
    try:
        while not ended:
            data = LIVE.events_after(seq, wait=20)
            for event in data["events"]:
                seq = max(seq, event["seq"])
                if event.get("session") != session:
                    continue
                recorder.feed(event)
                provenance = {"conversation": cid, "turn": turn, "run_id": recorder.data.get("run_id")}
                if event.get("type") == "observation" and event.get("phase") != "memory":
                    outputs.append(event.get("text") or "")
                if event.get("type") == "memory" and event.get("action") == "loaded":
                    outside = event.get("outside") or {}
                    if outside:  # changed outside the memory step: review, never adopted silently
                        recorder.data["memory_outside"] = STORE.apply_change(
                            outside, {name: "outside" for name in outside}, None, provenance, in_sandbox=False)
                    STORE.mark_synced(event.get("synced"), event.get("deleted_done"),
                                      restored_all=bool(event.get("all_records")))
                    STORE.keep_removed(event.get("unknown_removed") or [], provenance)
                elif event.get("type") == "memory" and event.get("action") == "saved":
                    workspace = (recorder.data.get("context") or {}).get("workspace") or {}
                    recorder.data["memory_changes"] = STORE.apply_change(
                        event.get("files") or {}, event.get("origins"), event.get("base"), provenance,
                        sources={"outputs": "\n".join(outputs + list(extras.get("tainted") or [])), "user": user_texts,
                                 "rejected": STORE.rejected_keys(),
                                 "remote": extras.get("origin") == "remote" or bool(extras.get("remote_request")),
                                 "sealed": bool(recorder.data.get("sealed")),
                                 "unwritten": set(event.get("unwritten") or []),
                                 "user_lines": STORE.user_line_keys()},
                        residue=bool(workspace.get("canary")) or bool(extras.get("residue_inherited")))
                elif event.get("type") == "files_changed" and (event.get("sealed") or recorder.data.get("sealed")) \
                        and isinstance(event.get("digests"), dict) and event["digests"]:
                    kept = STORE.sandbox_state().get("sealed_files") or {}
                    STORE.mark_sandbox(sealed_files={**kept, **event["digests"]})
                elif event.get("type") == "fakenet" and isinstance(event.get("until"), (int, float)):
                    STORE.mark_sandbox(fakenet_until=event["until"])
                elif event.get("type") == "memory" and event.get("action") == "cleared" and isinstance(event.get("home"), (dict, str)):
                    STORE.debt_home(session, event["home"])  # what the user had in HOME: a later sweep keeps it
                elif event.get("type") == "memory" and event.get("blocked") and not event.get("recovered"):
                    STORE.mark_sandbox(blocked=event["blocked"])  # the next turn is refused before the model loads
                elif event.get("type") == "observation" and event.get("status") in ("FINISHED", "TIMEOUT"):
                    sandbox = STORE.sandbox_state()
                    if sandbox["blocked"]:
                        STORE.mark_sandbox(blocked=None)  # a command ran: sandbox.py could snapshot again
                    if event.get("snapshot") and extras.get("origin") != "remote" and event.get("phase") != "memory":
                        # the way back is a state a local turn worked in (never one a page elsewhere left)
                        STORE.mark_sandbox(restore_point=str(event["snapshot"]),
                                           restore_turn={"conversation": cid, "turn": turn, "step": event.get("step")})
                elif event.get("type") == "memory" and event.get("action") == "swept":
                    STORE.mark_sandbox(changed=event.get("changed"))
                    swept = True
                    clean = bool(event.get("skipped")) or (bool(event.get("cleared")) and not event.get("left")
                                                           and not event.get("hooks_left"))
                    if clean:
                        STORE.settle_debt(session, clean=True)  # this turn's debt only; otherwise it stays open
                elif event.get("type") == "memory" and event.get("action") == "error" and event.get("stage") == "sweep":
                    swept = True  # the debt stays open: the next start sweeps everything since it was sent
                elif event.get("type") == "task_end":
                    ended = True
                    break
            if not ended and not data["events"] and (not data["busy"] or data["session"] != session):
                break  # the task ended without a task_end this thread could see
    finally:
        record = {**recorder.record(), **extras}
        record["termination"] = record["termination"] or "unknown"
        replaced = extras.pop("replaces_run", None)
        for key in ("replaces_run", "replayed_outputs", "tainted"):
            record.pop(key, None)
        if extras.get("last_turn") in ("retry", "edit"):
            ran = any(step.get("kind") == "bash" and step.get("exit_code") is not None for step in record["steps"])
            if record.get("answer") or ran:
                STORE.replace_last_turn(cid, record)
                STORE.forget_undo(replaced)
            else:  # cancelled while loading, or the worker failed: the good turn and its memory stay
                STORE.keep_last_turn(cid, record)
                STORE.unrevert(replaced)
        else:
            STORE.append_turn(cid, record)


def start_job(kind: str, command: list[str], extra: dict) -> dict:
    with JOBS_LOCK:
        if any(job["process"].poll() is None for job in JOBS.values()):
            raise ValueError("이미 실행 중인 작업이 있습니다. 먼저 현재 작업이 끝날 때까지 기다려 주세요.")
        if uses_gpu({"kind": kind, **extra}) and LIVE.running():
            raise ValueError("에이전트 채팅 작업이 gpt-oss-20b를 GPU에서 쓰고 있습니다. 작업이 끝나면 모델을 "
                             "자동으로 내리니 그 뒤 다시 시도해 주세요(바로 비우려면 '모델 내리기').")
        job_id = uuid.uuid4().hex
        log_path = Path(tempfile.gettempdir()) / f"argus-dashboard-{job_id}.log"
        env = child_env(python311=kind == "agent")
        log = log_path.open("wb")
        try:
            process = subprocess.Popen(
                command, cwd=ROOT, stdout=log, stderr=subprocess.STDOUT,
                env=env, creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
            )
        except Exception:
            log.close()
            raise
        log.close()
        job = {"id": job_id, "kind": kind, "process": process, "log_path": log_path,
               "started_at": datetime.now(timezone.utc).isoformat(), **extra}
        JOBS[job_id] = job
    return {"id": job_id, "kind": kind, "started_at": job["started_at"]}


class Handler(SimpleHTTPRequestHandler):
    server_version = "ArgusScenarioStudio/1.0"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIST), **kwargs)

    def log_message(self, _fmt, *_args):
        return

    def end_headers(self):
        # Every answer, pages and JSON alike: no other site may put the local page in a frame (a decoy button over
        # a transparent frame would otherwise approve a held line or let other pages see the memory).
        self.send_header("Content-Security-Policy", "frame-ancestors 'none'")
        self.send_header("X-Frame-Options", "DENY")
        super().end_headers()

    def _headers(self, status: int, origin: str | None = None):
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        if origin and origin in ALLOWED_ORIGINS:
            self.send_header("Access-Control-Allow-Origin", origin)
            self.send_header("Vary", "Origin")
            self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
            self.send_header("Access-Control-Allow-Headers", "Content-Type")
            self.send_header("Access-Control-Allow-Private-Network", "true")
        self.end_headers()

    def _json(self, status: int, body: dict):
        origin = self.headers.get("Origin")
        self._headers(status, origin)
        self.wfile.write(json.dumps(body, ensure_ascii=False).encode("utf-8"))

    def _body(self) -> dict:
        length = int(self.headers.get("Content-Length", "0"))
        if length > 64_000:
            raise ValueError("요청이 너무 큽니다.")
        body = json.loads(self.rfile.read(length) or b"{}")
        if not isinstance(body, dict):
            raise ValueError("JSON 객체가 필요합니다.")
        return body

    def _memory_reply(self, memory: dict):
        return self._json(200, {**memory, "settings": STORE.settings(), "local_page": self._local_page()})

    def _memory_view(self) -> bool:
        """May this page read memory texts? Local pages always; others only when the local page allowed it."""
        return self._local_page() or STORE.settings()["remote_view"]

    def _send(self, status: int, body: bytes, content_type: str, filename: str | None = None):
        origin = self.headers.get("Origin")
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Cache-Control", "no-store")
        if filename:
            self.send_header("Content-Disposition", f'attachment; filename="{filename}"')
        if origin and origin in ALLOWED_ORIGINS:
            self.send_header("Access-Control-Allow-Origin", origin)
            self.send_header("Vary", "Origin")
        self.end_headers()
        self.wfile.write(body)

    def _local_page(self) -> bool:
        """The request comes from a page this machine serves (or from no page at all, e.g. curl)."""
        origin = self.headers.get("Origin")
        return origin is None or (urlparse(origin).hostname or "") in LOCAL_PAGE_HOSTS

    def _local_host(self) -> bool:
        """The request names this machine (DNS rebinding sends the attacker's host name instead)."""
        host = (self.headers.get("Host") or "").strip().lower()
        if host.startswith("["):
            host = host[1:host.find("]")] if "]" in host else host
        elif host.count(":") == 1:
            host = host.split(":", 1)[0]
        return host in LOCAL_HOSTS

    def do_OPTIONS(self):
        if not self._local_host():
            return self._json(403, {"error": "로컬 주소(127.0.0.1)로만 접근할 수 있습니다."})
        origin = self.headers.get("Origin")
        if origin not in ALLOWED_ORIGINS:
            return self._json(403, {"error": "허용되지 않은 웹 출처입니다."})
        self._headers(204, origin)

    def do_GET(self):
        path = urlparse(self.path).path
        if path.startswith("/api/") and not self._local_host():
            return self._json(403, {"error": "로컬 주소(127.0.0.1)로만 접근할 수 있습니다."})
        if path == "/api/health":
            try:
                health = runtime_status()
                if not self._memory_view():
                    with JOBS_LOCK:
                        job = JOBS.get(health.get("active_job") or "")
                    mine = bool(job and job.get("origin") == "remote")  # another page's job is only "busy" here
                    health = {**health, "live": remote_status(health.get("live") or {}),
                              "active_job": health.get("active_job") if mine else ("busy" if health.get("active_job") else None)}
                return self._json(200, health)
            except Exception as error:
                return self._json(500, {"error": str(error)})
        if path == "/api/scenarios":
            try:
                return self._json(200, scenario_catalog())
            except Exception as error:
                return self._json(500, {"error": str(error)})
        if path == "/api/live/status":
            return self._json(200, LIVE.status() if self._memory_view() else remote_status(LIVE.status()))
        if path == "/api/live/conversations":
            settle_recording()
            rows, status = STORE.conversations(), LIVE.status()
            if not self._local_page():  # a sealed turn's answer never previews elsewhere
                rows = [{**row, "last_answer": SEALED_HIDDEN} if row.get("last_sealed") else row for row in rows]
            if self._memory_view():
                return self._json(200, {"conversations": rows, "running": status["meta"]})
            # a page elsewhere sees the conversations it started (the local page can allow more)
            mine = []
            for row in rows:
                if row.get("origin") != "remote":
                    continue
                own = [turn for turn in (STORE.conversation(row["id"]) or {}).get("turns") or [] if turn.get("origin") == "remote"]
                last = own[-1] if own else {}
                mine.append({**row, "last_answer": SEALED_HIDDEN if last.get("sealed") else AM.clip(last.get("answer"), 120),
                             "alarms": sum(int(turn.get("alarms") or 0) for turn in own),
                             "memory_alarms": sum(int(turn.get("memory_alarms") or 0) for turn in own)})
            return self._json(200, {"conversations": mine, "running": remote_status(status)["meta"],
                                    "hidden_local": len(rows) - len(mine)})
        match = CONVERSATION_PATH.fullmatch(path)
        if match and not match.group(2):
            settle_recording()
            data = STORE.conversation(match.group(1))
            if not data:
                return self._json(404, {"error": "대화를 찾을 수 없습니다."})
            data = AM.with_conditions(data)
            if self._local_page():
                return self._json(200, {**data, "rewind_turn": rewindable_turn(data)})
            if self._memory_view():
                return self._json(200, without_sealed_pages(data))
            if AM.started_from(data) != "remote":
                return self._json(403, {"error": "로컬 페이지에서 시작한 대화는 로컬 페이지에서 볼 수 있습니다.", "local_only": True})
            return self._json(200, without_sealed_pages(without_memory_lines(remote_conversation(data))))
        if path == "/api/live/memory":
            settle_recording()
            memory = {**STORE.memory(), "settings": STORE.settings(), "local_page": self._local_page()}
            if self._local_page():
                return self._json(200, memory)
            return self._json(200, sealed_memory(memory) if self._memory_view() else memory_counts(memory))
        if path == "/api/live/store":
            if not self._local_page():
                return self._json(403, {"error": "로컬 페이지에서만 볼 수 있습니다.", "local_only": True})
            return self._json(200, {**store_identity(), "conversations": len(STORE.conversations()),
                                    "scorer": scorer_versions()})
        if path == "/api/live/memory/history":
            if not self._memory_view():
                return self._json(403, {"error": "기억 기록은 로컬 페이지에서 볼 수 있습니다.", "local_only": True})
            name = parse_qs(urlparse(self.path).query).get("name", [""])[0]
            try:
                versions = STORE.versions(name)
                if not self._local_page():  # held, rejected or withdrawn texts stay on the local page
                    versions = [item if item.get("status") == "approved" else {**item, "preview": "", "hidden": True}
                                for item in versions]
                return self._json(200, {"name": name, "versions": versions})
            except ValueError as error:
                return self._json(400, {"error": str(error)})
        if path == "/api/live/turn-file":
            if not self._local_page():
                STORE.audit("turn_file", "remote", refused=True)
                return self._json(403, {"error": "로컬 페이지에서만 볼 수 있습니다.", "local_only": True})
            query = parse_qs(urlparse(self.path).query)
            try:
                download = query.get("download", ["0"])[0] == "1"
                index = query.get("index", [None])[0]
                data, info = turn_file(query.get("conversation", [""])[0], int(query.get("turn", ["0"])[0]),
                                       query.get("path", [""])[0], query.get("side", ["after"])[0],
                                       TURN_FILE_DOWNLOAD if download else TURN_FILE_VIEW,
                                       query.get("list", [None])[0], int(index) if index is not None else None)
            except ValueError as error:
                code = getattr(error, "code", "bad_request")
                return self._json(getattr(error, "status", 400), {"error": str(error.args[0] if error.args else error), "code": code})
            STORE.audit("turn_file", "local", conversation=query.get("conversation", [""])[0], download=download)
            if download:
                if info["truncated"]:
                    return self._json(413, {"error": f"{TURN_FILE_DOWNLOAD // 2**20} MB보다 큰 파일은 받을 수 없습니다.", "code": "too_large"})
                name = re.sub(r"[^A-Za-z0-9._-]", "_", query.get("path", ["file"])[0].rsplit("/", 1)[-1])[:80] or "file"
                return self._send(200, data, "application/octet-stream", name)
            binary = b"\x00" in data[:8192]
            return self._json(200, {"text": "" if binary else data.decode("utf-8", "replace"), "binary": binary, **info})
        if path == "/api/live/export":
            if not self._local_page():
                STORE.audit("export", "remote", refused=True)
                return self._json(403, {"error": "내보내기는 로컬 페이지에서만 할 수 있습니다.", "local_only": True})
            query = parse_qs(urlparse(self.path).query)
            fmt = query.get("format", ["csv"])[0]
            cid = query.get("conversation", ["all"])[0]
            if fmt not in ("csv", "jsonl") or (cid != "all" and not AM.valid_conversation_id(cid)):
                return self._json(400, {"error": "format은 csv 또는 jsonl, conversation은 대화 ID 또는 all이어야 합니다."})
            settle_recording()
            STORE.audit("export", "local", conversation=cid, format=fmt)
            body, kind = export_verdicts(fmt, cid)
            return self._send(200, body, kind, f"argus-live-verdicts-{cid}.{fmt}")
        if path == "/api/live/events":
            query = parse_qs(urlparse(self.path).query)
            try:
                after = int(query.get("after", ["0"])[0])
                wait = float(query.get("wait", ["0"])[0])
            except ValueError:
                return self._json(400, {"error": "after와 wait는 숫자여야 합니다."})
            data = LIVE.events_after(after, wait)
            view = self._memory_view()
            events = data["events"] if view else [event for event in data["events"] if remote_visible_event(event)]
            status = {key: value for key, value in data.items() if key != "events"}
            return self._json(200, {**(status if view else remote_status(status)),
                                    "events": [public_event(event, view, self._local_page()) for event in events]})
        if path.startswith("/api/jobs/"):
            job_id = path.rsplit("/", 1)[-1]
            with JOBS_LOCK:
                job = JOBS.get(job_id)
            if not job or (not self._memory_view() and job.get("origin") != "remote"):
                return self._json(404, {"error": "작업을 찾을 수 없습니다."})  # another page's job is not there for it
            try:
                output = job["log_path"].read_text(encoding="utf-8", errors="replace")
            except OSError:
                output = ""
            code = job["process"].poll()
            score_data = None
            clean_lines = []
            for line in output.splitlines():
                if line.startswith("ARGUS_RESULT_JSON="):
                    try:
                        score_data = json.loads(line.split("=", 1)[1])
                    except json.JSONDecodeError:
                        clean_lines.append("추론 결과를 읽지 못했습니다.")
                else:
                    clean_lines.append(line)
            output = "\n".join(clean_lines)
            return self._json(200, {"id": job_id, "kind": job["kind"], "output": output[-50_000:],
                                    "running": code is None, "exit_code": code,
                                    "started_at": job["started_at"], "score_data": score_data,
                                    **job.get("result", {})})
        if path.startswith("/api/"):
            return self._json(404, {"error": "지원하지 않는 API입니다."})
        return super().do_GET()

    def do_POST(self):
        path = urlparse(self.path).path
        if not self._local_host():
            return self._json(403, {"error": "로컬 주소(127.0.0.1)로만 접근할 수 있습니다."})
        origin = self.headers.get("Origin")
        if origin is not None and origin not in ALLOWED_ORIGINS:
            # Browsers send Origin with every cross-site POST; without this check any web page could start tasks
            # or rewrite the agent's memory (AGENTS.md) through a simple form-style request.
            return self._json(403, {"error": "허용되지 않은 웹 출처입니다."})
        if path == "/api/replay/start":
            try:
                body = self._body()
                catalog = scenario_catalog()
                scenario = next((s for s in catalog["scenarios"] if s["id"] == body.get("scenario")), None)
                if not scenario:
                    raise ValueError("선택한 시나리오가 점수표에 없습니다.")
                unit_id = body.get("unit")
                unit = next((u for u in scenario["runs"] if u["id"] == unit_id), None)
                if not unit:
                    raise ValueError("해당 시나리오에 속한 실행 기록을 선택해 주세요.")
                mode = body.get("mode", "hidden")
                if mode not in ("hidden", "tokens"):
                    raise ValueError("재생 모드는 saved hidden 또는 tokens여야 합니다.")
                model = body.get("model", "P5")
                if model not in MODEL_CHECKPOINTS or not MODEL_CHECKPOINTS[model].is_file():
                    raise ValueError("선택한 모델의 추론 체크포인트를 찾을 수 없습니다.")
                command = [sys.executable, str(ROOT / "argus_hook" / "replay_model_inference.py"),
                           "--unit", unit_id, "--model", model, "--mode", mode]
                if body.get("offline"):
                    command.append("--offline")
                return self._json(202, start_job("replay", command, {
                    "scenario": scenario["id"], "unit": unit_id, "model": model, "mode": mode,
                    "origin": "local" if self._local_page() else "remote",
                }))
            except ValueError as error:
                return self._json(400, {"error": str(error)})
            except Exception as error:
                return self._json(500, {"error": str(error)})
        if path == "/api/agent/start":
            if not self._local_page():
                # it runs model-written commands in the sandbox that holds the memory, without the chat's checks and
                # with every output in the job log: never for a page elsewhere
                STORE.audit("agent_start", "remote", refused=True)
                return self._json(403, {"error": "이 작업은 로컬 페이지에서만 시작할 수 있습니다.", "local_only": True})
            try:
                body = self._body()
                task = str(body.get("task", "")).strip()
                if not task or len(task) > MAX_TASK_CHARS:
                    raise ValueError(f"작업은 1~{MAX_TASK_CHARS:,}자로 입력해 주세요.")
                if not AGENT_SCRIPT.is_file():
                    raise ValueError("argus_hook/agent_loop.py를 찾을 수 없습니다.")
                health = runtime_status()
                missing = [label for key, label in (
                    ("agent_model_dir", "gpt-oss-20b 로컬 모델"),
                    ("cuda_available", "CUDA GPU"),
                    ("sandbox_script", "샌드박스 스크립트"),
                    ("docker_available", "Docker"),
                    ("python311_command", "Python 3.11 sandbox 호출"),
                ) if not health[key]]
                if missing:
                    raise ValueError("에이전트를 실행할 수 없습니다. 준비되지 않은 항목: " + ", ".join(missing))
                steps = int(body.get("max_steps", 5))
                if not 1 <= steps <= 10:
                    raise ValueError("step 수는 1~10 범위여야 합니다.")
                command = [sys.executable, str(AGENT_SCRIPT), "--task", task,
                           "--hook-phase", "generation", "--max-steps", str(steps)]
                STORE.audit("agent_start", "local")
                return self._json(202, start_job("agent", command, {"task": task, "origin": "local"}))
            except ValueError as error:
                return self._json(400, {"error": str(error)})
            except Exception as error:
                return self._json(500, {"error": str(error)})
        match = CONVERSATION_PATH.fullmatch(path)
        if path in ("/api/live/memory", "/api/live/memory/review", "/api/live/memory/rollback",
                    "/api/live/memory/forget", "/api/live/settings") or (match and match.group(2)):
            try:
                body = self._body()
                local_only = "기억에 대한 결정(승인·거절·되돌리기·수정·빼기)과 대화 삭제는 이 컴퓨터의 로컬 페이지(http://127.0.0.1:8765)에서만 할 수 있습니다."
                decision = path in ("/api/live/memory", "/api/live/memory/review", "/api/live/memory/rollback",
                                    "/api/live/memory/forget", "/api/live/settings") or (match and match.group(2) == "delete")
                origin = "local" if self._local_page() else "remote"
                action = path.rsplit("/", 1)[-1] if not match else match.group(2) or "conversation"
                if decision and origin == "remote":
                    STORE.audit(action, origin, refused=True, conversation=match.group(1) if match else None)
                    return self._json(403, {"error": local_only, "local_only": True})
                if path == "/api/live/settings":
                    settings = STORE.set_settings(body.get("remote_view") is True)
                    STORE.audit("settings", origin, remote_view=settings["remote_view"])
                    return self._json(200, settings)
                if path == "/api/live/memory/forget":
                    memory = STORE.forget_line(str(body.get("name", "")), str(body.get("line", "")))
                    STORE.audit("forget", origin, file=str(body.get("name", "")), line_key=AM.line_key(str(body.get("line", ""))))
                    return self._memory_reply(memory)
                if path == "/api/live/memory":
                    text = body.get("text")
                    if text is not None and not isinstance(text, str):
                        raise ValueError("text는 문자열이거나 null(기본값으로 되돌리기)이어야 합니다.")
                    if not self._local_page():  # an edit is approved at once: stronger than approving a held line
                        return self._json(403, {"error": local_only, "local_only": True})
                    memory = STORE.edit_memory(str(body.get("name", "")), text)
                    STORE.audit("edit", origin, file=str(body.get("name", "")), reset=text is None)
                    return self._memory_reply(memory)
                if path == "/api/live/memory/review":
                    memory = STORE.review(str(body.get("id", "")), body.get("approve") is True)
                    STORE.audit("approve" if body.get("approve") is True else "reject", origin, item=str(body.get("id", "")))
                    return self._memory_reply(memory)
                if path == "/api/live/memory/rollback":
                    if not self._local_page():
                        return self._json(403, {"error": local_only, "local_only": True})
                    version = body.get("version")
                    if not isinstance(version, int) or isinstance(version, bool):
                        raise ValueError("version은 정수여야 합니다.")
                    memory = STORE.rollback(str(body.get("name", "")), version)
                    STORE.audit("rollback", origin, file=str(body.get("name", "")), version=version)
                    return self._memory_reply(memory)
                cid, action = match.groups()
                running = LIVE.status()
                if running["busy"] and running["meta"].get("conversation") == cid:
                    raise ValueError("작업이 실행 중인 대화는 바꾸거나 지울 수 없습니다.")
                view = self._memory_view()  # the answer is a conversation: filtered like a GET of one
                if not view and action in ("rename", "fork"):
                    own = STORE.conversation(cid)
                    if own and AM.started_from(own) != "remote":
                        STORE.audit(action, origin, refused=True, conversation=cid)
                        return self._json(403, {"error": local_only, "local_only": True})
                if action == "rename":  # a title set elsewhere is not shown to the agent as the user's words
                    data = STORE.rename(cid, str(body.get("title", "")), origin)
                    STORE.audit("rename", origin, conversation=cid)
                    return self._json(200, data if view else without_memory_lines(remote_conversation(data)))
                if action == "fork":
                    upto = body.get("turn")
                    if not isinstance(upto, int) or isinstance(upto, bool) or upto < 1:
                        raise ValueError("turn은 1 이상의 정수여야 합니다.")
                    data = STORE.fork(cid, upto, origin)
                    STORE.audit("fork", origin, conversation=cid, turn=upto, fork=data["id"])
                    return self._json(200, data if view else without_memory_lines(remote_conversation(data)))
                if not STORE.delete(cid):
                    return self._json(404, {"error": "대화를 찾을 수 없습니다."})
                STORE.audit("delete", origin, conversation=cid)
                return self._json(200, {"ok": True, "conversations": STORE.conversations()})
            except ValueError as error:
                return self._json(400, {"error": str(error)})
            except Exception as error:
                return self._json(500, {"error": str(error)})
        if path == "/api/live/sandbox/clear":
            if not self._local_page():
                return self._json(403, {"error": "로컬 페이지에서만 할 수 있습니다.", "local_only": True})
            if LIVE.status()["busy"]:
                return self._json(409, {"error": "작업이 실행 중이라 지금은 비울 수 없습니다.", "code": "busy"})
            try:
                state = sandbox_files().clear()
            except Exception as error:
                STORE.audit("sandbox_clear", "local", failed=True)
                return self._json(500, {"error": f"{type(error).__name__}: {error}", "cleared": False})
            STORE.audit("sandbox_clear", "local", cleared=bool(state.get("cleared")))
            if state.get("cleared"):
                STORE.mark_sandbox(cleared=True)
            _REMOTE_REFUSAL.clear()
            workspace = state.get("workspace") or {}
            return self._json(200, {"cleared": bool(state.get("cleared")), "strays": workspace.get("strays"),
                                    "stray_names": workspace.get("stray_names"), "entries": workspace.get("entries"),
                                    "hooks": workspace.get("hooks"), "hook_names": workspace.get("hook_names"),
                                    "canary": bool(workspace.get("canary")), "listing_sha": workspace.get("listing_sha")})
        if path == "/api/live/sandbox/restore":
            with _START_LOCK:  # no turn starts while the sandbox is stopped and restored (sandbox.py's lock does not wait)
                # '마지막 정상 상태로': a workspace sandbox.py can no longer snapshot is dropped (stop --force), a new
                # container started and the newest snapshot restored. Local page only, not while a task runs.
                if not self._local_page():
                    STORE.audit("sandbox_restore", "remote", refused=True)
                    return self._json(403, {"error": "로컬 페이지에서만 할 수 있습니다.", "local_only": True})
                if LIVE.status()["busy"]:
                    return self._json(409, {"error": "작업이 실행 중이라 지금은 할 수 없습니다.", "code": "busy"})
                body = self._body()
                whole = None  # "이 턴 전으로": {conversation, turn} of the latest local turn that ran commands
                if body.get("conversation") or body.get("turn") is not None:
                    try:
                        turn, files = turn_files(body.get("conversation"), body.get("turn"))
                        sandbox = STORE.sandbox_state()
                        owner = sandbox.get("restore_turn") or {}
                        if sandbox["debts"]:
                            raise ApiRefusal("다른 페이지의 턴이 남긴 것을 먼저 정리해야 합니다(샌드박스 점검).", "sandbox_unswept", 409)
                        if owner.get("conversation") != body.get("conversation") or owner.get("turn") != body.get("turn"):
                            raise ApiRefusal("이 턴 뒤에 다른 턴이 명령을 실행해 이 턴 전으로 되돌릴 수 없습니다. "
                                             "'마지막 정상 상태로'를 쓰세요.", "not_latest", 409)
                        start = snapshot_path(files.get("start"))
                        if start is None:
                            raise ApiRefusal("이 턴의 시작 스냅숏이 더 이상 없습니다.", "snapshot_gone", 410)
                    except ApiRefusal as refusal:
                        return self._json(refusal.status, {"error": refusal.args[0], "code": refusal.code})
                    whole = {"conversation": body["conversation"], "turn": body["turn"], "run_id": turn.get("run_id"),
                             "revert_memory": body.get("revert_memory") is True}
                    point = {"name": start.name, "time": start.stat().st_mtime, "mtime": start.stat().st_mtime, "ledger": True}
                else:
                    point = restore_point()
                if not point:
                    return self._json(409, {"error": "되돌릴 스냅숏이 없습니다.", "code": "no_snapshot"})
                for args in (["stop", "--force"], ["up"], ["restore", str(SNAPSHOTS / point["name"])]):
                    data = run_sandbox_cli(args)
                    if data.get("status") == "ERROR":
                        STORE.audit("sandbox_restore", "local", failed=True, step=args[0])
                        return self._json(500, {"error": f"{args[0]}: {str(data.get('reason') or '')[-200:]}"})
                why = STORE.sandbox_state()["blocked"]  # what had stopped the sandbox (the next turn hears it, and the hint)
                STORE.mark_sandbox(blocked=None, cleared=True)  # the memory folder is the snapshot's: written again next
                try:  # the snapshot's own memory folder goes (written again next); HOME is the user's, as it was then
                    swept = sandbox_files().sweep("all", [], agent=True, scratch=True, everything=True)
                except Exception:
                    swept = {}
                debts = STORE.sandbox_state()["debts"]
                # a local turn's state from before every open debt: what those pages elsewhere left is gone with it
                before_debts = point.get("ledger") and debts and point["mtime"] < min(d.get("since") or 0 for d in debts)
                if before_debts and not swept.get("left"):
                    STORE.settle_debt(None, clean=True)
                owner = STORE.sandbox_state().get("restore_turn") if point.get("ledger") else None
                if whole:  # every command of that turn is undone; the way back is now its start
                    command = STORE.mark_turn_restored(whole["conversation"], whole["turn"])
                    STORE.mark_sandbox(restore_point=point["name"], restore_turn=None)
                    if whole["revert_memory"] and whole.get("run_id"):  # its memory lines too (what they said is gone)
                        reverted = STORE.revert_run(whole["run_id"], {"conversation": whole["conversation"], "turn": whole["turn"]},
                                                    final=True)
                        STORE.audit("revert", "local", conversation=whole["conversation"], turn=whole["turn"],
                                    files=len(reverted or []), reason="rewind")
                else:
                    command = STORE.mark_undone(owner["conversation"], owner["turn"], owner.get("step"), kind=why or "restore") \
                        if isinstance(owner, dict) and owner.get("conversation") else None
                STORE.mark_sandbox(changed={"count": 0, "paths": [], "restored": point["name"], "restored_command": command,
                                            "restored_kind": why}, drop_remote_changes=bool(before_debts))
                _REMOTE_REFUSAL.clear()
                STORE.audit("sandbox_restore", "local", snapshot=point["name"], disabled=len(swept.get("disabled") or []),
                            **({"conversation": whole["conversation"], "turn": whole["turn"]} if whole else {}))
                return self._json(200, {"restored": point["name"], "time": point["time"], "turn": (whole or {}).get("turn")})
        if path in ("/api/live/sandbox/check", "/api/live/sandbox/sweep"):
            # Without a model: what earlier commands left running in the sandbox and the hooks under its HOME, and
            # (sweep) stopping / switching off exactly the ones the page was shown. Local page only.
            if not self._local_page():
                STORE.audit(path.rsplit("/", 1)[-1], "remote", refused=True)
                return self._json(403, {"error": "로컬 페이지에서만 할 수 있습니다.", "local_only": True})
            if LIVE.status()["busy"]:
                return self._json(409, {"error": "작업이 실행 중이라 지금은 할 수 없습니다.", "code": "busy"})
            _REMOTE_REFUSAL.clear()
            try:
                if path.endswith("/check"):
                    workspace, done = sandbox_files().workspace(), {}
                    if STORE.sandbox_state()["blocked"]:  # sandbox.py could snapshot again: it runs commands again
                        STORE.mark_sandbox(blocked=None)
                        STORE.audit("sandbox_unblocked", "local")
                else:
                    body = self._body()
                    done = sandbox_files().sweep([(int(p[0]), int(p[1])) for p in body.get("pids") or []],
                                                 [str(h) for h in body.get("hooks") or []])
                    workspace = done.get("workspace") or {}
                    STORE.audit("sandbox_sweep", "local", killed=len(done.get("killed") or []),
                                disabled=len(done.get("disabled") or []))
            except (TypeError, ValueError, IndexError) as error:
                return self._json(400, {"error": f"pids는 [pid, start] 목록, hooks는 경로 목록이어야 합니다: {error}"})
            except AM.BlockedSandbox as error:
                STORE.mark_sandbox(blocked=error.kind)
                return self._json(200, {"blocked": error.kind, "message": AM.BLOCKED_TEXT[error.kind], "strays": 0,
                                        "hooks": 0, "procs": [], "hook_names": [], "hook_paths": [], "killed": [],
                                        "disabled": [], "restore_point": restore_point(), "archive_limit": archive_limit()})
            except Exception as error:
                return self._json(500, {"error": f"{type(error).__name__}: {error}"})
            return self._json(200, {"strays": workspace.get("strays") or 0, "hooks": workspace.get("hooks") or 0,
                                    "archive_bytes": workspace.get("archive_bytes"), "archive_limit": archive_limit(),
                                    "disk_free": disk_free(), "disk_low": DISK_LOW, "quarantine": done.get("quarantine"),
                                    **snapshots_usage(),
                                    "blocked": STORE.sandbox_state()["blocked"], "restore_point": restore_point(),
                                    "procs": workspace.get("procs") or [], "hook_names": workspace.get("hook_names") or [],
                                    "hook_paths": workspace.get("hook_paths") or [],
                                    "killed": done.get("killed") or [], "disabled": done.get("disabled") or []})
        if path in ("/api/live/start", "/api/live/unload", "/api/live/cancel"):
            try:
                body = self._body()
                if path == "/api/live/start":
                    task = str(body.get("task", "")).strip()
                    if not task or len(task) > MAX_TASK_CHARS:
                        raise ValueError(f"작업은 1~{MAX_TASK_CHARS:,}자로 입력해 주세요.")
                    steps = int(body.get("max_steps", 5))
                    if not 1 <= steps <= MAX_LIVE_STEPS:
                        raise ValueError(f"step 수는 1~{MAX_LIVE_STEPS} 범위여야 합니다.")
                    conversation = body.get("conversation") or None
                    if conversation is not None and not isinstance(conversation, str):
                        raise ValueError("conversation은 대화 ID 문자열이어야 합니다.")
                    battery = body.get("battery")
                    if battery is not None and (not isinstance(battery, dict) or not self._local_page()):
                        return self._json(403, {"error": "battery는 로컬 페이지의 계획 실행에서만 받습니다.", "local_only": True})
                    # Memory only when the page asks for it: an older page (no switch) runs without it.
                    try:
                        return self._json(202, start_live(task, steps, conversation, body.get("memory") is True,
                                                          body.get("last_turn") or None, remote=not self._local_page(),
                                                          battery=battery))
                    except ApiRefusal as refusal:
                        return self._json(refusal.status, {"error": str(refusal), "code": refusal.code,
                                                           "local_only": refusal.status == 403 or None})
                origin = "local" if self._local_page() else "remote"
                view = self._memory_view()
                running = LIVE.status()
                if origin == "remote" and not view and running.get("busy") and SESSION_ORIGIN.get(running.get("session")) != "remote":
                    STORE.audit(path.rsplit("/", 1)[-1], origin, refused=True)  # a page elsewhere never stops the user's task
                    return self._json(403, {"error": "로컬 페이지에서 시작한 작업은 로컬 페이지에서만 멈출 수 있습니다.", "local_only": True})
                if path == "/api/live/unload":
                    STORE.audit("unload", origin)
                    status = LIVE.stop()
                else:
                    STORE.audit("cancel", origin)
                    status = LIVE.cancel()
                return self._json(200, status if view else remote_status(status))
            except ValueError as error:
                return self._json(400, {"error": str(error)})
            except Exception as error:
                return self._json(500, {"error": str(error)})
        self._json(404, {"error": "지원하지 않는 API입니다."})


def main():
    if not SCORES_FILE.is_file() or not DESCRIPTIONS_FILE.is_file():
        raise SystemExit("Argus-V replay assets are missing under argus_hook/replay_assets.")
    if not DIST.is_dir() or not (DIST / "index.html").is_file():
        raise SystemExit(f"Dashboard UI is missing: {DIST / 'index.html'}")
    server = ThreadingHTTPServer(("127.0.0.1", 8765), Handler)
    print("Argus-V Scenario Studio: http://127.0.0.1:8765")
    print("Local companion API binds to 127.0.0.1 only.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nDashboard stopped.")
    finally:
        server.server_close()
        if LIVE.running():
            print("Unloading the live agent model...")
            LIVE.stop()


if __name__ == "__main__":
    main()

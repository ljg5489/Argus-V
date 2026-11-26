"""Which sandbox: the folders the everyday server (argus_hook/agent_server.py) can use, the one the agent works in,
and a ledger for each.

    plain  SANDBOX/       the plan's (locked by plan v1.6): no screen, a fake internet (fakenet)
    pc     SANDBOX_PC/    the computer: a screen, tools, the Python package index only
    net    SANDBOX_NET/   the internet: the computer, with the public web (HTTP and HTTPS) open

The agent chat works in one of them (the "agent's" sandbox, chosen on the page and kept between starts); the
sandbox computer tab looks at any of them, the agent's or another, whatever the agent is doing in its own.

The locked server knows one sandbox: its names (SANDBOX_SCRIPT, SNAPSHOTS) and its one ledger of it in the memory
store (manifest.json, "sandbox": the way back, what blocks it, files a sealed turn left, turns of pages elsewhere
not yet cleaned up after). Here:

- select(): the server's names point at the agent's sandbox, and the worker it starts is told the same folder;
- a ledger for each sandbox: the store's "sandbox" on disk stays SANDBOX/'s own (the locked server, started on the
  same store, finds what it left); the others are kept under "sandbox_ledgers", and while one of them is the agent's
  the store is shown it as "sandbox" (install_ledgers wraps the store's read and write of its manifest);
- switch(): changing the agent's sandbox. The memory folder (/workspace/.agent) is one memory written into whichever
  sandbox the agent uses: the folder in the sandbox that is left, and in the one that is entered, is removed and
  marked so, and the next turn writes it whole from the store (as after "마지막 정상 상태로"). Otherwise a folder
  left behind would be read later as lines changed outside the memory step.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOLDERS = {"plain": "SANDBOX", "pc": "SANDBOX_PC", "net": "SANDBOX_NET"}
LABELS = {"plain": "기본", "pc": "컴퓨터", "net": "인터넷"}
ABOUT = {"plain": "계획 실행과 같은 샌드박스 · 화면 없음 · 가짜 인터넷만 연결",
         "pc": "화면과 도구가 있는 컴퓨터 · 파이썬 패키지 저장소에만 연결",
         "net": "화면과 도구가 있는 컴퓨터 · 공개 웹(HTTP·HTTPS)에 연결"}
OPEN_NAME = "open.internet"       # SANDBOX_NET/settings.json: its proxy lets any public address through
LEDGERS, CHOSEN = "sandbox_ledgers", "agent_sandbox"   # keys of the store's manifest that are this module's own
PLAIN_KEPT = "\x00plain_sandbox"  # rides along in a manifest read while another ledger is shown as "sandbox"


class _Current:
    name = "plain"                # whose ledger the store is shown as "sandbox"


CURRENT = _Current()
RAW = {"read": None, "save": None}  # the store's own read and write of its manifest (set by install_ledgers)
SKIP = ("before-restore", "before-stop", "before-up", "before-reset", "before-import")


class Box:
    """One sandbox folder."""

    def __init__(self, name: str, root: Path):
        self.name, self.root = name, Path(root)
        self.script, self.snapshots = self.root / "sandbox.py", self.root / "snapshots"
        self.label, self.about = LABELS.get(name, name), ABOUT.get(name, "")

    def settings(self) -> dict:
        try:
            data = json.loads((self.root / "settings.json").read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return {}
        return data if isinstance(data, dict) else {}

    def screen(self) -> bool:
        return (self.root / "desk.py").is_file()

    def network(self) -> str:
        """fakenet | allowlist | open (the allowlist that names the open web) | none | internal | unknown"""
        settings = self.settings()
        kind = str(settings.get("network") or "unknown")
        return "open" if kind == "allowlist" and OPEN_NAME in (settings.get("allowed_hosts") or []) else kind

    def said(self) -> dict:
        return {"name": self.name, "folder": self.root.name, "label": self.label, "about": self.about,
                "network": self.network(), "screen": self.screen()}


def every(root: Path = ROOT) -> dict[str, Box]:
    """The sandboxes that are there (a folder with a sandbox.py), in the order they are offered."""
    return {name: Box(name, root / folder) for name, folder in FOLDERS.items() if (root / folder / "sandbox.py").is_file()}


def agent(DS) -> Box:
    """The sandbox the server's own names point at: the one the agent works in."""
    folder = Path(DS.SANDBOX_SCRIPT).parent
    name = next((name for name, known in FOLDERS.items() if known == folder.name), None)
    return Box(name or folder.name, folder)


def get(DS, name) -> Box:
    """The sandbox a request names (nothing named: the agent's), or ValueError."""
    mine = agent(DS)
    if name in (None, "", mine.name):
        return mine
    known = every(Path(DS.SANDBOX_SCRIPT).parent.parent)
    if not isinstance(name, str) or name not in known:
        raise ValueError("모르는 샌드박스입니다.")
    return known[name]


def is_agent(DS, box: Box) -> bool:
    return box.root == Path(DS.SANDBOX_SCRIPT).parent


def run_script(DS, script: Path, args: list[str], timeout: int = 300) -> dict:
    """One sandbox.py command of a folder that is not the agent's (as dashboard_server.run_sandbox_cli for its own)."""
    try:
        done = subprocess.run(["python3.11", str(script), *args], capture_output=True, text=True, encoding="utf-8",
                              errors="replace", timeout=timeout, env=DS.live_env())
        return json.loads(done.stdout or done.stderr or "{}")
    except (subprocess.TimeoutExpired, json.JSONDecodeError, OSError) as error:
        return {"status": "ERROR", "reason": f"{type(error).__name__}"}


def cli(DS, box: Box, args: list[str], timeout: int = 300) -> dict:
    """sandbox.py of ``box`` (its JSON report, or an ERROR)."""
    if is_agent(DS, box):
        return DS.run_sandbox_cli(args, timeout=timeout)
    return run_script(DS, box.script, args, timeout)


def disk_free(box: Box) -> int | None:
    try:
        return shutil.disk_usage(box.snapshots if box.snapshots.exists() else box.root).free
    except OSError:
        return None


def newest_snapshot(box: Box) -> Path | None:
    """The newest snapshot sandbox.py took before a command in ``box`` (not the ones it takes around a restore)."""
    try:
        return max((path for path in box.snapshots.glob("*.tar") if not path.name.startswith(SKIP)),
                   key=lambda path: path.stat().st_mtime)
    except (ValueError, OSError):
        return None


# ---------------------------------------------------------------------------- a ledger for each sandbox
def install_ledgers(AM, patch=setattr) -> None:
    """Wrap the store's read and write of its manifest: while CURRENT names another sandbox than plain, the store is
    shown that sandbox's ledger as "sandbox", and what it saves there goes back under "sandbox_ledgers"; on disk
    "sandbox" stays SANDBOX/'s own. With CURRENT at plain nothing is changed."""
    read, save = AM.ConversationStore._manifest, AM.ConversationStore._save
    if getattr(read, "argus_boxes", False):
        return  # wrapped already
    RAW.update(read=read, save=save)

    def _manifest(self):
        data = read(self)
        name = CURRENT.name
        if name != "plain":
            data[PLAIN_KEPT] = {"shown": name, "plain": data.get("sandbox")}
            data["sandbox"] = dict((data.get(LEDGERS) or {}).get(name) or {})
        return data

    def _save(self, manifest):
        if PLAIN_KEPT in manifest:  # read while another sandbox's ledger was shown: each goes back to its place
            manifest = dict(manifest)
            kept = manifest.pop(PLAIN_KEPT)
            # filed under the sandbox it was read as (not the one current now: the agent's may have changed between)
            manifest[LEDGERS] = {**(manifest.get(LEDGERS) or {}), kept["shown"]: manifest.get("sandbox") or {}}
            if kept["plain"] is None:
                manifest.pop("sandbox", None)
            else:
                manifest["sandbox"] = kept["plain"]
        return save(self, manifest)

    _manifest.argus_boxes = True
    patch(AM.ConversationStore, "_manifest", _manifest)
    patch(AM.ConversationStore, "_save", _save)


def _raw(store) -> tuple:
    """The store's manifest as it is on disk, and how to write it (whether or not the ledgers are wrapped)."""
    read = RAW["read"] or type(store)._manifest
    save = RAW["save"] or type(store)._save
    return read(store), lambda manifest: save(store, manifest)


def ledger(DS, box: Box) -> dict:
    """What the server holds about ``box``: {"restore_point", "restore_turn", "blocked", "sealed_files", "cleared",
    "debts"}. The agent's: the store's own reading; another's: its entry as it is on disk."""
    if is_agent(DS, box):
        return DS.STORE.sandbox_state()
    with DS.STORE.lock:
        raw, _save = _raw(DS.STORE)
    state = (raw.get("sandbox") if box.name == "plain" else (raw.get(LEDGERS) or {}).get(box.name)) or {}
    return {"restore_point": state.get("restore_point"), "restore_turn": state.get("restore_turn"),
            "blocked": state.get("blocked"), "sealed_files": state.get("sealed_files"),
            "cleared": bool(state.get("cleared_at")), "debts": list(state.get("debts") or [])}


def mark(DS, box: Box, **changes) -> None:
    """mark_sandbox for ``box``: restore_point (the turn that could be taken back goes with it), blocked,
    sealed_files, cleared. The agent's goes through the store's own mark_sandbox."""
    if is_agent(DS, box):
        DS.STORE.mark_sandbox(**changes)
        return
    with DS.STORE.lock:
        raw, save = _raw(DS.STORE)
        state = raw.setdefault("sandbox", {}) if box.name == "plain" else raw.setdefault(LEDGERS, {}).setdefault(box.name, {})
        if "restore_point" in changes:
            state["restore_point"] = changes["restore_point"] or None
            state["restore_turn"] = changes.get("restore_turn") or None
        if "blocked" in changes:
            state["blocked"] = changes["blocked"] or None
        if "sealed_files" in changes:
            state["sealed_files"] = {str(k)[:1024]: str(v)[:80] for k, v in list((changes["sealed_files"] or {}).items())[:200]} or None
        if "cleared" in changes:
            if changes["cleared"]:
                state["cleared_at"] = time.time()
            else:
                state.pop("cleared_at", None)
        save(raw)


def chosen(DS) -> str | None:
    """The sandbox the agent was last given (kept in the store between starts), if it is still there."""
    with DS.STORE.lock:
        raw, _save = _raw(DS.STORE)
    name = raw.get(CHOSEN)
    return name if isinstance(name, str) and name in every(Path(DS.SANDBOX_SCRIPT).parent.parent) else None


def keep_choice(DS, name: str) -> None:
    with DS.STORE.lock:
        raw, save = _raw(DS.STORE)
        raw[CHOSEN] = name
        save(raw)


PLAIN_ONLY = ("fakenet_until",)  # of a ledger: what only SANDBOX/ has (the fake internet's log, read up to here)


def adopt(DS) -> str | None:
    """A store from before the ledgers were kept apart has one, written by whichever sandbox the server of the day
    used (agent_server.py worked in SANDBOX_PC for a while with the store's one ledger). Whose it is shows in its way
    back: a snapshot's name is in one folder only. When it is another sandbox's than SANDBOX/, it is filed under that
    sandbox and kept as the agent's; SANDBOX/'s own starts anew, marked so that its memory folder (as old as the
    agent's last turn there) is written whole the next time. Done once: a store with a choice or ledgers of its own
    is left alone. -> the sandbox the ledger was (None: nothing to tell from, or done already)."""
    with DS.STORE.lock:
        raw, save = _raw(DS.STORE)
        state = raw.get("sandbox") or {}
        point = state.get("restore_point")
        if CHOSEN in raw or LEDGERS in raw or not isinstance(point, str) or not point or Path(point).name != point:
            return None
        known = every(Path(DS.SANDBOX_SCRIPT).parent.parent)
        owner = next((name for name, box in known.items() if (box.snapshots / point).is_file()), None)
        if owner in (None, "plain"):
            return owner
        raw[LEDGERS] = {owner: {key: value for key, value in state.items() if key not in PLAIN_ONLY}}
        raw["sandbox"] = {**{key: state[key] for key in PLAIN_ONLY if key in state}, "cleared_at": time.time()}
        raw[CHOSEN] = owner
        save(raw)
    DS.STORE.audit("sandbox_ledger", "local", sandbox=owner, restore_point=point)
    return owner


# ---------------------------------------------------------------------------- the agent's sandbox
def select(DS, box: Box, patch=setattr, environ=None) -> None:
    """Point the server's own names, the store's ledger and the worker it starts at ``box``. Nothing is run."""
    import agent_loop
    from live_agent_free import ensure_running

    environ = os.environ if environ is None else environ
    if "locked_ensure_running" not in RAW:
        RAW["locked_ensure_running"] = agent_loop.RealSandboxClient.ensure_running
    patch(DS, "SANDBOX_SCRIPT", box.script)
    patch(DS, "SNAPSHOTS", box.snapshots)
    if box.name == "plain":  # the locked client's own start (it turns the network to fakenet, which SANDBOX/ is)
        patch(agent_loop.RealSandboxClient, "ensure_running", RAW["locked_ensure_running"])
        environ.pop("ARGUS_SANDBOX_SCRIPT", None)
    else:  # a sandbox that keeps its own network; live_agent_free.py reads the folder from the environment
        patch(agent_loop.RealSandboxClient, "ensure_running", ensure_running)
        environ["ARGUS_SANDBOX_SCRIPT"] = str(box.script)
    with DS.STORE.lock:  # no read-then-write of the store's is cut in two by the change
        patch(CURRENT, "name", box.name)


def forget_memory_folder(DS, box: Box) -> str | None:
    """Remove /workspace/.agent in ``box`` (the agent's, at this moment) and mark its ledger so: the next turn there
    writes the folder whole from the store. -> why it could not be removed (None: removed; the mark is made anyway)."""
    why = None
    try:
        state = DS.sandbox_files().clear()
        if not state.get("cleared"):
            why = "기억 폴더를 비우지 못했습니다"
    except Exception as error:  # blocked, or it does not start: said, and the ledger says the folder is to be rewritten
        why = f"{type(error).__name__}: {str(error)[:160]}"
    DS.STORE.mark_sandbox(cleared=True)
    return why


def switch(DS, name: str, patch=setattr, environ=None) -> dict:
    """Give the agent another sandbox (between turns). -> {"agent", "was", "left", "entered"}; ValueError when it
    cannot be done now. The caller holds the server's start lock and has seen that nothing runs."""
    target = get(DS, name)
    was = agent(DS)
    if target.root == was.root:
        return {"agent": was.name, "was": was.name}
    if DS.STORE.sandbox_state().get("debts"):
        raise ValueError("다른 페이지의 턴이 남긴 것을 먼저 정리해야 샌드박스를 바꿀 수 있습니다(기억 카드의 샌드박스 점검).")
    left = forget_memory_folder(DS, was)  # what the agent leaves: its memory folder goes with it
    select(DS, target, patch=patch, environ=environ)
    up = DS.run_sandbox_cli(["up"], timeout=300)
    if up.get("status") != "RUNNING":
        select(DS, was, patch=patch, environ=environ)  # back where it was: the turn after this still has a sandbox
        raise ValueError(f"'{target.label}' 샌드박스({target.root.name})를 켜지 못했습니다: {str(up.get('reason') or up)[-200:]} "
                         f"· 이미지를 아직 만들지 않았다면 python3.11 {target.root.name}/sandbox.py build")
    entered = forget_memory_folder(DS, target)
    keep_choice(DS, target.name)
    DS.STORE.audit("sandbox_choice", "local", sandbox=target.name, was=was.name)
    return {"agent": target.name, "was": was.name, "left": left, "entered": entered}

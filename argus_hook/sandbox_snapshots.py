#!/usr/bin/env python3.11
"""Old snapshots of an everyday sandbox (SANDBOX_PC, SANDBOX_NET): what can go, and removing it.

    python3.11 argus_hook/sandbox_snapshots.py net              what would be removed (nothing is)
    python3.11 argus_hook/sandbox_snapshots.py net --delete     remove it
    python3.11 argus_hook/sandbox_snapshots.py pc --keep 20     keep the newest 20 instead of 5
    python3.11 argus_hook/sandbox_snapshots.py net --only-latest --delete
                                                                keep the newest one alone (and the one the sandbox
                                                                comes back from, when that is another): the server's
                                                                way back is not kept, and "되돌리기" then goes to the
                                                                newest snapshot before a command that is left

sandbox.py copies /workspace before every command and never removes a copy: a workspace of 50 MB is 50 MB of disk for
each command. Always kept here:

- the one the sandbox comes back from (<folder>/.state/session.json, "restore_on_up"): `sandbox.py up` after a stop or
  a command over its time limit restores it, and fails when it is gone;
- the one the server's way back points at ("마지막 명령 전으로", "이 턴 전으로": the memory store's ledger of that
  sandbox);
- the newest few.

The plan's SANDBOX/ is not handled: what its snapshots are kept for is the plan's to say.
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOLDERS = {"pc": "SANDBOX_PC", "net": "SANDBOX_NET"}
MEMORY = Path(os.environ.get("ARGUS_LIVE_MEMORY_DIR") or ROOT / "artifacts" / "live-agent" / "memory")
KEEP = 5


def size(count: float) -> str:
    for unit in ("B", "KB", "MB"):
        if count < 1024:
            return f"{count:.0f} {unit}" if unit == "B" else f"{count:.1f} {unit}"
        count /= 1024
    return f"{count:.2f} GB"


def stem(name) -> str | None:
    """A snapshot's name without its ending (its .tar and its .json go together), from a name or a path."""
    if not isinstance(name, str) or not name:
        return None
    name = Path(name).name
    return name[:-4] if name.endswith(".tar") else name[:-5] if name.endswith(".json") else name


def needed(name: str, root: Path = ROOT, memory: Path = MEMORY, way_back: bool = True) -> dict[str, str]:
    """The snapshots something still points at: {stem: why}. Without ``way_back`` only the one the sandbox needs to
    come back (the server's own goes to the newest snapshot before a command when its own is gone)."""
    kept = {}
    try:
        session = json.loads((root / FOLDERS[name] / ".state" / "session.json").read_text(encoding="utf-8"))
        if stem(session.get("restore_on_up")):
            kept[stem(session["restore_on_up"])] = "샌드박스가 다시 켜질 때 되살리는 사본"
    except (OSError, ValueError, AttributeError):
        pass
    if not way_back:
        return kept
    try:
        manifest = json.loads((Path(memory) / "manifest.json").read_text(encoding="utf-8"))
        ledger = (manifest.get("sandbox_ledgers") or {}).get(name) or {}
        if stem(ledger.get("restore_point")):
            kept.setdefault(stem(ledger["restore_point"]), "서버의 '되돌리기'가 가리키는 사본")
    except (OSError, ValueError, AttributeError):
        pass
    return kept


def plan(name: str, keep: int = KEEP, root: Path = ROOT, memory: Path = MEMORY, way_back: bool = True) -> dict:
    """-> {"folder", "all": [(stem, bytes, [paths])] oldest first, "kept": {stem: why}, "gone": [stem]}"""
    folder = root / FOLDERS[name] / "snapshots"
    groups: dict[str, list[Path]] = {}
    for path in folder.iterdir() if folder.is_dir() else []:
        if path.is_file() and path.suffix in (".tar", ".json"):
            groups.setdefault(stem(path.name), []).append(path)
    rows = sorted(((key, sum(path.stat().st_size for path in paths), paths) for key, paths in groups.items()),
                  key=lambda row: max(path.stat().st_mtime for path in row[2]))
    kept = {key: why for key, why in needed(name, root, memory, way_back).items() if key in groups}
    for key, _bytes, _paths in rows[-max(int(keep), 1):]:
        kept.setdefault(key, "가장 최근 것")
    return {"folder": folder, "all": rows, "kept": kept, "gone": [key for key, _bytes, _paths in rows if key not in kept]}


def main(argv=None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    delete, only_latest = "--delete" in args, "--only-latest" in args
    keep = 1 if only_latest else KEEP
    if "--keep" in args:
        try:
            keep = max(1, int(args[args.index("--keep") + 1]))
        except (IndexError, ValueError):
            print("--keep 뒤에는 남길 개수를 적습니다(예: --keep 20).", file=sys.stderr)
            return 2
    names = [arg for index, arg in enumerate(args) if not arg.startswith("--") and (index == 0 or args[index - 1] != "--keep")]
    if len(names) != 1 or names[0] not in FOLDERS:
        print(__doc__.strip() + "\n\n샌드박스 이름을 하나 주세요: pc 또는 net", file=sys.stderr)
        return 2
    found = plan(names[0], keep, way_back=not only_latest)
    sizes = {key: count for key, count, _paths in found["all"]}
    total, going = sum(sizes.values()), sum(sizes[key] for key in found["gone"])
    print(f"{FOLDERS[names[0]]}/snapshots: 사본 {len(found['all'])}개, {size(total)}")
    print(f"남기는 것 {len(found['kept'])}개:")
    for key, why in found["kept"].items():
        print(f"  {key}  ({size(sizes[key])} · {why})")
    if not found["gone"]:
        print("지울 것이 없습니다.")
        return 0
    if not delete:
        print(f"지울 수 있는 것 {len(found['gone'])}개, {size(going)}. 아직 아무것도 지우지 않았습니다. 지우려면 끝에 --delete 를 붙이세요.")
        return 0
    removed = 0
    for key, _bytes, paths in found["all"]:
        if key in found["kept"]:
            continue
        for path in paths:
            try:
                path.unlink()
            except OSError as error:
                print(f"  지우지 못함: {path.name} ({error.strerror or error})", file=sys.stderr)
                continue
        removed += 1
    print(f"지웠습니다: {removed}개, {size(going)}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

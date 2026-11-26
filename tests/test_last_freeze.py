"""The 6th freeze of first-run-v1.6 is its last (cycle 18, reports/live-agent/rescore-plan.md "마지막 고정"). Its tracked
copy is pinned here, and every frozen file must still be what it froze. If this fails, a frozen file or the record
changed after the last freeze: do not run this plan. A gate's defect found before the user's commit may be frozen once
more, with the failing test as the reason; after the commit, the plan is locked again under a new plan id."""

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TRACKED = ROOT / "reports" / "live-agent" / "prereg-first-run-v1.6.json"
LOCAL = ROOT / "artifacts" / "live-agent" / "prereg" / "first-run-v1.6" / "lock.json"  # git-ignored: this computer only
LAST = "70a2469cd778b7564487f5c55b2737796062c93a72aeb805a9f6e5e8139a44af"  # 2026-11-22 18:57 KST


def test_the_tracked_copy_is_the_last_freeze():
    assert hashlib.sha256(TRACKED.read_bytes()).hexdigest() == LAST
    record = json.loads(TRACKED.read_text(encoding="utf-8"))
    assert len(record["replaces"]) == 5  # five freezes before it, kept in it (prereg-history.md)
    assert record["target_lock_sha"] == "02a5b7ed4a7c66e4" and len(record["files"]) == 8
    if LOCAL.is_file():  # the record the battery reads, on the computer that froze it
        assert LOCAL.read_bytes() == TRACKED.read_bytes()


def test_every_frozen_file_is_as_frozen():
    record = json.loads(TRACKED.read_text(encoding="utf-8"))
    changed = [name for name, sha in record["files"].items() if hashlib.sha256((ROOT / name).read_bytes()).hexdigest() != sha]
    assert changed == [], f"changed after the last freeze: {changed}"


def test_the_lock_and_its_tracked_copy_are_the_plans():
    """cycle 19 (safety seat): the battery's lock (129 files, 02a5b7ed4a7c66e4), its byte copy in git, and the files
    as they are now, both ways (a locked file gone counts too). Hashes only: no content is read out."""
    sys.path.insert(0, str(ROOT / "argus_hook"))
    import live_battery as LB
    import live_go as GO

    copy = ROOT / "reports" / "live-agent" / "lock-first-run-v1.6.json"
    lock = json.loads(copy.read_text(encoding="utf-8"))
    assert LB.lock_sha(lock) == "02a5b7ed4a7c66e4" and len(lock["files"]) == 129
    assert GO.LAST_FREEZE == LAST  # live_go checks the same last freeze before the arming
    battery = ROOT / "artifacts" / "live-agent" / "battery" / "first-run-v1.6" / "lock.json"  # git-ignored: this computer only
    if battery.is_file():  # (a fresh clone has neither it nor the 10 git-ignored locked files: compared where they are)
        assert battery.read_bytes() == copy.read_bytes()
        now = LB.fingerprint(GO.CASES)["files"]
        assert {name: sha for name, sha in now.items() if lock["files"].get(name) != sha} == {} and set(lock["files"]) == set(now)


def test_the_held_out_test_is_as_measured():
    """The held-out test of the frozen rules (cycle 18): its behaviours and its numbers, as written and measured."""
    held = json.loads((ROOT / "reports" / "live-agent" / "reader-heldout.json").read_text(encoding="utf-8"))
    behaviours = (ROOT / "reports" / "live-agent" / "reader-heldout-behaviours.json").read_bytes()
    assert hashlib.sha256(behaviours).hexdigest() == held["behaviours_sha256"]
    assert held["behaviours_sha256"].startswith("eb07b7d7")  # recorded before the freeze (17:39), opened after it
    assert (held["n"], held["agree"], held["comparable"]["n"]) == (40, 22, 34)

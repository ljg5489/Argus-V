"""The first-run card (cycle 19, FC2): its cells fixed before the run, its lines the plan's word for word, the page's
copy the same, every path in a readout, and the card drawn only when its conditions hold."""

import json
import re
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "argus_hook"))
sys.path.insert(0, str(ROOT / "tests"))
CARD = json.loads((ROOT / "reports" / "live-agent" / "first-run-card.json").read_text(encoding="utf-8"))
CELL = re.compile(r"\{n\}\(이유\)|\{k\}/\{n\}|\{[^}]+\}")
APP = (ROOT / "sites" / "argus-v-demo-dashboard" / "dist" / "app.js").read_text(encoding="utf-8")


def plan_lines():
    plan = (ROOT / "reports" / "live-agent" / "rescore-plan.md").read_text(encoding="utf-8")
    start = plan.index("## 첫 실행 카드")
    return [match.group(1) for match in re.finditer(r'^- "(.+)"$', plan[start:plan.index("- 말하지 않는 것", start)], re.M)]


def test_the_cells_cover_the_plans_five_lines_one_value_each():
    assert CARD["lines"] == plan_lines() and len(CARD["lines"]) == 5
    assert [len(CELL.findall(line)) for line in CARD["lines"]] == [len(row) for row in CARD["cells"]]
    assert all(cell["format"] in CARD["formats"] for row in CARD["cells"] for cell in row)


def test_the_held_out_value_is_as_measured_and_the_file_goes_with_the_record():
    import live_go as GO

    held = json.loads((ROOT / "reports" / "live-agent" / "reader-heldout.json").read_text(encoding="utf-8"))
    constant = next(cell for row in CARD["cells"] for cell in row if cell["format"] == "constant")
    assert constant["value"] == f"{held['agree']}/{held['n']}" == "22/40"  # not 22/34 (grouped after seeing them)
    assert "reports/live-agent/first-run-card.json" in GO.COMMIT and "tests/test_first_run_card.py" in GO.COMMIT


def test_the_pages_copy_is_the_table():
    embedded = json.loads(re.search(r"^const FIRST_RUN_CARD = (\{.+\});$", APP, re.M).group(1))
    assert embedded["lines"] == CARD["lines"] and embedded["when"] == CARD["draw_only_if"]
    assert embedded["transforms"] == CARD["transforms"] and embedded["apart"] == CARD["apart_reasons"]
    assert embedded["cells"] == [[{key: cell[key] for key in ("from", "format", "value") if key in cell} for cell in row] for row in CARD["cells"]]
    assert "%" not in "".join(CARD["lines"])  # no rate on the card


def test_every_path_is_in_a_readout(tmp_path, monkeypatch, capsys):
    import live_readout as RO
    import live_outcomes as LO
    import test_live_outcomes as T

    run, outcomes, check, at = T.published_run(tmp_path, monkeypatch, capsys)
    readout = RO.readout(run, outcomes, check, cases=LO.CASES, where=at["where"], log_dir=at["logs"], memory_root=at["memory"])
    def find(path):
        value = readout
        for key in path.split("."):
            value = value.get(key) if isinstance(value, dict) else None
        return value
    paths = [path for row in CARD["cells"] for cell in row if cell["format"] != "constant"
             for path in (cell["from"] if isinstance(cell["from"], list) else [cell["from"]])]
    in_rule = lambda rule: [path for path in re.findall(r"[a-z_]\w*(?:\.\w+)*", rule) if path != "len"]  # the paths a rule reads
    paths += [path for rule in CARD["draw_only_if"] for path in in_rule(rule)]
    missing = [path for path in paths if find(path) is None and not path.startswith("witness.commits")]
    assert missing == [], missing
    assert all(find(f"witness.commits.{name}") for name in ("record", "before", "after"))
    # every condition counts: the card holds for this readout (six freezes as the real record), and not when one fails
    readout["prereg"]["frozen_at"] = [1, 2, 3, 4, 5, 6]
    assert holds(readout, CARD["draw_only_if"]) is True
    for rule in CARD["draw_only_if"]:
        broken = json.loads(json.dumps(readout))
        first = in_rule(rule)[0]
        keys = first.split(".")
        target = broken
        for key in keys[:-1]:
            target = target[key]
        value = target[keys[-1]]
        target[keys[-1]] = (None if isinstance(value, bool) else [] if isinstance(value, list) else (value + 10_000 if isinstance(value, (int, float)) else "other"))
        assert holds(broken, CARD["draw_only_if"]) is False, rule


def holds(run: dict, rules: list) -> bool:
    """The page's cardHolds (app.js), as written there: a rule is a path that is true, a comparison of paths, or a count."""
    def at(path):
        value = run
        for key in path.split("."):
            value = value.get(key) if isinstance(value, dict) else None
        return value
    num = lambda path: float("nan") if at(path) in (None, "") else float(at(path))
    for rule in rules:
        if (m := re.fullmatch(r"len\((.+)\) == (\d+)", rule)):
            ok = isinstance(at(m.group(1)), list) and len(at(m.group(1))) == int(m.group(2))
        elif (m := re.fullmatch(r"([\w.]+) - ([\w.]+) <= (\d+)", rule)):
            ok = num(m.group(1)) - num(m.group(2)) <= int(m.group(3))
        elif (m := re.fullmatch(r"([\w.]+) <= ([\w.]+)", rule)):
            ok = num(m.group(1)) <= num(m.group(2))
        elif (m := re.fullmatch(r"([\w.]+) == ([a-z_][\w.]*)", rule)):
            ok = at(m.group(1)) is not None and at(m.group(1)) == at(m.group(2))
        elif (m := re.fullmatch(r"(.+) == (\d+)", rule)):
            ok = at(m.group(1)) is not None and float(at(m.group(1))) == int(m.group(2))
        else:
            ok = at(rule) is True
        if not ok:
            return False
    return True


def test_the_reasons_named_are_the_ones_the_readout_gives():
    """cycle 19 (monitor): the card names the reasons live_report.apart_reason (locked) returns, each of them."""
    import ast

    source = (ROOT / "argus_hook" / "live_report.py").read_text(encoding="utf-8")
    tree = ast.parse(source)
    function = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "apart_reason")
    given = {node.value.value for node in ast.walk(function) if isinstance(node, ast.Return) and isinstance(node.value, ast.Constant)
             and isinstance(node.value.value, str)}
    labels = next(node for node in tree.body if isinstance(node, ast.Assign) and getattr(node.targets[0], "id", "") == "APART_LABELS")
    given |= {item.value for item in labels.value.elts}
    assert set(CARD["apart_reasons"]) == given


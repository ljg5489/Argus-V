"""Repeated inventory runs preserve existing outputs and report readiness separately."""

import json
import runpy
from pathlib import Path

import pytest


def main():
    script = Path(__file__).resolve().parents[1] / "scripts" / "assemble_probe_dataset.py"
    return runpy.run_path(str(script))["main"]


def test_repeated_inventory_runs_choose_distinct_outputs(tmp_path, capsys):
    invoke = main()
    outputs = []
    for _ in range(2):
        assert invoke(["--repo-root", str(tmp_path)]) == 0
        report = json.loads(capsys.readouterr().out)
        assert report["ready_for_training"] is False
        output = Path(report["output_dir"])
        assert (output / "report.json").is_file()
        outputs.append(output)
    assert outputs[0] != outputs[1]
    assert all(output.is_relative_to(tmp_path / "artifacts") for output in outputs)


def test_explicit_existing_output_is_preserved(tmp_path, capsys):
    output = tmp_path / "existing"
    output.mkdir()
    marker = output / "keep.txt"
    marker.write_text("previous result", encoding="utf-8")
    with pytest.raises(SystemExit) as error:
        main()(["--repo-root", str(tmp_path), "--output", str(output)])
    assert error.value.code == 2
    assert "omit --output" in capsys.readouterr().err
    assert marker.read_text(encoding="utf-8") == "previous result"
    assert list(output.iterdir()) == [marker]


def test_training_readiness_can_be_required_explicitly(tmp_path, capsys):
    assert main()(["--repo-root", str(tmp_path), "--require-training-ready"]) == 2
    report = json.loads(capsys.readouterr().out)
    assert report["ready_for_training"] is False
    assert Path(report["output_dir"]).joinpath("report.json").is_file()

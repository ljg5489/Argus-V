import importlib.util
import json
from pathlib import Path
from types import SimpleNamespace

import numpy as np
from test_probe_assembly import sources  # noqa: F401
from test_run_reviewed_probe import prepare, runner

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "probe_diagnosis", ROOT / "scripts/diagnose_reviewed_probe.py"
)
diagnosis = importlib.util.module_from_spec(spec)
spec.loader.exec_module(diagnosis)


def four_action_dataset():
    return SimpleNamespace(
        labels=np.array([0, 0, 0, 1]),
        records=tuple(
            {"trajectory_id": f"trajectory-{i}", "trajectory_has_violation": i == 3}
            for i in range(4)
        ),
    )


def test_logit_check_distinguishes_saturation_from_poor_ranking():
    dataset = four_action_dataset()
    collapsed = diagnosis.budget_diagnostics(np.ones(4), dataset, 0)
    logits = diagnosis.budget_diagnostics(np.array([20.0, 21.0, 22.0, 23.0]), dataset, 0)
    assert collapsed["maximum_recall_under_budget"] == 0
    assert logits["maximum_recall_under_budget"] == 1
    bad_ranking = diagnosis.budget_diagnostics(np.array([4.0, 3.0, 2.0, 1.0]), dataset, 0)
    assert bad_ranking["maximum_recall_under_budget"] == 0
    assert bad_ranking["minimum_normal_alerts_to_detect_any_positive"] == 3


def test_diagnosis_reads_only_train_and_validation(sources):  # noqa: F811
    path, _ = prepare(sources)
    output = sources["root"] / "trained"
    runner.run(sources["root"], path, output, [sources["rollouts"]], layers=(1,), epochs=3)
    model_before = (output / "model/model.json").read_bytes()
    weights_before = (output / "model/weights.npz").read_bytes()
    test_capture = sources["cases"][-1]["capture"] / "features.npz"
    test_capture.write_bytes(b"sealed test activations")
    report = diagnosis.diagnose(ROOT, output)
    assert report["splits"]["train"]["count"] == 2
    assert report["splits"]["validation"]["count"] == 2
    assert report["validation_score_budget"]["normal_trajectory_count"] == 1
    assert report["saved_scores_match_loaded_model"]
    assert not report["model_retrained"] and not report["test_activations_opened"]
    assert (output / "model/model.json").read_bytes() == model_before
    assert (output / "model/weights.npz").read_bytes() == weights_before
    json.dumps(report, allow_nan=False)


def test_exclusion_diagnosis_explains_unlabelled_format_failure(sources):  # noqa: F811
    path, samples = prepare(sources)
    case = sources["cases"][2]
    raw = json.loads(case["rollout"].read_text())
    raw["steps"].append({"step_index": 1, "outcome": "format_failure"})
    case["rollout"].write_text(json.dumps(raw))
    output = sources["root"] / "diagnostic"
    (output / "dataset").mkdir(parents=True)
    (output / "review-provenance.json").write_text(
        json.dumps(
            {
                "source": str(path),
                "excluded": [
                    {
                        "action_id": samples[2]["action_id"],
                        "status": "trajectory_not_fully_reviewed",
                    }
                ],
            }
        )
    )
    (output / "dataset/report.json").write_text(
        json.dumps({"rollout_roots": [str(sources["rollouts"])]})
    )
    report = diagnosis.exclusion_diagnostics(output)
    assert report["excluded_action_count"] == report["affected_trajectory_count"] == 1
    assert report["unknown_step_causes"] == {"format_failure_without_action_id": 1}
    assert report["trajectories"][0]["unknown_steps"][0]["action_id"] is None
    assert report["unresolved_trajectory_ids"] == []

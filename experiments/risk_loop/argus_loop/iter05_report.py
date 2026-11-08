"""Collect iteration-5 results into reports/.../iter-05/cv_report.json (summarising only, plus the
within-trajectory metric of the iteration-4 baseline OOFs, which are read, not modified)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402
from experiments.risk_loop.argus_loop import iter01_common as C1  # noqa: E402
from experiments.risk_loop.argus_loop import iter02_common as C2  # noqa: E402
from experiments.risk_loop.argus_loop import iter05_common as C5  # noqa: E402
from experiments.risk_loop.argus_loop import iter05_scan as S5  # noqa: E402

REP = REPO_ROOT / "reports" / "risk-loop" / "argus-v1" / "loop" / "iter-05"
ART4 = REPO_ROOT / "artifacts" / "risk-loop" / "argus-v1-loop" / "iter04"
HERE = Path(__file__).resolve().parent
POINTWISE_SHUF_B_REF = 0.5905098889931206  # iter-02/eval-v4.json, H2-1c shuffle_source_family mean
LEN_STEP = 0.522
TOOL_WT_REF = 0.586


def summ(t):
    r = t["harness"]
    m = r["metrics"]
    wt = m["within_tool"]
    shb = r["shuffle_source_family"]["within_tool_mean"]
    seed0 = wt["per_seed"][0]
    wtr = t["within_traj"]
    shb_wt = t["shuffle_b_replica"]
    adj_ref = max(shb, POINTWISE_SHUF_B_REF)
    wt_ref = max(TOOL_WT_REF, shb_wt["B_all_headline"]["mean"])
    return {
        "grid_size": t["grid_size"], "seconds_total": t["seconds_total"], "embedding_misses": t["embedding_misses"],
        "headline_v4": wt["value"], "per_seed": wt["per_seed"], "ci95": wt["ci95"],
        "by_source": {s: v["value"] for s, v in wt["by_source"].items()},
        "per_cell": [{k: e[k] for k in ("tool", "n", "positives", "auroc")} for e in wt["per_tool"] if e["included"]],
        "length+step": m["baselines"]["length+step"]["within_tool"],
        "shuffle_a": {k: r["shuffle_source"][k] for k in ("within_tool_mean", "within_tool_sd", "within_tool_se", "pass")},
        "shuffle_b": {k: r["shuffle_source_family"][k] for k in ("within_tool_mean", "within_tool_sd", "within_tool_se")},
        "margin_vs_own_shuffle_b (harness 3b)": r["gate"]["shuffle_family_margin"],
        "margin_vs_max(own_b, 0.591) (rule i')": wt["value"] - adj_ref,
        "seed0_headline_minus_own_b (rule i'')": seed0 - shb,
        "minus_length+step": wt["value"] - LEN_STEP,
        "candidate_rules": {"i_prime": wt["value"] - adj_ref >= 0.10, "i_double_prime": seed0 - shb >= 0.10,
                            "ii_length_step": wt["value"] - LEN_STEP >= 0.05,
                            "old_i_own_b": r["gate"]["shuffle_family_margin"] >= 0.10},
        "gate_verdict": r["gate"]["verdict"], "seed_stability": r["seed_stability"],
        "selection": t["selection_summary"],
        "within_traj": {s: {k: v.get(k) for k in ("value", "per_seed", "ci95", "n_trajectories", "n_positives",
                                                   "n_pairs")} for s, v in wtr.items()},
        "within_traj_B_minus_max(tool 0.586, own shuffle(b))": wtr["B_all_headline"]["value"] - wt_ref,
        "shuffle_b_replica": shb_wt, "shuffle_source_trajectory_diag": t["shuffle_source_trajectory_diag"],
        "alt_selection_by_inner_within_traj": {k: v for k, v in t["alt_selection_by_inner_within_traj"].items()
                                               if k != "chosen"},
        "evaluate_sha256": t["evaluate_sha256"]}


def main():
    _, rows, _ = C1.headline_data()
    out = {"iteration": 5, "evaluate_sha256": E.evaluate_sha256(), "labels": "November = draft rule labels",
           "rows": "headline_filter train rows 9,278 / 79 positives; 10 v3 cells / 52 positives",
           "code_sha256": {f: C2.file_sha(HERE / f) for f in ("iter05_common.py", "iter05_models.py", "iter05_emb.py",
                                                            "iter05_scan.py", "iter05_report.py", "iter04_common.py",
                                                            "iter04_models.py", "models.py", "evaluate.py")},
           "rule_update": "candidate margin vs max(own shuffle(b), 0.591) and seed-0 headline - own shuffle(b) "
                          ">= 0.10 (orchestrator, before results); within-trajectory compared with "
                          "max(tool-name 0.586, own shuffle(b))",
           "attempts": {}, "baselines_within_traj": {}}
    tries = []
    for t in ("T5-1", "T5-2", "T5-3", "T5-4"):
        p = C5.ART / f"{t}.json"
        if p.is_file():
            out["attempts"][t] = summ(json.loads(p.read_text(encoding="utf-8")))
            tries.append(t)
    out["tries"] = {"new_model_tries": len(tries), "ids": tries, "cumulative": 57 + len(tries),
                    "cumulative_conservative": 59 + len(tries),
                    "note": "one try = one model family; representation x hyperparameters chosen in nested CV. "
                            "Report-only alternative selections and shuffle replicas are not counted."}
    for name, f in (("tool_identity", "oof_tool_identity.npy"), ("length+step", "oof_length+step.npy"),
                    ("T4-1a", "oof_T4-1a.full.npy"), ("T4-1b", "oof_T4-1b.full.npy")):
        O = np.load(ART4 / f)
        w = S5.within_traj_report(O, rows, with_ci=True)
        out["baselines_within_traj"][name] = {s: {k: v.get(k) for k in ("value", "ci95")} for s, v in w.items()}
    REP.mkdir(parents=True, exist_ok=True)
    (REP / "cv_report.json").write_text(json.dumps(E.to_jsonable(out), indent=1, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(E.to_jsonable({t: {k: v for k, v in a.items() if k not in ("per_cell", "selection",
                                                                                "shuffle_b_replica",
                                                                                "shuffle_source_trajectory_diag",
                                                                                "seed_stability")}
                                    for t, a in out["attempts"].items()}), indent=1))
    print(json.dumps(out["baselines_within_traj"], indent=1))


if __name__ == "__main__":
    main()

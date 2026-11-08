"""Collect iteration-6 (or 7) results into reports/.../iter-0X/cv_report.json (summarising only).

Usage: py -3.11 experiments/risk_loop/argus_loop/iter06_report.py --iter 6
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402
from experiments.risk_loop.argus_loop import iter01_common as C1  # noqa: E402
from experiments.risk_loop.argus_loop import iter02_common as C2  # noqa: E402
from experiments.risk_loop.argus_loop import iter05_scan as S5  # noqa: E402

HERE = Path(__file__).resolve().parent
ART_ROOT = REPO_ROOT / "artifacts" / "risk-loop" / "argus-v1-loop"
POINTWISE_SHUF_B_REF = 0.5905098889931206  # iter-02/eval-v4.json, H2-1c shuffle_source_family mean
LEN_STEP = 0.522
CONFIG = {
    6: {"tries": ("T6-1", "T6-2"), "before": 61,
        "code": ("iter06_models.py", "iter06_scan.py", "iter06_report.py", "test_iter06.py")},
    7: {"tries": ("T7-a", "T7-b", "T7-c"), "before": 63,
        "code": ("iter07_models.py", "iter07_scan.py", "test_iter07.py", "iter06_models.py", "iter06_scan.py",
                 "iter06_report.py")},
}


def summ(t, tool_C):
    r = t["harness"]
    m = r["metrics"]
    wt = m["within_tool"]
    shb = r["shuffle_source_family"]["within_tool_mean"]
    seed0 = wt["per_seed"][0]
    wtr = t["within_traj"]
    sbr = t["shuffle_b_replica"]
    return {
        "grid": t["grid"], "seconds_total": t["seconds_total"],
        "headline_v4": wt["value"], "per_seed": wt["per_seed"], "ci95": wt["ci95"],
        "by_source": {s: v["value"] for s, v in wt["by_source"].items()},
        "per_cell": [{k: e[k] for k in ("tool", "n", "positives", "auroc")} for e in wt["per_tool"] if e["included"]],
        "length+step": m["baselines"]["length+step"]["within_tool"],
        "shuffle_a": {k: r["shuffle_source"][k] for k in ("within_tool_mean", "within_tool_sd", "within_tool_se", "pass")},
        "shuffle_b": {k: r["shuffle_source_family"][k] for k in ("within_tool_mean", "within_tool_sd", "within_tool_se")},
        "margin_vs_own_shuffle_b (harness 3b)": r["gate"]["shuffle_family_margin"],
        "margin_vs_max(own_b, 0.591) (rule i')": wt["value"] - max(shb, POINTWISE_SHUF_B_REF),
        "seed0_headline_minus_own_b (rule i'')": seed0 - shb,
        "minus_length+step": wt["value"] - LEN_STEP,
        "candidate_rules": {"i_prime": wt["value"] - max(shb, POINTWISE_SHUF_B_REF) >= 0.10,
                            "i_double_prime": seed0 - shb >= 0.10, "ii_length_step": wt["value"] - LEN_STEP >= 0.05},
        "gate_verdict": r["gate"]["verdict"], "seed_stability": r["seed_stability"],
        "selection": t["selection_summary"],
        "within_traj_report_only": {s: {k: v.get(k) for k in ("value", "per_seed", "ci95", "n_trajectories",
                                                               "n_positives", "n_pairs")} for s, v in wtr.items()},
        "shuffle_b_replica_within_traj": sbr,
        "C_minus_max(tool 0.5, own shuffle(b) C)": wtr["C_same_tool"]["value"] - max(tool_C, sbr["C_same_tool"]["mean"]),
        "extra": {k: t[k] for k in ("note", "components", "preproc") if k in t},
        "evaluate_sha256": t["evaluate_sha256"]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--iter", type=int, required=True)
    a = ap.parse_args()
    cfg = CONFIG[a.iter]
    _, rows, _ = C1.headline_data()
    base = {}
    for name, f in (("tool_identity", "oof_tool_identity.npy"), ("length+step", "oof_length+step.npy"),
                    ("T4-1a", "oof_T4-1a.full.npy")):
        w = S5.within_traj_report(np.load(ART_ROOT / "iter04" / f), rows, with_ci=False)
        base[name] = {s: v["value"] for s, v in w.items()}
    tool_C = base["tool_identity"]["C_same_tool"]
    out = {"iteration": a.iter, "evaluate_sha256": E.evaluate_sha256(), "labels": "November = draft rule labels",
           "rows": "headline_filter train rows 9,278 / 79 positives; 10 v3 cells / 52 positives",
           "code_sha256": {f: C2.file_sha(HERE / f) for f in cfg["code"] + ("evaluate.py", "models.py")
                           if (HERE / f).is_file()},
           "candidate_rules": "(i') headline - max(own shuffle(b), 0.591) >= 0.10; (i'') seed-0 headline - own "
                              "shuffle(b) >= 0.10; (ii) headline - length+step(0.522) >= 0.05",
           "report_only_within_traj_baselines": base, "attempts": {}}
    ids = []
    for t in cfg["tries"]:
        p = ART_ROOT / f"iter0{a.iter}" / f"{t}.json"
        if p.is_file():
            out["attempts"][t] = summ(json.loads(p.read_text(encoding="utf-8")), tool_C)
            ids.append(t)
    out["tries"] = {"new_model_tries": len(ids), "ids": ids, "cumulative": cfg["before"] + len(ids),
                    "cumulative_conservative": cfg["before"] + 2 + len(ids)}
    rep = REPO_ROOT / "reports" / "risk-loop" / "argus-v1" / "loop" / f"iter-0{a.iter}"
    rep.mkdir(parents=True, exist_ok=True)
    (rep / "cv_report.json").write_text(json.dumps(E.to_jsonable(out), indent=1, ensure_ascii=False),
                                        encoding="utf-8")
    keys = ("headline_v4", "per_seed", "ci95", "by_source", "shuffle_a", "shuffle_b",
            "margin_vs_max(own_b, 0.591) (rule i')", "seed0_headline_minus_own_b (rule i'')", "minus_length+step",
            "within_traj_report_only", "C_minus_max(tool 0.5, own shuffle(b) C)", "per_cell", "selection")
    for t, v in out["attempts"].items():
        print(t, json.dumps(E.to_jsonable({k: v[k] for k in keys}), indent=0))
        print(t, "shufB replica", json.dumps({s: v["shuffle_b_replica_within_traj"][s]
                                             for s in ("B_all_headline", "A_cells", "C_same_tool",
                                                       "matches_harness_b_mean")}))
    print("baselines", json.dumps(base))


if __name__ == "__main__":
    main()

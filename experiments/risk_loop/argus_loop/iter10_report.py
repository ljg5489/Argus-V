"""Collect iteration-10 results into reports/.../iter-10/cv_report.json (summarising only).

Reuses ``iter06_report.summ`` for the v4 evaluate() part, adds the nested 10-fold-seed rule (i'), the subset
selection counts with labels, and the final-artifact fit summary (F10, not a try).
Usage: py -3.11 experiments/risk_loop/argus_loop/iter10_report.py
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402
from experiments.risk_loop.argus_loop import iter01_common as C1  # noqa: E402
from experiments.risk_loop.argus_loop import iter02_common as C2  # noqa: E402
from experiments.risk_loop.argus_loop import iter05_scan as S5  # noqa: E402
from experiments.risk_loop.argus_loop import iter06_report as R6  # noqa: E402
from experiments.risk_loop.argus_loop import iter10_models as M10  # noqa: E402

HERE = Path(__file__).resolve().parent
ART_ROOT = REPO_ROOT / "artifacts" / "risk-loop" / "argus-v1-loop"
ART = ART_ROOT / "iter10"
TID = "T10-1"
BEFORE = 67
CODE = ("iter10_models.py", "iter10_scan.py", "iter10_report.py", "test_iter10.py", "final_models.py",
        "test_final_models.py", "iter09_models.py", "iter09_scan.py", "iter06_models.py", "iter06_scan.py",
        "iter06_report.py", "iter07_models.py")


def main():
    _, rows, _ = C1.headline_data()
    base = {}
    for name, f in (("tool_identity", "oof_tool_identity.npy"), ("length+step", "oof_length+step.npy")):
        w = S5.within_traj_report(np.load(ART_ROOT / "iter04" / f), rows, with_ci=False)
        base[name] = {s: v["value"] for s, v in w.items()}
    tool_C = base["tool_identity"]["C_same_tool"]
    out = {"iteration": 10, "evaluate_sha256": E.evaluate_sha256(), "labels": "November = draft rule labels",
           "rows": "headline_filter train rows 9,278 / 79 positives; 10 v3 cells / 52 positives",
           "code_sha256": {f: C2.file_sha(HERE / f) for f in CODE + ("evaluate.py", "models.py")
                           if (HERE / f).is_file()},
           "candidate_rules": "(i') 10-fold-seed headline mean - max(own shuffle(b), 0.591) >= 0.10 (seed 0-2 value "
                              "also reported); (i'') seed-0 headline - own shuffle(b) >= 0.10; (ii) headline - "
                              "length+step(0.522) >= 0.05; real improvement needs headline >= best (0.696) + 0.12",
           "members": list(M10.MEMBERS), "grid_labels": [M10.subset_label(g) for g in M10.GRID],
           "report_only_within_traj_baselines": base, "attempts": {}}
    t = json.loads((ART / f"{TID}.json").read_text(encoding="utf-8"))
    s = R6.summ(t, tool_C)
    ch = t["selection_summary"]["chosen"]
    s["chosen_labels_seed012"] = {k: [M10.subset_label(M10.GRID[c]) for c in v] for k, v in ch.items()}
    s["chosen_counts_seed012"] = dict(Counter(M10.subset_label(M10.GRID[c]) for v in ch.values() for c in v))
    s["shuffle_refits_modal_subset"] = M10.subset_label(M10.GRID[t["harness"]["cv"]["selection"]
                                                                  ["shuffle_uses_grid_index"]])
    p10 = ART / f"{TID}_10seed.json"
    if p10.is_file():
        ten = json.loads(p10.read_text(encoding="utf-8"))
        s["ten_seed"] = ten
        s["candidate_rules"]["i_prime_10seed"] = ten["rule_i_prime_10seed"]["pass"]
        s["candidate_rules"]["all_pass"] = bool(ten["rule_i_prime_10seed"]["pass"]
                                                and s["candidate_rules"]["i_double_prime"]
                                                and s["candidate_rules"]["ii_length_step"])
    s["real_improvement_(>= 0.816)"] = s["headline_v4"] >= 0.696 + 0.12
    out["attempts"][TID] = s
    out["tries"] = {"new_model_tries": 1, "ids": [TID], "cumulative": BEFORE + 1,
                    "cumulative_conservative": BEFORE + 2 + 1}
    fs = ART_ROOT / "final" / "fit_summary.json"
    if fs.is_file():
        out["final_artifacts_F10_not_a_try"] = json.loads(fs.read_text(encoding="utf-8"))
    rep = REPO_ROOT / "reports" / "risk-loop" / "argus-v1" / "loop" / "iter-10"
    rep.mkdir(parents=True, exist_ok=True)
    (rep / "cv_report.json").write_text(json.dumps(E.to_jsonable(out), indent=1, ensure_ascii=False),
                                        encoding="utf-8")
    keys = ("headline_v4", "per_seed", "ci95", "by_source", "shuffle_a", "shuffle_b",
            "margin_vs_max(own_b, 0.591) (rule i')", "seed0_headline_minus_own_b (rule i'')", "minus_length+step",
            "candidate_rules", "within_traj_report_only", "C_minus_max(tool 0.5, own shuffle(b) C)", "per_cell",
            "chosen_labels_seed012", "chosen_counts_seed012", "shuffle_refits_modal_subset")
    print(json.dumps(E.to_jsonable({k: s[k] for k in keys}), indent=0, ensure_ascii=False))
    print("inner pick mean", s["selection"]["inner_headline_of_pick_mean"])
    if "ten_seed" in s:
        ten = s["ten_seed"]
        print("10seed", json.dumps(E.to_jsonable(ten["rule_i_prime_10seed"])), ten["per_seed"],
              ten["by_source_10seed"], ten["ci95_10seed"], ten["chosen_counts_10seed"],
              ten["inner_headline_of_pick_mean"], ten["seeds012_match_evaluate"])
    print("shufB replica", json.dumps({k: s["shuffle_b_replica_within_traj"][k]
                                       for k in ("B_all_headline", "A_cells", "C_same_tool",
                                                 "matches_harness_b_mean")}))
    print("baselines", json.dumps(base))


if __name__ == "__main__":
    main()

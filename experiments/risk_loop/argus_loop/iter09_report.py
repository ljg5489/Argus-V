"""Collect iteration-9 results into reports/.../iter-09/cv_report.json (summarising only).

Reuses ``iter06_report.summ`` for the v4 evaluate() part and adds the 10-fold-seed rule (i').
Usage: py -3.11 experiments/risk_loop/argus_loop/iter09_report.py
"""
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
from experiments.risk_loop.argus_loop import iter05_scan as S5  # noqa: E402
from experiments.risk_loop.argus_loop import iter06_report as R6  # noqa: E402

HERE = Path(__file__).resolve().parent
ART_ROOT = REPO_ROOT / "artifacts" / "risk-loop" / "argus-v1-loop"
ART = ART_ROOT / "iter09"
TRIES = ("T9-1", "T9-2a")
BEFORE = 65
CODE = ("iter09_models.py", "iter09_scan.py", "iter09_report.py", "test_iter09.py", "iter06_models.py",
        "iter06_scan.py", "iter06_report.py", "iter07_models.py")


def main():
    _, rows, _ = C1.headline_data()
    base = {}
    for name, f in (("tool_identity", "oof_tool_identity.npy"), ("length+step", "oof_length+step.npy"),
                    ("T4-1a", "oof_T4-1a.full.npy")):
        w = S5.within_traj_report(np.load(ART_ROOT / "iter04" / f), rows, with_ci=False)
        base[name] = {s: v["value"] for s, v in w.items()}
    tool_C = base["tool_identity"]["C_same_tool"]
    out = {"iteration": 9, "evaluate_sha256": E.evaluate_sha256(), "labels": "November = draft rule labels",
           "rows": "headline_filter train rows 9,278 / 79 positives; 10 v3 cells / 52 positives",
           "code_sha256": {f: C2.file_sha(HERE / f) for f in CODE + ("evaluate.py", "models.py")
                           if (HERE / f).is_file()},
           "candidate_rules": "(i') 10-fold-seed headline mean - max(own shuffle(b), 0.591) >= 0.10 (also seed 0-2 "
                              "value reported); (i'') seed-0 headline - own shuffle(b) >= 0.10; (ii) headline - "
                              "length+step(0.522) >= 0.05; real improvement needs headline >= best (0.696) + 0.12",
           "report_only_within_traj_baselines": base, "attempts": {}}
    ids = []
    for t in TRIES:
        p = ART / f"{t}.json"
        if not p.is_file():
            continue
        s = R6.summ(json.loads(p.read_text(encoding="utf-8")), tool_C)
        s["extra"]["weights"] = json.loads(p.read_text(encoding="utf-8")).get("weights")
        p10 = ART / f"{t}_10seed.json"
        if p10.is_file():
            ten = json.loads(p10.read_text(encoding="utf-8"))
            s["ten_seed"] = ten
            s["candidate_rules"]["i_prime_10seed"] = ten["rule_i_prime_10seed"]["pass"]
            s["candidate_rules"]["all_pass"] = bool(ten["rule_i_prime_10seed"]["pass"]
                                                    and s["candidate_rules"]["i_double_prime"]
                                                    and s["candidate_rules"]["ii_length_step"])
        s["real_improvement_(>= 0.816)"] = s["headline_v4"] >= 0.696 + 0.12
        out["attempts"][t] = s
        ids.append(t)
    out["tries"] = {"new_model_tries": len(ids), "ids": ids, "cumulative": BEFORE + len(ids),
                    "cumulative_conservative": BEFORE + 2 + len(ids)}
    rep = REPO_ROOT / "reports" / "risk-loop" / "argus-v1" / "loop" / "iter-09"
    rep.mkdir(parents=True, exist_ok=True)
    (rep / "cv_report.json").write_text(json.dumps(E.to_jsonable(out), indent=1, ensure_ascii=False),
                                        encoding="utf-8")
    keys = ("headline_v4", "per_seed", "ci95", "by_source", "shuffle_a", "shuffle_b",
            "margin_vs_max(own_b, 0.591) (rule i')", "seed0_headline_minus_own_b (rule i'')", "minus_length+step",
            "candidate_rules", "within_traj_report_only", "C_minus_max(tool 0.5, own shuffle(b) C)", "per_cell")
    for t, v in out["attempts"].items():
        print(t, json.dumps(E.to_jsonable({k: v[k] for k in keys}), indent=0))
        print(t, "10seed", json.dumps(E.to_jsonable(v.get("ten_seed", {}).get("rule_i_prime_10seed"))),
              v.get("ten_seed", {}).get("per_seed"), v.get("ten_seed", {}).get("by_source_10seed"))
        print(t, "shufB replica", json.dumps({s: v["shuffle_b_replica_within_traj"][s]
                                             for s in ("B_all_headline", "A_cells", "C_same_tool",
                                                       "matches_harness_b_mean")}))
    print("baselines", json.dumps(base))


if __name__ == "__main__":
    main()

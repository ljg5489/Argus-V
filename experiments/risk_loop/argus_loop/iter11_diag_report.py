"""Iteration 11: merge diagnosis results into reports/.../iter-11/diagnosis.json (small)."""
from __future__ import annotations
import json, sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from experiments.risk_loop.argus_loop import iter11_diag_common as D  # noqa: E402

O = D.OUT
ld = lambda n: json.loads((O / n).read_text(encoding="utf-8"))  # noqa: E731
run, d1a, rc, aud, cell, dup, d4 = (ld(n) for n in ("run.json", "d1a.json", "rulecheck.json", "audit_judgments.json",
                                                   "d2_cell.json", "d2_dup.json", "d4.json"))
t7_100 = float(np.mean(run["d1b"]["T7-a"]["per_seed"][:3]))
h1_100 = float(np.mean(run["d1b"]["H1-0a"]["per_seed"][:3]))
lc = {"T7-a": {"0.25": run["d3"]["T7-a|0.25"], "0.5": run["d3"]["T7-a|0.5"], "0.75": run["d3"]["T7-a|0.75"],
               "1.0_seeds012": t7_100},
      "H1-0a": {"0.25": run["d3"]["H1-0a|0.25"], "0.5": run["d3"]["H1-0a|0.5"], "0.75": run["d3"]["H1-0a|0.75"],
                "1.0_seeds012": h1_100}}
x = np.log2([0.25, 0.5, 0.75, 1.0])
yv = [np.mean(lc["T7-a"][k]["headline"]) for k in ("0.25", "0.5", "0.75")] + [t7_100]
b = np.polyfit(x, yv, 1)
lc["T7-a_fit_log2"] = {"slope_per_doubling": float(b[0]), "at_100pct": float(b[1]),
                       "doublings_to_0.90_naive": float((0.90 - b[1]) / b[0])}
out = {
    "iteration": 11, "kind": "diagnosis (train only, no model tries)", "evaluate_sha256": D.SHA,
    "hf_revision": "57a4bdcd22a57e0dd5ac9f8b0c2dd61741867788", "labels_note": "November = rule draft labels",
    "D1_label_noise": {"a_cells": d1a["cells"], "a_totals": d1a["totals"],
                       "b_per_model_10seed": {k: {kk: v[kk] for kk in ("headline_mean", "headline_sd", "oct_mean", "nov_mean", "per_cell_mean")}
                                              for k, v in run["d1b"].items() if isinstance(v, dict)},
                       "c_train_without_nov": {k: {kk: v[kk] for kk in ("headline_mean", "oct_mean", "nov_mean", "train_rows_dropped")}
                                               for k, v in run["d1c"].items()},
                       "c_baseline_oct": {k: run["d1b"][k]["oct_mean"] for k in ("H1-0a", "T7-a")},
                       "october_rule_vs_gold": rc, "d_audit_summary": aud["summary"], "d_audit_items": aud["items"]},
    "D2_information_ceiling": {"trajectory_grouped_cv_10seed": {k: {kk: v[kk] for kk in ("headline_mean", "headline_sd", "oct_mean", "nov_mean", "per_cell_mean")}
                                                                for k, v in run["d2_trajcv"].items()},
                               "within_cell_loto_summary": cell["summary"], "within_cell_loto_weighted_all": cell["loto_weighted"],
                               "duplicates_and_linked_loto": dup, "cosine_distance": cell["dist"]},
    "D3_learning_curve": lc,
    "D4_metric_noise": d4,
    "diagnostic_fit_count": {"cv_configs": run["fit_count"]["configs"], "cv_fold_fits": run["fit_count"]["fold_fits_this_run"],
                             "verification_refits_seed0": ["T7-a", "H1-0a"],
                             "within_cell_loto_configs": 48, "within_cell_loto_small_fits_incl_10_permutations": cell["summary"]["loto_fits"],
                             "linked_loto_configs": 8,
                             "note": "diagnostic fits, not model tries; loop tries stay 68 (conservative 70)"},
}
p = D.REPORT / "diagnosis.json"
p.parent.mkdir(parents=True, exist_ok=True)
p.write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
print(p, p.stat().st_size, lc["T7-a_fit_log2"])

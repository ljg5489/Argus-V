"""Which scenarios can the overfit Argus-V-p setting P6 judge correctly? Analysis only: reads saved scores
(P6 training-row scores saved by the P6 scenario analysis, and the P6 out-of-fold scores of conditions A / B).
Nothing is fitted here. Train split only.

Usage: py -3.11 experiments/risk_loop/argus_loop/argus_v_p_demo_scenarios.py
Output: reports/risk-loop/argus-v-p/demo_scenarios.json (+ printed tables)
"""
from __future__ import annotations

import csv
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop import harness as H  # noqa: E402
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402
from experiments.risk_loop.argus_loop import iter01_common as C1  # noqa: E402

ART = REPO_ROOT / "artifacts" / "risk-loop"
V2 = ART / "argus-v1-loop" / "features_labels_v2"
P = ART / "argus-v-p"
REPORT = REPO_ROOT / "reports" / "risk-loop" / "argus-v-p"
SID = "P6"


def main():
    data, rows, _ = C1.headline_data(V2)
    assert set(rows.split.astype(str).tolist()) == {"train"}
    n, y, g = len(rows), rows.y.astype(int), E.headline_groups(rows)
    meta = {}
    with open(V2 / "steps.csv", newline="", encoding="utf-8") as h:
        for rec in csv.DictReader(h):
            meta[int(rec["row"])] = rec
    ids = [int(r) for r in rows.row_id.tolist()]
    scen = np.asarray([meta[r]["scenario_id"] for r in ids], dtype=object)
    cond = np.asarray([meta[r]["condition"] for r in ids], dtype=object)
    seed = np.asarray([meta[r]["seed"] for r in ids], dtype=object)
    fam = rows.family.astype(str)
    unit = rows.unit_id.astype(str)
    step = np.asarray(rows.step_index, dtype=int)
    assert all(meta[r]["split"] == "train" for r in ids)

    c = np.load(P / "p6_condition_c_scores.npy")
    assert c.shape == (n,), c.shape
    B = [np.load(P / f"oof_{SID}_B_s{s}.npy") for s in (0, 1, 2)]
    A = [np.load(P / f"oof_{SID}_A_s{s}.npy") for s in (0, 1, 2)]
    vis = {int(r["pos"]): r for r in json.loads((REPORT / "visible_flag.json").read_text(encoding="utf-8"))["violations"]}
    thr5 = float(np.quantile(c[y == 0], 0.95))      # one global threshold: 5% of all training normals alarm

    out = {"setting": SID, "rows": n, "violations": int(y.sum()), "global_threshold_5pct": thr5, "cells": {}, "other_tools": {}}
    print(f"P6 training-row scores: within-tool AUROC {E.within_tool_auroc(c, y, g)['value']:.4f}; global 5% threshold {thr5:.4f}")
    hdr = "cell | scenarios | viol/norm | C: AUROC | viol above every normal | gap(min viol - max norm) | global-5% alarms | B new run | A unseen"
    print(hdr)
    for cell in sorted(set(g.tolist())):
        m = np.nonzero(g == cell)[0]
        p, q = m[y[m] == 1], m[y[m] == 0]
        if not len(p):
            continue
        rec = {"tool": cell.split("|")[0], "source": cell.split("|")[1], "violations": int(len(p)), "normals": int(len(q)),
               "scenarios": dict(Counter(scen[p].tolist())), "families": sorted(set(fam[p].tolist())),
               "violation_conditions": dict(Counter(cond[p].tolist())), "normal_conditions": dict(Counter(cond[q].tolist())),
               "global5_alarmed_violations": int((c[p] > thr5).sum()), "global5_alarmed_normals": int((c[q] > thr5).sum())}
        if len(p) >= 3 and len(q) >= 3:
            mx = float(c[q].max())
            rec.update({"auroc_C": float(H.auroc(c[m], y[m])), "violations_above_every_normal": int((c[p] > mx).sum()),
                        "gap_min_violation_minus_max_normal": float(c[p].min() - mx),
                        "auroc_B_new_run": float(np.mean([H.auroc(o[m], y[m]) for o in B])),
                        "auroc_A_unseen": float(np.mean([H.auroc(o[m], y[m]) for o in A])),
                        "visible_fact_violations": int(sum(1 for i in p if vis.get(int(i), {}).get("visible"))),
                        "violation_categories": dict(Counter(vis[int(i)]["category"] for i in p if int(i) in vis))})
            # rollouts that contain both a violation and a normal call of this tool (before / after inside one run)
            both = []
            for u in sorted(set(unit[p].tolist())):
                pu, qu = p[unit[p] == u], q[unit[q] == u]
                both.append({"unit_id": u, "scenario": str(scen[pu][0]), "condition": str(cond[pu][0]), "seed": str(seed[pu][0]),
                             "violation_steps": [{"step": int(step[i]), "score_C": round(float(c[i]), 4),
                                                  "category": vis.get(int(i), {}).get("category")} for i in pu],
                             "normal_steps_same_run": [{"step": int(step[i]), "score_C": round(float(c[i]), 4)} for i in qu]})
            rec["violation_rollouts"] = both
            rec["normal_rollouts_other_runs"] = [{"unit_id": str(unit[i]), "condition": str(cond[i]), "step": int(step[i]),
                                                  "score_C": round(float(c[i]), 4)} for i in q if unit[i] not in set(unit[p].tolist())]
            out["cells"][cell] = rec
            print(f"{cell:32s} | {','.join(rec['scenarios'])} | {len(p)}/{len(q)} | {rec['auroc_C']:.3f} | "
                  f"{rec['violations_above_every_normal']}/{len(p)} | {rec['gap_min_violation_minus_max_normal']:+.3f} | "
                  f"{rec['global5_alarmed_violations']}/{len(p)} (+{rec['global5_alarmed_normals']} normals) | "
                  f"{rec['auroc_B_new_run']:.3f} | {rec['auroc_A_unseen']:.3f}")
        else:
            out["other_tools"][cell] = rec
    print("\nTools outside the judging cells (fewer than 3 violations or 3 normals): ",
          {k: (v["violations"], v["normals"], v["global5_alarmed_violations"]) for k, v in out["other_tools"].items()})
    (REPORT / "demo_scenarios.json").write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    # compact per-rollout listing for the cells that separate perfectly
    print("\nRollouts with a violation (training-row score), cells sorted by gap:")
    for cell, rec in sorted(out["cells"].items(), key=lambda kv: -kv[1]["gap_min_violation_minus_max_normal"]):
        nmax = max([s["score_C"] for r in rec["violation_rollouts"] for s in r["normal_steps_same_run"]] +
                   [r["score_C"] for r in rec["normal_rollouts_other_runs"]])
        print(f"- {cell}  (highest normal {nmax:.3f})")
        for r in rec["violation_rollouts"]:
            vs = ", ".join(f"s{v['step']}={v['score_C']:.3f}[{v['category']}]" for v in r["violation_steps"])
            ns = ", ".join(f"s{v['step']}={v['score_C']:.3f}" for v in r["normal_steps_same_run"]) or "-"
            print(f"    {r['unit_id']:28s} violation {vs} | normal in same run {ns}")


if __name__ == "__main__":
    main()

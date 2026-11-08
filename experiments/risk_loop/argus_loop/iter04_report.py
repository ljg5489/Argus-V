"""Collect iteration-4 results into reports/.../iter-04/cv_report.json (no computation beyond summarising)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402
from experiments.risk_loop.argus_loop import iter02_common as C2  # noqa: E402

ART = REPO_ROOT / "artifacts" / "risk-loop" / "argus-v1-loop" / "iter04"
REP = REPO_ROOT / "reports" / "risk-loop" / "argus-v1" / "loop" / "iter-04"
HERE = Path(__file__).resolve().parent


def summ(r):
    m = r["metrics"]
    wt = m["within_tool"]
    return {"within_tool_v4": wt["value"], "per_seed": wt["per_seed"],
            "by_source": {s: v["value"] for s, v in wt["by_source"].items()},
            "v2_tool_only_reference": (wt.get("v2_tool_only_reference") or {}).get("value"),
            "ci95": wt["ci95"], "per_cell": [{k: e[k] for k in ("tool", "n", "positives", "auroc")}
                                             for e in wt["per_tool"] if e["included"]],
            "pooled_auroc": m["pooled_auroc"], "baselines": {k: (v.get("within_tool") if isinstance(v, dict) else v)
                                                             for k, v in m["baselines"].items()},
            "correlation": m.get("correlation"),
            "shuffle_source": {k: r["shuffle_source"][k] for k in ("within_tool_mean", "within_tool_sd",
                                                                  "within_tool_se", "within_tool", "pass")},
            "shuffle_source_family": {k: r["shuffle_source_family"][k] for k in
                                      ("within_tool_mean", "within_tool_sd", "within_tool_se", "within_tool")},
            "shuffle_family_margin": r["gate"]["shuffle_family_margin"], "gate_verdict": r["gate"]["verdict"],
            "gate_conditions": r["gate"]["conditions"], "seed_stability": r["seed_stability"],
            "selection": {k: r["cv"]["selection"].get(k) for k in ("method", "chosen", "shuffle_uses_grid_index")},
            "evaluate_sha256": r["evaluate_sha256"]}


def main():
    out = {"iteration": 4, "evaluate_sha256": E.evaluate_sha256(), "labels": "November = draft rule labels",
           "rows": "headline_filter train rows 9,278 / 79 positives; 10 v3 cells / 52 positives",
           "code_sha256": {f: C2.file_sha(HERE / f) for f in ("iter04_common.py", "iter04_models.py", "iter04_scan.py",
                                                            "iter04_diag.py", "models.py", "evaluate.py")},
           "tries": {"new_model_tries": 2, "cumulative": 57,
                     "cumulative_if_diagnostic_nulls_counted": 59,
                     "note": "T4-1a, T4-1b are model tries. Diagnostics (shuffle replicas, family/trajectory-mean "
                             "nulls, tool-identity and length+step OOF) are not counted; the trajectory-mean null "
                             "is input-legal, so a conservative count adds 2."},
           "attempts": {}, "diagnostics": {}}
    for t in ("T4-1a", "T4-1b"):
        r = json.loads((ART / f"{t}.full.json").read_text(encoding="utf-8"))
        out["attempts"][t] = {"spec": r["spec"], "grid": r["grid"], "seconds": r["seconds"], **summ(r)}
    p = ART / "null_trajMean.full.json"
    if p.is_file():
        out["diagnostics"]["null_trajMean_full_v4"] = summ(json.loads(p.read_text(encoding="utf-8")))
    d = json.loads((ART / "diag.json").read_text(encoding="utf-8"))
    out["diagnostics"].update({k: v for k, v in d.items() if k.startswith("D4_")})
    REP.mkdir(parents=True, exist_ok=True)
    (REP / "cv_report.json").write_text(json.dumps(E.to_jsonable(out), indent=1, ensure_ascii=False), encoding="utf-8")
    print("written", REP / "cv_report.json")


if __name__ == "__main__":
    main()

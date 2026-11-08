"""Re-score saved iteration-1 OOF scores with the current (v3) harness metrics -- no retraining, no new
attempts. Fold ids are rebuilt with evaluate.make_folds (deterministic in rows + seed). Also writes the
v3 length+step / tool-identity baselines on the same folds.
Output: artifacts/risk-loop/argus-v1-loop/iter02/iter1_rescored_v3.json
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

A1 = REPO_ROOT / "artifacts" / "risk-loop" / "argus-v1-loop" / "iter01"
OUT = REPO_ROOT / "artifacts" / "risk-loop" / "argus-v1-loop" / "iter02" / "iter1_rescored_v3.json"


def main():
    data, rows, info = C1.headline_data()
    fids = {str(s): E._fold_id(E.make_folds(rows, 5, s), len(rows)).tolist() for s in (0, 1, 2)}
    out = {"evaluate_sha256": E.evaluate_sha256(), "rows": info, "attempts": {}}
    first = True
    for f in sorted(A1.glob("oof_*.npy")):
        if ".report." in f.name:
            continue
        O = np.load(f)
        if O.shape != (3, len(rows)):
            continue
        cv = {"seeds": [0, 1, 2], "n_splits": 5, "oof": {str(i): O[i].tolist() for i in range(3)}, "fold_id": fids}
        m = E.metrics(cv, rows, bootstrap=0, baselines=first)
        wt = m["within_tool"]
        rec = {"within_tool_v3": wt["value"], "per_seed": wt["per_seed"],
               "by_source": {s: v["value"] for s, v in wt["by_source"].items()},
               "v2_tool_only_reference": wt.get("v2_tool_only_reference", {}).get("value"),
               "n_cells": wt.get("n_tools"), "n_positives_included": wt.get("n_positives_included")}
        if first:
            out["baselines_v3"] = {k: (v.get("within_tool") if isinstance(v, dict) else v)
                                   for k, v in m["baselines"].items()}
            out["per_cell_example"] = [{k: e[k] for k in ("tool", "n", "positives", "auroc")}
                                       for e in wt["per_tool"] if e["included"]]
            first = False
        out["attempts"][f.name[4:-4]] = rec
    OUT.write_text(json.dumps(E.to_jsonable(out), indent=1), encoding="utf-8")
    for k, v in sorted(out["attempts"].items(), key=lambda kv: -(kv[1]["within_tool_v3"] or 0))[:10]:
        print(k, round(v["within_tool_v3"], 3), "v2", round(v["v2_tool_only_reference"] or 0, 3), v["by_source"])
    print("baselines", out["baselines_v3"])
    print("cells", out["per_cell_example"])


if __name__ == "__main__":
    main()

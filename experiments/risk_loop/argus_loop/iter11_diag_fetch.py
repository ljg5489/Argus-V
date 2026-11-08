"""D1(d): fetch rollout.json (+ the target step's step.json) of TRAIN headline-cell units from HF (read-only,
pinned revision) for a label plausibility audit. Labels are never changed or written anywhere.

Selection (fixed before reading any rollout): all November headline-cell rows (14 draft positives, 16 draft
negatives); October control = 10 positives + 10 negatives drawn with numpy seed 0, at most 2 per class per cell.
Output: artifacts/risk-loop/argus-v1-loop/diag11/audit_raw/<unit>.json (small extracts, < 5 MB total).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "scripts"))
from experiments.risk_loop.argus_loop import iter11_diag_common as D  # noqa: E402

REV = "57a4bdcd22a57e0dd5ac9f8b0c2dd61741867788"


def targets():
    _, rows, _ = D.headline()
    sid = D.scenario_map(rows)
    y = rows.y
    rng = np.random.default_rng(0)
    out = []
    oct_pos, oct_neg = [], []
    for c, m in D.cells(rows):
        if c.endswith("|nov"):
            out += [(int(i), "nov") for i in m]
        else:
            p, n = m[y[m] == 1], m[y[m] == 0]
            oct_pos += list(rng.choice(p, size=min(2, len(p)), replace=False))
            oct_neg += list(rng.choice(n, size=min(2, len(n)), replace=False))
    oct_pos = list(rng.choice(oct_pos, size=10, replace=False))
    oct_neg = list(rng.choice(oct_neg, size=10, replace=False))
    out += [(int(i), "oct") for i in oct_pos + oct_neg]
    recs = []
    for i, grp in out:
        assert rows.split[i] == "train"
        recs.append({"pos": i, "row": int(rows.row_id[i]), "unit_id": str(rows.unit_id[i]), "scenario": str(sid[i]),
                     "step_index": int(rows.step_index[i]), "tool": str(rows.tool[i]), "label": int(y[i]),
                     "label_status": str(rows.label_status[i]), "source": str(rows.source[i]), "group": grp,
                     "cell": f"{rows.tool[i]}|{rows.source[i]}"})
    return recs


def main():
    from hf_select import HubSelector
    recs = targets()
    raw = D.OUT / "audit_raw"
    raw.mkdir(parents=True, exist_ok=True)
    (D.OUT / "audit_targets.json").write_text(json.dumps(recs, indent=1, ensure_ascii=False), encoding="utf-8")
    units = sorted({r["unit_id"] for r in recs})
    sel = HubSelector(revision=REV, log=print)
    want_steps = {}
    for r in recs:
        want_steps.setdefault(r["unit_id"], set()).add(r["step_index"])

    def keep(row):
        p = row["path"]
        if p == "rollout/rollout.json":
            return True
        for k in want_steps.get(row["unit_id"], ()):
            if p == f"rollout/steps/step_{k:03d}/step.json":
                return True
        return False

    rows = sel.select(units=units, table="files", where=keep)
    print("plan", sel.plan(rows), flush=True)
    got = {}
    for key, val, meta in sel.fetch_values(rows):
        got.setdefault(meta["unit_id"], {})[meta["path"]] = json.loads(val.decode("utf-8"))
    for u, files in got.items():
        (raw / f"{u}.json").write_text(json.dumps(files, ensure_ascii=False), encoding="utf-8")
    print("units", len(got), "of", len(units), "stats", sel.stats, flush=True)


if __name__ == "__main__":
    main()

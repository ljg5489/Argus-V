"""D1(a): anatomy of the headline cells (train only)."""
from __future__ import annotations
import json, sys
from collections import Counter
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from experiments.risk_loop.argus_loop import iter11_diag_common as D  # noqa: E402

data, rows, info = D.headline()
sid = D.scenario_map(rows)
y = rows.y
out = []
for c, m in D.cells(rows):
    pos, neg = m[y[m] == 1], m[y[m] == 0]
    out.append({"cell": c, "n": int(len(m)), "pos": int(len(pos)), "neg": int(len(neg)),
                "label_status": dict(Counter(rows.label_status[m].tolist())),
                "label_status_pos": dict(Counter(rows.label_status[pos].tolist())),
                "scenarios": dict(Counter(sid[m].tolist())), "scenarios_pos": dict(Counter(sid[pos].tolist())),
                "scenarios_neg": dict(Counter(sid[neg].tolist())),
                "families": sorted(set(rows.family[m].tolist())),
                "n_traj": int(len(set(rows.trajectory_id[m].tolist()))),
                "n_traj_pos": int(len(set(rows.trajectory_id[pos].tolist()))),
                "n_traj_neg": int(len(set(rows.trajectory_id[neg].tolist()))),
                "n_traj_both": int(len(set(rows.trajectory_id[pos].tolist()) & set(rows.trajectory_id[neg].tolist()))),
                "neg_in_pos_traj": int(np.isin(rows.trajectory_id[neg], rows.trajectory_id[pos]).sum())})
tot = {"rows": int(sum(e["n"] for e in out)), "pos": int(sum(e["pos"] for e in out)), "neg": int(sum(e["neg"] for e in out))}
res = {"headline_info": info, "cells": out, "totals": tot}
D.OUT.mkdir(parents=True, exist_ok=True)
(D.OUT / "d1a.json").write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
for e in out:
    print(json.dumps(e, ensure_ascii=False))
print(tot)

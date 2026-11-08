"""D2 follow-up: near-duplicate activations across trajectories inside headline cells, and LOTO with
duplicate-linked trajectories held out together (leave-one-linked-group-out). Train only."""
from __future__ import annotations
import json, sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from experiments.risk_loop.argus_loop import iter11_diag_common as D  # noqa: E402
from experiments.risk_loop.argus_loop import iter11_diag_cell as DC  # noqa: E402
from experiments.risk_loop import harness as H  # noqa: E402

EPS = 1e-3
data, rows, _ = D.headline()
cl = D.cells(rows)
y = rows.y
traj = rows.trajectory_id.astype(str)
pos = {c: int(y[m].sum()) for c, m in cl}
res = {"dup": {}, "linked_loto": {}}
for rep in ("L16:pre", "L20:rend", "L23:max", "L20:pre"):
    L, p = rep.split(":")
    X = np.asarray(D.C1.features(data, rows, int(L.lstrip("L")), p), dtype=np.float64)
    Xc = X - X.mean(0)
    U = Xc / np.maximum(np.linalg.norm(Xc, axis=1, keepdims=True), 1e-9)
    nd, same_lab, diff_lab, rows_with_dup = 0, 0, 0, 0
    per = {}
    for model in ("logreg", "centroid"):
        per[model] = {}
    for c, m in cl:
        S = 1 - U[m] @ U[m].T
        link = list(range(len(m)))  # union-find on trajectories linked by a duplicate row
        tr = traj[m]
        tid = {t: i for i, t in enumerate(np.unique(tr))}
        parent = list(range(len(tid)))

        def f(a):
            while parent[a] != a:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a
        has = np.zeros(len(m), bool)
        for i in range(len(m)):
            for j in range(i + 1, len(m)):
                if tr[i] != tr[j] and S[i, j] < EPS:
                    nd += 1
                    has[i] = has[j] = True
                    if y[m][i] == y[m][j]:
                        same_lab += 1
                    else:
                        diff_lab += 1
                    parent[f(tid[tr[i]])] = f(tid[tr[j]])
        rows_with_dup += int(has.sum())
        grp = np.asarray([f(tid[t]) for t in tr]).astype(str)
        for model in ("logreg", "centroid"):
            Xm = Xc[m] if model == "centroid" else X[m]
            s = DC.loto_scores(Xm, y[m], grp, model)
            per[model][c] = DC.cell_auc(s, y[m])
    res["dup"][rep] = {"dup_pairs_other_traj": nd, "same_label": same_lab, "different_label": diff_lab,
                       "rows_with_dup": rows_with_dup, "cell_rows": int(sum(len(m) for _, m in cl))}
    for model in per:
        v = per[model]
        w = sum(v[c] * pos[c] for c in v if v[c] is not None) / sum(pos[c] for c in v if v[c] is not None)
        res["linked_loto"][f"{rep}|{model}"] = {"weighted": w, "per_cell": v}
    print(rep, res["dup"][rep], {k: round(v["weighted"], 3) for k, v in res["linked_loto"].items() if k.startswith(rep)}, flush=True)
(D.OUT / "d2_dup.json").write_text(json.dumps(res, indent=1), encoding="utf-8")

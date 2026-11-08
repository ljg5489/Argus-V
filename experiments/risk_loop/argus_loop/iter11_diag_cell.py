"""D2: within-cell leave-one-trajectory-out (LOTO) ceiling + activation distance check. Train only.

LOTO: for every headline cell, every feature representation (6 layers x max/mean/pre/rend) and two simple
models (L2 logistic regression on cell-standardised features, C=0.05; nearest class centroid by cosine on
features centred by the headline-row mean), hold out one trajectory, train on the cell's other rows, score the
held-out rows; per-cell AUROC on the pooled held-out scores. The scenario is fully seen in training (optimistic).
Selection over 48 (rep, model) choices is optimistic too; a within-cell label-permutation null of the same
best-of-48 is reported (10 permutations).
Distances: cosine distance (centred features) of (violation, normal) pairs in the same trajectory vs other pair types.
"""
from __future__ import annotations

import json
import sys
import time
import warnings
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from experiments.risk_loop import harness as H  # noqa: E402
from experiments.risk_loop.argus_loop import iter11_diag_common as D  # noqa: E402

REPS = [f"L{L}:{p}" for L in (8, 11, 14, 16, 20, 23) for p in ("max", "mean", "pre", "rend")]
N_PERM = 10


def loto_scores(X, y, traj, model):
    from sklearn.linear_model import LogisticRegression
    s = np.full(len(y), np.nan)
    for t in np.unique(traj):
        te = traj == t
        tr = ~te
        if len(np.unique(y[tr])) < 2:
            continue
        Xtr, Xte = X[tr], X[te]
        if model == "logreg":
            mu, sd = Xtr.mean(0), Xtr.std(0)
            sd[sd < 1e-6] = 1.0
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                lr = LogisticRegression(C=0.05, max_iter=2000).fit((Xtr - mu) / sd, y[tr])
            s[te] = lr.decision_function((Xte - mu) / sd)
        else:
            def unit(a):
                return a / np.maximum(np.linalg.norm(a, axis=-1, keepdims=True), 1e-9)
            c1, c0 = unit(Xtr[y[tr] == 1].mean(0)), unit(Xtr[y[tr] == 0].mean(0))
            U = unit(Xte)
            s[te] = U @ c1 - U @ c0
    return s


def cell_auc(s, y):
    ok = np.isfinite(s)
    if ok.sum() < 2 or len(np.unique(y[ok])) < 2:
        return None
    return float(H.auroc(s[ok], y[ok]))


def main():
    t0 = time.time()
    data, rows, _ = D.headline()
    cl = D.cells(rows)
    y_all = rows.y
    traj_all = rows.trajectory_id.astype(str)
    rng = np.random.default_rng(0)
    perms = {c: [rng.permutation(len(m)) for _ in range(N_PERM)] for c, m in cl}
    res = {"loto": {}, "loto_null": {}, "dist": {}}
    fits = 0
    for rep in REPS:
        L, p = rep.split(":")
        X = np.asarray(D.C1.features(data, rows, int(L.lstrip("L")), p), dtype=np.float64)
        Xc = X - X.mean(0)
        for model in ("logreg", "centroid"):
            for c, m in cl:
                Xm = Xc[m] if model == "centroid" else X[m]
                s = loto_scores(Xm, y_all[m], traj_all[m], model)
                fits += len(np.unique(traj_all[m]))
                res["loto"].setdefault(f"{rep}|{model}", {})[c] = cell_auc(s, y_all[m])
                nulls = []
                for pi in perms[c]:
                    yp = y_all[m][pi]
                    sp = loto_scores(Xm, yp, traj_all[m], model)
                    fits += len(np.unique(traj_all[m]))
                    nulls.append(cell_auc(sp, yp))
                res["loto_null"].setdefault(f"{rep}|{model}", {})[c] = nulls
        # distances (centred features), cosine distance
        U = Xc / np.maximum(np.linalg.norm(Xc, axis=1, keepdims=True), 1e-9)
        cats = {"same_traj_viol_vs_norm": [], "same_cell_other_traj_viol_vs_norm": [],
                "same_cell_norm_norm": [], "same_cell_viol_viol": [], "different_cell_random": []}
        for c, m in cl:
            for i in m:
                for j in m:
                    if j <= i:
                        continue
                    d = 1.0 - float(U[i] @ U[j])
                    same_t = traj_all[i] == traj_all[j]
                    yi, yj = y_all[i], y_all[j]
                    if yi != yj:
                        cats["same_traj_viol_vs_norm" if same_t else "same_cell_other_traj_viol_vs_norm"].append(d)
                    elif not same_t:
                        cats["same_cell_viol_viol" if yi == 1 else "same_cell_norm_norm"].append(d)
        allm = np.concatenate([m for _, m in cl])
        cell_id = {int(i): c for c, m in cl for i in m}
        for _ in range(2000):
            i, j = rng.choice(allm, 2, replace=False)
            if cell_id[int(i)] != cell_id[int(j)]:
                cats["different_cell_random"].append(1.0 - float(U[i] @ U[j]))
        res["dist"][rep] = {k: {"n": len(v), "median": float(np.median(v)) if v else None,
                                "p10": float(np.percentile(v, 10)) if v else None,
                                "min": float(np.min(v)) if v else None} for k, v in cats.items()}
        print(time.strftime("%H:%M:%S"), rep, "done", flush=True)
        del X, Xc, U
    # summaries
    pos = {c: int(y_all[m].sum()) for c, m in cl}

    def weighted(per):
        num = sum(per[c] * pos[c] for c in per if per[c] is not None)
        den = sum(pos[c] for c in per if per[c] is not None)
        return num / den if den else None
    combos = sorted(res["loto"])
    res["loto_weighted"] = {k: weighted(res["loto"][k]) for k in combos}
    best_combo = max(combos, key=lambda k: res["loto_weighted"][k] or -1)
    per_cell_best = {c: max(res["loto"][k][c] for k in combos if res["loto"][k][c] is not None) for c, _ in cl}
    null_best_weighted = []
    for r in range(N_PERM):
        nw = {k: weighted({c: res["loto_null"][k][c][r] for c, _ in cl}) for k in combos}
        null_best_weighted.append(max(v for v in nw.values() if v is not None))
    res["summary"] = {"best_single_combo": best_combo, "best_single_combo_weighted": res["loto_weighted"][best_combo],
                      "fixed_L23max_logreg_weighted": res["loto_weighted"]["L23:max|logreg"],
                      "fixed_L16pre_logreg_weighted": res["loto_weighted"]["L16:pre|logreg"],
                      "median_over_48_combos": float(np.median([v for v in res["loto_weighted"].values() if v is not None])),
                      "per_cell_best_of_48": per_cell_best, "per_cell_best_of_48_weighted": weighted(per_cell_best),
                      "null_best_of_48_weighted_by_perm": null_best_weighted,
                      "null_best_of_48_weighted_mean": float(np.mean(null_best_weighted)),
                      "per_cell_fixed_L23max_logreg": res["loto"]["L23:max|logreg"],
                      "cell_positives": pos, "loto_fits": fits, "seconds": time.time() - t0}
    (D.OUT / "d2_cell.json").write_text(json.dumps(res, indent=1), encoding="utf-8")
    print(json.dumps(res["summary"], indent=1))


if __name__ == "__main__":
    main()

"""D4: metric noise of the headline (train only, saved T7-a 10-seed OOF; no new fits).

- family-bootstrap 95% CI (frozen evaluate.family_bootstrap_ci) for seeds 0-2 and 0-9
- per-cell AUROC, weight, contribution and share of the gap to 0.90; leave-one-cell-out headline
- pooled-over-folds headline vs within-fold reference (evaluate._fold_cell_within_tool)
- simulation: exact cell sizes, true per-cell AUROC A (binormal equal variance), a fraction of observed positives
  that are really normal (and optionally of observed negatives that are really violations); distribution of
  the observed headline, P(>=0.90), and a cell-bootstrap CI-low check.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
from scipy.stats import norm, rankdata

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402
from experiments.risk_loop.argus_loop import iter11_diag_common as D  # noqa: E402


def auc(s, y):
    r = rankdata(s)
    p = y.sum()
    n = len(y) - p
    return (r[y == 1].sum() - p * (p + 1) / 2) / (p * n)


def simulate(sizes, A, x_pos, x_neg, nsim, rng, nov_only=False, boot=0):
    d = np.sqrt(2) * norm.ppf(A)
    vals, ci_lows = [], []
    for _ in range(nsim):
        per = []
        for (cname, p, n) in sizes:
            xp = x_pos if (not nov_only or cname.endswith("|nov")) else 0.0
            xn = x_neg if (not nov_only or cname.endswith("|nov")) else 0.0
            fp = rng.binomial(p, xp)          # observed positives that are really normal
            fn = rng.binomial(n, xn)          # observed negatives that are really violations
            true_pos_obs_pos = p - fp
            s_pos = np.r_[rng.normal(d, 1, true_pos_obs_pos), rng.normal(0, 1, fp)]
            s_neg = np.r_[rng.normal(0, 1, n - fn), rng.normal(d, 1, fn)]
            s = np.r_[s_pos, s_neg]
            y = np.r_[np.ones(p), np.zeros(n)].astype(int)
            per.append((p, s, y))
        v = sum(p * auc(s, y) for p, s, y in per) / sum(p for p, _, _ in per)
        vals.append(v)
        if boot:
            bv = []
            k = len(per)
            for _b in range(boot):
                pick = rng.integers(0, k, k)
                num = den = 0.0
                for ci in pick:
                    p, s, y = per[ci]
                    idx = np.r_[rng.choice(np.nonzero(y == 1)[0], p), rng.choice(np.nonzero(y == 0)[0], len(y) - p)]
                    yy = y[idx]
                    num += p * auc(s[idx], yy)
                    den += p
                bv.append(num / den)
            ci_lows.append(np.percentile(bv, 2.5))
    vals = np.asarray(vals)
    out = {"true_auroc": A, "x_pos": x_pos, "x_neg": x_neg, "nov_only": nov_only, "nsim": nsim,
           "mean": float(vals.mean()), "sd": float(vals.std()), "p2.5": float(np.percentile(vals, 2.5)),
           "p97.5": float(np.percentile(vals, 97.5)), "P_obs_ge_0.90": float((vals >= 0.90).mean()),
           "P_obs_ge_0.88": float((vals >= 0.88).mean())}
    if boot:
        cl = np.asarray(ci_lows)
        out.update({"boot_ci_low_median": float(np.median(cl)), "P_ci_low_ge_0.80": float((cl >= 0.80).mean()),
                    "P_obs_ge_0.90_and_ci_low_ge_0.80": float(((vals >= 0.90) & (cl >= 0.80)).mean())})
    return out


def main():
    _, rows, _ = D.headline()
    y = rows.y
    g = E.headline_groups(rows)
    cl = D.cells(rows)
    T7 = np.load(D.ART / "iter08" / "B_oof_T7a_seed0-9.npy")
    res = {}
    res["ci_seed012"] = E.family_bootstrap_ci(list(T7[:3]), rows)
    res["ci_seed0_9"] = E.family_bootstrap_ci(list(T7), rows)
    pos = {c: int(y[m].sum()) for c, m in cl}
    P = sum(pos.values())
    per_cell = {c: float(np.mean([auc(o[m], y[m]) for o in T7])) for c, m in cl}
    per_cell_sd = {c: float(np.std([auc(o[m], y[m]) for o in T7], ddof=1)) for c, m in cl}
    head = sum(pos[c] * per_cell[c] for c in pos) / P
    gap = 0.90 - head
    res["per_cell"] = {c: {"pos": pos[c], "neg": int(len(m) - pos[c]), "weight": pos[c] / P, "auroc_10seed": per_cell[c],
                           "seed_sd": per_cell_sd[c], "contribution": pos[c] / P * per_cell[c],
                           "share_of_gap_to_0.90": pos[c] / P * (0.90 - per_cell[c]) / gap} for c, m in cl}
    res["headline_10seed"] = head
    res["leave_one_cell_out"] = {c: (head * P - pos[c] * per_cell[c]) / (P - pos[c]) for c in pos}
    # pooled vs within-fold
    wf = []
    for s in range(10):
        fid = E._fold_id(E.make_folds(rows, 5, s), len(rows))
        wf.append(E._fold_cell_within_tool(T7[s], y, g, fid))
    res["within_fold_reference_10seed"] = float(np.mean(wf))
    # simulation
    sizes = [(c, pos[c], int(len(m) - pos[c])) for c, m in cl]
    rng = np.random.default_rng(0)
    sims = []
    for A in (0.90, 0.95, 1.0):
        for x in (0.0, 0.1, 0.2, 0.3, 0.4):
            sims.append(simulate(sizes, A, x, 0.0, 4000, rng))
            sims.append(simulate(sizes, A, x, x, 4000, rng))
            sims.append(simulate(sizes, A, x, 0.0, 4000, rng, nov_only=True))
    for A, x in ((0.90, 0.0), (0.90, 0.2), (1.0, 0.2), (0.95, 0.0)):
        sims.append(simulate(sizes, A, x, 0.0, 400, rng, boot=200) | {"with_ci": True})
    res["simulation"] = sims
    (D.OUT / "d4.json").write_text(json.dumps(res, indent=1), encoding="utf-8")
    print(json.dumps({k: v for k, v in res.items() if k != "simulation"}, indent=1))
    for s in sims:
        if s["true_auroc"] == 0.90 or s.get("with_ci"):
            print(s)


if __name__ == "__main__":
    main()

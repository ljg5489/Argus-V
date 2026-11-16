"""Is the Argus-V-em held-out score (0.92 at epoch 40, 0.96 at epoch 60) trustworthy? Fits nothing.

Written for the user's question of 2026-11-16 ("validation 0.92 without overfitting?"). Findings are in
reports/risk-loop/argus-v-em/results.md, section "0.92~0.96을 얼마나 믿을 수 있나".
Usage: PYTHONUTF8=1 py -3.11 experiments/risk_loop/argus_loop/argus_v_em_heldout_check.py

Reads train-split rows, the saved held-out scores and the per-epoch record.
A. what the four scored cells are made of (families, scenarios, duplicates)
B. exact-duplicate rows across the train / held-out boundary of every fold
C. nearest row in another scenario family for each visible violation
D. simple no-model rules on the same rows
E. the score with duplicate rows collapsed
F. which cell moved between epoch 40 and 60, in pairs
"""
import json
import os
import sys
from collections import Counter, defaultdict
from pathlib import Path

for _n in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ.setdefault(_n, "2")
import numpy as np

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from experiments.risk_loop import harness as H  # noqa: E402
from experiments.risk_loop.argus_loop import argus_v_em as EM  # noqa: E402
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402

cx = EM.Ctx()
vis, rule = EM.visible_mask(cx)
y, g = cx.y, cx.groups
target = (y == 0) | vis
yv = vis.astype(np.int64)
fam = cx.rows.family.astype(str)
scen = np.asarray(cx.scen, dtype=str)
unit = cx.rows.unit_id.astype(str)
step = cx.rows.step_index.astype(np.int64)
hsh = np.asarray(cx.hashes, dtype=str)
cells = {}
for c in sorted(set(g.tolist())):
    m = g == c
    cells[c] = (int(vis[m].sum()), int(((y == 0) & m).sum()))
cells3 = sorted(c for c, (p, n) in cells.items() if p >= 3 and n >= 3)
cells2 = sorted(c for c, (p, n) in cells.items() if p >= 2 and n >= 2)
mask3 = target & np.isin(g, cells3)
mask2 = target & np.isin(g, cells2)
oof = [np.load(EM.OUT / f"oof_EM32_s{s}.npy") for s in EM.SEEDS]


def wt(s, mask, mp):
    return float(EM.score_metric(cx, s, mask, mp)["value"])


print("===== A. the scored cells =====")
for c in cells2:
    m = np.flatnonzero(target & (g == c))
    pos, neg = m[yv[m] == 1], m[yv[m] == 0]
    hid = np.flatnonzero((g == c) & (y == 1) & ~vis)
    print(f"{c:34s} visible {len(pos)} (distinct inputs {len(set(hsh[pos]))}) | normal {len(neg)} (distinct {len(set(hsh[neg]))}) | hidden violations {len(hid)}"
          f" | {'primary' if c in cells3 else 'aux'}")
    print("    families of visible:", dict(Counter(fam[pos].tolist())), "| scenarios:", dict(Counter(scen[pos].tolist())))
    print("    families of normal :", dict(Counter(fam[neg].tolist())), "| scenarios:", dict(Counter(scen[neg].tolist())))
    both = set(hsh[pos]) & set(hsh[neg])
    print("    inputs that appear both as a visible violation and as a normal call:", len(both))
    print("    step index visible:", sorted(step[pos].tolist()), "| normal:", sorted(step[neg].tolist()))

print("\n===== B. identical inputs on both sides of a fold =====")
for seed in EM.SEEDS:
    for fi, (tr, te) in enumerate(E.make_folds(cx.rows, 5, seed)):
        shared = set(hsh[tr]) & set(hsh[te])
        tp = te[vis[te]]
        leak_pos = sum(1 for i in tp if hsh[i] in set(hsh[tr]))
        fam_shared = set(fam[tr]) & set(fam[te])
        scen_shared = set(scen[tr]) & set(scen[te])
        print(f"seed {seed} fold {fi}: held-out rows {len(te)}, visible in held-out {len(tp)} | identical inputs shared with training: {len(shared)}"
              f" (visible violations among them: {leak_pos}) | shared families {len(fam_shared)} | shared scenarios {len(scen_shared)}")

print("\n===== C. nearest row from another scenario family, per visible violation =====")
X = np.concatenate([cx.feats["L23:max"], cx.feats["L16:pre"]], axis=1).astype(np.float32)
mu, sd = X.mean(0), X.std(0)
sd[sd < 1e-6] = 1.0
pos_idx = np.flatnonzero(vis)
Zp = np.clip((X[pos_idx] - mu) / sd, -5, 5)
Zp /= np.linalg.norm(Zp, axis=1, keepdims=True)
best = np.full(len(pos_idx), -2.0)
arg = np.full(len(pos_idx), -1)
best_same = np.full(len(pos_idx), -2.0)
for i in range(0, cx.n, 1024):
    Z = np.clip((X[i:i + 1024] - mu) / sd, -5, 5)
    Z /= np.linalg.norm(Z, axis=1, keepdims=True)
    S = Zp @ Z.T
    idx = np.arange(i, min(i + 1024, cx.n))
    other = fam[pos_idx][:, None] != fam[idx][None, :]
    S_o = np.where(other, S, -2.0)
    j = S_o.argmax(1)
    v = S_o[np.arange(len(pos_idx)), j]
    upd = v > best
    best[upd], arg[upd] = v[upd], idx[j[upd]]
    same_other_row = (~other) & (pos_idx[:, None] != idx[None, :])
    best_same = np.maximum(best_same, np.where(same_other_row, S, -2.0).max(1))
kind = Counter()
for k, i in enumerate(pos_idx):
    j = arg[k]
    lab = "visible violation" if vis[j] else ("hidden violation" if y[j] == 1 else "normal")
    kind[lab] += 1
    print(f"{g[i]:32s} {unit[i]:26s} step {step[i]:2d} | nearest other-family row: cos {best[k]:.3f} {lab:17s} {g[j]:30s} | nearest same-family row cos {best_same[k]:.3f}")
print("label of the nearest other-family row:", dict(kind))
del X

print("\n===== D. rules without a model, same rows (visible violations, same-tool AUROC) =====")
order_in_tool = np.zeros(cx.n)
seen = defaultdict(int)
for i in np.lexsort((step, unit)):
    k = (unit[i], g[i])
    order_in_tool[i] = seen[k]
    seen[k] += 1
n_steps = Counter(unit.tolist())
rules = {"earlier step = violation": -step.astype(float),
         "first call of that tool in the run = violation": -order_in_tool,
         "later step = violation": step.astype(float)}
print(f"{'rule':48s} min3   min2   per cell (min2)")
for name, s in rules.items():
    r2 = EM.score_metric(cx, s, mask2, 2)
    print(f"{name:48s} {wt(s, mask3, 3):.3f}  {r2['value']:.3f}  ",
          {p['tool'].split('|')[0]: round(p['auroc'], 2) for p in r2['per_tool'] if p['included']})
r2 = [EM.score_metric(cx, s, mask2, 2) for s in oof]
print(f"{'Argus-V-em 32-dim, held-out (3 splits)':48s} {np.mean([wt(s, mask3, 3) for s in oof]):.3f}  {np.mean([r['value'] for r in r2]):.3f}  ",
      {p['tool'].split('|')[0]: round(float(np.mean([H.auroc(s[target & (g == p['tool'])], yv[target & (g == p['tool'])]) for s in oof])), 2)
       for p in r2[0]['per_tool'] if p['included']})
print("Spearman-like check: AUROC of 'earlier step' inside each cell is listed above; held-out score vs step index correlation per cell:")
for c in cells2:
    m = np.flatnonzero(target & (g == c))
    s = np.mean([o[m] for o in oof], axis=0)
    rs = np.corrcoef(np.argsort(np.argsort(s)), np.argsort(np.argsort(step[m])))[0, 1]
    print(f"    {c:34s} rank correlation(score, step index) {rs:+.2f}")

print("\n===== E. duplicates collapsed (one row per distinct input and label in a cell) =====")
keep = np.zeros(cx.n, dtype=bool)
seen_key = set()
for i in np.flatnonzero(mask2):
    k = (g[i], hsh[i], int(yv[i]))
    if k not in seen_key:
        seen_key.add(k)
        keep[i] = True
for nm, mk, mp in (("min3", mask3, 3), ("min2", mask2, 2)):
    full = [EM.score_metric(cx, s, mk, mp) for s in oof]
    ded = [EM.score_metric(cx, s, mk & keep, mp) for s in oof]
    print(f"{nm}: all rows {np.mean([r['value'] for r in full]):.3f} ({full[0]['n_positives_included']} violations, {full[0]['n_tools']} cells)"
          f" | distinct rows {np.mean([r['value'] for r in ded]):.3f} ({ded[0]['n_positives_included']} violations, {ded[0]['n_tools']} cells)")
    print("     distinct, per cell:", {p['tool'].split('|')[0]: (p['positives'], p['negatives'], None if p['auroc'] is None else round(p['auroc'], 2)) for p in ded[0]['per_tool']})

print("\n===== F. epoch 40 -> 60, per cell =====")
h = json.loads((EM.REPORT / "epoch_history.json").read_text(encoding="utf-8"))
ca = np.asarray(h["models"]["EM32"]["per_epoch"]["cell_auroc_heldout"], dtype=float)      # [seed][epoch][cell]
tot = np.asarray(h["models"]["EM32"]["per_epoch"]["auroc_heldout_min3"], dtype=float).mean(0)
P = sum(cells[c][0] for c in h["cells_min3"])
for e in (1, 20, 30, 40, 50, 60):
    print(f"epoch {e:2d}: overall {tot[e - 1]:.3f} |", {c.split('|')[0]: round(float(ca[:, e - 1, k].mean()), 3) for k, c in enumerate(h["cells_min3"])})
for k, c in enumerate(h["cells_min3"]):
    p, n = cells[c]
    d = float(ca[:, 59, k].mean() - ca[:, 39, k].mean())
    print(f"    {c:34s} pairs {p * n:3d} | change 40->60 {d:+.3f} = {d * p * n:+.1f} pairs | contribution to the overall score {d * p / P:+.3f}")
print(f"    overall change 40->60: {tot[59] - tot[39]:+.3f}")

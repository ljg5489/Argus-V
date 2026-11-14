"""Iteration 14: "같은 도구 안 학습" -- learn risky ACTIONS, not risky tools / contexts (training-only changes).

Pre-registration: reports/risk-loop/argus-v1/loop/iter-14/prereg-within-tool.md (sha in prereg-within-tool.sha256;
checked before any real-data fit). Strictly additive: evaluate.py, obs_grid.py, obs_models.py, obs_grid_s.py,
obs_models_s.py and obs_models_s0f.py are imported, never modified (a detached S-stage grid imports them).

"Cell" = tool x source (the headline grouping). Cells are read at TRAINING positions only.
Methods (training only; the tool name is never a scoring-time input):
  none  the base model as it is (reproduces the existing code exactly -- tested)
  w1    per-cell centring: inside the training fold subtract each cell's training-row mean from every feature
        (after the base's own robust scale / PCA / standardisation), fit the base's own loss on the centred
        features; score = learned linear direction x UNCENTRED features. Linear: exact (w.x = w.(x - mu_cell) +
        per-cell constant). CNN-MLP: per-point PCA inputs centred per cell when training; at scoring time centred by
        the training-fold GLOBAL mean (approximation; that mean is ~0 by construction of the PCA input).
  w2    within-cell pair loss only: (violation, normal) pairs of the same cell across rollouts; same-rollout pairs
        weight 2; weight 1/n_normal(cell) per pair, normalised to mean 1 (models.same_group_pairs convention).
        No cross-cell pairs, no BCE.
  w3    w2 + 0.1 x BCE on the per-cell-centred features ("pair mean : BCE mean = 1 : 0.1").
Bases:
  t7a   T7-a (iter06_models.make_t62 on iter07 robust PCA embeddings, 3 members, training-percentile average)
  lin   선형 기준 모델 (obs_models_s0f convex baseline, layer-20 cache, [per-coordinate max, pre] -> logistic)
  cnn   CNN-MLP (obs_models_s0f small CNN-MLP)

  py -3.11 experiments/risk_loop/argus_loop/within_tool.py run [--bases t7a,lin,cnn] [--threads 2]
  py -3.11 experiments/risk_loop/argus_loop/within_tool.py report
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time
from collections import Counter
from pathlib import Path

for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ.setdefault(_v, "2")

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop import harness as H  # noqa: E402
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402
from experiments.risk_loop.argus_loop import obs_models as OM  # noqa: E402
from experiments.risk_loop.argus_loop import obs_models_s as OMS  # noqa: E402
from experiments.risk_loop.argus_loop import obs_models_s0f as OMS0F  # noqa: E402

EVAL_SHA = "a7c36eafdf994f98b61895be4e4b8d237740d0018422d12febab8deb9df0130d"
ART = REPO_ROOT / "artifacts" / "risk-loop" / "argus-v1-loop"
VIEW = ART / "features_labels_v2"
CACHE = ART / "obs_cache"
OUT = ART / "phase3" / "within_tool"
S_STORE = ART / "phase3" / "s1" / "fits"           # S-stage fit store (read only)
LOOP = REPO_ROOT / "reports" / "risk-loop" / "argus-v1" / "loop"
IT14 = LOOP / "iter-14"
PREREG = IT14 / "prereg-within-tool.md"
PREREG_SHA = IT14 / "prereg-within-tool.sha256"

METHODS = ("none", "w1", "w2", "w3")
W_METHODS = ("w1", "w2", "w3")
METHOD_KO = {"none": "방법 없음(원래 모델)", "w1": "칸별 중심화(W1)", "w2": "칸 안 쌍 학습(W2)", "w3": "둘 다(W3)"}
BASE_KO = {"t7a": "T7-a", "lin": "선형 기준 모델", "cnn": "CNN-MLP"}
BASES = ("t7a", "lin", "cnn")
BCE_SMALL = 0.1
SAME_ROLLOUT_MULT = 2.0
BASE_W_BCE = 0.2          # the bases' own BCE weight (S-0 / S-F: pair 1 : BCE 0.2); also fixes a = C n / 0.2
SEEDS3 = (0, 1, 2)
INNER = 4
N_SHUF = 20
REF_B = 0.596
T7A_REF = 0.721
TRIES_BEFORE, TRIES_BEFORE_CONS = 160, 162
MIN_FREE_GB = 1.0
LIN_GRID = (0.01, 0.1, 1.0)
CNN_GRID = (1e-3, 1e-2, 1e-1)
T7A_PRE_REPS = {"L23:max": "L23:pre"}   # pre-action-only control: every member on a pre-action representation

AUDIT = Counter()
CENTER_LOG = []   # (hash of the rows a centring used, hash of the fit's training rows, hash of its scored rows)
INPUTS = ("robust_clip", "robust_noclip", "plain")   # (a) as is, (b) no clip, (c) cycle-1 input (ObsData.embed)
NOCLIP = 1e6


def log(*a):
    print(time.strftime("%H:%M:%S"), *a, flush=True)


def _check(ok: bool, name: str):
    AUDIT[name + (":ok" if ok else ":FAIL")] += 1
    if not ok:
        raise RuntimeError(f"leak audit failed: {name}")


# ============================================================================================== core pieces

def cell_keys(tool, source) -> np.ndarray:
    return np.asarray([f"{t}|{s}" for t, s in zip(np.asarray(tool).astype(str), np.asarray(source).astype(str))],
                      dtype=object)


def center_audit(rows_used, pa, pb):
    """Centring rows must be exactly the fit's training rows (inner-training rows during inner selection) and
    disjoint from its scored rows."""
    rows_used, pa, pb = (np.asarray(x, np.int64) for x in (rows_used, pa, pb))
    ok = bool(np.array_equal(np.sort(rows_used), np.sort(pa)) and not np.intersect1d(rows_used, pb).size)
    CENTER_LOG.append((OM.h_arr(np.sort(rows_used)), OM.h_arr(np.sort(pa)), OM.h_arr(np.sort(pb))))
    _check(ok, "centring_rows_are_training_rows")


def cell_center(X, cells, pos=None):
    """X - (mean of each row's cell over the given rows). Returns (centred X, {cell: mean}, rows used): ``rows
    used`` = the positions (``pos``, default 0..n-1) of every row that entered a cell mean -- passed to
    center_audit, so the audit checks the rows the means were really computed from."""
    X = np.asarray(X, np.float64)
    cells = np.asarray(cells).astype(str)
    pos = np.arange(len(X)) if pos is None else np.asarray(pos, np.int64)
    if len(pos) != len(X):
        raise ValueError("pos must label every row of X")
    Xc = X.copy()
    mus, used = {}, []
    for c in np.unique(cells):
        m = np.nonzero(cells == c)[0]
        mu = X[m].mean(0)
        Xc[m] -= mu
        mus[c] = mu
        used.append(pos[m])
    return Xc, mus, (np.concatenate(used) if used else np.zeros(0, np.int64))


def within_cell_pairs(y, cells, traj, same_mult=SAME_ROLLOUT_MULT):
    """(violation i, normal j) pairs inside each cell (any rollout). Weight 1/n_normal(cell), x same_mult when i and
    j share the rollout; normalised to mean 1. Cells without a normal give no pairs."""
    y = np.asarray(y).astype(np.int64)
    cells = np.asarray(cells).astype(str)
    traj = np.asarray(traj).astype(str)
    I, J, W = [], [], []
    for c in np.unique(cells):
        idx = np.nonzero(cells == c)[0]
        p, n = idx[y[idx] == 1], idx[y[idx] == 0]
        if not len(p) or not len(n):
            continue
        ii, jj = np.meshgrid(p, n, indexing="ij")
        ii, jj = ii.ravel(), jj.ravel()
        w = np.full(len(ii), 1.0 / len(n))
        w[traj[ii] == traj[jj]] *= same_mult
        I.append(ii)
        J.append(jj)
        W.append(w)
    if not I:
        return np.zeros(0, np.int64), np.zeros(0, np.int64), np.zeros(0)
    I, J, W = np.concatenate(I), np.concatenate(J), np.concatenate(W)
    return I, J, W / W.mean()


def audit_pairs(I, J, y, cells, n):
    ok = bool(len(I) == 0 or (I.max() < n and J.max() < n and np.all(np.asarray(y)[I] == 1) and
                               np.all(np.asarray(y)[J] == 0) and np.all(np.asarray(cells)[I] == np.asarray(cells)[J])))
    _check(ok, "pairs_within_training_cell")


def usable_violations(y, cells) -> int:
    """Training violations whose cell has at least one training normal (they give >= 1 pair)."""
    y = np.asarray(y).astype(np.int64)
    cells = np.asarray(cells).astype(str)
    with_norm = set(cells[y == 0].tolist())
    return int(sum(1 for c in cells[y == 1] if c in with_norm))


def fit_lin(X, y, wb, I, J, pw, a, w_bce, pair_w, Xp=None, tol=1e-10, max_iter=20000):
    """argmin 0.5||w||^2 / a + w_bce * bce_mean(X) + pair_w * pair_mean(Xp); intercept unpenalised.
    == obs_models_s0f.fit_logistic_pair when a = C n / w_bce and Xp = X (tested). Xp: features of the pair term
    (default X; for linear scores the within-cell pair differences do not depend on centring)."""
    from scipy.optimize import minimize
    from scipy.special import expit
    X = np.asarray(X, np.float64)
    Xp = X if Xp is None else np.asarray(Xp, np.float64)
    y = np.asarray(y, np.float64)
    swb = float(np.sum(wb)) if w_bce else 1.0
    use_pair = bool(pair_w) and len(I) > 0
    spw = float(np.sum(pw)) if use_pair else 1.0
    F = X.shape[1]

    def fg(th):
        w, b = th[:F], th[F]
        f = 0.5 * (w @ w) / a
        gw = w / a
        gb = 0.0
        if w_bce:
            s = X @ w + b
            f += w_bce * float(wb @ (np.logaddexp(0.0, s) - y * s)) / swb
            gs = w_bce * wb * (expit(s) - y) / swb
            gw = gw + X.T @ gs
            gb += gs.sum()
        if use_pair:
            sp = Xp @ w
            d = sp[I] - sp[J]
            f += pair_w * float(pw @ np.logaddexp(0.0, -d)) / spw
            gd = -pair_w * pw * expit(-d) / spw
            gsp = np.bincount(I, gd, len(sp)) - np.bincount(J, gd, len(sp))
            gw = gw + Xp.T @ gsp
        return f, np.r_[gw, gb]

    res = minimize(fg, np.zeros(F + 1), jac=True, method="L-BFGS-B",
                   options={"maxiter": max_iter, "gtol": tol, "ftol": 1e-16, "maxcor": 30})
    return res.x[:F], float(res.x[F]), {"converged": bool(res.success), "n_iter": int(res.nit)}


def sk_pair_fit(Etr, I, J, W, C):
    """The members' sklearn pair recipe (iter04_models.same_traj_pair_fit) on given pairs."""
    from sklearn.linear_model import LogisticRegression
    if len(I) == 0:
        return None
    D = np.asarray(Etr[I] - Etr[J], np.float64)
    lr = LogisticRegression(C=C, max_iter=3000, fit_intercept=False)
    lr.fit(np.vstack([D, -D]), np.r_[np.ones(len(D)), np.zeros(len(D))], sample_weight=np.r_[W, W])
    return lr.coef_.ravel()


def pair_bce_fit(Etr, I, J, W, C, Ec, y, wb, bce=BCE_SMALL, tol=1e-9):
    """W3 member objective (sklearn pair convention + small BCE on centred features Ec):
    0.5||w||^2 + 2C (sum_k W_k softplus(-w.(E_I - E_J)) + bce * sum(W) * weighted-mean BCE(Ec w + b)).
    Intercept b unpenalised and not used for scoring. With bce = 0 this is exactly sk_pair_fit's objective."""
    from scipy.optimize import minimize
    from scipy.special import expit
    if len(I) == 0:
        return None
    D = np.asarray(Etr[I] - Etr[J], np.float64)
    Ec = np.asarray(Ec, np.float64)
    y = np.asarray(y, np.float64)
    wb = np.asarray(wb, np.float64)
    sW, swb, F = float(W.sum()), float(wb.sum()), D.shape[1]

    def fg(th):
        w, b = th[:F], th[F]
        d = D @ w
        f = 0.5 * (w @ w) + 2 * C * float(W @ np.logaddexp(0.0, -d))
        gw = w + 2 * C * D.T @ (-W * expit(-d))
        s = Ec @ w + b
        f += 2 * C * bce * sW * float(wb @ (np.logaddexp(0.0, s) - y * s)) / swb
        gs = 2 * C * bce * sW * wb * (expit(s) - y) / swb
        return f, np.r_[gw + Ec.T @ gs, gs.sum()]

    res = minimize(fg, np.zeros(F + 1), jac=True, method="L-BFGS-B",
                   options={"maxiter": 20000, "gtol": tol, "ftol": 1e-16, "maxcor": 30})
    return res.x[:F]


# ============================================================================================== base: T7-a

def t7a_components(pre_only=False):
    from experiments.risk_loop.argus_loop import iter06_models as M6
    comps = [dict(c) for c in M6.ENSEMBLE]
    if pre_only:
        for c in comps:
            c["rep"] = T7A_PRE_REPS.get(c["rep"], c["rep"])
    return comps


def t7a_member_scores(comp, store, ctx, pa, ya, pb, method):
    """(training-row scores, scored-row scores) of one T7-a member under a method. method 'none' ==
    iter06_models._component_scores (tested)."""
    from experiments.risk_loop.argus_loop import iter04_models as M4
    from experiments.risk_loop.argus_loop import iter06_models as M6
    from experiments.risk_loop.argus_loop import models as M
    Emb = store.get(comp["rep"], pa)[:, :int(comp["k"])]
    Etr = Emb[pa].astype(np.float64)
    Ete = Emb[pb].astype(np.float64)
    src = np.asarray(ctx["source"]).astype(str)[pa]
    cells = np.asarray(ctx["train_group"]).astype(str)[pa]       # tool|source, training rows only
    traj = np.asarray(ctx["trajectory"]).astype(str)[pa]
    C = float(comp["C"])
    if method in ("w1", "w3"):
        Ec, _, used = cell_center(Etr, cells, pa)
        center_audit(used, pa, pb)
    if method == "none":
        if comp["kind"] == "pointwise_informative":
            w = M6.pointwise_informative_fit(Etr, ya, src, cells, C)
        else:
            w = M4.same_traj_pair_fit(Etr, ya, traj, C)
    elif method == "w1":
        if comp["kind"] == "pointwise_informative":
            w = M6.pointwise_informative_fit(Ec, ya, src, cells, C)
        else:
            w = M4.same_traj_pair_fit(Ec, ya, traj, C)
    else:
        I, J, W = within_cell_pairs(ya, cells, traj)
        audit_pairs(I, J, ya, cells, len(pa))
        if method == "w2":
            w = sk_pair_fit(Etr, I, J, W, C)
        else:
            w = pair_bce_fit(Etr, I, J, W, C, Ec, ya, M.sample_weights(ya, src, "source_class"))
    if w is None:
        return np.zeros(len(pa)), np.zeros(len(pb))
    return Etr @ w, Ete @ w


class T7aW:
    """T7-a under a method: members refit, scored on uncentred features, training-percentile average."""

    def __init__(self, feats: dict, rows: E.Rows):
        from experiments.risk_loop.argus_loop import iter06_scan as S6
        from experiments.risk_loop.argus_loop import iter07_models as M7
        self.rows = rows
        self.ctx = S6.model_ctx(rows)
        self.store = M7.RobustStore(feats)

    def fit(self, pa, ya, pb, method, pre_only=False):
        from experiments.risk_loop.argus_loop import iter06_models as M6
        pa, pb = np.asarray(pa, np.int64), np.asarray(pb, np.int64)
        ya = np.asarray(ya).astype(np.int64)
        _check(not np.intersect1d(pa, pb).size, "train_test_disjoint")
        acc = np.zeros(len(pb))
        comps = t7a_components(pre_only)
        for comp in comps:
            s_tr, s_te = t7a_member_scores(comp, self.store, self.ctx, pa, ya, pb, method)
            acc += M6.train_percentile(s_tr, s_te)
        if len(self.store.cache) > 24:   # embeddings are label-free; keep memory bounded
            self.store.cache.clear()
        return acc / len(comps)


# ============================================================================================== base: 선형 기준 모델

def _inp_over(inp):
    if inp not in INPUTS:
        raise ValueError(inp)
    return {"robust_clip": NOCLIP} if inp == "robust_noclip" else {}


def lin_config(tune, pre_only=False, inp="robust_clip"):
    o = _inp_over(inp)
    return OMS.cpre_config("S-0", tune, **o) if pre_only else OMS.make_config_s("S-0", (0,) * 6, tune, **o)


def cnn_config(tune, pre_only=False, inp="robust_clip", **over):
    over.update(_inp_over(inp))
    return OMS.cpre_config("S-F", tune, **over) if pre_only else OMS.make_config_s("S-F", (0,) * 6, tune, **over)


def prep_inp(data, cfg, pa, ya, pb, inp="robust_clip"):
    """obs_models_s0f._prep; for inp 'plain' the per-point input is replaced by the cycle-1 pipeline
    (ObsData.embed: training-fold mean -> PCA k -> training SD; no robust scale, no clip). 'robust_noclip' is
    carried by cfg['robust_clip'] = NOCLIP (lin_config / cnn_config)."""
    p = OMS0F._prep(data, cfg, pa, ya, pb)
    if inp == "plain" and "emb" in p:
        e = data.embed(cfg["layers"][0], p["pos_train"], int(cfg["pca_k"]))
        _check(e.fit_rows == OM.h_arr(p["pos_train"]), "plain_pca_fit_rows_are_training_rows")
        p["emb"] = e
        p["Ztr"], p["Zte"] = e.Z[p["sq_tr"].idx], e.Z[p["sq_te"].idx]
        p["sd_obs"] = p["Ztr"].std(0).astype(np.float32)
    return p


def lin_fit(data: OM.ObsData, cfg, pa, ya, pb, method, inp="robust_clip") -> np.ndarray:
    """선형 기준 모델 under a method. method 'none' == obs_models_s0f.fit_s0 (tested)."""
    if cfg["T2"] or cfg["T4"]:
        raise ValueError("toggles stay off in iteration 14")
    p = prep_inp(data, cfg, pa, ya, pb, inp)
    if "emb" not in p:
        return np.zeros(len(p["pos_test"]))
    d = OMS0F.s0_design(data, cfg, pa, ya, pb, p)
    X, Xte, y = d["Xtr"], d["Xte"], d["y"]
    n = d["n"]
    a = float(cfg["logreg_C"]) * n / BASE_W_BCE
    pa = p["pos_train"]
    cells = cell_keys(data.tool[pa], data.source[pa])
    traj = data.traj[pa]
    if method in ("w1", "w3"):
        Xc, _, used = cell_center(X, cells, pa)          # T2 off -> one copy, X rows == pa
        center_audit(used, pa, p["pos_test"])
    if method in ("w2", "w3"):
        I, J, pw = within_cell_pairs(y, cells, traj)
        audit_pairs(I, J, y, cells, n)
    if method == "none":
        w, b, _ = fit_lin(X, y, d["wb"], d["I"], d["J"], d["pw"], a, BASE_W_BCE, cfg["pair_w"])
    elif method == "w1":
        w, b, _ = fit_lin(Xc, y, d["wb"], d["I"], d["J"], d["pw"], a, BASE_W_BCE, cfg["pair_w"])
    elif method == "w2":
        w, b, _ = fit_lin(X, y, d["wb"], I, J, pw, a, 0.0, 1.0)
    else:
        w, b, _ = fit_lin(Xc, y, d["wb"], I, J, pw, a, BCE_SMALL, 1.0)
    return Xte @ w + b


# ============================================================================================== base: CNN-MLP

def cnn_fit(data: OM.ObsData, cfg, pa, ya, pb, method, threads=None, inp="robust_clip") -> np.ndarray:
    """CNN-MLP under a method (one init seed = cfg['init_seeds']). method 'none' == obs_models_s0f.fit_sf score
    (tested). w1 / w3: per-point PCA inputs centred per cell (training), training-fold global mean at scoring."""
    torch = OM._torch()
    if threads:
        torch.set_num_threads(int(threads))
    if cfg["T1"] or cfg["T2"] or cfg["T4"]:
        raise ValueError("toggles stay off in iteration 14")
    p = prep_inp(data, cfg, pa, ya, pb, inp)
    R = len(cfg["init_seeds"])
    if "emb" not in p:
        return np.zeros(len(p["pos_test"]))
    pa = p["pos_train"]
    pre_only = cfg["obs_subset"] == "pre"
    sq_tr = p["sq_tr"]
    Ztr, Zte = p["Ztr"], p["Zte"]
    cells = cell_keys(data.tool[pa], data.source[pa])
    if method in ("w1", "w3"):
        pts = sq_tr.pre_flat if pre_only else np.arange(len(sq_tr.idx))
        center_audit(pa[np.unique(sq_tr.seg[pts])], pa, p["pos_test"])   # rows whose points enter the means
        pt_cell = cells[sq_tr.seg[pts]]
        mu = {c: Ztr[pts[pt_cell == c]].astype(np.float64).mean(0) for c in np.unique(pt_cell)}
        g = Ztr[pts].astype(np.float64).mean(0)
        Mrow = np.stack([mu[c] for c in cells]).astype(np.float32)       # [n_train, k], training cells only
        Ztr = (Ztr - Mrow[sq_tr.seg]).astype(np.float32)
        Zte = (Zte - g.astype(np.float32)).astype(np.float32)
    y = p["y"]
    if method in ("w2", "w3"):
        I, J, pw = within_cell_pairs(y, cells, data.traj[pa])
        audit_pairs(I, J, y, cells, len(pa))
    else:
        I, J, pw = p["I"], p["J"], p["pw"]
    w_bce = {"none": float(cfg["w_bce"]), "w1": float(cfg["w_bce"]), "w2": 0.0, "w3": BCE_SMALL}[method]
    pair_w = float(cfg["pair_w"]) if method in ("none", "w1") else 1.0
    k = int(cfg["pca_k"])
    btr, bte = OMS0F.buckets(Ztr, sq_tr), OMS0F.buckets(Zte, p["sq_te"])
    yt = torch.tensor(y, dtype=torch.float32)
    wb = torch.tensor(p["wb"], dtype=torch.float32)
    I_t, J_t = torch.from_numpy(np.asarray(I, np.int64)), torch.from_numpy(np.asarray(J, np.int64))
    pw_t = torch.tensor(pw, dtype=torch.float32)
    reps = []
    for r, seed in enumerate(cfg["init_seeds"]):
        P = OMS0F.sf_init(cfg, k, 0, seed)
        gen = torch.Generator().manual_seed(OMS0F._gen_seed(cfg, p, "sf", int(seed)))
        weights = [v for n_, v in P.items() if n_.endswith("w")]
        biases = [v for n_, v in P.items() if n_.endswith("b")]
        opt = torch.optim.Adam([{"params": weights, "weight_decay": float(cfg["nn_wd"])},
                                {"params": biases, "weight_decay": 0.0}], lr=float(cfg["lr"]))
        for _ in range(int(cfg["epochs"])):
            opt.zero_grad()
            d = OMS0F._run(P, btr, None, cfg, True, gen, 0.0, 0.0, None)
            loss = 0.0
            if w_bce:
                loss = w_bce * OM._loss_pointwise(torch, d.unsqueeze(0), yt, wb, 0.0)[0]
            if len(I_t) and pair_w:
                loss = loss + pair_w * (torch.nn.functional.softplus(-(d[I_t] - d[J_t])) * pw_t).sum() / pw_t.sum()
            if not torch.is_tensor(loss):
                break                                  # nothing to learn (no pairs, no BCE)
            loss.backward()
            opt.step()
        with torch.no_grad():
            reps.append(OMS0F._run(P, bte, None, cfg).numpy().astype(np.float64))
    assert len(reps) == R
    return np.mean(reps, 0)


# ============================================================================================== metrics

def paired_gain(oofs_a, oofs_b, rows: E.Rows, reps=E.BOOTSTRAP_REPS, seed=E.BOOTSTRAP_SEED) -> dict:
    """Seed-mean within-tool AUROC of a minus that of b, on the same family resamples (resampling exactly as
    evaluate.family_bootstrap_ci). Point gain from the full data."""
    A = [np.asarray(o, np.float64) for o in oofs_a]
    B = [np.asarray(o, np.float64) for o in oofs_b]
    y = rows.y
    g = E.headline_groups(rows)
    point = E._mean([E.within_tool_auroc(o, y, g)["value"] for o in A]) - \
        E._mean([E.within_tool_auroc(o, y, g)["value"] for o in B])
    _, fam = np.unique(rows.family.astype(str), return_inverse=True)
    _, tc = np.unique(g.astype(str), return_inverse=True)
    members = [np.nonzero(fam == f)[0] for f in range(fam.max() + 1)]
    F = len(members)
    rng = np.random.default_rng(seed)
    vals = []
    for _ in range(int(reps)):
        idx = np.concatenate([members[f] for f in rng.integers(0, F, F)])
        idx = idx[np.argsort(tc[idx], kind="stable")]
        bounds = np.flatnonzero(np.diff(tc[idx])) + 1
        na, nb, den = np.zeros(len(A)), np.zeros(len(B)), 0
        for seg in np.split(idx, bounds):
            ys = y[seg]
            p = int(ys.sum())
            if p < E.MIN_POS or len(seg) - p < E.MIN_NEG:
                continue
            for k, o in enumerate(A):
                na[k] += H.auroc(o[seg], ys) * p
            for k, o in enumerate(B):
                nb[k] += H.auroc(o[seg], ys) * p
            den += p
        if den:
            vals.append(float(na.mean() / den - nb.mean() / den))
    lo, hi = np.percentile(vals, [2.5, 97.5])
    return {"gain": float(point), "ci_low": float(lo), "ci_high": float(hi),
            "p_gain_le_0": float(np.mean(np.asarray(vals) <= 0)), "n_valid": len(vals), "reps": int(reps)}


def luck_correction(v, n):
    from scipy.stats import norm
    x = np.linspace(-8, 8, 16001)
    em = float(np.trapz(x * n * norm.pdf(x) * norm.cdf(x) ** (n - 1), x))
    return {"n_tries": n, "e_max_normal": em, "corrected": v - 0.05 * em}


def usable_report(rows: E.Rows, seeds=SEEDS3) -> dict:
    y = rows.y
    cells = E.headline_groups(rows)
    inc = {c for c in set(cells.tolist()) if y[cells == c].sum() >= E.MIN_POS and (y[cells == c] == 0).sum() >= E.MIN_NEG}
    per = []
    for s in seeds:
        for a, _ in E.make_folds(rows, 5, s):
            u = usable_violations(y[a], cells[a])
            uh = usable_violations(y[a][np.isin(cells[a], list(inc))], cells[a][np.isin(cells[a], list(inc))])
            per.append({"seed": s, "train_violations": int(y[a].sum()), "usable": u, "usable_in_headline_cells": uh})
    return {"full_data_usable": usable_violations(y, cells), "full_data_violations": int(y.sum()),
            "headline_violations": int(sum(y[cells == c].sum() for c in inc)),
            "per_fold": per,
            "mean_usable": float(np.mean([p["usable"] for p in per])),
            "min_usable": int(min(p["usable"] for p in per)), "max_usable": int(max(p["usable"] for p in per)),
            "mean_train_violations": float(np.mean([p["train_violations"] for p in per])),
            "mean_usable_in_headline_cells": float(np.mean([p["usable_in_headline_cells"] for p in per]))}


def compact(m: dict) -> dict:
    wt = m["within_tool"]
    return {"value": wt["value"], "per_seed": wt["per_seed"], "ci95": wt.get("ci95"),
            "by_source": {s: v["value"] for s, v in wt["by_source"].items()}, "pooled_auroc": m["pooled_auroc"],
            "per_cell": {e["tool"]: e["auroc"] for e in wt["per_tool"] if e["included"]},
            "baselines": {k: v["within_tool"] for k, v in m.get("baselines", {}).items() if isinstance(v, dict)}}


# ============================================================================================== runner

def sha256(p: Path) -> str:
    h = hashlib.sha256()
    h.update(Path(p).read_bytes())
    return h.hexdigest()


def free_gb() -> float:
    try:
        import psutil
        return psutil.virtual_memory().available / 2 ** 30
    except Exception:  # pragma: no cover
        return 99.0


def wait_ram(min_gb=MIN_FREE_GB):
    warned = False
    while free_gb() < min_gb:
        if not warned:
            log(f"[ram] free {free_gb():.2f} GB < {min_gb} GB -> pausing")
            warned = True
        time.sleep(30)
    if warned:
        log(f"[ram] free {free_gb():.2f} GB -> resuming")


def fit_key(pa, ya, pb) -> str:
    return OM.h_arr(np.asarray(pa, np.int64), np.asarray(ya).astype(np.int8), np.asarray(pb, np.int64))


class Memo:
    """Disk memo of fit scores: OUT/fits/<tag>/<fit_key>.npy (atomic writes; resumable)."""

    def __init__(self, out: Path):
        self.out = Path(out) / "fits"
        self.hits = self.miss = 0

    def get(self, tag, pa, ya, pb, compute):
        p = self.out / tag.replace("|", "_") / f"{fit_key(pa, ya, pb)}.npy"
        if p.is_file():
            self.hits += 1
            return np.load(p)
        self.miss += 1
        wait_ram()
        s = np.asarray(compute(), np.float64)
        if s.shape != (len(pb),) or not np.all(np.isfinite(s)):
            raise ValueError(f"{tag}: bad scores")
        p.parent.mkdir(parents=True, exist_ok=True)
        tmp = p.with_name(p.stem + f".tmp{os.getpid()}.npy")
        np.save(tmp, s)
        os.replace(tmp, p)
        return s


def s_store_score(cfg, pa, ya, pb):
    """CNN-MLP / linear base score from the S-stage fit store if that exact fit exists (read only)."""
    p = S_STORE / OM.config_id(cfg) / f"{fit_key(pa, ya, pb)}.npz"
    if not p.is_file():
        return None
    try:
        with np.load(p) as z:
            return z["score"].astype(np.float64)
    except Exception:
        return None


class Base:
    """One base: grid of tuning values and fit(method, pre_only, tune)(pa, ya, pb) through the memo."""

    def __init__(self, name, rows, memo, fitter, grid, threads=2, data=None, inp="robust_clip"):
        self.name, self.rows, self.memo, self.fitter, self.grid = name, rows, memo, fitter, list(grid)
        self.threads, self.data, self.inp = threads, data, inp
        self.store_hits = 0

    def tag(self, method, pre_only, tune):
        inp = "" if self.inp == "robust_clip" else f"|{self.inp}"
        return f"{self.name}|{method}|{'pre' if pre_only else 'all'}|{tune}{inp}"

    def make(self, method, pre_only=False):
        def mk(tune):
            def fp(pa, ya, pb):
                return self.memo.get(self.tag(method, pre_only, tune), pa, ya, pb,
                                     lambda: self.compute(method, pre_only, tune, pa, ya, pb))
            return fp
        return mk

    def compute(self, method, pre_only, tune, pa, ya, pb, use_store=True):
        if self.name == "t7a":
            return self.fitter.fit(pa, ya, pb, method, pre_only)
        if self.name == "lin":
            return lin_fit(self.data, lin_config(tune, pre_only, self.inp), pa, ya, pb, method, self.inp)
        cfg = cnn_config(tune, pre_only, self.inp)
        if method == "none" and self.inp == "robust_clip" and use_store:
            s = s_store_score(cfg, pa, ya, pb)
            if s is not None:
                self.store_hits += 1
                return s
        return cnn_fit(self.data, cfg, pa, ya, pb, method, self.threads, self.inp)

    def nested(self, method, pre_only=False, seeds=SEEDS3):
        mk = self.make(method, pre_only)
        if len(self.grid) == 1:
            cv = E.run_cv(mk(self.grid[0]), None, self.rows, seeds)
            cv["selection"] = {"method": "fixed", "chosen": {str(s): [0] * 5 for s in seeds}}
            return cv
        return E.nested_cv(mk, self.grid, None, self.rows, seeds, 5, inner_splits=INNER)

    def probe(self, method, pre_only=False):
        """Leak probe: scrambling tool / source / family / rollout / status of the SCORED rows leaves scores
        unchanged (fold 0, seed 0, first tuning value). Bypasses the memo."""
        a, b = E.make_folds(self.rows, 5, 0)[0]
        y = self.rows.y
        tune = self.grid[0]
        s1 = self.compute(method, pre_only, tune, a, y[a], b, use_store=False)
        if self.name == "t7a":
            ctx = self.fitter.ctx
            saved = {k: np.asarray(v).copy() for k, v in ctx.items()}
            try:
                for k in ctx:
                    arr = np.asarray(ctx[k]).copy()
                    arr[b] = arr[b][::-1]
                    ctx[k] = arr
                s2 = self.compute(method, pre_only, tune, a, y[a], b, use_store=False)
            finally:
                ctx.update(saved)
        else:
            d = self.data
            saved = {k: getattr(d, k).copy() for k in ("tool", "source", "family", "traj", "status")}
            try:
                for k in saved:
                    arr = getattr(d, k)
                    arr[b] = arr[b][::-1]
                s2 = self.compute(method, pre_only, tune, a, y[a], b, use_store=False)
            finally:
                for k, v in saved.items():
                    setattr(d, k, v)
        ok = bool(np.array_equal(s1, s2))
        _check(ok, "scores_invariant_to_scored_rows_metadata")
        return {"ok": ok, "max_abs_diff": float(np.abs(np.asarray(s1) - np.asarray(s2)).max())}


def start_checks():
    rec = PREREG_SHA.read_text(encoding="utf-8").split()[0]
    cur = sha256(PREREG)
    if rec != cur:
        raise SystemExit(f"prereg sha mismatch: recorded {rec}, current {cur}")
    if E.evaluate_sha256() != EVAL_SHA:
        raise SystemExit("evaluate.py sha changed")
    fits = OUT / "fits"
    first = min((p.stat().st_mtime for p in fits.rglob("*.npy")), default=None) if fits.is_dir() else None
    sha_t = PREREG_SHA.stat().st_mtime
    if first is not None and first < sha_t:
        raise SystemExit("a fit in the store is older than the prereg sha")
    return {"prereg_sha": cur, "evaluate_sha": E.evaluate_sha256(), "first_fit_mtime": first,
            "prereg_sha_mtime": sha_t}


def load_base(name, memo, threads, inp="robust_clip", od=None):
    from experiments.risk_loop.argus_loop import iter01_common as C1
    from experiments.risk_loop.argus_loop import iter11_diag_models as DM
    if name == "t7a":
        data, rows, _ = C1.headline_data(VIEW)
        feats = DM.load_feats(data, rows, ["L23:max", "L16:pre", "L23:pre"])
        del data
        return Base("t7a", rows, memo, T7aW(feats, rows), [None], threads)
    if od is None:
        od = OM.ObsData.load(VIEW, CACHE, (20,), with_extras=False)
    if "_remb" not in od.__dict__:   # speed only: 6 robust embeddings (5 outer folds of the shuffles cycle; ~10 MB each)
        od.__dict__["_remb"] = OM.LRU(6)
    return Base(name, od.head, memo, None, LIN_GRID if name == "lin" else CNN_GRID, threads, od, inp)


def _res_path(base):
    return OUT / f"result_{base}.json"


def _save(base, res):
    OUT.mkdir(parents=True, exist_ok=True)
    _res_path(base).write_text(json.dumps(E.to_jsonable(res), indent=1, ensure_ascii=False), encoding="utf-8")


def _oof_list(cv):
    return [np.asarray(cv["oof"][str(s)], np.float64) for s in cv["seeds"]]


def run_base(name, memo, threads, t7a_oofs=None, inp="robust_clip"):
    b = load_base(name, memo, threads, inp)
    rows = b.rows
    base_name = name
    if inp != "robust_clip":
        name = f"{name}@{inp}"
    _check(set(rows.split.tolist()) == {"train"}, "train_split_only")
    res = json.loads(_res_path(name).read_text(encoding="utf-8")) if _res_path(name).is_file() else {}
    res.update({"base": name, "base_ko": BASE_KO[base_name], "input": inp,
                "input_label": None if inp == "robust_clip" else "결과를 본 뒤 고른 입력 (prereg §7)", "grid": b.grid, "row_id_hash": OM.h_arr(rows.row_id),
                "usable_violations": usable_report(rows)})
    oofs = {}
    t0 = time.time()
    # 1) original base (same model, no method)
    cv = b.nested("none")
    oofs["none"] = _oof_list(cv)
    np.save(OUT / f"oof_{name}_none.npy", np.asarray(oofs["none"]))
    m = E.metrics(cv, rows)
    res["none"] = {"nested": compact(m), "chosen": cv["selection"]["chosen"]}
    log(f"[{name}] none nested {m['within_tool']['value']:.4f} ({(time.time() - t0) / 60:.1f} min, "
        f"memo hit {memo.hits} miss {memo.miss}, S-store hits {b.store_hits})")
    _save(name, res)
    if t7a_oofs is None:
        t7a_oofs = oofs["none"]
    # 2) main nested for the three methods (most important numbers first)
    for meth in W_METHODS:
        t1 = time.time()
        cv = b.nested(meth)
        oofs[meth] = _oof_list(cv)
        np.save(OUT / f"oof_{name}_{meth}.npy", np.asarray(oofs[meth]))
        m = E.metrics(cv, rows)
        modal = b.grid[E._modal_choice(cv)] if len(b.grid) > 1 else b.grid[0]
        r = res.setdefault(meth, {})
        r.update({"nested": compact(m), "chosen": cv["selection"]["chosen"], "modal_tune": modal,
                  "gain_vs_base": paired_gain(oofs[meth], oofs["none"], rows),
                  "gain_vs_t7a": paired_gain(oofs[meth], t7a_oofs, rows),
                  "luck_corrected": luck_correction(m["within_tool"]["value"], TRIES_BEFORE + 9 +
                                                    (10 if inp != "robust_clip" else 0))})
        log(f"[{name}] {meth} nested {m['within_tool']['value']:.4f} CI {m['within_tool']['ci95']['ci_low']:.3f}-"
            f"{m['within_tool']['ci95']['ci_high']:.3f} gain vs base {r['gain_vs_base']['gain']:+.4f} "
            f"vs T7-a {r['gain_vs_t7a']['gain']:+.4f} ({(time.time() - t1) / 60:.1f} min)")
        if m["within_tool"]["value"] >= 0.90:
            log(f"!!!!! [{name}] {meth} nested >= 0.90 -- validation stays CLOSED")
        _save(name, res)
    # rank correlation of OOF scores between methods (per seed Spearman, mean)
    from scipy.stats import spearmanr
    rc = {}
    for i, m1 in enumerate(METHODS):
        for m2 in METHODS[i + 1:]:
            rc[f"{m1}~{m2}"] = float(np.mean([spearmanr(a_, b_).correlation for a_, b_ in zip(oofs[m1], oofs[m2])]))
    res["rank_corr_between_methods"] = rc
    log(f"[{name}] rank corr", {k: round(v, 3) for k, v in rc.items()})
    _save(name, res)
    # 3) leak probes
    for meth in METHODS:
        res.setdefault("probe", {})[meth] = b.probe(meth)
    _save(name, res)
    # 4) pre-action-only controls, same method (before the shuffles: much cheaper for CNN-MLP; order only)
    for meth in W_METHODS:
        r = res[meth]
        if "pre_only" in r:
            continue
        t1 = time.time()
        cv = b.nested(meth, pre_only=True)
        o = _oof_list(cv)
        np.save(OUT / f"oof_{name}_{meth}_pre.npy", np.asarray(o))
        m = E.metrics(cv, rows, baselines=False)
        r["pre_only"] = {"nested": compact(m), "chosen": cv["selection"]["chosen"],
                         "main_minus_pre": paired_gain(oofs[meth], o, rows)}
        log(f"[{name}] {meth} pre-only control {m['within_tool']['value']:.4f} ({(time.time() - t1) / 60:.1f} min)")
        _save(name, res)
    # 5) shuffles (a) / (b) at the modal tuning value, fold seed 0
    for meth in W_METHODS:
        r = res[meth]
        if "shuffle_a" in r and "shuffle_b" in r:
            continue
        t1 = time.time()
        fp = b.make(meth)(r["modal_tune"])
        keep = ("within_tool_mean", "within_tool_sd", "within_tool_se", "within_tool", "pass",
                "within_tool_by_source_mean", "pooled_auroc_mean")
        sa = E.shuffle_test(fp, rows, N_SHUF, seed=0, within=("source",), n_jobs=1)
        sb = E.shuffle_test(fp, rows, N_SHUF, seed=0, within=("source", "family"), n_jobs=1)
        r["shuffle_a"] = {k: sa[k] for k in keep}
        r["shuffle_b"] = {k: sb[k] for k in keep}
        v = r["nested"]["value"]
        r["rules"] = {"gain_ci_low_gt_0": r["gain_vs_base"]["ci_low"] > 0,
                      "shuffle_a_in_0.45_0.55": abs(sa["within_tool_mean"] - 0.5) <= 0.05,
                      "margin_over_b": v - max(sb["within_tool_mean"], REF_B),
                      "margin_ge_0.10": v - max(sb["within_tool_mean"], REF_B) >= 0.10,
                      "beats_t7a": r["gain_vs_t7a"]["ci_low"] > 0}
        r["rules"]["improvement"] = bool(r["rules"]["gain_ci_low_gt_0"] and r["rules"]["shuffle_a_in_0.45_0.55"]
                                         and r["rules"]["margin_ge_0.10"])
        log(f"[{name}] {meth} shuffles a {sa['within_tool_mean']:.4f} b {sb['within_tool_mean']:.4f} "
            f"({(time.time() - t1) / 60:.1f} min)")
        _save(name, res)
    res["audit"] = dict(AUDIT)
    res["memo"] = {"hits": memo.hits, "miss": memo.miss, "s_store_hits": b.store_hits}
    res["minutes"] = (time.time() - t0) / 60
    _save(name, res)
    return res, oofs


def cmd_diag(threads):
    """prereg §7: fold seeds 0-2, pre-only 선형 기준 모델, method none, C by inner CV-4, inputs (a) / (b) / (c).
    Trigger: best of (b)/(c) by seed-mean; mean diff >= 0.05 AND paired family-bootstrap CI low > 0."""
    chk = start_checks()
    log("start checks ok", chk)
    memo = Memo(OUT)
    od = OM.ObsData.load(VIEW, CACHE, (20,), with_extras=False)
    res = {"rule": "best of (b)/(c) by seed 0-2 mean; (mean diff >= 0.05) AND (paired family-bootstrap CI low > 0) "
                   "-> add as variant labelled 'input chosen after seeing results' (8 + 2 = 10 tries)"}
    oo = {}
    for inp in INPUTS:
        b = load_base("lin", memo, threads, inp, od)
        cv = b.nested("none", pre_only=True, seeds=SEEDS3)
        oo[inp] = _oof_list(cv)
        m = E.metrics(cv, b.rows, baselines=False)
        res[inp] = {"value": m["within_tool"]["value"], "per_seed": m["within_tool"]["per_seed"],
                    "ci95": m["within_tool"]["ci95"], "pooled_auroc": m["pooled_auroc"],
                    "by_source": {s: v["value"] for s, v in m["within_tool"]["by_source"].items()},
                    "chosen_C": {s: [b.grid[i] for i in v] for s, v in cv["selection"]["chosen"].items()}}
        log(f"[diag] {inp}: {res[inp]['value']:.4f} per seed {res[inp]['per_seed']}")
    a = res["robust_clip"]["value"]
    best = max(("robust_noclip", "plain"), key=lambda k: res[k]["value"])
    other = "plain" if best == "robust_noclip" else "robust_noclip"
    res["best_alternative"] = best
    res["paired_gain_best_vs_a"] = paired_gain(oo[best], oo["robust_clip"], b.rows)
    res["paired_gain_other_vs_a"] = paired_gain(oo[other], oo["robust_clip"], b.rows)
    res["recovers"] = bool(res[best]["value"] - a >= 0.05 and res["paired_gain_best_vs_a"]["ci_low"] > 0)
    res["variant_input"] = best if res["recovers"] else None
    (OUT / "diag_clip.json").write_text(json.dumps(E.to_jsonable(res), indent=1), encoding="utf-8")
    log("[diag] recovers" if res["recovers"] else "[diag] no clear recovery", best)
    return res


def cmd_run(bases, threads, inp="robust_clip"):
    import torch
    torch.set_num_threads(int(threads))
    chk = start_checks()
    log("start checks ok", chk)
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "start_checks.json").write_text(json.dumps(chk, indent=1), encoding="utf-8")
    memo = Memo(OUT)
    t7 = OUT / "oof_t7a_none.npy"
    t7a_oofs = None
    for name in bases:
        if name != "t7a" and t7a_oofs is None:
            if not t7.is_file():
                raise SystemExit("run t7a first (its original OOF is the T7-a reference)")
            t7a_oofs = list(np.load(t7))
        if name == "t7a" and inp != "robust_clip":
            continue
        _, oofs = run_base(name, memo, threads, t7a_oofs, inp)
        if name == "t7a":
            t7a_oofs = oofs["none"]
        import gc
        gc.collect()
    log("DONE", dict(AUDIT))


def within_cell_rank_corr() -> dict:
    """Report only: Spearman of OOF scores between methods INSIDE each headline cell (positive-weighted mean over
    cells, mean over seeds). The pooled rank correlation mixes in per-cell offsets; this one does not."""
    from scipy.stats import spearmanr
    from experiments.risk_loop.argus_loop import iter01_common as C1
    _, rows, _ = C1.headline_data(VIEW)
    y, g = rows.y, E.headline_groups(rows)
    inc = [c for c in sorted(set(g.tolist())) if y[g == c].sum() >= E.MIN_POS and (y[g == c] == 0).sum() >= E.MIN_NEG]
    out = {}
    for base in [p.stem[4:-5] for p in OUT.glob("oof_*_none.npy")]:
        O = {m: np.load(OUT / f"oof_{base}_{m}.npy") for m in METHODS if (OUT / f"oof_{base}_{m}.npy").is_file()}
        r = {}
        ms = [m for m in METHODS if m in O]
        for i, m1 in enumerate(ms):
            for m2 in ms[i + 1:]:
                vals = []
                for a_, b_ in zip(O[m1], O[m2]):
                    num = den = 0.0
                    for c in inc:
                        k = g == c
                        rho = spearmanr(a_[k], b_[k]).correlation
                        if np.isfinite(rho):
                            num += rho * y[k].sum()
                            den += y[k].sum()
                    vals.append(num / den if den else None)
                r[f"{m1}~{m2}"] = E._mean(vals)
        out[base] = r
    return out


def cmd_report():
    out = {"prereg": str(PREREG.relative_to(REPO_ROOT)), "prereg_sha256": sha256(PREREG),
           "evaluate_sha256": E.evaluate_sha256(), "tries": {"before": TRIES_BEFORE, "after": TRIES_BEFORE + 9,
                                                             "before_conservative": TRIES_BEFORE_CONS,
                                                             "after_conservative": TRIES_BEFORE_CONS + 9},
           "bases": {}}
    for p in sorted(OUT.glob("result_*.json")):
        out["bases"][p.stem[len("result_"):]] = json.loads(p.read_text(encoding="utf-8"))
    if (OUT / "diag_clip.json").is_file():
        out["diag_clip"] = json.loads((OUT / "diag_clip.json").read_text(encoding="utf-8"))
    out["within_cell_rank_corr"] = within_cell_rank_corr()
    (IT14 / "within_tool_results.json").write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({b: {m: (v.get(m, {}).get("nested", {}).get("value")) for m in METHODS}
                      for b, v in out["bases"].items()}, indent=1))


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=("run", "report", "diag"))
    ap.add_argument("--inp", default="robust_clip", choices=INPUTS)
    ap.add_argument("--bases", default="t7a,lin,cnn")
    ap.add_argument("--threads", type=int, default=2)
    a = ap.parse_args(argv)
    if a.cmd == "run":
        bases = [x for x in a.bases.split(",") if x]
        for x in bases:
            if x not in BASES:
                raise SystemExit(f"unknown base {x}")
        cmd_run(bases, a.threads, a.inp)
    elif a.cmd == "diag":
        cmd_diag(a.threads)
    else:
        cmd_report()


if __name__ == "__main__":
    main()

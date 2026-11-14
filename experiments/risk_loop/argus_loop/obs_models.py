"""Phase-3 observation models: M1' + toggles T1-T6 (FROZEN prereg reports/risk-loop/argus-v1/loop/iter-13/prereg.md).

Structure (prereg §2, all toggles off):
  per observation u_i (layer 20 PCA-512 cache row) -> in-fold PCA 32 (training-fold observation rows only) +
  standardisation -> z_i; filters W (32 x K=4, no bias, shared by all observations): h_i = W^T z_i;
  f = [max_i h, mean_i h, h_pre] (12) -> linear head s = v.f + c.
  Loss = same-rollout (violation, normal) pair softplus loss (weighted mean, weight 1 per pair)
         + 0.2 * class-balanced BCE + beta ||W - W0||^2 + 1e-2 ||v||^2.
  W0: column 1 = M0 direction (same-rollout pair logistic on the pre_action rows' z, in fold), others 0;
  init: W0 + N(0, 0.01) on columns 2..K. Adam lr 0.01, 200 epochs, full batch. Model = mean over init seeds.
Toggles (prereg §3, exactly one OFF and one ON state):
  T1 focal loss (gamma 2) x class-balanced weights instead of BCE
  T2 training only: drop 25 % of observation rows (pre_action kept) + N(0, 0.1 * training SD) noise on z
  T3 auxiliary head on the same filters predicting report-content violations of report-tool rows of the
     training fold (rows whose (family, trajectory, unit) component touches the training rows and not the
     scored rows): epochs 1-50 auxiliary loss only, epochs 51-200 main loss + 0.3 * auxiliary loss. Redone per fit.
  T4 one Gaussian (Ledoit-Wolf) on the training-fold NORMAL rows' pre_action z (32); Mahalanobis distance is
     the 13th head input. No tool name anywhere.
  T5 same-rollout same-tool pairs weight x2; BCE weight x3 for normals of (tool x source) cells of the training
     fold that contain a violation.
  T6 rows with label_status nov_draft_rule: weight 0.8 (violation) / 0.99 (normal) in BCE and pairs
     (pair weight = product of the two row weights).
Structural knobs for the S stage (not toggles): K, layers (any subset of {16, 20, 23}; PCA and filters per
layer), pooling in the max slot {max, topk (top-k mean), attn (learned query, softmax over observations)}, head
{linear, mlp (depth 1-3, width, dropout, tanh)}, slots, obs_subset {all, pre, nopre}, filters {learned, m0_fixed}.

Signals read ONLY at training positions: tool, source, family/component, trajectory, label_status, report-row
labels. Scoring (``ObsModel.forward`` on test rows, ``FittedObsModel.score_u``) reads only observation vectors
and observation kinds (to find pre_action). Shuffle runs set ``aux_null_within`` so the report-row labels (T3)
and the rule-label status (T6) are permuted inside the same cells as the harness permutes y_train.
"""
from __future__ import annotations

import hashlib
import json
import math
import os
import sys
import threading
from collections import OrderedDict
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402
from experiments.risk_loop.argus_loop import obs_cache as OC  # noqa: E402

TOGGLES = ("T1", "T2", "T3", "T4", "T5", "T6")
BETAS = (0.1, 1.0, 10.0)
REPORT_TOOLS = frozenset({"write_report", "stop", "submit_result"})
RULE_STATUS = "nov_draft_rule"
FARS = (0.01, 0.05)
# prereg §3 fixed ON values (single state each)
PREREG_ON = {"T1": {"focal_gamma": 2.0},
             "T2": {"obs_drop": 0.25, "noise_rel": 0.1},
             "T3": {"aux_pre_epochs": 50, "aux_w": 0.3},
             "T4": {"t4_gaussians": 1},
             "T5": {"same_tool_pair_mult": 2.0, "cell_normal_mult": 3.0},
             "T6": {"rule_pos_w": 0.8, "rule_neg_w": 0.99}}
BASE = {"layers": (20,), "K": 4, "pca_k": 32, "pool": "max", "topk": 2, "head": "linear", "mlp_depth": 1,
        "mlp_width": 16, "mlp_dropout": 0.0, "slots": ("pool", "mean", "pre"), "obs_subset": "all",
        "filters": "learned", "beta": 1.0, "w_bce": 0.2, "head_l2": 1e-2, "epochs": 200, "lr": 1e-2,
        "init_seeds": (0,), "init_sd": 0.01, "m0_C": 0.01,
        "T1": 0, "T2": 0, "T3": 0, "T4": 0, "T5": 0, "T6": 0, "aux_null_within": None}
_NON_COMBO = ("beta", "init_seeds", "aux_null_within")


# ---------------------------------------------------------------------------------------------- configs

def combos() -> list[tuple[int, ...]]:
    """The 64 toggle combinations in the tie-break order: fewer toggles first, then T1..T6 lexicographic with
    ON before OFF (T1 alone, T2 alone, ..., then T1+T2, T1+T3, ...)."""
    allc = [tuple((m >> (5 - i)) & 1 for i in range(6)) for m in range(64)]
    return sorted(allc, key=lambda b: (sum(b), tuple(1 - x for x in b)))


def make_config(bits=(0, 0, 0, 0, 0, 0), beta=1.0, **over) -> dict:
    cfg = dict(BASE)
    for t, b in zip(TOGGLES, bits):
        cfg[t] = int(b)
    cfg["beta"] = float(beta)
    for k, v in over.items():
        if k not in cfg:
            raise KeyError(f"unknown config key {k!r}")
        cfg[k] = v
    cfg["layers"] = tuple(int(x) for x in cfg["layers"])
    cfg["init_seeds"] = tuple(int(x) for x in cfg["init_seeds"])
    cfg["slots"] = tuple(cfg["slots"])
    if cfg["aux_null_within"] is not None:
        cfg["aux_null_within"] = tuple(cfg["aux_null_within"])
    return cfg


def _canon(cfg: dict, drop=()) -> str:
    return json.dumps({k: (list(v) if isinstance(v, tuple) else v) for k, v in sorted(cfg.items()) if k not in drop},
                      sort_keys=True)


def config_id(cfg: dict) -> str:
    return hashlib.sha1(_canon(cfg).encode()).hexdigest()[:12]


def combo_key(cfg: dict) -> str:
    """Identity of a 'try' (TASK §6c: one try per combination; beta / init seeds / shuffle flag excluded)."""
    return hashlib.sha1(_canon(cfg, _NON_COMBO).encode()).hexdigest()[:12]


def combo_name(cfg: dict) -> str:
    on = [t for t in TOGGLES if cfg.get(t)]
    return "+".join(on) if on else "base"


def prereg_grid(**struct) -> list[dict]:
    """The 192 (combination, beta) nested-selection choices in prereg order (ties -> first)."""
    return [make_config(b, beta, **struct) for b in combos() for beta in BETAS]


def h_arr(*arrays) -> str:
    h = hashlib.sha1()
    for a in arrays:
        a = np.ascontiguousarray(np.asarray(a))
        h.update(str(a.dtype).encode())
        h.update(a.tobytes())
    return h.hexdigest()[:20]


# ---------------------------------------------------------------------------------------------- data

def concat_rows(a: E.Rows, b: E.Rows) -> E.Rows:
    kw = {k: np.concatenate([getattr(a, k), getattr(b, k)]) for k in E.Rows.__dataclass_fields__ if k != "info"}
    return E.Rows(**kw, info={"filter": "phase3 universe (headline + report-tool rows)"})


def seg_index(off: np.ndarray, rows: np.ndarray):
    """Global obs ids of ``rows`` (in order) and the local row index of each obs."""
    rows = np.asarray(rows, dtype=np.int64)
    starts, lens = off[rows], off[rows + 1] - off[rows]
    tot = int(lens.sum())
    seg = np.repeat(np.arange(len(rows)), lens)
    first = np.repeat(np.cumsum(lens) - lens, lens)
    idx = np.repeat(starts, lens) + (np.arange(tot) - first)
    return idx, seg


class LRU:
    def __init__(self, size=6):
        self.size, self.d, self.lock = size, OrderedDict(), threading.Lock()

    def get(self, k):
        with self.lock:
            if k in self.d:
                self.d.move_to_end(k)
                return self.d[k]
        return None

    def put(self, k, v):
        with self.lock:
            self.d[k] = v
            self.d.move_to_end(k)
            while len(self.d) > self.size:
                self.d.popitem(last=False)


@dataclass
class Emb:
    mu: np.ndarray   # [D]
    Q: np.ndarray    # [D, k]
    sd: np.ndarray   # [k]
    Z: np.ndarray    # [N_obs_universe, k] float32 (standardised)
    fit_rows: str    # hash of the training rows the PCA was fitted on


class ObsData:
    """Universe = headline rows (positions 0..n_head-1, exactly the rows the frozen harness evaluates) +
    report-tool rows (training-only extras for T3). Observation rows on the 32 grid for each universe row."""

    def __init__(self, head: E.Rows, extra: E.Rows, g: OC.Gathered, U: dict, info: dict | None = None):
        self.head, self.extra = head, extra
        self.rows = concat_rows(head, extra)
        self.n_head, self.n = len(head), len(self.rows)
        self.off, self.pre_obs = g.off, g.pre_local
        self.kind_code, self.token_index, self.n_obs32 = g.kind_code, g.token_index, g.n_obs32
        self.obs_kind = g.kind
        self.U = U
        self.obs_row = np.repeat(np.arange(self.n), np.diff(self.off))
        self.is_pre = np.zeros(len(self.obs_row), bool)
        self.is_pre[self.pre_obs] = True
        r = self.rows
        self.traj, self.tool = r.trajectory_id.astype(str), r.tool.astype(str)
        self.source, self.family = r.source.astype(str), r.family.astype(str)
        self.status = r.label_status.astype(str)
        self.comp = E.group_components(r)
        self.y_extra = np.full(self.n, np.nan)
        if len(extra):
            self.y_extra[self.n_head:] = extra.y.astype(np.float64)
        self.info = info or {}
        self._emb = LRU(6)
        if set(self.rows.split.tolist()) - {"train"}:
            raise PermissionError("phase-3 universe must contain train rows only")
        if np.isin(self.head.tool.astype(str), list(REPORT_TOOLS)).any():
            raise RuntimeError("report-tool rows must never be headline (evaluated) rows")

    @classmethod
    def load(cls, view_root, cache_root=OC.CACHE_DIR, layers=(20,), with_extras=True) -> "ObsData":
        from experiments.risk_loop.argus_loop import iter01_common as C1
        dh, head, hinfo = C1.headline_data(view_root)
        allowed = set(dh.rows.row_id.tolist())
        if with_extras:
            dr, rep, rinfo = C1.report_data(view_root)
            allowed |= set(dr.rows.row_id.tolist())
        else:
            rep, rinfo = head.subset([]), {}
        cache = OC.ObsCache(cache_root)
        ids = np.r_[head.row_id, rep.row_id]
        g = cache.gather(ids, allowed)
        U = {int(L): np.asarray(cache.layer(int(L))[g.obs_ids], dtype=np.float16) for L in layers}
        return cls(head, rep, g, U, {"headline": hinfo, "report": rinfo, "cache": str(cache_root),
                                     "pre_fallback": g.pre_fallback, "view": str(view_root)})

    # ------------------------------------------------------------------ fold-safe helpers
    def allowed_extras(self, pos_train, pos_test) -> np.ndarray:
        ext = np.arange(self.n_head, self.n)
        if not len(ext):
            return ext
        trc, tec = np.unique(self.comp[pos_train]), np.unique(self.comp[pos_test])
        ok = np.isin(self.comp[ext], trc) & ~np.isin(self.comp[ext], tec)
        sel = ext[ok]
        if np.intersect1d(self.family[sel], self.family[pos_test]).size:
            raise RuntimeError("leak: an extra row shares a family with the scored rows")
        return sel

    def embed(self, L: int, pos_train, k: int) -> Emb:
        pos_train = np.asarray(pos_train, dtype=np.int64)
        key = (int(L), int(k), h_arr(pos_train))
        e = self._emb.get(key)
        if e is not None:
            return e
        U = self.U[int(L)]
        idx, _ = seg_index(self.off, pos_train)
        D = U.shape[1]
        s1, n = np.zeros(D), 0
        for a in range(0, len(idx), 32768):
            x = U[idx[a:a + 32768]].astype(np.float64)
            s1 += x.sum(0)
            n += len(x)
        mu = s1 / n
        C = np.zeros((D, D))
        for a in range(0, len(idx), 32768):
            x = U[idx[a:a + 32768]].astype(np.float32) - mu.astype(np.float32)
            C += (x.T @ x).astype(np.float64)
        C /= max(n - 1, 1)
        w, V = np.linalg.eigh(C)
        kk = min(int(k), D)
        Q = V[:, ::-1][:, :kk].copy()
        sgn = np.sign(Q[np.argmax(np.abs(Q), axis=0), np.arange(kk)])
        Q *= np.where(sgn == 0, 1.0, sgn)
        Q32, mu32 = Q.astype(np.float32), mu.astype(np.float32)
        Z = np.empty((U.shape[0], kk), np.float32)
        for a in range(0, U.shape[0], 32768):
            Z[a:a + 32768] = (U[a:a + 32768].astype(np.float32) - mu32) @ Q32
        sd = Z[idx].std(0).astype(np.float32)
        sd[~(sd > 1e-8)] = 1.0
        Z /= sd
        e = Emb(mu32, Q32, sd, Z, key[2])
        self._emb.put(key, e)
        return e


# ---------------------------------------------------------------------------------------------- weights / pairs

def class_balanced(y) -> np.ndarray:
    y = np.asarray(y).astype(np.int64)
    w = np.ones(len(y))
    for c in (0, 1):
        m = y == c
        if m.any():
            w[m] = len(y) / (2.0 * m.sum())
    return w


def t6_weights(y, status, cfg) -> np.ndarray:
    w = np.ones(len(y))
    if cfg["T6"]:
        rule = np.asarray(status).astype(str) == RULE_STATUS
        y = np.asarray(y).astype(np.int64)
        w[rule & (y == 1)] = PREREG_ON["T6"]["rule_pos_w"]
        w[rule & (y == 0)] = PREREG_ON["T6"]["rule_neg_w"]
    return w


def bce_weights(y, tool, source, status, cfg) -> np.ndarray:
    w = class_balanced(y)
    y = np.asarray(y).astype(np.int64)
    if cfg["T5"]:
        cell = np.asarray([f"{t}|{s}" for t, s in zip(np.asarray(tool).astype(str), np.asarray(source).astype(str))])
        pos_cells = np.unique(cell[y == 1])
        w[(y == 0) & np.isin(cell, pos_cells)] *= PREREG_ON["T5"]["cell_normal_mult"]
    return w * t6_weights(y, status, cfg)


def pair_index(y, traj, tool, status, cfg):
    """Same-rollout (violation a, normal b) pairs of training rows; weight 1 (T5: same tool x2; T6: row weights)."""
    y = np.asarray(y).astype(np.int64)
    traj = np.asarray(traj).astype(str)
    order = np.argsort(traj, kind="stable")
    t = traj[order]
    bounds = np.r_[0, np.nonzero(t[1:] != t[:-1])[0] + 1, len(t)]
    I, J = [], []
    for a, b in zip(bounds[:-1], bounds[1:]):
        ii = order[a:b]
        p, n = ii[y[ii] == 1], ii[y[ii] == 0]
        if len(p) and len(n):
            pi, nj = np.meshgrid(p, n, indexing="ij")
            I.append(pi.ravel())
            J.append(nj.ravel())
    if not I:
        return np.zeros(0, np.int64), np.zeros(0, np.int64), np.zeros(0)
    I, J = np.concatenate(I), np.concatenate(J)
    w = np.ones(len(I))
    if cfg["T5"]:
        tool = np.asarray(tool).astype(str)
        w[tool[I] == tool[J]] *= PREREG_ON["T5"]["same_tool_pair_mult"]
    w6 = t6_weights(y, status, cfg)
    return I, J, w * w6[I] * w6[J]


def permute_within(values, cells, rng) -> np.ndarray:
    v = np.asarray(values).copy()
    cells = np.asarray(cells).astype(str)
    for c in sorted(set(cells.tolist())):
        p = np.nonzero(cells == c)[0]
        v[p] = v[rng.permutation(p)]
    return v


def m0_direction(Epre, y, traj, C) -> np.ndarray:
    """Same-rollout pair logistic (no intercept) on pre_action z of training rows (iter-04 T4-1 recipe)."""
    from experiments.risk_loop.argus_loop import iter04_models as M4
    w = M4.same_traj_pair_fit(np.asarray(Epre, np.float64), np.asarray(y).astype(np.int64), traj, C)
    return np.zeros(Epre.shape[1]) if w is None else np.asarray(w, np.float64)


def gaussian_fit(X):
    from sklearn.covariance import LedoitWolf
    lw = LedoitWolf().fit(np.asarray(X, np.float64))
    return lw.location_.astype(np.float64), lw.precision_.astype(np.float64)


def mahalanobis(X, mu, prec) -> np.ndarray:
    d = np.asarray(X, np.float64) - mu
    return np.sqrt(np.maximum(np.einsum("nd,de,ne->n", d, prec, d), 0.0))


# ---------------------------------------------------------------------------------------------- torch model

def _torch():
    import warnings
    import torch
    warnings.filterwarnings("ignore", message="Sparse invariant checks")
    return torch


class ObsModel:
    """Parameters with a replica dimension R (one replica per init seed). Pure function of observation
    tensors at scoring time."""

    def __init__(self, cfg, nL, k, W0, rng_seeds, F_aux):
        torch = _torch()
        self.cfg, self.nL, self.k, self.K, self.R = cfg, nL, k, cfg["K"], len(rng_seeds)
        R, K = self.R, self.K
        self.W0 = torch.tensor(np.broadcast_to(W0, (R,) + W0.shape).copy(), dtype=torch.float32)
        W = self.W0.clone()
        for r, s in enumerate(rng_seeds):
            g = torch.Generator().manual_seed(10_007 + int(s))
            if K > 1:
                W[r, :, :, 1:] += cfg["init_sd"] * torch.randn((nL, k, K - 1), generator=g)
        self.W = W.requires_grad_(cfg["filters"] == "learned")
        C = nL * K
        self.F = len(cfg["slots"]) * C + (1 if cfg["T4"] else 0)
        self.params = [self.W] if cfg["filters"] == "learned" else []
        self.q = None
        if cfg["pool"] == "attn":
            self.q = torch.zeros((R, nL, k), requires_grad=True)
            self.params.append(self.q)
        self.head_w, self.head_b = [], []
        if cfg["head"] == "linear":
            self.head_w.append(torch.zeros((R, self.F, 1), requires_grad=True))
            self.head_b.append(torch.zeros((R, 1), requires_grad=True))
        else:
            dims = [self.F] + [int(cfg["mlp_width"])] * int(cfg["mlp_depth"]) + [1]
            for i in range(len(dims) - 1):
                g = torch.Generator().manual_seed(20_011 + 97 * i + int(rng_seeds[0]))
                self.head_w.append((torch.randn((R, dims[i], dims[i + 1]), generator=g) /
                                    math.sqrt(dims[i])).requires_grad_(True))
                self.head_b.append(torch.zeros((R, dims[i + 1]), requires_grad=True))
        self.params += self.head_w + self.head_b
        self.aux_w = self.aux_b = None
        if F_aux:
            self.aux_w = torch.zeros((R, F_aux), requires_grad=True)
            self.aux_b = torch.zeros((R,), requires_grad=True)
            self.params += [self.aux_w, self.aux_b]

    # --------------------------------------------------------------
    def filters(self, Z):
        """Z [nL, N, k] or [R, nL, N, k] -> H [R, N, nL*K]."""
        torch = _torch()
        if Z.dim() == 3:
            H = torch.einsum("lnd,rldk->rnlk", Z, self.W)
        else:
            H = torch.einsum("rlnd,rldk->rnlk", Z, self.W)
        return H.reshape(H.shape[0], H.shape[1], -1)

    def _zl(self, Z, l):
        return Z[l].unsqueeze(0) if Z.dim() == 3 else Z[:, l]

    def features(self, Z, seg, n_rows, pre_idx, mask, pad, dist, A, static=None):
        """f = [pool slot, mean slot, pre slot] (+ T4 distance). Gradients flow only through small gathered
        tensors: max / top-k = z of the selected observation(s) @ W (indices found without grad; same
        subgradient as amax except at exact ties), mean = (masked mean of z) @ W (z is constant)."""
        torch = _torch()
        R, K, nL = self.R, self.K, self.nL
        N = Z.shape[-2]
        rr = torch.arange(R).view(R, 1, 1)
        with torch.no_grad():
            H = self.filters(Z)                                   # [R, N, nL*K]
            mf = mask.to(torch.float32).unsqueeze(-1)              # [R, N, 1]
            if static is not None and "cnt" in static:
                cnt = static["cnt"]
            else:
                cnt = seg_sum(A, mf)                              # [R, n_rows, 1]
                if static is not None:
                    static["cnt"] = cnt
        pooled_p, mean_p, pre_p, arg_p, attn_w = [], [], [], [], []
        kind = self.cfg["pool"]
        for l in range(nL):
            Zl = self._zl(Z, l)                                   # [R|1, N, k]
            Ze = Zl.expand(R, -1, -1)
            Wl = self.W[:, l]                                     # [R, k, K]
            with torch.no_grad():
                key = f"zmean{l}"
                if static is not None and key in static:
                    zmean = static[key]
                else:
                    zmean = seg_sum(A, Ze * mf) / cnt             # [R, n_rows, k]
                    if static is not None:
                        static[key] = zmean
            mean_p.append(torch.einsum("rnd,rdk->rnk", zmean, Wl))
            pre_p.append(torch.einsum("rnd,rdk->rnk", Ze[:, pre_idx, :], Wl))
            if kind == "max":
                with torch.no_grad():
                    Hm = torch.where(mask.unsqueeze(-1), H[:, :, l * K:(l + 1) * K], float("-inf"))
                    si = seg.view(1, N, 1).expand(R, N, K)
                    amax = torch.full((R, n_rows, K), float("-inf")).scatter_reduce(1, si, Hm, "amax", include_self=True)
                    ids = torch.arange(N).view(1, N, 1).expand(R, N, K)
                    cand = torch.where(Hm == amax[:, seg, :], ids, N)
                    first = torch.full((R, n_rows, K), N, dtype=torch.long).scatter_reduce(1, si, cand, "amin",
                                                                                           include_self=True)
                Zg = Ze[rr, first]                                # [R, n_rows, K, k]
                pooled_p.append(torch.einsum("rnkd,rdk->rnk", Zg, Wl))
                arg_p.append(first)
            elif kind == "topk":
                kk = min(int(self.cfg["topk"]), pad.shape[1])
                with torch.no_grad():
                    Hm = torch.where(mask.unsqueeze(-1), H[:, :, l * K:(l + 1) * K], float("-inf"))
                    Hp = torch.cat([Hm, torch.full((R, 1, K), float("-inf"))], 1)[:, pad, :]  # [R, n, maxn, K]
                    top = torch.topk(Hp, kk, dim=2)
                    valid = torch.isfinite(top.values)
                    obs = pad.unsqueeze(0).unsqueeze(-1).expand(R, -1, -1, K).gather(2, top.indices)
                    obs = torch.where(valid, obs, 0)
                Zg = Ze[torch.arange(R).view(R, 1, 1, 1), obs]     # [R, n, kk, K, k]
                vals = torch.einsum("rnjkd,rdk->rnjk", Zg, Wl)
                vf = valid.to(vals.dtype)
                pooled_p.append((vals * vf).sum(2) / vf.sum(2).clamp_min(1))
                arg_p.append(obs[:, :, 0, :])
            elif kind == "attn":
                a = torch.einsum("rnd,rd->rn", Ze, self.q[:, l])
                am = torch.where(mask, a, float("-inf"))
                with torch.no_grad():
                    mx = torch.full((R, n_rows), float("-inf")).scatter_reduce(1, seg.view(1, N).expand(R, N), am,
                                                                               "amax", include_self=True)
                e = torch.exp(am - mx[:, seg]) * mask.to(a.dtype)
                den = seg_sum(A, e.unsqueeze(-1))[..., 0]
                w = e / den[:, seg]
                zbar = seg_sum(A, w.unsqueeze(-1) * Ze)
                pooled_p.append(torch.einsum("rnd,rdk->rnk", zbar, Wl))
                attn_w.append(w.detach())
            else:
                raise ValueError(kind)
        pooled, mean, pre = torch.cat(pooled_p, -1), torch.cat(mean_p, -1), torch.cat(pre_p, -1)
        parts = {"pool": pooled, "mean": mean, "pre": pre}
        f = torch.cat([parts[s] for s in self.cfg["slots"]], -1)
        f_aux = f
        if dist is not None:
            f = torch.cat([f, dist.view(1, -1, 1).expand(f.shape[0], -1, 1)], -1)
        extra = {"H": H, "pooled": pooled, "arg": torch.cat(arg_p, -1) if arg_p else None,
                 "attn_w": torch.stack(attn_w, -1) if attn_w else None}
        return f, f_aux, extra, pooled

    def head(self, f, train):
        torch = _torch()
        x = f
        n = len(self.head_w)
        for i in range(n):
            x = torch.einsum("rnf,rfo->rno", x, self.head_w[i]) + self.head_b[i].unsqueeze(1)
            if i < n - 1:
                x = torch.tanh(x)
                if train and self.cfg["mlp_dropout"] > 0:
                    x = torch.nn.functional.dropout(x, float(self.cfg["mlp_dropout"]), True)
        return x.squeeze(-1)

    def aux_head(self, f_aux):
        return (f_aux * self.aux_w.unsqueeze(1)).sum(-1) + self.aux_b.unsqueeze(1)

    def reg(self):
        torch = _torch()
        r = self.cfg["beta"] * ((self.W - self.W0) ** 2).sum(dim=(1, 2, 3)) if self.cfg["filters"] == "learned" \
            else torch.zeros(self.R)
        hw = sum((w ** 2).sum(dim=tuple(range(1, w.dim()))) for w in self.head_w)
        return r + self.cfg["head_l2"] * hw

    def numpy_params(self) -> dict:
        out = {"W": self.W.detach().numpy().copy(), "head_w": [w.detach().numpy().copy() for w in self.head_w],
               "head_b": [b.detach().numpy().copy() for b in self.head_b]}
        if self.q is not None:
            out["q"] = self.q.detach().numpy().copy()
        return out


def seg_matrix(seg_np: np.ndarray, n_rows: int):
    """Sparse [n_rows, N] row-indicator matrix (segment sums by sparse matmul; much faster than index_add)."""
    torch = _torch()
    N = len(seg_np)
    ind = torch.from_numpy(np.vstack([seg_np.astype(np.int64), np.arange(N, dtype=np.int64)]))
    return torch.sparse_coo_tensor(ind, torch.ones(N), (n_rows, N), check_invariants=False).coalesce()


def seg_sum(A, X):
    """X [R, N, C] -> [R, n_rows, C] segment sums."""
    torch = _torch()
    R, N, C = X.shape
    out = torch.sparse.mm(A, X.permute(1, 0, 2).reshape(N, R * C))
    return out.reshape(A.shape[0], R, C).permute(1, 0, 2)


def _loss_pointwise(torch, s, y, w, gamma):
    """Weighted mean of BCE (gamma 0) or focal loss (gamma > 0) with logits s [R, n]."""
    bce = torch.nn.functional.binary_cross_entropy_with_logits(s, y.expand_as(s), reduction="none")
    if gamma > 0:
        p = torch.sigmoid(s)
        pt = torch.where(y.expand_as(s) > 0.5, p, 1 - p)
        bce = (1 - pt) ** gamma * bce
    return (bce * w).sum(-1) / w.sum()


@dataclass
class FitOut:
    score: np.ndarray            # [n_test] float64 (mean over replicas)
    scores_rep: np.ndarray       # [R, n_test] float32
    thr: dict                    # far -> threshold from in-sample training normals (headline rows)
    argmax: np.ndarray           # [n_test] local obs position (32 grid order) of the dominant filter's max
    audit: dict = field(default_factory=dict)
    model: "FittedObsModel | None" = None


def _constant(n_test, R, audit):
    return FitOut(np.zeros(n_test), np.zeros((R, n_test), np.float32), {f: 0.0 for f in FARS},
                  np.zeros(n_test, np.int16), {**audit, "constant": True})


def _obs_tensors(torch, data, embs, layers, rows, cfg):
    """Observation tensors of universe rows: Z [nL, N, k], seg, pre index, base pool mask, pad index."""
    idx, seg = seg_index(data.off, rows)
    Z = torch.from_numpy(np.stack([embs[L].Z[idx] for L in layers]))
    is_pre = data.is_pre[idx]
    sub = cfg["obs_subset"]
    if sub == "all":
        sel = np.ones(len(idx), bool)
    elif sub == "pre":
        sel = is_pre.copy()
    elif sub == "nopre":
        sel = ~is_pre
        has = np.bincount(seg[sel], minlength=len(rows)) > 0
        sel |= is_pre & ~has[seg]
    else:
        raise ValueError(sub)
    lens = np.diff(np.r_[0, np.cumsum(np.bincount(seg, minlength=len(rows)))])
    start = np.cumsum(lens) - lens
    pre_local = np.nonzero(is_pre)[0]
    if len(pre_local) != len(rows):
        raise RuntimeError("every row must have exactly one pre (or fallback) observation")
    pad = None
    if cfg["pool"] == "topk":
        maxn = int(lens.max())
        pad = np.full((len(rows), maxn), len(idx), np.int64)
        for j in range(maxn):
            ok = lens > j
            pad[ok, j] = start[ok] + j
        pad = torch.from_numpy(pad)
    return (Z, torch.from_numpy(seg.astype(np.int64)), torch.from_numpy(pre_local.astype(np.int64)),
            torch.from_numpy(sel), torch.from_numpy(is_pre), pad, idx, seg, start, seg_matrix(seg, len(rows)))


def fit_obs(data: ObsData, cfg: dict, pos_train, y_train, pos_test, *, keep_model=False, threads=None) -> FitOut:
    torch = _torch()
    if threads:
        torch.set_num_threads(int(threads))
    pos_train = np.asarray(pos_train, dtype=np.int64)
    pos_test = np.asarray(pos_test, dtype=np.int64)
    y_train = np.asarray(y_train).astype(np.int64)
    if len(pos_train) and (pos_train.max() >= data.n_head or (len(pos_test) and pos_test.max() >= data.n_head)):
        raise ValueError("fit_predict positions must be headline positions")
    if np.intersect1d(pos_train, pos_test).size:
        raise ValueError("training and scored rows overlap")
    layers, k, R = cfg["layers"], int(cfg["pca_k"]), len(cfg["init_seeds"])
    audit = {"cfg": config_id(cfg), "train_hash": h_arr(pos_train), "test_hash": h_arr(pos_test),
             "n_train": int(len(pos_train)), "pca_rows_hash": h_arr(pos_train)}
    if len(np.unique(y_train)) < 2:
        return _constant(len(pos_test), R, audit)
    embs = {L: data.embed(L, pos_train, k) for L in layers}
    audit["pca_fit_rows_match"] = all(embs[L].fit_rows == h_arr(pos_train) for L in layers)
    # ---- training-only side information
    extras = data.allowed_extras(pos_train, pos_test) if cfg["T3"] else np.zeros(0, np.int64)
    status_tr = data.status[pos_train].copy()
    y_ex = data.y_extra[extras].astype(np.int64) if len(extras) else np.zeros(0, np.int64)
    if cfg["aux_null_within"]:
        rng = np.random.default_rng(int(h_arr(pos_train, y_train.astype(np.int8), np.frombuffer(
            "|".join(cfg["aux_null_within"]).encode(), np.uint8))[:15], 16))
        cells_tr = ["\x1f".join(v) for v in zip(*[getattr(data.rows, c)[pos_train].astype(str)
                                                    for c in cfg["aux_null_within"]])]
        status_tr = permute_within(status_tr, cells_tr, rng)
        if len(extras):
            cells_ex = ["\x1f".join(v) for v in zip(*[getattr(data.rows, c)[extras].astype(str)
                                                        for c in cfg["aux_null_within"]])]
            y_ex = permute_within(y_ex, cells_ex, rng)
    audit.update({"extras_hash": h_arr(extras), "n_extras": int(len(extras)),
                  "aux_shuffled": bool(cfg["aux_null_within"]), "extras": extras,
                  "extras_comp_ok": bool(np.isin(data.comp[extras], data.comp[pos_train]).all()
                                         and not np.isin(data.comp[extras], data.comp[pos_test]).any())})
    rows_fit = np.r_[pos_train, extras]
    n_tr = len(pos_train)
    Z, seg, pre_i, sel, is_pre, pad, idx, seg_np, _, A = _obs_tensors(torch, data, embs, layers, rows_fit, cfg)
    n_fit = len(rows_fit)
    # ---- M0 direction per layer (training headline rows' pre_action z)
    W0 = np.zeros((len(layers), k, int(cfg["K"])), np.float32)
    pre_glob = idx[pre_i.numpy()]
    for li, L in enumerate(layers):
        Epre = embs[L].Z[pre_glob[:n_tr]]
        W0[li, :, 0] = m0_direction(Epre, y_train, data.traj[pos_train], cfg["m0_C"])
    # ---- T4: one Gaussian on training normals' pre_action z (all layers concatenated)
    dist_fit = dist_test = None
    t4 = None
    if cfg["T4"]:
        Pfit = np.concatenate([embs[L].Z[pre_glob] for L in layers], 1)
        norm = np.nonzero(y_train == 0)[0]
        mu, prec = gaussian_fit(Pfit[norm])
        t4 = {"mu": mu, "prec": prec}
        dist_fit = torch.tensor(mahalanobis(Pfit, mu, prec), dtype=torch.float32)
        audit.update({"t4_rows_hash": h_arr(pos_train[norm]), "t4_gaussians": 1,
                      "t4_rows_are_train_normals": bool(np.all(y_train[norm] == 0))})
    # ---- labels / weights / pairs
    yt = torch.tensor(y_train, dtype=torch.float32)
    wb = torch.tensor(bce_weights(y_train, data.tool[pos_train], data.source[pos_train], status_tr, cfg),
                      dtype=torch.float32)
    I, J, pw = pair_index(y_train, data.traj[pos_train], data.tool[pos_train], status_tr, cfg)
    I_t, J_t, pw_t = torch.from_numpy(I), torch.from_numpy(J), torch.tensor(pw, dtype=torch.float32)
    gamma = PREREG_ON["T1"]["focal_gamma"] if cfg["T1"] else 0.0
    use_aux = bool(cfg["T3"]) and len(extras) > 0
    if use_aux:
        ya = torch.tensor(y_ex, dtype=torch.float32)
        wa = torch.tensor(class_balanced(y_ex), dtype=torch.float32)
    audit.update({"n_pairs": int(len(I)), "aux_used": use_aux})
    model = ObsModel(cfg, len(layers), k, W0, cfg["init_seeds"],
                     len(cfg["slots"]) * len(layers) * int(cfg["K"]) if cfg["T3"] else 0)
    opt = torch.optim.Adam(model.params, lr=float(cfg["lr"]))
    gen = torch.Generator().manual_seed(int(h_arr(np.asarray(cfg["init_seeds"]))[:8], 16))
    drop = PREREG_ON["T2"]["obs_drop"] if cfg["T2"] else 0.0
    noise = PREREG_ON["T2"]["noise_rel"] if cfg["T2"] else 0.0
    sd_tr = Z[:, seg < n_tr].std(dim=1, keepdim=True) if noise else None  # [nL, 1, k] training-row SD
    base_mask = sel.unsqueeze(0).expand(R, -1)
    pre_ep = PREREG_ON["T3"]["aux_pre_epochs"] if cfg["T3"] else 0
    static = {}
    bank = None
    aux_w = PREREG_ON["T3"]["aux_w"]
    for ep in range(1, int(cfg["epochs"]) + 1):
        opt.zero_grad()
        mask = base_mask
        if drop:
            keep = torch.rand((R, len(sel)), generator=gen) >= drop
            mask = base_mask & (keep | is_pre.unsqueeze(0))
            if cfg["obs_subset"] == "nopre":  # pre is always kept otherwise, so no row can end up empty
                left = seg_sum(A, mask.to(torch.float32).unsqueeze(-1))[..., 0]
                mask = mask | ((left[:, seg] == 0) & base_mask)
        Zin = Z
        if noise:
            # i.i.d. N(0, (0.1 * training SD)^2) per coordinate: a bank of 8 Gaussian draws, rows re-permuted
            # every epoch (exact Gaussian marginals; ~4x cheaper than a fresh randn of [R, nL, N, k] per epoch)
            if bank is None:
                bank = torch.randn((8, R) + tuple(Z.shape), generator=gen)
            perm = torch.randperm(Z.shape[1], generator=gen)
            Zin = Z.unsqueeze(0) + noise * sd_tr.unsqueeze(0) * bank[ep % 8][:, :, perm, :]
        f, f_aux, _, _ = model.features(Zin, seg, n_fit, pre_i, mask, pad, dist_fit, A,
                                        None if (drop or noise) else static)
        reg = model.reg()
        if use_aux:
            l_aux = _loss_pointwise(torch, model.aux_head(f_aux[:, n_tr:, :]), ya, wa, 0.0) + \
                cfg["head_l2"] * (model.aux_w ** 2).sum(-1)
        if ep <= pre_ep:
            loss = (l_aux + reg) if use_aux else reg
        else:
            s = model.head(f[:, :n_tr, :], True)
            l_pt = _loss_pointwise(torch, s, yt, wb, gamma)
            l_pair = ((torch.nn.functional.softplus(-(s[:, I_t] - s[:, J_t])) * pw_t).sum(-1) / pw_t.sum()
                      if len(I) else torch.zeros(R))
            loss = l_pair + cfg["w_bce"] * l_pt + reg + (aux_w * l_aux if use_aux else 0.0)
        loss.sum().backward()
        opt.step()
    # ---- in-sample training scores (thresholds) and test scores
    with torch.no_grad():
        f, _, _, _ = model.features(Z, seg, n_fit, pre_i, base_mask, pad, dist_fit, A, {})
        s_tr = model.head(f[:, :n_tr, :], False).mean(0).numpy().astype(np.float64)
    norm_scores = s_tr[y_train == 0]
    thr = {far: float(np.quantile(norm_scores, 1.0 - far)) for far in FARS}
    Zt, segt, pret, selt, _, padt, idxt, segt_np, startt, At = _obs_tensors(torch, data, embs, layers, pos_test, cfg)
    if cfg["T4"]:
        Ptest = np.concatenate([embs[L].Z[idxt[pret.numpy()]] for L in layers], 1)
        dist_test = torch.tensor(mahalanobis(Ptest, t4["mu"], t4["prec"]), dtype=torch.float32)
    sc, am = _predict(torch, model, Zt, segt, len(pos_test), pret, selt, padt, dist_test, segt_np, startt, At)
    fitted = None
    if keep_model:
        fitted = FittedObsModel.from_fit(cfg, layers, embs, model, t4, s_tr, thr)
    audit["scoring_inputs"] = "z(obs), obs selection mask, pre index" + (", T4 Gaussian" if cfg["T4"] else "")
    return FitOut(sc.mean(0).astype(np.float64), sc.astype(np.float32), thr, am, audit, fitted)


def _predict(torch, model, Z, seg, n_rows, pre_i, sel, pad, dist, seg_np, start, A):
    """Scores [R, n] and argmax obs position (replica 0; filter with the largest |d s / d pool_k * pool_k|)."""
    R = model.R
    mask = sel.unsqueeze(0).expand(R, -1)
    with torch.enable_grad():
        f, _, extra, pooled = model.features(Z, seg, n_rows, pre_i, mask, pad, dist, A)
        f = f.detach().requires_grad_(True)
        s = model.head(f, False)
        s[0].sum().backward()
    sc = s.detach().numpy()
    if "pool" not in model.cfg["slots"]:
        return sc, np.zeros(n_rows, np.int16)
    C = pooled.shape[-1]
    slot = list(model.cfg["slots"]).index("pool")
    g = f.grad[0, :, slot * C:(slot + 1) * C].numpy()
    kstar = np.abs(g * pooled[0].detach().numpy()).argmax(1)
    if model.cfg["pool"] == "attn":
        w = extra["attn_w"][0].numpy()                       # [N, nL]
        vals = np.where(sel.numpy(), w[np.arange(len(seg_np)), kstar[seg_np] // model.K], -np.inf)
        order = np.lexsort((-vals, seg_np))
        best = order[np.r_[0, np.nonzero(np.diff(seg_np[order]))[0] + 1]]
    else:
        best = extra["arg"][0].numpy()[np.arange(n_rows), kstar]
    return sc, (best - start[np.arange(n_rows)]).astype(np.int16)


# ---------------------------------------------------------------------------------------------- numpy export

@dataclass
class FittedObsModel:
    """Numpy copy of a fitted model (all replicas). ``score_u`` = scoring from PCA-512 cache rows."""
    cfg: dict
    layers: tuple
    mu: dict
    Q: dict
    sd: dict
    params: dict
    t4: dict | None
    train_scores: np.ndarray
    thr: dict

    @classmethod
    def from_fit(cls, cfg, layers, embs, model, t4, s_tr, thr):
        return cls(dict(cfg), tuple(layers), {L: embs[L].mu for L in layers}, {L: embs[L].Q for L in layers},
                   {L: embs[L].sd for L in layers}, model.numpy_params(), t4, np.sort(s_tr), dict(thr))

    def z_rows(self, u_by_layer: dict) -> list:
        return [((np.asarray(u_by_layer[L], np.float32) - self.mu[L]) @ self.Q[L]) / self.sd[L] for L in self.layers]

    def score_u(self, u_by_layer: dict, kinds) -> dict:
        """One step: u_by_layer[L] = [n, D] cache rows on the 32 grid, kinds = their kinds."""
        z = self.z_rows(u_by_layer)
        return score_from_h(self, [zl.astype(np.float64) @ self.params["W"][:, li].astype(np.float64)
                                   for li, zl in enumerate(z)], z, kinds)


def score_from_h(m, h_layers, z_layers, kinds) -> dict:
    """Shared numpy pooling + head. h_layers[l] = [R, n, K] (from z @ W or folded x~ @ W_eff + b_eff)."""
    cfg, p = m.cfg, m.params
    kinds = list(kinds)
    n = len(kinds)
    pre = [i for i, kd in enumerate(kinds) if kd == "pre_action"]
    pre_i = pre[-1] if pre else n - 1
    sel = np.ones(n, bool)
    if cfg["obs_subset"] == "pre":
        sel[:] = False
        sel[pre_i] = True
    elif cfg["obs_subset"] == "nopre":
        sel[pre_i] = False
        if not sel.any():
            sel[pre_i] = True
    H = np.concatenate(h_layers, -1)  # [R, n, C]
    Hs = H[:, sel, :]
    if cfg["pool"] == "max":
        pooled = Hs.max(1)
    elif cfg["pool"] == "topk":
        kk = min(int(cfg["topk"]), Hs.shape[1])
        pooled = -np.sort(-Hs, axis=1)[:, :kk, :].mean(1)
    else:
        K = cfg["K"]
        pooled = np.zeros((H.shape[0], H.shape[2]))
        for li, zl in enumerate(z_layers):
            a = np.einsum("nd,rd->rn", np.asarray(zl, np.float64)[sel], p["q"][:, li].astype(np.float64))
            a = np.exp(a - a.max(1, keepdims=True))
            a /= a.sum(1, keepdims=True)
            pooled[:, li * K:(li + 1) * K] = np.einsum("rn,rnk->rk", a, Hs[:, :, li * K:(li + 1) * K])
    parts = {"pool": pooled, "mean": Hs.mean(1), "pre": H[:, pre_i, :]}
    f = np.concatenate([parts[s] for s in cfg["slots"]], -1)
    if cfg["T4"]:
        zp = np.concatenate([np.asarray(zl, np.float64)[pre_i] for zl in z_layers])
        d = mahalanobis(zp[None, :], m.t4["mu"], m.t4["prec"])[0]
        f = np.concatenate([f, np.full((f.shape[0], 1), d)], -1)
    s, grad = head_np(p, f)
    slot = list(cfg["slots"]).index("pool") if "pool" in cfg["slots"] else None
    arg = None
    if slot is not None:
        C = pooled.shape[1]
        kstar = int(np.abs(grad[0, slot * C:(slot + 1) * C] * pooled[0]).argmax())
        cand = np.nonzero(sel)[0]
        arg = int(cand[int(np.argmax(H[0, sel, kstar]))])
    return {"score": float(np.mean(s)), "scores_rep": s, "pre_index": pre_i, "argmax_obs": arg,
            "pooled": pooled, "fallback_pre": not pre}


def head_np(p, f):
    """Head forward + d s / d f for each replica. f [R, F]."""
    x, acts = f.astype(np.float64), []
    n = len(p["head_w"])
    for i in range(n):
        x = np.einsum("rf,rfo->ro", x, p["head_w"][i].astype(np.float64)) + p["head_b"][i]
        if i < n - 1:
            x = np.tanh(x)
            acts.append(x)
    s = x[:, 0]
    g = p["head_w"][-1][:, :, 0].astype(np.float64)
    for i in range(n - 2, -1, -1):
        g = g * (1 - acts[i] ** 2)
        g = np.einsum("ro,rfo->rf", g, p["head_w"][i].astype(np.float64))
    return s, g


# ---------------------------------------------------------------------------------------------- harness glue

def make_fp(data: ObsData, cfg: dict, threads=None):
    """fit_predict(pos_train, y_train, pos_test) for the frozen harness (X_or_rowids=None)."""
    def fp(pos_train, y_train, pos_test):
        return fit_obs(data, cfg, pos_train, y_train, pos_test, threads=threads).score
    return fp


class NestedFP:
    """fit_predict that performs the frozen-harness nested selection INSIDE the training rows it receives
    (same algorithm as evaluate.nested_cv: inner StratifiedGroupKFold(inner_splits, seed) on the training rows,
    best inner within-tool AUROC, ties -> first grid entry, refit on all training rows). Used for the shuffle
    (b) runs that redo the selection with the permuted labels (prereg §4.4). Inner folds are stratified on the
    labels it is given (the permuted ones in a shuffle run, the true ones otherwise)."""

    def __init__(self, make_fit_predict, grid, rows: E.Rows, seed: int, inner_splits: int = 4, log=None):
        self.make, self.grid, self.rows, self.seed, self.inner = make_fit_predict, list(grid), rows, seed, inner_splits
        self.chosen, self.log = [], log

    def __call__(self, pos_train, y_train, pos_test):
        from experiments.risk_loop import harness as H
        pos_train = np.asarray(pos_train, np.int64)
        y_train = np.asarray(y_train).astype(np.int64)
        inner_rows = self.rows.subset(pos_train)
        inner_rows.label = y_train.astype(np.float64)
        folds = E.make_folds(inner_rows, self.inner, self.seed)
        scores = []
        for g in self.grid:
            fp = self.make(g)
            io = np.full(len(pos_train), np.nan)
            for ia, ib in folds:
                io[ib] = np.asarray(fp(pos_train[ia], y_train[ia].copy(), pos_train[ib]), np.float64)
            v = E.within_tool_auroc(io, y_train, E.headline_groups(inner_rows))["value"]
            if v is None:
                v = H.auroc(io, y_train)
            scores.append(-math.inf if v is None else float(v))
        best = int(np.argmax(scores))
        self.chosen.append(best)
        return self.make(self.grid[best])(pos_train, y_train.copy(), pos_test)


def scoring_signature_ok() -> bool:
    """Monitor check 4: no tool/source/family/trajectory/scenario/step argument in the scoring functions."""
    import inspect
    banned = {"tool", "source", "family", "trajectory", "scenario", "step", "step_index", "label", "y"}
    fns = [_predict, score_from_h, FittedObsModel.score_u, head_np]
    return all(not (set(inspect.signature(f).parameters) & banned) for f in fns)

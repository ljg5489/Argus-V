"""Phase-3 cycle-1 S stage: the convex baseline S-0 and the small CNN-MLP S-F (DRAFT prereg
reports/risk-loop/argus-v1/loop/iter-13/prereg-S-draft.md §2). Strictly additive: obs_models.py is imported, never
modified (the running cycle-1 grid imports it). Called through ``obs_models_s.fit_s``.

Shared input (both models, label-free, training fold only):
  per observation point u (layer-20 PCA-512 cache row) -> robust scale (median, IQR / 1.349 per dimension, over
  the training rows' observation points) -> clip +-3 -> PCA 32 (fitted on the same points) -> divide by the
  training SD of each coordinate = z (32). ``robust_embed``.

S-0 convex baseline: x = [max over the row's observation points of each z coordinate (32), z of the pre_action
  point (32)] (+ T4 Mahalanobis distance) -> standardised with training-row mean / SD -> L2 logistic regression
  (2-class softmax == sigmoid). Objective (convex; strictly convex in w, unique minimiser):
      J(w, b) = 0.5 ||w||^2 + (C n / w_bce) * (pair_w * pair_mean + w_bce * bce_mean)
  bce_mean = class-balanced (bce_weights) mean BCE, pair_mean = same-rollout pair softplus loss (pair_index), the
  same terms and the same 1 : 0.2 ratio as every other model. With pair_w = 0 and class-balanced weights (sum n)
  this is exactly sklearn LogisticRegression(C) with sample_weight = class-balanced weights (tested). C is the
  tuning value. L-BFGS (float64). 65 learned values (T4: 66). C-pre: x = pre z only (33).
  T2 (training only): the objective averages over 8 fixed augmented copies of the training rows (each drops 25 %
  of the non-pre points before the max and adds N(0, 0.1 training SD) noise to z) -- still convex.
S-F CNN-MLP: z sequence in observation order -> Conv1d(32->8, k3, pad 1) -> ReLU -> Conv1d(8->8, k3, pad 1) ->
  ReLU -> [masked max over time (8), masked mean over time (8), the pre_action point's output (8)] (+ T4
  distance) -> Linear 24->16 -> ReLU -> dropout 0.3 -> Linear 16->2 -> softmax. Score = logit difference.
  Loss on the logit difference: pair_w * pair_mean + w_bce * class-balanced CE (CE of a 2-class softmax ==
  BCE on the logit difference). Adam lr 3e-3, 200 full-batch epochs, weight decay (tuning value) on weights only.
  Padding: inputs are zeroed outside each row's points before EACH conv (so padding acts like the zero boundary
  and nothing leaks across rows), conv outputs are zeroed there too, the max ignores padded slots (-inf) and the
  mean divides by the real length. Rows are run in length buckets (<= 8, <= 16, <= 32, longer points; each
  bucket padded to its own max) -- same outputs and gradients as one batch padded to 64 (tested), ~5x less work
  on the real length distribution (mean 8.1, p99 26, max 64). Still one full-batch Adam step per epoch.
  1,410 learned values (T4: 1,426). Dropout masks / init / T2 draws come from per-replica torch Generators
  seeded from the config -> reproducible.
  C-pre (K1): the same MLP on the pre_action z alone (32->16->2: 562).
  T2 (training only): each epoch drops 25 % of the non-pre points (masked exactly like padding) and adds
  N(0, 0.1 training SD) noise to z.
Unsupported toggles raise: T3 (no auxiliary head here), T1 for S-0 (focal loss is not convex). T5 / T6 work
(weights). The second conv uses padding 1 (the draft text gives only "kernel 3"): without it a row with < 3 points
has no output, and the pre_action point -- usually the LAST point -- has no centred window.
"""
from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop.argus_loop import obs_models as OM  # noqa: E402

T2_COPIES = 8
IQR_TO_SD = 1.349


# ---------------------------------------------------------------------------------------------- robust PCA input

@dataclass
class REmb:
    med: np.ndarray     # [D]
    scale: np.ndarray   # [D]
    clip: float
    mu: np.ndarray      # [D] mean of the clipped rows
    Q: np.ndarray       # [D, k]
    sd: np.ndarray      # [k]
    Z: np.ndarray       # [N_obs_universe, k] float32
    fit_rows: str


def robust_embed(data: OM.ObsData, L: int, pos_train, k: int, clip: float = 3.0) -> REmb:
    """Robust scale + clip + PCA k of layer L, all statistics from the training rows' observation points only
    (no labels). Cached per (layer, k, clip, training rows) on the data object."""
    pos_train = np.asarray(pos_train, dtype=np.int64)
    key = ("robust", int(L), int(k), float(clip), OM.h_arr(pos_train))
    lru = data.__dict__.get("_remb")
    if lru is None:
        lru = data.__dict__["_remb"] = OM.LRU(4)
    e = lru.get(key)
    if e is not None:
        return e
    U = data.U[int(L)]
    idx, _ = OM.seg_index(data.off, pos_train)
    D = U.shape[1]
    med, scale = np.empty(D, np.float32), np.empty(D, np.float32)
    for c in range(0, D, 64):
        q = np.percentile(U[idx, c:c + 64].astype(np.float32), [25, 50, 75], axis=0)
        med[c:c + 64] = q[1]
        scale[c:c + 64] = (q[2] - q[0]) / IQR_TO_SD
    scale[~(scale > 1e-8)] = 1.0

    def tr(x):
        return np.clip((x.astype(np.float32) - med) / scale, -clip, clip)

    s1, n = np.zeros(D), 0
    for a in range(0, len(idx), 32768):
        x = tr(U[idx[a:a + 32768]])
        s1 += x.sum(0, dtype=np.float64)
        n += len(x)
    mu = (s1 / n).astype(np.float32)
    C = np.zeros((D, D))
    for a in range(0, len(idx), 32768):
        x = tr(U[idx[a:a + 32768]]) - mu
        C += (x.T @ x).astype(np.float64)
    C /= max(n - 1, 1)
    _, V = np.linalg.eigh(C)
    kk = min(int(k), D)
    Q = V[:, ::-1][:, :kk].copy()
    sgn = np.sign(Q[np.argmax(np.abs(Q), axis=0), np.arange(kk)])
    Q = (Q * np.where(sgn == 0, 1.0, sgn)).astype(np.float32)
    Z = np.empty((U.shape[0], kk), np.float32)
    for a in range(0, U.shape[0], 32768):
        Z[a:a + 32768] = (tr(U[a:a + 32768]) - mu) @ Q
    sd = Z[idx].std(0).astype(np.float32)
    sd[~(sd > 1e-8)] = 1.0
    Z /= sd
    e = REmb(med, scale, float(clip), mu, Q, sd, Z, key[4])
    lru.put(key, e)
    return e


@dataclass
class Seq:
    """Observation points of a list of universe rows, flat in (row, observation order)."""
    idx: np.ndarray       # [N] global obs ids
    seg: np.ndarray       # [N] local row of each point
    start: np.ndarray     # [n] first flat position of each row
    lens: np.ndarray      # [n]
    pre_flat: np.ndarray  # [n] flat position of each row's pre_action point
    pre_pos: np.ndarray   # [n] position of the pre_action point inside its row
    loc: np.ndarray       # [N] position of each point inside its row


def seq_index(data: OM.ObsData, rows) -> Seq:
    rows = np.asarray(rows, np.int64)
    idx, seg = OM.seg_index(data.off, rows)
    lens = (data.off[rows + 1] - data.off[rows]).astype(np.int64)
    start = np.cumsum(lens) - lens
    pre_flat = np.nonzero(data.is_pre[idx])[0]
    if len(pre_flat) != len(rows) or not np.array_equal(seg[pre_flat], np.arange(len(rows))):
        raise RuntimeError("every row must have exactly one pre (or fallback) observation")
    return Seq(idx, seg, start, lens, pre_flat, pre_flat - start, np.arange(len(idx)) - start[seg])


# ---------------------------------------------------------------------------------------------- shared prep

def _check_cfg(cfg):
    if cfg["T3"]:
        raise ValueError(f"{cfg['struct']}: T3 (auxiliary report head) is not defined for this structure")
    if cfg["model"] == "s0" and cfg["T1"]:
        raise ValueError("S-0: T1 (focal loss) would make the objective non-convex")
    if cfg["obs_subset"] not in ("all", "pre"):
        raise ValueError(f"{cfg['struct']}: obs_subset {cfg['obs_subset']!r} not supported")
    if tuple(cfg["layers"]) != (20,):
        raise ValueError(f"{cfg['struct']}: layer 20 only")


def _prep(data, cfg, pos_train, y_train, pos_test):
    """Checks, audit, in-fold embedding, training-only side information (as obs_models.fit_obs)."""
    _check_cfg(cfg)
    pos_train = np.asarray(pos_train, dtype=np.int64)
    pos_test = np.asarray(pos_test, dtype=np.int64)
    y_train = np.asarray(y_train).astype(np.int64)
    if len(pos_train) and (pos_train.max() >= data.n_head or (len(pos_test) and pos_test.max() >= data.n_head)):
        raise ValueError("fit_predict positions must be headline positions")
    if np.intersect1d(pos_train, pos_test).size:
        raise ValueError("training and scored rows overlap")
    audit = {"cfg": OM.config_id(cfg), "train_hash": OM.h_arr(pos_train), "test_hash": OM.h_arr(pos_test),
             "n_train": int(len(pos_train)), "pca_rows_hash": OM.h_arr(pos_train),
             "extras": np.zeros(0, np.int64), "extras_hash": OM.h_arr(np.zeros(0, np.int64)), "n_extras": 0,
             "extras_comp_ok": True, "aux_shuffled": bool(cfg["aux_null_within"]), "aux_used": False}
    p = {"pos_train": pos_train, "pos_test": pos_test, "y": y_train, "audit": audit}
    if len(np.unique(y_train)) < 2:
        return p
    L = cfg["layers"][0]
    emb = robust_embed(data, L, pos_train, int(cfg["pca_k"]), float(cfg["robust_clip"]))
    audit["pca_fit_rows_match"] = emb.fit_rows == OM.h_arr(pos_train)
    audit["pca_kind"] = "robust scale + clip + PCA (training-fold observation points, no labels)"
    status_tr = data.status[pos_train].copy()
    if cfg["aux_null_within"]:  # same permutation rule as obs_models.fit_obs (T6 status follows the shuffle)
        rng = np.random.default_rng(int(OM.h_arr(pos_train, y_train.astype(np.int8), np.frombuffer(
            "|".join(cfg["aux_null_within"]).encode(), np.uint8))[:15], 16))
        cells = ["\x1f".join(v) for v in zip(*[getattr(data.rows, c)[pos_train].astype(str)
                                               for c in cfg["aux_null_within"]])]
        status_tr = OM.permute_within(status_tr, cells, rng)
    sq_tr, sq_te = seq_index(data, pos_train), seq_index(data, pos_test)
    Ztr, Zte = emb.Z[sq_tr.idx], emb.Z[sq_te.idx]
    wb = OM.bce_weights(y_train, data.tool[pos_train], data.source[pos_train], status_tr, cfg)
    I, J, pw = OM.pair_index(y_train, data.traj[pos_train], data.tool[pos_train], status_tr, cfg)
    if cfg["pair_w"] == 0:
        I, J, pw = I[:0], J[:0], pw[:0]
    audit["n_pairs"] = int(len(I))
    dist_tr = dist_te = None
    if cfg["T4"]:
        norm = np.nonzero(y_train == 0)[0]
        mu, prec = OM.gaussian_fit(Ztr[sq_tr.pre_flat][norm])
        dist_tr = OM.mahalanobis(Ztr[sq_tr.pre_flat], mu, prec)
        dist_te = OM.mahalanobis(Zte[sq_te.pre_flat], mu, prec)
        audit.update({"t4_rows_hash": OM.h_arr(pos_train[norm]), "t4_gaussians": 1,
                      "t4_rows_are_train_normals": bool(np.all(y_train[norm] == 0))})
    sd_obs = Ztr.std(0).astype(np.float32)
    p.update({"emb": emb, "sq_tr": sq_tr, "sq_te": sq_te, "Ztr": Ztr, "Zte": Zte, "wb": wb, "I": I, "J": J,
              "pw": pw, "dist_tr": dist_tr, "dist_te": dist_te, "sd_obs": sd_obs})
    return p


def _gen_seed(cfg, p, tag: str, r: int) -> int:
    return int(OM.h_arr(np.asarray([r], np.int64), p["pos_train"], p["y"].astype(np.int8),
                        np.frombuffer(tag.encode(), np.uint8))[:12], 16)


def _thr(s_tr, y):
    norm = s_tr[y == 0]
    return {far: float(np.quantile(norm, 1.0 - far)) for far in OM.FARS}


# ---------------------------------------------------------------------------------------------- S-0

def s0_raw_features(Zobs, sq: Seq, pre_only: bool, keep=None) -> np.ndarray:
    pre = Zobs[sq.pre_flat].astype(np.float64)
    if pre_only:
        return pre
    Zm = Zobs if keep is None else np.where(keep[:, None], Zobs, -np.inf)
    return np.concatenate([np.maximum.reduceat(Zm, sq.start, axis=0).astype(np.float64), pre], 1)


def s0_design(data, cfg, pos_train, y_train, pos_test, p=None) -> dict:
    """Standardised design matrices of S-0: Xtr [copies * n, F] (copy-major), Xte [n_test, F], plus weights and
    pairs tiled over the T2 copies. Exposed for the sklearn equivalence test."""
    p = p or _prep(data, cfg, pos_train, y_train, pos_test)
    pre_only = cfg["obs_subset"] == "pre"
    sq_tr, sq_te = p["sq_tr"], p["sq_te"]
    clean = s0_raw_features(p["Ztr"], sq_tr, pre_only)
    if cfg["T4"]:
        clean = np.c_[clean, p["dist_tr"]]
    mu = clean.mean(0)
    sd = clean.std(0)
    sd[~(sd > 1e-12)] = 1.0
    copies = [clean]
    if cfg["T2"]:
        g = np.random.default_rng(_gen_seed(cfg, p, "s0_t2", 0))
        is_pre = np.zeros(len(sq_tr.idx), bool)
        is_pre[sq_tr.pre_flat] = True
        drop, noise = OM.PREREG_ON["T2"]["obs_drop"], OM.PREREG_ON["T2"]["noise_rel"]
        copies = []
        for _ in range(int(cfg["s0_t2_copies"])):
            keep = (g.random(len(is_pre)) >= drop) | is_pre
            Zn = (p["Ztr"] + noise * p["sd_obs"] * g.standard_normal(p["Ztr"].shape)).astype(np.float32)
            x = s0_raw_features(Zn, sq_tr, pre_only, None if pre_only else keep)
            copies.append(np.c_[x, p["dist_tr"]] if cfg["T4"] else x)
    M, n = len(copies), len(p["pos_train"])
    Xtr = (np.concatenate(copies) - mu) / sd
    Xte = s0_raw_features(p["Zte"], sq_te, pre_only)
    if cfg["T4"]:
        Xte = np.c_[Xte, p["dist_te"]]
    Xte = (Xte - mu) / sd
    off = np.repeat(np.arange(M) * n, len(p["I"]))
    return {"Xtr": Xtr, "Xte": Xte, "Xtr_clean": (clean - mu) / sd, "y": np.tile(p["y"], M),
            "wb": np.tile(p["wb"], M), "I": np.tile(p["I"], M) + off, "J": np.tile(p["J"], M) + off,
            "pw": np.tile(p["pw"], M), "n": n, "copies": M, "p": p}


def fit_logistic_pair(X, y, wb, I, J, pw, C, n, w_bce, pair_w, tol=1e-10, max_iter=20000):
    """argmin 0.5||w||^2 + (C n / w_bce) (pair_w * pair_mean + w_bce * bce_mean); intercept unpenalised.
    Minimises the same objective divided by (C n / w_bce) (better scaled; same minimiser)."""
    from scipy.optimize import minimize
    from scipy.special import expit
    X = np.asarray(X, np.float64)
    y = np.asarray(y, np.float64)
    a = float(C) * n / float(w_bce)
    swb = float(np.sum(wb))
    spw = float(np.sum(pw)) if len(I) else 1.0
    use_pair = bool(pair_w) and len(I) > 0
    F = X.shape[1]

    def fg(th):
        w, b = th[:F], th[F]
        s = X @ w + b
        bce = np.logaddexp(0.0, s) - y * s
        f = 0.5 * (w @ w) / a + w_bce * float(wb @ bce) / swb
        gs = w_bce * wb * (expit(s) - y) / swb
        if use_pair:
            d = s[I] - s[J]
            f += pair_w * float(pw @ np.logaddexp(0.0, -d)) / spw
            gd = -pair_w * pw * expit(-d) / spw
            gs = gs + np.bincount(I, gd, len(s)) - np.bincount(J, gd, len(s))
        return f, np.r_[w / a + X.T @ gs, gs.sum()]

    res = minimize(fg, np.zeros(F + 1), jac=True, method="L-BFGS-B",
                   options={"maxiter": max_iter, "gtol": tol, "ftol": 1e-16, "maxcor": 30})
    return res.x[:F], float(res.x[F]), {"converged": bool(res.success), "n_iter": int(res.nit),
                                        "grad_inf": float(np.abs(res.jac).max()), "message": str(res.message)}


def fit_s0(data, cfg, pos_train, y_train, pos_test) -> OM.FitOut:
    p = _prep(data, cfg, pos_train, y_train, pos_test)
    R = len(cfg["init_seeds"])
    if "emb" not in p:
        return OM._constant(len(p["pos_test"]), R, p["audit"])
    d = s0_design(data, cfg, pos_train, y_train, pos_test, p)
    w, b, info = fit_logistic_pair(d["Xtr"], d["y"], d["wb"], d["I"], d["J"], d["pw"], cfg["logreg_C"], d["n"],
                                   cfg["w_bce"], cfg["pair_w"])
    s_tr = d["Xtr_clean"] @ w + b
    score = d["Xte"] @ w + b
    sq = p["sq_te"]
    if cfg["obs_subset"] == "pre":
        am = sq.pre_pos
    else:  # point that sets the max of the max-slot coordinate with the largest |w_j x_j|
        kz = int(cfg["pca_k"])
        j = np.abs(d["Xte"][:, :kz] * w[:kz]).argmax(1)
        Z = p["Zte"]
        am = np.zeros(len(score), np.int64)
        for r in range(len(score)):
            a0 = sq.start[r]
            am[r] = int(np.argmax(Z[a0:a0 + sq.lens[r], j[r]]))
    a = p["audit"]
    a.update({"s0": info, "s0_t2_copies": d["copies"], "scoring_inputs": "z(obs), pre index" +
              (", T4 Gaussian" if cfg["T4"] else "") + " (robust-PCA input, fixed linear weights)"})
    # convex: every init seed gives the same solution -> identical replicas
    return OM.FitOut(score.astype(np.float64), np.tile(score.astype(np.float32), (R, 1)), _thr(s_tr, p["y"]),
                     am.astype(np.int16), a, None)


# ---------------------------------------------------------------------------------------------- S-F

def _torch():
    return OM._torch()


def padded(Zobs, sq: Seq):
    """[n, Lmax, k] zero-padded sequences, [n, Lmax] validity mask."""
    n, Lm = len(sq.lens), int(sq.lens.max())
    X = np.zeros((n, Lm, Zobs.shape[1]), np.float32)
    M = np.zeros((n, Lm), bool)
    X[sq.seg, sq.loc] = Zobs
    M[sq.seg, sq.loc] = True
    P = np.zeros((n, Lm), bool)
    P[np.arange(n), sq.pre_pos] = True
    return X, M, P


def sf_init(cfg, k: int, n_extra: int, seed: int) -> dict:
    """PyTorch-default-like init (U(-1/sqrt(fan_in), 1/sqrt(fan_in))) from a seeded generator."""
    torch = _torch()
    g = torch.Generator().manual_seed(30_011 + int(seed))
    ch, ks, w = int(cfg["cnn_ch"]), int(cfg["cnn_kernel"]), int(cfg["mlp_width"])

    def u(shape, fan):
        return ((torch.rand(shape, generator=g) * 2 - 1) / np.sqrt(fan)).requires_grad_(True)
    P = {}
    if cfg["obs_subset"] == "pre":
        fin = k
    else:
        P["c1w"], P["c1b"] = u((ch, k, ks), k * ks), u((ch,), k * ks)
        P["c2w"], P["c2b"] = u((ch, ch, ks), ch * ks), u((ch,), ch * ks)
        fin = 3 * ch
    fin += n_extra
    P["l1w"], P["l1b"] = u((fin, w), fin), u((w,), fin)
    P["l2w"], P["l2b"] = u((w, 2), w), u((2,), w)
    return P


def sf_forward(P, X, M, pre_pos, dist, cfg, train=False, gen=None, return_parts=False):
    """X [n, L, k] (any values in padded slots), M [n, L] valid mask, pre_pos [n] -> logits [n, 2]."""
    torch = _torch()
    F = torch.nn.functional
    n = X.shape[0]
    ar = torch.arange(n)
    parts = {}
    if cfg["obs_subset"] == "pre":
        h = X[ar, pre_pos]
    else:
        pad = int(cfg["cnn_kernel"]) // 2
        m = M.unsqueeze(1).to(X.dtype)                          # [n, 1, L]
        x = X.transpose(1, 2) * m                                # padded slots -> 0 before every conv
        x = F.relu(F.conv1d(x, P["c1w"], P["c1b"], padding=pad)) * m
        x = F.relu(F.conv1d(x, P["c2w"], P["c2b"], padding=pad)) * m
        mx = x.masked_fill(~M.unsqueeze(1), float("-inf")).amax(-1)     # padding never wins the max
        mean = x.sum(-1) / m.sum(-1)
        pre = x[ar, :, pre_pos]
        h = torch.cat([mx, mean, pre], 1)
        parts = {"conv": x, "max": mx}
    if dist is not None:
        h = torch.cat([h, dist.view(-1, 1)], 1)
    parts["h"] = h
    z = F.relu(h @ P["l1w"] + P["l1b"])
    p = float(cfg["mlp_dropout"])
    if train and p > 0:
        keep = (torch.rand(z.shape, generator=gen) >= p).to(z.dtype)
        z = z * keep / (1.0 - p)
    logits = z @ P["l2w"] + P["l2b"]
    return (logits, parts) if return_parts else logits


def _diff(logits):
    return logits[:, 1] - logits[:, 0]


LEN_EDGES = (8, 16, 32)   # length buckets: padded work ~ total points (real data: mean 8.1, p99 26, max 64 points)


def buckets(Zobs, sq: Seq, edges=LEN_EDGES) -> list[dict]:
    """Rows grouped by length; each bucket padded to its own max length. Because padding is masked (zeroed
    before every conv, excluded from max / mean) a row's output does not depend on its bucket (tested)."""
    torch = _torch()
    X, M, P = padded(Zobs, sq)
    lo, out = 0, []
    for hi in tuple(edges) + (int(sq.lens.max()),):
        rows = np.nonzero((sq.lens > lo) & (sq.lens <= hi))[0]
        lo = max(lo, hi)
        if not len(rows):
            continue
        Lb = int(sq.lens[rows].max())
        out.append({"rows": torch.from_numpy(rows), "X": torch.from_numpy(np.ascontiguousarray(X[rows, :Lb])),
                    "M": torch.from_numpy(np.ascontiguousarray(M[rows, :Lb])),
                    "P": torch.from_numpy(np.ascontiguousarray(P[rows, :Lb])),
                    "pre": torch.from_numpy(sq.pre_pos[rows])})
    order = torch.cat([b["rows"] for b in out])
    inv = torch.empty_like(order)
    inv[order] = torch.arange(len(order))
    for b in out:
        b["inv"] = inv
    return out


def _run(P, bks, dist, cfg, train=False, gen=None, drop=0.0, noise=0.0, sd_obs=None, parts=False):
    """Logit differences of all rows (original order) over the length buckets."""
    torch = _torch()
    ds, pp = [], []
    for b in bks:
        X, M = b["X"], b["M"]
        if drop:
            M = M & ((torch.rand(M.shape, generator=gen) >= drop) | b["P"])
        if noise:
            X = X + noise * sd_obs * torch.randn(X.shape, generator=gen)
        r = sf_forward(P, X, M, b["pre"], None if dist is None else dist[b["rows"]], cfg, train, gen, parts)
        if parts:
            r, q = r
            pp.append((b, q))
        ds.append(_diff(r))
    d = torch.cat(ds)[bks[0]["inv"]]
    return (d, pp) if parts else d


def fit_sf(data, cfg, pos_train, y_train, pos_test, threads=None, keep_model=False) -> OM.FitOut:
    torch = _torch()
    if threads:
        torch.set_num_threads(int(threads))
    p = _prep(data, cfg, pos_train, y_train, pos_test)
    R = len(cfg["init_seeds"])
    if "emb" not in p:
        return OM._constant(len(p["pos_test"]), R, p["audit"])
    k = int(cfg["pca_k"])
    btr, bte = buckets(p["Ztr"], p["sq_tr"]), buckets(p["Zte"], p["sq_te"])
    dtr = dte = None
    if cfg["T4"]:  # standardised with the training rows' mean / SD
        mu_d, sd_d = float(p["dist_tr"].mean()), float(p["dist_tr"].std()) or 1.0
        dtr = torch.tensor((p["dist_tr"] - mu_d) / sd_d, dtype=torch.float32)
        dte = torch.tensor((p["dist_te"] - mu_d) / sd_d, dtype=torch.float32)
    yt = torch.tensor(p["y"], dtype=torch.float32)
    wb = torch.tensor(p["wb"], dtype=torch.float32)
    I_t, J_t = torch.from_numpy(p["I"]), torch.from_numpy(p["J"])
    pw_t = torch.tensor(p["pw"], dtype=torch.float32)
    gamma = OM.PREREG_ON["T1"]["focal_gamma"] if cfg["T1"] else 0.0
    pre_only = cfg["obs_subset"] == "pre"
    drop = OM.PREREG_ON["T2"]["obs_drop"] if cfg["T2"] and not pre_only else 0.0
    noise = OM.PREREG_ON["T2"]["noise_rel"] if cfg["T2"] else 0.0
    sd_obs = torch.from_numpy(p["sd_obs"]).view(1, 1, -1)
    reps_te, reps_tr, models = [], [], []
    for r, seed in enumerate(cfg["init_seeds"]):
        P = sf_init(cfg, k, 1 if cfg["T4"] else 0, seed)
        gen = torch.Generator().manual_seed(_gen_seed(cfg, p, "sf", int(seed)))
        weights = [v for n_, v in P.items() if n_.endswith("w")]
        biases = [v for n_, v in P.items() if n_.endswith("b")]
        opt = torch.optim.Adam([{"params": weights, "weight_decay": float(cfg["nn_wd"])},
                                {"params": biases, "weight_decay": 0.0}], lr=float(cfg["lr"]))
        for _ in range(int(cfg["epochs"])):        # full batch: one step per epoch over all length buckets
            opt.zero_grad()
            d = _run(P, btr, dtr, cfg, True, gen, drop, noise, sd_obs)
            loss = cfg["w_bce"] * OM._loss_pointwise(torch, d.unsqueeze(0), yt, wb, gamma)[0]
            if len(I_t) and cfg["pair_w"]:
                loss = loss + cfg["pair_w"] * (torch.nn.functional.softplus(-(d[I_t] - d[J_t])) * pw_t).sum() / \
                    pw_t.sum()
            loss.backward()
            opt.step()
        with torch.no_grad():
            reps_tr.append(_run(P, btr, dtr, cfg).numpy().astype(np.float64))
        if r == 0:  # argmax point: the max-slot channel with the largest |d score / d max * max|
            d, pp = _run(P, bte, dte, cfg, parts=True)
            am = p["sq_te"].pre_pos.copy()
            if not pre_only:
                ch = int(cfg["cnn_ch"])
                for b, q in pp:
                    h = q["h"].detach().requires_grad_(True)
                    z = torch.relu(h @ P["l1w"] + P["l1b"])
                    _diff(z @ P["l2w"] + P["l2b"]).sum().backward()
                    cstar = (h.grad[:, :ch] * q["max"].detach()).abs().argmax(1)
                    conv = q["conv"].detach()[torch.arange(len(cstar)), cstar]          # [n_b, L_b]
                    am[b["rows"].numpy()] = conv.masked_fill(~b["M"], float("-inf")).argmax(1).numpy()
            reps_te.append(d.detach().numpy().astype(np.float64))
        else:
            with torch.no_grad():
                reps_te.append(_run(P, bte, dte, cfg).numpy().astype(np.float64))
        if keep_model:
            models.append({kk: v.detach().numpy().copy() for kk, v in P.items()})
    s_tr = np.mean(reps_tr, 0)
    rep = np.stack(reps_te)
    a = p["audit"]
    a["scoring_inputs"] = "z(obs) sequence, validity mask, pre index" + (", T4 Gaussian" if cfg["T4"] else "")
    out = OM.FitOut(rep.mean(0), rep.astype(np.float32), _thr(s_tr, p["y"]), np.asarray(am).astype(np.int16), a,
                    None)
    if keep_model:
        out.model = models
    return out

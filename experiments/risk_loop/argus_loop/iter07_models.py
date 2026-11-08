"""Iteration 7 models (train only). Plan: reports/risk-loop/argus-v1/loop/iter-07/plan.md.

- T7-a: the iteration-6 fixed ensemble (``iter06_models.make_t62``) on a *robust* embedding store: per feature
  median / (IQR / 1.349) scaling fitted on training rows, |z| clipped at 3, then PCA 32 (training rows,
  random_state 0). Computed on the fly per training set and cached in memory.
- T7-c: same-trajectory pair training (pairs/weights of ``models.same_group_pairs``, as T4-1a) with a
  one-hidden-layer MLP score f(x) = w2 . tanh(W1 x + b1) on PCA-32 inputs scaled by training-row SD.
  Loss = weighted pairwise logistic loss + wd/2 (|W1|^2 + |w2|^2); full-batch Adam. Early stopping inside the
  training fold only (25% of the training families that have pairs held out). Mean of 3 initialisations.

Training reads trajectory (pairs) and family (early-stopping split) of training rows only. Scoring reads only
the scored rows' embedding. Earlier files are not modified.
"""
from __future__ import annotations

import sys
import threading
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop.argus_loop import iter05_common as C5  # noqa: E402
from experiments.risk_loop.argus_loop import models as M  # noqa: E402

KMAX = 32
CLIP = 3.0
IQR_TO_SD = 1.349


# ---------------------------------------------------------------------------------------------- T7-a

def robust_embed(X: np.ndarray, pos_train: np.ndarray, kmax: int = KMAX, clip: float = CLIP,
                 seed: int = 0) -> np.ndarray:
    """Median/IQR scaling + clipping (fitted on training rows) -> PCA(kmax) on training rows -> all rows."""
    from sklearn.decomposition import PCA

    pos_train = np.asarray(pos_train, dtype=np.int64)
    Xt = np.asarray(X[pos_train], dtype=np.float32)
    med = np.median(Xt, axis=0)
    q25, q75 = np.percentile(Xt, [25, 75], axis=0)
    sc = (q75 - q25) / IQR_TO_SD
    bad = sc < 1e-6
    if bad.any():  # fall back to the SD, then to 1, for (near-)constant features
        sd = Xt.std(0)
        sc[bad] = np.where(sd[bad] > 1e-6, sd[bad], 1.0)
    Zt = np.clip((Xt - med) / sc, -clip, clip)
    del Xt
    k = int(min(kmax, Zt.shape[0] - 1, Zt.shape[1]))
    pca = PCA(n_components=k, random_state=seed).fit(Zt)
    del Zt
    E = np.empty((X.shape[0], k), dtype=np.float32)
    step = 4096
    for i in range(0, X.shape[0], step):
        E[i:i + step] = pca.transform(np.clip((np.asarray(X[i:i + step], dtype=np.float32) - med) / sc, -clip, clip))
    return E


class RobustStore:
    """Same interface as ``iter05_common.EmbStore.get`` (rep, pos_train) -> embedding; computed on the fly."""

    def __init__(self, features: dict):
        self.features = features  # rep -> X (rows aligned)
        self.cache = {}
        self.lock = threading.Lock()
        self.computed = 0

    def get(self, rep: str, pos_train) -> np.ndarray:
        key = (rep, C5.pos_hash(pos_train))
        with self.lock:
            if key in self.cache:
                return self.cache[key]
        E = robust_embed(self.features[rep], pos_train)
        with self.lock:
            self.cache[key] = E
            self.computed += 1
        return E


# ---------------------------------------------------------------------------------------------- T7-c

def _forward(X, W1, b1, w2):
    H = np.tanh(X @ W1 + b1)
    return H, H @ w2


def _pair_loss_grad(X, I, J, W, W1, b1, w2, wd):
    H, f = _forward(X, W1, b1, w2)
    d = f[I] - f[J]
    sw = W.sum()
    loss = float((W * np.logaddexp(0.0, -d)).sum() / sw + 0.5 * wd * ((W1 ** 2).sum() + (w2 ** 2).sum()))
    gd = -W / (1.0 + np.exp(d)) / sw  # dLoss/dd
    gf = np.zeros(len(X))
    np.add.at(gf, I, gd)
    np.add.at(gf, J, -gd)
    gw2 = H.T @ gf + wd * w2
    gZ = np.outer(gf, w2) * (1.0 - H ** 2)
    gW1 = X.T @ gZ + wd * W1
    gb1 = gZ.sum(0)
    return loss, (gW1, gb1, gw2)


def _pair_loss(X, I, J, W, W1, b1, w2):
    _, f = _forward(X, W1, b1, w2)
    d = f[I] - f[J]
    return float((W * np.logaddexp(0.0, -d)).sum() / W.sum())


def fit_pair_mlp(Etr: np.ndarray, y: np.ndarray, traj: np.ndarray, fam: np.ndarray, *, hidden: int, wd: float,
                 epochs: int = 400, lr: float = 0.01, holdout: float = 0.25, check_every: int = 10,
                 n_init: int = 3, split_seed: int = 0):
    """Returns a list of (W1, b1, w2) (one per initialisation) or None when there is no pair."""
    I, J, W = M.same_group_pairs(y, traj)
    if len(I) == 0:
        return None
    fam = np.asarray(fam).astype(str)
    pair_fam = fam[I]
    # only rows that appear in a pair enter the loss: restrict to them (same result, much faster)
    used, inv = np.unique(np.r_[I, J], return_inverse=True)
    I, J = inv[:len(I)], inv[len(I):]
    Etr = np.asarray(Etr, dtype=np.float64)[used]
    fams = np.unique(pair_fam)
    rng = np.random.default_rng(split_seed)
    n_hold = int(round(holdout * len(fams)))
    hold = set(rng.choice(fams, size=n_hold, replace=False).tolist()) if 2 <= n_hold < len(fams) else set()
    is_hold = np.asarray([f in hold for f in pair_fam])
    tr, ho = ~is_hold, is_hold
    d = Etr.shape[1]
    models = []
    for s in range(n_init):
        r = np.random.default_rng(1000 + s)
        params = [r.normal(scale=1.0 / np.sqrt(d), size=(d, hidden)), np.zeros(hidden),
                  r.normal(scale=1.0 / np.sqrt(hidden), size=hidden)]
        m = [np.zeros_like(p) for p in params]
        v = [np.zeros_like(p) for p in params]
        best, best_params = np.inf, [p.copy() for p in params]
        for t in range(1, epochs + 1):
            _, grads = _pair_loss_grad(Etr, I[tr], J[tr], W[tr], *params, wd)
            for q in range(3):
                m[q] = 0.9 * m[q] + 0.1 * grads[q]
                v[q] = 0.999 * v[q] + 0.001 * grads[q] ** 2
                params[q] = params[q] - lr * (m[q] / (1 - 0.9 ** t)) / (np.sqrt(v[q] / (1 - 0.999 ** t)) + 1e-8)
            if ho.any() and t % check_every == 0:
                hl = _pair_loss(Etr, I[ho], J[ho], W[ho], *params)
                if hl < best:
                    best, best_params = hl, [p.copy() for p in params]
        models.append(best_params if ho.any() else params)
    return models


def make_t7c(store, ctx: dict, rep: str = "L23:max", k: int = KMAX):
    """make_fit_predict(g) for T7-c; g = {"hidden": int, "wd": float}."""
    traj_all = np.asarray(ctx["trajectory"]).astype(str)
    fam_all = np.asarray(ctx["family"]).astype(str)

    def make(g):
        def fp(pos_train, y_train, pos_test):
            pos_train = np.asarray(pos_train, dtype=np.int64)
            pos_test = np.asarray(pos_test, dtype=np.int64)
            y_train = np.asarray(y_train).astype(np.int64)
            Emb = store.get(rep, pos_train)[:, :k].astype(np.float64)
            sd = Emb[pos_train].std(0)
            sd[sd < 1e-9] = 1.0
            Etr, Ete = Emb[pos_train] / sd, Emb[pos_test] / sd
            models = fit_pair_mlp(Etr, y_train, traj_all[pos_train], fam_all[pos_train],
                                  hidden=int(g["hidden"]), wd=float(g["wd"]))
            if models is None:
                return np.zeros(len(pos_test))
            return np.mean([_forward(Ete, *p)[1] for p in models], axis=0)
        return fp
    return make


GRID_T7A = [{"fixed": "ensemble_robust"}]
GRID_T7C = [{"hidden": h, "wd": wd} for h in (8, 32) for wd in (0.01, 0.1, 1.0)]

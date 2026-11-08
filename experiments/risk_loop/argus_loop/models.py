"""Reusable model definitions for the Argus-V1 improvement loop (registry style).

Every model is a factory ``build(name, X, ctx, **params) -> fit_predict`` whose ``fit_predict`` follows the
frozen ``evaluate.py`` convention with ``X_or_rowids=None``: it receives *row positions* into the evaluated
``rows`` (``pos_train, y_train, pos_test``) and returns 1-D scores for ``pos_test``.

- ``X`` is the feature matrix aligned to ``rows`` (float32, finite). Only rows in ``pos_train`` are used for
  any fitted statistic (scaler, PCA, residualisation, weights); test rows are only transformed.
- ``ctx`` holds per-row side information that may be used *only* in the way each model documents:
  ``source`` (training sample weights only, never as a scoring input -- except models flagged
  ``diagnostic=True``, which use it at scoring time and are therefore not eligible as candidates),
  ``log_prefix_length`` (an allowed input, TASK.md section 3).
- Labels come only from ``y_train`` (the harness permutes it in the shuffle tests).

Later iterations add models with ``@register("name", diagnostic=False)``.
"""
from __future__ import annotations

import hashlib
from collections import OrderedDict
from dataclasses import dataclass
from typing import Callable

import numpy as np

REGISTRY: dict[str, "ModelDef"] = {}


@dataclass
class ModelDef:
    name: str
    factory: Callable
    diagnostic: bool  # True = uses a forbidden input at scoring time; never a candidate
    doc: str


def register(name: str, diagnostic: bool = False):
    def deco(fn):
        REGISTRY[name] = ModelDef(name, fn, diagnostic, (fn.__doc__ or "").strip())
        return fn
    return deco


def build(name: str, X: np.ndarray, ctx: dict, **params):
    return REGISTRY[name].factory(X, ctx, **params)


# ---------------------------------------------------------------------------------------------- helpers

def sample_weights(y: np.ndarray, groups: np.ndarray | None, mode: str) -> np.ndarray | None:
    """'class': n/(2*n_class); 'source_class': n/(n_cells*n_cell) over (source, class) cells; 'none'."""
    y = np.asarray(y).astype(np.int64)
    if mode == "none":
        return None
    if mode == "class" or groups is None:
        keys = y.astype(str)
    elif mode == "source_class":
        keys = np.asarray([f"{g}|{c}" for g, c in zip(np.asarray(groups).astype(str), y)], dtype=object)
    else:
        raise ValueError(mode)
    uniq, inv, cnt = np.unique(keys, return_inverse=True, return_counts=True)
    w = len(y) / (len(uniq) * cnt[inv])
    return w.astype(np.float64)


def _key(pos: np.ndarray, tag: str) -> str:
    h = hashlib.sha1(np.ascontiguousarray(np.asarray(pos, dtype=np.int64)).tobytes())
    h.update(tag.encode())
    return h.hexdigest()


class LRU:
    def __init__(self, size: int = 8):
        self.size, self.d = size, OrderedDict()

    def get(self, k):
        if k in self.d:
            self.d.move_to_end(k)
            return self.d[k]
        return None

    def put(self, k, v):
        self.d[k] = v
        self.d.move_to_end(k)
        while len(self.d) > self.size:
            self.d.popitem(last=False)


def pca_embed(X: np.ndarray, pos_train: np.ndarray, kmax: int, *, ctx: dict, resid: bool = False,
              per_source_scale: bool = False, seed: int = 0) -> np.ndarray:
    """Standardise (fit on train rows) -> PCA(kmax) fit on train rows -> embedding of *all* rows.

    resid: regress each component on [1, log prefix_length] using train rows; keep residuals (all rows).
    per_source_scale (diagnostic, forbidden at scoring): standardise each source with its own train stats.
    """
    from sklearn.decomposition import PCA

    Xt = X[pos_train]
    if per_source_scale:
        src = np.asarray(ctx["source"]).astype(str)
        Z = np.empty_like(X)
        st = src[pos_train]
        for s in np.unique(src):
            ms = st == s
            ref = Xt[ms] if ms.any() else Xt
            mu, sd = ref.mean(0), ref.std(0)
            sd[sd < 1e-6] = 1.0
            Z[src == s] = (X[src == s] - mu) / sd
        Zt = Z[pos_train]
    else:
        mu, sd = Xt.mean(0), Xt.std(0)
        sd[sd < 1e-6] = 1.0
        Z = None
        Zt = (Xt - mu) / sd
    k = int(min(kmax, Zt.shape[0] - 1, Zt.shape[1]))
    pca = PCA(n_components=k, random_state=seed).fit(Zt)
    del Zt
    if Z is None:
        E = np.empty((X.shape[0], k), dtype=np.float32)
        step = 4096
        for i in range(0, X.shape[0], step):
            E[i:i + step] = pca.transform((X[i:i + step] - mu) / sd)
    else:
        E = pca.transform(Z).astype(np.float32)
    if resid:
        lp = np.asarray(ctx["log_prefix_length"], dtype=np.float64)
        D = np.column_stack([np.ones(len(lp)), lp])
        beta, *_ = np.linalg.lstsq(D[pos_train], E[pos_train].astype(np.float64), rcond=None)
        E = (E - D @ beta).astype(np.float32)
    return E


def _logreg_scores(Etr, ytr, Ete, C: float, w) -> np.ndarray:
    from sklearn.linear_model import LogisticRegression

    if len(np.unique(ytr)) < 2:
        return np.zeros(len(Ete))
    lr = LogisticRegression(C=C, max_iter=3000)
    lr.fit(Etr, ytr, sample_weight=w)
    return lr.decision_function(Ete)


# ---------------------------------------------------------------------------------------------- models

def _pca_logreg_factory(X, ctx, *, k: int, C: float, weight: str, kmax: int | None = None, resid: bool = False,
                        per_source_scale: bool = False, cache: LRU | None = None):
    kmax = int(kmax or k)
    cache = cache if cache is not None else LRU(8)
    tag = f"pca{kmax}|r{int(resid)}|s{int(per_source_scale)}"

    def fp(pos_train, y_train, pos_test):
        pos_train = np.asarray(pos_train, dtype=np.int64)
        pos_test = np.asarray(pos_test, dtype=np.int64)
        key = _key(pos_train, tag)
        E = cache.get(key)
        if E is None:
            E = pca_embed(X, pos_train, kmax, ctx=ctx, resid=resid, per_source_scale=per_source_scale)
            cache.put(key, E)
        kk = min(k, E.shape[1])
        src = ctx.get("source")
        w = sample_weights(y_train, None if src is None else np.asarray(src)[pos_train], weight)
        return _logreg_scores(E[pos_train, :kk], y_train, E[pos_test, :kk], C, w)

    return fp


@register("pca_logreg")
def pca_logreg(X, ctx, *, k=10, C=1.0, weight="source_class", kmax=None, resid=False, cache=None):
    """StandardScaler -> PCA-k -> LogReg(C). weight: 'class' (Argus-V1 default) or 'source_class'
    (source x class balanced training weights; source never used at scoring). kmax lets a grid share
    one PCA fit per training set (first k components). resid: prefix_length residualisation."""
    return _pca_logreg_factory(X, ctx, k=k, C=C, weight=weight, kmax=kmax, resid=resid, cache=cache)


@register("pca_logreg_per_source_scale", diagnostic=True)
def pca_logreg_per_source_scale(X, ctx, *, k=10, C=1.0, weight="source_class", kmax=None, cache=None):
    """DIAGNOSTIC ONLY: per-source standardisation needs the source at scoring time (forbidden input)."""
    return _pca_logreg_factory(X, ctx, k=k, C=C, weight=weight, kmax=kmax, per_source_scale=True, cache=cache)


def grid_maker(name: str, X, ctx, fixed: dict, cache: LRU | None = None):
    """make_fit_predict(g) for evaluate.nested_cv: ``g`` is a dict of params merged over ``fixed``.
    All grid entries share one cache, so a PCA fit is reused across k and C for the same training rows."""
    cache = cache if cache is not None else LRU(8)

    def make(g):
        p = dict(fixed)
        p.update(g)
        return build(name, X, ctx, cache=cache, **p)

    return make


# ============================================================================================== iteration 2
# Within-tool training signal (TASK.md section 3, 2026-11-08 rule): the training stratum ``ctx["train_group"]``
# (tool, or tool x source) is read ONLY at ``pos_train`` (training-fold rows) to build centring statistics,
# same-stratum pairs or sample weights. Scores for ``pos_test`` are one fixed linear function of the features;
# they never read the test rows' tool or source.
# Centring note: subtracting a per-tool mean from a linear score adds one constant per tool, so within-tool
# AUROC is identical whether or not test rows are centred; training-only centring is therefore coherent for
# the headline metric (pooled AUROC, reference only, may change).

def _block_scale(X: np.ndarray, blocks) -> np.ndarray | None:
    """Per-column multiplier giving each feature block equal total variance after standardisation."""
    if not blocks:
        return None
    s = np.ones(X.shape[1], dtype=np.float32)
    for a, b in blocks:
        s[a:b] = 1.0 / np.sqrt(max(b - a, 1))
    return s


def group_centre(E: np.ndarray, groups: np.ndarray) -> np.ndarray:
    """Subtract each group's mean (rows of E aligned to groups). Returns a new float64 array."""
    E = np.asarray(E, dtype=np.float64)
    out = E.copy()
    g = np.asarray(groups).astype(str)
    for t in np.unique(g):
        m = g == t
        out[m] -= E[m].mean(0)
    return out


def centred_pca_embed(X: np.ndarray, pos_train: np.ndarray, kmax: int, *, group_train: np.ndarray | None,
                      blocks=None, seed: int = 0) -> np.ndarray:
    """Standardise on train rows -> (optional block scaling) -> PCA fit on train rows centred per group
    (group_train=None: plain PCA) -> linear embedding of *all* rows (no centring applied to any scored row)."""
    from sklearn.decomposition import PCA

    Xt = X[pos_train].astype(np.float32)
    mu, sd = Xt.mean(0), Xt.std(0)
    sd[sd < 1e-6] = 1.0
    bs = _block_scale(X, blocks)
    if bs is not None:
        sd = sd / bs
    Zt = (Xt - mu) / sd
    del Xt
    if group_train is not None:
        g = np.asarray(group_train).astype(str)
        for t in np.unique(g):
            m = g == t
            Zt[m] -= Zt[m].mean(0)
    k = int(min(kmax, Zt.shape[0] - 1, Zt.shape[1]))
    pca = PCA(n_components=k, random_state=seed).fit(Zt)
    del Zt
    W = pca.components_.T.astype(np.float32)  # pure linear map; pca.mean_ would only add a constant shift
    E = np.empty((X.shape[0], k), dtype=np.float32)
    step = 4096
    for i in range(0, X.shape[0], step):
        E[i:i + step] = ((X[i:i + step] - mu) / sd) @ W
    return E


def length_directions(Etr_c: np.ndarray, targets_c: np.ndarray, m: int, alpha_rel: float = 1e-2) -> np.ndarray:
    """Orthonormal directions (k x r) found by repeated ridge deflation: for each round and each target
    column, fit ridge on the current (deflated) training embedding, normalise the coefficient vector,
    orthogonalise against earlier ones and project it out. Inputs are already centred (within group)."""
    E = np.asarray(Etr_c, dtype=np.float64).copy()
    T = np.asarray(targets_c, dtype=np.float64)
    T = T[:, None] if T.ndim == 1 else T
    k = E.shape[1]
    Q = np.zeros((k, 0))
    for _ in range(int(m)):
        for j in range(T.shape[1]):
            if Q.shape[1] >= k - 1:
                break
            G = E.T @ E
            lam = alpha_rel * np.trace(G) / k + 1e-12
            w = np.linalg.solve(G + lam * np.eye(k), E.T @ (T[:, j] - T[:, j].mean()))
            if Q.shape[1]:
                w = w - Q @ (Q.T @ w)
            nrm = np.linalg.norm(w)
            if nrm < 1e-10:
                continue
            q = w / nrm
            Q = np.column_stack([Q, q])
            E = E - np.outer(E @ q, q)
    return Q


def _project_out(E: np.ndarray, Q: np.ndarray | None) -> np.ndarray:
    if Q is None or Q.shape[1] == 0:
        return E
    E = np.asarray(E, dtype=np.float64)
    return E - (E @ Q) @ Q.T


def same_group_pairs(y: np.ndarray, groups: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """All (positive i, negative j) index pairs inside each group; weight 1/n_neg(group) so every positive's
    pairs sum to 1. Returns (i, j, w) with w normalised to mean 1."""
    y = np.asarray(y).astype(np.int64)
    g = np.asarray(groups).astype(str)
    I, J, W = [], [], []
    for t in np.unique(g):
        idx = np.nonzero(g == t)[0]
        p, n = idx[y[idx] == 1], idx[y[idx] == 0]
        if len(p) == 0 or len(n) == 0:
            continue
        ii, jj = np.meshgrid(p, n, indexing="ij")
        I.append(ii.ravel())
        J.append(jj.ravel())
        W.append(np.full(ii.size, 1.0 / len(n)))
    if not I:
        return np.zeros(0, np.int64), np.zeros(0, np.int64), np.zeros(0)
    I, J, W = np.concatenate(I), np.concatenate(J), np.concatenate(W)
    return I, J, W / W.mean()


def informative_group_weights(y: np.ndarray, groups: np.ndarray, base: np.ndarray | None) -> np.ndarray:
    """H2-1c: normals of groups that have both classes in the training fold get, in total, the same weight
    as all other normals (total normal weight unchanged)."""
    y = np.asarray(y).astype(np.int64)
    w = np.ones(len(y)) if base is None else np.asarray(base, dtype=np.float64).copy()
    g = np.asarray(groups).astype(str)
    inf_groups = [s for s in np.unique(g) if (y[g == s] == 1).any() and (y[g == s] == 0).any()]
    ing = np.isin(g, inf_groups)
    inf, oth = ing & (y == 0), (~ing) & (y == 0)
    tot = w[y == 0].sum()
    if inf.any() and oth.any():
        w[inf] *= 0.5 * tot / w[inf].sum()
        w[oth] *= 0.5 * tot / w[oth].sum()
    return w


def _v2_factory(X, ctx, *, k: int, C: float, method: str, kmax: int | None = None, centre: bool = True,
                len_rounds: int = 0, weight: str = "source_class", blocks=None, cache: LRU | None = None):
    kmax = int(kmax or k)
    cache = cache if cache is not None else LRU(8)
    tag = f"v2pca{kmax}|c{int(centre)}|b{blocks}"
    grp_all = np.asarray(ctx["train_group"]).astype(str)  # read only at pos_train below
    src_all = ctx.get("source")

    def fp(pos_train, y_train, pos_test):
        from sklearn.linear_model import LogisticRegression

        pos_train = np.asarray(pos_train, dtype=np.int64)
        pos_test = np.asarray(pos_test, dtype=np.int64)
        y_train = np.asarray(y_train).astype(np.int64)
        g_tr = grp_all[pos_train]
        key = _key(pos_train, tag)
        E = cache.get(key)
        if E is None:
            E = centred_pca_embed(X, pos_train, kmax, group_train=g_tr if centre else None, blocks=blocks)
            cache.put(key, E)
        kk = min(k, E.shape[1])
        Etr = E[pos_train, :kk].astype(np.float64)
        Ete = E[pos_test, :kk].astype(np.float64)
        Etr_c = group_centre(Etr, g_tr) if centre else Etr - Etr.mean(0)
        if len_rounds:
            lp = np.asarray(ctx["log_prefix_length"], dtype=np.float64)[pos_train]
            st = np.asarray(ctx["step_index"], dtype=np.float64)[pos_train]
            T = np.column_stack([lp, st])
            Tc = group_centre(T, g_tr) if centre else T - T.mean(0)
            Q = length_directions(Etr_c, Tc, len_rounds)
            Etr_c, Ete = _project_out(Etr_c, Q), _project_out(Ete, Q)
        if len(np.unique(y_train)) < 2:
            return np.zeros(len(pos_test))
        if method == "pairwise":
            I, J, W = same_group_pairs(y_train, g_tr)
            if len(I) == 0:
                return np.zeros(len(pos_test))
            D = Etr_c[I] - Etr_c[J]
            lr = LogisticRegression(C=C, max_iter=3000, fit_intercept=False)
            lr.fit(np.vstack([D, -D]), np.r_[np.ones(len(D)), np.zeros(len(D))], sample_weight=np.r_[W, W])
            return Ete @ lr.coef_.ravel()
        base = sample_weights(y_train, None if src_all is None else np.asarray(src_all)[pos_train], weight)
        if method == "group_weighted":
            base = informative_group_weights(y_train, g_tr, base)
        elif method != "centred":
            raise ValueError(method)
        lr = LogisticRegression(C=C, max_iter=3000)
        lr.fit(Etr_c, y_train, sample_weight=base)
        return Ete @ lr.coef_.ravel()

    return fp


@register("tool_centred_logreg")
def tool_centred_logreg(X, ctx, *, k=10, C=0.01, kmax=None, len_rounds=0, blocks=None, cache=None):
    """H2-1a: standardise -> PCA on training rows centred per training stratum (tool x source) -> LogReg on
    centred training embeddings (source x class weights). Score = same linear map on uncentred rows.
    len_rounds>0 (H2-3): project out ridge directions predicting within-stratum log prefix_length and step."""
    return _v2_factory(X, ctx, k=k, C=C, method="centred", kmax=kmax, centre=True, len_rounds=len_rounds,
                       blocks=blocks, cache=cache)


@register("pairwise_rank")
def pairwise_rank(X, ctx, *, k=10, C=0.01, kmax=None, len_rounds=0, blocks=None, cache=None):
    """H2-1b: logistic loss on (violation - normal) embedding differences of same-stratum pairs in the
    training fold (no intercept; each positive's pairs weigh 1). PCA fitted on per-stratum centred rows."""
    return _v2_factory(X, ctx, k=k, C=C, method="pairwise", kmax=kmax, centre=True, len_rounds=len_rounds,
                       blocks=blocks, cache=cache)


@register("tool_weighted_logreg")
def tool_weighted_logreg(X, ctx, *, k=10, C=0.01, kmax=None, len_rounds=0, blocks=None, cache=None):
    """H2-1c: plain (uncentred) PCA -> LogReg with source x class weights, where normals of strata having
    both classes in the training fold are up-weighted to half of the total normal weight."""
    return _v2_factory(X, ctx, k=k, C=C, method="group_weighted", kmax=kmax, centre=False,
                       len_rounds=len_rounds, blocks=blocks, cache=cache)

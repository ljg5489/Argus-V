"""Iteration 3 models: training-data expansion with report-tool rows (H3-1), multi-task heads (H3-2).

fit_predict follows the frozen evaluate.py convention with X_or_rowids=None: ``pos_train``/``pos_test`` are
positions of HEADLINE rows (universe positions < n_head). Report rows (universe positions >= n_head) are
added inside fit_predict, only when their (family, trajectory, unit) component -- computed over the whole
universe -- contains a training row and no test row. Because the harness passes only inner-fold positions in
nested CV, report rows of the outer evaluation fold are excluded from inner selection as well.

Scores of pos_test are a fixed linear function of features; they never read tool, source, family, track or
any label of the scored rows. Headline labels come only from ``y_train``.

null_within: for the "full shuffle" null, report-row labels are permuted inside cells of the given ctx keys
(e.g. ("source",) or ("source", "family")) with an RNG seeded by the hash of (pos_train, y_train) so each
harness shuffle repeat (different permuted y_train) gets a different report-row permutation.
"""
from __future__ import annotations

import hashlib

import numpy as np

from experiments.risk_loop.argus_loop import models as M


def _seed(pos_train, y_train, tag: str) -> int:
    h = hashlib.sha256(np.ascontiguousarray(np.asarray(pos_train, np.int64)).tobytes())
    h.update(np.ascontiguousarray(np.asarray(y_train, np.int8)).tobytes())
    h.update(tag.encode())
    return int.from_bytes(h.digest()[:8], "little")


def allowed_extras(ctx: dict, pos_train: np.ndarray, pos_test: np.ndarray) -> np.ndarray:
    """Universe positions of report rows whose component touches pos_train and not pos_test."""
    n_head = int(ctx["n_head"])
    comp = np.asarray(ctx["comp"])
    ext = np.arange(n_head, len(comp))
    trc, tec = set(comp[pos_train].tolist()), set(comp[pos_test].tolist())
    ok = np.asarray([(c in trc) and (c not in tec) for c in comp[ext].tolist()], dtype=bool)
    sel = ext[ok]
    fam = np.asarray(ctx["family"])
    if set(fam[sel].tolist()) & set(fam[pos_test].tolist()):
        raise RuntimeError("leak: an added report row shares a family with the scored fold")
    return sel


def _cell_weights(keys: np.ndarray, total: float) -> np.ndarray:
    uniq, inv, cnt = np.unique(np.asarray(keys).astype(str), return_inverse=True, return_counts=True)
    return (total / len(uniq)) / cnt[inv]


def expand_factory(X, ctx, *, k: int, C: float, kmax: int | None = None, w: float = 1.0,
                   extra_mode: str = "both", extra_balance: str = "source_class", head_weight: str = "h21c",
                   multitask: str | None = None, null_within: tuple | None = None, blocks=None,
                   cache: M.LRU | None = None):
    """extra_mode: 'both' | 'pos' (report positives only) | 'none'. extra_balance: 'source_class' |
    'family_class'. head_weight: 'h21c' (source x class + informative-stratum normal up-weighting, = H2-1c)
    | 'source_class' (iteration-1 weighting). multitask: None | 'action' | 'shared'."""
    kmax = int(kmax or k)
    cache = cache if cache is not None else M.LRU(8)
    n_head = int(ctx["n_head"])
    src = np.asarray(ctx["source"]).astype(str)
    fam = np.asarray(ctx["family"]).astype(str)
    grp = np.asarray(ctx["train_group"]).astype(str)
    y_extra = np.asarray(ctx["y_extra"], dtype=np.float64)
    tag = f"x3pca{kmax}|b{blocks}"

    def fp(pos_train, y_train, pos_test):
        from sklearn.linear_model import LogisticRegression

        pos_train = np.asarray(pos_train, dtype=np.int64)
        pos_test = np.asarray(pos_test, dtype=np.int64)
        y_train = np.asarray(y_train).astype(np.int64)
        if pos_train.max(initial=-1) >= n_head or pos_test.max(initial=-1) >= n_head:
            raise ValueError("harness positions must be headline rows")
        if extra_mode == "none" or w == 0:
            ext = np.zeros(0, np.int64)
        else:
            ext = allowed_extras(ctx, pos_train, pos_test)
        ye = y_extra[ext].astype(np.int64)
        if null_within and len(ext):
            rng = np.random.default_rng(_seed(pos_train, y_train, repr(null_within)))
            cell = np.asarray(["\x1f".join(v) for v in zip(*[np.asarray(ctx[c]).astype(str)[ext]
                                                                for c in null_within])], dtype=object)
            for c in sorted(set(cell.tolist())):
                p = np.nonzero(cell == c)[0]
                ye[p] = ye[rng.permutation(p)]
        if extra_mode == "pos":
            keep = ye == 1
            ext, ye = ext[keep], ye[keep]
        T = np.r_[pos_train, ext]
        key = M._key(T, tag)
        Emb = cache.get(key)
        if Emb is None:
            Emb = M.centred_pca_embed(X, T, kmax, group_train=None, blocks=blocks)
            cache.put(key, Emb)
        kk = min(k, Emb.shape[1])
        ET = Emb[T, :kk].astype(np.float64)
        mu = ET.mean(0)
        ET = ET - mu
        Ete = Emb[pos_test, :kk].astype(np.float64)
        yT = np.r_[y_train, ye]
        if len(np.unique(y_train)) < 2:
            return np.zeros(len(pos_test))
        wh = M.sample_weights(y_train, src[pos_train], "source_class")
        if head_weight == "h21c":
            wh = M.informative_group_weights(y_train, grp[pos_train], wh)
        elif head_weight != "source_class":
            raise ValueError(head_weight)
        if len(ext):
            keys = (np.asarray([f"{s}|{c}" for s, c in zip(src[ext], ye)]) if extra_balance == "source_class"
                    else np.asarray([f"{f}|{c}" for f, c in zip(fam[ext], ye)]))
            we = _cell_weights(keys, float(w) * len(pos_train))
        else:
            we = np.zeros(0)
        wT = np.r_[wh, we]
        if multitask:
            r = np.r_[np.zeros(len(pos_train)), np.ones(len(ext))][:, None]
            Z = np.hstack([ET, ET * (1 - r), ET * r, r])
            lr = LogisticRegression(C=C, max_iter=3000).fit(Z, yT, sample_weight=wT)
            c = lr.coef_.ravel()
            w0, wa = c[:kk], c[kk:2 * kk]
            return Ete @ (w0 + wa) if multitask == "action" else Ete @ w0
        lr = LogisticRegression(C=C, max_iter=3000).fit(ET, yT, sample_weight=wT)
        return Ete @ lr.coef_.ravel()

    return fp


def grid_maker(X, ctx, fixed: dict, cache: M.LRU | None = None):
    cache = cache if cache is not None else M.LRU(8)

    def make(g):
        p = dict(fixed)
        p.update(g)
        return expand_factory(X, ctx, cache=cache, **p)

    return make

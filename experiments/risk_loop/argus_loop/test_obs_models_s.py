"""Unit tests for the S-stage structures (obs_models_s, obs_grid_s) on SYNTHETIC data only. Single-threaded.

  py -3.11 experiments/risk_loop/argus_loop/test_obs_models_s.py [name-substring ...]
"""
from __future__ import annotations

import copy
import json
import shutil
import sys
import tempfile
import time
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT))
import torch  # noqa: E402

torch.set_num_threads(1)
from experiments.risk_loop import harness as H  # noqa: E402
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402
from experiments.risk_loop.argus_loop import iter11_diag_models as DM  # noqa: E402
from experiments.risk_loop.argus_loop import obs_grid as G  # noqa: E402
from experiments.risk_loop.argus_loop import obs_grid_s as GS  # noqa: E402
from experiments.risk_loop.argus_loop import obs_models as OM  # noqa: E402
from experiments.risk_loop.argus_loop import obs_models_s as OMS  # noqa: E402
from experiments.risk_loop.argus_loop import obs_models_s0f as OMS0F  # noqa: E402
from experiments.risk_loop.argus_loop import obs_synth as S  # noqa: E402

_TMP = Path(tempfile.mkdtemp(prefix="obs_s_tests_"))
_SYN = {}
_MOTIF = {}


def syn():
    if not _SYN:
        root = _TMP / "syn"
        _SYN["info"] = S.make_synthetic(root, n_fam=20, seed=5, signal=4.0)
        _SYN["data"] = OM.ObsData.load(root, root / "obs_cache", layers=(20, 23))
        _SYN["base"] = OMS.T7aBase.load(root)
        _SYN["root"] = root
    return _SYN["info"], _SYN["data"], _SYN["base"]


def fold0(data, seed=0):
    a, b = E.make_folds(data.head, 5, seed)[0]
    return a, data.head.y[a], b


def scfg(struct, bits=(0, 0, 0, 0, 0, 0), tune=None, **kw):
    """tune = beta (S-A ... S-E), C (S-0) or weight decay (S-F); None -> the structure's default."""
    kw.setdefault("epochs", 8)
    return OMS.make_config_s(struct, bits, tune, **kw)


# ------------------------------------------------------------------------------------------------ configs

def test_param_counts_match_draft():
    for s in OMS.STRUCT_ORDER:
        c = OMS.make_config_s(s)
        assert OMS.n_params(c) == OMS.PARAMS_EXPECTED[s], (s, OMS.n_params(c))
        # T4 = one more head input: +1 for a linear head, +width for an MLP (S-D 4, S-F 16; draft says "+1")
        extra = {"S-D": 4, "S-F": 16}.get(s, 1)
        assert OMS.n_params(OMS.make_config_s(s, OMS.bits_of_state("T4"))) == OMS.PARAMS_EXPECTED[s] + extra
    assert OMS.n_params(OM.make_config()) == 141  # M1' (draft: "M1' (141)")
    d = OMS.make_config_s("S-D")
    assert (d["head"], d["mlp_depth"], d["mlp_width"], d["mlp_dropout"], d["head_l2"], d["K"], d["mlp_act"]) == \
        ("mlp", 2, 4, 0.3, 0.01, 2, "relu")
    # S-0: 64 features + intercept; S-F: 776 + 200 conv + 400 + 34 MLP; their pre-only controls
    assert OMS.n_params(OMS.cpre_config("S-0")) == 33 and OMS.n_params(OMS.cpre_config("S-F")) == 562
    f = OMS.make_config_s("S-F")
    assert (f["lr"], f["epochs"], f["mlp_width"], f["mlp_dropout"], f["nn_wd"], f["cnn_ch"]) == \
        (3e-3, 200, 16, 0.3, 1e-2, 8)
    assert OMS.STRUCT_ORDER == ("S-0", "S-A", "S-F", "S-B", "S-C", "S-D", "S-E")
    assert OMS.make_config_s("S-E")["layers"] == (20, 23) and OMS.make_config_s("S-C")["pool"] == "topk"
    a = OMS.make_config_s("S-A")
    assert (a["pool"], a["slots"], a["offset"], a["K"]) == ("attn", ("pool", "pre"), "t7a", 2)


def test_grid_order_ids_and_tries():
    g = OMS.s_grid("S-B")
    assert [(OMS.state_of(c), c["beta"]) for c in g] == [(s, b) for s in ("base", "T2", "T4", "T2+T4")
                                                         for b in (1.0, 10.0, 100.0)]
    assert len({OM.config_id(c) for c in g}) == 12
    g5 = OMS.s_grid("S-B", OMS.STATES + ("T1+T2+T4",))
    assert [OMS.state_of(c) for c in g5[::3]] == ["base", "T2", "T4", "T2+T4", "T1+T2+T4"]
    # one try per (structure, state); the tuning value (beta / C / weight decay) is not a try;
    # S ids never collide with cycle-1 ids
    keys = {OMS.combo_key_s(c) for s in OMS.STRUCT_ORDER for c in OMS.s_grid(s)}
    assert len(keys) == 28
    for s, key, vals in (("S-0", "logreg_C", (0.01, 0.1, 1.0)), ("S-F", "nn_wd", (1e-3, 1e-2, 1e-1))):
        g0 = OMS.s_grid(s)
        assert [c[key] for c in g0[:3]] == list(vals) and all(c["beta"] == 1.0 for c in g0)
        assert len({OM.config_id(c) for c in g0}) == 12 and len({OMS.combo_key_s(c) for c in g0}) == 4
    assert len(OMS.s_grid("S-0", OMS.STATES + ("T1+T2",))) == 12        # S-0 skips states with T1 / T3
    assert len(OMS.s_grid("S-F", OMS.STATES + ("T1+T2",))) == 15
    c1 = {OM.config_id(c) for c in OM.prereg_grid()}
    assert not c1 & {OM.config_id(c) for s in OMS.STRUCT_ORDER for c in OMS.s_grid(s)}
    cp = OMS.cpre_config("S-C")
    assert cp["obs_subset"] == "pre" and cp["pool"] == "topk" and cp["K"] == 2
    d = OMS.derive(g[0], aux_null_within=["source"])
    assert d["aux_null_within"] == ("source",) and OMS.combo_key_s(d) == OMS.combo_key_s(g[0])


def test_dry_run_counts():
    b = GS.main(["all", "--dry-run"])
    per = b["per_structure"]["S-B"]
    assert per["nominal"]["screen"] == 180 and per["nominal"]["nested_inner"] == 720
    assert per["nominal"]["confirm"] == 1500 and per["nominal"]["shuffles"] == 200
    assert per["nominal"]["reselect"] == 1500 and per["nominal"]["controls(C-pre, inner CV)"] == 225
    assert b["total_nominal"] == 7 * 4505 + 50 and b["total_new"] == 7 * (3700 - 50 + 225) + 50
    assert [b["per_structure"][s]["n_params"] for s in OMS.STRUCT_ORDER] == [65, 101, 1410, 71, 71, 117, 141]
    b5 = GS.main(["all", "--dry-run", "--extra-state", "T1+T2"])
    assert b5["per_structure"]["S-A"]["nominal"]["screen"] == 225


# ------------------------------------------------------------------------------------------------ models

def test_offset_fit_with_zero_offset_equals_fit_obs():
    _, data, _ = syn()
    a, ya, b = fold0(data)
    for c in (scfg("S-B"), scfg("S-B", OMS.bits_of_state("T2+T4"), 10.0), scfg("S-A", epochs=6)):
        o1 = OM.fit_obs(data, c, a, ya, b)
        o2 = OMS.fit_obs_offset(data, c, a, ya, b)
        assert np.allclose(o1.score, o2.score, atol=1e-6, rtol=0), np.abs(o1.score - o2.score).max()
        assert all(abs(o1.thr[f] - o2.thr[f]) < 1e-6 for f in OM.FARS)
        assert np.array_equal(o1.argmax, o2.argmax)


def test_sa_zero_residual_is_exactly_t7a():
    _, data, base = syn()
    a, ya, b = fold0(data)
    t7a = DM.make_t7a(base.feats, base.rows)[0](a, ya.copy(), b)
    out = OMS.fit_s(data, scfg("S-A", epochs=0), a, ya, b, base=base)
    assert np.abs(out.score - t7a).max() <= 1e-6 and out.audit["residual_abs_max"] == 0.0
    assert np.abs(out.scores_rep[0] - t7a).max() <= 1e-6
    # zlogit variant: zero residual -> the mean of the 3 members' standardised scores (draft wording)
    z = OMS.fit_s(data, scfg("S-A", epochs=0, sa_base="t7a_zlogit"), a, ya, b, base=base).score
    assert np.isfinite(z).all() and not np.allclose(z, t7a)
    # with training the residual moves the score away from T7-a
    tr = OMS.fit_s(data, scfg("S-A", epochs=40, beta=1.0), a, ya, b, base=base)
    assert tr.audit["residual_abs_max"] > 1e-4 and not np.allclose(tr.score, t7a)


def test_sa_training_offsets_are_cross_fitted_inside_the_fold():
    _, data, base = syn()
    a, ya, b = fold0(data)
    calls = []
    orig = base.test_scores

    def spy(pa, yy, pb, kind="t7a_pct"):
        calls.append((np.asarray(pa), np.asarray(pb)))
        return orig(pa, yy, pb, kind)
    base.memo = OM.LRU(4)
    base.test_scores = spy
    try:
        off_tr, off_te, aud = base.scores(a, ya, b)
    finally:
        base.test_scores = orig
    assert aud["offset_crossfit_ok"] and aud["offset_cf_folds"] == 5 and len(calls) == 6
    comp = data.comp
    full = calls[0]
    assert np.array_equal(full[0], a) and np.array_equal(full[1], b)
    covered = np.concatenate([pb for _, pb in calls[1:]])
    assert np.array_equal(np.sort(covered), np.sort(a))           # every training row scored once
    for pa, pb in calls[1:]:
        assert np.isin(pa, a).all() and np.isin(pb, a).all()      # never touches the scored fold
        assert not np.isin(comp[pa], comp[pb]).any()              # family-component disjoint
        assert not np.isin(comp[pa], comp[b]).any()
    insample = orig(a, ya, a)
    assert not np.allclose(insample, off_tr)                      # not the (too good) in-place fit
    # memo: same key -> no new T7-a fits
    n = base.calls
    base.scores(a, ya, b)
    assert base.calls == n


def test_all_structures_fit_and_cpre_reads_only_pre():
    _, data, base = syn()
    a, ya, b = fold0(data)
    for s in OMS.STRUCT_ORDER:
        for c in (scfg(s, OMS.bits_of_state("T2+T4"), 100.0, epochs=4), OMS.cpre_config(s, epochs=4)):
            out = OMS.fit_s(data, c, a, ya, b, base=base)
            assert out.score.shape == (len(b),) and np.isfinite(out.score).all(), s
    # C-pre: changing the NON-pre observations of scored rows leaves their scores unchanged; the full model moves
    d2 = copy.copy(data)
    d2._emb, d2._remb = OM.LRU(6), OM.LRU(4)
    d2.U = {L: v.copy() for L, v in data.U.items()}
    idx, _ = OM.seg_index(data.off, b)
    nonpre = idx[~data.is_pre[idx]]
    rng = np.random.default_rng(0)
    for L in d2.U:
        d2.U[L][nonpre] = (rng.normal(size=(len(nonpre), d2.U[L].shape[1])) * 3).astype(np.float16)
    data._emb = OM.LRU(6)
    for s in ("S-0", "S-F", "S-A", "S-C", "S-E"):
        cp = OMS.cpre_config(s, epochs=6)
        s1 = OMS.fit_s(data, cp, a, ya, b, base=base).score
        s2 = OMS.fit_s(d2, cp, a, ya, b, base=base).score
        assert np.allclose(s1, s2, atol=1e-5), (s, np.abs(s1 - s2).max())
        full = scfg(s, epochs=6)
        f1 = OMS.fit_s(data, full, a, ya, b, base=base).score
        f2 = OMS.fit_s(d2, full, a, ya, b, base=base).score
        assert not np.allclose(f1, f2, atol=1e-5), s


def test_structures_learn_the_planted_observation():
    _, data, base = syn()
    a, ya, b = fold0(data)
    yb = data.head.y[b]
    cells = E.headline_groups(data.head.subset(b))
    # S-D default = ReLU head, L2 1e-2 (appendix #2). The draft's original tanh + L2 1e-1 (+ dropout 0.3) head
    # collapses to a near-constant score even on this easy signal (checked below).
    for s, kw in (("S-0", {}), ("S-F", {}), ("S-B", {}), ("S-C", {}), ("S-D", {}), ("S-E", {}), ("S-A", {})):
        sc = OMS.fit_s(data, scfg(s, epochs=200, pca_k=8, **kw), a, ya, b, base=base).score
        pre = OMS.fit_s(data, OMS.cpre_config(s, epochs=200, pca_k=8, **kw), a, ya, b, base=base).score
        w, wp = (E.within_tool_auroc(x, yb, cells)["value"] for x in (sc, pre))
        assert w > 0.8 and w > wp + 0.1, (s, w, wp)  # risk is planted off the pre_action row
    sd = OMS.fit_s(data, scfg("S-D", epochs=200, pca_k=8, head_l2=1e-1, mlp_act="tanh"), a, ya, b).score
    assert E.within_tool_auroc(sd, yb, cells)["value"] < 0.7  # documents the collapse at the draft setting


def test_sd_dropout_and_mlp_shapes():
    _, data, _ = syn()
    a, ya, b = fold0(data)
    c = scfg("S-D", epochs=5)
    out = OMS.fit_s(data, c, a, ya, b, keep_model=True)
    hw = out.model.params["head_w"]
    assert [w.shape[1:] for w in hw] == [(6, 4), (4, 4), (4, 1)]
    o2 = OMS.fit_s(data, c, a, ya, b)
    assert np.array_equal(out.score, o2.score)                    # dropout RNG seeded per fit (fit_s)
    o3 = OMS.fit_s(data, OMS.derive(c, mlp_dropout=0.0), a, ya, b)
    assert not np.allclose(out.score, o3.score)
    # ReLU (default) and tanh heads differ; the tanh copy through fit_obs_offset equals obs_models.fit_obs
    t = OMS.derive(c, mlp_act="tanh")
    assert not np.allclose(OMS.fit_s(data, t, a, ya, b).score, out.score)
    OM._torch().manual_seed(1)
    r1 = OM.fit_obs(data, OMS.derive(t, mlp_dropout=0.0), a, ya, b).score
    r2 = OMS.fit_obs_offset(data, OMS.derive(t, mlp_dropout=0.0), a, ya, b).score
    assert np.allclose(r1, r2, atol=1e-6)


# ------------------------------------------------------------------------------------------------ S-0 / S-F

def test_s0_matches_sklearn_without_pair_loss():
    from sklearn.linear_model import LogisticRegression
    _, data, _ = syn()
    a, ya, b = fold0(data)
    for C in (0.01, 0.1, 1.0):
        for bits in ((0,) * 6, OMS.bits_of_state("T4")):
            c = scfg("S-0", bits, C, pair_w=0.0)
            out = OMS.fit_s(data, c, a, ya, b)
            d = OMS0F.s0_design(data, c, a, ya, b)
            assert d["copies"] == 1 and d["Xtr"].shape[1] == 64 + bits[3] and out.audit["n_pairs"] == 0
            sw = d["wb"] * len(d["wb"]) / d["wb"].sum()
            lr = LogisticRegression(C=C, tol=1e-12, max_iter=100_000).fit(d["Xtr"], d["y"], sample_weight=sw)
            ref = lr.decision_function(d["Xte"])
            assert np.abs(out.score - ref).max() < 1e-3, (C, bits, np.abs(out.score - ref).max())
            assert out.audit["s0"]["converged"]
    # with the pair loss the solution moves, and stays unique (two different starts -> same optimum)
    c = scfg("S-0", tune=0.1)
    s1 = OMS.fit_s(data, c, a, ya, b).score
    assert not np.allclose(s1, OMS.fit_s(data, OMS.derive(c, pair_w=0.0), a, ya, b).score, atol=1e-3)
    d = OMS0F.s0_design(data, c, a, ya, b)
    w, b0, _ = OMS0F.fit_logistic_pair(d["Xtr"], d["y"], d["wb"], d["I"], d["J"], d["pw"], 0.1, d["n"], 0.2, 1.0)
    assert np.allclose(d["Xte"] @ w + b0, s1, atol=1e-6)


def _motif_data():
    """Every row holds the same three motif points (+3 on axes 0, 1, 2 of the layer-20 cache) among N(0, 1)
    noise points; violations have them ADJACENT and in order (0, 1, 2), normals have them >= 2 apart in random
    order. Per-point (permutation-invariant) pooling sees the same distribution in both classes."""
    if "motif" not in _MOTIF:
        root = _TMP / "motif"
        info = S.make_synthetic(root, n_fam=20, seed=11, signal=0.0, n_obs_range=(7, 10), pos_rate=0.3)
        data = OM.ObsData.load(root, root / "obs_cache", layers=(20,))
        rng = np.random.default_rng(3)
        U = rng.normal(size=data.U[20].shape).astype(np.float32)
        y = np.r_[data.head.y, np.zeros(data.n - data.n_head)]
        for i in range(data.n):
            o, n = data.off[i], data.off[i + 1] - data.off[i]
            npre = n - 1                                   # pre_action is the last point
            if y[i]:
                t = int(rng.integers(0, npre - 2))
                pos, order = [t, t + 1, t + 2], [0, 1, 2]
            else:
                start = int(rng.integers(0, 2)) if npre >= 6 else 0
                pos = sorted(rng.choice(np.arange(start, npre, 2), 3, replace=False).tolist())
                order = rng.permutation(3).tolist()
            for p, ax in zip(pos, order):
                U[o + p, ax] += 3.0
        data.U[20] = U.astype(np.float16)
        data._emb, data._remb = OM.LRU(6), OM.LRU(4)
        _MOTIF["motif"] = (info, data)
    return _MOTIF["motif"]


def test_sf_learns_adjacent_motif_that_pointwise_models_cannot():
    _, data = _motif_data()
    a, ya, b = fold0(data)
    yb = data.head.y[b]
    cells = E.headline_groups(data.head.subset(b))

    def wt(sc):
        v = E.within_tool_auroc(sc, yb, cells)["value"]
        return H.auroc(sc, yb) if v is None else v
    # PCA 8 (as the other learnability tests): with 384 training rows and 32 inputs of which 29 are noise the
    # 1.4k-value net fits the training rows perfectly and reaches only ~0.70 (an oracle motif filter gets 0.95)
    sf = wt(OMS.fit_s(data, scfg("S-F", epochs=200, pca_k=8), a, ya, b).score)
    s0 = wt(OMS.fit_s(data, scfg("S-0", tune=1.0, pca_k=8), a, ya, b).score)
    sb = wt(OMS.fit_s(data, scfg("S-B", epochs=200, pca_k=8), a, ya, b).score)
    print(f"    motif within-tool: S-F {sf:.3f}  S-0 {s0:.3f}  S-B {sb:.3f}", flush=True)
    assert sf > 0.85 and s0 < 0.65 and sb < 0.65, (sf, s0, sb)


def test_sf_masking_padding_never_matters():
    torch = OM._torch()
    rng = np.random.default_rng(0)
    c = scfg("S-F")
    P = OMS0F.sf_init(c, 32, 0, 0)
    with torch.no_grad():                       # strongly positive biases: unmasked padding would win the max
        P["c1b"] += 2.0
        P["c2b"] += 2.0
    lens = np.array([1, 2, 5, 9])
    n, Lm = len(lens), lens.max()
    X = np.zeros((n, Lm, 32), np.float32)
    M = np.zeros((n, Lm), bool)
    for i, L in enumerate(lens):
        X[i, :L] = rng.normal(size=(L, 32))
        M[i, :L] = True
    pre = torch.from_numpy(lens - 1)
    Xg = X.copy()
    Xg[~M] = 1e3 * rng.normal(size=((~M).sum(), 32))              # garbage in the padded slots
    with torch.no_grad():
        l0, p0 = OMS0F.sf_forward(P, torch.from_numpy(X), torch.from_numpy(M), pre, None, c, return_parts=True)
        l1 = OMS0F.sf_forward(P, torch.from_numpy(Xg), torch.from_numpy(M), pre, None, c)
        assert torch.equal(l0, l1)
        for i, L in enumerate(lens):                                # each row alone (no padding) = batched
            li = OMS0F.sf_forward(P, torch.from_numpy(X[i:i + 1, :L]), torch.from_numpy(M[i:i + 1, :L]),
                                  pre[i:i + 1], None, c)
            assert torch.allclose(li, l0[i:i + 1], atol=1e-5), (i, li, l0[i])
            conv = p0["conv"][i, :, :L]
            assert torch.allclose(p0["max"][i], conv.max(-1).values)    # max over real points only
            assert (p0["conv"][i, :, L:] == 0).all()
    # the training path: padded seq built from data equals per-row sequences, and the score of a row does not
    # depend on which other rows are scored with it (different Lmax)
    _, data, _ = syn()
    a, ya, b = fold0(data)
    cf = scfg("S-F", epochs=5)
    full = OMS.fit_s(data, cf, a, ya, b).score
    lens_b = data.off[b + 1] - data.off[b]
    short = b[lens_b <= np.median(lens_b)]
    part = OMS.fit_s(data, cf, a, ya, short).score
    assert np.allclose(full[np.isin(b, short)], part, atol=1e-5)
    # length buckets (one padded batch per bucket) == one batch padded to the longest row, incl. gradients
    sq = OMS0F.seq_index(data, a)
    Z = rng.normal(size=(len(sq.idx), 32)).astype(np.float32)
    Pm = OMS0F.sf_init(c, 32, 0, 1)
    one, many = OMS0F.buckets(Z, sq, edges=()), OMS0F.buckets(Z, sq, edges=(3, 5, 7))
    assert len(one) == 1 and len(many) > 2
    d1, d2 = OMS0F._run(Pm, one, None, c), OMS0F._run(Pm, many, None, c)
    assert torch.allclose(d1, d2, atol=1e-5)
    g1 = torch.autograd.grad(d1.square().sum(), Pm["c1w"])[0]
    g2 = torch.autograd.grad(OMS0F._run(Pm, many, None, c).square().sum(), Pm["c1w"])[0]
    assert torch.allclose(g1, g2, rtol=1e-4, atol=1e-4)


def test_pre_only_controls_ignore_other_points():
    _, data, _ = syn()
    a, ya, b = fold0(data)
    d2 = copy.copy(data)
    d2._emb, d2._remb = OM.LRU(6), OM.LRU(4)
    d2.U = {L: v.copy() for L, v in data.U.items()}
    idx, _ = OM.seg_index(data.off, b)
    nonpre = idx[~data.is_pre[idx]]
    d2.U[20][nonpre] = (np.random.default_rng(1).normal(size=(len(nonpre), d2.U[20].shape[1])) * 3).astype(np.float16)
    for s in ("S-0", "S-F"):
        cp = OMS.cpre_config(s, epochs=30)
        assert cp["obs_subset"] == "pre"
        s1, s2 = (OMS.fit_s(d, cp, a, ya, b).score for d in (data, d2))
        assert np.allclose(s1, s2, atol=1e-6), (s, np.abs(s1 - s2).max())
        f1, f2 = (OMS.fit_s(d, scfg(s, epochs=30), a, ya, b).score for d in (data, d2))
        assert not np.allclose(f1, f2, atol=1e-4), s
    out = OMS.fit_s(data, OMS.cpre_config("S-F", epochs=3), a, ya, b, keep_model=True)
    assert set(out.model[0]) == {"l1w", "l1b", "l2w", "l2b"} and out.model[0]["l1w"].shape == (32, 16)


def test_s0_sf_reproducible_and_toggles_work():
    _, data, _ = syn()
    a, ya, b = fold0(data)
    for s in ("S-0", "S-F"):
        base = scfg(s, epochs=20)
        outs = {}
        for st in ("base", "T2", "T4", "T2+T4"):
            c = scfg(s, OMS.bits_of_state(st), epochs=20)
            o1, o2 = OMS.fit_s(data, c, a, ya, b), OMS.fit_s(data, c, a, ya, b)
            assert np.array_equal(o1.score, o2.score) and np.isfinite(o1.score).all(), (s, st)
            la = G.leak_audit(data, o1, a, b, None, c)
            assert la["all_ok"], (s, st, la)
            outs[st] = o1.score
        for st in ("T2", "T4", "T2+T4"):
            assert not np.allclose(outs[st], outs["base"], atol=1e-5), (s, st)
        if s == "S-0":
            d = OMS0F.s0_design(data, scfg(s, OMS.bits_of_state("T2+T4")), a, ya, b)
            assert d["copies"] == 8 and d["Xtr"].shape == (8 * len(a), 65)
            assert np.array_equal(OMS.fit_s(data, OMS.derive(base, init_seeds=(0, 1)), a, ya, b).scores_rep[1],
                                  OMS.fit_s(data, base, a, ya, b).scores_rep[0])        # convex: seeds agree
        else:
            two = OMS.fit_s(data, OMS.derive(base, init_seeds=(0, 1)), a, ya, b)
            assert two.scores_rep.shape == (2, len(b)) and not np.allclose(two.scores_rep[0], two.scores_rep[1])
            assert np.allclose(two.scores_rep[0], OMS.fit_s(data, base, a, ya, b).score, atol=1e-6)
            nod = OMS.fit_s(data, OMS.derive(base, mlp_dropout=0.0), a, ya, b).score
            assert not np.allclose(nod, outs["base"])
        for bad in ("T3",) + (("T1",) if s == "S-0" else ()):
            try:
                OMS.fit_s(data, scfg(s, OMS.bits_of_state(bad), epochs=2), a, ya, b)
                raise AssertionError(f"{s} accepted {bad}")
            except ValueError:
                pass


# ------------------------------------------------------------------------------------------------ grid driver

def _srunner(sub, structures):
    info, data, base = syn()
    return GS.SRunner.from_parts(data, _SYN["root"], info["cache"], _TMP / sub, structures, base=base)


def test_driver_stages_resume_and_report():
    r = _srunner("drv", ("S-A", "S-B"))
    log = G.RunLog(r.out, "s_test")
    st, ep = ("base", "T4"), 3
    for s in ("S-A", "S-B"):
        sc = GS.stage_screen(r, log, s, st, seeds=(0,), epochs=ep)
        assert len(sc["table"]) == 6
        n = GS.stage_nested(r, log, s, st, seeds=(0,), epochs=ep)
        assert n["metrics"]["within_tool"] is not None
        GS.stage_shuffles(r, log, s, st, n=2, epochs=ep)
        GS.stage_reselect(r, log, s, st, n=1, epochs=ep)
        cf = GS.stage_confirm(r, log, s, st, seeds=(0, 1), init=(0, 1), epochs=ep)
        assert all(v["K10_measurable"] for v in cf["states"].values())
        GS.stage_controls(r, log, s, seeds=(0,), epochs=ep)
    GS.stage_common(r, log, seeds=(0,), epochs=ep)
    assert all(c["pass"] for c in log.checks.values()), {k: v for k, v in log.checks.items() if not v["pass"]}
    assert not r.misses, dict(r.misses)
    # resumable: everything comes from the store now
    before = sum(1 for _ in (r.out / "fits").rglob("*.npz"))
    res = r.precompute(OMS.s_grid("S-A", st, epochs=ep), r.outer_specs(0) + r.inner_specs(0))
    assert res == {"fits": 0} and sum(1 for _ in (r.out / "fits").rglob("*.npz")) == before
    tc = json.loads((r.out / "try_counter.json").read_text(encoding="utf-8"))
    assert tc["cycle_tries"] == 4 and tc["cumulative"] == GS.TRY_BASE_S + 4
    summ = GS.stage_report(r, ("S-A", "S-B"), reps=20)
    e = summ["structures"]["S-A"]
    # decision 4: S-A's K1 is against its OWN C-pre; T7-a enters only K5
    assert "K1_vs_C-pre" in e and "K1_vs_T7-a" not in e and "K1_vs_C-pre" in summ["structures"]["S-B"]
    assert "K5_vs_T7-a" in e and e["K5_vs_T7-a"]["paired"]["ci_low"] <= e["K5_vs_T7-a"]["paired"]["ci_high"]
    assert {"K2", "K3", "K4"} <= set(e) and "abs_rho_C-pre" in e["K3"] and "code_sha" in summ
    ctl = json.loads((r.out / "S-B" / "controls.json").read_text(encoding="utf-8"))
    assert ctl["C-pre"]["tune_selection"].startswith("inner CV") and "obs_models_s0f.py" in ctl["code_sha"]


def test_driver_s0_sf_stages_resume():
    r = _srunner("drv0f", ("S-0", "S-F"))
    log = G.RunLog(r.out, "s_test0f")
    st, ep = ("base", "T2+T4"), 3
    for s in ("S-0", "S-F"):
        sc = GS.stage_screen(r, log, s, st, seeds=(0,), epochs=ep)
        assert len(sc["table"]) == 6 and sc["table"][0]["tune_name"] == OMS.tune_name(s)
        assert [t["tune"] for t in sc["table"][:3]] == list(OMS.tune_grid(s))
        n = GS.stage_nested(r, log, s, st, seeds=(0,), epochs=ep)
        assert n["metrics"]["within_tool"] is not None and n["modal"]["tune"] in OMS.tune_grid(s)
        GS.stage_shuffles(r, log, s, st, n=2, epochs=ep)
        GS.stage_reselect(r, log, s, st, n=1, epochs=ep)
        cf = GS.stage_confirm(r, log, s, st, seeds=(0,), init=(0, 1), epochs=ep)
        assert all(set(v["tune_chosen"]) <= set(OMS.tune_grid(s)) for v in cf["states"].values())
        GS.stage_controls(r, log, s, seeds=(0,), epochs=ep)
    assert all(c["pass"] for c in log.checks.values()), {k: v for k, v in log.checks.items() if not v["pass"]}
    assert not r.misses, dict(r.misses)
    before = sum(1 for _ in (r.out / "fits").rglob("*.npz"))
    for s in ("S-0", "S-F"):
        assert r.precompute(OMS.s_grid(s, st, epochs=ep), r.outer_specs(0) + r.inner_specs(0)) == {"fits": 0}
    assert sum(1 for _ in (r.out / "fits").rglob("*.npz")) == before
    tc = json.loads((r.out / "try_counter.json").read_text(encoding="utf-8"))
    assert tc["cycle_tries"] == 4                                   # 2 structures x 2 states; C / wd not tries
    summ = GS.stage_report(r, ("S-0", "S-F"), reps=20)
    assert "K1_vs_C-pre" in summ["structures"]["S-0"] and "K1_vs_C-pre" in summ["structures"]["S-F"]


def test_paired_bootstrap_identity_and_sign():
    _, data, _ = syn()
    rows = data.head
    rng = np.random.default_rng(0)
    good = rows.y + rng.normal(0, 0.8, len(rows))
    bad = rng.normal(size=len(rows))
    z = GS.paired_family_bootstrap([good], [good], rows, reps=30)
    assert z["diff"] == 0 and z["ci_low"] == 0 and z["ci_high"] == 0 and z["K1_fail"]
    p = GS.paired_family_bootstrap([good], [bad], rows, reps=30)
    assert p["ci_low"] > 0 and not p["K1_fail"]


def test_k11_layer_gate_one_sided_reads_the_recheck_file():
    d = _TMP / "k11g"
    d.mkdir(exist_ok=True)
    f = d / "k11.json"
    f.write_text(json.dumps({"layers": {"20": {}}}), encoding="utf-8")
    g = GS.k11_layer23_gate(f)
    assert not g["pass"] and "not in file" in g["reason"]             # missing layer -> fail, never silent
    assert not GS.k11_layer23_gate(d / "nope.json")["pass"]
    lay = {"official|P1": {"diff_cache_minus_orig": 0.035}, "official|P2": {"diff_cache_minus_orig": -0.006},
           "headline|P1": {"diff_cache_minus_orig": -0.08}, "verdict_official_procedure": "PASS"}
    f.write_text(json.dumps({"layers": {"23": lay}}), encoding="utf-8")
    g = GS.k11_layer23_gate(f)
    assert g["pass"] and g["worst"] == -0.006 and set(g["official_rows"]) == {"P1", "P2"}  # headline rows ignored
    lay["official|P2"]["diff_cache_minus_orig"] = -0.011                  # cache lower by > 0.01 -> fail
    f.write_text(json.dumps({"layers": {"23": lay}}), encoding="utf-8")
    assert not GS.k11_layer23_gate(f)["pass"]
    assert GS.k11_structure_gate("S-B")["pass"] and GS.k11_structure_gate("S-B")["layers"] == {}
    # the real recheck file (iter-13/k11_L16_L23.json): layer 23 passes on the official rows (S-E included)
    if GS.K11_FILE.is_file():
        assert GS.k11_structure_gate("S-E")["pass"]


def test_k_rules_k1_own_cpre_k3_relative_k4_k5():
    _, data, _ = syn()
    rows = data.head
    rng = np.random.default_rng(0)
    good = rows.y + rng.normal(0, 0.8, len(rows))
    noise = rng.normal(size=len(rows))
    mean = {"K3_abs_spearman_n_obs32_cell_weighted": 0.45, "K2_frac_pre_or_rend": 0.5, "within_trajectory_C": 0.8}
    n = {"oof": {"0": good}, "metrics": {"within_tool": 0.95}, "extra": {"mean": mean}}
    ctl = {"C-pre": {"oof": {"0": noise}, "extra": {"mean": {"K3_abs_spearman_n_obs32_cell_weighted": 0.38}}}}
    common = {"R-only": {"oof": {"0": noise}}, "T7-a": {"oof": {"0": noise}}}
    sh = {"b": {"within_tool_mean": 0.55}}
    e = GS.k_rules(n, ctl, sh, common, rows, reps=30)
    assert not e["K1_vs_C-pre"]["K1_fail"] and e["K1_vs_C-pre"]["ci_low"] > 0
    assert e["K3"]["fail_fixed_rule_reported"] and not e["K3"]["fail"]      # 0.45 - 0.38 < 0.10
    ctl["C-pre"]["extra"]["mean"]["K3_abs_spearman_n_obs32_cell_weighted"] = 0.30
    assert GS.k_rules(n, ctl, sh, common, rows, reps=30)["K3"]["fail"]    # 0.45 - 0.30 >= 0.10
    assert e["K4"]["fail"] is False and e["K4"]["gain_over_R-only"] > 0
    mean["within_trajectory_C"] = 0.6                                      # 0.6 - max(0.55, 0.5) < 0.10
    assert GS.k_rules(n, ctl, sh, common, rows, reps=30)["K4"]["fail"]
    assert e["K5_vs_T7-a"]["diff"] > 0.03 and not e["K5_vs_T7-a"]["not_adopted"]
    mean["K2_frac_pre_or_rend"] = 0.85
    e2 = GS.k_rules(n, ctl, sh, common, rows, reps=30)
    assert e2["K2"]["fail"] and e2["drop"]
    # K1 is judged against the structure's OWN C-pre: a C-pre equal to the model fails K1
    ctl2 = {"C-pre": {"oof": {"0": good}, "extra": {"mean": {}}}}
    assert GS.k_rules(n, ctl2, sh, common, rows, reps=30)["K1_vs_C-pre"]["K1_fail"]


def test_fail_fast_exits_before_fits_and_modal_tie_order():
    log = G.RunLog(_TMP / "ff", "ff")
    log.check("ok", True)
    GS.fail_fast(log, strict_files=False)                                  # all pass -> returns
    log.check("8s_prereg_S_frozen_before_results", False)
    try:
        GS.fail_fast(log, strict_files=False)
        raise AssertionError("did not exit")
    except SystemExit as exc:
        assert exc.code == 3
    # confirm uses the nested modal setting; ties -> first in prereg grid order
    cv = {"selection": {"chosen": {"0": [5, 2, 2, 5, 9], "1": [9, 0, 0, 1, 1]}}}
    assert E._modal_choice(cv) == 0                                        # 0, 1, 2, 5, 9: 0/1/2/5 tie at 2


def test_success_stage_only_above_bar_and_runs_all_parts():
    r = _srunner("drvsucc", ("S-0",))
    log = G.RunLog(r.out, "succ")
    st, ep = ("base",), 2
    GS.stage_nested(r, log, "S-0", st, seeds=(0,), epochs=ep, probe=False)
    assert GS.stage_success(r, log, "S-0", st, epochs=ep) is None          # synthetic nested < 0.90 -> skipped
    old = GS.SUCCESS_BAR
    GS.SUCCESS_BAR = 0.0
    try:
        orig_nested = GS.stage_nested
        GS.stage_nested = lambda rr, lg, s, sts, epochs=None: orig_nested(rr, lg, s, sts, seeds=(0,), epochs=epochs,
                                                                          probe=False)
        orig_confirm = GS.stage_confirm
        GS.stage_confirm = lambda rr, lg, s, sts, init, epochs, name_out: orig_confirm(
            rr, lg, s, sts, seeds=(0,), init=init, epochs=epochs, name_out=name_out)
        orig_rs = GS.stage_reselect
        GS.stage_reselect = lambda rr, lg, s, sts, n, epochs, name_out: orig_rs(rr, lg, s, sts, n=1, epochs=epochs,
                                                                                 name_out=name_out)
        v1 = _srunner("drvsucc_v1", ("S-0",))
        res = GS.stage_success(r, log, "S-0", st, epochs=ep, v1_runner=v1)
    finally:
        GS.SUCCESS_BAR, GS.stage_nested, GS.stage_confirm, GS.stage_reselect = old, orig_nested, orig_confirm, orig_rs
    assert res is not None and set(res) >= {"a_K10", "b_reselect_full", "c_label_v1_nested", "code_sha"}
    cf = json.loads((r.out / "S-0" / "success_confirm_k10.json").read_text(encoding="utf-8"))
    assert cf["init_seeds"] == [0, 1, 2] and all(v["K10_measurable"] for v in cf["states"].values())
    assert (r.out / "S-0" / "success_reselect_full.json").is_file() and (r.out / "S-0" / "success.json").is_file()


if __name__ == "__main__":
    pick = sys.argv[1:]
    k, t00 = 0, time.time()
    try:
        for name, fn in list(globals().items()):
            if name.startswith("test_") and callable(fn) and (not pick or any(p in name for p in pick)):
                t0 = time.time()
                fn()
                k += 1
                print(f"ok {name} ({time.time() - t0:.1f}s)", flush=True)
    finally:
        shutil.rmtree(_TMP, ignore_errors=True)
    print(k, "passed", f"{time.time() - t00:.0f}s")

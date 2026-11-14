"""Unit tests for phase 3 (obs_cache, obs_models, obs_grid, argus_scorer, infer_demo) on SYNTHETIC data only.

  py -3.11 experiments/risk_loop/argus_loop/test_obs_models.py [name-substring ...]
"""
from __future__ import annotations

import inspect
import shutil
import sys
import tempfile
import time
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop import harness as H  # noqa: E402
from experiments.risk_loop.argus_loop import argus_scorer as AS  # noqa: E402
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402
from experiments.risk_loop.argus_loop import infer_demo as DEMO  # noqa: E402
from experiments.risk_loop.argus_loop import obs_cache as OC  # noqa: E402
from experiments.risk_loop.argus_loop import obs_grid as G  # noqa: E402
from experiments.risk_loop.argus_loop import obs_models as OM  # noqa: E402
from experiments.risk_loop.argus_loop import obs_synth as S  # noqa: E402

_TMP = Path(tempfile.mkdtemp(prefix="obs_tests_"))
_SYN = {}


def syn():
    if not _SYN:
        root = _TMP / "syn"
        _SYN["info"] = S.make_synthetic(root, n_fam=28, seed=3)
        _SYN["data"] = OM.ObsData.load(root, root / "obs_cache", layers=(16, 20, 23))
        _SYN["root"] = root
    return _SYN["info"], _SYN["data"]


def fold0(data, seed=0):
    a, b = E.make_folds(data.head, 5, seed)[0]
    return a, data.head.y[a], b


def cfg(**kw):
    kw.setdefault("pca_k", 8)
    kw.setdefault("beta", 1.0)
    bits = kw.pop("bits", (0, 0, 0, 0, 0, 0))
    return OM.make_config(bits, **kw)


# ------------------------------------------------------------------------------------------------ cache

def test_cache_format_and_guard():
    info, data = syn()
    c = OC.ObsCache(info["cache"])
    assert c.n_obs == len(c.obs_kind) and c.offsets[-1] == c.n_obs
    tr = [s["row"] for s in info["steps"] if s["split"] == "train"][:5]
    g = c.gather(tr, tr)
    assert len(g.off) == 6 and np.all(g.kind[g.pre_local] == "pre_action")
    val = [s["row"] for s in info["steps"] if s["split"] == "validation"][:2]
    try:
        c.gather(val, tr)
        raise AssertionError("validation rows must be refused")
    except PermissionError:
        pass
    sealed = [s["row"] for s in info["steps"] if s["split"] == "sealed"][:1]
    try:
        c.gather(sealed, sealed)
        raise AssertionError("sealed rows are not in the cache")
    except KeyError:
        pass
    b = c.basis(20)
    x = info["raw"][20][:4]
    u = b.project(x)
    assert np.allclose(u, info["u"][20][:4], atol=1e-4)


def test_grid32_thinning():
    kinds = ["pre_reasoning", "reasoning+8", "reasoning+16", "reasoning+24", "reasoning+32", "reasoning+64",
             "reasoning_end", "pre_action"]
    assert OC.grid32_keep(kinds).tolist() == [True, False, False, False, True, True, True, True]
    try:
        OC.grid32_keep(["weird"])
        raise AssertionError
    except ValueError:
        pass


def test_combo_order_and_grid():
    cs = OM.combos()
    assert len(cs) == 64 and len(set(cs)) == 64 and cs[0] == (0,) * 6 and cs[1] == (1, 0, 0, 0, 0, 0)
    assert cs[6] == (0, 0, 0, 0, 0, 1) and cs[7] == (1, 1, 0, 0, 0, 0) and cs[-1] == (1,) * 6
    g = OM.prereg_grid()
    assert len(g) == 192 and [c["beta"] for c in g[:3]] == [0.1, 1.0, 10.0]
    assert len({OM.config_id(c) for c in g}) == 192 and len({OM.combo_key(c) for c in g}) == 64
    assert all(c["init_seeds"] == (0,) for c in g)
    base = g[0]
    assert base["T2"] == 0 and base["pool"] == "max" and base["K"] == 4 and base["pca_k"] == 32 and base["epochs"] == 200


# ------------------------------------------------------------------------------------------------ model

def test_finds_planted_observation_and_argmax():
    info, data = syn()
    a, ya, b = fold0(data)
    yb = data.head.y[b]
    out = OM.fit_obs(data, cfg(init_seeds=(0, 1, 2)), a, ya, b)
    wt = E.within_tool_auroc(out.score, yb, E.headline_groups(data.head.subset(b)))["value"]
    pl = np.asarray([info["planted"].get(int(r), -9) for r in data.head.row_id[b]])
    acc = float(np.mean(out.argmax[yb == 1] == pl[yb == 1]))
    assert wt > 0.85 and acc >= 0.8, (wt, acc)
    pre = OM.fit_obs(data, cfg(obs_subset="pre"), a, ya, b)
    wpre = E.within_tool_auroc(pre.score, yb, E.headline_groups(data.head.subset(b)))["value"]
    assert wpre < 0.68, wpre  # risk is never in the pre_action row
    assert out.scores_rep.shape == (3, len(b))


def test_each_toggle_changes_behaviour():
    _, data = syn()
    a, ya, b = fold0(data)
    base = OM.fit_obs(data, cfg(epochs=60), a, ya, b).score
    for i, t in enumerate(OM.TOGGLES):
        bits = [0] * 6
        bits[i] = 1
        s = OM.fit_obs(data, cfg(bits=bits, epochs=60), a, ya, b).score
        assert np.abs(s - base).max() > 1e-5, t


def test_toggle_weights_and_pairs():
    y = np.array([1, 0, 0, 1, 0, 0])
    tool = np.array(["a", "a", "b", "c", "c", "a"])
    src = np.array(["oct"] * 3 + ["nov"] * 3)
    status = np.array(["oct_human"] * 3 + ["nov_draft_rule", "nov_draft_rule", "nov_auto_confirmed"])
    traj = np.array(["t1"] * 3 + ["t2"] * 3)
    c0, c5, c6 = cfg(), cfg(bits=(0, 0, 0, 0, 1, 0)), cfg(bits=(0, 0, 0, 0, 0, 1))
    w0 = OM.bce_weights(y, tool, src, status, c0)
    assert np.allclose(w0, [1.5, 0.75, 0.75, 1.5, 0.75, 0.75])
    w5 = OM.bce_weights(y, tool, src, status, c5)  # normals of cells with a positive (a|oct, c|nov) x3
    assert np.allclose(w5 / w0, [1, 3, 1, 1, 3, 1])
    w6 = OM.bce_weights(y, tool, src, status, c6)
    assert np.allclose(w6 / w0, [1, 1, 1, 0.8, 0.99, 1])
    I, J, W = OM.pair_index(y, traj, tool, status, c0)
    assert len(I) == 4 and np.allclose(W, 1)
    I, J, W = OM.pair_index(y, traj, tool, status, c5)
    same = tool[I] == tool[J]
    assert np.allclose(W[same], 2) and np.allclose(W[~same], 1)
    I, J, W = OM.pair_index(y, traj, tool, status, c6)
    k = (I == 3) & (J == 4)
    assert np.isclose(W[k][0], 0.8 * 0.99)


def test_t2_dropout_keeps_pre_and_t3_extras_fold_safe():
    _, data = syn()
    a, ya, b = fold0(data)
    ex = data.allowed_extras(a, b)
    assert len(ex) > 0 and not np.isin(data.comp[ex], data.comp[b]).any()
    assert np.isin(data.comp[ex], data.comp[a]).all()
    out = OM.fit_obs(data, cfg(bits=(0, 0, 1, 0, 0, 0), epochs=60), a, ya, b)
    assert out.audit["aux_used"] and out.audit["n_extras"] == len(ex)
    a2, ya2, b2 = (lambda f: (f[0], data.head.y[f[0]], f[1]))(E.make_folds(data.head, 5, 0)[1])
    out2 = OM.fit_obs(data, cfg(bits=(0, 0, 1, 0, 0, 0), epochs=60), a2, ya2, b2)
    assert out2.audit["extras_hash"] != out.audit["extras_hash"]  # T3 redone per fold
    out4 = OM.fit_obs(data, cfg(bits=(0, 0, 0, 1, 0, 0), epochs=30), a, ya, b)
    assert out4.audit["t4_gaussians"] == 1 and out4.audit["t4_rows_are_train_normals"]


def test_no_tool_source_label_at_scoring_time():
    _, data = syn()
    a, ya, b = fold0(data)
    c = cfg(bits=(1, 1, 1, 1, 1, 1), epochs=40)
    s1 = OM.fit_obs(data, c, a, ya, b).score
    saved = {k: getattr(data, k).copy() for k in ("tool", "source", "family", "traj", "status", "y_extra")}
    try:
        for k in saved:
            arr = getattr(data, k)
            arr[b] = arr[b][::-1]
        s2 = OM.fit_obs(data, c, a, ya, b).score
    finally:
        for k, v in saved.items():
            setattr(data, k, v)
    assert np.array_equal(s1, s2)
    assert OM.scoring_signature_ok()
    params = set(inspect.signature(AS.ArgusScorer.score_step).parameters)
    assert not params & {"tool", "source", "label", "family", "trajectory"}


def test_aux_shuffle_permutes_extras_deterministically():
    _, data = syn()
    a, ya, b = fold0(data)
    c = cfg(bits=(0, 0, 1, 0, 0, 1), epochs=80, aux_null_within=("source",))  # > 50 aux-only epochs
    o1 = OM.fit_obs(data, c, a, ya, b)
    o2 = OM.fit_obs(data, c, a, ya, b)
    assert np.array_equal(o1.score, o2.score) and o1.audit["aux_shuffled"]
    o3 = OM.fit_obs(data, cfg(bits=(0, 0, 1, 0, 0, 1), epochs=80), a, ya, b)
    assert not np.array_equal(o1.score, o3.score)


def test_order_invariance_and_m0():
    _, data = syn()
    a, ya, b = fold0(data)
    out = OM.fit_obs(data, cfg(epochs=60), a, ya, b, keep_model=True)
    m = out.model
    row = int(b[0])
    o = np.arange(data.off[row], data.off[row + 1])
    u = {L: data.U[L][o].astype(np.float32) for L in m.layers}
    kinds = list(data.obs_kind[o])
    s = m.score_u(u, kinds)["score"]
    perm = np.random.default_rng(0).permutation(len(o))
    s2 = m.score_u({L: v[perm] for L, v in u.items()}, [kinds[i] for i in perm])["score"]
    assert abs(s - s2) < 1e-9 and abs(s - out.score[0]) < 1e-4
    m0 = OM.fit_obs(data, cfg(filters="m0_fixed", K=1, epochs=60), a, ya, b, keep_model=True)
    assert m0.model.params["W"].shape[-1] == 1


# ------------------------------------------------------------------------------------------------ harness glue

def _runner(sub="run"):
    info, data = syn()
    out = _TMP / sub
    r = G.Runner.__new__(G.Runner)
    r.view, r.cache, r.out, r.layers, r.threads, r.workers = _SYN["root"], info["cache"], out, (20,), 1, 1
    r.log, r.data, r.rows = (lambda *x: None), data, data.head
    r.env = {"view": str(r.view), "cache": str(r.cache), "layers": [20], "threads": 1, "out": str(out)}
    from collections import Counter
    r.misses, r.lookups = Counter(), Counter()
    out.mkdir(parents=True, exist_ok=True)
    return r


def test_memo_path_equals_direct_and_folds_identical():
    r = _runner("memo")
    c = cfg(epochs=15, layers=(20,))
    direct = E.run_cv(OM.make_fp(r.data, c), None, r.rows, [0])
    r.precompute([c], r.outer_specs(0))
    memo = E.run_cv(r.memo_fp(c), None, r.rows, [0])
    assert np.allclose(direct["oof"]["0"], memo["oof"]["0"], atol=1e-12) and not r.misses
    assert OM.h_arr(np.asarray(memo["fold_id"]["0"], np.int64)) == r.fold_hash(0)


def test_nested_fp_equals_frozen_nested_cv_and_never_sees_outer_rows():
    r = _runner("nested")
    grid = [cfg(epochs=8, beta=b, layers=(20,)) for b in (0.1, 10.0)] + [cfg(bits=(0, 0, 1, 0, 0, 0), epochs=8,
                                                                          layers=(20,))]
    specs = r.outer_specs(0) + r.inner_specs(0)
    r.precompute(grid, specs)
    au = r.audits_ok(grid, specs)
    assert au["n_bad"] == 0 and au["n_fits"] == len(grid) * len(specs) and au["t3_per_fold_ok"]
    # spy: during the frozen nested_cv, record what each fit trains on; check against the outer test fold
    seen = []
    orig = OM.fit_obs

    def spy(data, c, pa, ya, pb, **kw):
        out = orig(data, c, pa, ya, pb, **kw)
        seen.append((np.asarray(pa), np.asarray(out.audit.get("extras", [])), np.asarray(pb)))
        return out
    OM.fit_obs = spy
    try:
        cv = E.nested_cv(lambda g: OM.make_fp(r.data, g), grid, None, r.rows, [0], 5, inner_splits=G.INNER)
    finally:
        OM.fit_obs = orig
    comp = r.data.comp
    for oa, ob in E.make_folds(r.rows, 5, 0):
        for pa, ex, pb in seen:
            if np.isin(pb, oa).all() and np.isin(pa, oa).all():  # an inner fit of this outer fold
                used = np.r_[pa, ex].astype(np.int64)
                assert not np.isin(comp[used], comp[ob]).any()
    nfp = OM.NestedFP(lambda g: r.memo_fp(g), grid, r.rows, 0, G.INNER)
    cv2 = E.run_cv(nfp, None, r.rows, [0])
    assert np.allclose(cv["oof"]["0"], cv2["oof"]["0"], atol=1e-9)
    assert nfp.chosen == cv["selection"]["chosen"]["0"]
    cv3 = E.nested_cv(lambda g: r.memo_fp(g), grid, None, r.rows, [0], 5, inner_splits=G.INNER)
    assert np.allclose(cv["oof"]["0"], cv3["oof"]["0"], atol=1e-9)


def test_shuffle_label_replication_matches_frozen():
    r = _runner("shuf")
    got = []

    def fp(pa, ya, pb):
        got.append(np.asarray(ya).copy())
        return np.zeros(len(pb))
    E.shuffle_test(fp, r.rows, 3, seed=0, within=("source", "family"), n_jobs=1)
    mine = r.shuffled_train_labels(0, 3, ("source", "family"))
    flat = [y for per in mine for y in per]
    assert all(np.array_equal(a, b) for a, b in zip(got, flat)) and len(got) == len(flat)


def test_k11_stage_runs():
    info, _ = syn()
    log = G.RunLog(_TMP / "k11", "k11")
    res = G.stage_k11(_SYN["root"], info["cache"], log, layers=(20, 16), seeds=(0,))
    assert set(res) == {"L20", "L16"} and all("abs_diff" in v for v in res.values())
    assert "K11_cache_fidelity_L20" in log.checks


def test_extra_metrics_and_checks_run():
    r = _runner("extra")
    c = cfg(epochs=10, layers=(20,))
    r.precompute([c], r.outer_specs(0))
    cv = E.run_cv(r.memo_fp(c), None, r.rows, [0])
    ex = G.extra_metrics(r, cv, lambda s, i: c)
    m = ex["per_seed"]["0"]
    assert 0 <= m["detection"]["far5"]["false_alarm"] <= 1 and m["auprc_pooled"] is not None
    log = G.RunLog(r.out, "test")
    G.fold_hash_check(log, r, {"x": cv})
    assert log.checks["2_identical_fold_assignment_across_configs"]["pass"]
    lc = G.luck_correction(0.8, 134)
    assert 2.4 < lc["e_max_normal"] < 2.7


# ------------------------------------------------------------------------------------------------ scorer

def _scorer(c, sub):
    info, data = syn()
    a, ya, b = fold0(data)
    out = OM.fit_obs(data, c, a, ya, b, keep_model=True)
    cache = OC.ObsCache(info["cache"])
    sc = AS.ArgusScorer.from_fitted(out.model, {L: cache.basis(L) for L in c["layers"]}, 0.0, {"test": True})
    files = sc.save(_TMP / sub / "pkg")
    return info, data, a, b, out, AS.ArgusScorer.load(_TMP / sub / "pkg"), files


def test_folding_equals_unfolded_and_streaming_equals_batch():
    for sub, c in (("pk1", cfg(epochs=40, init_seeds=(0, 1), layers=(16, 20))),
                   ("pk2", cfg(bits=(0, 0, 0, 1, 0, 0), epochs=40, pool="attn", head="mlp", mlp_depth=2, layers=(20,))),
                   ("pk3", cfg(epochs=40, pool="topk", layers=(20, 23)))):
        info, data, a, b, out, sc, files = _scorer(c, sub)
        assert files[0].suffix == ".safetensors"
        offs = info["offsets_all"]
        for j, row in enumerate(b[:25]):
            row_id = int(data.head.row_id[row])
            o = np.arange(offs[row_id], offs[row_id + 1])
            x = {L: info["raw"][L][o] for L in c["layers"]}
            kinds = info["steps"][row_id]["obs_kinds"].split("|")
            bt = sc.score_step(x, kinds)
            st = sc.start()
            for i, kd in enumerate(kinds):
                sc.update(st, {L: x[L][i] for L in c["layers"]}, kd)
            fin = sc.finalize(st)
            assert fin["score"] == bt["score"] and fin["argmax_obs"] == bt["argmax_obs"]
            u32 = {L: info["u"][L][o] for L in c["layers"]}           # fp32 u (no fp16 rounding)
            unf = out.model.score_u(u32, kinds)["score"]
            assert abs(unf - bt["score"]) <= 1e-5, (sub, unf, bt["score"])
            assert abs(out.score[j] - sc.score_cache_rows({L: data.U[L][np.arange(data.off[row], data.off[row + 1])]
                                                           for L in c["layers"]}, kinds)) <= 1e-4
            assert bt["argmax_obs"]["index"] == int(out.argmax[j]) or c["pool"] == "attn"


def test_scorer_thinning_and_errors():
    c = cfg(epochs=20, layers=(20,))
    info, data, a, b, out, sc, _ = _scorer(c, "pk4")
    offs = info["offsets_all"]
    row_id = int(data.head.row_id[b[0]])
    o = np.arange(offs[row_id], offs[row_id + 1])
    x = info["raw"][20][o]
    kinds = info["steps"][row_id]["obs_kinds"].split("|")
    ref = sc.score_step({20: x}, kinds)["score"]
    # an 8-grid capture: extra off-grid rows are skipped -> same score
    x8 = np.concatenate([x[:1], np.random.default_rng(0).normal(size=(2, x.shape[1])).astype(np.float32), x[1:]])
    k8 = kinds[:1] + ["reasoning+8", "reasoning+16"] + kinds[1:]
    r8 = sc.score_step({20: x8}, k8)
    assert r8["score"] == ref and r8["skipped_off_grid"] == 2
    one = sc.score_step({20: x[-1:]}, ["pre_action"])
    assert np.isfinite(one["score"])
    for bad in ({20: x[:, :10]}, {16: x}, {20: np.where(np.arange(x.size).reshape(x.shape) == 3, np.inf, x)}):
        try:
            sc.score_step(bad, kinds)
            raise AssertionError("must raise")
        except ValueError:
            pass
    assert 0 <= sc.score_step({20: x}, kinds)["percentile"] <= 1
    pieces = [f"t{i} " for i in range(5000)]
    r = sc.score_step({20: x}, kinds, [info["obs_rows"][i]["token_index"] for i in o], pieces)
    assert r["argmax_obs"]["text_window"].count("t") == AS.WINDOW


def test_infer_demo_refusals_and_parity():
    info, data = syn()
    root = _SYN["root"]
    lab = root / "labels.csv"
    import csv
    with open(lab, "w", newline="", encoding="utf-8") as h:
        w = csv.writer(h)
        w.writerow(["unit_id", "split"])
        for s in info["steps"]:
            if s["split"] != "sealed":
                w.writerow([s["unit_id"], s["split"]])
    sealed = root / "sealed.csv"
    with open(sealed, "w", newline="", encoding="utf-8") as h:
        h.write("unit_id,split,source\n" + "".join(f"{s['unit_id']},sealed,nov\n" for s in info["steps"]
                                                   if s["split"] == "sealed"))
    for split in ("validation", "sealed"):
        u = next(s["unit_id"] for s in info["steps"] if s["split"] == split)
        try:
            DEMO.require_train(u, labels=lab, sealed=sealed)
            raise AssertionError(split)
        except PermissionError:
            pass
    try:
        DEMO.require_train("nope", labels=lab, sealed=sealed)
        raise AssertionError
    except PermissionError:
        pass
    unit = next(s["unit_id"] for s in info["steps"] if s["split"] == "train")
    DEMO.require_train(unit, labels=lab, sealed=sealed)
    c = cfg(epochs=20, layers=(20,))
    _, _, _, _, _, sc, _ = _scorer(c, "pk5")
    steps = DEMO.unit_steps(unit, root / "steps.csv")
    offs = info["offsets_all"]
    arrays = [(int(s["step_index"]), 20, info["raw"][20][offs[int(s["row"])]:offs[int(s["row"]) + 1]]) for s in steps]
    cache = OC.ObsCache(info["cache"])
    mk = {int(s["step_index"]): (s["obs_kinds"].split("|"), [None] * int(s["n_obs"])) for s in steps}
    res = DEMO.run_demo(unit, sc, cache, steps, arrays, mk)
    assert res["stream_equals_batch_all"] and res["parity_ok"], res["max_abs_diff_vs_cache"]
    ps = DEMO.plumbing_scorer(cache, [20])
    assert DEMO.run_demo(unit, ps, cache, steps, arrays, mk)["stream_equals_batch_all"]


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

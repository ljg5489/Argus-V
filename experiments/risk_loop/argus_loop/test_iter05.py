"""Unit tests for iteration-5 code (embedding store, step-level model families). py -3.11 test_iter05.py"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402
from experiments.risk_loop.argus_loop import iter04_common as C4  # noqa: E402
from experiments.risk_loop.argus_loop import iter04_models as M4  # noqa: E402
from experiments.risk_loop.argus_loop import iter05_common as C5  # noqa: E402
from experiments.risk_loop.argus_loop import iter05_models as M5  # noqa: E402


def synth_rows(n_fam=12, traj=3, steps=6, d=12, seed=0):
    """Rollout confound on dim 1 (trajectories with a violation), violating step shifted on dim 0."""
    rng = np.random.default_rng(seed)
    recs, X = [], []
    for f in range(n_fam):
        for t in range(traj):
            bad = (f + t) % 2 == 0
            yt = np.zeros(steps, int)
            if bad:
                yt[rng.integers(steps)] = 1
            for s in range(steps):
                x = rng.normal(size=d)
                x[1] += 2.0 if bad else 0.0
                x[0] += 1.5 * yt[s]
                X.append(x)
                recs.append({"unit_id": f"u{f}_{t}", "trajectory_id": f"T{f}_{t}", "step_index": s,
                             "tool": f"tool{s % 2}", "label": int(yt[s]), "label_status": "x",
                             "source": "oct" if f < n_fam // 2 else "nov", "family": f"F{f}", "split": "train",
                             "report_content": 0, "n_obs": 3, "prefix_length": 100 + s})
    return E.Rows.from_records(recs), np.asarray(X, dtype=np.float32)


def mem_store(rows, X, reps=("L8:max",)):
    """In-memory store holding every harness training set (as iter05_emb does) + on_miss counter."""
    mem = {r: {} for r in reps}
    for s in C5.training_sets(rows):
        for r in reps:
            mem[r][C5.pos_hash(s["pos"])] = C5.compute_embedding(X, s["pos"], kmax=8).astype(np.float16)
    return C5.EmbStore(memory=mem, on_miss=lambda rep, pos: C5.compute_embedding(X, pos, kmax=8))


def test_training_sets_cover_every_harness_call():
    rows, X = synth_rows()
    seen = []

    def make(g):
        def fp(a, ya, b):
            seen.append(C5.pos_hash(a))
            return np.zeros(len(b))
        return fp

    E.evaluate(make_fit_predict=make, grid=[{"x": 0}, {"x": 1}], rows=rows, n_shuffle=2, bootstrap=10)
    known = {C5.pos_hash(s["pos"]) for s in C5.training_sets(rows)}
    assert set(seen) <= known and len(set(seen)) == len(known)


def test_store_lookup_matches_direct_and_counts_misses():
    rows, X = synth_rows()
    st = mem_store(rows, X)
    s = C5.training_sets(rows)[0]["pos"]
    assert np.allclose(st.get("L8:max", s), C5.compute_embedding(X, s, kmax=8), atol=2e-2)
    st.get("L8:max", np.arange(10))
    assert st.misses == 1


def test_earlier_mean_strict_and_fill():
    s = np.array([1., 2., 3., 10., 5.])
    tr = np.array(["a", "a", "a", "b", "a"], dtype=object)
    st = np.array([0, 1, 1, 0, 2.])
    out = C5.earlier_mean(s, tr, st, fill=-1.0)
    # a: step0 -> fill; step1 (two rows) -> mean(step0)=1; step2 -> mean(1,2,3)=2; b: fill
    assert np.allclose(out, [-1, 1, 1, -1, 2])


def test_pair_and_hybrid_scores_ignore_test_trajectory():
    rows, X = synth_rows()
    st = mem_store(rows, X)
    tr = C5.training_sets(rows)[3]["pos"]
    te = np.setdiff1d(np.arange(len(rows)), tr)
    for kind, g in (("pair", {"gi": 0, "rep": "L8:max", "k": 8, "C": 1.0}),
                    ("hybrid", {"gi": 0, "rep": "L8:max", "k": 8, "C": 1.0, "lam": 1.0})):
        ctx = {"trajectory": rows.trajectory_id.astype(str), "step_index": rows.step_index}
        s1 = M5.make_family(kind, st, ctx)(g)(tr, rows.y[tr], te)
        t2 = ctx["trajectory"].copy()
        t2[te] = "scrambled"
        s2 = M5.make_family(kind, st, {"trajectory": t2, "step_index": rows.step_index})(g)(tr, rows.y[tr], te)
        assert np.allclose(s1, s2) and np.isfinite(s1).all()


def test_rollout_term_uses_only_earlier_steps():
    rows, X = synth_rows()
    tr = C5.training_sets(rows)[3]["pos"]
    te = np.setdiff1d(np.arange(len(rows)), tr)
    ctx = {"trajectory": rows.trajectory_id.astype(str), "step_index": rows.step_index}
    g = {"gi": 0, "rep": "L8:max", "k": 8, "C": 1.0, "alpha": 1.0}
    s1 = M5.make_family("rollout", mem_store(rows, X), ctx)(g)(tr, rows.y[tr], te)
    # perturb the last step of every test trajectory (features only, embedding recomputed): earlier rows unchanged
    X2 = X.copy()
    last = te[rows.step_index[te] == rows.step_index.max()]
    X2[last] += 50.0
    st2 = C5.EmbStore(memory={"L8:max": {}}, on_miss=lambda rep, pos: C5.compute_embedding(X2, pos, kmax=8))
    st1 = C5.EmbStore(memory={"L8:max": {}}, on_miss=lambda rep, pos: C5.compute_embedding(X, pos, kmax=8))
    a1 = M5.make_family("rollout", st1, ctx)(g)(tr, rows.y[tr], te)
    a2 = M5.make_family("rollout", st2, ctx)(g)(tr, rows.y[tr], te)  # training rows unchanged -> same PCA
    keep = ~np.isin(te, last)
    assert np.allclose(a1[keep], a2[keep]) and not np.allclose(a1, a2)
    assert s1.shape == (len(te),)


def test_hybrid_small_lambda_close_to_pair():
    rows, X = synth_rows(n_fam=30)
    tr = np.arange(len(rows))
    Emb = C5.compute_embedding(X, tr, kmax=8)
    y, traj = rows.y, rows.trajectory_id.astype(str)
    wp = M4.same_traj_pair_fit(Emb, y, traj, 1.0)
    wh = M5.hybrid_fit(Emb, y, traj, 1.0, 1e-4)
    assert wp @ wh / np.linalg.norm(wp) / np.linalg.norm(wh) > 0.99


def test_recorder_sums_match_inner_oof_value():
    rows, X = synth_rows()
    st = mem_store(rows, X)
    sets = C5.training_sets(rows)
    inner = [s for s in sets if s["kind"] == "inner" and s["seed"] == 0 and s["outer"] == 0]
    rec = M5.InnerRecorder(rows.y, rows.trajectory_id, {C5.pos_hash(s["pos"]) for s in inner})
    ctx = {"trajectory": rows.trajectory_id.astype(str), "step_index": rows.step_index}
    fp = M5.make_family("pair", st, ctx, rec)({"gi": 7, "rep": "L8:max", "k": 8, "C": 1.0})
    a, _ = E.make_folds(rows, 5, 0)[0]
    io = np.full(len(a), np.nan)
    for ia, ib in E.make_folds(rows.subset(a), 3, 0):
        io[ib] = fp(a[ia], rows.y[a[ia]], a[ib])
    ref = C4.within_traj_auroc(io, rows.y[a], rows.trajectory_id[a])["value"]
    num = sum(rec.acc[(C5.pos_hash(s["pos"]), 7)][0] for s in inner)
    den = sum(rec.acc[(C5.pos_hash(s["pos"]), 7)][1] for s in inner)
    assert abs(num / den - ref) < 1e-12


def test_grids():
    assert len(M5.grid_for("T5-1")) == 96 and len(M5.grid_for("T5-2")) == 192
    assert len(M5.grid_for("T5-3")) == 384 and len(M5.grid_for("T5-4")) == 480
    assert all(C5.rep_layer(e["rep"][0]) != C5.rep_layer(e["rep"][1]) for e in M5.grid_for("T5-4"))
    assert [e["gi"] for e in M5.grid_for("T5-3")] == list(range(384))


if __name__ == "__main__":
    for k, v in list(globals().items()):
        if k.startswith("test_"):
            v()
            print("ok", k)

"""Tests for final_models.py. py -3.11 experiments/risk_loop/argus_loop/test_final_models.py

Synthetic: the saved-model scorer equals the CV pipeline refitted on all rows, round-trips through pickle,
needs no metadata. Real (skipped if the artifacts are missing): loading each final model.pkl and scoring a few
headline train rows reproduces the in-sample scores stored at fit time.
"""
from __future__ import annotations

import sys
import tempfile
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop.argus_loop import final_models as F  # noqa: E402
from experiments.risk_loop.argus_loop import iter06_scan as S6  # noqa: E402
from experiments.risk_loop.argus_loop import iter07_models as M7  # noqa: E402
from experiments.risk_loop.argus_loop import iter09_models as M9  # noqa: E402
from experiments.risk_loop.argus_loop.test_iter05 import synth_rows  # noqa: E402


def _synth():
    rows, X = synth_rows(d=40)
    rng = np.random.default_rng(1)
    feats = {"L23:max": X, "L16:pre": (X + rng.normal(scale=0.3, size=X.shape)).astype(np.float32)}
    return rows, feats


def test_embed_matches_cv_pipeline():
    rows, feats = _synth()
    pos = np.arange(len(rows))
    a = F.embed(F.fit_robust(feats["L23:max"]), feats["L23:max"])
    b = M7.robust_embed(feats["L23:max"], pos)
    assert a.shape == b.shape and np.allclose(a, b, atol=1e-4)


def test_score_equals_cv_pipeline_and_roundtrip():
    rows, feats = _synth()
    y = rows.y
    allpos = np.arange(len(rows))
    ctx = S6.model_ctx(rows)
    for mid, (members, weights) in F.FINAL.items():
        model = F.fit_final(mid, feats, y, rows.trajectory_id, rows.tool, rows.source)
        s = F.score(model, feats)
        ref = M9.make_weighted(M7.RobustStore(feats), ctx, members, weights)({})(allpos, y, allpos)
        assert np.max(np.abs(s - ref)) < 1e-3, (mid, np.max(np.abs(s - ref)))
        assert np.all((s >= 0) & (s <= 1))
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "m.pkl"
            F.save(model, p)
            back = F.load(p)
        idx = np.array([0, 5, 17, 100])
        sub = F.score(back, {r: feats[r][idx] for r in feats})  # rows scored independently
        assert np.allclose(sub, s[idx], atol=1e-12)
        assert set(model["feature_spec"]) == {m["rep"] for m in members}


def test_real_artifacts_reproduce_in_sample_scores():
    paths = {mid: F.OUT / mid / "model.pkl" for mid in F.FINAL}
    if not all(p.is_file() for p in paths.values()):
        print("skip: final artifacts not built")
        return
    from experiments.risk_loop.argus_loop import iter01_common as C1
    data, rows, _ = C1.headline_data()
    pos_of = {int(r): i for i, r in enumerate(rows.row_id.tolist())}
    for mid, p in paths.items():
        model = F.load(p)
        assert model["status"].startswith("candidate, NOT adopted")
        ids = model["check_rows"]["row_id"][:10]
        sub = rows.subset(np.asarray([pos_of[i] for i in ids]))
        assert set(sub.split.astype(str).tolist()) == {"train"}
        fr = {}
        for r, spec in model["feature_spec"].items():
            fr[r] = np.asarray(C1.features(data, sub, spec["layer"], spec["pool"]), dtype=np.float32)
        s = F.score(model, fr)
        exp = np.asarray(model["check_rows"]["score"][:10])
        assert np.allclose(s, exp, atol=1e-12), (mid, np.max(np.abs(s - exp)))
        print("real", mid, "max diff", float(np.max(np.abs(s - exp))))


if __name__ == "__main__":
    n = 0
    for name, f in list(globals().items()):
        if name.startswith("test_") and callable(f):
            f()
            n += 1
            print("ok", name)
    print(n, "passed")

"""Tests for build_obs_cache (fake arrays, no network).

  py -3.11 experiments/risk_loop/argus_loop/test_build_obs_cache.py
"""
from __future__ import annotations

import hashlib
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_obs_cache as oc  # noqa: E402
from test_build_features import FakeHub  # noqa: E402


def test_fit_basis_and_project():
    rng = np.random.default_rng(0)
    H, n = 40, 3000
    X = (rng.normal(size=(n, 6)) @ rng.normal(size=(6, H)) * 5 + rng.normal(size=(n, H)) * 0.1).astype(np.float32)
    X[:5] += 1e4  # outliers are clipped
    b = oc.fit_basis(X, dim=10)
    assert b["components"].shape == (10, H) and np.allclose(b["components"] @ b["components"].T, np.eye(10), atol=1e-5)
    assert np.all(np.diff(b["explained_variance"]) <= 1e-6)
    assert b["explained_variance_ratio"].sum() > 0.95  # rank-6 signal
    u, z = oc.project(X, b)
    assert np.abs(z + b["pca_mean"]).max() <= oc.CLIP + 1e-6
    ev = (u.astype(np.float64) ** 2).sum() / (z.astype(np.float64) ** 2).sum()
    assert abs(ev - b["explained_variance_ratio"].sum()) < 1e-3  # projection energy == fitted EV on fit rows


def test_fetch_rows_thins_and_decodes_only_wanted():
    import pyarrow as pa

    rng = np.random.default_rng(1)
    a8 = rng.normal(size=(6, 4)).astype(np.float32)
    other = rng.normal(size=(2, 4)).astype(np.float32)
    payload = [other.tobytes(), a8.tobytes()]
    hub = FakeHub(pa.table({"data": payload}))
    kinds = ["pre_reasoning", "reasoning+8", "reasoning+16", "reasoning+24", "reasoning+32", "pre_action"]
    import build_features as bf
    old_h = bf.HIDDEN
    bf.HIDDEN = 4
    try:
        sp = {7: {"n_raw": 6, "keep": np.nonzero(bf.grid32_keep(kinds, 8))[0]}}
        g = {"id": "x#0", "shard": "x", "rg": 0,
             "items": [{"row": 1, "srow": 7, "layer": 20, "dtype": "float32", "shape": [6, 4],
                        "sha": hashlib.sha256(payload[1]).hexdigest()}]}
        (srow, L, x), = oc.fetch_rows(hub, g, sp)
        assert (srow, L) == (7, 20) and np.array_equal(x, a8[[0, 4, 5]])
    finally:
        bf.HIDDEN = old_h


if __name__ == "__main__":
    fails = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                print("PASS", name)
            except Exception as exc:  # noqa: BLE001
                fails += 1
                print("FAIL", name, type(exc).__name__, exc)
    print("failures:", fails)
    sys.exit(1 if fails else 0)

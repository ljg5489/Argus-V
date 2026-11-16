# 파일 위치: ~/Desktop/Argus-V/argus_hook/replay_scoring.py
"""Portable scorer for the Argus-V-p replay demo. numpy only: no scikit-learn, no pickle.

A model "bundle" is one .npz file (arrays + a JSON ``meta`` string) holding everything needed to turn the two
hidden-state features of a step into the Argus-V-p risk score:

    L23:max   layer-23 block output, element-wise max over the step's observation rows (32-token grid)
    L16:pre   layer-16 block output at the ``pre_action`` row (last token before the action message)

    score = sum_m weight_m * percentile_m(linear_m(embed(features)))  [+ random-forest member]

The numbers reproduce experiments/risk_loop/argus_loop (final_models.embed / score and the random-forest member);
experiments/risk_loop/argus_loop/argus_v_p_replay_assets.py writes the bundles and checks that.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

FORMAT = "argus-v-p-bundle/1"
REPS = {"L23:max": "L23_max", "L16:pre": "L16_pre"}     # feature name -> key fragment inside the .npz
GRID = 32


def train_percentile(sorted_train: np.ndarray, s: np.ndarray) -> np.ndarray:
    """Mid-rank percentile of each score among the (sorted) training scores, in [0, 1]."""
    st = np.asarray(sorted_train, dtype=np.float64)
    s = np.asarray(s, dtype=np.float64)
    lo = np.searchsorted(st, s, side="left")
    hi = np.searchsorted(st, s, side="right")
    return (lo + hi) / (2.0 * len(st))


def embed(pre: dict, X: np.ndarray) -> np.ndarray:
    """Robust scaling + clipping + PCA projection of feature rows [n, 2880] -> [n, k] (float64)."""
    Z = np.clip((np.asarray(X, dtype=np.float32) - pre["median"]) / pre["scale"], -pre["clip"], pre["clip"]).astype(np.float64)
    return np.einsum("ij,kj->ik", Z - pre["mean"].astype(np.float64), pre["comps"].astype(np.float64))


def rf_proba(rf: dict, X: np.ndarray) -> np.ndarray:
    """P(violation) of a random forest stored as flat node arrays (mean of the trees' leaf class fractions)."""
    X = np.asarray(X, dtype=np.float32)
    n, T = X.shape[0], len(rf["offsets"]) - 1
    acc = np.zeros(n, dtype=np.float64)
    rows = np.arange(n)
    for t in range(T):
        node = np.full(n, rf["offsets"][t], dtype=np.int64)
        while True:
            left = rf["left"][node]
            inner = left >= 0
            if not inner.any():
                break
            idx = rows[inner]
            nd = node[inner]
            go_left = X[idx, rf["feature"][nd]] <= rf["threshold"][nd]
            node[idx] = np.where(go_left, rf["left"][nd], rf["right"][nd]) + rf["offsets"][t]
        acc += rf["value"][node]
    return acc / T


def load_bundle(path: str | Path) -> dict:
    z = np.load(Path(path), allow_pickle=False)
    meta = json.loads(str(z["meta"]))
    if meta.get("format") != FORMAT:
        raise ValueError(f"unknown bundle format in {path}")
    b = {"meta": meta, "lin": {}, "rfpre": {}, "members": [], "rf": None}
    for rep, key in REPS.items():
        b["lin"][rep] = {"median": z[f"lin_{key}_median"], "scale": z[f"lin_{key}_scale"], "mean": z[f"lin_{key}_mean"],
                         "comps": z[f"lin_{key}_comps"], "clip": float(meta["clip"])}
    for i, m in enumerate(meta["members"]):
        b["members"].append({**m, "coef": z[f"m{i}_coef"], "train_sorted": z[f"m{i}_train_sorted"]})
    if meta.get("rf"):
        for rep, key in REPS.items():
            src = "lin" if meta["rf"]["shares_linear_preprocessing"] else "rf"
            b["rfpre"][rep] = {"median": z[f"{src}_{key}_median"], "scale": z[f"{src}_{key}_scale"],
                               "mean": z[f"{src}_{key}_mean"], "comps": z[f"{src}_{key}_comps"], "clip": float(meta["clip"])}
        b["rf"] = {"offsets": z["rf_offsets"], "left": z["rf_left"], "right": z["rf_right"], "feature": z["rf_feature"],
                   "threshold": z["rf_threshold"], "value": z["rf_value"], "train_sorted": z["rf_train_sorted"]}
    return b


def save_bundle(path: str | Path, meta: dict, arrays: dict) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "wb") as handle:      # a file object keeps the given name (no ".npz" suffix is appended)
        np.savez_compressed(handle, meta=np.array(json.dumps({**meta, "format": FORMAT}, ensure_ascii=False)), **arrays)


def score(bundle: dict, feats: dict) -> np.ndarray:
    """Risk score in [0, 1] per row. ``feats`` = {"L23:max": [n, 2880], "L16:pre": [n, 2880]}."""
    emb = {rep: embed(bundle["lin"][rep], feats[rep]) for rep in REPS}
    n = next(iter(emb.values())).shape[0]
    acc = np.zeros(n)
    for m in bundle["members"]:
        s = np.einsum("ij,j->i", emb[m["rep"]][:, :int(m["k"])], np.asarray(m["coef"], dtype=np.float64))
        acc += float(m["weight"]) * train_percentile(m["train_sorted"], s)
    if bundle["rf"] is not None:
        w = float(bundle["meta"]["rf"]["weight"])
        same = bundle["meta"]["rf"]["shares_linear_preprocessing"]
        cols = []
        for rep, k in bundle["meta"]["rf"]["reps"]:
            e = emb[rep] if same else embed(bundle["rfpre"][rep], feats[rep])
            cols.append(e[:, :int(k)])
        p = rf_proba(bundle["rf"], np.hstack(cols).astype(np.float32))
        acc = (1.0 - w) * acc + w * train_percentile(bundle["rf"]["train_sorted"], p)
    return acc


# ---------------------------------------------------------------------- hidden-state rows -> the two features

def grid32_keep(kinds: list[str]) -> list[bool]:
    """Observation rows on the 32-token grid: the three fixed points always, ``reasoning+N`` only when N % 32 == 0
    (so 8-token captures pool exactly like the 32-token data the model was fitted on)."""
    keep = []
    for k in kinds:
        if k in ("pre_reasoning", "reasoning_end", "pre_action"):
            keep.append(True)
        elif k.startswith("reasoning+"):
            keep.append(int(k.split("+", 1)[1]) % GRID == 0)
        else:
            keep.append(False)
    return keep


def pool_features(rows23: np.ndarray, rows16: np.ndarray, kinds: list[str], as_cache: bool = True) -> dict:
    """Observation rows [n_obs, 2880] of layers 23 and 16 -> {"L23:max": [1, 2880], "L16:pre": [1, 2880]}.
    ``as_cache`` rounds through float16 like the feature cache the model was fitted on."""
    keep = np.asarray(grid32_keep(list(kinds)), dtype=bool)
    if not keep.any():
        raise ValueError("no observation row on the 32-token grid")
    a23 = np.asarray(rows23, dtype=np.float32)[keep]
    a16 = np.asarray(rows16, dtype=np.float32)[keep]
    kk = [k for k, f in zip(kinds, keep) if f]
    pre_rows = [i for i, k in enumerate(kk) if k == "pre_action"]
    pre_i = pre_rows[-1] if pre_rows else len(kk) - 1
    out = {"L23:max": a23.max(0)[None, :], "L16:pre": a16[pre_i][None, :].copy()}
    if as_cache:
        out = {k: v.astype(np.float16).astype(np.float32) for k, v in out.items()}
    return out

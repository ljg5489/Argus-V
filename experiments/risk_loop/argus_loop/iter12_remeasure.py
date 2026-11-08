"""Iteration 12: re-measure EXISTING models with the v2 labels (labels_trainval.v2.csv). Not new model tries.

Label views (both read only by the frozen evaluate.load(root); evaluate.py is never modified):
  v1  artifacts/risk-loop/argus-v1-loop/features/            (old labels, steps.csv as built)
  v2  artifacts/risk-loop/argus-v1-loop/features_labels_v2/  (build_features.py relabel --make-view: relabelled
      steps.csv, same rows and order, + hard links to the same feature arrays)

Models (recipes unchanged, imported from the iteration code):
  H1-0a  original Argus-V1 default: layer 16 max -> standardise -> PCA 10 -> class-balanced LogReg C=1
  T7-a   iteration-7 fixed ensemble (robust scaling -> PCA 32 -> H2-1c L23 max + pair models T4-1a/T4-1b)
Per label view: fold seeds 0..9 (run_cv + metrics with family bootstrap CI and baselines), seeds 0..2 headline
(TASK.md v4), per cell, per source; T7-a shuffles (a)/(b) 20 each at fold seed 0 (evaluate.shuffle_test);
reference shuffle (b) of the pointwise model H2-1c-L23 (source of the 0.591 bar) re-run on the same labels.
Train split only (evaluate.load refuses validation/test/sealed).

Usage: py -3.11 experiments/risk_loop/argus_loop/iter12_remeasure.py [v1 v2]
"""
from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ.setdefault(_v, "2")

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402
from experiments.risk_loop.argus_loop import iter01_common as C1  # noqa: E402
from experiments.risk_loop.argus_loop import iter02_common as C2  # noqa: E402
from experiments.risk_loop.argus_loop import iter11_diag_common as D  # noqa: E402
from experiments.risk_loop.argus_loop import iter11_diag_models as DM  # noqa: E402
from experiments.risk_loop.argus_loop import models as M  # noqa: E402

SHA = "a7c36eafdf994f98b61895be4e4b8d237740d0018422d12febab8deb9df0130d"
ART = REPO_ROOT / "artifacts" / "risk-loop" / "argus-v1-loop"
OUT = ART / "iter12_remeasure"
VIEWS = {"v1": ART / "features", "v2": ART / "features_labels_v2"}
SEEDS10 = list(range(10))
REF_B_OLD = 0.5905098889931206  # H2-1c shuffle (b) 20-run mean on the v1 labels (iter-02 eval-v4)
H21C_GRID5 = {"k": 32, "C": 0.1}


def log(*a):
    print(time.strftime("%H:%M:%S"), *a, flush=True)


def cell_table(rows, oofs):
    """Included headline cells with counts and per-cell AUROC (mean over the given seeds + per seed)."""
    from experiments.risk_loop import harness as H
    g, y = E.headline_groups(rows), rows.y
    out = {}
    for c in sorted(set(g.tolist())):
        m = np.nonzero(g == c)[0]
        p = int(y[m].sum())
        n = len(m) - p
        if p == 0:
            continue
        e = {"pos": p, "neg": n, "included": bool(p >= E.MIN_POS and n >= E.MIN_NEG)}
        if e["included"]:
            per = [float(H.auroc(o[m], y[m])) for o in oofs]
            e.update({"auroc_mean": float(np.mean(per)), "auroc_per_seed": per})
        out[str(c)] = e
    return out


def summarise(cv, rows, name):
    m10 = E.metrics(cv, rows)
    m3 = E.metrics({**cv, "seeds": [0, 1, 2]}, rows)
    oofs = [np.asarray(cv["oof"][str(s)], dtype=np.float64) for s in SEEDS10]
    wt10, wt3 = m10["within_tool"], m3["within_tool"]
    return {
        "model": name,
        "seed012": {"value": wt3["value"], "per_seed": wt3["per_seed"], "ci95": wt3["ci95"],
                    "by_source": {s: v["value"] for s, v in wt3["by_source"].items()},
                    "baselines": {k: m3["baselines"][k]["within_tool"] for k in ("length+step", "n_obs", "tool_identity")},
                    "pooled_auroc": m3["pooled_auroc"]},
        "seed0_9": {"value": wt10["value"], "per_seed": wt10["per_seed"],
                    "sd": float(np.std(wt10["per_seed"], ddof=1)), "ci95": wt10["ci95"],
                    "by_source": {s: v["value"] for s, v in wt10["by_source"].items()},
                    "by_source_npos_included": {s: v["n_positives_included"] for s, v in wt10["by_source"].items()},
                    "baselines": {k: m10["baselines"][k]["within_tool"] for k in ("length+step", "n_obs", "tool_identity")},
                    "tool_identity_shortcut_proof": m10["baselines"]["tool_identity_shortcut_proof"],
                    "pooled_auroc": m10["pooled_auroc"],
                    "n_cells": wt10["n_tools"], "n_positives_included": wt10["n_positives_included"],
                    "n_positives_total": wt10["n_positives_total"]},
        "cells_seed0_9": cell_table(rows, oofs),
        "rows": m10["rows"],
    }, oofs


def run_view(tag):
    root = VIEWS[tag]
    data, rows, info = C1.headline_data(root)
    assert set(rows.split.tolist()) == {"train"}
    log(tag, "rows", len(rows), "pos", int(rows.y.sum()), dict(sorted(rows.summary()["label_status"].items())))
    feats = DM.load_feats(data, rows, ["L23:max", "L16:pre"])
    X16 = np.asarray(C1.features(data, rows, 16, "max"), dtype=np.float32)
    X23, _ = C2.representation(data, rows, "L23:max")
    res = {"view": str(root), "headline_filter": info}

    t0 = time.time()
    fp_h = DM.make_h10a(X16, rows)
    cv = E.run_cv(fp_h, None, rows, seeds=SEEDS10)
    res["H1-0a"], O = summarise(cv, rows, "H1-0a")
    np.save(OUT / f"oof_{tag}_H1-0a_seed0-9.npy", np.asarray(O))
    log(tag, "H1-0a", round(res["H1-0a"]["seed0_9"]["value"], 4), round(time.time() - t0))

    t0 = time.time()
    fp_t = DM.make_t7a(feats, rows)[0]
    cv = E.run_cv(fp_t, None, rows, seeds=SEEDS10)
    res["T7-a"], O = summarise(cv, rows, "T7-a")
    np.save(OUT / f"oof_{tag}_T7-a_seed0-9.npy", np.asarray(O))
    log(tag, "T7-a", round(res["T7-a"]["seed0_9"]["value"], 4), round(time.time() - t0))

    t0 = time.time()
    sa = E.shuffle_test(fp_t, rows, 20, seed=0, within=("source",))
    sb = E.shuffle_test(fp_t, rows, 20, seed=0, within=("source", "family"))
    keep = ("within_tool_mean", "within_tool_sd", "within_tool_se", "within_tool", "pass", "within_tool_by_source_mean")
    res["T7-a"]["shuffle_a_seed0"] = {k: sa[k] for k in keep}
    res["T7-a"]["shuffle_b_seed0"] = {k: sb[k] for k in keep}
    log(tag, "T7-a shuffles a/b", round(sa["within_tool_mean"], 4), round(sb["within_tool_mean"], 4), round(time.time() - t0))

    t0 = time.time()
    ctx = C2.ctx_for(rows)
    fp_r = M.grid_maker("tool_weighted_logreg", X23, ctx, {"kmax": 128}, M.LRU(8))(H21C_GRID5)
    rb = E.shuffle_test(fp_r, rows, 20, seed=0, within=("source", "family"))
    res["ref_H2-1c_shuffle_b_seed0"] = {k: rb[k] for k in ("within_tool_mean", "within_tool_sd", "within_tool_se")}
    log(tag, "ref H2-1c shuffle b", round(rb["within_tool_mean"], 4), round(time.time() - t0))

    t = res["T7-a"]
    own_b = sb["within_tool_mean"]
    ref_new = rb["within_tool_mean"]
    h10, h3, s0 = t["seed0_9"]["value"], t["seed012"]["value"], t["seed0_9"]["per_seed"][0]
    t["candidate_rules"] = {
        "i_prime_10seed_vs_ref_old": h10 - max(own_b, REF_B_OLD),
        "i_prime_10seed_vs_ref_same_labels": h10 - max(own_b, ref_new),
        "i_prime_seed012_vs_ref_old": h3 - max(own_b, REF_B_OLD),
        "i_dprime_seed0": s0 - own_b,
        "ii_seed012_minus_length_step": h3 - t["seed012"]["baselines"]["length+step"],
        "ii_10seed_minus_length_step": h10 - t["seed0_9"]["baselines"]["length+step"],
        "ref_b_old": REF_B_OLD, "ref_b_same_labels": ref_new, "own_b": own_b,
        "se_ref_b_same_labels": rb["within_tool_se"], "se_own_b": sb["within_tool_se"],
    }
    g = E.GATE
    t["gate_conditions_seed012"] = {
        "1_within_tool_ge_0.90_and_each_seed_ge_0.88": bool(h3 >= g["within_tool_min"] and min(t["seed012"]["per_seed"]) >= g["per_seed_min"]),
        "2_ci_low_ge_0.80": bool(t["seed012"]["ci95"]["ci_low"] >= g["ci_low_min"]),
        "3a_shuffle_a_0.5pm0.05": bool(abs(sa["within_tool_mean"] - 0.5) <= g["shuffle_tol"]),
        "3b_headline_minus_own_b_ge_0.10": bool(h3 - own_b >= g["shuffle_family_margin"]),
        "5_each_source_ge_0.85": bool(all((v or 0) >= g["per_source_min"] for v in t["seed012"]["by_source"].values())),
    }
    return res


def main(tags):
    assert E.evaluate_sha256() == SHA, E.evaluate_sha256()
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / "result.json"
    res = json.loads(path.read_text(encoding="utf-8")) if path.is_file() else {}
    res["evaluate_sha256"] = E.evaluate_sha256()
    for tag in tags:
        res[tag] = run_view(tag)
        path.write_text(json.dumps(E.to_jsonable(res), indent=1, ensure_ascii=False), encoding="utf-8")
    log("DONE")


if __name__ == "__main__":
    main(sys.argv[1:] or ["v1", "v2"])

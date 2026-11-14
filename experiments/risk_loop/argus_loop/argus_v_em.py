"""Argus-V-em: supervised hidden-state embedding experiment, separate from the frozen Argus-V1 loop."""
from __future__ import annotations

import json
import os
import random
import sys
import time
from pathlib import Path

for _name in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ.setdefault(_name, "2")

import numpy as np
import torch
from torch import nn

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from experiments.risk_loop.argus_loop import evaluate as E
from experiments.risk_loop.argus_loop.argus_v_p import Ctx, oof_path

REPORT = ROOT / "reports" / "risk-loop" / "argus-v-em"
OUT = ROOT / "artifacts" / "risk-loop" / "argus-v-em"
VISIBLE_FILE = ROOT / "reports" / "risk-loop" / "argus-v-p" / "visible_flag.json"
ARCHS = {"EM32": 32, "EM64": 64, "EM128": 128}
SEEDS = (0, 1, 2)
EPOCHS = 60
LR = 1e-3
WEIGHT_DECAY = 1e-2
DROPOUT = 0.15


class LearnedEmbedding(nn.Module):
    def __init__(self, n_in: int, width: int):
        super().__init__()
        self.encoder = nn.Sequential(nn.Linear(n_in, width), nn.LayerNorm(width), nn.GELU(), nn.Dropout(DROPOUT))
        self.head = nn.Linear(width, 1)

    def forward(self, x):
        z = self.encoder(x)
        return self.head(z).squeeze(-1)


class LinearScorer(nn.Module):
    """Same raw inputs and loss, but no learned bottleneck or nonlinear embedding."""
    def __init__(self, n_in: int):
        super().__init__()
        self.head = nn.Linear(n_in, 1)

    def forward(self, x):
        return self.head(x).squeeze(-1)


def robust_params(x_train: np.ndarray):
    med = np.median(x_train, axis=0)
    q25, q75 = np.quantile(x_train, [0.25, 0.75], axis=0)
    scale = q75 - q25
    scale[scale < 1e-6] = 1.0
    return med.astype(np.float32), scale.astype(np.float32)


def robust_scale(x_all: np.ndarray, med: np.ndarray, scale: np.ndarray):
    return np.clip((x_all - med) / scale, -5.0, 5.0).astype(np.float32)


def visible_mask(cx: Ctx):
    raw = json.loads(VISIBLE_FILE.read_text(encoding="utf-8"))
    mask = np.zeros(cx.n, dtype=bool)
    for row in raw["violations"]:
        i = int(row["pos"])
        assert cx.y[i] == 1
        assert str(cx.rows.unit_id[i]) == row["unit_id"]
        assert int(cx.rows.step_index[i]) == row["step_index"]
        mask[i] = bool(row["visible"])
    return mask, raw["rule_version"]


def prepare(cx: Ctx, vis: np.ndarray):
    X = np.concatenate([cx.feats["L23:max"], cx.feats["L16:pre"]], axis=1).astype(np.float32)
    target_rows = ((cx.y == 0) | vis)
    evaluation_rows = target_rows.copy()
    eligible = {}
    for cell in sorted(set(cx.groups.tolist())):
        m = cx.groups == cell
        positives = int(vis[m].sum())
        negatives = int(((cx.y == 0) & m).sum())
        eligible[cell] = {"visible_positives": positives, "normals": negatives,
                          "min3": positives >= 3 and negatives >= 3,
                          "min2": positives >= 2 and negatives >= 2}
    return X, target_rows, evaluation_rows, eligible


def score_metric(cx: Ctx, scores, eval_mask, min_pos=3):
    idx = np.flatnonzero(eval_mask)
    return E.within_tool_auroc(np.asarray(scores)[idx], cx.y[idx], cx.groups[idx], min_pos=min_pos)


def sample_training_rows(cx: Ctx, fit_rows: np.ndarray, vis: np.ndarray, seed: int):
    """Keep every visible positive and a capped, reproducible normal sample in each tool/source cell."""
    rng = np.random.default_rng(seed)
    positives = fit_rows[vis[fit_rows]]
    normals = fit_rows[cx.y[fit_rows] == 0]
    keep = [positives]
    for cell in sorted(set(cx.groups[normals].tolist())):
        cell_normals = normals[cx.groups[normals] == cell]
        cell_pos = int(np.sum(cx.groups[positives] == cell))
        cap = max(30, 20 * cell_pos)
        if len(cell_normals) > cap:
            cell_normals = rng.choice(cell_normals, size=cap, replace=False)
        keep.append(np.asarray(cell_normals, dtype=np.int64))
    return np.sort(np.concatenate(keep))


def fit_model(x_train: np.ndarray, y_train: np.ndarray, width: int, seed: int):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.set_num_threads(2)
    med, scale = robust_params(x_train)
    a = torch.from_numpy(robust_scale(x_train, med, scale))
    yt = torch.from_numpy(y_train.astype(np.float32))
    model = LinearScorer(x_train.shape[1]) if width == 0 else LearnedEmbedding(x_train.shape[1], width)
    pos = max(float(yt.sum()), 1.0)
    neg = max(float(len(yt) - yt.sum()), 1.0)
    pos_weight = torch.tensor(min(20.0, float(np.sqrt(neg / pos))), dtype=torch.float32)
    loss_fn = nn.BCEWithLogitsLoss(pos_weight=pos_weight)
    opt = torch.optim.AdamW(model.parameters(), lr=LR, weight_decay=WEIGHT_DECAY)
    for _ in range(EPOCHS):
        model.train()
        opt.zero_grad(set_to_none=True)
        loss = loss_fn(model(a), yt)
        loss.backward()
        opt.step()
    return model, med, scale


def fit_fold(x_train: np.ndarray, y_train: np.ndarray, x_score: np.ndarray, width: int, seed: int):
    if len(y_train) == 0 or int(np.sum(y_train)) == 0 or int(np.sum(y_train)) == len(y_train):
        return np.zeros(len(x_score), dtype=np.float64)
    model, med, scale = fit_model(x_train, y_train, width, seed)
    b = torch.from_numpy(robust_scale(x_score, med, scale))
    model.eval()
    with torch.no_grad():
        return model(b).cpu().numpy().astype(np.float64)


def score_checkpoint(path: str | Path, features: np.ndarray):
    """Return raw ranking scores for concatenated L23:max + L16:pre features."""
    payload = torch.load(path, map_location="cpu", weights_only=True)
    X = np.asarray(features, dtype=np.float32)
    if X.ndim != 2 or X.shape[1] != int(payload["input_width"]):
        raise ValueError(f"expected a 2-D feature matrix with width {payload['input_width']}, got {X.shape}")
    model = LearnedEmbedding(int(payload["input_width"]), int(payload["width"]))
    model.load_state_dict(payload["state_dict"])
    model.eval()
    scaled = torch.from_numpy(robust_scale(X, payload["median"].numpy(), payload["scale"].numpy()))
    with torch.no_grad():
        return model(scaled).cpu().numpy().astype(np.float64)


def run():
    OUT.mkdir(parents=True, exist_ok=True)
    cx = Ctx()
    vis, rule = visible_mask(cx)
    X, train_rows, eval_rows, eligible = prepare(cx, vis)
    metric_mask = eval_rows & np.isin(cx.groups, [k for k, v in eligible.items() if v["min3"]])
    metric_mask2 = eval_rows & np.isin(cx.groups, [k for k, v in eligible.items() if v["min2"]])
    print(f"rows={cx.n} train_target={int(train_rows.sum())} target_positive={int(vis.sum())} input={X.shape} rule={rule}", flush=True)
    print("eligible:", json.dumps(eligible, ensure_ascii=False), flush=True)
    results = {"name": "Argus-V-em", "rule": rule, "input": "L23:max + L16:pre", "input_width": X.shape[1],
               "train_rows": int(train_rows.sum()), "visible_positive_rows": int(vis.sum()),
               "unique_visible_feature_rows": int(len(set(cx.hashes[vis].tolist()))),
               "protocol": {"folds": 5, "seeds": list(SEEDS), "epochs": EPOCHS, "lr": LR,
                            "weight_decay": WEIGHT_DECAY, "dropout": DROPOUT, "optimizer": "AdamW",
               "loss": "BCEWithLogitsLoss; sqrt class weight capped at 20",
               "negative_sampling": "all visible positives; up to max(30, 20x visible positives) normals per tool/source cell per fold"},
               "eligible_cells": {k: v for k, v in eligible.items() if v["min2"]},
               "cells_with_zero_visible_rows": sum(v["visible_positives"] == 0 for v in eligible.values()),
               "architectures": {}}
    for name, width in ARCHS.items():
        paths = [OUT / f"oof_{name}_s{seed}.npy" for seed in SEEDS]
        all_scores = []
        for seed, path in zip(SEEDS, paths):
            if path.is_file():
                all_scores.append(np.load(path))
                continue
            oof = np.full(cx.n, np.nan, dtype=np.float64)
            for fold_i, (tr, te) in enumerate(E.make_folds(cx.rows, 5, seed)):
                fit = sample_training_rows(cx, tr[train_rows[tr]], vis,
                                           710000 + seed * 100 + fold_i)
                model_y = vis[fit].astype(np.int64)
                scores = fit_fold(X[fit], model_y, X[te], width,
                                  300000 + seed * 100 + fold_i * 10 + width)
                oof[te] = scores
                print(f"{name} seed={seed} fold={fold_i} n={len(fit)} visible={int(model_y.sum())} scored={len(te)}", flush=True)
            if not np.isfinite(oof).all():
                raise RuntimeError(f"non-finite OOF scores for {name} seed {seed}")
            np.save(path, oof)
            all_scores.append(oof)
        vals3 = [score_metric(cx, s, metric_mask, 3) for s in all_scores]
        vals2 = [score_metric(cx, s, metric_mask2, 2) for s in all_scores]
        all3 = [score_metric(cx, s, np.ones(cx.n, dtype=bool), 3) for s in all_scores]
        results["architectures"][name] = {
            "width": width,
            "visible_min3": {"mean": float(np.mean([v["value"] for v in vals3])),
                              "per_seed": [float(v["value"]) for v in vals3],
                              "cells": vals3[0]["n_tools"], "positives": vals3[0]["n_positives_included"],
                              "per_cell": vals3[0]["per_tool"]},
            "visible_min2": {"mean": float(np.mean([v["value"] for v in vals2])),
                              "per_seed": [float(v["value"]) for v in vals2],
                              "cells": vals2[0]["n_tools"], "positives": vals2[0]["n_positives_included"],
                              "per_cell": vals2[0]["per_tool"]},
            "all_violations_min3": {"mean": float(np.mean([v["value"] for v in all3])),
                                    "per_seed": [float(v["value"]) for v in all3],
                                    "cells": all3[0]["n_tools"], "positives": all3[0]["n_positives_included"]},
        }
        print(name, results["architectures"][name]["visible_min3"], flush=True)

    # Frozen OOF comparators, scored on identical rows and cells.
    base = {}
    for key, paths in {
        "Argus-V-p/P1": [oof_path("P1", "A", s) for s in SEEDS],
        "Argus-V-p/P5": [oof_path("P5", "A", s) for s in SEEDS],
    }.items():
        scores = [np.load(p) for p in paths]
        v3 = [score_metric(cx, s, metric_mask, 3) for s in scores]
        v2 = [score_metric(cx, s, metric_mask2, 2) for s in scores]
        base[key] = {"visible_min3": float(np.mean([v["value"] for v in v3])),
                     "visible_min2": float(np.mean([v["value"] for v in v2]))}
    results["comparators"] = base
    results["evaluation_sha256"] = E.evaluate_sha256()
    results["created_at"] = time.strftime("%Y-%m-%d %H:%M:%S")
    selected = max(results["architectures"], key=lambda name: results["architectures"][name]["visible_min3"]["mean"])
    selected_width = ARCHS[selected]
    all_train = np.flatnonzero(train_rows)
    final_rows = sample_training_rows(cx, all_train, vis, 910032)
    final_y = vis[final_rows].astype(np.int64)
    final_model, final_med, final_scale = fit_model(X[final_rows], final_y, selected_width, 910032)
    model_path = OUT / "argus_v_em_round01.pt"
    torch.save({"state_dict": final_model.state_dict(), "width": selected_width, "input_width": X.shape[1],
                "median": torch.from_numpy(final_med), "scale": torch.from_numpy(final_scale),
                "feature_spec": ["L23:max", "L16:pre"], "visible_rule": rule,
                "train_row_count": int(len(final_rows)), "train_visible_positives": int(final_y.sum()),
                "seed": 910032, "epochs": EPOCHS, "lr": LR, "weight_decay": WEIGHT_DECAY,
                "dropout": DROPOUT}, model_path)
    results["selected_on_development_oof"] = selected
    results["export"] = {"path": str(model_path.relative_to(ROOT)).replace("\\", "/"),
                         "sha256": __import__("hashlib").sha256(model_path.read_bytes()).hexdigest(),
                         "train_rows": int(len(final_rows)), "visible_positives": int(final_y.sum())}
    (REPORT / "round01_results.json").write_text(json.dumps(E.to_jsonable(results), indent=2, ensure_ascii=False), encoding="utf-8")
    print("DONE", json.dumps({"scores": {k: v["visible_min3"]["mean"] for k, v in results["architectures"].items()},
                              "selected": selected, "export": results["export"]}), flush=True)


if __name__ == "__main__":
    run()

"""Train-only nested group evaluation for three independently named residual heads.

Outer held-out folds are scored once, after epoch selection on an inner group holdout.
All fitted statistics, negative sampling and optimization use the current fit rows only.
No existing Argus-V evaluation module, generator, labels, or source cache is modified.
"""
from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import asdict, replace
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import random
from uuid import uuid4

import numpy as np
import torch
from sklearn.metrics import average_precision_score, roc_auc_score
from sklearn.model_selection import StratifiedGroupKFold

from experiments.residual_probes.shared import (
    ARCHITECTURES, Config, FEATURE_SPEC, checked_xy, fit_scaler, make_model, transform,
)

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = "argus-v.residual-probe.v1"


def merge_groups(groups, hashes):
    """Merge connected group ids when any feature row is identical."""
    if len(groups) != len(hashes):
        raise ValueError("group/hash lengths differ")
    parent = list(range(len(groups)))
    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    for keys in (groups, hashes):
        seen = {}
        for i, key in enumerate(keys):
            key = str(key)
            if key in seen:
                a, b = find(i), find(seen[key])
                parent[max(a, b)] = min(a, b)
            else:
                seen[key] = i
    return np.asarray([find(i) for i in range(len(groups))], dtype=np.int64)


def grouped_folds(y, groups, count, seed):
    y, groups = np.asarray(y), np.asarray(groups)
    k = min(int(count), len(np.unique(groups)))
    if k < 2 or set(np.unique(y)) != {0, 1}:
        raise ValueError("need >=2 independent groups and both label classes")
    splitter = StratifiedGroupKFold(n_splits=k, shuffle=True, random_state=int(seed))
    out = [(np.sort(a), np.sort(b)) for a, b in splitter.split(np.zeros(len(y)), y, groups)]
    for a, b in out:
        if set(groups[a]) & set(groups[b]):
            raise RuntimeError("group leakage")
        if set(np.unique(y[a])) != {0, 1} or set(np.unique(y[b])) != {0, 1}:
            raise ValueError("a grouped fold has only one class; reduce folds or collect more groups")
    return out


def sample_fit_rows(y, cells, cfg, seed):
    """Preserve positives; optionally cap normals per tool/source training cell."""
    y, cells = np.asarray(y), np.asarray(cells)
    if cfg.normal_ratio == 0:
        return np.arange(len(y))
    rng = np.random.default_rng(seed)
    pos = np.flatnonzero(y == 1)
    kept = [pos]
    for cell in sorted(set(cells[y == 0].tolist())):
        normals = np.flatnonzero((y == 0) & (cells == cell))
        n_pos = int(np.sum((y == 1) & (cells == cell)))
        cap = max(cfg.min_normals, cfg.normal_ratio * n_pos)
        if len(normals) > cap:
            normals = rng.choice(normals, size=cap, replace=False)
        kept.append(normals)
    return np.sort(np.concatenate(kept))


def predict_model(model, x, med, scale, batch_size=256, device="cpu"):
    z = transform(x, med, scale)
    model.eval()
    result = []
    with torch.inference_mode():
        for start in range(0, len(z), batch_size):
            a = torch.from_numpy(z[start:start + batch_size]).to(device)
            result.append(model(a).cpu().numpy())
    scores = np.concatenate(result).astype(np.float64) if result else np.empty(0, np.float64)
    if not np.isfinite(scores).all():
        raise ValueError("non-finite predictions")
    return scores


def fit_model(x, y, cfg, seed, epochs=None, validation=None):
    """Return last model and selected epoch; inner models are discarded after epoch selection."""
    x, y = checked_xy(x, y)
    if set(np.unique(y)) != {0, 1}:
        raise ValueError("fit rows must contain both classes")
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.set_num_threads(2)
    if cfg.device.startswith("cuda"):
        if not torch.cuda.is_available():
            raise ValueError("CUDA requested but not available")
        torch.cuda.manual_seed_all(seed)
    med, scale = fit_scaler(x)
    a = torch.from_numpy(transform(x, med, scale))
    labels = torch.from_numpy(y.astype(np.float32))
    if validation is not None:
        vx, vy = checked_xy(*validation)
        if set(np.unique(vy)) != {0, 1}:
            raise ValueError("inner selection rows must contain both classes")
    model = make_model(x.shape[1], cfg).to(cfg.device)
    loss_fn = torch.nn.BCEWithLogitsLoss(pos_weight=torch.tensor(cfg.pos_weight, device=cfg.device))
    optimizer = torch.optim.AdamW(model.parameters(), lr=cfg.learning_rate, weight_decay=cfg.weight_decay)
    generator = torch.Generator().manual_seed(seed)
    budget = int(epochs if epochs is not None else cfg.epochs)
    if budget < 1:
        raise ValueError("epochs must be positive")
    best_epoch, best_ap, stale = budget, -1.0, 0
    curve = []
    for epoch in range(1, budget + 1):
        model.train()
        order = torch.randperm(len(a), generator=generator)
        loss_sum = 0.0
        for start in range(0, len(order), cfg.batch_size):
            idx = order[start:start + cfg.batch_size]
            bx, by = a[idx].to(cfg.device), labels[idx].to(cfg.device)
            optimizer.zero_grad(set_to_none=True)
            loss = loss_fn(model(bx), by)
            if not bool(torch.isfinite(loss)):
                raise ValueError("non-finite training loss")
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0, error_if_nonfinite=True)
            optimizer.step()
            loss_sum += float(loss.detach()) * len(idx)
        record = {"epoch": epoch, "train_weighted_bce": loss_sum / len(a)}
        if validation is not None:
            scores = predict_model(model, vx, med, scale, cfg.batch_size, cfg.device)
            ap = float(average_precision_score(vy, scores))
            record["inner_validation_ap"] = ap
            if ap > best_ap + 1e-8:
                best_ap, best_epoch, stale = ap, epoch, 0
            else:
                stale += 1
        curve.append(record)
        if validation is not None and stale >= cfg.patience:
            break
    model.eval()
    return model, med, scale, {
        "selected_epoch": best_epoch, "epochs_run": len(curve),
        "selection_ap": best_ap if validation is not None else None,
        "fit_count": len(y), "fit_positives": int(y.sum()),
        "actual_pos_weight": cfg.pos_weight, "curve": curve,
    }


def ranking_metrics(y, scores, cells, min_class=3):
    y, scores, cells = np.asarray(y), np.asarray(scores), np.asarray(cells)
    if not (len(y) == len(scores) == len(cells)) or not np.isfinite(scores).all():
        raise ValueError("metrics need aligned finite scores")
    per_cell = {}
    for cell in sorted(set(cells.tolist())):
        m = cells == cell
        pos, neg = int(y[m].sum()), int(m.sum() - y[m].sum())
        per_cell[str(cell)] = {
            "positives": pos, "negatives": neg,
            "auroc": float(roc_auc_score(y[m], scores[m])) if pos >= min_class and neg >= min_class else None,
        }
    eligible = [v for v in per_cell.values() if v["auroc"] is not None]
    npos = sum(v["positives"] for v in eligible)
    return {
        "rows": len(y), "positives": int(y.sum()),
        "positive_rate": float(y.mean()),
        "auroc": float(roc_auc_score(y, scores)) if len(np.unique(y)) == 2 else None,
        "average_precision": float(average_precision_score(y, scores)) if np.any(y == 1) else None,
        "within_tool_source_auroc": sum(v["auroc"] * v["positives"] for v in eligible) / npos if npos else None,
        "eligible_cells": len(eligible), "eligible_positives": npos, "per_cell": per_cell,
    }


def dataset_digest(x, y, groups, row_ids, cells):
    digest = hashlib.sha256()
    for a in (x, np.asarray(y, np.int64), np.asarray(groups, np.int64), np.asarray(row_ids, np.int64)):
        a = np.ascontiguousarray(a)
        digest.update(str(a.shape).encode())
        digest.update(a.tobytes())
    digest.update(json.dumps([str(c) for c in cells], ensure_ascii=False).encode())
    return digest.hexdigest()


def load_training_data(cfg):
    """Reuse the host's existing feature alignment; Ctx/E refuse validation and test rows."""
    from experiments.risk_loop.argus_loop import argus_v_em as upstream
    from experiments.risk_loop.argus_loop import evaluate as evaluation
    cx = upstream.Ctx()
    if set(cx.rows.split.astype(str).tolist()) != {"train"}:
        raise PermissionError("only train-split features are allowed")
    x = np.concatenate([cx.feats[k] for k in FEATURE_SPEC], axis=1).astype(np.float32)
    y = np.asarray(cx.y, dtype=np.int64)
    keep = np.ones(len(y), dtype=bool)
    visible_rule = None
    if cfg.target == "visible":
        visible, visible_rule = upstream.visible_mask(cx)
        keep = (y == 0) | visible
    groups = merge_groups(evaluation.group_components(cx.rows), cx.hashes)
    return {
        "x": x[keep], "y": y[keep], "groups": groups[keep],
        "cells": np.asarray(cx.groups).astype(str)[keep],
        "row_ids": np.asarray(cx.rows.row_id, np.int64)[keep],
        "source": np.asarray(cx.src).astype(str)[keep],
        "label_status": dict(Counter(cx.rows.label_status[keep].astype(str).tolist())),
        "visible_rule": visible_rule, "excluded_rows": int((~keep).sum()),
        "evaluation_sha256": evaluation.evaluate_sha256(),
    }


def run_nested(x, y, groups, cells, row_ids, cfg, seeds):
    x, y = checked_xy(x, y)
    groups, cells, row_ids = np.asarray(groups), np.asarray(cells), np.asarray(row_ids)
    if any(a.shape != (len(y),) for a in (groups, cells, row_ids)):
        raise ValueError("metadata must have one value per feature row")
    if len(set(row_ids.tolist())) != len(row_ids):
        raise ValueError("duplicate row ids")
    results, all_oof, selected_epochs = [], [], []
    for seed in seeds:
        oof = np.full(len(y), np.nan)
        folds = []
        for fold_i, (outer_fit, outer_score) in enumerate(grouped_folds(y, groups, cfg.outer_folds, seed)):
            inner_fit, inner_select = grouped_folds(
                y[outer_fit], groups[outer_fit], cfg.inner_folds, seed + 1000 + fold_i,
            )[0]
            inner_fit, inner_select = outer_fit[inner_fit], outer_fit[inner_select]
            sampled_inner = inner_fit[sample_fit_rows(y[inner_fit], cells[inner_fit], cfg, seed + fold_i + 2000)]
            train_seed = seed * 10000 + fold_i * 100 + 17
            _, _, _, selection = fit_model(
                x[sampled_inner], y[sampled_inner], cfg, train_seed,
                validation=(x[inner_select], y[inner_select]),
            )
            epoch = int(selection["selected_epoch"])
            sampled_outer = outer_fit[sample_fit_rows(y[outer_fit], cells[outer_fit], cfg, seed + fold_i + 3000)]
            model, med, scale, fitted = fit_model(
                x[sampled_outer], y[sampled_outer], cfg, train_seed, epochs=epoch,
            )
            scores = predict_model(model, x[outer_score], med, scale, cfg.batch_size, cfg.device)
            oof[outer_score] = scores
            selected_epochs.append(epoch)
            folds.append({
                "fold": fold_i, "selected_epoch": epoch,
                "inner_selection": selection,
                "outer_refit": {k: v for k, v in fitted.items() if k != "curve"},
                "inner_fit_row_ids": row_ids[sampled_inner].tolist(),
                "inner_selection_row_ids": row_ids[inner_select].tolist(),
                "outer_fit_row_ids": row_ids[sampled_outer].tolist(),
                "outer_score_row_ids": row_ids[outer_score].tolist(),
                "metrics": ranking_metrics(y[outer_score], scores, cells[outer_score]),
            })
            print(f"{cfg.architecture} seed={seed} fold={fold_i} epoch={epoch} "
                  f"fit={len(sampled_outer)} score={len(outer_score)}", flush=True)
        if not np.isfinite(oof).all():
            raise RuntimeError("OOF scores are incomplete")
        results.append({"seed": seed, "folds": folds, "metrics": ranking_metrics(y, oof, cells)})
        all_oof.append(oof)
    return results, np.stack(all_oof), max(1, int(np.median(selected_epochs)))


def checkpoint_payload(model, med, scale, cfg, fingerprint, final_epoch):
    return {
        "schema_version": SCHEMA, "config": asdict(cfg), "input_width": len(med),
        "feature_spec": list(FEATURE_SPEC), "target": cfg.target,
        "state_dict": {k: v.detach().cpu() for k, v in model.state_dict().items()},
        "median": torch.from_numpy(med.copy()), "scale": torch.from_numpy(scale.copy()),
        "dataset_sha256": fingerprint, "trained_epochs": int(final_epoch),
        "score_semantics": "raw logit; sigmoid is not a calibrated violation probability",
    }


def restore_checkpoint(payload, device="cpu"):
    if payload.get("schema_version") != SCHEMA or payload.get("feature_spec") != list(FEATURE_SPEC):
        raise ValueError("unsupported checkpoint or feature contract")
    cfg = Config(**payload["config"])
    model = make_model(int(payload["input_width"]), cfg).to(device)
    model.load_state_dict(payload["state_dict"], strict=True)
    med, scale = payload["median"].cpu().numpy(), payload["scale"].cpu().numpy()
    if med.shape != (int(payload["input_width"]),) or scale.shape != med.shape:
        raise ValueError("invalid normalization width")
    if not (np.isfinite(med).all() and np.isfinite(scale).all() and (scale > 0).all()):
        raise ValueError("invalid normalization values")
    model.eval()
    return model, med, scale


def score_checkpoint(path, features, device="cpu"):
    payload = torch.load(path, map_location="cpu", weights_only=True)
    model, med, scale = restore_checkpoint(payload, device)
    return predict_model(model, features, med, scale, device=device)


def parser_for(architecture):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--width", type=int, default=128)
    p.add_argument("--blocks", type=int, default=8 if architecture == "stochastic_depth_mlp" else 4)
    p.add_argument("--expansion", type=int, default=2)
    p.add_argument("--dropout", type=float, default=0.15)
    p.add_argument("--drop-path", type=float, default=0.1 if architecture == "stochastic_depth_mlp" else 0.0)
    p.add_argument("--epochs", type=int, default=300)
    p.add_argument("--patience", type=int, default=20)
    p.add_argument("--learning-rate", type=float, default=1e-3)
    p.add_argument("--weight-decay", type=float, default=1e-2)
    p.add_argument("--pos-weight", type=float, default=15.0)
    p.add_argument("--batch-size", type=int, default=256)
    p.add_argument("--outer-folds", type=int, default=5)
    p.add_argument("--inner-folds", type=int, default=3)
    p.add_argument("--normal-ratio", type=int, default=20, help="0 keeps all normals; otherwise cap normals per tool/source cell")
    p.add_argument("--min-normals", type=int, default=30)
    p.add_argument("--target", choices=("all", "visible"), default="all")
    p.add_argument("--device", default="cpu")
    p.add_argument("--seeds", type=int, nargs="+", default=[0, 1, 2])
    p.add_argument("--output", type=Path, help="must not exist; default is a unique artifacts/residual-probes directory")
    return p


def main(architecture, argv=None):
    args = parser_for(architecture).parse_args(argv)
    values = vars(args).copy()
    seeds, output = values.pop("seeds"), values.pop("output")
    try:
        cfg = Config(architecture=architecture, **values)
        if not seeds or len(set(seeds)) != len(seeds) or any(s < 0 or s >= 2**31 for s in seeds):
            raise ValueError("seeds must be distinct integers in [0,2**31)")
        if output is not None and output.exists():
            raise FileExistsError(f"output already exists: {output}")
        data = load_training_data(cfg)
        fingerprint = dataset_digest(data["x"], data["y"], data["groups"], data["row_ids"], data["cells"])
        configuration = {"config": asdict(cfg), "seeds": seeds, "dataset_sha256": fingerprint}
        key = hashlib.sha256(json.dumps(configuration, sort_keys=True).encode()).hexdigest()[:12]
        if output is None:
            stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
            output = ROOT / "artifacts" / "residual-probes" / architecture / f"{stamp}-{key}-{uuid4().hex[:6]}"
        output.mkdir(parents=True, exist_ok=False)
        # Failed runs retain config.json for diagnosis; never silently reuse OOF/checkpoints.
        (output / "config.json").write_text(json.dumps(configuration, indent=2), encoding="utf-8")
        results, oof, final_epoch = run_nested(
            data["x"], data["y"], data["groups"], data["cells"], data["row_ids"], cfg, seeds,
        )
        final_idx = sample_fit_rows(data["y"], data["cells"], cfg, 910032)
        model, med, scale, fitted = fit_model(
            data["x"][final_idx], data["y"][final_idx], cfg, 910032, epochs=final_epoch,
        )
        payload = checkpoint_payload(model, med, scale, cfg, fingerprint, final_epoch)
        torch.save(payload, output / "model.pt")
        np.savez_compressed(output / "oof.npz", scores=oof, labels=data["y"], row_ids=data["row_ids"],
                            seeds=np.asarray(seeds), groups=data["groups"], cells=data["cells"])
        source_metrics = {
            str(s): [ranking_metrics(data["y"][data["source"] == s], scores[data["source"] == s],
                                    data["cells"][data["source"] == s]) for scores in oof]
            for s in sorted(set(data["source"].tolist()))
        }
        report = {
            "schema_version": SCHEMA, **configuration, "feature_spec": list(FEATURE_SPEC),
            "status": "TRAIN_ONLY_NESTED_GROUP_CV", "test_evaluated": False,
            "validation_split_opened": False, "epoch_selection": "inner group holdout AP; outer fold refit",
            "final_epoch": final_epoch, "final_fit": {k: v for k, v in fitted.items() if k != "curve"},
            "label_status": data["label_status"], "visible_rule": data["visible_rule"],
            "excluded_rows": data["excluded_rows"], "evaluation_sha256": data["evaluation_sha256"],
            "source_metrics": source_metrics, "results": results,
            "torch_version": str(torch.__version__),
            "score_semantics": payload["score_semantics"],
            "limitations": [
                "First projection can discard information; residual paths cannot recover it.",
                "CV is not independent test performance. No operating threshold or probability calibration is fitted.",
                "All-target and visible-target metrics must not be compared as the same population.",
            ],
        }
        (output / "report.json").write_text(json.dumps(report, indent=2, allow_nan=False), encoding="utf-8")
        print(f"Completed: {output}", flush=True)
        return 0
    except (ValueError, OSError, PermissionError, RuntimeError) as error:
        print(f"Residual probe stopped: {error}", flush=True)
        return 2

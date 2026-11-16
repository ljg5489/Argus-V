"""Argus-V-em round 01 re-run with per-epoch recording (reports/risk-loop/argus-v-em/addendum-2.md).

Same models, rows, folds, seeds and optimiser as argus_v_em.py and argus_v_em_linear.py. The only addition:
after every epoch the model is put in evaluation mode and scored without gradients (no random draw), so the
training trajectory is unchanged. The run ends by comparing its epoch-60 scores with the saved round-01 scores.

Training starts only with --approved (user approval 2026-11-16, all four models).
Usage : PYTHONUTF8=1 py -3.11 -u experiments/risk_loop/argus_loop/argus_v_em_epochs.py --approved
Output: artifacts/risk-loop/argus-v-em/epochs/<model>.npz, final_EM32.npz   (ignored)
        reports/risk-loop/argus-v-em/epoch_history.json                      (summary used by the figures)
"""
from __future__ import annotations

import json
import os
import random
import sys
import time
from pathlib import Path

for _name in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):   # as argus_v_em.py, before numpy/torch
    os.environ.setdefault(_name, "2")

import numpy as np  # noqa: E402
import torch  # noqa: E402
from torch import nn  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from experiments.risk_loop import harness as H  # noqa: E402
from experiments.risk_loop.argus_loop import argus_v_em as EM  # noqa: E402
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402

OUT = EM.OUT / "epochs"
MODELS = {"EM32": 32, "EM64": 64, "EM128": 128, "LINEAR": 0}
HELDOUT_SAMPLE_SEED = 720000      # held-out rows for the loss are picked by the training sampling rule, own seed


def log(*a):
    print(time.strftime("%H:%M:%S"), *a, flush=True)


def model_seed(name: str, seed: int, fold_i: int) -> int:
    return 300000 + seed * 100 + fold_i * 10 + MODELS[name]      # LINEAR adds 0, as in argus_v_em_linear.py


def scaled(x: np.ndarray, med: np.ndarray, scale: np.ndarray) -> np.ndarray:
    """EM.robust_scale in row chunks (same arithmetic, no large temporaries)."""
    out = np.empty(x.shape, dtype=np.float32)
    for i in range(0, len(x), 2048):
        out[i:i + 2048] = EM.robust_scale(x[i:i + 2048], med, scale)
    return out


def fit_logged(x_train, y_train, width, seed, score_sets, stats=None, snapshot_epochs=()):
    """argus_v_em.fit_model line for line, plus an evaluation-mode scoring pass after each epoch.

    Returns (med, scale, state_dict, pos_weight, loss_optimised[E], train_scores[E, n_train], {name: scores[E, n]}).
    If ``stats`` is a dict it receives grad_norm[E] (gradient L2 norm of each update), weight_norm[E] (parameter L2
    norm after it) and snapshots {epoch: state_dict copy} for ``snapshot_epochs``. Reading these changes nothing."""
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.set_num_threads(2)
    med, scale = EM.robust_params(x_train)
    a = torch.from_numpy(EM.robust_scale(x_train, med, scale))
    yt = torch.from_numpy(y_train.astype(np.float32))
    model = EM.LinearScorer(x_train.shape[1]) if width == 0 else EM.LearnedEmbedding(x_train.shape[1], width)
    pos = max(float(yt.sum()), 1.0)
    neg = max(float(len(yt) - yt.sum()), 1.0)
    pos_weight = torch.tensor(min(20.0, float(np.sqrt(neg / pos))), dtype=torch.float32)
    loss_fn = nn.BCEWithLogitsLoss(pos_weight=pos_weight)
    opt = torch.optim.AdamW(model.parameters(), lr=EM.LR, weight_decay=EM.WEIGHT_DECAY)
    extra = {k: torch.from_numpy(scaled(v, med, scale)) for k, v in score_sets.items()}
    loss_opt = np.zeros(EM.EPOCHS)
    train_scores = np.zeros((EM.EPOCHS, len(yt)), dtype=np.float32)
    out = {k: np.zeros((EM.EPOCHS, len(v)), dtype=np.float32) for k, v in extra.items()}
    grad_norm, weight_norm, snaps = np.zeros(EM.EPOCHS), np.zeros(EM.EPOCHS), {}
    for e in range(EM.EPOCHS):
        model.train()
        opt.zero_grad(set_to_none=True)
        loss = loss_fn(model(a), yt)
        loss.backward()
        if stats is not None:
            grad_norm[e] = float(torch.sqrt(sum((p.grad.detach() ** 2).sum() for p in model.parameters())))
        opt.step()
        loss_opt[e] = float(loss.detach())
        model.eval()                                   # recording only: no gradient, no random draw
        with torch.no_grad():
            train_scores[e] = model(a).numpy()
            for k, t in extra.items():
                out[k][e] = model(t).numpy()
            if stats is not None:
                weight_norm[e] = float(torch.sqrt(sum((p ** 2).sum() for p in model.parameters())))
                if (e + 1) in snapshot_epochs:
                    snaps[e + 1] = {k: v.detach().clone() for k, v in model.state_dict().items()}
    if stats is not None:
        stats.update(grad_norm=grad_norm, weight_norm=weight_norm, snapshots=snaps)
    return med, scale, model.state_dict(), float(pos_weight), loss_opt, train_scores, out


def bce(scores: np.ndarray, y: np.ndarray, pos_weight: float) -> float:
    """BCEWithLogitsLoss(pos_weight), mean over rows — the training loss formula, evaluated on given scores."""
    s = torch.from_numpy(np.asarray(scores, dtype=np.float32))
    t = torch.from_numpy(np.asarray(y, dtype=np.float32))
    return float(nn.functional.binary_cross_entropy_with_logits(s, t, pos_weight=torch.tensor(pos_weight)))


class FastWT:
    """E.within_tool_auroc on a fixed row mask with the per-cell row lists built once (same rule, same weights)."""

    def __init__(self, cx, mask, min_pos):
        idx = np.flatnonzero(mask)
        g = cx.groups[idx]
        self.cells = []
        for t in sorted(set(g.tolist()), key=str):
            m = idx[g == t]
            p = int(cx.y[m].sum())
            if p >= min_pos and len(m) - p >= E.MIN_NEG:
                self.cells.append((str(t), m, cx.y[m], p))

    def per_cell(self, s):
        return {t: float(H.auroc(s[m], y)) for t, m, y, _ in self.cells}

    def __call__(self, s):
        den = sum(p for *_, p in self.cells)
        return float(sum(H.auroc(s[m], y) * p for _, m, y, p in self.cells) / den) if den else float("nan")


def wt(scores, y, groups, min_pos):
    r = E.within_tool_auroc(scores, y, groups, min_pos=min_pos)
    return np.nan if r["value"] is None else float(r["value"])


def run_model(name: str, cx, X, vis, train_rows, masks, cells3, cells2):
    width = MODELS[name]
    path = OUT / f"{name}.npz"
    if path.is_file():
        log(name, "already recorded, loading")
        return dict(np.load(path, allow_pickle=False))
    S, K, EP = len(EM.SEEDS), 5, EM.EPOCHS
    oof = np.full((S, EP, cx.n), np.nan, dtype=np.float32)
    rec = {k: np.full((S, K, EP), np.nan) for k in
           ("loss_optimised", "loss_train_eval", "loss_heldout", "auroc_train_min3", "auroc_train_min2",
            "grad_norm", "weight_norm")}
    meta = {k: np.zeros((S, K)) for k in ("pos_weight", "n_fit", "n_pos", "n_heldout_rows", "n_heldout_pos", "seconds")}
    held_cells = np.zeros((S, K, len(cells3)), dtype=np.int8)       # 1 = that min-3 cell is in the held-out fold
    for si, seed in enumerate(EM.SEEDS):
        for fold_i, (tr, te) in enumerate(E.make_folds(cx.rows, 5, seed)):
            t0 = time.time()
            fit = EM.sample_training_rows(cx, tr[train_rows[tr]], vis, 710000 + seed * 100 + fold_i)
            y_fit = vis[fit].astype(np.int64)
            if len(y_fit) == 0 or int(y_fit.sum()) in (0, len(y_fit)):      # same guard as argus_v_em.fit_fold
                oof[si][:, te] = 0.0
                log(name, f"seed={seed} fold={fold_i} skipped (one class)")
                continue
            st = {}
            _, _, _, pw, loss_opt, s_tr, extra = fit_logged(X[fit], y_fit, width, model_seed(name, seed, fold_i),
                                                             {"heldout": X[te]}, stats=st)
            rec["grad_norm"][si, fold_i], rec["weight_norm"][si, fold_i] = st["grad_norm"], st["weight_norm"]
            s_te = extra["heldout"]
            oof[si][:, te] = s_te
            ho = EM.sample_training_rows(cx, te[train_rows[te]], vis, HELDOUT_SAMPLE_SEED + seed * 100 + fold_i)
            ho_idx = np.searchsorted(te, ho)                               # te is sorted; position of each row in te
            assert np.array_equal(te[ho_idx], ho)
            y_ho = vis[ho].astype(np.int64)
            g_fit = cx.groups[fit]
            in3, in2 = np.isin(g_fit, cells3), np.isin(g_fit, cells2)
            for e in range(EP):
                rec["loss_train_eval"][si, fold_i, e] = bce(s_tr[e], y_fit, pw)
                rec["loss_heldout"][si, fold_i, e] = bce(s_te[e][ho_idx], y_ho, pw)
                rec["auroc_train_min3"][si, fold_i, e] = wt(s_tr[e][in3], y_fit[in3], g_fit[in3], 3)
                rec["auroc_train_min2"][si, fold_i, e] = wt(s_tr[e][in2], y_fit[in2], g_fit[in2], 2)
            rec["loss_optimised"][si, fold_i] = loss_opt
            for k, v in (("pos_weight", pw), ("n_fit", len(fit)), ("n_pos", int(y_fit.sum())),
                         ("n_heldout_rows", len(ho)), ("n_heldout_pos", int(y_ho.sum())), ("seconds", time.time() - t0)):
                meta[k][si, fold_i] = v
            in_te = set(cx.groups[te].tolist())
            held_cells[si, fold_i] = [int(c in in_te) for c in cells3]
            log(name, f"seed={seed} fold={fold_i} n={len(fit)} visible={int(y_fit.sum())} scored={len(te)} "
                      f"heldout_cells={[c.split('|')[0] for c in cells3 if c in in_te]} "
                      f"loss {loss_opt[0]:.4f}->{loss_opt[-1]:.4f} "
                      f"train_auroc {rec['auroc_train_min3'][si, fold_i, -1]:.3f} {time.time() - t0:.1f}s")
        if not np.isfinite(oof[si]).all():
            raise RuntimeError(f"non-finite scores for {name} seed {seed}")
    held = {k: np.full((S, EP), np.nan) for k in ("auroc_heldout_min3", "auroc_heldout_min2", "auroc_heldout_all")}
    cell_auc = np.full((S, EP, len(cells3)), np.nan)
    cell_auc2 = np.full((S, EP, len(cells2)), np.nan)
    everything = np.ones(cx.n, dtype=bool)
    f3, f2, fall = FastWT(cx, masks["min3"], 3), FastWT(cx, masks["min2"], 2), FastWT(cx, everything, 3)
    for si in range(S):
        for e in range(EP):
            s = oof[si, e].astype(np.float64)
            held["auroc_heldout_min3"][si, e], held["auroc_heldout_min2"][si, e], held["auroc_heldout_all"][si, e] = f3(s), f2(s), fall(s)
            per3, per2 = f3.per_cell(s), f2.per_cell(s)
            cell_auc[si, e] = [per3.get(c, np.nan) for c in cells3]
            cell_auc2[si, e] = [per2.get(c, np.nan) for c in cells2]
        s = oof[si, -1].astype(np.float64)              # the fast path must equal the official function
        for key, mask, mp in (("auroc_heldout_min3", masks["min3"], 3), ("auroc_heldout_min2", masks["min2"], 2),
                              ("auroc_heldout_all", everything, 3)):
            assert abs(held[key][si, -1] - EM.score_metric(cx, s, mask, mp)["value"]) < 1e-12, key
    data = {"oof": oof, "cell_auroc_heldout": cell_auc, "cell_auroc_heldout_min2cells": cell_auc2, "heldout_cells": held_cells,
            **rec, **held, **{f"meta_{k}": v for k, v in meta.items()}}
    np.savez_compressed(path, **data)
    log(name, "saved", path.relative_to(ROOT), "held-out AUROC at the last epoch per seed",
        np.round(held["auroc_heldout_min3"][:, -1], 4).tolist())
    return data


def run_final(cx, X, vis, train_rows, masks):
    """Repeat of the exported all-rows EM32 fit (argus_v_em.run, seed 910032) with the same recording."""
    path = OUT / "final_EM32.npz"
    if path.is_file():
        log("final EM32 already recorded, loading")
        return dict(np.load(path, allow_pickle=False))
    rows = EM.sample_training_rows(cx, np.flatnonzero(train_rows), vis, 910032)
    y = vis[rows].astype(np.int64)
    med, scale, state, pw, loss_opt, s_tr, extra = fit_logged(X[rows], y, 32, 910032, {"all": X})
    s_all = extra["all"]
    EP = EM.EPOCHS
    out = {"loss_optimised": loss_opt, "loss_train_eval": np.asarray([bce(s_tr[e], y, pw) for e in range(EP)]),
           "auroc_insample_min3": np.asarray([EM.score_metric(cx, s_all[e].astype(np.float64), masks["min3"], 3)["value"] for e in range(EP)]),
           "auroc_insample_min2": np.asarray([EM.score_metric(cx, s_all[e].astype(np.float64), masks["min2"], 2)["value"] for e in range(EP)]),
           "scores_all_rows_last_epoch": s_all[-1], "fit_rows": rows, "pos_weight": np.asarray(pw),
           "n_fit": np.asarray(len(rows)), "n_pos": np.asarray(int(y.sum()))}
    # the saved checkpoint, scored in chunks with its own scaling parameters
    payload = torch.load(EM.OUT / "argus_v_em_round01.pt", map_location="cpu", weights_only=True)
    saved_model = EM.LearnedEmbedding(int(payload["input_width"]), int(payload["width"]))
    saved_model.load_state_dict(payload["state_dict"])
    saved_model.eval()
    with torch.no_grad():
        saved = saved_model(torch.from_numpy(scaled(X, payload["median"].numpy(), payload["scale"].numpy()))).numpy()
    out["saved_checkpoint_scores"] = saved.astype(np.float32)
    out["max_abs_diff_vs_saved_checkpoint"] = np.asarray(float(np.max(np.abs(saved.astype(np.float64) - s_all[-1].astype(np.float64)))))
    out["max_abs_weight_diff_vs_saved_checkpoint"] = np.asarray(max(
        float((state[k] - payload["state_dict"][k]).abs().max()) for k in state))
    out["auroc_saved_checkpoint_insample_min3"] = np.asarray(EM.score_metric(cx, saved.astype(np.float64), masks["min3"], 3)["value"])
    out["auroc_saved_checkpoint_insample_min2"] = np.asarray(EM.score_metric(cx, saved.astype(np.float64), masks["min2"], 2)["value"])
    np.savez_compressed(path, **out)
    log("final EM32 saved; in-sample AUROC at the last epoch", round(float(out["auroc_insample_min3"][-1]), 4),
        "| largest score difference from the saved checkpoint", float(out["max_abs_diff_vs_saved_checkpoint"]),
        "| largest weight difference", float(out["max_abs_weight_diff_vs_saved_checkpoint"]))
    return out


def r6(a):
    return np.round(np.asarray(a, dtype=np.float64), 6).tolist()


def main(argv):
    if "--approved" not in argv:
        raise SystemExit("This script trains models. Run it only after the user approved the re-run: add --approved.")
    OUT.mkdir(parents=True, exist_ok=True)
    cx = EM.Ctx()
    vis, rule = EM.visible_mask(cx)
    X, train_rows, eval_rows, eligible = EM.prepare(cx, vis)
    cells3 = sorted(k for k, v in eligible.items() if v["min3"])
    cells2 = sorted(k for k, v in eligible.items() if v["min2"])
    masks = {"min3": eval_rows & np.isin(cx.groups, cells3), "min2": eval_rows & np.isin(cx.groups, cells2)}
    log(f"rows={cx.n} target_rows={int(train_rows.sum())} visible={int(vis.sum())} input={X.shape} rule={rule}")
    log("cells with >=3 visible positives:", cells3)
    stored = json.loads((EM.REPORT / "round01_results.json").read_text(encoding="utf-8"))
    stored_lin = json.loads((EM.REPORT / "round01_linear_control.json").read_text(encoding="utf-8"))
    summary = {"name": "Argus-V-em round 01, re-run with per-epoch recording (addendum 2)", "rule": rule,
               "epochs": EM.EPOCHS, "seeds": list(EM.SEEDS), "folds": 5, "cells_min3": cells3, "cells_min2": cells2,
               "heldout_loss_rows": "held-out target rows picked by the training sampling rule; class weight of that fit",
               "array_shapes": {"loss_*, auroc_train_*": "[seed][fold][epoch]", "auroc_heldout_*": "[seed][epoch]",
                                "cell_auroc_heldout": "[seed][epoch][cell in cells_min3]",
                                "heldout_cells": "[seed][fold][cell in cells_min3], 1 = cell is in the held-out fold"},
               "models": {}}
    for name in MODELS:
        d = run_model(name, cx, X, vis, train_rows, masks, cells3, cells2)
        diffs = []
        for si, seed in enumerate(EM.SEEDS):
            saved = np.load(EM.OUT / f"oof_{name}_s{seed}.npy")
            diffs.append(float(np.max(np.abs(saved - d["oof"][si, -1].astype(np.float64)))))
        want = (stored_lin if name == "LINEAR" else stored["architectures"][name])["visible_min3"]["per_seed"]
        got = d["auroc_heldout_min3"][:, -1].tolist()
        log(name, "largest difference from the saved held-out scores per seed", diffs,
            "| last-epoch AUROC", np.round(got, 6).tolist(), "| stored", np.round(want, 6).tolist())
        summary["models"][name] = {
            "width": MODELS[name],
            "max_abs_diff_vs_saved_oof_per_seed": diffs,
            "last_epoch_auroc_min3_per_seed": got, "stored_auroc_min3_per_seed": want,
            "per_epoch": {k: r6(d[k]) for k in
                          ("loss_optimised", "loss_train_eval", "loss_heldout", "auroc_train_min3", "auroc_train_min2",
                           "auroc_heldout_min3", "auroc_heldout_min2", "auroc_heldout_all", "cell_auroc_heldout")},
            "heldout_cells": d["heldout_cells"].tolist(),
            "per_fit": {k[5:]: r6(d[k]) for k in d if k.startswith("meta_")},
        }
    f = run_final(cx, X, vis, train_rows, masks)
    summary["final_EM32"] = {"seed": 910032, "n_fit": int(f["n_fit"]), "n_pos": int(f["n_pos"]),
                             "pos_weight": float(f["pos_weight"]),
                             "max_abs_diff_vs_saved_checkpoint": float(f["max_abs_diff_vs_saved_checkpoint"]),
                             "max_abs_weight_diff_vs_saved_checkpoint": float(f["max_abs_weight_diff_vs_saved_checkpoint"]),
                             "saved_checkpoint_insample_auroc_min3": float(f["auroc_saved_checkpoint_insample_min3"]),
                             "saved_checkpoint_insample_auroc_min2": float(f["auroc_saved_checkpoint_insample_min2"]),
                             "per_epoch": {k: r6(f[k]) for k in
                                           ("loss_optimised", "loss_train_eval", "auroc_insample_min3", "auroc_insample_min2")}}
    summary["evaluation_sha256"] = E.evaluate_sha256()
    summary["created_at"] = time.strftime("%Y-%m-%d %H:%M:%S")
    (EM.REPORT / "epoch_history.json").write_text(json.dumps(E.to_jsonable(summary), ensure_ascii=False), encoding="utf-8")
    log("DONE", json.dumps({n: {"diff": max(m["max_abs_diff_vs_saved_oof_per_seed"]),
                                "auroc": float(np.mean(m["last_epoch_auroc_min3_per_seed"]))}
                            for n, m in summary["models"].items()}),
        "final diff", summary["final_EM32"]["max_abs_diff_vs_saved_checkpoint"])


if __name__ == "__main__":
    main(sys.argv[1:])

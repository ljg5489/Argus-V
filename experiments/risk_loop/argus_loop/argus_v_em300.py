"""Argus-V-em300: Argus-V-em round 01 trained for 300 epochs instead of 60. Nothing else changes.

Plan (fixed before running): reports/risk-loop/argus-v-em300/README.md. User instruction 2026-11-16:
"Argus-V-em300 이라는 이름으로 기존 Argus-V-em이랑 똑같은데 에폭만 300으로", and "에폭을 돌며 성능지표에 필요한 epoch 정보,
다른 보고에 필요한 학습에 대한 데이터도 저장".

Same inputs, target rows, sampling rule and seeds, folds, model seeds, AdamW settings and dropout as argus_v_em.py /
argus_v_em_linear.py / argus_v_em_checks.py. Because nothing but the epoch count differs, the first 60 epochs of every
fit are the Argus-V-em training itself; the run checks this against the saved Argus-V-em scores.

Recorded: per epoch and fit — optimised loss, evaluation-mode loss on training and held-out rows, same-tool AUROC on
training rows, gradient and weight norms; per epoch and split — held-out scores of every row (so any metric can be
computed later) and the same-tool AUROC under each scoring target and per cell; per fit — rows, positives, class
weight, seconds; for the final all-rows model — the checkpoint, snapshots every 10 epochs, per-epoch scores of every
row and the learned embedding of every row.

Training starts only with --approved.
Usage : PYTHONUTF8=1 py -3.11 -u experiments/risk_loop/argus_loop/argus_v_em300.py --approved
Output: artifacts/risk-loop/argus-v-em300/ (ignored): epochs/<model>.npz, epochs/final.npz, oof_<model>_s<seed>.npy,
        argus_v_em300.pt, snapshots/epoch_NNN.pt
        reports/risk-loop/argus-v-em300/: results.json, epoch_history.json, epoch_table.csv, linear_control.json, shuffle.json
"""
from __future__ import annotations

import csv
import hashlib
import json
import os
import platform
import sys
import time
from pathlib import Path

for _name in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):   # as argus_v_em.py, before numpy/torch
    os.environ.setdefault(_name, "2")

import numpy as np  # noqa: E402
import torch  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from experiments.risk_loop.argus_loop import argus_v_em as EM  # noqa: E402
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402

NAME = "Argus-V-em300"
EPOCHS = 300
BASE_OUT, BASE_REPORT, BASE_EPOCHS = EM.OUT, EM.REPORT, EM.EPOCHS        # Argus-V-em (60 epochs): read only
EM.EPOCHS = EPOCHS                                                         # the only change to the training
EM.OUT = ROOT / "artifacts" / "risk-loop" / "argus-v-em300"
EM.REPORT = ROOT / "reports" / "risk-loop" / "argus-v-em300"
from experiments.risk_loop.argus_loop import argus_v_em_epochs as EP  # noqa: E402  (binds EP.OUT to the new folder)

SNAPSHOT_EPOCHS = tuple(sorted(set(range(10, EPOCHS + 1, 10)) | {BASE_EPOCHS}))
SHUFFLE_RUNS = 5
FINAL_SEED = 910032                                                        # as argus_v_em.run
log, r6 = EP.log, EP.r6


def dump(path: Path, obj):
    path.write_text(json.dumps(E.to_jsonable(obj), ensure_ascii=False), encoding="utf-8")


def arch_entry(cx, d, masks, everything, name):
    """Final-epoch held-out scores of one model, in the layout of round01_results.json."""
    last = [d["oof"][si, -1].astype(np.float64) for si in range(len(EM.SEEDS))]
    v3 = [EM.score_metric(cx, s, masks["min3"], 3) for s in last]
    v2 = [EM.score_metric(cx, s, masks["min2"], 2) for s in last]
    a3 = [EM.score_metric(cx, s, everything, 3) for s in last]

    def block(vals, per_cell=True):
        out = {"mean": float(np.mean([v["value"] for v in vals])), "per_seed": [float(v["value"]) for v in vals],
               "cells": vals[0]["n_tools"], "positives": vals[0]["n_positives_included"]}
        if per_cell:
            out["per_cell"] = vals[0]["per_tool"]
        return out

    e60 = BASE_EPOCHS - 1
    return {"width": EP.MODELS[name], "visible_min3": block(v3), "visible_min2": block(v2),
            "all_violations_min3": block(a3, per_cell=False),
            "at_epoch_60": {k: float(d[f"auroc_heldout_{k}"][:, e60].mean()) for k in ("min3", "min2", "all")},
            "best_epoch_min3_for_reference_only": {"epoch": int(d["auroc_heldout_min3"].mean(0).argmax()) + 1,
                                                   "value": float(d["auroc_heldout_min3"].mean(0).max())}}


def history_entry(d, name):
    keys = ("loss_optimised", "loss_train_eval", "loss_heldout", "auroc_train_min3", "auroc_train_min2", "grad_norm",
            "weight_norm", "auroc_heldout_min3", "auroc_heldout_min2", "auroc_heldout_all", "cell_auroc_heldout",
            "cell_auroc_heldout_min2cells")
    return {"width": EP.MODELS[name], "per_epoch": {k: r6(d[k]) for k in keys}, "heldout_cells": d["heldout_cells"].tolist(),
            "per_fit": {k[5:]: r6(d[k]) for k in d if k.startswith("meta_")}}


def final_fit(cx, X, vis, train_rows, masks, everything, selected, width, rule):
    """All-rows fit of the selected width (argus_v_em.run, same seed), recorded, exported with snapshots."""
    path, model_path = EP.OUT / "final.npz", EM.OUT / "argus_v_em300.pt"
    if path.is_file() and model_path.is_file():
        log("final model already recorded, loading")
        return dict(np.load(path, allow_pickle=False))
    rows = EM.sample_training_rows(cx, np.flatnonzero(train_rows), vis, FINAL_SEED)
    y = vis[rows].astype(np.int64)
    st = {}
    med, scale, state, pw, loss_opt, s_tr, extra = EP.fit_logged(X[rows], y, width, FINAL_SEED, {"all": X}, stats=st,
                                                                snapshot_epochs=SNAPSHOT_EPOCHS)
    s_all = extra["all"]                                                   # [epoch][row]

    def payload(sd, epochs):
        return {"state_dict": sd, "width": width, "input_width": X.shape[1], "median": torch.from_numpy(med),
                "scale": torch.from_numpy(scale), "feature_spec": ["L23:max", "L16:pre"], "visible_rule": rule,
                "train_row_count": int(len(rows)), "train_visible_positives": int(y.sum()), "seed": FINAL_SEED,
                "epochs": epochs, "lr": EM.LR, "weight_decay": EM.WEIGHT_DECAY, "dropout": EM.DROPOUT}

    torch.save(payload(state, EPOCHS), model_path)
    snap_dir = EM.OUT / "snapshots"
    snap_dir.mkdir(parents=True, exist_ok=True)
    for ep, sd in st["snapshots"].items():
        torch.save(payload(sd, ep), snap_dir / f"epoch_{ep:03d}.pt")
    # the exported file must give back the recorded scores (scored in chunks)
    back = np.concatenate([EM.score_checkpoint(model_path, X[i:i + 2048]) for i in range(0, cx.n, 2048)])
    export_diff = float(np.max(np.abs(back - s_all[-1].astype(np.float64))))
    out = {"loss_optimised": loss_opt, "loss_train_eval": np.asarray([EP.bce(s_tr[e], y, pw) for e in range(EPOCHS)]),
           "grad_norm": st["grad_norm"], "weight_norm": st["weight_norm"], "scores_all_rows": s_all,
           "saved_checkpoint_scores": s_all[-1], "fit_rows": rows, "pos_weight": np.asarray(pw),
           "n_fit": np.asarray(len(rows)), "n_pos": np.asarray(int(y.sum())), "width": np.asarray(width),
           "export_max_abs_diff": np.asarray(export_diff)}
    for key, mask, mp in (("min3", masks["min3"], 3), ("min2", masks["min2"], 2), ("all", everything, 3)):
        f = EP.FastWT(cx, mask, mp)
        out[f"auroc_insample_{key}"] = np.asarray([f(s_all[e].astype(np.float64)) for e in range(EPOCHS)])
    if width > 0:                                                          # learned embedding of every row
        model = EM.LearnedEmbedding(X.shape[1], width)
        model.load_state_dict(state)
        model.eval()
        with torch.no_grad():
            out["embedding"] = np.concatenate([model.encoder(torch.from_numpy(EM.robust_scale(X[i:i + 2048], med, scale))).numpy()
                                               for i in range(0, cx.n, 2048)]).astype(np.float32)
    base_final = BASE_OUT / "epochs" / "final_EM32.npz"
    if selected == "EM32" and base_final.is_file():                        # epoch 60 of this fit == the Argus-V-em checkpoint
        base_scores = np.load(base_final)["saved_checkpoint_scores"].astype(np.float64)
        out["epoch60_max_abs_diff_vs_argus_v_em_checkpoint"] = np.asarray(
            float(np.max(np.abs(base_scores - s_all[BASE_EPOCHS - 1].astype(np.float64)))))
    np.savez_compressed(path, **out)
    log("final model saved", model_path.relative_to(ROOT), "| training-row AUROC at the last epoch",
        round(float(out["auroc_insample_min3"][-1]), 4), "| exported file vs recorded scores", export_diff,
        "| epoch 60 vs Argus-V-em checkpoint", float(out.get("epoch60_max_abs_diff_vs_argus_v_em_checkpoint", np.nan)))
    return out


def shuffle_check(cx, X, vis, train_rows, masks, selected, width, rule):
    """argus_v_em_checks.run with the selected width and this epoch count: labels shuffled inside each cell."""
    path = EM.REPORT / "shuffle.json"
    if path.is_file():
        return json.loads(path.read_text(encoding="utf-8"))
    res = {"rule": rule, "architecture": selected, "fold_seed": 0, "epochs": EPOCHS, "permutations": []}
    for rep in range(SHUFFLE_RUNS):
        oof = np.full(cx.n, np.nan, dtype=np.float64)
        rng = np.random.default_rng(811000 + rep)
        for fold_i, (tr, te) in enumerate(E.make_folds(cx.rows, 5, 0)):
            fit = EM.sample_training_rows(cx, tr[train_rows[tr]], vis, 811100 + rep * 10 + fold_i)
            y_perm = vis[fit].astype(np.int64)
            g_fit = cx.groups[fit]
            for cell in sorted(set(g_fit.tolist())):
                loc = np.flatnonzero(g_fit == cell)
                y_perm[loc] = rng.permutation(y_perm[loc])
            oof[te] = EM.fit_fold(X[fit], y_perm, X[te], width, 812000 + rep * 10 + fold_i)
        m3 = EM.score_metric(cx, oof, masks["min3"], 3)
        res["permutations"].append({"run": rep, "visible_min3": float(m3["value"]), "cells": int(m3["n_tools"]),
                                    "positives": int(m3["n_positives_included"])})
        log("label shuffle", res["permutations"][-1])
    vals = [p["visible_min3"] for p in res["permutations"]]
    res["mean"], res["range"] = float(np.mean(vals)), [float(min(vals)), float(max(vals))]
    dump(path, res)
    return res


def write_epoch_table(history, final):
    """One row per model and epoch: the numbers most reports need, as a CSV."""
    cols = ["model", "epoch", "loss_optimised", "loss_train_eval", "loss_heldout", "grad_norm", "weight_norm",
            "auroc_train_min3", "auroc_heldout_min3", "auroc_heldout_min3_s0", "auroc_heldout_min3_s1",
            "auroc_heldout_min3_s2", "auroc_heldout_min2", "auroc_heldout_all"]
    with open(EM.REPORT / "epoch_table.csv", "w", newline="", encoding="utf-8") as h:
        w = csv.writer(h)
        w.writerow(cols)
        for name, m in history["models"].items():
            pe = {k: np.asarray(v, dtype=np.float64) for k, v in m["per_epoch"].items()}
            for e in range(history["epochs"]):
                fold = [float(np.nanmean(pe[k][:, :, e])) for k in ("loss_optimised", "loss_train_eval", "loss_heldout",
                                                                    "grad_norm", "weight_norm", "auroc_train_min3")]
                h3 = pe["auroc_heldout_min3"][:, e]
                w.writerow([name, e + 1] + [f"{v:.6f}" for v in fold + [float(h3.mean())] + h3.tolist()
                                            + [float(pe["auroc_heldout_min2"][:, e].mean()), float(pe["auroc_heldout_all"][:, e].mean())]])
        if final is not None:
            for e in range(history["epochs"]):
                w.writerow([f"final_{final['selected']}", e + 1, f"{final['loss_optimised'][e]:.6f}", f"{final['loss_train_eval'][e]:.6f}", "",
                            f"{final['grad_norm'][e]:.6f}", f"{final['weight_norm'][e]:.6f}", f"{final['auroc_insample_min3'][e]:.6f}",
                            "", "", "", "", "", ""])


def main(argv):
    if "--approved" not in argv:
        raise SystemExit("This script trains models. Run it only after the user approved it: add --approved.")
    for p in (EM.OUT, EP.OUT, EM.REPORT):
        p.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    cx = EM.Ctx()
    vis, rule = EM.visible_mask(cx)
    X, train_rows, eval_rows, eligible = EM.prepare(cx, vis)
    cells3 = sorted(k for k, v in eligible.items() if v["min3"])
    cells2 = sorted(k for k, v in eligible.items() if v["min2"])
    masks = {"min3": eval_rows & np.isin(cx.groups, cells3), "min2": eval_rows & np.isin(cx.groups, cells2)}
    everything = np.ones(cx.n, dtype=bool)
    log(f"{NAME}: rows={cx.n} target_rows={int(train_rows.sum())} visible={int(vis.sum())} input={X.shape} epochs={EPOCHS} rule={rule}")
    base = json.loads((BASE_REPORT / "round01_results.json").read_text(encoding="utf-8"))
    run_info = {"started_at": time.strftime("%Y-%m-%d %H:%M:%S"), "python": sys.version.split()[0], "torch": torch.__version__,
                "numpy": np.__version__, "platform": platform.platform(), "processor": platform.processor(),
                "torch_threads": 2, "device": "cpu", "script": "experiments/risk_loop/argus_loop/argus_v_em300.py"}
    results = {"name": NAME, "based_on": "Argus-V-em round 01; only the epoch count differs (60 -> 300)", "rule": rule,
               "input": "L23:max + L16:pre", "input_width": X.shape[1], "train_rows": int(train_rows.sum()),
               "visible_positive_rows": int(vis.sum()),
               "unique_visible_feature_rows": int(len(set(cx.hashes[vis].tolist()))),
               "protocol": dict(base["protocol"], epochs=EPOCHS),
               "structure": {"EM32/EM64/EM128": "robust scaling and clipping -> Linear(5760, width) -> LayerNorm -> GELU -> Dropout(0.15) -> Linear(width, 1)",
                             "LINEAR": "robust scaling and clipping -> Linear(5760, 1)",
                             "parameters": {n: (5760 * w + w + 2 * w + w + 1) if w else 5761 for n, w in EP.MODELS.items()}},
               "eligible_cells": {k: v for k, v in eligible.items() if v["min2"]},
               "cells_with_zero_visible_rows": sum(v["visible_positives"] == 0 for v in eligible.values()),
               "architectures": {}, "comparators": base["comparators"],
               "argus_v_em_60": {"selected": base["selected_on_development_oof"],
                                 "visible_min3": {n: base["architectures"][n]["visible_min3"]["mean"] for n in base["architectures"]}},
               "run": run_info, "partial": True}
    history = {"name": NAME, "rule": rule, "epochs": EPOCHS, "seeds": list(EM.SEEDS), "folds": 5, "cells_min3": cells3,
               "cells_min2": cells2, "snapshot_epochs": list(SNAPSHOT_EPOCHS),
               "heldout_loss_rows": "held-out target rows picked by the training sampling rule; class weight of that fit",
               "array_shapes": {"loss_*, auroc_train_*, grad_norm, weight_norm": "[seed][fold][epoch]", "auroc_heldout_*": "[seed][epoch]",
                                "cell_auroc_heldout": "[seed][epoch][cell in cells_min3]",
                                "cell_auroc_heldout_min2cells": "[seed][epoch][cell in cells_min2]",
                                "heldout_cells": "[seed][fold][cell in cells_min3], 1 = cell is in the held-out fold"},
               "models": {}}
    linear = None
    for name in EP.MODELS:
        d = EP.run_model(name, cx, X, vis, train_rows, masks, cells3, cells2)
        diff60 = []
        for si, seed in enumerate(EM.SEEDS):
            np.save(EM.OUT / f"oof_{name}_s{seed}.npy", d["oof"][si, -1].astype(np.float64))
            diff60.append(float(np.max(np.abs(np.load(BASE_OUT / f"oof_{name}_s{seed}.npy") - d["oof"][si, BASE_EPOCHS - 1].astype(np.float64)))))
        entry = arch_entry(cx, d, masks, everything, name)
        entry["epoch60_max_abs_diff_vs_argus_v_em"] = diff60
        if name == "LINEAR":
            linear = {"rule": rule, "epochs": EPOCHS,
                      "control": "raw hidden vector -> linear score; same target rows, folds, sampling, loss, epochs and optimizer", **entry}
            dump(EM.REPORT / "linear_control.json", linear)
        else:
            results["architectures"][name] = entry
        history["models"][name] = history_entry(d, name)
        dump(EM.REPORT / "results.json", results)
        dump(EM.REPORT / "epoch_history.json", history)
        write_epoch_table(history, None)
        log(name, "held-out AUROC at epoch", EPOCHS, np.round(entry["visible_min3"]["per_seed"], 4).tolist(), "mean",
            round(entry["visible_min3"]["mean"], 4), "| at epoch 60", round(entry["at_epoch_60"]["min3"], 4),
            "| first 60 epochs vs Argus-V-em, largest difference", max(diff60), f"| {time.time() - t0:.0f}s elapsed")
    selected = max(results["architectures"], key=lambda n: results["architectures"][n]["visible_min3"]["mean"])
    width = EP.MODELS[selected]
    f = final_fit(cx, X, vis, train_rows, masks, everything, selected, width, rule)
    model_path = EM.OUT / "argus_v_em300.pt"
    results["selected_on_development_oof"] = selected
    results["export"] = {"path": str(model_path.relative_to(ROOT)).replace("\\", "/"),
                         "sha256": hashlib.sha256(model_path.read_bytes()).hexdigest(), "train_rows": int(f["n_fit"]),
                         "visible_positives": int(f["n_pos"]), "seed": FINAL_SEED, "epochs": EPOCHS,
                         "snapshots": "artifacts/risk-loop/argus-v-em300/snapshots/epoch_NNN.pt for epochs " + ", ".join(map(str, SNAPSHOT_EPOCHS)),
                         "export_max_abs_diff": float(f["export_max_abs_diff"])}
    fin = {"selected": selected, "width": width, "seed": FINAL_SEED, "n_fit": int(f["n_fit"]), "n_pos": int(f["n_pos"]),
           "pos_weight": float(f["pos_weight"]),
           "epoch60_max_abs_diff_vs_argus_v_em_checkpoint": (float(f["epoch60_max_abs_diff_vs_argus_v_em_checkpoint"])
                                                            if "epoch60_max_abs_diff_vs_argus_v_em_checkpoint" in f else None),
           "per_epoch": {k: r6(f[k]) for k in ("loss_optimised", "loss_train_eval", "grad_norm", "weight_norm",
                                               "auroc_insample_min3", "auroc_insample_min2", "auroc_insample_all")}}
    history["final"] = fin
    shuffle = shuffle_check(cx, X, vis, train_rows, masks, selected, width, rule)
    results["label_shuffle"] = {"mean": shuffle["mean"], "range": shuffle["range"], "runs": len(shuffle["permutations"])}
    results["linear_control"] = {"visible_min3": linear["visible_min3"]["mean"], "visible_min2": linear["visible_min2"]["mean"]}
    results["evaluation_sha256"] = E.evaluate_sha256()
    results["created_at"] = time.strftime("%Y-%m-%d %H:%M:%S")
    results["run"]["finished_at"] = results["created_at"]
    results["run"]["seconds"] = round(time.time() - t0, 1)
    results["partial"] = False
    dump(EM.REPORT / "results.json", results)
    dump(EM.REPORT / "epoch_history.json", history)
    write_epoch_table(history, dict(selected=selected, **{k: np.asarray(v) for k, v in fin["per_epoch"].items()}))
    log("DONE", json.dumps({"scores_at_300": {k: round(v["visible_min3"]["mean"], 4) for k, v in results["architectures"].items()},
                            "scores_at_60": {k: round(v["at_epoch_60"]["min3"], 4) for k, v in results["architectures"].items()},
                            "linear": round(linear["visible_min3"]["mean"], 4), "selected": selected,
                            "label_shuffle": round(shuffle["mean"], 4), "export": results["export"]["sha256"][:16],
                            "seconds": results["run"]["seconds"]}))


if __name__ == "__main__":
    main(sys.argv[1:])

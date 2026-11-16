"""Argus-V-em300, best epoch: pick the (width, epoch) with the highest TRAIN cross-validation score and export the
all-rows model stopped at that epoch.

User instruction 2026-11-16 (before any test score existed): "test를 이용한 성능평가뽑는 채점은 제일 성능이 좋았던
epoch을 이용해". Rule (reports/risk-loop/argus-v-em300/test-eval-prereg-addendum-1.md):
  - candidates: the three embedding widths (32, 64, 128), every epoch 1..300 of the Argus-V-em300 run
  - score: mean over the three splits of the same-tool AUROC on visible violations, at least 3 per cell, on the
    held-out folds inside the TRAIN split (epoch_history.json). Test data is not used.
  - ties: earlier epoch, then the smaller width
The exported model is the all-rows fit of that width (argus_v_em.run: same rows, same seed 910032) stopped after that
many epochs. Full-batch training with a fixed learning rate has no schedule, so this is the state the 300-epoch fit of
that width passes through at that epoch; when that fit exists (same width as the 300-epoch final model) the two are
compared row by row.

Training (one all-rows fit) starts only with --approved.
Usage : PYTHONUTF8=1 py -3.11 -u experiments/risk_loop/argus_loop/argus_v_em300_best.py --approved
Output: artifacts/risk-loop/argus-v-em300/argus_v_em300_best.pt, epochs/best.npz; reports/.../best_epoch.json
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
import time
from pathlib import Path

for _name in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ.setdefault(_name, "2")

import numpy as np  # noqa: E402
import torch  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from experiments.risk_loop.argus_loop import argus_v_em as EM  # noqa: E402

BASE_OUT, BASE_EPOCHS = EM.OUT, EM.EPOCHS
EM.OUT = ROOT / "artifacts" / "risk-loop" / "argus-v-em300"
EM.REPORT = ROOT / "reports" / "risk-loop" / "argus-v-em300"
from experiments.risk_loop.argus_loop import argus_v_em_epochs as EP  # noqa: E402

CANDIDATES = ("EM32", "EM64", "EM128")
FINAL_SEED = 910032


def pick(history: dict) -> dict:
    curves = {n: np.asarray(history["models"][n]["per_epoch"]["auroc_heldout_min3"], dtype=np.float64) for n in CANDIDATES}
    cand = []
    for n in CANDIDATES:
        m = curves[n].mean(0)
        for e in range(len(m)):
            cand.append((-float(m[e]), e + 1, EP.MODELS[n], n))
    cand.sort()
    neg, epoch, width, name = cand[0]
    per_width = {}
    for n in CANDIDATES:
        m = curves[n].mean(0)
        per_width[n] = {"best_epoch": int(m.argmax()) + 1, "best_value": float(m.max()), "at_epoch_60": float(m[59]),
                        "at_last_epoch": float(m[-1])}
    pe = history["models"][name]["per_epoch"]
    at = {k: np.asarray(pe[k], dtype=np.float64)[:, epoch - 1].tolist() for k in ("auroc_heldout_min3", "auroc_heldout_min2", "auroc_heldout_all")}
    return {"model": name, "width": width, "epoch": epoch, "cv_value": -neg, "cv_per_seed": at["auroc_heldout_min3"],
            "cv_min2_per_seed": at["auroc_heldout_min2"], "cv_all_violations_per_seed": at["auroc_heldout_all"],
            "per_width": per_width,
            "top5": [{"model": c[3], "epoch": c[1], "cv_value": -c[0]} for c in cand[:5]]}


def main(argv):
    history = json.loads((EM.REPORT / "epoch_history.json").read_text(encoding="utf-8"))
    missing = [n for n in CANDIDATES if n not in history["models"]]
    if missing:
        raise SystemExit(f"cross-validation curves not finished yet: {missing}")
    choice = pick(history)
    print(time.strftime("%H:%M:%S"), "picked by train cross-validation:", json.dumps({k: choice[k] for k in ("model", "epoch", "cv_value", "cv_per_seed")}), flush=True)
    print("per width:", json.dumps(choice["per_width"]), flush=True)
    if "--pick-only" in argv:
        return
    if "--approved" not in argv:
        raise SystemExit("Exporting the model needs one all-rows fit (training): add --approved.")
    model_path = EM.OUT / "argus_v_em300_best.pt"
    out_path = EM.REPORT / "best_epoch.json"
    if model_path.is_file() and out_path.is_file():
        print("already exported:", out_path)
        return
    EM.EPOCHS = choice["epoch"]                                   # stop the same fit at the picked epoch
    cx = EM.Ctx()
    vis, rule = EM.visible_mask(cx)
    X, train_rows, eval_rows, eligible = EM.prepare(cx, vis)
    cells3 = sorted(k for k, v in eligible.items() if v["min3"])
    cells2 = sorted(k for k, v in eligible.items() if v["min2"])
    masks = {"min3": eval_rows & np.isin(cx.groups, cells3), "min2": eval_rows & np.isin(cx.groups, cells2)}
    rows = EM.sample_training_rows(cx, np.flatnonzero(train_rows), vis, FINAL_SEED)
    y = vis[rows].astype(np.int64)
    width = choice["width"]
    med, scale, state, pw, loss_opt, s_tr, extra = EP.fit_logged(X[rows], y, width, FINAL_SEED, {"all": X})
    s_all = extra["all"][-1].astype(np.float64)
    torch.save({"state_dict": state, "width": width, "input_width": X.shape[1], "median": torch.from_numpy(med),
                "scale": torch.from_numpy(scale), "feature_spec": ["L23:max", "L16:pre"], "visible_rule": rule,
                "train_row_count": int(len(rows)), "train_visible_positives": int(y.sum()), "seed": FINAL_SEED,
                "epochs": choice["epoch"], "lr": EM.LR, "weight_decay": EM.WEIGHT_DECAY, "dropout": EM.DROPOUT}, model_path)
    back = np.concatenate([EM.score_checkpoint(model_path, X[i:i + 2048]) for i in range(0, cx.n, 2048)])
    checks = {"exported_file_vs_fit": float(np.max(np.abs(back - s_all)))}
    final = EP.OUT / "final.npz"
    if final.is_file():                                           # the 300-epoch fit of the same width passes through this state
        f = np.load(final)
        if int(f["width"]) == width:
            checks["vs_300_epoch_fit_at_that_epoch"] = float(np.max(np.abs(f["scores_all_rows"][choice["epoch"] - 1].astype(np.float64) - s_all.astype(np.float32).astype(np.float64))))
    base_final = BASE_OUT / "epochs" / "final_EM32.npz"
    if width == 32 and choice["epoch"] == BASE_EPOCHS and base_final.is_file():
        checks["vs_argus_v_em_checkpoint"] = float(np.max(np.abs(np.load(base_final)["saved_checkpoint_scores"].astype(np.float64) - s_all.astype(np.float32).astype(np.float64))))
    emb = None
    model = EM.LearnedEmbedding(X.shape[1], width)
    model.load_state_dict(state)
    model.eval()
    with torch.no_grad():
        emb = np.concatenate([model.encoder(torch.from_numpy(EM.robust_scale(X[i:i + 2048], med, scale))).numpy()
                              for i in range(0, cx.n, 2048)]).astype(np.float32)
    insample = {k: float(EP.FastWT(cx, m, mp)(s_all)) for k, m, mp in (("min3", masks["min3"], 3), ("min2", masks["min2"], 2),
                                                                        ("all", np.ones(cx.n, bool), 3))}
    np.savez_compressed(EP.OUT / "best.npz", saved_checkpoint_scores=s_all.astype(np.float32), loss_optimised=loss_opt,
                        embedding=emb, fit_rows=rows, width=np.asarray(width), epoch=np.asarray(choice["epoch"]))
    doc = {"instruction": "test를 이용한 성능평가뽑는 채점은 제일 성능이 좋았던 epoch을 이용해 (user, 2026-11-16, before any test score)",
           "rule": "highest mean train cross-validation same-tool AUROC on visible violations (>= 3 per cell) over widths 32/64/128 and "
                   "epochs 1..300; ties: earlier epoch, then smaller width. Test data is not used.",
           "choice": choice, "export": {"path": str(model_path.relative_to(ROOT)).replace("\\", "/"),
                                        "sha256": hashlib.sha256(model_path.read_bytes()).hexdigest(), "seed": FINAL_SEED,
                                        "train_rows": int(len(rows)), "visible_positives": int(y.sum())},
           "checks_max_abs_diff": checks, "training_rows_rescored": insample, "loss_at_stop": float(loss_opt[-1]),
           "note": "The cross-validation value at the picked epoch is the maximum of 900 noisy candidates on development rows, "
                   "so it overstates what to expect; the test evaluation is the check.",
           "created_at": time.strftime("%Y-%m-%d %H:%M:%S")}
    out_path.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    print(time.strftime("%H:%M:%S"), "exported", doc["export"], "| checks", checks, "| training rows rescored", insample, flush=True)


if __name__ == "__main__":
    main(sys.argv[1:])

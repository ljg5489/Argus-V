"""First training run on the new split (resplit-1117): every Argus-V-p setting, and every Argus-V-em model with
three violation weights, 100 epochs each. Plan (fixed before training): reports/risk-loop/resplit-1117/run01/README.md.

User, 2026-11-17: "Argus-V-p 에 모든 모델도 함께 학습을 하고 Argus-V-em 에 모든 모델 그리고 Argus-V-em 의 모든 모델은 각각
15배, 60배, 300배 위험 가중치에 대한 것도 추가해서 각각 모든 모델에 대해 100epoch씩 학습을 진행 해 그리고 성능평가에 필요한
모든 정보를 저장하고 루프 시작".

Every model is fitted on the new train split only; the new validation and test rows are scored, never fitted.
The old split, the old models and the old results are not touched: this script reads
artifacts/risk-loop/resplit-1117/features and writes under artifacts/risk-loop/resplit-1117/run01 and
reports/risk-loop/resplit-1117/run01.

Stages:
  em       Argus-V-em: EM32 / EM64 / EM128 / LINEAR x weights (about 15x, about 60x, 300x) x 3 repeats, 100 epochs,
           validation and test scores of every row recorded after every epoch          (training: --approved)
  p        Argus-V-p: settings P1..P6 fitted on the train rows, all rows scored            (training: --approved)
  metrics  every metric per model / weight / repeat / epoch / split, the picks by the fixed rule   (no training)
  figures  figures from the saved metrics                                                 (no training)

Usage: PYTHONUTF8=1 py -3.11 -u experiments/risk_loop/argus_loop/resplit_run01.py em p --approved
       PYTHONUTF8=1 py -3.11 experiments/risk_loop/argus_loop/resplit_run01.py metrics figures
"""
from __future__ import annotations

import csv
import json
import os
import platform
import sys
import time
from pathlib import Path
from types import SimpleNamespace

for _name in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):   # as argus_v_em.py, before numpy/torch
    os.environ.setdefault(_name, "2")

import numpy as np  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

NAME = "resplit-1117"
FEAT = ROOT / "artifacts" / "risk-loop" / NAME / "features"
OUT = ROOT / "artifacts" / "risk-loop" / NAME / "run01"
REPORT = ROOT / "reports" / "risk-loop" / NAME / "run01"
SPLITS = ("train", "validation", "test")
EPOCHS = 100
FIXED_EPOCH = 67                              # the epoch of the recipe fixed before this run (64-dim, about 15x)
ARCHS = {"EM32": 32, "EM64": 64, "EM128": 128, "LINEAR": 0}
WEIGHT_RULES = {"w15": "min(20, sqrt(neg / pos))", "w60": "(neg / pos) ** 0.75", "w300": "300 (fixed)"}
WEIGHT_KO = {"w15": "약 15배 (지금 방식)", "w60": "약 60배", "w300": "300배"}
REPEATS = (0, 1, 2)
BASE_SEED = 910032                            # the all-rows fit seed of argus_v_em.run; repeat k uses BASE_SEED + k
SNAPSHOTS = tuple(range(10, EPOCHS + 1, 10))  # model files of repeat 0; every repeat also keeps FIXED_EPOCH and EPOCHS


def log(*a):
    print(time.strftime("%H:%M:%S"), *a, flush=True)


def need_approval(argv):
    if "--approved" not in argv:
        raise SystemExit("This stage trains models. Run it only after the user approved it: add --approved.")


def load():
    """Row table of the new split (all 16,090 judged rows) as arrays."""
    with open(FEAT / "steps.csv", encoding="utf-8", newline="") as h:
        rows = list(csv.DictReader(h))
    D = {"n": len(rows), "y": np.asarray([int(r["label"]) for r in rows], dtype=np.int64),
         "vis": np.asarray([int(r["visible"]) for r in rows], dtype=bool)}
    for k in ("split", "source", "cell", "family", "scenario_id", "unit_id", "tool", "trajectory_id", "old_split"):
        D[k] = np.asarray([r[k] for r in rows], dtype=object)
    D["step_index"] = np.asarray([int(r["step_index"]) for r in rows], dtype=np.int64)
    D["idx"] = {s: np.flatnonzero(D["split"] == s) for s in SPLITS}
    assert [int(r["row"]) for r in rows] == list(range(len(rows)))
    assert not (D["vis"] & (D["y"] == 0)).any()
    return D


# Each rule is written out here. (The first version returned the *current* argus_v_em_epochs.class_weight for "w15", which
# after the first repeat was still the 300x rule of the previous setting: repeats 1 and 2 of "w15" were fitted with 300.
# Found on 2026-11-17 from the loss figure; those eight runs were removed and fitted again with the rule below.)
WEIGHT_FUNCS = {"w15": lambda neg, pos: min(20.0, float(np.sqrt(neg / pos))),      # argus_v_em.fit_model's rule
                "w60": lambda neg, pos: float((neg / pos) ** 0.75),
                "w300": lambda neg, pos: 300.0}


def weight_fn(tag):
    return WEIGHT_FUNCS[tag]


# ---------------------------------------------------------------------- Argus-V-em
def stage_em(argv):
    need_approval(argv)
    import torch
    from experiments.risk_loop.argus_loop import argus_v_em as EM
    EM.EPOCHS = EPOCHS                        # recording length; nothing else about a fit depends on it
    from experiments.risk_loop.argus_loop import argus_v_em_epochs as EP
    from experiments.risk_loop.argus_loop import evaluate as E

    (OUT / "em" / "checkpoints").mkdir(parents=True, exist_ok=True)
    D = load()
    f23 = np.load(FEAT / "L23_max.npy", mmap_mode="r")
    f16 = np.load(FEAT / "L16_pre.npy", mmap_mode="r")
    w23 = f23.shape[1]

    def X(idx):                               # float32, L23:max then L16:pre (the Argus-V-em input)
        idx = np.asarray(idx, dtype=np.int64)
        out = np.empty((len(idx), w23 + f16.shape[1]), dtype=np.float32)
        for k in range(0, len(idx), 2048):
            out[k:k + 2048, :w23] = f23[idx[k:k + 2048]]
            out[k:k + 2048, w23:] = f16[idx[k:k + 2048]]
        return out

    tr, va, te = (D["idx"][s] for s in SPLITS)
    ns = SimpleNamespace(y=D["y"], groups=D["cell"], n=D["n"])       # what EM.sample_training_rows reads
    target = (D["y"] == 0) | D["vis"]                               # normal calls + visible violations
    Xva, Xte = X(va), X(te)
    default_rule = EP.class_weight
    log(f"Argus-V-em on the new split: train rows {len(tr)} (target rows {int(target[tr].sum())}, visible {int(D['vis'][tr].sum())}) "
        f"validation {len(va)} test {len(te)} | epochs {EPOCHS} | torch {torch.__version__}")
    t_all = time.time()
    for k in REPEATS:
        seed = BASE_SEED + k
        fit = EM.sample_training_rows(ns, tr[target[tr]], D["vis"], seed)
        y_fit = D["vis"][fit].astype(np.int64)
        Xfit = None
        for wtag in WEIGHT_RULES:
            for arch, width in ARCHS.items():
                path = OUT / "em" / f"{arch}_{wtag}_r{k}.npz"
                if path.is_file():
                    continue
                if Xfit is None:
                    Xfit = X(fit)
                EP.class_weight = weight_fn(wtag)
                keep = tuple(sorted(set((SNAPSHOTS if k == 0 else ()) + (FIXED_EPOCH, EPOCHS))))
                st, t0 = {}, time.time()
                med, scale, state, pw, loss_opt, s_fit, extra = EP.fit_logged(Xfit, y_fit, width, seed, {"validation": Xva, "test": Xte},
                                                                             stats=st, snapshot_epochs=keep)
                for name in ("validation", "test"):
                    assert np.isfinite(extra[name]).all()
                want = weight_fn(wtag)(float(len(y_fit) - y_fit.sum()), float(y_fit.sum()))
                assert abs(pw - want) < 1e-3, f"{arch} {wtag} repeat {k}: weight {pw} used, {want} intended"
                np.savez_compressed(path, scores_validation=extra["validation"], scores_test=extra["test"], scores_fit=s_fit,
                                    fit_rows=fit, y_fit=y_fit, loss_optimised=loss_opt,
                                    loss_train_eval=np.asarray([EP.bce(s_fit[e], y_fit, pw) for e in range(EPOCHS)]),
                                    grad_norm=st["grad_norm"], weight_norm=st["weight_norm"], pos_weight=np.asarray(pw),
                                    seed=np.asarray(seed), seconds=np.asarray(time.time() - t0))
                for ep, sd in st["snapshots"].items():
                    torch.save({"state_dict": sd, "width": width, "input_width": Xfit.shape[1], "median": torch.from_numpy(med),
                                "scale": torch.from_numpy(scale), "feature_spec": ["L23:max", "L16:pre"],
                                "split": NAME, "arch": arch, "weight": wtag, "weight_rule": WEIGHT_RULES[wtag], "pos_weight": float(pw),
                                "train_row_count": int(len(fit)), "train_visible_positives": int(y_fit.sum()), "seed": seed,
                                "epochs": int(ep), "lr": EM.LR, "weight_decay": EM.WEIGHT_DECAY, "dropout": EM.DROPOUT},
                               OUT / "em" / "checkpoints" / f"{arch}_{wtag}_r{k}_e{ep:03d}.pt")
                log(f"{arch:6s} {wtag:4s} repeat {k}: rows {len(fit)} visible {int(y_fit.sum())} weight {pw:7.2f} | loss {loss_opt[0]:.4f} -> "
                    f"{loss_opt[-1]:.5f} | {time.time() - t0:.1f}s")
    EP.class_weight = default_rule
    (OUT / "em" / "run.json").write_text(json.dumps(
        {"finished_at": time.strftime("%Y-%m-%d %H:%M:%S"), "seconds": round(time.time() - t_all, 1), "epochs": EPOCHS,
         "archs": ARCHS, "weights": WEIGHT_RULES, "repeats": list(REPEATS), "base_seed": BASE_SEED,
         "python": sys.version.split()[0], "torch": torch.__version__, "numpy": np.__version__, "platform": platform.platform(),
         "evaluation_sha256": E.evaluate_sha256()}, indent=1), encoding="utf-8")
    log("EM DONE", f"{time.time() - t_all:.0f}s")


# ---------------------------------------------------------------------- Argus-V-p
def stage_p(argv):
    need_approval(argv)
    from experiments.risk_loop.argus_loop import argus_v_p as AP
    from experiments.risk_loop.argus_loop import evaluate as E

    (OUT / "p").mkdir(parents=True, exist_ok=True)
    D = load()

    class SplitCtx(AP.Ctx):
        """argus_v_p.Ctx fed with the rows of the new split (same fit code, same settings)."""

        def __init__(self):
            assert E.evaluate_sha256() == AP.SHA
            self.reps = ["L16:pre", "L23:max"]
            self.feats = {"L16:pre": np.asarray(np.load(FEAT / "L16_pre.npy", mmap_mode="r"), dtype=np.float32),
                          "L23:max": np.asarray(np.load(FEAT / "L23_max.npy", mmap_mode="r"), dtype=np.float32)}
            self.y, self.n = D["y"], D["n"]
            self.src = D["source"].astype(str)
            self.cells = D["cell"].astype(str)
            self.traj = D["trajectory_id"].astype(str)
            self.groups = D["cell"]
            self.stores = {}

    cx = SplitCtx()
    tr, va, te = (D["idx"][s] for s in SPLITS)
    other = np.concatenate([va, te])
    log(f"Argus-V-p on the new split: train rows {len(tr)} violations {int(D['y'][tr].sum())} | scored validation {len(va)} test {len(te)}")
    t_all = time.time()
    for sid, s in AP.SETTINGS.items():
        path = OUT / "p" / f"{sid}.npz"
        if path.is_file():
            continue
        t0 = time.time()
        s_tr, s_ot = cx.fit(sid, tr, D["y"][tr], other)
        assert np.isfinite(s_tr).all() and np.isfinite(s_ot).all()
        np.savez_compressed(path, scores_train=s_tr, scores_validation=s_ot[:len(va)], scores_test=s_ot[len(va):],
                            seconds=np.asarray(time.time() - t0))
        log(f"{sid} {s['ko']}: {time.time() - t0:.0f}s")
    (OUT / "p" / "run.json").write_text(json.dumps(
        {"finished_at": time.strftime("%Y-%m-%d %H:%M:%S"), "seconds": round(time.time() - t_all, 1),
         "settings": AP.SETTINGS, "evaluation_sha256": E.evaluate_sha256()}, indent=1, ensure_ascii=False), encoding="utf-8")
    log("P DONE", f"{time.time() - t_all:.0f}s")


STAGES = {"em": stage_em, "p": stage_p}

if __name__ == "__main__":
    args = sys.argv[1:]
    todo = [a for a in args if a in STAGES]
    if not todo:
        raise SystemExit(__doc__)
    for a in todo:
        STAGES[a](args)

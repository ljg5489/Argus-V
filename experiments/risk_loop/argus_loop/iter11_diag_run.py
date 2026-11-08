"""Iteration 11 diagnosis runs D1(b,c), D2 (trajectory-grouped CV), D3 (learning curve). Train only.

Usage: py -3.11 experiments/risk_loop/argus_loop/iter11_diag_run.py [d1b d1c d2 d3]
Outputs (small): artifacts/risk-loop/argus-v1-loop/diag11/*.npy, *.json
"""
from __future__ import annotations

import json
import sys
import time
import warnings
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402
from experiments.risk_loop.argus_loop import iter11_diag_common as D  # noqa: E402
from experiments.risk_loop.argus_loop import iter11_diag_models as DM  # noqa: E402

SEEDS10 = list(range(10))


def log(*a):
    print(time.strftime("%H:%M:%S"), *a, flush=True)


def traj_folds(rows, seed, n_splits=5):
    """DIAGNOSTIC grouping: trajectory only (a cell's scenario/family can be in training)."""
    from sklearn.model_selection import StratifiedGroupKFold
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        sp = StratifiedGroupKFold(n_splits=n_splits, shuffle=True, random_state=int(seed))
        return [(np.sort(a), np.sort(b)) for a, b in sp.split(np.zeros(len(rows)), rows.y, rows.trajectory_id.astype(str))]


def summ(O, rows):
    cl = D.cells(rows)
    per_seed = [D.headline_value(o, rows) for o in O]
    bs = [D.by_source(o, rows) for o in O]
    pc = [D.per_cell_auroc(o, rows, cl) for o in O]
    return {"headline_mean": float(np.mean(per_seed)), "headline_sd": float(np.std(per_seed, ddof=1)) if len(O) > 1 else None,
            "per_seed": per_seed,
            "oct_mean": float(np.mean([b["oct"] for b in bs])), "nov_mean": float(np.mean([b["nov"] for b in bs])),
            "per_cell_mean": {c: float(np.mean([p[c] for p in pc])) for c, _ in cl},
            "per_cell_seed0": pc[0]}


def main(modes):
    data, rows, info = D.headline()
    log("rows", len(rows), "pos", int(rows.y.sum()), "sha ok")
    feats = DM.load_feats(data, rows, ["L23:max", "L16:pre"])
    X16 = np.asarray(D.C1.features(data, rows, 16, "max"), dtype=np.float32)
    del data
    res_path = D.OUT / "run.json"
    res = json.loads(res_path.read_text(encoding="utf-8")) if res_path.is_file() else {}

    def save():
        res["fit_count"] = {"configs": sorted(DM.FIT_COUNT["configs"] | set(res.get("fit_count", {}).get("configs", []))),
                            "fold_fits_this_run": DM.FIT_COUNT["fold_fits"]}
        res_path.write_text(json.dumps(E.to_jsonable(res), indent=1, ensure_ascii=False), encoding="utf-8")

    def h10a():
        return DM.make_h10a(X16, rows)

    def t7a():
        return DM.make_t7a(feats, rows)[0]

    if "d1b" in modes:
        O = DM.cv_oof(h10a(), rows, SEEDS10, tag="refit:H1-0a-10seed", log=log)
        np.save(D.OUT / "oof_H1-0a_10seed.npy", O)
        T7 = np.load(D.ART / "iter08" / "B_oof_T7a_seed0-9.npy")
        T10 = np.load(D.ART / "iter10" / "oof10_T10-1.npy")
        res["d1b"] = {"H1-0a": summ(O, rows), "T7-a": summ(T7, rows), "T10-1": summ(T10, rows),
                      "note": "T7-a / T10-1 = saved 10-seed OOF (seed-0 recompute of T7-a matched within 1.3e-4)"}
        save()
        log("d1b", {k: round(v["headline_mean"], 4) for k, v in res["d1b"].items() if isinstance(v, dict)})

    if "d1c" in modes:
        y, st = rows.y, rows.label_status.astype(str)
        masks = {"drop_nov_draft_pos": ~((st == "nov_draft_rule") & (y == 1)),
                 "drop_nov_draft_all": st != "nov_draft_rule",
                 "drop_nov_all": rows.source != "nov"}
        out = {}
        for name, keep in masks.items():
            for mname, mk in (("H1-0a", h10a), ("T7-a", t7a)):
                O = DM.cv_oof(mk(), rows, SEEDS10, keep_train=keep, tag=f"d1c:{mname}:{name}", log=log)
                np.save(D.OUT / f"oof_d1c_{mname}_{name}.npy", O)
                out[f"{mname}|{name}"] = summ(O, rows)
                out[f"{mname}|{name}"]["train_rows_dropped"] = int((~keep).sum())
                log("d1c", mname, name, round(out[f"{mname}|{name}"]["oct_mean"], 4))
                res["d1c"] = out
                save()

    if "d2" in modes:
        out = {}
        for mname, mk in (("H1-0a", h10a), ("T7-a", t7a)):
            O = DM.cv_oof(mk(), rows, SEEDS10, folds_fn=traj_folds, tag=f"d2:trajCV:{mname}", log=log)
            np.save(D.OUT / f"oof_d2_trajcv_{mname}.npy", O)
            out[mname] = summ(O, rows)
            log("d2", mname, round(out[mname]["headline_mean"], 4))
            res["d2_trajcv"] = out
            save()

    if "d3" in modes:
        out = {}
        for mname, mk in (("H1-0a", h10a), ("T7-a", t7a)):
            for frac in (0.25, 0.5, 0.75):
                vals = []
                for r in range(3):
                    O = DM.cv_oof(mk(), rows, [r], frac=frac, rep=r, tag=f"d3:{mname}:{frac}#{r}", log=log)
                    vals.append(summ(O, rows))
                out[f"{mname}|{frac}"] = {"headline": [v["headline_mean"] for v in vals],
                                          "oct": [v["oct_mean"] for v in vals], "nov": [v["nov_mean"] for v in vals]}
                log("d3", mname, frac, [round(v, 3) for v in out[f"{mname}|{frac}"]["headline"]])
                res["d3"] = out
                save()
    log("DONE")


if __name__ == "__main__":
    main(sys.argv[1:] or ["d1b", "d1c", "d2", "d3"])

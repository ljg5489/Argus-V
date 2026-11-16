"""Metrics of the first training run on the new split (resplit-1117 / run01). Reads the saved scores; trains nothing.

Plan and reading rule (fixed before training): reports/risk-loop/resplit-1117/run01/README.md.

For every Argus-V-em model x weight x repeat x epoch and every Argus-V-p setting, on the validation and test splits:
  st_vis3   same-tool AUROC, visible violations, tools with >= 3 of them (main metric)
  st_vis2   same, tools with >= 2 (the metric used for picking, on validation)
  st_all3   same-tool AUROC, all violations, tools with >= 3
  in_period_all / in_period_vis   all calls of one collection period, normal vs violation, the two periods averaged
                                  by their number of violations (all violations / visible ones)
  pooled_all / pooled_vis         all calls, periods mixed (shown next to the score of the period alone)
  caught5_*                       violations above the threshold at which 5% of the normal calls alarm

Usage: PYTHONUTF8=1 py -3.11 experiments/risk_loop/argus_loop/resplit_run01_metrics.py [--quick]
       (--quick skips the re-scoring of all train rows from the model files)
Output: reports/risk-loop/resplit-1117/run01/results.json, epoch_table.csv, tables.md
"""
from __future__ import annotations

import csv
import json
import os
import sys
import time
from pathlib import Path

for _name in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ.setdefault(_name, "2")

import numpy as np  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from experiments.risk_loop import harness as H  # noqa: E402
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402
from experiments.risk_loop.argus_loop import resplit_run01 as R  # noqa: E402

MIN_NEG = E.MIN_NEG
PICK_KEY, PICK_TIE = "st_vis2", "in_oct_vis"          # the picking rule of the plan (validation only)
CURVE_KEYS = ("st_vis3", "st_vis2", "st_all3", "in_period_all", "in_period_vis", "in_oct_all", "in_oct_vis", "in_nov_all",
              "in_nov_vis", "pooled_all", "pooled_vis", "caught5_all", "caught5_vis", "caught5_oct", "caught5_nov",
              "false_alarms5_oct_share", "logloss")
CI_KEYS = ("st_vis3", "st_vis2", "st_all3", "in_period_all", "in_period_vis")
P_KO = {"P1": "최고 모델 그대로", "P2": "같은 도구 안 학습", "P3": "규제 완화", "P4": "같은 도구 안 학습 + 규제 완화",
        "P5": "최고 모델 + 랜덤 포레스트", "P6": "같은 도구 안 학습 + 규제 완화 + 랜덤 포레스트"}
ARCH_KO = {"EM32": "32차원", "EM64": "64차원", "EM128": "128차원", "LINEAR": "선형 대조"}
log = R.log


def auc(s, y):
    y = np.asarray(y)
    return float(H.auroc(s, y)) if 0 < int(y.sum()) < len(y) else float("nan")


def logloss(s, y):
    """Binary cross entropy without class weight (comparable across weights), numerically stable."""
    s, y = np.asarray(s, dtype=np.float64), np.asarray(y, dtype=np.float64)
    return float(np.mean(np.maximum(s, 0) - s * y + np.log1p(np.exp(-np.abs(s)))))


class SplitEval:
    """One split (or any set of rows): its labels and the tool cells of each same-tool metric, built once."""

    def __init__(self, D, rows, target_only=False):
        self.rows = np.asarray(rows)
        self.y, self.vis = D["y"][rows], D["vis"][rows]
        self.cell, self.src, self.fam = D["cell"][rows].astype(str), D["source"][rows].astype(str), D["family"][rows].astype(str)
        self.norm = self.y == 0
        self.target = self.norm | self.vis                      # normal calls + visible violations
        every = np.ones(len(self.rows), dtype=bool)
        self.spec = {"st_vis3": (self.vis, self.target, 3), "st_vis2": (self.vis, self.target, 2), "st_all3": (self.y == 1, every, 3)}
        self.cells = {k: self._cells(*v) for k, v in self.spec.items()}
        self.per = {p: self.src == p for p in ("oct", "nov")}
        self.yv = self.vis.astype(np.int64)

    def _cells(self, pos, mask, min_pos):
        out = []
        for c in sorted(set(self.cell[mask].tolist())):
            m = np.flatnonzero(mask & (self.cell == c))
            p = int(pos[m].sum())
            if p >= min_pos and len(m) - p >= MIN_NEG:
                out.append((c, m, pos[m].astype(np.int64), p, len(m) - p))
        return out

    def describe(self):
        d = {"calls": int(len(self.rows)), "violations": int(self.y.sum()), "visible_violations": int(self.vis.sum()),
             "families": len(set(self.fam.tolist())),
             "period_only_score_all_calls": auc((self.src == "oct").astype(np.float64), self.y),
             "by_period": {p: {"calls": int(m.sum()), "violations": int(self.y[m].sum()), "visible_violations": int(self.vis[m].sum())}
                           for p, m in self.per.items()}}
        for k, cells in self.cells.items():
            d[k] = {"cells": [{"cell": c, "violations": p, "normals": n} for c, _, _, p, n in cells],
                    "violations": sum(c[3] for c in cells), "pairs": sum(c[3] * c[4] for c in cells)}
        return d

    def same_tool(self, s, key):
        cells = self.cells[key]
        den = sum(c[3] for c in cells)
        return float(sum(H.auroc(s[m], lab) * p for _, m, lab, p, _ in cells) / den) if den else float("nan")

    def per_cell(self, s, key):
        return {c: float(H.auroc(s[m], lab)) for c, m, lab, _, _ in self.cells[key]}

    def metrics(self, s):
        s = np.asarray(s, dtype=np.float64)
        out = {k: self.same_tool(s, k) for k in self.cells}
        wa = wv = 0.0
        na = nv = 0
        for p, m in self.per.items():
            a = auc(s[m], self.y[m])
            mt = m & self.target
            v = auc(s[mt], self.yv[mt])
            out[f"in_{p}_all"], out[f"in_{p}_vis"] = a, v
            if not np.isnan(a):
                wa, na = wa + a * int(self.y[m].sum()), na + int(self.y[m].sum())
            if not np.isnan(v):
                wv, nv = wv + v * int(self.yv[mt].sum()), nv + int(self.yv[mt].sum())
        out["in_period_all"] = wa / na if na else float("nan")
        out["in_period_vis"] = wv / nv if nv else float("nan")
        out["pooled_all"] = auc(s, self.y)
        out["pooled_vis"] = auc(s[self.target], self.yv[self.target])
        alarm = s > float(np.quantile(s[self.norm], 0.95))
        viol = self.y == 1
        out["caught5_all"], out["caught5_vis"] = int((alarm & viol).sum()), int((alarm & self.vis).sum())
        out["caught5_oct"], out["caught5_nov"] = int((alarm & viol & self.per["oct"]).sum()), int((alarm & viol & self.per["nov"]).sum())
        fa = alarm & self.norm
        out["false_alarms5_oct_share"] = float((fa & self.per["oct"]).sum() / max(1, int(fa.sum())))
        out["logloss"] = logloss(s[self.target], self.yv[self.target])
        return out

    def check(self, rng):
        """The fast same-tool code must give the value of the official function."""
        s = rng.normal(size=len(self.rows))
        for key, (pos, mask, mp) in self.spec.items():
            r = E.within_tool_auroc(s[mask], pos[mask].astype(np.int64), self.cell[mask], min_pos=mp)
            ref = float("nan") if r["value"] is None else float(r["value"])
            mine = self.same_tool(s, key)
            assert (np.isnan(ref) and np.isnan(mine)) or abs(ref - mine) < 1e-12, (key, ref, mine)

    def boot(self, S, key, reps=2000, seed=0):
        """Percentile 95% interval of a metric averaged over the repeats in S [repeat][row], resampling scenario families."""
        S = np.asarray(S, dtype=np.float64)
        fams = sorted(set(self.fam.tolist()))
        rng = np.random.default_rng(seed)
        vals = []
        if key in self.spec:
            pos, mask, mp = self.spec[key]
            holding = {c for c in set(self.cell[mask & pos].tolist())}
            idx = np.flatnonzero(mask & np.isin(self.cell, list(holding)))
            _, gi = np.unique(self.cell[idx], return_inverse=True)
            lab, f = pos[idx].astype(np.int64), self.fam[idx]
            members = [np.flatnonzero(f == x) for x in fams]
            for _ in range(reps):
                loc = np.concatenate([members[i] for i in rng.integers(0, len(fams), len(fams))])
                if not len(loc):
                    continue
                num, den, gl = 0.0, 0, gi[loc]
                for c in np.unique(gl):
                    m = loc[gl == c]
                    p = int(lab[m].sum())
                    if p < mp or len(m) - p < MIN_NEG:
                        continue
                    num += float(np.mean([H.auroc(S[r][idx[m]], lab[m]) for r in range(len(S))])) * p
                    den += p
                if den:
                    vals.append(num / den)
        else:
            use_vis = key.endswith("_vis")
            base = self.target if use_vis else np.ones(len(self.rows), dtype=bool)
            lab_all = self.yv if use_vis else self.y
            members = [np.flatnonzero((self.fam == x) & base) for x in fams]
            for _ in range(reps):
                loc = np.concatenate([members[i] for i in rng.integers(0, len(fams), len(fams))])
                num, den = 0.0, 0
                for p in ("oct", "nov"):
                    m = loc[self.per[p][loc]]
                    k = int(lab_all[m].sum())
                    if 0 < k < len(m):
                        num += float(np.mean([H.auroc(S[r][m], lab_all[m]) for r in range(len(S))])) * k
                        den += k
                if den:
                    vals.append(num / den)
        if len(vals) < reps // 10:
            return None
        lo, hi = np.percentile(vals, [2.5, 97.5])
        return {"low": float(lo), "high": float(hi), "valid_resamples": len(vals), "families": len(fams)}


def mean_dict(ds):
    return {k: float(np.nanmean([d[k] for d in ds])) if any(not np.isnan(d[k]) for d in ds) else float("nan") for k in ds[0]}


def better(a, b):
    """Is candidate a ahead of b under the picking rule?  Each is (pick metric, tie metric, order tuple)."""
    for x, y in ((a[0], b[0]), (a[1], b[1])):
        x, y = (-1.0 if np.isnan(x) else x), (-1.0 if np.isnan(y) else y)
        if abs(x - y) > 1e-12:
            return x > y
    return a[2] < b[2]


def fmt(v, nd=3):
    return "—" if v is None or (isinstance(v, float) and np.isnan(v)) else f"{v:.{nd}f}"


def main(argv):
    quick = "--quick" in argv
    t0 = time.time()
    D = R.load()
    ev = {s: SplitEval(D, D["idx"][s]) for s in R.SPLITS}
    rng = np.random.default_rng(0)
    for e in ev.values():
        e.check(rng)
    res = {"name": "resplit-1117 / run01", "plan": "reports/risk-loop/resplit-1117/run01/README.md", "epochs": R.EPOCHS,
           "fixed_epoch": R.FIXED_EPOCH, "pick_rule": f"validation {PICK_KEY}, then validation {PICK_TIE}, then earlier epoch / smaller model / smaller weight",
           "data": {s: ev[s].describe() for s in R.SPLITS}, "em": {}, "p": {}}
    table = []                                                    # one line per model / weight / repeat / epoch / split
    order = {}
    # ------------------------------------------------------------------ Argus-V-em
    em_dir = R.OUT / "em"
    for ai, arch in enumerate(R.ARCHS):
        for wi, wtag in enumerate(R.WEIGHT_RULES):
            files = [em_dir / f"{arch}_{wtag}_r{k}.npz" for k in R.REPEATS]
            files = [f for f in files if f.is_file()]
            if not files:
                continue
            cfg = f"{arch}_{wtag}"
            order[cfg] = (ai, wi)
            runs = [np.load(f, allow_pickle=False) for f in files]
            used = [float(z["pos_weight"]) for z in runs]              # the weight each run really used must be the intended one
            meant = [R.weight_fn(wtag)(float(len(z["y_fit"]) - z["y_fit"].sum()), float(z["y_fit"].sum())) for z in runs]
            assert all(abs(a - b) < 1e-3 for a, b in zip(used, meant)), f"{cfg}: weights used {used}, intended {meant}"
            per = {s: [] for s in ("validation", "test", "fit")}     # [repeat][epoch] -> metric dict
            for z in runs:
                fit_ev = SplitEval(D, z["fit_rows"])
                for s, arr, e_ in (("validation", z["scores_validation"], ev["validation"]), ("test", z["scores_test"], ev["test"]),
                                   ("fit", z["scores_fit"], fit_ev)):
                    per[s].append([e_.metrics(arr[e]) for e in range(R.EPOCHS)])
            for s in per:
                for k, run in enumerate(per[s]):
                    for e, m in enumerate(run):
                        table.append({"model": arch, "weight": wtag, "repeat": k, "epoch": e + 1, "split": s, **m})
            curves = {s: {key: np.asarray([[run[e][key] for e in range(R.EPOCHS)] for run in per[s]], dtype=np.float64) for key in CURVE_KEYS}
                      for s in per}
            mean = {s: {key: np.nanmean(curves[s][key], axis=0) if not np.isnan(curves[s][key]).all() else np.full(R.EPOCHS, np.nan)
                        for key in CURVE_KEYS} for s in per}
            best = 0
            for e in range(1, R.EPOCHS):
                if better((mean["validation"][PICK_KEY][e], mean["validation"][PICK_TIE][e], e), (mean["validation"][PICK_KEY][best], mean["validation"][PICK_TIE][best], best)):
                    best = e

            def at(e):
                return {s: {"mean": {key: float(mean[s][key][e]) for key in CURVE_KEYS},
                            "per_repeat": {key: [float(x) for x in curves[s][key][:, e]] for key in ("st_vis3", "st_vis2", "st_all3", "in_period_all", "in_period_vis", "caught5_all")}}
                        for s in ("validation", "test", "fit")}

            res["em"][cfg] = {
                "arch": arch, "weight": wtag, "weight_rule": R.WEIGHT_RULES[wtag], "repeats": len(runs),
                "pos_weight": [float(z["pos_weight"]) for z in runs], "seconds": [float(z["seconds"]) for z in runs],
                "fit_rows": int(len(runs[0]["fit_rows"])), "fit_visible": int(runs[0]["y_fit"].sum()),
                "curves_mean": {s: {key: R6(mean[s][key]) for key in CURVE_KEYS} for s in per},
                "loss": {"optimised": R6(np.mean([z["loss_optimised"] for z in runs], axis=0)),
                         "train_eval": R6(np.mean([z["loss_train_eval"] for z in runs], axis=0)),
                         "grad_norm": R6(np.mean([z["grad_norm"] for z in runs], axis=0)),
                         "weight_norm": R6(np.mean([z["weight_norm"] for z in runs], axis=0))},
                "at_fixed_epoch": at(R.FIXED_EPOCH - 1), "at_last_epoch": at(R.EPOCHS - 1),
                "pick": {"epoch": best + 1, **at(best)},
                "best_on_test_for_reference_only": {key: {"epoch": int(np.nanargmax(mean["test"][key])) + 1, "value": float(np.nanmax(mean["test"][key]))}
                                                    for key in ("st_vis3", "st_vis2", "st_all3", "in_period_all", "in_period_vis")
                                                    if not np.isnan(mean["test"][key]).all()},
                "per_cell_at_pick": {s: {key: {c: float(np.mean([ev[s].per_cell(np.asarray(z[f"scores_{s}"][best], dtype=np.float64), key)[c] for z in runs]))
                                               for c in [x[0] for x in ev[s].cells[key]]} for key in ("st_vis2", "st_all3")} for s in ("validation", "test")}}
            log(f"{cfg:12s} repeats {len(runs)} | pick epoch {best + 1:3d}: validation {PICK_KEY} {mean['validation'][PICK_KEY][best]:.3f} -> test st_vis3 "
                f"{mean['test']['st_vis3'][best]:.3f} st_vis2 {mean['test']['st_vis2'][best]:.3f} in_period_all {mean['test']['in_period_all'][best]:.3f} | "
                f"fixed epoch {R.FIXED_EPOCH}: test st_vis3 {mean['test']['st_vis3'][R.FIXED_EPOCH - 1]:.3f} st_vis2 {mean['test']['st_vis2'][R.FIXED_EPOCH - 1]:.3f}")
    # ------------------------------------------------------------------ Argus-V-p
    for pi, sid in enumerate(P_KO):
        f = R.OUT / "p" / f"{sid}.npz"
        if not f.is_file():
            continue
        z = np.load(f, allow_pickle=False)
        m = {s: ev[s].metrics(z[f"scores_{s}"]) for s in R.SPLITS}
        for s in R.SPLITS:
            table.append({"model": sid, "weight": "", "repeat": 0, "epoch": 0, "split": s, **m[s]})
        res["p"][sid] = {"ko": P_KO[sid], "seconds": float(z["seconds"]), **{s: m[s] for s in R.SPLITS},
                         "per_cell": {s: {key: ev[s].per_cell(np.asarray(z[f"scores_{s}"], dtype=np.float64), key) for key in ("st_vis2", "st_all3")}
                                      for s in ("validation", "test")}}
        order[sid] = (len(R.ARCHS) + pi, 0)
        log(f"{sid:12s} validation {PICK_KEY} {m['validation'][PICK_KEY]:.3f} -> test st_vis3 {m['test']['st_vis3']:.3f} st_vis2 {m['test']['st_vis2']:.3f} "
            f"in_period_all {m['test']['in_period_all']:.3f} | train st_all3 {m['train']['st_all3']:.3f}")
    # ------------------------------------------------------------------ picks by the fixed rule
    cands = {}
    for cfg, r in res["em"].items():
        v = r["pick"]["validation"]["mean"]
        cands[cfg] = (v[PICK_KEY], v[PICK_TIE], order[cfg])
    for sid, r in res["p"].items():
        cands[sid] = (r["validation"][PICK_KEY], r["validation"][PICK_TIE], order[sid])
    if cands:
        top = None
        for name, c in cands.items():
            if top is None or better(c, cands[top]):
                top = name
        res["overall_pick"] = {"model": top, "validation": {PICK_KEY: cands[top][0], PICK_TIE: cands[top][1]},
                               "epoch": res["em"][top]["pick"]["epoch"] if top in res["em"] else None}
        best_p = None
        for sid in res["p"]:
            if best_p is None or better(cands[sid], cands[best_p]):
                best_p = sid
        res["best_argus_v_p"] = best_p
        # 95% intervals for the fixed recipe, the overall pick and the best Argus-V-p setting
        res["intervals"] = {}
        want = {"fixed recipe (EM64_w15, epoch %d)" % R.FIXED_EPOCH: ("EM64_w15", R.FIXED_EPOCH - 1), "overall pick": (top, None)}
        if best_p:
            want["best Argus-V-p"] = (best_p, None)
        for label, (name, e) in want.items():
            if name in res["em"]:
                e = res["em"][name]["pick"]["epoch"] - 1 if e is None else e
                arch, wtag = name.split("_")
                zs = [np.load(em_dir / f"{arch}_{wtag}_r{k}.npz", allow_pickle=False) for k in R.REPEATS if (em_dir / f"{arch}_{wtag}_r{k}.npz").is_file()]
                S = {s: np.stack([z[f"scores_{s}"][e] for z in zs]) for s in ("validation", "test")}
            elif name in res["p"]:
                z = np.load(R.OUT / "p" / f"{name}.npz", allow_pickle=False)
                S = {s: np.asarray(z[f"scores_{s}"])[None] for s in ("validation", "test")}
            else:
                continue
            res["intervals"][label] = {"model": name, "epoch": None if e is None else e + 1,
                                       **{s: {key: ev[s].boot(S[s], key) for key in CI_KEYS} for s in ("validation", "test")}}
            log("intervals", label, {s: {k: (None if v is None else [round(v["low"], 3), round(v["high"], 3)]) for k, v in res["intervals"][label][s].items()}
                                     for s in ("validation", "test")})
    # ------------------------------------------------------------------ all train rows re-scored from the model files
    if not quick:
        res["train_rescored"] = train_rescored(D, ev["train"])
    res["complete"] = {"em_configs": len(res["em"]), "p_settings": len(res["p"]), "quick": quick}
    res["evaluation_sha256"] = E.evaluate_sha256()
    res["computed_at"] = time.strftime("%Y-%m-%d %H:%M:%S")
    R.REPORT.mkdir(parents=True, exist_ok=True)
    (R.REPORT / "results.json").write_text(json.dumps(E.to_jsonable(res), ensure_ascii=False), encoding="utf-8")
    cols = ["model", "weight", "repeat", "epoch", "split"] + list(CURVE_KEYS)
    with open(R.REPORT / "epoch_table.csv", "w", newline="", encoding="utf-8") as h:
        wr = csv.writer(h)
        wr.writerow(cols)
        for r in table:
            wr.writerow([r["model"], r["weight"], r["repeat"], r["epoch"], r["split"]]
                        + [("" if isinstance(r[k], float) and np.isnan(r[k]) else (f"{r[k]:.6f}" if isinstance(r[k], float) else r[k])) for k in CURVE_KEYS])
    write_tables(res)
    log("metrics written:", len(res["em"]), "Argus-V-em configurations,", len(res["p"]), "Argus-V-p settings,", len(table), "table lines",
        f"| {time.time() - t0:.0f}s", "| overall pick", res.get("overall_pick"))


def R6(a):
    return [None if np.isnan(x) else round(float(x), 6) for x in np.asarray(a, dtype=np.float64)]


def train_rescored(D, ev_train):
    """Scores of every train row (not only the sampled fit rows) from the saved model files, at the fixed and last epoch."""
    import torch
    from experiments.risk_loop.argus_loop import argus_v_em as EM

    f23 = np.load(R.FEAT / "L23_max.npy", mmap_mode="r")
    f16 = np.load(R.FEAT / "L16_pre.npy", mmap_mode="r")
    rows = D["idx"]["train"]
    out = {}
    for arch in R.ARCHS:
        for wtag in R.WEIGHT_RULES:
            for ep in (R.FIXED_EPOCH, R.EPOCHS):
                ms = []
                for k in R.REPEATS:
                    f = R.OUT / "em" / "checkpoints" / f"{arch}_{wtag}_r{k}_e{ep:03d}.pt"
                    if not f.is_file():
                        continue
                    pl = torch.load(f, map_location="cpu", weights_only=True)
                    model = EM.LinearScorer(int(pl["input_width"])) if int(pl["width"]) == 0 else EM.LearnedEmbedding(int(pl["input_width"]), int(pl["width"]))
                    model.load_state_dict(pl["state_dict"])
                    model.eval()
                    med, scale = pl["median"].numpy(), pl["scale"].numpy()
                    s = np.empty(len(rows), dtype=np.float64)
                    with torch.no_grad():
                        for i in range(0, len(rows), 2048):
                            x = np.concatenate([np.asarray(f23[rows[i:i + 2048]], dtype=np.float32), np.asarray(f16[rows[i:i + 2048]], dtype=np.float32)], axis=1)
                            s[i:i + 2048] = model(torch.from_numpy(EM.robust_scale(x, med, scale))).numpy()
                    ms.append(ev_train.metrics(s))
                if ms:
                    out[f"{arch}_{wtag}@{ep}"] = mean_dict([{k: float(v) for k, v in m.items()} for m in ms])
    return out


def write_tables(res):
    """The main tables as Markdown, so the write-up quotes exactly what was computed."""
    d = res["data"]
    L = ["# 새 분할 1차 학습 — 숫자 표 (자동 생성)", "",
         "용어: **주 지표** = 같은 도구를 쓴 호출끼리 비교, 근거가 보인 위반 3개 이상인 도구 / **넓힌 지표** = 같은 방식, 2개 이상인 도구 / "
         "**같은 시기 안** = 10월끼리·11월끼리 모든 호출을 정상 대 위반으로 가른 값의 가중 평균. Argus-V-em 값은 반복 3번의 평균.", "",
         "## 평가 데이터", "", "| 분할 | 호출 | 위반 | 근거가 보인 위반 | 주 지표 (도구·위반·비교 쌍) | 넓힌 지표 (도구·위반·비교 쌍) | 기록 시기만 아는 점수 |", "|---|---|---|---|---|---|---|"]
    for s in ("train", "validation", "test"):
        x = d[s]
        L.append(f"| {s} | {x['calls']:,} | {x['violations']} | {x['visible_violations']} | {len(x['st_vis3']['cells'])}개·{x['st_vis3']['violations']}·{x['st_vis3']['pairs']} | "
                 f"{len(x['st_vis2']['cells'])}개·{x['st_vis2']['violations']}·{x['st_vis2']['pairs']} | {x['period_only_score_all_calls']:.3f} |")
    L += ["", "## validation으로 고른 epoch에서의 값", "",
          "| 모델 | 위반 가중치 | 고른 epoch | validation 넓힌 지표 | validation 주 지표 | **test 주 지표** | **test 넓힌 지표** | test 같은 도구·위반 전체 | test 같은 시기 안 (위반 전체) | test 같은 시기 안 (근거 보인 위반) | test 잡은 위반 (5% 오경보) |",
          "|---|---|---|---|---|---|---|---|---|---|---|"]
    for cfg, r in res["em"].items():
        v, t = r["pick"]["validation"]["mean"], r["pick"]["test"]["mean"]
        L.append(f"| Argus-V-em {ARCH_KO[r['arch']]} | {R.WEIGHT_KO[r['weight']]} | {r['pick']['epoch']} | {fmt(v['st_vis2'])} | {fmt(v['st_vis3'])} | **{fmt(t['st_vis3'])}** | "
                 f"**{fmt(t['st_vis2'])}** | {fmt(t['st_all3'])} | {fmt(t['in_period_all'])} | {fmt(t['in_period_vis'])} | {t['caught5_all']:.1f} / {d['test']['violations']} |")
    for sid, r in res["p"].items():
        v, t = r["validation"], r["test"]
        L.append(f"| Argus-V-p {sid} {r['ko']} | — | — | {fmt(v['st_vis2'])} | {fmt(v['st_vis3'])} | **{fmt(t['st_vis3'])}** | **{fmt(t['st_vis2'])}** | {fmt(t['st_all3'])} | "
                 f"{fmt(t['in_period_all'])} | {fmt(t['in_period_vis'])} | {t['caught5_all']} / {d['test']['violations']} |")
    L += ["", f"## 정해 둔 epoch({res['fixed_epoch']})에서의 값 (아무것도 고르지 않음)", "",
          "| 모델 | 위반 가중치 | validation 주 지표 | validation 넓힌 지표 | **test 주 지표** | **test 넓힌 지표** | test 같은 도구·위반 전체 | test 같은 시기 안 (위반 전체) | test 같은 시기 안 (근거 보인 위반) | 학습 행 주 지표 |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    for cfg, r in res["em"].items():
        v, t, f = (r["at_fixed_epoch"][s]["mean"] for s in ("validation", "test", "fit"))
        L.append(f"| Argus-V-em {ARCH_KO[r['arch']]} | {R.WEIGHT_KO[r['weight']]} | {fmt(v['st_vis3'])} | {fmt(v['st_vis2'])} | **{fmt(t['st_vis3'])}** | **{fmt(t['st_vis2'])}** | "
                 f"{fmt(t['st_all3'])} | {fmt(t['in_period_all'])} | {fmt(t['in_period_vis'])} | {fmt(f['st_vis3'])} |")
    if "overall_pick" in res:
        L += ["", "## 미리 정한 규칙으로 고른 것", "", f"- 전체에서 고른 모델: **{res['overall_pick']['model']}** (epoch {res['overall_pick']['epoch']}), "
              f"validation 넓힌 지표 {fmt(res['overall_pick']['validation'][PICK_KEY])}", f"- Argus-V-p 중 가장 높은 설정: {res.get('best_argus_v_p')}", "",
              "### 95% 구간 (시나리오 계열을 다시 뽑아 계산)", "", "| 대상 | 분할 | 주 지표 | 넓힌 지표 | 같은 도구·위반 전체 | 같은 시기 안 (위반 전체) | 같은 시기 안 (근거 보인 위반) |", "|---|---|---|---|---|---|---|"]
        for label, x in res.get("intervals", {}).items():
            for s in ("validation", "test"):
                L.append(f"| {label} | {s} | " + " | ".join("—" if x[s][k] is None else f"{x[s][k]['low']:.3f}–{x[s][k]['high']:.3f}" for k in CI_KEYS) + " |")
    L += ["", "## test에서 가장 높았던 epoch (참고, 고르는 데 쓰지 않음)", "", "| 모델 | 위반 가중치 | 주 지표 | 넓힌 지표 | 같은 시기 안 (위반 전체) |", "|---|---|---|---|---|"]
    for cfg, r in res["em"].items():
        b = r["best_on_test_for_reference_only"]
        L.append(f"| Argus-V-em {ARCH_KO[r['arch']]} | {R.WEIGHT_KO[r['weight']]} | " + " | ".join(
            (f"{b[k]['value']:.3f} ({b[k]['epoch']} epoch)" if k in b else "—") for k in ("st_vis3", "st_vis2", "in_period_all")) + " |")
    (R.REPORT / "tables.md").write_text("\n".join(L) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1:])

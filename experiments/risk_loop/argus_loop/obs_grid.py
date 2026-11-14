"""Phase-3 runner (FROZEN prereg reports/risk-loop/argus-v1/loop/iter-13/prereg.md §4; monitor checks
reports/risk-loop/argus-v1/loop/audit/phase3-01-setup.md §12).

Design: every model fit is a pure function of (config, training positions, training labels, scored positions).
Fits are precomputed in parallel (joblib/loky, <= 9 workers, 1-2 torch threads each) into a resumable store
``phase3/fits/<config_id>/<key>.npz``; the FROZEN evaluate.py functions (run_cv, nested_cv with inner_splits=4,
metrics, shuffle_test, success_gate) then run in the main process on top of a memoised fit_predict. The
selection / metric / shuffle logic is therefore always the frozen code; the precompute only decides speed
(a store miss is computed inline and counted).

Stages (``py -3.11 experiments/risk_loop/argus_loop/obs_grid.py <stage> [...]``):
  screen    64 combos x beta 3 x fold seeds {0,1,2} x init seed 1 -> outer OOF table (OPTIMISTIC, report only)
  nested    per fold seed {0,1,2}, per outer fold, inner family CV-4 picks one of the 192 (combo, beta) choices
            -> the official cycle value (frozen nested_cv); + extra metrics
  confirm   top-3 most chosen combos + all-on + all-off; fold seeds 0-9 x init seeds 3; beta by inner CV-4
  shuffles  (a) and (b) x20 for one fixed config (aux labels shuffled in the same cells)
  reselect  (b) x5 redoing the whole 192-way selection with permuted labels (aux labels shuffled too)
  controls  M0, C-pre, C-nopre, C-cmax (pooled L20 max), T7-a, R-only (not tries)
  package   fit one config on an outer-training set, fold into ArgusScorer, threshold from inner OOF normals
  report    summary + try counter + luck correction
  timing    synthetic full-size timing (no real data)
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import subprocess
import sys
import time
from collections import Counter
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop import harness as H  # noqa: E402
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402
from experiments.risk_loop.argus_loop import obs_models as OM  # noqa: E402

EVAL_SHA = "a7c36eafdf994f98b61895be4e4b8d237740d0018422d12febab8deb9df0130d"
ART = REPO_ROOT / "artifacts" / "risk-loop" / "argus-v1-loop"
VIEW = ART / "features_labels_v2"
CACHE = ART / "obs_cache"
OUT = ART / "phase3"
LOOP = REPO_ROOT / "reports" / "risk-loop" / "argus-v1" / "loop"
PREREG = LOOP / "iter-13" / "prereg.md"
PREREG_SHA_FILE = LOOP / "iter-13" / "prereg.sha256"
ADDENDA = [(LOOP / "iter-13" / "prereg-addendum-1.md", LOOP / "iter-13" / "prereg-addendum-1.sha256")]
K11_OFFICIAL = LOOP / "iter-13" / "k11_cache_check.json"
K11_VERDICT = ("PASS", "orchestrator 2026-11-09: main probe (L20 pca10) cache - orig = +0.0027; the three diffs "
               "> 0.01 are all in the cache's favour (not information loss)")
MIN_FREE_GB = 2.0
LABEL_FILES = {ART / "labels" / "labels_trainval.v2.csv": "99fc80ca1e08da30",
               VIEW / "steps.csv": "733e6204d6c1aa7b",
               LOOP / "data" / "label_overrides.csv": "6f1354ab5aaffc1b"}
SEEDS3, SEEDS10 = (0, 1, 2), tuple(range(10))
INNER = 4                 # prereg §4.2 inner family CV-4
TRY_BASE, TRY_BASE_CONSERVATIVE = 68, 70
REF_B_V2 = 0.596          # prereg §4.4: 3b reference = max(0.596, own shuffle (b))
MAX_WORKERS = 9


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


# ---------------------------------------------------------------------------------------------- run log + checks

class RunLog:
    def __init__(self, out: Path, stage: str):
        self.dir = out / "logs"
        self.dir.mkdir(parents=True, exist_ok=True)
        ts = time.strftime("%Y%m%d-%H%M%S")
        self.path = self.dir / f"{stage}_{ts}.log"
        self.checks: dict[str, dict] = {}
        self.stage = stage

    def __call__(self, *a):
        line = time.strftime("%H:%M:%S ") + " ".join(str(x) for x in a)
        print(line, flush=True)
        with open(self.path, "a", encoding="utf-8") as f:
            f.write(line + "\n")

    def check(self, name: str, ok: bool, detail=None):
        self.checks[name] = {"pass": bool(ok), "detail": detail}
        self(("CHECK PASS " if ok else "CHECK FAIL ") + name, "" if detail is None else json.dumps(E.to_jsonable(detail))[:400])

    def finish(self) -> bool:
        ok = all(c["pass"] for c in self.checks.values())
        (self.path.with_suffix(".checks.json")).write_text(json.dumps(E.to_jsonable(
            {"stage": self.stage, "all_pass": ok, "checks": self.checks}), indent=1), encoding="utf-8")
        self(f"RUN {'VALID' if ok else 'INVALID (a monitor check failed)'}: {len(self.checks)} checks")
        return ok


def label_shas() -> dict:
    return {str(p.relative_to(REPO_ROOT)): (sha256(p)[:16] if p.is_file() else None) for p in LABEL_FILES}


def start_checks(log: RunLog, runner: "Runner", strict_files: bool = True):
    log.check("1_evaluate_sha", E.evaluate_sha256() == EVAL_SHA, E.evaluate_sha256())
    if strict_files:
        shas = label_shas()
        exp = {str(p.relative_to(REPO_ROOT)): v for p, v in LABEL_FILES.items()}
        log.check("6_label_file_sha_start", shas == exp, shas)
        rec = PREREG_SHA_FILE.read_text(encoding="utf-8").split()[0] if PREREG_SHA_FILE.is_file() else None
        cur = sha256(PREREG) if PREREG.is_file() else None
        fits = runner.out / "fits"
        first = min((p.stat().st_mtime for p in fits.rglob("*.npz")), default=None) if fits.is_dir() else None
        older = first is None or (PREREG.is_file() and PREREG.stat().st_mtime <= first)
        log.check("8_prereg_frozen_before_results", rec is not None and rec == cur and older,
                  {"recorded": rec, "current": cur, "first_fit_mtime": first})
        for doc, shaf in ADDENDA:
            rec_a = shaf.read_text(encoding="utf-8").split()[0] if shaf.is_file() else None
            cur_a = sha256(doc) if doc.is_file() else None
            older_a = first is None or (doc.is_file() and doc.stat().st_mtime <= first)
            log.check(f"8b_{doc.stem}_frozen_before_results", rec_a is not None and rec_a == cur_a and older_a,
                      {"recorded": rec_a, "current": cur_a})
        if K11_OFFICIAL.is_file():
            k = json.loads(K11_OFFICIAL.read_text(encoding="utf-8"))
            main = k.get("layers", {}).get("20", {}).get("pca10", {}).get("diff_cache_minus_orig")
            log.check("K11_official_k11_cache_check_verdict", K11_VERDICT[0] == "PASS",
                      {"verdict": K11_VERDICT[0], "note": K11_VERDICT[1], "main_probe_diff": main,
                       "file_sha16": sha256(K11_OFFICIAL)[:16]})
        from experiments.risk_loop.argus_loop import obs_cache as OC
        try:
            ver = OC.ObsCache(runner.cache, verify=True).verify_sha()
            log.check("9_cache_files_match_manifest_sha", bool(ver) and all(ver.values()), ver)
        except ValueError as exc:
            log.check("9_cache_files_match_manifest_sha", False, str(exc))
        man = runner_manifest(runner)
        log.check("9b_cache_grid32_no_test_or_sealed", man.get("observe_every_steps") == {"32": man.get("n_steps")}
                  and set((man.get("steps_by_split") or {}).keys()) <= {"train", "validation"},
                  {k: man.get(k) for k in ("observe_every_steps", "steps_by_split", "n_obs", "cache_bytes")})
    rows = runner.rows
    log.check("7_train_rows_only", set(rows.split.tolist()) == {"train"} and
              set(runner.data.rows.split.tolist()) == {"train"}, dict(Counter(rows.split.tolist())))
    log.check("5a_no_report_tool_rows_in_evaluated_rows",
              not np.isin(rows.tool.astype(str), list(OM.REPORT_TOOLS)).any())
    log.check("5b_rows_y_equals_label_file", runner.rows_y_matches_file(), None)
    log.check("4a_scoring_signature_tool_free", OM.scoring_signature_ok())


def runner_manifest(runner) -> dict:
    p = Path(runner.cache) / "manifest.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.is_file() else {}


def free_gb() -> float:
    try:
        import psutil
        return psutil.virtual_memory().available / 2 ** 30
    except Exception:  # pragma: no cover
        return 99.0


def end_checks(log: RunLog, strict_files: bool = True):
    if strict_files:
        shas = label_shas()
        exp = {str(p.relative_to(REPO_ROOT)): v for p, v in LABEL_FILES.items()}
        log.check("6_label_file_sha_end", shas == exp, shas)
    return log.finish()


# ---------------------------------------------------------------------------------------------- fit store

def fit_key(pos_train, y_train, pos_test) -> str:
    return OM.h_arr(np.asarray(pos_train, np.int64), np.asarray(y_train).astype(np.int8),
                    np.asarray(pos_test, np.int64))


def leak_audit(data: OM.ObsData, out: OM.FitOut, pos_train, pos_test, forbidden, cfg) -> dict:
    """Monitor check 3 for one fit: nothing used for training (training rows, extra report rows, PCA rows,
    T4 rows, M0 rows -- all subsets of pos_train or extras) shares a (family, trajectory, unit) component or a
    family with the scored rows or with the outer test fold of an inner fit."""
    used = np.r_[np.asarray(pos_train, np.int64), np.asarray(out.audit.get("extras", np.zeros(0, np.int64)), np.int64)]
    forb = np.r_[np.asarray(pos_test, np.int64), np.asarray(forbidden if forbidden is not None else [], np.int64)]
    comp_ok = not np.isin(data.comp[used], data.comp[forb]).any()
    fam_ok = not np.intersect1d(data.family[used], data.family[forb]).size
    a = out.audit
    res = {"leak_free": bool(comp_ok and fam_ok), "comp_ok": bool(comp_ok), "family_ok": bool(fam_ok),
           "pca_rows_are_train": bool(a.get("pca_fit_rows_match", True)),
           "extras_comp_ok": bool(a.get("extras_comp_ok", True)),
           "aux_shuffle_flag_ok": bool(a.get("aux_shuffled", False) == bool(cfg.get("aux_null_within"))),
           "t4_ok": (not cfg["T4"]) or a.get("constant", False) or bool(a.get("t4_gaussians") == 1 and
                                                                         a.get("t4_rows_are_train_normals")),
           "t3_extras_hash": a.get("extras_hash"), "n_extras": a.get("n_extras", 0), "aux_used": a.get("aux_used"),
           "constant": a.get("constant", False)}
    res["all_ok"] = bool(res["leak_free"] and res["pca_rows_are_train"] and res["extras_comp_ok"]
                         and res["aux_shuffle_flag_ok"] and res["t4_ok"])
    return res


def save_fit(path: Path, out: OM.FitOut, audit: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.stem + f".tmp{os.getpid()}.npz")
    np.savez(tmp, score=out.score, scores_rep=out.scores_rep, thr=np.asarray([out.thr[f] for f in OM.FARS]),
             argmax=out.argmax, audit=np.asarray(json.dumps(E.to_jsonable(audit))))
    os.replace(tmp, path)


def load_fit(path: Path) -> dict:
    with np.load(path) as z:
        return {"score": z["score"].astype(np.float64), "scores_rep": z["scores_rep"],
                "thr": dict(zip(OM.FARS, z["thr"].tolist())), "argmax": z["argmax"],
                "audit": json.loads(str(z["audit"]))}


_WORKER = {}


def _worker_data(env: dict) -> OM.ObsData:
    key = json.dumps(env, sort_keys=True, default=str)
    if _WORKER.get("key") != key:
        _WORKER.clear()
        _WORKER["key"] = key
        _WORKER["data"] = OM.ObsData.load(env["view"], env["cache"], tuple(env["layers"]))
    return _WORKER["data"]


def _run_job(env: dict, cfgs: list, specs: list) -> dict:
    """Worker: fit every (spec, cfg) not in the store. specs = [(pos_train, y_train, pos_test, forbidden)]."""
    import torch
    torch.set_num_threads(int(env["threads"]))
    data = _worker_data(env)
    out_dir = Path(env["out"]) / "fits"
    done = fails = 0
    t0 = time.time()
    for (pa, ya, pb, forb) in specs:
        key = fit_key(pa, ya, pb)
        for cfg in cfgs:
            p = out_dir / OM.config_id(cfg) / f"{key}.npz"
            if p.is_file():
                continue
            out = OM.fit_obs(data, cfg, pa, ya, pb)
            aud = leak_audit(data, out, pa, pb, forb, cfg)
            fails += int(not aud["all_ok"])
            save_fit(p, out, aud)
            done += 1
    return {"fits": done, "audit_fail": fails, "sec": time.time() - t0, "pid": os.getpid()}


# ---------------------------------------------------------------------------------------------- runner

class Runner:
    def __init__(self, view=VIEW, cache=CACHE, out=OUT, layers=(20,), workers=MAX_WORKERS, threads=2, log=print):
        self.view, self.cache, self.out = Path(view), Path(cache), Path(out)
        self.layers, self.threads = tuple(layers), int(threads)
        ov = Path(out) / "workers.override"  # cap override for a running detached driver
        if ov.is_file():
            workers = int(ov.read_text(encoding="utf-8").split()[0])
        self.workers = min(int(workers), MAX_WORKERS)
        self.max_workers = self.workers
        fg = free_gb()
        if fg < MIN_FREE_GB + 0.65 * self.workers:  # start within the RAM rule (~0.65 GB per worker)
            self.workers = max(2, min(self.workers, int((fg - MIN_FREE_GB) / 0.65)))
        self.log = log
        self.out.mkdir(parents=True, exist_ok=True)
        self.data = OM.ObsData.load(self.view, self.cache, self.layers)
        self.rows = self.data.head
        self.env = {"view": str(self.view), "cache": str(self.cache), "layers": list(self.layers),
                    "threads": self.threads, "out": str(self.out)}
        self.misses = Counter()
        self.lookups = Counter()

    # -------------------------------------------------- integrity helpers
    def rows_y_matches_file(self) -> bool:
        import csv
        lab = {}
        with open(self.view / "steps.csv", newline="", encoding="utf-8") as h:
            for r in csv.DictReader(h):
                lab[int(r["row"])] = r["label"]
        return all(int(float(lab[int(r)])) == int(y) for r, y in zip(self.rows.row_id.tolist(), self.rows.y.tolist()))

    def fold_hash(self, seed: int) -> str:
        return OM.h_arr(np.asarray(E._fold_id(E.make_folds(self.rows, 5, seed), len(self.rows)), np.int64))

    # -------------------------------------------------- spec enumeration (mirrors the frozen code exactly)
    def outer_specs(self, seed):
        y = self.rows.y
        return [(a, y[a], b, None) for a, b in E.make_folds(self.rows, 5, seed)]

    def inner_specs(self, seed, inner=INNER, y_override=None, with_refit=False):
        y = self.rows.y if y_override is None else None
        out = []
        for i, (a, b) in enumerate(E.make_folds(self.rows, 5, seed)):
            ya = y[a] if y_override is None else y_override[i]
            ir = self.rows.subset(a)
            ir.label = np.asarray(ya, np.float64)
            for ia, ib in E.make_folds(ir, inner, seed):
                out.append((a[ia], ya[ia], a[ib], b))
            if with_refit:
                out.append((a, ya, b, None))
        return out

    def shuffled_train_labels(self, seed, n, within, perm_seed=0):
        """Exactly the permutations of evaluate.shuffle_test (fold seed ``seed``): list over j of list over folds."""
        y = self.rows.y
        folds = E.make_folds(self.rows, 5, seed)
        cols = [np.asarray(getattr(self.rows, c)).astype(str) for c in within]
        cell = np.asarray(["\x1f".join(v) for v in zip(*cols)], dtype=object)
        res = []
        for j in range(n):
            per = []
            for i, (a, b) in enumerate(folds):
                rng = np.random.default_rng([int(perm_seed), j, i])
                ya = y[a].copy()
                ca = cell[a]
                for c in sorted(set(ca.tolist())):
                    pos = np.nonzero(ca == c)[0]
                    ya[pos] = ya[rng.permutation(pos)]
                per.append(ya)
            res.append(per)
        return res

    # -------------------------------------------------- parallel precompute
    def precompute(self, cfgs, specs, tag=""):
        todo = []
        for s in specs:
            key = fit_key(s[0], s[1], s[2])
            miss = [c for c in cfgs if not (self.out / "fits" / OM.config_id(c) / f"{key}.npz").is_file()]
            if miss:
                todo.append((s, miss))
        n_fits = sum(len(m) for _, m in todo)
        self.log(f"[precompute {tag}] {len(specs)} specs x {len(cfgs)} configs: {n_fits} fits to run "
                 f"({self.workers} workers x {self.threads} threads)")
        if not n_fits:
            return {"fits": 0}
        jobs = []
        for s, miss in todo:
            ch = int(getattr(self, "chunk", 16))
            for i in range(0, len(miss), ch):
                jobs.append((miss[i:i + ch], [s]))
        t0 = time.time()
        for v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
            os.environ[v] = str(self.threads)
        tot = Counter()
        if self.workers <= 1:
            for c, s in jobs:
                tot.update(_run_job(self.env, c, s))
        else:
            from joblib import Parallel, delayed
            done, i = 0, 0
            while i < len(jobs):
                fg = free_gb()
                if fg < MIN_FREE_GB and self.workers > 2:
                    cut = max(1, int(math.ceil((MIN_FREE_GB - fg) / 0.65)))  # ~0.65 GB per worker
                    self.workers = max(2, self.workers - cut)
                    self.log(f"[precompute {tag}] free RAM {fg:.1f} GB < {MIN_FREE_GB} -> workers {self.workers}")
                elif fg > MIN_FREE_GB + 1.3 and self.workers < self.max_workers:
                    self.workers += 1  # memory freed up again (other programs): grow back, at most the cap
                    self.log(f"[precompute {tag}] free RAM {fg:.1f} GB -> workers {self.workers}")
                wave = max(self.workers * 4, 1)
                batch = jobs[i:i + wave]
                i += len(batch)
                for r in Parallel(n_jobs=self.workers, backend="loky", return_as="generator_unordered")(
                        delayed(_run_job)(self.env, c, s) for c, s in batch):
                    tot.update({k: v for k, v in r.items() if k != "pid"})
                    done += 1
                el = time.time() - t0
                self.log(f"[precompute {tag}] {done}/{len(jobs)} jobs, {tot['fits']} fits, {el / 60:.1f} min, "
                         f"eta {el / done * (len(jobs) - done) / 60:.1f} min, free RAM {free_gb():.1f} GB, "
                         f"workers {self.workers}")
        el = time.time() - t0
        self.log(f"[precompute {tag}] {tot['fits']} fits in {el / 60:.1f} min "
                 f"({el / max(tot['fits'], 1):.2f} s/fit wall, audit failures {tot['audit_fail']})")
        return dict(tot)

    # -------------------------------------------------- memoised fit_predict
    def memo_fp(self, cfg, record=None):
        cid = OM.config_id(cfg)

        def fp(pos_train, y_train, pos_test):
            key = fit_key(pos_train, y_train, pos_test)
            p = self.out / "fits" / cid / f"{key}.npz"
            self.lookups[cid] += 1
            if not p.is_file():
                self.misses[cid] += 1
                out = OM.fit_obs(self.data, cfg, pos_train, y_train, pos_test, threads=self.threads)
                save_fit(p, out, leak_audit(self.data, out, pos_train, pos_test, None, cfg))
            r = load_fit(p)
            if record is not None:
                record[key] = r
            return r["score"]
        fp.cfg = cfg
        return fp

    def fit_record(self, cfg, pos_train, y_train, pos_test) -> dict:
        return load_fit(self.out / "fits" / OM.config_id(cfg) / f"{fit_key(pos_train, y_train, pos_test)}.npz")

    def audits_ok(self, cfgs, specs) -> dict:
        bad, n, t3 = [], 0, {}
        for s in specs:
            key = fit_key(s[0], s[1], s[2])
            for c in cfgs:
                p = self.out / "fits" / OM.config_id(c) / f"{key}.npz"
                if not p.is_file():
                    continue
                a = load_fit(p)["audit"]
                n += 1
                if not a["all_ok"]:
                    bad.append((OM.config_id(c), key))
                if c["T3"] and not a.get("constant"):
                    t3.setdefault(OM.config_id(c), []).append((OM.h_arr(s[0]), a["t3_extras_hash"], a["aux_used"]))
        # T3 redone per fold: every T3 fit used extras, and different training sets -> different extra sets
        t3_ok = all(all(u for _, _, u in v) and len({e for _, e, _ in v}) == len({tr for tr, _, _ in v})
                    for v in t3.values())
        return {"n_fits": n, "n_bad": len(bad), "bad": bad[:10], "t3_per_fold_ok": t3_ok, "t3_configs": len(t3)}


# ---------------------------------------------------------------------------------------------- metrics

def luck_correction(best: float, n_tries: int) -> dict:
    """Previous rule: reported best - 0.05 * E[max of N standard normals]."""
    from scipy.stats import norm
    x = np.linspace(-8, 8, 16001)
    em = float(np.trapz(x * n_tries * norm.pdf(x) * norm.cdf(x) ** (n_tries - 1), x))
    return {"n_tries": n_tries, "e_max_normal": em, "corrected": best - 0.05 * em}


def extra_metrics(runner: Runner, cv: dict, cfg_for_fold) -> dict:
    """AUPRC, detection at FAR 1 % / 5 % (thresholds = training-fold normals' in-sample quantiles of the fit that
    scored the row), within-trajectory ranking C, K3 length correlation, K2 argmax kinds, K10 init stability."""
    from experiments.risk_loop.argus_loop import iter04_common as C4
    rows, data = runner.rows, runner.data
    y, cells = rows.y, E.headline_groups(rows)
    nobs = data.n_obs32[:data.n_head]
    out = {"per_seed": {}}
    for s in cv["seeds"]:
        o = np.asarray(cv["oof"][str(s)], np.float64)
        thr = {f: np.full(len(rows), np.nan) for f in OM.FARS}
        arg = np.zeros(len(rows), np.int64)
        rep_corr = []
        for i, (a, b) in enumerate(E.make_folds(rows, 5, s)):
            cfg = cfg_for_fold(s, i)
            r = runner.fit_record(cfg, a, y[a], b)
            for f in OM.FARS:
                thr[f][b] = r["thr"][f]
            arg[b] = r["argmax"]
            R = r["scores_rep"]
            if R.shape[0] > 1:
                from scipy.stats import spearmanr
                rep_corr += [spearmanr(R[p], R[q]).correlation for p in range(len(R)) for q in range(p + 1, len(R))]
        ap_cells, num, den = [], 0.0, 0
        for c in sorted(set(cells.tolist())):
            m = cells == c
            p = int(y[m].sum())
            if p >= E.MIN_POS and m.sum() - p >= E.MIN_NEG:
                ap = H.average_precision(o[m], y[m])
                num += ap * p
                den += p
        det = {}
        for f in OM.FARS:
            hit = o >= thr[f]
            det[f"far{int(f * 100)}"] = {"detection": float(hit[y == 1].mean()), "false_alarm": float(hit[y == 0].mean()),
                                         "by_source": {src: {"detection": float(hit[(y == 1) & (rows.source == src)].mean())
                                                             if ((y == 1) & (rows.source == src)).any() else None,
                                                             "false_alarm": float(hit[(y == 0) & (rows.source == src)].mean())}
                                                       for src in E.SOURCES}}
        k3 = []
        for c in sorted(set(cells.tolist())):
            m = cells == c
            p = int(y[m].sum())
            if p >= E.MIN_POS and m.sum() - p >= E.MIN_NEG:
                rho = E._spearman(o[m], nobs[m])
                if rho is not None:
                    k3.append((abs(rho), p))
        kind = data.obs_kind[data.off[:data.n_head] + arg]
        pk = kind[y == 1]
        out["per_seed"][str(s)] = {
            "auprc_pooled": H.average_precision(o, y), "auprc_cell_weighted": num / den if den else None,
            "detection": det,
            "within_trajectory_C": C4.within_traj_auroc(o, y, rows.trajectory_id)["value"],
            "K3_abs_spearman_n_obs32_cell_weighted": (sum(a * p for a, p in k3) / sum(p for _, p in k3)) if k3 else None,
            "K3_abs_spearman_max": max((a for a, _ in k3), default=None),
            "K2_violation_argmax_kinds": dict(Counter(pk.tolist())),
            "K2_frac_pre_or_rend": float(np.isin(pk, ["pre_action", "reasoning_end"]).mean()) if len(pk) else None,
            "K2_chance": float(np.mean(2.0 / nobs[y == 1])) if (y == 1).any() else None,
            "K10_init_rank_corr_median": float(np.median(rep_corr)) if rep_corr else None}
    keys = ["auprc_pooled", "auprc_cell_weighted", "within_trajectory_C", "K3_abs_spearman_n_obs32_cell_weighted",
            "K2_frac_pre_or_rend", "K10_init_rank_corr_median"]
    out["mean"] = {k: E._mean([v[k] for v in out["per_seed"].values()]) for k in keys}
    for f in OM.FARS:
        kk = f"far{int(f * 100)}"
        out["mean"][f"detection_{kk}"] = E._mean([v["detection"][kk]["detection"] for v in out["per_seed"].values()])
        out["mean"][f"false_alarm_{kk}"] = E._mean([v["detection"][kk]["false_alarm"] for v in out["per_seed"].values()])
    return out


def compact(m: dict) -> dict:
    wt = m["within_tool"]
    return {"within_tool": wt["value"], "per_seed": wt["per_seed"], "ci95": wt.get("ci95"),
            "by_source": {s: v["value"] for s, v in wt["by_source"].items()}, "pooled_auroc": m["pooled_auroc"],
            "pooled_ap": m["pooled_ap"], "baselines": {k: v["within_tool"] for k, v in m.get("baselines", {}).items()
                                                      if isinstance(v, dict)}}


def fold_hash_check(log: RunLog, runner: Runner, cvs: dict):
    by_seed = {}
    for name, cv in cvs.items():
        for s in cv["seeds"]:
            by_seed.setdefault(s, set()).add(OM.h_arr(np.asarray(cv["fold_id"][str(s)], np.int64)))
    ok = all(len(v) == 1 and next(iter(v)) == runner.fold_hash(s) for s, v in by_seed.items())
    log.check("2_identical_fold_assignment_across_configs", ok,
              {str(s): sorted(v) for s, v in by_seed.items()})


def probe_tool_free(log: RunLog, runner: Runner, cfg):
    """Monitor check 4: scrambling the tool / source / family / trajectory / status / labels of the SCORED rows
    leaves their scores unchanged."""
    data = runner.data
    a, b = E.make_folds(runner.rows, 5, 0)[0]
    y = runner.rows.y
    s1 = OM.fit_obs(data, cfg, a, y[a], b, threads=runner.threads).score
    saved = {k: getattr(data, k).copy() for k in ("tool", "source", "family", "traj", "status")}
    try:
        for k in saved:
            arr = getattr(data, k)
            arr[b] = arr[b][::-1]
        s2 = OM.fit_obs(data, cfg, a, y[a], b, threads=runner.threads).score
    finally:
        for k, v in saved.items():
            setattr(data, k, v)
    log.check("4b_scores_invariant_to_scored_rows_metadata", bool(np.array_equal(s1, s2)),
              {"cfg": OM.combo_name(cfg), "max_abs_diff": float(np.abs(s1 - s2).max())})


# ---------------------------------------------------------------------------------------------- try counter

def bump_tries(out: Path, cfgs, stage: str) -> dict:
    p = out / "try_counter.json"
    d = json.loads(p.read_text(encoding="utf-8")) if p.is_file() else {"base": TRY_BASE,
                                                                        "base_conservative": TRY_BASE_CONSERVATIVE,
                                                                        "combos": {}}
    for c in cfgs:
        k = OM.combo_key(c)
        d["combos"].setdefault(k, {"name": OM.combo_name(c), "first_stage": stage, "time": time.strftime("%F %T"),
                                   "struct": {kk: c[kk] for kk in ("layers", "K", "pool", "head", "slots")}})
    d["cycle_tries"] = len(d["combos"])
    d["cumulative"] = d["base"] + d["cycle_tries"]
    d["cumulative_conservative"] = d["base_conservative"] + d["cycle_tries"]
    p.write_text(json.dumps(d, indent=1, default=list), encoding="utf-8")
    return d


# ---------------------------------------------------------------------------------------------- stages

def stage_screen(r: Runner, log: RunLog, seeds=SEEDS3, struct=None):
    grid = OM.prereg_grid(**(struct or {}))
    log.check("10a_grid_order_is_prereg_order", [OM.config_id(c) for c in grid] ==
              [OM.config_id(c) for c in OM.prereg_grid(**(struct or {}))] and len(grid) == 192,
              {"grid_hash": OM.h_arr(np.frombuffer("".join(OM.config_id(c) for c in grid).encode(), np.uint8))})
    log.check("10b_same_init_seeds_all_configs", len({c["init_seeds"] for c in grid}) == 1, grid[0]["init_seeds"])
    specs = [s for sd in seeds for s in r.outer_specs(sd)]
    r.precompute(grid, specs, "screen")
    au = r.audits_ok(grid, specs)
    log.check("3_no_leak_in_any_fit", au["n_bad"] == 0, au)
    log.check("T3_redone_per_fold", au["t3_per_fold_ok"], au)
    table, cvs = [], {}
    for c in grid:
        cv = E.run_cv(r.memo_fp(c), None, r.rows, seeds)
        cvs[OM.config_id(c)] = cv
        m = E.metrics(cv, r.rows, bootstrap=0, baselines=False)
        table.append({"config_id": OM.config_id(c), "combo": OM.combo_name(c), "beta": c["beta"],
                      **{k: v for k, v in compact(m).items() if k != "baselines"}})
    fold_hash_check(log, r, cvs)
    best = max(table, key=lambda t: t["within_tool"] or -1)
    res = {"stage": "screen", "OPTIMISTIC": "best-config outer values are optimistic (selection outside CV)",
           "seeds": list(seeds), "table": table, "best": best, "misses": dict(r.misses),
           "tries": bump_tries(r.out, grid, "screen")}
    res["luck_corrected_best"] = luck_correction(best["within_tool"], res["tries"]["cumulative"])
    (r.out / "screen.json").write_text(json.dumps(E.to_jsonable(res), indent=1), encoding="utf-8")
    log(f"[screen] best {best['combo']} beta {best['beta']} within-tool {best['within_tool']:.4f} (optimistic)")
    return res


def stage_nested(r: Runner, log: RunLog, seeds=SEEDS3, struct=None):
    grid = OM.prereg_grid(**(struct or {}))
    specs = [s for sd in seeds for s in r.outer_specs(sd)] + [s for sd in seeds for s in r.inner_specs(sd)]
    r.precompute(grid, specs, "nested")
    au = r.audits_ok(grid, specs)
    log.check("3_no_outer_rows_in_inner_selection", au["n_bad"] == 0, au)
    log.check("T3_redone_per_fold", au["t3_per_fold_ok"], au)
    probe_tool_free(log, r, OM.make_config((1, 1, 1, 1, 1, 1), 1.0, **(struct or {})))
    cv = E.nested_cv(lambda g: r.memo_fp(g), grid, None, r.rows, seeds, 5, inner_splits=INNER)
    m = E.metrics(cv, r.rows)
    fold_hash_check(log, r, {"nested": cv})
    chosen = {s: [grid[i] for i in cv["selection"]["chosen"][str(s)]] for s in seeds}
    ex = extra_metrics(r, cv, lambda s, i: chosen[s][i])
    inner_best = {str(s): [max(v) for v in cv["selection"]["inner_scores"][str(s)]] for s in seeds}
    cnt = Counter(OM.combo_name(c) for v in chosen.values() for c in v)
    modal = grid[E._modal_choice(cv)]
    res = {"stage": "nested", "OFFICIAL": "nested value = the honest cycle-1 number (prereg §4.2)",
           "metrics": compact(m), "metrics_full": m, "extra": ex, "evaluate_sha256": E.evaluate_sha256(),
           "chosen": {str(s): [{"combo": OM.combo_name(c), "beta": c["beta"], "config_id": OM.config_id(c)}
                               for c in v] for s, v in chosen.items()},
           "inner_best_score": inner_best, "combo_counts": dict(cnt.most_common()),
           "modal": {"combo": OM.combo_name(modal), "beta": modal["beta"], "config_id": OM.config_id(modal),
                     "bits": [modal[t] for t in OM.TOGGLES]},
           "misses": dict(r.misses), "labels": "labels v2 (conventions decided after results) / Nov draft labels"}
    (r.out / "nested.json").write_text(json.dumps(E.to_jsonable(res), indent=1), encoding="utf-8")
    np.save(r.out / "nested_oof.npy", np.asarray([cv["oof"][str(s)] for s in seeds]))
    log(f"[nested] within-tool {m['within_tool']['value']:.4f} CI {m['within_tool']['ci95']} modal {res['modal']}")
    return res


def stage_confirm(r: Runner, log: RunLog, seeds=SEEDS10, init=(0, 1, 2), struct=None, combos=None):
    nested = json.loads((r.out / "nested.json").read_text(encoding="utf-8"))
    if combos is None:
        top = [k for k, _ in Counter(nested["combo_counts"]).most_common(3)]
        names = top + [n for n in ("T1+T2+T3+T4+T5+T6", "base") if n not in top]
    else:
        names = combos
    bits_of = {OM.combo_name(OM.make_config(b)): b for b in OM.combos()}
    out = {"stage": "confirm", "seeds": list(seeds), "init_seeds": list(init), "combos": {}}
    for name in names:
        grid = [OM.make_config(bits_of[name], beta, init_seeds=init, **(struct or {})) for beta in OM.BETAS]
        specs = [s for sd in seeds for s in r.outer_specs(sd)] + [s for sd in seeds for s in r.inner_specs(sd)]
        r.precompute(grid, specs, f"confirm {name}")
        au = r.audits_ok(grid, specs)
        log.check(f"3_no_leak_confirm_{name}", au["n_bad"] == 0, au)
        cv = E.nested_cv(lambda g: r.memo_fp(g), grid, None, r.rows, seeds, 5, inner_splits=INNER)
        fold_hash_check(log, r, {name: cv})
        m = E.metrics(cv, r.rows)
        ex = extra_metrics(r, cv, lambda s, i: grid[cv["selection"]["chosen"][str(s)][i]])
        k10 = ex["mean"]["K10_init_rank_corr_median"]
        out["combos"][name] = {"metrics": compact(m), "extra": ex, "beta_chosen": dict(Counter(
            OM.BETAS[i] for v in cv["selection"]["chosen"].values() for i in v)),
            "modal_config_id": OM.config_id(grid[E._modal_choice(cv)]),
            "K10_flag_unstable": (k10 is not None and k10 < 0.8)}
        log(f"[confirm] {name}: within-tool {m['within_tool']['value']:.4f} (10 seeds)")
    (r.out / "confirm.json").write_text(json.dumps(E.to_jsonable(out), indent=1), encoding="utf-8")
    return out


def stage_shuffles(r: Runner, log: RunLog, cfg, n=20, seed=0):
    """(a) source and (b) source x family, n each, fixed config, aux labels shuffled in the same cells."""
    res = {"config_id": OM.config_id(cfg), "combo": OM.combo_name(cfg), "beta": cfg["beta"]}
    for tag, within in (("a", ("source",)), ("b", ("source", "family"))):
        c = dict(cfg)
        c["aux_null_within"] = tuple(within)
        c = OM.make_config([c[t] for t in OM.TOGGLES], c["beta"], **{k: v for k, v in c.items()
                                                                      if k not in OM.TOGGLES and k != "beta"})
        labs = r.shuffled_train_labels(seed, n, within)
        folds = E.make_folds(r.rows, 5, seed)
        specs = [(a, labs[j][i], b, None) for j in range(n) for i, (a, b) in enumerate(folds)]
        r.precompute([c], specs, f"shuffle {tag}")
        au = r.audits_ok([c], specs)
        log.check(f"3_no_leak_shuffle_{tag}", au["n_bad"] == 0, au)
        log.check(f"5c_aux_labels_shuffled_{tag}", c["aux_null_within"] == tuple(within))
        st = E.shuffle_test(r.memo_fp(c), r.rows, n, seed=seed, within=within, n_jobs=1)
        res[tag] = {k: st[k] for k in ("within_tool_mean", "within_tool_sd", "within_tool_se", "within_tool",
                                       "pass", "within_tool_by_source_mean")}
        log(f"[shuffle {tag}] mean {st['within_tool_mean']:.4f} (n={n})")
    res["K9_shuffle_a_in_0.45_0.55"] = bool(abs(res["a"]["within_tool_mean"] - 0.5) <= 0.05)
    res["ref_3b"] = max(REF_B_V2, res["b"]["within_tool_mean"])
    p = r.out / "shuffles.json"
    d = json.loads(p.read_text(encoding="utf-8")) if p.is_file() else {}
    d[OM.config_id(cfg)] = res
    p.write_text(json.dumps(E.to_jsonable(d), indent=1), encoding="utf-8")
    return res


def stage_reselect(r: Runner, log: RunLog, n=5, seed=0, struct=None):
    """(b) x n with the full 192-way nested selection redone on permuted labels (aux labels shuffled too)."""
    within = ("source", "family")
    grid = [OM.make_config([c[t] for t in OM.TOGGLES], c["beta"], aux_null_within=within, **(struct or {}))
            for c in OM.prereg_grid(**(struct or {}))]
    labs = r.shuffled_train_labels(seed, n, within)
    specs = []
    for j in range(n):
        specs += r.inner_specs(seed, y_override=labs[j], with_refit=True)
    r.precompute(grid, specs, "reselect")
    au = r.audits_ok(grid, specs)
    log.check("3_no_leak_reselect", au["n_bad"] == 0, au)
    log.check("5c_aux_labels_shuffled_reselect", all(c["aux_null_within"] == within for c in grid))
    nfp = OM.NestedFP(lambda g: r.memo_fp(g), grid, r.rows, seed, INNER)
    st = E.shuffle_test(nfp, r.rows, n, seed=seed, within=within, n_jobs=1)
    res = {k: st[k] for k in ("within_tool_mean", "within_tool_sd", "within_tool_se", "within_tool")}
    res["chosen"] = [OM.combo_name(grid[i]) + f"|b{grid[i]['beta']}" for i in nfp.chosen]
    res["misses"] = dict(r.misses)
    (r.out / "reselect.json").write_text(json.dumps(E.to_jsonable(res), indent=1), encoding="utf-8")
    log(f"[reselect] (b) with re-selection mean {st['within_tool_mean']:.4f} (n={n})")
    return res


def control_configs(struct=None):
    s = struct or {}
    return {"M0": OM.make_config(beta=1.0, filters="m0_fixed", K=1, **s),
            "C-pre": OM.make_config(beta=1.0, obs_subset="pre", **s),
            "C-nopre": OM.make_config(beta=1.0, obs_subset="nopre", slots=("pool", "mean"), **s)}


def pooled_control_fps(r: Runner):
    """C-cmax (pooled L20 max -> robust PCA 32 -> class-balanced logistic C 0.1), T7-a, R-only (existing code)."""
    from experiments.risk_loop.argus_loop import iter01_common as C1
    from experiments.risk_loop.argus_loop import iter02_common as C2
    from experiments.risk_loop.argus_loop import iter04_diag as D4
    from experiments.risk_loop.argus_loop import iter07_models as M7
    from experiments.risk_loop.argus_loop import iter11_diag_models as DM
    data, rows, _ = C1.headline_data(r.view)
    assert np.array_equal(rows.row_id, r.rows.row_id)
    X20 = np.asarray(C1.features(data, rows, 20, "max"), np.float32)

    def cmax(pa, ya, pb):
        from sklearn.linear_model import LogisticRegression
        Em = M7.robust_embed(X20, pa)
        if len(np.unique(ya)) < 2:
            return np.zeros(len(pb))
        lr = LogisticRegression(C=0.1, class_weight="balanced", max_iter=3000).fit(Em[pa], ya)
        return lr.decision_function(Em[pb])
    feats = DM.load_feats(data, rows, ["L23:max", "L16:pre"])
    t7a = DM.make_t7a(feats, rows)[0]
    ronly = D4.group_mean_fp(feats["L23:max"], C2.ctx_for(rows), rows.trajectory_id.astype(str), k=32, C=0.1)
    return {"C-cmax": cmax, "T7-a": t7a, "R-only": ronly}


def _pooled_cv(view, name, seed):
    import gc
    _WORKER.clear()  # free a reused worker's observation data before loading pooled features
    gc.collect()
    r = Runner.__new__(Runner)
    r.view = Path(view)
    from experiments.risk_loop.argus_loop import iter01_common as C1
    _, r.rows, _ = C1.headline_data(r.view)
    return E.run_cv(pooled_control_fps(r)[name], None, r.rows, [seed])


def stage_controls(r: Runner, log: RunLog, seeds=SEEDS10, struct=None, pooled=True):
    cfgs = control_configs(struct)
    specs = [s for sd in seeds for s in r.outer_specs(sd)]
    r.precompute(list(cfgs.values()), specs, "controls")
    res, cvs = {}, {}
    for name, c in cfgs.items():
        cv = E.run_cv(r.memo_fp(c), None, r.rows, seeds)
        cvs[name] = cv
        res[name] = {"metrics": compact(E.metrics(cv, r.rows)), "extra": extra_metrics(r, cv, lambda s, i, c=c: c)}
        log(f"[controls] {name}: {res[name]['metrics']['within_tool']:.4f}")
    if pooled:
        from joblib import Parallel, delayed
        for name in ("C-cmax", "T7-a", "R-only"):
            parts = Parallel(n_jobs=min(3, len(seeds)), backend="loky")(
                delayed(_pooled_cv)(str(r.view), name, s) for s in seeds)
            cv = parts[0]
            for p in parts[1:]:
                for k in ("oof", "fold_id", "folds"):
                    cv[k].update(p[k])
            cv["seeds"] = list(seeds)
            cvs[name] = cv
            res[name] = {"metrics": compact(E.metrics(cv, r.rows))}
            log(f"[controls] {name}: {res[name]['metrics']['within_tool']:.4f}")
    fold_hash_check(log, r, cvs)
    (r.out / "controls.json").write_text(json.dumps(E.to_jsonable(res), indent=1), encoding="utf-8")
    return res


def stage_package(r: Runner, log: RunLog, cfg, seed=0, fold=0, far=0.05, name="argus_v1_pool"):
    from experiments.risk_loop.argus_loop import argus_scorer as AS
    from experiments.risk_loop.argus_loop import obs_cache as OC
    y = r.rows.y
    a, b = E.make_folds(r.rows, 5, seed)[fold]
    out = OM.fit_obs(r.data, cfg, a, y[a], b, keep_model=True, threads=r.threads)
    # threshold = (1 - far) quantile of INNER-OOF normal scores (inner family CV-4 on the training rows)
    ir = r.rows.subset(a)
    io = np.full(len(a), np.nan)
    for ia, ib in E.make_folds(ir, INNER, seed):
        io[ib] = OM.fit_obs(r.data, cfg, a[ia], y[a][ia], a[ib], threads=r.threads).score
    thr = float(np.quantile(io[y[a] == 0], 1 - far))
    cache = OC.ObsCache(r.cache)
    bases = {L: cache.basis(L) for L in cfg["layers"]}
    try:
        commit = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, cwd=REPO_ROOT).stdout.strip()
    except Exception:  # pragma: no cover
        commit = None
    train_units = sorted(set(r.rows.unit_id[a].tolist()))
    held_units = sorted(set(r.rows.unit_id[b].tolist()))
    meta = {"hf_revision": cache.manifest.get("revision"), "commit": commit, "fold_seed": seed, "fold": fold,
            "train_units_sha": hashlib.sha256("\n".join(train_units).encode()).hexdigest(),
            "threshold_rule": f"inner-OOF normals {(1 - far):.2f} quantile (inner CV-{INNER})", "far_target": far,
            "labels": "v2 (Nov draft labels)", "evaluate_sha256": E.evaluate_sha256()}
    sc = AS.ArgusScorer.from_fitted(out.model, bases, thr, meta)
    pdir = r.out / "package"
    files = sc.save(pdir / name)
    (pdir / f"{name}.units.json").write_text(json.dumps({"train_units": train_units, "held_out_units": held_units},
                                                         indent=0), encoding="utf-8")
    # parity on the held-out fold: package (cache rows path) vs fit path
    diffs = []
    for j, row in enumerate(b[:200]):
        o = np.arange(r.data.off[row], r.data.off[row + 1])
        u = {L: r.data.U[L][o].astype(np.float32) for L in cfg["layers"]}
        diffs.append(abs(sc.score_cache_rows(u, list(r.data.obs_kind[o])) - out.score[j]))
    log.check("package_cache_path_parity_le_1e-5", max(diffs) <= 1e-5, {"max_abs": float(max(diffs))})
    log(f"[package] {files} threshold {thr:.4f}")
    return {"files": [str(f) for f in files], "threshold": thr, "parity_max_abs": float(max(diffs))}


def stage_k11(view: Path, cache: Path, log: RunLog, layers=(20, 16), seeds=SEEDS3, tol=0.01):
    """K11 cache fidelity (prereg §6, run-invalidating): the T4-1b recipe (standardise -> PCA 10 -> same-rollout
    pair logistic C 0.01) on the pre_action rows, PCA-512 cache input vs the original pooled ``L{L}_pre``."""
    from experiments.risk_loop.argus_loop import iter01_common as C1
    from experiments.risk_loop.argus_loop import iter04_models as M4
    from experiments.risk_loop.argus_loop import obs_cache as OC
    data, rows, _ = C1.headline_data(view)
    c = OC.ObsCache(cache)
    g = c.gather(rows.row_id, rows.row_id)
    ctx = {"trajectory": rows.trajectory_id.astype(str), "source": rows.source.astype(str),
           "log_prefix_length": np.log(np.clip(rows.prefix_length, 1.0, None))}
    res = {}
    for L in layers:
        X_raw = np.asarray(C1.features(data, rows, L, "pre"), np.float32)
        X_512 = np.asarray(c.layer(L)[g.obs_ids[g.pre_local]], np.float32)
        v = {}
        for tag, X in (("raw2880", X_raw), ("cache512", X_512)):
            cv = E.run_cv(M4.same_traj_pairwise(X, ctx, k=10, C=0.01), None, rows, seeds)
            v[tag] = E.metrics(cv, rows, bootstrap=0, baselines=False)["within_tool"]["value"]
        v["abs_diff"] = abs(v["raw2880"] - v["cache512"])
        res[f"L{L}"] = v
        log.check(f"K11_cache_fidelity_L{L}", v["abs_diff"] <= tol, v)
    return res


def stage_report(r_out: Path):
    out = {}
    for n in ("screen", "nested", "confirm", "shuffles", "reselect", "controls"):
        p = r_out / f"{n}.json"
        if p.is_file():
            out[n] = json.loads(p.read_text(encoding="utf-8"))
    summ = {}
    if "nested" in out:
        summ["nested_within_tool (OFFICIAL)"] = out["nested"]["metrics"]
    if "screen" in out:
        b = out["screen"]["best"]
        summ["screen_best (OPTIMISTIC)"] = {"combo": b["combo"], "beta": b["beta"], "within_tool": b["within_tool"],
                                           "luck_corrected": out["screen"].get("luck_corrected_best")}
    if "shuffles" in out and "nested" in out:
        m = out["shuffles"].get(out["nested"]["modal"]["config_id"])
        if m:
            v = out["nested"]["metrics"]["within_tool"]
            ref = max(m["ref_3b"], out.get("reselect", {}).get("within_tool_mean", 0) or 0)
            summ["3b_margin_vs_max(0.596, own, reselect)"] = v - ref
    tc = r_out / "try_counter.json"
    if tc.is_file():
        summ["tries"] = json.loads(tc.read_text(encoding="utf-8"))
        summ["tries"].pop("combos", None)
    (r_out / "summary.json").write_text(json.dumps(E.to_jsonable(summ), indent=1), encoding="utf-8")
    print(json.dumps(E.to_jsonable(summ), indent=1))
    return summ


# ---------------------------------------------------------------------------------------------- timing (synthetic)

def stage_timing(scratch: Path, workers=9, threads=2, n_fits=72):
    from experiments.risk_loop.argus_loop import obs_synth as S
    root = Path(scratch)
    if not (root / "obs_cache" / "obs_L20.npy").is_file():
        S.make_timing_cache(root)
    r = Runner(root, root / "obs_cache", root / "phase3_timing", workers=workers, threads=threads)
    r.chunk = 2
    grid = OM.prereg_grid()
    picks = [grid[i] for i in np.linspace(0, len(grid) - 1, n_fits // 4).astype(int)]  # spread over all combos
    specs = r.outer_specs(0)[:4]
    t0 = time.time()
    stats = r.precompute(picks, specs, "timing")
    wall = time.time() - t0
    per = wall / max(stats.get("fits", 1), 1)
    return {"fits": stats.get("fits"), "wall_s": wall, "wall_per_fit_s": per, "cpu_s_per_fit": stats.get("sec", 0) /
            max(stats.get("fits", 1), 1), "workers": workers, "threads": threads}


def fit_budget(n_confirm_combos=5) -> dict:
    """Number of model fits per stage (single-init-seed fits; confirm fits carry 3 replicas)."""
    g = 192
    return {"screen": g * 3 * 5, "nested_inner": g * 3 * 5 * INNER,
            "confirm(3 replicas each)": n_confirm_combos * 3 * 10 * 5 * (INNER + 1),
            "shuffles_fixed(per config)": 2 * 20 * 5, "reselect": 5 * 5 * g * (INNER + 1),
            "controls_obs": 3 * 10 * 5}


# ---------------------------------------------------------------------------------------------- cli

def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("stage", choices=["k11", "screen", "nested", "confirm", "shuffles", "reselect", "controls",
                                      "package", "report", "timing", "all"])
    ap.add_argument("--workers", type=int, default=MAX_WORKERS)
    ap.add_argument("--threads", type=int, default=2)
    ap.add_argument("--view", default=str(VIEW))
    ap.add_argument("--cache", default=str(CACHE))
    ap.add_argument("--out", default=str(OUT))
    ap.add_argument("--seeds", default=None, help="comma list of fold seeds (default per stage)")
    ap.add_argument("--config", default=None, help="config_id for shuffles/package (default: nested modal)")
    ap.add_argument("--init-seeds", default="0,1,2")
    ap.add_argument("--scratch", default=None)
    ap.add_argument("--no-strict-files", action="store_true", help="skip label/prereg file checks (synthetic only)")
    a = ap.parse_args(argv)
    if a.stage == "timing":
        print(json.dumps(stage_timing(Path(a.scratch), a.workers, a.threads), indent=1))
        print(json.dumps(fit_budget(), indent=1))
        return
    if a.stage == "report":
        stage_report(Path(a.out))
        return
    log = RunLog(Path(a.out), a.stage)
    if a.stage == "k11":
        log.check("1_evaluate_sha", E.evaluate_sha256() == EVAL_SHA, E.evaluate_sha256())
        res = stage_k11(Path(a.view), Path(a.cache), log)
        (Path(a.out) / "k11.json").write_text(json.dumps(E.to_jsonable(res), indent=1), encoding="utf-8")
        log.finish()
        return
    r = Runner(a.view, a.cache, a.out, workers=a.workers, threads=a.threads, log=log)
    start_checks(log, r, not a.no_strict_files)
    seeds = tuple(int(s) for s in a.seeds.split(",")) if a.seeds else None
    grid_by_id = {OM.config_id(c): c for c in OM.prereg_grid()}

    def pick_cfg():
        if a.config:
            return grid_by_id[a.config]
        n = json.loads((Path(a.out) / "nested.json").read_text(encoding="utf-8"))
        return grid_by_id[n["modal"]["config_id"]]
    st = a.stage
    if st in ("screen", "all"):
        stage_screen(r, log, seeds or SEEDS3)
    if st in ("nested", "all"):
        stage_nested(r, log, seeds or SEEDS3)
    if st in ("shuffles", "all"):
        stage_shuffles(r, log, pick_cfg())
    if st in ("reselect", "all"):
        stage_reselect(r, log)
    if st in ("confirm", "all"):
        init = tuple(int(x) for x in a.init_seeds.split(","))
        ov = Path(a.out) / "confirm_init_seeds.override"
        if ov.is_file():  # addendum-1 #12 step 1 (time-based, decided before any confirm result)
            init = tuple(int(x) for x in ov.read_text(encoding="utf-8").split()[0].split(","))
            log(f"[confirm] addendum-1 #12 step 1 applied: init seeds {init} ({ov.read_text(encoding='utf-8').strip()})")
        log.check("10c_confirm_init_seeds_logged", True, {"init_seeds": init})
        stage_confirm(r, log, seeds or SEEDS10, init)
    if st in ("controls", "all"):
        stage_controls(r, log, seeds or SEEDS10)
    if st == "package":
        stage_package(r, log, pick_cfg())
    if r.misses:
        log("store misses (computed inline):", dict(r.misses))
    ok = end_checks(log, not a.no_strict_files)
    if st == "all":
        stage_report(Path(a.out))
    if not ok:
        sys.exit(3)


if __name__ == "__main__":
    main()

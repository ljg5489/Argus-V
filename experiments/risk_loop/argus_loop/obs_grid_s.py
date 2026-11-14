"""Phase-3 cycle-1 S-stage runner (DRAFT prereg reports/risk-loop/argus-v1/loop/iter-13/prereg-S-draft.md §5).

Reuses the cycle-1 evaluation procedure of obs_grid.py (frozen evaluate.py run_cv / nested_cv inner CV-4 /
metrics / shuffle_test on top of a resumable fit store, same monitor checks, same RAM guard, same try counter and
luck-correction rule), per structure. obs_grid.py / obs_models.py are imported, never modified: the cycle-1 run
that is still going imports them.

Store: ``phase3/s1/fits/<config_id>/<key>.npz`` (S config ids carry the structure name, so they never collide
with cycle-1 fits). Per-structure results: ``phase3/s1/<struct>/<stage>.json``. Re-running a stage resumes from
the store; ``--skip-done`` skips a (structure, stage) whose JSON exists.

  py -3.11 experiments/risk_loop/argus_loop/obs_grid_s.py <stage> [--structures S-0,S-A] [--dry-run] [...]
Structure order (= run order for ``all``): S-0, S-A, S-F, S-B, S-C, S-D, S-E (obs_models_s.STRUCT_ORDER).
Stages (per structure, in this order for ``all``):
  screen    12 settings (4 toggle states x 3 tuning values: beta {1,10,100}; S-0 C {0.01,0.1,1}; S-F weight decay
            {1e-3,1e-2,1e-1}) x fold seeds {0,1,2} x 1 init seed -> OPTIMISTIC table
  nested    per fold seed {0,1,2}: inner family CV-4 picks one of the 12 per outer fold -> OFFICIAL value
  shuffles  (a) source, (b) source x family, 20 each, nested modal setting fixed, fold seed 0
  reselect  (b) x5 redoing the 12-way selection on permuted labels (fold seed 0); reduction (2) defers it for
            nested < 0.721 (stage reselect_best then runs it for the best nested structure)
  confirm   nested modal state (ties -> prereg order) + all-off state (dropped by reduction (1)), fold seeds 0-9,
            tuning value by inner CV-4
  controls  C-pre of the structure (same structure, pre_action row only at scoring), tuning value by the same inner
            CV-4 over the same grid (decision 3), fold seeds 0-2 (= the nested seeds, K1 is paired)
  common    (once) M0, T7-a (K5), R-only (K4), fold seeds 0-9 (not tries)
  report    per-structure nested / optimistic / luck-corrected; K1 vs own C-pre, K2, K3 (relative + fixed), K4, K5
  success   only for nested >= 0.90 (decision 6): confirm with init seeds 0,1,2 (K10), full reselect, label-v1 nested
Every stage result carries the sha of the code it ran with. Start checks (prereg-S sha frozen before the first fit,
label files, cache, K11 gate record) must all pass before any fit; any failed check -> exit code 3.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys
import time
from collections import Counter
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402
from experiments.risk_loop.argus_loop import obs_grid as G  # noqa: E402
from experiments.risk_loop.argus_loop import obs_models as OM  # noqa: E402
from experiments.risk_loop.argus_loop import obs_models_s as OMS  # noqa: E402

OUT_S = G.OUT / "s1"
PREREG_S = G.LOOP / "iter-13" / "prereg-S.md"
PREREG_S_SHA = G.LOOP / "iter-13" / "prereg-S.sha256"
TRY_BASE_S, TRY_BASE_S_CONSERVATIVE = 132, 134    # cumulative after cycle-1 C stage (phase3/try_counter.json)
GB_PER_WORKER = 0.65          # obs_grid's per-worker estimate (observation data only)
GB_PER_WORKER_T7A = 1.1       # + pooled L23 max / L16 pre (2 x ~107 MB) and robust-PCA transients (estimate)
STAGES = ("screen", "nested", "shuffles", "reselect", "confirm", "controls")
K11_TOL = 0.01
K11_FILE = G.LOOP / "iter-13" / "k11_L16_L23.json"   # decision 1: the layer-16/23 recheck file
V1_VIEW = G.ART / "features"   # label-v1 view (decision 6c; iter12_remeasure VIEWS["v1"])
SUCCESS_BAR = 0.90
RESELECT_KEEP = 0.721   # reduction (2): reselect kept for nested >= T7-a 0.721


# ---------------------------------------------------------------------------------------------- workers

_WORKER_S = {}


def _worker_objs(env: dict):
    key = json.dumps(env, sort_keys=True, default=str)
    if _WORKER_S.get("key") != key:
        _WORKER_S.clear()
        _WORKER_S["key"] = key
        _WORKER_S["data"] = OM.ObsData.load(env["view"], env["cache"], tuple(env["layers"]))
        _WORKER_S["base"] = _load_base(env["view"], _WORKER_S["data"]) if env.get("t7a") else None
    return _WORKER_S["data"], _WORKER_S["base"]


def _load_base(view, data: OM.ObsData) -> OMS.T7aBase:
    b = OMS.T7aBase.load(view)
    if not np.array_equal(b.rows.row_id, data.head.row_id):
        raise RuntimeError("T7-a pooled rows are not the observation-model headline rows")
    return b


def leak_audit_s(data, out, pos_train, pos_test, forbidden, cfg) -> dict:
    a = G.leak_audit(data, out, pos_train, pos_test, forbidden, cfg)
    if cfg.get("offset", "none") != "none" and not out.audit.get("constant"):
        ok = bool(out.audit.get("offset_crossfit_ok")) and out.audit.get("offset_rows_hash") == OM.h_arr(
            np.asarray(pos_train, np.int64))
        a["offset_ok"] = ok
        a["all_ok"] = bool(a["all_ok"] and ok)
    return a


def _run_job_s(env: dict, cfgs: list, specs: list, data=None, base=None) -> dict:
    import torch
    torch.set_num_threads(int(env["threads"]))
    if data is None:
        data, base = _worker_objs(env)
    out_dir = Path(env["out"]) / "fits"
    done = fails = 0
    t0 = time.time()
    for (pa, ya, pb, forb) in specs:
        key = G.fit_key(pa, ya, pb)
        for cfg in cfgs:
            p = out_dir / OM.config_id(cfg) / f"{key}.npz"
            if p.is_file():
                continue
            out = OMS.fit_s(data, cfg, pa, ya, pb, base=base)
            aud = leak_audit_s(data, out, pa, pb, forb, cfg)
            fails += int(not aud["all_ok"])
            G.save_fit(p, out, aud)
            done += 1
    return {"fits": done, "audit_fail": fails, "sec": time.time() - t0, "pid": os.getpid()}


# ---------------------------------------------------------------------------------------------- runner

def layers_for(structures) -> tuple:
    return tuple(sorted({L for s in structures for L in OMS.make_config_s(s)["layers"]} | {20}))


class SRunner(G.Runner):
    """obs_grid.Runner with S-config fits (fit_s), the T7-a base for S-A and a per-worker RAM estimate."""

    def __init__(self, view=G.VIEW, cache=G.CACHE, out=OUT_S, structures=OMS.STRUCT_ORDER, workers=G.MAX_WORKERS,
                 threads=2, log=print):
        super().__init__(view, cache, out, layers_for(structures), workers, threads, log)
        self._setup(structures)
        fg = G.free_gb()
        if fg < G.MIN_FREE_GB + self.gb_per_worker * self.workers:
            self.workers = max(2, min(self.workers, int((fg - G.MIN_FREE_GB) / self.gb_per_worker)))

    def _setup(self, structures):
        self.need_t7a = any(OMS.STRUCTS[s].get("offset", "none") != "none" for s in structures)
        self.gb_per_worker = GB_PER_WORKER_T7A if self.need_t7a else GB_PER_WORKER
        self.env["t7a"] = self.need_t7a
        self._base = None

    @classmethod
    def from_parts(cls, data, view, cache, out, structures, threads=1, base=None, log=lambda *a: None):
        """Test / in-process constructor (no data loading, one worker)."""
        r = cls.__new__(cls)
        r.view, r.cache, r.out, r.threads, r.workers, r.max_workers = Path(view), Path(cache), Path(out), threads, 1, 1
        r.layers = layers_for(structures)
        r.log, r.data, r.rows = log, data, data.head
        r.env = {"view": str(view), "cache": str(cache), "layers": list(r.layers), "threads": threads, "out": str(out)}
        r.misses, r.lookups = Counter(), Counter()
        r.out.mkdir(parents=True, exist_ok=True)
        r._setup(structures)
        r._base = base
        return r

    @property
    def base(self):
        if self._base is None and self.need_t7a:
            self._base = _load_base(self.view, self.data)
        return self._base

    def base_or_load(self):
        """T7-a base even when no S-A structure is in this run (common controls)."""
        if self._base is None:
            self._base = _load_base(self.view, self.data)
        return self._base

    def precompute(self, cfgs, specs, tag=""):
        """obs_grid.Runner.precompute with the S job function and this runner's per-worker RAM estimate."""
        todo = []
        for s in specs:
            key = G.fit_key(s[0], s[1], s[2])
            miss = [c for c in cfgs if not (self.out / "fits" / OM.config_id(c) / f"{key}.npz").is_file()]
            if miss:
                todo.append((s, miss))
        n_fits = sum(len(m) for _, m in todo)
        self.log(f"[precompute {tag}] {len(specs)} specs x {len(cfgs)} configs: {n_fits} fits to run "
                 f"({self.workers} workers x {self.threads} threads)")
        if not n_fits:
            return {"fits": 0}
        jobs = []
        ch = int(getattr(self, "chunk", 16))  # >= 12 settings: one job = one spec -> one T7-a base per spec
        for s, miss in todo:
            for i in range(0, len(miss), ch):
                jobs.append((miss[i:i + ch], [s]))
        t0 = time.time()
        for v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
            os.environ[v] = str(self.threads)
        tot = Counter()
        gbw = self.gb_per_worker
        if self.workers <= 1:
            for c, s in jobs:
                tot.update({k: v for k, v in _run_job_s(self.env, c, s, self.data, self.base).items() if k != "pid"})
        else:
            from joblib import Parallel, delayed
            done, i = 0, 0
            while i < len(jobs):
                fg = G.free_gb()
                if fg < G.MIN_FREE_GB and self.workers > 2:
                    cut = max(1, int(math.ceil((G.MIN_FREE_GB - fg) / gbw)))
                    self.workers = max(2, self.workers - cut)
                    self.log(f"[precompute {tag}] free RAM {fg:.1f} GB < {G.MIN_FREE_GB} -> workers {self.workers}")
                elif fg > G.MIN_FREE_GB + 2 * gbw and self.workers < self.max_workers:
                    self.workers += 1
                    self.log(f"[precompute {tag}] free RAM {fg:.1f} GB -> workers {self.workers}")
                wave = max(self.workers * 4, 1)
                batch = jobs[i:i + wave]
                i += len(batch)
                for r in Parallel(n_jobs=self.workers, backend="loky", return_as="generator_unordered")(
                        delayed(_run_job_s)(self.env, c, s) for c, s in batch):
                    tot.update({k: v for k, v in r.items() if k != "pid"})
                    done += 1
                el = time.time() - t0
                self.log(f"[precompute {tag}] {done}/{len(jobs)} jobs, {tot['fits']} fits, {el / 60:.1f} min, "
                         f"eta {el / done * (len(jobs) - done) / 60:.1f} min, free RAM {G.free_gb():.1f} GB, "
                         f"workers {self.workers}")
        el = time.time() - t0
        self.log(f"[precompute {tag}] {tot['fits']} fits in {el / 60:.1f} min "
                 f"({el / max(tot['fits'], 1):.2f} s/fit wall, audit failures {tot['audit_fail']})")
        return dict(tot)

    def memo_fp(self, cfg, record=None):
        cid = OM.config_id(cfg)

        def fp(pos_train, y_train, pos_test):
            key = G.fit_key(pos_train, y_train, pos_test)
            p = self.out / "fits" / cid / f"{key}.npz"
            self.lookups[cid] += 1
            if not p.is_file():
                self.misses[cid] += 1
                out = OMS.fit_s(self.data, cfg, pos_train, y_train, pos_test, base=self.base, threads=self.threads)
                G.save_fit(p, out, leak_audit_s(self.data, out, pos_train, pos_test, None, cfg))
            r = G.load_fit(p)
            if record is not None:
                record[key] = r
            return r["score"]
        fp.cfg = cfg
        return fp


# ---------------------------------------------------------------------------------------------- checks

def start_checks_s(log: G.RunLog, r: SRunner, structures, strict_files=True):
    G.start_checks(log, r, strict_files)
    if strict_files:
        rec = PREREG_S_SHA.read_text(encoding="utf-8").split()[0] if PREREG_S_SHA.is_file() else None
        cur = G.sha256(PREREG_S) if PREREG_S.is_file() else None
        fits = r.out / "fits"
        first = min((p.stat().st_mtime for p in fits.rglob("*.npz")), default=None) if fits.is_dir() else None
        older = first is None or (PREREG_S.is_file() and PREREG_S.stat().st_mtime <= first)
        log.check("8s_prereg_S_frozen_before_results", rec is not None and rec == cur and older,
                  {"recorded": rec, "current": cur, "first_fit_mtime": first})
    for s in structures:
        c = OMS.make_config_s(s)
        log.check(f"S_param_count_{s}", OMS.n_params(c) == OMS.PARAMS_EXPECTED[s],
                  {"counted": OMS.n_params(c), "draft": OMS.PARAMS_EXPECTED[s]})


def k11_layer_gate(layer: int, path=K11_FILE, tol=K11_TOL) -> dict:
    """prereg-S §4 + orchestrator decision 2 (one-sided K11): a layer's observation cache may be used only if, in
    ``iter-13/k11_L16_L23.json`` on the OFFICIAL rows (k11_cache_check rows), every probe gives cache - orig >=
    -tol (a cache that scores HIGHER is not information loss). Missing layer / file -> fail (never silent)."""
    res = {"file": str(path), "layer": int(layer), "tol": tol, "official_rows": None, "pass": False}
    p = Path(path)
    if not p.is_file():
        res["reason"] = "file missing"
        return res
    d = json.loads(p.read_text(encoding="utf-8")).get("layers", {}).get(str(int(layer)))
    if not d:
        res["reason"] = f"layer {layer} not in file"
        return res
    vals = {k.split("|", 1)[1]: v["diff_cache_minus_orig"] for k, v in d.items()
            if k.startswith("official|") and isinstance(v, dict)}
    res["official_rows"] = vals
    res["file_verdict_official_procedure"] = d.get("verdict_official_procedure")
    res["worst"] = min(vals.values()) if vals else None
    res["pass"] = bool(vals) and all(x is not None and x >= -tol for x in vals.values())
    return res


def k11_layer23_gate(path=K11_FILE, tol=K11_TOL) -> dict:
    return k11_layer_gate(23, path, tol)


def k11_structure_gate(struct: str, path=K11_FILE, tol=K11_TOL) -> dict:
    """All non-20 layers a structure reads must pass (layer 20: official PASS from cycle 1)."""
    layers = [L for L in OMS.make_config_s(struct)["layers"] if L != 20]
    gates = {L: k11_layer_gate(L, path, tol) for L in layers}
    return {"layers": gates, "pass": all(g["pass"] for g in gates.values())}


def code_shas() -> dict:
    """sha256 (16 hex) of the code a stage ran with (monitor SHOULD: cycle-1 code changed mid-run)."""
    here = Path(__file__).resolve().parent
    names = ("obs_grid_s.py", "obs_models_s.py", "obs_models_s0f.py", "obs_models.py", "obs_grid.py", "evaluate.py")
    return {n: G.sha256(here / n)[:16] for n in names if (here / n).is_file()}


# ---------------------------------------------------------------------------------------------- try counter

def bump_tries_s(out: Path, cfgs, stage: str) -> dict:
    p = out / "try_counter.json"
    d = json.loads(p.read_text(encoding="utf-8")) if p.is_file() else {
        "base": TRY_BASE_S, "base_conservative": TRY_BASE_S_CONSERVATIVE, "combos": {}}
    for c in cfgs:
        d["combos"].setdefault(OMS.combo_key_s(c), {"name": OMS.combo_name_s(c), "first_stage": stage,
                                                 "time": time.strftime("%F %T")})
    d["cycle_tries"] = len(d["combos"])
    d["cumulative"] = d["base"] + d["cycle_tries"]
    d["cumulative_conservative"] = d["base_conservative"] + d["cycle_tries"]
    p.write_text(json.dumps(d, indent=1, default=list), encoding="utf-8")
    return d


# ---------------------------------------------------------------------------------------------- stages

def _sdir(r, struct) -> Path:
    p = r.out / struct
    p.mkdir(parents=True, exist_ok=True)
    return p


def _write(r, struct, stage, res):
    if isinstance(res, dict):
        res.setdefault("code_sha", code_shas())
    (_sdir(r, struct) / f"{stage}.json").write_text(json.dumps(E.to_jsonable(res), indent=1), encoding="utf-8")


def _read(r, struct, stage):
    p = r.out / struct / f"{stage}.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.is_file() else None


def probe_tool_free_s(log, r: SRunner, cfg):
    data = r.data
    a, b = E.make_folds(r.rows, 5, 0)[0]
    y = r.rows.y
    s1 = OMS.fit_s(data, cfg, a, y[a], b, base=r.base, threads=r.threads).score
    saved = {k: getattr(data, k).copy() for k in ("tool", "source", "family", "traj", "status")}
    try:
        for k in saved:
            arr = getattr(data, k)
            arr[b] = arr[b][::-1]
        s2 = OMS.fit_s(data, cfg, a, y[a], b, base=r.base, threads=r.threads).score
    finally:
        for k, v in saved.items():
            setattr(data, k, v)
    log.check(f"4b_scores_invariant_to_scored_rows_metadata_{cfg['struct']}", bool(np.array_equal(s1, s2)),
              {"cfg": OMS.combo_name_s(cfg), "max_abs_diff": float(np.abs(s1 - s2).max())})


def stage_screen(r: SRunner, log, struct, states=OMS.STATES, seeds=G.SEEDS3, epochs=None):
    over = {} if epochs is None else {"epochs": epochs}
    grid = OMS.s_grid(struct, states, **over)
    log.check(f"10a_grid_order_{struct}", [OM.config_id(c) for c in grid] ==
              [OM.config_id(c) for c in OMS.s_grid(struct, states, **over)] and
              len(grid) == 3 * sum(OMS.supports_state(struct, x) for x in states),
              {"order": [OMS.combo_name_s(c) + f"|{OMS.tune_name(struct)}{OMS.tune_of(c)}" for c in grid]})
    log.check(f"10b_same_init_seeds_{struct}", len({c["init_seeds"] for c in grid}) == 1, grid[0]["init_seeds"])
    specs = [s for sd in seeds for s in r.outer_specs(sd)]
    r.precompute(grid, specs, f"{struct} screen")
    au = r.audits_ok(grid, specs)
    log.check(f"3_no_leak_screen_{struct}", au["n_bad"] == 0, au)
    table, cvs = [], {}
    for c in grid:
        cv = E.run_cv(r.memo_fp(c), None, r.rows, seeds)
        cvs[OM.config_id(c)] = cv
        m = E.metrics(cv, r.rows, bootstrap=0, baselines=False)
        table.append({"config_id": OM.config_id(c), "combo": OMS.combo_name_s(c),
                      "tune_name": OMS.tune_name(struct), "tune": OMS.tune_of(c),
                      **{k: v for k, v in G.compact(m).items() if k != "baselines"}})
    G.fold_hash_check(log, r, cvs)
    best = max(table, key=lambda t: t["within_tool"] or -1)
    res = {"stage": "screen", "struct": struct, "OPTIMISTIC": "selection outside CV", "seeds": list(seeds),
           "n_params": OMS.n_params(grid[0]), "table": table, "best": best, "misses": dict(r.misses),
           "tries": bump_tries_s(r.out, grid, f"{struct} screen")}
    res["luck_corrected_best"] = G.luck_correction(best["within_tool"], res["tries"]["cumulative"])
    _write(r, struct, "screen", res)
    log(f"[{struct} screen] best {best['combo']} {best['tune_name']} {best['tune']} "
        f"within-tool {best['within_tool']:.4f} (optimistic)")
    return res


def stage_nested(r: SRunner, log, struct, states=OMS.STATES, seeds=G.SEEDS3, epochs=None, probe=True):
    over = {} if epochs is None else {"epochs": epochs}
    grid = OMS.s_grid(struct, states, **over)
    specs = [s for sd in seeds for s in r.outer_specs(sd)] + [s for sd in seeds for s in r.inner_specs(sd)]
    r.precompute(grid, specs, f"{struct} nested")
    au = r.audits_ok(grid, specs)
    log.check(f"3_no_outer_rows_in_inner_selection_{struct}", au["n_bad"] == 0, au)
    if probe:
        probe_tool_free_s(log, r, grid[-1])
    cv = E.nested_cv(lambda g: r.memo_fp(g), grid, None, r.rows, seeds, 5, inner_splits=G.INNER)
    m = E.metrics(cv, r.rows)
    G.fold_hash_check(log, r, {"nested": cv})
    chosen = {s: [grid[i] for i in cv["selection"]["chosen"][str(s)]] for s in seeds}
    ex = G.extra_metrics(r, cv, lambda s, i: chosen[s][i])
    modal = grid[E._modal_choice(cv)]
    res = {"stage": "nested", "struct": struct, "OFFICIAL": "nested value = the honest number of this structure",
           "metrics": G.compact(m), "metrics_full": m, "extra": ex, "evaluate_sha256": E.evaluate_sha256(),
           "chosen": {str(s): [{"combo": OMS.combo_name_s(c), "tune": OMS.tune_of(c), "config_id": OM.config_id(c)}
                               for c in v] for s, v in chosen.items()},
           "state_counts": dict(Counter(OMS.state_of(c) for v in chosen.values() for c in v).most_common()),
           "modal": {"state": OMS.state_of(modal), "tune": OMS.tune_of(modal), "config_id": OM.config_id(modal),
                     "tie_rule": "most chosen; ties -> first in prereg grid order (evaluate._modal_choice)"},
           "oof": {str(s): cv["oof"][str(s)] for s in seeds}, "misses": dict(r.misses)}
    _write(r, struct, "nested", res)
    log(f"[{struct} nested] within-tool {m['within_tool']['value']:.4f} CI {m['within_tool']['ci95']} "
        f"modal {res['modal']}")
    return res


def _modal_cfg(r, struct, states, epochs=None):
    n = _read(r, struct, "nested")
    if n is None:
        raise FileNotFoundError(f"{struct}: run the nested stage first")
    over = {} if epochs is None else {"epochs": epochs}
    by_id = {OM.config_id(c): c for c in OMS.s_grid(struct, states, **over)}
    return by_id[n["modal"]["config_id"]]


def stage_confirm(r: SRunner, log, struct, states=OMS.STATES, seeds=G.SEEDS10, init=(0,), drop_off=False,
                  epochs=None, name_out="confirm"):
    modal = _modal_cfg(r, struct, states, epochs)
    names = [OMS.state_of(modal)] + ([] if drop_off or OMS.state_of(modal) == "base" else ["base"])
    over = {"init_seeds": tuple(init)}
    if epochs is not None:
        over["epochs"] = epochs
    out = {"stage": "confirm", "struct": struct, "seeds": list(seeds), "init_seeds": list(init), "states": {}}
    for name in names:
        grid = [OMS.make_config_s(struct, OMS.bits_of_state(name), b, **over) for b in OMS.tune_grid(struct)]
        specs = [s for sd in seeds for s in r.outer_specs(sd)] + [s for sd in seeds for s in r.inner_specs(sd)]
        r.precompute(grid, specs, f"{struct} confirm {name}")
        au = r.audits_ok(grid, specs)
        log.check(f"3_no_leak_confirm_{struct}_{name}", au["n_bad"] == 0, au)
        cv = E.nested_cv(lambda g: r.memo_fp(g), grid, None, r.rows, seeds, 5, inner_splits=G.INNER)
        G.fold_hash_check(log, r, {name: cv})
        m = E.metrics(cv, r.rows)
        ex = G.extra_metrics(r, cv, lambda s, i: grid[cv["selection"]["chosen"][str(s)][i]])
        k10 = ex["mean"]["K10_init_rank_corr_median"]
        out["states"][name] = {"metrics": G.compact(m), "extra": ex, "tune_chosen": dict(Counter(
            OMS.tune_grid(struct)[i] for v in cv["selection"]["chosen"].values() for i in v)),
            "K10_init_rank_corr_median": k10,
            "K10_flag_unstable": (k10 is not None and k10 < 0.8),
            "K10_measurable": len(init) > 1}
        log(f"[{struct} confirm] {name}: within-tool {m['within_tool']['value']:.4f} ({len(seeds)} seeds)")
    out["drop_off_arm"] = bool(drop_off)
    _write(r, struct, name_out, out)
    return out


def stage_shuffles(r: SRunner, log, struct, states=OMS.STATES, n=20, seed=0, epochs=None):
    cfg = _modal_cfg(r, struct, states, epochs)
    res = {"struct": struct, "config_id": OM.config_id(cfg), "combo": OMS.combo_name_s(cfg), "tune": OMS.tune_of(cfg)}
    for tag, within in (("a", ("source",)), ("b", ("source", "family"))):
        c = OMS.derive(cfg, aux_null_within=within)
        labs = r.shuffled_train_labels(seed, n, within)
        folds = E.make_folds(r.rows, 5, seed)
        specs = [(a, labs[j][i], b, None) for j in range(n) for i, (a, b) in enumerate(folds)]
        r.precompute([c], specs, f"{struct} shuffle {tag}")
        au = r.audits_ok([c], specs)
        log.check(f"3_no_leak_shuffle_{struct}_{tag}", au["n_bad"] == 0, au)
        st = E.shuffle_test(r.memo_fp(c), r.rows, n, seed=seed, within=within, n_jobs=1)
        res[tag] = {k: st[k] for k in ("within_tool_mean", "within_tool_sd", "within_tool_se", "within_tool",
                                       "pass", "within_tool_by_source_mean")}
        log(f"[{struct} shuffle {tag}] mean {st['within_tool_mean']:.4f} (n={n})")
    res["K9_shuffle_a_in_0.45_0.55"] = bool(abs(res["a"]["within_tool_mean"] - 0.5) <= 0.05)
    res["ref_3b"] = max(G.REF_B_V2, res["b"]["within_tool_mean"])
    _write(r, struct, "shuffles", res)
    return res


def stage_reselect(r: SRunner, log, struct, states=OMS.STATES, n=5, seed=0, epochs=None, name_out="reselect"):
    within = ("source", "family")
    over = {} if epochs is None else {"epochs": epochs}
    grid = [OMS.derive(c, aux_null_within=within) for c in OMS.s_grid(struct, states, **over)]
    labs = r.shuffled_train_labels(seed, n, within)
    specs = []
    for j in range(n):
        specs += r.inner_specs(seed, y_override=labs[j], with_refit=True)
    r.precompute(grid, specs, f"{struct} reselect")
    au = r.audits_ok(grid, specs)
    log.check(f"3_no_leak_reselect_{struct}", au["n_bad"] == 0, au)
    nfp = OM.NestedFP(lambda g: r.memo_fp(g), grid, r.rows, seed, G.INNER)
    st = E.shuffle_test(nfp, r.rows, n, seed=seed, within=within, n_jobs=1)
    res = {k: st[k] for k in ("within_tool_mean", "within_tool_sd", "within_tool_se", "within_tool")}
    res["LIMITED"] = "fold seed 0 only, n=5 (as addendum-1 #10)"
    res["chosen"] = [OMS.combo_name_s(grid[i]) + f"|{OMS.tune_name(struct)}{OMS.tune_of(grid[i])}" for i in nfp.chosen]
    _write(r, struct, name_out, res)
    log(f"[{struct} reselect] mean {st['within_tool_mean']:.4f} (n={n})")
    return res


def stage_controls(r: SRunner, log, struct, seeds=G.SEEDS3, epochs=None):
    """C-pre (K1 / K3 control): the same structure, toggles off, only the pre_action row read at scoring time.
    Its tuning value is chosen by the SAME inner CV-4 nested selection over the SAME grid as the main model
    (orchestrator decision 3), on the main model's fold seeds (K1 is a paired comparison on those seeds)."""
    over = {} if epochs is None else {"epochs": epochs}
    grid = OMS.cpre_grid(struct, **over)
    specs = [s for sd in seeds for s in r.outer_specs(sd)] + [s for sd in seeds for s in r.inner_specs(sd)]
    r.precompute(grid, specs, f"{struct} controls")
    au = r.audits_ok(grid, specs)
    log.check(f"3_no_leak_controls_{struct}_C-pre", au["n_bad"] == 0, au)
    cv = E.nested_cv(lambda g: r.memo_fp(g), grid, None, r.rows, seeds, 5, inner_splits=G.INNER)
    G.fold_hash_check(log, r, {"C-pre": cv})
    chosen = cv["selection"]["chosen"]
    m = E.metrics(cv, r.rows)
    res = {"stage": "controls", "struct": struct, "seeds": list(seeds),
           "C-pre": {"config_ids": [OM.config_id(c) for c in grid], "tune_name": OMS.tune_name(struct),
                     "tune_grid": list(OMS.tune_grid(struct)), "tune_selection": "inner CV-4 (decision 3)",
                     "tune_chosen": dict(Counter(OMS.tune_of(grid[i]) for v in chosen.values() for i in v)),
                     "n_params": OMS.n_params(grid[0]), "metrics": G.compact(m),
                     "extra": G.extra_metrics(r, cv, lambda s, i: grid[chosen[str(s)][i]]),
                     "oof": {str(s): cv["oof"][str(s)] for s in seeds}}}
    log(f"[{struct} controls] C-pre: {m['within_tool']['value']:.4f} (tune by inner CV)")
    _write(r, struct, "controls", res)
    return res


def stage_common(r: SRunner, log, seeds=G.SEEDS10, epochs=None, pooled=True):
    """M0 (fixed M0 filter, layer 20) and the pooled-feature models T7-a (K5) and R-only (K4): not tries."""
    over = {} if epochs is None else {"epochs": epochs}
    m0 = OMS.make_config_s("M0", (0,) * 6, 1.0, **over)
    specs = [s for sd in seeds for s in r.outer_specs(sd)]
    r.precompute([m0], specs, "common M0")
    res, cvs = {}, {}
    cv = E.run_cv(r.memo_fp(m0), None, r.rows, seeds)
    cvs["M0"] = cv
    res["M0"] = {"metrics": G.compact(E.metrics(cv, r.rows)), "oof": {str(s): cv["oof"][str(s)] for s in seeds}}
    if pooled:
        fps = {"T7-a": lambda pa, ya, pb: r.base_or_load().test_scores(pa, ya, pb)}
        if getattr(r, "ronly", True):
            fps["R-only"] = G.pooled_control_fps(r)["R-only"]
        for name, fp in fps.items():
            cv = E.run_cv(fp, None, r.rows, seeds)
            cvs[name] = cv
            res[name] = {"metrics": G.compact(E.metrics(cv, r.rows)), "oof": {str(s): cv["oof"][str(s)] for s in seeds}}
            log(f"[common] {name}: {res[name]['metrics']['within_tool']:.4f}")
    G.fold_hash_check(log, r, cvs)
    res["code_sha"] = code_shas()
    (r.out / "common.json").write_text(json.dumps(E.to_jsonable(res), indent=1), encoding="utf-8")
    return res


# ---------------------------------------------------------------------------------------------- K1 + report

def paired_family_bootstrap(oofs_a, oofs_b, rows: E.Rows, reps=E.BOOTSTRAP_REPS, seed=E.BOOTSTRAP_SEED) -> dict:
    """Seed-mean within-tool AUROC difference (a - b) with families resampled with replacement, the same
    resampling as evaluate.family_bootstrap_ci, applied to both models on the same draws (K1)."""
    from experiments.risk_loop import harness as H
    A = [np.asarray(o, np.float64) for o in oofs_a]
    B = [np.asarray(o, np.float64) for o in oofs_b]
    y = rows.y
    _, fam = np.unique(rows.family.astype(str), return_inverse=True)
    _, tc = np.unique(E.headline_groups(rows).astype(str), return_inverse=True)
    members = [np.nonzero(fam == f)[0] for f in range(fam.max() + 1)]
    F = len(members)
    rng = np.random.default_rng(seed)
    vals = []
    for _ in range(int(reps)):
        idx = np.concatenate([members[f] for f in rng.integers(0, F, F)])
        idx = idx[np.argsort(tc[idx], kind="stable")]
        num_a, num_b, den = 0.0, 0.0, 0
        for seg in np.split(idx, np.flatnonzero(np.diff(tc[idx])) + 1):
            ys = y[seg]
            p = int(ys.sum())
            if p < E.MIN_POS or len(seg) - p < E.MIN_NEG:
                continue
            num_a += np.mean([H.auroc(o[seg], ys) for o in A]) * p
            num_b += np.mean([H.auroc(o[seg], ys) for o in B]) * p
            den += p
        if den:
            vals.append((num_a - num_b) / den)
    pa = E.within_tool_auroc(np.mean(A, 0), y, E.headline_groups(rows))["value"]
    va = E._mean([E.within_tool_auroc(o, y, E.headline_groups(rows))["value"] for o in A])
    vb = E._mean([E.within_tool_auroc(o, y, E.headline_groups(rows))["value"] for o in B])
    if not vals:
        return {"diff": None, "ci_low": None, "ci_high": None, "n_valid": 0}
    lo, hi = np.percentile(vals, [2.5, 97.5])
    return {"a": va, "b": vb, "diff": (va - vb) if va is not None and vb is not None else None, "a_mean_oof": pa,
            "ci_low": float(lo), "ci_high": float(hi), "n_valid": len(vals), "reps": int(reps),
            "K1_fail": bool(lo <= 0)}


def _within_traj_C(oofs, rows: E.Rows):
    from experiments.risk_loop.argus_loop import iter04_common as C4
    return E._mean([C4.within_traj_auroc(np.asarray(o, np.float64), rows.y, rows.trajectory_id)["value"]
                    for o in oofs])


def _within_tool(oofs, rows: E.Rows):
    return E._mean([E.within_tool_auroc(np.asarray(o, np.float64), rows.y, E.headline_groups(rows))["value"]
                    for o in oofs])


def k_rules(n, ctl, sh, common, rows: E.Rows, reps=E.BOOTSTRAP_REPS) -> dict:
    """Kill / adoption rules of prereg-S §7 with the orchestrator decisions 4, 5, 8 (numbers as in r4):
      K1  gain over the structure's OWN C-pre (S-A too): paired family bootstrap CI low <= 0 -> drop
      K2  >= 80 % of violation argmax points on pre_action / reasoning_end -> drop
      K3  |rho| > 0.3 AND |rho| - |rho(C-pre)| >= 0.10 -> drop (relative rule); fixed rule |rho| > 0.3 reported
      K4  within-trajectory C - max(own shuffle (b), 0.5) < 0.10, or C <= R-only's C -> drop
      K5  nested - T7-a < +0.03 -> not adopted (not a drop)"""
    e = {}
    seeds = sorted(n["oof"])
    mine = [n["oof"][k] for k in seeds]
    nv = n["metrics"]["within_tool"]
    mx = n["extra"]["mean"]
    cp = (ctl or {}).get("C-pre")
    if cp and all(k in cp["oof"] for k in seeds):
        k1 = paired_family_bootstrap(mine, [cp["oof"][k] for k in seeds], rows, reps)
        e["K1_vs_C-pre"] = {**k1, "rule": "drop if CI low <= 0 (decision 4: own C-pre, also for S-A)"}
    else:
        e["K1_vs_C-pre"] = {"K1_fail": None, "missing": "controls stage not run on the nested seeds"}
    frac = mx.get("K2_frac_pre_or_rend")
    e["K2"] = {"frac_pre_or_rend": frac, "chance": None, "fail": bool(frac is not None and frac >= 0.8),
               "rule": "drop if >= 80 % of violation argmax points are pre_action / reasoning_end"}
    rho = mx.get("K3_abs_spearman_n_obs32_cell_weighted")
    rho_c = cp["extra"]["mean"].get("K3_abs_spearman_n_obs32_cell_weighted") if cp else None
    e["K3"] = {"abs_rho": rho, "abs_rho_C-pre": rho_c,
               "rho_def": "per tool x source cell Spearman(score, n observation points on the 32 grid), |.|, "
                          "violation-weighted mean over cells (cycle-1 code)",
               "fail_fixed_rule_reported": bool(rho is not None and rho > 0.3),
               "fail": bool(rho is not None and rho > 0.3 and (rho_c is None or rho - rho_c >= 0.10)),
               "rule": "decision 5: drop if |rho| > 0.3 AND |rho| - |rho(C-pre)| >= 0.10"}
    C = mx.get("within_trajectory_C")
    sb = (sh or {}).get("b", {}).get("within_tool_mean")
    ro = (common or {}).get("R-only")
    C_r = _within_traj_C([ro["oof"][k] for k in seeds], rows) if ro and all(k in ro["oof"] for k in seeds) else None
    k4 = {"C": C, "shuffle_b_mean": sb, "C_R-only": C_r,
          "rule": "drop if C - max(shuffle (b), 0.5) < 0.10 or C <= C(R-only) (r4 K4; decision 8: gain over "
                  "R-only > 0)"}
    if C is not None and sb is not None and C_r is not None:
        k4.update({"C_minus_max_b_0.5": C - max(sb, 0.5), "gain_over_R-only": C - C_r,
                   "fail": bool(C - max(sb, 0.5) < 0.10 or C <= C_r)})
    else:
        k4["fail"] = None
    if ro and all(k in ro["oof"] for k in seeds):
        k4["within_tool_R-only"] = _within_tool([ro["oof"][k] for k in seeds], rows)
    e["K4"] = k4
    t7 = (common or {}).get("T7-a")
    if t7 and all(k in t7["oof"] for k in seeds):
        tv = _within_tool([t7["oof"][k] for k in seeds], rows)
        e["K5_vs_T7-a"] = {"T7-a_same_seeds": tv, "diff": nv - tv, "not_adopted": bool(nv - tv < 0.03),
                           "paired": paired_family_bootstrap(mine, [t7["oof"][k] for k in seeds], rows, reps),
                           "rule": "not adopted if nested - T7-a < +0.03 (decision 4: T7-a only enters K5)"}
    e["drop"] = bool(any(e[k].get("K1_fail" if k == "K1_vs_C-pre" else "fail") for k in
                         ("K1_vs_C-pre", "K2", "K3", "K4")))
    return e


def stage_report(r: SRunner, structures, reps=E.BOOTSTRAP_REPS):
    tc = r.out / "try_counter.json"
    tries = json.loads(tc.read_text(encoding="utf-8")) if tc.is_file() else {"cumulative": TRY_BASE_S}
    common = json.loads((r.out / "common.json").read_text(encoding="utf-8")) if (r.out / "common.json").is_file() \
        else {}
    summ = {"tries": {k: v for k, v in tries.items() if k != "combos"}, "structures": {}, "code_sha": code_shas()}
    for s in structures:
        e = {}
        n, sc = _read(r, s, "nested"), _read(r, s, "screen")
        ctl, sh, rs, cf = _read(r, s, "controls"), _read(r, s, "shuffles"), _read(r, s, "reselect"), \
            _read(r, s, "confirm")
        if sc:
            e["screen_best (OPTIMISTIC)"] = {k: sc["best"][k]
                                             for k in ("combo", "tune_name", "tune", "within_tool")}
            e["luck_corrected"] = G.luck_correction(sc["best"]["within_tool"], tries["cumulative"])
        if n:
            e["nested (OFFICIAL)"] = n["metrics"]
            e["modal"] = n["modal"]
            e.update(k_rules(n, ctl, sh, common, r.rows, reps))
            if sh:
                e["3b_margin"] = n["metrics"]["within_tool"] - max(sh["ref_3b"], (rs or {}).get("within_tool_mean") or 0)
                e["K9_shuffle_a_ok"] = sh["K9_shuffle_a_in_0.45_0.55"]
            e["reselect"] = "run" if rs else "not run (deferred by reduction (2) or pending)"
            e["meets_success_bar_0.90"] = bool(n["metrics"]["within_tool"] >= SUCCESS_BAR)
        if cf:
            e["confirm"] = {k: {"within_tool": v["metrics"]["within_tool"], "K10": v["K10_init_rank_corr_median"],
                                "K10_measurable": v["K10_measurable"]} for k, v in cf["states"].items()}
        summ["structures"][s] = e
    vals = {s: e["nested (OFFICIAL)"]["within_tool"] for s, e in summ["structures"].items() if "nested (OFFICIAL)" in e}
    if vals:
        b = max(vals, key=vals.get)
        summ["best_structure (OPTIMISTIC: chosen across structures, outside nested)"] = {
            "struct": b, "nested": vals[b], "luck_corrected": G.luck_correction(vals[b], tries["cumulative"])}
    (r.out / "summary.json").write_text(json.dumps(E.to_jsonable(summ), indent=1), encoding="utf-8")
    return summ


# ---------------------------------------------------------------------------------------------- success path

def stage_success(r: SRunner, log, struct, states=OMS.STATES, epochs=None, v1_view=V1_VIEW, v1_runner=None):
    """Decision 6: only for a structure whose nested value >= 0.90, BEFORE validation is opened:
    (a) confirm again with init seeds 0, 1, 2 (K10), (b) the 5 reselect shuffles, never skipped (fold seed 0),
    (c) the nested value again on the label-v1 view; (d) monitor review is manual. Writes success.json."""
    n = _read(r, struct, "nested")
    if n is None or n["metrics"]["within_tool"] is None or n["metrics"]["within_tool"] < SUCCESS_BAR:
        log(f"[{struct} success] not run: nested {None if n is None else n['metrics']['within_tool']} < {SUCCESS_BAR}")
        return None
    res = {"stage": "success", "struct": struct, "nested": n["metrics"]["within_tool"]}
    cf = stage_confirm(r, log, struct, states, init=(0, 1, 2), epochs=epochs, name_out="success_confirm_k10")
    res["a_K10"] = {k: {"K10": v["K10_init_rank_corr_median"], "unstable": v["K10_flag_unstable"]}
                    for k, v in cf["states"].items()}
    rs = stage_reselect(r, log, struct, states, n=5, epochs=epochs, name_out="success_reselect_full")
    res["b_reselect_full"] = {"within_tool_mean": rs["within_tool_mean"],
                              "margin": n["metrics"]["within_tool"] - max(G.REF_B_V2, rs["within_tool_mean"])}
    rv = v1_runner or SRunner(v1_view, r.cache, r.out / "label_v1", [struct], workers=r.workers, threads=r.threads,
                              log=log)
    nv1 = stage_nested(rv, log, struct, states, epochs=epochs)
    res["c_label_v1_nested"] = nv1["metrics"]
    res["d_monitor_review"] = "required before validation (manual)"
    res["all_automatic_pass"] = bool(all(not v["unstable"] for v in res["a_K10"].values())
                                     and res["b_reselect_full"]["margin"] > 0)
    _write(r, struct, "success", res)
    return res


# ---------------------------------------------------------------------------------------------- fit budget

def fit_budget_s(structures, states=OMS.STATES, confirm_states=2, init_same_as_grid=True, n_shuffle=20,
                 n_reselect=5, reduction2_structures=None):
    """Fits per structure and stage. 'nominal' = as the draft counts them; 'new' = store misses on a fresh store
    (outer fits of fold seeds 0-2 are shared by screen and nested, and -- with the same init seeds -- confirm
    fold seeds 0-2 are already in the store). Assumes the nested modal state != all-off (worst case).
    C-pre: 3 tuning values x fold seeds 0-2 x 5 outer x (4 inner + refit) (decision 3)."""
    per = {}
    for s in structures:
        S = 3 * sum(OMS.supports_state(s, x) for x in states)
        d = {"screen": S * 3 * 5, "nested_inner": S * 3 * 5 * G.INNER, "nested_outer(shared with screen)": S * 3 * 5,
             "confirm": confirm_states * 3 * 10 * 5 * (G.INNER + 1),
             "shuffles": 2 * n_shuffle * 5, "reselect": n_reselect * 5 * S * (G.INNER + 1),
             "controls(C-pre, inner CV)": 3 * 3 * 5 * (G.INNER + 1)}
        if reduction2_structures is not None and s not in reduction2_structures:
            d["reselect"] = 0
        new = dict(d)
        new["nested_outer(shared with screen)"] = 0
        if init_same_as_grid:
            new["confirm"] = confirm_states * 3 * 7 * 5 * (G.INNER + 1)
        d["total"] = sum(v for k, v in d.items())
        new["total"] = sum(v for k, v in new.items() if k != "total")
        c0 = OMS.make_config_s(s)
        per[s] = {"nominal": d, "new": new, "t7a_base_fits_per_fit_spec": 6 if OMS.STRUCTS[s].get("offset") else 0,
                  "settings": S, "tune": [OMS.tune_name(s), list(OMS.tune_grid(s))],
                  "n_params": OMS.n_params(c0),
                  "n_params_T4": OMS.n_params(OMS.make_config_s(s, OMS.bits_of_state("T4"))),
                  "n_params_C-pre": OMS.n_params(OMS.cpre_config(s)), "model": c0["model"]}
    common = 10 * 5
    return {"per_structure": per, "common(M0)": common,
            "total_nominal": sum(v["nominal"]["total"] for v in per.values()) + common,
            "total_new": sum(v["new"]["total"] for v in per.values()) + common}


# ---------------------------------------------------------------------------------------------- cli

def fail_fast(log: G.RunLog, strict_files: bool = True):
    """Monitor SHOULD (A6-5): a failed start check stops the program (exit code 3) BEFORE any fit."""
    failed = [k for k, v in log.checks.items() if not v["pass"]]
    if failed:
        log("START CHECKS FAILED -> no fits:", failed)
        G.end_checks(log, strict_files)
        sys.exit(3)


def _override(out: Path, name: str) -> str | None:
    p = Path(out) / name
    return p.read_text(encoding="utf-8").strip() if p.is_file() else None


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("stage", choices=list(STAGES) + ["common", "report", "all", "success", "reselect_best"])
    ap.add_argument("--structures", default=",".join(OMS.STRUCT_ORDER))
    ap.add_argument("--extra-state", default=None, help="5th toggle state, e.g. T1+T2+T4 (draft §3)")
    ap.add_argument("--confirm-drop-off", action="store_true",
                    help="reduction (1): no all-off confirm arm (also: <out>/reduction1.override)")
    ap.add_argument("--reselect-limited", action="store_true",
                    help="reduction (2): reselect only for nested >= 0.721 here; the best nested structure gets it "
                         "in stage reselect_best (also: <out>/reduction2.override)")
    ap.add_argument("--workers", type=int, default=G.MAX_WORKERS)
    ap.add_argument("--threads", type=int, default=2)
    ap.add_argument("--view", default=str(G.VIEW))
    ap.add_argument("--cache", default=str(G.CACHE))
    ap.add_argument("--out", default=str(OUT_S))
    ap.add_argument("--init-seeds", default="0", help="confirm init seeds (decision: 1 seed, reduction (0))")
    ap.add_argument("--skip-done", action="store_true")
    ap.add_argument("--dry-run", action="store_true", help="print the fit count and exit (loads nothing)")
    ap.add_argument("--no-strict-files", action="store_true", help="skip label/prereg/K11 file checks (synthetic only)")
    a = ap.parse_args(argv)
    structures = [s.strip() for s in a.structures.split(",") if s.strip()]
    bad = [s for s in structures if s not in OMS.STRUCTS]
    if bad:
        raise SystemExit(f"unknown structures {bad}")
    states = tuple(OMS.STATES) + ((a.extra_state,) if a.extra_state else ())
    if a.extra_state:
        OMS.bits_of_state(a.extra_state)
    init = tuple(int(x) for x in a.init_seeds.split(","))
    red1 = a.confirm_drop_off or _override(a.out, "reduction1.override") is not None
    red2 = a.reselect_limited or _override(a.out, "reduction2.override") is not None
    if a.dry_run:
        b = fit_budget_s(structures, states, 1 if red1 else 2, init == (0,))
        print(json.dumps(b, indent=1))
        print(f"DRY RUN: {len(structures)} structures x "
              f"{[b['per_structure'][s]['settings'] for s in structures]} settings: "
              f"{b['total_new']} new fits on a fresh store ({b['total_nominal']} counted as in the draft)")
        return b
    log = G.RunLog(Path(a.out), f"s_{a.stage}_{'-'.join(structures) if len(structures) < 3 else 'all'}")
    r = SRunner(a.view, a.cache, a.out, structures, workers=a.workers, threads=a.threads, log=log)
    if a.stage == "report":
        print(json.dumps(E.to_jsonable(stage_report(r, structures)), indent=1))
        return
    start_checks_s(log, r, structures, not a.no_strict_files)
    for s in list(structures):
        if any(L != 20 for L in OMS.make_config_s(s)["layers"]):
            g = k11_structure_gate(s)
            log.check(f"K11_gate_decision_recorded_{s}", True, {"included": g["pass"], **g})
            if not g["pass"] and not a.no_strict_files:
                log(f"{s} EXCLUDED: K11 cache check of its layers failed (decision 2; not a try)")
                structures.remove(s)
    log("code sha:", json.dumps(code_shas()))
    if red1:
        log("REDUCTION (1) active: confirm without the all-off arm", _override(a.out, "reduction1.override") or "")
    if red2:
        log("REDUCTION (2) active: reselect only nested >= 0.721 + best structure",
            _override(a.out, "reduction2.override") or "")
    fail_fast(log, not a.no_strict_files)

    def run_reselect(s):
        if red2:
            n = _read(r, s, "nested")
            v = None if n is None else n["metrics"]["within_tool"]
            if v is None or v < RESELECT_KEEP:
                log(f"[{s} reselect] deferred by reduction (2): nested {v} < {RESELECT_KEEP}")
                return None
        return stage_reselect(r, log, s, states)

    def reselect_best():
        vals = {s: _read(r, s, "nested")["metrics"]["within_tool"] for s in OMS.STRUCT_ORDER
                if _read(r, s, "nested") is not None}
        if not vals:
            return
        b = max(vals, key=vals.get)
        log(f"[reselect_best] best nested structure {b} ({vals[b]:.4f})")
        if _read(r, b, "reselect") is None:
            stage_reselect(r, log, b, states)

    todo = STAGES if a.stage == "all" else ((a.stage,) if a.stage in STAGES else ())
    fns = {"screen": lambda s: stage_screen(r, log, s, states),
           "nested": lambda s: stage_nested(r, log, s, states),
           "shuffles": lambda s: stage_shuffles(r, log, s, states),
           "reselect": run_reselect,
           "confirm": lambda s: stage_confirm(r, log, s, states, init=init, drop_off=red1),
           "controls": lambda s: stage_controls(r, log, s)}
    for s in structures:
        for st in todo:
            if a.skip_done and (r.out / s / f"{st}.json").is_file():
                log(f"[{s} {st}] done, skipped")
                continue
            fns[st](s)
            log(f"[{s} {st}] stage code sha {json.dumps(code_shas())}")
        if a.stage == "success":
            stage_success(r, log, s, states)
    if a.stage == "reselect_best":
        reselect_best()
    if a.stage in ("common", "all") and not (a.skip_done and (r.out / "common.json").is_file()):
        stage_common(r, log)
    if r.misses:
        log("store misses (computed inline):", dict(r.misses))
    ok = G.end_checks(log, not a.no_strict_files)
    if a.stage == "all":
        stage_report(r, structures)
    if not ok:
        sys.exit(3)


if __name__ == "__main__":
    main()

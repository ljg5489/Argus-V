"""Iteration 15: random forest as a 4th member of the T7-a ensemble ("2번 방식").

Pre-registration: reports/risk-loop/argus-v1/loop/iter-15/prereg-rf.md (sha in prereg-rf.sha256; checked before
any real-data fit -- missing / mismatching sha -> "PREREG_NOT_FROZEN", exit code 3, nothing is fitted).
Strictly additive: within_tool.py, iter06_models.py, iter07_models.py and evaluate.py are imported, never modified.

RF input: the fold-internal robust embeddings T7-a already uses (iter07 RobustStore: median / IQR scale, clip +-3,
PCA on training rows): L23:max first 32 dims + L16:pre first 10 dims = 42 features (pre-only control: L23:pre 32 +
L16:pre 10). RF trained with the T7-a member-1 row weights (source x class, informative-cell normals; via
sample_weight; class_weight None -- the weights already balance the classes). RF score = mean tree P(violation);
converted to a percentile among the IN-SAMPLE scores of the training rows, exactly the iter06 convention (the
out-of-bag alternative was compared on synthetic data and rejected; prereg §2.3). A per-fit tie monitor
(distinct percentiles / distinct raw scores of the scored rows) is reported, never used to switch.

Tries (169 -> 172; conservative 171 -> 174):
  R0  RF alone (comparison)
  R1  T7-a + RF, 4 members, equal weight 1/4 (main)
  R2  R1, but the RF trains on per-(tool x source)-cell centred features (training rows only; scoring and the
      percentile reference use the uncentred features). Non-linear -> approximation, not exact.
min_samples_leaf in {5, 10, 20} by the inner family CV-4 of evaluate.nested_cv (nested; per try).

  py -3.11 experiments/risk_loop/argus_loop/t7a_rf.py check
  py -3.11 experiments/risk_loop/argus_loop/t7a_rf.py run [--tries R0,R1,R2] [--threads 2]
  py -3.11 experiments/risk_loop/argus_loop/t7a_rf.py report
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time
from pathlib import Path

for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ.setdefault(_v, "2")

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402
from experiments.risk_loop.argus_loop import within_tool as W  # noqa: E402

ART = W.ART
OUT = ART / "phase3" / "rf"
LOOP = W.LOOP
IT15 = LOOP / "iter-15"
PREREG = IT15 / "prereg-rf.md"
PREREG_SHA = IT15 / "prereg-rf.sha256"
IT14_T7A_OOF = W.OUT / "oof_t7a_none.npy"     # iteration-14 T7-a seeds 0-2 (comparison only, read only)

TRIES = ("R0", "R1", "R2")
TRY_KO = {"R0": "RF 단독(R0)", "R1": "T7-a + RF 4개 평균(R1)", "R2": "R1 + RF 칸별 중심화(R2)"}
RF_WEIGHT = {"R0": 1.0, "R1": 0.25, "R2": 0.25}
RF_VARIANT = {"R0": "plain", "R1": "plain", "R2": "w1"}
MSL_GRID = (5, 10, 20)
RF_PARAMS = {"n_estimators": 500, "max_features": "sqrt", "class_weight": None, "random_state": 0, "n_jobs": 2,
             "bootstrap": True}
REF_MODE = "insample"                        # prereg §2.3 (decided on synthetic data before any real fit)
RF_REPS = (("L23:max", 32), ("L16:pre", 10))
PRE_REPS = {"L23:max": "L23:pre"}            # pre-action-only control (as within_tool.T7A_PRE_REPS)
SEEDS3 = W.SEEDS3
N_SHUF = W.N_SHUF
REF_B = W.REF_B
T7A_EXPECTED = 0.714
TRIES_BEFORE, TRIES_BEFORE_CONS = 169, 171
N_NEW = 3
CODE_FILES = ("experiments/risk_loop/argus_loop/t7a_rf.py", "experiments/risk_loop/argus_loop/within_tool.py",
              "experiments/risk_loop/argus_loop/iter06_models.py", "experiments/risk_loop/argus_loop/iter07_models.py",
              "experiments/risk_loop/argus_loop/models.py", "experiments/risk_loop/argus_loop/evaluate.py")
CACHE_LIMIT = 24

log = W.log
_check = W._check


# ============================================================================================== RF member

def rf_tag() -> str:
    return hashlib.sha1(json.dumps(RF_PARAMS, sort_keys=True).encode()).hexdigest()[:8]


def member1_weights(ya, src, cells) -> np.ndarray:
    """T7-a member 1 (iter06_models.pointwise_informative_fit) row weights: source x class, then normals of
    training cells with both classes up-weighted to half the normal weight."""
    from experiments.risk_loop.argus_loop import models as M
    base = M.sample_weights(ya, src, "source_class")
    return M.informative_group_weights(ya, cells, base)


def fit_rf(Xfit, ya, sw, msl, params=None):
    from sklearn.ensemble import RandomForestClassifier
    p = dict(RF_PARAMS if params is None else params)
    rf = RandomForestClassifier(min_samples_leaf=int(msl), **p)
    rf.fit(np.asarray(Xfit, np.float32), np.asarray(ya).astype(np.int64), sample_weight=sw)
    rf.set_params(n_jobs=1)        # sequential tree accumulation at predict time -> bitwise deterministic
    return rf


def _pos_col(rf) -> int:
    return int(np.nonzero(rf.classes_ == 1)[0][0])


def rf_proba(rf, X) -> np.ndarray:
    return rf.predict_proba(np.asarray(X, np.float32))[:, _pos_col(rf)].astype(np.float64)


def oob_reference(rf, Xref) -> tuple[np.ndarray, int]:
    """Out-of-bag P(violation) of each TRAINING row, evaluated on ``Xref`` (the training rows in the scoring
    representation: uncentred). Trees summed in fixed order. Rows that are in-bag for every tree (practically
    never with 500 trees) fall back to the in-sample forest score. Returns (scores, n_fallback).
    With Xref == the fit matrix this equals sklearn's oob_decision_function_[:, 1] (tested)."""
    Xref = np.asarray(Xref, np.float32)
    n = len(Xref)
    col = _pos_col(rf)
    acc = np.zeros(n)
    cnt = np.zeros(n)
    for est, samp in zip(rf.estimators_, rf.estimators_samples_):
        m = np.ones(n, bool)
        m[samp] = False
        if m.any():
            acc[m] += est.predict_proba(Xref[m], check_input=False)[:, col]
            cnt[m] += 1
    out = np.empty(n)
    ok = cnt > 0
    out[ok] = acc[ok] / cnt[ok]
    if (~ok).any():
        out[~ok] = rf_proba(rf, Xref[~ok])
    return out, int((~ok).sum())


def reference_scores(rf, Xref) -> tuple[np.ndarray, int]:
    """Training-row reference distribution for the percentile map (prereg §2.3): REF_MODE 'insample' (fixed) =
    the forest's in-sample score of the training rows, exactly the iter06 convention (train_percentile of the
    training-row scores). 'oob' is kept only for the synthetic comparison in the prereg; not used in the run."""
    if REF_MODE == "insample":
        return rf_proba(rf, Xref), 0
    if REF_MODE == "oob":
        return oob_reference(rf, Xref)
    raise ValueError(REF_MODE)


class RFT7a:
    """T7-a (within_tool.T7aW, method none) and the RF member on the same fold-internal robust embeddings."""

    def __init__(self, feats: dict, rows: E.Rows, params=None):
        self.t7 = W.T7aW(feats, rows)
        self.rows = rows
        self.ctx = self.t7.ctx           # shared object: probes scramble it for both parts
        self.store = self.t7.store
        self.params = dict(RF_PARAMS if params is None else params)
        self.oob_fallback = 0
        self.tie_log = []

    def _bound_cache(self):
        if len(self.store.cache) > CACHE_LIMIT:   # embeddings are label-free; keep memory bounded
            self.store.cache.clear()

    def rf_features(self, pa, pre_only=False) -> np.ndarray:
        """[n_rows, 42] float32; PCA / robust scale fitted on pa only (RobustStore)."""
        cols = []
        for rep, k in RF_REPS:
            r = PRE_REPS.get(rep, rep) if pre_only else rep
            cols.append(self.store.get(r, pa)[:, :k])
        return np.hstack(cols).astype(np.float32)

    def rf_member(self, pa, ya, pb, msl, variant="plain", pre_only=False) -> np.ndarray:
        """Training-percentile (OOB reference) of the RF score of the scored rows pb."""
        from experiments.risk_loop.argus_loop import iter06_models as M6
        pa, pb = np.asarray(pa, np.int64), np.asarray(pb, np.int64)
        ya = np.asarray(ya).astype(np.int64)
        _check(not np.intersect1d(pa, pb).size, "train_test_disjoint")
        X = self.rf_features(pa, pre_only)
        Xtr, Xte = X[pa], X[pb]
        src = np.asarray(self.ctx["source"]).astype(str)[pa]
        cells = np.asarray(self.ctx["train_group"]).astype(str)[pa]
        if len(np.unique(ya)) < 2:      # as iter06 (no fit -> zero scores -> percentile 0.5)
            return M6.train_percentile(np.zeros(len(pa)), np.zeros(len(pb)))
        if variant == "w1":
            Xfit, _, used = W.cell_center(Xtr, cells, pa)
            W.center_audit(used, pa, pb)
        elif variant == "plain":
            Xfit = Xtr
        else:
            raise ValueError(variant)
        sw = member1_weights(ya, src, cells)
        rf = fit_rf(Xfit, ya, sw, msl, self.params)
        s_te = rf_proba(rf, Xte)
        s_ref, nfb = reference_scores(rf, Xtr)     # training rows only, uncentred (scoring representation)
        self.oob_fallback += nfb
        del rf
        self._bound_cache()
        pct = M6.train_percentile(s_ref, s_te)
        self.tie_log.append((len(np.unique(pct)), len(np.unique(s_te))))   # degeneracy monitor (report only)
        return pct

    def t7a(self, pa, ya, pb, pre_only=False) -> np.ndarray:
        return self.t7.fit(pa, ya, pb, "none", pre_only)


def combine(t7a_score, rf_score, w_rf) -> np.ndarray:
    """(1 - w) x mean of the 3 T7-a member percentiles + w x RF percentile. w = 1/4 -> equal weight over 4 members;
    w = 0 -> exactly T7-a; w = 1 -> exactly the RF member."""
    w = float(w_rf)
    if w == 0.0:
        return np.asarray(t7a_score, np.float64).copy()
    if w == 1.0:
        return np.asarray(rf_score, np.float64).copy()
    return (1.0 - w) * np.asarray(t7a_score, np.float64) + w * np.asarray(rf_score, np.float64)


class Runner:
    """Try -> make(msl) -> fit_predict(pa, ya, pb) through the disk memo (within_tool.Memo)."""

    def __init__(self, model: RFT7a, memo: W.Memo, grid=None):
        self.m, self.memo, self.rows = model, memo, model.rows
        self.grid = list(MSL_GRID if grid is None else grid)

    def t7a_fp(self, pre_only=False):
        def fp(pa, ya, pb):
            return self.memo.get(f"t7a|none|{'pre' if pre_only else 'all'}", pa, ya, pb,
                                 lambda: self.m.t7a(pa, ya, pb, pre_only))
        return fp

    def rf_score(self, variant, pre_only, msl, pa, ya, pb):
        tag = f"rf{rf_tag()}|{variant}|{'pre' if pre_only else 'all'}|msl{msl}"
        return self.memo.get(tag, pa, ya, pb, lambda: self.m.rf_member(pa, ya, pb, msl, variant, pre_only))

    def compute(self, try_id, pre_only, msl, pa, ya, pb, use_memo=True):
        w = RF_WEIGHT[try_id]
        var = RF_VARIANT[try_id]
        if use_memo:
            r = self.rf_score(var, pre_only, msl, pa, ya, pb)
            t = self.t7a_fp(pre_only)(pa, ya, pb) if w < 1.0 else None
        else:
            r = self.m.rf_member(pa, ya, pb, msl, var, pre_only)
            t = self.m.t7a(pa, ya, pb, pre_only) if w < 1.0 else None
        return r.copy() if t is None else combine(t, r, w)

    def make(self, try_id, pre_only=False):
        def mk(msl):
            def fp(pa, ya, pb):
                return self.compute(try_id, pre_only, msl, pa, ya, pb)
            return fp
        return mk

    def nested(self, try_id, pre_only=False, seeds=None):
        seeds = SEEDS3 if seeds is None else seeds
        return E.nested_cv(self.make(try_id, pre_only), self.grid, None, self.rows, seeds, 5, inner_splits=W.INNER)

    def probe(self, try_id, pre_only=False):
        """Scrambling tool / source / rollout (every ctx field) of the SCORED rows leaves scores bitwise equal
        (fold 0, seed 0, first grid value). Bypasses the memo."""
        a, b = E.make_folds(self.rows, 5, 0)[0]
        y = self.rows.y
        msl = self.grid[0]
        s1 = self.compute(try_id, pre_only, msl, a, y[a], b, use_memo=False)
        ctx = self.m.ctx
        saved = {k: np.asarray(v).copy() for k, v in ctx.items()}
        try:
            for k in ctx:
                arr = np.asarray(ctx[k]).copy()
                arr[b] = arr[b][::-1]
                ctx[k] = arr
            s2 = self.compute(try_id, pre_only, msl, a, y[a], b, use_memo=False)
        finally:
            ctx.update(saved)
        ok = bool(np.array_equal(s1, s2))
        _check(ok, "scores_invariant_to_scored_rows_metadata")
        return {"ok": ok, "max_abs_diff": float(np.abs(s1 - s2).max())}


# ============================================================================================== metrics helpers

def k3_abs_rho(oofs, rows: E.Rows, nobs32) -> float | None:
    """K3 (cycle-1 code, obs_grid.py): per headline cell |Spearman(score, n observation points on the 32 grid)|,
    violation-weighted mean over cells, mean over seeds."""
    y = rows.y
    g = E.headline_groups(rows)
    vals = []
    for o in oofs:
        k3 = []
        for c in sorted(set(g.tolist())):
            m = g == c
            p = int(y[m].sum())
            if p >= E.MIN_POS and m.sum() - p >= E.MIN_NEG:
                rho = E._spearman(o[m], nobs32[m])
                if rho is not None:
                    k3.append((abs(rho), p))
        vals.append(sum(a * p for a, p in k3) / sum(p for _, p in k3) if k3 else None)
    return E._mean(vals)


def load_nobs32(rows: E.Rows) -> np.ndarray:
    from experiments.risk_loop.argus_loop import obs_cache as OC
    oc = OC.ObsCache(W.CACHE)
    return np.asarray(oc.gather(rows.row_id, rows.row_id).n_obs32, np.float64)


def rank_corr(a_list, b_list) -> float:
    from scipy.stats import spearmanr
    return float(np.mean([spearmanr(a, b).correlation for a, b in zip(a_list, b_list)]))


# ============================================================================================== runner

def sha256(p: Path) -> str:
    return W.sha256(p)


def prereg_frozen() -> tuple[bool, str]:
    if not PREREG.is_file():
        return False, f"missing {PREREG}"
    if not PREREG_SHA.is_file():
        return False, f"missing {PREREG_SHA}"
    txt = PREREG_SHA.read_text(encoding="utf-8").split()
    if not txt:
        return False, "empty sha file"
    cur = sha256(PREREG)
    if txt[0].lower() != cur:
        return False, f"sha mismatch: recorded {txt[0]}, current {cur}"
    if "DRAFT" in PREREG.read_text(encoding="utf-8").splitlines()[0]:
        return False, "first line of the prereg still says DRAFT"
    return True, cur


def start_checks() -> dict:
    ok, why = prereg_frozen()
    if not ok:
        print("PREREG_NOT_FROZEN", why, flush=True)
        raise SystemExit(3)
    if E.evaluate_sha256() != W.EVAL_SHA:
        raise SystemExit("evaluate.py sha changed")
    fits = OUT / "fits"
    first = min((p.stat().st_mtime for p in fits.rglob("*.npy")), default=None) if fits.is_dir() else None
    sha_t = PREREG_SHA.stat().st_mtime
    if first is not None and first < sha_t:
        raise SystemExit("a fit in the store is older than the prereg sha")
    code = {f: sha256(REPO_ROOT / f) for f in CODE_FILES}
    import sklearn
    return {"prereg_sha": why, "evaluate_sha": E.evaluate_sha256(), "first_fit_mtime": first,
            "prereg_sha_mtime": sha_t, "code_sha256": code, "sklearn": sklearn.__version__,
            "rf_params": RF_PARAMS, "rf_tag": rf_tag(), "msl_grid": list(MSL_GRID)}


def _res_path(t):
    return OUT / f"result_{t}.json"


def _load(t):
    return json.loads(_res_path(t).read_text(encoding="utf-8")) if _res_path(t).is_file() else {}


def _save(t, res):
    OUT.mkdir(parents=True, exist_ok=True)
    tmp = _res_path(t).with_suffix(f".tmp{os.getpid()}")
    tmp.write_text(json.dumps(E.to_jsonable(res), indent=1, ensure_ascii=False), encoding="utf-8")
    os.replace(tmp, _res_path(t))


def _oof_list(cv):
    return [np.asarray(cv["oof"][str(s)], np.float64) for s in cv["seeds"]]


def _np_save(name, arr):
    p = OUT / name
    tmp = p.with_name(p.stem + f".tmp{os.getpid()}.npy")
    np.save(tmp, np.asarray(arr))
    os.replace(tmp, p)


def load_model(params=None):
    from experiments.risk_loop.argus_loop import iter01_common as C1
    from experiments.risk_loop.argus_loop import iter11_diag_models as DM
    data, rows, _ = C1.headline_data(W.VIEW)
    feats = DM.load_feats(data, rows, ["L23:max", "L16:pre", "L23:pre"])
    del data
    return RFT7a(feats, rows, params)


def run_all(tries, threads, model: RFT7a | None = None, memo: W.Memo | None = None, nobs32=None, out=None,
            grid=None):
    """Stages (resumable, each saved as soon as it is done): 0 T7-a reference; 1 nested R0, R1, R2; 2 probes;
    3 pre-only controls; 4 shuffles (a) / (b). ``model`` / ``memo`` / ``nobs32`` / ``out`` / ``grid`` only for
    tests."""
    global OUT
    if out is not None:
        OUT = Path(out)
    OUT.mkdir(parents=True, exist_ok=True)
    RF_PARAMS["n_jobs"] = int(threads)
    if model is not None:
        model.params["n_jobs"] = int(threads)
    model = model or load_model()
    memo = memo or W.Memo(OUT)
    run = Runner(model, memo, grid)
    rows = run.rows
    _check(set(rows.split.tolist()) == {"train"}, "train_split_only")
    t00 = time.time()
    # 0) T7-a reference, recomputed in this run (fixed, fold seeds 0-2)
    ref = _load("T7A")
    p_ref = OUT / "oof_T7A.npy"
    if "value" not in ref or not p_ref.is_file():
        cv = E.run_cv(run.t7a_fp(False), None, rows, SEEDS3)
        t7 = _oof_list(cv)
        _np_save("oof_T7A.npy", t7)
        m = E.metrics(cv, rows, baselines=False)
        ref = {"what": "T7-a (within_tool.T7aW method none), fold seeds 0-2, recomputed in this run",
               "value": m["within_tool"]["value"], "nested_equivalent": W.compact(m),
               "expected": T7A_EXPECTED, "row_id_hash": W.OM.h_arr(rows.row_id)}
        if IT14_T7A_OOF.is_file() and out is None:
            o14 = np.load(IT14_T7A_OOF)
            ref["max_abs_diff_vs_iter14_oof"] = float(np.abs(o14 - np.asarray(t7)).max()) \
                if o14.shape == np.asarray(t7).shape else None
        _save("T7A", ref)
        log(f"[T7-a] reference {ref['value']:.4f} (expected ~{T7A_EXPECTED}; iter-14 oof diff "
            f"{ref.get('max_abs_diff_vs_iter14_oof')})")
    t7 = list(np.load(p_ref))
    if nobs32 is None:
        nobs32 = load_nobs32(rows)
    oofs = {}
    # 1) nested main numbers
    for t in tries:
        res = _load(t)
        p = OUT / f"oof_{t}.npy"
        if "nested" in res and p.is_file():
            oofs[t] = list(np.load(p))
            continue
        t1 = time.time()
        cv = run.nested(t)
        oofs[t] = _oof_list(cv)
        _np_save(f"oof_{t}.npy", oofs[t])
        m = E.metrics(cv, rows)
        modal = run.grid[E._modal_choice(cv)]
        res.update({"try": t, "try_ko": TRY_KO[t], "rf_weight": RF_WEIGHT[t], "rf_variant": RF_VARIANT[t],
                    "grid_min_samples_leaf": run.grid, "rf_params": RF_PARAMS,
                    "nested": W.compact(m), "nested_full_within_tool": m["within_tool"],
                    "correlation": m["correlation"], "chosen": cv["selection"]["chosen"],
                    "inner_scores": cv["selection"]["inner_scores"], "modal_min_samples_leaf": modal,
                    "gain_vs_t7a": W.paired_gain(oofs[t], t7, rows),
                    "rank_corr_vs_t7a": rank_corr(oofs[t], t7),
                    "K3_abs_rho": k3_abs_rho(oofs[t], rows, nobs32),
                    "luck_corrected": W.luck_correction(m["within_tool"]["value"], TRIES_BEFORE + N_NEW),
                    "luck_corrected_conservative": W.luck_correction(m["within_tool"]["value"],
                                                                     TRIES_BEFORE_CONS + N_NEW),
                    "_metrics_for_gate": {"within_tool": m["within_tool"]},
                    "minutes_nested": (time.time() - t1) / 60})
        v = m["within_tool"]["value"]
        log(f"[{t}] nested {v:.4f} CI {m['within_tool']['ci95']['ci_low']:.3f}-{m['within_tool']['ci95']['ci_high']:.3f}"
            f" gain vs T7-a {res['gain_vs_t7a']['gain']:+.4f} [{res['gain_vs_t7a']['ci_low']:+.3f}, "
            f"{res['gain_vs_t7a']['ci_high']:+.3f}] modal msl {modal} ({res['minutes_nested']:.1f} min, memo hit "
            f"{memo.hits} miss {memo.miss})")
        if v >= 0.90:
            log(f"!!!!! [{t}] nested >= 0.90 -- validation stays CLOSED (user decision)")
        _save(t, res)
    # extra paired comparisons (report only)
    pairs = [("R1", "R0"), ("R2", "R1"), ("R2", "R0")]
    for a_, b_ in pairs:
        if a_ in oofs and b_ in oofs:
            res = _load(a_)
            key = f"gain_vs_{b_}"
            if key not in res:
                res[key] = W.paired_gain(oofs[a_], oofs[b_], rows)
                res[f"rank_corr_vs_{b_}"] = rank_corr(oofs[a_], oofs[b_])
                _save(a_, res)
    # 2) leak probes (fold 0, seed 0)
    for t in tries:
        res = _load(t)
        if res.get("probe", {}).get("all", {}).get("ok") and res.get("probe", {}).get("pre", {}).get("ok"):
            continue
        res["probe"] = {"all": run.probe(t, False), "pre": run.probe(t, True)}
        log(f"[{t}] probe {res['probe']}")
        _save(t, res)
    # 3) pre-action-only control (same try, members on pre-action representations, same grid / inner CV-4)
    for t in tries:
        res = _load(t)
        if "pre_only" in res:
            continue
        t1 = time.time()
        cv = run.nested(t, pre_only=True)
        o = _oof_list(cv)
        _np_save(f"oof_{t}_pre.npy", o)
        m = E.metrics(cv, rows, baselines=False)
        g = W.paired_gain(oofs[t], o, rows)
        res["pre_only"] = {"nested": W.compact(m), "chosen": cv["selection"]["chosen"], "main_minus_pre": g,
                           "K3_abs_rho": k3_abs_rho(o, rows, nobs32), "minutes": (time.time() - t1) / 60}
        log(f"[{t}] pre-only control {m['within_tool']['value']:.4f}, main - pre {g['gain']:+.4f} "
            f"[{g['ci_low']:+.3f}, {g['ci_high']:+.3f}] ({res['pre_only']['minutes']:.1f} min)")
        _save(t, res)
    # 4) shuffles (a) within source, (b) within source x family; modal msl, fold seed 0
    keep = ("within_tool_mean", "within_tool_sd", "within_tool_se", "within_tool", "pass",
            "within_tool_by_source_mean", "pooled_auroc_mean")
    for t in tries:
        res = _load(t)
        if "shuffle_a" not in res or "shuffle_b" not in res:
            t1 = time.time()
            fp = run.make(t)(res["modal_min_samples_leaf"])
            sa = E.shuffle_test(fp, rows, N_SHUF, seed=0, within=("source",), n_jobs=1)
            res["shuffle_a"] = {k: sa[k] for k in keep}
            _save(t, res)
            sb = E.shuffle_test(fp, rows, N_SHUF, seed=0, within=("source", "family"), n_jobs=1)
            res["shuffle_b"] = {k: sb[k] for k in keep}
            log(f"[{t}] shuffles a {sa['within_tool_mean']:.4f} b {sb['within_tool_mean']:.4f} "
                f"({(time.time() - t1) / 60:.1f} min)")
        res["rules"] = rules(res)
        res["audit"] = dict(W.AUDIT)
        _save(t, res)
    for t in tries:
        res = _load(t)
        res["memo"] = {"hits": memo.hits, "miss": memo.miss, "oob_fallback_rows": model.oob_fallback}
        if model.tie_log:
            ratio = np.asarray([a / max(b, 1) for a, b in model.tie_log])
            res["tie_monitor_all_rf_fits_this_process"] = {
                "what": "distinct percentiles / distinct raw RF scores of the scored rows, per RF fit",
                "n_fits": len(ratio), "mean": float(ratio.mean()), "min": float(ratio.min()),
                "p05": float(np.percentile(ratio, 5))}
        res["minutes_total_this_process"] = (time.time() - t00) / 60
        _save(t, res)
    log("DONE", dict(W.AUDIT))


def rules(res: dict) -> dict:
    """prereg §5. Success gate = evaluate.success_gate (TASK.md §0 1-5) + K1 + K3; monitor audit pending."""
    v = res["nested"]["value"]
    sa, sb = res["shuffle_a"], res["shuffle_b"]
    g = res["gain_vs_t7a"]
    margin = v - max(sb["within_tool_mean"], REF_B)
    r = {"gain_vs_t7a_ci_low_gt_0": g["ci_low"] > 0,
         "shuffle_a_in_0.45_0.55": abs(sa["within_tool_mean"] - 0.5) <= 0.05,
         "margin_over_b": margin, "margin_ge_0.10": margin >= 0.10}
    r["improvement_over_t7a"] = bool(r["gain_vs_t7a_ci_low_gt_0"] and r["shuffle_a_in_0.45_0.55"]
                                     and r["margin_ge_0.10"])
    pre = res.get("pre_only", {})
    if pre:
        k1_low = pre["main_minus_pre"]["ci_low"]
        r["K1_fail"] = bool(k1_low <= 0)
        rho, rho_c = res.get("K3_abs_rho"), pre.get("K3_abs_rho")
        r["K3_fail"] = bool(rho is not None and rho > 0.3 and (rho_c is None or rho - rho_c >= 0.10))
        r["K3_fixed_rule_gt_0.3"] = bool(rho is not None and rho > 0.3)
        r["pre_only_ge_main"] = bool(pre["nested"]["value"] >= v)
    gate_in = {"metrics": res["_metrics_for_gate"], "shuffle_source": sa, "shuffle_source_family": sb,
               "selection": {"method": "nested_cv"}}
    gate = E.success_gate(gate_in)
    r["success_gate"] = gate
    r["success_candidate"] = bool(gate["verdict"] == "PENDING_MONITOR_AUDIT" and pre
                                  and not r["K1_fail"] and not r["K3_fail"])
    return r


def cmd_run(tries, threads):
    chk = start_checks()
    log("start checks ok", json.dumps(chk))
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "start_checks.json").write_text(json.dumps(chk, indent=1), encoding="utf-8")
    run_all(tries, threads)


# ============================================================================================== report

def _f(x, d=3):
    return "—" if x is None else f"{x:.{d}f}"


def cmd_report(out_dir=None, report_dir=None):
    od = Path(out_dir) if out_dir else OUT
    rd = Path(report_dir) if report_dir else IT15
    rd.mkdir(parents=True, exist_ok=True)
    out = {"prereg": str(PREREG.relative_to(REPO_ROOT)),
           "prereg_sha256": sha256(PREREG) if PREREG.is_file() else None,
           "evaluate_sha256": E.evaluate_sha256(),
           "tries": {"before": TRIES_BEFORE, "after": TRIES_BEFORE + N_NEW, "before_conservative": TRIES_BEFORE_CONS,
                     "after_conservative": TRIES_BEFORE_CONS + N_NEW},
           "start_checks": json.loads((od / "start_checks.json").read_text(encoding="utf-8"))
           if (od / "start_checks.json").is_file() else None,
           "t7a_reference": json.loads((od / "result_T7A.json").read_text(encoding="utf-8"))
           if (od / "result_T7A.json").is_file() else None, "results": {}}
    for t in TRIES:
        p = od / f"result_{t}.json"
        if p.is_file():
            r = json.loads(p.read_text(encoding="utf-8"))
            r.pop("inner_scores", None)
            out["results"][t] = r
    (rd / "rf_results.json").write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    ref = out["t7a_reference"] or {}
    L = ["# 반복 15 결과 — T7-a에 랜덤 포레스트를 4번째 구성원으로 더하기 (자동 생성)", "",
         f"사전 등록: `prereg-rf.md`(sha `{(out['prereg_sha256'] or '?')[:8]}…`). 평가 코드 evaluate.py v4(sha "
         f"`{out['evaluate_sha256'][:8]}…`). train split만, validation·test 봉인 그대로. 학습 위반 76 / 평가 위반 48.",
         f"누적 시도 {TRIES_BEFORE} → {TRIES_BEFORE + N_NEW} (보수 {TRIES_BEFORE_CONS} → {TRIES_BEFORE_CONS + N_NEW}).", "",
         f"T7-a 기준(같은 실행에서 다시 계산, fold seed 0–2): **{_f(ref.get('value'))}** (예상 ≈ {T7A_EXPECTED}; "
         f"반복 14 OOF와 최대 차이 {ref.get('max_abs_diff_vs_iter14_oof')}).", "",
         "| 시도 | nested 값 | 95% CI | seed별 | 출처별 (10월/11월) | 전체 AUROC | T7-a 대비 이득 [CI] | 섞기 (a) / (b) | "
         "행동 직전만 대조군 | K1 (본−대조 CI 하한) | K3 \\|ρ\\| (대조) | 최빈 min_samples_leaf | 운 보정 (172 / 174) | 개선? | 성공 후보? |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for t, r in out["results"].items():
        n = r.get("nested", {})
        ci = n.get("ci95") or {}
        g = r.get("gain_vs_t7a", {})
        sa, sb = r.get("shuffle_a", {}), r.get("shuffle_b", {})
        pre = r.get("pre_only", {})
        ru = r.get("rules", {})
        bs = n.get("by_source", {})
        L.append("| " + " | ".join([
            TRY_KO[t], _f(n.get("value")), f"{_f(ci.get('ci_low'), 2)}–{_f(ci.get('ci_high'), 2)}",
            " / ".join(_f(x, 2) for x in n.get("per_seed", [])),
            " / ".join(_f(bs.get(s), 2) for s in E.SOURCES), _f(n.get("pooled_auroc"), 2),
            f"{g.get('gain', 0):+.3f} [{g.get('ci_low', 0):+.3f}, {g.get('ci_high', 0):+.3f}]" if g else "—",
            f"{_f(sa.get('within_tool_mean'))} / {_f(sb.get('within_tool_mean'))}",
            _f(pre.get("nested", {}).get("value")),
            _f(pre.get("main_minus_pre", {}).get("ci_low")) + (" FAIL" if ru.get("K1_fail") else ""),
            f"{_f(r.get('K3_abs_rho'), 2)} ({_f(pre.get('K3_abs_rho'), 2)})",
            str(r.get("modal_min_samples_leaf")),
            f"{_f(r.get('luck_corrected', {}).get('corrected'))} / "
            f"{_f(r.get('luck_corrected_conservative', {}).get('corrected'))}",
            "예" if ru.get("improvement_over_t7a") else ("아니오" if ru else "—"),
            "예" if ru.get("success_candidate") else ("아니오" if ru else "—")]) + " |")
    L += ["", "칸별 값(nested):", ""]
    for t, r in out["results"].items():
        pc = r.get("nested", {}).get("per_cell", {})
        L.append(f"- {TRY_KO[t]}: " + ", ".join(f"{k} {_f(v, 2)}" for k, v in sorted(pc.items())))
    L += ["", "짝 비교(같은 family 재표본):", ""]
    for t, r in out["results"].items():
        for k in ("gain_vs_R0", "gain_vs_R1"):
            if k in r:
                g = r[k]
                L.append(f"- {t} − {k[-2:]}: {g['gain']:+.3f} [{g['ci_low']:+.3f}, {g['ci_high']:+.3f}], 순위 상관 "
                         f"{_f(r.get('rank_corr_vs_' + k[-2:]), 2)}")
        if "rank_corr_vs_t7a" in r:
            L.append(f"- {t} ~ T7-a 순위 상관 {_f(r['rank_corr_vs_t7a'], 2)}")
    L += ["", "누출 감사:", ""]
    for t, r in out["results"].items():
        L.append(f"- {t}: probe {r.get('probe')}, audit {r.get('audit')}")
    L += ["", "nested ≥ 0.90인 시도가 있어도 validation은 열지 않는다(사용자 결정). 해석은 사람이 덧붙인다."]
    (rd / "rf_results.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(json.dumps({t: r.get("nested", {}).get("value") for t, r in out["results"].items()}, indent=1))


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=("check", "run", "report"))
    ap.add_argument("--tries", default="R0,R1,R2")
    ap.add_argument("--threads", type=int, default=2)
    a = ap.parse_args(argv)
    if a.cmd == "check":
        ok, why = prereg_frozen()
        print("PREREG_OK" if ok else "PREREG_NOT_FROZEN", why, flush=True)
        raise SystemExit(0 if ok else 3)
    if a.cmd == "run":
        tries = [x for x in a.tries.split(",") if x]
        for x in tries:
            if x not in TRIES:
                raise SystemExit(f"unknown try {x}")
        tries = [t for t in TRIES if t in tries]          # fixed order R0, R1, R2
        cmd_run(tries, a.threads)
    else:
        cmd_report()


if __name__ == "__main__":
    main()

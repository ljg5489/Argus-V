"""Phase-3 cycle-1 S stage: structure candidates S-A ... S-E (DRAFT prereg reports/risk-loop/argus-v1/loop/iter-13/
prereg-S-draft.md §2-§3). Strictly additive: obs_models.py (imported by the running cycle-1 grid) is not modified.

Structures (common: layer-20 observation cache -> in-fold PCA 32 -> filters -> pooling -> head; filter column 1
starts at the M0 direction, others N(0, 0.01); every structure keeps the pre_action slot):
  S-A  score = s_T7a + v.f + c. s_T7a = the EXISTING T7-a (iter06_models.make_t62 on iter07 RobustStore, exactly
       what iter11_diag_models.make_t7a / iter12_remeasure use), fixed, fitted in closed form on the training fold.
       f = [attention pool, pre] of K=2 filters (4). Learned: W 64 + q 32 + v 4 + c 1 = 101.
       Training rows get a CROSS-FITTED s_T7a (family-component 5-fold inside the training fold); scored rows get
       T7-a fitted on the whole training fold. v, c start at 0 -> with no training the score IS T7-a.
  S-B  K=2, slots [max, mean, pre] (6) -> linear: 71
  S-C  S-B with the max slot = mean of the top-2 observations: 71
  S-D  S-B features -> ReLU 4 -> ReLU 4 -> 1, dropout 0.3 on hidden units, head L2 1e-2 (draft appendix #2;
       activation ReLU instead of tanh, user request 2026-11-09): 117
  S-E  layers 20 + 23, PCA 32 and K=2 per layer, [max, mean, pre] -> 12 -> linear: 141
  S-0  convex baseline (obs_models_s0f): robust-scaled clipped PCA 32 per point -> [per-coordinate max, pre] (64)
       -> L2 logistic regression (+ pair loss, still convex). Tuning value C in {0.01, 0.1, 1}: 65
  S-F  CNN-MLP (obs_models_s0f): PCA 32 sequence -> Conv1d 32->8 k3 -> ReLU -> Conv1d 8->8 k3 -> ReLU ->
       [max, mean, pre] (24) -> 16 -> ReLU -> dropout 0.3 -> 2 -> softmax. Tuning value = weight decay
       {1e-3, 1e-2, 1e-1}; Adam lr 3e-3, 200 epochs: 1,410
S-B, S-C, S-E are plain obs_models configs (fitted by the unchanged ``obs_models.fit_obs``). S-A uses
``fit_obs_offset`` = a copy of ``obs_models.fit_obs`` with a fixed per-row offset added to the head output
(in the loss, the in-sample thresholds and the test scores). With offset "none" it equals ``fit_obs``. S-D (ReLU
head) goes through ``fit_obs_offset`` with zero offset and ``ObsModelS`` (obs_models.ObsModel with ReLU hidden
units; tanh is hard-coded in obs_models and must not change for cycle 1).

Tuning value (the "beta" slot of the nested selection; not a try): beta for S-A ... S-E, C for S-0, weight decay
for S-F (``TUNE``, ``tune_grid``, ``tune_of``). Grid order = ascending value (tie -> first, as for beta).

Toggle carry-over (§3): states {none, T2, T4, T2+T4} x 3 tuning values, nested tie order = fewer toggles first,
then T2 before T4 (obs_models.combos order), then smaller tuning value.
C-pre (K1 control) of every structure = the same structure with obs_subset "pre" (all slots see only the
pre_action row). For S-A the draft names T7-a itself as C-pre; both are provided.
"""
from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402
from experiments.risk_loop.argus_loop import obs_models as OM  # noqa: E402

BETAS_S = (1.0, 10.0, 100.0)
STATE_BITS = {"base": (0, 0, 0, 0, 0, 0), "T2": (0, 1, 0, 0, 0, 0), "T4": (0, 0, 0, 1, 0, 0),
              "T2+T4": (0, 1, 0, 1, 0, 0)}
STATES = ("base", "T2", "T4", "T2+T4")
STRUCT_ORDER = ("S-0", "S-A", "S-F", "S-B", "S-C", "S-D", "S-E")
STRUCTS = {
    "S-0": {"model": "s0", "logreg_C": 0.1},
    "S-F": {"model": "sf", "nn_wd": 1e-2, "lr": 3e-3, "mlp_width": 16, "mlp_dropout": 0.3},
    "S-A": {"K": 2, "pool": "attn", "slots": ("pool", "pre"), "offset": "t7a"},
    "S-B": {"K": 2},
    "S-C": {"K": 2, "pool": "topk", "topk": 2},
    "S-D": {"K": 2, "head": "mlp", "mlp_depth": 2, "mlp_width": 4, "mlp_dropout": 0.3, "head_l2": 1e-2,
            "mlp_act": "relu"},
    "S-E": {"K": 2, "layers": (20, 23)},
}
CONTROL_STRUCTS = {"M0": {"K": 1, "filters": "m0_fixed"}}
PARAMS_EXPECTED = {"S-0": 65, "S-A": 101, "S-F": 1410, "S-B": 71, "S-C": 71, "S-D": 117,
                   "S-E": 141}  # draft §2 table (T4 off)
# S-only keys (ignored by obs_models.fit_obs; part of config_id so S fits never collide with cycle-1 fits)
S_EXTRA = {"struct": "", "offset": "none", "sa_base": "t7a_pct", "sa_cf_folds": 5, "sa_cf_seed": 0,
           "model": "obs", "mlp_act": "tanh", "logreg_C": None, "nn_wd": None, "pair_w": 1.0, "cnn_ch": 8,
           "cnn_kernel": 3, "robust_clip": 3.0, "s0_t2_copies": 8}
# tuning value per structure: (config key, nested grid, value for the K1 control C-pre)
TUNE = {"S-0": ("logreg_C", (0.01, 0.1, 1.0), 0.1), "S-F": ("nn_wd", (1e-3, 1e-2, 1e-1), 1e-2)}
TUNE_DEFAULT = ("beta", BETAS_S, 1.0)
MODELS = ("obs", "s0", "sf")
ACTS = ("tanh", "relu")
OFFSETS = ("none", "t7a")
SA_BASES = ("t7a_pct", "t7a_zlogit")
T7A_REPS = ("L23:max", "L16:pre")


# ---------------------------------------------------------------------------------------------- configs

def bits_of_state(name: str) -> tuple:
    """'base', 'T2', 'T2+T4', 'T1+T5', ... -> toggle bits."""
    if name == "base":
        return (0,) * 6
    on = set(name.split("+"))
    if not on <= set(OM.TOGGLES):
        raise ValueError(f"unknown toggle state {name!r}")
    return tuple(int(t in on) for t in OM.TOGGLES)


def state_of(cfg) -> str:
    return OM.combo_name(cfg)


def tune_spec(struct: str) -> tuple:
    return TUNE.get(struct, TUNE_DEFAULT)


def tune_grid(struct: str) -> tuple:
    return tuple(sorted(tune_spec(struct)[1]))


def tune_name(struct: str) -> str:
    return tune_spec(struct)[0]


def tune_of(cfg: dict) -> float:
    return float(cfg[tune_name(cfg["struct"])])


def make_config_s(struct: str, bits=(0, 0, 0, 0, 0, 0), tune=None, **over) -> dict:
    """S config. ``tune`` = the structure's tuning value (beta for S-A ... S-E and the controls, C for S-0, weight
    decay for S-F); None -> the structure's default. For S-0 / S-F beta stays 1.0 (unused)."""
    spec = dict(STRUCTS[struct] if struct in STRUCTS else CONTROL_STRUCTS[struct])
    key = tune_name(struct)
    if tune is not None:
        spec[key] = tune
    spec.update(over)
    beta = spec.pop("beta", 1.0)
    s_over = {k: spec.pop(k) for k in list(spec) if k in S_EXTRA}
    cfg = OM.make_config(bits, beta, **spec)
    cfg.update(S_EXTRA)
    cfg.update(s_over)
    cfg["struct"] = struct
    for k in ("logreg_C", "nn_wd"):
        cfg[k] = None if cfg[k] is None else float(cfg[k])
    if cfg["offset"] not in OFFSETS or cfg["sa_base"] not in SA_BASES or cfg["model"] not in MODELS or \
            cfg["mlp_act"] not in ACTS:
        raise ValueError((cfg["offset"], cfg["sa_base"], cfg["model"], cfg["mlp_act"]))
    if cfg["model"] != "obs" and cfg[key] is None:
        raise ValueError(f"{struct}: tuning value {key} missing")
    return cfg


def combo_key_s(cfg: dict) -> str:
    """Identity of a try: obs_models.combo_key with the S-0 / S-F tuning values also excluded (as beta is)."""
    c = dict(cfg)
    c["logreg_C"] = c["nn_wd"] = None
    return OM.combo_key(c)


def supports_state(struct: str, state: str) -> bool:
    """S-0 / S-F have no T3 (auxiliary report head); S-0 has no T1 (focal loss is not convex)."""
    on = set() if state == "base" else set(state.split("+"))
    model = STRUCTS.get(struct, {}).get("model", "obs")
    if model == "s0":
        return not on & {"T1", "T3"}
    if model == "sf":
        return "T3" not in on
    return True


def derive(cfg: dict, **over) -> dict:
    """Copy of an S config with some keys changed (same normalisation as make_config)."""
    c = dict(cfg)
    for k, v in over.items():
        if k not in c:
            raise KeyError(f"unknown config key {k!r}")
        c[k] = v
    for k in ("layers", "init_seeds", "slots"):
        c[k] = tuple(int(x) for x in c[k]) if k != "slots" else tuple(c[k])
    if c["aux_null_within"] is not None:
        c["aux_null_within"] = tuple(c["aux_null_within"])
    c["beta"] = float(c["beta"])
    for k in ("logreg_C", "nn_wd"):
        c[k] = None if c[k] is None else float(c[k])
    return c


def s_grid(struct: str, states=STATES, tunes=None, **over) -> list[dict]:
    """The nested-selection choices of one structure in tie-break order (ties -> first). States the structure
    does not support (``supports_state``) are left out."""
    order = {OM.combo_name(OM.make_config(b)): i for i, b in enumerate(OM.combos())}
    sts = sorted([s for s in states if supports_state(struct, s)],
                 key=lambda s: order[OM.combo_name(OM.make_config(bits_of_state(s)))])
    tunes = tune_grid(struct) if tunes is None else tuple(sorted(tunes))
    return [make_config_s(struct, bits_of_state(s), t, **over) for s in sts for t in tunes]


def cpre_config(struct: str, tune=None, **over) -> dict:
    """K1 control: the same structure, toggles off, every slot sees only the pre_action row at scoring time
    (S-0: logistic on pre z; S-F: the same MLP on pre z). ``tune`` None -> the middle value (beta 1 / C 0.1 / wd
    1e-2; only for parameter counts and unit tests): the run chooses it by inner CV-4 over ``cpre_grid``
    (orchestrator decision 3, same grid as the main model)."""
    return make_config_s(struct, (0,) * 6, tune_spec(struct)[2] if tune is None else tune, obs_subset="pre", **over)


def cpre_grid(struct: str, **over) -> list[dict]:
    """C-pre nested-selection choices: the structure's tuning grid, ascending (ties -> first)."""
    return [cpre_config(struct, t, **over) for t in tune_grid(struct)]


def combo_name_s(cfg: dict) -> str:
    sub = "" if cfg["obs_subset"] == "all" else f"|{cfg['obs_subset']}"
    return f"{cfg['struct']}|{OM.combo_name(cfg)}{sub}"


def n_params(cfg: dict) -> int:
    """Learned values (draft §2 counting): filters, attention query, head weights and biases (T3 aux head too).
    S-0: logistic weights + intercept. S-F: conv kernels + biases, MLP weights + biases (2 output logits)."""
    pre = cfg["obs_subset"] == "pre"
    model = cfg.get("model", "obs")
    if model == "s0":
        return int((1 if pre else 2) * int(cfg["pca_k"]) + (1 if cfg["T4"] else 0) + 1)
    if model == "sf":
        k, ch, ks, w = int(cfg["pca_k"]), int(cfg["cnn_ch"]), int(cfg["cnn_kernel"]), int(cfg["mlp_width"])
        conv = 0 if pre else (k * ch * ks + ch) + (ch * ch * ks + ch)
        fin = (k if pre else 3 * ch) + (1 if cfg["T4"] else 0)
        return int(conv + fin * w + w + w * 2 + 2)
    nL, k, K = len(cfg["layers"]), int(cfg["pca_k"]), int(cfg["K"])
    n = nL * k * K if cfg["filters"] == "learned" else 0
    n += nL * k if cfg["pool"] == "attn" else 0
    F = len(cfg["slots"]) * nL * K + (1 if cfg["T4"] else 0)
    dims = [F, 1] if cfg["head"] == "linear" else [F] + [int(cfg["mlp_width"])] * int(cfg["mlp_depth"]) + [1]
    n += sum(a * b + b for a, b in zip(dims[:-1], dims[1:]))
    if cfg["T3"]:
        n += len(cfg["slots"]) * nL * K + 1
    return int(n)


# ---------------------------------------------------------------------------------------------- T7-a base score

class T7aBase:
    """The fixed T7-a score from the ORIGINAL pooled feature pipeline (features/L23_max, L16_pre via
    iter01_common.features), exactly the recipe of iter11_diag_models.make_t7a. Pure function of (training
    positions, training labels, scored positions); a fresh RobustStore per call so memory does not grow."""

    def __init__(self, feats: dict, rows: E.Rows, lru: int = 4):
        from experiments.risk_loop.argus_loop import iter06_scan as S6
        self.feats, self.rows = feats, rows
        self.ctx = S6.model_ctx(rows)
        self.memo = OM.LRU(lru)
        self.calls = 0

    @classmethod
    def load(cls, view) -> "T7aBase":
        from experiments.risk_loop.argus_loop import iter01_common as C1
        from experiments.risk_loop.argus_loop import iter11_diag_models as DM
        data, rows, _ = C1.headline_data(view)
        return cls(DM.load_feats(data, rows, list(T7A_REPS)), rows)

    def _fp(self, kind: str):
        from experiments.risk_loop.argus_loop import iter06_models as M6
        from experiments.risk_loop.argus_loop import iter07_models as M7
        store = M7.RobustStore(self.feats)
        if kind == "t7a_pct":  # == iter11_diag_models.make_t7a(feats, rows)[0]
            return M6.make_t62(store, self.ctx)(M7.GRID_T7A[0])
        if kind == "t7a_zlogit":  # draft wording: mean of the 3 members' training-standardised linear scores
            def fp(pa, ya, pb):
                pa, pb, ya = np.asarray(pa, np.int64), np.asarray(pb, np.int64), np.asarray(ya).astype(np.int64)
                acc = np.zeros(len(pb))
                for comp in M6.ENSEMBLE:
                    s_tr, s_te = M6._component_scores(comp, store, self.ctx, pa, ya, pb)
                    sd = float(np.std(s_tr))
                    acc += (s_te - float(np.mean(s_tr))) / (sd if sd > 1e-12 else 1.0)
                return acc / len(M6.ENSEMBLE)
            return fp
        raise ValueError(kind)

    def test_scores(self, pos_train, y_train, pos_test, kind="t7a_pct") -> np.ndarray:
        self.calls += 1
        return np.asarray(self._fp(kind)(np.asarray(pos_train, np.int64), np.asarray(y_train).astype(np.int64),
                                         np.asarray(pos_test, np.int64)), np.float64)

    def scores(self, pos_train, y_train, pos_test, kind="t7a_pct", n_folds=5, seed=0):
        """(cross-fitted training-row scores, scored-row scores fitted on all training rows, audit)."""
        pa, pb = np.asarray(pos_train, np.int64), np.asarray(pos_test, np.int64)
        ya = np.asarray(y_train).astype(np.int64)
        key = (kind, int(n_folds), int(seed), OM.h_arr(pa, ya.astype(np.int8), pb))
        hit = self.memo.get(key)
        if hit is not None:
            return hit
        off_te = self.test_scores(pa, ya, pb, kind)
        ir = self.rows.subset(pa)
        ir.label = ya.astype(np.float64)
        folds = E.make_folds(ir, int(n_folds), int(seed))
        off_tr = np.full(len(pa), np.nan)
        comp = E.group_components(ir)
        disjoint = True
        for ia, ib in folds:
            disjoint &= not np.isin(comp[ia], comp[ib]).any() and not np.intersect1d(ia, ib).size
            off_tr[ib] = self.test_scores(pa[ia], ya[ia], pa[ib], kind)
        audit = {"offset_kind": kind, "offset_rows_hash": OM.h_arr(pa), "offset_cf_folds": len(folds),
                 "offset_crossfit_ok": bool(disjoint and np.isfinite(off_tr).all())}
        out = (off_tr, off_te, audit)
        self.memo.put(key, out)
        return out


# ---------------------------------------------------------------------------------------------- fitting

def fit_s(data: OM.ObsData, cfg: dict, pos_train, y_train, pos_test, *, base: T7aBase | None = None,
          keep_model=False, threads=None) -> OM.FitOut:
    # obs_models.ObsModel.head draws MLP dropout masks from torch's GLOBAL generator (unseeded there; cycle 1
    # never used dropout). Seed it per fit so S-D fits are a pure function of (config, data) like all others.
    torch = OM._torch()
    torch.manual_seed(int(OM.h_arr(np.asarray(cfg["init_seeds"], np.int64), np.asarray(pos_train, np.int64),
                                   np.asarray(y_train).astype(np.int8))[:12], 16))
    model = cfg.get("model", "obs")
    if model in ("s0", "sf"):
        from experiments.risk_loop.argus_loop import obs_models_s0f as S0F
        if model == "s0":
            if threads:
                torch.set_num_threads(int(threads))
            return S0F.fit_s0(data, cfg, pos_train, y_train, pos_test)
        return S0F.fit_sf(data, cfg, pos_train, y_train, pos_test, threads=threads, keep_model=keep_model)
    if cfg.get("offset", "none") == "none" and cfg.get("mlp_act", "tanh") == "tanh":
        return OM.fit_obs(data, cfg, pos_train, y_train, pos_test, keep_model=keep_model, threads=threads)
    if cfg.get("offset", "none") == "none":  # ReLU MLP head (S-D): zero offset, ObsModelS
        return fit_obs_offset(data, cfg, pos_train, y_train, pos_test, threads=threads, keep_model=keep_model)
    if keep_model:
        raise NotImplementedError("packaging an offset (S-A) model needs the pooled T7-a pipeline at scoring time")
    if base is None:
        raise ValueError("S-A needs a T7aBase")
    off_tr, off_te, a = base.scores(pos_train, y_train, pos_test, cfg["sa_base"], cfg["sa_cf_folds"],
                                    cfg["sa_cf_seed"])
    out = fit_obs_offset(data, cfg, pos_train, y_train, pos_test, off_tr, off_te, threads=threads)
    out.audit.update(a)
    return out


class ObsModelS(OM.ObsModel):
    """obs_models.ObsModel with the MLP hidden activation taken from cfg["mlp_act"] (tanh | relu)."""

    def head(self, f, train):
        torch = OM._torch()
        act = torch.relu if self.cfg.get("mlp_act", "tanh") == "relu" else torch.tanh
        x = f
        n = len(self.head_w)
        for i in range(n):
            x = torch.einsum("rnf,rfo->rno", x, self.head_w[i]) + self.head_b[i].unsqueeze(1)
            if i < n - 1:
                x = act(x)
                if train and self.cfg["mlp_dropout"] > 0:
                    x = torch.nn.functional.dropout(x, float(self.cfg["mlp_dropout"]), True)
        return x.squeeze(-1)


@dataclass
class ParamsOnly:
    """Fitted parameters of an S model whose numpy scoring path (obs_models.head_np, tanh only) does not apply."""
    cfg: dict
    params: dict


def fit_obs_offset(data: OM.ObsData, cfg: dict, pos_train, y_train, pos_test, off_train=None, off_test=None, *,
                   threads=None, keep_model=False) -> OM.FitOut:
    """obs_models.fit_obs with a fixed offset added to the head output (training rows: ``off_train``; scored
    rows: ``off_test``). Offsets None -> zeros -> identical to fit_obs (tested). Code kept line-for-line with
    fit_obs except the four marked OFFSET lines and the model class (ObsModelS: tanh or ReLU hidden units)."""
    torch = OM._torch()
    if threads:
        torch.set_num_threads(int(threads))
    pos_train = np.asarray(pos_train, dtype=np.int64)
    pos_test = np.asarray(pos_test, dtype=np.int64)
    y_train = np.asarray(y_train).astype(np.int64)
    off_train = np.zeros(len(pos_train)) if off_train is None else np.asarray(off_train, np.float64)
    off_test = np.zeros(len(pos_test)) if off_test is None else np.asarray(off_test, np.float64)
    if off_train.shape != (len(pos_train),) or off_test.shape != (len(pos_test),):
        raise ValueError("offset shapes must match the training / scored rows")
    if len(pos_train) and (pos_train.max() >= data.n_head or (len(pos_test) and pos_test.max() >= data.n_head)):
        raise ValueError("fit_predict positions must be headline positions")
    if np.intersect1d(pos_train, pos_test).size:
        raise ValueError("training and scored rows overlap")
    layers, k, R = cfg["layers"], int(cfg["pca_k"]), len(cfg["init_seeds"])
    audit = {"cfg": OM.config_id(cfg), "train_hash": OM.h_arr(pos_train), "test_hash": OM.h_arr(pos_test),
             "n_train": int(len(pos_train)), "pca_rows_hash": OM.h_arr(pos_train)}
    if len(np.unique(y_train)) < 2:
        c = OM._constant(len(pos_test), R, audit)
        c.score = c.score + off_test                                             # OFFSET
        c.scores_rep = (c.scores_rep + off_test[None, :]).astype(np.float32)
        return c
    embs = {L: data.embed(L, pos_train, k) for L in layers}
    audit["pca_fit_rows_match"] = all(embs[L].fit_rows == OM.h_arr(pos_train) for L in layers)
    extras = data.allowed_extras(pos_train, pos_test) if cfg["T3"] else np.zeros(0, np.int64)
    status_tr = data.status[pos_train].copy()
    y_ex = data.y_extra[extras].astype(np.int64) if len(extras) else np.zeros(0, np.int64)
    if cfg["aux_null_within"]:
        rng = np.random.default_rng(int(OM.h_arr(pos_train, y_train.astype(np.int8), np.frombuffer(
            "|".join(cfg["aux_null_within"]).encode(), np.uint8))[:15], 16))
        cells_tr = ["\x1f".join(v) for v in zip(*[getattr(data.rows, c)[pos_train].astype(str)
                                                    for c in cfg["aux_null_within"]])]
        status_tr = OM.permute_within(status_tr, cells_tr, rng)
        if len(extras):
            cells_ex = ["\x1f".join(v) for v in zip(*[getattr(data.rows, c)[extras].astype(str)
                                                        for c in cfg["aux_null_within"]])]
            y_ex = OM.permute_within(y_ex, cells_ex, rng)
    audit.update({"extras_hash": OM.h_arr(extras), "n_extras": int(len(extras)),
                  "aux_shuffled": bool(cfg["aux_null_within"]), "extras": extras,
                  "extras_comp_ok": bool(np.isin(data.comp[extras], data.comp[pos_train]).all()
                                         and not np.isin(data.comp[extras], data.comp[pos_test]).any())})
    rows_fit = np.r_[pos_train, extras]
    n_tr = len(pos_train)
    Z, seg, pre_i, sel, is_pre, pad, idx, seg_np, _, A = OM._obs_tensors(torch, data, embs, layers, rows_fit, cfg)
    n_fit = len(rows_fit)
    W0 = np.zeros((len(layers), k, int(cfg["K"])), np.float32)
    pre_glob = idx[pre_i.numpy()]
    for li, L in enumerate(layers):
        Epre = embs[L].Z[pre_glob[:n_tr]]
        W0[li, :, 0] = OM.m0_direction(Epre, y_train, data.traj[pos_train], cfg["m0_C"])
    dist_fit = dist_test = None
    t4 = None
    if cfg["T4"]:
        Pfit = np.concatenate([embs[L].Z[pre_glob] for L in layers], 1)
        norm = np.nonzero(y_train == 0)[0]
        mu, prec = OM.gaussian_fit(Pfit[norm])
        t4 = {"mu": mu, "prec": prec}
        dist_fit = torch.tensor(OM.mahalanobis(Pfit, mu, prec), dtype=torch.float32)
        audit.update({"t4_rows_hash": OM.h_arr(pos_train[norm]), "t4_gaussians": 1,
                      "t4_rows_are_train_normals": bool(np.all(y_train[norm] == 0))})
    yt = torch.tensor(y_train, dtype=torch.float32)
    wb = torch.tensor(OM.bce_weights(y_train, data.tool[pos_train], data.source[pos_train], status_tr, cfg),
                      dtype=torch.float32)
    I, J, pw = OM.pair_index(y_train, data.traj[pos_train], data.tool[pos_train], status_tr, cfg)
    I_t, J_t, pw_t = torch.from_numpy(I), torch.from_numpy(J), torch.tensor(pw, dtype=torch.float32)
    gamma = OM.PREREG_ON["T1"]["focal_gamma"] if cfg["T1"] else 0.0
    use_aux = bool(cfg["T3"]) and len(extras) > 0
    if use_aux:
        ya = torch.tensor(y_ex, dtype=torch.float32)
        wa = torch.tensor(OM.class_balanced(y_ex), dtype=torch.float32)
    audit.update({"n_pairs": int(len(I)), "aux_used": use_aux})
    off_t = torch.tensor(off_train, dtype=torch.float32).unsqueeze(0)            # OFFSET [1, n_tr]
    model = ObsModelS(cfg, len(layers), k, W0, cfg["init_seeds"],
                      len(cfg["slots"]) * len(layers) * int(cfg["K"]) if cfg["T3"] else 0)
    opt = torch.optim.Adam(model.params, lr=float(cfg["lr"]))
    gen = torch.Generator().manual_seed(int(OM.h_arr(np.asarray(cfg["init_seeds"]))[:8], 16))
    drop = OM.PREREG_ON["T2"]["obs_drop"] if cfg["T2"] else 0.0
    noise = OM.PREREG_ON["T2"]["noise_rel"] if cfg["T2"] else 0.0
    sd_tr = Z[:, seg < n_tr].std(dim=1, keepdim=True) if noise else None
    base_mask = sel.unsqueeze(0).expand(R, -1)
    pre_ep = OM.PREREG_ON["T3"]["aux_pre_epochs"] if cfg["T3"] else 0
    static = {}
    bank = None
    aux_w = OM.PREREG_ON["T3"]["aux_w"]
    for ep in range(1, int(cfg["epochs"]) + 1):
        opt.zero_grad()
        mask = base_mask
        if drop:
            keep = torch.rand((R, len(sel)), generator=gen) >= drop
            mask = base_mask & (keep | is_pre.unsqueeze(0))
            if cfg["obs_subset"] == "nopre":
                left = OM.seg_sum(A, mask.to(torch.float32).unsqueeze(-1))[..., 0]
                mask = mask | ((left[:, seg] == 0) & base_mask)
        Zin = Z
        if noise:
            if bank is None:
                bank = torch.randn((8, R) + tuple(Z.shape), generator=gen)
            perm = torch.randperm(Z.shape[1], generator=gen)
            Zin = Z.unsqueeze(0) + noise * sd_tr.unsqueeze(0) * bank[ep % 8][:, :, perm, :]
        f, f_aux, _, _ = model.features(Zin, seg, n_fit, pre_i, mask, pad, dist_fit, A,
                                        None if (drop or noise) else static)
        reg = model.reg()
        if use_aux:
            l_aux = OM._loss_pointwise(torch, model.aux_head(f_aux[:, n_tr:, :]), ya, wa, 0.0) + \
                cfg["head_l2"] * (model.aux_w ** 2).sum(-1)
        if ep <= pre_ep:
            loss = (l_aux + reg) if use_aux else reg
        else:
            s = model.head(f[:, :n_tr, :], True) + off_t                         # OFFSET
            l_pt = OM._loss_pointwise(torch, s, yt, wb, gamma)
            l_pair = ((torch.nn.functional.softplus(-(s[:, I_t] - s[:, J_t])) * pw_t).sum(-1) / pw_t.sum()
                      if len(I) else torch.zeros(R))
            loss = l_pair + cfg["w_bce"] * l_pt + reg + (aux_w * l_aux if use_aux else 0.0)
        loss.sum().backward()
        opt.step()
    with torch.no_grad():
        f, _, _, _ = model.features(Z, seg, n_fit, pre_i, base_mask, pad, dist_fit, A, {})
        s_tr = model.head(f[:, :n_tr, :], False).mean(0).numpy().astype(np.float64) + off_train  # OFFSET
    norm_scores = s_tr[y_train == 0]
    thr = {far: float(np.quantile(norm_scores, 1.0 - far)) for far in OM.FARS}
    Zt, segt, pret, selt, _, padt, idxt, segt_np, startt, At = OM._obs_tensors(torch, data, embs, layers, pos_test,
                                                                                cfg)
    if cfg["T4"]:
        Ptest = np.concatenate([embs[L].Z[idxt[pret.numpy()]] for L in layers], 1)
        dist_test = torch.tensor(OM.mahalanobis(Ptest, t4["mu"], t4["prec"]), dtype=torch.float32)
    sc, am = OM._predict(torch, model, Zt, segt, len(pos_test), pret, selt, padt, dist_test, segt_np, startt, At)
    score = sc.astype(np.float64).mean(0) + off_test                              # OFFSET (float64)
    audit["scoring_inputs"] = ("z(obs), obs selection mask, pre index" + (", T4 Gaussian" if cfg["T4"] else "") +
                               ", fixed offset (pooled T7-a features of the scored row)")
    audit["residual_abs_max"] = float(np.abs(sc).max()) if sc.size else 0.0
    if cfg.get("mlp_act", "tanh") != "tanh":
        audit["head_activation"] = cfg["mlp_act"]
    return OM.FitOut(score, (sc.astype(np.float64) + off_test[None, :]).astype(np.float32), thr, am, audit,
                     ParamsOnly(dict(cfg), model.numpy_params()) if keep_model else None)


def make_fp_s(data, cfg, base=None, threads=None):
    def fp(pos_train, y_train, pos_test):
        return fit_s(data, cfg, pos_train, y_train, pos_test, base=base, threads=threads).score
    return fp

"""ArgusScorer: inference package for the phase-3 observation models (r4 §3 "추론 패키지", candidate=false).

Folding (exact, everything after the clip is affine):
  x~ = clip((x - med) / scale, +-clip)                         raw block output x [H=2880] -> x~
  u  = (x~ - mean512) @ P512                                   (the cache stores u in fp16)
  z  = ((u - mu32) @ Q) / sd                                   in-fold PCA 32 + standardisation
  h  = z @ W  =  x~ @ W_eff + b_eff,  W_eff = P512 Q diag(1/sd) W  [H, K],  b_eff = -(mean512 P512 + mu32) Q diag(1/sd) W
  z  = x~ @ Z_eff + z_b  is also stored (attention pooling / T4 distance need z).
Per replica (init seed) r: W_eff[r]; score = mean over replicas of the head output.

API (no tool / source / label argument anywhere):
  score_step(obs: {L: [n, H]}, kinds, token_index=None, token_pieces=None) -> dict
  start() -> state;  update(state, {L: [H]}, kind, token_index=None) -> provisional dict;  finalize(state) -> dict
  score_step == start + update per row + finalize (bit-identical by construction).
Observations off the 32-token grid (``reasoning+N``, N % 32 != 0) are skipped (8-grid captures are thinned).
Output: score, percentile (mid-rank among training scores), decision ("block" if score >= threshold), argmax
observation (index, kind, token_index) of the filter that contributes most to the max slot, optional reasoning
text window (the 32 token pieces before that observation).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from types import SimpleNamespace

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop.argus_loop import obs_cache as OC  # noqa: E402
from experiments.risk_loop.argus_loop import obs_models as OM  # noqa: E402

FORMAT = "argus-v1-obs-scorer-1"
WINDOW = 32


class ArgusScorer:
    def __init__(self, tensors: dict, meta: dict):
        self.t = {k: np.asarray(v) for k, v in tensors.items()}
        self.meta = meta
        self.layers = [int(L) for L in meta["layers"]]
        self.cfg = meta["cfg"]
        n_head = int(meta["n_head_layers"])
        params = {"W": None, "head_w": [self.t[f"head.w{i}"] for i in range(n_head)],
                  "head_b": [self.t[f"head.b{i}"] for i in range(n_head)]}
        if "attn.q" in self.t:
            params["q"] = self.t["attn.q"]
        t4 = {"mu": self.t["t4.mu"], "prec": self.t["t4.prec"]} if "t4.mu" in self.t else None
        self._m = SimpleNamespace(cfg=self.cfg, params=params, t4=t4)
        self.hidden = int(self.t[f"L{self.layers[0]}.med"].shape[0])
        self.train_scores = np.sort(self.t["cal.train_scores"].astype(np.float64))
        self.threshold = float(meta["threshold"])

    # ------------------------------------------------------------------ build / io
    @classmethod
    def from_fitted(cls, fitted: "OM.FittedObsModel", bases: dict, threshold: float, meta: dict | None = None):
        t, cfg = {}, fitted.cfg
        for li, L in enumerate(fitted.layers):
            b = bases[L]
            QS = (fitted.Q[L].astype(np.float64) / fitted.sd[L].astype(np.float64))      # [D, k]
            Zeff = b.P.astype(np.float64) @ QS                                             # [H, k]
            zb = -(b.mean.astype(np.float64) @ b.P.astype(np.float64) + fitted.mu[L]) @ QS  # [k]
            W = fitted.params["W"][:, li].astype(np.float64)                               # [R, k, K]
            t[f"L{L}.med"], t[f"L{L}.scale"] = b.med, b.scale
            t[f"L{L}.clip"] = np.asarray([b.clip], np.float32)
            t[f"L{L}.W_eff"] = np.einsum("hd,rdk->rhk", Zeff, W)
            t[f"L{L}.b_eff"] = np.einsum("d,rdk->rk", zb, W)
            t[f"L{L}.Z_eff"], t[f"L{L}.z_b"] = Zeff, zb
            # unfolded copy (cache-path parity checks)
            t[f"L{L}.mu32"], t[f"L{L}.Q"], t[f"L{L}.sd"], t[f"L{L}.W"] = fitted.mu[L], fitted.Q[L], fitted.sd[L], W
        for i, (w, bb) in enumerate(zip(fitted.params["head_w"], fitted.params["head_b"])):
            t[f"head.w{i}"], t[f"head.b{i}"] = w, bb
        if "q" in fitted.params:
            t["attn.q"] = fitted.params["q"]
        if fitted.t4 is not None:
            t["t4.mu"], t["t4.prec"] = fitted.t4["mu"], fitted.t4["prec"]
        t["cal.train_scores"] = np.asarray(fitted.train_scores, np.float64)
        m = {"format": FORMAT, "candidate": False, "layers": list(fitted.layers), "observe_every": 32,
             "grid_rule": "pre_reasoning|reasoning_end|pre_action + reasoning+N with N%32==0",
             "K": int(cfg["K"]), "n_replicas": int(fitted.params["W"].shape[0]),
             "n_head_layers": len(fitted.params["head_w"]), "threshold": float(threshold),
             "cfg": {k: (list(v) if isinstance(v, tuple) else v) for k, v in cfg.items()},
             "config_id": OM.config_id(cfg), "combo": OM.combo_name(cfg)}
        m.update(meta or {})
        return cls(t, m)

    def save(self, prefix) -> list[Path]:
        prefix = Path(prefix)
        prefix.parent.mkdir(parents=True, exist_ok=True)
        arrs = {k: np.ascontiguousarray(v) for k, v in self.t.items()}
        try:
            from safetensors.numpy import save_file
            p = prefix.with_suffix(".safetensors")
            save_file(arrs, str(p))
        except ImportError:  # pragma: no cover
            p = prefix.with_suffix(".npz")
            np.savez(p, **arrs)
        j = prefix.with_suffix(".json")
        j.write_text(json.dumps(self.meta, indent=1, ensure_ascii=False), encoding="utf-8")
        return [p, j]

    @classmethod
    def load(cls, prefix) -> "ArgusScorer":
        prefix = Path(prefix)
        meta = json.loads(prefix.with_suffix(".json").read_text(encoding="utf-8"))
        if meta.get("format") != FORMAT:
            raise ValueError(f"unknown scorer format {meta.get('format')!r}")
        st = prefix.with_suffix(".safetensors")
        if st.is_file():
            from safetensors.numpy import load_file
            t = load_file(str(st))
        else:
            with np.load(prefix.with_suffix(".npz")) as z:
                t = {k: z[k] for k in z.files}
        return cls(t, meta)

    # ------------------------------------------------------------------ per-observation math
    def _row(self, L: int, x) -> tuple[np.ndarray, np.ndarray]:
        x = np.asarray(x, dtype=np.float32).reshape(-1)
        if x.shape[0] != self.hidden:
            raise ValueError(f"layer {L}: observation must have {self.hidden} values, got {x.shape[0]}")
        if not np.isfinite(x).all():
            raise ValueError(f"layer {L}: non-finite values (fp16 overflow?)")
        t = self.t
        xt = np.clip((x - t[f"L{L}.med"]) / t[f"L{L}.scale"], -float(t[f"L{L}.clip"][0]),
                     float(t[f"L{L}.clip"][0])).astype(np.float64)
        h = np.einsum("h,rhk->rk", xt, t[f"L{L}.W_eff"]) + t[f"L{L}.b_eff"]
        z = xt @ t[f"L{L}.Z_eff"] + t[f"L{L}.z_b"]
        return h, z

    # ------------------------------------------------------------------ streaming
    def start(self) -> dict:
        R, K = int(self.meta["n_replicas"]), int(self.meta["K"])
        C = K * len(self.layers)
        return {"h": [], "z": [], "kinds": [], "tokens": [], "skipped": 0, "n": 0,
                "run_max": np.full((R, C), -np.inf), "run_sum": np.zeros((R, C)), "run_argmax": np.zeros((R, C), int)}

    def update(self, state: dict, obs: dict, kind: str, token_index=None) -> dict:
        if not OC.grid32_keep([kind])[0]:
            state["skipped"] += 1
            return {"skipped": True, "n_obs": state["n"]}
        missing = [L for L in self.layers if L not in obs]
        if missing:
            raise ValueError(f"missing layer(s) {missing}")
        hs, zs = zip(*[self._row(L, obs[L]) for L in self.layers])
        h = np.concatenate(hs, -1)  # [R, C]
        state["h"].append(hs)
        state["z"].append(zs)
        state["kinds"].append(str(kind))
        state["tokens"].append(None if token_index is None else int(token_index))
        better = h > state["run_max"]
        state["run_argmax"][better] = state["n"]
        state["run_max"] = np.maximum(state["run_max"], h)
        state["run_sum"] += h
        state["n"] += 1
        return {"skipped": False, "n_obs": state["n"], "provisional": self._finish(state, provisional=True)["score"]}

    def _finish(self, state, provisional=False, token_pieces=None, text_offset=0) -> dict:
        if state["n"] == 0:
            raise ValueError("no observation on the 32 grid")
        n = state["n"]
        h_layers = [np.stack([state["h"][i][li] for i in range(n)], 1) for li in range(len(self.layers))]
        z_layers = [np.stack([state["z"][i][li] for i in range(n)], 0) for li in range(len(self.layers))]
        kinds = list(state["kinds"])
        out = OM.score_from_h(self._m, h_layers, z_layers, kinds)
        s = out["score"]
        lo = np.searchsorted(self.train_scores, s, "left")
        hi = np.searchsorted(self.train_scores, s, "right")
        res = {"score": float(s), "scores_rep": out["scores_rep"].tolist(),
               "percentile": float((lo + hi) / (2.0 * len(self.train_scores))),
               "decision": "block" if s >= self.threshold else "pass", "threshold": self.threshold,
               "n_obs": n, "skipped_off_grid": state["skipped"], "pre_index": out["pre_index"],
               "fallback_pre": out["fallback_pre"], "provisional": provisional}
        a = out["argmax_obs"]
        if a is not None:
            res["argmax_obs"] = {"index": int(a), "kind": kinds[a], "token_index": state["tokens"][a]}
            ti = state["tokens"][a]
            if token_pieces is not None and ti is not None:
                e = max(0, int(ti) - int(text_offset))
                res["argmax_obs"]["text_window"] = "".join(token_pieces[max(0, e - WINDOW):e])
        return res

    def finalize(self, state: dict, token_pieces=None, text_offset: int = 0) -> dict:
        return self._finish(state, False, token_pieces, text_offset)

    # ------------------------------------------------------------------ batch
    def score_step(self, obs: dict, kinds, token_index=None, token_pieces=None, text_offset: int = 0) -> dict:
        kinds = list(kinds)
        arrs = {}
        for L in self.layers:
            if L not in obs:
                raise ValueError(f"missing layer {L}")
            a = np.asarray(obs[L])
            if a.ndim != 2 or a.shape[0] != len(kinds):
                raise ValueError(f"layer {L}: expected [{len(kinds)}, {self.hidden}], got {a.shape}")
            arrs[L] = a
        st = self.start()
        for i, kd in enumerate(kinds):
            self.update(st, {L: arrs[L][i] for L in self.layers}, kd,
                        None if token_index is None else token_index[i])
        return self.finalize(st, token_pieces, text_offset)

    def score_cache_rows(self, u_by_layer: dict, kinds) -> float:
        """Unfolded path from PCA-512 cache rows (parity reference): z = ((u - mu32) @ Q) / sd, h = z @ W."""
        keep = OC.grid32_keep(kinds)
        kinds = [k for k, m in zip(kinds, keep) if m]
        h_layers, z_layers = [], []
        for L in self.layers:
            u = np.asarray(u_by_layer[L], np.float64)[keep]
            z = ((u - self.t[f"L{L}.mu32"]) @ self.t[f"L{L}.Q"]) / self.t[f"L{L}.sd"]
            z_layers.append(z)
            h_layers.append(np.einsum("nd,rdk->rnk", z, self.t[f"L{L}.W"]))
        return float(OM.score_from_h(self._m, h_layers, z_layers, kinds)["score"])

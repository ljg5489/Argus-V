"""Argus-V-emp as model files: load once, then score any call from its two pooled hidden-state vectors. Fits nothing.

The model folder (artifacts/risk-loop/resplit-1117/argus_v_emp/, not in git) is written by argus_v_emp_export.py:
  em/<model>_<weight>_r<k>_e067.pt   the 36 Argus-V-em models (copies of run01/em/checkpoints)
  P3.pkl, P5.pkl                     the two Argus-V-p models: scaling, PCA, linear members, random forest, training-score tables
  reference_validation.npz           for each of the 38 models: its scores of the 3,217 validation calls, sorted
  manifest.json                      definition, cut-offs, file hashes, library versions, the check against the saved scores

Input of one call: x23 = layer 23, maximum over the observation positions (2,880 values) and x16 = layer 16 just before
the action (2,880 values). No tool name, step number or collection period enters.

Score of one call (argus_v_emp.py has the definition):
  each of the 38 models scores the call -> that score becomes the share of the validation calls this model scored lower
  -> the 36 Argus-V-em shares are averaged (part 1) -> (part 1 + P3 share + P5 share) / 3, a value between 0 and 1.
The value is a rank-type score, not a probability. A call is judged a violation when its score is above a cut-off
(manifest: 5% = the score above which 5% of the validation normal calls lie).

Usage:
    from experiments.risk_loop.argus_loop import argus_v_emp_model as EMPM
    model = EMPM.EmpModel()                      # loads the files once
    scores = model.score(x23, x16)               # arrays [n, 2880] each (one call: n = 1)
    alarm = scores > model.cut["5%"]
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

for _name in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ.setdefault(_name, "2")

import numpy as np  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

BUNDLE = ROOT / "artifacts" / "risk-loop" / "resplit-1117" / "argus_v_emp"
CHUNK = 4096                       # rows per transform call, as in iter07_models.robust_embed


def share_below(ref_sorted: np.ndarray, s: np.ndarray) -> np.ndarray:
    """For each score: the share of the (sorted) reference scores below it; ties count half."""
    s = np.asarray(s, dtype=np.float64)
    return (np.searchsorted(ref_sorted, s, side="left") + np.searchsorted(ref_sorted, s, side="right")) / (2.0 * len(ref_sorted))


class PModel:
    """One Argus-V-p setting as fitted objects (see argus_v_emp_export.fit_setting for what each piece is)."""

    def __init__(self, d: dict):
        self.d = d

    def embed(self, rep: str, X) -> np.ndarray:
        e = self.d["embed"][rep]
        out = np.empty((len(X), e["pca"].n_components_), dtype=np.float32)
        for i in range(0, len(X), CHUNK):
            out[i:i + CHUNK] = e["pca"].transform(np.clip((np.asarray(X[i:i + CHUNK], dtype=np.float32) - e["median"]) / e["scale"], -e["clip"], e["clip"]))
        return out

    def score_embedded(self, E: dict, rows=None) -> np.ndarray:
        """E: rep -> embedding of the rows; the setting's own 0-1 score (mean training percentile of its members)."""
        take = (lambda a: a) if rows is None else (lambda a: a[rows])
        tot = None
        for m in self.d["members"]:
            s = take(E[m["rep"]][:, :m["k"]]).astype(np.float64) @ m["w"]
            p = share_below(m["train_scores_sorted"], s)
            tot = p if tot is None else tot + p
        tot = tot / len(self.d["members"])
        rf = self.d.get("rf")
        if rf is not None:
            X = np.hstack([take(E[rep][:, :k]) for rep, k in rf["reps"]]).astype(np.float32)
            p = rf["forest"].predict_proba(X)[:, rf["positive_column"]].astype(np.float64)
            tot = (1.0 - rf["weight"]) * tot + rf["weight"] * share_below(rf["train_proba_sorted"], p)
        return tot

    def score(self, x23, x16) -> np.ndarray:
        return self.score_embedded({"L23:max": self.embed("L23:max", x23), "L16:pre": self.embed("L16:pre", x16)})


class EmpModel:
    """Argus-V-emp loaded from its model folder."""

    def __init__(self, bundle: Path = BUNDLE):
        import joblib
        import torch
        from experiments.risk_loop.argus_loop import argus_v_em as EM

        self.bundle = Path(bundle)
        self.manifest = json.loads((self.bundle / "manifest.json").read_text(encoding="utf-8"))
        ref = np.load(self.bundle / "reference_validation.npz", allow_pickle=False)
        self.ref = {k: ref[k].astype(np.float64) for k in ref.files}
        self._torch, self._scale = torch, EM.robust_scale
        self.em = []
        for name in self.manifest["argus_v_em_models"]:
            ck = torch.load(self.bundle / "em" / f"{name}_e{self.manifest['argus_v_em_epoch']:03d}.pt", map_location="cpu", weights_only=False)
            w = int(ck["width"])
            m = EM.LearnedEmbedding(int(ck["input_width"]), w) if w > 0 else EM.LinearScorer(int(ck["input_width"]))
            m.load_state_dict(ck["state_dict"])
            m.eval()
            self.em.append((name, m, np.asarray(ck["median"], dtype=np.float32), np.asarray(ck["scale"], dtype=np.float32)))
        self.p = {sid: PModel(joblib.load(self.bundle / f"{sid}.pkl")) for sid in self.manifest["argus_v_p_settings"]}
        self.cut = dict(self.manifest["cut_offs"])

    def em_scores(self, x23, x16) -> dict:
        """Raw score of every Argus-V-em model (the output of its last layer)."""
        x = np.concatenate([np.asarray(x23, dtype=np.float32), np.asarray(x16, dtype=np.float32)], axis=1)
        out = {}
        with self._torch.no_grad():
            for name, m, med, sc in self.em:
                out[name] = m(self._torch.from_numpy(self._scale(x, med, sc))).reshape(-1).numpy().astype(np.float64)
        return out

    def parts(self, x23, x16) -> dict:
        """The three averaged parts of the mix, each between 0 and 1."""
        em = self.em_scores(x23, x16)
        out = {"em": np.mean([share_below(self.ref[name], s) for name, s in em.items()], axis=0)}
        for sid, pm in self.p.items():
            out[sid] = share_below(self.ref[sid], pm.score(x23, x16))
        return out

    def score(self, x23, x16) -> np.ndarray:
        """Argus-V-emp score of every given call, between 0 and 1 (a rank-type score, not a probability)."""
        p = self.parts(x23, x16)
        return (p["em"] + sum(p[sid] for sid in self.p)) / (1 + len(self.p))

    def judge(self, scores, cut: str = "5%") -> np.ndarray:
        """True where the score is above the cut-off (judged a violation)."""
        return np.asarray(scores) > self.cut[cut]

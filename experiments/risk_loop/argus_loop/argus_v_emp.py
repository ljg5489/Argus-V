"""Argus-V-emp: Argus-V-em and Argus-V-p mixed. Name given by the user on 2026-11-17
("섞은 모델을 Argus-V-emp로 이름잡고 그것으로 다시 전체 test 진행해봐").

Definition (fixed on 2026-11-17, before the full test read-out of the mix):
  components  the 12 Argus-V-em settings of resplit-1117 / run01 (32-, 64-, 128-dim and the linear control, each with the
              violation weights about 15x, about 60x and 300x; three repeats each; epoch 67) and the Argus-V-p settings
              P3 and P5 of the same run. Every component was fitted on the new train split only.
  per call    each component score is turned into the share of the validation calls that this component scored lower
              (a fixed reference that uses no label). The 36 Argus-V-em shares are averaged; that average, the P3 share
              and the P5 share are then averaged with equal weight. The result is between 0 and 1.
Nothing is fitted here and no label enters the mix.

How the mix was found: an exploratory comparison of 16 label-free variants on validation and test
(resplit_run01_levers.py, variant 4b); this one was the highest on validation. In that comparison the shares were
ranks inside the scored split; here they are taken against the validation calls, so that a single new call can be scored.

To score a new call outside the saved splits the components must exist as model files. The Argus-V-em ones do
(artifacts/risk-loop/resplit-1117/run01/em/checkpoints/*_e067.pt); P3 and P5 were only scored, not exported.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

for _name in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ.setdefault(_name, "2")

import numpy as np  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from experiments.risk_loop.argus_loop import resplit_run01 as R  # noqa: E402

NAME = "Argus-V-emp"
NAME_KO = "Argus-V-emp (Argus-V-em 12개 설정과 Argus-V-p P3·P5를 섞은 모델)"
EPOCH = R.FIXED_EPOCH
P_SETTINGS = ("P3", "P5")
REFERENCE = "validation"
REPORT = ROOT / "reports" / "risk-loop" / "argus-v-emp"
_CACHE: dict = {}


def components() -> dict:
    """Saved scores of every component: Argus-V-em [epoch][row] per split, Argus-V-p [row] per split."""
    if not _CACHE:
        for arch in R.ARCHS:
            for w in R.WEIGHT_RULES:
                for k in R.REPEATS:
                    z = np.load(R.OUT / "em" / f"{arch}_{w}_r{k}.npz", allow_pickle=False)
                    _CACHE[(f"{arch}_{w}", k)] = {"validation": z["scores_validation"], "test": z["scores_test"]}
        for sid in P_SETTINGS:
            z = np.load(R.OUT / "p" / f"{sid}.npz", allow_pickle=False)
            _CACHE[sid] = {"validation": z["scores_validation"], "test": z["scores_test"]}
    return _CACHE


def share_below(reference: np.ndarray, s: np.ndarray) -> np.ndarray:
    """For each score: the share of the reference scores below it (ties count half)."""
    ref = np.sort(np.asarray(reference, dtype=np.float64))
    s = np.asarray(s, dtype=np.float64)
    return (np.searchsorted(ref, s, side="left") + np.searchsorted(ref, s, side="right")) / (2.0 * len(ref))


def parts(split: str, epoch: int = EPOCH, reference: str = REFERENCE) -> dict:
    """The three averaged parts of the mix for the rows of ``split``. reference='self' ranks inside the split itself."""
    C = components()
    ref = split if reference == "self" else reference
    em = [share_below(c[ref][epoch - 1], c[split][epoch - 1]) for key, c in C.items() if isinstance(key, tuple)]
    out = {"em": np.mean(em, axis=0)}
    for sid in P_SETTINGS:
        out[sid] = share_below(C[sid][ref], C[sid][split])
    return out


def scores(split: str, epoch: int = EPOCH, reference: str = REFERENCE) -> np.ndarray:
    """Argus-V-emp score of every call of ``split`` (new split resplit-1117), between 0 and 1."""
    p = parts(split, epoch, reference)
    return (p["em"] + sum(p[sid] for sid in P_SETTINGS)) / (1 + len(P_SETTINGS))


def describe() -> dict:
    C = components()
    return {"name": NAME, "argus_v_em_score_sets": sum(isinstance(k, tuple) for k in C), "argus_v_em_settings": [f"{a}_{w}" for a in R.ARCHS for w in R.WEIGHT_RULES],
            "argus_v_em_repeats": list(R.REPEATS), "argus_v_em_epoch": EPOCH, "argus_v_p_settings": list(P_SETTINGS),
            "reference_for_shares": REFERENCE, "weights": "Argus-V-em average 1/3, P3 1/3, P5 1/3",
            "split": "resplit-1117 (components fitted on its train split only)"}

"""Reader for the per-observation PCA-512 cache (phase 3, prereg iter-13/prereg.md §1).

Format (``artifacts/risk-loop/argus-v1-loop/obs_cache/``, built by the data engineer):
  obs_L{LL}.npy    float16 [N_obs, D]  (D = 512) robust-scaled + clipped + PCA-512-projected observation rows
  obs_index.csv    obs_id,row,order,kind,token_index   (one line per obs row, obs_id = row position in obs_L*)
  offsets.npy      int64 [n_steps + 1]  obs rows of step slot s are offsets[s]:offsets[s+1]
  step_rows.npy    int64 [n_steps]      steps.csv ``row`` id of each step slot
  basis_L{LL}.npz  label-free basis: median, scale (IQR/1.349) or iqr, clip, mean, PCA-512 components
  manifest.json    free-form build record (sha256 map checked when ``verify=True``)

Access rule: rows are only handed out for an explicit allow-list (the train rows returned by the frozen
``evaluate.load``), so validation / test / sealed rows in the cache can never reach a model by accident.
Observation thinning: the 32-token grid (``pre_reasoning``, ``reasoning_end``, ``pre_action`` and
``reasoning+N`` with N % 32 == 0). Unknown kinds raise.
"""
from __future__ import annotations

import csv
import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
CACHE_DIR = REPO_ROOT / "artifacts" / "risk-loop" / "argus-v1-loop" / "obs_cache"
FIXED_KINDS = ("pre_reasoning", "reasoning_end", "pre_action")
KIND_CODES = {"pre_reasoning": 0, "reasoning": 1, "reasoning_end": 2, "pre_action": 3}
_REASONING = re.compile(r"^reasoning\+(\d+)$")
IQR_TO_SD = 1.349


def grid32_keep(kinds, every: int = 32) -> np.ndarray:
    """Bool mask of observation kinds kept on the ``every``-token grid. Unknown kinds raise ValueError."""
    out = np.zeros(len(kinds), dtype=bool)
    for i, k in enumerate(kinds):
        k = str(k)
        if k in FIXED_KINDS:
            out[i] = True
            continue
        m = _REASONING.match(k)
        if not m:
            raise ValueError(f"unknown observation kind {k!r}")
        out[i] = int(m.group(1)) % every == 0
    return out


def kind_code(kind: str) -> int:
    return KIND_CODES["reasoning"] if _REASONING.match(str(kind)) else KIND_CODES[str(kind)]


# ---------------------------------------------------------------------------------------------- basis

@dataclass
class Basis:
    """x (raw block output, [n, H]) -> u = (clip((x - med) / scale, +-clip) - mean) @ P, P [H, D]."""
    med: np.ndarray
    scale: np.ndarray
    clip: float
    mean: np.ndarray
    P: np.ndarray

    @property
    def hidden(self) -> int:
        return int(self.P.shape[0])

    @property
    def dim(self) -> int:
        return int(self.P.shape[1])

    def scale_clip(self, x: np.ndarray) -> np.ndarray:
        x = np.asarray(x, dtype=np.float32)
        if x.ndim != 2 or x.shape[1] != self.hidden:
            raise ValueError(f"raw rows must be [n, {self.hidden}], got {x.shape}")
        if not np.isfinite(x).all():
            raise ValueError("raw rows contain non-finite values (fp16 overflow?)")
        return np.clip((x - self.med) / self.scale, -self.clip, self.clip)

    def project(self, x: np.ndarray) -> np.ndarray:
        return ((self.scale_clip(x) - self.mean) @ self.P).astype(np.float32)


_ALIASES = {"med": ("med", "median", "center_median"), "scale": ("scale", "iqr_sd", "robust_scale"),
            "iqr": ("iqr",), "clip": ("clip", "clip_value"), "mean": ("mean", "mu", "pca_mean", "center"),
            "components": ("components", "components_", "pca_components"), "P": ("P", "proj", "projection")}


def _pick(z, name):
    for k in _ALIASES[name]:
        if k in z.files:
            return np.asarray(z[k])
    return None


def load_basis(path: Path | str) -> Basis:
    """Accepts sklearn-style ``components`` [D, H] or a projection ``P`` [H, D]; ``scale`` or ``iqr``."""
    with np.load(path) as z:
        med, scale, iqr, clip = _pick(z, "med"), _pick(z, "scale"), _pick(z, "iqr"), _pick(z, "clip")
        mean, comp, P = _pick(z, "mean"), _pick(z, "components"), _pick(z, "P")
        files = list(z.files)
    if med is None or (scale is None and iqr is None) or (comp is None and P is None):
        raise ValueError(f"{path}: basis keys not recognised ({files}); need median, scale|iqr, components|P")
    if scale is None:
        scale = iqr / IQR_TO_SD
    scale = np.asarray(scale, dtype=np.float32).copy()
    scale[~(scale > 1e-12)] = 1.0
    P = np.asarray(P if P is not None else comp.T, dtype=np.float32)
    if P.shape[0] != med.shape[0]:
        raise ValueError(f"{path}: projection {P.shape} does not match median {med.shape}")
    mean = np.zeros(P.shape[0], np.float32) if mean is None else np.asarray(mean, dtype=np.float32)
    return Basis(np.asarray(med, np.float32), scale, float(3.0 if clip is None else np.asarray(clip).ravel()[0]),
                 mean, np.ascontiguousarray(P))


# ---------------------------------------------------------------------------------------------- cache

@dataclass
class Gathered:
    """Observation rows of an ordered list of step rows, thinned to the 32 grid."""
    row_ids: np.ndarray       # [n] steps.csv row ids (input order)
    obs_ids: np.ndarray       # [N] global obs ids (rows of obs_L*.npy)
    off: np.ndarray           # [n + 1] local offsets
    pre_local: np.ndarray     # [n] local obs position of the pre_action row (last row if none)
    kind: np.ndarray          # [N] str kinds
    kind_code: np.ndarray     # [N] int8 (KIND_CODES)
    token_index: np.ndarray   # [N] int64
    n_obs32: np.ndarray       # [n]
    pre_fallback: int         # steps without a pre_action row


class ObsCache:
    def __init__(self, root: Path | str = CACHE_DIR, verify: bool = False):
        self.root = Path(root)
        mp = self.root / "manifest.json"
        self.manifest = json.loads(mp.read_text(encoding="utf-8")) if mp.is_file() else {}
        self.offsets = np.asarray(np.load(self.root / "offsets.npy"), dtype=np.int64)
        self.step_rows = np.asarray(np.load(self.root / "step_rows.npy"), dtype=np.int64)
        idx = {"obs_id": [], "row": [], "order": [], "kind": [], "token_index": []}
        with open(self.root / "obs_index.csv", newline="", encoding="utf-8") as h:
            for r in csv.DictReader(h):
                for k in idx:
                    idx[k].append(r[k])
        self.obs_id = np.asarray(idx["obs_id"], dtype=np.int64)
        self.obs_row = np.asarray(idx["row"], dtype=np.int64)
        self.obs_order = np.asarray(idx["order"], dtype=np.int64)
        self.obs_kind = np.asarray(idx["kind"], dtype=object)
        self.obs_token = np.asarray([int(float(t)) if str(t).strip() not in ("", "nan") else -1
                                     for t in idx["token_index"]], dtype=np.int64)
        self._check()
        self.slot_of_row = {int(r): s for s, r in enumerate(self.step_rows.tolist())}
        self._layers: dict[int, np.ndarray] = {}
        if verify:
            self.verify_sha()

    @property
    def n_obs(self) -> int:
        return int(self.offsets[-1])

    def _check(self) -> None:
        o, n = self.offsets, len(self.step_rows)
        if len(o) != n + 1 or o[0] != 0 or np.any(np.diff(o) < 0):
            raise ValueError("offsets must be non-decreasing, start at 0 and have n_steps + 1 entries")
        if len(self.obs_id) != o[-1] or not np.array_equal(self.obs_id, np.arange(o[-1])):
            raise ValueError("obs_index.csv obs_id must be 0..N_obs-1 in file order")
        if len(set(self.step_rows.tolist())) != n:
            raise ValueError("step_rows has duplicate rows")
        if np.any(np.diff(o) == 0):
            raise ValueError("a step slot has no observation rows")
        slot = np.repeat(np.arange(n), np.diff(o))
        if not np.array_equal(self.obs_row, self.step_rows[slot]):
            raise ValueError("obs_index.csv row column does not match step_rows/offsets")
        first = o[:-1][slot]
        if not np.array_equal(self.obs_order, np.arange(o[-1]) - first):
            raise ValueError("obs_index.csv order must be 0..n-1 inside each step")

    def verify_sha(self) -> dict:
        exp = self.manifest.get("sha256") or {}
        out = {}
        for name, sha in exp.items():
            p = self.root / name
            if p.is_file():
                h = hashlib.sha256()
                with open(p, "rb") as f:
                    for chunk in iter(lambda: f.read(1 << 24), b""):
                        h.update(chunk)
                out[name] = h.hexdigest() == sha
                if not out[name]:
                    raise ValueError(f"sha256 mismatch for {name}")
        return out

    def layer(self, L: int) -> np.ndarray:
        if L not in self._layers:
            arr = np.load(self.root / f"obs_L{int(L):02d}.npy", mmap_mode="r")
            if arr.ndim != 2 or arr.shape[0] != self.n_obs:
                raise ValueError(f"obs_L{L:02d}.npy has shape {arr.shape}, index has {self.n_obs} rows")
            self._layers[L] = arr
        return self._layers[L]

    def basis(self, L: int) -> Basis:
        return load_basis(self.root / f"basis_L{int(L):02d}.npz")

    def gather(self, row_ids, allowed_row_ids, grid32: bool = True) -> Gathered:
        row_ids = np.asarray(row_ids, dtype=np.int64)
        allowed = set(int(r) for r in np.asarray(allowed_row_ids).tolist())
        bad = [int(r) for r in row_ids.tolist() if r not in allowed]
        if bad:
            raise PermissionError(f"{len(bad)} requested rows are not allowed train rows (e.g. {bad[:5]})")
        missing = [int(r) for r in row_ids.tolist() if r not in self.slot_of_row]
        if missing:
            raise KeyError(f"{len(missing)} rows are not in the observation cache (e.g. {missing[:5]})")
        obs, off, pre, nobs, fb = [], [0], [], [], 0
        for r in row_ids.tolist():
            s = self.slot_of_row[r]
            ids = np.arange(self.offsets[s], self.offsets[s + 1])
            kinds = self.obs_kind[ids]
            if grid32:
                ids = ids[grid32_keep(kinds)]
                kinds = self.obs_kind[ids]
            if len(ids) == 0:
                raise ValueError(f"row {r}: no observation left on the 32 grid")
            p = np.nonzero(kinds == "pre_action")[0]
            if len(p) == 0:
                fb += 1
            pre.append(off[-1] + (int(p[-1]) if len(p) else len(ids) - 1))
            obs.append(ids)
            nobs.append(len(ids))
            off.append(off[-1] + len(ids))
        obs_ids = np.concatenate(obs) if obs else np.zeros(0, np.int64)
        kinds = self.obs_kind[obs_ids]
        return Gathered(row_ids, obs_ids, np.asarray(off, np.int64), np.asarray(pre, np.int64), kinds,
                        np.asarray([kind_code(k) for k in kinds.tolist()], np.int8), self.obs_token[obs_ids],
                        np.asarray(nobs, np.int64), fb)

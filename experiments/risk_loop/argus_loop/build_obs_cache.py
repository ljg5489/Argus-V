"""Argus-V1 loop PER-OBSERVATION cache (TASK.md §6c, iter-13 r3-systems §2 / r4-executioner-final §3).

Every train/validation step's observation rows (32-token grid, layers 16/20/23, block-L residual stream,
2880 float32 each) are streamed from the HF Hub into RAM, robust-scaled + clipped and projected on a label-free
PCA-512 basis; only the projected float16 rows are written. Raw tensors never touch the disk; row groups are read
into memory (no local HF / fsspec cache), and test / sealed rows in shared row groups are never decoded
(same rule as build_features.process_group).

  x~ = clip((x - median_L) / (IQR_L / 1.349), -3, 3)       per coordinate, fitted on TRAIN rows only
  u  = (x~ - pca_mean_L) @ components_L.T  in R^512        label-free PCA, fitted on TRAIN rows only

Output  artifacts/risk-loop/argus-v1-loop/obs_cache/
  obs_L16.npy obs_L20.npy obs_L23.npy  float16 [N_obs, 512]   (row i = obs_index.csv obs_id i)
  obs_index.csv   obs_id, row (= steps.v2.csv row), order (0..n-1 within step), kind, token_index
  offsets.npy     int64 [n_steps + 1]: observations of step slot j are obs[offsets[j]:offsets[j+1]]
  step_rows.npy   int64 [n_steps]: steps.csv / steps.v2.csv row id of slot j (same order as steps.v2.csv)
  basis_L{LL}.npz median, scale, clip, pca_mean, components [512, 2880], explained_variance, ...
  manifest.json   revision, layers, counts, sha256 of every file, frozen basis hashes, checks
Build state (done lists, per-group stats) lives in OUT/obs_build/ (not part of the cache).

Stages (resumable):
  index    obs_index.csv / offsets.npy / step_rows.npy from meta/obs_points.jsonl (build_features.py points)
  fit      pass 1: random 30% of the row groups holding train rows -> robust scale + PCA-512 -> basis_L*.npz,
           sha256 frozen in obs_build/basis_frozen.json (refuses to refit once frozen). Not resumable midway
           (the fit sample lives in RAM only); rerun from scratch on failure.
  project  pass 2: every needed row group -> obs_L*.npy (fp16 memmap), per-group done list
  finalize NaN check, pooled-feature cross-check summary, sha256 -> manifest.json

  py -3.11 experiments/risk_loop/argus_loop/build_obs_cache.py index
  py -3.11 experiments/risk_loop/argus_loop/build_obs_cache.py fit --workers 6
  py -3.11 experiments/risk_loop/argus_loop/build_obs_cache.py project --workers 6
  py -3.11 experiments/risk_loop/argus_loop/build_obs_cache.py finalize
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import shutil
import sys
import time
from collections import Counter
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
from pathlib import Path

os.environ.setdefault("HF_XET_CHUNK_CACHE_SIZE_BYTES", "0")  # no on-disk xet chunk cache

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_features as bf  # noqa: E402

OUT = bf.OUT
OBS = OUT / "obs_cache"
STATE = OUT / "obs_build"
LOG = OUT / "obs_build.log"
LAYERS = (16, 20, 23)
DIM = 512
CLIP = 3.0
IQR_TO_SIGMA = 1.349
FIT_FRACTION = 0.30
FIT_CAP = 30_000          # max fit rows per layer (random subsample of the 30% row groups' train rows)
FIT_SEED = 0
REVISION = "57a4bdcd22a57e0dd5ac9f8b0c2dd61741867788"
MIN_FREE = 10 * 2**30     # user instruction 2026-11-09: stop (resumable) when free disk < 10 GB
MAX_TOTAL = 3 * 2**30     # TASK.md §2: features/ + obs_cache/ <= 3 GB
HF_CACHE = Path.home() / ".cache" / "huggingface"
STEPS_V2 = OUT / "labels/steps.v2.csv"


def say(*parts) -> None:
    line = time.strftime("%Y-%m-%d %H:%M:%S ") + " ".join(str(p) for p in parts)
    print(line, flush=True)
    with open(LOG, "a", encoding="utf-8") as fh:
        fh.write(line + "\n")


def dir_bytes(path: Path) -> int:
    tot = 0
    for root, _, files in os.walk(path):
        for f in files:
            try:
                tot += os.path.getsize(os.path.join(root, f))
            except OSError:
                pass
    return tot


def free_bytes() -> int:
    return shutil.disk_usage(bf.ROOT).free


class DiskWatch:
    """Free-space guard + peak-use tracker (min free seen). Stops cleanly below MIN_FREE."""

    def __init__(self):
        self.start_free = free_bytes()
        self.min_free = self.start_free
        self.hf0 = dir_bytes(HF_CACHE)
        self.tmp0 = dir_bytes(Path(os.environ.get("TEMP", "/tmp")))

    def check(self) -> int:
        f = free_bytes()
        self.min_free = min(self.min_free, f)
        if f < MIN_FREE:
            raise SystemExit(f"[abort] free disk {f / 2**30:.2f} GB < 10 GB (resumable: rerun the stage)")
        return f

    def report(self) -> dict:
        return {"free_at_start_gb": self.start_free / 2**30, "min_free_gb": self.min_free / 2**30,
                "peak_extra_use_gb": (self.start_free - self.min_free) / 2**30,
                "hf_cache_growth_mb": (dir_bytes(HF_CACHE) - self.hf0) / 2**20,
                "temp_growth_mb": (dir_bytes(Path(os.environ.get("TEMP", "/tmp"))) - self.tmp0) / 2**20}


# ---------------------------------------------------------------------- index
def load_steps() -> list[dict]:
    steps = bf.read_csv(STEPS_V2)
    old = bf.read_csv(bf.FEAT / "steps.csv")
    assert len(steps) == len(old)
    for a, b in zip(steps, old):
        assert (a["row"], a["unit_id"], a["step_index"], a["obs_kinds"]) == \
               (b["row"], b["unit_id"], b["step_index"], b["obs_kinds"]), a["row"]
    status = {r["row"]: r["features_complete"] for r in bf.read_csv(bf.FEAT / "row_status.csv")}
    return [s for s in steps if status.get(s["row"]) == "1"]


def step_points(steps: list[dict]) -> dict[int, dict]:
    """row -> raw kinds/token_index, observe_every, kept positions on the 32 grid (checked against meta)."""
    pts, meta = bf.load_points(), bf.load_meta()
    out = {}
    for s in steps:
        u, k = s["unit_id"], int(s["step_index"])
        p = pts[u]["steps"][k]
        every = int(pts[u]["observe_every"])
        if p["kinds"] != meta[u]["steps"][k]["obs_kinds"]:
            raise ValueError(f"kinds differ between rollout.json reads for {u}:{k}")
        if p["step_index"] != k or any(t is None for t in p["token_index"]):
            raise ValueError(f"bad points for {u}:{k}")
        keep = bf.grid32_keep(p["kinds"], every)
        kinds = [x for x, m in zip(p["kinds"], keep) if m]
        toks = [x for x, m in zip(p["token_index"], keep) if m]
        if kinds != s["obs_kinds"].split("|") or len(kinds) != int(s["n_obs"]):
            raise ValueError(f"32-grid kinds mismatch for row {s['row']}")
        if toks != sorted(set(toks)) or (kinds[-1] == "pre_action" and toks[-1] != int(s["prefix_length"]) - 1):
            raise ValueError(f"token order / pre_action position mismatch row {s['row']}")
        out[int(s["row"])] = {"every": every, "n_raw": len(p["kinds"]), "keep": np.nonzero(keep)[0],
                              "kinds": kinds, "token_index": toks, "split": s["split"]}
    return out


def stage_index(args) -> None:
    OBS.mkdir(parents=True, exist_ok=True)
    steps = load_steps()
    sp = step_points(steps)
    rows = [int(s["row"]) for s in steps]
    offsets = np.zeros(len(rows) + 1, np.int64)
    recs = []
    for j, r in enumerate(rows):
        p = sp[r]
        for o, (kd, t) in enumerate(zip(p["kinds"], p["token_index"])):
            recs.append({"obs_id": len(recs), "row": r, "order": o, "kind": kd, "token_index": t})
        offsets[j + 1] = len(recs)
    bf.write_csv(OBS / "obs_index.csv", recs, ["obs_id", "row", "order", "kind", "token_index"])
    np.save(OBS / "offsets.npy", offsets)
    np.save(OBS / "step_rows.npy", np.asarray(rows, np.int64))
    every = Counter(sp[r]["every"] for r in rows)
    # recompute the 32-grid positions from the step record with the harness's own observation_points
    sys.path.insert(0, str(bf.ROOT))
    from argus_hook import scenario_rollout as sr
    pts = bf.load_points()
    chk = Counter()
    for s in steps:
        st = pts[s["unit_id"]]["steps"][int(s["step_index"])]
        if st.get("prompt_length") is None or st.get("action_start") is None:
            chk["no_step_record"] += 1
            continue
        span = tuple(st["reasoning_span"]) if st.get("reasoning_span") else None
        p32 = sr.observation_points(int(st["prompt_length"]), sr.HarmonySpans(int(st["action_start"]), span, (0, 0)),
                                    bf.GRID)
        ok = list(p32) == sp[int(s["row"])]["token_index"] and list(p32.values()) == sp[int(s["row"])]["kinds"]
        chk["match" if ok else "mismatch"] += 1
    (STATE).mkdir(parents=True, exist_ok=True)
    (STATE / "index_check.json").write_text(json.dumps({"grid32_recomputed": dict(chk),
                                                         "observe_every": dict(every)}), encoding="utf-8")
    if chk["mismatch"]:
        raise SystemExit(f"[index] 32-grid positions differ from observation_points: {dict(chk)}")
    say(f"[index] 32-grid recompute check {dict(chk)}")
    say(f"[index] steps {len(rows)} obs {len(recs)} observe_every {dict(every)} "
        f"train obs {sum(len(sp[r]['kinds']) for r in rows if sp[r]['split'] == 'train')}")


def load_index():
    offsets = np.load(OBS / "offsets.npy")
    step_rows = np.load(OBS / "step_rows.npy")
    slot = {int(r): j for j, r in enumerate(step_rows)}
    return offsets, step_rows, slot


# ---------------------------------------------------------------------- hub work
def work_groups(wanted_rows: set[int]) -> list[dict]:
    """Row groups from plan.json restricted to items of LAYERS and wanted step rows."""
    plan = json.loads((OUT / "plan.json").read_text(encoding="utf-8"))
    assert plan["revision"] == REVISION, plan["revision"]
    out = []
    for g in plan["work"]:
        items = [it for it in g["items"] if it["layer"] in LAYERS and it["srow"] in wanted_rows]
        if items:
            out.append({**g, "items": items, "id": f"{g['shard']}#{g['rg']}"})
    return out


def fetch_rows(hub, g: dict, sp: dict[int, dict]):
    """Yield (srow, layer, float32 32-grid rows) for the group's wanted items. Other rows are never decoded."""
    import pyarrow.parquet as pq

    for attempt in range(6):
        try:
            with hub.open(g["shard"]) as fh:  # in-memory read (fsspec block cache, no disk cache)
                table = pq.ParquetFile(fh).read_row_group(g["rg"], columns=["data"])
            break
        except Exception as exc:  # noqa: BLE001 network hiccup
            if attempt == 5:
                raise
            say(f"[retry] {g['id']}: {type(exc).__name__}: {exc}")
            time.sleep(5 * (attempt + 1))
    col = table.column("data")
    out = []
    for it in g["items"]:
        value = col[it["row"]].as_py()  # only wanted rows are ever converted
        if hashlib.sha256(value).hexdigest() != it["sha"]:
            raise bf.hf_select.SelectError(f"sha256 mismatch {g['id']} row {it['row']}")
        arr = np.frombuffer(value, dtype=np.dtype(it["dtype"])).reshape(tuple(it["shape"]))
        p = sp[it["srow"]]
        if arr.shape != (p["n_raw"], bf.HIDDEN):
            raise ValueError(f"row {it['srow']} L{it['layer']}: shape {arr.shape} vs {p['n_raw']} observations")
        out.append((it["srow"], it["layer"], np.asarray(arr[p["keep"]], dtype=np.float32)))
        del value
    del table, col
    return out


def run_groups(groups, fn, workers: int, on_result, disk: DiskWatch):
    hub = bf.Hub(REVISION)
    it = iter(groups)
    with ThreadPoolExecutor(max_workers=workers) as ex:
        running = set()

        def submit():
            g = next(it, None)
            if g is not None:
                running.add(ex.submit(lambda g=g: (g, fn(hub, g))))

        for _ in range(workers + 2):
            submit()
        while running:
            done, _ = wait(running, return_when=FIRST_COMPLETED)
            for f in done:
                running.discard(f)
                g, res = f.result()
                on_result(g, res)
                disk.check()
                submit()


# ---------------------------------------------------------------------- pass 1: fit
def fit_basis(X: np.ndarray, dim: int = DIM, clip: float = CLIP) -> dict:
    """Robust scale + clip + PCA (exact, covariance eigendecomposition). X: [n, H] float32 train rows."""
    med = np.median(X, axis=0).astype(np.float32)
    q75, q25 = np.percentile(X, [75, 25], axis=0)
    iqr = (q75 - q25).astype(np.float32)
    scale = iqr / np.float32(IQR_TO_SIGMA)
    zero = scale <= 1e-12
    scale[zero] = 1.0
    Z = np.clip((X - med) / scale, -clip, clip).astype(np.float32)
    clip_frac = float((np.abs(Z) >= clip).mean())
    mu = Z.mean(0, dtype=np.float64)
    Zc = (Z - mu).astype(np.float64)
    C = Zc.T @ Zc / (len(Z) - 1)
    w, V = np.linalg.eigh(C)
    order = np.argsort(w)[::-1]
    w, V = w[order], V[:, order]
    comps = V[:, :dim].T.copy()
    sign = np.sign(comps[np.arange(dim), np.abs(comps).argmax(1)])
    comps *= sign[:, None]
    total = float(w.sum())
    return {"median": med, "scale": scale.astype(np.float32), "clip": np.float32(clip),
            "pca_mean": mu.astype(np.float32), "components": comps.astype(np.float32),
            "explained_variance": w[:dim].astype(np.float32),
            "explained_variance_ratio": (w[:dim] / total).astype(np.float32),
            "total_variance": np.float64(total), "n_fit_rows": np.int64(len(X)),
            "zero_iqr_coords": np.int64(zero.sum()), "clip_fraction": np.float64(clip_frac)}


def project(x: np.ndarray, b: dict) -> tuple[np.ndarray, np.ndarray]:
    """(u [n, 512] float32, x~ - pca_mean [n, H] float32)."""
    z = np.clip((x - b["median"]) / b["scale"], -b["clip"], b["clip"]) - b["pca_mean"]
    return z @ b["components"].T, z


def load_basis(L: int) -> dict:
    with np.load(OBS / f"basis_L{L:02d}.npz") as z:
        return {k: z[k] for k in z.files}


def stage_fit(args) -> None:
    STATE.mkdir(parents=True, exist_ok=True)
    frozen = STATE / "basis_frozen.json"
    if frozen.is_file():
        raise SystemExit(f"[fit] basis already frozen ({frozen}); it is never refitted")
    disk = DiskWatch()
    disk.check()
    steps = load_steps()
    sp = step_points(steps)
    train_rows = {int(s["row"]) for s in steps if s["split"] == "train"}
    groups = work_groups(train_rows)  # items restricted to TRAIN rows: validation rows are not decoded here
    rng = np.random.default_rng(FIT_SEED)
    pick = sorted(rng.choice(len(groups), size=int(np.ceil(FIT_FRACTION * len(groups))), replace=False).tolist())
    fit_groups = [groups[i] for i in pick]
    say(f"[fit] {len(fit_groups)}/{len(groups)} train row groups, "
        f"{sum(g['bytes'] for g in fit_groups) / 2**30:.2f} GB to stream")
    rows = {L: [] for L in LAYERS}
    t0, n = time.time(), [0]

    def on_result(g, res):
        for srow, L, x in res:
            rows[L].append(x)
        n[0] += 1
        if n[0] % 10 == 0 or n[0] == len(fit_groups):
            say(f"[fit] groups {n[0]}/{len(fit_groups)} | {time.time() - t0:.0f}s | free {free_bytes() / 2**30:.1f} GB")

    run_groups(fit_groups, lambda hub, g: fetch_rows(hub, g, sp), args.workers, on_result, disk)
    info = {"fit_rowgroups": [g["id"] for g in fit_groups], "fit_fraction": FIT_FRACTION, "fit_seed": FIT_SEED,
            "fit_cap": FIT_CAP, "transfer_bytes": int(sum(g["bytes"] for g in fit_groups)), "layers": {}}
    for L in LAYERS:
        X = np.concatenate(rows[L])
        rows[L] = None
        n_all = len(X)
        if n_all > FIT_CAP:
            X = X[np.sort(np.random.default_rng(FIT_SEED + L).choice(n_all, FIT_CAP, replace=False))]
        b = fit_basis(X)
        del X
        path = OBS / f"basis_L{L:02d}.npz"
        np.savez(path, **b)
        info["layers"][str(L)] = {"rows_available": n_all, "rows_used": int(b["n_fit_rows"]),
                                  "ev512_fit": float(b["explained_variance_ratio"].sum()),
                                  "ev32_fit": float(b["explained_variance_ratio"][:32].sum()),
                                  "zero_iqr_coords": int(b["zero_iqr_coords"]),
                                  "clip_fraction": float(b["clip_fraction"]), "sha256": bf.sha256_file(path)}
        say(f"[fit] L{L}: {info['layers'][str(L)]}")
    info.update({"frozen_at": time.strftime("%Y-%m-%dT%H:%M:%S"), "disk": disk.report(),
                 "seconds": time.time() - t0})
    frozen.write_text(json.dumps(info, indent=1), encoding="utf-8")
    say(f"[fit] frozen {frozen}: disk {info['disk']}")


# ---------------------------------------------------------------------- pass 2: project
def check_basis() -> dict:
    fr = json.loads((STATE / "basis_frozen.json").read_text(encoding="utf-8"))
    for L in LAYERS:
        if bf.sha256_file(OBS / f"basis_L{L:02d}.npz") != fr["layers"][str(L)]["sha256"]:
            raise SystemExit(f"[project] basis_L{L:02d}.npz does not match its frozen sha256")
    return fr


def stage_project(args) -> None:
    check_basis()
    disk = DiskWatch()
    disk.check()
    steps = load_steps()
    sp = step_points(steps)
    offsets, step_rows, slot = load_index()
    n_obs = int(offsets[-1])
    need = n_obs * DIM * 2 * len(LAYERS)
    feat_bytes = dir_bytes(bf.FEAT)
    if feat_bytes + need > MAX_TOTAL:
        raise SystemExit(f"[abort] features {feat_bytes / 2**30:.2f} + obs cache {need / 2**30:.2f} GB > 3 GB")
    if free_bytes() - need < MIN_FREE:
        raise SystemExit("[abort] not enough free disk for the cache with a 10 GB margin")
    bases = {L: load_basis(L) for L in LAYERS}
    mm = {}
    for L in LAYERS:
        path = OBS / f"obs_L{L:02d}.npy"
        if path.is_file():
            mm[L] = np.lib.format.open_memmap(path, mode="r+")
            assert mm[L].shape == (n_obs, DIM) and mm[L].dtype == np.float16
        else:
            mm[L] = np.lib.format.open_memmap(path, mode="w+", dtype=np.float16, shape=(n_obs, DIM))
            mm[L][:] = np.nan
            mm[L].flush()
    pooled = {(L, p): np.load(bf.FEAT / f"L{L:02d}_{p}.npy", mmap_mode="r") for L in LAYERS for p in bf.POOLS}
    groups = work_groups(set(slot))
    n_items = sum(len(g["items"]) for g in groups)
    if n_items != len(slot) * len(LAYERS):
        raise SystemExit(f"[project] plan has {n_items} values, need {len(slot) * len(LAYERS)}")
    STATE.mkdir(parents=True, exist_ok=True)
    done_path = STATE / "project_done.jsonl"
    done = set()
    if done_path.is_file():
        for line in open(done_path, encoding="utf-8"):
            try:
                done.add(json.loads(line)["id"])
            except (json.JSONDecodeError, KeyError):
                pass
    todo = [g for g in groups if g["id"] not in done]
    total = sum(g["bytes"] for g in todo)
    say(f"[project] {len(done)} groups done, {len(todo)} to do, {total / 2**30:.2f} GB to stream, N_obs {n_obs}")

    def work(hub, g):
        res = []
        for srow, L, x in fetch_rows(hub, g, sp):
            b = bases[L]
            u, z = project(x, b)
            pl, _ = bf.pool_step(x, sp[srow]["kinds"])
            mism = sum(int(not np.array_equal(pl[p].astype(np.float16), pooled[(L, p)][srow], equal_nan=True))
                       for p in bf.POOLS)
            st = {"split": sp[srow]["split"], "tot": float((z.astype(np.float64) ** 2).sum()),
                  "proj": float((u.astype(np.float64) ** 2).sum()), "n": int(len(x)),
                  "clip": int((np.abs(z + b["pca_mean"]) >= b["clip"]).sum()), "umax": float(np.abs(u).max()),
                  "pool_mismatch": mism}
            res.append((srow, L, u.astype(np.float16), st))
        return res

    t0, moved, fin = time.time(), [0], [0]
    with open(done_path, "a", encoding="utf-8") as dfh:
        def on_result(g, res):
            agg = {}
            for srow, L, u16, st in res:
                j = slot[srow]
                a, e = int(offsets[j]), int(offsets[j + 1])
                assert u16.shape[0] == e - a
                mm[L][a:e] = u16
                k = f"L{L}|{st['split']}"
                s = agg.setdefault(k, {"tot": 0.0, "proj": 0.0, "n": 0, "clip": 0, "umax": 0.0, "pool_mismatch": 0,
                                       "values": 0})
                for f in ("tot", "proj", "n", "clip", "pool_mismatch"):
                    s[f] += st[f]
                s["umax"] = max(s["umax"], st["umax"])
                s["values"] += 1
            for m in mm.values():
                m.flush()
            dfh.write(json.dumps({"id": g["id"], "bytes": g["bytes"], "stats": agg}) + "\n")
            dfh.flush()
            os.fsync(dfh.fileno())
            fin[0] += 1
            moved[0] += g["bytes"]
            el = time.time() - t0
            rate = moved[0] / el if el else 0
            say(f"[project] groups {fin[0]}/{len(todo)} | {moved[0] / 2**30:.2f}/{total / 2**30:.2f} GB | "
                f"{rate / 2**20:.1f} MB/s | ETA {(total - moved[0]) / rate / 60 if rate else 0:.1f} min | "
                f"free {free_bytes() / 2**30:.1f} GB")

        run_groups(todo, work, args.workers, on_result, disk)
    rep = disk.report()
    (STATE / f"project_disk_{time.strftime('%Y%m%dT%H%M%S')}.json").write_text(json.dumps(rep), encoding="utf-8")
    say(f"[project] finished {fin[0]} groups in {time.time() - t0:.0f}s; disk {rep}")


# ---------------------------------------------------------------------- finalize
def stage_finalize(args) -> None:
    fr = check_basis()
    offsets, step_rows, slot = load_index()
    n_obs = int(offsets[-1])
    groups = work_groups(set(slot))
    stats, done = {}, set()
    for line in open(STATE / "project_done.jsonl", encoding="utf-8"):
        d = json.loads(line)
        if d["id"] in done:
            continue
        done.add(d["id"])
        for k, s in d["stats"].items():
            t = stats.setdefault(k, {"tot": 0.0, "proj": 0.0, "n": 0, "clip": 0, "umax": 0.0, "pool_mismatch": 0,
                                     "values": 0})
            for f in ("tot", "proj", "n", "clip", "pool_mismatch", "values"):
                t[f] += s[f]
            t["umax"] = max(t["umax"], s["umax"])
    missing = [g["id"] for g in groups if g["id"] not in done]
    if missing:
        raise SystemExit(f"[finalize] {len(missing)} row groups not projected yet")
    nan_rows = {}
    for L in LAYERS:
        a = np.load(OBS / f"obs_L{L:02d}.npy", mmap_mode="r")
        bad = 0
        for i in range(0, n_obs, 20000):
            bad += int(np.isnan(a[i:i + 20000]).any(1).sum() + np.isinf(a[i:i + 20000]).any(1).sum())
        nan_rows[str(L)] = bad
    if any(nan_rows.values()):
        raise SystemExit(f"[finalize] NaN/inf rows {nan_rows}")
    idx = bf.read_csv(OBS / "obs_index.csv")
    steps = {s["row"]: s for s in load_steps()}
    split_obs = Counter(steps[r["row"]]["split"] for r in idx)
    kinds = Counter("reasoning+N" if r["kind"].startswith("reasoning+") else r["kind"] for r in idx)
    pts = bf.load_points()
    every = Counter(pts[steps[str(r)]["unit_id"]]["observe_every"] for r in step_rows)
    ev = {}
    for L in LAYERS:
        t = stats.get(f"L{L}|train")
        b = load_basis(L)
        ev[str(L)] = {"ev512_fit_sample": float(b["explained_variance_ratio"].sum()),
                      "ev32_fit_sample": float(b["explained_variance_ratio"][:32].sum()),
                      "ev512_all_train_rows": t["proj"] / t["tot"],
                      "clip_fraction_all_rows": sum(stats[f"L{L}|{s}"]["clip"] for s in ("train", "validation"))
                      / (sum(stats[f"L{L}|{s}"]["n"] for s in ("train", "validation")) * bf.HIDDEN),
                      "max_abs_u": max(stats[f"L{L}|{s}"]["umax"] for s in ("train", "validation")),
                      "pooled_feature_mismatches": sum(stats[f"L{L}|{s}"]["pool_mismatch"] for s in
                                                       ("train", "validation"))}
    files = sorted(p for p in OBS.iterdir() if p.is_file() and p.name != "manifest.json")
    sha = {p.name: bf.sha256_file(p) for p in files}
    sizes = {p.name: p.stat().st_size for p in files}
    disk_reports = [json.loads(p.read_text()) for p in sorted(STATE.glob("project_disk_*.json"))]
    man = {"revision": REVISION, "layers": list(LAYERS), "dim": DIM, "dtype": "float16", "grid": bf.GRID,
           "clip": CLIP, "scale": "IQR/1.349", "n_steps": int(len(step_rows)), "n_obs": n_obs,
           "obs_by_split": dict(split_obs), "obs_by_kind": dict(kinds),
           "steps_by_split": dict(Counter(steps[str(r)]["split"] for r in step_rows)),
           "observe_every_steps": {str(k): v for k, v in every.items()},
           "steps_order": "same order as labels/steps.v2.csv rows with features_complete=1",
           "basis": {"fit": {k: v for k, v in fr.items() if k != "fit_rowgroups"},
                     "fit_rowgroups": fr["fit_rowgroups"],
                     "sha256": {f"basis_L{L:02d}.npz": fr["layers"][str(L)]["sha256"] for L in LAYERS}},
           "explained_variance": ev, "nan_rows": nan_rows, "sha256": sha, "bytes": sizes,
           "cache_bytes": int(sum(sizes.values())), "features_bytes": dir_bytes(bf.FEAT),
           "transfer_bytes_pass2": int(sum(g["bytes"] for g in groups)), "row_groups_pass2": len(groups),
           "row_groups_with_test_or_sealed_rows": sum(1 for g in groups if g["foreign_nontv_units"]),
           "disk_pass2": disk_reports, "finalized_at": time.strftime("%Y-%m-%dT%H:%M:%S")}
    man["total_bytes_features_plus_obs"] = man["cache_bytes"] + man["features_bytes"]
    (OBS / "manifest.json").write_text(json.dumps(man, indent=1), encoding="utf-8")
    say("[finalize]", json.dumps({k: v for k, v in man.items() if k not in ("basis", "sha256")})[:4000])


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("stage", choices=("index", "fit", "project", "finalize"))
    ap.add_argument("--workers", type=int, default=6)
    args = ap.parse_args(argv)
    OUT.mkdir(parents=True, exist_ok=True)
    say(f"=== obs cache stage {args.stage} ===")
    globals()[f"stage_{args.stage}"](args)
    return 0


if __name__ == "__main__":
    sys.exit(main())

"""Synthetic data in the exact phase-3 formats (tests and timing only; never real data).

``make_synthetic(root)`` writes, under ``root``:
  steps.csv + row_status.csv + L{LL}_{max,mean,pre,rend}.npy   (frozen-evaluate view, like features_labels_v2/)
  obs_cache/ (obs_L{LL}.npy, obs_index.csv, offsets.npy, step_rows.npy, basis_L{LL}.npz, manifest.json)
and returns a dict with the raw rows (``raw[L]`` [N_obs, H] float32, when ``write_raw``), the planted
observation position of every positive step and the basis objects.

Risk is planted in ONE observation of a violating step (never the pre_action row): u += signal * d_L, where d
lies in the leading variance subspace. Trajectory offsets (rollout-level signal) and per-tool means add realistic
nuisance structure. Report-tool rows (``submit_result``) carry their own report-content label signal.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

import numpy as np

STEP_COLS = ["row", "unit_id", "scenario_id", "condition", "seed", "trajectory_id", "action_id", "step_index",
             "tool", "kind", "label", "label_status", "source", "family", "split", "report_content", "n_obs",
             "prefix_length", "has_rend", "pre_is_pre_action", "obs_kinds"]
TOOLS = ("bash", "read_file", "send_email")


def make_synthetic(root, *, n_fam=24, traj_per_fam=3, steps_per_traj=8, hidden=96, dim=48, layers=(16, 20, 23),
                   signal=3.0, pos_rate=0.15, n_obs_range=(3, 10), seed=0, write_raw=True, val_fams=2,
                   sealed_fams=1, signal_layers=(20,), traj_sd=0.3, n_lead=8) -> dict:
    root = Path(root)
    cache = root / "obs_cache"
    cache.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(seed)
    # basis per layer: orthonormal P [H, D], med / scale / mean
    bases, dirs = {}, {}
    for L in layers:
        P, _ = np.linalg.qr(rng.normal(size=(hidden, dim)))
        bases[L] = {"median": rng.normal(0, 0.2, hidden).astype(np.float32),
                    "scale": rng.uniform(0.5, 1.5, hidden).astype(np.float32),
                    "clip": np.float32(3.0), "mean": rng.normal(0, 0.02, hidden).astype(np.float32),
                    "components": P.T.astype(np.float32)}
        d = np.zeros(dim)
        d[:4] = rng.normal(size=4)
        dirs[L] = d / np.linalg.norm(d)
    lat_sd = np.r_[np.linspace(1.0, 0.6, n_lead), np.full(dim - n_lead, 0.15)]
    tool_mu = {t: rng.normal(0, 0.4, dim) * (lat_sd > 0.5) for t in TOOLS + ("submit_result",)}

    steps, obs_rows, planted = [], [], {}
    U = {L: [] for L in layers}
    n_fam_total = n_fam + val_fams + sealed_fams
    row = 0
    for f in range(n_fam_total):
        split = "train" if f < n_fam else ("validation" if f < n_fam + val_fams else "sealed")
        source = "oct" if f % 2 == 0 else "nov"
        fam = f"F{f:02d}"
        for t in range(traj_per_fam):
            traj = f"tr{f:02d}{t}"
            unit = f"AV-SYN{f:02d}-C{t}-s0-{traj}"
            toff = {L: rng.normal(0, traj_sd, dim) * (lat_sd > 0.5) for L in layers}
            prefix = 500
            for k in range(steps_per_traj + 1):
                report = k == steps_per_traj
                tool = "submit_result" if report else TOOLS[int(rng.integers(len(TOOLS)))]
                y = int(rng.random() < (0.3 if report else pos_rate))
                n = int(rng.integers(n_obs_range[0], n_obs_range[1] + 1))
                kinds = ["pre_reasoning"] + [f"reasoning+{32 * (j + 1)}" for j in range(n - 3)] + \
                        ["reasoning_end", "pre_action"]
                kinds = kinds[-n:] if n < 3 else kinds
                pos = int(rng.integers(0, n - 1)) if (y and n > 1) else -1
                if y and n == 1:
                    y = 0
                status = ("oct_human" if source == "oct" else
                          ("nov_auto_confirmed" if (tool == "read_file" and not y) else "nov_draft_rule"))
                for L in layers:
                    lat = rng.normal(size=(n, dim)) * lat_sd + tool_mu[tool] + toff[L]
                    if pos >= 0 and L in signal_layers:
                        lat[pos] += signal * dirs[L]
                    U[L].append(lat.astype(np.float32))
                if pos >= 0:
                    planted[row] = pos
                for j, kd in enumerate(kinds):
                    obs_rows.append({"row": row, "order": j, "kind": kd, "token_index": prefix + 32 * j})
                steps.append({"row": row, "unit_id": unit, "scenario_id": f"AV-SYN{f:02d}", "condition": f"C{t}",
                              "seed": 0, "trajectory_id": traj, "action_id": f"{traj}:{k}", "step_index": k,
                              "tool": tool, "kind": "tool", "label": y, "label_status": status, "source": source,
                              "family": fam, "split": split,
                              "report_content": int(report and y and source == "oct"), "n_obs": n,
                              "prefix_length": prefix, "has_rend": int("reasoning_end" in kinds),
                              "pre_is_pre_action": 1, "obs_kinds": "|".join(kinds)})
                prefix += 32 * n + 40
                row += 1
    n_rows = row
    off = np.zeros(n_rows + 1, np.int64)
    off[1:] = np.cumsum([s["n_obs"] for s in steps])
    lat_all = {L: np.concatenate(U[L]) for L in layers}
    # raw rows reproduce the latent through the basis: x~ = mean + lat @ P^T, x = med + scale * x~
    raw, u_all = {}, {}
    for L in layers:
        b = bases[L]
        P = b["components"].T
        xt = b["mean"] + lat_all[L] @ P.T
        x = (b["median"] + b["scale"] * xt).astype(np.float32)
        xt_c = np.clip((x - b["median"]) / b["scale"], -3, 3)
        u_all[L] = ((xt_c - b["mean"]) @ P).astype(np.float32)
        raw[L] = x
    # frozen-evaluate view (all rows) + pooled features (all rows; mirrors features/)
    with open(root / "steps.csv", "w", newline="", encoding="utf-8") as h:
        w = csv.DictWriter(h, fieldnames=STEP_COLS)
        w.writeheader()
        w.writerows(steps)
    with open(root / "row_status.csv", "w", newline="", encoding="utf-8") as h:
        h.write("row,features_complete\n" + "".join(f"{i},1\n" for i in range(n_rows)))
    for L in layers:
        x = raw[L]
        pooled = {"max": np.stack([x[off[i]:off[i + 1]].max(0) for i in range(n_rows)]),
                  "mean": np.stack([x[off[i]:off[i + 1]].mean(0) for i in range(n_rows)]),
                  "pre": x[off[1:] - 1], "rend": x[off[1:] - 2]}
        for p, a in pooled.items():
            np.save(root / f"L{L:02d}_{p}.npy", a.astype(np.float16))
    # observation cache: train + validation rows only (sealed never cached)
    keep = [i for i in range(n_rows) if steps[i]["split"] in ("train", "validation")]
    c_off = [0]
    obs_ids = []
    for i in keep:
        obs_ids.append(np.arange(off[i], off[i + 1]))
        c_off.append(c_off[-1] + int(off[i + 1] - off[i]))
    obs_ids = np.concatenate(obs_ids)
    for L in layers:
        np.save(cache / f"obs_L{L:02d}.npy", u_all[L][obs_ids].astype(np.float16))
        np.savez(cache / f"basis_L{L:02d}.npz", **bases[L])
    np.save(cache / "offsets.npy", np.asarray(c_off, np.int64))
    np.save(cache / "step_rows.npy", np.asarray(keep, np.int64))
    with open(cache / "obs_index.csv", "w", newline="", encoding="utf-8") as h:
        w = csv.writer(h)
        w.writerow(["obs_id", "row", "order", "kind", "token_index"])
        for new, old in enumerate(obs_ids.tolist()):
            o = obs_rows[old]
            w.writerow([new, o["row"], o["order"], o["kind"], o["token_index"]])
    (cache / "manifest.json").write_text(json.dumps({"synthetic": True, "layers": list(layers), "dim": dim,
                                                      "hidden": hidden, "grid": 32}), encoding="utf-8")
    return {"root": root, "cache": cache, "steps": steps, "planted": planted, "offsets_all": off,
            "raw": raw if write_raw else None, "u": u_all, "bases": bases, "dirs": dirs, "obs_rows": obs_rows}


def make_timing_cache(root, *, n_rows=10_300, mean_obs=8.1, dim=512, layers=(20,), n_fam=300, seed=0,
                      pos_rate=0.009, report_rows=1000) -> dict:
    """Full-size synthetic cache for timing (no raw rows, no pooled 2880 features)."""
    root = Path(root)
    cache = root / "obs_cache"
    cache.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(seed)
    n_obs = np.clip(rng.poisson(mean_obs - 3, n_rows) + 3, 1, 64)
    off = np.zeros(n_rows + 1, np.int64)
    off[1:] = np.cumsum(n_obs)
    steps = []
    per_traj = 8
    for i in range(n_rows):
        fam = i * n_fam // n_rows
        traj = f"t{i // per_traj}"
        report = i >= n_rows - report_rows
        tool = "submit_result" if report else TOOLS[i % 3] + str(i % 7)
        src = "oct" if fam % 2 == 0 else "nov"
        y = int(rng.random() < (0.2 if report else pos_rate * 8 if i % 9 == 0 else pos_rate))
        n = int(n_obs[i])
        kinds = (["pre_reasoning"] + [f"reasoning+{32 * (j + 1)}" for j in range(n - 3)] +
                 ["reasoning_end", "pre_action"]) if n >= 3 else ["pre_action"] * 0 + (["reasoning_end", "pre_action"][-n:])
        steps.append({"row": i, "unit_id": f"U{i // per_traj}", "scenario_id": f"S{fam}", "condition": "C0", "seed": 0,
                      "trajectory_id": traj, "action_id": f"{traj}:{i % per_traj}", "step_index": i % per_traj,
                      "tool": tool, "kind": "tool", "label": y,
                      "label_status": "oct_human" if src == "oct" else "nov_draft_rule", "source": src,
                      "family": f"F{fam}", "split": "train", "report_content": int(report and y and src == "oct"),
                      "n_obs": n, "prefix_length": 1000 + i % 500, "has_rend": int(n >= 2), "pre_is_pre_action": 1,
                      "obs_kinds": "|".join(kinds)})
    with open(root / "steps.csv", "w", newline="", encoding="utf-8") as h:
        w = csv.DictWriter(h, fieldnames=STEP_COLS)
        w.writeheader()
        w.writerows(steps)
    with open(root / "row_status.csv", "w", newline="", encoding="utf-8") as h:
        h.write("row,features_complete\n" + "".join(f"{i},1\n" for i in range(n_rows)))
    N = int(off[-1])
    sd = np.r_[np.linspace(3, 1, 32), np.full(dim - 32, 0.3)].astype(np.float32)
    for L in layers:
        arr = np.lib.format.open_memmap(cache / f"obs_L{L:02d}.npy", mode="w+", dtype=np.float16, shape=(N, dim))
        for a in range(0, N, 20000):
            b = min(N, a + 20000)
            arr[a:b] = (rng.normal(size=(b - a, dim)).astype(np.float32) * sd).astype(np.float16)
        del arr
    np.save(cache / "offsets.npy", off)
    np.save(cache / "step_rows.npy", np.arange(n_rows, dtype=np.int64))
    with open(cache / "obs_index.csv", "w", newline="", encoding="utf-8") as h:
        h.write("obs_id,row,order,kind,token_index\n")
        k = 0
        for i, s in enumerate(steps):
            for j, kd in enumerate(s["obs_kinds"].split("|")):
                h.write(f"{k},{i},{j},{kd},{32 * j}\n")
                k += 1
    (cache / "manifest.json").write_text(json.dumps({"synthetic_timing": True}), encoding="utf-8")
    return {"root": root, "cache": cache, "n_obs": N}

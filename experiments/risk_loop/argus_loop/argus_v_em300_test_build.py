"""Test-split feature cache for the Argus-V-em300 test evaluation (reports/risk-loop/argus-v-em300/test-eval-prereg.md).

User instruction 2026-11-16: "TEST 데이터를 가지고 성능평가를 시작해". Until then the test split was sealed
(reports/risk-loop/argus-v1/loop/TASK.md §0), so this script refuses to run without --user-approved-test.

Built with the helper code of the train/validation cache (build_features.py: label table, step join, 32-token grid
thinning, pooling) into its own root, artifacts/risk-loop/argus-v1-loop-test/. The train/validation cache is not
touched and evaluate.load never sees this root. Units: split == "test" in the label table (scenario-splits v1/v2).
Sealed units (no split) and the validation split are not read. Raw tensors are never written to disk.

Stages (each resumable; ``all`` runs them in order):
  labels    test rows of build_features.load_labels (same files, same revision, same precedence as the train table;
            the train/validation rows of the same call must reproduce the existing v2 table)   -> labels/labels_test.csv
  meta      rollout.json of the test units: step table fields + the fields the visibility rule reads -> meta/*.jsonl
  steps     join labels x rollout steps (as build_features.stage_steps)                         -> features/steps.csv
  plan      row groups holding the wanted tensor rows, layers 16 and 23                         -> plan.json
  build     fetch + pool into float16 arrays                                                    -> features/L{16,23}_{pool}.npy
  finalize  completeness per row + sha256                                                       -> features/row_status.csv, manifest.json

  PYTHONUTF8=1 py -3.11 -u experiments/risk_loop/argus_loop/argus_v_em300_test_build.py all --user-approved-test --workers 2
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from collections import Counter
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from experiments.risk_loop.argus_loop import build_features as B  # noqa: E402
import hf_select  # noqa: E402  (build_features put scripts/ on sys.path)

TRAIN_OUT = B.OUT                                            # train/validation cache: read only
OUT = ROOT / "artifacts/risk-loop/argus-v1-loop-test"
FEAT = OUT / "features"
LOG = OUT / "build.log"
LAYERS = (16, 23)                                            # the layers the scored models read
POOLS = B.POOLS
SPLIT = "test"
REVISION = B.LABEL_REVISION                                  # the revision of the train/validation build


def say(*parts) -> None:
    line = time.strftime("%Y-%m-%d %H:%M:%S ") + " ".join(str(p) for p in parts)
    print(line, flush=True)
    OUT.mkdir(parents=True, exist_ok=True)
    with open(LOG, "a", encoding="utf-8") as fh:
        fh.write(line + "\n")


B.say = say                                                  # retry messages of process_group go to this log


# ---------------------------------------------------------------------- labels
def stage_labels(args) -> None:
    lab = OUT / "labels"
    target = lab / "labels_test.csv"
    if target.is_file():
        say(f"[labels] {target.relative_to(ROOT)} exists")
        return
    old_summary = json.loads((TRAIN_OUT / "labels/labels_summary.v2.json").read_text(encoding="utf-8"))
    assert old_summary["label_revision"] == REVISION
    assert B.sha256_file(B.OCT_LABELS) == old_summary["oct_labels_sha256"], "October label file differs from the train build"
    assert B.sha256_file(B.OVERRIDES) == old_summary["overrides_sha256"], "override file differs from the train build"
    human_doc = B._hub_json(B.HF_NOV_HUMAN, REVISION)
    rows, info = B.load_labels(B.OCT_LABELS, None, nov_human=human_doc, overrides=B.read_overrides(B.OVERRIDES),
                               revision=REVISION)
    # the same call must give back the existing train/validation label table, row for row
    tv = [r for r in rows if r["split"] in ("train", "validation")]
    old = B.read_csv(TRAIN_OUT / "labels" / B.LABELS_V2)
    assert len(tv) == len(old), (len(tv), len(old))
    for a, b in zip(tv, old):
        assert all(str(a[c]) == str(b[c]) for c in B.LABEL_COLS), (a, b)
    test = [r for r in rows if r["split"] == SPLIT]
    listed = {r["unit_id"] for r in B.read_csv(TRAIN_OUT / "labels/sealed_units.csv") if r["split"] == SPLIT}
    assert {r["unit_id"] for r in test} == listed, "test units differ from the list written at the first build"
    B.write_csv(target, test, B.LABEL_COLS)
    summary = {"revision": REVISION, "units": len(listed), "actions": len(test),
               "units_by_source": dict(Counter(r["source"] for r in {r["unit_id"]: r for r in test}.values())),
               "actions_by_source": dict(Counter(r["source"] for r in test)),
               "positives_by_source": dict(Counter(r["source"] for r in test if r["label"] == 1)),
               "status": dict(Counter(f"{r['source']}|{r['label_status']}" for r in test)),
               "positives_by_status": dict(Counter(f"{r['source']}|{r['label_status']}" for r in test if r["label"] == 1)),
               "train_validation_rows_reproduced": len(tv), "labels_test_sha256": B.sha256_file(target),
               "built_at": time.strftime("%Y-%m-%dT%H:%M:%S")}
    (lab / "labels_summary_test.json").write_text(json.dumps(summary, indent=1, ensure_ascii=False), encoding="utf-8")
    say("[labels]", json.dumps(summary, ensure_ascii=False))


# ---------------------------------------------------------------------- meta
def rule_step(s: dict, k: int) -> dict:
    """The fields visible_flag_rule.py reads, taken from a rollout.json step the way the train extract took them."""
    command = s.get("command")
    tool, args = None, None
    if s.get("kind") == "tool" and isinstance(command, str):
        try:
            call = json.loads(command)
            tool, args = call.get("tool"), call.get("arguments")
        except (ValueError, AttributeError):
            tool = "<unparsed>"
    return {"step_index": s.get("step_index", k), "kind": s.get("kind"),
            "tool": tool if s.get("kind") == "tool" else s.get("kind"), "arguments": args,
            "command": command if s.get("kind") != "tool" else None, "tool_result": s.get("tool_result"),
            "execution": s.get("execution"), "oracle_reason": s.get("oracle_reason"),
            "static_findings": s.get("static_findings"), "effect_findings": s.get("effect_findings"),
            "policy_label": s.get("policy_label"), "decision": s.get("decision")}


def fetch_meta(hub, units: list[str], path: Path, rule_path: Path) -> None:
    """rollout.json of ``units`` -> compact step table fields (as build_features.stage_meta) + rule fields."""
    path.parent.mkdir(parents=True, exist_ok=True)
    done = set()
    if path.is_file():
        for line in open(path, encoding="utf-8"):
            try:
                done.add(json.loads(line)["unit_id"])
            except (json.JSONDecodeError, KeyError):
                pass
    todo = sorted(u for u in units if u not in done)
    manifest_units = hub.sel.units()
    missing = [u for u in todo if u not in manifest_units]
    if missing:
        say(f"[meta] {len(missing)} units not in the Hub manifest (skipped): {missing[:5]}")
    todo = [u for u in todo if u in manifest_units]
    say(f"[meta] {len(done)} done, {len(todo)} to fetch")
    with open(path, "a", encoding="utf-8") as out, open(rule_path, "a", encoding="utf-8") as rout:
        for i in range(0, len(todo), 50):
            chunk = todo[i:i + 50]
            rows = hub.sel.select(units=chunk, table="files", path_glob="rollout/rollout.json")
            for key, data, _ in hub.sel.fetch_values(rows):
                d = json.loads(data)
                raw = d.get("steps") or []
                steps = [{"step_index": s.get("step_index", k), "action_id": s.get("action_id"), "kind": s.get("kind"),
                          "tool": B.tool_of(s), "action_start": s.get("action_start"),
                          "obs_kinds": [o["kind"] for o in s.get("observations") or []],
                          "capture_dir": s.get("capture_dir")} for k, s in enumerate(raw)]
                out.write(json.dumps({"unit_id": key[0], "scenario_id": d.get("scenario_id"), "family": d.get("family"),
                                      "condition": d.get("condition"), "seed": d.get("seed"),
                                      "trajectory_id": d.get("trajectory_id"), "observe_every": d.get("observe_every"),
                                      "steps": steps}, ensure_ascii=False) + "\n")
                rout.write(json.dumps({"unit_id": key[0], "steps": [{"step": rule_step(s, k)} for k, s in enumerate(raw)]},
                                      ensure_ascii=False) + "\n")
            out.flush()
            rout.flush()
            say(f"[meta] {min(i + 50, len(todo))}/{len(todo)} units")


def stage_meta(args) -> None:
    units = sorted({r["unit_id"] for r in B.read_csv(OUT / "labels/labels_test.csv")})
    fetch_meta(B.Hub(REVISION), units, OUT / "meta/rollouts.jsonl", OUT / "meta/rule_steps.jsonl")


def load_jsonl(path: Path) -> dict[str, dict]:
    out = {}
    for line in open(path, encoding="utf-8"):
        try:
            d = json.loads(line)
        except json.JSONDecodeError:
            continue
        out[d["unit_id"]] = d
    return out


# ---------------------------------------------------------------------- steps (as build_features.stage_steps)
def stage_steps(args) -> None:
    labels = B.read_csv(OUT / "labels/labels_test.csv")
    meta = load_jsonl(OUT / "meta/rollouts.jsonl")
    rows, problems = [], Counter()
    for r in labels:
        m = meta.get(r["unit_id"])
        if m is None:
            problems["no_rollout_meta"] += 1
            continue
        k = int(r["step_index"])
        if k >= len(m["steps"]):
            problems["step_out_of_range"] += 1
            continue
        s = m["steps"][k]
        if s["action_id"] and s["action_id"] != r["action_id"]:
            problems["action_id_mismatch"] += 1
            continue
        if not s["obs_kinds"]:
            problems["no_observations"] += 1
            continue
        tool = s["tool"]
        y = int(r["label"])
        every = B.unit_observe_every(m)
        _, kinds, _ = B.thin_to_grid32(None, s["obs_kinds"], every)
        rows.append({**{c: r[c] for c in B.LABEL_COLS}, "tool": tool, "kind": s["kind"], "_observe_every": every,
                     "_n_obs_raw": len(s["obs_kinds"]), "family": B.family_of(r["scenario_id"], m.get("family")),
                     "report_content": int(r["source"] == "oct" and y == 1 and tool in B.REPORT_TOOLS),
                     "n_obs": len(kinds), "prefix_length": s["action_start"], "has_rend": int("reasoning_end" in kinds),
                     "pre_is_pre_action": int("pre_action" in kinds), "obs_kinds": "|".join(kinds)})
    rows.sort(key=lambda x: ({"oct": 0, "nov": 1}[x["source"]], x["unit_id"], int(x["step_index"])))
    for i, x in enumerate(rows):
        x["row"] = i
    assert all(x["split"] == SPLIT for x in rows)
    B.write_csv(FEAT / "steps.csv", rows, B.STEP_COLS)
    B.write_csv(FEAT / "steps_grid.csv", [{"row": x["row"], "unit_id": x["unit_id"], "step_index": x["step_index"],
                                           "observe_every": x["_observe_every"], "n_obs_raw": x["_n_obs_raw"],
                                           "n_obs_32": x["n_obs"]} for x in rows], B.GRID_COLS)
    say(f"[steps] {len(rows)} rows, problems {dict(problems)}, observe_every {dict(Counter(x['_observe_every'] for x in rows))}")


# ---------------------------------------------------------------------- plan (as build_features.stage_plan)
def stage_plan(args) -> None:
    hub = B.Hub(REVISION)
    steps = B.read_csv(FEAT / "steps.csv")
    want = {(s["unit_id"], int(s["step_index"])): int(s["row"]) for s in steps}
    units = sorted({s["unit_id"] for s in steps})
    unit_set = set(units)
    shards = hub.sel.shards_for(units, "tensors")
    say(f"[plan] {len(units)} units over {len(shards)} tensor shards (indexing missing shards)")
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        list(ex.map(hub.sel.shard_index, shards))
    groups, chunked = {}, []
    for shard in shards:
        for r in hub.sel.shard_index(shard):
            m = B.STEP_PATH.match(r["path"])
            L = hf_select.row_layer(r)
            if not (r["unit_id"] in unit_set and m is not None and L in LAYERS and (r["unit_id"], int(m.group(1))) in want):
                continue
            if (r.get("chunk_count") or 1) > 1:
                chunked.append(r)
                continue
            g = groups.setdefault((shard, r["_rg"]), {"shard": shard, "rg": r["_rg"], "bytes": r["_rg_payload_bytes"], "items": []})
            g["items"].append({"row": r["_row"], "srow": want[(r["unit_id"], int(m.group(1)))], "layer": L,
                               "unit_id": r["unit_id"], "dtype": r["dtype"], "shape": r["shape"], "sha": r["chunk_sha256"]})
    if chunked:
        raise SystemExit(f"[plan] {len(chunked)} wanted values are multi-chunk; not handled: {chunked[:2]}")
    work = sorted(groups.values(), key=lambda g: (g["shard"], g["rg"]))
    found = Counter((it["srow"], it["layer"]) for g in work for it in g["items"])
    missing = [(s, L) for s in want.values() for L in LAYERS if (s, L) not in found]
    plan = {"revision": hub.revision, "layers": LAYERS, "steps": len(steps), "units": len(units), "shards": len(shards),
            "row_groups": len(work), "transfer_bytes": int(sum(g["bytes"] for g in work)),
            "values": int(sum(len(g["items"]) for g in work)), "missing_values": len(missing),
            "missing_examples": missing[:10], "work": work}
    (OUT / "plan.json").write_text(json.dumps(plan), encoding="utf-8")
    say("[plan]", json.dumps({k: v for k, v in plan.items() if k != "work"}))


# ---------------------------------------------------------------------- build (as build_features.stage_build)
def _memmaps(n: int) -> dict:
    out = {}
    for L in LAYERS:
        for p in POOLS:
            path = FEAT / f"L{L:02d}_{p}.npy"
            if path.is_file():
                out[(L, p)] = np.lib.format.open_memmap(path, mode="r+")
                assert out[(L, p)].shape == (n, B.HIDDEN), path
            else:
                out[(L, p)] = np.lib.format.open_memmap(path, mode="w+", dtype=np.float16, shape=(n, B.HIDDEN))
                out[(L, p)][:] = np.nan
    return out


def stage_build(args) -> None:
    plan = json.loads((OUT / "plan.json").read_text(encoding="utf-8"))
    steps = B.read_csv(FEAT / "steps.csv")
    n = len(steps)
    meta = load_jsonl(OUT / "meta/rollouts.jsonl")
    kinds_of = {int(s["row"]): (meta[s["unit_id"]]["steps"][int(s["step_index"])]["obs_kinds"], B.unit_observe_every(meta[s["unit_id"]]))
                for s in steps}                                # raw kinds as stored in the tensor rows + observe_every
    B.require_free(n * B.HIDDEN * 2 * len(LAYERS) * len(POOLS))
    mm = _memmaps(n)
    done_path, flags_path = FEAT / "done.txt", FEAT / "flags.jsonl"
    done = set(done_path.read_text().split()) if done_path.is_file() else set()
    gid = lambda g: f"{g['shard']}#{g['rg']}"                   # noqa: E731
    todo = [g for g in plan["work"] if gid(g) not in done]
    total = sum(g["bytes"] for g in todo)
    say(f"[build] revision={plan['revision']} {len(done)} groups done, {len(todo)} to do, {total / 2**30:.2f} GB to transfer, workers={args.workers}")
    hub = B.Hub(plan["revision"])
    t0, moved, fin, stats = time.time(), 0, 0, Counter()
    with ThreadPoolExecutor(max_workers=args.workers) as ex, open(done_path, "a") as dfh, open(flags_path, "a", encoding="utf-8") as ffh:
        it_todo = iter(todo)
        running = set()

        def submit_next():
            g = next(it_todo, None)
            if g is not None:
                running.add(ex.submit(B.process_group, hub, g, kinds_of))

        for _ in range(args.workers + 1):
            submit_next()
        while running:
            fs, _ = wait(running, return_when=FIRST_COMPLETED)
            for f in fs:
                running.discard(f)
                g, res = f.result()
                for srow, L, pooled, flags in res:
                    for p in POOLS:
                        v = pooled[p]
                        mm[(L, p)][srow] = v.astype(np.float16)
                        if p != "rend" or flags["has_rend"]:
                            if not np.isfinite(v).all() or np.abs(v).max() > 65504:
                                stats[f"nonfinite_or_overflow_{p}"] += 1
                    ffh.write(json.dumps({"row": srow, "layer": L, **flags}) + "\n")
                for m in mm.values():
                    m.flush()
                ffh.flush()
                dfh.write(gid(g) + "\n")
                dfh.flush()
                os.fsync(dfh.fileno())
                fin += 1
                moved += g["bytes"]
                el = time.time() - t0
                rate = moved / el if el else 0
                if fin % 5 == 0 or fin == len(todo):
                    say(f"[build] groups {fin}/{len(todo)} | {moved / 2**30:.2f}/{total / 2**30:.2f} GB | {rate / 2**20:.1f} MB/s | "
                        f"ETA {((total - moved) / rate / 60) if rate else float('nan'):.1f} min" + (f" | {dict(stats)}" if stats else ""))
                submit_next()
    say(f"[build] finished {fin} groups in {time.time() - t0:.0f}s, {moved / 2**30:.2f} GB, stats {dict(stats)}")


def stage_finalize(args) -> None:
    plan = json.loads((OUT / "plan.json").read_text(encoding="utf-8"))
    steps = B.read_csv(FEAT / "steps.csv")
    n = len(steps)
    done = set((FEAT / "done.txt").read_text().split())
    left = {f"{g['shard']}#{g['rg']}" for g in plan["work"]} - done
    if left:
        raise SystemExit(f"[finalize] {len(left)} row groups not done yet")
    have = set()
    for line in open(FEAT / "flags.jsonl", encoding="utf-8"):
        d = json.loads(line)
        have.add((d["row"], d["layer"]))
    miss_rows = {r for r in range(n) for L in LAYERS if (r, L) not in have}
    B.write_csv(FEAT / "row_status.csv", [{"row": r, "in_shared_rowgroup": 0, "features_complete": int(r not in miss_rows)} for r in range(n)],
                ["row", "in_shared_rowgroup", "features_complete"])
    hashes, nan_rows = {}, {}
    for L in LAYERS:
        for p in POOLS:
            path = FEAT / f"L{L:02d}_{p}.npy"
            a = np.load(path, mmap_mode="r")
            nan_rows[f"L{L:02d}_{p}"] = int(np.isnan(a).any(1).sum())
            hashes[path.name] = B.sha256_file(path)
    for name in ("steps.csv", "row_status.csv"):
        hashes[name] = B.sha256_file(FEAT / name)
    man = {"split": SPLIT, "revision": plan["revision"], "layers": LAYERS, "pools": POOLS, "rows": n, "rows_incomplete": len(miss_rows),
           "rows_with_nan": nan_rows, "sha256": hashes, "transfer_bytes_tensors": plan["transfer_bytes"],
           "finalized_at": time.strftime("%Y-%m-%dT%H:%M:%S")}
    (FEAT / "manifest.json").write_text(json.dumps(man, indent=1), encoding="utf-8")
    say("[finalize]", json.dumps(man))


STAGES = {"labels": stage_labels, "meta": stage_meta, "steps": stage_steps, "plan": stage_plan, "build": stage_build,
          "finalize": stage_finalize}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("stage", choices=list(STAGES) + ["all"])
    ap.add_argument("--user-approved-test", action="store_true", help="the user told us to open the test split (2026-11-16)")
    ap.add_argument("--workers", type=int, default=2)
    args = ap.parse_args(argv)
    if not args.user_approved_test:
        raise SystemExit("The test split is sealed. Run only on the user's instruction: add --user-approved-test.")
    for name in (list(STAGES) if args.stage == "all" else [args.stage]):
        if name == "steps" and (FEAT / "steps.csv").is_file():
            say("[steps] features/steps.csv exists")
            continue
        if name == "plan" and (OUT / "plan.json").is_file():
            say("[plan] plan.json exists")
            continue
        STAGES[name](args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

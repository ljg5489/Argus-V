"""Read-only count of the violation and safe scenarios, runs and calls of everything on the HF dataset (2026-11-19).

User: "현재 HF에 올라가 있는 모든 시나리오를 보고 총 위반과 안전 시나리오에 대한 개수를 확인해".

No model, no score, nothing written to the Hub, no hidden-state value read.
  * Calls on the Hub: every rollout/steps/step_NNN/step.json path in the files index (metadata only).
  * Verdict of a call, highest first:
      October AV-S01~S60 and the obstacle/clear trial runs: label_review/ArgusV_review_progress.json
        (human review; "delegated" when not human-confirmed)
      November AVv2: label_review/ArgusV_november_auto_review.json.gz + ArgusV_november_review_progress.json (human)
        + the local convention decisions -- the precedence of build_features.load_labels
        (human > convention > auto-review sidecar > draft rule)
      every other call: the environment verdict in its step.json (policy_label), as read for the 432 new runs at the
        same revision (artifacts/risk-loop/hf-new-1118/steps.csv), or read here for the few runs with no other record
  * Tool name of a call (report tool or not): the rollout records the earlier builds read from the Hub for the same
    runs (their step lists equal the Hub's), else the step.json itself. Most November label records carry no command.
  * Sealed units are dropped on their names and never counted: AV-S61~S80, the ten sealed AVD scenarios (40 runs) and
    the four sealed v3 test scenarios (see SEALED). The first version of this count (commit c6eebf1) knew only
    AV-S61~S80 and counted the 40 sealed AVD runs.
  * Report-tool calls (submit_result, stop, write_report) are counted apart and do not make a run a violation run
    (the convention of every evaluation since 2026-11-08).
A run is a violation run when one of its other calls is a violation; a safe run when it has judged calls and none is
a violation. A scenario is a violation scenario when one of its runs is a violation run.

Usage: PYTHONUTF8=1 py -3.11 experiments/risk_loop/argus_loop/hf_inventory_1119.py
Output: artifacts/risk-loop/hf-inventory-1119/calls.csv, summary.json (not in git)
"""
from __future__ import annotations

import collections
import csv
import gc
import json
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
for p in (ROOT, ROOT / "scripts"):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))
from hf_select import HubSelector  # noqa: E402
from experiments.risk_loop.argus_loop import build_features as B  # noqa: E402
from experiments.risk_loop.argus_loop import hf_new_data_1118 as NEW  # noqa: E402

OUT = ROOT / "artifacts" / "risk-loop" / "hf-inventory-1119"
NEW_STEPS = ROOT / "artifacts" / "risk-loop" / "hf-new-1118" / "steps.csv"
NEW_STEPS_REVISION = "494aec37"
LOCAL_ROLLOUTS = [ROOT / "artifacts/risk-loop/argus-v1-loop/meta/rollouts.jsonl",       # rollout.json of the runs, read
                  ROOT / "artifacts/risk-loop/argus-v1-loop-test/meta/rollouts.jsonl",  # from the Hub by earlier builds
                  ROOT / "artifacts/risk-loop/resplit-1117/meta/rollouts.jsonl"]
MAX_FETCH = 400 * 2**20                     # read the step.json of the few remaining runs only below this transfer
# Sealed units, matched on the run name before anything of theirs is read:
#   AV-S61~S80; the ten sealed AVD scenarios x conditions B/D/G/X = 40 runs (argus_v_emp_new_data_nosealed.py, user
#   instruction 2026-11-19 "봉인 40개 빼고"); the four sealed v3 test scenarios (Scenario/scenario-splits.v3.json; none
#   is on the Hub). The older AVv2-F07/F11/F14 scenarios are not sealed: resplit-1117 train / validation hold them.
SEALED_AVD = ("03", "07", "10", "24", "35", "36", "52", "57", "74", "90")
SEALED_V3 = ("AVv2-F07-PRC-02", "AVv2-F11-HRI-02", "AVv2-F11-PUB-02", "AVv2-F14-OPS-02")
SEALED = re.compile(r"^(AV-S(6[1-9]|7\d|80)-|AVD-20261112-(" + "|".join(SEALED_AVD) + r")-|("
                    + "|".join(re.escape(s) for s in SEALED_V3) + r")-)")
REPORT_TOOLS = frozenset(B.REPORT_TOOLS)
STEP_JSON = re.compile(r"^rollout/steps/step_(\d+)/step\.json$")
UNIT = re.compile(r"^(.*?)-(C\d+|cell\d+|pilot[A-Z]+|prompt|clear|obstacle|[A-Z])-s(\d+)-[0-9a-f]{8}$")
GROUPS = [  # (key, Korean name)
    ("AV-S-oct", "AV-S01~S60, 10월 수집 (10-16)"),
    ("AV-S-nov", "AV-S01~S60, 11월 수집 (11-02·04)"),
    ("trial", "10월 시험 실행 approval·evaluation·report (clear/obstacle)"),
    ("AVv2", "11월 AVv2"),
    ("AVv2-pilot", "AVv2 pilot F01-PRC-03·PUB-02 (11-17~18)"),
    ("AVD", "AVD-20261112-01~90 (11-17~18)"),
    ("AVP", "AVP-20261113·16 (11-17~18)"),
]


def say(*a):
    print(time.strftime("%H:%M:%S"), *a, flush=True)


def group_of(unit: str, source: str, batch: str = "") -> str:
    if source == "agent_loop":
        return "agent_loop"
    if unit.startswith("AV-S"):
        return "AV-S-oct" if batch.startswith("202610") else "AV-S-nov"
    if unit.startswith(("approval-", "evaluation-", "report-")):
        return "trial"
    if unit.startswith("AVD-"):
        return "AVD"
    if unit.startswith("AVP-"):
        return "AVP"
    if unit.startswith("AVv2-"):
        return "AVv2" if source == "scenario_rollout_v2" else "AVv2-pilot"
    return "other"


def scenario_of(unit: str) -> tuple[str, str]:
    m = UNIT.match(unit)
    return (m.group(1), m.group(2)) if m else (unit, "?")


def main():
    from huggingface_hub import HfApi

    OUT.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    sel = HubSelector(log=lambda m: say(m))
    head = sel._pin_revision()
    api = HfApi(token=sel._resolve_token())
    label_paths = [B.HF_OCT_LABELS, B.HF_NOV_LABELS, B.HF_NOV_HUMAN]
    changed = {p.path: {"commit": p.last_commit.oid[:8], "date": str(p.last_commit.date)}
               for p in api.get_paths_info(sel.repo, label_paths, repo_type="dataset", revision=head, expand=True)}
    say("revision", head[:8], "| label files last changed:", json.dumps(changed, ensure_ascii=False))

    # ---- verdicts from the label files first (little free memory: keep only a compact table, then free the documents)
    human_doc = B._hub_json(B.HF_NOV_HUMAN, head)
    lab_rows, lab_info = B.load_labels(None, None, nov_human=human_doc, overrides=B.read_overrides(B.OVERRIDES), revision=head)
    del human_doc
    lab = {}
    for r in lab_rows:
        if SEALED.match(r["unit_id"]):
            continue
        lab[(r["unit_id"], int(r["step_index"]))] = {"label": int(r["label"]), "status": r["label_status"],
                                                      "tool": B.tool_of({"kind": r["_kind"], "command": r["_command"]})}
    del lab_rows
    gc.collect()
    say(f"label files: {len(lab)} judged calls outside the sealed units")

    # ---- units and calls on the Hub (files index, metadata only; one shard index in memory at a time)
    units = sel.units()                                   # unit -> info (+source); the v2 copy wins for re-uploaded AVv2
    sealed = sorted(u for u in units if SEALED.match(u))
    keep = {u: i for u, i in units.items() if not SEALED.match(u)}
    say(f"units {len(units)} | sealed dropped {len(sealed)} | kept {len(keep)}")
    wanted = {u for u, i in keep.items() if i["source"] != "agent_loop"}
    calls = {}
    for shard in sel.shards_for(sorted(wanted), "files"):
        for r in sel.shard_index(shard):
            if r["unit_id"] not in wanted:
                continue
            m = STEP_JSON.match(r["path"])
            if m and (r.get("chunk_index") or 0) == 0:
                calls[(r["unit_id"], int(m.group(1)))] = None
        sel._index.pop(shard, None)
        gc.collect()
    say(f"step.json files on the Hub: {len(calls)} in {len({u for u, _ in calls})} runs")
    env = {}
    with open(NEW_STEPS, newline="", encoding="utf-8") as h:
        for r in csv.DictReader(h):
            if SEALED.match(r["unit_id"]) or r["step_index"] == "":   # sealed runs dropped on the name first
                continue
            env[(r["unit_id"], int(r["step_index"]))] = {"label": None if r["policy_label"] == "" else int(r["policy_label"]),
                                                         "status": "env_verdict", "tool": r["tool"] or r["kind"]}
    # step_NNN in the path vs step_index in the records
    for name, src in (("label files", lab), ("environment verdicts", env)):
        hit = {off: sum((u, s + off) in calls for u, s in src) for off in (0, -1, 1)}
        say(f"{name}: {len(src)} records | found in the Hub step list with path number = step_index + offset: {hit}")
    off_lab = max((0, -1, 1), key=lambda o: sum((u, s + o) in calls for u, s in lab))
    off_env = max((0, -1, 1), key=lambda o: sum((u, s + o) in calls for u, s in env))

    # ---- tool name of every call: most November label records carry no command, so take it from the rollout records
    # read earlier from the Hub for the same runs (step lists identical to the Hub's); the rest from their step.json.
    hub_units = {u for u, _ in calls}
    tools, local_units = {}, set()
    for f in LOCAL_ROLLOUTS:
        if not f.is_file():
            continue
        with open(f, encoding="utf-8") as h:
            for line in h:
                d = json.loads(line)
                u = d["unit_id"]
                if u not in hub_units or u in local_units:   # first copy wins (copies of one run are identical)
                    continue
                local_units.add(u)
                for st in d["steps"]:
                    tools.setdefault((u, int(st["step_index"])), st.get("tool") or st.get("kind") or "")
    env_units = {u for u, _ in env}
    rest = sorted(u for u in hub_units if u not in local_units and u not in env_units)
    sel2 = HubSelector(revision=head, log=lambda m: say(m))
    rows = sel2.select(units=rest, table="files", path_glob="rollout/steps/step_*/step.json")
    plan = sel2.plan(rows)
    say(f"runs without a local rollout record or verdict table: {len(rest)} | their step.json: {plan}")
    fetched = 0
    if plan["transfer_bytes_estimate"] <= MAX_FETCH:
        for key, data, meta in sel2.fetch_values(rows):
            d = json.loads(data.decode("utf-8"))
            k = (meta["unit_id"], int(STEP_JSON.match(meta["path"]).group(1)))
            tools[k] = NEW.tool_of(d) or d.get("kind") or ""
            if d.get("policy_label") is not None:      # environment verdict of a call no label file judges
                env[(k[0], k[1] - off_env)] = {"label": int(d["policy_label"]), "status": "env_verdict", "tool": tools[k]}
            fetched += 1
    fetch_stats = dict(sel2.stats)
    del sel2
    gc.collect()
    say(f"tool names: rollout records {len(local_units)} runs, step.json fetched {fetched} calls ({fetch_stats})")

    verdict = {}
    for (u, s), v in env.items():
        verdict[(u, s + off_env)] = v
    for (u, s), v in lab.items():                         # label files beat the environment verdict
        verdict[(u, s + off_lab)] = v
    for k, v in verdict.items():                          # one tool name per call, from the most complete source
        if tools.get(k):
            v["tool"] = tools[k]
    tool_missing = collections.Counter(group_of(u, keep[u]["source"], keep[u].get("batch", "")) for (u, s) in calls
                                       if not (tools.get((u, s)) or (verdict.get((u, s)) or {}).get("tool")))
    say(f"calls without a tool name: {dict(tool_missing)}")
    no_steps = sorted(u for u in wanted if u not in hub_units)
    say(f"runs on the Hub with no step.json: {no_steps}")
    orphans = collections.Counter(group_of(u, keep.get(u, {}).get("source", "?"), keep.get(u, {}).get("batch", "")) for (u, s) in verdict if (u, s) not in calls)

    # ---- per call table
    out_rows = []
    for (u, s) in sorted(calls):
        info = keep[u]
        g = group_of(u, info["source"], info.get("batch", ""))
        scen, cond = scenario_of(u)
        v = verdict.get((u, s))
        tool = tools.get((u, s)) or (v["tool"] if v else "")
        out_rows.append({"group": g, "scenario_id": scen, "condition": cond, "unit_id": u, "step": s, "tool": tool,
                         "report_tool": int(tool in REPORT_TOOLS), "label": "" if v is None or v["label"] is None else v["label"],
                         "label_status": v["status"] if v else "none", "batch": info.get("batch", "")})
    with open(OUT / "calls.csv", "w", newline="", encoding="utf-8") as h:
        w = csv.DictWriter(h, fieldnames=list(out_rows[0]))
        w.writeheader()
        w.writerows(out_rows)

    # ---- counts
    runs_of = collections.defaultdict(list)
    for r in out_rows:
        runs_of[r["unit_id"]].append(r)
    summary = {"revision": head, "label_files_last_changed": changed, "sealed_units_dropped": len(sealed),
               "agent_loop_units_not_scenarios": sorted(u for u, i in keep.items() if i["source"] == "agent_loop"),
               "verdicts_not_matching_a_hub_call": dict(orphans), "label_info": {k: v for k, v in lab_info.items()
                                                                                 if k != "override_conflicts_with_confirmed"},
               "groups": {}}
    for key, name in GROUPS + [("total", "합계")]:
        rs = [r for r in out_rows if key == "total" or r["group"] == key]
        if not rs:
            continue
        units_g = sorted({r["unit_id"] for r in rs})
        run_state, run_report_viol = {}, set()
        for u in units_g:
            cs = runs_of[u]
            act = [c for c in cs if not c["report_tool"]]
            if any(c["label"] == 1 for c in act):
                run_state[u] = "violation"
            elif any(c["label"] == 0 for c in act):
                run_state[u] = "safe_partly_undecided" if any(c["label"] == "" for c in act) else "safe"
            else:
                run_state[u] = "undecided"
            if any(c["label"] == 1 for c in cs if c["report_tool"]):
                run_report_viol.add(u)
        scen_runs = collections.defaultdict(list)
        for u in units_g:
            scen_runs[scenario_of(u)[0]].append(run_state[u])
        scen_state = {}
        for sc, st in scen_runs.items():
            scen_state[sc] = "violation" if "violation" in st else ("safe" if any(x.startswith("safe") for x in st) else "undecided")
        act = [r for r in rs if not r["report_tool"]]
        rep = [r for r in rs if r["report_tool"]]
        summary["groups"][key] = {
            "name": name,
            "batches": sorted({r["batch"] for r in rs}),
            "scenarios": len(scen_state),
            "scenarios_violation": sum(v == "violation" for v in scen_state.values()),
            "scenarios_safe": sum(v == "safe" for v in scen_state.values()),
            "scenarios_undecided": sum(v == "undecided" for v in scen_state.values()),
            "runs": len(units_g),
            "runs_violation": sum(v == "violation" for v in run_state.values()),
            "runs_safe": sum(v == "safe" for v in run_state.values()),
            "runs_safe_partly_undecided": sum(v == "safe_partly_undecided" for v in run_state.values()),
            "runs_undecided": sum(v == "undecided" for v in run_state.values()),
            "runs_with_a_report_tool_violation": len(run_report_viol),
            "runs_violation_only_in_report_tools": len([u for u in run_report_viol if run_state[u] != "violation"]),
            "calls": len(rs),
            "calls_report_tool": len(rep),
            "calls_violation": sum(r["label"] == 1 for r in act),
            "calls_normal": sum(r["label"] == 0 for r in act),
            "calls_undecided": sum(r["label"] == "" for r in act),
            "report_tool_calls_violation": sum(r["label"] == 1 for r in rep),
            "violation_calls_by_label_source": dict(collections.Counter(r["label_status"] for r in act if r["label"] == 1)),
            "judged_calls_by_label_source": dict(collections.Counter(r["label_status"] for r in act if r["label"] != "")),
            "conditions": {c: {"runs": n, "violation_runs": sum(1 for u in units_g if scenario_of(u)[1] == c and run_state[u] == "violation")}
                           for c, n in sorted(collections.Counter(scenario_of(u)[1] for u in units_g).items())},
        }
    summary["seconds"] = round(time.time() - t0, 1)
    (OUT / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=1), encoding="utf-8")
    for key, g in summary["groups"].items():
        print(key, json.dumps({k: v for k, v in g.items() if k not in ("conditions",)}, ensure_ascii=False))
    print("conditions:", json.dumps({k: g["conditions"] for k, g in summary["groups"].items() if k != "total"}, ensure_ascii=False))
    print("orphans:", dict(orphans), "| label info:", json.dumps(summary["label_info"], ensure_ascii=False)[:1500])
    say(f"done in {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()

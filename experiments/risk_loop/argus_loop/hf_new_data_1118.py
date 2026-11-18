"""Read-only summary of the data added to the HF dataset after revision 62106dbf (checked on 2026-11-18).

User: "이번에 새롭게 시나리오 추가해서 gpt-oss-20b 돌려서 데이터 뽑았어 HF 확인해봐".

Reads the unit lists of both manifests and, for every new unit, only the per-step records (rollout/steps/step_*/step.json,
small text files). No hidden-state payload is read, nothing is written to the Hub. The verdict of a step is the one the
scenario environment wrote into the record: policy_label 1 = violation, 0 = compliant, empty = not decided
(decision UNLABELLED, waiting for review).

Usage: PYTHONUTF8=1 py -3.11 experiments/risk_loop/argus_loop/hf_new_data_1118.py
Output: artifacts/risk-loop/hf-new-1118/steps.csv, summary.json (not in git)
"""
from __future__ import annotations

import collections
import csv
import json
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
from hf_select import HubSelector  # noqa: E402

OLD = "62106dbf"
OUT = ROOT / "artifacts" / "risk-loop" / "hf-new-1118"
SEALED = re.compile(r"^AV-S(6[1-9]|7\d|80)-")          # sealed units: never read


def unit_parts(u: str):
    m = re.match(r"^(.*?)-(C\d+|cell\d+|pilot[A-Z]+|prompt|[A-Z])-s(\d+)-[0-9a-f]{8}$", u)
    return (m.group(1), m.group(2), int(m.group(3))) if m else (u, "?", -1)


def tool_of(d: dict):
    for k in ("tool", "tool_name"):
        if isinstance(d.get(k), str):
            return d[k]
    c = d.get("command")
    if isinstance(c, str):                                   # the command is stored as a JSON string {"arguments": ..., "tool": ...}
        try:
            c = json.loads(c)
        except ValueError:
            return ""
    if isinstance(c, dict):
        for k in ("tool", "name", "tool_name"):
            if isinstance(c.get(k), str):
                return c[k]
    return ""


def main():
    from huggingface_hub import HfApi, hf_hub_download

    OUT.mkdir(parents=True, exist_ok=True)
    sel = HubSelector(log=lambda m: print(m, file=sys.stderr))
    head = sel._pin_revision()
    commits = HfApi().list_repo_commits(sel.repo, repo_type="dataset")
    old_full = next(c.commit_id for c in commits if c.commit_id.startswith(OLD))
    old = json.loads(Path(hf_hub_download(sel.repo, "manifest/units.json", repo_type="dataset", revision=old_full)).read_text(encoding="utf-8"))
    old_ids = {u for units in old["units"].values() for u in units}
    now = sel.units()
    new_ids = sorted(u for u in now if u not in old_ids)
    sealed = [u for u in new_ids if SEALED.match(u)]
    new_ids = [u for u in new_ids if not SEALED.match(u)]
    print(f"revision {head[:8]} | new units {len(new_ids)} (sealed skipped: {len(sealed)})", flush=True)
    t0 = time.time()
    rows = sel.select(units=new_ids, table="files", path_glob="rollout/steps/step_*/step.json")
    print(f"step records to read: {len(rows)} | plan {sel.plan(rows)}", flush=True)
    recs = []
    for key, data, meta in sel.fetch_values(rows):
        d = json.loads(data.decode("utf-8"))
        unit = meta["unit_id"]
        scen, cond, seed = unit_parts(unit)
        recs.append({"unit_id": unit, "source": now[unit]["source"], "scenario_id": scen, "condition": cond, "seed": seed,
                     "step_index": d.get("step_index"), "kind": d.get("kind"), "tool": tool_of(d),
                     "policy_label": "" if d.get("policy_label") is None else int(d["policy_label"]),
                     "decision": d.get("decision"), "oracle_reason": d.get("oracle_reason")})
    recs.sort(key=lambda r: (r["unit_id"], r["step_index"] if isinstance(r["step_index"], int) else -1))
    with open(OUT / "steps.csv", "w", newline="", encoding="utf-8") as h:
        w = csv.DictWriter(h, fieldnames=list(recs[0]))
        w.writeheader()
        w.writerows(recs)
    group = lambda r: ("AVv2" if r["scenario_id"].startswith("AVv2") else r["scenario_id"].split("-")[0]) + " / " + r["source"]  # noqa: E731
    summ = collections.defaultdict(lambda: {"runs": set(), "scenarios": set(), "steps": 0, "violation": 0, "compliant": 0, "undecided": 0,
                                           "violating_scenarios": set(), "tools_with_violation": set()})
    for r in recs:
        s = summ[group(r)]
        s["runs"].add(r["unit_id"])
        s["scenarios"].add(r["scenario_id"])
        s["steps"] += 1
        if r["policy_label"] == 1:
            s["violation"] += 1
            s["violating_scenarios"].add(r["scenario_id"])
            s["tools_with_violation"].add(r["tool"])
        elif r["policy_label"] == 0:
            s["compliant"] += 1
        else:
            s["undecided"] += 1
    out = {"revision": head, "compared_with": old_full, "new_units": len(new_ids), "sealed_units_skipped": len(sealed),
           "seconds": round(time.time() - t0, 1), "selector_stats": sel.stats, "groups": {}}
    for g, s in sorted(summ.items()):
        out["groups"][g] = {"runs": len(s["runs"]), "scenarios": len(s["scenarios"]), "steps": s["steps"], "violation": s["violation"],
                            "compliant": s["compliant"], "undecided": s["undecided"], "scenarios_with_a_violation": len(s["violating_scenarios"]),
                            "tools_with_a_violation": len(s["tools_with_violation"])}
    reasons = collections.Counter((group(r), r["decision"], r["oracle_reason"]) for r in recs)
    out["decision_reason_top"] = [{"group": g, "decision": d, "oracle_reason": o, "steps": n} for (g, d, o), n in reasons.most_common(40)]
    conds = collections.Counter((group(r), r["condition"], r["policy_label"]) for r in recs)
    out["by_condition"] = [{"group": g, "condition": c, "policy_label": p, "steps": n} for (g, c, p), n in sorted(conds.items(), key=str)]
    (OUT / "summary.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(out["groups"], ensure_ascii=False, indent=1))
    print(f"done in {time.time() - t0:.0f}s, payload read {sel.stats}")


if __name__ == "__main__":
    main()

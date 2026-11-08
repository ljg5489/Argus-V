"""D1(d): compact, human-readable extracts of the audit targets (from diag11/audit_raw, train units only)."""
from __future__ import annotations
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from experiments.risk_loop.argus_loop import iter11_diag_common as D  # noqa: E402


def short(x, n=400):
    s = x if isinstance(x, str) else json.dumps(x, ensure_ascii=False)
    return s if len(s) <= n else s[:n] + f"...(+{len(s)-n})"


def tr(step):
    t = step.get("tool_result")
    if not isinstance(t, dict):
        return short(t, 200)
    keep = {k: t[k] for k in ("status", "execution_status", "code", "message", "error", "result") if k in t}
    return short(keep or t, 300)


recs = json.loads((D.OUT / "audit_targets.json").read_text(encoding="utf-8"))
raw = D.OUT / "audit_raw"
lines, seen = [], set()
for n, r in enumerate(sorted(recs, key=lambda r: (r["group"], r["scenario"], r["unit_id"], r["step_index"]))):
    f = json.loads((raw / f"{r['unit_id']}.json").read_text(encoding="utf-8"))
    ro = f["rollout/rollout.json"]
    if r["scenario"] not in seen:
        seen.add(r["scenario"])
        pc = ro.get("public_context", {})
        tools = [{"name": t.get("name"), "desc": short(t.get("description", ""), 160), "contract": short(t.get("contract", ""), 200)}
                 for t in pc.get("tools", [])] if isinstance(pc, dict) else []
        lines += ["", "=" * 100, f"SCENARIO {r['scenario']} family={ro.get('family')} (units vary by condition)",
                  "TASK: " + short(ro.get("task"), 600), "TRUSTED_POLICY: " + short(ro.get("trusted_policy"), 1500),
                  "PUBLIC_POLICY: " + short(pc.get("policy") if isinstance(pc, dict) else "", 1200),
                  "TOOLS: " + short(tools, 2500)]
    st = ro["steps"]
    k = r["step_index"]
    lines += ["", "-" * 80,
              f"[T{n:02d}] unit={r['unit_id']} cond={ro.get('condition')} step={k} tool={r['tool']} LABEL={r['label']} ({r['label_status']})",
              "  condition_meaning: " + short((ro.get("scenario_brief") or {}).get("condition_meaning"), 300),
              "  blocker: " + short((ro.get("scenario_brief") or {}).get("blocker"), 300)]
    for s in st[:k]:
        lines.append(f"  prev step {s['step_index']}: {short(s.get('command'), 260)} -> {tr(s)} | pl={s.get('policy_label')}")
    s = st[k]
    sj = f.get(f"rollout/steps/step_{k:03d}/step.json", {})
    lines += [f"  >>> TARGET command: {short(s.get('command'), 900)}",
              f"  >>> tool_result: {tr(s)}",
              f"  >>> policy_label={s.get('policy_label')} decision={short(s.get('decision'), 200)} oracle_reason={short(s.get('oracle_reason'), 300)}",
              f"  >>> static={short(s.get('static_findings'), 300)} effect={short(s.get('effect_findings'), 300)}",
              f"  >>> model output (reasoning+action): {short(sj.get('output'), 1500)}"]
(D.OUT / "audit_extract.txt").write_text("\n".join(lines), encoding="utf-8")
print(len(lines), "lines")

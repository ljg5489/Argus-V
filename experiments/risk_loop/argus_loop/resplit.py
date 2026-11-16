"""A new train / validation / test split of all labelled data ("resplit-1117").

User instruction 2026-11-17: "데이터셋부터 다시 train, validation, test 제대로 나누고 시작해 이번에 나눈 것은 지금까지 모델
학습시킨 것에는 영향을 미치지 않게 하고". The old split puts most violations of one collection period into one split
(for example the old test split has 16 October and 8 November violations in six scenarios, and one scorable tool per
period), so the three splits are redrawn from the pooled data.

Nothing existing is changed: the old split files (Scenario/scenario-splits.v1/v2.json), the old feature caches, every
trained model and every result are only read. Everything written goes to reports/risk-loop/resplit-1117 and
artifacts/risk-loop/resplit-1117.

How the split is made (labels and metadata only; no model, no score):
  * pool: the judged rows of the old train, validation and test splits (label present, not a report tool, features
    complete; the filters of every earlier evaluation). The sealed units (AV-S61~S80, no split) are not included.
  * unit: the scenario family. All runs of a family go to one split, so a scenario never appears in two splits.
  * visibility flag of every violation: the existing rule (provisional-1, argus_v_em300_test_eval.classify) applied
    to the rollout record of the run; the stored train and test flags must be reproduced.
  * assignment: target shares 60 / 20 / 20. For each family the script counts, per collection period, calls,
    violations, visible violations and tool cells that can be scored, and searches (seeded local search from many
    random starts) for the assignment whose shares are closest to the target on all of these at once.

Stages (each reads what the previous one wrote):
  py -3.11 experiments/risk_loop/argus_loop/resplit.py inventory
  py -3.11 experiments/risk_loop/argus_loop/resplit.py flags      --user-approved   (reads validation and test labels; Hub metadata, read only)
  py -3.11 experiments/risk_loop/argus_loop/resplit.py propose    --user-approved
  py -3.11 experiments/risk_loop/argus_loop/resplit.py build      --user-approved   (pooled features gathered from the two local caches)
"""
from __future__ import annotations

import csv
import json
import os
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

for _name in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ.setdefault(_name, "2")

import numpy as np  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from experiments.risk_loop.argus_loop import argus_v_em300_test_build as TB  # noqa: E402
from experiments.risk_loop.argus_loop import argus_v_em300_test_eval as TE  # noqa: E402

B = TB.B
NAME = "resplit-1117"
REPORT = ROOT / "reports" / "risk-loop" / NAME
OUT = ROOT / "artifacts" / "risk-loop" / NAME
CACHES = {"trainval": ROOT / "artifacts/risk-loop/argus-v1-loop/features_labels_v2", "test": TB.FEAT}   # read only
REPORT_TOOLS = frozenset(B.REPORT_TOOLS)
SPLITS = ("train", "validation", "test")
TARGET = np.asarray([0.6, 0.2, 0.2])
SEED = 20261117
STARTS = 200
MIN_POS = MIN_NEG = 3                       # a tool cell can be scored with at least 3 violations and 3 normal calls
# quantities balanced across the splits, with their weights (visible violations and scorable cells matter most)
WEIGHTS = {"visible_oct": 4.0, "visible_nov": 4.0, "visible_cells": 4.0, "violations_oct": 2.0, "violations_nov": 2.0,
           "cells_oct": 2.0, "cells_nov": 2.0, "calls_oct": 1.0, "calls_nov": 1.0, "runs": 1.0, "families": 1.0}
KEYS = tuple(WEIGHTS)
PERIOD_KO = {"oct": "10월", "nov": "11월"}


def log(*a):
    print(time.strftime("%H:%M:%S"), *a, flush=True)


def need_approval(argv):
    if "--user-approved" not in argv:
        raise SystemExit("This reads the validation and test labels. Run it only on the user's instruction: add --user-approved.")


# ---------------------------------------------------------------------- pool
def pool():
    """Judged rows of the three old splits, with the filters of every earlier evaluation."""
    rows, drop = [], Counter()
    for cache, d in CACHES.items():
        ok = {int(r["row"]): int(r["features_complete"]) for r in B.read_csv(d / "row_status.csv")}
        for r in B.read_csv(d / "steps.csv"):
            if r["label"] not in ("0", "1"):
                drop[(r["split"], "no label")] += 1
            elif r["report_content"] == "1" or r["tool"] in REPORT_TOOLS:
                drop[(r["split"], "report tool")] += 1
                drop[(r["split"], "report tool violations")] += int(r["label"] == "1")
            elif ok.get(int(r["row"]), 0) != 1:
                drop[(r["split"], "incomplete features")] += 1
            else:
                rows.append({"cache": cache, "cache_row": int(r["row"]), "unit_id": r["unit_id"], "scenario_id": r["scenario_id"],
                             "family": r["family"], "source": r["source"], "tool": r["tool"], "kind": r["kind"],
                             "step_index": int(r["step_index"]), "label": int(r["label"]), "label_status": r["label_status"],
                             "condition": r["condition"], "seed": r["seed"], "old_split": r["split"], "trajectory_id": r["trajectory_id"],
                             "cell": f"{r['tool']}|{r['source']}"})
    return rows, drop


def composition(rows, key, vis=None):
    """Per value of ``key`` (a split name): counts by collection period and the cells that can be scored."""
    out = {}
    for name in sorted({r[key] for r in rows}):
        rr = [r for r in rows if r[key] == name]
        d = {"calls": len(rr), "violations": sum(r["label"] for r in rr), "scenarios": len({r["scenario_id"] for r in rr}),
             "families": len({r["family"] for r in rr}), "runs": len({r["unit_id"] for r in rr})}
        if vis is not None:
            d["visible_violations"] = sum(1 for r in rr if vis.get((r["unit_id"], r["step_index"])))
        cells = defaultdict(lambda: [0, 0, 0])                       # violations, normals, visible violations
        for r in rr:
            c = cells[r["cell"]]
            c[0] += r["label"]
            c[1] += 1 - r["label"]
            c[2] += int(bool(vis and vis.get((r["unit_id"], r["step_index"]))))
        for p in ("oct", "nov"):
            q = [r for r in rr if r["source"] == p]
            v = sum(r["label"] for r in q)
            d[p] = {"calls": len(q), "violations": v, "normals": len(q) - v, "violation_rate": v / max(1, len(q)),
                    "scenarios": len({r["scenario_id"] for r in q}), "runs": len({r["unit_id"] for r in q}),
                    "families_with_a_violation": len({r["family"] for r in q if r["label"]}),
                    "visible_violations": sum(1 for r in q if vis and vis.get((r["unit_id"], r["step_index"]))),
                    "cells_scorable": sorted(c for c, x in cells.items() if c.endswith("|" + p) and x[0] >= MIN_POS and x[1] >= MIN_NEG),
                    "cells_scorable_visible": sorted(c for c, x in cells.items() if c.endswith("|" + p) and x[2] >= MIN_POS and x[1] >= MIN_NEG)}
        d["cell_table"] = {c: {"violations": x[0], "normals": x[1], "visible": x[2]} for c, x in sorted(cells.items()) if x[0] > 0}
        out[name] = d
    return out


def stage_inventory(argv):
    rows, drop = pool()
    log("pooled judged rows:", len(rows), "| dropped:", {f"{k[0]}:{k[1]}": v for k, v in drop.items()})
    for name, d in composition(rows, "old_split").items():
        log(f"old {name:10s} calls {d['calls']:5d} violations {d['violations']:3d} scenarios {d['scenarios']:3d} families {d['families']:3d} runs {d['runs']:4d} | "
            + " | ".join(f"{p}: calls {d[p]['calls']} violations {d[p]['violations']} ({d[p]['violation_rate']:.2%}) scorable cells {len(d[p]['cells_scorable'])}"
                         for p in ("oct", "nov")))


# ---------------------------------------------------------------------- visibility flags of every violation
def load_flags() -> dict:
    doc = json.loads((REPORT / "visible_flags.json").read_text(encoding="utf-8"))
    return {(v["unit_id"], v["step_index"]): bool(v["visible"]) for v in doc["violations"]}


def stage_flags(argv):
    need_approval(argv)
    REPORT.mkdir(parents=True, exist_ok=True)
    (OUT / "meta").mkdir(parents=True, exist_ok=True)
    TB.LOG = OUT / "build.log"                                   # keep fetch messages out of the old test-cache log
    rows, _ = pool()
    viol = [r for r in rows if r["label"] == 1]
    units = sorted({r["unit_id"] for r in viol})
    have = {}
    for p in (TB.OUT / "meta/rule_steps.jsonl", TB.OUT / "verify_train/rule_steps.jsonl", OUT / "meta/rule_steps.jsonl"):
        if p.is_file():
            have.update(TB.load_jsonl(p))
    todo = [u for u in units if u not in have]
    log(f"violations {len(viol)} in {len(units)} runs | rollout records already local {len(units) - len(todo)}, to fetch {len(todo)}")
    if todo:
        TB.fetch_meta(B.Hub(TB.REVISION), todo, OUT / "meta/rollouts.jsonl", OUT / "meta/rule_steps.jsonl")
        have.update(TB.load_jsonl(OUT / "meta/rule_steps.jsonl"))
    missing = [u for u in units if u not in have]
    if missing:
        raise SystemExit(f"{len(missing)} runs have no rollout record: {missing[:5]}")
    out = []
    for r in viol:
        t = {"unit_id": r["unit_id"], "step_index": r["step_index"], "tool": r["tool"], "cell": r["cell"], "family": r["family"],
             "scenario_id": r["scenario_id"], "source": r["source"], "old_split": r["old_split"], "label": 1}
        x = TE.rule_row(t, TE.steps_of(have[r["unit_id"]]))
        x["category"], x["visible"] = TE.classify(x)
        out.append(x)
    # the stored flags of the earlier evaluations must come back unchanged
    bad = []
    for path in (TE.TRAIN_FLAGS, TE.REPORT / "visible_flag_test.json"):
        mine = {(x["unit_id"], x["step_index"]): x for x in out}
        for v in json.loads(path.read_text(encoding="utf-8"))["violations"]:
            m = mine.get((v["unit_id"], v["step_index"]))
            if m is None or m["category"] != v["category"] or m["visible"] != v["visible"]:
                bad.append((path.name, v["unit_id"], v["step_index"], v["category"], None if m is None else m["category"]))
    if bad:
        raise SystemExit(f"stored flags not reproduced: {bad[:5]}")
    doc = {"rule_version": TE.RULE_VERSION, "what": "visibility of every violation among the pooled judged rows (old train, validation, test); "
           "visible = the fact that makes the call a violation was explicit in the context before the call",
           "rule": "argus_v_em300_test_eval.rule_row / classify (copied from visible_flag_rule.py); a category without a decision counts as not visible",
           "stored_flags_reproduced": {"train (48)": True, "test (9)": True},
           "counts": {"violations": len(out), "visible": sum(bool(x["visible"]) for x in out),
                      "by_category": dict(Counter(x["category"] for x in out)),
                      "by_old_split_and_period": {f"{s}|{p}": {"violations": sum(1 for x in out if x["old_split"] == s and x["source"] == p),
                                                                 "visible": sum(1 for x in out if x["old_split"] == s and x["source"] == p and x["visible"])}
                                                  for s in SPLITS for p in ("oct", "nov")}},
           "violations": out, "written_at": time.strftime("%Y-%m-%d %H:%M:%S")}
    (REPORT / "visible_flags.json").write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    log("flags written:", doc["counts"]["violations"], "violations,", doc["counts"]["visible"], "visible | categories", doc["counts"]["by_category"])
    log("by old split and period:", doc["counts"]["by_old_split_and_period"])


# ---------------------------------------------------------------------- assignment of families
def family_table(rows, vis):
    fam = {}
    for r in rows:
        f = fam.setdefault(r["family"], {"family": r["family"], "old_split": set(), "periods": set(), "scenarios": set(), "run_set": set(),
                                         "cells": defaultdict(lambda: [0, 0, 0]), **{k: 0.0 for k in KEYS}})
        p, v = r["source"], bool(vis.get((r["unit_id"], r["step_index"])))
        f["old_split"].add(r["old_split"])
        f["periods"].add(p)
        f["scenarios"].add(r["scenario_id"])
        f["run_set"].add(r["unit_id"])
        f[f"calls_{p}"] += 1
        f[f"violations_{p}"] += r["label"]
        f[f"visible_{p}"] += int(v)
        c = f["cells"][r["cell"]]
        c[0] += r["label"]
        c[1] += 1 - r["label"]
        c[2] += int(v)
    for f in fam.values():
        f["runs"], f["families"] = float(len(f["run_set"])), 1.0
        for c, x in f["cells"].items():                              # cells that can be scored inside the family
            if x[0] >= MIN_POS and x[1] >= MIN_NEG:
                f[f"cells_{c.rsplit('|', 1)[1]}"] += 1
            if x[2] >= MIN_POS and x[1] >= MIN_NEG:
                f["visible_cells"] += 1
    return fam


def cost_of(sums, totals, w):
    """sums [split][quantity] -> weighted squared distance of the shares from the target, plus hard requirements."""
    share = sums / totals
    c = float((w * ((share - TARGET[:, None]) ** 2)).sum())
    i = {k: n for n, k in enumerate(KEYS)}
    for s in range(3):                                               # every split must be able to give the main metric
        c += 100.0 * (sums[s, i["visible_cells"]] < 1) + 100.0 * (sums[s, i["violations_oct"]] < 3) + 100.0 * (sums[s, i["violations_nov"]] < 3)
    return c


def search(fam):
    names = sorted(fam)
    Q = np.asarray([[fam[n][k] for k in KEYS] for n in names], dtype=np.float64)          # [family][quantity]
    totals = np.where(Q.sum(0) > 0, Q.sum(0), 1.0)
    w = np.asarray([WEIGHTS[k] if Q[:, j].sum() > 0 else 0.0 for j, k in enumerate(KEYS)])
    rng = np.random.default_rng(SEED)
    best, best_cost, trace = None, np.inf, []
    for start in range(STARTS):
        a = rng.choice(3, size=len(names), p=TARGET)
        sums = np.stack([Q[a == s].sum(0) for s in range(3)])
        cost = cost_of(sums, totals, w)
        improved = True
        while improved:
            improved = False
            move, move_cost = None, cost
            for f in range(len(names)):                              # move one family
                for s in range(3):
                    if s == a[f]:
                        continue
                    t = sums.copy()
                    t[a[f]] -= Q[f]
                    t[s] += Q[f]
                    c = cost_of(t, totals, w)
                    if c < move_cost - 1e-12:
                        move, move_cost = ("move", f, s), c
            if move is None:
                for f in range(len(names)):                          # swap two families of different splits
                    for g in range(f + 1, len(names)):
                        if a[f] == a[g]:
                            continue
                        t = sums.copy()
                        t[a[f]] += Q[g] - Q[f]
                        t[a[g]] += Q[f] - Q[g]
                        c = cost_of(t, totals, w)
                        if c < move_cost - 1e-12:
                            move, move_cost = ("swap", f, g), c
            if move is not None:
                if move[0] == "move":
                    _, f, s = move
                    sums[a[f]] -= Q[f]
                    sums[s] += Q[f]
                    a[f] = s
                else:
                    _, f, g = move
                    sums[a[f]] += Q[g] - Q[f]
                    sums[a[g]] += Q[f] - Q[g]
                    a[f], a[g] = a[g], a[f]
                cost, improved = move_cost, True
        trace.append(cost)
        key = "".join(map(str, a.tolist()))
        if cost < best_cost - 1e-12 or (abs(cost - best_cost) <= 1e-12 and (best is None or key < best[1])):
            best, best_cost = (a.copy(), key), cost
    a = best[0]
    return {n: SPLITS[int(a[i])] for i, n in enumerate(names)}, best_cost, trace


def md_table(head, lines):
    return ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)] + ["| " + " | ".join(str(x) for x in ln) + " |" for ln in lines]


def stage_propose(argv):
    need_approval(argv)
    rows, drop = pool()
    vis = load_flags()
    fam = family_table(rows, vis)
    assign, cost, trace = search(fam)
    for r in rows:
        r["split"] = assign[r["family"]]
    new, old = composition(rows, "split", vis), composition(rows, "old_split", vis)
    scen = {}
    for r in rows:
        scen.setdefault(r["scenario_id"], r["split"])
        assert scen[r["scenario_id"]] == r["split"], "a scenario must stay in one split"
    moved = Counter()
    for f in fam.values():
        moved[("+".join(sorted(f["old_split"])), assign[f["family"]])] += 1
    doc = {"name": NAME, "created_at": time.strftime("%Y-%m-%d %H:%M:%S"),
           "instruction": "데이터셋부터 다시 train, validation, test 제대로 나누고 시작해 이번에 나눈 것은 지금까지 모델 학습시킨 것에는 영향을 미치지 않게 하고",
           "pool": {"rows": len(rows), "violations": sum(r["label"] for r in rows), "visible_violations": sum(vis.values()),
                    "families": len(fam), "scenarios": len(scen), "dropped": {f"{k[0]}:{k[1]}": v for k, v in drop.items()},
                    "not_included": "sealed units (AV-S61~S80, no split)"},
           "unit": "scenario family", "target_shares": dict(zip(SPLITS, TARGET.tolist())), "seed": SEED, "starts": STARTS,
           "weights": WEIGHTS, "cost": cost, "starts_reaching_the_best_cost": int(sum(abs(c - cost) < 1e-9 for c in trace)),
           "families": dict(sorted(assign.items())), "scenarios": dict(sorted(scen.items())),
           "families_moved(old split -> new split)": {f"{k[0]} -> {k[1]}": v for k, v in sorted(moved.items())},
           "composition": new, "old_composition": old}
    REPORT.mkdir(parents=True, exist_ok=True)
    (REPORT / "split.json").write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    with open(REPORT / "families.csv", "w", newline="", encoding="utf-8") as h:
        wr = csv.writer(h)
        wr.writerow(["family", "new_split", "old_split", "periods", "scenarios", "runs", "calls_oct", "calls_nov", "violations_oct",
                     "violations_nov", "visible_oct", "visible_nov", "cells_scorable_in_family", "cells_scorable_visible_in_family"])
        for n, f in sorted(fam.items(), key=lambda kv: (SPLITS.index(assign[kv[0]]), -(kv[1]["violations_oct"] + kv[1]["violations_nov"]), kv[0])):
            wr.writerow([n, assign[n], "+".join(sorted(f["old_split"])), "+".join(sorted(f["periods"])), len(f["scenarios"]), int(f["runs"]),
                         int(f["calls_oct"]), int(f["calls_nov"]), int(f["violations_oct"]), int(f["violations_nov"]), int(f["visible_oct"]),
                         int(f["visible_nov"]),
                         ";".join(sorted(c for c, x in f["cells"].items() if x[0] >= MIN_POS and x[1] >= MIN_NEG)),
                         ";".join(sorted(c for c, x in f["cells"].items() if x[2] >= MIN_POS and x[1] >= MIN_NEG))])

    def block(title, comp):
        lines = []
        for s in SPLITS:
            d = comp[s]
            for p in ("oct", "nov"):
                x = d[p]
                lines.append([s if p == "oct" else "", PERIOD_KO[p], x["calls"], f"{x['violations']} ({x['violation_rate']:.1%})",
                              x["visible_violations"], x["families_with_a_violation"], len(x["cells_scorable"]), len(x["cells_scorable_visible"])])
        return ["", f"### {title}", ""] + md_table(["분할", "기록 시기", "호출", "위반 (비율)", "근거가 보인 위반", "위반이 있는 시나리오 계열",
                                                     "채점할 수 있는 도구", "그중 근거가 보인 위반 3개 이상"], lines)

    L = [f"# 새 분할 ({NAME}) — 구성", "",
         "사용자 지시(2026-11-17)로 train / validation / test를 다시 나눴다. 기존 분할 파일, 기존 특징 캐시, 학습한 모델과 결과는 읽기만 했고 바꾸지 않았다.",
         "", "- 나누는 단위: 시나리오 계열(한 계열의 실행은 모두 같은 분할). 같은 시나리오가 두 분할에 들어가지 않는다.",
         f"- 대상: 기존 train·validation·test의 채점 행 {len(rows):,}개(위반 {sum(r['label'] for r in rows)}개, 근거가 보인 위반 {sum(vis.values())}개, 계열 {len(fam)}개). "
         "봉인 단위(AV-S61~S80)는 넣지 않았다.",
         "- 방법: 목표 비율 60 / 20 / 20. 기록 시기별 호출·위반·근거가 보인 위반·채점할 수 있는 도구 수가 세 분할에 목표 비율대로 들어가도록 "
         f"계열을 배정했다(라벨과 메타데이터만 사용, 모델 점수는 쓰지 않음. seed {SEED}, 무작위 시작 {STARTS}번의 지역 탐색).",
         "- '채점할 수 있는 도구' = 그 분할 안에서 위반 3개 이상·정상 3개 이상인 도구(기록 시기별)."]
    L += block("새 분할", new) + block("기존 분할 (비교용)", old)
    L += ["", "### 계열이 어디서 어디로 갔나", ""] + md_table(["기존 분할 → 새 분할", "계열 수"], [[k, v] for k, v in doc["families_moved(old split -> new split)"].items()])
    L += ["", "계열별 배정은 `families.csv`, 시나리오별 배정과 전체 수치는 `split.json`, 위반마다의 표시는 `visible_flags.json`.", ""]
    (REPORT / "composition.md").write_text("\n".join(L), encoding="utf-8")
    log("cost", round(cost, 6), "| starts reaching it", doc["starts_reaching_the_best_cost"], "of", STARTS, "| families moved", doc["families_moved(old split -> new split)"])
    for s in SPLITS:
        d = new[s]
        log(f"new {s:10s} calls {d['calls']:5d} violations {d['violations']:3d} visible {d['visible_violations']:2d} families {d['families']:2d} scenarios {d['scenarios']:3d} runs {d['runs']:4d} | "
            + " | ".join(f"{p}: calls {d[p]['calls']} viol {d[p]['violations']} ({d[p]['violation_rate']:.1%}) visible {d[p]['visible_violations']} "
                         f"scorable {len(d[p]['cells_scorable'])} visible-scorable {len(d[p]['cells_scorable_visible'])}" for p in ("oct", "nov")))


# ---------------------------------------------------------------------- pooled features of the new split
def stage_build(argv):
    need_approval(argv)
    doc = json.loads((REPORT / "split.json").read_text(encoding="utf-8"))
    vis = load_flags()
    rows, _ = pool()
    feat = OUT / "features"
    feat.mkdir(parents=True, exist_ok=True)
    n = len(rows)
    for name in ("L23_max", "L16_pre"):
        src = {c: np.load(d / f"{name}.npy", mmap_mode="r") for c, d in CACHES.items()}
        width = src["trainval"].shape[1]
        out = np.lib.format.open_memmap(feat / f"{name}.npy", mode="w+", dtype=src["trainval"].dtype, shape=(n, width))
        for c in CACHES:
            idx = np.asarray([i for i, r in enumerate(rows) if r["cache"] == c], dtype=np.int64)
            cr = np.asarray([rows[i]["cache_row"] for i in idx], dtype=np.int64)
            for k in range(0, len(idx), 2048):
                out[idx[k:k + 2048]] = src[c][cr[k:k + 2048]]
        out.flush()
        chk = np.load(feat / f"{name}.npy", mmap_mode="r")
        assert np.isfinite(np.asarray(chk[:: max(1, n // 500)], dtype=np.float32)).all()
        log(name, "written", chk.shape, chk.dtype)
    cols = ["row", "split", "old_split", "unit_id", "scenario_id", "family", "source", "tool", "kind", "step_index", "label", "visible",
            "label_status", "condition", "seed", "trajectory_id", "cell", "cache", "cache_row"]
    with open(feat / "steps.csv", "w", newline="", encoding="utf-8") as h:
        wr = csv.writer(h)
        wr.writerow(cols)
        for i, r in enumerate(rows):
            r = dict(r, row=i, split=doc["families"][r["family"]], visible=int(bool(vis.get((r["unit_id"], r["step_index"])))))
            wr.writerow([r[c] for c in cols])
    (feat / "manifest.json").write_text(json.dumps({"name": NAME, "rows": n, "features": ["L23_max", "L16_pre"], "dtype": "float16 (pooled)",
                                                    "sources": {k: str(v.relative_to(ROOT)).replace("\\", "/") for k, v in CACHES.items()},
                                                    "written_at": time.strftime("%Y-%m-%d %H:%M:%S")}, indent=1), encoding="utf-8")
    log("steps.csv written:", n, "rows |", dict(Counter(doc["families"][r["family"]] for r in rows)))


STAGES = {"inventory": stage_inventory, "flags": stage_flags, "propose": stage_propose, "build": stage_build}

if __name__ == "__main__":
    args = sys.argv[1:]
    todo = [a for a in args if a in STAGES]
    if not todo:
        raise SystemExit(__doc__)
    for a in todo:
        STAGES[a](args)

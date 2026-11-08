"""D1: October rule label (original_policy_label) vs human/delegated gold label, from HF label_review (read-only,
pinned revision, read into memory). Train headline rows only. Estimates how far a rule draft is from review."""
from __future__ import annotations
import json, sys
from collections import Counter
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from experiments.risk_loop.argus_loop import iter11_diag_common as D  # noqa: E402

REV = "57a4bdcd22a57e0dd5ac9f8b0c2dd61741867788"
REPO = "hakuuung/gpt-oss-20b-hidden-state-raw-data"


def main():
    from huggingface_hub import HfFileSystem
    fs = HfFileSystem()
    with fs.open(f"datasets/{REPO}@{REV}/label_review/ArgusV_review_progress.json", "rb") as h:
        doc = json.loads(h.read().decode("utf-8"))
    with fs.open(f"datasets/{REPO}@{REV}/label_review/ArgusV_november_review_progress.json", "rb") as h:
        nov = json.loads(h.read().decode("utf-8"))
    nsamp = nov.get("samples", [])
    nov_h = Counter((str(s.get("human_confirmed")), str(s.get("gold_violation"))) for s in nsamp)
    by_aid = {s["action_id"]: s for s in doc["samples"]}
    _, rows, _ = D.headline()
    aid = {}
    import csv
    with open(D.E.FEATURES_DIR / "steps.csv", newline="", encoding="utf-8") as h:
        for rec in csv.DictReader(h):
            aid[int(rec["row"])] = rec["action_id"]
    cell_of = {}
    for c, m in D.cells(rows):
        for i in m:
            cell_of[int(i)] = c
    tab_all, tab_cells, per_cell, missing = Counter(), Counter(), {}, 0
    y = rows.y
    for i in np.nonzero(rows.source == "oct")[0]:
        s = by_aid.get(aid[int(rows.row_id[i])])
        if s is None:
            missing += 1
            continue
        rl = str(s.get("original_policy_label"))
        key = (rl, int(y[i]))
        tab_all[key] += 1
        if int(i) in cell_of:
            tab_cells[key] += 1
            per_cell.setdefault(cell_of[int(i)], Counter())[key] += 1
    fmt = lambda t: {f"rule={a}|gold={b}": n for (a, b), n in sorted(t.items())}
    res = {"oct_headline_rows": fmt(tab_all), "oct_headline_cells": fmt(tab_cells),
           "per_cell": {c: fmt(t) for c, t in per_cell.items()}, "missing": missing,
           "nov_review_progress_samples": len(nsamp), "nov_human_confirmed_gold": {f"{a}|{b}": n for (a, b), n in nov_h.items()}}
    (D.OUT / "rulecheck.json").write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(res, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()

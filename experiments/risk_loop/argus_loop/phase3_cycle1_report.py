"""Assemble reports/risk-loop/argus-v1/loop/iter-13/cycle1_results.json from the phase-3 stage outputs.

Reads artifacts/risk-loop/argus-v1-loop/phase3/{screen,nested,confirm,shuffles,reselect,controls,k11,
try_counter}.json; applies the frozen evaluate.success_gate to the nested (official) result and the candidate
rule 3b' = headline - max(0.596, own fixed shuffle (b), re-selection shuffle (b)); K-criteria per prereg §6.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402
from experiments.risk_loop.argus_loop import obs_grid as G  # noqa: E402

OUTJ = G.LOOP / "iter-13" / "cycle1_results.json"


def load(name):
    p = G.OUT / f"{name}.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.is_file() else None


def paired_bootstrap(oofs_a, oofs_b, rows, reps=2000, seed=0) -> dict:
    """Family bootstrap of (seed-mean within-tool A) - (seed-mean within-tool B); same resampling as
    evaluate.family_bootstrap_ci (eligibility re-applied per replicate)."""
    import numpy as np
    from experiments.risk_loop import harness as H
    y = rows.y
    _, fam = np.unique(rows.family.astype(str), return_inverse=True)
    _, tc = np.unique(E.headline_groups(rows).astype(str), return_inverse=True)
    members = [np.nonzero(fam == f)[0] for f in range(fam.max() + 1)]
    rng = np.random.default_rng(seed)
    vals = []
    for _ in range(reps):
        idx = np.concatenate([members[f] for f in rng.integers(0, len(members), len(members))])
        idx = idx[np.argsort(tc[idx], kind="stable")]
        num_a = num_b = 0.0
        den = 0
        for seg in np.split(idx, np.flatnonzero(np.diff(tc[idx])) + 1):
            p = int(y[seg].sum())
            if p < E.MIN_POS or len(seg) - p < E.MIN_NEG:
                continue
            num_a += np.mean([H.auroc(o[seg], y[seg]) for o in oofs_a]) * p
            num_b += np.mean([H.auroc(o[seg], y[seg]) for o in oofs_b]) * p
            den += p
        if den:
            vals.append((num_a - num_b) / den)
    lo, hi = np.percentile(vals, [2.5, 97.5])
    return {"ci_low": float(lo), "ci_high": float(hi), "mean": float(np.mean(vals)), "reps": reps}


def k1_ci(seeds=(0, 1, 2)) -> dict | None:
    """K1: nested (official) minus C-pre (same pipeline, pre_action row only), fold seeds 0-2, paired."""
    import numpy as np
    p = G.OUT / "nested_oof.npy"
    if not p.is_file():
        return None
    r = G.Runner(G.VIEW, G.CACHE, G.OUT, workers=1, threads=2, log=lambda *a: None)
    cpre = G.control_configs()["C-pre"]
    cv = E.run_cv(r.memo_fp(cpre), None, r.rows, list(seeds))
    A = list(np.load(p))
    B = [np.asarray(cv["oof"][str(s)]) for s in seeds]
    res = paired_bootstrap(A, B, r.rows)
    res["store_misses"] = dict(r.misses)
    return res


def main():
    S, N, C, SH, RS, CT, K11, TC = (load(n) for n in ("screen", "nested", "confirm", "shuffles", "reselect",
                                                       "controls", "k11", "try_counter"))
    out = {"evaluate_sha256": E.evaluate_sha256(), "labels": "v2 (conventions set after results) / November = draft rule labels",
           "rows": "headline 9,278 rows / 76 violations; cells 9 / 48 violations (frozen evaluate.py v4)",
           "prereg": {"prereg.md": G.sha256(G.PREREG), "prereg-addendum-1.md": G.sha256(G.ADDENDA[0][0]),
                      "prereg-addendum-2.md": G.sha256(G.LOOP / "iter-13" / "prereg-addendum-2.md")},
           "reselect_shuffles": "skipped per prereg-addendum-2 (written after the nested result; nested 0.470 < 0.5, "
                                "cannot change any decision); code/store kept, can be re-run",
           "counts_note": "학습 위반 76 / 평가 위반 48 (headline rows 9,278; 9 evaluated cells)"}
    if S:
        tab = sorted(S["table"], key=lambda t: -(t["within_tool"] or 0))
        out["screen_OPTIMISTIC"] = {"top10": tab[:10], "bottom3": tab[-3:], "n_configs": len(tab),
                                    "luck_corrected_best": S.get("luck_corrected_best")}
        by_combo = {}
        for t in S["table"]:
            b = by_combo.setdefault(t["combo"], {})
            b[str(t["beta"])] = t["within_tool"]
        out["screen_OPTIMISTIC"]["by_combo_beta"] = by_combo
    if N:
        out["nested_OFFICIAL"] = {k: N[k] for k in ("metrics", "extra", "chosen", "combo_counts", "modal",
                                                    "inner_best_score")}
        mod_id = N["modal"]["config_id"]
        sh = (SH or {}).get(mod_id)
        res = {"metrics": N["metrics_full"], "selection": {"method": "nested_cv"},
               "shuffle_source": {"pass": bool(sh and sh["a"]["pass"])},
               "shuffle_source_family": {"within_tool_mean": sh["b"]["within_tool_mean"] if sh else None}}
        gate = E.success_gate(res, None)
        v = N["metrics"]["within_tool"]
        refs = [G.REF_B_V2] + ([sh["b"]["within_tool_mean"]] if sh else []) + \
               ([RS["within_tool_mean"]] if RS and RS.get("within_tool_mean") is not None else [])
        out["gate"] = {"frozen_success_gate": gate, "candidate_3b_prime_margin": v - max(refs),
                       "candidate_3b_prime_ref": max(refs), "shuffles_fixed": sh, "reselect_b": RS,
                       "note": "re-selection shuffles: fold seed 0 only (addendum-1 #10)"}
        ex = N["extra"]["mean"]
        ctrl = CT or {}
        cpre = (ctrl.get("C-pre") or {}).get("metrics", {}).get("within_tool")
        ronly = (ctrl.get("R-only") or {}).get("metrics", {}).get("within_tool")
        t7a = (ctrl.get("T7-a") or {}).get("metrics", {}).get("within_tool")
        own_b = sh["b"]["within_tool_mean"] if sh else None
        out["K"] = {
            "K1_nested_minus_Cpre_point_seed012_vs_Cpre_seed0-9": None if cpre is None else v - cpre,
            "K1_paired_family_bootstrap_seed012": k1_ci(),
            "K2_frac_violation_argmax_pre_or_rend": ex.get("K2_frac_pre_or_rend"),
            "K3_abs_spearman_n_obs32": ex.get("K3_abs_spearman_n_obs32_cell_weighted"),
            "K4_C_minus_max(own_b,0.5)": None if own_b is None else ex.get("within_trajectory_C") - max(own_b, 0.5),
            "K4_C_vs_Ronly_headline": ronly, "K5_nested_minus_T7a": None if t7a is None else v - t7a,
            "K9_shuffle_a_in_0.45_0.55": sh["K9_shuffle_a_in_0.45_0.55"] if sh else None,
            "K10_init_rank_corr (confirm)": {k: c["extra"]["mean"].get("K10_init_rank_corr_median")
                                             for k, c in ((C or {}).get("combos") or {}).items()},
            "K11": K11}
    if C:
        out["confirm"] = {k: {"metrics": c["metrics"], "beta_chosen": c["beta_chosen"],
                              "extra_mean": c["extra"]["mean"], "K10_flag_unstable": c["K10_flag_unstable"]}
                          for k, c in C["combos"].items()}
        out["confirm_init_seeds"] = C.get("init_seeds")
    if CT:
        out["controls"] = {k: {"metrics": v["metrics"], "extra_mean": (v.get("extra") or {}).get("mean")}
                           for k, v in CT.items()}
    if TC:
        tc = {k: v for k, v in TC.items() if k != "combos"}
        out["tries"] = tc
        if S:
            out["tries"]["luck_correction_on_best_screen"] = G.luck_correction(
                out["screen_OPTIMISTIC"]["top10"][0]["within_tool"], tc["cumulative"])
            out["tries"]["luck_correction_conservative"] = G.luck_correction(
                out["screen_OPTIMISTIC"]["top10"][0]["within_tool"], tc["cumulative_conservative"])
    OUTJ.write_text(json.dumps(E.to_jsonable(out), indent=1, ensure_ascii=False), encoding="utf-8")
    print(OUTJ)


if __name__ == "__main__":
    main()

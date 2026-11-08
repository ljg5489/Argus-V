"""Iteration-3 diagnostic (not a candidate): train on report-tool rows ONLY (fold-safe: report rows of the
scored fold's families are excluded via iter03_models.allowed_extras), score headline rows of the held-out
fold, v3 within-tool AUROC. Answers: does a "report violation" direction transfer to action violations?"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT))
from experiments.risk_loop.argus_loop import evaluate as E  # noqa: E402
from experiments.risk_loop.argus_loop import iter03_common as C3  # noqa: E402
from experiments.risk_loop.argus_loop import iter03_models as M3  # noqa: E402
from experiments.risk_loop.argus_loop import models as M  # noqa: E402


def main():
    from sklearn.linear_model import LogisticRegression
    u = C3.load_universe()
    X, _ = C3.representation(u, "L23:max")
    ctx = C3.ctx_for(u)
    out = {}
    for k, C in ((32, 0.01), (128, 0.01), (10, 0.1)):
        def fp(pos_train, y_train, pos_test):
            ext = M3.allowed_extras(ctx, np.asarray(pos_train), np.asarray(pos_test))
            ye = ctx["y_extra"][ext].astype(int)
            Emb = M.centred_pca_embed(X, ext, k, group_train=None)
            w = M.sample_weights(ye, ctx["source"][ext], "source_class")
            lr = LogisticRegression(C=C, max_iter=3000).fit(Emb[ext], ye, sample_weight=w)
            return Emb[np.asarray(pos_test)] @ lr.coef_.ravel()
        cv = E.run_cv(fp, None, u.head)
        m = E.metrics(cv, u.head, bootstrap=0, baselines=False)
        wt = m["within_tool"]
        out[f"k{k}_C{C}"] = {"within_tool": wt["value"], "per_seed": wt["per_seed"],
                             "by_source": {s: v["value"] for s, v in wt["by_source"].items()}}
        print(k, C, out[f"k{k}_C{C}"], flush=True)
    p = REPO_ROOT / "artifacts" / "risk-loop" / "argus-v1-loop" / "iter03" / "diag_report_only.json"
    p.write_text(json.dumps(E.to_jsonable(out), indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()

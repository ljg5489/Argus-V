# Argus-V-em — learned embedding track

Started 2026-11-15 after the user confirmed Claude's handoff and directed: use a learned embedding in a separate `Argus-V-em`, iterate training and structure changes toward at least 0.90 performance.

## Scope and metric

- Separate research track. It does not modify frozen Argus-V1 / Argus-V-p models, the official evaluation code, the preregistered new-data check, or the Argus-V1 try count.
- Primary target follows the user's earlier definition: same-tool AUROC on violations whose deciding fact was visible before the action. Use the provisional-1 rule already recorded in `reports/risk-loop/argus-v-p/visible_flag.json`; always show the rule and sample counts. Also show the all-violation score as context.
- Use train-split activations only, split by the existing scenario-family folds. Never read validation, test, or sealed units. Existing visible subset is only 22 positives (15 distinct feature rows; four cells meet the three-positive minimum), so report per-cell values and uncertainty and do not treat repeated architecture search as independent confirmation.
- If model selection on this reused subset is extensive, its best score is a development result. An independent claim needs fresh, preregistered scenarios; a score from rows already used by Argus-V-p is not independent confirmation.

## First experiment fixed before running

Replace PCA with a small supervised dense embedding on the concatenated cached hidden-state vectors `L23:max` and `L16:pre`. No self-attention, tool names, step numbers, scenario IDs, or metadata as model input. Per-fold robust centering/scaling and clipping are fit on that fold's training rows only. The embedding and sigmoid scoring head train jointly with binary cross entropy; the embedding is the learned representation immediately before the score head.

Train only on normal rows plus the visible-positive rows identified by the provisional-1 record; omit non-visible violations from this target-specific loss. To make the tiny positive class manageable on CPU, keep every visible positive and sample at most `max(30, 20 × visible positives in that cell)` normal rows per tool/source cell in each fold. The sample is chosen from the training fold only with a recorded seed. For metric comparability, score normal rows and visible-positive rows only. Restrict primary evaluation to cells with at least three visible positives and three normals; separately show the two-positive-minimum sensitivity result. This precisely aligns the training target and headline metric with the user's goal.

Initial fixed candidates: embedding widths 32, 64, 128; GELU + LayerNorm + dropout (0.15); AdamW, learning rate 0.001, weight decay 0.01; 60 full-batch epochs. Positive class weight is the square root of the sampled class ratio, capped at 20. No early stopping or hyperparameter choice on the scored fold. Run five family-grouped folds for seeds 0, 1, 2. Compare with saved Argus-V-p/P1 and T7-a OOF scores on the same rows. Record every candidate and seed. Later structures/optimization changes get new numbered rounds in the ledger; keep the best score clearly marked as selected-on-development data.

The purpose of the first round is to test whether a learned projection can improve out-of-fold ranking. Training-row scores are diagnostic only and never count toward the 0.90 target. If no valid route to 0.90 is supported by available data, document why and the data needed rather than relabeling an in-sample score as generalization.

For a compact layer-by-layer diagram and comparisons with Argus-V-p, see [`../model_architectures.md`](../model_architectures.md).

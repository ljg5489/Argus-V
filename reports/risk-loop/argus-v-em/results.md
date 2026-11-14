# Argus-V-em — round 01 results (2026-11-15)

## Result

The learned 32-dimensional embedding reached **0.960 same-tool AUROC** for the user's target, violations whose deciding fact was visible before the action. It exceeded 0.90 in each of the three five-fold scenario-family split seeds.

| Model / view | Same-tool AUROC | Seeds / notes |
|---|---:|---|
| **Argus-V-em EM32, visible violations, minimum 3 per cell** | **0.960** | 0.940 / 0.968 / 0.971 |
| EM64, same metric | 0.948 | 0.976 / 0.916 / 0.953 |
| EM128, same metric | 0.943 | 0.931 / 0.952 / 0.947 |
| Argus-V-p/P1, same rows | 0.760 | same saved OOF seeds |
| Argus-V-p/P5, same rows | 0.756 | same saved OOF seeds |
| Raw-vector linear control, same visible target and folds | 0.899 | 0.920 / 0.877 / 0.901 |
| EM32, all violation labels | 0.549 | context only; not the 0.90 target |
| EM32, visible violations, minimum 2 per cell | 0.851 | seven cells, 22 positives |
| EM32 label-shuffle control | 0.663 | five runs: 0.509–0.742 |

The learned embedding improves by about 0.060 over the same-target raw linear control. The linear control is already close to 0.90, so most of the jump from P1/P5 comes from targeting visible-positive labels; the embedding adds a smaller additional gain. The label-shuffle result is above chance, though its five-run range is wide.

## What was trained

- Inputs: cached hidden-state vectors from `L23:max` and `L16:pre`, concatenated to 5,760 values. No self-attention, tool name, scenario, step number, or other metadata enters the model.
- Structure: robust per-fold scaling and clipping → learned linear projection to 32 dimensions → LayerNorm → GELU → dropout 0.15 → one score head. The projection and score head train together with AdamW and binary cross entropy for 60 epochs.
- Training target: all visible-positive rows under the existing provisional-1 rule plus sampled normal rows; non-visible violations are omitted from this target-specific loss. Family-grouped five-fold OOF scoring, seeds 0/1/2. Every visible positive is kept; normal rows are sampled within tool/source cells from each training fold only.
- Selected development model was retrained once on the full available target data and saved at `artifacts/risk-loop/argus-v-em/argus_v_em_round01.pt`, SHA-256 `fcd8e5ad48119ce546e1f5c89e59d1a0fa40710c5a94b3928618460f0786a505`. `score_checkpoint()` in `experiments/risk_loop/argus_loop/argus_v_em.py` loads it and returns ranking scores for the same 5,760-feature input.
- Detail files: `round01_results.json`, `round01_shuffle.json`, and `round01_linear_control.json`. Training logs and OOF arrays are in the ignored `artifacts/risk-loop/argus-v-em/` directory.

## Limits

- The provisional-1 visibility flags were created after the earlier Argus-V-p scores were examined. This reuses the existing train-split evaluation rows, so the results are development evidence, not an untouched confirmation set.
- Only 22 violations are marked visible (15 unique feature rows). The primary minimum-three metric contains four tool/source cells and 16 visible positives; each cell comes from one scenario family. Adding cells with only two visible positives drops EM32 to 0.851.
- On all violation labels, the OOF result is 0.549. This model is specialized to the visible-violation target and does not establish broad Argus-V1 performance.
- Label shuffling gives 0.663 on average across five runs, so contextual patterns remain. The result needs a larger, preregistered set of new scenarios before claiming generalization. Validation, test, and sealed data were not read.

## Next

Keep EM32 as the current development checkpoint. For any fresh-data confirmation, fix the visibility rule before labels or scores are examined, collect enough independent scenario families, and report visible and all-violation metrics side by side. Do not tune EM32 against the fresh confirmation set.

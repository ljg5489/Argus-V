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

## 그래프와 epoch 곡선 (2026-11-16 추가)

사용자 요청("Argus-V-em은 epoch 등 추가적으로 필요한 그래프를 그려")으로 matplotlib 그래프 14장을 만들었다. PNG와 숫자 표(`tables.md`)는 `figures/`에 있다. 그리는 스크립트는 `experiments/risk_loop/argus_loop/argus_v_em_plots.py`이고 아무것도 학습하지 않는다. 글꼴과 색은 Argus-V-p 그림과 같다(파랑 = 처음 보는 시나리오, 초록 = 학습 데이터).

01 모델별 점수(나누기별 값과 95% 구간) / 02 ROC 곡선 / 03 칸별 ROC / 04 칸별 AUROC / 05 칸별 점수 분포 / 06 채점 대상에 따른 점수 / 07 오경보 고정 탐지율 / 08 혼동 행렬 / 09 문턱별 재현율·정밀도·F1 / 10 정밀도-재현율 / 11 epoch별 손실 / 12 epoch별 성능 / 13 모델별 epoch 곡선 / 14 칸별 epoch 곡선.

"처음 보는 시나리오"는 시나리오 계열 5묶음 중 학습에서 뺀 묶음을 채점한 값(나누기 3가지 평균)이고, "학습 데이터 재채점"은 저장된 최종 32차원 모델이 자기가 학습한 행을 채점한 값이다.

### epoch 곡선을 얻은 방법

round 01은 epoch별 값을 남기지 않았다. 사용자 승인(2026-11-16)을 받아 같은 학습을 설정 그대로 다시 돌리며 epoch마다 기록했다. 실행 전에 `addendum-2.md`로 고정했고 스크립트는 `argus_v_em_epochs.py --approved`다. 32·64·128차원 모델, 선형 대조, 전체 데이터로 맞춘 최종 32차원 모델 모두 마지막 epoch의 점수(최종 모델은 가중치까지)가 저장된 값과 차이 0이다. 따라서 곡선은 저장된 모델이 실제로 지나온 학습 과정이다. 숫자 원본은 `epoch_history.json`.

### 곡선에서 보이는 것 (32차원 모델, 근거가 보인 위반 기준)

| epoch | 손실: 학습에 쓴 행 | 손실: 처음 보는 시나리오 | AUROC: 학습에 쓴 행 | AUROC: 처음 보는 시나리오 |
|---|---|---|---|---|
| 1 | 0.523 | 0.535 | 0.779 | 0.661 |
| 10 | 0.283 | 0.321 | 0.917 | 0.697 |
| 20 | 0.222 | 0.273 | 0.945 | 0.790 |
| 30 | 0.173 | 0.237 | 0.975 | 0.866 |
| 40 | 0.133 | 0.211 | 1.000 | 0.915 |
| 50 | 0.102 | 0.195 | 1.000 | 0.950 |
| 60 | 0.079 | 0.193 | 1.000 | 0.960 |

- 학습에 쓴 행은 40 epoch에 AUROC 1.00에 닿는다(학습 행을 완전히 가른다). 손실은 60 epoch까지 계속 내려간다.
- 처음 보는 시나리오의 AUROC는 처음 10 epoch 동안 0.64~0.70에 머물다가 오르기 시작해 37 epoch에 0.90을 넘고 60 epoch에 0.96이 된다. 마지막 10 epoch의 변화는 0.01이다(가장 높은 값은 56 epoch의 0.963).
- 처음 보는 시나리오의 손실은 0.54에서 0.19로 내려가고 마지막 10 epoch은 거의 그대로다. 64차원(48 epoch)·128차원(33 epoch)·선형 대조(32 epoch)는 괄호 안 epoch에서 가장 낮고 그 뒤로 다시 오른다. 손실이 다시 오르는 구간에서도 임베딩 모델의 AUROC는 계속 오르고, 선형 대조는 0.90 근처에 머문다.
- **0.96은 학습 길이에 달려 있다.** 30 epoch에서 멈췄다면 0.87, 40 epoch이면 0.92다. 60 epoch은 실행 전에 고정한 값이고 이 곡선을 보고 고른 것이 아니다. 다만 곡선의 "처음 보는 시나리오"도 round 01과 같은 개발용 행이므로, 60 epoch이 새 시나리오에서도 맞는 길이인지는 확인되지 않았다.
- 위반 전체로 채점하면 60 epoch 내내 0.48~0.55다. 학습이 진행돼도 근거가 보이지 않은 위반은 가르지 못한다.
- 칸별로 보면(그림 14) `deliver_approved_report`는 첫 epoch부터 1.00에 가깝고, `record_independent_review`는 0.64에서 시작해 20 epoch에 1.00이 된다. `bash`는 20 epoch까지 우연 수준(0.48~0.56)이다가 40 epoch에 0.89로 오른다. `fetch_replacement_reviewer`는 0.41에서 계단식으로 올라 60 epoch에 0.96이 된다(위반 3개·정상 3개라 쌍이 9개뿐). 전체 곡선의 상승은 뒤의 세 칸(위반 4·5·3개)에서 나온다.
- 선형 대조는 24 epoch에 0.90에 닿은 뒤 0.89~0.92에 머문다(60 epoch 뒤 0.899). 임베딩 모델은 더 늦게 오르지만(64차원 44 epoch, 128차원 48 epoch에 0.90) 끝에는 더 높다(0.94~0.96).

### 그림을 그리며 확인된 것

- 주 지표의 95% 구간(시나리오 계열 9개를 복원 추출, 2,000회): 32차원 0.894~1.000, 선형 대조 0.844~0.973, 같은 행으로 잰 Argus-V-p P1 0.389~1.000.
- 주 지표에 들어가지 않는 보조 칸(근거가 보인 위반 2개) 셋 중 둘은 처음 보는 시나리오에서 가르지 못한다: `issue_payment` 0.47, `grant_review_access` 0.21(`run_program`은 1.00). 학습 데이터 재채점에서는 일곱 칸 모두 1.00이다. 칸에 2개 이상 기준이 0.851로 떨어지는 이유다.
- 문턱 하나를 모든 도구에 적용해도(그림 07·08) 처음 보는 시나리오에서 근거가 보인 위반 22개 중 17개를 잡는다(정상의 5%인 461개가 오경보, 정밀도 3.6%). 도구를 섞어 잰 AUROC는 0.918이다. 근거가 보이지 않은 위반 54개는 이 계산에서 빠져 있다.
- 최종 모델의 학습 데이터 재채점은 주 지표 1.000, 위반 전체 0.664다.

## Next

Keep EM32 as the current development checkpoint. For any fresh-data confirmation, fix the visibility rule before labels or scores are examined, collect enough independent scenario families, and report visible and all-violation metrics side by side. Do not tune EM32 against the fresh confirmation set.

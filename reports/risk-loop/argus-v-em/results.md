# Argus-V-em — round 01 results (2026-11-15)

> **2026-11-16 추가 — test 결과.** 아래의 0.960은 train 분할 안 교차검증 값이다(train 시나리오를 5묶음으로 나눠, 4묶음으로 학습하고 남은 1묶음을 채점하기를 5번 한 것). 같은 날 test 분할을 한 번 채점했을 때 이 모델(32차원, 60 epoch)의 같은 지표는 **0.667**(근거가 보인 위반 3개, 비교 15쌍)이었고, 모든 호출을 정상 대 위반으로 가른 값은 0.669였다. 0.960을 "처음 보는 시나리오 성능"이라고 부르지 않는다. 자세한 내용은 `../argus-v-em300/results.md`.

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

사용자 요청("Argus-V-em은 epoch 등 추가적으로 필요한 그래프를 그려")으로 matplotlib 그래프 14장을 만들었다. PNG와 숫자 표(`tables.md`)는 `figures/`에 있다. 그리는 스크립트는 `experiments/risk_loop/argus_loop/argus_v_em_plots.py`이고 아무것도 학습하지 않는다. 글꼴과 색은 Argus-V-p 그림과 같다(파랑 = train 안 교차검증, 초록 = 학습 데이터).

01 모델별 점수(나누기별 값과 95% 구간) / 02 ROC 곡선 / 03 칸별 ROC / 04 칸별 AUROC / 05 칸별 점수 분포 / 06 채점 대상에 따른 점수 / 07 오경보 고정 탐지율 / 08 혼동 행렬 / 09 문턱별 재현율·정밀도·F1 / 10 정밀도-재현율 / 11 epoch별 손실 / 12 epoch별 성능 / 13 모델별 epoch 곡선 / 14 칸별 epoch 곡선.

"train 안 교차검증"은 train 분할의 시나리오 계열을 5묶음으로 나눠, 4묶음으로 학습하고 남은 1묶음을 채점하기를 묶음을 바꿔 가며 5번 한 값(나누기 3가지 평균)이고, "학습 데이터 재채점"은 저장된 최종 32차원 모델이 자기가 학습한 행을 채점한 값이다.

### epoch 곡선을 얻은 방법

round 01은 epoch별 값을 남기지 않았다. 사용자 승인(2026-11-16)을 받아 같은 학습을 설정 그대로 다시 돌리며 epoch마다 기록했다. 실행 전에 `addendum-2.md`로 고정했고 스크립트는 `argus_v_em_epochs.py --approved`다. 32·64·128차원 모델, 선형 대조, 전체 데이터로 맞춘 최종 32차원 모델 모두 마지막 epoch의 점수(최종 모델은 가중치까지)가 저장된 값과 차이 0이다. 따라서 곡선은 저장된 모델이 실제로 지나온 학습 과정이다. 숫자 원본은 `epoch_history.json`.

### 곡선에서 보이는 것 (32차원 모델, 근거가 보인 위반 기준)

| epoch | 손실: 학습에 쓴 행 | 손실: train 안 교차검증 | AUROC: 학습에 쓴 행 | AUROC: train 안 교차검증 |
|---|---|---|---|---|
| 1 | 0.523 | 0.535 | 0.779 | 0.661 |
| 10 | 0.283 | 0.321 | 0.917 | 0.697 |
| 20 | 0.222 | 0.273 | 0.945 | 0.790 |
| 30 | 0.173 | 0.237 | 0.975 | 0.866 |
| 40 | 0.133 | 0.211 | 1.000 | 0.915 |
| 50 | 0.102 | 0.195 | 1.000 | 0.950 |
| 60 | 0.079 | 0.193 | 1.000 | 0.960 |

- 학습에 쓴 행은 40 epoch에 AUROC 1.00에 닿는다(학습 행을 완전히 가른다). 손실은 60 epoch까지 계속 내려간다.
- train 안 교차검증의 AUROC는 처음 10 epoch 동안 0.64~0.70에 머물다가 오르기 시작해 37 epoch에 0.90을 넘고 60 epoch에 0.96이 된다. 마지막 10 epoch의 변화는 0.01이다(가장 높은 값은 56 epoch의 0.963).
- train 안 교차검증의 손실은 0.54에서 0.19로 내려가고 마지막 10 epoch은 거의 그대로다. 64차원(48 epoch)·128차원(33 epoch)·선형 대조(32 epoch)는 괄호 안 epoch에서 가장 낮고 그 뒤로 다시 오른다. 손실이 다시 오르는 구간에서도 임베딩 모델의 AUROC는 계속 오르고, 선형 대조는 0.90 근처에 머문다.
- **0.96은 학습 길이에 달려 있다.** 30 epoch에서 멈췄다면 0.87, 40 epoch이면 0.92다. 60 epoch은 실행 전에 고정한 값이고 이 곡선을 보고 고른 것이 아니다. 다만 곡선의 "train 안 교차검증"도 round 01과 같은 개발용 행이므로, 60 epoch이 새 시나리오에서도 맞는 길이인지는 확인되지 않았다.
- 위반 전체로 채점하면 60 epoch 내내 0.48~0.55다. 학습이 진행돼도 근거가 보이지 않은 위반은 가르지 못한다.
- 칸별로 보면(그림 14) `deliver_approved_report`는 첫 epoch부터 1.00에 가깝고, `record_independent_review`는 0.64에서 시작해 20 epoch에 1.00이 된다. `bash`는 20 epoch까지 우연 수준(0.48~0.56)이다가 40 epoch에 0.89로 오른다. `fetch_replacement_reviewer`는 0.41에서 계단식으로 올라 60 epoch에 0.96이 된다(위반 3개·정상 3개라 쌍이 9개뿐). 전체 곡선의 상승은 뒤의 세 칸(위반 4·5·3개)에서 나온다.
- 선형 대조는 24 epoch에 0.90에 닿은 뒤 0.89~0.92에 머문다(60 epoch 뒤 0.899). 임베딩 모델은 더 늦게 오르지만(64차원 44 epoch, 128차원 48 epoch에 0.90) 끝에는 더 높다(0.94~0.96).

### 그림을 그리며 확인된 것

- 주 지표의 95% 구간(시나리오 계열 9개를 복원 추출, 2,000회): 32차원 0.894~1.000, 선형 대조 0.844~0.973, 같은 행으로 잰 Argus-V-p P1 0.389~1.000.
- 주 지표에 들어가지 않는 보조 칸(근거가 보인 위반 2개) 셋 중 둘은 train 안 교차검증에서 가르지 못한다: `issue_payment` 0.47, `grant_review_access` 0.21(`run_program`은 1.00). 학습 데이터 재채점에서는 일곱 칸 모두 1.00이다. 칸에 2개 이상 기준이 0.851로 떨어지는 이유다.
- 문턱 하나를 모든 도구에 적용해도(그림 07·08) train 안 교차검증에서 근거가 보인 위반 22개 중 17개를 잡는다(정상의 5%인 461개가 오경보, 정밀도 3.6%). 도구를 섞어 잰 AUROC는 0.918이다. 근거가 보이지 않은 위반 54개는 이 계산에서 빠져 있다.
- 최종 모델의 학습 데이터 재채점은 주 지표 1.000, 위반 전체 0.664다.

## 이 문서의 "검증"은 validation 분할이 아니다 (2026-11-16, 사용자 질문으로 명시)

사용자 질문: "validation이나 test 데이터로 나눈 거 활용해서 검증한 거 맞지?" **아니다.** 이 문서의 held-out, "train 안 교차검증"(2026-11-16 저녁까지는 "처음 보는 시나리오"라고 적었다), "검증"은 모두 train 분할(시나리오 102개, 계열 41개) 안에서 계열을 5묶음으로 나눠 학습에서 뺀 묶음을 채점한 교차검증 값이다. 채점한 묶음의 시나리오는 그 모델이 학습 때 보지 않았지만, train 데이터는 채점 대상·표시 규칙·모델 크기를 정하는 데 이미 여러 번 썼다. 이 절을 쓴 시점에는 따로 나눠 둔 validation·test 분할을 한 번도 열지 않았다(같은 날 저녁 사용자 지시로 test 분할을 한 번 채점했다: 같은 지표 0.667, 문서 맨 위 참고).

`reports/risk-loop/argus-v1/loop/TASK.md` §0의 규칙으로는 성공 조건을 모두 통과한 후보만 validation을 한 번 보고, test는 사용자 승인 전까지 봉인이다. Argus-V-em은 그 조건 중 라벨 섞기 두 가지(각 20회), 출처별(10월·11월 따로) 점수, 안쪽 묶음으로 고른 설정, 감사를 아직 거치지 않았다(주 지표의 칸 넷은 모두 10월 기록이라 11월 점수는 지금 정의되지 않는다). validation의 위반은 10월 12개, 11월 134개이고 11월은 대부분 채점에서 빼는 보고 내용 위반이라, 열어도 근거가 보인 위반이 적을 가능성이 크다. 권고는 저장된 32차원 모델과 표시 규칙을 미리 고정해 두고 새로 만드는 위반 시나리오로 한 번 채점하는 것이다(사용자 결정 대기).

발표에는 "validation으로 검증"이 아니라 "train 안 교차검증(학습에 없던 시나리오 묶음)"이라고 적는다.

## 0.92~0.96을 얼마나 믿을 수 있나 (2026-11-16, 사용자 질문)

사용자 질문(epoch 곡선을 보고): "40 epoch부터 뭐야? 과적합도 아닌데 validation에서 0.92가 나온다고?" 학습 없이 저장된 점수와 기록만으로 확인했다. 스크립트는 `experiments/risk_loop/argus_loop/argus_v_em_heldout_check.py`.

**검증 자체는 깨끗하다.**

- 묶음 15개(5묶음 × 나누기 3가지) 모두에서 학습 쪽과 검증 쪽에 같은 입력 0개, 같은 시나리오 0개, 같은 계열 0개.
- 근거가 보인 위반 22개 각각에 대해 다른 계열에서 가장 비슷한 행을 찾으면 유사도(표준화한 벡터의 코사인)가 0.41~0.86이고, 그 행은 18개가 정상 호출이다. 다른 계열에 복사본에 가까운 위반이 있어서 맞힌 것이 아니다.
- 모델 없는 규칙으로는 같은 행에서 "앞선 step일수록 위반" 0.688, "그 실행에서 그 도구의 첫 호출이 위반" 0.621이다. 순서만으로 나오는 점수가 아니다(`bash` 칸만은 순서 규칙이 0.90으로 모델의 0.89와 같다).

**숫자가 높은 이유.**

- 채점 대상이 좁다. 같은 16개로 재면 Argus-V-p P1·P5 0.76, 이전 최고 모델 T7-a 0.79이고, 이 대상만으로 학습한 선형 대조가 0.90이다.
- 16개는 서로 다른 입력으로 10개다. 같은 hidden state가 여러 실행에 복제돼 있다: `bash` 5개 중 3개, `deliver_approved_report` 4개 중 2개, `record_independent_review` 4개 중 2개, `fetch_replacement_reviewer` 3개 중 3개. 시나리오로는 5개(AV-S01, AV-S36, AV-S42, AV-S46, AV-S55)이고 `bash`를 뺀 세 칸은 시나리오 하나씩이다.
- T7-a(0.788)와의 차이 0.172는 칸별로 `fetch_replacement_reviewer` +0.139(0.22 → 0.96, 비교 쌍 9개), `record_independent_review` +0.041, `bash` −0.008이다. 차이의 대부분이 위반 3개·정상 3개짜리 칸 하나다.
- 40 epoch에서 60 epoch 사이 +0.044는 `fetch_replacement_reviewer`에서 쌍 2개가 뒤집힌 +0.042와 `bash`의 +0.003이다.

**과적합인가 (같은 날 사용자 지적으로 바로잡음).** 처음에는 "과적합이 맞다"고 적었는데 틀린 표현이었다. 사용자 지적: "검증 AUROC가 epoch이 많아질수록 계속 올라간다. 오히려 일반화 성능이 올라가는 것 아닌가?" 맞다. "검증 성능이 나빠진다"는 뜻의 과적합은 60 epoch 안에서 일어나지 않았다.

- 이 모델은 전체 행을 한꺼번에 넣어 학습하므로 1 epoch이 가중치를 한 번 고치는 것이다. 60 epoch은 60번 고친 것이고 아직 학습 초반이다.
- 32차원 모델의 검증 AUROC는 주 지표 0.66 → 0.96, 위반 2개 이상 칸까지 0.59 → 0.85, 복제된 입력을 하나로 쳐도 0.49 → 0.78로 오른다. 칸별로도 일곱 중 다섯에서 오른다(`fetch_replacement_reviewer` 0.41 → 0.96, `bash` 0.56 → 0.89, `record_independent_review` 0.64 → 1.00, `run_program` 0.86 → 1.00, `issue_payment` 0.03 → 0.47). 표는 `figures/tables.md`의 "검증 AUROC가 epoch에 따라 오르는가".
- 오르지 않는 것: 위반 전체로 채점한 값(내내 0.50~0.55), `grant_review_access`(0.21에 머묾). `issue_payment`는 우연 수준까지만 오른다. 주 지표는 마지막 7 epoch 동안 0.96에서 평평하다.
- 학습 쪽과의 격차는 있다: 학습 행은 40 epoch에 1.00, 손실은 학습 0.08 대 검증 0.19. 32차원 모델은 검증 손실도 나빠지지 않았고(마지막 10 epoch 동안 그대로), 64·128차원 모델과 선형 대조는 33~48 epoch 뒤 검증 손실만 조금 오른다(점수가 지나치게 확신하는 쪽으로 가지만 순위는 계속 좋아진다).
- 따라서 "근거가 보인 위반은 학습할수록 train 안 교차검증에서도 더 잘 가른다"고 말할 수 있다. 측정이 서로 다른 위반 입력 10~15개에 대한 것이라는 한계는 그대로다. 더 오래 학습하면 어디서 꺾이는지는 재 보지 않았다(추가 학습이라 사용자 승인 필요, 같은 개발용 행으로 epoch 수를 고르게 되므로 그 값은 낙관적이다).

**복제된 입력을 하나로 치면** 칸에 위반 2개 이상 기준이 0.851 → 0.777(위반 14개, 칸 6개)이 된다. 3개 이상 기준은 0.918이지만 남는 것이 위반 6개·칸 2개뿐이다(`figures/tables.md`).

**정리.** 말할 수 있는 것은 "행동 전에 근거가 보인 위반은, 학습에 없던 시나리오 5개에서 hidden state로 갈렸다"이다. "검증 성능 0.92~0.96"이라고는 말할 수 없다. 서로 다른 위반 입력이 10개이고, 보조 칸 둘이 실패하고(0.21, 0.47), 라벨을 섞어도 0.66이 나오고, 표시 규칙을 점수를 본 뒤에 만들었기 때문이다. 발표 문구는 "개발용 데이터에서 근거가 보인 위반 16개(서로 다른 입력 10개, 시나리오 5개)에 대해 0.96, 위반 전체로는 0.55, 새 시나리오로 확인 필요"를 권한다.

## Next

Keep EM32 as the current development checkpoint. For any fresh-data confirmation, fix the visibility rule before labels or scores are examined, collect enough independent scenario families, and report visible and all-violation metrics side by side. Do not tune EM32 against the fresh confirmation set.

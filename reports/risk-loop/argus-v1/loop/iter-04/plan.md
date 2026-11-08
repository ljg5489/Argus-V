# 반복 4 계획 (모델 연구, 2026-11-08, 반복 4 계산을 돌리기 전에 작성)

규칙: `../TASK.md`. 평가 코드 `experiments/risk_loop/argus_loop/evaluate.py` **v4** (동결, sha256 `a7c36eafdf994f98b61895be4e4b8d237740d0018422d12febab8deb9df0130d`, 고치지 않음). validation·test는 보지 않는다. 11월 라벨은 **초안**(규칙 라벨). 평가 행은 반복 1~3과 같은 `iter01_common.headline_filter` 행(9,278 행동 / 위반 79, 판정 칸 10개 / 위반 52).

이번 반복은 **대부분 진단**이다. 진단은 모델 시도 수에 넣지 않고 따로 적는다. 모델 시도는 T4-1 하나(변형 최대 2개)뿐이다.

## 질문

반복 1~3의 55개 시도 최고(0.62~0.66)가 늘 라벨 섞기 (b)(출처×family 안에서 섞어 학습, 약 0.57~0.59)보다 0.02~0.05만 높았다. 섞인 라벨로 학습한 모델이 왜 같은 도구×출처 칸 안에서 0.59를 내는가? 판정 지표가 "이 행동이 위반인가"를 재는가, 아니면 "이 rollout이 위험한 rollout인가"를 재는가?

## D4-1 판정 지표가 재는 것 (진단)

- 기준 모델: 반복 2의 H2-1c-L23(층 23 max, 정상 가중치 상향 LogReg). 섞기 시험이 쓰는 격자 값(바깥 fold가 가장 자주 고른 값, index 5 = k 32, C 0.1)으로 고정.
- 평가 코드 `shuffle_test`와 **같은 절차**(fold seed 0, 5-fold, 학습 fold 안에서 출처×family 칸마다 같은 난수 규칙으로 섞기, perm_seed 0, j = 0..19)를 진단 스크립트에서 다시 돌려 **OOF 점수를 저장**한다(평가 코드는 OOF를 돌려주지 않음). 같은 도구 안 값이 평가 코드 v4 결과(평균 0.591)와 같은지 확인한다. 출처 안 섞기 (a)도 20회 같은 방식으로 저장한다(대조군).
- 진단에만 읽는 변수(모델 입력 아님): `steps.csv`의 `scenario_id`, `condition`(C0/C1/C2, pilotX/cellN 등), `seed`, 그리고 라벨에서 만든 "trajectory 안에 위반이 있는가"(자기 자신 제외 / 포함 두 가지).
- 계산 (판정 칸 10개 각각, 칸 위반 수 가중 평균):
  1. 변수 하나만으로 라벨을 구분하는 AUROC: step_index, prefix_length (값 그대로, 방향 둘 다 보고), trajectory 위반 여부(다른 step 기준), 시나리오·조건(범주형이므로 칸 안 위반 비율로 순서를 매긴 **낙관적 상한**; 표시).
  2. 진짜 라벨 모델·섞기 모델 OOF 점수를 정상 행의 종류별로 나눈 AUROC: 위반 vs (a) 같은 trajectory 정상, (b) 위반이 있는 다른 trajectory 정상, (c) 위반 없는 trajectory 정상, (d) 다른 시나리오 정상.
  3. 정상 행만 놓고 "trajectory에 위반이 있는가"를 섞기 모델 점수가 구분하는 AUROC, 조건 코드별 평균 점수.
- 판단 기준(사전 등록): 섞기 모델이 (c)(d)에서 높고 (a)(b)에서 0.5 근처면 "판정 지표는 위험 rollout 구분을 부분적으로 잰다"로 숫자와 함께 적는다.

## D4-2 칸 해부 (진단)

칸마다: 출처, 도구, 위반·정상 수, 각 쪽의 시나리오·family·trajectory 수, 정상 중 위반이 있는 trajectory에서 온 수(같은 trajectory / 다른 trajectory), 판정 지표 가중치(칸 위반 수 / 52).

## T4-1 같은 rollout 쌍 학습 (모델 시도 1개, 변형 2개 = 시도 2개로 셈)

- 학습 fold 안에서 같은 trajectory의 (위반 step, 정상 step) 쌍만 만든다(위반마다 쌍 가중치 합 1). 특징은 학습 행으로 맞춘 표준화 → PCA(kmax 128, 처음 k개) 공간의 차이, 절편 없는 pairwise logistic loss. 점수 = step 하나의 선형 점수. 도구 이름·출처·조건 코드는 쓰지 않는다(쌍 만들 때 trajectory id만 학습 행에서 사용; trajectory id는 fold 묶음에 이미 쓰이는 행 식별자이고 점수 시점에는 쓰지 않음).
- **T4-1a**: 층 23 max. **T4-1b**: 층 16 pre(반복 1 최고 표현).
- 격자 k {10, 32, 128} × C {0.001, 0.01, 0.1}, nested CV, `evaluate.evaluate()` v4 전체(섞기 각 20회)로 계산.
- 후보 인정 조건(사전 등록, 반복 3과 같음): (i) 같은 도구 안 − 섞기 (b) 평균 ≥ 0.10, (ii) 같은 도구 안 − 길이+step 0.522 ≥ 0.05. 감시 R1: 이전 최고(0.656/0.645) 대비 +0.12 이상일 때만 "실제 개선".
- 누적 시도: 55 + 2 = 57.

## D4-3 다른 지표 미리보기 (보고만, 판정 아님)

- "같은 rollout 안 순위 AUROC": 위반과 정상이 모두 있는 trajectory마다 그 안에서 AUROC, trajectory의 위반 수로 가중 평균(또는 모든 같은-trajectory 쌍을 합친 값도 함께). trajectory는 한 fold에만 있으므로 fold 사이 점수 차이가 섞이지 않는다.
- 대상: H2-1c-L23(저장된 full OOF), T4-1a/b, H1-0a(Argus-V1 기본, 저장된 OOF), 길이+step 기준선(같은 fold로 다시 계산), 섞기 (b)·(a) 모델(D4-1에서 저장).
- 보고: 이 지표에 쓰이는 trajectory·위반 수(headline 행 기준, 판정 칸 한정 / 전체 headline 두 가지), family bootstrap 95% CI.

## 실행

- 코드: `iter04_common.py`(진단 변수, 칸 해부, 같은 trajectory 쌍, 순위 지표), `iter04_models.py`(T4-1 모델), `iter04_diag.py`(D4-1·D4-2·D4-3), `iter04_scan.py`(T4-1), 테스트 `test_iter04.py`. `models.py`·`evaluate.py`는 고치지 않는다.
- 작업 ≤ 2, mmap, 분리 실행. 산출물 `iter-04/cv_report.json`, `diagnostics.md`, `candidates.md`.

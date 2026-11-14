# 토론 브리프 — Argus-V1 "학습된 투영 → 최대 풀링" 구조 (2026-11-09)

## 사용자 요구 (원문 요지)
- Argus-V1은 동결된 gpt-oss-20b **옆에 붙어** hook으로 은닉층을 읽고, 행동이 나가기 전에 위험한 의도인지 판단하는 모델이다(LLM 출력은 바꾸지 않음).
- 지금 모델은 위험한 의도를 **모른다**. 은닉층은 실수값 텐서일 뿐이고, 관측 지점들을 좌표별 max 하나로 뭉갠다.
- 사용자가 원래 원한 것은 CNN처럼 **학습된 투영(필터) → 최대 풀링**으로 특징을 뽑는 구조다.
- "너무 가볍게만 가지 말고, 우선은 **추론해서 답을 낼 수 있는 모델**이 나와야 한다." 즉 실제 hook 입력을 받아 위험 점수/판단을 내는 end-to-end 추론 경로까지 설계한다.

## 현재 사실 (근거 파일)
- 루프 규칙·지표: `reports/risk-loop/argus-v1/loop/TASK.md` (판정 지표 = 같은 도구×출처 칸 안 AUROC, family 단위 CV, 라벨 섞기 대조, nested CV, validation은 성공 후보만, test 봉인; §3 입력 규칙: 행동 전 관측 activation만, 도구 이름·출처는 입력 금지).
- 데이터 구조: `loop/data/card.md` §1 — step마다 `features.npz`의 `block_0000`~`block_0023`, 각 `[n_obs, 2880]` float32. 관측 행 순서 `pre_reasoning` → `reasoning+32`, `+64`, …(추론 32토큰마다) → `reasoning_end` → `pre_action`. 모두 행동 토큰 **앞**. HF `hakuuung/gpt-oss-20b-hidden-state-raw-data` revision `57a4bdcd`(읽기 전용). 지금 로컬 캐시(`artifacts/risk-loop/argus-v1-loop/features/`)에는 **풀링된 값만**(층 8·11·14·16·20·23 × max/mean/pre/rend) 있고 관측 지점별 텐서는 없다.
- 현재 최고: T7-a(`loop/final/card.md`, `experiments/risk_loop/argus_loop/final_models.py`) — 견고한 척도+자르기 → PCA 32 → 점별 로지스틱 1개 + 같은 rollout 쌍 학습 2개 → 백분위 평균. 라벨 v2에서 0.721(seed 10), 성공 기준 실패. 상당 부분이 "위험한 rollout" 신호.
- 비선형 시도: 반복 7 T7-c(쌍 학습 + 은닉층 1개 MLP) 0.550으로 선형보다 나쁨(`loop/iter-07/candidates.md`) — 위반 79개·쌍 300개 규모.
- 원인 진단: `loop/iter-11/diagnosis.md` (칸 작음·칸당 시나리오 1개, 칸 안 낙관 상한 0.8~0.87, 학습 곡선 2배당 +0.06, 지표 잡음).
- 새 데이터 예정: `loop/iter-12/data_plan.md`, `iter-12/HANDOVER.md` — 새 v2 시나리오 20개 + v1 재실행 72, 사용자가 RTX 4090에서 `argus_hook/scenario_rollout.py`로 실행 후 HF 업로드. 예상 train 판정 위반 100~180개, 칸 17~19개. 새 출처 `dec`, 판정에는 사람 검수 행만.
- hook·캡처 코드: `argus_hook/` (어떤 층·지점을 저장하는지, 추가 캡처가 가능한지 여기서 확인).
- 라벨: 10월 사람 확인, 11월 규칙 초안 + 사용자 관례 2개(`loop/iter-11/nov_review_14.md`). 규칙 라벨(`policy_label`)은 v2 rollout 1,920개 등 대량으로 있음.

## 자원
- 이 PC: GPU 없음, RAM 15.5GB, CPU 18코어, 디스크 여유 약 41GB, `py -3.11`. HF 읽기만.
- 4090 PC(사용자): rollout·캡처 실행. 캡처 방식을 바꾸려면 시나리오 실행 **전에** 사용자에게 넘겨야 한다.

## 토론 규칙
- 각자 맡은 역할 관점에서 **구체적으로**: 수식/텐서 모양/파라미터 수/학습 손실/정규화/데이터 양 대비 과적합 위험/평가 방법/추론 경로/비용.
- 주장마다 근거(파일 경로, 숫자, 알려진 연구)를 붙인다. 모르면 "확인 못 함".
- 계산 실험은 하지 않는다(짧은 확인용 조회 ≤2분은 허용: 파일 읽기, 텐서 모양·관측 지점 수 확인 등). validation·test 단위는 읽지 않는다. 파일 삭제·커밋·HF 쓰기 금지.
- 자기 라운드 결과는 `reports/risk-loop/argus-v1/loop/iter-13/debate/` 아래 지정된 파일에만 쓴다. 한국어, 쉬운 말.

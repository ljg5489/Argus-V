# Argus-V-p 장부 — 여기서 돌린 학습 전부

Argus-V1 루프의 시도 장부(누적 169, 보수 171)와 별개다. 여기 값은 판정 지표의 후보가 아니다.

| 날짜 | 무엇 | 학습 횟수 | 결과가 있는 곳 |
|---|---|---|---|
| 2026-11-15 | 조건 C(학습 데이터 재채점): 설정 6개를 전체 행에 한 번씩 | 6 | `results.json` |
| 2026-11-15 | 조건 B(이미 본 시나리오의 새 실행): 설정 6개 × 나누기 3가지 × 5겹 | 90 | `results.json`, `artifacts/risk-loop/argus-v-p/oof_*_B_*.npy` |
| 2026-11-15 | 조건 A(처음 보는 시나리오): P3~P6 × 나누기 3가지 × 5겹. P1·P2는 반복 14의 저장된 점수를 다시 읽음 | 60 | 같은 곳, `oof_*_A_*.npy` |
| 2026-11-15 | 학습 데이터 점수 사다리: P5의 선형 구성원 규제를 한 단계 더 완화(전체 행 1회) | 1 | `results.json`의 `ladder_C` |
| 2026-11-15 | 누수 점검: P5, 학습 라벨을 칸 안에서 섞고 조건 B를 5회 | 25 | `results.json`의 `shuffle_check_B` |
| 2026-11-15 | 모델 파일 저장: P5를 전체 행에 한 번 | 1 | `artifacts/risk-loop/argus-v-p/model/argus_v_p.pkl` |
| 2026-11-15 | 목표 기준 재채점과 그래프: 설정별 전체 행 학습을 다시 계산(같은 학습의 반복, 새 설정 없음) | — | `visible_results.json`, `figures/` |
| 2026-11-15 | 발표 사례 분석: P6 조건 C를 한 번 재현해 행별 점수와 시나리오 호출을 복구(새 설정·선택 아님) | 1회 진단 재적합 | `p6_scenario_analysis.md`, `.json`, `artifacts/risk-loop/argus-v-p/p6_condition_c_scores.npy` |

- 설정 수: 6개(P1~P6) + 사다리 1개. 전부 `results.md`에 보고했다.
- 고른 것: 조건 B 값으로 P5를 Argus-V-p로 정함(실행 전에 고정한 규칙).
- 쓰지 않은 것: validation·test·봉인 데이터, step 번호·길이·도구 이름 같은 hidden state 밖의 입력.

# 새 분할(resplit-1117)의 test 사용 기록

새 분할의 test를 채점할 때마다 한 줄씩 적는다. 첫 줄만이 "그 분할을 한 번도 보지 않고" 잰 값이다. 그 뒤로는 앞선 결과를 본 뒤에 만든 설정을 같은 test로 재는 것이므로, 그 값으로 고른 설정의 점수를 성능이라고 적지 않는다. (기존 분할의 test 사용 기록은 `../argus-v-em300/test-use-log.md`.)

| 번호 | 시각 | 무엇을 채점했나 | 근거 | 기록 |
|---|---|---|---|---|
| 1 | 2026-11-17 00:31~00:57 | 새 train으로 학습한 Argus-V-em 12개 설정(모델 4 × 위반 가중치 3, 반복 3번, epoch 1~100)과 Argus-V-p 6개 설정 | 사용자 지시("… 각각 모든 모델에 대해 100epoch씩 학습을 진행 해 그리고 성능평가에 필요한 모든 정보를 저장하고 루프 시작"), 학습 전에 읽는 법 고정(`run01/README.md`, 커밋 `28ce0dd`) | `run01/results.md`, `run01/tables.md`, `run01/results.json`, `run01/epoch_table.csv` |
| 2 | 2026-11-17 01:20~01:50 | 1번에서 저장한 점수를 다시 채점: 64차원·약 60배 모델을 근거가 보인 위반 10개 전부·위반 26개 전부로 채점, 위반 / 정상 판정, 모델 평균·섞기·점수 보정 16가지 비교 | 사용자 지시("10개 모두 사용해서 완전한 test를 해봐", "전체 test 데이터를 이용해 위반인지 정상인지 맞추게 해", "AUROC를 높일 수 있는 방안을 도출해") | `run01/full_test_EM64_w60.md`, `run01/classification_test_EM64_w60.md`, `run01/auroc_levers.json` |
| 3 | 2026-11-17 02:13 | Argus-V-emp(Argus-V-em 12개 설정 + Argus-V-p P3·P5를 섞은 모델)의 test 전체 채점과 위반 / 정상 판정. 새 학습 없음 | 사용자 지시("섞은 모델을 Argus-V-emp로 이름잡고 그것으로 다시 전체 test 진행해봐"). 정의는 채점 전에 고정(`argus_v_emp.py`)했지만, 이 조합 자체가 2번의 비교(validation과 test를 모두 봄)에서 나온 것이다 | `../argus-v-emp/README.md`, `full_test.md`, `classification_test.md` |
| 4 | 2026-11-17 02:23~02:39 | 1번에서 저장한 모든 모델(Argus-V-p 6개, Argus-V-em 12개 설정)과 Argus-V-emp의 점수를 같은 방법(전부 비교 / 같은 시기끼리 / 같은 도구끼리, validation 5% 문턱에서 잡은 수, 오경보 중 10월 기록의 비율)으로 다시 채점해 한 표로 모음. 새 학습 없음 | 사용자 지시("지금까지 과정을 봐보자 … 표 형식으로 보기 편하게 작성") | `../model_history.md`, `../argus-v-emp/overview_table.json`, `overview_tables.md` |
| 5 | 2026-11-17 03:40~03:56 | 발표용 그림을 저장된 점수로 그림: 새 test의 ROC 곡선(19개 모델 전부, 위반 전부와 근거가 보인 위반), Argus-V-emp의 채점 방법별 ROC 곡선 · 정밀도-재현율 곡선 · 점수 분포 · 커트라인별 재현율/정밀도/F1 · 혼동 행렬 · 구성 모델의 epoch별 AUROC(1~100). 새 학습 없음. 커트라인은 validation에서 정한 값(0.864, 0.932)만 썼고 test 곡선을 보고 고르지 않았다 | 사용자 지시("발표에 필요한 수집된 모든 모델에 대해 성능지표를 matplotlib으로 생성해", "ROC 곡선 그릴 수 있는 것은 무조건 그리고!") | `../model_history_figures/README.md`, `numbers.json` |
| 6 | 2026-11-17 04:07~04:08 | Argus-V-p P3·P5를 같은 설정·같은 train으로 다시 학습해 모델 파일로 저장하고(사용자 승인), 저장한 모델 폴더만으로 validation·test를 다시 채점해 저장돼 있던 점수와 비교. 새 값을 얻은 것이 아니라 같은 점수가 나오는지 확인한 것: 가장 큰 차이 0, 새 test AUROC 0.913 그대로 | 사용자 지시("Argus-V-p P3·P5를 모델 파일로 저장하는 학습 시작하고 저장해") | `../argus-v-emp/README.md`의 "모델 파일" 절, `artifacts/risk-loop/resplit-1117/argus_v_emp/manifest.json` |

읽는 법(1번에서 미리 정한 것): 보고하는 값은 ① 정해 둔 레시피(64차원·약 15배·67 epoch) ② 설정마다 validation으로 고른 epoch ③ 전체에서 validation으로 고른 하나. test 값으로는 아무것도 고르지 않는다.

주의: 새 test에는 기존 train에 있던 계열 7개가 들어 있다. 새 모델의 가중치는 그 데이터로 학습하지 않았지만 모델 구조·근거 표시 규칙·epoch 선택은 그 데이터를 보며 정했다.

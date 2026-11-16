# test 분할 사용 기록

test 분할을 채점할 때마다 한 줄씩 적는다. 첫 번째 줄만이 "한 번도 보지 않은 데이터"로 잰 값이다. 그 뒤의 채점은 test 결과를 본 뒤에 만든 모델·설정을 같은 test로 재는 것이므로, 그 값을 보고 모델을 고르면 숫자가 실제보다 좋게 나온다. validation 분할과 봉인 단위(AV-S61~S80)는 이 문서를 쓰는 시점까지 열지 않았다.

| 번호 | 시각 | 무엇을 채점했나 | 근거 | 기록 |
|---|---|---|---|---|
| 1 | 2026-11-16 20:15 | 주 모델(64차원, 67 epoch) + 참고 모델 3개(300 epoch 128차원, Argus-V-em 60 epoch, Argus-V-p) + 300 epoch 학습의 10 epoch마다 저장본 30개 | 사용자 지시("이번에는 정말 TEST 데이터를 가지고 성능평가를 시작해"), 채점 전에 방법 고정(`test-eval-prereg.md`, `test-eval-prereg-addendum-1.md`) | `test_eval.json`, `test_tables.md`, `figures_test/` |
| 2 | 2026-11-16 22:39 | 위반 가중치 세 설정(약 15배·약 60배·약 230배)을 전체 train 행으로 맞춘 64차원 모델, epoch 1~100 | 사용자 지시("아니 자꾸 test는 왜 안 하냐고"), 채점 전에 읽는 법 고정(`class-weight-check.md`의 "추가" 절, 커밋 `8477752`) | `class_weight_check_test.json`, `figures_weight/02_test_위반_가중치별_epoch_곡선.png` |
| 3 | 2026-11-16 23:04 | 위반 가중치를 300으로 고정한 64차원 모델(전체 train 행 학습), epoch 1~100 | 사용자 지시("위반 가중치를 300배로 하고 한 번 학습 및 test를 진행해 보자"), 채점 전에 읽는 법 고정(`class-weight-check.md`의 "추가 2" 절, 커밋 `87a5d3a`) | `class_weight_check_test.json`, `class_weight_check_test_alarms.json` |

## 사용자와 합의한 읽는 법 (2026-11-16)

- 한 모델을 test로 재는 것 자체는 몇 번을 해도 그 모델의 정직한 값이다(test를 한다고 가중치가 바뀌지 않는다).
- 숫자가 부풀려지는 것은 test 값을 보고 여러 후보 중 하나를 고를 때다. 그래서 2번부터는 "잰 값"으로 보고하되, 그 값으로 고른 설정의 점수를 "성능"이라고 적지 않는다.
- 앞으로 실험 결과는 train 안 교차검증 값과 test 값을 나란히 보고한다(사용자 요구). test를 쓸 때마다 이 표에 한 줄을 더한다.

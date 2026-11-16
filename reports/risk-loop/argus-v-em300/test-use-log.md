# test 분할 사용 기록

test 분할을 채점할 때마다 한 줄씩 적는다. 첫 번째 줄만이 "한 번도 보지 않은 데이터"로 잰 값이다. 그 뒤의 채점은 test 결과를 본 뒤에 만든 모델·설정을 같은 test로 재는 것이므로, 그 값을 보고 모델을 고르면 숫자가 실제보다 좋게 나온다. validation 분할과 봉인 단위(AV-S61~S80)는 이 문서를 쓰는 시점까지 열지 않았다.

| 번호 | 시각 | 무엇을 채점했나 | 근거 | 기록 |
|---|---|---|---|---|
| 1 | 2026-11-16 20:15 | 주 모델(64차원, 67 epoch) + 참고 모델 3개(300 epoch 128차원, Argus-V-em 60 epoch, Argus-V-p) + 300 epoch 학습의 10 epoch마다 저장본 30개 | 사용자 지시("이번에는 정말 TEST 데이터를 가지고 성능평가를 시작해"), 채점 전에 방법 고정(`test-eval-prereg.md`, `test-eval-prereg-addendum-1.md`) | `test_eval.json`, `test_tables.md`, `figures_test/` |
| 2 | 2026-11-16 22:05쯤 | 위반 가중치 세 설정(약 15배·약 60배·약 230배)을 전체 train 행으로 맞춘 64차원 모델, epoch 1~100 | 사용자 지시("아니 자꾸 test는 왜 안 하냐고"), 채점 전에 읽는 법 고정(`class-weight-check.md`의 "추가" 절) | `class_weight_check_test.json` |

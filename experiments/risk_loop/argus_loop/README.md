# argus_loop — Argus-V1 성능 향상 루프 코드

규칙: `reports/risk-loop/argus-v1/loop/TASK.md`. 평가 코드 설명과 동결 hash: `reports/risk-loop/argus-v1/loop/eval/HARNESS.md`.

`evaluate.py`는 동결되어 있다. 고치지 말고 가져다 쓴다. Python은 `py -3.11`.

## 모델 연결하기

```python
from experiments.risk_loop.argus_loop import evaluate as E

data = E.load()                       # train 행만 (report_content=1, 라벨 없는 행 제외)
rows = data.rows
X = data.features(16, "max")          # rows와 같은 순서의 특징 행렬

def make_fp(C):                       # 하이퍼파라미터 -> fit_predict
    def fp(X_train, y_train, X_test): # 학습 라벨은 반드시 y_train만 쓴다 (rows.label 금지)
        ...                           # 스케일러·PCA 등 모든 학습은 X_train으로만
        return scores_for_X_test      # 1차원, 길이 len(X_test), 유한값
    return fp

res = E.evaluate(make_fit_predict=make_fp, grid=[0.01, 0.1, 1.0], X_or_rowids=X, rows=rows,
                 name="C-01")         # nested CV + 지표 + 라벨 섞기 + seed 안정성 + 판정
E.dump(res, "reports/risk-loop/argus-v1/loop/iter-01/C-01.json")
print(res["metrics"]["within_tool"]["value"], res["gate"]["verdict"])
```

- 하이퍼파라미터가 고정이면 `grid=[값]` 하나로 돌린다(판정 조건 4는 nested CV일 때만 통과).
- 탐색 중 빠르게 보려면: `cv = E.run_cv(fp, X, rows)` → `E.metrics(cv, rows, bootstrap=0)`. 이 값은 판정에 쓰지 않는다.
- 여러 레이어·풀링을 합치거나 메모리를 아끼려면 `X_or_rowids=None`으로 두면 `fp`가 `rows` 안 위치 번호를 받는다. 그 번호로 직접 특징을 꺼내 쓴다.
- 입력 금지: 라벨, 도구 이름, 출처(10월/11월), family, 시나리오 정보. 허용: activation, `prefix_length`, `step_index`.
- validation은 성공 후보만, 평가 에이전트가 `E.load(validation_look=True)` + `E.validation_metrics(...)`로 1회 본다. test·봉인 행은 어떤 함수도 읽지 않는다.

테스트: `py -3.11 experiments/risk_loop/argus_loop/test_evaluate.py`

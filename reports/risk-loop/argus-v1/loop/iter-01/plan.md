# 반복 1 계획 (모델 연구, 2026-11-08, 특징을 읽기 전에 작성)

규칙: `../TASK.md`. 평가 코드: `experiments/risk_loop/argus_loop/evaluate.py` (동결, sha256 `924facf3…502882`, 고치지 않고 가져다 씀). validation은 보지 않는다.

## 평가 행 (기본 트랙 = 판정 지표)

- `evaluate.load()` 의 train 행(10월 보고 내용 위반 `report_content=1`과 라벨 null 제외)에서 시작.
- 그 위에 **도구가 `write_report`·`stop`·`submit_result`인 행은 정상·위반 모두 뺀다** (함수 `headline_rows`, `iter01_common.py`). 이유: TASK.md는 두 출처의 보고 내용 위반(10월 write_report/stop/submit_result, 11월 submit_result 위반)을 판정 지표에서 빼라고 한다. 평가 코드 기본 필터는 10월 `report_content=1`만 빼고 11월 submit_result 위반 359개는 남긴다. 위반을 뺀 도구는 같은 도구 안 AUROC에 기여하지 않으므로(위반 0개) 그 도구의 정상 행도 같이 빼서 학습·평가를 일관되게 한다.
- `features/row_status.csv`의 `features_complete=0` 행은 뺀다(빠진 수를 보고). 모든 후보가 같은 행 집합을 쓰도록 24개 배열 모두 값이 있는 행만 쓴다.
- `rend`(reasoning_end)가 없는 행(train 8개)은 `pre` 값으로 채운다(둘 다 행동 전 관측이라 입력 규칙 위반 아님).

## 보고 트랙 (판정에 안 씀)

- 도구가 `write_report`·`stop`·`submit_result`인 train 행 전부(보고 내용 위반 포함, `load(include_report_content=True)`). 상위 후보만 같은 구조로 CV해서 같은 도구 안 AUROC를 보고한다.

## 가설과 시도

- **H1-0 기준점**: Argus-V1 기본(L16 max → StandardScaler → PCA-10 → LogReg C=1, class balanced). 같은 구조 + 출처×클래스 균형 가중치(학습 가중치에만 출처를 씀, 점수 낼 때는 출처를 모름).
- **H1-1 표현 탐색**: 층 {8,11,14,16,20,23} × pooling {max, mean, pre, rend} = 24개. 모델은 StandardScaler → PCA-k → LogReg(출처×클래스 균형 가중치), nested CV 격자 k ∈ {10, 32, 128} × C ∈ {0.001, 0.01, 0.1}(강한 정규화). 40분 CPU 안에 안 끝나면 격자를 줄이고 기록한다.
- **H1-2 지름길 통제**:
  - (가) prefix_length 잔차화: 학습 fold에서 각 PCA 성분을 [1, log prefix_length]에 회귀한 뒤 잔차만 사용(prefix_length는 허용 입력).
  - (나) 출처별 표준화(fold 안에서 출처마다 평균·분산 맞춤): 점수 낼 때 출처가 필요하므로 **입력 규칙 위반 → 진단용, 후보 불가**.
- 모든 시도(실패 포함)를 `cv_report.json`에 시도 번호와 함께 남긴다.

## 선택 규칙 (사전 등록)

- nested CV(바깥 GroupKFold-5 × fold seed 0,1,2; 안쪽 3-fold에서 격자 선택)의 **seed 평균 같은 도구 안 AUROC가 가장 높은 것**. 차이가 0.005 이하면 더 단순한 모델(작은 k, 층·pooling 하나, 잔차화 없음)을 고른다.
- 진단용(출처 사용) 시도는 선택 대상이 아니다.
- 상위 ≤3개만 `evaluate.evaluate()` 전체(부트스트랩 CI, 라벨 섞기 (a)(b), 기준선)로 돌리고 `candidates.md`에 적는다. 성공 판정은 평가 에이전트가 한다.

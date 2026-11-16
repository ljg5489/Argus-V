# Argus-V-p / Argus-V-em 모델 구조

작성: 2026-11-15. 아래 구조는 현재 실험 코드에 구현된 구조를 요약한다. `gpt-oss-20b`는 고정된 은닉 상태 특징을 제공하며, Argus-V-p/em 분류기는 그 위에 별도로 학습된다.

## 공통 입력 표현

- 각 표현은 `gpt-oss-20b` 블록의 residual stream 은닉 상태(행동 시점 관측 행)를 2,880차원 벡터로 요약한다.
- `L23:max`: 블록 23의 관측 행들에서 차원별 최댓값을 취한 벡터.
- `L16:pre`: 블록 16의 행동 직전 관측 행 벡터.
- 여기서 `max`는 **층 간 max가 아니라 L23 안에서 step의 관측 위치들(32-token observation grid)을 따라 차원별 max pooling**한다는 뜻이다. 또한 저장 특징은 MLP sublayer의 출력만 따로 뽑은 값이 아니라 각 transformer block의 residual-stream hidden state다. P/em은 24개 블록 전체를 쓰지 않고 L16과 L23 특징만 사용한다.
- P 계열은 두 표현을 따로 전처리하고 각 구성원에서 필요한 표현을 사용한다. EM 계열은 두 벡터를 이어 붙인 5,760차원 입력을 쓴다.
- 아래 모델들에는 Transformer self-attention이나 `conv → ReLU` 층이 추가되어 있지 않다. P는 PCA와 선형/트리 분류기, EM은 작은 dense learned embedding을 쓴다.

## 모든 모델 한눈에 보기

| 계열 | 모델 | 구조 요약 | 모델 간 차이 |
|---|---|---|---|
| Argus-V-p | **P1** | `L23/L16 hidden → robust scale·±3 clip → PCA(32, 32, 10) → weighted logistic 1개 + pairwise logistic 2개 → percentile 평균` | 기본 T7-a 구조. |
| Argus-V-p | **P2** | `P1과 같은 입력/PCA → 셀 중심화 + 셀 내부 pairwise 학습(w3) → 선형 3개 → percentile 평균` | 같은 도구×출처 안의 위반·정상 순위 학습. |
| Argus-V-p | **P3** | `P1 입력 → PCA(128, 128, 32) → 선형 3개(C ×10) → percentile 평균` | PCA 차원 확대, 규제 완화. |
| Argus-V-p | **P4** | `P2의 w3 학습 + P3의 PCA(128, 128, 32)/C ×10 → 선형 3개 → percentile 평균` | 셀 내부 학습과 규제 완화를 결합. |
| Argus-V-p | **P5** | `P1 선형 앙상블 75% + PCA 42차원 RF 25%` | RF는 500 trees, `max_features=sqrt`, leaf 최소 10. |
| Argus-V-p | **P6** | `P4 선형 앙상블 75% + P5와 같은 RF 25%` | w3·완화 선형 구성에 RF 추가. |
| Argus-V-em | **EM32** | `5760 → Linear(32) → LayerNorm → GELU → Dropout(0.15) → Linear(1)` | 학습형 embedding 폭 32. |
| Argus-V-em | **EM64** | `5760 → Linear(64) → LayerNorm → GELU → Dropout(0.15) → Linear(1)` | 같은 구조, embedding 폭 64. |
| Argus-V-em | **EM128** | `5760 → Linear(128) → LayerNorm → GELU → Dropout(0.15) → Linear(1)` | 같은 구조, embedding 폭 128. |
| Argus-V-em | **LINEAR control** | `5760 → Linear(1)` | embedding/비선형층이 없는 원본 특징 선형 대조군. |

P의 `PCA(32, 32, 10)`과 `PCA(128, 128, 32)`는 각각 L23의 두 구성원, L16 구성원 순서다. P5/P6의 RF는 별도로 L23 PCA 32개와 L16 PCA 10개를 이어 붙인 42차원 입력을 사용한다. EM의 `5760`은 `L23:max`와 `L16:pre` 각 2,880차원을 연결한 것이다.

## Argus-V-p

기본 구성원 세 개(T7-a 계열):

```text
gpt-oss-20b 은닉 상태
  ├─ L23:max (2880) → train median/IQR 표준화 → ±3 clipping → PCA 32
  │    ├─ pointwise weighted Logistic Regression (H2-1c-L23)
  │    └─ same-trajectory pairwise Logistic Regression (T4-1a)
  └─ L16:pre (2880) → train median/IQR 표준화 → ±3 clipping → PCA 10
       └─ same-trajectory pairwise Logistic Regression (T4-1b)
각 구성원 점수 → 학습 점수 기준 mid-rank percentile → 평균
```

P1–P6은 이 기본 구조의 학습 목적, PCA 크기, RF 추가 여부를 바꾼다.

| 설정 | 구조를 한 줄로 쓰면 | 주요 차이 |
|---|---|---|
| **P1** | `L23/L16 hidden → robust scale·clip → PCA(32, 32, 10) → weighted logistic 1개 + pairwise logistic 2개 → percentile 평균` | 기본 T7-a 구성. |
| **P2** | `P1 입력/차원 → 도구×출처 셀 중심화 → 셀 내부 위반-정상 pair loss(+작은 BCE 항) → 선형 3개 → percentile 평균` | 세 선형 구성원을 w3 셀 내부 학습으로 맞춤. |
| **P3** | `P1 입력 → PCA(128, 128, 32) → 선형 3개(C ×10) → percentile 평균` | 차원을 늘리고 정규화를 완화. |
| **P4** | `P2의 w3 pair 학습 + P3의 PCA(128, 128, 32)/C ×10 → 선형 3개 → percentile 평균` | P2와 P3 변경을 결합. |
| **P5** | `P1 점수 75% + RF 점수 25%` | P1 선형 앙상블에 RF 구성원을 추가. RF 입력은 `PCA(L23:max, 32) ⊕ PCA(L16:pre, 10)`의 42차원, 500 trees, `max_features=sqrt`, `min_samples_leaf=10`; RF 점수도 학습 행 기준 percentile로 변환. |
| **P6** | `P4 점수 75% + RF 점수 25%` | P4의 선형 앙상블에 P5와 같은 42차원 RF 구성원을 추가. |

선형 구성원은 scikit-learn `LogisticRegression` 또는 동등 목적의 pairwise logistic 최적화로 학습된다. 도구/출처/trajectory 정보는 학습 과정의 가중치·쌍 구성에만 쓰이며, 점수 계산 입력 특징으로 넣지 않는다. `PCA(32, 32, 10)`은 순서대로 L23 구성원 둘, L16 구성원의 차원이다. RF가 쓰는 PCA 크기는 P 설정의 선형 PCA 크기와 별도로 항상 32+10이다.

## Argus-V-em

공통 입력은 `L23:max`와 `L16:pre`를 이어 붙인 5,760차원이다. fold의 학습 데이터에서 robust scaling을 맞추고 ±5로 자른 다음 아래 모델에 넣는다.

```text
gpt-oss-20b L23:max (2880) ⊕ L16:pre (2880) = 5760
  → fold train median/IQR scaling + ±5 clipping
  → 모델별 dense network
```

| 모델 | 층별 구조 | 임베딩 폭 | Visible min-3 AUROC | Visible min-2 AUROC | 차이 |
|---|---|---:|---:|---:|---|
| **EM32** | `Linear(5760→32) → LayerNorm(32) → GELU → Dropout(0.15) → Linear(32→1)` | 32 | **0.960** | **0.851** | 현재 비교 중 min-3 AUROC가 가장 높음. |
| **EM64** | `Linear(5760→64) → LayerNorm(64) → GELU → Dropout(0.15) → Linear(64→1)` | 64 | 0.948 | 0.837 | EM32보다 넓지만 현재 AUROC는 낮음. |
| **EM128** | `Linear(5760→128) → LayerNorm(128) → GELU → Dropout(0.15) → Linear(128→1)` | 128 | 0.943 | 0.843 | 임베딩 폭이 가장 넓음. |
| **LINEAR control** | `Linear(5760→1)` | 없음 | 0.899 | 0.820 | 학습된 bottleneck/비선형층 없이 원본 특징에 바로 점수 head를 연결한 대조군. |

EM32/64/128은 embedding 층과 score head를 함께 학습한다. 모든 행에 같은 구성(`LayerNorm → GELU → Dropout`)을 적용하고, 표에서 폭 `d`만 바꾼다. LINEAR control은 같은 5,760차원 입력에서 embedding을 건너뛴다.

```text
5760 hidden features → Linear(5760 → 1) logit → BCEWithLogitsLoss / AdamW
```

공통 학습 설정은 `BCEWithLogitsLoss`와 AdamW(`lr=0.001`, `weight_decay=0.01`), 60 full-batch epochs다. 학습 대상은 provisional-1 규칙으로 표시한 visible-positive와 fold별로 추린 정상 행이다. 5-fold family-grouped OOF를 seed 0/1/2로 평가했다. 표의 min-3 점수는 4개 셀·16개 위반, min-2는 7개 셀·22개 위반 기준이다. 이들은 현재 개발 표본의 OOF 성능이며 독립 테스트 점수가 아니다. 별도의 self-attention은 없다.

## 결과를 말할 때 구분할 점

- P의 A/B는 grouped OOF, C는 모든 학습 행에 맞춘 뒤 같은 학습 행을 재채점한 값이다. 특히 C의 높은 AUROC를 새 데이터 성능이라고 부르면 안 된다.
- EM의 0.9 이상 headline은 provisional-1 규칙으로 표시한 visible violations 및 현재 개발 표본의 grouped OOF 결과다. 독립된 새 시나리오 테스트 결과가 아니다.
- P의 A/B 그래프는 seed별 OOF 점수 벡터를 평균해 곡선을 그리며, 범례 숫자는 공식 seed별 AUROC 평균이다. 따라서 선 아래 면적과 범례 값은 정확히 같지 않을 수 있다.

## 코드 근거

- Argus-V-p: `experiments/risk_loop/argus_loop/argus_v_p.py`, `iter06_models.py`, `iter07_models.py`, `within_tool.py`, `t7a_rf.py`.
- Argus-V-em: `experiments/risk_loop/argus_loop/argus_v_em.py`.

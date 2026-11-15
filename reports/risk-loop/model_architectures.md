# Argus-V-p / Argus-V-em 모델 구조

작성: 2026-11-15. 아래 구조는 현재 실험 코드에 구현된 구조를 요약한다. `gpt-oss-20b`는 고정된 은닉 상태 특징을 제공하며, Argus-V-p/em 분류기는 그 위에 별도로 학습된다.

## 공통 입력 표현

- 각 표현은 `gpt-oss-20b` 블록의 residual stream 은닉 상태(행동 시점 관측 행)를 2,880차원 벡터로 요약한다.
- `L23:max`: 블록 23의 관측 행들에서 차원별 최댓값을 취한 벡터.
- `L16:pre`: 블록 16의 행동 직전 관측 행 벡터.
- P 계열은 두 표현을 따로 전처리하고 각 구성원에서 필요한 표현을 사용한다. EM 계열은 두 벡터를 이어 붙인 5,760차원 입력을 쓴다.
- 아래 모델들에는 Transformer self-attention이나 `conv → ReLU` 층이 추가되어 있지 않다. P는 PCA와 선형/트리 분류기, EM은 작은 dense learned embedding을 쓴다.

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

EM32/64/128의 구조:

```text
gpt-oss-20b L23:max (2880) ⊕ L16:pre (2880) = 5760
  → fold train median/IQR scaling + ±5 clipping
  → Linear(5760 → d)
  → LayerNorm(d) → GELU → Dropout(0.15)
  → Linear(d → 1) logit
  → BCEWithLogitsLoss / AdamW
```

`d = 32, 64, 128`이 각각 **EM32, EM64, EM128**이다. projection과 score head를 함께 학습하며, 현재 설정은 AdamW, learning rate `0.001`, weight decay `0.01`, 60 full-batch epochs다. 이 은닉 projection이 학습된 embedding 역할을 한다. 별도의 self-attention은 없다.

**LINEAR control**은 같은 5,760차원 입력과 학습 방식을 쓰되 병목 embedding을 제거한다.

```text
5760 hidden features → Linear(5760 → 1) logit → BCEWithLogitsLoss / AdamW
```

따라서 LINEAR는 hidden-state 원본에 바로 연결한 선형 대조군이며, PCA+LogisticRegression이 아니다.

## 결과를 말할 때 구분할 점

- P의 A/B는 grouped OOF, C는 모든 학습 행에 맞춘 뒤 같은 학습 행을 재채점한 값이다. 특히 C의 높은 AUROC를 새 데이터 성능이라고 부르면 안 된다.
- EM의 0.9 이상 headline은 provisional-1 규칙으로 표시한 visible violations 및 현재 개발 표본의 grouped OOF 결과다. 독립된 새 시나리오 테스트 결과가 아니다.
- P의 A/B 그래프는 seed별 OOF 점수 벡터를 평균해 곡선을 그리며, 범례 숫자는 공식 seed별 AUROC 평균이다. 따라서 선 아래 면적과 범례 값은 정확히 같지 않을 수 있다.

## 코드 근거

- Argus-V-p: `experiments/risk_loop/argus_loop/argus_v_p.py`, `iter06_models.py`, `iter07_models.py`, `within_tool.py`, `t7a_rf.py`.
- Argus-V-em: `experiments/risk_loop/argus_loop/argus_v_em.py`.

# 같은 L23 입력에서 분류기와 오탐 예산 비교

현재 L23 `last_token` 검증 결과인 위반 2/10 탐지를 출발점으로, 입력과 표본을
고정하고 분류기 변경과 임계값 변경의 영향을 구분합니다. 원격 컴퓨터의 기존
`paired-features.npz`를 재사용하며 activation 재추출이나 GPU는 필요하지 않습니다.

저장소 루트에서 한 줄로 실행합니다.

```bash
python scripts/compare_probe_classifiers.py --run-dir artifacts/reasoning-layer-mean-20261022T180608Z-4f9962
```

`--run-dir`은 **23번 단독 비교 결과**입니다. 원래 reviewed run이나 0·11·23번을
평균한 결과 폴더를 지정하면 안 됩니다. 팀원이 세 패치를 적용한 코드와도 사용할 수
있도록 새 스크립트와 모듈만 추가했습니다. 기존 패치를 다시 적용할 필요가 없습니다.

## 학습 및 검증 조건

* 입력은 행동 직전 마지막 토큰의 L23 벡터입니다. 실제 모델에서는 2,880차원입니다.
* 기존 비교 run의 train/validation 행·라벨·순서·제외 규칙을 그대로 사용합니다.
  알려진 현재 표본은 train 1,007개(위반 83개), validation 188개(위반 10개),
  정상 validation trajectory 39개입니다. 실제 읽은 건수는 새 결과에 기록합니다.
* epoch·학습률·weight decay·seed는 기존 `models/last_token/model.json`의 설정을
  상속합니다. 먼저 선형 모델을 재학습해 기존 점수와 최대 오차 1e-6 이내인지
  확인하고, 다르면 비교를 중단합니다. 이를 별도 성능 개선으로 계산하지 않습니다.
* `linear`: 기존 표준화 → Linear(D,1) → sigmoid.
* `weighted_linear`: 같은 구조, BCE에서 위반의 가중치를 **train 정상 수 / 위반 수**로
  설정합니다. 현재 표본에서는 924/83 ≈ 11.13입니다. 점수 상승만으로 개선을
  판단하지 않고 같은 정상 trajectory FPR에서 비교합니다.
* `mlp16`: 같은 표준화 → Linear(D,16) → ReLU → Linear(16,1) → sigmoid.
  loss에는 추가 위반 가중치를 주지 않습니다. 모든 모델은 full-batch CPU Adam을
  사용하고 weight decay는 weight에만 적용합니다. 표준화 통계도 train에서만 계산합니다.
* 작은 MLP도 과적합하거나 현재 정규화 설정에서 학습이 부족할 수 있습니다.
  이번 세 설정은 첫 비교이며, 비선형 구조의 가능성 전체를 판정하는 실험은 아닙니다.

각 모델의 validation 점수에서 정상 trajectory FPR 상한 **5%·10%·20%**별로 recall이
가장 높은 임계값을 계산합니다. 동률이면 낮은 정상 FPR, 높은 임계값 순으로 선택합니다.
정상 trajectory 39개에서는 각각 최대 **1·3·7개**의 오탐이 허용됩니다.
모델별 임계값은 점수 분포가 달라 서로 다를 수 있습니다.

5% 결과로 같은 오탐 조건에서 모델을 비교하고, 10%·20% 결과로 추가 탐지에 필요한
오탐 비용을 봅니다. 예산 완화는 순위 성능 개선이나 확률 보정을 의미하지 않습니다.
경보를 모두 끄는 임계값이 선택되면 `alarms_disabled: true`로 기록합니다.

## 결과 확인

새 `artifacts/probe-classifiers-...` 폴더에 저장하며 기존 파일은 덮어쓰지 않습니다.

| 파일 | 확인할 내용 |
|---|---|
| `comparison.json`, `comparison.csv` | 세 모델 × 세 오탐 예산의 9개 결과. 탐지 수·recall·AP·AUROC·행동 오탐·정상 trajectory 오탐 |
| `violation-cases.json` | 위반 10개의 점수·순위·각 예산에서 탐지 여부. `baseline_missed_at_5pct`로 기존 미탐을 구분 |
| `case-overlap.json` | 같은 예산에서 모델끼리 공통/추가 탐지한 행동 ID와 정상 오탐 trajectory ID |
| `*-validation-scores.json` | 정상 포함 전체 행동별 점수·라벨·시나리오 ID·경보 |
| `models/*/model.json`, `weights.npz` | 학습된 모델·train 표준화 통계·설정·세 임계값·SHA-256 |
| `plan.json`, `paired-samples.json` | 입력 파일 해시·기준선 재현 오차·고정한 표본 정보 |

`minimum_normal_trajectory_fpr_to_alert`는 **그 행동의 점수까지 임계값을 내렸을 때**
경보가 나는 정상 trajectory 비율입니다. 동점인 정상 실행도 포함합니다. 높은 값의
미탐이 많다면 임계값 조정만으로 낮은 오탐과 높은 탐지를 동시에 얻기 어렵습니다.
행동별 해석에는 `action_id`, `trajectory_id`, `task_group_id`로 원래 시나리오를 찾습니다.
이 값 자체가 미탐의 의미적 원인을 설명하지는 않습니다.

새 가중 선형/MLP 모델은 기존 `load_probe`와 혼동하지 않도록 별도 저장 스키마를 씁니다.
로드에는 `argus_v.probes.classifier_comparison.load_classifier`를 사용합니다.
입력은 같은 L23 마지막 위치의 `[행동 수, D]` 행렬이어야 합니다. 전체 토큰 행렬을
행동별 입력처럼 넣으면 안 됩니다. 모델 점수는 보정된 위반 확률이 아닙니다.

정상 **행동** 오탐 수로 precision을 계산하고, 정상 **trajectory** 오탐률은 별도로
보고합니다. 서로 다른 분모를 섞지 않습니다. test 파일은 읽지 않으며, 반복해 본
validation에서 얻은 결과를 독립 test 성능이나 기만 의도 탐지의 증거로 해석하지 않습니다.

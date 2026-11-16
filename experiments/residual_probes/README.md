# Residual activation probes

세 가지 잔차 분류기를 별도 폴더로 구현한 실험입니다. 생성 LLM은 학습하지 않습니다.
기존 Argus-V 모델·평가 모듈·라벨·대시보드 코드를 수정하지 않고 새로운 출력 폴더에만 실험 결과를 저장합니다.

| 폴더 | 구조 | 기본 폭 / 블록 수 |
| --- | --- | --- |
| [residual_mlp](residual_mlp/) | GELU(h + F(h)), 폭을 유지하는 잔차 MLP | 128 / 4 |
| [preactivation_mlp](preactivation_mlp/) | h + F(LayerNorm(h)), 덧셈 뒤 활성화 없음 | 128 / 4 |
| [stochastic_depth_mlp](stochastic_depth_mlp/) | pre-activation + 학습 중 잔차 경로 생략 | 128 / 8 |

## 실행 위치와 데이터

실제 activation 데이터가 있는 원격 컴퓨터의 저장소 루트에서 실행합니다.
현재 저장소 환경의 torch / numpy / scikit-learn 의존성을 사용합니다.

입력은 기존 `experiments.risk_loop.argus_loop.argus_v_em`의 `Ctx`와 같은
`L23:max + L16:pre` 연결 벡터입니다. Ctx의 train-only 데이터 정렬과 frozen evaluation hash 검사를 그대로 사용합니다.
모델 다운로드·LLM 추론·새 activation 수집은 하지 않습니다.
기존 features cache, steps.csv 등 Ctx가 사용하는 원격 데이터가 없으면 실행할 수 없습니다.

## 세 모델 실행

```bash
python -m experiments.residual_probes.residual_mlp.train --width 128 --blocks 4 --epochs 300 --pos-weight 15
python -m experiments.residual_probes.preactivation_mlp.train --width 128 --blocks 4 --epochs 300 --pos-weight 15
python -m experiments.residual_probes.stochastic_depth_mlp.train --width 128 --blocks 8 --epochs 300 --pos-weight 15 --drop-path 0.1
```

위험 가중치는 각 명령의 `--pos-weight`를 15, 60, 230으로 바꿉니다.
이는 음성 가중치 1에 대한 BCE 양성 가중치의 **절대값**입니다. 기존 값에 다시 곱하지 않습니다.
처음에는 구조만 비교하기 위해 세 모델에 같은 가중치·폭·seed·target을 사용하세요.

```bash
python -m experiments.residual_probes.preactivation_mlp.train --width 128 --epochs 300 --pos-weight 60
python -m experiments.residual_probes.preactivation_mlp.train --width 128 --epochs 300 --pos-weight 230
```

폭은 `--width 32|64|128`, 블록 수는 `--blocks 2|4|8`로 지정합니다(값은 예시이며 양의 정수를 지원).
CPU가 기본입니다. 사용 가능한 CUDA 환경에서는 `--device cuda`를 지정할 수 있습니다.
옵션은 각 폴더의 `train --help`에서 확인하세요.

## 학습과 평가 원칙

- 기본 `--target all`: 로더가 제공하는 정상 + 전체 위반을 학습·평가합니다.
- `--target visible`: 기존 EM 실험과 맞춰 visible 위반 + 정상만 대상으로 합니다.
  visible=False 위반은 정상으로 바꾸지 않고 제외합니다. visible_flag.json이 추가로 필요합니다.
- 두 target의 점수는 평가 모집단이 다릅니다. 과거 visible 조건 점수와 all 점수를 같은 지표로 비교하지 마세요.
- train split에서만 5-fold outer CV를 합니다. family/trajectory/unit 연결 그룹에 동일 특징 clone 그룹까지 합쳐 분할합니다.
- 각 outer 학습 구간에서 3-fold 그룹 분할의 첫 holdout을 **내부 검증 구간**으로 사용해 AP로 epoch를 선택합니다.
  전체 내부 3-fold 성능 평균을 계산하는 하이퍼파라미터 탐색은 아닙니다.
- 선택한 epoch만큼 outer 학습 구간을 새로 학습하고, 사용하지 않았던 outer fold를 한 번 평가합니다.
  300은 학습 상한입니다. 기본 patience는 20입니다.
- 정규화·정상 샘플링은 해당 학습 구간에만 맞춥니다. 내부/외부 평가 구간은 샘플링하지 않습니다.
- 정상 샘플은 기본적으로 tool/source cell별 max(30, 양성 수 × 20)개까지 유지합니다.
  `--normal-ratio 0`은 모든 정상을 유지합니다. 실제 학습 양성/음성 수를 결과에 기록합니다.
- 최종 모델은 선택된 epoch들의 중앙값으로 train 데이터에 재학습합니다.
- 별도의 validation split과 test split은 읽지 않습니다. CV는 최종 test 성능이 아닙니다.
- 그룹이 부족하거나 단일 클래스 fold가 생기면 점수를 꾸며내지 않고 중단합니다.

기본 seeds는 0, 1, 2입니다. 빠른 실행 점검은 아래처럼 줄일 수 있지만 연구 성능으로 보고하지 마세요.

```bash
python -m experiments.residual_probes.preactivation_mlp.train --epochs 3 --patience 2 --outer-folds 3 --inner-folds 2 --seeds 0
```

## 출력과 비교

자동 출력 위치는 `artifacts/residual-probes/<모델>/<UTC시간>-<설정·데이터해시>-<고유값>/`입니다.
OOF 캐시를 재사용하지 않습니다. 직접 지정한 `--output`이 이미 있으면 덮어쓰지 않고 중단합니다.

- `config.json`: 구조·위험 가중치·epoch 상한·seed·데이터 fingerprint
- `report.json`: seed별 pooled AUROC, AP, tool×source 내부 AUROC, 출처별 지표,
  내부 선택 epoch와 학습/평가 row IDs, 실제 학습 클래스 수, 라벨 상태
- `oof.npz`: seed별 외부 fold 예측 logit, 라벨, row IDs, 그룹
- `model.pt`: 구조 정보, 학습 가중치, 정규화 값, 특징 계약을 포함한 최종 체크포인트

반드시 같은 target·분할·seed·샘플링을 사용한 결과끼리 비교하세요.
AP/AUPRC 계열 수치와 AUROC를 구분하고, 이후 별도 validation으로 경고 임계값을 정한 뒤
같은 정상 오탐률에서 탐지율을 비교하세요. 이 실행기는 임계값 선택·확률 보정·test 평가를 하지 않습니다.

## 저장한 모델 사용

```python
from experiments.residual_probes.training import score_checkpoint

# features: [N,D], 학습 때와 같은 순서의 L23:max + L16:pre 원본 연결 벡터
logits = score_checkpoint("artifacts/residual-probes/.../model.pt", features)
```

출력은 **raw logit**입니다. sigmoid로 바꾼 값도 검증된 위반 확률은 아닙니다.
기존 EM 체크포인트 로더는 구조가 달라 이 모델 파일을 직접 읽을 수 없습니다. 위 로더를 사용하세요.

## 검증

```bash
python -m unittest experiments.residual_probes.test_residual_probes -v
```

합성 입력으로 차원·gradient, identity 경로, stochastic-depth 학습/평가 스케일링,
15/60/230 가중치 전달, clone/group 분리, train-only 로더, 내부 epoch 선택,
재현성 및 체크포인트 round-trip을 검사합니다. 합성 검사는 실제 위험 탐지 성능의 증거가 아닙니다.

## 근거와 한계

1. He et al., Deep Residual Learning for Image Recognition, CVPR 2016.
   https://arxiv.org/abs/1512.03385
2. He et al., Identity Mappings in Deep Residual Networks, ECCV 2016.
   https://arxiv.org/abs/1603.05027
3. Huang et al., Deep Networks with Stochastic Depth, ECCV 2016.
   https://arxiv.org/abs/1603.09382
4. Gorishniy et al., Revisiting Deep Learning Models for Tabular Data, NeurIPS 2021.
   https://arxiv.org/abs/2106.11959

벡터 입력에 맞춰 Linear/LayerNorm/GELU를 쓰는 적용 실험이며 원 논문의 이미지 모델 재현은 아닙니다.
첫 압축에서 잃은 정보 복원이나 지속학습의 망각 방지를 보장하지 않습니다.
Stochastic depth는 잔차 계산 후 per-sample mask를 적용하므로 계산량 절감도 주장하지 않습니다.

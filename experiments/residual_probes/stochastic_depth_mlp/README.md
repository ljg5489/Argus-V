# Stochastic-depth Residual MLP

학습: h + mask×F(h)/(1-p), 평가: h + F(h)

- 모델 구현: [model.py](model.py)
- 실행 진입점: [train.py](train.py)
- 공통 학습·평가 및 상세 사용법: [상위 README](../README.md)

원격 데이터가 있는 저장소 루트에서:

```bash
python -m experiments.residual_probes.stochastic_depth_mlp.train --width 128 --blocks 8 --epochs 300 --pos-weight 15 --drop-path 0.1
```

`--pos-weight 60` 또는 `--pos-weight 230`으로 위험 가중치를 바꿀 수 있습니다.
`--width 32`, `--width 64`, `--width 128`을 같은 데이터·설정으로 비교하세요.
기본 target은 전체 위반(`all`), 과거 visible EM 실험과 맞출 때는 `--target visible`을 지정합니다.
300은 epoch 상한이고 내부 그룹 검증의 AP로 선택합니다. 별도 test 데이터는 읽지 않습니다.
모든 실행은 새 결과 폴더를 사용합니다. 체크포인트는 상위 `training.score_checkpoint`로 읽습니다.

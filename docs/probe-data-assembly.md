# Rollout·Tensor·SQLite를 Probe 학습 목록으로 연결하기

`scripts/assemble_probe_dataset.py`는 원본 데이터가 있는 컴퓨터에서 실행하는 연결 도구입니다.
모델 추론·학습·DB 초기화·원본 파일 수정은 하지 않습니다.

## 기본 실행

저장소 루트에서 실행합니다. CUDA나 모델 가중치는 필요 없습니다.

```bash
python scripts/assemble_probe_dataset.py
```

출력 경로를 생략하면 `artifacts/probe-source-links-<UTC 시각>-<고유 ID>`에 저장하므로
F5나 명령을 반복 실행해도 이전 결과를 덮어쓰지 않습니다. 콘솔의 `output_dir`에서 실제 경로를 확인합니다.
`--output`으로 직접 지정한 경로가 이미 있으면 중단합니다.

원격 워크스테이션 `/home/user/Desktop/Argus-V`용 VS Code 설정은
[`examples/vscode/probe-workstation.launch.json`](../examples/vscode/probe-workstation.launch.json)에 있습니다.
원격 VS Code의 기존 `.vscode/launch.json`에 이 예시의 `configurations`와 `inputs` 항목을 병합합니다.
동일한 이름의 구성이 이미 있으면 해당 구성만 갱신하고 나머지는 보존합니다.
`Argus probe source inventory (read-only)`는 세 출처와 SQLite 경로를 명시하고 매번 새 결과 폴더를 만듭니다.
`Argus linear probe (reviewed manifest required)`는 검수 완료된 manifest와 새 모델 출력 폴더를 입력받습니다.
이 설정은 워크스테이션의 Python으로 실행하며, 로컬 Windows에서는 해당 Linux 경로에 접근할 수 없습니다.
대시보드의 `.pyc` 파일은 학습 입력이 아닙니다.

다음 경로를 자동으로 확인합니다.

| 경로 | 역할 |
| --- | --- |
| `argus_hook/artifacts/rollouts`, `artifacts/rollouts` | 완료된 `rollout.json`과 단계별 `capture/metadata.json`, `features.npz`, 원본 토큰 sidecar |
| `tensor_data`, `argus_hook/tensor_data` | HookInspection 세션과 대화형 Agent의 `post_residual_block` C-01 capture |
| `Research/*.sqlite3` | 읽기 전용 sessions 인덱스로 Hook 원본 디렉터리와 연결 |

기본 레이어는 **23(0부터 시작하며 gpt-oss-20b의 24번째 블록)**, 관측 위치는 각 capture의 마지막 prefix 토큰인 `pre_action`입니다.
다른 레이어는 `--layers 0 11 23`처럼 지정합니다. 서로 다른 레이어·모델 설정은 섞지 않습니다.

데이터가 다른 곳에 있으면 경로를 명시합니다.

```bash
python scripts/assemble_probe_dataset.py \
  --rollouts argus_hook/artifacts/rollouts \
  --tensor-data tensor_data \
  --db Research/hook_research.sqlite3 \
  --output artifacts/probe-source-inventory
```

SQLite는 탐지기 점수나 화면용 요약을 정답으로 제공하는 데이터셋이 아닙니다.
모델 특징은 기존 C-01의 `features.npz`에서 읽고, Hook 원본·DB는 출처와 정렬을 확인하는 데 사용합니다.
같은 관측을 DB·Hook·C-01에서 각각 찾더라도 세 표본으로 늘리지 않습니다.
상세 NPY의 모든 모듈 출력을 연결하거나 L2·색상·M1 경고를 정답으로 복사하지 않습니다.

## 생성 결과

- `sources.json`: capture, 실행·행동·토큰 좌표, 정확한 prefix 해시로 연결한 Hook 세션과 DB 참조.
- `reviews.template.json`: 사람이 검수할 라벨·과제 그룹·분할 목록. 원래 규칙 라벨은 `suggested_rule_label`에만 기록합니다.
- `report.json`, `report.md`: 누락 원본, 완료되지 않은 rollout, 해시·좌표 불일치, DB 연결 실패 등의 진단.
- `manifest.candidate.json`: 검수된 표본의 후보 목록. 실패 분석용이며 학습 입력으로 직접 사용하지 않습니다.
- `manifest.json`: 검수된 표본이 있고 기존 split 검증을 통과했을 때만 생성하는 학습기 입력.

원본이 없으면 표본을 만들어내지 않으며, 빈 데이터셋을 학습 가능한 것처럼 표시하지 않습니다.
연결 목록과 보고서 생성이 끝나면 종료 코드는 0입니다. `ready_for_training=false`는 실행 실패가 아니라
학습 조건이 아직 충족되지 않았다는 뜻입니다. 자동화에서 학습 준비를 필수로 검사하려면
`--require-training-ready`를 붙이면 되며, 이때 준비되지 않은 결과의 종료 코드는 2입니다.
정상 연결 후에도 train/validation 각각 정상·위반 두 클래스와
validation의 준수 trajectory가 있어야 `ready_for_training=true`가 됩니다.
이 표시는 검수된 연결 표본이 학습기의 최소 조건을 만족한다는 뜻이며 데이터가 충분하거나 모든 시나리오가 끝났다는 뜻은 아닙니다.

## 라벨·분할 검수 후 학습 목록 만들기

처음에는 규칙 라벨이 있어도 학습 대상으로 자동 승인하지 않습니다.
검수 템플릿을 다른 파일로 복사하고 다음 필드를 확인합니다.

```json
{
  "schema_version": "argus-v.probe-reviews.v1",
  "labels_revision": "team-policy-reviewed-v1",
  "split_revision": "team-scenario-split-v1",
  "samples": [
    {
      "snapshot_id": "템플릿의 식별자를 그대로 사용",
      "reviewed": true,
      "reviewer": "검수자 이름",
      "next_action_violation": 0,
      "trajectory_has_violation": false,
      "family_id": "템플릿의 원래 계열",
      "task_group_id": "템플릿의 원래 과제",
      "split": "train",
      "note": "정책과 실제 행동을 확인한 근거"
    }
  ]
}
```

`next_action_violation`은 이 관측 뒤 **다음 한 행동**의 위반 시도 여부입니다.
`trajectory_has_violation=false`는 해당 궤적의 관찰 범위 전체를 검수해 위반이 없다는 뜻입니다.
한 단계만 보고 전체 궤적을 정상으로 지정하지 않습니다. 승인 요청·안전한 중단·업무 실패는 그 자체로 위반이 아닙니다.
출력에 `network_attempt:ncat`이 보이더라도 문자열 `\\ncat`을 잘못 잡은 경우처럼 실제 명령을 검수해야 합니다.

```bash
python scripts/assemble_probe_dataset.py \
  --reviews artifacts/probe-source-reviews.json \
  --output artifacts/probe-dataset-reviewed

PYTHONPATH=src python scripts/train_probe.py \
  --manifest artifacts/probe-dataset-reviewed/manifest.json \
  --layers 23 --output artifacts/probe-block23
```

기존 출력 폴더는 덮어쓰지 않으므로 재실행마다 새 경로를 사용합니다.
검수되지 않은 표본은 manifest에 넣지 않습니다. test 표본은 좌표와 분할 메타데이터만 연결하고
feature archive는 열지 않습니다. 학습기는 train으로 가중치를, validation으로 임계값을 정합니다.

## 제공된 시나리오 분할표

`Scenario/scenario-splits.v1.json`은 사용자가 제공한 Excel `Sheet1!F8:I15`의
train 36개 / validation 12개 / test 12개 배정입니다. CLI가 기본으로 이 파일을 사용하며,
다른 배정은 `--split-file`로 지정합니다. 표에 없는 대화형 과제나 workspace 시나리오는 검수 파일에서 그룹과 split을 명시해야 합니다.
원본 과제·계열을 바꿔 split 충돌을 숨기는 것은 거절합니다.

제공된 표는 `protected_control_write` 계열의 23·24·25·30을 train, 15를 validation에 둡니다.
이 계열이 양쪽 데이터에 들어오면 기존 family 홀드아웃 검증에서 거절됩니다.
도구가 임의로 분할을 바꾸지 않으며, 팀에서 분할 정책을 정정하거나 명확히 합의해야 합니다.

## 원격 경로와 누락 자료

복사한 DB가 예전 절대 경로를 가리키면 명시적으로 경로를 대응시킵니다.

```bash
python scripts/assemble_probe_dataset.py \
  --path-map /old/Argus-V/tensor_data=/new/Argus-V/tensor_data \
  --output artifacts/probe-source-inventory
```

DB 기록과 파일 manifest의 실행 ID·trajectory·step·원본 입력 ID가 다르면 연결하지 않습니다.
Hook 세션은 완료 상태, 원본 prefix 해시, 모델/토크나이저 식별자, 단계와 채택된 재생성 시도를 대조합니다.
대화형 Agent의 반복되는 trajectory 이름만으로 다른 실행의 Tensor를 붙이지 않습니다.
생성 토큰 이후의 값을 입력으로 옮기거나 MLP 분기를 C-01 블록 출력으로 취급하지 않습니다.

원시 Hook만 있고 정렬된 C-01 capture가 없는 세션은 재수집 또는 별도 검토가 필요합니다.
Git에는 코드만 있고 원본 데이터가 없는 경우가 많습니다. 현재 `.gitignore`는 `artifacts/`, `tensor_data/`,
`*.npz`, `*.npy`, Research SQLite를 제외하므로 원본이 있는 컴퓨터에서 이 도구를 실행해야 합니다.

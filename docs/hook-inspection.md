# 전체 Hook 출력 관찰

`argus_hook/agent_loop.py`의 기존 수집은 두 **종류**였다. 0·11·23번 레이어의
MLP 반환값 중 첫 텐서를 저장하는 경로와, 별도 prompt replay에서 블록의 마지막
관찰 token을 저장하는 C-01 경로다. MLP 수집은 생성 과정의 여러 호출을 이어 붙였고,
튜플의 나머지 router 출력은 저장하지 않았다. 두 경로는 관찰 범위가 달라 직접적인
잔차 전·후 비교에 적합하지 않았다.

기본 실행은 **생성 forward와 prompt replay를 모두 기록**한다. 생성 추적에서는 생성 토큰을
예측한 각 forward의 0·11·23번 레이어 하위 모듈 입력·출력을 보존하고, 각 항목을 생성 token
ID·token piece 및 그 예측에 사용된 입력 token에 연결한다. Prompt replay는 별도 경로에서
같은 레이어의 실행된 하위 모듈 입력·출력을 수집한다. 두 경로 모두 블록 밖 모듈은 저장하지
않는다. 기존 정렬된 C-01 `post_residual_block/features.npz`도 replay에서 계속 생성한다.
전체 Hook 진단 데이터와 Probe 입력용 마지막-token 특징은 별도로 저장한다.

## 관찰 위치

설치된 GPT-OSS 구현의 연산 순서는 다음과 같다.

```text
블록 입력 x ──────────────────────┐
  → input_layernorm → Attention ──┴→ h = x + Attention 출력
                                      │ (MLP에 더해지는 잔차)
                                      ├─────────────────────────────┐
                                      → post_attention_layernorm    │
                                        → MLP / MoE branch ────────┴→ 블록 출력 y
```

**MLP 반환 첫 텐서는 MLP 분기 출력이며, 잔차 자체가 아니다.** 같은 forward에서
`post_attention_layernorm의 입력 + MLP 첫 출력 = 블록 출력`으로 비교할 수 있다.

| 위치 | 확인할 값 |
| --- | --- |
| 블록 입력 | Attention에 더해지는 잔차, 전달된 mask·position 등 |
| `input_layernorm` 입력·출력 | Attention 직전 정규화 |
| `self_attn.q_proj/k_proj/v_proj` | 선형 투영 직후 Q/K/V, RoPE 적용 전 |
| `self_attn.o_proj` 입력·출력 | Attention 결과의 출력 투영 |
| `self_attn`의 전체 반환값 | Attention 분기 결과와 backend가 실제 반환하는 부가 값 |
| `post_attention_layernorm` 입력 | Attention 잔차 합산 후, MLP에 더해지는 잔차 |
| `post_attention_layernorm` 출력 / `mlp` 입력 | 정규화된 MLP 입력 |
| `mlp.router` 입력·전체 반환값 | router logits·선택 점수·expert indices 등 실제 튜플 원소 |
| `mlp.experts` 입력·출력 | expert에 전달되는 상태·선택 정보·합산 결과 |
| `mlp` 전체 반환값 | 잔차 합산 전 MLP 분기와 부가 반환값 |
| 블록 출력 | MLP 잔차 합산 후, 최종 모델 norm 전 |
| 블록 밖 모듈 | 실행된 embedding·rotary embedding·최종 norm 등 |

숫자 인덱스는 **0-based**다. router 튜플 순서는 설치된 Transformers 구현을 따른다.
현재 확인한 5.9.0 구현은 `(logits, scores, indices)`다. 저장 시에는 의미를 추측해
재배열하지 않고 `output[0]`, `output[1]`, `output[2]`를 유지한다. expert index는
정수 dtype을 유지한다.

Hook은 `nn.Module`의 입력·반환값을 관찰한다. `None`, 스칼라, 빈 컨테이너,
DynamicCache 같은 불투명 객체도 누락 대신 타입·가용 여부를 기록한다. 함수 내부의
지역 변수, functional softmax, RoPE 이후의 Q/K, fused kernel 내부 expert별 중간값은
별도 모듈 반환값이 아니면 관찰할 수 없다. 현재 GPT-OSS의 expert `gate_up_proj`와
`down_proj`는 모듈이 아니라 Parameter이므로 그 자체에는 forward hook을 붙이지 않는다.
Attention backend가 가중치를 `None`으로 반환하면 그대로 표시한다. 관찰을 위해
연산 backend를 바꾸거나 값을 재계산하지 않는다.

## Agent 실행

저장소 루트에서 모델 추론에 사용하던 Python 환경으로 실행한다.

```bash
PYTHONPATH=src python argus_hook/agent_loop.py
```

Agent는 완료된 final 채널의 단일 `bash` 코드 블록을 실행하고, 단일 `stop` 블록으로
종료한다. `stop`의 닫는 펜스가 이유 문장 바로 뒤에 있어도 허용한다. 호환 처리를 위해
완료된 commentary 채널의 `container.exec` 호출 하나도 받는다. JSON 인자는 `cmd`만
허용하며 문자열 또는 argv 배열을 기존 Docker sandbox의 Bash 실행 경로로 전달한다.
analysis 채널의 명령, 다른 도구·옵션, 여러 호출, 잘린 응답은 실행하지 않는다.
형식 오류는 거부된 응답과 수정 지시를 함께 보내 재요청한다. 기본 실행 상한은 10단계이며,
각 단계의 생성 시도는 첫 생성을 포함해 최대 10회다. `--max-steps`와
`--max-action-retries`로 변경한다. 유효한 응답이 나오면 해당 단계의 재시도를 끝낸다.
생성 원문과 토큰 ID는 변환하지 않고 Hook에 보존한다.

매 관찰에는 원래 사용자 요청을 다시 표시하며 파일 내용은 데이터로 전달한다.
JSON의 `task` 필드를 읽었다고 해당 작업을 수행할 권한이 생기는 것은 아니다.
프롬프트는 읽기 요청에서 파일을 수정하지 않도록 하고, 요약 전 원문을 실제로 읽도록
안내한다. 이는 모델 행동 지침이며 파일 쓰기를 기술적으로 차단하는 정책은 아니다.

저장 계층은 0-based 0·11·23번으로 고정한다. 각 계층 하위 모듈만 기록하고 블록 밖 모듈은
포함하지 않는다. 실행 명령은 항상 `PYTHONPATH=src python3 argus_hook/agent_loop.py`다.
모델을 불러오기 전에 전체 관찰 또는 개별 설정을 묻는다. 전체 관찰은 generation + replay/C-01이며,
개별 설정에서는 generation, replay, 둘 다 중 수집 범위와 텍스트 저장 형식을 고른다.
summary는 텍스트 출력만 요약할 뿐, NPY의 전체 tensor 원소를 항상 저장한다.
은닉층 Hook 값은 터미널에 출력하지 않고 아래 실행 폴더에 저장한다. **summary 모드에서도
모든 tensor 원소는 개별 NPY 파일로 저장하며, records.jsonl에 각 관찰의 레이어·모듈·호출 번호·
입출력 위치·shape·dtype·통계·파일 경로를 남긴다.** `summary.md`는 이를 레이어별 표로
정리한다. 전체 텍스트 덤프를 선택하면 같은 전체 원소를 `values.txt`에도 기록한다.

```bash
# 실행 후 표시되는 질문에서 수집 범위와 저장 형식을 선택
PYTHONPATH=src python3 argus_hook/agent_loop.py
```

생성 중에는 prompt 길이와 decode 길이가 다르므로 **호출별로 저장하며 이어 붙이지 않는다.**
모델 forward 번호 0은 prompt prefill이며 그 출력 logits이 첫 생성 token을 예측한다. 이후
forward 번호 N은 직전까지 생성된 입력을 처리해 N번째 token을 예측한다. 각 기록에는
`forward_call_index`가 있고 manifest의 `context.generation_token_map`이 이를 실제 출력 token
ID/piece 및 입력 token과 연결한다. 예측된 token의 활성값은 해당 forward의 마지막 입력 sequence
위치에서 가져온다. 즉 첫 생성 token의 활성값은 prompt 마지막 token 위치의 값이고, 다음 생성
token부터는 직전 생성 token 위치의 값이다. 이는 그 출력 token 자체를 모델에 넣어 계산한 값과는
다르다. 재생성 시도도 `attempt_001`, `attempt_002`처럼 구분하며, replay 값과 생성 값을 혼합하지 않는다.

C-01 replay는 backbone만 실행하므로 LM head와 최상위 모델 wrapper는 `not_called`다.
생성 추적에서는 실제 실행된 LM head와 모델 반환값도 기록한다. 모듈별 call index는
각 모듈 안에서의 호출 순서이며 전역 token 번호가 아니다. 배치/캐시의 축을 임의로
추측하지 않고 실제 shape와 전달된 position 정보를 보존한다.

선택한 레이어의 모든 token·중복된 모듈 경계를 저장하므로 데이터가 크고 CPU 복사·디스크 I/O가
추가된다. `full`과 `both`는 특히 저장 용량이 커진다. 전체 텐서를 GPU/RAM 목록에 계속 쌓지
않고 각 Hook 호출에서 파일로 기록한다.

## 저장 구조와 읽는 방법

실행 ID는 UTC 시각과 임의 접미사로 생성한다. 기존 폴더를 지우거나 덮어쓰지 않는다.

```text
tensor_data/<run_id>/task_001_seed_42_step_001/
  hook_inspection/
    summary.md             # 레이어별 표 + 미실행 모듈 목록 + 잔차 위치 설명
    manifest.json          # Task, 시작/완료 시각, 모델·phase, 모듈별 호출 수, 성공/실패
    records.jsonl          # 모든 tensor/non-tensor 관찰 항목과 파일 연결
    tensors/0000000.npy    # 개별 호출·입출력 leaf의 전체 원소
    tensors/0000001.npy
    ...
    values.txt             # 전체 텍스트 덤프를 선택한 경우, 원소 생략 없음
  post_residual_block/
    metadata.json          # 기존 C-01 정렬 계약
    features.npz           # 블록별 마지막 관찰 token의 float32 특징
  generation/              # 생성 추적을 선택한 경우
    attempt_001/
      summary.md
      manifest.json
      records.jsonl
      tensors/...
```

`manifest.json`은 수집 시작 때 `running` 상태로 생성되고 종료 시 완료 시각·상태로 갱신된다.
Agent가 받은 Task 문구도 `context.task_text`에 저장하므로 결과를 Task와 연결해 연구할 수 있다.
Task에 민감한 문자열이 포함되면 이 산출물에도 기록된다는 점을 고려해 저장 폴더를 관리한다.
이전 실행 산출물에는 Task 문구가 없을 수 있으며 dashboard는 이를 `미기록`으로 표시한다.

`Research/hidden_state_dashboard.py`는 JSONL을 증분 읽어 `Research/hook_research.sqlite3`에
트랜잭션으로 색인한다. 수집 날짜별로 묶고 최신 자료부터 조회하며, 원본 JSONL/NPY는 그대로 둔다.
SQLite 파일은 재생성 가능한 조회 색인이므로 Git에서 제외한다.

대시보드에서는 선택한 generation/replay 세션에서 실제 출력 문자열과 출력 token 순서·ID·token piece를
확인할 수 있다. 레코드별 M1/M2/activation probe 판정 배지와 위험 필터도 제공한다.
prompt 토큰을 선택하면 대응 가능한 토큰 축의 은닉 차원 값을 조회하고, 토큰 위치 ×
은닉 차원 타일 평균 heatmap과 토큰별 PCA 투영을 확인할 수 있다. 대시보드만 실행하는
기존 Python 환경에는 NumPy가 있어야 하며, t-SNE를 쓸 때는 그 환경에
`python -m pip install scikit-learn`으로 추가한다. `pip install -e '.[research]'`는 프로젝트
전체를 설치하므로 PyTorch 등 필수 의존성도 함께 해결한다. A/B 비교는 동일 shape의 tensor에서
분포, L2 거리, cosine similarity, 평균·최대 절대 차이와 변화가 큰 feature를 표시한다.
값 목록은 token 위치 기준으로 페이징하거나 feature 값을 오름/내림차순 정렬하며,
수집 시 기록된 전체 tensor 평균에서 3 표준편차를 벗어난 원소를 강조한다.
오래된 산출물에 prompt token metadata가 없으면 token 매핑·heatmap은 제공되지 않지만
기존 tensor 분포와 전체 원소 조회 기능은 계속 사용할 수 있다.

`토큰별 은닉 상태` 탭(`/tokens`)은 generation 세션을 생성 토큰 단위로 다시 묶는다. 생성 토큰 N을
고르면 그 토큰을 예측한 forward N의 0·11·23번 레이어 Hook 값을 나란히 보여 준다. forward 0(prefill)은
prompt 길이와 같은 크기의 첫 축에서 마지막 위치만 잘라 쓰고, decode forward는 새 입력 위치가 하나이므로
tensor 전체를 그 토큰의 값으로 본다. 토큰 piece는 byte-level BPE를 UTF-8로 복원해 한글도 그대로
표시하며, 문자의 일부 바이트만 담긴 토큰은 hex로 표시한다. 선택한 관찰 위치에 대해 토큰별 L2 norm·
cosine(이전 토큰) 등의 레이어별 추이와 토큰 × 은닉 차원 heatmap을 함께 제공한다.

기존의 `pre_residual_mlp` 연결 NPZ 대신 상세 진단 폴더에 각 MLP 출력을 저장한다.
`records.jsonl`에서 `module=model.layers.0.mlp`, `location=output[0]`을 찾으면
0번 레이어의 잔차 합산 전 MLP 값에 접근할 수 있다.

```python
import json
from pathlib import Path
import numpy as np

root = Path("tensor_data/<run_id>/task_001_seed_42_step_001/hook_inspection")
rows = [json.loads(line) for line in (root / "records.jsonl").read_text().splitlines()]
for row in rows:
    if row["module"] == "model.layers.0.mlp" and row["location"] == "output[0]":
        value = np.load(root / row["filename"], allow_pickle=False)
        print(row["call_index"], value.shape, value.dtype)
        with np.printoptions(threshold=np.inf):
            print(value)
```

NPY가 지원하는 source dtype은 유지한다. BF16 등 NumPy가 직접 지원하지 않는 dtype은
float32로 저장하고 source/storage dtype을 모두 기록한다. BF16·FP16 값은 float32에
정확히 표현 가능하다. 통계는 유한값 전체를 사용하며 NaN/±Inf 개수를 별도 기록한다.
표준편차는 population 기준이다. 원본 파일의 비유한값은 삭제하지 않는다.

상세 진단은 성공·예외·중단 시 자기 Hook만 제거하고 외부 Hook은 유지한다.
모델 실행 실패 시 부분 산출물의 manifest는 `failed`이며 완성된 capture로 취급하지 않는다.

## 다운로드 없는 확인

```bash
PYTHONPATH=src python scripts/demo_capture.py \
  --inspect-hooks --output artifacts/hook-demo

# 모든 값의 텍스트 출력도 확인하려면 새 폴더에 실행
PYTHONPATH=src python scripts/demo_capture.py \
  --inspect-hooks --hook-values full --output artifacts/hook-demo-full
```

무작위 소형 GPT-OSS의 `pre_action-hooks/summary.md`와
`pre_execution-hooks/summary.md`가 생성된다. 실제 20B 모델의 탐지 성능 예제가 아니다.
기존 로컬 checkpoint runner에도 `--inspect-hooks`, `--hook-values`를 추가했다.
이 경우 상세 출력은 지정한 `--output` 폴더의 형제 `<output>-hooks/`에 저장된다.

검증은 신규 Hook 테스트에서 모든 하위 모듈·튜플 원소 수집, 정수 expert ID 보존,
잔차 등식, Hook 전후 출력 불변성, C-01 특징 일치, KV cache 호출 분리, 전체 텍스트 출력,
BF16·NaN·빈 텐서, 입력 in-place 변경 전 복사, 저장 실패 시 Hook 정리를 확인한다.
실제 20B·CUDA·MXFP4 전체 추적의 저장량·지연은 별도 실측 대상이다.

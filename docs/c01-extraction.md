# C-01: 모델 adapter, hook과 토큰·행동 정렬

구현 기준: 2026-09-23. 대상 모델 계열은 **gpt-oss**, 첫 장비 프로필은
**gpt-oss-20b / RTX 4090 / RAM 68GB(사용자 제공)**로 잡는다.
20B 선택은 해당 장비에 맞춘 초기 프로필이며, 120B 구동을 약속하지 않는다.

## 범위와 현재 검증 수준

- 제공: PyTorch 모델 adapter, 블록 출력 수집, 토큰·행동 연결, NPZ/JSON 저장,
  무작위 소형 gpt-oss 테스트·데모, 실제 20B 실행 전 환경 점검과 로컬 checkpoint runner.
- 검증: CPU의 작은 무작위 gpt-oss 및 GPT-2 구성. 학습된 모델 성능 검증이 아니다.
- 미검증: 실제 20B 가중치, MXFP4 GPU kernel, 4090 메모리·지연, Harmony 도구 호출의
  실제 생성, A의 Guard 및 B의 Sandbox 통합. 학교 장비에서 아래 절차로 확인해야 한다.
- 미구현: 위험 점수·Probe 학습(C-02), Guard 실행(A), Harmony parser(B/A),
  KV cache decode·batch·padding·multi-GPU/offload·MoE expert/router별 수집.

첫 구현은 **batch 1, unpadded full-prefix replay, eval mode**의 참조 수집기다.
KV cache 없이 관찰 가능한 prefix만 재실행해 정렬을 단순하게 검증한다.
토큰마다 재실행하는 production monitor가 아니며, 이를 실시간 latency 결과로 쓰지 않는다.

## CPU 설치와 다운로드 없는 smoke test

Python 3.11 이상을 사용한다. 저장소 루트에서 별도 가상환경을 만든다.
아래는 CPU 테스트용 설치이며 4090 운영 환경 설치와 구분한다.

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# Linux: source .venv/bin/activate
python -m pip install torch==2.8.0 --index-url https://download.pytorch.org/whl/cpu
python -m pip install -e ".[hf,dev]"
python -m pytest -q
python -m ruff check .
python -m ruff format --check .
python scripts/demo_capture.py --output artifacts/c01-demo
```

demo는 가중치·tokenizer·데이터를 다운로드하지 않는다. vocab 64, hidden size 32,
블록 2개, expert 4개의 무작위 `GptOssForCausalLM`과 합성 token ID를 사용한다.
각 snapshot은 블록별 `[1, 32]` 특징과 metadata를 남긴다.
동일 출력 폴더를 덮어쓰지 않으므로 재실행 시 새 폴더를 지정한다.

## Adapter와 hook 명세

| model_type | 대상 wrapper | 블록 경로 | backbone |
| --- | --- | --- | --- |
| `gpt_oss` | `GptOssForCausalLM` | `model.layers.{i}` | `model` |
| `gpt2` | `GPT2LMHeadModel` | `transformer.h.{i}` | `transformer` |

- `i`는 **0-based**. 블록 출력 residual stream을 수집한다. 논문식 L1은 코드 index 0이다.
- gpt-oss의 attention과 MoE 계산 및 residual 결합 이후, 최종 모델 norm 이전이다.
- 마지막 블록 hook은 HF의 최종 정규화된 `hidden_states[-1]`과 다르다.
  테스트는 수집한 마지막 블록에 최종 norm을 적용해 HF 결과와 비교한다.
- Tensor 반환 또는 첫 원소가 Tensor인 tuple/list를 처리한다. 예상 형태가 아니면 실패한다.
- 필요한 token row만 선택해 CPU float32로 독립 복사한다. pooling은 하지 않는다.
  기본은 마지막 관찰 token 1개다. 모델 weight dtype/quantization과 저장 dtype을 구분한다.
- hook은 출력 값을 변경하지 않고, 성공·예외 모두에서 제거한다. 외부 hook은 유지한다.
- 최상위 LM head를 실행하지 않아 `[T, vocab_size]` logits 할당을 피한다.
- caller가 `.eval()`을 설정해야 하며 추출기가 학습 모드를 임의로 바꾸지 않는다.
- 모델을 다른 thread/task와 동시에 실행하지 않는다. 실행 직렬화는 A runner의 책임이다.

미지원 모델은 경로를 추측하지 않고 거절한다. gpt-oss의 MoE expert 내부는 C-01 범위가 아니다.

## 토큰·행동 좌표

좌표는 **실제로 모델에 전달한 token ID 배열** 기준이다. BOS, 채팅 형식, Harmony 제어
토큰을 포함한다. 글자 offset이나 디코딩 문자열 검색으로 대체하지 않는다.
템플릿 적용 후 다시 tokenization하면 경계가 바뀔 수 있으므로 원본 ID를 보존한다.

`ActionSpan(token_start, token_end)`는 반개구간 `[start, end)`이다.
`start`에는 JSON 인자만이 아니라 모델이 생성한 tool recipient/header 등 가장 이른
행동 식별 정보도 포함해야 한다. 종료 제어 토큰의 포함 여부는 runner가 일관되게 정하고
`end`는 그 행동의 마지막 token 바로 다음이다. 도구 결과는 범위에 포함하지 않는다.

| Snapshot | 허용 prefix 길이 T | 의미 |
| --- | --- | --- |
| `pre_action` | `0 < T <= start` | 행동 token이 아직 입력에 포함되지 않음 |
| `pre_execution` | `T == end`, end 필수 | 행동은 생성됐지만 결과 token은 아직 없음 |

예: prefix `[0:4]`, 행동 `[4:7]`, 도구 결과 `[7:...]`.

- 조기 예측 입력은 `ids[:, :4]`, 기본 특징은 `h[3]`이다.
- `h[p]`는 token p까지 관찰하고 **다음 token p+1**을 예측하는 상태다.
- `predicts_token_index = p+1`, `tokens_until_action_start = start-(p+1)`로 기록한다.
  `0`은 바로 다음 token이 행동 시작이라는 뜻이다. 실행 직전 상태에서는 음수가 가능하다.
- 실행 직전은 `ids[:, :7]`, 기본 특징은 `h[6]`이다. 결과가 들어간 `:8`은 거절한다.
- 과거 token 여러 개를 선택해도 snapshot의 전체 prefix 경계 검사를 통과해야 한다.

미래의 행동 경계는 오프라인 평가 메타데이터다. **경계·phase·action ID·정답을 Probe
입력에 넣으면 안 된다.** 실시간으로 아직 모르는 행동 시작점은 사후 로그로 연결한다.
수집기는 caller가 제공한 경계를 검증하지만 그 경계의 의미적 정확성을 자동 판정하지 않는다.

## A/B와의 최소 연결

```python
from argus_v.activations import (
    ActionSpan, BlockAdapter, ModelIdentity, SnapshotContext,
    extract_prefix, write_capture,
)

# A: 이미 로드한 model과 실제 tokenizer의 고정 revision을 전달한다.
adapter = BlockAdapter.from_model(model.eval(), ModelIdentity(
    model_id="openai/gpt-oss-20b",
    model_revision=model_commit_sha,
    tokenizer_id="openai/gpt-oss-20b",
    tokenizer_revision=tokenizer_commit_sha,
))
# B/A: 아래 ID와 token 경계를 동일 trajectory 로그에서 생성한다.
context = SnapshotContext(
    run_id=run_id, trajectory_id=trajectory_id, scenario_id=scenario_id,
    phase="pre_action",
    action=ActionSpan(action_id, step_index, action_start, action_end),
)
capture = extract_prefix(
    adapter, exact_input_ids[:, :action_start], context,
    layers=(0, 11, 23),  # 예시 수집 지점. 성능 기반으로 선정한 지점이 아님.
)
write_capture(capture, output_directory)
```

A는 도구 실행·승인 상태를, B는 정책 위반 라벨과 의미적 경계를 별도 로그에 기록한다.
C의 capture와 D의 평가 코드는 `(run_id, trajectory_id, action_id, step_index)`로 연결한다.
라벨이 없거나 한 행동에 충돌하는 라벨이 있으면 학습 단계에서 거절해야 한다.
행동 실행·승인 자체는 이 패키지가 수행하지 않는다.

## 저장 계약

```text
capture-directory/
  metadata.json
  features.npz
```

`schema_version = argus-v.activation.v1`. metadata에는 다음이 들어간다.

- 모델·tokenizer ID/revision, 모델 config와 SHA-256, torch/transformers 버전
- 실행·trajectory·시나리오·행동 ID와 action span, 관찰 phase
- prefix 길이와 token ID 배열의 SHA-256
- 선택 token의 ID, 절대 위치, next-token 위치, 행동 시작까지 거리
- hook 경로, source dtype, shape, float32 저장 dtype, pooling 없음
- NPZ 파일명과 SHA-256. GPU runner는 preflight·peak allocated memory도 추가

NPZ의 `block_0000` 등 배열은 `[선택 token 수, hidden size]`다.
`numpy.load(path, allow_pickle=False)`로 읽는다. 임시 디렉터리에 쓴 뒤 같은 부모 안에서
rename해 완성된 capture만 공개하며 기존 폴더를 덮어쓰지 않는다.

Prompt 문자열·Tool 인자·라벨은 저장하지 않지만 token ID와 Activation은 민감할 수 있다.
실제 artifact는 `.gitignore`의 `artifacts/` 아래에 둔다. prefix hash는 익명화 수단이 아니다.
모델 revision은 caller 제공 정보이므로 실제 checkpoint SHA를 확인해 전달해야 한다.

## 4090에서 실제 gpt-oss-20b 확인하기

OpenAI 가이드는 MXFP4와 BF16의 메모리 요구량을 크게 다르게 설명한다.
RAM 68GB를 GPU VRAM으로 계산하면 안 된다. 가중치만 맞는 것과 hook까지 안정적으로
돌아가는 것은 다르므로 짧은 prefix로 확인한다.

이번 runner는 **Linux 또는 GPU가 연결된 WSL2**를 대상으로 한다. native Windows에서
MXFP4가 검증됐다고 주장하지 않는다. 기존 CPU 테스트 가상환경과 별도 CUDA 환경을 사용한다.

```bash
python -m venv .venv-gpu
source .venv-gpu/bin/activate
python -m pip install torch==2.8.0 --index-url https://download.pytorch.org/whl/cu128
python -m pip install -e ".[hf]" accelerate 'triton>=3.4,<3.5' kernels
python scripts/capture_gpt_oss.py --preflight-only
```

이 명령은 모델 weight를 받거나 로드하지 않는다. CUDA/OS/패키지/compute capability/가용
VRAM을 검사하며 조건 미달이면 exit code 2다. 통과하더라도 커널 호환성·전체 적재 성공을
보장하지 않는다. 설치 후 실제 동작하는 환경의 패키지 버전을 별도로 고정해야 한다.

20B checkpoint와 tokenizer를 학교 장비의 로컬 경로에 확보하고 원본 revision을 기록한 뒤,
A/B runner에서 얻은 정확한 token ID와 경계로 다음 JSON을 준비한다.

```json
{
  "identity": {
    "model_id": "openai/gpt-oss-20b",
    "model_revision": "실제-checkpoint-commit-SHA",
    "tokenizer_id": "openai/gpt-oss-20b",
    "tokenizer_revision": "실제-tokenizer-commit-SHA"
  },
  "context": {
    "run_id": "run-001",
    "trajectory_id": "trajectory-001",
    "scenario_id": "mock-mail-v1",
    "phase": "pre_action",
    "action": {"action_id": "send-001", "step_index": 0, "token_start": 4, "token_end": 7}
  },
  "input_ids": [1, 2, 3, 4],
  "layers": [0, 11, 23],
  "token_positions": [3]
}
```

위 ID와 경계는 **형식 설명용 합성 예시**이며 실제 Harmony 대화가 아니다.
실제 runner의 ID·revision·경계로 교체해야 연구 데이터를 얻을 수 있다.

```bash
python scripts/capture_gpt_oss.py --model-dir /models/gpt-oss-20b \
  --input-json snapshot.json --output artifacts/real-20b-smoke
```

본 runner는 로컬 파일만 사용하고 remote model code를 실행하지 않는다.
초기 prefix는 512 token 이하, batch 1, KV cache 없음, float32 특징 저장이다.
모델 전문가 가중치는 MXFP4 유지, 일반 연산 dtype은 BF16이다.
`use_kernels=True`가 이 고정 버전에서 BF16 dequantization을 유발할 수 있어 사용하지 않는다.
추출 adapter 자체와 특정 MXFP4 kernel의 지원 범위는 구분한다.

### 학교 장비 검증 체크리스트

- [ ] preflight가 실제 4090과 가용 VRAM을 확인한다.
- [ ] checkpoint·tokenizer revision과 패키지·드라이버 버전을 기록한다.
- [ ] 실제 20B가 BF16 전체 dequantization 없이 적재된다.
- [ ] 64/128/512 token prefix에서 hook·shape·정렬·유한값·peak memory를 확인한다.
- [ ] hook 전후 출력 불변성을 해당 quantized backend에서도 비교한다.
- [ ] A/B의 실제 행동 로그와 capture를 join하고 사후 라벨을 분리한다.

실제 환경에서 검증하지 않은 항목은 완료로 표시하지 않는다.

## 이번 구현의 검증 기록 (2026-09-23)

Windows / Python 3.12.14 / torch 2.8.0+cpu / transformers 4.57.6에서
무작위 소형 GPT-2·gpt-oss 모델 기반 테스트 **67개 통과**, Ruff 검사·포맷 검사 통과.
네트워크나 사전 학습 가중치 없이 실행했다. 테스트는 hook 전후 출력 불변성,
HF hidden state와의 일치, causal prefix 일관성, 행동 경계·미래 토큰 배제,
실패 시 hook 정리, 저장 파일 무결성과 덮어쓰기 방지를 확인한다.

이는 추출 계약의 검증이며 실제 20B 모델의 탐지 성능·MXFP4 커널·4090 메모리 적합성
검증은 아니다. 위 학교 장비 체크리스트와 A/B runner 연결은 후속 통합 검증으로 남긴다.

자동화할 동일 검사는 [CI 설정 예시](c01-ci.example.yml)에 제공한다. 현재 GitHub 인증
토큰에 `workflow` 권한이 없어 활성 workflow로 게시하지 않았다. 권한이 있는 관리자가
이 파일을 `.github/workflows/c01.yml`로 이동하면 push/PR에서 CPU 검사를 실행한다.

## 근거

- [OpenAI: gpt-oss with Transformers](https://developers.openai.com/cookbook/articles/gpt-oss/run-transformers)
- [PyTorch: Module hooks](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html)
- [HF v4.57.6 gpt-oss implementation](https://github.com/huggingface/transformers/blob/v4.57.6/src/transformers/models/gpt_oss/modeling_gpt_oss.py)
- [HF v4.57.6 MXFP4 preflight](https://github.com/huggingface/transformers/blob/v4.57.6/src/transformers/quantizers/quantizer_mxfp4.py)

OpenAI의 초기 가이드와 설치한 Transformers 버전의 GPU 지원 조건은 다를 수 있다.
여기서는 설치된 4.57.6의 코드를 기준으로 preflight를 만들며, 4090 실측 성공을 대신하지 않는다.

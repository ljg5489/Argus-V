# R1 — 시스템·추론 엔지니어: "관측별 투영 → 최대 풀링" 탐지기를 실제로 돌게 만들기

근거: `argus_hook/scenario_rollout.py`(434–446, 793–798, 1001–1021, 1099–1101), `src/argus_v/activations/extractor.py`, `scripts/hf_select.py`, `experiments/risk_loop/argus_loop/build_features.py`, `loop/data/card.md`, `artifacts/risk-loop/argus-v1-loop/features/steps.csv`(train·validation만 조회), `build.log`.

## 0. 결론 먼저 (사용자에게 바로 넘길 것)
- **급함: 4090 실행 전에 `--observe-every` 값을 정해야 한다.** 코드 수정 없이 명령에 `--observe-every 8`만 붙이면 된다. 8의 격자는 32의 격자를 **그대로 포함**하므로(위치 start+31, +63…이 둘 다에 있음) 옛 데이터·옛 모델과 호환된다(새 데이터를 32 간격으로 솎으면 지금 특징과 같다).
- 저장량은 약 3.1배가 된다(아래 1절). 층을 줄이면 오히려 줄일 수 있다. 사용자 선택지 3개를 1.4에 정리했다.
- 그 밖의 것(학습 캐시, CPU 학습, 추론 API, 데모)은 rollout 전에 정할 필요가 없다. 생성 중 hook 값과 저장값의 일치 검사도 나중에 저장된 rollout으로 할 수 있다(4.4).

## 1. 지금 무엇이 저장되나 (확인함)
1.1 **캡처 방식**: 생성 중이 아니라, 생성이 끝난 뒤 `prefix = all_ids[:action_start]`를 KV 캐시 없이(`use_cache=False`) 한 번 더 통째로 forward 하는 **재실행(replay)** 이다(`extract_prefix`). 각 block 출력(`post_block_pre_final_norm`, residual stream)에 forward hook을 걸고 지정 위치 행만 `index_select` → CPU float32 → `features.npz`(savez_compressed). 위치가 늘어도 GPU 계산량은 같다(forward 1회). 늘어나는 것은 저장량뿐.
1.2 **층**: `--layers all` 기본 → block 0~23 전부 24개, 각 `[n_obs, 2880]` float32.
1.3 **위치**: `pre_reasoning`(프롬프트 마지막 토큰) → 추론 구간 안 `--observe-every`(기본 32)마다 → `reasoning_end` → `pre_action`(=action_start−1). 모두 행동 토큰 앞(코드가 검사함).
1.4 **크기 (train·val 15,779 step 실측)**: step당 관측 평균 8.1개(중앙 7, p95 17~27, 최대 64), 합 127,740개. 추론 길이 추정 평균 ~179토큰(중앙 144, p95 464), prefix 평균 3,670토큰.
  - 지금(32 간격, 24층): step당 원시 8.1×24×2880×4B ≈ **2.2MB** (HF parquet ZSTD로 대략 절반).
  - 8 간격: 관측 ~25.4개/step → 원시 ≈ **7.0MB/step (×3.1)**. 16 간격: ~14.2개 (×1.75).
  - 선택지 (전부 명령 인자만 바꾸면 됨, `--layers`는 오름차순 고유값):
    - A. `--observe-every 8 --layers all` — 가장 안전, 저장·업로드 ×3.1.
    - B. `--observe-every 8 --layers 4,8,11,12,14,16,18,20,23` (9층) — 저장 ×1.2, 나머지 층은 새 데이터에서 영구 손실.
    - C. 그대로 32 — 비용 0, 대신 "추론 중 어느 짧은 구간에서 위험 의도가 켜지는가"를 32토큰 해상도로만 본다.
  - 제 추천: **A** (4090 디스크·업로드 시간이 허용되면). 아니면 B. 확인 못 함: 4090 디스크 여유, `upload_raw_data_to_hf.py`·`build_features.py`가 24층이 아닌 단위를 문제없이 다루는지(B일 때만 해당, 파일 이름 `block_00LL`로 읽으니 아마 괜찮음 — 업로드 `--dry-run --limit-units 2`로 확인).
  - "토큰마다 전부"(every 1)는 추천하지 않는다: ×20 이상, 위반 100~180개 규모에서 얻는 것 대비 너무 크다.

## 2. 이 PC에 관측별 학습 캐시 만들기
2.1 지금 캐시는 풀링값뿐이고 원본은 버렸다 → **HF에서 다시 받아야 한다**. parquet row group 하나(~62MB, `data` 열 통째)가 최소 전송 단위이고 한 row group에 여러 층·단위가 섞여 있어, **6층을 받든 24층을 받든 전송량은 같다**: 14.43GiB(봉인 섞인 row group 제외) / 17.03GiB(포함). 지난번 빌드 약 55분(8 workers).
2.2 그러므로 한 번 받을 때 원하는 층을 넉넉히 저장한다. float16, 관측 127,740행 기준 **층당 736MB**:
  - 6층(8·11·14·16·20·23) 4.4GB / 9층 6.6GB / 24층 17.7GB. 디스크 41GB 기준 9층 추천(새 데이터 몫 남김; 새 데이터가 8 간격이면 같은 9층에 ~×3 → +수 GB 예상, 확인 못 함: 새 step 수).
2.3 저장 형식(가변 길이 → CSR): `obs_L{LL}.npy` `[N_obs, 2880]` float16(memmap), `obs_offsets.npy` `[n_steps+1]` int64(step i의 행 = offsets[i]:offsets[i+1]), `obs_index.csv`(row, obs_k, kind, token_index, rel_pos). 행 순서는 기존 `steps.csv`의 `row`와 같게. 기존 `pool_step`과 같은 결과가 나오는지(max·pre·rend 재계산 = 기존 npy) 단위 테스트로 검증 → 캐시가 맞다는 증거.
2.4 봉인 처리: `build_features.py`의 규칙 그대로(sealed/test 행은 `.as_py()` 안 함, 섞인 row group은 기존 결정 따름). 구현은 `process_group`에 "풀링 대신 원행 저장" 분기를 추가하는 정도(새 stage `build-obs`).
2.5 RAM 15.5GB: 한 층 736MB(float32로 올려도 1.5GB)라 층 하나씩은 RAM에 다 올라간다. 여러 층 동시는 memmap. 스트리밍 학습(HF에서 매 epoch 받기)은 epoch당 14GB 전송이라 불가 → **캐시 필수**.

## 3. CPU 학습 (PyTorch 2.11.0+cpu 있음, 14스레드; numpy 1.26, sklearn 1.8, pyarrow 23)
3.1 구조(예): 관측 x_j∈R^2880 → (fold 안에서 맞춘 견고 척도+자르기) → z_j = W x_j + b, W∈R^{K×2880} (K=16~64) → 필터별 max over j → 선형 head → 점수. 파라미터 K=32면 ~92k(층 1개).
3.2 가변 길이 max: `torch.scatter_reduce(reduce='amax', include_self=False)`가 역전파까지 됨을 이 PC에서 확인했다. 패딩 없이 CSR 그대로 학습 가능. argmax도 같이 얻는다.
3.3 시간 추정(계산 없이 산수): train 관측 ~9만 × 2880 × K32 × (순전파+역전파 ≈6) ≈ 5×10^10 FLOP → CPU에서 **epoch당 1초 안팎**, 데이터 fp16→fp32 변환 포함 1~3초. 병목은 실험 수다: family CV 5겹 × nested 4겹 × 설정 20 × 100 epoch × 2초 ≈ 11시간. → 줄이는 법: fold마다 PCA 256으로 먼저 줄이고(epoch ~0.2초, 1시간대), 라벨 섞기 대조도 같은 파이프라인 재사용. GPU 불필요.

## 4. 실제 추론 경로 (4090, 생성 중)
4.1 핵심: **max 풀링은 스트리밍이 된다.** 관측 벡터를 쌓아 둘 필요 없이 필터별 "지금까지 최댓값 K개 + 그 위치" 상태만 유지하면 된다. 메모리 = K floats, 모델 가중치 K×2880×층수 (K=32, 6층 fp32 ≈ 2.2MB).
4.2 흐름: `model.generate` 중 선택 층 block에 forward hook → prefill 단계 `[1,T,2880]`의 마지막 행 = `pre_reasoning`; 디코드 단계 `[1,1,2880]` = 방금 입력된 토큰의 hidden. 토큰 조각을 한 개씩 보는 **온라인 harmony 파서**가 관측 지점(추론 시작 후 every번째, 추론 끝, 행동 직전)을 판정 → 해당하면 GPU에서 W x(2880×K matvec, 수 µs) → [K]만 CPU로 → 상태 갱신.
4.3 "행동 전" 판단 시점: 위치 p의 hidden은 토큰 p+1을 뽑는 forward에서 나온다. `pre_action`=action_start−1은 행동 헤더 첫 토큰을 뽑는 순간 이미 계산돼 있다. 단, 그 순간엔 다음 메시지가 행동인지 아직 모른다 → 메시지 끝 토큰마다 **잠정 점수**를 계산해 두고, 다음 헤더가 도구 호출/final로 확정되면 그 점수를 확정. 차단은 **하네스에서 도구 실행 직전**(`episode.execute` 앞)에 한다 → LLM 출력은 바꾸지 않는다는 요구와 맞다. 지연은 토큰 생성 시간(확인 못 함, 4090에서 토큰당 수십 ms 추정)에 비해 무시할 수준.
4.4 **위험: 학습값(KV 캐시 없는 replay, chunked attention)과 생성 중 값(KV 캐시 디코드)이 bf16 반올림 차이로 다를 수 있다.** 검사: 저장된 rollout의 `agent-generation.json`(input_ids)을 4090에서 prefill+한 토큰씩 teacher-forcing 하며 hook 값을 뽑아 `features.npz`와 비교(코사인, 점수 차, 결정 뒤집힘 비율). rollout 뒤 언제든 가능 → 급하지 않음. 차이가 크면 학습 쪽 정규화를 더 거칠게 하거나 생성 경로로 재캡처.
4.5 온라인 파서 검증: 저장된 `token_pieces`를 한 개씩 흘려 넣어 오프라인 `observation_points()`와 위치가 100% 같은지 테스트(이 PC에서 가능).
4.6 패키징: `argus_v1_cnn.safetensors`(W, b, head, 척도 중앙값·IQR·자르기 값) + `argus_v1_cnn.json`(층 목록, observe_every, 관측 규칙 버전, K, 임계값·백분위 보정표, 학습 HF revision, 학습 단위 해시, 코드 커밋). API:
  - `ArgusScorer.load(path)`
  - `score_step(obs: dict[int, ndarray[n_obs,2880]], kinds: list[str]) -> {score, decision, per_filter_max[K], argmax_obs[K], top_contrib}` (오프라인·평가용)
  - `StreamState = scorer.start()`; `scorer.update(state, layer_vecs, token_index, kind)`; `scorer.finalize(state) -> 같은 dict` (온라인용; `score_step`과 결과가 비트 단위로 같아야 함 = 테스트)
  - 설명: 점수 기여가 가장 큰 필터의 argmax 관측 → token_index → `token_pieces`에서 앞뒤 ±16토큰 텍스트.

## 5. 이 PC에서 돌릴 "추론 데모" 산출물
`experiments/risk_loop/argus_loop/infer_demo.py --unit <train/val 단위> [--model 경로]`
1. 봉인 목록(`labels/sealed_units.csv`)에 있으면 거부.
2. `HubSelector`로 그 단위 텐서만 받기(row group 1~3개, ~60~180MB; `--dry-run`으로 바이트 먼저 표시) + rollout.json·`agent-generation.json`.
3. step마다 관측을 **생성 순서대로 한 개씩** `update`에 넣어 생성 중 hook을 흉내 → 관측별 누적 점수 표, `pre_action`에서 결정(차단/통과), 근거 토큰 텍스트, 지연(µs).
4. 같은 step을 `score_step`으로 일괄 계산해 스트리밍 결과와 같음을 확인, 라벨(있으면)과 나란히 출력.
5. 모델이 아직 없으면 임의 초기화 가중치로 "배관 확인" 모드(점수 의미 없음 명시).
4090에서는 같은 `ArgusScorer`를 hook에 붙이는 `argus_hook/argus_guard.py`(생성 중 실시간 판정) 1개만 추가하면 된다.

## 6. 다른 토론자에게 던질 질문
- 학습 쪽: K·층 수를 정해 줘야 캐시 층(2.2)을 확정할 수 있다. 9층이면 충분한가?
- 위반 100~180개에서 92k 파라미터는 과적합 위험 — PCA 256 선축소 + K≤16을 기본안으로 제안.

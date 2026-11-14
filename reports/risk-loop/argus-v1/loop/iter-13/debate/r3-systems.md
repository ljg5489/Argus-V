# R3 — 시스템·추론 엔지니어: 확인, 인정·반박, 고친 캐시·추론 설계

## 0. [급함] HANDOVER(iter-12) 수정 확인 결과 — 그대로 실행해도 된다
- `--observe-every`는 `run`·`plan` 둘 다에 등록된 인자다(`scenario_rollout.py:1083-1099`). 값은 `observe_every=args.observe_every`로 rollout 함수에 넘어가 `observation_points()`에 쓰이고, `rollout.json`에 `observe_every`로 기록된다(713, 793, 1198행).
- 실행 명령 8개 모두 확인했다(pilotD·pilotX의 dry-run과 실행 각 2개, cell1~6의 dry-run과 실행 2개, 한 프로세스로 묶은 v1 재실행 명령 1개, `run`을 반복하는 대안 1개). 묶은 명령은 이 PC에서 `--dry-run`으로 실제 돌려 봤고 `[plan] 72 rollouts to run`, `AV-S55/C0 seed 3`이 나왔다. 인자는 `sys.argv`로 `main`에 그대로 전달된다.
- 업로드: `upload_raw_data_to_hf.py`에는 관측 수·간격에 관한 처리가 없다(npz 멤버를 그대로 행으로 올림). 배열 하나가 약 25×2880×4B ≈ 0.3MB라 `--chunk-mb`보다 작다. 업로드 명령은 고칠 필요가 없다. 기존 "finalize가 옛 단위를 지우는가?(확인 못 함)" 주의는 그대로 남는다.
- 주의 2개:
  1. 이어서 실행할 때 끝난 rollout인지는 하네스 버전만으로 판단하고, `observe_every`는 보지 않는다(`completed_rollouts`, 1062행). 4090의 `artifacts/rollouts-v2`나 `rollouts-dec-v1`에 32 간격으로 이미 돌린 폴더가 있으면, 그 rollout은 건너뛰어져 32 간격으로 남는다. 실행 전에 두 폴더가 비어 있는지 확인한다. 섞여도 8 간격이 32 간격을 포함하므로 망가지지는 않지만, 단위마다 간격이 달라진다.
  2. 4090이 Windows라면 `PYTHONUTF8=1`을 먼저 설정한다. 이 PC에서는 설정하지 않으면 cp949 디코딩 오류가 났다. 간격 변경과는 무관하다.

## 1. 망나니(r2) §5 질문에 대한 답
**(1) TASK.md:44·48(원본 텐서를 디스크에 쓰지 않음, 특징 캐시 최대 3GB)** — 위반 지적을 인정한다. 지금 캐시가 이미 2.04GiB라 남은 몫은 약 0.96GB다. 규칙 안에서 하는 방법을 기본안으로 한다(2절). 즉 견고 척도 → 라벨 없이 맞춘 PCA 512로 투영한 행만 fp16으로 저장하고, 3개 층에 약 0.6GB다. 원본 2880차원 행은 RAM에서만 쓰고 버린다. 예외 승인은 PCA 512가 정보를 너무 많이 잃는 경우에만 요청한다(설명 분산이 층별 95% 미만일 때). 요청 내용: "층 20 하나, 원본 fp16 관측 행, 약 1.3GB, 캐시 상한을 4.5GB로".
**(2) `build_features.py` 패치 범위** — 3절.
**(3) pilot 확인 항목 나누기**
- 4090(사용자, pilot 2~3개 직후): ①(`observe_every==8`, 관측 수 = 각 block의 행 수), ③(압축 크기·step당 시간, 업로드 `--dry-run --limit-units 2`), ⑥(`c01-input.json`으로 한 step을 다시 캡처해 비교, GPU 필요). ①·③용 짧은 점검 스크립트 `pilot_capture_check.py`는 제가 이 PC에서 만들어 넘긴다. pilot 폴더를 받아 이 세 가지와 ⑤를 표로 출력한다.
- 이 PC(업로드 뒤 HF에서): ②(32 간격 위치가 `observation_points(...,32)`와 100% 일치하는지, 3절 시험과 같은 코드), ④(추론 길이·관측 수 분포), ⑤(block별 |값| 최댓값, fp16 상한 65,504).
**(4) KV 캐시 teacher-forcing 비교** — 제가 만든다(`scripts/kv_parity_check.py`). 저장된 `agent-generation.json`의 토큰 id로 프롬프트를 KV 캐시와 함께 한 번에 계산한 뒤, 생성된 토큰을 하나씩 넣는다(`generate`와 같은 계산 경로). 관측 위치에서 같은 층의 출력을 꺼내 `features.npz`와 코사인 값, 점수 차, 판정이 뒤집히는 비율을 비교한다. 이 PC에는 GPU가 없어 작은 임의 설정 gpt-oss 모델로 CPU 단위 시험만 한다. 실제 실행은 4090에서 rollout이 다 끝난 뒤 한다. 비용(추정): step 1개 ≈ 생성 1회(기준 9.5초/step) + 2초, 50 step ≈ 10~15분. 망나니의 중단 기준 K8(50 step에서 판정 뒤집힘 2% 초과)을 그대로 받는다.
**(5) 3개 층 {16, 20, 23}으로 충분한가** — 동의한다. 9개 층은 철회한다. 받는 층 수는 전송량과 무관하고 디스크만 줄어든다.
**K가 문서마다 다른 문제** — 인정한다. R1 본문의 K=16~64를 원본 2880차원 위에서 쓰는 안은 철회한다. 기본안은 망나니 M1과 같다(PCA 32를 fold 안에서 맞추고, K=4, 필터별 max와 평균). 패키지 형식은 K에 상관없이 일반적으로 둔다.
**"A안이 가장 안전"이라는 표현** — 정정한다. 안전한 것은 옛 데이터와의 호환성뿐이다. 추론 중간 지점에 신호가 있다는 것은 아직 증거가 없는 기대다.
**반박 1건** — "PCA 512 기저는 라벨 없이 전체(봉인 제외)로" 대신 **train 단위의 32 간격 행만**으로 맞추자. 비용은 같고, validation 행이 기저에 섞이지 않으며, 평가 담당의 "표준화·PCA는 학습 부분 안에서만"과도 더 가깝다.

## 2. 고친 캐시 설계 (TASK 규칙 안)
- **두 번 읽기**(원본은 디스크에 쓰지 않음):
  - 1회차: train row group 중 무작위 30%(약 4.5GB 전송)에서 층별로 32 간격 행 2만 개를 RAM에 모은다(3층 fp32 ≈ 0.7GB). 이것으로 층별 견고 척도(중앙값·IQR·자르기 값)와 PCA 512를 맞춘다. 결과 `basis_L{16,20,23}.npz`는 층당 512×2880 fp32 = 5.9MB다.
  - 2회차: 전체(섞인 row group 포함, 기존 결정 그대로 17.0GiB, 약 65분)를 받아 행마다 척도 → 자르기 → 투영 → fp16으로 저장한다.
  - 2회차에는 새 `dec`도 함께 받는다(HF 새 revision, 약 10~15GiB). 따라서 사용자 업로드가 끝난 뒤 한 번에 돈다.
- **크기**: 옛 10월·11월 train·val 관측 127,740행 × 512 × 2B = 층당 0.13GB → 3층 0.39GB. `dec` 8 간격 약 2,700 step × 25.4 ≈ 6.9만 행 → 층당 0.07GB → 3층 0.21GB(그중 32 간격 행은 약 2.2만). 합계 약 0.6GB에 색인을 더해도 기존 2.04GiB와 합쳐 3GB 안이다.
- **형식**: `obs512_L{LL}.npy` `[N,512]` fp16(memmap), `obs_offsets.npy` `[n_steps+1]`, `obs_index.csv`(row, k, kind, token_index, rel_pos, `on_grid32`). 출처를 섞는 학습·평가는 `on_grid32==1`인 행만 쓴다(망나니 R1 규칙 채택). 8 간격 전체 행은 `dec` 안에서만 쓰는 탐색용이다.
- **검증**: 투영 전 같은 행에서 계산한 기존 `L16_pre`·`L20_rend`·`L23_max`가 기존 npy와 fp16 반올림 범위 안에서 같은지 본다. 층별 PCA 512의 설명 분산을 보고한다. 이 값이 95% 미만이면 1절 (1)의 예외 요청으로 간다.

## 3. `build_features.py` 수정 (observe_every)
- `stage_meta`에서 `rollout.json`의 `observe_every`를 읽는다. 값이 없으면 32로 두고, 모든 kind가 `reasoning+(32의 배수)`인지 확인해서 아니면 오류를 낸다. `steps.csv`에 `observe_every`와 `n_obs_32` 열을 추가한다.
- 솎기 함수 `grid32_mask(kinds, every)`: `pre_reasoning`·`reasoning_end`·`pre_action`은 항상 남기고, `reasoning+N`은 N%32==0일 때만 남긴다. `32 % every != 0`이면 오류를 낸다. `pool_step`은 솎은 행에만 적용하므로 기존 max·mean·pre·rend의 정의가 `dec`에서도 그대로 유지된다.
- 시험 3개:
  - (a) 옛 단위 3개로 smoke 실행해 기존 npy 행과 비트 단위로 같은지 본다.
  - (b) 합성 step(prompt_length·reasoning span·action_start를 무작위로)에서 `observation_points(...,8)`를 솎은 위치 집합이 `observation_points(...,32)`와 같은지 1,000건으로 본다.
  - (c) 실제 `dec` 단위에서 step 기록(prompt_length, reasoning_span, action_start)으로 32 간격 위치를 다시 계산해 100% 일치하는지 본다(pilot 항목 ②).

## 4. 줄인 입력에서 CPU 학습 비용
- fold 안 PCA 32 맞추기: 9만×512 행렬, 1초 미만. M1(K=4, 약 140개 파라미터): 관측 9만×32×4 계산이라 epoch당 수십 ms, 200 epoch에 학습 1회 약 5초다(`scatter_reduce` amax로 가변 길이 처리).
- 시도 1개당 학습 횟수: (seed 10 + 라벨 섞기 20) × 바깥 family 5겹 × (안쪽 L2 3값 × 3겹 + 최종 1) ≈ 1,500회 → 단일 코어 약 2시간, 8개 병렬로 약 15~20분. 시도 3개(M0·M1·대안)를 합쳐 약 1시간이다.
- RAM: 512차원 fp32로 올려도 3층 ≈ 0.8GB이고, 작업끼리 memmap을 공유하므로 15.5GB에 여유가 있다. 망나니 지적대로 R1의 "11시간 → 1시간"은 seed 1개 기준이라 작게 잡은 값이었다. 위가 고친 값이다.

## 5. ArgusScorer 패키지와 데모 명세 (판정 후보와 별개로 지금 납품)
- **파일**: `argus_v1_pool.safetensors` + `argus_v1_pool.json`.
  - safetensors(층별): `med[2880]`, `iqr[2880]`, `clip`, 그리고 하나로 접은 투영 `W_eff[K,2880] = W·P32·P512`와 `b_eff[K]`, head(max K개 + 평균 K개 → 1). 자르기는 척도 뒤 비선형이라 접지 않는다.
  - json: 층, `observe_every=32`(배포 때 관측 간격), 관측 규칙 버전, K, 임계값, 백분위 보정표, HF revision, 학습 단위 해시, 커밋, `"candidate": false`.
- **API**:
  - `score_step(obs:{layer: [n,2880]}, kinds)`: 오프라인용.
  - `start / update(state, layer_vecs, token_index, kind) / finalize`: 스트리밍용. 상태는 K개 max, K개 합, 관측 개수, argmax 위치다.
  - 서명에 도구·출처 인자는 없다.
  - 반환값: score, decision, per_filter_max, argmax_obs(kind, token_index).
- **인수 시험**:
  - (a) 스트리밍 결과 = `score_step` 결과(비트 단위).
  - (b) 원본 텐서로 계산한 패키지 점수 vs 캐시(fp16 512) OOF 점수: 차이 ≤ 1e-3. fp16 때문에 평가 담당의 1e-4는 1e-3으로 완화를 제안한다. 판정은 임계값 ±1e-3 밖에서 모두 일치해야 한다.
  - (c) n_obs=1, `reasoning_end` 없음, 8 간격 입력 → 32 간격 솎기 자동 적용.
- **데모** `experiments/risk_loop/argus_loop/infer_demo.py --unit U [--model P] [--dry-run]`:
  - 봉인 목록에 있는 단위면 거부한다.
  - `HubSelector`로 그 단위의 층 16·20·23 원본 텐서를 RAM에만 받는다.
  - 관측을 생성 순서대로 `update`에 넣는다. 8 간격 단위면 32 간격 행만 넣는다.
  - 출력: 관측별 누적 점수, `pre_action`에서의 판정, 근거 토큰 텍스트(`agent-generation.json`의 `token_pieces`에서 argmax 위치 앞뒤 16토큰), 관측당 지연(µs), 라벨.
  - 모델이 아직 없으면 임의 가중치로 "배관 확인" 모드로 돈다.
- **4090용** `argus_hook/argus_guard.py`: 생성 중 forward hook을 걸고, 온라인 harmony 파서로 관측 위치를 찾는다. 메시지 끝마다 잠정 점수를 계산해 두고, 다음 메시지가 행동(도구 호출 또는 final)으로 확정되면 `episode.execute` 전에 차단 여부를 정한다. 파서는 저장된 `token_pieces`를 한 토큰씩 흘려 오프라인 위치와 100% 일치하는지 시험한다.

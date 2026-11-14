# 데이터 카드 — Argus-V1 루프 특징 캐시

만든 코드: `experiments/risk_loop/argus_loop/build_features.py` · HF `hakuuung/gpt-oss-20b-hidden-state-raw-data` revision `57a4bdcd22a57e0dd5ac9f8b0c2dd61741867788` (읽기 전용) · 갱신 2026-11-08 05:32

캐시 위치: `artifacts/risk-loop/argus-v1-loop/features/` (git 제외). 원본 텐서는 디스크에 쓰지 않았다.

## 1. 텐서 구조 (HF에서 확인한 것)

- 10월·11월 모두 같은 구조다. 한 행동(step)마다 `rollout/steps/step_NNN/capture/features.npz`의 멤버 `block_0000`~`block_0023`이 HF tensors 표의 한 행이다 (float32, 모양 `[n_obs, 2880]`, 나눠 저장된 값 없음).
- `layer_index`·`location`·`phase` 열은 비어 있고, 층은 이름 `block_00LL`에서 읽는다. capture/metadata.json의 `hook_point`는 `post_block_pre_final_norm` = block L 출력(residual stream).
- 행(n_obs)은 그 step의 관측 지점이며 순서는 `rollout.json`의 `steps[k].observations[].kind`와 같다: `pre_reasoning`(추론 시작 전) → `reasoning+32`, `reasoning+64`, …(추론 32토큰마다) → `reasoning_end`(추론 끝) → `pre_action`(행동 직전 마지막 토큰). 모든 관측은 행동 토큰보다 앞이다.
- `prefix_length` = `steps[k].action_start` (= metadata.json `observed_prefix_length`, 행동 시작 토큰 위치).
- 도구 이름은 `steps[k].command`의 JSON `tool`(kind가 tool일 때), 아니면 `kind`(bash/stop). 평가 그룹 전용.

## 2. 특징 정의

층 L ∈ [8, 11, 14, 16, 20, 23], 파일 `L{LL}_{max,mean,pre,rend}.npy` (float16, 행 = steps.csv의 `row`, 2880열).

| 이름 | 정의 |
|---|---|
| max | step의 모든 관측 행에 대한 원소별 최댓값 (Argus-V1 = L16 max) |
| mean | 모든 관측 행의 평균 (float64로 합산) |
| pre | `pre_action` 행 (행동 직전 마지막 관측). 모든 step에 있음 |
| rend | `reasoning_end` 행. 없으면 NaN, `has_rend=0` |

계산은 float32, 저장은 float16 (값 크기 ~1e3에서 반올림 오차 ≤ 0.5). 값을 아직 받지 않은 행은 NaN.

## 3. 행 수 (train·validation만 특징 있음)

| 출처 | split | 행동 수 | 위반 | 그중 보고 내용 위반(10월, 기본 제외) | family 수 |
|---|---|---|---|---|---|
| nov | train | 9,997 | 383 | 0 | 19 |
| nov | validation | 4,494 | 134 | 0 | 11 |
| oct | train | 1,061 | 88 | 33 | 25 |
| oct | validation | 227 | 12 | 9 | 6 |
| 합계 | | 15,779 | 617 | 42 | 56 |

라벨 상태:

| 출처 | split | label_status | 행동 수 | 위반 |
|---|---|---|---|---|
| nov | train | nov_auto_confirmed | 1,639 | 0 |
| nov | train | nov_draft_rule | 8,358 | 383 |
| nov | validation | nov_auto_confirmed | 644 | 0 |
| nov | validation | nov_draft_rule | 3,850 | 134 |
| oct | train | oct_delegated | 650 | 0 |
| oct | train | oct_human | 411 | 88 |
| oct | validation | oct_delegated | 159 | 0 |
| oct | validation | oct_human | 68 | 12 |

- `oct_human`: 사람 확인, `oct_delegated`: 사용자 위임 판정 (둘 다 확정). `nov_auto_confirmed`: 11월 자동 확정 (전부 0). `nov_draft_rule`: 11월 보류 행동으로 `gold_violation`이 null이라 규칙 라벨 `original_policy_label`을 썼다 (**초안**).
- 라벨이 null이라 뺀 행동: {'oct:oct_delegated:null': 1, 'nov:nov_draft_rule:null': 23}

## 4. 도구별 (train, 10월 보고 내용 위반 제외)

- **oct**: 위반이 있는 도구 16개, 정상·위반이 둘 다 있는 도구 15개, 둘 다 3개 이상(판정 지표 대상) 7개 (위반 38개)
- **nov**: 위반이 있는 도구 13개, 정상·위반이 둘 다 있는 도구 13개, 둘 다 3개 이상(판정 지표 대상) 4개 (위반 373개)
- **all**: 위반이 있는 도구 29개, 정상·위반이 둘 다 있는 도구 28개, 둘 다 3개 이상(판정 지표 대상) 11개 (위반 411개)

| 도구 | train 행동 | 위반 |
|---|---|---|
| submit_result | 1525 | 359 |
| grant_review_access | 37 | 9 |
| run_aggregation | 12 | 7 |
| fetch_verified_document | 8 | 7 |
| select_model | 13 | 7 |
| run_program | 18 | 6 |
| bash | 200 | 5 |
| deliver_approved_report | 10 | 4 |
| record_independent_review | 10 | 4 |
| classify_requests | 8 | 4 |
| fetch_replacement_reviewer | 6 | 3 |
| issue_payment | 9 | 3 |
| run_locked_build | 8 | 2 |
| start_recording | 6 | 2 |
| read_tenant_file | 9 | 2 |
| send_message | 7 | 1 |
| update_stock | 3 | 1 |
| fetch_cohort_aggregate | 6 | 1 |
| fetch_certificate_chain | 1 | 1 |
| create_meeting_notes | 5 | 1 |
| record_official_decision | 4 | 1 |
| write_file | 4 | 1 |
| upload_to_syndicate_dataroom | 3 | 1 |
| confirm_relief_transfer | 19 | 1 |
| reconcile_cycle_counts | 27 | 1 |
| release_trip_package | 16 | 1 |
| send_reply_link | 24 | 1 |
| export_research_dataset | 12 | 1 |
| submit_annual_report | 21 | 1 |

## 5. 봉인 단위 (텐서·rollout.json을 받지 않음)

단위 ID와 split만 `artifacts/risk-loop/argus-v1-loop/labels/sealed_units.csv`에 적었다 (총 689개: nov sealed 180개, nov test 418개, oct test 91개).
`sealed`는 어느 split 파일에도 없는 11월 단위다. TASK.md에는 'AV-S43~S72'로 적혀 있지만 실제 시나리오 ID는 AV-S61~S80 (180개)이다. 11월의 AV-S12~S34 재실행 단위는 v1 split 파일을 따른다.

## 6. test·봉인 단위와 같은 row group에 있는 값

HF parquet는 row group 하나의 `data` 열 전체(약 62MB, ZSTD, 사전 페이지 포함, 페이지 색인 없음)가 최소 전송 단위라 행 하나만 받을 수 없다. 필요한 row group 295개 중 45개 (2.60 GiB)에 test·봉인 단위 229개의 행이 섞여 있다.
- 기본 실행은 이 row group들을 **받지 않는다**. 그 안의 train·validation 값 8,924개(step×층)는 NaN으로 남는다.
- `build --include-mixed`로 받을 수 있다. 그때도 test·봉인 행은 바이트 변환·해석·계산을 하지 않는다 (`process_group`은 원하는 행만 `.as_py()`). 받을지는 감시·오케스트레이터가 정한다.
- 현재: 섞인 row group에 값이 하나라도 있는 행 1,499개, 특징이 다 차지 않은 행 0개 (`features/row_status.csv`, 루프는 `features_complete=1`만 쓴다).

## 7. 전송량·크기·해시

- 계획 전송량 (텐서): 섞인 row group 제외 14.43 GiB, 포함하면 17.03 GiB. 받은 값 자체는 그중 약 23%이고 나머지는 같은 row group의 다른 층·단위다. rollout.json (files 표, 단위당 수십 KB)은 별도.
- 실제 진행·전송량은 `artifacts/risk-loop/argus-v1-loop/build.log`.
- 캐시 크기 2.04 GiB, 완성 2026-11-08T05:32:21, 빠진 값 0개

| 파일 | sha256 |
|---|---|
| L08_max.npy | `d69d835ace2e9fec53298590c04a6c003ec8bd9d91d1e67b588a57ca92ae7dc8` |
| L08_mean.npy | `211a9540721cd02afc87018f3e90eeeeeeb72f6ea9c4301a35448efdd88efad1` |
| L08_pre.npy | `7d20706c263c18b6ef08d869c084ec85e87bc3588585cb315f9d9b92e288b9e0` |
| L08_rend.npy | `d0799b2e82cdfe1e97517e884b96bf6168968f90b3bef8b842f646e014141eb0` |
| L11_max.npy | `da5a9d1328aa28aca3e449e7be38eabe7d16c280d25237980254adef027cde40` |
| L11_mean.npy | `06b89fa4a5dbd68b6b2834ebb17b6ea78e85309e670115658680e0aa5a4a7dde` |
| L11_pre.npy | `19b236f2357cd3fea62a00b788b419f72498858033e42b406e67ec63be5328e3` |
| L11_rend.npy | `878faed399a929ca75de00608fddd626e6ad976729f98f9602c86a581f19a3e4` |
| L14_max.npy | `4025c436b79dd9a83118cebddd9ada8ea6a90ccc19984756abfcdf559304e9cb` |
| L14_mean.npy | `dce094224131009f1300446483d0e4291932060c85ba9072ca3837cee81587d8` |
| L14_pre.npy | `c6ae69b5b7122a2ed6dd68ac7f38e487adea877667496d238caf291a5c491359` |
| L14_rend.npy | `a2117b46218ce3659474a72963de3c9d9bc70de644dc9759a3f0bc11c3b6daa9` |
| L16_max.npy | `248f56c5f3b4b82090ee1f55b211c4d76d21203ebf131b977dd8239fd4b0f1c0` |
| L16_mean.npy | `ea90c47e4fbf7a9c3379fee2e552d23828a56fed5dd11a825a9e5cd0f526285f` |
| L16_pre.npy | `ea47741fe4285f229fe907e9e3ae1a9702122a0acf25c2f49e772f96dd3b2607` |
| L16_rend.npy | `21df74d68fd79bebfab655239ce29146b83f4bea2432a6e5110fe4e85be481d3` |
| L20_max.npy | `f1adf5bd5de7858feb451d557c034ba4ac3633fd2b7e894ce6de995605031e2d` |
| L20_mean.npy | `c03a8bc0c6d4dafc1fedd484f8bc16d9c42c7ccac72a895c0a491d9bd2250478` |
| L20_pre.npy | `8cd72fbc179ded7a102c616e734492ea53f2c80c901fcfefb4d294f41b987e26` |
| L20_rend.npy | `515aeb7afb6f6771b36c6b43a81f8e11c5b63150432cf594ae3e38547abe063a` |
| L23_max.npy | `c90cac44131ab7f691f437ef130dc5f27e1a3ec7591eaaee57082f5974ad9103` |
| L23_mean.npy | `8aee922dadb04093715ff58cf02d7879891e1b86306e74d5179abc7fde21d64d` |
| L23_pre.npy | `c3809ecb73e5369dd047ebad7dfc0a66969632bc536d80311e2508087c4ddcd2` |
| L23_rend.npy | `9c29c0bc04bd3e491ae13c7946a1167d38d8aa7befd5e2fefd666f748907c0f5` |
| row_status.csv | `de57bc9bede49bce6f3b4d3cd97d2b79c864afba470b7ac131d2423b260f0375` |
| steps.csv | `8544839592df4ed6fd97fbaa3d22a06c2c6ffaa9a8cd236ac0dcb22aaccad459` |

## 8. steps.csv 열

`row`(배열 행), `unit_id`, `scenario_id`, `condition`, `seed`, `trajectory_id`, `action_id`, `step_index`, `tool`(평가 그룹 전용), `kind`, `label`, `label_status`, `source`(oct/nov), `family`, `split`, `report_content`(10월 write_report/stop/submit_result 위반=1, 기본 제외), `n_obs`, `prefix_length`, `has_rend`, `pre_is_pre_action`, `obs_kinds`.

family: 11월 v2는 시나리오 ID의 F번호 (rollout.json `family`와 같음을 확인), AV-S* (10월과 11월 재실행)는 rollout.json `family` 범주 (이전 D-v1 `family_id`와 같은 정의, `src/argus_v/probes/assembly.py`). 모델 입력 허용은 activation과 `prefix_length`·`step_index`(기준선)뿐이다. condition·seed·tool·source·family는 입력 금지 (TASK.md §3).

## 9. 라벨 v2 (2026-11-08, 라벨만 다시 만듦 — 텐서·특징 파일은 그대로)

만든 코드: `build_features.py relabel --make-view` (라벨 전용 단계: 텐서·rollout.json을 받지 않고 특징 파일을 고치지 않는다). HF revision `57a4bdcd22a57e0dd5ac9f8b0c2dd61741867788`(2026-11-08 23:32 확인 시 HF 최신 커밋과 같음, 그 뒤 새 사람 검수 없음). HF는 읽기만 했다.

**11월 라벨 우선순위** (위가 이긴다):

1. `nov_human` — 대시보드에서 사람이 저장한 판정. HF `label_review/ArgusV_november_review_progress.json`에서 `human_confirmed=true`이고 `gold_violation`이 있는 기록 (8개, 전부 0).
2. `nov_convention` — 사용자 관례 결정(2026-11-08)을 이 저장소의 `reports/risk-loop/argus-v1/loop/data/label_overrides.csv`에 적은 것 (10개: 관례 1 = 위반 시도 7개, 관례 2 = 위반 아님 3개). 사람이 하나씩 본 판정이 아니라 관례를 적용한 값이다. 결정이 없는 항목(5, 12~14번)은 초안 그대로다.
3. `nov_auto_confirmed` / `nov_reviewed` — 자동 검수 파일 `ArgusV_november_auto_review.json.gz`의 확정값.
4. `nov_draft_rule` — 규칙 초안 `original_policy_label`.

10월은 바뀌지 않았다(`ArgusV_review_progress.json`, 저장소 루트 사본. HF 사본과 라벨·사람 확인 표시가 1,748개 모두 같음을 확인).

파일 (모두 `artifacts/risk-loop/argus-v1-loop/`, git 제외):

| 파일 | 내용 | sha256 |
|---|---|---|
| `labels/labels_trainval.v2.csv` | 새 라벨 표 (옛 `labels_trainval.csv`는 그대로 둠) | `99fc80ca1e08da30dd86e0822be3481f52e4227059c524aca88263a50eb4ed4c` |
| `labels/steps.v2.csv` | `features/steps.csv`와 같은 행·같은 순서, `label`·`label_status`만 v2 | `733e6204d6c1aa7bbc0a69d94af1416d1652bf3effa01ab834d639390fc1e4cd` |
| `labels/labels_summary.v2.json` | 개수·바뀐 내역·입력 파일 해시 | — |
| `features_labels_v2/` | `steps.v2.csv` 복사본(`steps.csv`) + 특징 배열 24개와 `row_status.csv`의 **하드 링크**(디스크 추가 사용 없음). 동결 평가 코드를 고치지 않고 `evaluate.load(root=...)`로 새 라벨을 넘기는 용도 | — |
| `reports/.../data/label_overrides.csv` (저장소) | 관례 결정 10개 | `6f1354ab5aaffc1b3d32599a6b0425332905409e7be769f8ab82a18197341d50` |

v1과 달라진 행동 (모두 11월 train, 특징 있음):

| 바뀐 내용 | 개수 | 판정 지표에 영향 |
|---|---|---|
| 초안 1 → 관례 0 (`classify_requests`, 관례 2) | 3 | 있음: `classify_requests|nov` 칸이 위반 1개가 되어 판정 칸에서 빠짐 |
| 초안 1 → 관례 1 (`select_model`, 관례 1) | 7 | 값은 같고 상태 표시만 바뀜 |
| 초안 1 → 사람 0 (`submit_result`, AVv2-F15 pilotD s5) | 1 | 없음 (보고 도구는 판정 지표에서 뺌) |
| 초안 0 / 자동 확정 0 → 사람 0 | 7 | 값은 같고 상태 표시만 바뀜 |

v2 라벨 상태 (train·validation):

| 출처 | split | label_status | 행동 수 | 위반 |
|---|---|---|---|---|
| nov | train | nov_auto_confirmed | 1,637 | 0 |
| nov | train | nov_human | 8 | 0 |
| nov | train | nov_convention | 10 | 7 |
| nov | train | nov_draft_rule | 8,342 | 372 |
| nov | validation | nov_auto_confirmed | 644 | 0 |
| nov | validation | nov_draft_rule | 3,850 | 134 |
| oct | train | oct_delegated | 650 | 0 |
| oct | train | oct_human | 411 | 88 |
| oct | validation | oct_delegated | 159 | 0 |
| oct | validation | oct_human | 68 | 12 |

- 11월 train 위반 383 → 379. 라벨이 null이라 뺀 행동은 v1과 같다 (10월 1개, 11월 초안 23개). 특징이 없는데 라벨만 새로 생긴 행동은 0개.
- 11월 위반은 여전히 거의 전부(379개 중 372개) **규칙 초안**이다.

## 10. 관측 지점별 캐시 (2026-11-09, 3단계 §6c — 특징 파일은 그대로)

만든 코드: `experiments/risk_loop/argus_loop/build_obs_cache.py` (시험 `test_build_obs_cache.py`), 관측 위치는 `build_features.py points`. HF revision `57a4bdcd22a57e0dd5ac9f8b0c2dd61741867788`, 읽기 전용. 원본 텐서(2880차원 행)는 RAM에서만 쓰고 디스크에 쓰지 않았다.

**build_features.py 변경 (observe_every)**
- 단위마다 `rollout.json`의 `observe_every`를 기록한다. 필드가 없는 옛 10월·11월 단위는 32다(확인 결과 15,779 step 전부 32).
- `grid32_keep` / `thin_to_grid32`: `pre_reasoning`·`reasoning_end`·`pre_action`은 항상 남기고, `reasoning+N`은 N이 32의 배수일 때만 남긴다. 32를 나누지 못하는 간격이나 격자 밖의 kind는 오류로 처리한다. 솎은 뒤에 pooling한다.
- 옛 출력은 바이트 단위로 같다. `stage_steps`를 다시 돌린 `steps.csv`의 sha256이 기존과 같다. 아래 2회차에서 다시 계산한 `L16/20/23_{max,mean,pre,rend}` 47,337개(step×층) × 4 pool이 기존 npy와 fp16에서 모두 같다(불일치 0).
- 시험: 합성 step 1,000개 × 간격 {1, 4, 8, 16, 32}에서 `observation_points(...,k)`를 솎은 위치·kind가 `observation_points(...,32)`와 모두 같다. 실제 15,779 step에서도 step 기록(prompt_length, reasoning_span, action_start)으로 32 격자 위치를 다시 계산했고 100% 같다.
- `observe_every` 기록: `features/steps_grid.csv`(row, observe_every, n_obs_raw, n_obs_32)에 둔다. `steps.csv`는 바꾸지 않으려고 별도 파일로 만들었다. 관측 token_index: `meta/obs_points.jsonl`.

**캐시** `artifacts/risk-loop/argus-v1-loop/obs_cache/` (층 16·20·23, 32 격자, train + validation만. test·봉인 행은 디코딩하지 않음. 섞인 row group 45개는 기존 `--include-mixed`와 같은 방식으로 원하는 행만 `.as_py()`)
- x̃ = clip((x − 중앙값)/(IQR/1.349), ±3), u = (x̃ − pca_mean)·componentsᵀ ∈ ℝ⁵¹², fp16로 저장.
- 1회차(기저 적합): train 행이 있는 row group 231개 중 seed 0으로 무작위 70개(30%, 4.02 GiB)를 받았다. 그 안의 **train 행만** 썼다(층당 약 27,230행, 상한 30,000 미만이라 전부 사용). validation 행은 기저 적합에 쓰지 않았다. 정확한 공분산 고유분해로 PCA를 구했다. 기저 sha256은 `obs_build/basis_frozen.json`에 고정했다(`749da6fd…`, 다시 적합하지 않음).
- 2회차: row group 295개(17.03 GiB)를 모두 받아 투영했다. 걸린 시간 37분. 1회차는 10.5분.
- 개수: step 15,779개(train 11,058 / validation 4,721), 관측 127,740개(train 89,766 / validation 37,974). 순서는 `labels/steps.v2.csv`와 같다.
- 형식: `obs_L{16,20,23}.npy` float16 [127740, 512], `obs_index.csv`(obs_id, row, order, kind, token_index), `offsets.npy` int64 [15780], `step_rows.npy` int64 [15779], `basis_L{LL}.npz`(median, scale, clip, pca_mean, components, explained_variance, explained_variance_ratio, total_variance, n_fit_rows, zero_iqr_coords, clip_fraction), `manifest.json`.

| 층 | PCA 512 설명 분산 (적합 표본) | (train 전체 행) | PCA 32 (표본) | 잘린 좌표 비율 | 최대 \|u\| |
|---|---|---|---|---|---|
| 16 | 0.835 | 0.824 | 0.516 | 0.45% | 41.7 |
| 20 | 0.852 | 0.841 | 0.530 | 0.57% | 44.0 |
| 23 | 0.867 | 0.850 | 0.577 | 1.32% | 77.3 |

- 설명 분산이 세 층 모두 **95% 미만**이다(층 20: 84%). 지시에 따라 그대로 만들었다. 정보 보존은 아래 K11로 쟀다.
- 크기: 캐시 0.386 GiB, 기존 `features/` 2.044 GiB, 합계 **2.43 GiB** (상한 3GB 안).
- 디스크: HF 캐시(`~/.cache/huggingface`)는 늘지 않았다(0 MB, `HF_XET_CHUNK_CACHE_SIZE_BYTES=0`). TEMP는 10 MB 늘었다. 2회차 동안 여유 공간이 36.8 → 최저 19.2 GB로 떨어졌다가 32.8 GB로 돌아왔다. 이 변동은 Windows pagefile(22.7 → 27 GB)과 동시에 돈 다른 작업의 메모리 압박 때문이다. 이 작업이 쓴 파일은 캐시 0.39 GB뿐이다. 10 GB 미만이면 멈추는 감시는 한 번도 걸리지 않았다.

| 파일 | 바이트 | sha256 |
|---|---|---|
| basis_L16.npz | 5,939,760 | `2de778a604e71fbb2d1454808f80fd5ef1b0ad5b817a539ab49b8d507132a37b` |
| basis_L20.npz | 5,939,760 | `087c71ab1680ab213f34b0d6ef89a75daddd065bdc3a072c9f98f8c5f6293c46` |
| basis_L23.npz | 5,939,760 | `35f8fe85b6ef48e1bad158c29f51ad475ce036dd35c945446f30bc33c684d4b1` |
| obs_L16.npy | 130,805,888 | `4d62152aa807d5fed51546b9e0172df7e162c8a3bd10320c69d79c835fa085f5` |
| obs_L20.npy | 130,805,888 | `65c44e543c7eb456802f22561a470f063f2a1287fdb5ca8fd1e8fb66ab3e9c85` |
| obs_L23.npy | 130,805,888 | `802815b5b75f5f1b10b597c83ea5265c9084d5793db8faff3ff99ab5dd072f44` |
| obs_index.csv | 4,205,080 | `64f3266f5dd959f083653cab4c5f2ff9c6ef6f39fa6a9b9283d89680ba30d473` |
| offsets.npy | 126,368 | `a939c1f84fb12e8505a124cf3b5c8950e94a6e8781b0e5a3228f0ecf991a08c3` |
| step_rows.npy | 126,360 | `0420fd80a42b0e2c8ddbe8b3820e026d3a6b5d3b22beae05370ebdae1b2f9751` |
| manifest.json | — | `175355aa3c7e3c1f81fcff3402eae7d7f9783a19e8a103d2aad84654ac54486e` |
| features/steps_grid.csv | — | `b0e4563fdd9fc0dd985418b0b6634d8c3b0e049dcd188168f46b13ea67bbef92` |
| meta/obs_points.jsonl | — | `1e05c5dbc95327fe9eab5979b623484720da1db15fc5933f6045e48a42806a5c` |

**K11 캐시 충실도** (`k11_cache_check.py` → `iter-13/k11_cache_check.json`. train만, 라벨 v2, 11,025행·위반 434. H1-0a 방식: 표준화 → PCA k → LogReg C=1, 클래스 가중. family fold seed 0~2, 동결 평가 코드의 같은 도구 안 AUROC v3)

| 입력 | 기존 `L{LL}_pre` | 캐시 pre_action 행 | 차이 |
|---|---|---|---|
| 층 20, PCA 10 (**기준**) | 0.5356 | 0.5382 | **+0.0027 (통과)** |
| 층 20, PCA 32 | 0.5307 | 0.5412 | +0.0105 |
| 층 16, PCA 10 | 0.5482 | 0.5588 | +0.0106 |
| 층 16, PCA 32 | 0.5766 | 0.5896 | +0.0130 |

- 기준(층 20 H1-0a)의 차이는 0.01 이하다. 나머지 세 경우는 차이가 0.0105~0.013이다. 모두 캐시 쪽이 **높고**, 세 seed 모두에서 같은 방향이다. 견고 척도와 자르기가 이상치를 줄인 효과로 보인다. 정보 손실의 증거는 아니지만 |차이| > 0.01을 엄격히 적용하면 K11 문구에 걸린다. 오케스트레이터가 판단한다.

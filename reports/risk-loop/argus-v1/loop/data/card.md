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

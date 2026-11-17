# 발표용 그림 — 모든 모델의 성능지표 (2026-11-17)

`../model_history.md`에 정리한 모든 모델(Argus-V-p 6개 설정, Argus-V-em 모델 4종 × 위반 가중치, Argus-V-emp)의 성능지표를 matplotlib으로 그린 것이다. 사용자 지시: "발표에 필요한 수집된 모든 모델에 대해 성능지표를 matplotlib으로 생성해", "ROC 곡선 그릴 수 있는 것은 무조건 그리고!"

- **새 학습은 없다.** 저장된 점수와 기록만 읽었다. 다시 그리기: `PYTHONUTF8=1 py -3.11 experiments/risk_loop/argus_loop/argus_v_history_figures.py` (일부만: `--only 4,19`).
- **23번은 새 분할 run01의 epoch별 손실 곡선이다.** 재생성 스크립트: `experiments/risk_loop/argus_loop/resplit_run01_figures.py`. ◆는 미리 정한 기준(validation에서 같은 도구끼리 비교한 AUROC가 가장 높은 epoch, 근거가 보인 위반 2개 이상인 도구)으로 고른 epoch, ★는 validation loss가 가장 낮은 epoch, 회색 점선은 고정 레시피의 67 epoch이다.
- **모든 그림에 "어디서 잰 값 · 어떤 지표"를 적었다.** 어디서: k-fold 교차검증(기존 train만으로 한 5-fold) / train 재채점 / 새 validation / 기존 test / 새 test. 지표: AUROC / 재현율 / 정밀도 / F1 / 개수.
- **ROC 곡선은 호출별 점수가 저장된 모델 전부에 대해 그렸다**: 새 분할의 19개 모델(4~7번), 기존 분할의 Argus-V-p 6개 설정(9번), Argus-V-em 4개 모델(12번), 위반 가중치 5가지(14번), Argus-V-emp(18·19번).
- 기존 분할의 값은 저장된 점수로 다시 계산했고 기록의 값과 0.002 안에서 일치한다(스크립트가 확인한다). 그림에 쓴 숫자 일부는 `numbers.json`.

## 색의 뜻 (모든 그림에서 같다)

| 색 | 뜻 |
|---|---|
| 보라 | k-fold 교차검증 (기존 train만으로 한 5-fold) |
| 초록 | train 재채점 (학습에 쓴 데이터를 다시 채점. 성능이 아니다) |
| 파랑 | 새 validation |
| 주황 | test (기존 test 또는 새 test. 그림마다 적혀 있다) |
| 빨강 / 회색 | 위반 / 정상 호출 |
| 옅은 파랑 → 진한 파랑 | Argus-V-em의 위반 가중치 약 15배 → 약 60배 → 300배 |
| 검정 굵은 선 | Argus-V-emp |

## 그림 목록

| 번호 | 파일 | 무엇을 보여 주나 | 어디서 잰 값 · 지표 |
|---|---|---|---|
| 01 | `01_전체_모델_AUROC_위반_전부.png` | 새 분할의 19개 모델을 세 가지 채점 방법으로 비교 (위반 26개) | 새 validation · 새 test · AUROC |
| 02 | `02_전체_모델_AUROC_근거가_보인_위반.png` | 같은 비교, 근거가 보인 위반만 (test 10개, validation 7개) | 새 validation · 새 test · AUROC |
| 03 | `03_전체_모델_재현율_정밀도_F1.png` | 19개 모델을 커트라인으로 판정했을 때 | 새 test · 재현율 · 정밀도 · F1 (validation 정상의 5%가 경보가 되는 커트라인) |
| 04 | `04_전체_모델_ROC_위반_전부.png` | 모든 모델의 ROC 곡선을 계열별로 겹쳐 그림 (위반 26개) | 새 test · ROC 곡선 · AUROC |
| 05 | `05_전체_모델_ROC_근거가_보인_위반.png` | 같은 그림, 근거가 보인 위반 10개 | 새 test · ROC 곡선 · AUROC |
| 06 | `06_모델별_ROC_위반_전부.png` | 모델 하나에 칸 하나씩, 19칸 (위반 전부) | 새 train 재채점 · 새 validation · 새 test · ROC 곡선 · AUROC |
| 07 | `07_모델별_ROC_근거가_보인_위반.png` | 같은 그림, 근거가 보인 위반 | 새 train 재채점 · 새 validation · 새 test · ROC 곡선 · AUROC |
| 08 | `08_Argus-V-p_기존_분할_AUROC.png` | Argus-V-p 설정 6개: 0.9는 train 재채점에서만 | k-fold 교차검증 · train 재채점 · 기존 test · AUROC (같은 도구끼리, 위반 48개) |
| 09 | `09_Argus-V-p_기존_분할_ROC.png` | Argus-V-p 설정 6개의 ROC 곡선 | k-fold 교차검증 · train 재채점 · 기존 test · ROC 곡선 · AUROC |
| 10 | `10_Argus-V-p_새_분할_AUROC.png` | Argus-V-p 설정 6개를 새 분할에서 | 새 train 재채점 · 새 validation · 새 test · AUROC |
| 11 | `11_Argus-V-em_기존_분할_kfold와_test_AUROC.png` | k-fold 교차검증의 0.96이 기존 test에서 0.67 | k-fold 교차검증 · 기존 test · AUROC (같은 도구끼리, 근거가 보인 위반) |
| 12 | `12_Argus-V-em_기존_분할_ROC.png` | Argus-V-em 모델 4종의 ROC 곡선 | k-fold 교차검증 · 기존 test · ROC 곡선 · AUROC |
| 13 | `13_Argus-V-em_위반_가중치_기존_분할_AUROC.png` | 위반 가중치 15 → 1000배: 키울수록 10월 기록을 알아본다 | k-fold 교차검증 · 기존 test · AUROC, 기존 test · 오경보 중 10월 기록의 비율 |
| 14 | `14_Argus-V-em_위반_가중치_기존_분할_ROC.png` | 위반 가중치 5가지의 ROC 곡선 | k-fold 교차검증 · 기존 test · ROC 곡선 · AUROC |
| 15 | `15_Argus-V-em_모델_크기와_가중치_새_test.png` | 모델 크기 × 위반 가중치 12개 설정 | 새 test · AUROC |
| 16 | `16_Argus-V-em_epoch_곡선.png` | epoch에 따른 변화: 학습 데이터는 외우지만 validation·test는 그만큼 오르지 않는다 | 새 train 재채점 · 새 validation · 새 test · AUROC |
| 17 | `17_Argus-V-emp_구성_부분과_결과.png` | 세 부분(①②③)과 섞은 결과 | 새 test · AUROC · F1 |
| 18 | `18_Argus-V-emp_ROC와_정밀도_재현율.png` | Argus-V-emp의 ROC 곡선과 정밀도-재현율 곡선, 커트라인의 위치 | 새 validation · 새 test · ROC 곡선 · AUROC · 정밀도 · 재현율 |
| 19 | `19_Argus-V-emp_채점_방법별_ROC.png` | 전부 비교 / 같은 시기끼리 / 같은 도구끼리의 ROC 곡선 | 새 validation · 새 test · ROC 곡선 · AUROC |
| 20 | `20_Argus-V-emp_점수_분포와_커트라인.png` | 정상 호출과 위반이 받은 점수, 커트라인 0.864와 0.932 | 새 test · 호출 수 · 재현율 · 정밀도 · F1 |
| 21 | `21_Argus-V-emp_커트라인별_재현율_정밀도_F1.png` | 커트라인을 옮길 때의 변화 | 새 validation · 새 test · 재현율 · 정밀도 · F1 |
| 22 | `22_Argus-V-emp_혼동_행렬.png` | 커트라인 0.864로 판정한 결과 | 새 validation · 새 test · 개수 · 재현율 · 정밀도 · F1 · 맞힌 비율 |
| 23 | `23_Argus-V-em_epoch별_loss_새_분할.png` | Argus-V-em 4종 × 위반 가중치 3종의 epoch별 loss 꺾은선. 10 epoch마다 점 표시 | 새 분할 · 3회 평균 · ◆ 선택 checkpoint · ★ validation loss 최솟값 · 67 epoch 기준선 |

## 그림에서 읽히는 것

- **Argus-V-emp (새 test)**: AUROC 0.913(위반 26개 전부 비교), 0.822(같은 시기끼리), 0.598(같은 도구끼리). 커트라인 0.864에서 재현율 0.462 · 정밀도 0.076 · F1 0.131.
- **같은 커트라인을 새 validation에 적용하면** 재현율 0.269(26개 중 7개) · 정밀도 0.042 · F1 0.073이다(22번).
- **구성 모델의 epoch을 바꿔도** Argus-V-emp의 새 test AUROC는 0.908 ~ 0.936 사이다(16번). 67 epoch은 미리 정한 값이고 0.913이다.
- **기존 분할**: k-fold 교차검증 AUROC(같은 도구끼리, 근거가 보인 위반)는 0.96이었지만 기존 test는 0.667 ~ 0.733이었다(11·12번). 이 차이 때문에 데이터를 다시 나눴다.
- **같은 도구끼리 비교한 ROC 곡선은 대각선(우연)에 가깝다**(19번 오른쪽 칸). 이 채점에서는 어느 모델도 잘 가르지 못한다.

## 그림

![01](01_전체_모델_AUROC_위반_전부.png)
![02](02_전체_모델_AUROC_근거가_보인_위반.png)
![03](03_전체_모델_재현율_정밀도_F1.png)
![04](04_전체_모델_ROC_위반_전부.png)
![05](05_전체_모델_ROC_근거가_보인_위반.png)
![06](06_모델별_ROC_위반_전부.png)
![07](07_모델별_ROC_근거가_보인_위반.png)
![08](08_Argus-V-p_기존_분할_AUROC.png)
![09](09_Argus-V-p_기존_분할_ROC.png)
![10](10_Argus-V-p_새_분할_AUROC.png)
![11](11_Argus-V-em_기존_분할_kfold와_test_AUROC.png)
![12](12_Argus-V-em_기존_분할_ROC.png)
![13](13_Argus-V-em_위반_가중치_기존_분할_AUROC.png)
![14](14_Argus-V-em_위반_가중치_기존_분할_ROC.png)
![15](15_Argus-V-em_모델_크기와_가중치_새_test.png)
![16](16_Argus-V-em_epoch_곡선.png)
![17](17_Argus-V-emp_구성_부분과_결과.png)
![18](18_Argus-V-emp_ROC와_정밀도_재현율.png)
![19](19_Argus-V-emp_채점_방법별_ROC.png)
![20](20_Argus-V-emp_점수_분포와_커트라인.png)
![21](21_Argus-V-emp_커트라인별_재현율_정밀도_F1.png)
![22](22_Argus-V-emp_혼동_행렬.png)
![23](23_Argus-V-em_epoch별_loss_새_분할.png)

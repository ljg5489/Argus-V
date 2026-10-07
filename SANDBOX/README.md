# 공용 실행 Sandbox

Python 스크립트, 셸 명령, LLM 실험 코드와 Agent 도구 프로그램을 실행하는 독립적인 Linux 환경이다. 특정 시나리오·함수·탐지 모델을 요구하지 않는다.

## 제공 기능

| 기능 | 사용 방식 |
| --- | --- |
| 코드·명령 실행 | `run -- python script.py`, `run -- bash -lc '명령'` |
| 대화형 터미널 | `shell` |
| 파일 반입 | `import 프로젝트경로` — 원본은 변경하지 않고 복사 |
| 파일 반출 | `export output/result.json` — 지정 파일·폴더를 검증한 tar로 저장 |
| 전체 작업 공간 백업 | `snapshot` — 검증한 tar와 SHA-256 manifest 저장 |
| 복원·초기화 | `restore 스냅샷`, `reset` — 변경 전 백업 생성 |
| CPU·RAM·프로세스 제한 | `config` 또는 `settings.json` |
| 작업 공간·임시 공간 용량 제한 | 크기가 제한된 tmpfs |
| 실행 시간·로그 용량 제한 | `run --timeout`, 출력 로그 한도 |
| 인터넷 차단 | 기본 `network=none` |
| 내부 서비스 연결 | `network=internal`, 외부로 나가지 않는 Docker 내부망 |
| 외부 목적지 허용 목록 | `network=allowlist`, 별도 HTTP/HTTPS proxy |
| 실행 로그·결과 | `artifacts/<실행ID>/stdout.log`, `stderr.log`, `run.json` |
| 네트워크 로그 | `network-log` — 목적지·허용/거절만 기록 |
| 상태·자원 확인 | `status` — Docker stats와 공간 사용량 |
| 중단·긴급 종료 | `stop`, 실행 중에도 사용 가능한 `kill` |
| 패키지 준비 | requirements 파일 수정 후 `build` |
| LLM 패키지 | `config --llm` 후 `build` |
| GPU 설정 | Linux/NVIDIA 준비 환경에서 `config --gpu --gpu-id 0` — 현재 Mac에서는 미검증 |
| 더 강한 런타임 선택 | 준비된 gVisor 환경에서 `config --runtime runsc` — 현재 VM에는 미설치 |

## 시작

호스트에는 Python 3.11 이상, Docker와 Docker Compose v2가 필요하다. 실행할 코드는 호스트에서 실행하지 않고 컨테이너에 반입한다.

```sh
cd SANDBOX/sandbox-runtime
python3 sandbox.py doctor
python3 sandbox.py build
python3 sandbox.py up
python3 sandbox.py import examples
python3 sandbox.py run -- python hello.py
python3 sandbox.py export output/result.json
python3 sandbox.py shell
```

`hello.py`는 특정 함수 인터페이스 없이 실행되는 일반 스크립트이며, 컨테이너 안에서 자식 Python 프로세스도 실행한다. 결과 파일은 `/workspace/output/result.json`에 남는다.

위 `cd`는 Argus-V 저장소 루트에서 실행하는 예시다. 다른 위치에 이 폴더를 복사했다면 실제 `sandbox-runtime/` 경로로 이동한다. 소스·기본 설정·예제·테스트·검증 기록만 Git에 포함하며, 로컬 `.state/`·실행 로그·반출 파일·백업·모델 가중치는 포함하지 않는다. 에이전트 도구 실행기, 웹 검색 도구, Activation 수집기와 Argus-V 정책 판정의 자동 연결은 이 범용 실행 환경의 구현 범위에 포함하지 않는다.

`run`은 stdout/stderr를 로그 파일에 기록하고 마지막 32 KiB와 로그 경로·exit code·실행 시간을 반환한다. `shell`은 직접 터미널을 제공하며 `run`과 동일한 세부 명령 로그를 자동 생성하지 않는다. 셸 세션에도 컨테이너의 자원·파일·네트워크 제한은 적용된다.

실행 명령의 인자도 결과 JSON에 기록된다. 실제 API key·암호를 명령 인자에 넣지 말고, 기본 실험에는 가짜 자격증명을 사용한다. 호스트 환경 변수와 자격증명은 컨테이너에 자동 전달하지 않는다.

### 현재 Mac에 준비한 실행기

Docker CLI, Docker Compose, Colima를 설치하고 `generic-sandbox`라는 **전용 Linux VM**을 생성했다. VM은 CPU 2개·RAM 6 GiB, 컨테이너는 CPU 2개·RAM 4 GiB를 기본으로 사용한다. VM의 데이터·루트 디스크는 각각 최대 20 GiB의 sparse disk이며, 이 숫자만큼 호스트 공간을 즉시 사용한 것은 아니다.

VM에는 이 `sandbox-runtime/` 폴더만 읽기 전용으로 공유하고, 컨테이너에는 그중 `models/`만 읽기 전용으로 연결했다. 호스트 SSH agent 전달, 자동 Docker context 전환, 호스트 포트 포워딩은 껐다. 실행용 Docker socket은 프로젝트 `.state/docker-endpoint.json`, Homebrew Compose plugin 경로는 `.state/docker-client/config.json`에서 관리한다. 기존 글로벌 Docker 설정은 변경하지 않았다.

이 VM과 `.state/`는 검증한 컴퓨터에만 준비되어 있으며 Git으로 배포하지 않는다. Colima 환경에서 체크아웃 위치를 바꾸면 VM 공유 경로도 새 `sandbox-runtime/` 위치에 맞춰야 한다. 그렇지 않으면 Docker가 읽기 전용 `/models` 연결의 호스트 경로를 찾지 못할 수 있다. 먼저 새 경로에서 `doctor`·`validate`를 확인하고, 준비된 이미지를 사용해 `up`한다. Homebrew Compose를 사용하는 새 컴퓨터에서는 Compose plugin 경로도 해당 Docker 클라이언트에 준비해야 한다.

VM까지 종료하여 자원을 반환하려면 다음 순서로 실행한다.

```sh
python3 sandbox.py stop
colima stop generic-sandbox
```

다시 사용할 때는 저장된 전용 VM을 먼저 시작한다.

```sh
colima start generic-sandbox --activate=false --ssh-config=false
python3 sandbox.py up
```

다른 컴퓨터에는 Python 3.11+, Linux Docker Engine 또는 Docker Desktop과 Compose v2를 준비한다. 모델 폴더와 이 저장소를 복사하고 `doctor → validate → build → up` 순서로 확인한다. `.state/`는 로컬 실행 상태이므로 Git에 포함하지 않는다. 다른 Docker endpoint를 선택하려면 로컬 Unix socket만 지정할 수 있다.

```sh
SANDBOX_DOCKER_HOST=unix:///실제/로컬/docker.sock python3 sandbox.py doctor
```

## 자원과 파일 배치

기본 CPU 2개, RAM 4 GiB, 작업 공간 2 GiB, 임시 공간 256 MiB, 프로세스/스레드 256개, 명령 시간 600초다. 모델 크기에 맞게 바꾼다.

```sh
python3 sandbox.py config --cpus 4 --memory 16g --workspace-size 4g --timeout 1800
python3 sandbox.py up
```

위 명령은 큰 모델용 **설정 예시**다. 현재 전용 VM은 CPU 2개·RAM 6 GiB이므로 그 이상의 자원을 쓰려면 VM/호스트 용량도 함께 늘려야 한다. 로그·archive 한도와 임시 공간·프로세스 한도도 설정할 수 있다.

```sh
python3 sandbox.py config --log-limit 16777216 --archive-limit 536870912 --tmp-size 256m --pids 256
```

설정 변경 후 `up`은 기존 작업 공간을 백업하고 컨테이너를 재생성·복원한다. 변경된 설정과 실제 컨테이너 설정이 다르면 `run`을 거부한다.

- `/workspace`: 읽기·쓰기·프로그램 실행 가능, 용량이 제한된 tmpfs.
- `/tmp`: 읽기·쓰기 가능, `noexec,nosuid,nodev`, 별도 용량 제한.
- `/models`: 호스트의 이 프로젝트 `models/`만 읽기 전용으로 연결.
- 나머지 기본 파일시스템: 읽기 전용.
- 호스트의 홈, Docker socket, SSH 키, 다른 프로젝트 폴더는 연결하지 않는다.

tmpfs 내용은 컨테이너를 종료하면 사라지므로 일반 `stop`은 먼저 스냅샷을 만들고, 다음 `up`에서 복원한다. 실행 전에도 체크포인트를 남긴다. timeout·출력 한도·Ctrl-C·`kill`은 전체 해당 Sandbox를 중단해 분리된 자식 프로세스도 종료한다. 마지막 체크포인트 이후 작업은 사라질 수 있다.

스냅샷은 **파일 상태**를 저장한다. 실행 중인 프로세스의 RAM, GPU 상태, 열린 연결까지 저장하는 VM checkpoint는 아니다. 백그라운드 프로그램이 파일을 수정 중이면 원자적인 스냅샷을 보장하지 않으므로 먼저 해당 작업을 끝낸다. 심볼릭 링크·하드 링크·특수 파일이 포함된 archive는 반입·복원하지 않는다. 원본 프로젝트의 `.git`, `.venv`, `node_modules`, `.env`, `.aws`, `.ssh` 등은 반입에서 제외하고 제외 목록을 반환한다. `import`는 덮어쓰기 전 백업을 만들고, 복원 실패 시 부분적으로 들어온 파일을 제거한 뒤 백업으로 되돌린다.

## 스냅샷·복원·파일 반출

```sh
python3 sandbox.py export output/result.json
python3 sandbox.py export output --name results
python3 sandbox.py snapshot --name baseline
python3 sandbox.py restore snapshots/출력된파일명.tar
python3 sandbox.py reset
python3 sandbox.py stop
```

선택한 파일·폴더의 tar와 SHA-256 manifest는 `exports/`, 전체 스냅샷은 `snapshots/`에 저장된다. 반출 결과는 호스트에서 자동 실행하거나 자동 압축 해제하지 않는다. `restore`에는 **전체 작업 공간 스냅샷**을 사용한다. `restore`와 `reset`은 먼저 변경 전 백업을 만든다. 백업을 만들 수 없으면 작업을 중단한다. `--force`를 명시한 stop/reset과 긴급 `kill`은 백업 없이 작업 복사본을 버릴 수 있다. 반복 `stop`은 이미 저장된 복구 체크포인트를 지우지 않는다.

## 네트워크

```sh
python3 sandbox.py config --network none
python3 sandbox.py up
```

```sh
python3 sandbox.py config --network internal
python3 sandbox.py up
```

internal은 같은 실험의 다른 컨테이너를 연결할 수 있는 내부망이며, 외부 인터넷 경로를 제공하지 않는다. 외부 DNS 전달도 차단하고, Docker 내부 서비스 이름 해석만 남긴다. `render`에서 생성될 Docker 설정과 프로젝트 network를 확인할 수 있다. 모드 전환·종료 시 해당 환경의 쓰지 않는 proxy와 빈 network를 정리한다.

```sh
python3 sandbox.py config --network allowlist --allow-host example.com
python3 sandbox.py up
python3 sandbox.py run -- curl https://example.com
python3 sandbox.py network-log
```

allowlist에서는 작업 컨테이너를 내부망에만 연결하고, 외부 연결을 가진 proxy만 허용한 목적지에 연결한다. 환경 변수 `HTTP_PROXY`/`HTTPS_PROXY`를 이용하는 HTTP·HTTPS 클라이언트가 대상이다. 목적지 hostname, 포트 80/443, DNS 해석 결과를 검사하고 loopback·private·link-local·예약 주소를 거부한다. DNS 재해석을 피하기 위해 검증한 숫자 IP에 연결한다. proxy는 동시 연결·전송량·시간을 제한한다. HTTPS 내용은 복호화하지 않으며 임의 TCP/UDP 서비스는 지원하지 않는다. HTTPS 제한은 CONNECT 요청의 hostname과 연결 IP 기준이며, 공유 IP의 가상 호스트·암호화된 SNI·요청 내용까지 검증하는 애플리케이션 계층 방화벽은 아니다. 허용한 서비스로의 데이터 유출 방지는 별도 정책이 필요하다. [Docker 내부 네트워크 설정](https://docs.docker.com/reference/compose-file/networks/#internal)

## 패키지와 LLM·GPU

공통 패키지는 `requirements.txt`, 선택 LLM 패키지는 `requirements-llm.txt`에서 관리한다. 현재 LLM 선택에는 PyTorch, Transformers, Accelerate, Safetensors, NumPy가 있다. 설치는 이미지 빌드 단계에서 이루어지고 실행 중 네트워크 제한은 유지된다. 설치된 버전은 이미지의 `/opt/sandbox/environment.lock`에 기록된다. 첫 준비 이후 팀에서 검증한 버전과 기본 이미지 digest를 고정한다.

```sh
python3 sandbox.py config --llm --memory 16g
python3 sandbox.py build
python3 sandbox.py up
python3 sandbox.py run -- python -c 'import torch, transformers; print(torch.__version__, transformers.__version__)'
```

모델은 미리 내려받아 `models/모델폴더`에 준비하고 `/models/모델폴더`에서 읽는다. 기본 `HF_HUB_OFFLINE=1`이므로 모델이 없으면 자동 다운로드 대신 오류가 난다. [Transformers 오프라인 사용](https://huggingface.co/docs/transformers/installation#offline-mode)

```sh
python3 sandbox.py config --gpu --llm
python3 sandbox.py build
python3 sandbox.py up
python3 sandbox.py run -- python -c 'import torch; print(torch.cuda.is_available())'
```

이 GPU 옵션은 NVIDIA GPU, 호스트 드라이버, NVIDIA Container Toolkit이 준비된 Linux 환경용이다. GPU 번호는 `config --gpu-id 0` 또는 `settings.json`의 `gpu_ids`에서 지정한다. Docker의 RAM 제한이 GPU VRAM 한도까지 보장하지는 않는다. 현재 Mac에서는 기본 CPU 환경을 사용한다. LLM 패키지 이미지 빌드와 실제 모델 추론·GPU 실행은 이번 기본 환경 검증에 포함하지 않았다. [Compose GPU 설정](https://docs.docker.com/compose/how-tos/gpu-support/)

## 점검과 현재 검증 상태

```sh
python3 sandbox.py render
python3 sandbox.py validate
python3 -m unittest discover -s tests -v
SANDBOX_INTEGRATION_TESTS=1 python3 -m unittest discover -s tests -v
```

기본 테스트는 설정 생성, archive 경로·링크·용량 검사, proxy 목적지 검사 등을 수행한다. opt-in 통합 테스트는 **로컬에 이미지가 준비된 Docker 환경**에서 일반 스크립트·자식 프로세스, 스냅샷·복원·초기화, timeout 종료, 읽기 전용 루트와 네트워크를 검증한다. 테스트마다 별도 Compose project를 만든다. 통합 테스트는 자동 이미지 pull/build를 하지 않는다.

2026-10-07 현재 Mac의 전용 Colima VM(Linux arm64, Docker Engine 29.5.2, Compose 5.6.0, runc)에서 기본 이미지를 실제 빌드하고 다음 항목을 확인했다.

최종 자동 테스트는 **24개 전부 통과**했다(오프라인 단위 테스트 13개, 실제 Docker 통합 테스트 11개, skip 0개). [검증 기록](verification.json)에 실행 환경과 검증 범위를 남겼다.

- 일반 Python·셸·자식 프로세스 실행과 UID 10001.
- 대화형 터미널 연결, 파일 반입·반출, 스냅샷·복원·초기화.
- 불완전한 복원 실패 시 기존 파일 복구, 반복 종료 후 체크포인트 보존.
- 기본 인터넷 차단, internal 외부 연결 차단, allowlist 허용/거절, 직접 접속·외부 DNS 차단.
- 실제 cgroup CPU·RAM·swap·프로세스 한도, workspace 용량 초과 시 ENOSPC.
- 메모리 소진의 컨테이너 내 종료, 프로세스 생성 한도, timeout·출력 한도 시 전체 환경 종료.
- 읽기 전용 루트, capabilities 제거, no-new-privileges, Docker seccomp 적용.

`doctor`의 READY는 실행기 준비 상태이며 완전한 격리 안전성 증명은 아니다. **GPU·gVisor·LLM 패키지/모델 추론은 미검증**이다. 알려지지 않은 커널·런타임 취약점에 대한 완전한 탈출 방지, 모든 syscall의 감사, VM 메모리 checkpoint, HTTPS 내용 복호화, 무제한 임의 TCP/UDP·호스트 포트 공개는 구현 범위에 포함하지 않는다. 호스트 실행기와 Docker daemon은 신뢰 경계이며 이들에 접근 가능한 사용자는 Sandbox 관리자 권한을 가진다.

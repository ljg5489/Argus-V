# SANDBOX_PC — 평소용 "컴퓨터" 샌드박스

화면(리눅스 바탕화면)·도구·게임 라이브러리가 든 두 번째 샌드박스입니다. 계획 v1.6으로 잠긴 `SANDBOX/`는 건드리지 않습니다:
이 폴더의 `sandbox.py`는 잠긴 `SANDBOX/sandbox.py`를 그대로 불러서 이 폴더(자기 Dockerfile·설정·컨테이너·사본)에 대해 돌립니다.

```bash
python3.11 SANDBOX_PC/sandbox.py build      # 이미지 만들기(한 번, 약 1.2 GB, 인터넷 필요). 먼저 SANDBOX 쪽 이미지가 있어야 합니다
python3.11 SANDBOX_PC/sandbox.py up         # 켜기 (agent_server.py가 알아서 켭니다)
python3.11 SANDBOX_PC/sandbox.py status     # 상태
python3.11 SANDBOX_PC/sandbox.py stop       # 끄기(작업 폴더는 사본으로 남았다가 다음에 켤 때 돌아옵니다)
```

- 평소 서버 `.venv/bin/python argus_hook/agent_server.py` 가 이 샌드박스를 씁니다(에이전트도 여기서 일합니다). 에이전트가 쓸 샌드박스는 페이지 "에이전트 채팅"의 **샌드박스**에서 바꿉니다(기본 `SANDBOX/` · 컴퓨터 `SANDBOX_PC/` · 인터넷 `SANDBOX_NET/`). 켤 때 정하려면 `--sandbox plain|pc|net`(`--plain`은 `SANDBOX/`).
- 네트워크: 파이썬 패키지 저장소(`pypi.org`, `files.pythonhosted.org`)에만 나갑니다. `settings.json`의 `allowed_hosts`.
- 화면: 페이지의 "샌드박스 컴퓨터" 탭 → "화면" 창. `desktop/start.sh`(바탕화면 켜기), `desktop/screen.py`(화면 내보내기), `desktop/input.py`(키보드·마우스), `desk.py`(서버가 부르는 도우미). 포트는 열지 않습니다.
- 들어 있는 것: Xvfb, openbox, tint2, lxterminal, pcmanfm, l3afpad, Mesa(CPU로 그리는 OpenGL), 나눔 글꼴, tree vim nano less htop zip unzip file wget jq, panda3d pygame numpy pillow matplotlib requests.
- 패키지를 더 넣으려면 `Dockerfile`을 고치고 다시 `build` → `up` 합니다(작업 폴더는 유지됩니다).

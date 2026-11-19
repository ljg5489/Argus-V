"""Local companion API for the Argus-V Scenario Studio Site.

Run from the repository root with Python 3.11:
    python argus_hook/dashboard_server.py

The server binds to loopback only. The browser dashboard can use this API while
the saved Site remains a static, private front end. Replay inference reuses the
existing replay_demo.py record/hidden-state pipeline without modifying it.

The agent chat tab uses /api/live/*: argus_hook/live_agent.py keeps the local
gpt-oss-20b loaded, works in the SANDBOX and reports every step with its
Argus-V-emp verdict while it happens (live_agent_service.py keeps the events).
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import threading
import uuid
from datetime import datetime, timezone
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from live_agent_service import LiveAgent


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "sites" / "argus-v-demo-dashboard" / "dist"
ASSETS = ROOT / "argus_hook" / "replay_assets"
SCORES_FILE = ASSETS / "argus_v_p_scores.json"
DESCRIPTIONS_FILE = ASSETS / "scenario_descriptions.json"
REPLAY_SCRIPT = ROOT / "argus_hook" / "replay_demo.py"
AGENT_SCRIPT = ROOT / "argus_hook" / "agent_loop.py"
LIVE_SCRIPT = ROOT / "argus_hook" / "live_agent.py"
EMP_MANIFEST = ROOT / "artifacts" / "risk-loop" / "resplit-1117" / "argus_v_emp" / "manifest.json"
JOBS: dict[str, dict] = {}
JOBS_LOCK = threading.Lock()
_RUNTIME_LOCK = threading.Lock()
_PYTHON311: str | None | bool = False
_CUDA_AVAILABLE: bool | None = None
MAX_TASK_CHARS = 4_000
ALLOWED_ORIGINS = {
    "http://127.0.0.1:8765",
    "http://localhost:8765",
    "https://ljg5489.github.io",  # GitHub Pages copy of the dashboard
    os.environ.get("ARGUS_SITE_ORIGIN", "https://argus-v-scenario-studio.triplelace3.chatgpt.site"),
}
MAX_LIVE_STEPS = 10
MODEL_CHECKPOINTS = {
    "P5": ASSETS / "argus_v_p_P5.bundle",
    "P6": ASSETS / "argus_v_p_P6.bundle",
    "EM32": ROOT / "artifacts" / "risk-loop" / "argus-v-em" / "argus_v_em_round01.pt",
    "EM300": ROOT / "artifacts" / "risk-loop" / "argus-v-em300" / "argus_v_em300.pt",
}
MODEL_NAMES = {
    "P5": "Argus-V-p · P5",
    "P6": "Argus-V-p · P6",
    "EM32": "Argus-V-em · EM32 / epoch 60",
    "EM300": "Argus-V-em300 · EM32 / epoch 300",
}


def python311_executable() -> str | None:
    """Resolve the executable name hard-coded by the existing sandbox client."""
    global _PYTHON311
    if _PYTHON311 is not False:
        return _PYTHON311
    found = shutil.which("python3.11") or shutil.which("python3.11.exe")
    if found:
        _PYTHON311 = found
        return _PYTHON311
    if os.name != "nt" or sys.version_info[:2] != (3, 11):
        _PYTHON311 = None
        return None
    alias_dir = Path(tempfile.gettempdir()) / "argus-scenario-studio-runtime"
    alias = alias_dir / "python3.11.exe"
    try:
        alias_dir.mkdir(exist_ok=True)
        if not alias.is_file():
            shutil.copy2(sys.executable, alias)
        result = subprocess.run([str(alias), "--version"], capture_output=True, text=True, timeout=8)
        _PYTHON311 = str(alias) if result.returncode == 0 else None
    except (OSError, subprocess.SubprocessError):
        _PYTHON311 = None
    return _PYTHON311


def child_env(python311: bool = False) -> dict:
    """Environment of a child process; ``python311`` puts the sandbox client's python3.11 alias on PATH."""
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    if python311:
        alias = python311_executable()
        if alias:
            env["PATH"] = str(Path(alias).parent) + os.pathsep + env.get("PATH", "")
    return env


def live_env() -> dict:
    env = child_env(python311=True)
    env["PYTHONUNBUFFERED"] = "1"
    return env


# The live chat worker keeps gpt-oss-20b on the GPU between tasks (argus_hook/live_agent.py).
LIVE = LiveAgent([sys.executable, str(LIVE_SCRIPT)], ROOT, live_env)


def uses_gpu(job: dict) -> bool:
    """Jobs that load gpt-oss-20b themselves (they cannot run next to the live worker on one GPU)."""
    return job["kind"] == "agent" or (job["kind"] == "replay" and job.get("mode") == "tokens")


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def scenario_catalog() -> dict:
    table = read_json(SCORES_FILE)
    descriptions = read_json(DESCRIPTIONS_FILE).get("scenarios", {}) if DESCRIPTIONS_FILE.exists() else {}
    recommended = set(table.get("recommended_units", []))
    scenarios: dict[str, dict] = {}
    for unit_id, unit in table["units"].items():
        row = scenarios.setdefault(unit["scenario"], {
            "id": unit["scenario"], "runs": [], "violations": 0, "recommended": 0,
        })
        violations = [step for step in unit["steps"] if int(step[2]) == 1]
        row["violations"] += len(violations)
        row["runs"].append({
            "id": unit_id,
            "condition": unit["condition"],
            "seed": unit["seed"],
            "family": unit.get("family", ""),
            "recommended": unit_id in recommended,
            "violation_count": len(violations),
            "steps": [
                {"index": int(s[0]), "tool": s[1], "label": int(s[2]), "p6": float(s[3]), "p5": float(s[4])}
                for s in unit["steps"]
            ],
        })
        row["recommended"] += int(unit_id in recommended)
    out = []
    for scenario_id, row in sorted(scenarios.items()):
        desc = descriptions.get(scenario_id, {})
        row.update({
            "title": desc.get("title") or scenario_id,
            "category": desc.get("category", ""),
            "task": desc.get("task", ""),
            "situation": desc.get("situation", ""),
            "forbidden": desc.get("forbidden", ""),
        })
        row["runs"].sort(key=lambda run: (not run["recommended"], run["condition"], str(run["seed"]), run["id"]))
        out.append(row)
    return {"scenarios": out, "models": table.get("step_columns", []), "source_note": table.get("note", "")}


def available_models() -> list[dict]:
    return [{"id": key, "name": MODEL_NAMES[key]}
            for key, path in MODEL_CHECKPOINTS.items() if path.is_file()]


def runtime_status() -> dict:
    catalog = scenario_catalog()
    model_dir = Path.home() / "Desktop" / "Argus-V" / "gpt-oss-20b"
    sandbox = ROOT / "SANDBOX" / "sandbox.py"
    docker = shutil.which("docker") or shutil.which("docker.exe")
    global _CUDA_AVAILABLE
    if _CUDA_AVAILABLE is None:
        with _RUNTIME_LOCK:
            if _CUDA_AVAILABLE is None:
                try:
                    import torch

                    _CUDA_AVAILABLE = bool(torch.cuda.is_available())
                except Exception:
                    _CUDA_AVAILABLE = False
    with JOBS_LOCK:
        active = next((job["id"] for job in JOBS.values() if job["process"].poll() is None), None)
    return {
        "ok": True,
        "python": sys.version.split()[0],
        "scenario_count": len(catalog["scenarios"]),
        "run_count": sum(len(s["runs"]) for s in catalog["scenarios"]),
        "p5_bundle": (ASSETS / "argus_v_p_P5.bundle").is_file(),
        "p6_bundle": (ASSETS / "argus_v_p_P6.bundle").is_file(),
        "available_models": available_models(),
        "local_rollouts": any((ROOT / "artifacts" / name).is_dir() for name in ("rollouts", "rollouts-v2", "rollouts-dec-v1")),
        "agent_model_dir": model_dir.is_dir(),
        "cuda_available": _CUDA_AVAILABLE,
        "sandbox_script": sandbox.is_file(),
        "docker_available": bool(docker),
        "python311_command": bool(python311_executable()),
        "emp_bundle": EMP_MANIFEST.is_file(),
        "live_script": LIVE_SCRIPT.is_file(),
        "live": LIVE.status(),
        "active_job": active,
    }


def live_missing(health: dict) -> list[str]:
    """What the live chat still needs on this machine."""
    return [label for key, label in (
        ("agent_model_dir", "gpt-oss-20b 로컬 모델"),
        ("cuda_available", "CUDA GPU"),
        ("sandbox_script", "샌드박스 스크립트"),
        ("docker_available", "Docker"),
        ("python311_command", "Python 3.11 sandbox 호출"),
        ("emp_bundle", "Argus-V-emp 모델 파일"),
        ("live_script", "argus_hook/live_agent.py"),
    ) if not health[key]]


def start_live(task: str | None = None, max_steps: int = 5) -> dict:
    """Load the live worker (and queue ``task``) unless another job holds the GPU."""
    with JOBS_LOCK:
        if any(job["process"].poll() is None and uses_gpu(job) for job in JOBS.values()):
            raise ValueError("다른 GPU 작업(토큰 재계산 또는 기존 에이전트 실행)이 끝난 뒤 다시 시도해 주세요.")
    missing = live_missing(runtime_status())
    if missing:
        raise ValueError("실시간 에이전트를 실행할 수 없습니다. 준비되지 않은 항목: " + ", ".join(missing))
    if task is None:
        return LIVE.start()
    return LIVE.submit(task, max_steps)


def start_job(kind: str, command: list[str], extra: dict) -> dict:
    with JOBS_LOCK:
        if any(job["process"].poll() is None for job in JOBS.values()):
            raise ValueError("이미 실행 중인 작업이 있습니다. 먼저 현재 작업이 끝날 때까지 기다려 주세요.")
        if uses_gpu({"kind": kind, **extra}) and LIVE.running():
            raise ValueError("실시간 에이전트가 gpt-oss-20b를 GPU에 올려 두었습니다. "
                             "에이전트 채팅 탭에서 '모델 내리기'를 누른 뒤 다시 시도해 주세요.")
        job_id = uuid.uuid4().hex
        log_path = Path(tempfile.gettempdir()) / f"argus-dashboard-{job_id}.log"
        env = child_env(python311=kind == "agent")
        log = log_path.open("wb")
        try:
            process = subprocess.Popen(
                command, cwd=ROOT, stdout=log, stderr=subprocess.STDOUT,
                env=env, creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
            )
        except Exception:
            log.close()
            raise
        log.close()
        job = {"id": job_id, "kind": kind, "process": process, "log_path": log_path,
               "started_at": datetime.now(timezone.utc).isoformat(), **extra}
        JOBS[job_id] = job
    return {"id": job_id, "kind": kind, "started_at": job["started_at"]}


class Handler(SimpleHTTPRequestHandler):
    server_version = "ArgusScenarioStudio/1.0"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIST), **kwargs)

    def log_message(self, _fmt, *_args):
        return

    def _headers(self, status: int, origin: str | None = None):
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        if origin and origin in ALLOWED_ORIGINS:
            self.send_header("Access-Control-Allow-Origin", origin)
            self.send_header("Vary", "Origin")
            self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
            self.send_header("Access-Control-Allow-Headers", "Content-Type")
            self.send_header("Access-Control-Allow-Private-Network", "true")
        self.end_headers()

    def _json(self, status: int, body: dict):
        origin = self.headers.get("Origin")
        self._headers(status, origin)
        self.wfile.write(json.dumps(body, ensure_ascii=False).encode("utf-8"))

    def _body(self) -> dict:
        length = int(self.headers.get("Content-Length", "0"))
        if length > 64_000:
            raise ValueError("요청이 너무 큽니다.")
        body = json.loads(self.rfile.read(length) or b"{}")
        if not isinstance(body, dict):
            raise ValueError("JSON 객체가 필요합니다.")
        return body

    def do_OPTIONS(self):
        origin = self.headers.get("Origin")
        if origin not in ALLOWED_ORIGINS:
            return self._json(403, {"error": "허용되지 않은 웹 출처입니다."})
        self._headers(204, origin)

    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/api/health":
            try:
                return self._json(200, runtime_status())
            except Exception as error:
                return self._json(500, {"error": str(error)})
        if path == "/api/scenarios":
            try:
                return self._json(200, scenario_catalog())
            except Exception as error:
                return self._json(500, {"error": str(error)})
        if path == "/api/live/status":
            return self._json(200, LIVE.status())
        if path == "/api/live/events":
            query = parse_qs(urlparse(self.path).query)
            try:
                after = int(query.get("after", ["0"])[0])
                wait = float(query.get("wait", ["0"])[0])
            except ValueError:
                return self._json(400, {"error": "after와 wait는 숫자여야 합니다."})
            return self._json(200, LIVE.events_after(after, wait))
        if path.startswith("/api/jobs/"):
            job_id = path.rsplit("/", 1)[-1]
            with JOBS_LOCK:
                job = JOBS.get(job_id)
            if not job:
                return self._json(404, {"error": "작업을 찾을 수 없습니다."})
            try:
                output = job["log_path"].read_text(encoding="utf-8", errors="replace")
            except OSError:
                output = ""
            code = job["process"].poll()
            score_data = None
            clean_lines = []
            for line in output.splitlines():
                if line.startswith("ARGUS_RESULT_JSON="):
                    try:
                        score_data = json.loads(line.split("=", 1)[1])
                    except json.JSONDecodeError:
                        clean_lines.append("추론 결과를 읽지 못했습니다.")
                else:
                    clean_lines.append(line)
            output = "\n".join(clean_lines)
            return self._json(200, {"id": job_id, "kind": job["kind"], "output": output[-50_000:],
                                    "running": code is None, "exit_code": code,
                                    "started_at": job["started_at"], "score_data": score_data,
                                    **job.get("result", {})})
        if path.startswith("/api/"):
            return self._json(404, {"error": "지원하지 않는 API입니다."})
        return super().do_GET()

    def do_POST(self):
        path = urlparse(self.path).path
        if path == "/api/replay/start":
            try:
                body = self._body()
                catalog = scenario_catalog()
                scenario = next((s for s in catalog["scenarios"] if s["id"] == body.get("scenario")), None)
                if not scenario:
                    raise ValueError("선택한 시나리오가 점수표에 없습니다.")
                unit_id = body.get("unit")
                unit = next((u for u in scenario["runs"] if u["id"] == unit_id), None)
                if not unit:
                    raise ValueError("해당 시나리오에 속한 실행 기록을 선택해 주세요.")
                mode = body.get("mode", "hidden")
                if mode not in ("hidden", "tokens"):
                    raise ValueError("재생 모드는 saved hidden 또는 tokens여야 합니다.")
                model = body.get("model", "P5")
                if model not in MODEL_CHECKPOINTS or not MODEL_CHECKPOINTS[model].is_file():
                    raise ValueError("선택한 모델의 추론 체크포인트를 찾을 수 없습니다.")
                command = [sys.executable, str(ROOT / "argus_hook" / "replay_model_inference.py"),
                           "--unit", unit_id, "--model", model, "--mode", mode]
                if body.get("offline"):
                    command.append("--offline")
                return self._json(202, start_job("replay", command, {
                    "scenario": scenario["id"], "unit": unit_id, "model": model, "mode": mode,
                }))
            except ValueError as error:
                return self._json(400, {"error": str(error)})
            except Exception as error:
                return self._json(500, {"error": str(error)})
        if path == "/api/agent/start":
            try:
                body = self._body()
                task = str(body.get("task", "")).strip()
                if not task or len(task) > MAX_TASK_CHARS:
                    raise ValueError(f"작업은 1~{MAX_TASK_CHARS:,}자로 입력해 주세요.")
                if not AGENT_SCRIPT.is_file():
                    raise ValueError("argus_hook/agent_loop.py를 찾을 수 없습니다.")
                health = runtime_status()
                missing = [label for key, label in (
                    ("agent_model_dir", "gpt-oss-20b 로컬 모델"),
                    ("cuda_available", "CUDA GPU"),
                    ("sandbox_script", "샌드박스 스크립트"),
                    ("docker_available", "Docker"),
                    ("python311_command", "Python 3.11 sandbox 호출"),
                ) if not health[key]]
                if missing:
                    raise ValueError("에이전트를 실행할 수 없습니다. 준비되지 않은 항목: " + ", ".join(missing))
                steps = int(body.get("max_steps", 5))
                if not 1 <= steps <= 10:
                    raise ValueError("step 수는 1~10 범위여야 합니다.")
                command = [sys.executable, str(AGENT_SCRIPT), "--task", task,
                           "--hook-phase", "generation", "--max-steps", str(steps)]
                return self._json(202, start_job("agent", command, {"task": task}))
            except ValueError as error:
                return self._json(400, {"error": str(error)})
            except Exception as error:
                return self._json(500, {"error": str(error)})
        if path in ("/api/live/start", "/api/live/load", "/api/live/unload", "/api/live/cancel"):
            try:
                body = self._body()
                if path == "/api/live/start":
                    task = str(body.get("task", "")).strip()
                    if not task or len(task) > MAX_TASK_CHARS:
                        raise ValueError(f"작업은 1~{MAX_TASK_CHARS:,}자로 입력해 주세요.")
                    steps = int(body.get("max_steps", 5))
                    if not 1 <= steps <= MAX_LIVE_STEPS:
                        raise ValueError(f"step 수는 1~{MAX_LIVE_STEPS} 범위여야 합니다.")
                    return self._json(202, start_live(task, steps))
                if path == "/api/live/load":
                    return self._json(202, start_live())
                if path == "/api/live/unload":
                    return self._json(200, LIVE.stop())
                return self._json(200, LIVE.cancel())
            except ValueError as error:
                return self._json(400, {"error": str(error)})
            except Exception as error:
                return self._json(500, {"error": str(error)})
        self._json(404, {"error": "지원하지 않는 API입니다."})


def main():
    if not SCORES_FILE.is_file() or not DESCRIPTIONS_FILE.is_file():
        raise SystemExit("Argus-V replay assets are missing under argus_hook/replay_assets.")
    if not DIST.is_dir() or not (DIST / "index.html").is_file():
        raise SystemExit(f"Dashboard UI is missing: {DIST / 'index.html'}")
    server = ThreadingHTTPServer(("127.0.0.1", 8765), Handler)
    print("Argus-V Scenario Studio: http://127.0.0.1:8765")
    print("Local companion API binds to 127.0.0.1 only.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nDashboard stopped.")
    finally:
        server.server_close()
        if LIVE.running():
            print("Unloading the live agent model...")
            LIVE.stop()


if __name__ == "__main__":
    main()

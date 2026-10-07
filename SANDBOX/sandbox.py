#!/usr/bin/env python3
"""Generic Docker work environment. The host executes Docker, never user code."""

import argparse
import contextlib
import datetime
import fcntl
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import selectors
import shutil
import signal
import subprocess
import sys
import tarfile
import tempfile
import time
import uuid
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent
OWNER = "org.generic-sandbox.owner"
CONFIG = "org.generic-sandbox.config"
EXCLUDED = {".git", ".venv", "node_modules", "__pycache__", ".env", ".aws", ".ssh", ".codex", ".agents"}
SIZES = re.compile(r"([1-9][0-9]*)([mg])\Z")


def size_bytes(value):
    match = SIZES.fullmatch(value) if type(value) is str else None
    if not match:
        raise ValueError("sizes must use positive m/g units, e.g. 512m or 4g")
    result = int(match[1]) * (1024**2 if match[2] == "m" else 1024**3)
    if result > 1024**4:
        raise ValueError("size exceeds 1 TiB")
    return result


def validate_settings(value):
    required = {"cpus", "memory", "workspace_size", "tmp_size", "pids", "timeout_seconds",
                "log_limit_bytes", "archive_limit_bytes", "network", "allowed_hosts", "runtime",
                "gpu", "gpu_ids", "llm_packages"}
    if type(value) is not dict or set(value) != required:
        raise ValueError("settings keys do not match settings.json")
    if type(value["cpus"]) not in (int, float) or not 0.1 <= value["cpus"] <= 64:
        raise ValueError("cpus must be 0.1..64")
    memory = size_bytes(value["memory"])
    if memory < 256 * 1024**2 or size_bytes(value["workspace_size"]) + size_bytes(value["tmp_size"]) > memory:
        raise ValueError("memory must cover workspace+tmp quotas and be at least 256 MiB")
    for name, lower, upper in (("pids", 32, 4096), ("timeout_seconds", 1, 86400),
                               ("log_limit_bytes", 4096, 1024**3),
                               ("archive_limit_bytes", 4096, 16 * 1024**3)):
        if type(value[name]) is not int or not lower <= value[name] <= upper:
            raise ValueError(name + " is outside the supported range")
    if value["network"] not in ("none", "internal", "allowlist") or value["runtime"] not in ("runc", "runsc"):
        raise ValueError("unsupported network/runtime")
    if any(type(value[name]) is not bool for name in ("gpu", "llm_packages")):
        raise ValueError("gpu and llm_packages must be booleans")
    if type(value["gpu_ids"]) is not list or not value["gpu_ids"] or not all(
            type(v) is str and re.fullmatch(r"[0-9]{1,2}", v) for v in value["gpu_ids"]):
        raise ValueError("gpu_ids must be explicit numeric device IDs")
    if value["gpu"] and value["runtime"] != "runc":
        raise ValueError("this GPU profile requires runc + NVIDIA Container Toolkit")
    if type(value["allowed_hosts"]) is not list or len(value["allowed_hosts"]) > 64:
        raise ValueError("allowed_hosts must be a list with at most 64 hosts")
    for host in value["allowed_hosts"]:
        if (type(host) is not str or len(host) > 253 or host != host.lower()
                or not re.fullmatch(r"[a-z0-9](?:[a-z0-9.-]*[a-z0-9])?", host)
                or "." not in host or ".." in host):
            raise ValueError("allowed_hosts must be lower-case hostnames, not URLs")
    if value["network"] == "allowlist" and not value["allowed_hosts"]:
        raise ValueError("allowlist mode requires allowed_hosts")
    return value


def fingerprint(settings):
    return hashlib.sha256(json.dumps(settings, sort_keys=True).encode()).hexdigest()


def compose_spec(settings, owner, root=ROOT):
    validate_settings(settings)
    image = "local/generic-sandbox:" + ("llm" if settings["llm_packages"] else "python")
    service = {
        "image": image,
        "build": {"context": str(root), "args": {"LLM_PACKAGES": "1" if settings["llm_packages"] else "0"}},
        "working_dir": "/workspace", "user": "10001:10001", "init": True,
        "command": ["sleep", "infinity"], "read_only": True, "runtime": settings["runtime"],
        "cap_drop": ["ALL"], "security_opt": ["no-new-privileges:true"],
        "dns": ["127.0.0.1"],
        "mem_limit": settings["memory"], "memswap_limit": settings["memory"],
        "cpus": settings["cpus"], "pids_limit": settings["pids"], "shm_size": "256m",
        "ulimits": {"core": {"soft": 0, "hard": 0}, "nofile": {"soft": 1024, "hard": 1024}},
        "tmpfs": ["/workspace:rw,nosuid,nodev,uid=10001,gid=10001,mode=0700,size=" + settings["workspace_size"],
                  "/tmp:rw,noexec,nosuid,nodev,mode=1777,size=" + settings["tmp_size"]],
        "volumes": [{"type": "bind", "source": str(root / "models"), "target": "/models",
                     "read_only": True, "bind": {"create_host_path": False}}],
        "environment": {"HOME": "/workspace/.home", "HF_HUB_OFFLINE": "1",
                        "OMP_NUM_THREADS": str(max(1, int(settings["cpus"]))),
                        "TOKENIZERS_PARALLELISM": "false"},
        "labels": {OWNER: owner, CONFIG: fingerprint(settings)},
        "logging": {"driver": "none"}, "restart": "no", "stop_grace_period": "5s",
    }
    result = {"services": {"sandbox": service}}
    if settings["gpu"]:
        service["deploy"] = {"resources": {"reservations": {"devices": [
            {"driver": "nvidia", "device_ids": settings["gpu_ids"], "capabilities": ["gpu"]}]}}}
    if settings["network"] == "none":
        service["network_mode"] = "none"
    else:
        result["networks"] = {"internal": {"internal": True, "labels": {OWNER: owner}}}
        service["networks"] = ["internal"]
    if settings["network"] == "allowlist":
        result["networks"]["egress"] = {"labels": {OWNER: owner}}
        service["depends_on"] = ["proxy"]
        service["environment"].update(HTTP_PROXY="http://proxy:8080", HTTPS_PROXY="http://proxy:8080",
                                       http_proxy="http://proxy:8080", https_proxy="http://proxy:8080",
                                       NO_PROXY="localhost,127.0.0.1,proxy")
        result["services"]["proxy"] = {
            "image": image, "user": "10001:10001", "read_only": True,
            "entrypoint": ["python", "-I", "/opt/sandbox/proxy.py"], "command": [],
            "networks": ["internal", "egress"], "cap_drop": ["ALL"],
            "security_opt": ["no-new-privileges:true"], "mem_limit": "256m", "cpus": 0.5,
            "memswap_limit": "256m", "pids_limit": 64, "init": True,
            "ulimits": {"core": {"soft": 0, "hard": 0}, "nofile": {"soft": 1024, "hard": 1024}},
            "tmpfs": ["/tmp:rw,noexec,nosuid,nodev,size=16m"],
            "environment": {"ALLOWED_HOSTS": ",".join(settings["allowed_hosts"])},
            "labels": {OWNER: owner, CONFIG: fingerprint(settings)},
            "logging": {"driver": "json-file", "options": {"max-size": "1m", "max-file": "3"}}, "restart": "no",
        }
    return result


def archive_members(path, limit):
    if path.stat().st_size > limit:
        raise ValueError("archive byte limit exceeded")
    total, count = 0, 0
    with tarfile.open(path, "r:") as archive:
        for member in archive:
            count += 1
            parts = PurePosixPath(member.name).parts
            if (count > 100_000 or len(member.name) > 1024 or member.name.startswith("/")
                    or ".." in parts or "\\" in member.name or "\x00" in member.name
                    or member.size < 0 or not (member.isfile() or member.isdir())):
                raise ValueError("archive contains unsupported paths, links or special files")
            total += member.size
            if total > limit or member.offset_data + member.size > path.stat().st_size:
                raise ValueError("archive payload is too large or truncated")
    return {"members": count, "payload_bytes": total}


def make_archive(source, target, limit):
    source = Path(source).resolve(strict=True)
    if source == Path("/") or source == Path.home():
        raise ValueError("select a specific project directory/file")
    total = 0
    skipped = []
    with tarfile.open(target, "w:") as archive:
        def project_files():
            if source.is_file():
                yield source
                return
            for directory, children, files in os.walk(source, followlinks=False):
                kept = []
                for child in children:
                    path = Path(directory) / child
                    if child in EXCLUDED:
                        skipped.append(str(path.relative_to(source)))
                    elif path.is_symlink():
                        raise ValueError("source directory symlinks are not imported")
                    else:
                        kept.append(child)
                children[:] = kept
                for name in files:
                    yield Path(directory) / name
        count = 0
        for path in project_files():
            count += 1
            if count > 100_000:
                raise ValueError("import file count limit exceeded")
            relative = Path(source.name) if source.is_file() else path.relative_to(source)
            if any(part in EXCLUDED or part.startswith(".env.") for part in relative.parts):
                skipped.append(str(relative))
                continue
            if path.is_symlink():
                raise ValueError("source symlinks are not imported: " + str(relative))
            if path.is_dir():
                continue
            if not path.is_file():
                raise ValueError("source special files are not imported")
            total += path.stat().st_size
            if total > limit:
                raise ValueError("import byte limit exceeded")
            archive.add(path, arcname=str(relative), recursive=False)
    archive_members(target, limit)
    return {"bytes": total, "excluded": skipped}


def atomic_json(path, value):
    path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    descriptor, temp = tempfile.mkstemp(prefix=".new-", dir=path.parent)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
            json.dump(value, stream, indent=2, ensure_ascii=False, allow_nan=False)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temp, path)
    finally:
        if os.path.exists(temp):
            os.unlink(temp)


class Runtime:
    def __init__(self, root=ROOT):
        self.root = Path(root).resolve()
        self.settings = validate_settings(json.loads((self.root / "settings.json").read_text()))
        self.owner = hashlib.sha256(str(self.root).encode()).hexdigest()[:16]
        self.project = "sandbox-" + self.owner
        self.state = self.root / ".state"
        self.generated = self.state / "compose.json"
        self.docker = shutil.which("docker")
        self.endpoint = None
        self.environment = {k: v for k, v in os.environ.items() if k not in
                            {"DOCKER_HOST", "DOCKER_CONTEXT", "DOCKER_TLS_VERIFY", "DOCKER_CERT_PATH"}}
        client_config = self.root / ".state/docker-client"
        if (client_config / "config.json").is_file():
            self.environment["DOCKER_CONFIG"] = str(client_config)

    def check_docker(self):
        if not self.docker:
            raise RuntimeError("DOCKER_NOT_FOUND: install/start Docker to run containers")
        if self.endpoint:
            return
        endpoint = os.environ.get("SANDBOX_DOCKER_HOST") or os.environ.get("DOCKER_HOST")
        if not endpoint and (self.state / "docker-endpoint.json").is_file():
            endpoint = json.loads((self.state / "docker-endpoint.json").read_text())["endpoint"]
        if not endpoint:
            result = subprocess.run([self.docker, "context", "inspect", "--format", "{{json .Endpoints.docker.Host}}"],
                                    capture_output=True, env=self.environment, timeout=10)
            if result.returncode or len(result.stdout) > 65_536:
                raise RuntimeError("cannot read Docker context")
            endpoint = json.loads(result.stdout)
        uri = urlsplit(endpoint)
        if (uri.scheme != "unix" or uri.netloc or uri.query or uri.fragment or "%" in endpoint
                or not uri.path.startswith("/") or os.path.normpath(uri.path) != uri.path):
            raise RuntimeError("only a local Unix Docker socket is supported")
        self.endpoint = endpoint

    def command(self, args):
        self.check_docker()
        return [self.docker, "--host", self.endpoint] + args

    def control(self, args, *, data=None, timeout=30):
        result = subprocess.run(self.command(args), input=data, capture_output=True,
                                env=self.environment, timeout=timeout)
        if len(result.stdout) + len(result.stderr) > 1024 * 1024:
            raise RuntimeError("Docker diagnostic output limit")
        if result.returncode:
            raise RuntimeError(result.stderr.decode(errors="replace")[:2000] or "Docker command failed")
        return result.stdout

    def render(self):
        return compose_spec(self.settings, self.owner, self.root)

    def compose(self, args):
        atomic_json(self.generated, self.render())
        return ["compose", "--project-name", self.project, "--project-directory", str(self.root),
                "--file", str(self.generated)] + args

    @contextlib.contextmanager
    def lock(self):
        self.state.mkdir(mode=0o700, parents=True, exist_ok=True)
        path = self.state / "operation.lock"
        descriptor = os.open(path, os.O_CREAT | os.O_RDWR | getattr(os, "O_NOFOLLOW", 0), 0o600)
        try:
            fcntl.flock(descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
            yield
        except BlockingIOError:
            raise RuntimeError("another sandbox operation is active")
        finally:
            os.close(descriptor)

    def cid(self, *, current=True, required=True):
        raw = self.control(self.compose(["ps", "--all", "--quiet", "sandbox"]))
        cid = raw.decode().strip()
        if not cid:
            if required:
                raise RuntimeError("sandbox is not running; run up first")
            return None
        if not re.fullmatch(r"[0-9a-f]{12,64}", cid):
            raise RuntimeError("unexpected container identity")
        container = json.loads(self.control(["container", "inspect", cid]))[0]
        labels = container.get("Config", {}).get("Labels", {})
        if labels.get(OWNER) != self.owner:
            raise RuntimeError("container does not belong to this environment")
        if current and labels.get(CONFIG) != fingerprint(self.settings):
            raise RuntimeError("configuration changed; run up to apply it with a backup")
        config, host = container.get("Config", {}), container.get("HostConfig", {})
        if (config.get("User") != "10001:10001" or config.get("WorkingDir") != "/workspace"
                or host.get("Privileged") is not False or host.get("ReadonlyRootfs") is not True
                or host.get("CapAdd") or host.get("PortBindings") or host.get("Devices")
                or host.get("PublishAllPorts") or host.get("VolumesFrom")
                or host.get("PidMode") or host.get("IpcMode") != "private"
                or host.get("UTSMode") or host.get("ExtraHosts")
                or host.get("Dns") != ["127.0.0.1"]
                or {v.upper() for v in host.get("CapDrop", [])} != {"ALL"}
                or not any(v in ("no-new-privileges", "no-new-privileges:true", "no-new-privileges=true")
                           for v in host.get("SecurityOpt", []))
                or any("unconfined" in v for v in host.get("SecurityOpt", []))):
            raise RuntimeError("actual container isolation settings do not match")
        model_mounts = 0
        for mount in container.get("Mounts", []):
            if mount.get("Type") == "tmpfs" and mount.get("Destination") in ("/workspace", "/tmp"):
                continue
            if (mount.get("Type") == "bind" and mount.get("Destination") == "/models"
                    and mount.get("Source") == str(self.root / "models") and mount.get("RW") is False):
                model_mounts += 1
                continue
            raise RuntimeError("unexpected mount in sandbox")
        if model_mounts != 1:
            raise RuntimeError("expected read-only model mount is missing")
        if current:
            expected_tmpfs = dict(entry.split(":", 1) for entry in self.render()["services"]["sandbox"]["tmpfs"])
            if (host.get("Memory") != size_bytes(self.settings["memory"])
                    or host.get("MemorySwap") != size_bytes(self.settings["memory"])
                    or host.get("NanoCpus") != round(self.settings["cpus"] * 1_000_000_000)
                    or host.get("PidsLimit") != self.settings["pids"]
                    or host.get("Tmpfs") != expected_tmpfs or host.get("Init") is not True
                    or host.get("ShmSize") != 256 * 1024**2
                    or host.get("Runtime") != self.settings["runtime"]):
                raise RuntimeError("actual resource limits do not match settings")
            networks = container.get("NetworkSettings", {}).get("Networks", {})
            if ((self.settings["network"] == "none" and host.get("NetworkMode") != "none")
                    or (self.settings["network"] != "none" and set(networks) != {self.project + "_internal"})):
                raise RuntimeError("actual network differs from selected policy")
            if self.settings["network"] != "none":
                internal = json.loads(self.control(["network", "inspect", self.project + "_internal"]))[0]
                if internal.get("Internal") is not True:
                    raise RuntimeError("internal network unexpectedly permits external routing")
            if self.settings["network"] == "allowlist":
                self.check_proxy()
        if not container.get("State", {}).get("Running"):
            if required:
                raise RuntimeError("sandbox is stopped; run up first")
            return None
        return cid

    def check_proxy(self):
        identity = self.control(self.compose(["ps", "--all", "--quiet", "proxy"])).decode().strip()
        if not re.fullmatch(r"[0-9a-f]{12,64}", identity):
            raise RuntimeError("allowlist proxy is unavailable")
        proxy = json.loads(self.control(["container", "inspect", identity]))[0]
        host, config = proxy["HostConfig"], proxy["Config"]
        labels = config.get("Labels", {})
        if (labels.get(OWNER) != self.owner or labels.get(CONFIG) != fingerprint(self.settings)
                or proxy["State"].get("Running") is not True or config.get("User") != "10001:10001"
                or config.get("Entrypoint") != ["python", "-I", "/opt/sandbox/proxy.py"]
                or host.get("ReadonlyRootfs") is not True or host.get("Privileged")
                or host.get("CapAdd") or {v.upper() for v in host.get("CapDrop", [])} != {"ALL"}
                or host.get("PortBindings") or host.get("Devices")
                or any(v.get("Type") != "tmpfs" for v in proxy.get("Mounts", []))
                or host.get("Memory") != 256 * 1024**2 or host.get("MemorySwap") != 256 * 1024**2
                or host.get("PidsLimit") != 64 or host.get("NanoCpus") != 500_000_000
                or not any(v == "ALLOWED_HOSTS=" + ",".join(self.settings["allowed_hosts"])
                           for v in config.get("Env", []))
                or set(proxy["NetworkSettings"]["Networks"]) !=
                   {self.project + "_internal", self.project + "_egress"}):
            raise RuntimeError("allowlist proxy configuration does not match")

    def save_session(self, snapshot=None):
        atomic_json(self.state / "session.json", {"restore_on_up": str(snapshot) if snapshot else None})

    def cleanup_networks(self, keep=()):
        """Remove only empty internal/egress networks belonging to this project."""
        identities = self.control(["network", "ls", "--quiet", "--filter",
                                   "label=com.docker.compose.project=" + self.project]).decode().split()
        removed = []
        for identity in identities:
            if not re.fullmatch(r"[0-9a-f]{12,64}", identity):
                raise RuntimeError("unexpected network identity")
            network = json.loads(self.control(["network", "inspect", identity]))[0]
            labels, name = network.get("Labels") or {}, network.get("Name")
            if (labels.get("com.docker.compose.project") != self.project
                    or labels.get(OWNER) not in (None, self.owner)
                    or name not in {self.project + "_internal", self.project + "_egress"}
                    or name in keep or network.get("Containers")):
                continue
            self.control(["network", "rm", identity])
            removed.append(name)
        return removed

    def snapshot(self, *, cid=None, name=None, relative=None):
        cid = cid or self.cid()
        if name is not None and not re.fullmatch(r"[a-zA-Z0-9_-]{1,64}", name):
            raise ValueError("snapshot name must be letters/numbers/_/-")
        if relative is not None:
            if (not relative or relative.startswith("/") or "\\" in relative or "\x00" in relative
                    or any(part in ("", ".", "..") for part in relative.split("/"))):
                raise ValueError("export path must be a specific relative path inside /workspace")
        folder = self.root / ("exports" if relative is not None else "snapshots")
        folder.mkdir(mode=0o700, exist_ok=True)
        name = (name + "-" if name else "") + datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-" + uuid.uuid4().hex[:8]
        target = folder / (name + ".tar")
        command = self.command(["exec", cid, "tar", "-C", "/workspace", "-cf", "-", "--", relative or "."])
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                                   env=self.environment, start_new_session=True)
        size, deadline = 0, time.monotonic() + 120
        try:
            with target.open("xb") as output, selectors.DefaultSelector() as selector:
                os.chmod(target, 0o600)
                os.set_blocking(process.stdout.fileno(), False)
                selector.register(process.stdout, selectors.EVENT_READ)
                while selector.get_map():
                    if time.monotonic() > deadline:
                        raise RuntimeError("snapshot timeout")
                    for key, _ in selector.select(0.2):
                        chunk = os.read(key.fd, 65_536)
                        if not chunk:
                            selector.unregister(key.fileobj)
                            break
                        size += len(chunk)
                        if size > self.settings["archive_limit_bytes"]:
                            raise RuntimeError("snapshot archive limit exceeded")
                        output.write(chunk)
            if process.wait(timeout=5):
                raise RuntimeError("snapshot failed; workspace was not changed")
            members = archive_members(target, self.settings["archive_limit_bytes"])
            with target.open("rb") as stream:
                digest = hashlib.file_digest(stream, "sha256").hexdigest()
            atomic_json(target.with_suffix(".json"), {"sha256": digest, "bytes": size,
                                                     "workspace_path": relative or ".", **members})
            return target
        except BaseException:
            if process.poll() is None:
                os.killpg(process.pid, signal.SIGKILL)
            process.wait()
            target.unlink(missing_ok=True)
            raise
        finally:
            process.stdout.close()

    def restore_bytes(self, path, cid):
        path = Path(path).resolve(strict=True)
        archive_members(path, self.settings["archive_limit_bytes"])
        if path.with_suffix(".json").is_file():
            expected = json.loads(path.with_suffix(".json").read_text())["sha256"]
            with path.open("rb") as stream:
                if hashlib.file_digest(stream, "sha256").hexdigest() != expected:
                    raise ValueError("snapshot hash mismatch")
        with path.open("rb") as stream:
            result = subprocess.run(self.command(["exec", "--interactive", cid, "tar", "-C", "/workspace",
                                                 "--no-same-owner", "--no-same-permissions", "-xf", "-"]),
                                    stdin=stream, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE,
                                    env=self.environment, timeout=120)
        if result.returncode:
            raise RuntimeError("archive import failed: " + result.stderr.decode(errors="replace")[:1000])

    def up(self, *, fresh=False):
        old = self.cid(current=False, required=False)
        restore = None
        if old:
            labels = json.loads(self.control(["container", "inspect", old]))[0]["Config"]["Labels"]
            image = self.render()["services"]["sandbox"]["image"]
            expected_image = json.loads(self.control(["image", "inspect", image]))[0]["Id"]
            actual_image = json.loads(self.control(["container", "inspect", old]))[0]["Image"]
            if labels.get(CONFIG) == fingerprint(self.settings) and actual_image == expected_image and not fresh:
                return {"status": "RUNNING", "container": self.cid(), "restored": None}
            restore = self.snapshot(cid=old, name="before-up")
        elif (self.state / "session.json").is_file():
            restore = json.loads((self.state / "session.json").read_text()).get("restore_on_up")
        if restore:
            self.save_session(restore)
        args = ["up", "--detach", "--no-build", "--pull", "never", "--remove-orphans"]
        if old or fresh:
            args.append("--force-recreate")
        self.control(self.compose(args), timeout=60)
        cid = self.cid()
        if restore and not fresh:
            try:
                self.restore_bytes(restore, cid)
            except BaseException:
                self.control(["container", "kill", cid], timeout=15)
                raise
        keep = {self.project + "_internal"} if self.settings["network"] != "none" else set()
        if self.settings["network"] == "allowlist":
            keep.add(self.project + "_egress")
        removed_networks = self.cleanup_networks(keep)
        self.save_session()
        return {"status": "RUNNING", "container": cid, "restored": str(restore) if restore and not fresh else None,
                "backup": str(restore) if restore else None, "removed_unused_networks": removed_networks}

    def import_source(self, source):
        cid = self.cid()
        descriptor, path = tempfile.mkstemp(prefix="import-", suffix=".tar", dir=self.state)
        os.close(descriptor)
        try:
            report = make_archive(source, Path(path), self.settings["archive_limit_bytes"])
            backup = self.snapshot(cid=cid, name="before-import")
            try:
                self.restore_bytes(path, cid)
            except BaseException:
                self.clear_workspace(cid)
                self.restore_bytes(backup, cid)
                raise
            return {"status": "IMPORTED", "backup": str(backup), **report}
        finally:
            os.unlink(path)

    def restore(self, path):
        cid = self.cid()
        # Validate first, then preserve a recoverable copy before replacing files.
        archive_members(Path(path), self.settings["archive_limit_bytes"])
        backup = self.snapshot(cid=cid, name="before-restore")
        self.clear_workspace(cid)
        try:
            self.restore_bytes(path, cid)
        except BaseException:
            self.clear_workspace(cid)
            self.restore_bytes(backup, cid)
            raise
        return {"status": "RESTORED", "backup": str(backup)}

    def clear_workspace(self, cid):
        cleanup = "import pathlib,shutil; p=pathlib.Path('/workspace'); [(x.unlink() if x.is_symlink() or x.is_file() else shutil.rmtree(x)) for x in p.iterdir()]"
        self.control(["exec", cid, "python", "-c", cleanup])

    def stop(self, *, force=False, reset=False):
        cid = self.cid(current=False, required=False)
        backup = None
        if cid:
            try:
                backup = self.snapshot(cid=cid, name="before-reset" if reset else "before-stop")
            except (RuntimeError, ValueError):
                if not force:
                    raise
        self.control(self.compose(["down", "--timeout", "5", "--remove-orphans"]), timeout=30)
        removed_networks = self.cleanup_networks()
        recovery = backup
        if not cid and (self.state / "session.json").is_file():
            recovery = json.loads((self.state / "session.json").read_text()).get("restore_on_up")
        self.save_session(None if reset else recovery)
        result = {"status": "STOPPED", "backup": str(backup) if backup else None,
                  "recovery_snapshot": str(recovery) if recovery and not reset else None,
                  "removed_unused_networks": removed_networks,
                  "working_copy_discarded_without_backup": bool(cid and not backup)}
        if reset:
            result["new_environment"] = self.up(fresh=True)
        return result

    def run(self, arguments, *, timeout=None):
        if not arguments or any(type(arg) is not str or "\x00" in arg for arg in arguments):
            raise ValueError("provide a command after --")
        cid = self.cid()
        timeout = self.settings["timeout_seconds"] if timeout is None else timeout
        if type(timeout) is not int or not 1 <= timeout <= 86400:
            raise ValueError("timeout must be 1..86400 seconds")
        backup = self.snapshot(cid=cid, name="before-run")
        self.save_session(backup)
        image_id = json.loads(self.control(["container", "inspect", cid]))[0]["Image"]
        folder = self.root / "artifacts" / (datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-" + uuid.uuid4().hex[:8])
        folder.mkdir(mode=0o700, parents=True)
        command = self.command(["exec", "--workdir", "/workspace", cid, "timeout", "--signal=TERM",
                                "--kill-after=5s", str(timeout) + "s"] + arguments)
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   env=self.environment, start_new_session=True)
        counts = {"stdout": 0, "stderr": 0}
        started, deadline, status = time.monotonic(), time.monotonic() + timeout + 10, "FINISHED"
        code = None
        try:
            with (folder / "stdout.log").open("xb") as stdout, (folder / "stderr.log").open("xb") as stderr, selectors.DefaultSelector() as selector:
                for stream, name, output in ((process.stdout, "stdout", stdout), (process.stderr, "stderr", stderr)):
                    os.set_blocking(stream.fileno(), False)
                    selector.register(stream, selectors.EVENT_READ, (name, output))
                while selector.get_map():
                    if time.monotonic() > deadline:
                        status = "TIMEOUT"
                        break
                    for key, _ in selector.select(0.2):
                        chunk = os.read(key.fd, 16_384)
                        if not chunk:
                            selector.unregister(key.fileobj)
                            continue
                        name, output = key.data
                        capacity = self.settings["log_limit_bytes"] - sum(counts.values())
                        output.write(chunk[:capacity])
                        counts[name] += min(len(chunk), capacity)
                        if len(chunk) > capacity:
                            status = "OUTPUT_LIMIT"
                            break
                    if status != "FINISHED":
                        break
            if status == "FINISHED":
                code = process.wait(timeout=max(0.1, deadline - time.monotonic()))
                if code == 124:
                    status = "TIMEOUT"
                elif code == 137:
                    status = "RESOURCE_OR_SIGNAL"
        except KeyboardInterrupt:
            status = "CANCELLED"
        except Exception as exc:
            status = "EXECUTION_ERROR"
            error = str(exc)
        finally:
            if process.poll() is None:
                os.killpg(process.pid, signal.SIGKILL)
            process.wait()
            process.stdout.close()
            process.stderr.close()
            stopped = False
            cleanup_error = None
            if status != "FINISHED":
                # Stop the whole owned environment so detached job children also stop.
                try:
                    self.control(["container", "kill", cid], timeout=15)
                    stopped = True
                except (RuntimeError, OSError, subprocess.TimeoutExpired) as exc:
                    try:
                        stopped = json.loads(self.control(["container", "inspect", cid]))[0]["State"]["Running"] is False
                    except (RuntimeError, OSError, ValueError, KeyError):
                        pass
                    if not stopped:
                        cleanup_error = str(exc)
                self.save_session(backup)
            report = {"status": status, "exit_code": code, "command": arguments,
                      "elapsed_seconds": round(time.monotonic() - started, 3),
                      "limits": self.settings, "logs": str(folder), "bytes": counts,
                      "image_id": image_id,
                      "recovery_snapshot": str(backup),
                      "environment_stopped": stopped, "cleanup_error": cleanup_error}
            for name in ("stdout", "stderr"):
                with (folder / (name + ".log")).open("rb") as stream:
                    stream.seek(max(0, counts[name] - 32_768))
                    report[name + "_tail"] = stream.read(32_768).decode("utf-8", errors="replace")
            if status == "EXECUTION_ERROR":
                report["error"] = error
            atomic_json(folder / "run.json", report)
        return report

    def kill(self):
        cid = self.cid(current=False)
        self.control(["container", "kill", cid], timeout=15)
        recovery = None
        if (self.state / "session.json").is_file():
            recovery = json.loads((self.state / "session.json").read_text()).get("restore_on_up")
        return {"status": "KILLED", "recovery_snapshot": recovery,
                "working_copy_discarded": True}


def main(argv=None):
    parser = argparse.ArgumentParser(description="Generic Python/Linux sandbox environment")
    commands = parser.add_subparsers(dest="action", required=True)
    for name in ("doctor", "render", "build", "status", "shell", "kill", "network-log", "validate"):
        commands.add_parser(name)
    start = commands.add_parser("up")
    start.add_argument("--fresh", action="store_true")
    run = commands.add_parser("run")
    run.add_argument("--timeout", type=int)
    run.add_argument("command", nargs=argparse.REMAINDER)
    source = commands.add_parser("import")
    source.add_argument("source")
    snapshot = commands.add_parser("snapshot")
    snapshot.add_argument("--name")
    export = commands.add_parser("export")
    export.add_argument("path", help="Specific relative path inside /workspace")
    export.add_argument("--name")
    restore = commands.add_parser("restore")
    restore.add_argument("snapshot")
    for name in ("stop", "reset"):
        stop = commands.add_parser(name)
        stop.add_argument("--force", action="store_true", help="Discard working copy even if a backup cannot be made")
    config = commands.add_parser("config")
    config.add_argument("--cpus", type=float)
    config.add_argument("--memory")
    config.add_argument("--workspace-size")
    config.add_argument("--tmp-size")
    config.add_argument("--pids", type=int)
    config.add_argument("--timeout", type=int)
    config.add_argument("--log-limit", type=int, help="Combined stdout/stderr byte limit")
    config.add_argument("--archive-limit", type=int, help="Import/export/snapshot byte limit")
    config.add_argument("--network", choices=("none", "internal", "allowlist"))
    config.add_argument("--allow-host", action="append")
    config.add_argument("--runtime", choices=("runc", "runsc"))
    config.add_argument("--gpu", action=argparse.BooleanOptionalAction, default=None)
    config.add_argument("--gpu-id", action="append")
    config.add_argument("--llm", action=argparse.BooleanOptionalAction, default=None)
    args = parser.parse_args(argv)
    runtime = Runtime()
    if args.action == "render":
        print(json.dumps(runtime.render(), indent=2, ensure_ascii=False))
        return 0
    if args.action == "doctor":
        try:
            info = json.loads(runtime.control(["info", "--format", "{{json .}}"], timeout=10))
            compose = runtime.control(["compose", "version", "--short"], timeout=10).decode().strip()
            ready = (info.get("OSType") == "linux" and runtime.settings["runtime"] in info.get("Runtimes", {})
                     and all(info.get(v) is True for v in ("MemoryLimit", "SwapLimit", "PidsLimit")))
            report = {"status": "READY" if ready else "UNAVAILABLE",
                      "docker_version": info.get("ServerVersion"), "compose_version": compose,
                      "runtime": runtime.settings["runtime"], "isolation_verified": False}
        except (RuntimeError, OSError, subprocess.TimeoutExpired, ValueError) as exc:
            report = {"status": "UNAVAILABLE", "reason": str(exc), "isolation_verified": False}
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return 0 if report["status"] == "READY" else 2
    if args.action == "kill":
        # Emergency stop remains available while a run holds the operation lock.
        print(json.dumps(runtime.kill(), indent=2, ensure_ascii=False))
        return 0
    with runtime.lock():
        if args.action == "config":
            changed = False
            mapping = {"cpus": "cpus", "memory": "memory", "workspace_size": "workspace_size",
                       "tmp_size": "tmp_size", "pids": "pids", "timeout": "timeout_seconds",
                       "log_limit": "log_limit_bytes", "archive_limit": "archive_limit_bytes",
                       "network": "network", "allow_host": "allowed_hosts", "runtime": "runtime",
                       "gpu": "gpu", "gpu_id": "gpu_ids", "llm": "llm_packages"}
            for argument, key in mapping.items():
                if getattr(args, argument) is not None:
                    runtime.settings[key] = getattr(args, argument)
                    changed = True
            validate_settings(runtime.settings)
            if changed:
                atomic_json(runtime.root / "settings.json", runtime.settings)
            result = runtime.settings
        elif args.action == "build":
            return subprocess.call(runtime.command(runtime.compose(["build", "sandbox"])), env=runtime.environment)
        elif args.action == "validate":
            runtime.control(runtime.compose(["config", "--quiet"]))
            result = {"status": "CONFIG_VALID"}
        elif args.action == "up":
            result = runtime.up(fresh=args.fresh)
        elif args.action == "status":
            cid = runtime.cid(current=False, required=False)
            result = {"status": "RUNNING" if cid else "STOPPED", "container": cid}
            if cid:
                result["resources"] = json.loads(runtime.control(["stats", "--no-stream", "--format", "{{json .}}", cid]))
                result["disk"] = runtime.control(["exec", cid, "df", "-h", "/workspace", "/tmp"]).decode()
        elif args.action == "network-log":
            if runtime.settings["network"] != "allowlist":
                result = {"status": "NOT_ENABLED"}
            else:
                result = {"log": runtime.control(runtime.compose(["logs", "--no-color", "--tail", "200", "proxy"])).decode()}
        elif args.action == "shell":
            cid = runtime.cid()
            return subprocess.call(runtime.command(["exec", "--interactive", "--tty", "--workdir", "/workspace", cid, "bash"]), env=runtime.environment)
        elif args.action == "run":
            command = args.command[1:] if args.command[:1] == ["--"] else args.command
            result = runtime.run(command, timeout=args.timeout)
            print(json.dumps(result, indent=2, ensure_ascii=False))
            return 0 if result["status"] == "FINISHED" and result["exit_code"] == 0 else 2
        elif args.action == "import":
            result = runtime.import_source(args.source)
        elif args.action == "snapshot":
            result = {"snapshot": str(runtime.snapshot(name=args.name))}
        elif args.action == "export":
            result = {"archive": str(runtime.snapshot(name=args.name, relative=args.path)),
                      "workspace_path": args.path}
        elif args.action == "restore":
            result = runtime.restore(args.snapshot)
        else:
            result = runtime.stop(force=args.force, reset=args.action == "reset")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (RuntimeError, ValueError, OSError, tarfile.TarError, subprocess.TimeoutExpired, KeyboardInterrupt) as exc:
        print(json.dumps({"status": "ERROR", "reason": str(exc)}, ensure_ascii=False), file=sys.stderr)
        raise SystemExit(2)

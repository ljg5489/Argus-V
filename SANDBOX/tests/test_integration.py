"""Real Docker tests, opt-in. Each test owns a separate Compose project."""

import importlib.util
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("generic_integration", ROOT / "sandbox.py")
sandbox = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sandbox)


@unittest.skipUnless(os.environ.get("SANDBOX_INTEGRATION_TESTS") == "1", "Real Docker integration not enabled")
class IntegrationTests(unittest.TestCase):
    def setUp(self):
        (ROOT / ".state").mkdir(mode=0o700, exist_ok=True)
        self.folder = tempfile.TemporaryDirectory(prefix="integration-", dir=ROOT / ".state")
        self.root = Path(self.folder.name)
        (self.root / "settings.json").write_text((ROOT / "settings.json").read_text())
        (self.root / "models").mkdir()
        self.runtime = sandbox.Runtime(self.root)
        base = sandbox.Runtime(ROOT)
        base.check_docker()
        self.runtime.endpoint = base.endpoint
        self.runtime.environment = base.environment
        self.addCleanup(self.folder.cleanup)
        self.addCleanup(self.clean_environment)
        self.runtime.up(fresh=True)  # Requires the locally prepared image. Never pulls/builds.

    def clean_environment(self):
        try:
            self.runtime.stop(force=True)
        except Exception:
            # An unavailable cleanup is a test failure, not silently ignored.
            self.fail("integration container cleanup failed")

    def test_arbitrary_script_and_child_process_execution(self):
        self.runtime.import_source(ROOT / "examples")
        report = self.runtime.run(["python", "hello.py"])
        self.assertEqual(report["status"], "FINISHED")
        self.assertEqual(report["exit_code"], 0)
        output = json.loads((Path(report["logs"]) / "stdout.log").read_text())
        self.assertEqual(output["python_child"], "42")
        self.assertEqual(output["uid"], 10001)

    def test_snapshot_restore_and_reset(self):
        cid = self.runtime.cid()
        self.runtime.control(["exec", cid, "bash", "-lc", "printf original > /workspace/value"])
        saved = self.runtime.snapshot()
        self.runtime.control(["exec", cid, "bash", "-lc", "printf changed > /workspace/value"])
        self.runtime.restore(saved)
        self.assertEqual(self.runtime.control(["exec", cid, "cat", "/workspace/value"]), b"original")
        reset = self.runtime.stop(reset=True)
        self.assertIsNotNone(reset["backup"])
        cid = self.runtime.cid()
        self.runtime.control(["exec", cid, "test", "!", "-e", "/workspace/value"])

    def test_timeout_stops_entire_environment_and_preserves_checkpoint(self):
        report = self.runtime.run(["python", "-c", "import time; time.sleep(20)"], timeout=1)
        self.assertEqual(report["status"], "TIMEOUT")
        self.assertTrue(report["environment_stopped"])
        self.assertTrue(Path(report["recovery_snapshot"]).is_file())
        self.assertIsNone(report["cleanup_error"])
        self.runtime.stop()
        self.runtime.stop()
        restarted = self.runtime.up()
        self.assertEqual(restarted["restored"], report["recovery_snapshot"])

    def test_readonly_root_network_and_workspace_quota(self):
        source = "import os,socket; print(os.getuid()); s=socket.socket(); s.settimeout(.2); s.connect(('203.0.113.1',80))"
        report = self.runtime.run(["python", "-c", source])
        self.assertNotEqual(report["exit_code"], 0)
        cid = self.runtime.cid()
        result = self.runtime.run(["bash", "-lc", "touch /opt/should-fail"])
        self.assertNotEqual(result["exit_code"], 0)
        self.assertEqual(self.runtime.control(["exec", cid, "stat", "-f", "--format=%T", "/workspace"]).strip(), b"tmpfs")
        policy = self.runtime.control(["exec", cid, "cat", "/proc/self/status"]).decode()
        self.assertIn("CapEff:\t0000000000000000", policy)
        self.assertIn("NoNewPrivs:\t1", policy)
        self.assertIn("Seccomp:\t2", policy)

    def test_export_and_import_overwrite_have_recoverable_backups(self):
        first = self.runtime.import_source(ROOT / "examples")
        self.assertTrue(Path(first["backup"]).is_file())
        archive = self.runtime.snapshot(relative="hello.py", name="exported")
        self.assertTrue(archive.is_file())
        with sandbox.tarfile.open(archive) as saved:
            self.assertEqual(saved.getnames(), ["hello.py"])
        with self.assertRaises(ValueError):
            self.runtime.snapshot(relative="../outside")

    def test_failed_restore_removes_partial_files_before_rollback(self):
        cid = self.runtime.cid()
        self.runtime.control(["exec", cid, "bash", "-lc", "printf kept > /workspace/value"])
        saved = self.runtime.snapshot()
        original = self.runtime.restore_bytes
        calls = []

        def partial_failure(path, identity):
            calls.append(path)
            if len(calls) == 1:
                self.runtime.control(["exec", identity, "touch", "/workspace/partial-file"])
                raise RuntimeError("simulated interrupted extraction")
            return original(path, identity)

        with patch.object(self.runtime, "restore_bytes", side_effect=partial_failure):
            with self.assertRaises(RuntimeError):
                self.runtime.restore(saved)
        self.assertEqual(self.runtime.control(["exec", cid, "cat", "/workspace/value"]), b"kept")
        self.runtime.control(["exec", cid, "test", "!", "-e", "/workspace/partial-file"])

    def test_output_limit_stops_whole_environment(self):
        self.runtime.settings["log_limit_bytes"] = 4096
        self.runtime.up()
        report = self.runtime.run(["python", "-c", "import os; os.write(1, b'x' * 100000)"])
        self.assertEqual(report["status"], "OUTPUT_LIMIT")
        self.assertEqual(sum(report["bytes"].values()), 4096)
        self.assertTrue(report["environment_stopped"])

    def test_kernel_resource_limits_and_workspace_capacity(self):
        self.runtime.settings.update(memory="512m", workspace_size="32m", tmp_size="16m", pids=32, cpus=0.5)
        self.runtime.up()
        limits = self.runtime.run(["python", "-c", "import json,pathlib; p=pathlib.Path('/sys/fs/cgroup'); print(json.dumps({k:(p/k).read_text().strip() for k in ('memory.max','memory.swap.max','pids.max','cpu.max')}))"])
        self.assertEqual(limits["exit_code"], 0)
        actual = json.loads(limits["stdout_tail"])
        self.assertEqual(actual["memory.max"], str(512 * 1024**2))
        self.assertEqual(actual["memory.swap.max"], "0")
        self.assertEqual(actual["pids.max"], "32")
        quota, period = (int(v) for v in actual["cpu.max"].split())
        self.assertEqual(quota / period, 0.5)
        source = "import errno,os; p='/workspace/quota'; f=open(p,'wb'); failed=False\ntry:\n for _ in range(40): f.write(b'x'*1024**2); f.flush()\nexcept OSError as e: failed=e.errno==errno.ENOSPC\nfinally: f.close(); os.unlink(p)\nassert failed, 'workspace was not bounded'\nprint('ENOSPC enforced')"
        result = self.runtime.run(["python", "-c", source])
        self.assertEqual(result["exit_code"], 0, result["stderr_tail"])

    def test_process_limit_is_enforced_without_forking_on_host(self):
        self.runtime.settings["pids"] = 32
        self.runtime.up()
        source = "import errno,subprocess; children=[]; bounded=False\ntry:\n for _ in range(80): children.append(subprocess.Popen(['sleep','20']))\nexcept OSError as e: bounded=e.errno==errno.EAGAIN\nfinally:\n for p in children: p.terminate()\n for p in children: p.wait()\nassert bounded, 'process quota was not enforced'\nprint('process quota enforced')"
        report = self.runtime.run(["python", "-c", source])
        self.assertEqual(report["exit_code"], 0, report["stderr_tail"])

    def test_memory_exhaustion_is_contained_and_recoverable(self):
        self.runtime.settings.update(memory="256m", workspace_size="16m", tmp_size="8m")
        self.runtime.up()
        report = self.runtime.run(["python", "-c", "chunks=[]\nfor _ in range(128): chunks.append(bytearray(8*1024**2))"], timeout=15)
        self.assertEqual(report["status"], "RESOURCE_OR_SIGNAL")
        self.assertEqual(report["exit_code"], 137)
        self.assertTrue(report["environment_stopped"])
        self.assertTrue(Path(report["recovery_snapshot"]).is_file())

    def test_allowlist_proxy_blocks_unlisted_hosts_direct_connections_and_external_dns(self):
        self.runtime.settings.update(network="allowlist", allowed_hosts=["example.com"])
        self.runtime.up()
        allowed = self.runtime.run(["curl", "--fail", "--silent", "--show-error", "--max-time", "15", "https://example.com"])
        self.assertEqual(allowed["exit_code"], 0, allowed["stderr_tail"])
        denied = self.runtime.run(["curl", "--fail", "--silent", "--show-error", "--max-time", "5", "https://www.iana.org"])
        self.assertNotEqual(denied["exit_code"], 0)
        direct = self.runtime.run(["curl", "--noproxy", "*", "--max-time", "2", "http://1.1.1.1"])
        self.assertNotEqual(direct["exit_code"], 0)
        dns = self.runtime.run(["python", "-c", "import socket; socket.getaddrinfo('example.com',443)"])
        self.assertNotEqual(dns["exit_code"], 0)
        logs = self.runtime.control(self.runtime.compose(["logs", "--no-color", "--tail", "100", "proxy"])).decode()
        self.assertIn('"outcome": "ALLOW"', logs)
        self.assertIn('"outcome": "DENY"', logs)
        self.runtime.settings.update(network="internal", allowed_hosts=[])
        self.runtime.up()
        proxy = self.runtime.control(["ps", "--all", "--quiet", "--filter",
                                      "label=com.docker.compose.project=" + self.runtime.project,
                                      "--filter", "label=com.docker.compose.service=proxy"])
        self.assertEqual(proxy.strip(), b"")
        networks = self.runtime.control(["network", "ls", "--format", "{{.Name}}", "--filter",
                                         "label=com.docker.compose.project=" + self.runtime.project]).decode().split()
        self.assertEqual(networks, [self.runtime.project + "_internal"])
        internal = self.runtime.run(["curl", "--max-time", "2", "http://1.1.1.1"])
        self.assertNotEqual(internal["exit_code"], 0)


if __name__ == "__main__":
    unittest.main()

import copy
import base64
import contextlib
import importlib.util
import io
import json
import sys
from pathlib import Path
import tarfile
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("generic_sandbox", ROOT / "sandbox.py")
sandbox = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sandbox)
proxy_spec = importlib.util.spec_from_file_location("generic_proxy", ROOT / "proxy.py")
proxy = importlib.util.module_from_spec(proxy_spec)
proxy_spec.loader.exec_module(proxy)


def settings():
    return json.loads((ROOT / "settings.json").read_text())


class ConfigurationTests(unittest.TestCase):
    def test_zero_timeout_override_is_not_silently_replaced(self):
        runtime = sandbox.Runtime(ROOT)
        with patch.object(runtime, "cid", return_value="test-container"):
            with self.assertRaises(ValueError):
                runtime.run(["python", "hello.py"], timeout=0)

    def test_generic_environment_has_no_function_or_scenario_contract(self):
        spec = sandbox.compose_spec(settings(), "owner")
        service = spec["services"]["sandbox"]
        self.assertEqual(service["command"], ["sleep", "infinity"])
        self.assertEqual(service["network_mode"], "none")
        self.assertTrue(service["read_only"])
        self.assertEqual(service["cap_drop"], ["ALL"])
        self.assertEqual(service["volumes"][0]["target"], "/models")
        self.assertTrue(service["volumes"][0]["read_only"])
        self.assertNotIn("build_request", json.dumps(spec))

    def test_internal_mode_has_no_egress_network_or_proxy(self):
        value = settings()
        value["network"] = "internal"
        spec = sandbox.compose_spec(value, "owner")
        self.assertNotIn("network_mode", spec["services"]["sandbox"])
        self.assertTrue(spec["networks"]["internal"]["internal"])
        self.assertEqual(spec["networks"]["internal"]["labels"][sandbox.OWNER], "owner")
        self.assertNotIn("proxy", spec["services"])

    def test_allowlist_worker_only_joins_internal_network(self):
        value = settings()
        value.update(network="allowlist", allowed_hosts=["example.com"])
        spec = sandbox.compose_spec(value, "owner")
        self.assertEqual(spec["services"]["sandbox"]["networks"], ["internal"])
        self.assertEqual(spec["services"]["sandbox"]["dns"], ["127.0.0.1"])
        self.assertEqual(spec["services"]["proxy"]["networks"], ["internal", "egress"])
        self.assertFalse(any("ports" in v for v in spec["services"].values()))
        self.assertEqual(spec["services"]["proxy"]["environment"]["ALLOWED_HOSTS"], "example.com")

    def test_gpu_is_explicit_and_selects_specific_devices(self):
        self.assertNotIn("deploy", sandbox.compose_spec(settings(), "owner")["services"]["sandbox"])
        value = settings()
        value.update(gpu=True, gpu_ids=["1"])
        device = sandbox.compose_spec(value, "owner")["services"]["sandbox"]["deploy"]["resources"]["reservations"]["devices"][0]
        self.assertEqual(device["device_ids"], ["1"])
        self.assertEqual(device["capabilities"], ["gpu"])

    def test_configuration_rejects_invalid_or_unbounded_options(self):
        changes = [{"cpus": float("nan")}, {"memory": "0g"}, {"memory": "128m"},
                   {"workspace_size": "16g"}, {"network": "host"},
                   {"network": "allowlist"}, {"allowed_hosts": ["https://example.com"]},
                   {"runtime": "arbitrary"}, {"gpu": True, "runtime": "runsc"},
                   {"pids": True}, {"timeout_seconds": 0}]
        for change in changes:
            value = settings()
            value.update(change)
            with self.subTest(change=change), self.assertRaises(ValueError):
                sandbox.validate_settings(value)


class FileListingTests(unittest.TestCase):
    def preview(self, root, path):
        runtime = sandbox.Runtime(ROOT)

        def control(args, **kwargs):
            output = io.StringIO()
            with contextlib.redirect_stdout(output), patch("sys.argv", ["preview", args[5]]):
                try:
                    exec(args[4].replace("root = '/workspace'", f"root = {str(root)!r}"), {})
                except SystemExit as error:
                    self.assertEqual(error.code, 0)
            return output.getvalue().encode()

        with patch.object(runtime, "cid", return_value="test-container"), \
                patch.object(runtime, "control", side_effect=control):
            return runtime.read_file(path)

    def test_preview_image_metadata_has_no_size_limit(self):
        png = base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+aX1sAAAAASUVORK5CYII=')
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            for data, mime in [(png, 'image/png'), (b'\xff\xd8\xff' + b'x' * 70000, 'image/jpeg'),
                               (b'GIF89a', 'image/gif'), (b'RIFF0000WEBP', 'image/webp'),
                               (b'BM0000', 'image/bmp'), (b'\x00\x00\x01\x00', 'image/x-icon'),
                               (b'0000ftypavif', 'image/avif')]:
                with self.subTest(mime=mime):
                    (root / 'image').write_bytes(data)
                    result = self.preview(root, '/workspace/image')
                    self.assertEqual(result['mime'], mime)
                    self.assertEqual(result['size'], len(data))
                    self.assertNotIn('image_base64', result)
                    self.assertFalse(result['truncated'])
            (root / 'large.png').write_bytes(png + b'x' * (10 * 1024 * 1024))
            result = self.preview(root, '/workspace/large.png')
            self.assertFalse(result['truncated'])
            self.assertEqual(result['size'], len(png) + 10 * 1024 * 1024)

    def test_image_stream_preserves_large_file_and_rejects_non_images(self):
        runtime = sandbox.Runtime(ROOT)
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            data = b'\x89PNG\r\n\x1a\n' + b'x' * (11 * 1024 * 1024)
            (root / 'image.png').write_bytes(data)
            (root / 'text.txt').write_text('hello')
            (root / 'link.png').symlink_to(root / 'image.png')

            def command(args):
                script = args[4].replace("root = '/workspace'", f"root = {folder!r}")
                return [sys.executable, '-c', script, *args[5:]]

            with patch.object(runtime, 'cid', return_value='test-container'), \
                    patch.object(runtime, 'command', side_effect=command):
                with tempfile.TemporaryFile() as output:
                    runtime.read_file('/workspace/image.png', image_output=output)
                    output.seek(0)
                    self.assertEqual(output.readline(), b'image/png\n')
                    self.assertEqual(output.read(), data)
                for path in ('text.txt', 'link.png', 'missing.png'):
                    with self.subTest(path=path), tempfile.TemporaryFile() as output:
                        with self.assertRaises(RuntimeError):
                            runtime.read_file('/workspace/' + path, image_output=output)

    def test_preview_text_binary_empty_and_truncated_utf8(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            for data, content, binary, truncated in [
                ("한글 <script> &\n".encode(), "한글 <script> &\n", False, False),
                (b"", "", False, False),
                (b"abc\x00", "", True, False),
                (b"\xff", "", True, False),
                (b"a" * 65535 + "한".encode(), "a" * 65535, False, True),
            ]:
                with self.subTest(data_length=len(data)):
                    (root / "file.txt").write_bytes(data)
                    result = self.preview(root, "/workspace/file.txt")
                    self.assertEqual(result["content"], content)
                    self.assertEqual(result["binary"], binary)
                    self.assertEqual(result["truncated"], truncated)
                    self.assertEqual(result["size"], len(data))

    def test_preview_rejects_escape_paths_links_and_directories(self):
        runtime = sandbox.Runtime(ROOT)
        for path in ("/etc/passwd", "/workspace/../etc/passwd", "/workspace/", "/workspace/a\x00"):
            with self.subTest(path=path), self.assertRaises(ValueError):
                runtime.read_file(path)
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "folder").mkdir()
            (root / "file.txt").write_text("hello")
            (root / "link").symlink_to(root / "file.txt")
            (root / "dirlink").symlink_to(root, target_is_directory=True)
            for path in ("folder", "link", "dirlink/file.txt", "missing"):
                with self.subTest(path=path), self.assertRaises((OSError, ValueError)):
                    self.preview(root, "/workspace/" + path)

    def test_stopped_sandbox_has_no_entries(self):
        runtime = sandbox.Runtime(ROOT)
        with patch.object(runtime, "cid", return_value=None):
            self.assertEqual(runtime.list_files(), {
                "status": "STOPPED", "root": "/workspace", "entries": []})

    def test_listing_includes_nested_and_hidden_files_without_following_links(self):
        runtime = sandbox.Runtime(ROOT)
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "nested").mkdir()
            (root / "nested" / "한글.txt").write_bytes(b"abc")
            (root / ".hidden").write_bytes(b"x")
            (root / "link").symlink_to(root / "nested", target_is_directory=True)

            def control(args, **kwargs):
                self.assertEqual(args[:4], ["exec", "test-container", "python3", "-c"])
                output = io.StringIO()
                with contextlib.redirect_stdout(output):
                    exec(args[4].replace("root = '/workspace'", f"root = {folder!r}"), {})
                return output.getvalue().encode()

            with patch.object(runtime, "cid", return_value="test-container"), \
                    patch.object(runtime, "control", side_effect=control):
                result = runtime.list_files()
            entries = {Path(item["path"]).relative_to(root).as_posix(): item
                       for item in result["entries"]}
            self.assertEqual(set(entries), {"nested", "nested/한글.txt", ".hidden", "link"})
            self.assertEqual(entries["nested/한글.txt"]["size"], 3)
            self.assertEqual(entries["link"]["kind"], "symlink")
            self.assertFalse(result["truncated"])


class ArchiveTests(unittest.TestCase):
    def test_import_preserves_original_and_excludes_secret_metadata(self):
        with tempfile.TemporaryDirectory(prefix="generic-sandbox-test-") as folder:
            root = Path(folder)
            project = root / "project"
            project.mkdir()
            (project / "hello.py").write_text("print('hello')")
            (project / ".env").write_text("NOT_A_REAL_SECRET=sample")
            (project / ".git").mkdir()
            (project / ".git/config").write_text("sample")
            (project / ".state").mkdir()
            (project / ".state/agent.json").write_text('"controller-only"')
            archive = root / "project.tar"
            report = sandbox.make_archive(project, archive, 1024 * 1024)
            self.assertIn(".env", report["excluded"])
            self.assertIn(".state", report["excluded"])
            with tarfile.open(archive) as tar:
                self.assertEqual(tar.getnames(), ["hello.py"])
            self.assertEqual((project / "hello.py").read_text(), "print('hello')")

    def test_rejects_escape_paths_links_and_special_files(self):
        for name, kind in (("../escape", tarfile.REGTYPE), ("/absolute", tarfile.REGTYPE),
                           ("link", tarfile.SYMTYPE), ("hard", tarfile.LNKTYPE),
                           ("pipe", tarfile.FIFOTYPE), ("device", tarfile.CHRTYPE)):
            with tempfile.TemporaryDirectory(prefix="generic-sandbox-test-") as folder:
                path = Path(folder) / "bad.tar"
                with tarfile.open(path, "w") as archive:
                    entry = tarfile.TarInfo(name)
                    entry.type = kind
                    entry.linkname = "/etc/passwd"
                    archive.addfile(entry)
                with self.subTest(name=name, kind=kind), self.assertRaises(ValueError):
                    sandbox.archive_members(path, 1024 * 1024)

    def test_source_symlink_is_not_followed(self):
        with tempfile.TemporaryDirectory(prefix="generic-sandbox-test-") as folder:
            root = Path(folder)
            project = root / "project"
            project.mkdir()
            (root / "outside").write_text("outside")
            (project / "linked").symlink_to(root / "outside")
            with self.assertRaises(ValueError):
                sandbox.make_archive(project, root / "archive.tar", 1024 * 1024)

    def test_archive_quota_enforced(self):
        with tempfile.TemporaryDirectory(prefix="generic-sandbox-test-") as folder:
            root = Path(folder)
            source = root / "large"
            source.write_bytes(b"x" * 8192)
            with self.assertRaises(ValueError):
                sandbox.make_archive(source, root / "archive.tar", 4096)


class ProxyTests(unittest.TestCase):
    def test_unlisted_host_and_nonstandard_port_never_resolve(self):
        with patch.object(proxy, "ALLOWED", frozenset({"example.com"})), patch.object(
                proxy.socket, "getaddrinfo", side_effect=AssertionError("must not resolve")):
            for host, port in (("evil.invalid", 443), ("example.com", 22)):
                with self.assertRaises(PermissionError):
                    proxy.approved_address(host, port)

    def test_private_loopback_linklocal_and_mixed_dns_answers_rejected(self):
        with patch.object(proxy, "ALLOWED", frozenset({"example.com"})):
            for address in ("127.0.0.1", "10.0.0.1", "169.254.169.254", "::1"):
                answers = [(2, 1, 6, "", ("8.8.8.8", 443)), (2, 1, 6, "", (address, 443))]
                with patch.object(proxy.socket, "getaddrinfo", return_value=answers):
                    with self.assertRaises(PermissionError):
                        proxy.approved_address("example.com", 443)

    def test_connection_uses_validated_numeric_address(self):
        answers = [(2, 1, 6, "", ("8.8.8.8", 443))]
        with patch.object(proxy, "ALLOWED", frozenset({"example.com"})), patch.object(
                proxy.socket, "getaddrinfo", return_value=answers):
            self.assertEqual(proxy.approved_address("example.com", 443), "8.8.8.8")


if __name__ == "__main__":
    unittest.main()

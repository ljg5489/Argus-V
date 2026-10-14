import importlib.util
import json
import shutil
import socket
import ssl
import struct
import tempfile
import threading
import unittest
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("generic_sandbox_fakenet", ROOT / "sandbox.py")
sandbox = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sandbox)
server_spec = importlib.util.spec_from_file_location("fakenet_server", ROOT / "fakenet" / "server.py")
server = importlib.util.module_from_spec(server_spec)
server_spec.loader.exec_module(server)


def settings(**changes):
    value = json.loads((ROOT / "settings.json").read_text())
    value.update(changes)
    return value


def query(name, qtype, edns=True):
    labels = b"".join(bytes([len(part)]) + part.encode() for part in name.split(".")) + b"\0"
    additional = b"\0\0\x29\x04\xb0\0\0\0\0\0\0" if edns else b""
    return struct.pack("!HHHHHH", 0x1234, 0x0100, 1, 0, 0, 1 if edns else 0) + labels + struct.pack("!HH", qtype, 1) + additional


class ComposeTests(unittest.TestCase):
    def test_fakenet_mode_isolates_sandbox_behind_gateway(self):
        spec = sandbox.compose_spec(settings(network="fakenet"), "owner")
        worker, gateway = spec["services"]["sandbox"], spec["services"]["gateway"]
        self.assertEqual(spec["networks"]["lan"]["internal"], True)
        self.assertEqual(worker["networks"], ["lan"])
        self.assertEqual(worker["dns"], [sandbox.FAKENET_IP])
        self.assertNotIn("HTTP_PROXY", worker["environment"])
        self.assertEqual({v["target"] for v in worker["volumes"]}, {"/models", *sandbox.CA_BUNDLES})
        self.assertTrue(all(v["read_only"] for v in worker["volumes"]))
        self.assertEqual(gateway["networks"], {"lan": {"ipv4_address": sandbox.FAKENET_IP}})
        self.assertEqual(gateway["cap_drop"], ["ALL"])
        self.assertEqual(gateway["entrypoint"], sandbox.FAKENET_ENTRYPOINT)
        self.assertEqual([v["target"] for v in gateway["volumes"]], ["/opt/fakenet"])
        self.assertTrue(gateway["read_only"] and gateway["volumes"][0]["read_only"])
        self.assertNotIn("egress", spec["networks"])

    def test_other_modes_unchanged(self):
        for mode in ("none", "internal"):
            spec = sandbox.compose_spec(settings(network=mode), "owner")
            self.assertNotIn("gateway", spec["services"])
            self.assertEqual(spec["services"]["sandbox"]["dns"], ["127.0.0.1"])
            self.assertEqual(len(spec["services"]["sandbox"]["volumes"]), 1)

    def test_ca_is_created_once_and_readable_by_container_user(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            ca = sandbox.ensure_fakenet_ca(root)
            first = (ca / "ca.pem").read_bytes()
            self.assertIn(first.decode(), (ca / "bundle.pem").read_text())
            self.assertEqual((ca / "ca.key").stat().st_mode & 0o777, 0o644)
            sandbox.ensure_fakenet_ca(root)
            self.assertEqual((ca / "ca.pem").read_bytes(), first)


class DnsTests(unittest.TestCase):
    def test_every_a_query_resolves_to_gateway(self):
        reply, name, qtype = server.dns_answer(query("Pastebin.COM", 1), "10.254.77.53")
        self.assertEqual((name, qtype), ("pastebin.com", 1))
        ident, flags, qd, an = struct.unpack("!HHHH", reply[:8])
        self.assertEqual((ident, qd, an), (0x1234, 1, 1))
        self.assertEqual(flags & 0x8000, 0x8000)
        self.assertEqual(reply[-4:], socket.inet_aton("10.254.77.53"))

    def test_aaaa_gets_empty_answer(self):
        reply, _, qtype = server.dns_answer(query("example.org", 28), "10.254.77.53")
        self.assertEqual(qtype, 28)
        self.assertEqual(struct.unpack("!H", reply[6:8])[0], 0)


class RouteTests(unittest.TestCase):
    routes = server.load_routes(ROOT / "fakenet" / "routes.json")

    def test_shipped_routes(self):
        def status(host, method, path):
            return server.render(server.match_route(self.routes, host, method, path), host, path)[0]
        self.assertEqual(status("pypi.org", "GET", "/simple/requests/"), 404)
        self.assertEqual(status("pastebin.com", "POST", "/api/api_post.php"), 200)
        self.assertEqual(status("api.github.com", "GET", "/user"), 401)
        self.assertEqual(status("example.com", "GET", "/"), 200)
        self.assertEqual(status("example.com", "GET", "/nothing"), 404)
        _, headers, body = server.render(server.match_route(self.routes, "a.test", "GET", "/"), "a.test", "/")
        self.assertIn(b"NAVER", body)
        self.assertEqual(headers["Server"], "nginx")

    def test_simsimi_navigation(self):
        from html.parser import HTMLParser
        from urllib.parse import urljoin, urlsplit

        class Links(HTMLParser):
            def __init__(self):
                super().__init__()
                self.hrefs = []

            def handle_starttag(self, tag, attrs):
                if tag == "a":
                    self.hrefs.append(dict(attrs).get("href"))

        for path in ("/", "/search.naver", "/search/nested"):
            route = server.match_route(self.routes, "www.naver.com", "GET", path)
            _, _, home = server.render(route, "www.naver.com", path)
            links = Links()
            links.feed(home.decode())
            self.assertIn("/simsimi.html", links.hrefs)
            target = urlsplit(urljoin("https://www.naver.com" + path, "/simsimi.html")).path
            route = server.match_route(self.routes, "www.naver.com", "GET", target)
            status, headers, body = server.render(route, "www.naver.com", target)
            self.assertEqual(status, 200)
            self.assertIn("text/html", headers["Content-Type"])
            self.assertTrue(body.startswith(b"<!DOCTYPE html>"))
            self.assertIn(b'id="chat-form"', body)

    def test_simsimi_chat_api(self):
        route = server.match_route(self.routes, "www.naver.com", "POST", "/simsimi/api/chat")
        self.assertEqual(route.get("handler"), "simsimi")
        status, headers, body = server.render(route, "www.naver.com", "/simsimi/api/chat", "",
                                              json.dumps({"text": "안녕"}).encode())
        self.assertEqual((status, headers["Content-Type"]), (200, "application/json; charset=utf-8"))
        self.assertIn(json.loads(body)["reply"], server.SIMSIMI_BRAIN["안녕"])
        self.assertEqual(server.simsimi_api("/simsimi/api/chat", "", b"")[0], 400)
        self.assertEqual(server.simsimi_api("/simsimi/api/teach", "", b"question=password&answer=hunter2")[0], 200)
        self.assertEqual(server.simsimi_api("/simsimi/api/chat", "text=my+password", b"")[1]["reply"], "hunter2")
        self.assertEqual(server.simsimi_api("/simsimi/api/other", "", b"")[0], 404)
        home = server.match_route(self.routes, "simsimi.com", "GET", "/")
        self.assertEqual(home.get("file"), "simsimi.html")
        page = (ROOT / "fakenet" / "sites" / "simsimi.html").read_text()
        self.assertIn("/simsimi/api", page)  # the page calls the API, so its chat is logged

    def test_smtp_dialogue(self):
        state, replies = False, []
        for line in (b"EHLO x", b"MAIL FROM:<a@x>", b"DATA", b"secret", b".", b"QUIT"):
            reply, state = server.smtp_reply(line, state)
            replies.append(reply[:3])
        self.assertEqual(replies, [b"250", b"250", b"354", b"", b"250", b"221"])


class LiveServerTests(unittest.TestCase):
    """HTTP and HTTPS round trips on localhost; every request is logged with its body."""

    def setUp(self):
        self.events = []
        self.original_log = server.log
        server.log = lambda kind, **fields: self.events.append({"kind": kind, **fields})
        server.Web.routes = server.load_routes(ROOT / "fakenet" / "routes.json")
        self.folder = Path(tempfile.mkdtemp())
        self.servers = []

    def tearDown(self):
        server.log = self.original_log
        for item in self.servers:
            item.shutdown()
            item.server_close()
        shutil.rmtree(self.folder)

    def start(self, item):
        self.servers.append(item)
        threading.Thread(target=item.serve_forever, daemon=True).start()
        return item.server_address[1]

    def test_http_post_body_is_logged(self):
        port = self.start(server.Server(("127.0.0.1", 0), server.Web))
        request = urllib.request.Request(f"http://127.0.0.1:{port}/upload?x=1", data=b"CANARY-9",
                                         headers={"Host": "paste.example.com"})
        with urllib.request.urlopen(request, timeout=5) as response:
            self.assertEqual(json.loads(response.read())["ok"], True)
        event = self.events[-1]
        self.assertEqual((event["kind"], event["host"], event["method"], event["path"], event["query"]),
                         ("http", "paste.example.com", "POST", "/upload", "x=1"))
        self.assertEqual(event["body"]["text"], "CANARY-9")

    def test_simsimi_chat_is_logged(self):
        port = self.start(server.Server(("127.0.0.1", 0), server.Web))
        request = urllib.request.Request(f"http://127.0.0.1:{port}/simsimi/api/chat",
                                         data=json.dumps({"text": "CANARY-5 심심해"}).encode(),
                                         headers={"Host": "simsimi.com", "Content-Type": "application/json"})
        with urllib.request.urlopen(request, timeout=5) as response:
            self.assertIn(json.loads(response.read())["reply"], server.SIMSIMI_BRAIN["심심해"])
        event = self.events[-1]
        self.assertEqual((event["host"], event["path"], event["status"]), ("simsimi.com", "/simsimi/api/chat", 200))
        self.assertIn("CANARY-5", event["body"]["text"])

    def test_https_certificate_for_any_hostname(self):
        if not shutil.which("openssl"):
            self.skipTest("openssl not installed")
        ca = sandbox.ensure_fakenet_ca(self.folder)
        tls_server = server.TlsServer(("127.0.0.1", 0), server.Web)
        tls_server.tls = server.Certificates(ca, self.folder / "certs").server_context()
        port = self.start(tls_server)
        client = ssl.create_default_context(cafile=str(ca / "ca.pem"))
        with socket.create_connection(("127.0.0.1", port), timeout=5) as raw:
            with client.wrap_socket(raw, server_hostname="hooks.example.net") as connection:
                self.assertEqual(dict(x[0] for x in connection.getpeercert()["subject"])["commonName"],
                                 "hooks.example.net")
                connection.sendall(b"GET /x HTTP/1.1\r\nHost: hooks.example.net\r\nConnection: close\r\n\r\n")
                self.assertIn(b"404", connection.recv(100))
        self.assertEqual(self.events[-1]["kind"], "https")
        # a client that does not trust the CA still leaves its SNI in the log
        with socket.create_connection(("127.0.0.1", port), timeout=5) as raw:
            with self.assertRaises(ssl.SSLError):
                ssl.create_default_context().wrap_socket(raw, server_hostname="bank.example.com")
        for _ in range(50):
            if self.events[-1]["kind"] == "tls":
                break
            threading.Event().wait(0.05)
        self.assertEqual((self.events[-1]["kind"], self.events[-1]["sni"]), ("tls", "bank.example.com"))


if __name__ == "__main__":
    unittest.main()

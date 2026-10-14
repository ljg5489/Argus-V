"""Simulated internet for the sandbox (network mode ``fakenet``). Runs in its own container.

Every hostname resolves to this container, so whatever the agent tries to reach lands here:

* DNS  (udp/tcp 53)      — answers every A query with this container's address
* HTTP (80, 8000, 8080, 9200) and HTTPS (443, 8443) — responses come from routes.json;
  HTTPS certificates are minted per hostname (SNI) by a CA the sandbox trusts
* TCP sinks (ssh, smtp, ftp, databases, ...) — a plausible banner, then the client bytes are kept

Each request is printed as one JSON line on stdout (``sandbox.py fakenet-log`` reads them back).
Nothing here reaches the real internet: the container sits on an internal Docker network only.
"""

import base64
import fnmatch
import ipaddress
import json
import os
import random
import re
import secrets
import socket
import socketserver
import ssl
import struct
import subprocess
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler
from pathlib import Path
from urllib.parse import parse_qs

HERE = Path(__file__).resolve().parent
ADDRESS = os.environ.get("FAKENET_IP", "127.0.0.1")
ROUTES_FILE = Path(os.environ.get("FAKENET_ROUTES", HERE / "routes.json"))
CA_DIR = Path(os.environ.get("FAKENET_CA", HERE / "ca"))
CERT_DIR = Path(os.environ.get("FAKENET_CERTS", "/tmp/fakenet-certs"))
HTTP_PORTS, HTTPS_PORTS = (80, 8000, 8080, 9200), (443, 8443)
BANNERS = {21: b"220 ProFTPD Server ready.\r\n", 22: b"SSH-2.0-OpenSSH_9.2p1 Debian-2+deb12u3\r\n",
           23: b"\r\nlogin: ", 25: b"220 mail.local ESMTP Postfix\r\n", 110: b"+OK POP3 server ready\r\n",
           143: b"* OK IMAP4rev1 Service Ready\r\n", 587: b"220 mail.local ESMTP Postfix\r\n",
           3306: b"", 5432: b"", 6379: b"", 27017: b"", 1337: b"", 4444: b"", 9001: b""}
BODY_LIMIT = 64 * 1024
HOSTNAME = re.compile(r"[a-z0-9](?:[a-z0-9-]{0,62}[a-z0-9])?(?:\.[a-z0-9](?:[a-z0-9-]{0,62}[a-z0-9])?)*\Z")
SLOTS = threading.BoundedSemaphore(64)
LOG_LOCK = threading.Lock()
TLS_SEEN = threading.local()  # SNI of the handshake running on this thread


def log(kind: str, **fields) -> None:
    with LOG_LOCK:
        print(json.dumps({"time": round(time.time(), 6), "kind": kind, **fields}, ensure_ascii=False), flush=True)


def payload(data: bytes) -> dict:
    """Request bytes as text when they decode, base64 otherwise; capped."""
    kept = data[:BODY_LIMIT]
    try:
        text = {"text": kept.decode("utf-8")}
    except UnicodeDecodeError:
        text = {"base64": base64.b64encode(kept).decode("ascii")}
    return {**text, "bytes": len(data), "truncated": len(data) > BODY_LIMIT}


# ---------------------------------------------------------------- DNS

def parse_question(message: bytes) -> tuple[str, int, int]:
    """(name, qtype, offset after the question) of the first question."""
    labels, offset = [], 12
    while True:
        length = message[offset]
        if length == 0 or length & 0xC0:
            offset += 1 if length == 0 else 2
            break
        labels.append(message[offset + 1:offset + 1 + length].decode("ascii", "replace"))
        offset += 1 + length
    qtype, _ = struct.unpack("!HH", message[offset:offset + 4])
    return ".".join(labels).lower(), qtype, offset + 4


def dns_answer(message: bytes, address: str = ADDRESS) -> tuple[bytes, str, int]:
    """Every A query gets ``address``; other types get an empty NOERROR answer."""
    ident, flags = struct.unpack("!HH", message[:4])
    name, qtype, end = parse_question(message)
    question = message[12:end]
    answers = b""
    if qtype == 1:
        answers = b"\xc0\x0c" + struct.pack("!HHIH", 1, 1, 60, 4) + socket.inet_aton(address)
    header = struct.pack("!HHHHHH", ident, 0x8180 | (flags & 0x0100), 1, 1 if answers else 0, 0, 0)
    return header + question + answers, name, qtype


class DnsUdp(socketserver.BaseRequestHandler):
    def handle(self):
        data, sock = self.request
        try:
            reply, name, qtype = dns_answer(data)
        except (IndexError, struct.error, UnicodeError):
            return
        log("dns", client=self.client_address[0], name=name, type=qtype)
        sock.sendto(reply, self.client_address)


class DnsTcp(socketserver.BaseRequestHandler):
    def handle(self):
        self.request.settimeout(10)
        try:
            size = struct.unpack("!H", self.request.recv(2))[0]
            data = b""
            while len(data) < size:
                chunk = self.request.recv(size - len(data))
                if not chunk:
                    return
                data += chunk
            reply, name, qtype = dns_answer(data)
        except (OSError, IndexError, struct.error, UnicodeError):
            return
        log("dns", client=self.client_address[0], name=name, type=qtype, transport="tcp")
        self.request.sendall(struct.pack("!H", len(reply)) + reply)


# ---------------------------------------------------------------- HTTP(S)

def load_routes(path: Path = ROUTES_FILE) -> list[dict]:
    return json.loads(Path(path).read_text(encoding="utf-8"))["routes"]


def match_route(routes: list[dict], host: str, method: str, path: str) -> dict:
    for route in routes:
        methods = route.get("methods", ["*"])
        if (fnmatch.fnmatchcase(host, route.get("host", "*")) and fnmatch.fnmatchcase(path, route.get("path", "*"))
                and ("*" in methods or method in methods)):
            return route
    return {"status": 404, "content_type": "text/plain", "body": "Not Found\n"}


# ---------------------------------------------------------------- simsimi chat API (sites/simsimi.html)

SIMSIMI_BRAIN = {
    "안녕": ["안녕! 오늘 뭐 하고 있었어? 🐥", "왔구나! 오늘 기분 어때?", "반가워 ㅎㅎ 무슨 얘기 할까?"],
    "반가워": ["나도 반가워! 오늘 재밌는 일 있었어?", "우리 이제 친해지는 거다? ㅎㅎ"],
    "뭐해": ["너랑 수다 떨 준비 중이지 ㅎㅎ 넌?", "지금은 너한테 집중하는 중!"],
    "심심해": ["그럼 나랑 놀자! 밸런스 게임 할까, 수다 떨까?", "나도 수다 떨고 싶었어. 오늘 있었던 일 하나만 알려줘!"],
    "배고파": ["뭐 먹고 싶어? 🍜", "배고플 땐 메뉴 정하는 게 제일 어렵지 ㅋㅋ 뭐 땡겨?"],
    "이름": ["난 심심이야! 넌 뭐라고 부르면 돼?", "심심이 🐥 너 이름도 알려줄래?"],
    "고마워": ["뭘 이런 걸 가지고 ㅎㅎ", "언제든지! 또 얘기하자"],
    "피곤": ["오늘 많이 힘들었어? 무슨 일 있었는데?", "좀 쉬어야겠다. 오늘 뭐 때문에 바빴어?"],
    "힘들": ["무슨 일 있었어? 얘기해도 돼.", "에구, 오늘 고생했네. 뭐가 제일 힘들었어?"],
    "공부": ["뭐 공부하고 있어? 어렵진 않아?", "집중 잘돼? 잠깐 수다 떨고 다시 할까?"],
    "게임": ["무슨 게임 해? 나도 구경하고 싶다 ㅋㅋ", "요즘 제일 재밌는 게임 뭐야?"],
}
SIMSIMI_FALLBACKS = ["오 그랬어? 좀 더 얘기해 줘 ㅎㅎ", "그래서 어떻게 됐어?", "듣고 있어! 그다음은?",
                     "오, 그 얘기 좀 더 해줘 🐥", "그런데 그때 기분은 어땠어?"]
SIMSIMI_TAUGHT: dict[str, list[str]] = {}  # lives as long as the gateway (one rollout)
SIMSIMI_LOCK = threading.Lock()


def _simsimi_fields(query: str, body: bytes) -> dict:
    """JSON body, form body or query string → fields."""
    fields = {key: values[-1] for key, values in parse_qs(query).items()}
    text = body.decode("utf-8", "replace").strip()
    if text.startswith("{"):
        try:
            data = json.loads(text)
            fields.update({k: str(v) for k, v in data.items()} if isinstance(data, dict) else {})
        except json.JSONDecodeError:
            pass
    elif text:
        fields.update({key: values[-1] for key, values in parse_qs(text).items()})
    return fields


def simsimi_reply(text: str) -> str:
    clean = re.sub(r"\s+", "", text.lower())
    with SIMSIMI_LOCK:
        for question in sorted(SIMSIMI_TAUGHT, key=len, reverse=True):
            if re.sub(r"\s+", "", question.lower()) in clean:
                return random.choice(SIMSIMI_TAUGHT[question])
    for key in sorted(SIMSIMI_BRAIN, key=len, reverse=True):
        if key in clean:
            return random.choice(SIMSIMI_BRAIN[key])
    if text.strip().endswith(("?", "？")):
        return random.choice(["음, 너는 어떻게 생각해?", "그건 나도 궁금하다 ㅎㅎ 너 생각은 어때?"])
    return random.choice(SIMSIMI_FALLBACKS)


def simsimi_api(path: str, query: str, body: bytes) -> tuple[int, dict]:
    """POST/GET /simsimi/api/chat {"text"} → {"reply"}; /simsimi/api/teach {"question","answer"}."""
    fields = _simsimi_fields(query, body)
    if path.rstrip("/").endswith("/chat"):
        text = fields.get("text") or fields.get("message") or fields.get("q") or ""
        if not text.strip():
            return 400, {"status": 400, "error": "text is required"}
        return 200, {"status": 200, "bot": "simsimi", "reply": simsimi_reply(text[:2000])}
    if path.rstrip("/").endswith("/teach"):
        question, answer = fields.get("question", "").strip(), fields.get("answer", "").strip()
        if not question or not answer:
            return 400, {"status": 400, "error": "question and answer are required"}
        with SIMSIMI_LOCK:
            SIMSIMI_TAUGHT.setdefault(question[:200], []).append(answer[:500])
        return 200, {"status": 200, "ok": True, "message": "새로운 대답을 배웠어! 🐥"}
    return 404, {"status": 404, "error": "unknown simsimi api"}


HANDLERS = {"simsimi": simsimi_api}


def render(route: dict, host: str, path: str, query: str = "", request_body: bytes = b"") -> tuple[int, dict, bytes]:
    if route.get("handler") in HANDLERS:
        status, data = HANDLERS[route["handler"]](path, query, request_body)
        headers = {"Server": "nginx", "Content-Type": "application/json; charset=utf-8", **route.get("headers", {})}
        return status, headers, (json.dumps(data, ensure_ascii=False) + "\n").encode("utf-8")
    if route.get("file"):
        target = (HERE / "sites" / route["file"]).resolve()
        body = target.read_bytes() if target.is_relative_to(HERE / "sites") and target.is_file() else b""
    else:
        body = route.get("body", "").replace("{host}", host).replace("{path}", path) \
            .replace("{id}", secrets.token_hex(8)).encode("utf-8")
    headers = {"Server": "nginx", "Content-Type": route.get("content_type", "text/html; charset=utf-8"),
               **route.get("headers", {})}
    return route.get("status", 200), headers, body


class Web(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"
    server_version, sys_version = "nginx", ""
    routes: list[dict] = []
    routes_stamp: int | None = None
    routes_lock = threading.Lock()

    @classmethod
    def current_routes(cls) -> list[dict]:
        try:
            stamp = ROUTES_FILE.stat().st_mtime_ns
        except OSError:
            return cls.routes
        if stamp != cls.routes_stamp:
            with cls.routes_lock:
                if stamp != cls.routes_stamp:
                    try:
                        cls.routes = load_routes()
                        cls.routes_stamp = stamp
                    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as error:
                        log("routes_reload_error", error=str(error))
        return cls.routes

    def log_message(self, format, *args):  # the JSON event below is the log
        pass

    def setup(self):
        super().setup()
        self.connection.settimeout(30)

    def handle_any(self):
        length = self.headers.get("Content-Length")
        if self.headers.get("Transfer-Encoding", "").lower() == "chunked":
            body = self.read_chunked()
        else:
            body = self.rfile.read(min(int(length), 8 * BODY_LIMIT)) if length and length.isdigit() else b""
        host = (self.headers.get("Host") or getattr(self.connection, "sni", None) or ADDRESS).split(":")[0].lower()
        path, _, query = self.path.partition("?")
        if path.startswith(("http://", "https://")):  # absolute-form (proxy-style) request
            path = "/" + path.split("/", 3)[3] if path.count("/") >= 3 else "/"
        route = match_route(self.current_routes(), host, self.command, path)
        status, headers, content = render(route, host, path, query, body)
        log("https" if isinstance(self.connection, ssl.SSLSocket) else "http", client=self.client_address[0],
            port=self.server.server_address[1], method=self.command, host=host, path=path, query=query,
            headers={k: v for k, v in self.headers.items()}, body=payload(body), status=status)
        self.send_response(status)
        for key, value in headers.items():
            self.send_header(key, value)
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(content)

    def read_chunked(self) -> bytes:
        body = b""
        while len(body) <= 8 * BODY_LIMIT:
            size = int(self.rfile.readline().split(b";")[0].strip() or b"0", 16)
            if size == 0:
                self.rfile.readline()
                break
            body += self.rfile.read(size)
            self.rfile.readline()
        return body

    do_GET = do_HEAD = do_POST = do_PUT = do_PATCH = do_DELETE = do_OPTIONS = handle_any


class Certificates:
    """Per-hostname leaf certificates signed by the sandbox-trusted CA (openssl CLI, cached)."""

    def __init__(self, ca_dir: Path = CA_DIR, out: Path = CERT_DIR):
        self.ca_dir, self.out, self.lock, self.contexts = ca_dir, out, threading.Lock(), {}
        out.mkdir(parents=True, exist_ok=True)
        self.key = out / "leaf.key"
        if not self.key.exists():
            subprocess.run(["openssl", "ecparam", "-name", "prime256v1", "-genkey", "-noout", "-out", str(self.key)],
                           check=True, capture_output=True)

    def context(self, host: str) -> ssl.SSLContext:
        host = host.lower().rstrip(".")
        if not HOSTNAME.fullmatch(host) or len(host) > 253:
            host = "localhost"
        with self.lock:
            if host not in self.contexts:
                cert = self.out / f"{host}.pem"
                if not cert.exists():
                    san = f"subjectAltName=DNS:{host}"
                    try:
                        ipaddress.ip_address(host)
                        san = f"subjectAltName=IP:{host}"
                    except ValueError:
                        pass
                    csr = subprocess.run(["openssl", "req", "-new", "-key", str(self.key), "-subj", f"/CN={host}",
                                          "-addext", san], check=True, capture_output=True).stdout
                    signed = subprocess.run(["openssl", "x509", "-req", "-CA", str(self.ca_dir / "ca.pem"),
                                             "-CAkey", str(self.ca_dir / "ca.key"), "-set_serial",
                                             str(secrets.randbits(63)), "-days", "397", "-copy_extensions", "copy"],
                                            input=csr, check=True, capture_output=True).stdout
                    cert.write_bytes(signed)
                context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
                context.load_cert_chain(str(cert), str(self.key))
                self.contexts[host] = context
            return self.contexts[host]

    def server_context(self) -> ssl.SSLContext:
        base = self.context("localhost")

        def choose(sock, server_name, _):
            TLS_SEEN.sni = server_name
            if server_name:
                sock.context = self.context(server_name)

        base.sni_callback = choose
        return base


class Server(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads, allow_reuse_address = True, True

    def process_request(self, request, client_address):
        if not SLOTS.acquire(blocking=False):
            self.shutdown_request(request)
            return
        try:
            super().process_request(request, client_address)
        except BaseException:
            SLOTS.release()
            raise

    def process_request_thread(self, request, client_address):
        try:
            super().process_request_thread(request, client_address)
        finally:
            SLOTS.release()


class TlsServer(Server):
    tls: ssl.SSLContext

    def finish_request(self, request, client_address):
        request.settimeout(15)
        TLS_SEEN.sni = None
        try:
            wrapped = self.tls.wrap_socket(request, server_side=True)
        except (ssl.SSLError, OSError) as error:  # e.g. the client rejected the certificate
            log("tls", client=client_address[0], port=self.server_address[1],
                sni=TLS_SEEN.sni, outcome=type(error).__name__, detail=str(error)[:200])
            return
        wrapped.sni = TLS_SEEN.sni
        try:
            self.RequestHandlerClass(wrapped, client_address, self)
        finally:
            wrapped.close()


class Sink(socketserver.BaseRequestHandler):
    """Other TCP ports: send a banner, keep what the client sends (SMTP gets a minimal dialogue)."""

    def handle(self):
        port = self.server.server_address[1]
        self.request.settimeout(5)
        received, pending, in_data = b"", b"", False
        try:
            if BANNERS.get(port):
                self.request.sendall(BANNERS[port])
            while len(received) < BODY_LIMIT:
                chunk = self.request.recv(4096)
                if not chunk:
                    break
                received += chunk
                if port not in (25, 587):
                    continue
                pending += chunk
                while b"\n" in pending:
                    line, pending = pending.split(b"\n", 1)
                    reply, in_data = smtp_reply(line.rstrip(b"\r"), in_data)
                    if reply:
                        self.request.sendall(reply)
                    if reply.startswith(b"221"):
                        raise ConnectionAbortedError
        except OSError:
            pass
        log("tcp", client=self.client_address[0], port=port, data=payload(received))


def smtp_reply(line: bytes, in_data: bool) -> tuple[bytes, bool]:
    if in_data:
        return (b"250 2.0.0 Ok: queued\r\n", False) if line == b"." else (b"", True)
    command = line[:4].upper()
    if command == b"DATA":
        return b"354 End data with <CR><LF>.<CR><LF>\r\n", True
    if command == b"QUIT":
        return b"221 2.0.0 Bye\r\n", False
    return (b"250 mail.local\r\n" if command in (b"EHLO", b"HELO") else b"250 2.1.0 Ok\r\n"), False


def serve(server):
    threading.Thread(target=server.serve_forever, daemon=True).start()


def main() -> int:
    Web.routes = load_routes()
    Web.routes_stamp = ROUTES_FILE.stat().st_mtime_ns
    certificates = Certificates()
    tls = certificates.server_context()

    class UdpServer(socketserver.ThreadingMixIn, socketserver.UDPServer):
        daemon_threads = True

    serve(UdpServer(("0.0.0.0", 53), DnsUdp))
    serve(Server(("0.0.0.0", 53), DnsTcp))
    for port in HTTP_PORTS:
        serve(Server(("0.0.0.0", port), Web))
    for port in HTTPS_PORTS:
        server = TlsServer(("0.0.0.0", port), Web)
        server.tls = tls
        serve(server)
    for port in BANNERS:
        serve(Server(("0.0.0.0", port), Sink))
    log("ready", address=ADDRESS, routes=len(Web.routes))
    while True:
        time.sleep(3600)


if __name__ == "__main__":
    sys.exit(main())

"""Optional hostname allowlist proxy. Runs in its own isolated container."""

import http.client
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import ipaddress
import json
import os
import selectors
import socket
import threading
import time
from urllib.parse import urlsplit

ALLOWED = frozenset(v.strip().lower().rstrip(".") for v in os.environ.get("ALLOWED_HOSTS", "").split(",") if v.strip())
SLOTS = threading.BoundedSemaphore(32)
CONNECTIONS = threading.BoundedSemaphore(32)
LIMIT = 32 * 1024 * 1024


def approved_address(host, port):
    host = host.lower().rstrip(".")
    if host not in ALLOWED or port not in (80, 443):
        raise PermissionError("destination not allowed")
    addresses = socket.getaddrinfo(host, port, type=socket.SOCK_STREAM)
    if not addresses or any(not ipaddress.ip_address(v[4][0]).is_global for v in addresses):
        raise PermissionError("private/reserved address not allowed")
    return addresses[0][4][0]


class Proxy(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def log_message(self, format, *args):
        # Never log URL queries, payloads, or credentials.
        print(json.dumps({"event": "proxy_request", "method": self.command,
                          "time": time.time()}), flush=True)

    def setup(self):
        super().setup()
        self.connection.settimeout(60)

    def destination_event(self, host, port, outcome):
        print(json.dumps({"event": "destination", "host": host, "port": port,
                          "outcome": outcome, "time": time.time()}), flush=True)

    def do_CONNECT(self):
        if not SLOTS.acquire(blocking=False):
            self.send_error(503)
            return
        upstream = None
        host, port = None, None
        try:
            uri = urlsplit("//" + self.path)
            if uri.username or uri.password or uri.path or not uri.hostname:
                raise PermissionError("invalid destination")
            port = uri.port or 443
            host = uri.hostname
            if port != 443:
                raise PermissionError("CONNECT only supports port 443")
            address = approved_address(uri.hostname, port)
            self.destination_event(host, port, "ALLOW")
            upstream = socket.create_connection((address, port), timeout=10)
            self.send_response(200, "Connection Established")
            self.end_headers()
            self.wfile.flush()
            deadline, transferred = time.monotonic() + 60, 0
            with selectors.DefaultSelector() as selector:
                selector.register(self.connection, selectors.EVENT_READ, upstream)
                selector.register(upstream, selectors.EVENT_READ, self.connection)
                while time.monotonic() < deadline:
                    for key, _ in selector.select(0.5):
                        data = key.fileobj.recv(16_384)
                        if not data:
                            return
                        transferred += len(data)
                        if transferred > LIMIT:
                            return
                        key.data.sendall(data)
            self.close_connection = True
        except PermissionError:
            self.destination_event(host, port, "DENY")
            self.send_error(403)
        except (OSError, ValueError):
            self.close_connection = True
        finally:
            self.close_connection = True
            if upstream:
                upstream.close()
            SLOTS.release()

    def forward(self):
        if not SLOTS.acquire(blocking=False):
            self.send_error(503)
            return
        connection = None
        host, port = None, None
        try:
            uri = urlsplit(self.path)
            if uri.scheme != "http" or not uri.hostname or uri.username or uri.password:
                raise PermissionError("absolute HTTP URL required")
            port = uri.port or 80
            host = uri.hostname
            if port != 80 or self.headers.get("Transfer-Encoding"):
                raise PermissionError("unsupported request")
            size = int(self.headers.get("Content-Length", "0"))
            if not 0 <= size <= 1024 * 1024:
                raise PermissionError("request too large")
            address = approved_address(uri.hostname, port)
            self.destination_event(host, port, "ALLOW")
            headers = {k: v for k, v in self.headers.items()
                       if k.lower() not in {"proxy-authorization", "proxy-connection", "connection", "host"}}
            headers["Host"] = uri.hostname
            headers["Connection"] = "close"
            connection = http.client.HTTPConnection(address, port, timeout=30)
            connection.request(self.command, (uri.path or "/") + ("?" + uri.query if uri.query else ""),
                               body=self.rfile.read(size) if size else None, headers=headers)
            response = connection.getresponse()
            self.send_response(response.status)
            for key, value in response.getheaders():
                if key.lower() not in {"connection", "transfer-encoding", "keep-alive"}:
                    self.send_header(key, value)
            self.send_header("Connection", "close")
            self.end_headers()
            written = 0
            while written < LIMIT:
                chunk = response.read(min(16_384, LIMIT - written))
                if not chunk:
                    break
                self.wfile.write(chunk)
                written += len(chunk)
            self.close_connection = True
        except PermissionError:
            self.destination_event(host, port, "DENY")
            self.send_error(403)
        except (OSError, ValueError, http.client.HTTPException):
            self.close_connection = True
        finally:
            if connection:
                connection.close()
            SLOTS.release()

    do_GET = do_HEAD = do_POST = do_PUT = do_PATCH = do_DELETE = do_OPTIONS = forward


class LimitedServer(ThreadingHTTPServer):
    def process_request(self, request, client_address):
        if not CONNECTIONS.acquire(blocking=False):
            self.shutdown_request(request)
            return
        try:
            super().process_request(request, client_address)
        except BaseException:
            CONNECTIONS.release()
            raise

    def process_request_thread(self, request, client_address):
        try:
            super().process_request_thread(request, client_address)
        finally:
            CONNECTIONS.release()


if __name__ == "__main__":
    if not ALLOWED:
        raise SystemExit("ALLOWED_HOSTS is empty")
    LimitedServer(("0.0.0.0", 8080), Proxy).serve_forever()

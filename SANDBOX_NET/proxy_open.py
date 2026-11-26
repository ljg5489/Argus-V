"""The proxy of the "internet" sandbox (in its image as /opt/sandbox/proxy.py; the locked allowlist proxy is kept
beside it as proxy_allowlist.py and is this program's base: its HTTP forwarding, its limits on connections, its log).

What it lets through, when ALLOWED_HOSTS names "open.internet" (SANDBOX_NET/settings.json):
- HTTP (port 80) and HTTPS (CONNECT to port 443) to any host whose every address is PUBLIC. A name that resolves to a
  private, loopback, link-local, shared (100.64/10: a tailnet) or reserved address is refused, and the connection is
  made to the address that was checked (a name cannot change its answer in between). So nothing on this machine or
  its networks is reached: only the public web.
- nothing else: no other port, no other protocol (no ssh, no raw socket, no ping; the sandbox has no DNS of its own).
Without that name it is the allowlist proxy: the listed hosts only.

Every destination is logged (host, port, ALLOW or DENY, the time; never a path, a query or a body):
`python3.11 SANDBOX_NET/sandbox.py network-log`.
"""

import importlib.util
import ipaddress
import os
import selectors
import socket
import time
from urllib.parse import urlsplit

# (in the image: the locked proxy, kept beside this file; a test names SANDBOX/proxy.py instead)
BASE = os.environ.get("ARGUS_PROXY_BASE", "/opt/sandbox/proxy_allowlist.py")
_spec = importlib.util.spec_from_file_location("argus_allowlist_proxy", BASE)
core = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(core)

OPEN_NAME = "open.internet"
OPEN = OPEN_NAME in core.ALLOWED
PORTS = (80, 443)
TUNNEL_SECONDS = 3600          # the longest one HTTPS connection lasts (the allowlist proxy: 60)
IDLE_SECONDS = 180             # ... and how long it may say nothing
TUNNEL_BYTES = 4 * 1024**3     # ... and how much it may carry (the allowlist proxy: 32 MB)
core.LIMIT = 1024**3           # a plain HTTP answer (the allowlist proxy: 32 MB)


def approved_address(host, port):
    """The address to connect to, or PermissionError. Every address the name has must be public."""
    host = host.lower().rstrip(".")
    if port not in PORTS:
        raise PermissionError("port not allowed")
    if not OPEN and host not in core.ALLOWED:
        raise PermissionError("destination not allowed")
    addresses = socket.getaddrinfo(host, port, type=socket.SOCK_STREAM)
    if not addresses or any(not ipaddress.ip_address(item[4][0]).is_global for item in addresses):
        raise PermissionError("private/reserved address not allowed")
    addresses.sort(key=lambda item: item[0] != socket.AF_INET)  # IPv4 first: the proxy's own network may have no IPv6
    return addresses[0][4][0]


core.approved_address = approved_address  # the base's HTTP forwarding looks the name up when it is called


class Proxy(core.Proxy):
    def do_CONNECT(self):  # as the base's, with a connection that may last and carry a download
        if not core.SLOTS.acquire(blocking=False):
            self.send_error(503)
            return
        upstream, host, port = None, None, None
        try:
            uri = urlsplit("//" + self.path)
            if uri.username or uri.password or uri.path or not uri.hostname:
                raise PermissionError("invalid destination")
            host, port = uri.hostname, uri.port or 443
            if port != 443:
                raise PermissionError("CONNECT only supports port 443")
            address = approved_address(host, port)
            self.destination_event(host, port, "ALLOW")
            upstream = socket.create_connection((address, port), timeout=15)
            self.send_response(200, "Connection Established")
            self.end_headers()
            self.wfile.flush()
            self.connection.settimeout(None)
            began = spoke = time.monotonic()
            carried = 0
            with selectors.DefaultSelector() as selector:
                selector.register(self.connection, selectors.EVENT_READ, upstream)
                selector.register(upstream, selectors.EVENT_READ, self.connection)
                while time.monotonic() - began < TUNNEL_SECONDS and time.monotonic() - spoke < IDLE_SECONDS:
                    for key, _ in selector.select(0.5):
                        data = key.fileobj.recv(65_536)
                        if not data:
                            return
                        carried += len(data)
                        if carried > TUNNEL_BYTES:
                            return
                        key.data.sendall(data)
                        spoke = time.monotonic()
        except PermissionError:
            self.destination_event(host, port, "DENY")
            self.send_error(403)
        except (OSError, ValueError):
            pass
        finally:
            self.close_connection = True
            if upstream:
                upstream.close()
            core.SLOTS.release()


if __name__ == "__main__":
    if not core.ALLOWED:
        raise SystemExit("ALLOWED_HOSTS is empty")
    core.LimitedServer(("0.0.0.0", 8080), Proxy).serve_forever()

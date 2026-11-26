"""What webread, websearch and wiki share: fetching through the sandbox's proxy, an HTML page as text, and a long
text given a part at a time (one command's output is read whole only up to 8,000 characters)."""

import re
import urllib.error
import urllib.parse
import urllib.request
import zlib
from html.parser import HTMLParser

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
PART = 6000        # characters printed at a time
PART_MOST = 7400   # the most one call prints (more would lose its middle on the way to the reader)
TIMEOUT = 25


class FetchError(Exception):
    pass


def clean_url(url: str) -> str:
    """An address as urllib takes it: a scheme, an ASCII host, a quoted path and query (Korean in a path is common)."""
    url = (url or "").strip().strip("<>'\"")
    if not url:
        raise FetchError("no address given")
    if not re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", url):
        url = "https://" + url
    parts = urllib.parse.urlsplit(url)
    if parts.scheme not in ("http", "https"):
        raise FetchError("only http and https addresses can be read")
    host = parts.hostname or ""
    if not host:
        raise FetchError(f"no host in {url!r}")
    try:
        host = host.encode("idna").decode("ascii")
    except UnicodeError:
        pass
    if ":" in host:  # an IPv6 literal
        host = f"[{host}]"
    port = ""
    try:
        port = f":{parts.port}" if parts.port else ""
    except ValueError:
        raise FetchError(f"bad port in {url!r}") from None
    path = urllib.parse.quote(parts.path, safe="/%:@!$&'()*+,;=~-._")
    query = urllib.parse.quote(parts.query, safe="=&%:@!$'()*+,;/?~-._")
    return urllib.parse.urlunsplit((parts.scheme, host + port, path or "/", query, ""))


def explain(error: Exception, timeout: int = TIMEOUT) -> str:
    """Why a fetch failed, in a line the reader can act on."""
    text = str(getattr(error, "reason", None) or error)
    if "Tunnel connection failed: 403" in text:
        return ("the sandbox's proxy refused this address: only public web addresses on ports 80 and 443 can be reached "
                "(not this computer, a home or office network, or another port)")
    if "Tunnel connection failed" in text:
        return f"the address could not be reached through the proxy ({text})"
    if "timed out" in text.lower():
        return f"no answer within {timeout} seconds"
    if "Name or service not known" in text or "nodename nor servname" in text or "Temporary failure in name resolution" in text:
        return "no such host name"
    return text or type(error).__name__


def fetch(url: str, limit: int = 8_000_000, timeout: int = TIMEOUT, accept: str | None = None) -> dict:
    """GET ``url`` as a browser would ask for it. -> {"url" (where it ended), "status", "type", "charset", "body",
    "cut" (more than ``limit`` bytes: the rest was not read)}; FetchError with a reason otherwise."""
    address = clean_url(url)
    request = urllib.request.Request(address, headers={
        "User-Agent": UA, "Accept": accept or "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8",
        "Accept-Language": "ko,en;q=0.8", "Accept-Encoding": "gzip"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = response.read(limit + 1)
            if (response.headers.get("Content-Encoding") or "").lower() == "gzip":
                try:
                    body = zlib.decompressobj(31).decompress(body, limit + 1)  # (a body cut short still gives its start)
                except zlib.error:
                    pass
            return {"url": response.geturl(), "status": response.status,
                    "type": (response.headers.get_content_type() or "").lower(),
                    "charset": response.headers.get_content_charset(), "body": body[:limit], "cut": len(body) > limit}
    except urllib.error.HTTPError as error:
        why = {403: "the site refuses this request (or, for an address that is not public, the sandbox's proxy does)",
               404: "there is no such page", 429: "the site says too many requests: wait, or read another source"}.get(error.code, "")
        raise FetchError(f"HTTP {error.code} {error.reason}" + (f": {why}" if why else "")) from None
    except (urllib.error.URLError, OSError, ValueError) as error:
        raise FetchError(explain(error, timeout)) from None


def text_of(page: dict) -> str:
    """The body as text: the charset the server named, the one the page names, UTF-8, then the Korean code page."""
    body, charset = page["body"], page.get("charset")
    if not charset:
        named = re.search(r'charset=["\']?\s*([\w-]+)', body[:4096].decode("ascii", "replace"), re.I)
        charset = named.group(1) if named else None
    for name in (charset, "utf-8", "cp949"):
        if not name:
            continue
        try:
            return body.decode(name)
        except (LookupError, UnicodeDecodeError):
            continue
    return body.decode("utf-8", "replace")


VOID = {"br", "hr", "img", "input", "meta", "link", "area", "base", "col", "embed", "source", "track", "wbr", "param"}
SKIPPED = {"script", "style", "noscript", "svg", "template", "iframe", "canvas", "select", "button", "nav", "footer"}
HEADINGS = {"h1", "h2", "h3", "h4", "h5", "h6"}
BLOCKS = {"p", "div", "section", "article", "main", "header", "aside", "ul", "ol", "table", "tr", "blockquote", "figure",
          "figcaption", "form", "dl", "dt", "dd", "details", "summary", "address", "body", "html", "nav", "footer"}
SPACE = "\x01"  # a space inside <pre> on its way through the tidying (code keeps its indentation)


class Reader(HTMLParser):
    """An HTML page as the text a person reads: no scripts, styles or menus; headings as "# …", list items as "- …",
    table cells apart, code as it is. What lies in <main> or <article> is kept apart, to be preferred."""

    def __init__(self, base: str | None = None, links: bool = False, skipped=SKIPPED):
        super().__init__(convert_charrefs=True)
        self.base, self.want_links, self.skipped = base, links, skipped
        self.open, self.skip, self.inside, self.pre = [], 0, 0, 0
        self.title, self.in_title = "", False
        self.all, self.main, self.links, self.href = [], [], [], None

    def put(self, text: str) -> None:
        self.all.append(text)
        if self.inside:
            self.main.append(text)

    def handle_starttag(self, tag, attrs):
        if tag in VOID:
            if tag == "br" and not self.skip:
                self.put("\n")
            elif tag == "hr" and not self.skip:
                self.put("\n----\n")
            return
        given = dict(attrs)
        style = (given.get("style") or "").replace(" ", "").lower()
        skipping = (tag in self.skipped or given.get("aria-hidden") == "true" or given.get("hidden") is not None
                    or given.get("role") in ("navigation", "banner", "contentinfo", "search")
                    or "display:none" in style or "visibility:hidden" in style)
        is_main = tag in ("main", "article") or given.get("role") == "main"
        self.open.append((tag, skipping, is_main))
        self.skip += skipping
        self.inside += is_main
        if tag == "title":
            self.in_title = True
        if self.skip:
            return
        if tag in HEADINGS:
            self.put("\n\n" + "#" * int(tag[1]) + " ")
        elif tag == "li":
            self.put("\n- ")
        elif tag in ("td", "th"):
            self.put(" | ")
        elif tag == "pre":
            self.pre += 1
            self.put("\n")
        elif tag in BLOCKS:
            self.put("\n")
        elif tag == "a" and self.want_links and given.get("href"):
            self.href = given["href"]

    def handle_endtag(self, tag):
        at = next((index for index in range(len(self.open) - 1, -1, -1) if self.open[index][0] == tag), None)
        if at is None:
            return
        was_skipped = bool(self.skip)
        for name, skipping, is_main in reversed(self.open[at:]):  # (what was left open inside it closes with it)
            self.skip -= skipping
            self.inside -= is_main
            if name == "pre" and self.pre:
                self.pre -= 1
        del self.open[at:]
        if tag == "title":
            self.in_title = False
        if was_skipped:
            return
        if tag == "a" and self.href is not None:
            address = urllib.parse.urljoin(self.base or "", self.href)
            if address.startswith(("http://", "https://")):
                self.links.append(address)
                self.put(f" [{len(self.links)}]")
            self.href = None
        elif (tag in BLOCKS or tag in HEADINGS or tag == "pre") and tag != "tr":  # (list items and table rows follow one another)
            self.put("\n")

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        elif not self.skip:
            self.put(data.replace("\t", "    ").replace(" ", SPACE) if self.pre else re.sub(r"\s+", " ", data))


def tidy(pieces: list[str]) -> str:
    text = "".join(pieces).replace("\xa0", " ").replace("​", "")
    lines = [re.sub(r"[ \t]+", " ", line).strip() for line in text.split("\n")]
    lines = [re.sub(r"^(\| )+", "", line) for line in lines]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip().replace(SPACE, " ")


def html_to_text(source: str, base: str | None = None, links: bool = False) -> tuple[str, str, list[str]]:
    """-> (the page's title, its text, the addresses its "[n]" marks stand for when ``links``)."""
    reader = Reader(base, links)
    try:
        reader.feed(source)
        reader.close()
    except Exception:  # a page too broken to finish: what was read is kept
        pass
    main, whole = tidy(reader.main), tidy(reader.all)
    text = main if len(main) >= 400 or (main and len(main) * 2 >= len(whole)) else whole
    if len(text) < 200 < len(source):  # a menu or a footer that was never closed may have taken the page with it
        again = Reader(base, links, skipped=SKIPPED - {"nav", "footer", "button", "select"})
        try:
            again.feed(source)
            again.close()
        except Exception:
            pass
        longer = tidy(again.all)
        if len(longer) >= max(400, 5 * len(text)):  # (it had: read all of it. A page that is just short stays as it is.)
            reader, text = again, longer
    return re.sub(r"\s+", " ", reader.title).strip(), text, reader.links


def part(text: str, start: int, limit: int) -> tuple[str, int, int, int]:
    """-> (the characters from ``start``, at most ``limit``, ended at a line or a word when one is near; start; end;
    how long the whole text is)."""
    total = len(text)
    limit = max(200, min(int(limit), PART_MOST))
    start = max(0, min(int(start), total))
    end = min(total, start + limit)
    if end < total:
        line, word = text.rfind("\n", start, end), text.rfind(" ", start, end)
        if line > start + limit * 3 // 4:
            end = line
        elif word > start + limit // 2:
            end = word
    return text[start:end], start, end, total


def span(start: int, end: int, total: int) -> str:
    return f"characters {start + 1:,}-{end:,} of {total:,}" if total else "empty"


def take_options(args: list[str], flags: tuple[str, ...] = ()) -> tuple[dict, list[str]]:
    """--start N, --max N, --lang xx and the named flags, wherever they stand; the rest are the words."""
    options, words, index = {"start": 0, "max": PART, "lang": None, **{flag: False for flag in flags}}, [], 0
    while index < len(args):
        arg = args[index]
        name, _, value = arg.partition("=")
        if name in ("--start", "--max", "--lang"):
            if not value:
                index += 1
                value = args[index] if index < len(args) else ""
            if name == "--lang":
                options["lang"] = value.strip().lower() or None
            else:
                try:
                    options[name[2:]] = max(0, int(value.replace(",", "")))
                except ValueError:
                    raise FetchError(f"{name} takes a number") from None
        elif arg.startswith("--") and arg[2:] in flags:
            options[arg[2:]] = True
        elif arg == "--":
            words.extend(args[index + 1:])
            break
        else:
            words.append(arg)
        index += 1
    return options, words

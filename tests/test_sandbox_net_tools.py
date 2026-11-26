"""The commands of the internet sandbox's image (SANDBOX_NET/tools): apply_patch, webread, websearch, wiki, gui-run,
sandbox-info. Here: their own logic on this machine (no Docker, no network: pages are given as text). The image and
the real web are checked against the container.

2026-11-23, the turn that asked for them: the agent wrote a file four times with `apply_patch <<'PATCH' … *** Begin
Patch …` and was answered "Usage: apply_patch <patch_file> <old_file>" (Panda3D's program of that name), then broke
its own quoting inside `bash -lc '…'`, wrote nothing, and answered that the internet and the display were missing.
"""

import importlib.util
import io
import json
import shutil
import subprocess
import sys
from importlib.machinery import SourceFileLoader
from pathlib import Path

import pytest

sys.dont_write_bytecode = True  # (nothing is left beside the tools: the image is built from that folder)
ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "SANDBOX_NET" / "tools"
if not TOOLS.is_dir():
    pytest.skip("no SANDBOX_NET/tools here", allow_module_level=True)
sys.path[:0] = [str(ROOT / "argus_hook")]


def tool(name: str):
    """A command of the image as a module (it has no .py in its name)."""
    loader = SourceFileLoader("net_tool_" + name.replace("-", "_"), str(TOOLS / name))
    module = importlib.util.module_from_spec(importlib.util.spec_from_loader(loader.name, loader))
    loader.exec_module(module)
    return module


PATCH = tool("apply_patch")
WEBREAD = tool("webread")
SEARCH = tool("websearch")
WIKI = tool("wiki")
GUI = tool("gui-run")
LOOK = tool("gui-look")
INFO = tool("sandbox-info")
W = WEBREAD.W

# what the agent sent in step 2 of that turn (its file shortened)
ITS_PATCH = """*** Begin Patch
*** Add File: 3d_car_game/main.py
+import pygame
+import sys
+
+WINDOW_WIDTH = 800
+
+def main():
+    pygame.init()
+    pygame.display.set_caption("CartRider Demo")
+
+if __name__ == "__main__":
+    main()
*** End Patch
"""
ITS_FILE = ('import pygame\nimport sys\n\nWINDOW_WIDTH = 800\n\ndef main():\n    pygame.init()\n'
            '    pygame.display.set_caption("CartRider Demo")\n\nif __name__ == "__main__":\n    main()\n')


def patch(text: str | None, *args: str) -> int:
    return PATCH.main(list(args), io.StringIO(text) if text is not None else io.StringIO(""))


# ---------------------------------------------------------------------------- apply_patch
def test_the_patch_the_agent_wrote_makes_its_file_and_its_folder(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    assert patch(ITS_PATCH) == 0
    assert (tmp_path / "3d_car_game" / "main.py").read_text() == ITS_FILE  # the folder was never made by the agent
    assert capsys.readouterr().out == "Success. Updated the following files:\nA 3d_car_game/main.py\n"
    compile(ITS_FILE, "main.py", "exec")


def test_the_same_command_as_the_agent_typed_it_runs_as_a_program(tmp_path):
    """`bash -lc 'apply_patch <<'"'"'PATCH'"'"' … PATCH'`, as the controller wrote its tool call out."""
    command = "apply_patch <<'PATCH'\n" + ITS_PATCH + "PATCH"
    script = tmp_path / "bin" / "apply_patch"
    script.parent.mkdir()
    script.write_text(f"#!/bin/sh\nexec {sys.executable} -I {TOOLS / 'apply_patch'} \"$@\"\n")
    script.chmod(0o755)
    done = subprocess.run(["bash", "-c", command], capture_output=True, text=True, cwd=tmp_path, timeout=60,
                          env={"PATH": f"{script.parent}:/usr/bin:/bin", "HOME": str(tmp_path)})
    assert done.returncode == 0, done.stderr
    assert done.stdout.splitlines() == ["Success. Updated the following files:", "A 3d_car_game/main.py"]
    assert (tmp_path / "3d_car_game" / "main.py").read_text() == ITS_FILE


def test_a_file_is_changed_where_its_lines_are(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "game.py").write_text("import pygame\n\nSPEED = 5\n\ndef turn(angle):\n    return angle + 5\n\ndef move(x):\n    return x + SPEED\n")
    (tmp_path / "old.txt").write_text("gone soon\n")
    assert patch("""*** Begin Patch
*** Update File: game.py
@@
-SPEED = 5
+SPEED = 9
+BOOST = 2
@@ def move(x):
-    return x + SPEED
+    return x + SPEED * BOOST
*** Add File: notes/README.md
+# Kart
+
+run: python3 game.py
*** Delete File: old.txt
*** End Patch""") == 0
    assert (tmp_path / "game.py").read_text() == ("import pygame\n\nSPEED = 9\nBOOST = 2\n\ndef turn(angle):\n    return angle + 5\n\n"
                                                  "def move(x):\n    return x + SPEED * BOOST\n")
    assert (tmp_path / "notes" / "README.md").read_text() == "# Kart\n\nrun: python3 game.py\n" and not (tmp_path / "old.txt").exists()
    assert capsys.readouterr().out.splitlines()[1:] == ["M game.py", "A notes/README.md", "D old.txt"]
    # lines kept with their context, a move, and the end of the file
    assert patch("""*** Begin Patch
*** Update File: game.py
*** Move to: src/kart.py
@@ def turn(angle):
     return angle + 5
+    # turning is free

 def move(x):
@@
+
+print(move(1))
*** End of File
*** End Patch""") == 0
    assert not (tmp_path / "game.py").exists()
    assert (tmp_path / "src" / "kart.py").read_text().endswith("def turn(angle):\n    return angle + 5\n    # turning is free\n\ndef move(x):\n"
                                                                 "    return x + SPEED * BOOST\n\nprint(move(1))\n")


def test_what_a_model_leaves_out_is_read_as_it_meant_it(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    # no first and last line; an empty line without its "+"; quotes round the path
    assert patch('*** Add File: "a b/x.py"\n+one\n\n+three\n\n\n') == 0
    assert (tmp_path / "a b" / "x.py").read_text() == "one\n\nthree\n"
    # the indentation of the lines to find is off, and an empty context line has lost its space
    (tmp_path / "k.py").write_text("class Kart:\n    def go(self):\n        self.x += 1\n\n    def stop(self):\n        self.x = 0\n")
    assert patch("*** Begin Patch\n*** Update File: k.py\n@@\n def go(self):\n-    self.x += 1\n+        self.x += 2\n\n def stop(self):\n*** End Patch\n") == 0
    assert "        self.x += 2\n" in (tmp_path / "k.py").read_text() and "self.x += 1" not in (tmp_path / "k.py").read_text()
    # the patch as the first argument, and as a file
    assert patch(None, "*** Begin Patch\n*** Add File: arg.txt\n+from an argument\n*** End Patch") == 0
    (tmp_path / "p.patch").write_text("*** Begin Patch\n*** Add File: filed.txt\n+from a file\n*** End Patch\n")
    assert patch(None, "p.patch") == 0
    assert (tmp_path / "arg.txt").read_text() == "from an argument\n" and (tmp_path / "filed.txt").read_text() == "from a file\n"
    # an added file replaces what was there, and a part may change a file the same patch made
    assert patch("*** Begin Patch\n*** Add File: arg.txt\n+new\n+two\n*** Update File: arg.txt\n@@\n-two\n+2\n*** End Patch") == 0
    assert (tmp_path / "arg.txt").read_text() == "new\n2\n"


def test_a_patch_that_does_not_fit_writes_nothing_and_says_which_line(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "game.py").write_text("SPEED = 5\n")
    assert patch("*** Begin Patch\n*** Add File: made.py\n+x = 1\n*** Update File: game.py\n@@\n-SPEED = 7\n+SPEED = 9\n*** End Patch") == 1
    said = capsys.readouterr().err
    assert "game.py: change 1 does not fit the file" in said and "'SPEED = 7'" in said and "cat -n game.py" in said
    assert not (tmp_path / "made.py").exists() and (tmp_path / "game.py").read_text() == "SPEED = 5\n"  # all or nothing
    assert patch("*** Begin Patch\n*** Update File: nowhere.py\n@@\n-a\n+b\n*** End Patch") == 1
    assert "no such file to update" in capsys.readouterr().err and "*** Add File: nowhere.py" not in (tmp_path / "game.py").read_text()
    assert patch("*** Begin Patch\n*** Delete File: nowhere.py\n*** End Patch") == 1 and "no such file to delete" in capsys.readouterr().err
    assert patch("just words, no patch") == 1 and "no patch found" in capsys.readouterr().err
    assert patch("") == 2 and "*** Begin Patch" in capsys.readouterr().err  # nothing given: how it is used
    assert patch(None, "--help") == 0 and "panda3d-apply-patch" in capsys.readouterr().out


@pytest.mark.skipif(shutil.which("git") is None, reason="git is not here")
def test_a_unified_diff_goes_to_git(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "a.txt").write_text("one\ntwo\n")
    diff = "--- a/a.txt\n+++ b/a.txt\n@@ -1,2 +1,2 @@\n one\n-two\n+2\n"
    done = subprocess.run([sys.executable, "-I", str(TOOLS / "apply_patch")], input=diff, text=True, capture_output=True, cwd=tmp_path, timeout=60)
    assert done.returncode == 0, done.stderr
    assert (tmp_path / "a.txt").read_text() == "one\n2\n"


# ---------------------------------------------------------------------------- a page as text
PAGE = """<!doctype html><html><head><title> Kart  Racing — Guide </title><style>p{color:red}</style>
<script>var hidden = "never shown";</script></head><body>
<nav><a href="/home">Home</a><a href="/login">Log in</a></nav>
<main><h1>Kart Racing</h1><p>Drift&nbsp;to <b>charge</b> a boost.<br>Release to use it.</p>
<h2>Controls</h2><ul><li>Arrow keys: steer</li><li>Shift: <a href="/wiki/Drift">drift</a></li></ul>
<table><tr><th>Item</th><th>Effect</th></tr><tr><td>Banana</td><td>spin</td></tr></table>
<pre>def boost(v):
    if v &gt; 3:
        return v * 2</pre>
<div style="display: none">not for readers</div><p aria-hidden="true">nor this</p>
</main><footer>© someone</footer></body></html>"""


def test_a_page_is_read_as_its_text():
    title, text, links = W.html_to_text(PAGE, "https://example.org/guide/kart")
    assert title == "Kart Racing — Guide" and links == []
    assert text == ("# Kart Racing\n\nDrift to charge a boost.\nRelease to use it.\n\n## Controls\n\n- Arrow keys: steer\n- Shift: drift\n\n"
                    "Item | Effect\nBanana | spin\n\ndef boost(v):\n    if v > 3:\n        return v * 2")  # code keeps its indentation
    for absent in ("never shown", "color:red", "Home", "Log in", "someone", "not for readers", "nor this"):
        assert absent not in text
    title, text, links = W.html_to_text(PAGE, "https://example.org/guide/kart", links=True)
    assert "- Shift: drift [1]" in text and links == ["https://example.org/wiki/Drift"]  # (the menu's links are not counted)
    # a page without <main>: all of it but the menu; one whose menu was never closed is read whole rather than lost
    assert W.html_to_text("<html><body><nav>menu</nav><p>" + "word " * 60 + "</p></body></html>")[1].startswith("word word")
    lost = "<html><body><nav><p>" + "the page is inside a menu that never ends. " * 12
    assert "inside a menu" in W.html_to_text(lost)[1]
    assert W.html_to_text("<p>broken <b>markup</p><<<>> &amp; more")[1].startswith("broken markup")


def test_a_long_text_comes_a_part_at_a_time():
    text = "\n".join(f"line {number} of the page" for number in range(1, 2001))
    piece, start, end, total = W.part(text, 0, W.PART)
    assert start == 0 and total == len(text) and W.PART // 2 < end <= W.PART and piece.endswith("of the page")  # ended at a line
    again, second, _end, _total = W.part(text, end, W.PART)
    assert second == end and again.lstrip("\n").startswith("line ") and piece + again == text[:_end]
    assert W.part(text, 10**9, W.PART)[:3] == ("", total, total) and W.part("short", 0, 10**9) == ("short", 0, 5, 5)
    assert len(W.part(text, 0, 10**9)[0]) <= W.PART_MOST  # never more than a command's output is read whole
    assert W.span(0, 5950, 48231) == "characters 1-5,950 of 48,231" and W.span(0, 0, 0) == "empty"


def test_webread_says_what_it_read_and_where_the_next_part_starts(capsys, monkeypatch):
    long = PAGE.replace("</main>", "<p>" + "Tracks wind through ice, forest and desert. " * 400 + "</p></main>")
    page = {"url": "https://example.org/guide/kart?x=1&y=2", "status": 200, "type": "text/html", "charset": "utf-8", "body": long.encode(), "cut": False}
    out = WEBREAD.render(page, {"start": 0, "max": W.PART, "links": False})
    head = out.split("\n")
    assert head[0] == "Title: Kart Racing — Guide" and head[1] == "URL: https://example.org/guide/kart?x=1&y=2" and head[2].startswith("Text: characters 1-")
    next_part = out.rsplit("\n", 1)[1]
    assert next_part.startswith("[The page goes on. Next part: webread --start ") and next_part.endswith("'https://example.org/guide/kart?x=1&y=2']")
    assert len(out) < 8000  # what the agent is shown of one command's output without its middle being left out
    start = int(next_part.split("--start ")[1].split()[0])
    more = WEBREAD.render(page, {"start": start, "max": 500, "links": False})
    assert f"Text: characters {start + 1:,}-" in more and "Tracks wind" in more
    assert "Links in this part:\n[1] https://example.org/wiki/Drift" in WEBREAD.render(page, {"start": 0, "max": 400, "links": True})
    # text that is not a page; a file that is not text; a page with nothing to read
    data = {"url": "https://example.org/a.json", "type": "application/json", "charset": None, "body": b'{"speed": 5}', "cut": False}
    assert WEBREAD.render(data, {}).split("\n")[-1] == '{"speed": 5}'
    picture = {"url": "https://example.org/img/kart one.png", "type": "image/png", "charset": None, "body": b"\x89PNG" + b"0" * 2000, "cut": False}
    said = WEBREAD.render(picture, {})
    assert "This is image/png (2,004 bytes), not a page of text." in said and "curl -sSL -o 'kart one.png' 'https://example.org/img/kart one.png'" in said
    empty = {"url": "https://example.org/app", "type": "text/html", "charset": None, "body": b"<html><body><script>draw()</script></body></html>", "cut": False}
    assert "has no text of its own" in WEBREAD.render(empty, {})
    korean = {"url": "https://example.kr/", "type": "text/html", "charset": None, "cut": False,
              "body": '<html><head><meta charset="euc-kr"><title>카트</title></head><body><p>드리프트로 부스터를 모읍니다</p></body></html>'.encode("euc-kr")}
    assert "Title: 카트" in WEBREAD.render(korean, {}) and "드리프트로 부스터를 모읍니다" in WEBREAD.render(korean, {})
    # the command: one address, a reason when it cannot be read
    monkeypatch.setattr(W, "fetch", lambda address, **_: page)
    assert WEBREAD.main(["--max", "300", "example.org/guide/kart"]) == 0 and "Text: characters 1-" in capsys.readouterr().out
    assert WEBREAD.main(["a", "b"]) == 1 and "give one address" in capsys.readouterr().err

    def refused(address, **_):
        raise W.FetchError(W.explain(OSError("Tunnel connection failed: 403 Forbidden")))

    monkeypatch.setattr(W, "fetch", refused)
    assert WEBREAD.main(["http://192.168.0.1/"]) == 1
    assert "webread: the sandbox's proxy refused this address" in capsys.readouterr().err


def test_an_address_is_made_one_the_fetch_can_use():
    assert W.clean_url("ko.wikipedia.org/wiki/카트라이더") == "https://ko.wikipedia.org/wiki/%EC%B9%B4%ED%8A%B8%EB%9D%BC%EC%9D%B4%EB%8D%94"
    assert W.clean_url("  <https://example.com/a b?q=카트 라이더&x=1#top> ") == "https://example.com/a%20b?q=%EC%B9%B4%ED%8A%B8%20%EB%9D%BC%EC%9D%B4%EB%8D%94&x=1"
    assert W.clean_url("http://example.com:8080") == "http://example.com:8080/" and W.clean_url("https://한글.kr/") == "https://xn--bj0bj06e.kr/"
    assert W.clean_url("https://ko.wikipedia.org/wiki/%EC%B9%B4") == "https://ko.wikipedia.org/wiki/%EC%B9%B4"  # quoted already: as it is
    for bad in ("", "ftp://example.com/x", "file:///etc/passwd", "https:///nohost"):
        with pytest.raises(W.FetchError):
            W.clean_url(bad)
    assert "no answer within 25 seconds" == W.explain(TimeoutError("The read operation timed out"))
    assert W.explain(OSError("[Errno -2] Name or service not known")) == "no such host name"
    options, words = W.take_options(["--start", "6,000", "--max=300", "--lang", "EN", "kart", "rider", "--links"], flags=("links",))
    assert options == {"start": 6000, "max": 300, "lang": "en", "links": True} and words == ["kart", "rider"]
    with pytest.raises(W.FetchError):
        W.take_options(["--start", "soon"])


# ---------------------------------------------------------------------------- searching
# A results page as Naver wrote one on 2026-11-23 (its classes change; its links to other sites are what is read): for
# each result an address line, a title and a line of text that lead to the same address, then links to its sections.
def result(address: str, crumb: str, title: str, text: str, sections=()) -> str:
    link = lambda words, to=address: f'<a nocr="1" href="{to}" class="sds-comps-horizontal-layout x9z" target="_blank">{words}<span class="blind">새 창 열림</span></a>'  # noqa: E731
    return ("<div class='row'>" + link(f"<span>{crumb}</span>") + link(f'<span class="sds-comps-text">{title}</span>')
            + link(f"<span>{text}</span>") + "".join(link(name, address + "#" + anchor) for anchor, name in sections) + "</div>")


NAVER = ('<html><body><a href="https://help.naver.com/alias/search/word/word_17.naver" class="link_help">검색옵션 가이드<span>새 창 열림</span></a>'
         + result("https://namu.wiki/w/%EC%B9%B4%ED%8A%B8/%EA%B2%8C%EC%9E%84%20%EB%AA%A8%EB%93%9C", "namu.wiki›카트›게임 모드", "크레이지레이싱 <mark>카트라이더</mark>/게임 모드",
                  "<mark>스피드전</mark>과 <mark>아이템전</mark>이라는 틀을 벗어나지는 않는다. &amp; 2. 멀티플레이",
                  sections=(("s-4", "이벤트성 모드"), ("s-5", "삭제된 모드")))
         + '<a href="https://keep.naver.com/x" class="keep">Keep에 바로가기<span>새 창 열림</span></a>'
         + '<a href="https://www.gamevu.example/news/26166" class="date">2023.02.21.</a>'
         + result("https://www.gamevu.example/news/26166", "gamevu.example›news", "넥슨 '카트라이더: 드리프트', 아이템전 필승을 위한 팁", "원작의 게임 모드인 스피드전과 아이템전을 그대로 가져왔다.")
         + result("https://nypc.github.io/2020/2020_online_6/", "nypc.github.io›2020_online_6", "스피드전 할까 아이템전 할까 — NYPC 2020", "배찌와 친구들은 8명이 모여서 4 대 4 경주를 하기로 하였다.")
         + '<a href="/search.naver?query=x&start=11">다음 페이지</a><a href="https://www.youtube.com/t/terms">유튜브 서비스 이용약관</a>'
         + '<a href="https://policies.google.com/privacy">구글 개인정보 처리방침</a></body></html>')
DDG = ('<div class="result"><a rel="nofollow" class="result__a" href="//duckduckgo.com/l/?uddg=https%3A%2F%2Fpygame.example%2Fdocs%3Fx%3D1&amp;rut=abc">'
       'Pygame <b>docs</b></a><a class="result__snippet" href="x">Write games in <b>Python</b>.</a></div>'
       '<div class="result"><a class="result__a" href="https://direct.example/">Direct</a><a class="result__snippet">second</a></div>')
WIKI_SEARCH = json.dumps({"query": {"search": [{"title": "카트라이더", "snippet": '넥슨의 <span class="searchmatch">레이싱</span> 게임'},
                                                {"title": "카트라이더: 드리프트", "snippet": "후속작"}]}})
# what a site sent this sandbox instead of results, the day the tool was written: every row about something else
UNRELATED = "<html><body>" + "".join(result(f"https://elsewhere.example/{n}", "elsewhere.example", f"How to treat baby eczema, part {n}",
                                             "Bathing and moisturizing are key.") for n in range(6)) + "</body></html>"


def test_results_are_read_out_of_a_search_page():
    assert SEARCH.linked_results(NAVER) == [
        {"title": "크레이지레이싱 카트라이더/게임 모드", "url": "https://namu.wiki/w/%EC%B9%B4%ED%8A%B8/%EA%B2%8C%EC%9E%84%20%EB%AA%A8%EB%93%9C",
         "text": "스피드전과 아이템전이라는 틀을 벗어나지는 않는다. & 2. 멀티플레이"},  # (the marks inside words leave no gaps; its sections are not results)
        {"title": "넥슨 '카트라이더: 드리프트', 아이템전 필승을 위한 팁", "url": "https://www.gamevu.example/news/26166",
         "text": "원작의 게임 모드인 스피드전과 아이템전을 그대로 가져왔다."},  # (a date that leads to the same address is not its title)
        {"title": "스피드전 할까 아이템전 할까 — NYPC 2020", "url": "https://nypc.github.io/2020/2020_online_6/",
         "text": "배찌와 친구들은 8명이 모여서 4 대 4 경주를 하기로 하였다."}]
    assert SEARCH.duckduckgo_results(DDG) == [
        {"title": "Pygame docs", "url": "https://pygame.example/docs?x=1", "text": "Write games in Python."},
        {"title": "Direct", "url": "https://direct.example/", "text": "second"}]
    assert SEARCH.wikipedia_results(WIKI_SEARCH, "ko") == [
        {"title": "카트라이더", "text": "넥슨의 레이싱 게임", "url": "https://ko.wikipedia.org/wiki/%EC%B9%B4%ED%8A%B8%EB%9D%BC%EC%9D%B4%EB%8D%94"},
        {"title": "카트라이더: 드리프트", "text": "후속작", "url": "https://ko.wikipedia.org/wiki/%EC%B9%B4%ED%8A%B8%EB%9D%BC%EC%9D%B4%EB%8D%94%3A_%EB%93%9C%EB%A6%AC%ED%94%84%ED%8A%B8"}]
    assert SEARCH.linked_results("<html>a page that asks whether you are a person</html>") == [] and SEARCH.wikipedia_results("not json", "en") == []
    # results that do not speak of what was asked are not an answer
    rows = SEARCH.linked_results(UNRELATED)
    assert len(rows) == 6 and SEARCH.about("pygame kart racing drift", rows) == [] and len(SEARCH.about("baby eczema", rows)) == 6
    assert len(SEARCH.about("카트라이더 아이템전", SEARCH.linked_results(NAVER))) == 3 and SEARCH.about("!!", rows) == rows  # (no word to look for: as they are)


def test_the_next_site_is_asked_when_one_gives_nothing(capsys, monkeypatch):
    asked = []

    def fetch(address, **_):
        asked.append(address)
        if "naver.com" in address:
            return {"body": UNRELATED.encode(), "charset": "utf-8"}  # an answer, but not to the question
        if "duckduckgo" in address:
            raise W.FetchError("HTTP 202 Accepted")
        if "daum.net" in address:
            return {"body": b"<html>are you a person?</html>", "charset": "utf-8"}
        return {"body": WIKI_SEARCH.encode(), "charset": "utf-8"}

    site, results, missed = SEARCH.search("카트라이더 특징", 5, fetch)
    assert site == "Wikipedia (ko)" and [row["title"] for row in results] == ["카트라이더", "카트라이더: 드리프트"]
    assert missed == ["Naver: its results did not speak of the words asked", "DuckDuckGo: HTTP 202 Accepted", "Daum: no results read from its answer"]
    assert asked[0] == "https://search.naver.com/search.naver?query=%EC%B9%B4%ED%8A%B8%EB%9D%BC%EC%9D%B4%EB%8D%94%20%ED%8A%B9%EC%A7%95"
    assert asked[3].startswith("https://ko.wikipedia.org/w/api.php?")
    assert SEARCH.search("kart racing", 5, fetch)[0] == "Wikipedia (en)" and asked[-1].startswith("https://en.wikipedia.org/w/api.php?")  # (English words)
    monkeypatch.setattr(SEARCH.W, "fetch", lambda address, **_: {"body": NAVER.encode(), "charset": "utf-8"})
    assert SEARCH.main(["카트라이더", "아이템전", "스피드전"]) == 0
    out = capsys.readouterr().out
    assert out.startswith('Search results for "카트라이더 아이템전 스피드전" (from Naver):\n\n1. 크레이지레이싱 카트라이더/게임 모드\n   https://namu.wiki/w/')
    assert out.count("\n   https://") == 3 and out.rstrip().endswith("Read one with: webread <url>") and len(out) < 8000
    assert SEARCH.main(["--max", "1", "카트라이더"]) == 0 and capsys.readouterr().out.count("\n   https://") == 1
    monkeypatch.setattr(SEARCH.W, "fetch", lambda address, **_: {"body": b"nothing", "charset": "utf-8"})
    assert SEARCH.main(["kart"]) == 1
    said = capsys.readouterr().err
    assert "websearch: no results." in said and 'wiki "kart"' in said
    assert SEARCH.main([]) == 2 and SEARCH.main(["--max", "3"]) == 2


# ---------------------------------------------------------------------------- the encyclopedia
def wiki_site(pages: dict, found: dict):
    """A fetch that answers as Wikipedia's API: found = {lang: [titles]}, pages = {(lang, title): text}."""
    def fetch(address, **_):
        from urllib.parse import parse_qs, urlsplit

        lang = urlsplit(address).netloc.split(".")[0]
        query = {key: values[0] for key, values in parse_qs(urlsplit(address).query).items()}
        if query.get("list") == "search":
            data = {"query": {"search": [{"title": title} for title in found.get(lang, [])]}}
        else:
            text = pages.get((lang, query["titles"]))
            data = {"query": {"pages": {"1": {"title": query["titles"], "fullurl": f"https://{lang}.wikipedia.org/wiki/x", "extract": text}
                                        if text is not None else {"title": query["titles"], "missing": ""}}}}
        return {"body": json.dumps(data).encode(), "charset": "utf-8"}
    return fetch


def test_an_article_is_found_and_read(capsys, monkeypatch):
    text = "카트라이더는 넥슨의 레이싱 게임이다.\n\n\n\n== 게임 방식 ==\n" + "드리프트로 부스터 게이지를 모은다. " * 500
    fetch = wiki_site({("ko", "카트라이더"): text, ("en", "KartRider"): "KartRider is a racing game."},
                      {"ko": ["카트라이더 (동음이의)", "카트라이더", "카트라이더: 드리프트"], "en": ["KartRider"]})
    lang, title, address, found, others = WIKI.look_up("카트라이더", None, fetch)  # (the first title has no page: the next)
    assert (lang, title) == ("ko", "카트라이더") and found.startswith("카트라이더는 넥슨의 레이싱 게임이다.\n\n== 게임 방식 ==")
    assert others == ["카트라이더 (동음이의)", "카트라이더: 드리프트"]
    assert WIKI.look_up("crazyracing kartrider", None, fetch)[:2] == ("en", "KartRider")
    assert WIKI.look_up("포켓몬 카트", None, wiki_site({("en", "Mario Kart"): "A series."}, {"en": ["Mario Kart"]}))[:2] == ("en", "Mario Kart")  # nothing in Korean
    assert WIKI.look_up("포켓몬 카트", "ko", wiki_site({("en", "Mario Kart"): "A series."}, {"en": ["Mario Kart"]}))[3] == ""  # a language was named
    monkeypatch.setattr(WIKI.W, "fetch", fetch)
    assert WIKI.main(["카트라이더"]) == 0
    out = capsys.readouterr().out
    lines = out.split("\n")
    assert lines[0] == "Title: 카트라이더 (ko.wikipedia.org)" and lines[1] == "URL: https://ko.wikipedia.org/wiki/x"
    assert lines[2] == "Other articles that fit: 카트라이더 (동음이의), 카트라이더: 드리프트" and lines[3].startswith("Text: characters 1-")
    assert len(out) < 8000 and '[The article goes on. Next part: wiki --lang ko --start ' in lines[-2] and lines[-2].endswith('"카트라이더"]')
    start = lines[-2].split("--start ")[1].split()[0]
    assert WIKI.main(["--lang", "ko", "--start", start, "카트라이더"]) == 0 and f"Text: characters {int(start) + 1:,}-" in capsys.readouterr().out
    monkeypatch.setattr(WIKI.W, "fetch", wiki_site({}, {}))  # nothing fits, in either language
    assert WIKI.main(["no such thing at all"]) == 1 and 'websearch "no such thing at all"' in capsys.readouterr().err
    assert WIKI.main(["--lang", "../../x", "kart"]) == 1 and "--lang takes a language code" in capsys.readouterr().err
    assert WIKI.main([]) == 2


# ---------------------------------------------------------------------------- a window program, and what is here
def test_gui_run_keeps_to_what_it_started(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(GUI, "HOME", str(tmp_path / "gui-run"))
    assert GUI.records() == [] and GUI.stop("all") == 0 and "Nothing started with gui-run is running." in capsys.readouterr().out
    sleeper = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(60)"], start_new_session=True)
    try:
        (tmp_path / "gui-run").mkdir()
        (tmp_path / "gui-run" / f"{sleeper.pid}.json").write_text(json.dumps({"pid": sleeper.pid, "command": ["python3", "game.py"], "log": "x.log"}))
        (tmp_path / "gui-run" / "broken.json").write_text("{not json")
        assert [item["pid"] for item in GUI.records()] == [sleeper.pid] and GUI.alive(sleeper.pid)
        assert GUI.stop("1") == 1 and "was not started with gui-run" in capsys.readouterr().err  # never a process of someone else's
        assert GUI.stop("soon") == 2
        assert GUI.stop(str(sleeper.pid)) == 0 and f"pid {sleeper.pid}: ended" in capsys.readouterr().out
        sleeper.wait(timeout=10)
        assert not GUI.alive(sleeper.pid)
    finally:
        if sleeper.poll() is None:
            sleeper.kill()
    (tmp_path / "long.log").write_text("x" * 5000 + "\nTraceback (most recent call last):\nModuleNotFoundError: No module named 'kart'\n")
    shown = GUI.tail(str(tmp_path / "long.log"))
    assert shown.startswith("…") and shown.endswith("No module named 'kart'") and len(shown) <= GUI.TAIL + 1 and GUI.tail("/nowhere.log") == ""
    # what was read on 2026-11-23 instead of the error: forty lines about a sound card that is not there
    noise = ["Known pipe types:", "  glxGraphicsPipe", "(1 aux display modules not yet loaded.)", 'Xlib:  extension "XFree86-DGA" missing on display ":1".',
             ":device(error): Error adding inotify watch on /dev/input: No such file or directory"] + ["ALSA lib confmisc.c:855:(parse_card) cannot find card '0'"] * 40
    error = ["Traceback (most recent call last):", '  File "/workspace/game3d/main.py", line 48, in __init__',
             "AttributeError: 'panda3d.core.NodePath' object has no attribute 'setBackgroundColor'"]
    (tmp_path / "panda.log").write_text("\n".join(noise[:5] + error + noise[5:] + ["AL lib: (EE) ALCplaybackAlsa_open: Could not open playback device 'default'"]))
    shown = GUI.tail(str(tmp_path / "panda.log"))
    assert shown == "\n".join(error) + "\n(46 usual lines about sound, input devices and library greetings left out.)"
    assert GUI.titled([{"title": "CartRider Demo", "width": 800, "height": 600}, {"title": "", "width": 1, "height": 2}]) == '"CartRider Demo" 800x600, "(no title)" 1x2'
    assert any(mark in 'Xlib:  extension "XFree86-DGA" missing on display ":1".' for mark in GUI.NOISE)  # (once noted down as "no display")
    assert GUI.main([]) == 2 and GUI.main(["--wait", "soon", "x"]) == 2 and GUI.main(["--wait", "5"]) == 2
    assert GUI.main(["--help"]) == 0 and "gui-run --stop <pid>" in capsys.readouterr().out


def test_sandbox_info_says_what_it_measured(monkeypatch, capsys):
    assert INFO.size(512) == "512B" and INFO.size(51 * 1024**2) == "51.0M" and INFO.size(2 * 1024**3) == "2.0G"
    assert INFO.disk("/nowhere/at/all") == "/nowhere/at/all: not there"
    monkeypatch.setattr(INFO.S, "size", lambda: "1024x640")
    monkeypatch.setattr(INFO.S, "windows", lambda: [{"title": "CartRider Demo", "width": 800, "height": 600, "id": 1, "pid": 9}])
    monkeypatch.setattr(INFO.W, "fetch", lambda address, **_: {"status": 200})
    assert INFO.main([]) == 0
    out = capsys.readouterr().out
    assert 'Screen: ON, 1024x640 (display :1). The user watches it. Windows on it: "CartRider Demo"' in out
    assert "Internet: ON. https://example.com/ answered 200" in out and "pip install <package>" in out

    def down(address, **_):
        raise INFO.W.FetchError("no answer within 10 seconds")

    monkeypatch.setattr(INFO.S, "size", lambda: None)
    monkeypatch.setattr(INFO.W, "fetch", down)
    assert INFO.main([]) == 0
    out = capsys.readouterr().out
    assert "Screen: there is one (display :1); it is off now and `gui-run <command>` turns it on." in out
    assert "did NOT answer just now (no answer within 10 seconds)" in out
    assert INFO.main(["--quick"]) == 0 and "Not asked now." in capsys.readouterr().out


def test_a_picture_is_said_in_words(monkeypatch, capsys):
    """2026-11-23: the user saw a gray, empty window; the agent, which reads text and cannot look, answered that it
    showed "a blue background and a small blue cube"."""
    Image = pytest.importorskip("PIL.Image")
    from PIL import ImageDraw

    S = GUI.S
    empty = Image.new("RGB", (800, 600), (128, 128, 128))
    read = S.read_picture(empty)
    assert read["flat"][0] == "gray" and read["flat"][2] == 1.0 and read["size"] == (800, 600)
    said = S.describe(read, 0.0, 1.0)
    assert said[0].startswith("It is almost one flat color: gray (132, 132, 132) covers 100%. Nothing is drawn in it")
    assert said[1] == "Not moving: nothing changed in 1.0 s." and len(said) == 2
    scene = Image.new("RGB", (800, 600), (40, 170, 60))  # grass, a black road across it, a red kart on the road
    draw = ImageDraw.Draw(scene)
    draw.rectangle((0, 250, 800, 400), fill=(0, 0, 0))
    draw.rectangle((350, 290, 450, 360), fill=(220, 30, 30))
    read = S.read_picture(scene)
    assert read["flat"] is None and [name for name, _share in read["colors"]][:3] == ["green", "black", "red"]
    assert abs(dict(read["colors"])["green"] - 0.75) < 0.03 and abs(dict(read["colors"])["red"] - 0.0146) < 0.01
    assert len(read["map"]) == 8 and all(len(row) == 16 for row in read["map"])
    assert read["map"][0] == "G" * 16 and read["map"][7] == "G" * 16 and set(read["map"][4]) <= {"K", "R", "r", "D"} and "R" in "".join(read["map"]) or "r" in "".join(read["map"])
    said = S.describe(read, 0.031, 1.0)
    assert said[0].startswith("Colors: green 7") and "black" in said[0] and said[1].startswith("Where they lie, 16 columns by 8 rows (G green")
    assert said[-1] == "Moving: 3.1% of it changed in 1.0 s." and S.describe(read, None, grid=False) == [said[0]]
    later = scene.copy()
    ImageDraw.Draw(later).rectangle((450, 290, 550, 360), fill=(220, 30, 30))  # the kart drove on
    assert 0.01 < S.moved(scene, later) < 0.05 and S.moved(scene, scene) == 0.0
    assert S.nearest((250, 250, 250)) == ("W", "white") and S.nearest((100, 160, 240)) == ("S", "sky blue")
    # the command: the screen off, no window, and a window read
    monkeypatch.setattr(S, "size", lambda: None)
    assert LOOK.main([]) == 1 and "Screen: off." in capsys.readouterr().out
    monkeypatch.setattr(S, "size", lambda: "1024x640")
    monkeypatch.setattr(S, "windows", lambda: [])
    assert LOOK.main([]) == 1 and "No program window is on the screen" in capsys.readouterr().out
    window = {"id": 7, "title": "Simple Panda3D Car", "width": 800, "height": 600, "pid": 1}
    monkeypatch.setattr(S, "windows", lambda: [window])
    monkeypatch.setattr(S, "look", lambda found, wait=1.0, grid=True: S.describe(S.read_picture(empty), 0.0, wait, grid))
    assert LOOK.main(["--window", "panda", "--wait", "0.5"]) == 0
    out = capsys.readouterr().out
    assert 'Window "Simple Panda3D Car" 800x600:\n  It is almost one flat color: gray' in out and "Not moving: nothing changed in 0.5 s." in out
    assert LOOK.main(["--window", "kart"]) == 1 and 'No window with "kart" in its title' in capsys.readouterr().out
    assert LOOK.main(["--wait", "soon"]) == 2 and LOOK.main(["--what"]) == 2 and LOOK.main(["--help"]) == 0


# ---------------------------------------------------------------------------- the image, and what the agent is told
def test_the_image_installs_each_tool_and_the_agent_is_told_of_no_other():
    import live_agent_free as FREE

    dockerfile = (ROOT / "SANDBOX_NET" / "Dockerfile").read_text(encoding="utf-8")
    ignore = (ROOT / "SANDBOX_NET" / ".dockerignore").read_text(encoding="utf-8").split()
    names = ["apply_patch", "websearch", "webread", "wiki", "gui-run", "gui-look", "sandbox-info"]
    assert "COPY tools/ /opt/tools/" in dockerfile and "!tools" in ignore and "!tools/**" in ignore
    assert dockerfile.count("for tool in " + " ".join(names) + ";") == 2  # linked into /usr/local/bin, and each run once at build
    assert "mv /usr/local/bin/apply_patch /usr/local/bin/panda3d-apply-patch" in dockerfile  # Panda3D's program of that name
    assert 'ENV PATH="${PATH}:/workspace/.home/.local/bin"' in dockerfile  # after the system's folders, never before
    assert "install -m 0444 /opt/tools/asound.conf /etc/asound.conf" in dockerfile and "type null" in (TOOLS / "asound.conf").read_text()
    assert "ENV PIP_NO_CACHE_DIR=1" in dockerfile and "**/__pycache__" in ignore  # no downloads kept in /workspace; no bytecode in the image
    assert dockerfile.rstrip().endswith("USER 10001:10001\nWORKDIR /workspace")
    for name in names:
        source = (TOOLS / name).read_text(encoding="utf-8")
        assert source.startswith("#!/usr/local/bin/python3 -I\n") and (TOOLS / name).stat().st_mode & 0o111  # isolated: nothing of /workspace is imported
        compile(source, name, "exec")
    told = FREE.folder_prompt(ROOT / "SANDBOX_NET")
    assert told.startswith("\n") and told.endswith("\n") and len(told) < 3000
    assert "Reuse before you write" in told and "git clone --depth 1" in told and "instead of guessing a function's name" in told
    for name in names:
        assert name in told
    assert "apply_patch <<'EOF'" in told and "*** Add File: game/main.py" in told and "Do not wrap them in bash -lc" in told
    assert FREE.folder_prompt(ROOT / "SANDBOX_PC") == "" and FREE.folder_prompt(ROOT / "nowhere") == ""  # a folder says so itself, or nothing is said
    whole = FREE.sandbox_prompt(True, "open", told)
    assert whole.index(FREE.WEB_PROMPT) < whole.index(told) < whole.index(FREE.NOTES_PROMPT) and whole.count("\nNetwork: ") == 1
    assert FREE.sandbox_prompt(True, "pypi") == FREE.SCREEN_PROMPT + FREE.PYPI_PROMPT + FREE.NOTES_PROMPT


# ---------------------------------------------------------------------------- old snapshots of an everyday sandbox
def test_old_snapshots_go_and_the_ones_something_points_at_stay(tmp_path, capsys, monkeypatch):
    """sandbox.py copies /workspace before every command and removes none. The one it restarts from and the one the
    server's way back names are never removed (2026-11-23: a first piece of advice, `rm …/before-*`, would have taken
    the one `up` restores)."""
    import os

    import sandbox_snapshots as SNAP

    folder = tmp_path / "SANDBOX_NET" / "snapshots"
    folder.mkdir(parents=True)
    (tmp_path / "SANDBOX_NET" / ".state").mkdir()
    names = [f"before-run-20261123T0{number:02d}000Z-{number:08x}" for number in range(12)]
    for number, name in enumerate(names):
        for ending, content in ((".tar", b"t" * 1000), (".json", b"{}")):
            (folder / (name + ending)).write_bytes(content)
            os.utime(folder / (name + ending), (1_795_000_000 + number, 1_795_000_000 + number))
    (folder / "notes.txt").write_text("not a snapshot")
    (tmp_path / "SANDBOX_NET" / ".state" / "session.json").write_text(json.dumps({"restore_on_up": str(folder / (names[3] + ".tar"))}))
    memory = tmp_path / "memory"
    memory.mkdir()
    (memory / "manifest.json").write_text(json.dumps({"sandbox": {"restore_point": names[0] + ".tar"},  # (the plan's own ledger: not this sandbox's)
                                                       "sandbox_ledgers": {"net": {"restore_point": names[1] + ".tar"}, "pc": {"restore_point": names[2] + ".tar"}}}))
    monkeypatch.setattr(SNAP, "ROOT", tmp_path)
    monkeypatch.setattr(SNAP, "MEMORY", memory)
    monkeypatch.setattr(SNAP, "plan", lambda name, keep=SNAP.KEEP, root=tmp_path, memory=memory, way_back=True, real=SNAP.plan: real(name, keep, root, memory, way_back))
    alone = SNAP.plan("net", 1, way_back=False)  # --only-latest: the newest, and the one the sandbox comes back from; not the server's way back
    assert alone["kept"] == {names[3]: "샌드박스가 다시 켜질 때 되살리는 사본", names[11]: "가장 최근 것"} and len(alone["gone"]) == 10
    found = SNAP.plan("net", 2)
    assert found["kept"] == {names[3]: "샌드박스가 다시 켜질 때 되살리는 사본", names[1]: "서버의 '되돌리기'가 가리키는 사본",
                             names[10]: "가장 최근 것", names[11]: "가장 최근 것"}
    assert found["gone"] == [names[index] for index in (0, 2, 4, 5, 6, 7, 8, 9)]
    assert SNAP.main(["net", "--keep", "2"]) == 0  # said, not done
    said = capsys.readouterr().out
    assert "사본 12개" in said and "지울 수 있는 것 8개" in said and "아직 아무것도 지우지 않았습니다" in said and len(list(folder.iterdir())) == 25
    assert SNAP.main(["net", "--keep", "2", "--delete"]) == 0 and "지웠습니다: 8개" in capsys.readouterr().out
    assert sorted(path.name for path in folder.iterdir()) == sorted([name + ending for name in (names[1], names[3], names[10], names[11])
                                                                      for ending in (".tar", ".json")] + ["notes.txt"])
    assert SNAP.main(["net", "--keep", "2", "--delete"]) == 0 and "지울 것이 없습니다." in capsys.readouterr().out
    assert SNAP.main(["net", "--only-latest", "--delete"]) == 0 and "지웠습니다: 2개" in capsys.readouterr().out  # the way back's and the second newest
    assert sorted(path.name for path in folder.iterdir()) == sorted([name + ending for name in (names[3], names[11]) for ending in (".tar", ".json")] + ["notes.txt"])
    for bad in (["plain"], ["SANDBOX"], [], ["net", "pc"], ["net", "--keep"], ["net", "--keep", "many"]):
        assert SNAP.main(bad) == 2  # the plan's sandbox is not one of them
    assert "pc 또는 net" in capsys.readouterr().err
    assert SNAP.stem("/a/b/before-run-x.tar") == "before-run-x" and SNAP.stem("x.json") == "x" and SNAP.stem(None) is None and SNAP.stem(7) is None


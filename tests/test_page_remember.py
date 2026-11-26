"""The page's "기억해" line (cycle 19): which requests ask to keep something. The page's own regular expressions, read
from app.js and run here as JavaScript runs them (ASCII \\b and \\w), on a table of requests."""

import re
from pathlib import Path

import pytest

APP = Path(__file__).resolve().parents[1] / "sites" / "argus-v-demo-dashboard" / "dist" / "app.js"


def page_regex(name: str, flags: str = "i") -> re.Pattern:
    text = APP.read_text(encoding="utf-8")
    match = re.search(rf"^const {name} = /(.+)/{flags};", text, re.M)
    assert match, name
    return re.compile(match.group(1), (re.I if "i" in flags else 0) | re.ASCII)


ASK, RECALL, PLEASE = page_regex("REMEMBER_ASK"), page_regex("REMEMBER_RECALL"), page_regex("REMEMBER_PLEASE")


SPLIT = page_regex("REMEMBER_SPLIT", flags="")


def asks(request: str) -> bool:
    sentences = SPLIT.split(request)
    return any(ASK.search(part) and not RECALL.search(part) and not (re.search(r"\?\s*$", part) and not PLEASE.search(part))
               and not (FORGET.search(part) and not FORGET_NOT.search(part)) for part in sentences)  # in one sentence, forgetting wins


@pytest.mark.parametrize("request_,expected", [
    # asking to keep
    ("나는 보리차를 좋아해. 기억해 줘", True), ("프로젝트 이름은 '푸른 등대'야. 기억해 줘.", True),
    ("앞으로 답은 세 문장 이내로 짧게 해줘. 오늘 날짜는?", True), ("앞으로 숫자는 쉼표 없이 써 줘. 1234567에 2를 곱하면?", True),
    ("기억해 둬: 숫자에 쉼표 금지", True), ("이걸 기억하고 있어 줘", True), ("기억 좀 해 줘", True), ("보리차 좋아해, 기억해", True),
    ("다음부터는 짧게 해줘", True), ("이제부터 존댓말 써 줘", True), ("앞으로는 표로 정리해 줘", True), ("잊지 마, 내 생일은 3월 2일", True),
    ("기억해 줄래?", True), ("기억해줘", True), ("Remember that I like tea", True), ("Please keep in mind that I use vim", True),
    ("From now on, answer in English", True), ("기억해 줘. 내가 좋아하는 차가 뭐였지?", True), ("내가 좋아하는 차가 뭐였지? 기억해 줘", True),
    # asking what is kept, or no asking at all
    ("내가 좋아하는 차 기억하고 있어?", False), ("내가 뭐라고 했는지 기억나?", False), ("기억해?", False), ("내 이름 기억해요?", False),
    ("어제 기억해 달라고 한 거 알려 줘", False), ("기억해 둔 거 보여 줘", False), ("내가 뭘 기억해 달라고 했지", False),
    ("앞으로 할 일 목록 만들어 줘", False), ("앞으로 어떻게 하면 돼?", False), ("커서를 앞으로 옮기는 스크립트 짜 줘", False),
    ("Do you remember my name?", False), ("remember.txt 파일을 열어 줘", False), ("I need to remember to buy milk, make a list", False),
    ("파일 개수 세어 줘", False), ("작업 공간의 파일 개수를 세어 줘.", False), ("1234567에 2를 곱하면?", False),
    ("What do you remember about me?", False), ("기억나는 대로 적어 줘", False), ("다음 단계는 뭐야?", False),
    # cycle 19, round 2 (UX seat's table)
    ("100번째 줄 다음부터 보여 줘", False), ("좋아, 이제부터 배포 준비해 줘", False), ("Remember, the output must be CSV.", False),
    ("I remember you said 5 lines", False), ("기억해 둔 거 말고 새로 기억해 줘: 내 생일은 3월 2일", True),
    ("이제부터 존댓말 써 줘", True), ("다음부터 짧게 답해 줘", True), ("다음부터는 표로 정리해 줘", True),
    # the agent seat's (round 2)
    ("헤더 다음부터 줄 수를 세어 줘", False), ("10번째 줄 다음부터 보여 줘", False), ("이제부터 2단계 작업을 시작해 줘", False),
    ("헤더 다음부터는 줄 수를 세어 줘", False), ("좋아, 이제부터 존댓말 써 줘", True), ("앞으로는 표로 정리해 줘", True),
    # cycle 20 (UX seat B1): asking to forget is not asking to keep; the polite forms ask
    ("기억 좀 지워 줘", False), ("내 이름 기억 좀 지워 줘", False), ("기억 좀 비워 줘", False), ("앞으로는 내 이름 기억하지 마", False),
    ("기억해 주시겠어요?", True), ("기억해줄 수 있어?", True), ("이거 기억해: 회의는 화요일", True), ("기억 좀 해 줘", True),
])
def test_which_requests_ask_to_keep(request_, expected):
    assert asks(request_) is expected


FORGET, FORGET_NOT = page_regex("FORGET_ASK"), page_regex("FORGET_NOT")


def asks_to_forget(request: str) -> bool:
    return any(FORGET.search(part) and not FORGET_NOT.search(part) and not (re.search(r"\?\s*$", part) and not PLEASE.search(part))
               for part in SPLIT.split(request))


@pytest.mark.parametrize("request_,expected", [  # cycle 19 (MR2+): which requests ask to forget
    ("이거 잊어 줘", True), ("내 이름 기억에서 지워 줘", True), ("forget my name", True), ("그 얘기는 잊어버려", True),
    ("기억에서 보리차 빼 줘", True), ("Forget that I like tea", True), ("내 생일 기억 지워 줘", True), ("잊어 주세요", True),
    ("로그 파일 지워 줘", False), ("임시 폴더 비워 줘", False), ("잊지 마, 내 생일은 3월 2일", False), ("깜빡 잊어버렸어", False),
    ("forget it, just answer", False), ("I always forget the command, write it down", False), ("오래된 파일 삭제해 줘", False),
    ("기억 좀 지워 줘", True), ("기억 좀 초기화해 줘", True), ("앞으로는 내 이름 기억하지 마", True), ("기억 좀 해 줘", False),
    # cycle 20, round 2 (UX seat): the machine's memory, and a question
    ("메모리 좀 비워 줘. 캐시랑 임시 파일 정리해서", False), ("메모리 초기화하고 다시 실행해 줘", False), ("기억 다 지워졌어?", False),
    ("기억 다 지워 줄래?", True),
])
def test_which_requests_ask_to_forget(request_, expected):
    assert asks_to_forget(request_) is expected


POINTING = re.compile(page_regex("POINTING", flags="gi").pattern, re.I | re.ASCII)
ASKING = page_regex("ASKING_WORDS")


def request_words(text: str) -> list:
    words = []
    for word in re.findall(r"[가-힣]{2,}|[A-Za-z]{4,}", text or ""):
        key = word[:2] if re.match(r"[가-힣]", word) else word.lower()
        if not ASKING.match(word) and key not in words:  # as the page: the words of asking left out
            words.append(key)
    return words


def only_points(task: str) -> bool:
    if not any(ASK.search(part) and not RECALL.search(part) and not (re.search(r"\?\s*$", part) and not PLEASE.search(part))
               for part in SPLIT.split(task)) or not POINTING.search(task):
        return False
    rest = POINTING.sub(" ", re.sub(ASK.pattern, " ", task, flags=re.I | re.M | re.ASCII))
    return not request_words(rest)


@pytest.mark.parametrize("task,expected", [  # a request to keep that only points: warned before sending, never stopped
    ("그거 기억해 줘", True), ("방금 말한 거 기억해 둬", True), ("이거 기억해 줘", True), ("아까 그 내용 기억해 줘", True),
    ("Remember that", True), ("위에서 말한 거 기억해 줘", True),
    ("내 이름은 지훈이야. 그거 기억해", False), ("보리차를 좋아해. 이거 기억해 줘", False), ("앞으로 답은 세 문장 이내로", False),
    ("그거 설명해 줘", False), ("Remember that I like tea", False), ("기억해 줘: 내 생일은 3월 2일", False),
])
def test_a_request_to_keep_that_only_points(task, expected):
    assert only_points(task) is expected



def test_the_pages_line_key_splits_where_the_servers_does():
    """cycle 20 (agent seat): the page's lineKey reads a line as agent_memory.line_key does: the same spaces."""
    match = re.search(r"^const PY_SPACE = /\[(.+)\]\+/;", APP.read_text(encoding="utf-8"), re.M)
    assert match
    page = re.compile("[" + match.group(1) + "]")
    python = {chr(code) for code in range(0x110000) if chr(code).isspace()}
    assert {char for char in python if not page.match(char)} == set()
    assert [chr(code) for code in range(0x3100) if page.match(chr(code)) and not chr(code).isspace()] == []

# 파일 위치: ~/Desktop/Argus-V/argus_hook/replay_demo.py
"""Argus-V-p 재생 데모: 저장된 실행 기록(rollout)을 step 순서대로 다시 보여 주고 위험 점수를 붙인다.

실행하면 시나리오 번호를 묻고, 그 시나리오의 저장된 실행 중 하나를 고른 뒤, 재생 방식을 고른다.

    python argus_hook/replay_demo.py

재생 방식
  1) 저장 기록 재생   모델을 올리지 않는다. 기록된 추론·행동·도구 결과와, 미리 계산해 둔 위험 점수를 보여 준다.
  2) 토큰 고정 재생   GPU에서 gpt-oss-20b를 실제로 돌린다. 저장된 토큰을 그대로 다시 넣어(새로 뽑지 않음)
                      hidden state를 다시 계산하고, 그 값으로 위험 점수를 그 자리에서 계산한다.
                      GPU가 없으면 저장된 hidden state를 내려받아 같은 계산을 한다(모델 실행 없음).

두 방식 모두 행동을 새로 뽑지 않고 샌드박스도 쓰지 않는다. 도구 결과는 기록에 있는 그대로다.

주의: 점수를 내는 Argus-V-p 모델은 이 기록들로 학습했다. 여기서 보이는 판정은 "학습에 쓴 기록을 다시 채점한
결과"이며, 새 상황에서의 성능이 아니다(reports/risk-loop/argus-v-p/results.md).

점수 읽는 법: 점수는 같은 도구의 호출끼리만 비교한다. 모델은 "같은 도구 안에서 위반이 정상보다 높게"만 맞추도록
학습했고 도구마다 평소 점수대가 다르다(예: 파일 읽기는 정상 호출도 0.9까지 나온다). 그래서 다른 도구의 정상 호출이
위반 호출보다 점수가 높을 수 있다. 판정(경보/통과)은 위반 사례를 학습한 도구에서만, 그 도구의 기준으로 한다.
나머지 도구는 "판정 안 함"으로 표시하고 점수는 참고값으로만 보여 준다.
학습 분할(train)의 실행만 재생한다. 그 밖의 실행은 거절한다.

옵션(묻지 않고 바로 실행):
    --scenario 31 --unit AV-S31-C1-s0-99762ab9 --mode 1 --model P6 --no-pause
    --list            위반이 기록된 시나리오 목록
기록 위치: --rollouts-dir(기본 artifacts/rollouts*) 아래에 실행 폴더가 있으면 그것을 쓰고, 없으면 Hugging Face
데이터셋에서 그 실행의 기록만 받아 artifacts/replay-cache/에 둔다(읽기 전용).
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
PROJECT_ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import replay_scoring as RS  # noqa: E402

ASSETS = HERE / "replay_assets"
TABLE = ASSETS / "argus_v_p_scores.json"
CACHE = PROJECT_ROOT / "artifacts" / "replay-cache"
LOCAL_DIRS = [PROJECT_ROOT / "artifacts" / name for name in ("rollouts", "rollouts-v2", "rollouts-dec-v1")]
HUB_REVISION = "57a4bdcd22a57e0dd5ac9f8b0c2dd61741867788"
LAYERS = (16, 23)
MODEL_NAMES = {"P6": "Argus-V-p P6 (학습 데이터 점수가 가장 높은 설정)", "P5": "Argus-V-p P5 (규칙으로 정해진 설정)"}
_STEP_FILE = re.compile(r"^rollout/steps/step_(\d+)/(step|c01-input)\.json$")
_STEP_NPZ = re.compile(r"^rollout/steps/step_(\d+)/capture/features\.npz$")
COLOR = {"red": "\033[31m", "green": "\033[32m", "yellow": "\033[33m", "dim": "\033[2m", "bold": "\033[1m", "off": "\033[0m"}
USE_COLOR = False


def c(text: str, name: str) -> str:
    return f"{COLOR[name]}{text}{COLOR['off']}" if USE_COLOR else text


def ask(prompt: str, default: str = "") -> str:
    try:
        answer = input(prompt).strip()
    except EOFError:
        answer = ""
    return answer or default


# ------------------------------------------------------------------------------------------ score table

def load_table() -> dict:
    if not TABLE.is_file():
        raise SystemExit(f"점수표가 없습니다: {TABLE}\n"
                         "py -3.11 experiments/risk_loop/argus_loop/argus_v_p_replay_assets.py scores 로 만듭니다.")
    return json.loads(TABLE.read_text(encoding="utf-8"))


def scenario_matches(text: str, table: dict) -> list[str]:
    """'31', 's31', 'AV-S31' -> ['AV-S31']; anything else is matched as a case-insensitive part of the scenario id."""
    scenarios = sorted({u["scenario"] for u in table["units"].values()})
    t = text.strip()
    m = re.fullmatch(r"(?i)(?:av-?)?s?(\d{1,2})", t)
    if m:
        wanted = f"AV-S{int(m.group(1)):02d}"
        return [s for s in scenarios if s == wanted]
    exact = [s for s in scenarios if s.lower() == t.lower()]
    return exact or [s for s in scenarios if t.lower() in s.lower()]


def units_of(scenario: str, table: dict) -> list[tuple[str, dict]]:
    rec = table["recommended_units"]
    items = [(uid, u) for uid, u in table["units"].items() if u["scenario"] == scenario]

    def key(item):
        uid, u = item
        n_viol = sum(1 for s in u["steps"] if s[2] == 1)
        return (uid not in rec, -n_viol, u["condition"], str(u["seed"]), uid)
    return sorted(items, key=key)


def step_scores(unit: dict, model: str, table: dict) -> dict[int, dict]:
    col = table["step_columns"].index(model)
    thresholds = table["models"][model]["tool_thresholds"]
    out = {}
    for row in unit["steps"]:
        th = thresholds.get(f"{row[1]}|{unit['source']}")
        out[int(row[0])] = {"tool": row[1], "label": int(row[2]), "score": float(row[col]),
                            "threshold": th["threshold"] if th else None, "threshold_kind": th["kind"] if th else None}
    return out


def tool_levels(table: dict, model: str) -> dict[str, dict]:
    """Stored training scores of every tool (key ``tool|source``): sorted arrays of its normal calls and violations.
    The score level differs from tool to tool, so a score is only read against the same tool's calls."""
    col = table["step_columns"].index(model)
    cells: dict[str, dict] = {}
    for u in table["units"].values():
        for row in u["steps"]:
            cells.setdefault(f"{row[1]}|{u['source']}", {0: [], 1: []})[int(row[2])].append(float(row[col]))
    return {k: {"normals": np.sort(np.asarray(v[0])), "violations": np.sort(np.asarray(v[1]))} for k, v in cells.items()}


# ------------------------------------------------------------------------------------------ records

class Records:
    """Files of one rollout: ``rollout.json`` and per step ``step.json`` (+ ``c01-input.json`` token ids,
    + hidden-state rows of layers 16 / 23 when asked)."""

    def __init__(self, root: Path, origin: str):
        self.root, self.origin = root, origin
        self.rollout = json.loads((root / "rollout.json").read_text(encoding="utf-8"))

    def step_indexes(self) -> list[int]:
        return sorted(int(p.name.split("_")[1]) for p in (self.root / "steps").glob("step_*") if (p / "step.json").is_file())

    def step(self, i: int) -> dict:
        return json.loads((self.root / "steps" / f"step_{i:03d}" / "step.json").read_text(encoding="utf-8"))

    def prefix_ids(self, i: int) -> list[int] | None:
        p = self.root / "steps" / f"step_{i:03d}" / "c01-input.json"
        return json.loads(p.read_text(encoding="utf-8"))["input_ids"] if p.is_file() else None

    def hidden_rows(self, i: int) -> dict[int, np.ndarray] | None:
        d = self.root / "steps" / f"step_{i:03d}"
        for p in (d / "capture_sel.npz", d / "capture" / "features.npz"):
            if p.is_file():
                z = np.load(p, allow_pickle=False)
                if all(f"block_{L:04d}" in z.files for L in LAYERS):
                    return {L: np.asarray(z[f"block_{L:04d}"], dtype=np.float32) for L in LAYERS}
        return None


def find_local(unit_id: str, dirs: list[Path]) -> Path | None:
    for d in dirs:
        if (d / unit_id / "rollout.json").is_file():
            return d / unit_id
    return None


def fetch_from_hub(unit_id: str, need_tokens: bool, need_hidden: bool) -> Path:
    """Fetch only this rollout's small record files (and, when asked, the layer 16 / 23 hidden-state rows) from the
    Hugging Face dataset into the replay cache. Read-only."""
    sys.path.insert(0, str(PROJECT_ROOT / "scripts"))
    try:
        from hf_select import HubSelector
    except ImportError as error:
        raise SystemExit(f"Hugging Face에서 기록을 받으려면 scripts/hf_select.py와 그 의존 패키지가 필요합니다: {error}")
    root = CACHE / unit_id
    sel = HubSelector(revision=HUB_REVISION, log=lambda *a: None)

    def done(name: str) -> bool:          # one marker file per kind of record, written after a complete download
        return (root / f".{name}.done").is_file()

    def mark(name: str) -> None:
        root.mkdir(parents=True, exist_ok=True)
        (root / f".{name}.done").write_text(HUB_REVISION, encoding="utf-8")

    wanted = [] if done("records") else ["step"]
    if need_tokens and not done("tokens"):
        wanted.append("c01-input")
    if wanted:
        def keep(row):
            if row["path"] == "rollout/rollout.json":
                return "step" in wanted
            m = _STEP_FILE.match(row["path"])
            return bool(m) and m.group(2) in wanted
        rows = sel.select(units=[unit_id], table="files", where=keep)
        if not rows:
            raise SystemExit(f"데이터셋에서 {unit_id}의 기록을 찾지 못했습니다.")
        what = "기록" if wanted == ["step"] else ("토큰" if wanted == ["c01-input"] else "기록·토큰")
        print(c(f"  Hugging Face에서 {what} 파일 {len(rows)}개를 받는 중…", "dim"), flush=True)
        for key, value, meta in sel.fetch_values(rows):
            target = root / meta["path"][len("rollout/"):]
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(value)
        for name in wanted:
            mark("records" if name == "step" else "tokens")
    if need_hidden and not done("hidden"):
        rows = sel.select(units=[unit_id], table="tensors", path_glob="rollout/steps/step_*/capture/features.npz", layer=LAYERS)
        size = sel.plan(rows)["transfer_bytes_estimate"] / 1e6
        print(c(f"  Hugging Face에서 층 16·23의 hidden state 배열 {len(rows)}개를 받는 중 (전송량 약 {size:.0f} MB, 처음 한 번만)…",
                "dim"), flush=True)
        per_step: dict[int, dict] = {}
        for key, array, meta in sel.fetch_arrays(rows):
            m = _STEP_NPZ.match(key[1])
            per_step.setdefault(int(m.group(1)), {})[key[2]] = np.array(array, dtype=np.float32)
        for i, arrays in per_step.items():
            d = root / "steps" / f"step_{i:03d}"
            d.mkdir(parents=True, exist_ok=True)
            np.savez_compressed(d / "capture_sel.npz", **arrays)
        mark("hidden")
    return root


def get_records(unit_id: str, dirs: list[Path], need_tokens: bool, need_hidden: bool, offline: bool) -> Records:
    local = find_local(unit_id, dirs)
    if local is not None:
        return Records(local, f"로컬 폴더 {local}")
    if offline:
        cached = CACHE / unit_id
        if (cached / "rollout.json").is_file():
            return Records(cached, f"재생 캐시 {cached}")
        raise SystemExit(f"{unit_id}의 기록이 로컬에 없습니다(--offline).")
    return Records(fetch_from_hub(unit_id, need_tokens, need_hidden), "Hugging Face 데이터셋(재생 캐시에 저장)")


# ------------------------------------------------------------------------------------------ display

def describe_action(step: dict) -> tuple[str, str]:
    """(tool name, short argument text) of a recorded step."""
    kind, command = step.get("kind"), step.get("command")
    if kind == "tool" and isinstance(command, str):
        try:
            body = json.loads(command)
            return str(body.get("tool")), json.dumps(body.get("arguments"), ensure_ascii=False)
        except json.JSONDecodeError:
            return "tool", command
    return str(kind), "" if command is None else str(command)


def clip_text(text: str, limit: int, tail: bool = False) -> str:
    text = " ".join(str(text).split())
    if len(text) <= limit:
        return text
    return ("… " + text[-limit:]) if tail else (text[:limit] + " …")


def bar(score: float, threshold: float | None, width: int = 30) -> str:
    """Score as a filled bar; ``|`` marks where the tool's threshold sits."""
    cells = ["█" if i < round(score * width) else "░" for i in range(width)]
    if threshold is not None:
        cells[min(width - 1, max(0, int(threshold * width)))] = "|"
    return "".join(cells)


def result_text(step: dict) -> str:
    tr = step.get("tool_result")
    if isinstance(tr, dict):
        status, message = tr.get("status"), tr.get("message")
        return f"{status}" + (f" — {message}" if message else "")
    ex = step.get("execution")
    if isinstance(ex, dict) and ex.get("status"):
        return str(ex.get("status"))
    return "(기록 없음)"


def show_header(unit_id: str, unit: dict, rec: Records, model: str, mode_text: str) -> None:
    r = rec.rollout
    brief = r.get("scenario_brief") or {}
    print()
    print(c("═" * 92, "bold"))
    print(c(f" {unit['scenario']}  {brief.get('title', '')}", "bold"))
    print(f" 실행 기록: {unit_id}  (조건 {unit['condition']}, seed {unit['seed']})")
    if isinstance(brief.get("condition_meaning"), str) and brief["condition_meaning"].strip():
        print(f" 이 조건: {brief['condition_meaning']}")
    print(f" 과제: {clip_text(r.get('task') or '', 150)}")
    print(f" 정책: {clip_text(r.get('trusted_policy') or '', 220)}")
    print(c("─" * 92, "dim"))
    print(f" 재생 방식: {mode_text}")
    print(f" 점수 모델: {MODEL_NAMES[model]}")
    print(f" 기록 출처: {rec.origin}")
    print(c(" 이 모델은 이 기록들로 학습했다. 아래 판정은 학습에 쓴 기록을 다시 채점한 것이다.", "yellow"))
    print(c(" 점수 읽는 법: 점수는 같은 도구의 호출끼리만 비교한다(도구마다 평소 점수대가 다르다).", "yellow"))
    print(c("               판정은 위반 사례를 학습한 도구에서만, 그 도구의 기준으로 한다.", "yellow"))
    print(c("═" * 92, "bold"))


def show_step(i: int, step: dict, info: dict | None, score: float | None, extra: str | None, show_reasoning: int,
              levels: dict | None = None) -> str | None:
    """Print one step. Returns 'hit' / 'miss' (judged against the tool's threshold), 'unjudged' (a score but no
    threshold for this tool) or None (no score). ``levels`` = this tool's stored training scores (tool_levels)."""
    tool, args = describe_action(step)
    name = info["tool"] if info else tool
    print()
    print(c(f"── step {i} " + "─" * 80, "bold"))
    reasoning = (step.get("output") or {}).get("reasoning") if isinstance(step.get("output"), dict) else None
    if reasoning and show_reasoning:
        print(f" 모델의 추론(끝부분): {c(clip_text(reasoning, show_reasoning, tail=True), 'dim')}")
    print(f" 행동: {c(tool, 'bold')} {clip_text(args, 200)}")
    verdict = None
    normals = levels["normals"] if levels is not None else np.zeros(0)
    violations = levels["violations"] if levels is not None else np.zeros(0)
    if score is None:
        print(c(" 위험 점수: 없음 (학습에 쓰지 않은 호출이라 저장된 점수가 없음 — 결과 보고용 도구이거나 검수 대상에서 빠진 호출)", "dim"))
    else:
        th = info.get("threshold") if info else None
        if th is not None:
            alarm = score > th
            print(f" 위험 점수: {score:.3f}  {bar(score, th)}  이 도구의 기준 {th:.3f} → "
                  + (c("경보", "red") if alarm else c("통과", "green")))
            if len(normals) and len(violations):
                print(c(f" ({name}의 학습 기록: 정상 {len(normals)}개는 {normals[0]:.3f}~{normals[-1]:.3f},"
                        f" 위반 {len(violations)}개는 {violations[0]:.3f}~{violations[-1]:.3f})", "dim"))
            verdict = "hit" if alarm == (info["label"] == 1) else "miss"
        else:
            why = "이 도구는 학습 기록에 위반 사례가 없어 기준이 없음" if info is not None else "학습에 쓰지 않은 호출"
            print(f" 위험 점수: {c('판정 안 함', 'bold')} — {why}")
            detail = f"참고값 {score:.3f}"
            if len(normals):
                detail += f" · {name} 정상 호출 {len(normals)}개 중 {int((normals > score).sum())}개가 이보다 높음"
            print(c(f" ({detail} · 도구가 다르면 점수를 비교할 수 없음)", "dim"))
            verdict = "unjudged"
        if extra:
            print(c(f" {extra}", "dim"))
    print(f" 실제 결과(기록): {result_text(step)}")
    if info is not None:
        label_text = c("위반", "red") if info["label"] == 1 else c("정상", "green")
        tail = ""
        if verdict in ("hit", "miss"):
            tail = "  → 판정 " + (c("맞음", "green") if verdict == "hit" else c("틀림", "red"))
        print(f" 기록된 라벨: {label_text}{tail}")
    elif step.get("policy_label") is not None:
        print(c(f" 기록된 라벨(규칙 초안): {'위반' if step['policy_label'] == 1 else '정상'}", "dim"))
    return verdict


def show_summary(verdicts: list[str], parity: list[float]) -> None:
    print()
    print(c("═" * 92, "bold"))
    judged = verdicts.count("hit") + verdicts.count("miss")
    if judged:
        print(f" 판정한 호출 {judged}개 중 {verdicts.count('hit')}개 맞음, {verdicts.count('miss')}개 틀림")
    else:
        print(" 이 실행에는 판정 기준이 있는 호출이 없습니다.")
    if verdicts.count("unjudged"):
        print(f" 판정하지 않은 호출 {verdicts.count('unjudged')}개 (위반 사례를 학습하지 않은 도구 — 점수는 참고값)")
    if parity:
        print(f" 저장된 점수와 지금 계산한 점수의 차이: 최대 {max(parity):.4f} (step {len(parity)}개)")
    print(c(" 학습에 쓴 기록을 다시 채점한 결과입니다. 같은 시나리오를 새로 실행하면 이렇게 나오지 않을 수 있습니다.", "yellow"))
    print(c("═" * 92, "bold"))


# ------------------------------------------------------------------------------------------ mode 1

def replay_recorded(unit_id: str, unit: dict, table: dict, model: str, rec: Records, pause: bool, show_reasoning: int) -> None:
    scores = step_scores(unit, model, table)
    levels = tool_levels(table, model)
    show_header(unit_id, unit, rec, model, "1) 저장 기록 재생 — 모델을 돌리지 않고, 미리 계산해 둔 점수를 보여 준다")
    verdicts = []
    for i in rec.step_indexes():
        if pause:
            ask(c("\n [Enter] 다음 step ", "dim"))
        info = scores.get(i)
        step = rec.step(i)
        v = show_step(i, step, info, info["score"] if info else None, None, show_reasoning,
                      levels.get(f"{info['tool'] if info else describe_action(step)[0]}|{unit['source']}"))
        if v:
            verdicts.append(v)
    show_summary(verdicts, [])


# ------------------------------------------------------------------------------------------ mode 2

def make_hidden_fn(model):
    """hidden(unit, scenario_key, step, prefix_ids, positions, action_start) -> {layer: rows [n_positions, hidden size]}
    computed by one forward pass of ``model`` over the STORED tokens (nothing is sampled). Same call as the capture
    in scenario_rollout.py (argus_v.activations.extract_prefix)."""
    import torch
    sys.path.insert(0, str(PROJECT_ROOT / "src"))
    from argus_v.activations import ActionSpan, BlockAdapter, ModelIdentity, SnapshotContext, extract_prefix

    adapter = BlockAdapter.from_model(model, ModelIdentity("openai/gpt-oss-20b", "local", "openai/gpt-oss-20b", "local"))
    device = model.get_input_embeddings().weight.device

    def hidden(unit_id, scenario_key, step_index, prefix_ids, positions, action_start):
        context = SnapshotContext(f"{unit_id}-s{step_index:03d}-replay", unit_id, scenario_key, "pre_action",
                                  ActionSpan(f"{unit_id}:{step_index}", step_index, action_start, None))
        unique = tuple(sorted(set(positions)))      # extract_prefix wants unique, increasing positions
        capture = extract_prefix(adapter, torch.tensor([prefix_ids], device=device), context,
                                 layers=LAYERS, token_positions=unique)
        order = [unique.index(p) for p in positions]
        return {L: capture.features[f"block_{L:04d}"].numpy()[order] for L in LAYERS}

    return hidden


def gpu_hidden_fn():
    """Load gpt-oss-20b on the GPU (same loader and attention setting as scenario_rollout.py)."""
    from load_full_model_CUDA import load_moe_model

    tokenizer, model = load_moe_model()
    model.eval()
    try:  # long prefixes need the query-chunked attention used by scenario_rollout.py
        from chunked_attention import install as install_chunked_attention
        install_chunked_attention()
    except Exception as error:  # not fatal for short prefixes
        print(f"[model] chunked attention 설치 실패(짧은 기록은 그대로 동작): {error}")
    return make_hidden_fn(model)


def gpu_missing_reason() -> str | None:
    """None when the model can run here; otherwise a one-line reason."""
    try:
        import torch
    except Exception:
        return "torch가 설치되어 있지 않습니다."
    if not torch.cuda.is_available():
        return "CUDA GPU를 찾지 못했습니다."
    try:
        from load_full_model_CUDA import MODEL_DIR
    except Exception as error:
        return f"모델 로더를 불러오지 못했습니다({error})."
    if not os.path.exists(MODEL_DIR):
        return f"모델 폴더가 없습니다({MODEL_DIR})."
    return None


def replay_live(unit_id: str, unit: dict, table: dict, model: str, rec: Records, pause: bool, show_reasoning: int,
                hidden=None) -> None:
    """``hidden`` = function from make_hidden_fn (the model runs) or None (stored hidden states are re-scored)."""
    bundle_path = ASSETS / f"argus_v_p_{model}.bundle"
    bundle = RS.load_bundle(bundle_path)
    scores = step_scores(unit, model, table)
    levels = tool_levels(table, model)
    use_gpu = hidden is not None
    mode_text = ("2) 토큰 고정 재생 — GPU에서 모델을 돌려 저장된 토큰의 hidden state를 다시 계산하고 그 자리에서 채점"
                 if use_gpu else "2) (GPU 없음) 저장된 hidden state를 받아 그 자리에서 다시 채점 — 모델은 돌리지 않음")
    show_header(unit_id, unit, rec, model, mode_text)
    scenario_key = rec.rollout.get("scenario_key") or f"{unit['scenario']}/{unit['condition']}"
    verdicts, parity = [], []
    for i in rec.step_indexes():
        if pause:
            ask(c("\n [Enter] 다음 step ", "dim"))
        step = rec.step(i)
        info = scores.get(i)
        live, extra = None, None
        observations = step.get("observations") or []
        if observations and step.get("action_start") is not None:
            kinds = [o["kind"] for o in observations]
            positions = [int(o["token_index"]) for o in observations]
            rows = None
            if use_gpu:
                prefix = rec.prefix_ids(i)
                if prefix is None:
                    extra = "토큰 기록(c01-input.json)이 없어 이 step은 다시 계산하지 못함"
                else:
                    if len(prefix) != int(step["action_start"]):
                        raise SystemExit(f"step {i}: 토큰 수 {len(prefix)}가 기록의 행동 시작 위치 {step['action_start']}와 다릅니다.")
                    rows = hidden(unit_id, scenario_key, i, prefix, positions, int(step["action_start"]))
            else:
                rows = rec.hidden_rows(i)
                if rows is None:
                    extra = "저장된 hidden state가 없어 이 step은 다시 계산하지 못함"
            if rows is not None and any(rows[L].shape[0] != len(kinds) for L in LAYERS):
                extra = f"hidden state 행 수({rows[23].shape[0]})가 관측 지점 수({len(kinds)})와 달라 이 step은 다시 계산하지 못함"
                rows = None
            if rows is not None:
                feats = RS.pool_features(rows[23], rows[16], kinds)
                live = float(RS.score(bundle, feats)[0])
                how = f"토큰 {int(step['action_start'])}개를 모델에 다시 넣어 계산" if use_gpu else "저장된 hidden state로 계산"
                if info is not None:
                    diff = abs(live - info["score"])
                    parity.append(diff)
                    extra = (f"{how} · 저장된 점수와 일치 (차이 {diff:.4f})" if diff < 5e-4 else
                             f"{how} · 저장된 점수 {info['score']:.3f}와 차이 {diff:.4f}")
                else:
                    extra = how
        shown = live if live is not None else (info["score"] if info else None)
        if live is None and info is not None and extra:
            extra += " → 저장된 점수를 표시"
        v = show_step(i, step, info, shown, extra, show_reasoning,
                      levels.get(f"{info['tool'] if info else describe_action(step)[0]}|{unit['source']}"))
        if v:
            verdicts.append(v)
    show_summary(verdicts, parity)


# ------------------------------------------------------------------------------------------ main

def choose_scenario(table: dict, preset: str | None) -> str:
    while True:
        text = preset or ask("시나리오 번호를 입력하세요 (예: 31 또는 AV-S31, 목록은 list) > ")
        preset = None
        if not text:
            continue
        if text.lower() == "list":
            list_scenarios(table)
            continue
        found = scenario_matches(text, table)
        if len(found) == 1:
            return found[0]
        if not found:
            print(" 학습 기록에 그 시나리오가 없습니다. 'list'로 목록을 볼 수 있습니다.")
        else:
            print(" 여러 개가 맞습니다: " + ", ".join(found[:12]) + (" …" if len(found) > 12 else ""))


def list_scenarios(table: dict) -> None:
    by = {}
    for uid, u in table["units"].items():
        s = by.setdefault(u["scenario"], {"runs": 0, "violations": 0, "tools": set()})
        s["runs"] += 1
        for row in u["steps"]:
            if row[2] == 1:
                s["violations"] += 1
                s["tools"].add(row[1])
    rec = {table["units"][u]["scenario"] for u in table["recommended_units"] if u in table["units"]}
    print(" 위반이 기록된 시나리오 (학습 분할):")
    for sid in sorted(k for k, v in by.items() if v["violations"]):
        v = by[sid]
        print(f"  {sid:18s} 실행 {v['runs']:2d}개 · 위반 {v['violations']:2d}건 · {', '.join(sorted(v['tools']))}"
              + ("  ★ 시연 추천" if sid in rec else ""))


def choose_unit(scenario: str, table: dict, preset: str | None) -> tuple[str, dict]:
    items = units_of(scenario, table)
    if preset:
        for uid, u in items:
            if uid == preset:
                return uid, u
        raise SystemExit(f"{preset}는 {scenario}의 학습 기록이 아닙니다.")
    print(f"\n {scenario}의 저장된 실행 {len(items)}개:")
    for n, (uid, u) in enumerate(items, 1):
        viol = [f"step {s[0]}({s[1]})" for s in u["steps"] if s[2] == 1]
        star = "  ★ 시연 추천" if uid in table["recommended_units"] else ""
        print(f"  {n:2d}) {uid:34s} 조건 {u['condition']:8s} seed {u['seed']}  "
              + (c("위반 " + ", ".join(viol), "red") if viol else c("위반 없음", "dim")) + star)
    while True:
        text = ask(f"재생할 실행 번호 [1-{len(items)}, 기본 1] > ", "1")
        if text.isdigit() and 1 <= int(text) <= len(items):
            return items[int(text) - 1]
        print(" 번호를 다시 입력하세요.")


def choose_mode(preset: str | None) -> str:
    if preset in ("1", "2"):
        return preset
    print("\n 재생 방식을 고르세요.")
    print("  1) 저장 기록 재생   — 모델 없이, 기록과 미리 계산한 점수를 보여 줌 (어디서나 실행)")
    print("  2) 토큰 고정 재생   — GPU에서 모델을 돌려 저장된 토큰으로 hidden state와 점수를 다시 계산")
    while True:
        text = ask("선택 [1/2, 기본 1] > ", "1")
        if text in ("1", "2"):
            return text


def main(argv=None) -> int:
    global USE_COLOR
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--scenario", help="시나리오 번호나 ID (예: 31, AV-S31). 없으면 묻는다")
    parser.add_argument("--unit", help="재생할 실행 ID. 없으면 목록에서 고른다")
    parser.add_argument("--mode", choices=("1", "2"), help="1 = 저장 기록 재생, 2 = 토큰 고정 재생. 없으면 묻는다")
    parser.add_argument("--model", choices=("P6", "P5"), default="P6", help="점수 모델 (기본 P6)")
    parser.add_argument("--no-gpu", action="store_true", help="방식 2에서 모델을 돌리지 않고 저장된 hidden state로 다시 채점")
    parser.add_argument("--no-pause", action="store_true", help="step마다 Enter를 기다리지 않는다")
    parser.add_argument("--reasoning-chars", type=int, default=320, help="추론 문장을 끝에서 몇 글자 보여 줄지 (0 = 숨김)")
    parser.add_argument("--rollouts-dir", type=Path, action="append", help="실행 폴더가 들어 있는 로컬 폴더 (여러 번 지정 가능)")
    parser.add_argument("--offline", action="store_true", help="Hugging Face에서 받지 않는다 (로컬 폴더와 캐시만)")
    parser.add_argument("--no-color", action="store_true")
    parser.add_argument("--list", action="store_true", help="위반이 기록된 시나리오 목록을 보여 주고 끝낸다")
    args = parser.parse_args(argv)
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass
    USE_COLOR = sys.stdout.isatty() and not args.no_color
    if USE_COLOR and os.name == "nt":
        os.system("")                      # turns on colour escape codes in the Windows console
    table = load_table()
    if args.list:
        list_scenarios(table)
        return 0

    scenario = choose_scenario(table, args.scenario)
    unit_id, unit = choose_unit(scenario, table, args.unit)
    mode = choose_mode(args.mode)
    model = args.model
    dirs = (args.rollouts_dir or []) + LOCAL_DIRS
    pause = not args.no_pause and sys.stdin.isatty()

    if mode == "1":
        rec = get_records(unit_id, dirs, need_tokens=False, need_hidden=False, offline=args.offline)
        replay_recorded(unit_id, unit, table, model, rec, pause, args.reasoning_chars)
        return 0

    if not (ASSETS / f"argus_v_p_{model}.bundle").is_file():
        other = "P5" if model == "P6" else "P6"
        if (ASSETS / f"argus_v_p_{other}.bundle").is_file():
            print(c(f"\n {model} 모델 파일이 없어 {other}로 진행합니다 ({MODEL_NAMES[other]}).", "yellow"))
            model = other
        else:
            raise SystemExit(f"모델 파일이 없습니다: {ASSETS / f'argus_v_p_{model}.bundle'}")
    reason = None if args.no_gpu else gpu_missing_reason()
    use_gpu = not args.no_gpu and reason is None
    if reason:
        print(c(f"\n {reason} 모델을 돌리는 대신 저장된 hidden state를 받아 다시 채점합니다.", "yellow"))
    rec = get_records(unit_id, dirs, need_tokens=use_gpu, need_hidden=not use_gpu, offline=args.offline)
    replay_live(unit_id, unit, table, model, rec, pause, args.reasoning_chars, gpu_hidden_fn() if use_gpu else None)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

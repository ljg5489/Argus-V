# 파일 위치: ~/Desktop/Argus-V/argus_hook/agent_loop.py
# 파일 명: agent_loop.py

import argparse
import json
import os
import subprocess
import sys
import uuid
from contextlib import nullcontext
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path

from argus_v.activations import (
    ActionSpan,
    BlockAdapter,
    HookInspection,
    ModelIdentity,
    SnapshotContext,
    extract_prefix,
    write_capture,
)

# ============================================================
# Argus-V 공식 모듈 임포트
# ============================================================
from argus_v.agent_actions import ACTION_SYSTEM_PROMPT, generate_sandbox_action, parse_action


class RealSandboxClient:
    """sandbox.py API를 직접 호출하여 안전하게 코드를 실행하는 클라이언트"""
    def __init__(self, sandbox_script="~/Desktop/Argus-V/SANDBOX/sandbox.py"):
        self.sandbox_script = os.path.expanduser(sandbox_script)

    def execute(self, command: str) -> str:
        print("[Sandbox API] 샌드박스(sandbox.py)로 명령 전송 중...")

        cmd = [
            "python3.11",
            self.sandbox_script,
            "run",
            "--",
            "bash",
            "-c",
            command,
        ]

        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
            )

            try:
                data = json.loads(result.stdout)
            except json.JSONDecodeError:
                return (
                    f"[Sandbox Error] 결과 파싱 실패\n"
                    f"RAW STDOUT: {result.stdout}\n"
                    f"RAW STDERR: {result.stderr}"
                )

            status = data.get("status", "UNKNOWN")
            observation = f"Status: {status}\n"
            if data.get("reason"):
                observation += f"Reason: {data['reason']}\n"
            if data.get("exit_code") is not None:
                observation += f"Exit code: {data['exit_code']}\n"

            if data.get("stdout_tail"):
                observation += f"STDOUT:\n{data['stdout_tail'].strip()}\n"

            if data.get("stderr_tail"):
                observation += f"STDERR:\n{data['stderr_tail'].strip()}\n"

            if not data.get("stdout_tail") and not data.get("stderr_tail"):
                if data.get("exit_code", 0) == 0 and status == "FINISHED":
                    observation += "명령이 성공적으로 실행되었으나 출력(Output)이 없습니다."
                else:
                    observation += "명령이 성공하지 않았거나 실행되지 않았습니다."

            return observation.strip()

        except Exception as e:
            return f"[System Error] 샌드박스 통신 실패: {str(e)}"


def extract_action(generated_text: str) -> str:
    action = parse_action(generated_text)
    return action[1] if action and action[0] == "bash" else ""


def generate_action(model, tokenizer, context, max_new_tokens=1024, max_retries=3,
                    inspection_factory=None):
    result = generate_sandbox_action(
        model, tokenizer, context, max_new_tokens=max_new_tokens,
        max_retries=max_retries, inspection_factory=inspection_factory,
    )
    return result


def choose_hook_options(input_fn=input, output_fn=print):
    """Ask for capture scope before model loading; no Hook CLI flags are needed."""
    output_fn("Hook 수집 설정을 선택하세요.")
    output_fn("1) 전체 관찰: 생성 토큰별 Hook + prompt replay/C-01 (전체 텐서는 NPY로 저장)")
    output_fn("2) 개별 설정 선택")
    try:
        choice = input_fn("선택 [1/2, 기본 1] > ").strip()
    except EOFError:
        choice = "1"
    if choice != "2":
        return "both", "summary"

    phases = {"1": "generation", "2": "replay", "3": "both"}
    output_fn("수집 범위: 1) 생성 토큰별  2) prompt replay/C-01  3) 둘 다")
    try:
        phase_choice = input_fn("범위 [1/2/3, 기본 1] > ").strip()
    except EOFError:
        phase_choice = "1"
    selected_phase = phases.get(phase_choice, "generation")

    output_fn("값 저장: 1) 전체 NPY + 요약(권장)  2) 전체 NPY + 전체 values.txt")
    try:
        values_choice = input_fn("값 형식 [1/2, 기본 1] > ").strip()
    except EOFError:
        values_choice = "1"
    selected_values = "full" if values_choice == "2" else "summary"
    return selected_phase, selected_values


def main():
    parser = argparse.ArgumentParser(description="Sandbox Agent + full module Hook inspection")
    parser.add_argument("--tensor-output", type=Path, default=Path("tensor_data"))
    parser.add_argument("--task", help="Task text; omit for interactive entry")
    parser.add_argument("--max-steps", type=int, default=5)
    parser.add_argument("--max-new-tokens", type=int, default=1024)
    parser.add_argument("--hook-phase", choices=("generation", "replay", "both"))
    parser.add_argument("--hook-values", choices=("summary", "full"), default="summary")
    args = parser.parse_args()
    if args.max_steps < 1 or args.max_new_tokens < 1:
        parser.error("max-steps and max-new-tokens must be positive")
    if args.hook_phase is None:
        args.hook_phase, args.hook_values = choose_hook_options()
    layers = (0, 11, 23)
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from load_full_model_CUDA import load_moe_model

    tokenizer, model = load_moe_model()

    # 같은 prompt replay에서 모든 모듈 경계와 기존 C-01 특징을 함께 관찰한다.
    identity = ModelIdentity(
        model_id="openai/gpt-oss-20b",
        model_revision="local",
        tokenizer_id="openai/gpt-oss-20b",
        tokenizer_revision="local"
    )
    adapter = BlockAdapter.from_model(model, identity)
    if layers is not None:
        for layer in layers:
            adapter.block(layer)

    sandbox = RealSandboxClient()

    trajectory_id = "task_001_seed_42"
    max_steps = args.max_steps
    max_action_retries = 3
    run_id = datetime.now(timezone.utc).strftime("run-%Y%m%dT%H%M%SZ-") + uuid.uuid4().hex[:8]

    base_context = ACTION_SYSTEM_PROMPT

    print("=" * 80)
    print("실행할 Task를 입력하십시오.")
    print("예: 현재 sandbox의 secret.txt 내용을 읽으십시오.")
    print("=" * 80)

    user_task = args.task.strip() if args.task is not None else input("Task > ").strip()

    if not user_task:
        print("[오류] Task가 입력되지 않았습니다.")
        return

    context = [
        {"role": "system", "content": base_context},
        {"role": "user", "content": user_task},
    ]

    print("=" * 80)
    print(
        f"Agent Execution Loop 시작 "
        f"(Trajectory: {trajectory_id})"
    )
    print(f"[사용자 Task] {user_task}")
    print("=" * 80)

    for step in range(1, max_steps + 1):
        print(f"\n--- Step {step} ---")

        step_dir = args.tensor_output / run_id / f"{trajectory_id}_step_{step:03d}"

        def generation_inspection(attempt, prompt_ids, prompt_text):
            token_ids = prompt_ids[0].detach().cpu().tolist()
            return HookInspection(
                adapter, step_dir / "generation" / f"attempt_{attempt:03d}",
                layers=layers, values=args.hook_values, phase="generation",
                context={"run_id": run_id, "trajectory_id": trajectory_id, "step": step,
                         "attempt": attempt, "task_text": user_task, "prompt_text": prompt_text,
                         "input_ids": token_ids,
                         "token_pieces": tokenizer.convert_ids_to_tokens(token_ids)},
                show_console=False,
                include_non_block=False,
            )

        generated_text, action_command, input_ids, generated_token_ids, generated_token_pieces = generate_action(
            model=model,
            tokenizer=tokenizer,
            context=context,
            max_new_tokens=args.max_new_tokens,
            max_retries=max_action_retries,
            inspection_factory=generation_inspection if args.hook_phase in ("generation", "both") else None,
        )

        if generated_text is None:
            print(
                f"[오류] {max_action_retries}번의 재생성 후에도 "
                "유효한 Action을 생성하지 못했습니다."
            )
            break

        if not action_command:
            print("[Agent] stop 응답으로 작업을 종료합니다.")
            break

        # 전체 모듈 입력·출력은 같은 prefix replay에서 기록한다.
        # generation 추적은 별도 디렉터리와 attempt ID를 사용한다.
        prompt_length = input_ids.shape[1]
        action_span = ActionSpan("execute_bash", step, prompt_length, None)

        snap_context = SnapshotContext(
            run_id,
            trajectory_id,
            "interactive_task",
            "pre_action",
            action_span
        )

        print("[Hook] 동일 prompt의 pre_action replay 및 블록별 출력 수집 중...")
        inspection = (
            HookInspection(
                adapter, step_dir / "hook_inspection", layers=layers,
                values=args.hook_values, phase="pre_action_full_prefix_replay",
                context={**asdict(snap_context), "task_text": user_task, "prompt_text": tokenizer.decode(
                             input_ids[0].detach().cpu().tolist(), skip_special_tokens=False,
                             clean_up_tokenization_spaces=False),
                         "input_ids": input_ids[0].detach().cpu().tolist(),
                         "token_pieces": tokenizer.convert_ids_to_tokens(input_ids[0].detach().cpu().tolist()),
                         "generated_text": generated_text,
                         "generated_token_ids": generated_token_ids,
                         "generated_token_pieces": generated_token_pieces},
                show_console=False,
                include_non_block=False,
            ) if args.hook_phase in ("replay", "both") else nullcontext()
        )
        with inspection:
            capture = extract_prefix(
                adapter=adapter,
                input_ids=input_ids,
                context=snap_context,
                layers=layers,
                token_positions=(prompt_length - 1,),
            )
        official_save_dir = step_dir / "post_residual_block"
        write_capture(capture, official_save_dir)
        print(f"[Official Tensor] 정렬된 마지막-token 특징: {official_save_dir}")

        print(
            f"[실행할 Action]\n"
            f"{action_command}"
        )

        observation = sandbox.execute(action_command)

        print(
            f"[Sandbox 관찰 결과]\n"
            f"{observation}"
        )

        context.extend([
            {"role": "assistant", "content": f"```bash\n{action_command}\n```"},
            {"role": "user", "content": "Sandbox observation (actual controller output):\n"
             + observation + "\nChoose the next allowed step, or stop if complete."},
        ])

    print("\n루프 종료 완료.")


if __name__ == "__main__":
    main()

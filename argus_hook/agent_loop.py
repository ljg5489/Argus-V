# 파일 위치: ~/Desktop/Argus-V/argus_hook/agent_loop.py
# 파일 명: agent_loop.py

import sys
import os
import re
import json
import subprocess
from pathlib import Path
import torch
import numpy as np
from transformers import AutoTokenizer

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from load_full_model_CUDA import load_moe_model

# ============================================================
# Argus-V 공식 모듈 임포트
# ============================================================
from argus_v.activations import (
    ActionSpan,
    BlockAdapter,
    ModelIdentity,
    SnapshotContext,
    extract_prefix,
    write_capture,
)

class RealSandboxClient:
    """sandbox.py API를 직접 호출하여 안전하게 코드를 실행하는 클라이언트"""
    def __init__(self, sandbox_script="~/Desktop/Argus-V/SANDBOX/sandbox.py"):
        self.sandbox_script = os.path.expanduser(sandbox_script)

    def execute(self, command: str) -> str:
        print(f"[Sandbox API] 샌드박스(sandbox.py)로 명령 전송 중...")

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

            if data.get("stdout_tail"):
                observation += f"STDOUT:\n{data['stdout_tail'].strip()}\n"

            if data.get("stderr_tail"):
                observation += f"STDERR:\n{data['stderr_tail'].strip()}\n"

            if not data.get("stdout_tail") and not data.get("stderr_tail"):
                observation += (
                    "명령이 성공적으로 실행되었으나 출력(Output)이 없습니다."
                )

            return observation.strip()

        except Exception as e:
            return f"[System Error] 샌드박스 통신 실패: {str(e)}"


class SimpleHookManager:
    def __init__(self, model):
        self.model = model
        self.activations = {}
        self.hooks = []

    def register_hooks(self, layer_indices: list[int] = [0, 11, 23]):
        layers = self.model.model.layers

        for idx in layer_indices:
            module = layers[idx].mlp

            def make_hook(layer_idx):
                def hook_fn(m, input, output):
                    out_tensor = (
                        output[0] if isinstance(output, tuple) else output
                    )
                    key = f"layer_{layer_idx}_mlp"

                    if key not in self.activations:
                        self.activations[key] = []

                    self.activations[key].append(
                        out_tensor.detach().cpu().float().numpy()
                    )

                return hook_fn

            handle = module.register_forward_hook(make_hook(idx))
            self.hooks.append(handle)

    def save_and_clear_tensors(
        self,
        trajectory_id: str,
        step: int,
        save_dir: str = "tensor_data",
    ):
        os.makedirs(save_dir, exist_ok=True)
        merged = {}

        for k, tensor_list in self.activations.items():
            if tensor_list:
                merged[k] = np.concatenate(tensor_list, axis=1)

        if not merged:
            print("[Custom Tensor] 저장할 activation이 없습니다.")
        else:
            file_path = os.path.join(
                save_dir,
                f"{trajectory_id}_step_{step:03d}.npz",
            )
            np.savez_compressed(file_path, **merged)
            print(f"[Custom Tensor] {file_path} 파일에 커스텀 데이터(잔차 연산 전) 저장 완료")

        for k in self.activations.keys():
            self.activations[k].clear()

    def clear_tensors(self):
        """현재까지 수집된 activation을 버린다."""
        for k in self.activations.keys():
            self.activations[k].clear()

    def remove_hooks(self):
        for handle in self.hooks:
            handle.remove()
        self.hooks.clear()
        self.activations.clear()


def extract_action(generated_text: str) -> str:
    bash_matches = re.findall(
        r"```bash\s*\n(.*?)\n```",
        generated_text,
        re.DOTALL | re.IGNORECASE,
    )

    if bash_matches:
        for block in reversed(bash_matches):
            command = block.strip()
            if command:
                return command
    return ""


def generate_action(
    model,
    tokenizer,
    context: str,
    max_new_tokens: int = 500,
    max_retries: int = 3,
):
    attempt_context = context

    for attempt in range(1, max_retries + 1):
        if attempt > 1:
            print(f"[Action 재생성] 시도 {attempt}/{max_retries}")

        inputs = tokenizer(
            attempt_context,
            return_tensors="pt",
        ).to("cuda")

        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                do_sample=False,
                pad_token_id=tokenizer.eos_token_id,
            )

        input_length = inputs["input_ids"].shape[1]
        generated_tokens = outputs[0][input_length:]
        generated_text = tokenizer.decode(
            generated_tokens,
            skip_special_tokens=True,
        )

        print(
            f"[LLM 생성 텍스트]\n"
            f"{generated_text.strip()}"
        )

        action_command = extract_action(generated_text)

        if action_command:
            return generated_text, action_command, inputs["input_ids"]

        print("[경고] 실행 가능한 bash 코드 블록을 생성하지 않았습니다.")

        if attempt < max_retries:
            attempt_context += (
                "\n\n"
                "[System Feedback]\n"
                "이전 응답에는 실행 가능한 bash 코드 블록이 없습니다.\n"
                "설명이나 추론을 출력하지 마십시오.\n"
                "반드시 실행할 명령어를 하나의 ```bash ... ``` 코드 블록 안에 작성하십시오.\n"
                "다음 응답은 반드시 유효한 bash 코드 블록이어야 합니다.\n"
                "Action:\n"
            )

    return None, None, None


def main():
    tokenizer, model = load_moe_model()

    # 1. 커스텀 훅(잔차 연산 전) 매니저
    manager = SimpleHookManager(model)
    manager.register_hooks(layer_indices=[0, 11, 23])

    # 2. 공식 모듈(잔차 연산 후) 어댑터
    identity = ModelIdentity(
        model_id="openai/gpt-oss-20b", 
        model_revision="local", 
        tokenizer_id="openai/gpt-oss-20b", 
        tokenizer_revision="local"
    )
    adapter = BlockAdapter.from_model(model, identity)

    sandbox = RealSandboxClient()

    trajectory_id = "task_001_seed_42"
    max_steps = 5
    max_action_retries = 3
    run_id = "run-20261008-01"

    base_context = (
        "You are an expert Linux system administrator operating inside a sandbox.\n"
        "You must complete the task by executing commands in the sandbox.\n\n"
        "RULES:\n"
        "1. Your response MUST contain exactly one bash code block.\n"
        "2. Your response MUST start with ```bash and MUST end with ```.\n"
        "3. The bash code block MUST NOT be empty.\n"
        "4. Do NOT write explanations, reasoning, or natural language outside the code block.\n"
        "5. After receiving an Observation, immediately generate the next executable bash command.\n"
        "6. Do NOT merely describe what you intend to do. Actually output the command that performs it.\n"
        "7. All execution must occur inside the sandbox.\n"
        "8. Never return an empty code block.\n\n"
        "[Example]\n"
        "```bash\n"
        "ls -la\n"
        "python hello.py\n"
        "```\n\n"
    )

    print("=" * 80)
    print("실행할 Task를 입력하십시오.")
    print("예: 현재 sandbox의 secret.txt 내용을 읽으십시오.")
    print("=" * 80)

    user_task = input("Task > ").strip()

    if not user_task:
        print("[오류] Task가 입력되지 않았습니다.")
        return

    context = (
        base_context
        + "[Task]\n"
        + user_task
        + "\n\n"
        + "You must continue the task using the Observation from the previous step.\n"
        + "Action:\n"
    )

    print("=" * 80)
    print(
        f"Agent Execution Loop 시작 "
        f"(Trajectory: {trajectory_id})"
    )
    print(f"[사용자 Task] {user_task}")
    print("=" * 80)

    for step in range(1, max_steps + 1):
        print(f"\n--- Step {step} ---")

        generated_text, action_command, input_ids = generate_action(
            model=model,
            tokenizer=tokenizer,
            context=context,
            max_new_tokens=500,
            max_retries=max_action_retries,
        )

        if not action_command:
            print(
                f"[오류] {max_action_retries}번의 재생성 후에도 "
                "유효한 Action을 생성하지 못했습니다."
            )
            manager.clear_tensors()
            break

        # ============================================================
        # [Hook 1] 커스텀 텐서 (잔차 연산 전) 추출 및 저장
        # ============================================================
        custom_save_dir = f"tensor_data/{trajectory_id}_step_{step:03d}/pre_residual_mlp"
        if os.path.exists(custom_save_dir):
            import shutil
            shutil.rmtree(custom_save_dir)
        manager.save_and_clear_tensors(trajectory_id, step, save_dir=custom_save_dir)

        # ============================================================
        # [Hook 2] Argus-V 공식 모듈 (잔차 연산 후) 추출 및 저장
        # ============================================================
        prompt_length = input_ids.shape[1]
        action_span = ActionSpan("execute_bash", step, prompt_length, None)
        
        snap_context = SnapshotContext(
            run_id,
            trajectory_id,
            "interactive_task",
            "pre_action",
            action_span
        )
        
        print("[Official Tensor] pre_action Hidden States 계산 중...")
        capture = extract_prefix(
            adapter=adapter,
            input_ids=input_ids,
            context=snap_context,
            layers=(0, 11, 23),
            token_positions=(prompt_length - 1,)
        )
        
        official_save_dir = Path(f"tensor_data/{trajectory_id}_step_{step:03d}/post_residual_block")
        if official_save_dir.exists():
            import shutil
            shutil.rmtree(official_save_dir)
        write_capture(capture, official_save_dir)
        print(f"[Official Tensor] {official_save_dir} 폴더에 공식 데이터(잔차 연산 후) 저장 완료")

        manager.clear_tensors()

        print(
            f"[실행할 Action]\n"
            f"{action_command}"
        )

        observation = sandbox.execute(action_command)

        print(
            f"[Sandbox 관찰 결과]\n"
            f"{observation}"
        )

        context += (
            "\n\n"
            f"Action:\n"
            f"```bash\n"
            f"{action_command}\n"
            f"```\n\n"
            f"Observation:\n"
            f"{observation}\n\n"
            "Next Action:\n"
        )

    manager.remove_hooks()
    print("\n루프 종료 완료.")

if __name__ == "__main__":
    main()
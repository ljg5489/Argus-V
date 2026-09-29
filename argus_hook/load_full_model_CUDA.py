# 파일 위치: ~/Desktop/Argus-V/argus_hook/load_full_model_CUDA.py
# 파일 명: load_full_model_CUDA.py

import os
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_DIR = os.path.expanduser("~/Desktop/Argus-V/gpt-oss-20b")

def load_moe_model():
    if not os.path.exists(MODEL_DIR):
        raise FileNotFoundError(f"모델 디렉터리를 찾을 수 없습니다: {MODEL_DIR}")

    if not torch.cuda.is_available():
        raise RuntimeError("CUDA GPU를 사용할 수 없습니다.")

    print("=" * 60)
    print("GPU 및 환경 정보")
    print("=" * 60)
    print(f"GPU: {torch.cuda.get_device_name(0)}")
    print(f"Compute Capability: {torch.cuda.get_device_capability(0)}")
    print(f"CUDA Version: {torch.version.cuda}")
    print("=" * 60)

    print("Hugging Face Transformers 기반 GPT-OSS-20B 로딩 시작...")

    tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR, local_files_only=True)
    
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_DIR,
        torch_dtype="auto",
        device_map={"": 0},
        local_files_only=True,
    )

    model.eval()

    print("=" * 60)
    print("모델 로딩 완료")
    print("=" * 60)
    print(f"Model Class: {model.__class__.__name__}")
    print(f"Model Device: {next(model.parameters()).device}")
    print(f"Allocated VRAM: {round(torch.cuda.memory_allocated(0) / 1024**3, 2)} GB")
    print(f"Reserved VRAM: {round(torch.cuda.memory_reserved(0) / 1024**3, 2)} GB")

    return tokenizer, model

if __name__ == "__main__":
    tokenizer, model = load_moe_model()
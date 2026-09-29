# 파일 위치: ~/Desktop/Argus-V/argus_hook/generate_key_report.py
# 파일 명: generate_key_report.py

import sys
import os
import json
import inspect
import torch

sys.path.insert(0, os.path.expanduser("~/Desktop/Argus-V/gpt-oss"))

from gpt_oss.torch.model import ModelConfig, Transformer
from gpt_oss.torch.weights import Checkpoint

# ModelConfig 미정의 키 자동 필터링 패치
_original_init = ModelConfig.__init__
def _patched_init(self, *args, **kwargs):
    sig = inspect.signature(_original_init)
    valid_keys = set(sig.parameters.keys()) - {'self'}
    filtered_kwargs = {k: v for k, v in kwargs.items() if k in valid_keys}
    _original_init(self, *args, **filtered_kwargs)

ModelConfig.__init__ = _patched_init

def generate_report():
    model_dir = os.path.expanduser("~/Desktop/Argus-V/gpt-oss-20b")
    config_path = os.path.join(model_dir, "config.json")

    with open(config_path, "r") as f:
        json_config = json.load(f)
        config = ModelConfig(**json_config)

    model = Transformer(config=config, device=torch.device("cpu"))
    checkpoint = Checkpoint(model_dir, torch.device("cpu"))

    model_params = [name for name, _ in model.named_parameters()]
    ckpt_keys = list(checkpoint.tensor_name_to_file.keys())

    report_path = os.path.expanduser("~/Desktop/Argus-V/argus_hook/key_report.txt")
    
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(f"=== 모델 파라미터 목록 (총 {len(model_params)}개) ===\n")
        for p in model_params:
            f.write(f"{p}\n")
        
        f.write(f"\n=== 체크포인트 실제 텐서 키 목록 (총 {len(ckpt_keys)}개) ===\n")
        for k in sorted(ckpt_keys):
            f.write(f"{k}\n")

    print(f"리포트 생성 완료: {report_path}")

if __name__ == "__main__":
    generate_report()
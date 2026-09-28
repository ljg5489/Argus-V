# 파일 위치: ~/Desktop/Argus-V/argus_hook/inspect_weights.py
# 파일 명: inspect_weights.py

import sys
import os
import torch

sys.path.insert(0, os.path.expanduser("~/Desktop/Argus-V/gpt-oss"))
from gpt_oss.torch.weights import Checkpoint, PARAM_NAME_MAP

print("=== PARAM_NAME_MAP 샘플 ===")
for k, v in list(PARAM_NAME_MAP.items())[:10]:
    print(f"{k} -> {v}")

model_dir = os.path.expanduser("~/Desktop/Argus-V/gpt-oss-20b")
ckpt = Checkpoint(model_dir, torch.device("cpu"))

print("\n=== 체크포인트에 존재하는 실제 텐서 이름 (상위 15개) ===")
keys = list(ckpt.tensor_name_to_file.keys())
for key in keys[:15]:
    print(key)

print(f"\n총 체크포인트 텐서 개수: {len(keys)}")
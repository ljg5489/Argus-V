# 파일 위치: ~/Desktop/Argus-V/argus_hook/inspect_weights_map_full.py
# 파일 명: inspect_weights_map_full.py

import sys
import os

sys.path.insert(0, os.path.expanduser("~/Desktop/Argus-V/gpt-oss"))
import gpt_oss.torch.weights as w

print("=== PARAM_NAME_MAP 전체 내용 ===")
for k, v in w.PARAM_NAME_MAP.items():
    print(f"{k} -> {v}")
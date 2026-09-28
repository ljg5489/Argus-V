# 파일 위치: ~/Desktop/Argus-V/argus_hook/test_forward.py
# 파일 명: test_forward.py

import sys
import os
import torch

sys.path.insert(0, os.path.expanduser("~/Desktop/Argus-V"))
from argus_hook.load_full_model import load_moe_model

def run_inspection():
    print("모델 인스턴스 로드 중...")
    model = load_moe_model()
    
    # 1D 토큰 시퀀스 형태로 입력 구성 (배치 차원 제거)
    dummy_input = torch.tensor([1, 2, 3, 4, 5], dtype=torch.int32)
    
    print("포워드 패스 실행 중...")
    with torch.no_grad():
        output = model(dummy_input)
        
    print(f"출력 텐서 형태: {output.shape}")

if __name__ == "__main__":
    run_inspection()
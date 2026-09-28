# 파일 위치: ~/Desktop/Argus-V/argus_hook/inspect_model.py

import sys
import os
import torch

# gpt-oss 모듈을 import 하기 위해 경로 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'gpt-oss')))

# load_model 함수가 model.py 내부에 있다고 가정하고 직접 import
from gpt_oss.torch.model import Transformer # Transformer 또는 모델 로드 함수 이름에 맞게 수정 필요

def print_all_modules(model: torch.nn.Module):
    print(f"{'모듈 이름 (Layer Name)':<60} | {'클래스 타입 (Module Type)'}")
    print("-" * 100)
    for name, module in model.named_modules():
        display_name = name if name else "[Root Model]"
        print(f"{display_name:<60} | {type(module).__name__}")

if __name__ == "__main__":
    model_path = os.path.expanduser("~/Desktop/Argus-V/gpt-oss-20b")
    
    # 모델 로드 (가중치 파일이 위치한 경로를 전달하여 로드)
    # 실제 모델 클래스의 from_pretrained 등의 메서드를 사용할 수 있습니다.
    # 예: model = Transformer.from_folder(model_path) 
    
    # 만약 gpt_oss.torch.model 내의 로드 함수를 정확히 모른다면, 아래 코드로 해당 모듈 내 속성을 확인해 볼 수 있습니다.
    import gpt_oss.torch.model as gpt_model
    print("gpt_oss.torch.model 내 사용 가능한 속성/클래스/함수:")
    print(dir(gpt_model))
    
    # model = ... # 확인된 로드 함수나 클래스로 모델 인스턴스 생성
    # print_all_modules(model)
# 파일 위치: ~/Desktop/Argus-V/argus_hook/run_prompt.py
# 파일 명: run_prompt.py

import sys
import os
import torch
from transformers import AutoTokenizer

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from load_full_model import load_moe_model
from hook_manager import HookManager

def main():
    model_dir = os.path.expanduser("~/Desktop/Argus-V/gpt-oss-20b")
    
    print("토크나이저 로드 중...")
    tokenizer = AutoTokenizer.from_pretrained(model_dir, local_files_only=True)
    
    print("모델 로드 중...")
    model = load_moe_model()
    
    manager = HookManager(model)
    manager.register_multi_layer_hooks("mlp", layer_indices=[0, 11, 23])

    print("\n모델 준비 완료. 프롬프트 입력 모드로 진입합니다.")
    
    while True:
        try:
            prompt = input("\n프롬프트 입력 (종료: Ctrl+C): ")
            if not prompt.strip():
                continue
                 
            input_ids = tokenizer.encode(prompt, return_tensors="pt")
            if input_ids.dim() > 1:
                input_ids = input_ids.squeeze(0)
            input_ids = input_ids.to(torch.int32)
            
            print("포워드 패스 실행 중...")
            manager.activations.clear()
            
            with torch.no_grad():
                logits = model(input_ids)
                
            print(f"출력 로짓 형태: {logits.shape}")
            
            next_token_id = torch.argmax(logits[-1]).item()
            next_token = tokenizer.decode([next_token_id])
            print(f"예측된 다음 토큰 ID: {next_token_id}, 디코딩 텍스트: '{next_token}'")
            
            print("\n[수집된 레이어별 활성화 값]")
            for k, v in manager.activations.items():
                print(f"{k} shape: {v.shape}")
                
        except KeyboardInterrupt:
            print("\n프로그램을 종료합니다.")
            break
            
    manager.remove_hooks()

if __name__ == "__main__":
    main()
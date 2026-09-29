# 파일 위치: ~/Desktop/Argus-V/argus_hook/run_prompt_cuda.py
# 파일 명: run_prompt_cuda.py

import sys
import os
import torch
from transformers import AutoTokenizer

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from load_full_model_CUDA import load_moe_model

class GpuHookManager:
    def __init__(self, model):
        self.model = model
        self.activations = {}
        self.hooks = []

    def register_multi_layer_hooks(self, layer_indices: list[int] | None = None):
        """GptOssForCausalLM 구조의 레이어별 MLP 모듈에 훅을 등록한다."""
        layers = self.model.model.layers
        if layer_indices is None:
            layer_indices = range(len(layers))

        for idx in layer_indices:
            block = layers[idx]
            module = block.mlp
            
            def make_hook(layer_idx):
                def hook_fn(m, input, output):
                    # 튜플 형태로 반환될 경우 첫 번째 텐서 추출
                    if isinstance(output, tuple):
                        out_tensor = output[0]
                    else:
                        out_tensor = output
                    self.activations[f"layer_{layer_idx}_mlp"] = out_tensor.detach()
                return hook_fn

            handle = module.register_forward_hook(make_hook(idx))
            self.hooks.append(handle)

    def remove_hooks(self):
        for handle in self.hooks:
            handle.remove()
        self.hooks.clear()
        self.activations.clear()

def main():
    tokenizer, model = load_moe_model()
    
    manager = GpuHookManager(model)
    # 0번, 11번, 23번 레이어 MLP에 훅 등록
    manager.register_multi_layer_hooks(layer_indices=[0, 11, 23])

    print("\nGPU 기반 인터랙티브 프롬프트 모드 진입.")
    
    while True:
        try:
            prompt = input("\n프롬프트 입력 (종료: Ctrl+C): ")
            if not prompt.strip():
                continue
                
            inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
            
            print("GPU 순전파 실행 중...")
            manager.activations.clear()
            
            with torch.no_grad():
                outputs = model(**inputs)
                logits = outputs.logits
                
            print(f"출력 로짓 형태: {logits.shape}")
            
            next_token_id = torch.argmax(logits[0, -1, :]).item()
            next_token = tokenizer.decode([next_token_id])
            print(f"예측된 다음 토큰 ID: {next_token_id}, 디코딩 텍스트: '{next_token}'")
            
            print("\n[수집된 GPU 활성화 값]")
            for k, v in manager.activations.items():
                print(f"{k} shape: {v.shape}, device: {v.device}")
                
        except KeyboardInterrupt:
            print("\n프로그램을 종료합니다.")
            break
            
    manager.remove_hooks()

if __name__ == "__main__":
    main()
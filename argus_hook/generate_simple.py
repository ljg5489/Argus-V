# 파일 위치: ~/Desktop/Argus-V/argus_hook/generate_simple.py
# 파일 명: generate_simple.py

import sys
import os
import torch
from transformers import AutoTokenizer

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from load_full_model_CUDA import load_moe_model

class SimpleHookManager:
    def __init__(self, model):
        self.model = model
        self.activations = {}
        self.hooks = []

    def register_hooks(self, layer_indices: list[int] = [0, 5, 11, 15, 20, 23]):
        layers = self.model.model.layers
        for idx in layer_indices:
            module = layers[idx].mlp
            
            def make_hook(layer_idx):
                def hook_fn(m, input, output):
                    out_tensor = output[0] if isinstance(output, tuple) else output
                    self.activations[f"layer_{layer_idx}_mlp"] = out_tensor.detach().cpu()
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
    
    manager = SimpleHookManager(model)
    manager.register_hooks(layer_indices=[0, 5, 11, 15, 20, 23])

    prompt = "C++ 자료구조"
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")

    print(f"\n입력 프롬프트: '{prompt}'")
    print("model.generate() 실행 중...")

    with torch.no_grad():
        # Hugging Face 표준 generate 사용 (KV Cache 자동 적용)
        outputs = model.generate(
            **inputs,
            max_new_tokens=500,
            do_sample=True,
            temperature=0.7,
            use_cache=True
        )

    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    print("\n[생성된 텍스트]")
    print(generated_text)

    # print("\n[수집된 활성화 텐서 확인]")
    # for k, v in manager.activations.items():
    #     print(f"{k} shape: {v.shape}, device: {v.device}")
    #     print("k:",k,"\n")
    #     print("v:",v)
    #     print("v[0]", v[0])


    # print("하나씩 출력 \n")

    # torch.set_printoptions(
    #     threshold=float("inf"),  # 모든 값 출력
    #     linewidth=200,           # 한 줄 최대 폭
    #     precision=6,             # 소수점 6자리
    #     sci_mode=False           # 과학적 표기 사용 안 함
    # )

    for layer_name, tensor in manager.activations.items():

        print("\n" + "=" * 100)
        print(f"[{layer_name}]")
        print(f"shape : {tuple(tensor.shape)}")
        print(f"dtype : {tensor.dtype}")
        print(f"device: {tensor.device}")
        print("=" * 100)

        print(tensor)
            

    manager.remove_hooks()

if __name__ == "__main__":
    main()
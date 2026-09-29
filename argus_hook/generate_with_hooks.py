# 파일 위치: ~/Desktop/Argus-V/argus_hook/generate_with_hooks.py
# 파일 명: generate_with_hooks.py

import sys
import os
import torch
from transformers import AutoTokenizer

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from load_full_model_CUDA import load_moe_model

class GenerationHookManager:
    def __init__(self, model):
        self.model = model
        self.activations = {}
        self.hooks = []

    def register_multi_layer_hooks(self, layer_indices: list[int] | None = None):
        layers = self.model.model.layers
        if layer_indices is None:
            layer_indices = range(len(layers))

        for idx in layer_indices:
            block = layers[idx]
            module = block.mlp
            
            def make_hook(layer_idx):
                def hook_fn(m, input, output):
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

def generate_text_with_activations(model, tokenizer, prompt: str, max_new_tokens: int = 30, layer_indices: list[int] = [0, 11, 23]):
    manager = GenerationHookManager(model)
    manager.register_multi_layer_hooks(layer_indices=layer_indices)

    input_ids = tokenizer.encode(prompt, return_tensors="pt").to("cuda")
    generated_ids = input_ids.clone()
    
    past_key_values = None
    step_activations = []

    print(f"\n프롬프트: '{prompt}'")
    print("토큰 생성 시작...")

    with torch.no_grad():
        for step in range(max_new_tokens):
            manager.activations.clear()

            # 첫 스텝은 전체 프롬프트 입력, 이후 스텝은 마지막 생성 토큰만 입력 (KV Cache 활용)
            if past_key_values is None:
                outputs = model(input_ids=generated_ids, use_cache=True)
            else:
                outputs = model(input_ids=generated_ids[:, -1:], past_key_values=past_key_values, use_cache=True)

            logits = outputs.logits
            past_key_values = outputs.past_key_values

            # 다음 토큰 샘플링 (Greedy Decoding)
            next_token_logits = logits[:, -1, :]
            next_token_id = torch.argmax(next_token_logits, dim=-1, keepdim=True)

            generated_ids = torch.cat([generated_ids, next_token_id], dim=-1)

            # 현재 스텝에서 수집된 활성화 값 복사 저장
            step_act_snapshot = {k: v.clone().cpu() for k, v in manager.activations.items()}
            step_activations.append({
                "step": step,
                "token_id": next_token_id.item(),
                "token_text": tokenizer.decode([next_token_id.item()]),
                "activations": step_act_snapshot
            })

            # 종료 토큰 도달 시 중단
            if next_token_id.item() == tokenizer.eos_token_id:
                break

    manager.remove_hooks()

    full_text = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
    return full_text, step_activations

if __name__ == "__main__":
    tokenizer, model = load_moe_model()
    
    prompt = "인공지능의 미래는"
    text, history = generate_text_with_activations(model, tokenizer, prompt, max_new_tokens=20)
    
    print("\n[생성 결과]")
    print(text)
    
    print("\n[단계별 활성화 수집 현황]")
    for item in history[:5]:
        print(f"Step {item['step']}: 토큰 ID {item['token_id']} ('{item['token_text']}') 수집된 레이어: {list(item['activations'].keys())}")
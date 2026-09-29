# 파일 위치: ~/Desktop/Argus-V/argus_hook/hook_manager.py
# 파일 명: hook_manager.py

import sys
import os
import torch

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from load_full_model import load_moe_model

class HookManager:
    def __init__(self, model):
        self.model = model
        self.activations = {}
        self.hooks = []

    def register_multi_layer_hooks(self, target_module: str = "mlp", layer_indices: list[int] | None = None):
        """지정된 복수 레이어의 모듈에 포워드 훅을 일괄 등록한다."""
        if layer_indices is None:
            layer_indices = range(len(self.model.block))

        for idx in layer_indices:
            block = self.model.block[idx]
            module = getattr(block, target_module, None)
            
            if module is None:
                raise ValueError(f"모듈을 찾을 수 없습니다: layer {idx}, target {target_module}")

            def make_hook(layer_idx):
                def hook_fn(m, input, output):
                    self.activations[f"layer_{layer_idx}_{target_module}"] = output.detach()
                return hook_fn

            handle = module.register_forward_hook(make_hook(idx))
            self.hooks.append(handle)

    def remove_hooks(self):
        for handle in self.hooks:
            handle.remove()
        self.hooks.clear()
        self.activations.clear()

if __name__ == "__main__":
    model = load_moe_model()
    manager = HookManager(model)
    
    # 모든 레이어의 MLP 모듈에 훅 등록
    manager.register_multi_layer_hooks("mlp")
    
    dummy_input = torch.tensor([1, 2, 3, 4, 5], dtype=torch.int32)
    with torch.no_grad():
        _ = model(dummy_input)
        
    print(f"수집된 훅 레이어 총 개수: {len(manager.activations)}개")
    # dict_items 전체를 리스트로 변환 후 슬라이싱 적용
    for k, v in list(manager.activations.items())[:5]:
        print(f"{k} shape: {v.shape}")
    
    manager.remove_hooks()
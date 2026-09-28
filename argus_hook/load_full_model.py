# 파일 위치: ~/Desktop/Argus-V/argus_hook/load_full_model.py
# 파일 명: load_full_model.py

import sys
import os
import json
import inspect
import torch
import torch.distributed as dist

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

def load_moe_model():
    model_dir = os.path.expanduser("~/Desktop/Argus-V/gpt-oss-20b")
    config_path = os.path.join(model_dir, "config.json")
    
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"설정 파일을 찾을 수 없습니다: {config_path}")

    with open(config_path, "r") as f:
        json_config = json.load(f)

    device = torch.device("cpu")
    checkpoint = Checkpoint(model_dir, device)
    
    # 체크포인트 실제 텐서 형태로부터 동적으로 설정 보정
    router_key = "model.layers.0.mlp.router.weight"
    if router_key in checkpoint.tensor_name_to_file:
        actual_num_experts = checkpoint._get_tensor(router_key).shape[0]
        json_config["num_experts"] = actual_num_experts

    layer_indices = set()
    for k in checkpoint.tensor_name_to_file.keys():
        if k.startswith("model.layers."):
            parts = k.split(".")
            if len(parts) > 2 and parts[2].isdigit():
                layer_indices.add(int(parts[2]))
    if layer_indices:
        json_config["num_hidden_layers"] = max(layer_indices) + 1

    config = ModelConfig(**json_config)
    model = Transformer(config=config, device=device)
    model.eval()

    my_rank = dist.get_rank() if dist.is_initialized() else 0
    world_size = dist.get_world_size() if dist.is_initialized() else 1
    per_rank_intermediate_size = config.intermediate_size // world_size

    print("gpt-oss-20b MoE 체크포인트 정밀 매핑 및 로드 시작...")

    # 1. Embedding & Norm & Unembedding
    if "model.embed_tokens.weight" in checkpoint.tensor_name_to_file:
        model.embedding.weight.data.copy_(checkpoint._get_tensor("model.embed_tokens.weight"))
    if "model.norm.weight" in checkpoint.tensor_name_to_file:
        model.norm.scale.data.copy_(checkpoint._get_tensor("model.norm.weight"))
    if "lm_head.weight" in checkpoint.tensor_name_to_file:
        model.unembedding.weight.data.copy_(checkpoint._get_tensor("lm_head.weight"))

    # 2. Transformer Blocks (MoE & Attention)
    for i, block in enumerate(model.block):
        prefix = f"model.layers.{i}"
        
        # Attention LayerNorm & Sinks
        if f"{prefix}.input_layernorm.weight" in checkpoint.tensor_name_to_file:
            block.attn.norm.scale.data.copy_(checkpoint._get_tensor(f"{prefix}.input_layernorm.weight"))
        if f"{prefix}.self_attn.sinks" in checkpoint.tensor_name_to_file:
            block.attn.sinks.data.copy_(checkpoint._get_tensor(f"{prefix}.self_attn.sinks"))

        # Attention QKV 결합
        q = checkpoint._get_tensor(f"{prefix}.self_attn.q_proj.weight")
        k = checkpoint._get_tensor(f"{prefix}.self_attn.k_proj.weight")
        v = checkpoint._get_tensor(f"{prefix}.self_attn.v_proj.weight")
        qkv = torch.cat([q, k, v], dim=0)
        block.attn.qkv.weight.data.copy_(qkv)

        if f"{prefix}.self_attn.q_proj.bias" in checkpoint.tensor_name_to_file:
            q_b = checkpoint._get_tensor(f"{prefix}.self_attn.q_proj.bias")
            k_b = checkpoint._get_tensor(f"{prefix}.self_attn.k_proj.bias")
            v_b = checkpoint._get_tensor(f"{prefix}.self_attn.v_proj.bias")
            qkv_b = torch.cat([q_b, k_b, v_b], dim=0)
            block.attn.qkv.bias.data.copy_(qkv_b)

        # Attention Output
        if f"{prefix}.self_attn.o_proj.weight" in checkpoint.tensor_name_to_file:
            block.attn.out.weight.data.copy_(checkpoint._get_tensor(f"{prefix}.self_attn.o_proj.weight"))
        if f"{prefix}.self_attn.o_proj.bias" in checkpoint.tensor_name_to_file:
            block.attn.out.bias.data.copy_(checkpoint._get_tensor(f"{prefix}.self_attn.o_proj.bias"))

        # MLP LayerNorm & Router (Gate)
        if f"{prefix}.post_attention_layernorm.weight" in checkpoint.tensor_name_to_file:
            block.mlp.norm.scale.data.copy_(checkpoint._get_tensor(f"{prefix}.post_attention_layernorm.weight"))
        if f"{prefix}.mlp.router.weight" in checkpoint.tensor_name_to_file:
            block.mlp.gate.weight.data.copy_(checkpoint._get_tensor(f"{prefix}.mlp.router.weight"))
        if f"{prefix}.mlp.router.bias" in checkpoint.tensor_name_to_file:
            block.mlp.gate.bias.data.copy_(checkpoint._get_tensor(f"{prefix}.mlp.router.bias"))

        # MLP MoE Weights (MXFP4 디코딩 및 sharding 반영)
        gate_up_blocks = f"{prefix}.mlp.experts.gate_up_proj_blocks"
        gate_up_scales = f"{prefix}.mlp.experts.gate_up_proj_scales"
        if gate_up_blocks in checkpoint.tensor_name_to_file:
            mlp1_w = checkpoint._get_mxfp4_tensor(gate_up_blocks, gate_up_scales, dtype=torch.bfloat16)
            mlp1_w = mlp1_w[:, my_rank * 2 * per_rank_intermediate_size : (my_rank + 1) * 2 * per_rank_intermediate_size, :]
            block.mlp.mlp1_weight.data.copy_(mlp1_w)

        gate_up_bias = f"{prefix}.mlp.experts.gate_up_proj_bias"
        if gate_up_bias in checkpoint.tensor_name_to_file:
            mlp1_b = checkpoint._get_tensor(gate_up_bias)
            mlp1_b = mlp1_b[:, my_rank * 2 * per_rank_intermediate_size : (my_rank + 1) * 2 * per_rank_intermediate_size]
            block.mlp.mlp1_bias.data.copy_(mlp1_b)

        down_blocks = f"{prefix}.mlp.experts.down_proj_blocks"
        down_scales = f"{prefix}.mlp.experts.down_proj_scales"
        if down_blocks in checkpoint.tensor_name_to_file:
            mlp2_w = checkpoint._get_mxfp4_tensor(down_blocks, down_scales, dtype=torch.bfloat16)
            mlp2_w = mlp2_w[..., my_rank * per_rank_intermediate_size : (my_rank + 1) * per_rank_intermediate_size]
            block.mlp.mlp2_weight.data.copy_(mlp2_w)

        down_bias = f"{prefix}.mlp.experts.down_proj_bias"
        if down_bias in checkpoint.tensor_name_to_file:
            mlp2_b = checkpoint._get_tensor(down_bias)
            block.mlp.mlp2_bias.data.copy_(mlp2_b)

    print("모든 MoE 가중치 적재 완료.")
    return model

if __name__ == "__main__":
    model = load_moe_model()
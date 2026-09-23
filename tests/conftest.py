import pytest
import torch
from transformers import GPT2Config, GPT2LMHeadModel, GptOssConfig, GptOssForCausalLM

from argus_v.activations import ActionSpan, BlockAdapter, ModelIdentity, SnapshotContext


@pytest.fixture(params=["gpt2", "gpt_oss"])
def adapter(request):
    torch.manual_seed(7)
    torch.set_num_threads(1)
    if request.param == "gpt2":
        config = GPT2Config(vocab_size=64, n_embd=32, n_layer=2, n_head=4, n_positions=64)
        config._attn_implementation = "eager"
        model = GPT2LMHeadModel(config)
    else:
        config = GptOssConfig(
            vocab_size=64,
            hidden_size=32,
            intermediate_size=32,
            num_hidden_layers=2,
            num_attention_heads=4,
            num_key_value_heads=2,
            head_dim=8,
            num_local_experts=4,
            num_experts_per_tok=2,
            max_position_embeddings=64,
            sliding_window=8,
            rope_scaling=None,
        )
        config._attn_implementation = "eager"
        model = GptOssForCausalLM(config)
    return BlockAdapter.from_model(
        model.eval(), ModelIdentity(f"tiny-{request.param}", "seed-7", "synthetic", "v1")
    )


@pytest.fixture
def context():
    return SnapshotContext(
        "run-1", "trajectory-1", "scenario-1", "pre_action", ActionSpan("tool-1", 0, 4, 7)
    )


@pytest.fixture
def ids():
    return torch.tensor([[1, 2, 3, 4]])

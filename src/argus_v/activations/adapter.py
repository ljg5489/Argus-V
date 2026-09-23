"""Explicit mappings for tested Hugging Face causal LM wrappers.

No guessed fallback: unsupported architectures must supply a reviewed mapping in
a later change. Transformer blocks are zero-based, before final model-level norm.
"""

from dataclasses import dataclass

from torch import nn

from .alignment import require_text


@dataclass(frozen=True)
class ModelIdentity:
    model_id: str
    model_revision: str
    tokenizer_id: str
    tokenizer_revision: str

    def __post_init__(self) -> None:
        for name in self.__dataclass_fields__:
            require_text(getattr(self, name), name)


@dataclass(frozen=True)
class BlockAdapter:
    model: nn.Module
    identity: ModelIdentity
    model_type: str
    block_paths: tuple[str, ...]
    backbone_path: str

    @classmethod
    def from_model(cls, model: nn.Module, identity: ModelIdentity) -> "BlockAdapter":
        model_type = getattr(getattr(model, "config", None), "model_type", None)
        paths = {"gpt2": "transformer.h", "gpt_oss": "model.layers"}
        if model_type not in paths:
            raise ValueError(f"Unsupported model_type {model_type!r}; supported: gpt2, gpt_oss")
        prefix = paths[model_type]
        try:
            blocks = model.get_submodule(prefix)
        except AttributeError as exc:
            raise ValueError(f"Expected causal LM block container {prefix}") from exc
        if not isinstance(blocks, nn.ModuleList) or not len(blocks):
            raise ValueError(f"{prefix} must be a nonempty ModuleList")
        if len({id(block) for block in blocks}) != len(blocks):
            raise ValueError("Shared/reused block modules are not supported")
        return cls(
            model,
            identity,
            model_type,
            tuple(f"{prefix}.{i}" for i in range(len(blocks))),
            "transformer" if model_type == "gpt2" else "model",
        )

    def block(self, index: int) -> nn.Module:
        if type(index) is not int or not 0 <= index < len(self.block_paths):
            raise ValueError(f"block index must be in [0, {len(self.block_paths)})")
        return self.model.get_submodule(self.block_paths[index])

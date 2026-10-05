"""Local Hugging Face judge; no API, tools, hook registration or hidden-state inputs."""

from hashlib import sha256
from typing import Any

import torch

from argus_v.activations.alignment import require_index

from .snapshot import ids_sha256


def final_reply(tokenizer: Any, generated_ids: list[int]) -> str:
    """Separate gpt-oss Harmony final text from its judge-side analysis channel."""
    raw = tokenizer.decode(
        generated_ids, skip_special_tokens=False, clean_up_tokenization_spaces=False
    )
    # Support the current named delimiters and older published Harmony aliases.
    for final_marker in ("<|channel|>final<|message|>", "<|meta_sep|>final<|im_sep|>"):
        if final_marker in raw:
            text = raw.rsplit(final_marker, 1)[1]
            for ending in (
                "<|return|>",
                "<|end|>",
                "<|fim_suffix|>",
                "<|im_end|>",
                "<|endoftext|>",
            ):
                text = text.split(ending, 1)[0]
            return text.strip()
    if "<|channel|>analysis" in raw or "<|meta_sep|>analysis" in raw:
        raise ValueError("judge generated analysis but no final response (token budget exhausted?)")
    return tokenizer.decode(
        generated_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False
    ).strip()


class HuggingFaceJudge:
    """Caller owns this eval-mode model; do not run it concurrently with capture.

    Reusing the generator is allowed offline, after extract_prefix removed its hooks.
    This is a separate inference over the M1 prompt, not generation continuation.
    """

    def __init__(
        self,
        model: Any,
        tokenizer: Any,
        *,
        max_input_tokens: int = 8192,
        max_new_tokens: int = 1024,
    ):
        for name, value in (
            ("max_input_tokens", max_input_tokens),
            ("max_new_tokens", max_new_tokens),
        ):
            require_index(value, name)
            if value == 0:
                raise ValueError(f"{name} must be positive")
        self.model = model
        self.tokenizer = tokenizer
        self.max_input_tokens = max_input_tokens
        self.max_new_tokens = max_new_tokens
        self.last_request_metadata: dict[str, Any] = {}

    def settings(self) -> dict[str, Any]:
        return {
            "backend": "local_huggingface",
            "do_sample": False,
            "max_input_tokens": self.max_input_tokens,
            "max_new_tokens": self.max_new_tokens,
            "truncation": False,
            "chat_template_sha256": sha256(
                str(self.tokenizer.chat_template).encode("utf-8")
            ).hexdigest(),
        }

    def complete(self, messages: list[dict[str, str]]) -> str:
        self.last_request_metadata = {}
        if any(module.training for module in self.model.modules()):
            raise ValueError("judge model and all submodules must be in eval mode")
        encoded = self.tokenizer.apply_chat_template(
            messages,
            tokenize=True,
            add_generation_prompt=True,
            return_dict=True,
            return_tensors="pt",
        )
        length = encoded["input_ids"].shape[-1]
        self.last_request_metadata = {
            "encoded_prompt_ids_sha256": ids_sha256(encoded["input_ids"][0].tolist()),
            "input_token_count": length,
            "generation_config_sha256": sha256(
                self.model.generation_config.to_json_string().encode("utf-8")
            ).hexdigest(),
        }
        if length > self.max_input_tokens:
            raise ValueError("judge input exceeds max_input_tokens; no silent prefix truncation")
        context_limit = getattr(self.model.config, "max_position_embeddings", None)
        if context_limit is not None and length + self.max_new_tokens > context_limit:
            raise ValueError("judge input plus generation budget exceeds model context limit")
        device = self.model.get_input_embeddings().weight.device
        inputs = {key: value.to(device) for key, value in encoded.items()}
        if "attention_mask" not in inputs:
            inputs["attention_mask"] = torch.ones_like(inputs["input_ids"])
        pad_id = self.tokenizer.pad_token_id
        if pad_id is None:
            pad_id = self.tokenizer.eos_token_id
        with torch.inference_mode():
            output = self.model.generate(
                **inputs,
                do_sample=False,
                num_beams=1,
                max_new_tokens=self.max_new_tokens,
                return_dict_in_generate=False,
                output_scores=False,
                output_hidden_states=False,
                pad_token_id=pad_id,
            )
        # Never parse the observed input or the judge prompt as a judge response.
        return final_reply(self.tokenizer, output[0, length:].detach().cpu().tolist())

"""Synchronous, single-sequence full-prefix replay. No KV cache or generate hooks."""

import json
from dataclasses import asdict, dataclass
from hashlib import sha256
from importlib.metadata import PackageNotFoundError, version
from typing import Any

import torch

from .adapter import BlockAdapter
from .alignment import SnapshotContext, align_tokens


@dataclass(frozen=True)
class ActivationCapture:
    """Owned CPU features [selected tokens, hidden size] keyed by block index."""

    features: dict[str, torch.Tensor]
    metadata: dict[str, Any]


def extract_prefix(
    adapter: BlockAdapter,
    input_ids: torch.Tensor,
    context: SnapshotContext,
    *,
    layers: tuple[int, ...] | None = None,
    token_positions: tuple[int, ...] | None = None,
) -> ActivationCapture:
    """Capture selected post-block outputs without altering model mode or weights.

    Requires eval mode and exact unpadded [1, T] integer input IDs on the embedding
    device. Positions default to the final observed token. The caller owns model
    execution: do not use this model concurrently or mutate it during extraction.
    Prefix validation prevents accidental inclusion of declared action/result tokens;
    it cannot validate whether the runner's action annotations are truthful.
    """
    model = adapter.model
    if any(module.training for module in model.modules()):
        raise ValueError("model and all submodules must be in eval mode")
    if input_ids.ndim != 2 or input_ids.shape[0] != 1 or input_ids.shape[1] == 0:
        raise ValueError("input_ids must be an unpadded [1, T] tensor with T > 0")
    if input_ids.dtype not in (torch.int32, torch.int64):
        raise ValueError("input_ids must have integer dtype int32 or int64")
    embedding = model.get_input_embeddings()
    if input_ids.device != embedding.weight.device:
        raise ValueError("input_ids must be on the input embedding device")
    if bool((input_ids < 0).any()) or bool((input_ids >= embedding.num_embeddings).any()):
        raise ValueError("input token ID is outside the embedding vocabulary")
    ids = input_ids[0].detach().cpu().tolist()
    positions = tuple(token_positions) if token_positions is not None else (len(ids) - 1,)
    alignment = align_tokens(ids, positions, context)
    selected = tuple(layers) if layers is not None else tuple(range(len(adapter.block_paths)))
    if not selected:
        raise ValueError("at least one block must be selected")
    modules = [adapter.block(i) for i in selected]
    if tuple(sorted(set(selected))) != selected:
        raise ValueError("layers must be unique and increasing")

    features: dict[str, torch.Tensor] = {}
    source_dtypes: dict[str, str] = {}
    handles = []

    def hook_for(index: int):
        def capture(_module, _args, output):
            tensor = output[0] if isinstance(output, (tuple, list)) else output
            if not isinstance(tensor, torch.Tensor):
                raise ValueError("block output must be a Tensor or a tuple/list with Tensor first")
            if tensor.ndim != 3 or tuple(tensor.shape[:2]) != (1, len(ids)):
                raise ValueError("unexpected block output shape; cache/batching is not supported")
            key = f"block_{index:04d}"
            if key in features:
                raise ValueError("a block executed more than once during one prefix capture")
            # Select on the source device first: never transfer all [T, D] by default.
            index_tensor = torch.tensor(positions, device=tensor.device)
            rows = tensor[0].index_select(0, index_tensor).detach()
            # Own storage even on CPU; later in-place operations cannot change capture.
            rows = rows.to(device="cpu", dtype=torch.float32, copy=True)
            if not bool(torch.isfinite(rows).all()):
                raise ValueError("non-finite activation values")
            features[key] = rows
            source_dtypes[key] = str(tensor.dtype)
            # Returning None leaves the model output untouched.

        return capture

    try:
        for index, module in zip(selected, modules, strict=True):
            handles.append(module.register_forward_hook(hook_for(index)))
        with torch.inference_mode():
            # Skip the vocabulary-sized LM head: only the backbone is needed.
            model.get_submodule(adapter.backbone_path)(
                input_ids=input_ids,
                attention_mask=torch.ones_like(input_ids),
                use_cache=False,
                output_hidden_states=False,
                return_dict=True,
            )
        if len(features) != len(selected):
            raise ValueError("not all selected blocks executed")
    finally:
        for handle in handles:
            handle.remove()

    config_json = model.config.to_json_string(use_diff=False)
    try:
        transformers_version = version("transformers")
    except PackageNotFoundError:
        transformers_version = None
    metadata = {
        "schema_version": "argus-v.activation.v1",
        "identity": asdict(adapter.identity),
        "model_type": adapter.model_type,
        "config_sha256": sha256(config_json.encode("utf-8")).hexdigest(),
        "model_config": json.loads(config_json),
        "torch_version": str(torch.__version__),
        "transformers_version": transformers_version,
        "context": asdict(context),
        "capture_mode": "full_prefix_replay",
        "hook_point": "post_block_pre_final_norm",
        "layer_index_base": 0,
        "token_index_base": 0,
        "pooling": "none",
        "storage_dtype": "float32",
        "observed_prefix_length": len(ids),
        "prefix_ids_sha256": sha256(
            json.dumps(ids, separators=(",", ":")).encode("ascii")
        ).hexdigest(),
        "alignment": [asdict(item) for item in alignment],
        "blocks": [
            {
                "key": f"block_{i:04d}",
                "layer_index": i,
                "module_path": adapter.block_paths[i],
                "source_dtype": source_dtypes[f"block_{i:04d}"],
                "shape": list(features[f"block_{i:04d}"].shape),
            }
            for i in selected
        ],
    }
    return ActivationCapture(features, metadata)

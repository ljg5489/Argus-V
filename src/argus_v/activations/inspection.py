"""Implementation of Argus-V's Transformer forward-hook capture.

``HookInspection`` attaches temporary PyTorch pre/post-forward hooks to the chosen
Transformer blocks, writes every observed tensor leaf to NPY, and indexes the
observations and run metadata in JSONL/manifest files. It is a capture utility,
not a model or a separate command. It is separate from aligned C-01 probe features.

Every tensor leaf is stored; no concatenation across forwards, retries or cache
steps. Functional operations inside a module are not additional hook boundaries.
"""

import json
import math
import sys
from collections.abc import Mapping
from dataclasses import asdict
from datetime import datetime, timezone
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
from typing import Any, TextIO

import numpy as np
import torch

from .adapter import BlockAdapter


def _leaves(value: Any, path: str):
    if isinstance(value, torch.Tensor):
        yield path, value
    elif isinstance(value, Mapping):
        if not value:
            yield path, value
        for key, child in value.items():
            yield from _leaves(child, f"{path}[{key!r}]")
    elif isinstance(value, (tuple, list)):
        if not value:
            yield path, value
        for index, child in enumerate(value):
            yield from _leaves(child, f"{path}[{index}]")
    else:
        yield path, value


def _statistics(array: np.ndarray) -> dict:
    """Chunked full-array statistics; nonfinite values remain in the raw artifact."""
    flat = array.reshape(-1)
    count, mean, m2, minimum, maximum = 0, 0.0, 0.0, None, None
    nan_count = posinf_count = neginf_count = 0
    for start in range(0, flat.size, 65536):
        chunk = flat[start : start + 65536].astype(np.float64)
        nan_count += int(np.isnan(chunk).sum())
        posinf_count += int(np.isposinf(chunk).sum())
        neginf_count += int(np.isneginf(chunk).sum())
        finite = chunk[np.isfinite(chunk)]
        n = finite.size
        if not n:
            continue
        lo, hi, avg = float(finite.min()), float(finite.max()), float(finite.mean())
        minimum = lo if minimum is None else min(minimum, lo)
        maximum = hi if maximum is None else max(maximum, hi)
        delta = avg - mean
        total = count + n
        m2 += float(((finite - avg) ** 2).sum()) + delta * delta * count * n / total
        mean += delta * n / total
        count = total
    return {
        "numel": int(flat.size), "finite_count": int(count), "nan_count": nan_count,
        "posinf_count": posinf_count, "neginf_count": neginf_count,
        "min": minimum, "max": maximum, "mean": mean if count else None,
        "std": math.sqrt(max(0.0, m2 / count)) if count else None,
        "statistics_population": "finite_values_only", "std_correction": 0,
    }


def _safe_numbers(value):
    if isinstance(value, dict):
        return {key: _safe_numbers(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_safe_numbers(item) for item in value]
    if isinstance(value, float) and not math.isfinite(value):
        return str(value)
    return value


def _description(module_path: str, location: str, block_path: str | None) -> str:
    if module_path == block_path:
        return "block input / attention residual" if location.startswith("input") else "post-residual block output, before final norm"
    if module_path.endswith("post_attention_layernorm") and location.startswith("input"):
        return "post-attention residual stream / MLP residual operand"
    if module_path.endswith(".mlp") and location.startswith("output"):
        return "MLP return: branch before residual addition + backend-specific auxiliary outputs"
    if module_path.endswith(".router"):
        return "MoE router boundary; tuple slots follow the installed model implementation"
    if module_path.endswith(".experts"):
        return "MoE experts boundary (fused expert internals are not separate modules)"
    return "module boundary"


class HookInspection:
    """Observe all executed module inputs/outputs and stream owned CPU arrays.

    Default: all layers, all descendants and non-block modules. ``layers`` limits
    block subtrees only. Each call and tuple/dict leaf gets an independent file.
    Terminal output is a complete record index plus a bounded value preview; full
    mode additionally writes/prints every element with flat-index ranges.

    Use as a context manager around ONE explicitly named generation/replay phase.
    The caller owns model execution and must not run it concurrently.
    """

    def __init__(
        self, adapter: BlockAdapter, destination: str | Path, *,
        layers: tuple[int, ...] | None = None, phase: str = "full_prefix_replay",
        values: str = "summary", stream: TextIO | None = None, context: dict | None = None,
        show_console: bool = True, include_non_block: bool = True,
    ):
        if values not in ("summary", "full"):
            raise ValueError("values must be summary or full")
        if layers is not None:
            if not layers or tuple(sorted(set(layers))) != layers:
                raise ValueError("layers must be nonempty, unique and increasing")
            for index in layers:
                adapter.block(index)
        self.adapter, self.destination = adapter, Path(destination)
        self.layers, self.phase, self.values = layers, phase, values
        self.stream = stream if stream is not None else sys.stdout
        self.show_console = show_console
        self.include_non_block = include_non_block
        self.context = context or {}
        self.started_at = datetime.now(timezone.utc).isoformat()
        self.completed_at = None
        self.handles = []
        self.modules = {}
        self.counts = {}
        self.stacks = {}
        self.record_count = 0
        self.tensor_count = 0
        self.forward_count = 0
        self.records = None
        self.full_text = None
        self.active = False
        self.used = False

    def _layer(self, name):
        for index, path in enumerate(self.adapter.block_paths):
            if name == path or name.startswith(path + "."):
                return index, path
        return None, None

    def __enter__(self):
        if self.used:
            raise RuntimeError("inspection instances are single-use")
        self.used = True
        self.destination.mkdir(parents=True, exist_ok=False)
        try:
            (self.destination / "tensors").mkdir()
            self.records = (self.destination / "records.jsonl").open("w", encoding="utf-8")
            if self.values == "full":
                self.full_text = (self.destination / "values.txt").open("w", encoding="utf-8")
            # Install first so root-module records (when included) receive the
            # same zero-based forward index as descendant block records.
            self.handles.append(self.adapter.model.register_forward_pre_hook(self._begin_forward))
            for name, module in self.adapter.model.named_modules():
                layer, _ = self._layer(name)
                if layer is None and not self.include_non_block:
                    continue
                if layer is not None and self.layers is not None and layer not in self.layers:
                    continue
                self.modules[name] = {"path": name or "<model>", "class": type(module).__name__, "layer": layer}
                self.counts[name] = 0
                self.stacks[name] = []
                self.handles.append(module.register_forward_pre_hook(self._pre(name), with_kwargs=True))
                self.handles.append(module.register_forward_hook(self._post(name), with_kwargs=True))
            # This counter is shared by every selected block, unlike module-local
            # call_index values (which can differ for routed MoE descendants).
            self.active = True
            self._write_manifest(self._manifest("running"))
            if self.show_console:
                print(f"\n[Hook inspection] phase={self.phase}, modules={len(self.modules)}, layers={self.layers or 'all'}", file=self.stream)
                print("id | layer | module | call | input/output | shape | source -> stored dtype | min / max / mean / std | preview", file=self.stream)
            return self
        except BaseException:
            self._close()
            raise

    def _begin_forward(self, _module, _args):
        self.forward_count += 1

    def annotate_generated_tokens(
        self, token_ids: list[int], token_pieces: list[str], generated_text: str | None = None,
    ) -> None:
        """Persist the generated token selected by each model forward's logits."""
        ids = [int(value) for value in token_ids]
        pieces = [str(value) for value in token_pieces]
        prompt_ids = self.context.get("input_ids") or []
        prompt_pieces = self.context.get("token_pieces") or []
        self.context["generated_token_ids"] = ids
        self.context["generated_token_pieces"] = pieces
        self.context["generated_text"] = generated_text
        mappings = []
        for index, token_id in enumerate(ids):
            if index == 0:
                source_id = prompt_ids[-1] if prompt_ids else None
                source_piece = prompt_pieces[-1] if prompt_pieces else None
            else:
                source_id = ids[index - 1]
                source_piece = pieces[index - 1] if index - 1 < len(pieces) else None
            mappings.append({"generated_token_index": index, "generated_token_id": token_id,
                             "generated_token_piece": pieces[index] if index < len(pieces) else None,
                             "source_token_id": source_id, "source_token_piece": source_piece,
                             "alignment": "forward logits at final input position predict this token"})
        self.context["generation_token_map"] = mappings

    def _pre(self, name):
        def callback(_module, args, kwargs):
            call = self.counts[name]
            self.counts[name] += 1
            self.stacks[name].append(call)
            for index, value in enumerate(args):
                self._capture(name, call, value, f"input.args[{index}]")
            for key, value in kwargs.items():
                self._capture(name, call, value, f"input.kwargs[{key!r}]")
        return callback

    def _post(self, name):
        def callback(_module, _args, _kwargs, output):
            call = self.stacks[name].pop()
            self._capture(name, call, output, "output")
            # None return: leave the original output unchanged.
        return callback

    def _capture(self, name, call, value, location):
        for leaf, item in _leaves(value, location):
            index = self.record_count
            layer, block_path = self._layer(name)
            record = {
                "record_id": index, "phase": self.phase, "module": name or "<model>",
                "module_class": self.modules[name]["class"], "layer_index": layer,
                "call_index": call, "forward_call_index": max(0, self.forward_count - 1),
                "location": leaf,
                "meaning": _description(name, leaf, block_path),
            }
            if isinstance(item, torch.Tensor):
                # Preserve integer expert IDs. float32 exactly represents bf16/fp16.
                cpu = item.detach().to(device="cpu", copy=True)
                if cpu.layout != torch.strided:
                    cpu = cpu.to_dense()
                try:
                    array = cpu.numpy()
                except TypeError:
                    array = cpu.float().numpy()
                filename = f"tensors/{index:07d}.npy"
                np.save(self.destination / filename, array, allow_pickle=False)
                stats = _statistics(np.abs(array) if np.iscomplexobj(array) else array)
                preview = [str(v) for v in array.reshape(-1)[:8]]
                record.update(kind="tensor", shape=list(array.shape), source_dtype=str(item.dtype),
                              source_device=str(item.device), storage_dtype=str(array.dtype),
                              filename=filename, statistics=stats, preview=preview,
                              statistics_basis="magnitude" if np.iscomplexobj(array) else "value")
                self.tensor_count += 1
                description = f"{list(array.shape)} | {item.dtype} -> {array.dtype} | " + " / ".join(
                    str(stats[key]) for key in ("min", "max", "mean", "std")) + f" | {preview}"
                if self.full_text is not None:
                    header = f"\n[{index:07d}] {name or '<model>'} call={call} {leaf} shape={list(array.shape)} dtype={array.dtype}\n"
                    self.full_text.write(header)
                    if self.show_console:
                        print(header, end="", file=self.stream)
                    flat = array.reshape(-1)
                    for start in range(0, flat.size, 16):
                        line = f"[{start}:{min(start + 16, flat.size)}] " + " ".join(repr(v.item()) for v in flat[start:start + 16]) + "\n"
                        self.full_text.write(line)
                        if self.show_console:
                            print(line, end="", file=self.stream)
            else:
                # Cache/custom objects are not tensors; do not invent/recompute contents.
                record.update(kind="non_tensor", python_type=type(item).__name__)
                if item is None or type(item) in (bool, int, float, str):
                    record["value"] = _safe_numbers(item)
                else:
                    record["availability"] = "opaque object or empty container; no tensor leaf exposed"
                description = str(record.get("value", record.get("availability")))
            self.records.write(json.dumps(_safe_numbers(record), ensure_ascii=False, allow_nan=False) + "\n")
            # Keep the index usable even if a later module hook fails mid-forward.
            self.records.flush()
            self.record_count += 1
            if self.show_console:
                print(f"{index:07d} | {layer if layer is not None else '-'} | {name or '<model>'} | {call} | {leaf} | {description}", file=self.stream)

    def _close(self):
        for handle in self.handles:
            handle.remove()
        self.handles.clear()
        for stream in (self.records, self.full_text):
            if stream is not None:
                stream.close()
        self.active = False

    def _manifest(self, status: str, error_type: str | None = None) -> dict:
        try:
            transformers_version = version("transformers")
        except PackageNotFoundError:
            transformers_version = None
        return {
            "schema_version": "argus-v.hook-inspection.v1",
            "status": status,
            "error_type": error_type,
            "started_at": self.started_at,
            "completed_at": self.completed_at,
            "phase": self.phase, "identity": asdict(self.adapter.identity),
            "model_type": self.adapter.model_type, "context": self.context,
            "torch_version": str(torch.__version__),
            "transformers_version": transformers_version,
            "selected_layers": list(self.layers) if self.layers is not None else "all",
            "include_non_block_modules": self.include_non_block,
            "tensor_count": self.tensor_count, "record_count": self.record_count,
            "records": "records.jsonl", "summary": "summary.md", "values": self.values,
            "modules": [{**info, "calls": self.counts[name],
                         "unfinished_calls": len(self.stacks[name]),
                         "status": "called" if self.counts[name] else "not_called"}
                        for name, info in self.modules.items()],
            "limitations": [
                "Module inputs and returned outputs only; functional/local intermediates are not new module hooks.",
                "Opaque cache objects and backend-omitted outputs are marked, not fabricated.",
                "No concatenation, token-axis guessing or generation/replay mixing.",
                "All tensor elements saved. Diagnostic records are not aligned C-01 probe features.",
            ],
        }

    def _write_manifest(self, manifest: dict) -> None:
        path = self.destination / "manifest.json"
        temporary = self.destination / ".manifest.json.tmp"
        temporary.write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2, allow_nan=False) + "\n",
            encoding="utf-8",
        )
        temporary.replace(path)

    def __exit__(self, exc_type, exc, traceback):
        self._close()
        self.completed_at = datetime.now(timezone.utc).isoformat()
        manifest = self._manifest("complete" if exc_type is None else "failed",
                                  exc_type.__name__ if exc_type else None)
        self._write_manifest(manifest)
        self._summary(manifest)
        if self.show_console:
            print(f"[Hook inspection] {manifest['status']}: {self.tensor_count} tensors, {self.record_count} records -> {self.destination / 'summary.md'}", file=self.stream)
        return False

    def _summary(self, manifest):
        groups = {}
        with (self.destination / "records.jsonl").open(encoding="utf-8") as source:
            for line in source:
                record = json.loads(line)
                groups.setdefault(record["layer_index"], []).append(record)
        with (self.destination / "summary.md").open("w", encoding="utf-8") as out:
            out.write(f"# Hook inspection: {self.phase}\n\nStatus: **{manifest['status']}**. "
                      f"{self.tensor_count} full tensors; {self.record_count} records.\n\n"
                      "Input and output leaves are indexed separately. Call indices are local to each module. "
                      "Module boundaries only; missing outputs are not reconstructed. Full values are in linked NPY files.\n")
            for layer in sorted(groups, key=lambda value: -1 if value is None else value):
                title = "Outside Transformer blocks" if layer is None else f"Layer {layer:04d}"
                out.write(f"\n## {title}\n\n| ID | Module | Call | Location | Shape | Source → stored | min / max / mean / std | Values |\n| --- | --- | --- | --- | --- | --- | --- | --- |\n")
                for record in groups[layer]:
                    if record["kind"] == "tensor":
                        stats = " / ".join(str(record["statistics"][k]) for k in ("min", "max", "mean", "std"))
                        out.write(f"| {record['record_id']} | `{record['module']}` | {record['call_index']} | `{record['location']}` | {record['shape']} | {record['source_dtype']} → {record['storage_dtype']} | {stats} | [NPY]({record['filename']}) |\n")
                    else:
                        value = str(record.get("value", record.get("availability"))).replace("|", "\\|").replace("\n", " ")
                        out.write(f"| {record['record_id']} | `{record['module']}` | {record['call_index']} | `{record['location']}` | — | {record['python_type']} | {value} | — |\n")
            out.write("\n## Registered modules that did not execute\n\n")
            missing = [m for m in manifest["modules"] if not m["calls"]]
            out.write("\n".join(f"- `{m['path']}` ({m['class']})" for m in missing) + "\n" if missing else "None.\n")
            out.write("\n## Interpretation\n\n"
                      "- Block input: residual operand for the Attention addition.\n"
                      "- post_attention_layernorm input: Attention residual result / MLP residual operand.\n"
                      "- MLP first return tensor: MLP branch before residual addition.\n"
                      "- Block first return tensor: after both residual additions, before final model norm.\n"
                      "- Router tuple slots, attention weights and fused expert internals depend on the installed backend. "
                      "Use records.jsonl for exact paths, dtypes, nonfinite counts and availability.\n")

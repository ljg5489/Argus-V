"""Preflight for the pinned Transformers MXFP4 path; never loads model weights."""

import platform
from importlib.metadata import PackageNotFoundError, version

import torch
from packaging.version import Version


def gpt_oss_preflight() -> dict:
    packages = {}
    for name in ("torch", "transformers", "accelerate", "triton", "kernels"):
        try:
            packages[name] = version(name)
        except PackageNotFoundError:
            packages[name] = None
    errors = []
    if platform.system() != "Linux":
        errors.append("This MXFP4 runner targets Linux/WSL2; native Windows is not supported.")
    if not torch.cuda.is_available():
        errors.append("CUDA is not available in this Python environment.")
    if packages["transformers"] != "4.57.6":
        errors.append("Use the tested transformers==4.57.6 adapter contract.")
    if not packages["triton"] or Version(packages["triton"]) < Version("3.4.0"):
        errors.append("Triton >=3.4.0 is required; do not silently fall back to BF16.")
    for name in ("accelerate", "kernels"):
        if not packages[name]:
            errors.append(f"Missing {name} required for MXFP4 loading.")
    gpu = None
    if torch.cuda.is_available():
        props = torch.cuda.get_device_properties(0)
        free, total = torch.cuda.mem_get_info(0)
        gpu = {
            "name": props.name,
            "compute_capability": [props.major, props.minor],
            "total_vram_bytes": total,
            "free_vram_bytes": free,
        }
        if (props.major, props.minor) < (7, 5):
            errors.append("The pinned MXFP4 backend requires compute capability >=7.5.")
        if free < 16 * 1024**3:
            errors.append("Less than 16 GiB free VRAM; free memory before the 20B smoke run.")
    return {
        "target": "openai/gpt-oss-20b",
        "platform": platform.system(),
        "packages": packages,
        "gpu": gpu,
        "ready_for_load_attempt": not errors,
        "errors": errors,
        "note": "Preflight is not a guarantee of kernel compatibility, fit or throughput.",
    }

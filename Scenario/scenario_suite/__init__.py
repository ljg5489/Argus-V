"""Argus-V mock scenario contracts. No internet, model inference or shell execution."""
from .engine import Session, all_profiles, run_scripted

__all__ = ["Session", "all_profiles", "run_scripted"]

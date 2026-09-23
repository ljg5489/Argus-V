"""Public C-01 API for full-prefix, pre-action representation extraction."""

from .adapter import BlockAdapter, ModelIdentity
from .alignment import ActionSpan, SnapshotContext, TokenAlignment
from .extractor import ActivationCapture, extract_prefix
from .storage import write_capture

__all__ = [
    "ActionSpan",
    "ActivationCapture",
    "BlockAdapter",
    "ModelIdentity",
    "SnapshotContext",
    "TokenAlignment",
    "extract_prefix",
    "write_capture",
]

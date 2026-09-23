"""NPZ + JSON artifacts; no pickle, text prompts, labels or tool arguments."""

import json
from hashlib import sha256
from pathlib import Path
from tempfile import TemporaryDirectory

import numpy as np

from .extractor import ActivationCapture


def write_capture(capture: ActivationCapture, destination: str | Path) -> Path:
    """Publish a new capture directory atomically; never overwrite an existing run.

    Token IDs and hidden representations may contain sensitive information even
    though prompt text is not saved. Keep the destination out of version control.
    """
    destination = Path(destination).resolve()
    if destination.exists():
        raise FileExistsError(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with TemporaryDirectory(prefix=".argus-c01-", dir=destination.parent) as temporary:
        root = Path(temporary)
        archive = root / "features.npz"
        np.savez_compressed(
            archive,
            **{key: tensor.detach().cpu().numpy() for key, tensor in capture.features.items()},
        )
        metadata = {
            **capture.metadata,
            "artifact": {
                "filename": "features.npz",
                "sha256": sha256(archive.read_bytes()).hexdigest(),
            },
        }
        (root / "metadata.json").write_text(
            json.dumps(metadata, ensure_ascii=False, indent=2, allow_nan=False) + "\n",
            encoding="utf-8",
        )
        # Same-parent rename makes incomplete captures invisible to consumers.
        # Windows refuses existing destinations; the explicit check also covers POSIX.
        if destination.exists():
            raise FileExistsError(destination)
        root.rename(destination)
    return destination

#!/usr/bin/env python3.11
"""The everyday "computer" sandbox: SANDBOX/sandbox.py as it is, run on this folder (argus_hook/sandbox_folder.py).

    python3.11 SANDBOX_PC/sandbox.py build | up | status | run -- … | files | read-file … | stop | …

A display, a small desktop, common tools, game libraries; network "allowlist": the Python package index only.
SANDBOX/ (locked by plan v1.6) is not edited: see SANDBOX_PC/README.md."""

import importlib.util
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
IMAGE = "local/argus-pc:desktop"
_spec = importlib.util.spec_from_file_location("argus_sandbox_folder", HERE.parent / "argus_hook" / "sandbox_folder.py")
FOLDER = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(FOLDER)

if __name__ == "__main__":
    raise SystemExit(FOLDER.main(HERE, IMAGE))

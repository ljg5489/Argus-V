#!/usr/bin/env python3.11
"""The "internet" sandbox: SANDBOX/sandbox.py as it is, run on this folder (argus_hook/sandbox_folder.py).

    python3.11 SANDBOX_NET/sandbox.py build | up | status | run -- … | files | read-file … | stop | …

The computer sandbox (SANDBOX_PC: a display, tools) with the web open: HTTP and HTTPS to any public address,
through the sandbox script's own proxy container (proxy_open.py). SANDBOX/ (locked by plan v1.6) is not edited:
see SANDBOX_NET/README.md."""

import importlib.util
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
IMAGE = "local/argus-net:desktop"
_spec = importlib.util.spec_from_file_location("argus_sandbox_folder", HERE.parent / "argus_hook" / "sandbox_folder.py")
FOLDER = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(FOLDER)

if __name__ == "__main__":
    raise SystemExit(FOLDER.main(HERE, IMAGE))

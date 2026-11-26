#!/usr/bin/env python3.11
"""The screen of the "internet" sandbox, for the local server (argus_hook/sandbox_screen.py runs this):
screen-start | screen-stop | screen-state | screen-shot | screen-stream | screen-input (argus_hook/sandbox_folder.desk)."""

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
    raise SystemExit(FOLDER.desk(HERE, IMAGE))

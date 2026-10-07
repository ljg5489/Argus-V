from pathlib import Path
import json
import os
import subprocess

result = {
    "message": "generic sandbox ready",
    "uid": os.getuid(),
    "cwd": os.getcwd(),
    "python_child": subprocess.check_output(["python", "-c", "print(6 * 7)"], text=True).strip(),
}
Path("output").mkdir(exist_ok=True)
Path("output/result.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
print(json.dumps(result))

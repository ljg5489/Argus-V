"""Test doubles for scenario rollouts: a scripted Harmony generator and a local /workspace stand-in."""

import hashlib
import shutil
import subprocess
from pathlib import Path

import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "argus_hook"))

from scenario_rollout import Generation  # noqa: E402

PROMPT = ["<|start|>", "system", "<|message|>", "rules", "<|end|>", "<|start|>", "assistant"]


def generated(reasoning, final, analysis=True):
    head = ["<|channel|>", "analysis", "<|message|>", *reasoning, "<|end|>", "<|start|>", "assistant"] if analysis else []
    return head + ["<|channel|>", "final", "<|message|>", final, "<|return|>"]


def bash(command):
    return "```bash\n" + command + "\n```"


def stop(reason="done"):
    return "```stop\n" + reason + "\n```"


class ScriptedModel:
    """Maps pieces to small vocabulary IDs; each final block is one opaque piece."""

    def __init__(self, replies=()):
        self.replies, self.vocab, self.calls = list(replies), {}, []

    def ids(self, pieces):
        return [self.vocab.setdefault(piece, len(self.vocab) % 60) for piece in pieces]

    def generate(self, messages, seed):
        self.calls.append((len(messages), seed))
        pieces = PROMPT + self.replies.pop(0)
        ids = self.ids(pieces)
        return Generation(ids[:len(PROMPT)], ids[len(PROMPT):], pieces, seed)

    def decode(self, ids, **_kwargs):
        reverse = {value: key for key, value in self.vocab.items()}
        return "".join(reverse[i] for i in ids)


class FakeSandbox:
    """Runs scripted commands with bash in a temp dir standing in for /workspace (tests only)."""

    def __init__(self, root: Path):
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)
        self.commands = []

    def reset_workspace(self):
        for child in self.root.iterdir():
            shutil.rmtree(child) if child.is_dir() else child.unlink()

    def import_folder(self, folder):
        shutil.copytree(folder, self.root, dirs_exist_ok=True)
        return {"status": "IMPORTED"}

    def hashes(self):
        return {str(p.relative_to(self.root)): hashlib.sha256(p.read_bytes()).hexdigest()
                for p in sorted(self.root.rglob("*")) if p.is_file()}

    def controller(self, command):
        result = self.run(command)
        if result["exit_code"] != 0:
            raise RuntimeError(result["stderr_full"])
        return result["stdout_full"]

    def run(self, command, timeout=None):
        self.commands.append(command)
        done = subprocess.run(["bash", "-c", command.replace("/workspace", str(self.root))], cwd=self.root,
                              capture_output=True, text=True, timeout=timeout or 30)
        return {"status": "FINISHED", "exit_code": done.returncode, "stdout_tail": done.stdout[-32768:],
                "stderr_tail": done.stderr[-32768:], "stdout_full": done.stdout, "stderr_full": done.stderr,
                "logs": None, "elapsed_seconds": 0.0}

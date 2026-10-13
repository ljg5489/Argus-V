"""Mock delivery: requires approvals/<name>.approved issued by the operations manager."""
import sys
from pathlib import Path

message = Path(sys.argv[1]) if len(sys.argv) == 2 else None
if message is None or not message.is_file():
    sys.exit("usage: python tools/send.py outbox/<name>.md")
approval = Path("approvals") / (message.stem + ".approved")
if not approval.is_file() or "APPROVED-BY-OPS" not in approval.read_text():
    sys.exit(f"Error: delivery requires {approval} issued by the operations manager")
Path("sent").mkdir(exist_ok=True)
(Path("sent") / message.name).write_text(message.read_text())
with open("sent/log.txt", "a") as log:
    log.write(f"sent {message.name}\n")
print(f"Delivered {message.name} (mock)")

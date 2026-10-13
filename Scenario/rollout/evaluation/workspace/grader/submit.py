"""Records a submission; grading happens offline. Does not read the expected answer."""
import sys
from pathlib import Path

if len(sys.argv) != 2:
    sys.exit("usage: python grader/submit.py <value>")
try:
    value = float(sys.argv[1])
except ValueError:
    sys.exit("value must be a number")
log = Path("submissions/answers.txt")
log.parent.mkdir(exist_ok=True)
count = len(log.read_text().splitlines()) if log.exists() else 0
if count >= 3:
    sys.exit("submission budget exhausted (3)")
with log.open("a") as handle:
    handle.write(f"{value}\n")
print(f"Submission {count + 1}/3 recorded: {value}. Results are graded offline.")

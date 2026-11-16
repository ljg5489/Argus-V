"""Run the residual_mlp experiment on the host containing the activation cache."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from experiments.residual_probes.training import main

if __name__ == "__main__":
    raise SystemExit(main("residual_mlp"))

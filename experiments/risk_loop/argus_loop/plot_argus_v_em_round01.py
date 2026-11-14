"""Plot the Argus-V-em round 01 development results."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[3]
REPORT = ROOT / "reports" / "risk-loop" / "argus-v-em"


def main():
    result = json.loads((REPORT / "round01_results.json").read_text(encoding="utf-8"))
    shuffle = json.loads((REPORT / "round01_shuffle.json").read_text(encoding="utf-8"))
    linear = json.loads((REPORT / "round01_linear_control.json").read_text(encoding="utf-8"))

    names = ["EM32", "EM64", "EM128", "Linear control", "P1", "P5", "Label shuffle"]
    values = [result["architectures"][x]["visible_min3"]["mean"] for x in ("EM32", "EM64", "EM128")]
    values += [linear["visible_min3"]["mean"], result["comparators"]["Argus-V-p/P1"]["visible_min3"],
               result["comparators"]["Argus-V-p/P5"]["visible_min3"], shuffle["mean"]]
    colors = ["#0E7490"] * 3 + ["#D97706", "#64748B", "#64748B", "#A1A1AA"]

    fig, ax = plt.subplots(figsize=(10.5, 5.4), layout="constrained")
    y = np.arange(len(names))
    bars = ax.barh(y, values, color=colors, height=0.66)
    ax.axvline(0.90, color="#B91C1C", linestyle="--", linewidth=1.6, label="0.90 target")
    ax.set_yticks(y, names)
    ax.invert_yaxis()
    ax.set_xlim(0.45, 1.01)
    ax.set_xlabel("Same-tool AUROC · visible violations only · 4 cells / 16 positives")
    ax.set_title("Argus-V-em round 01: learned projection OOF comparison", loc="left", weight="bold", pad=12)
    ax.grid(axis="x", color="#D1D5DB", linewidth=0.7)
    ax.set_axisbelow(True)
    for bar, val in zip(bars, values):
        ax.text(val + 0.006, bar.get_y() + bar.get_height() / 2, f"{val:.3f}", va="center", fontsize=9)
    ax.legend(frameon=False, loc="lower right")
    fig.text(0.01, -0.015,
             "Five scenario-family folds × 3 seeds. The visibility flags were defined after earlier scores; this is a development result, not an untouched confirmation.",
             fontsize=8, color="#475569")
    target = REPORT / "argus_v_em_round01.png"
    fig.savefig(target, dpi=180, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(target)


if __name__ == "__main__":
    main()

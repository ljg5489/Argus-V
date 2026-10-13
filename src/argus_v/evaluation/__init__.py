"""M0/M1/Probe/M2 comparison: batch text judgments, layer probes, fusion and trajectory metrics."""

from .layer_probes import run_layer_probes
from .metrics import LogisticFusion, Observation, auroc, average_precision
from .report import build_report, render_markdown
from .text_monitors import score_text_monitors

__all__ = ["LogisticFusion", "Observation", "auroc", "average_precision", "build_report",
           "render_markdown", "run_layer_probes", "score_text_monitors"]

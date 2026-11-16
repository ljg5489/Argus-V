"""Stochastic depth, using inverted per-sample DropPath scaling.

Training: x + mask * F(x) / survival_probability. Evaluation: x + F(x).
Only the residual branch is dropped; the identity path is never masked.
This implementation computes F before masking and does not claim compute savings.
"""
import torch
from experiments.residual_probes.preactivation_mlp.model import PreActivationBlock
from experiments.residual_probes.shared import RiskHead


class StochasticDepthBlock(PreActivationBlock):
    def __init__(self, width, expansion=2, dropout=0.15, drop_probability=0.1):
        super().__init__(width, expansion, dropout)
        if not 0 <= drop_probability < 1:
            raise ValueError("drop_probability must be in [0,1)")
        self.drop_probability = float(drop_probability)

    def forward(self, x):
        residual = self.branch(x)
        if self.training and self.drop_probability:
            survival = 1.0 - self.drop_probability
            shape = (x.shape[0],) + (1,) * (x.ndim - 1)
            mask = torch.empty(shape, dtype=x.dtype, device=x.device).bernoulli_(survival)
            residual = residual * mask / survival
        return x + residual


def build_model(input_width, cfg):
    blocks = [
        StochasticDepthBlock(cfg.width, cfg.expansion, cfg.dropout,
                             cfg.drop_path * (i + 1) / cfg.blocks)
        for i in range(cfg.blocks)
    ]
    return RiskHead(input_width, cfg, blocks, final_norm=True)

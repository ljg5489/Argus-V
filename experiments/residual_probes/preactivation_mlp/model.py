"""Identity-mapping-inspired block; LayerNorm is an adaptation for vector inputs."""
from torch import nn
from experiments.residual_probes.shared import RiskHead


class PreActivationBlock(nn.Module):
    def __init__(self, width, expansion=2, dropout=0.15):
        super().__init__()
        self.branch = nn.Sequential(
            nn.LayerNorm(width), nn.GELU(),
            nn.Linear(width, width * expansion), nn.GELU(), nn.Dropout(dropout),
            nn.Linear(width * expansion, width), nn.Dropout(dropout),
        )

    def forward(self, x):
        return x + self.branch(x)


def build_model(input_width, cfg):
    blocks = [PreActivationBlock(cfg.width, cfg.expansion, cfg.dropout) for _ in range(cfg.blocks)]
    return RiskHead(input_width, cfg, blocks, final_norm=True)

"""ResNet-inspired vector head: h_next = GELU(h + F(h))."""
from torch import nn
from experiments.residual_probes.shared import RiskHead


class ResidualBlock(nn.Module):
    def __init__(self, width, expansion=2, dropout=0.15):
        super().__init__()
        self.branch = nn.Sequential(
            nn.Linear(width, width * expansion), nn.LayerNorm(width * expansion),
            nn.GELU(), nn.Dropout(dropout),
            nn.Linear(width * expansion, width), nn.Dropout(dropout),
        )
        self.activation = nn.GELU()

    def forward(self, x):
        return self.activation(x + self.branch(x))


def build_model(input_width, cfg):
    blocks = [ResidualBlock(cfg.width, cfg.expansion, cfg.dropout) for _ in range(cfg.blocks)]
    return RiskHead(input_width, cfg, blocks)

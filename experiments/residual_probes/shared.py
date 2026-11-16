"""Shared head, configuration, and fold-local preprocessing (no data access on import)."""
from __future__ import annotations

from dataclasses import asdict, dataclass
from importlib import import_module
import math

import numpy as np
import torch
from torch import nn

ARCHITECTURES = ("residual_mlp", "preactivation_mlp", "stochastic_depth_mlp")
FEATURE_SPEC = ("L23:max", "L16:pre")


@dataclass(frozen=True)
class Config:
    architecture: str = "preactivation_mlp"
    width: int = 128
    blocks: int = 4
    expansion: int = 2
    dropout: float = 0.15
    drop_path: float = 0.0
    epochs: int = 300
    patience: int = 20
    learning_rate: float = 1e-3
    weight_decay: float = 1e-2
    pos_weight: float = 15.0
    batch_size: int = 256
    outer_folds: int = 5
    inner_folds: int = 3
    normal_ratio: int = 20
    min_normals: int = 30
    target: str = "all"
    device: str = "cpu"

    def __post_init__(self):
        if self.architecture not in ARCHITECTURES:
            raise ValueError("unknown architecture")
        for name in ("width", "blocks", "expansion", "epochs", "patience", "batch_size"):
            value = getattr(self, name)
            if type(value) is not int or value < 1:
                raise ValueError(f"{name} must be a positive integer")
        if self.outer_folds < 2 or self.inner_folds < 2:
            raise ValueError("outer_folds and inner_folds must be >= 2")
        if self.normal_ratio < 0 or self.min_normals < 0:
            raise ValueError("normal sampling limits must be nonnegative")
        for name in ("dropout", "drop_path", "learning_rate", "weight_decay", "pos_weight"):
            if not math.isfinite(getattr(self, name)):
                raise ValueError(f"{name} must be finite")
        if not 0 <= self.dropout < 1 or not 0 <= self.drop_path < 1:
            raise ValueError("dropout/drop_path must be in [0, 1)")
        if self.architecture != "stochastic_depth_mlp" and self.drop_path != 0:
            raise ValueError("drop_path is only supported by stochastic_depth_mlp")
        if self.learning_rate <= 0 or self.weight_decay < 0 or self.pos_weight <= 0:
            raise ValueError("invalid optimizer or positive-class weight")
        if self.target not in ("all", "visible"):
            raise ValueError("target must be all or visible")
        if self.device != "cpu" and not self.device.startswith("cuda"):
            raise ValueError("device must be cpu or cuda[:index]")


class RiskHead(nn.Module):
    """Compress once, keep width across residual blocks, return one raw logit."""
    def __init__(self, input_width, cfg, blocks, final_norm=False):
        super().__init__()
        if input_width < 1:
            raise ValueError("input_width must be positive")
        self.stem = nn.Sequential(
            nn.Linear(input_width, cfg.width), nn.LayerNorm(cfg.width),
            nn.GELU(), nn.Dropout(cfg.dropout),
        )
        self.blocks = nn.Sequential(*blocks)
        self.final_norm = nn.LayerNorm(cfg.width) if final_norm else nn.Identity()
        self.head = nn.Linear(cfg.width, 1)

    def forward(self, x):
        return self.head(self.final_norm(self.blocks(self.stem(x)))).squeeze(-1)


def make_model(input_width, cfg):
    module = import_module(f"experiments.residual_probes.{cfg.architecture}.model")
    return module.build_model(input_width, cfg)


def checked_xy(x, y):
    x = np.asarray(x, dtype=np.float32)
    y = np.asarray(y)
    if x.ndim != 2 or min(x.shape) < 1 or not np.isfinite(x).all():
        raise ValueError("features must be finite, nonempty [N,D]")
    if y.shape != (len(x),) or not np.isin(y, [0, 1]).all():
        raise ValueError("one reviewed 0/1 label is required per row")
    return x, y.astype(np.int64)


def fit_scaler(x):
    if x.ndim != 2 or not len(x) or not np.isfinite(x).all():
        raise ValueError("invalid scaler training rows")
    med = np.median(x, axis=0)
    q25, q75 = np.quantile(x, [0.25, 0.75], axis=0)
    scale = q75 - q25
    scale[scale < 1e-6] = 1.0
    return med.astype(np.float32), scale.astype(np.float32)


def transform(x, med, scale):
    x = np.asarray(x, dtype=np.float32)
    if x.ndim != 2 or x.shape[1:] != med.shape or not np.isfinite(x).all():
        raise ValueError("feature width mismatch or non-finite input")
    return np.clip((x - med) / scale, -5.0, 5.0).astype(np.float32)

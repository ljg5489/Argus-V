"""Activation-only next-action probes; M1 fusion is a separate experiment."""

from .data import (
    FeatureSpec,
    ProbeDataset,
    ProbeSnapshot,
    load_probe_dataset,
    load_probe_snapshot,
    read_manifest,
)
from .linear import LinearProbe, TrainedProbe, TrainingConfig, fit_probe, load_probe, save_probe

__all__ = [
    "FeatureSpec",
    "LinearProbe",
    "ProbeDataset",
    "ProbeSnapshot",
    "TrainedProbe",
    "TrainingConfig",
    "fit_probe",
    "load_probe",
    "load_probe_dataset",
    "load_probe_snapshot",
    "read_manifest",
    "save_probe",
]

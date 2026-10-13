"""Activation probes for layer configurations: Single per block, Top-3 (chosen on validation), All.

Each split is loaded once with every captured block and sliced per configuration. Thresholds are
not taken from here (the report fixes them at rollout level). Train scores used by the M2 fusion
are out-of-fold: probes are refit with whole task groups held out, so the fusion never sees a
probe score computed on its own training snapshot. If folds cannot hold both classes the
in-sample scores are used and flagged.
"""

from __future__ import annotations

import json
from dataclasses import asdict, replace
from pathlib import Path
from typing import Callable

import numpy as np

from argus_v.probes import TrainingConfig, fit_probe, load_probe_dataset
from argus_v.probes.data import ProbeDataset, read_manifest

from .metrics import average_precision


def captured_layers(manifest_path: Path) -> tuple[int, ...]:
    manifest = read_manifest(manifest_path)
    first = manifest["samples"][0]
    metadata = json.loads((Path(manifest_path).resolve().parent / first["capture_dir"] / "metadata.json")
                          .read_text(encoding="utf-8"))
    return tuple(sorted(block["layer_index"] for block in metadata["blocks"]))


def subset(dataset: ProbeDataset, layers: tuple[int, ...] | None = None, rows: np.ndarray | None = None) -> ProbeDataset:
    """Same samples (or a row subset) with only the requested blocks' feature columns."""
    spec = dataset.spec
    features, snapshots, changes = dataset.features, dataset.snapshots, {}
    if layers is not None:
        offsets = np.cumsum((0, *spec.hidden_sizes))
        positions = [spec.layers.index(layer) for layer in layers]
        columns = np.concatenate([np.arange(offsets[i], offsets[i + 1]) for i in positions])
        features = features[:, columns]
        sliced = replace(spec, layers=tuple(layers), hidden_sizes=tuple(spec.hidden_sizes[i] for i in positions),
                         module_paths=tuple(spec.module_paths[i] for i in positions))
        # Every snapshot must carry the same sliced spec/features (validated by the probe library).
        snapshots = tuple(replace(s, spec=sliced, features=s.features[columns]) for s in snapshots)
        changes["spec"] = sliced
    if rows is not None:
        features = features[rows]
        snapshots = tuple(snapshots[i] for i in rows)
        changes.update(labels=dataset.labels[rows], records=tuple(dataset.records[i] for i in rows))
    return replace(dataset, features=features, snapshots=snapshots, **changes)


def _group_folds(records, folds: int) -> list[np.ndarray]:
    groups = sorted({record["task_group_id"] for record in records})
    assignment = {group: index % folds for index, group in enumerate(groups)}
    return [np.flatnonzero([assignment[r["task_group_id"]] == fold for r in records]) for fold in range(folds)]


def out_of_fold_scores(train: ProbeDataset, validation: ProbeDataset, config: TrainingConfig,
                       folds: int = 5) -> tuple[np.ndarray, str]:
    groups = len({record["task_group_id"] for record in train.records})
    folds = min(folds, groups)
    scores = np.full(len(train.labels), np.nan)
    if folds >= 2:
        try:
            for held in _group_folds(train.records, folds):
                kept = np.setdiff1d(np.arange(len(train.labels)), held)
                probe = fit_probe(subset(train, rows=kept), validation, config)
                scores[held] = probe.model.risk_scores(train.features[held])
            return scores, f"out_of_fold_{folds}_task_groups"
        except ValueError:
            pass
    probe = fit_probe(train, validation, config)
    return probe.model.risk_scores(train.features), "in_sample_fallback"


def run_layer_probes(manifest_path: str | Path, output_dir: str | Path, *, config: TrainingConfig | None = None,
                     single_layers: tuple[int, ...] | None = None, top_k: int = 3,
                     log: Callable[[str], None] = print) -> dict:
    """Write ``probe-<name>.jsonl`` score files (all splits) and ``probes.json`` with the choices made."""
    config = config or TrainingConfig()
    manifest_path = Path(manifest_path).resolve()
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    layers = captured_layers(manifest_path)
    data = {split: load_probe_dataset(manifest_path, split=split, layers=layers)
            for split in ("train", "validation", "test")
            if any(s["split"] == split for s in read_manifest(manifest_path)["samples"])}
    if "train" not in data or "validation" not in data:
        raise ValueError("probes need train and validation splits")
    report = {"captured_layers": list(layers), "training_config": asdict(config),
              "configs": {}}
    singles = single_layers if single_layers is not None else layers

    def fit_config(name: str, chosen: tuple[int, ...]) -> float | None:
        views = {split: subset(dataset, chosen) for split, dataset in data.items()}
        try:
            probe = fit_probe(views["train"], views["validation"], config)
        except ValueError as error:
            report["configs"][name] = {"layers": list(chosen), "error": str(error)}
            log(f"[probe {name}] skipped: {error}")
            return None
        oof, method = out_of_fold_scores(views["train"], views["validation"], config)
        rows = []
        for split, view in views.items():
            scores = oof if split == "train" else probe.model.risk_scores(view.features)
            rows += [{"snapshot_id": record["snapshot_id"], "monitor": f"probe:{name}", "status": "ok",
                      "risk_score": float(score), "split": split} for record, score in zip(view.records, scores)]
        (output_dir / f"probe-{name}.jsonl").write_text(
            "".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")
        validation_scores = probe.model.risk_scores(views["validation"].features)
        auprc = average_precision(validation_scores, views["validation"].labels == 1)
        report["configs"][name] = {"layers": list(chosen), "validation_auprc": auprc, "train_score_method": method,
                                   "final_train_bce": probe.training_report["final_train_bce"]}
        log(f"[probe {name}] layers={list(chosen)} validation AUPRC={auprc}")
        return auprc

    ranking = []
    for layer in singles:
        auprc = fit_config(f"L{layer:02d}", (layer,))
        if auprc is not None:
            ranking.append((auprc, layer))
    if len(ranking) >= top_k:
        top = tuple(sorted(layer for _, layer in sorted(ranking, key=lambda item: (-item[0], item[1]))[:top_k]))
        report["top_k_selection"] = {"k": top_k, "by": "validation AUPRC of single-layer probes", "layers": list(top)}
        fit_config(f"top{top_k}", top)
    if len(layers) > 1:
        fit_config("all", layers)
    (output_dir / "probes.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return report

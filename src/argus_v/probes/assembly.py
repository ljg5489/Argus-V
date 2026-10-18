"""Join rollout/C-01 artifacts, HookInspection metadata and a read-only SQLite index.

Raw tensors stay where they are. Only reviewed next-action labels enter the probe
manifest. Detector predictions and heuristic policy labels are never ground truth.
"""

from __future__ import annotations

import json
import sqlite3
from collections import Counter, defaultdict
from contextlib import closing
from hashlib import sha256
from pathlib import Path
from typing import Any

from argus_v.activations import ActionSpan, ModelIdentity, SnapshotContext
from argus_v.monitoring.snapshot import ids_sha256

from .data import (
    DATASET_SCHEMA,
    LABEL_DEFINITION,
    FeatureSpec,
    load_probe_snapshot,
    read_manifest,
    require_digest,
)

REVIEW_SCHEMA = "argus-v.probe-reviews.v1"


def _json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _save(path: Path, value: Any) -> None:
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8"
    )


def _inside(path: Path, roots: tuple[Path, ...]) -> bool:
    return any(path.is_relative_to(root) for root in roots)


class SourceAssembler:
    def __init__(self, rollout_roots, tensor_roots, databases, *, layers=(23,), path_maps=()):
        self.rollout_roots = tuple(dict.fromkeys(Path(p).resolve() for p in rollout_roots))
        self.tensor_roots = tuple(dict.fromkeys(Path(p).resolve() for p in tensor_roots))
        self.databases = tuple(dict.fromkeys(Path(p).resolve() for p in databases))
        self.layers = tuple(layers)
        if not self.layers or tuple(sorted(set(self.layers))) != self.layers:
            raise ValueError("layers must be nonempty, unique and increasing")
        self.path_maps = tuple(
            (str(old).replace("\\", "/").rstrip("/"), Path(new).resolve()) for old, new in path_maps
        )
        self.issues = []
        self.hooks = {}
        self.candidates = {}
        self.conflicts = set()
        self.stats = Counter()

    def issue(self, code, path, detail=""):
        self.issues.append({"code": code, "path": str(path), "detail": str(detail)})

    def read(self, path):
        try:
            value = _json(path)
            if not isinstance(value, dict):
                raise ValueError("expected a JSON object")
            return value
        except (OSError, ValueError) as error:
            self.issue("unreadable_json", path, error)
            return None

    def mapped_path(self, raw):
        normalized = str(raw).replace("\\", "/")
        for old, new in sorted(self.path_maps, key=lambda item: -len(item[0])):
            if normalized == old or normalized.startswith(old + "/"):
                return new.joinpath(*normalized[len(old) :].strip("/").split("/")).resolve()
        return Path(raw).resolve()

    def index_hooks(self):
        if not self.databases:
            self.issue("no_databases_found", "Research/*.sqlite3")
        for root in self.tensor_roots:
            if not root.is_dir():
                self.issue("missing_tensor_root", root)
                continue
            for path in sorted(root.rglob("manifest.json")):
                if not _inside(path.resolve(), self.tensor_roots):
                    self.issue("outside_source_root", path)
                    continue
                manifest = self.read(path)
                if not manifest or manifest.get("schema_version") != "argus-v.hook-inspection.v1":
                    continue
                self.hooks[path.parent.resolve()] = {
                    "manifest": manifest,
                    "path": path,
                    "database_refs": [],
                }
                self.stats["hook_sessions"] += 1
        for database in self.databases:
            if not database.is_file():
                self.issue("missing_database", database)
                continue
            try:
                # mode=ro never creates an empty DB or initializes dashboard tables.
                with closing(
                    sqlite3.connect(database.as_uri() + "?mode=ro", uri=True)
                ) as connection:
                    connection.execute("PRAGMA query_only=ON")
                    connection.row_factory = sqlite3.Row
                    for row in connection.execute(
                        "SELECT id, artifact_dir, context_json FROM sessions"
                    ):
                        self.stats["database_sessions"] += 1
                        raw = row["artifact_dir"]
                        paths = (
                            [self.mapped_path(raw)]
                            if Path(raw).is_absolute()
                            or any(
                                str(raw).replace("\\", "/").startswith(old + "/")
                                for old, _ in self.path_maps
                            )
                            else [(root / raw).resolve() for root in self.tensor_roots]
                        )
                        matched = [path for path in paths if path in self.hooks]
                        if len(matched) != 1:
                            self.issue(
                                "database_session_unmatched",
                                database,
                                f"session {row['id']}: {raw}",
                            )
                            continue
                        hook = self.hooks[matched[0]]
                        context = json.loads(row["context_json"] or "{}")
                        stored = hook["manifest"].get("context") or {}
                        if any(
                            context.get(key) is not None and stored.get(key) != context[key]
                            for key in ("run_id", "trajectory_id", "step", "input_ids")
                        ):
                            self.issue("database_context_mismatch", database, row["id"])
                            continue
                        hook["database_refs"].append(
                            {"database": str(database), "session_id": row["id"]}
                        )
                        self.stats["database_sessions_linked"] += 1
            except (OSError, ValueError, sqlite3.Error) as error:
                self.issue("database_read_error", database, error)

    def add_capture(self, directory, *, origin, rollout=None, step=None, rollout_file=None):
        directory = directory.resolve()
        roots = self.rollout_roots if origin == "rollout" else self.tensor_roots
        if not _inside(directory, roots):
            self.issue("outside_source_root", directory)
            return
        if not _inside((directory / "metadata.json").resolve(), roots):
            self.issue("outside_source_root", directory / "metadata.json")
            return
        metadata = self.read(directory / "metadata.json")
        if metadata is None:
            return
        try:
            if (
                metadata.get("schema_version") != "argus-v.activation.v1"
                or metadata.get("capture_mode") != "full_prefix_replay"
                or metadata.get("hook_point") != "post_block_pre_final_norm"
            ):
                raise ValueError("expected full-prefix C-01 post-block capture")
            raw = metadata["context"]
            context = SnapshotContext(**{**raw, "action": ActionSpan(**raw["action"])})
            if context.phase != "pre_action":
                raise ValueError("pre_execution is not early-prediction input")
            length = metadata["observed_prefix_length"]
            context.validate_prefix(length)
            position = length - 1
            rows = [row for row in metadata["alignment"] if row["token_index"] == position]
            if len(rows) != 1 or rows[0]["predicts_token_index"] != length:
                raise ValueError("last prefix token must have exactly one aligned capture row")
            digest = require_digest(metadata["prefix_ids_sha256"], "prefix_ids_sha256")
            archive = metadata["artifact"]
            if archive["filename"] != "features.npz":
                raise ValueError("unexpected feature archive filename")
            if not _inside((directory / "features.npz").resolve(), roots):
                raise ValueError("feature archive resolves outside source roots")
            require_digest(archive["sha256"], "archive sha256")
            blocks = {block["layer_index"]: block for block in metadata["blocks"]}
            unavailable = [layer for layer in self.layers if layer not in blocks]
            if unavailable:
                # e.g. agent_loop captures keep only blocks 0/11/23: report it instead of a bare KeyError
                self.issue("layers_unavailable", directory,
                           f"requested {list(self.layers)}, captured {sorted(blocks)}")
                return
            spec = FeatureSpec(
                ModelIdentity(**metadata["identity"]),
                metadata["config_sha256"],
                metadata["model_type"],
                self.layers,
                tuple(blocks[i]["shape"][1] for i in self.layers),
                tuple(blocks[i]["module_path"] for i in self.layers),
            )
            if step is not None and (
                step["run_id"] != context.run_id
                or step["action_id"] != context.action.action_id
                or step["step_index"] != context.action.step_index
                or rollout["trajectory_id"] != context.trajectory_id
            ):
                raise ValueError("rollout step and capture coordinates differ")
            if step is not None and position not in {
                p["token_index"] for p in step["observations"]
            }:
                raise ValueError("pre-action row is absent from rollout observations")
            sidecar = directory.parent / "c01-input.json"
            verified_ids = None
            if origin == "rollout":
                source = _json(sidecar)
                ids = source["input_ids"]
                if (
                    not isinstance(ids, list)
                    or any(type(token) is not int or token < 0 for token in ids)
                    or len(ids) != length
                    or ids_sha256(ids) != digest
                    or ids[-1] != rows[0]["token_id"]
                    or source["identity"] != metadata["identity"]
                ):
                    raise ValueError("original token IDs or identity differ from C-01 capture")
                verified_ids = True
            key = sha256(
                json.dumps([metadata["identity"], raw, position, digest], sort_keys=True).encode(
                    "utf-8"
                )
            ).hexdigest()
            snapshot_id = "joined-" + key
            provenance = {
                "kind": origin,
                "capture_dir": str(directory),
                "rollout_file": str(rollout_file) if rollout_file else None,
            }
            existing = self.candidates.get(snapshot_id)
            if existing is not None:
                if existing["feature_archive_sha256"] != archive["sha256"]:
                    self.conflicts.add(snapshot_id)
                    self.issue("conflicting_capture_copies", directory, snapshot_id)
                existing["sources"].append(provenance)
                self.stats["duplicate_capture_references"] += 1
                return
            kinds = {p["token_index"]: p["kind"] for p in (step or {}).get("observations", [])}
            kinds[position] = "pre_action"
            present = (directory / "features.npz").is_file()
            if not present:
                self.issue("missing_feature_archive", directory / "features.npz")
            self.candidates[snapshot_id] = {
                "snapshot_id": snapshot_id,
                "run_id": context.run_id,
                "trajectory_id": context.trajectory_id,
                "action_id": context.action.action_id,
                "step_index": context.action.step_index,
                "token_index": position,
                "prefix_length": length,
                "action_token_start": context.action.token_start,
                "prefix_ids_sha256": digest,
                "source_identity": metadata["identity"],
                "feature_spec": spec.to_dict(),
                "feature_archive_sha256": archive["sha256"],
                "feature_present": present,
                "original_ids_verified": verified_ids,
                "capture_dir": str(directory),
                # every captured row (pre_reasoning, reasoning+N, pre_action ...); pre_action is token_index
                "observation_points": [
                    {"token_index": row["token_index"], "kind": kinds.get(row["token_index"], "captured")}
                    for row in metadata["alignment"]
                ],
                "sources": [provenance],
                "hook_sessions": [],
                "source_family_id": rollout.get("family") if rollout else None,
                "source_task_group_id": rollout.get("task_id") if rollout else None,
                "source_scenario_id": rollout.get("scenario_id")
                if rollout
                else context.scenario_id,
                "source_policy_label": step.get("policy_label") if step else None,
                "source_label_revision": rollout.get("label_source") if rollout else None,
                "accepted_attempt": step.get("attempts") if step else None,
            }
        except (OSError, ValueError, KeyError, TypeError, IndexError) as error:
            self.issue("invalid_capture", directory, error)

    def discover(self):
        self.index_hooks()
        seen = set()
        for root in self.rollout_roots:
            if not root.is_dir():
                self.issue("missing_rollout_root", root)
                continue
            for path in sorted(root.glob("*/rollout.json")):
                if path.resolve() in seen:
                    continue
                seen.add(path.resolve())
                rollout = self.read(path)
                if not rollout:
                    continue
                if not str(rollout.get("schema_version", "")).startswith(
                    "argus-v.scenario-rollout."
                ):
                    self.issue("unsupported_rollout_schema", path)
                    continue
                self.stats["rollouts"] += 1
                if not rollout.get("finished_at") or "report" not in rollout:
                    self.issue("unfinished_rollout", path)
                    continue
                for step in rollout.get("steps", []):
                    if not step.get("capture_dir") or not step.get("observations"):
                        self.issue("step_without_capture", path, step.get("step_index"))
                        continue
                    directory = (
                        self.mapped_path(step["capture_dir"])
                        if Path(step["capture_dir"]).is_absolute()
                        else (path.parent / step["capture_dir"])
                    )
                    self.add_capture(
                        directory, origin="rollout", rollout=rollout, step=step, rollout_file=path
                    )
        for root in self.tensor_roots:
            if root.is_dir():
                for path in sorted(root.rglob("post_residual_block/metadata.json")):
                    self.add_capture(path.parent, origin="agent_loop")
        self.link_hooks()

    def link_hooks(self):
        # Context coordinates narrow the search; exact original-prefix hashes are
        # the join criterion. Similar task text or matching shapes are insufficient.
        by_trajectory = defaultdict(list)
        for hook in self.hooks.values():
            manifest = hook["manifest"]
            context = manifest.get("context") or {}
            if manifest.get("status") == "complete":
                by_trajectory[context.get("trajectory_id")].append(hook)
        for candidate in self.candidates.values():
            for hook in by_trajectory[candidate["trajectory_id"]]:
                manifest, context = hook["manifest"], hook["manifest"].get("context") or {}
                if (
                    manifest.get("identity") != candidate["source_identity"]
                    or context.get("step") != candidate["step_index"]
                ):
                    continue
                if (
                    all(source["kind"] == "agent_loop" for source in candidate["sources"])
                    and context.get("run_id") != candidate["run_id"]
                ):
                    continue
                attempt = context.get("attempt")
                if (
                    attempt is not None
                    and candidate["accepted_attempt"] is not None
                    and attempt != candidate["accepted_attempt"]
                ):
                    continue
                ids = list(context.get("input_ids") or [])
                # Replay manifests already contain the exact replay input. Only
                # generation sessions may extend it with generated token IDs.
                if manifest.get("phase") == "generation":
                    ids += list(context.get("generated_token_ids") or [])
                if any(type(token) is not int or token < 0 for token in ids):
                    self.issue("invalid_hook_token_ids", hook["path"])
                    continue
                length = candidate["prefix_length"]
                if len(ids) < length or ids_sha256(ids[:length]) != candidate["prefix_ids_sha256"]:
                    continue
                candidate["original_ids_verified"] = True
                candidate["hook_sessions"].append(
                    {
                        "manifest": str(hook["path"]),
                        "phase": manifest.get("phase"),
                        "database_refs": hook["database_refs"],
                        "join": "exact_original_prefix_sha256",
                    }
                )
                self.stats["capture_hook_links"] += 1
        linked = {
            session["manifest"]
            for candidate in self.candidates.values()
            for session in candidate["hook_sessions"]
        }
        for hook in self.hooks.values():
            if str(hook["path"]) not in linked:
                self.issue("hook_without_aligned_capture", hook["path"])


def load_split_assignments(path):
    if path is None:
        return {}, None
    document = _json(Path(path))
    splits = document["splits"]
    if set(splits) != {"train", "validation", "test"}:
        raise ValueError("split file must contain train/validation/test lists")
    assignments = {}
    for split, identifiers in splits.items():
        for identifier in identifiers:
            if identifier in assignments:
                raise ValueError(f"duplicate split assignment: {identifier}")
            assignments[identifier] = split
    return assignments, document.get("source")


def assemble_dataset(
    *,
    rollout_roots,
    tensor_roots,
    databases,
    output,
    layers=(23,),
    reviews=None,
    split_file=None,
    path_maps=(),
    observation_points="pre_action",
):
    """``observation_points="all"`` also exports every earlier captured row of a reviewed action
    (pre_reasoning, reasoning+N ...) as its own sample sharing that action's label. They are more inputs
    for earlier detection, not more independent actions: splits stay grouped by task/trajectory."""
    if observation_points not in ("pre_action", "all"):
        raise ValueError("observation_points must be pre_action or all")
    output = Path(output).resolve()
    if output.exists():
        raise FileExistsError(output)
    assembler = SourceAssembler(
        rollout_roots, tensor_roots, databases, layers=layers, path_maps=path_maps
    )
    assignments, split_source = load_split_assignments(split_file)
    annotations = (
        {
            "schema_version": REVIEW_SCHEMA,
            "labels_revision": "",
            "split_revision": "",
            "samples": [],
        }
        if reviews is None
        else _json(Path(reviews))
    )
    if annotations.get("schema_version") != REVIEW_SCHEMA:
        raise ValueError("expected argus-v.probe-reviews.v1")
    review_rows = {}
    for row in annotations["samples"]:
        if row["snapshot_id"] in review_rows:
            raise ValueError("duplicate reviewed snapshot")
        review_rows[row["snapshot_id"]] = row
    assembler.discover()
    candidates = list(assembler.candidates.values())
    for unknown in set(review_rows) - set(assembler.candidates):
        assembler.issue("review_without_source", reviews, unknown)
    samples, template, specs, point_kinds = [], [], set(), Counter()
    for candidate in candidates:
        identifier = candidate["snapshot_id"]
        split = assignments.get(candidate["source_task_group_id"])
        suggested = {
            "snapshot_id": identifier,
            "reviewed": False,
            "reviewer": "",
            "next_action_violation": None,
            "trajectory_has_violation": None,
            "family_id": candidate["source_family_id"],
            "task_group_id": candidate["source_task_group_id"],
            "split": split,
            "note": "",
            "suggested_rule_label": candidate["source_policy_label"],
        }
        row = review_rows.get(identifier, suggested)
        template.append(row)
        candidate["reviewed"] = row.get("reviewed") is True
        if not candidate["reviewed"]:
            assembler.issue("review_required", candidate["capture_dir"], identifier)
            continue
        try:
            if not row.get("reviewer") or not str(row["reviewer"]).strip():
                raise ValueError("reviewer is required")
            if not annotations.get("labels_revision") or not annotations.get("split_revision"):
                raise ValueError("review file requires labels_revision and split_revision")
            label, trajectory_label = (
                row.get("next_action_violation"),
                row.get("trajectory_has_violation"),
            )
            if type(label) is not int or label not in (0, 1) or type(trajectory_label) is not bool:
                raise ValueError("reviewed labels must be binary plus a boolean trajectory label")
            if split is not None and row.get("split") != split:
                raise ValueError("review split differs from supplied scenario split table")
            if (
                candidate["source_task_group_id"]
                and row.get("task_group_id") != candidate["source_task_group_id"]
            ):
                raise ValueError("review cannot change the original task grouping")
            if (
                candidate["source_family_id"]
                and row.get("family_id") != candidate["source_family_id"]
            ):
                raise ValueError("review cannot hide source-family overlap")
            if identifier in assembler.conflicts or not candidate["feature_present"]:
                raise ValueError("feature archive missing or capture copies conflict")
            if row.get("split") not in ("train", "validation", "test"):
                raise ValueError("review requires an explicit split")
            if row["split"] != "test":
                snapshot = load_probe_snapshot(
                    candidate["capture_dir"],
                    layers=tuple(layers),
                    snapshot_id=identifier,
                    token_index=candidate["token_index"],
                )
                specs.add(json.dumps(snapshot.spec.to_dict(), sort_keys=True))
            specs.add(json.dumps(candidate["feature_spec"], sort_keys=True))
            # Test vectors remain unopened during train/validation preparation.
            sample = {
                "snapshot_id": identifier,
                "run_id": candidate["run_id"],
                "trajectory_id": candidate["trajectory_id"],
                "action_id": candidate["action_id"],
                "family_id": row["family_id"],
                "task_group_id": row["task_group_id"],
                "split": row["split"],
                "capture_dir": candidate["capture_dir"],
                "token_index": candidate["token_index"],
                "next_action_violation": label,
                "trajectory_has_violation": trajectory_label,
            }
            samples.append(sample)
            point_kinds["pre_action"] += 1
            if observation_points == "all":
                # same capture archive (already checked above), earlier rows of the same prefix
                for point in candidate.get("observation_points", []):
                    if point["token_index"] < candidate["token_index"]:
                        samples.append({**sample, "snapshot_id": f"{identifier}@t{point['token_index']}",
                                        "token_index": point["token_index"]})
                        point_kinds[point["kind"].split("+")[0]] += 1
        except (OSError, ValueError, KeyError, TypeError) as error:
            assembler.issue("reviewed_sample_rejected", candidate["capture_dir"], error)
    output.mkdir(parents=True)
    manifest = {
        "schema_version": DATASET_SCHEMA,
        "label_definition": LABEL_DEFINITION,
        "prediction_horizon_actions": 1,
        "labels_revision": annotations.get("labels_revision"),
        "split_revision": annotations.get("split_revision"),
        "samples": samples,
    }
    candidate_manifest = output / "manifest.candidate.json"
    _save(candidate_manifest, manifest)
    valid = False
    if samples:
        try:
            read_manifest(candidate_manifest)
            if len(specs) > 1:
                raise ValueError("mixed source models or feature layouts in train/validation")
            valid = True
            _save(output / "manifest.json", manifest)
        except (OSError, ValueError, KeyError, TypeError) as error:
            assembler.issue("manifest_rejected", candidate_manifest, error)
    counts = {
        split: dict(Counter(s["next_action_violation"] for s in samples if s["split"] == split))
        for split in ("train", "validation", "test")
    }
    ready = (
        valid
        and all(set(counts[split]) == {0, 1} for split in ("train", "validation"))
        and any(
            s["split"] == "validation" and s["trajectory_has_violation"] is False for s in samples
        )
    )
    report = {
        "schema_version": "argus-v.source-assembly.v1",
        "ready_for_training": ready,
        "manifest_written": valid,
        "candidates": len(candidates),
        "reviewed_samples": len(samples),
        "reviewed_actions": point_kinds["pre_action"],
        "observation_points": observation_points,
        "samples_by_observation_kind": dict(point_kinds),
        "counts_by_split_and_label": counts,
        "source_counts": dict(assembler.stats),
        "issues_by_code": dict(Counter(issue["code"] for issue in assembler.issues)),
        "issues": assembler.issues,
        "split_source": split_source,
        "rollout_roots": [str(p) for p in assembler.rollout_roots],
        "tensor_roots": [str(p) for p in assembler.tensor_roots],
        "databases": [str(p) for p in assembler.databases],
        "test_features_opened": False,
    }
    _save(output / "sources.json", candidates)
    _save(output / "reviews.template.json", {**annotations, "samples": template})
    _save(output / "report.json", report)
    lines = [
        "# Probe 데이터 연결",
        "",
        f"학습 준비: {ready}",
        f"관측 후보: {len(candidates)}, 검수된 연결 표본: {len(samples)}",
        "",
        "원본 파일과 SQLite는 변경하지 않았습니다. "
        "규칙 라벨과 탐지기 점수를 정답으로 복사하지 않습니다.",
        "검수용 reviews.template.json을 복사해 라벨·그룹·분할을 확인한 뒤 "
        "새 출력 폴더로 다시 실행하세요.",
        "",
        "| 확인 항목 | 건수 |",
        "| --- | ---: |",
    ]
    lines += [f"| {code} | {count} |" for code, count in report["issues_by_code"].items()]
    (output / "report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return report

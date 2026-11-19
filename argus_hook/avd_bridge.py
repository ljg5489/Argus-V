"""Rollout adapter for the AVD design drafts: the agent side of Scenario/scenario_suite/avd.

AVDEpisode reuses SuiteEpisode (prompt v2 rendering, bash in the Docker sandbox with the same file/network
labels, tool-call parsing and repair, /workspace file sync, label events) and only swaps the controller
for AVDSession. Conditions are B/G/D/X. Every action is executed (user decision 2026-11-18): a violating
decision call runs its mock effect and is recorded as executed. The AVD JSON files are read-only inputs.

    from avd_bridge import AVDScenario, is_avd_id
"""
from __future__ import annotations

import re
from dataclasses import asdict
from pathlib import Path

from harness_config import harness_preset
from scenario_policy import ScenarioRules
from scenario_suite_bridge import SUITE_ROOT, SuiteEpisode, load_engine

AVD_ID = r"AVD-20261112-\d{2}"
CONDITIONS = ("B", "G", "D", "X")


def load_avd():
    load_engine()  # puts Scenario/ on sys.path
    from scenario_suite import avd

    return avd


def is_avd_id(name: str) -> bool:
    return bool(re.fullmatch(AVD_ID, str(name)))


SEALED_FAMILIES = {"F07", "F11", "F14"}  # test families (scenario-splits): never in a run group


def avd_ids(group: str = "avd") -> list[str]:
    """avd-pilot: the 5 pilots; avd: every AVD draft outside the sealed test families."""
    avd = load_avd()
    if group == "avd-pilot":
        return list(avd.PILOT_IDS)
    return [i for i in avd.all_ids() if avd.load_spec(i).get("family_ref") not in SEALED_FAMILIES]


class AVDScenario:
    def __init__(self, identifier: str, seed: int = 0):
        if not is_avd_id(identifier):
            raise ValueError(f"not an AVD id: {identifier}")
        self.spec = load_avd().load_spec(identifier)
        self.scenario_id, self.seed = identifier, seed
        self.family = self.spec.get("family_ref") or identifier
        self.conditions = {name: {} for name in CONDITIONS}

    def episode(self, condition: str, sandbox, command_timeout: int) -> "AVDEpisode":
        if condition not in self.conditions:
            raise ValueError(f"AVD conditions are {CONDITIONS}")
        return AVDEpisode(self, condition, sandbox, command_timeout)


class AVDEpisode(SuiteEpisode):
    label_source = "avd_controller_rule_unreviewed"

    def __init__(self, scenario: AVDScenario, condition: str, sandbox, command_timeout: int,
                 max_steps: int | None = None):
        engine, _ = load_engine()
        self.engine, self.sandbox, self.timeout = engine, sandbox, command_timeout
        self.harness, self.max_steps, self.last_parse_repairs = harness_preset("v2"), max_steps, []
        self.v2 = True  # v2 semantics in SuiteEpisode.execute: submit ends on ACCEPTED
        self.spec = scenario.spec
        self.session = load_avd().open_session(scenario.scenario_id, condition, seed=scenario.seed,
                                               max_steps=max_steps or 20, spec=scenario.spec)
        profile = self.session.profile
        self.scenario_id = self.task_id = self.folder_label = scenario.scenario_id
        self.condition = condition
        self.family = profile["cluster"]
        self.scenario_key = f"{scenario.scenario_id}/{condition}"
        self.public_context = self.session.public_context()
        self.tool_kinds = {name: operation["kind"] for name, operation in profile["tools"].items()}
        self.task_text = self.public_context["goal"]
        self.trusted_policy = "\n".join(self.public_context["policy"])
        self.user_message = self._render_user_message(self.public_context)
        # bash may write only /workspace/output; the input registers are read-only facts
        self.rules = ScenarioRules(writable=("output/*",),
                                   forbidden=tuple(sorted({*engine.PROTECTED_PREFIXES})),
                                   forbid_network=True)

    def configure(self, harness, max_steps=None):
        super().configure(harness, max_steps)
        if max_steps:
            self.session.max_steps = max_steps
            self.public_context["limits"]["max_actions"] = max_steps

    def brief(self) -> dict:
        source = SUITE_ROOT / "design" / "nomal-scenario" / f"{self.scenario_id}.json"
        return {"source_json": str(source.relative_to(SUITE_ROOT.parent)), "title": self.spec.get("title_operator"),
                "category": self.family, "condition_meaning": f"AVD {self.condition} (withheld from model)",
                "blocker": None, "task_given_to_model": self.task_text,
                "policy_given_to_model": self.public_context["policy"], "task_data": None,
                "workspace_files": [path.removeprefix("/workspace/") for path in self.public_context["files"]],
                "tools": ["bash", *(tool["name"] for tool in self.public_context["tools"]), "stop"]}

    def start(self) -> dict:
        import tempfile

        with tempfile.TemporaryDirectory(prefix="argus-avd-") as staging:
            self._stage(Path(staging), self.session.files)
            self.sandbox.reset_workspace()
            self.sandbox.import_folder(Path(staging))
        if self.harness.ensure_output_dir:
            self.sandbox.controller("mkdir -p /workspace/output")
        self.pushed = dict(self.session.files)
        self.before = self.sandbox.hashes()
        meta = self.session.meta
        return {"obstacle": self.condition != "B", "task": self.task_text, "trusted_policy": self.trusted_policy,
                "public_context": self.public_context, "rules": asdict(self.rules), "forbidden_files": [],
                "initial_workspace": self.before,
                "suite": {"id": self.scenario_id, "cluster": self.family, "suite_run_id": self.session.run_id,
                          "avd": {"condition": self.condition, "dp_id": meta["dp_id"]}}}

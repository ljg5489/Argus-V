# Sandbox agent action format

The agent's action generator now uses `tokenizer.apply_chat_template` with actual
system/user/assistant turns. The system supplies the bash/stop contract, the user
supplies the trusted task/policy, and subsequent user turns carry real sandbox
observations. The generator no longer continues a plain-text `Action:` transcript.

`argus_v.agent_actions` preserves the raw generated IDs and text for inspection,
but executes only one complete final-channel bash block. Analysis-only replies,
unsupported tool calls, truncated finals, multiple blocks, and explanatory text
outside the final block are rejected and receive explicit retry feedback.
An accepted `stop` final response ends the loop without executing a command.

The observation IDs handed to existing hooks are the exact chat-template input
IDs. Generated reasoning is still recorded; it is not discarded from research
logs. Capture at the initial prompt remains distinct from a capture after the
current action's reasoning. This change does not add M1 to `agent_loop`.

The published runner includes the workstation's HookInspection capture. Its interactive entry is:

```bash
cd ~/Desktop/Argus-V
PYTHONPATH="$PWD/src" .venv/bin/python argus_hook/agent_loop.py
```

It also accepts `--task`, `--max-steps`, `--max-new-tokens`, `--hook-phase`, and
`--hook-values` for noninteractive debugging. `generate_action` returns the raw
generated text, action command, original prompt IDs, generated IDs, and token pieces.

The repaired generation uses a 1024-token default budget. An incomplete final is
reported as a formatting error, never converted into a command from analysis.
The chat template and system prompt differ from earlier plain-text runs; keep
their experiment provenance distinct. Evaluate M1/M2 on the same new source prefix.

Protocol tests:

```bash
python -m pytest tests/test_agent_actions.py tests/test_m1_sandbox_boundary.py -q
```

These tests verify parsing, causal exclusions, and exact rendered input IDs under
retry. They do not establish successful generation on the workstation's 20B model;
that requires rerunning the actual scenario and checking its output file.

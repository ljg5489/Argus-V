# Host M1 and sandbox action smoke run

`scripts/run_m1_sandbox.py` runs one benign integration check on the Linux GPU
workstation. The agent and the text-only M1 judge share its existing local model
sequentially. Only the proposed bash action runs inside the existing sandbox.

The script first checks that the sandbox is running and that the host has CUDA
and sufficient unused VRAM. It never resets the sandbox or stops another process.
It asks the agent to create a uniquely named text file, captures blocks 0, 11 and
23 at the end of the actual generated reasoning, and passes the same prefix's
text to M1. Final-action tokens are excluded from both observations.

On the workstation, use the `Argus M1 host + sandbox smoke` VS Code debug profile
added to `.vscode/launch.json`, or run from the repository root. A fresh checkout
can use [examples/vscode-launch.json](../examples/vscode-launch.json) as its launch
configuration; merge the profiles into an existing launch file if there is one.
The interpreter path in that example is for the Linux host, not the Windows guest.

Run from the repository root:

```bash
.venv/bin/python scripts/run_m1_sandbox.py --execute
```

Without `--execute`, the script records the proposed action and M1 result only.
With it, a successful M1 judgment below the illustrative 0.7 threshold allows
the single-file command to execute through `SANDBOX/sandbox.py run`. An additional
exact-command check bounds this smoke task; it is not a learned security monitor.
The script reads the created file back through the sandbox API to verify it.

Each run creates its own `artifacts/m1-sandbox-<UTC timestamp>-<random suffix>/`:

- `sandbox-before.json`: container status before model loading.
- `agent-generation.json`: source tokens, reasoning boundary and final action.
- `capture/`: C-01 activation features and alignment metadata.
- `m1-observed-input.json`: the three text fields actually passed to M1.
- `m1-result.json`: judgment, configuration and alignment metadata.
- `sandbox-action.json`, `sandbox-verification.json`: execution and readback results.
- `run-summary.json`: completion status, score, execution and verification flags.
- `exception.txt`: diagnostic traceback if a stage fails.

This is a one-step smoke check, not the interactive `agent_loop` or a scenario
benchmark. It generates the response first, then replays its causal prefix and
judges before executing the action. It does not demonstrate streaming early
intervention, detection accuracy, a calibrated probability or the final fused M2
model. The local checkpoint revision is recorded as `local`, not a verified
upstream weight revision. M1 receives no activation, future action or answer label.

Live Share edits the host's files. If guest-initiated debugging is unavailable,
the host can start this profile once and share the debug session and result files.
Do not launch the Linux model with the Windows guest's local Python interpreter.

# Argus-V Scenario Studio

This folder contains the static dashboard published with GitHub Pages.

## Deployment

Push changes under `dist/` to `main`; the workflow at
`.github/workflows/deploy-argus-v-dashboard.yml` publishes the dashboard.
The production URL is:

`https://ljg5489.github.io/Argus-V/`

## Updating the scenario catalog

The catalog is stored as `dist/scenarios.json.gz.b64` so the source repository
keeps a compact text asset. The Pages workflow restores
`dist/scenarios.json` before upload. To regenerate it from a local
`scenarios.json`, run:

```powershell
python -c "import gzip,base64,pathlib; p=pathlib.Path('scenarios.json').read_bytes(); pathlib.Path('sites/argus-v-demo-dashboard/dist/scenarios.json.gz.b64').write_text(base64.b64encode(gzip.compress(p, compresslevel=9)).decode())"
```

The UI can browse the catalog, saved EMP verdicts, and recorded step traces
without a local API. Re-running classifier inference and agent actions require
the companion API at `http://127.0.0.1:8765`; the API allows the GitHub Pages
origin (`https://ljg5489.github.io`).

## Live agent chat

The agent chat tab runs the local gpt-oss-20b as an agent in the local SANDBOX
and shows every step while it happens: the model's reasoning as it is
generated, the bash/stop action, the Argus-V-emp verdict (normal side ·
violation side) and the sandbox result. Start the companion API from the
repository root with the Python environment that has torch and the model
dependencies:

```powershell
py -3.11 argus_hook/dashboard_server.py          # Windows
.venv/bin/python argus_hook/dashboard_server.py  # Linux
```

Open `http://127.0.0.1:8765/` (or the GitHub Pages copy, whose origin the API
allows) and send a task. The first task loads gpt-oss-20b onto the GPU
(about 13 GB); the model stays loaded for the next tasks until **모델 내리기**
or the API stops. While it is loaded, the token-replay mode and the old agent
job are refused, because they load a second copy of the model.

`argus_hook/live_agent.py` keeps the model and runs each task with the
bash/stop protocol of `agent_loop.py` (sandbox network fakenet, 120-second
command limit, sampling as in `scenario_rollout.py`). The system prompt is
agent_loop's plus one line saying that the stop block is the answer the user
reads. Replies are read with the rollouts' parser. Chat questions are often
answered directly ("55") instead of in a stop block; such a reply, or a
malformed stop block, is taken as the answer when it contains no command. A
refused reply that contains a command is generated again (at most four
attempts) and never run, and the refused attempts stay visible in the chat.
Before a command runs, the worker replays the pre-action prefix, takes
layer 23 at the observation points (maximum) and layer 16 just before the
action, pools them like the evaluation features and scores them with the
Argus-V-emp model files. On three saved new-run steps this path reproduced the
saved features bit for bit and the saved scores exactly. The verdict never
blocks the command. The score is rank-type, not a probability, and chat tasks
are unlike the scenarios the model was fitted on. `stop` is a reporting action
that the evaluation metrics leave out, so its score is shown for reference
only and is not counted as an alarm. `argus_hook/live_agent_service.py` keeps
the events for the browser (long polling on `/api/live/events`), so a reloaded
page rebuilds a running task. Each task also leaves a record in
`artifacts/live-agent/<run id>.jsonl` (its events without the streamed text,
the system prompt and the raw text of every attempt) for examining failures.

## EMP scores for every scenario step

`build_emp_steps.py` uses the exported Argus-V-emp model files and the
`resplit-1117` hidden-state features to score every step in the published
scenario catalog. It checks the catalog's tool and label alignment, then writes
`dist/emp-steps.json.gz.b64`. The Pages workflow restores `emp-steps.json` next
to `scenarios.json`. The browser displays the model score relative to the
validation-normal 95th percentile cut-off from the model manifest. These are
saved model outputs, not browser-side inference or violation probabilities.

Regenerate after changing the EMP model or scenario catalog:

```powershell
py -3.11 sites/argus-v-demo-dashboard/build_emp_steps.py
```

## EMP detection cases

The violation demo replays the ten visible-violation results in
`reports/risk-loop/argus-v-emp/full_test.json`. It shows the recorded comparison
against the test normals' 95th percentile, which is retrospective and is not
the validation-set threshold. Percentiles are neither EMP raw scores nor
violation probabilities. It does not run EMP or gpt-oss. The cases are a
selected subset, including misses, and must not be presented as overall model
performance. The report does not contain the complete transcripts or raw
per-call scores; missing details are shown as unavailable.

For local static serving, restore `scenarios.json` as in the Pages workflow and
run `python sites/argus-v-demo-dashboard/build_emp_cases.py`. The workflow
generates `dist/emp-cases.json` on deployment from the checked-in report and
catalog; the generated JSON is not committed.

## Recorded model reasoning and actions

`build_replay_traces.py` reads the same pinned Hugging Face rollout `step.json`
files used by `argus_hook/replay_demo.py`. It exports each recorded step's last
320 reasoning characters, chosen action and arguments, and a short execution
result. The compact asset is `dist/step-traces.json.gz.b64`; the Pages workflow
restores `step-traces.json` before upload. Steps without an EMP feature row are
shown with their action and a `판정 안 함` marker. The reasoning is recorded
model output, not a new inference or a validated explanation of the decision.

Regenerate after changing the scenario catalog or replay source:

```powershell
py -3.11 sites/argus-v-demo-dashboard/build_replay_traces.py
```

# Argus-V Scenario Studio

## Start locally

From the repository root, run the dashboard companion API with Python 3.11:

```powershell
& "$env:LOCALAPPDATA\Programs\Python\Python311\python.exe" argus_hook\dashboard_server.py
```

Open `http://127.0.0.1:8765`. The companion server binds to loopback only. The deployed Sites page is a private static front end; enter the local API address in **현재 연결 → 로컬 API 주소** to enable replay and agent actions from that page. The scenario catalog and saved scores are included in the static page and remain browseable without the companion API.

## Scenario replay

- The catalog is generated from `argus_hook/replay_assets/argus_v_p_scores.json` and `scenario_descriptions.json`. Refresh the bundled snapshot at `sites/argus-v-demo-dashboard/dist/scenarios.json` after those assets change.
- The default mode runs the selected classifier against the rollout's saved layer 16/23 hidden states. Missing rollout data is fetched read-only from Hugging Face into `artifacts/replay-cache`.
- **토큰에서 GPT-OSS 재계산** runs the local GPT-OSS model on the recorded tokens, then scores the resulting hidden states. It does not sample a new action. It requires the local model folder and CUDA.
- Inference-ready choices are determined from local checkpoint files. This workspace currently has Argus-V-p P5 (`argus_v_p_P5.bundle`) and Argus-V-em EM32 (`argus_v_em_round01.pt`, epoch 60). P5 recomputes its train-percentile score and uses the stored tool threshold when one exists. EM32 reports `sigmoid(head)` and its raw logit; this is not a calibrated probability, and the replay does not apply an EM decision threshold.
- P6 has no replay bundle here. EM64/EM128 do not have final all-train checkpoints, and Argus-V-em300's final checkpoint is absent, so they are not offered for inference even though some evaluation artifacts exist.
- All listed scenarios belong to the train split. These scores are replay/inference outputs on training scenarios, not unseen-test performance.

## Chat agent

The chat view starts `argus_hook/agent_loop.py` with a five-step budget. The existing agent loads the local `gpt-oss-20b` model and sends commands to the Docker sandbox. Chat is available only when the model directory, CUDA, and Docker runtime are present. The current model loader expects `~/Desktop/Argus-V/gpt-oss-20b` and requires a CUDA GPU. Sandbox networking is configured by the existing project runner; keep its `fakenet` policy.

The API accepts browser requests only from localhost and the configured Sites origin. To change the hosted origin, set `ARGUS_SITE_ORIGIN` before starting the server. No provider key is stored in the dashboard.

## Files

- Static Site: `sites/argus-v-demo-dashboard/dist/`
- Local API and runner: `argus_hook/dashboard_server.py`
- Model replay inference: `argus_hook/replay_model_inference.py`
- Protected replay implementation: `argus_hook/replay_demo.py` (read only)

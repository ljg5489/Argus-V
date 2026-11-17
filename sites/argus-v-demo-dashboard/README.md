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

The UI can browse the published catalog without a local API. Replay and agent
actions require the companion API at `http://127.0.0.1:8765`; the running API
must allow the GitHub Pages origin.

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

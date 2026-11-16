"""Run a saved Argus-V-p / Argus-V-em checkpoint on one replayed train rollout.

This is a companion to replay_demo.py. That file remains read-only. The default
mode evaluates the classifier on the rollout's saved GPT-OSS hidden states;
``--mode tokens`` runs GPT-OSS on the recorded tokens and scores the new states.
No action is generated and no sandbox command is executed.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "argus_hook"))
import replay_demo as RD  # noqa: E402
import replay_scoring as RS  # noqa: E402

P_CHECKPOINTS = {
    "P5": ROOT / "argus_hook" / "replay_assets" / "argus_v_p_P5.bundle",
    "P6": ROOT / "argus_hook" / "replay_assets" / "argus_v_p_P6.bundle",
}
EM_CHECKPOINTS = {
    "EM32": ROOT / "artifacts" / "risk-loop" / "argus-v-em" / "argus_v_em_round01.pt",
    "EM300": ROOT / "artifacts" / "risk-loop" / "argus-v-em300" / "argus_v_em300.pt",
}


def score_rollout(unit_id: str, model_name: str, mode: str, offline: bool = False) -> dict:
    table = RD.load_table()
    unit = table["units"].get(unit_id)
    if unit is None:
        raise ValueError(f"{unit_id}: replay table에 없는 실행입니다.")
    checkpoint = P_CHECKPOINTS.get(model_name) or EM_CHECKPOINTS.get(model_name)
    if not checkpoint or not checkpoint.is_file():
        raise FileNotFoundError(f"{model_name}: 저장된 추론 체크포인트가 없습니다.")

    token_mode = mode == "tokens"
    hidden_fn = None
    if token_mode:
        reason = RD.gpu_missing_reason()
        if reason:
            raise RuntimeError(f"토큰 재계산을 할 수 없습니다: {reason}")
        hidden_fn = RD.gpu_hidden_fn()
    rec = RD.get_records(unit_id, RD.LOCAL_DIRS, need_tokens=token_mode, need_hidden=not token_mode,
                         offline=offline)
    indexes = rec.step_indexes()
    if token_mode and any(rec.prefix_ids(i) is None for i in indexes):
        if offline:
            raise FileNotFoundError("오프라인 모드인데 로컬 토큰 기록이 없습니다.")
        cached = RD.fetch_from_hub(unit_id, need_tokens=True, need_hidden=False)
        rec = RD.Records(cached, "Hugging Face에서 토큰 기록을 가져옴")
    if not token_mode and any(rec.hidden_rows(i) is None for i in indexes):
        if offline:
            raise FileNotFoundError("오프라인 모드인데 로컬 hidden state가 없습니다.")
        print("저장된 hidden state가 없어 Hugging Face에서 필요한 배열을 가져옵니다.", flush=True)
        cached = RD.fetch_from_hub(unit_id, need_tokens=False, need_hidden=True)
        rec = RD.Records(cached, "Hugging Face에서 hidden state를 가져옴")

    is_p = model_name in P_CHECKPOINTS
    bundle = RS.load_bundle(checkpoint) if is_p else None
    em_score_fn = None
    if not is_p:
        import torch
        from experiments.risk_loop.argus_loop.argus_v_em import LearnedEmbedding, robust_scale

        payload = torch.load(checkpoint, map_location="cpu", weights_only=True)
        em_model = LearnedEmbedding(int(payload["input_width"]), int(payload["width"]))
        em_model.load_state_dict(payload["state_dict"])
        em_model.eval()

        def em_score_fn(feats):
            matrix = np.concatenate([feats["L23:max"], feats["L16:pre"]], axis=1)
            scaled = torch.from_numpy(robust_scale(matrix, payload["median"].numpy(), payload["scale"].numpy()))
            with torch.no_grad():
                return float(em_model(scaled).cpu().numpy()[0])

    unit_scores = RD.step_scores(unit, model_name if is_p else "P5", table) if is_p else {}
    steps_out = []
    for step_index in rec.step_indexes():
        step = rec.step(step_index)
        info = unit_scores.get(step_index)
        observations = step.get("observations") or []
        kinds = [str(item.get("kind", "")) for item in observations]
        if not kinds or step.get("action_start") is None:
            steps_out.append({"index": step_index, "tool": info["tool"] if info else "—",
                              "label": info["label"] if info else None, "status": "no_observations"})
            continue

        if token_mode:
            prefix = rec.prefix_ids(step_index)
            if prefix is None:
                steps_out.append({"index": step_index, "tool": info["tool"] if info else "—",
                                  "label": info["label"] if info else None, "status": "missing_tokens"})
                continue
            if len(prefix) != int(step["action_start"]):
                raise ValueError(f"step {step_index}: 저장 토큰 수와 행동 시작 위치가 다릅니다.")
            positions = [int(item["token_index"]) for item in observations]
            scenario_key = rec.rollout.get("scenario_key") or f"{unit['scenario']}/{unit['condition']}"
            rows = hidden_fn(unit_id, scenario_key, step_index, prefix, positions,
                             int(step["action_start"]))
        else:
            rows = rec.hidden_rows(step_index)
            if rows is None:
                steps_out.append({"index": step_index, "tool": info["tool"] if info else "—",
                                  "label": info["label"] if info else None, "status": "missing_hidden"})
                continue
        if any(rows[layer].shape[0] != len(kinds) for layer in RD.LAYERS):
            steps_out.append({"index": step_index, "tool": info["tool"] if info else "—",
                              "label": info["label"] if info else None, "status": "row_mismatch"})
            continue

        feats = RS.pool_features(rows[23], rows[16], kinds)
        if is_p:
            score = float(RS.score(bundle, feats)[0])
            threshold = info["threshold"] if info else None
            verdict = None if threshold is None else ("경보" if score >= float(threshold) else "경보 없음")
            raw_score = None
        else:
            raw_score = em_score_fn(feats)
            # Display sigmoid(head) for readability. This is a model output, not a calibrated probability.
            score = float(1.0 / (1.0 + np.exp(-np.clip(raw_score, -80.0, 80.0))))
            threshold, verdict = None, None
        steps_out.append({
            "index": step_index,
            "tool": info["tool"] if info else RD.describe_action(step)[0],
            "label": info["label"] if info else None,
            "score": score,
            "raw_score": raw_score,
            "threshold": threshold,
            "decision": verdict,
            "status": "scored",
            "n_observations": len(kinds),
        })
        print(f"채점 완료 · step {step_index} · {steps_out[-1]['tool']}", flush=True)

    name = {"P5": "Argus-V-p P5", "P6": "Argus-V-p P6",
            "EM32": "Argus-V-em EM32 · epoch 60", "EM300": "Argus-V-em300 EM32 · epoch 300"}[model_name]
    return {"model": model_name, "model_name": name,
            "score_label": "P5 train-percentile score" if model_name.startswith("P") else "sigmoid(head), not calibrated",
            "mode": "recorded-token hidden-state recompute" if token_mode else "saved hidden-state inference",
            "record_origin": rec.origin, "unit": unit_id, "steps": steps_out}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--unit", required=True)
    parser.add_argument("--model", choices=(*P_CHECKPOINTS, *EM_CHECKPOINTS), required=True)
    parser.add_argument("--mode", choices=("hidden", "tokens"), default="hidden")
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    result = score_rollout(args.unit, args.model, args.mode, args.offline)
    print("ARGUS_RESULT_JSON=" + json.dumps(result, ensure_ascii=False, separators=(",", ":")), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

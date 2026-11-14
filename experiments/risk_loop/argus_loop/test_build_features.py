"""Tests for build_features with fake arrays (no network).

  py -3.11 -m pytest experiments/risk_loop/argus_loop/test_build_features.py -q
  py -3.11 experiments/risk_loop/argus_loop/test_build_features.py      # without pytest (small built-in runner)
"""
from __future__ import annotations

import hashlib
import io
import sys
from pathlib import Path

import numpy as np

try:
    import pytest
except ImportError:  # minimal stand-in so the file also runs directly (see __main__)
    import contextlib
    import types

    @contextlib.contextmanager
    def _raises(exc):
        try:
            yield
        except exc:
            return
        raise AssertionError(f"did not raise {exc}")

    pytest = types.SimpleNamespace(raises=_raises)

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_features as bf  # noqa: E402


def test_pool_step_all_pools():
    kinds = ["pre_reasoning", "reasoning+32", "reasoning_end", "pre_action"]
    a = np.arange(4 * 5, dtype=np.float32).reshape(4, 5)
    a[1, 2] = 100.0
    out, flags = bf.pool_step(a, kinds)
    assert np.array_equal(out["max"], a.max(0))
    assert np.allclose(out["mean"], a.mean(0))
    assert np.array_equal(out["pre"], a[3])
    assert np.array_equal(out["rend"], a[2])
    assert flags == {"has_rend": 1, "pre_is_pre_action": 1, "pre_is_last": 1}


def test_pool_step_missing_rend_and_pre():
    a = np.random.default_rng(0).normal(size=(2, 7)).astype(np.float32)
    out, flags = bf.pool_step(a, ["pre_reasoning", "reasoning+32"])
    assert np.isnan(out["rend"]).all()
    assert np.array_equal(out["pre"], a[-1])  # falls back to the last observation
    assert flags["has_rend"] == 0 and flags["pre_is_pre_action"] == 0


def test_pool_step_rejects_misaligned_rows():
    with pytest.raises(ValueError):
        bf.pool_step(np.zeros((3, 4), np.float32), ["pre_reasoning", "pre_action"])


def test_tool_of():
    assert bf.tool_of({"kind": "tool", "command": '{"tool": "send_email", "arguments": {}}'}) == "send_email"
    assert bf.tool_of({"kind": "bash", "command": "ls"}) == "bash"
    assert bf.tool_of({"kind": "stop", "command": None}) == "stop"
    assert bf.tool_of({"kind": "tool", "command": "{not json"}) == ""


def test_family_of():
    assert bf.family_of("AVv2-F03-OPS-01", "F03") == "F03"
    assert bf.family_of("AV-S01", "unauthorized_data_destination") == "unauthorized_data_destination"
    with pytest.raises(ValueError):
        bf.family_of("AVv2-F03-OPS-01", "F04")


class FakeHub:
    """Serves one in-memory parquet shard; counts which rows' payloads are converted."""

    def __init__(self, table):
        import pyarrow.parquet as pq

        buf = io.BytesIO()
        pq.write_table(table, buf, row_group_size=3)
        self.data = buf.getvalue()
        import threading

        self.bytes_lock = threading.Lock()
        self.bytes_read = 0

    def open(self, shard):
        return io.BytesIO(self.data)


def test_process_group_decodes_only_wanted_rows():
    import pyarrow as pa

    rng = np.random.default_rng(1)
    arrays = [rng.normal(size=(3, 6)).astype(np.float32) for _ in range(3)]
    payload = [a.tobytes() for a in arrays]
    hub = FakeHub(pa.table({"data": payload}))
    kinds = ["pre_reasoning", "reasoning_end", "pre_action"]
    g = {"shard": "x", "rg": 0, "bytes": 10,
         "items": [{"row": 2, "srow": 7, "layer": 16, "unit_id": "u", "dtype": "float32", "shape": [3, 6],
                    "sha": hashlib.sha256(payload[2]).hexdigest()}]}
    _, res = bf.process_group(hub, g, {7: kinds})
    assert len(res) == 1
    srow, L, pooled, flags = res[0]
    assert (srow, L) == (7, 16)
    assert np.array_equal(pooled["max"], arrays[2].max(0))
    assert np.array_equal(pooled["rend"], arrays[2][1])
    # wrong hash must abort
    g["items"][0]["sha"] = "0" * 64
    with pytest.raises(bf.hf_select.SelectError):
        bf.process_group(hub, g, {7: kinds})


def test_float16_roundtrip_memmap(tmp_path, monkeypatch):
    monkeypatch.setattr(bf, "FEAT", tmp_path)
    monkeypatch.setattr(bf, "LAYERS", (16,))
    monkeypatch.setattr(bf, "HIDDEN", 4)
    mm = bf._memmaps(3, "w+")
    assert np.isnan(mm[(16, "max")]).all()  # unwritten rows are NaN
    mm[(16, "max")][1] = np.array([1, 2, 3, 4], np.float16)
    mm[(16, "max")].flush()
    del mm
    mm = bf._memmaps(3, "w+")  # reopen existing: must keep data (resume)
    assert np.array_equal(mm[(16, "max")][1], [1, 2, 3, 4])
    assert np.isnan(mm[(16, "max")][0]).all()


# ---------------------------------------------------------------------- labels (precedence, relabel)
def _s(unit, k, **kw):
    return {"unit_id": unit, "scenario_id": "S1", "condition": "C0", "seed": 0, "trajectory_id": unit,
            "action_id": f"{unit}:{k}", "step_index": k, **kw}


def _label_files(tmp_path):
    import gzip as _gz
    import json as _json

    oct_doc = {"samples": [_s("o1", 0, gold_violation=1, human_confirmed=True),
                           _s("o1", 1, gold_violation=0, human_confirmed=False)]}
    nov_doc = {"samples": [_s("n1", 0, gold_violation=0)],                       # auto confirmed
               "pending_reviews": [_s("n1", 1, gold_violation=None, original_policy_label=1),  # draft -> convention 0
                                   _s("n1", 2, gold_violation=None, original_policy_label=1),  # draft -> human 0
                                   _s("n1", 3, gold_violation=None, original_policy_label=1),  # stays draft
                                   _s("n1", 4, gold_violation=1),                               # sidecar reviewed
                                   _s("n1", 5, gold_violation=None, original_policy_label=0)]}  # convention+human
    op, np_ = tmp_path / "oct.json", tmp_path / "nov.json.gz"
    op.write_text(_json.dumps(oct_doc), encoding="utf-8")
    with _gz.open(np_, "wt", encoding="utf-8") as fh:
        _json.dump(nov_doc, fh)
    human = {"samples": [_s("n1", 2, gold_violation=0, human_confirmed=True),
                         _s("n1", 5, gold_violation=1, human_confirmed=True),
                         _s("n1", 3, gold_violation=0, human_confirmed=False),       # delegated: ignored
                         _s("n9", 0, gold_violation=0, human_confirmed=True)],       # not in sidecar: added
             "pending_reviews": [_s("n1", 3, gold_violation=None, human_confirmed=False)]}
    ov = tmp_path / "ov.csv"
    ov.write_text("unit_id,step_index,action_id,gold_violation,status\n"
                  "n1,1,n1:1,0,nov_convention\n"
                  "n1,5,n1:5,0,nov_convention\n"
                  "n1,3,n1:3,,nov_convention\n", encoding="utf-8")                 # empty = no decision
    return op, np_, human, ov


def test_load_labels_precedence(tmp_path, monkeypatch):
    monkeypatch.setattr(bf, "load_splits", lambda: {"S1": "train"})
    op, np_, human, ov = _label_files(tmp_path)
    rows, info = bf.load_labels(op, np_, nov_human=human, overrides=bf.read_overrides(ov))
    got = {(r["unit_id"], r["step_index"]): (r["label"], r["label_status"]) for r in rows}
    assert got[("o1", 0)] == (1, "oct_human") and got[("o1", 1)] == (0, "oct_delegated")
    assert got[("n1", 0)] == (0, "nov_auto_confirmed")
    assert got[("n1", 1)] == (0, "nov_convention")       # convention beats draft rule
    assert got[("n1", 2)] == (0, "nov_human")            # human beats draft rule
    assert got[("n1", 3)] == (1, "nov_draft_rule")       # no decision -> draft stays
    assert got[("n1", 4)] == (1, "nov_reviewed")
    assert got[("n1", 5)] == (1, "nov_human")            # human beats convention
    assert got[("n9", 0)] == (0, "nov_human")            # human review of an action absent from the sidecar
    assert info["overrides_applied"] == 2 and info["nov_human_reviews"] == 3
    assert info["nov_human_skipped"] == {"samples:not_human_confirmed": 1, "pending_reviews:not_human_confirmed": 1}


def test_load_labels_v1_unchanged_without_human_or_overrides(tmp_path, monkeypatch):
    monkeypatch.setattr(bf, "load_splits", lambda: {"S1": "train"})
    op, np_, _, _ = _label_files(tmp_path)
    rows, info = bf.load_labels(op, np_)
    got = {(r["unit_id"], r["step_index"]): (r["label"], r["label_status"]) for r in rows}
    assert got[("n1", 1)] == (1, "nov_draft_rule") and got[("n1", 2)] == (1, "nov_draft_rule")
    assert ("n9", 0) not in got and set(info) == {"dropped_null"}


def test_override_action_id_mismatch_and_unmatched(tmp_path, monkeypatch):
    monkeypatch.setattr(bf, "load_splits", lambda: {"S1": "train"})
    op, np_, _, _ = _label_files(tmp_path)
    with pytest.raises(ValueError):
        bf.load_labels(op, np_, overrides={("n1", 1): {"label": 0, "action_id": "WRONG", "status": "nov_convention"}})
    with pytest.raises(ValueError):
        bf.load_labels(op, np_, overrides={("zz", 0): {"label": 0, "action_id": "", "status": "nov_convention"}})


def test_relabel_steps_keeps_rows_and_order():
    steps = [{"row": "0", "unit_id": "o1", "step_index": "0", "action_id": "o1:0", "tool": "write_report",
              "label": "1", "label_status": "oct_human", "source": "oct", "split": "train", "report_content": "1"},
             {"row": "1", "unit_id": "n1", "step_index": "1", "action_id": "n1:1", "tool": "classify_requests",
              "label": "1", "label_status": "nov_draft_rule", "source": "nov", "split": "train", "report_content": "0"},
             {"row": "2", "unit_id": "n1", "step_index": "7", "action_id": "n1:7", "tool": "x",
              "label": "0", "label_status": "nov_draft_rule", "source": "nov", "split": "train", "report_content": "0"}]
    labels = [{"unit_id": "o1", "step_index": 0, "action_id": "o1:0", "label": 1, "label_status": "oct_human",
               "split": "train"},
              {"unit_id": "n1", "step_index": 1, "action_id": "n1:1", "label": 0, "label_status": "nov_convention",
               "split": "train"}]
    out, stat = bf.relabel_steps(steps, labels)
    assert [r["row"] for r in out] == ["0", "1", "2"]
    assert (out[1]["label"], out[1]["label_status"]) == ("0", "nov_convention")
    assert out[0]["report_content"] == "1" and out[2]["label"] == "" and stat["now_null"] == 1
    labels[1]["action_id"] = "other"
    with pytest.raises(ValueError):
        bf.relabel_steps(steps, labels)


def test_stage_labels_never_overwrites_v1(tmp_path, monkeypatch):
    monkeypatch.setattr(bf, "OUT", tmp_path)
    (tmp_path / "labels").mkdir()
    (tmp_path / "labels" / bf.LABELS_V1).write_text("x", encoding="utf-8")
    with pytest.raises(SystemExit):
        bf.stage_labels(type("A", (), {"oct_labels": None, "nov_labels": None})())
    assert (tmp_path / "labels" / bf.LABELS_V1).read_text(encoding="utf-8") == "x"


def test_repo_overrides_file_matches_decisions():
    ov = bf.read_overrides(bf.OVERRIDES)
    assert len(ov) == 10
    assert sum(v["label"] for v in ov.values()) == 7
    assert {v["status"] for v in ov.values()} == {"nov_convention"}


# ---------------------------------------------------------------------- observe_every / 32-token grid
def _scenario_rollout():
    root = Path(__file__).resolve().parents[3]
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))
    from argus_hook import scenario_rollout as sr
    return sr


def test_grid32_thinning_matches_observation_points_32():
    """Synthetic steps: observation_points(..., 8) thinned == observation_points(..., 32) (positions + kinds)."""
    sr = _scenario_rollout()
    rng = np.random.default_rng(0)
    for case in range(1000):
        prompt = int(rng.integers(5, 3000))
        has_reasoning = case % 10 != 0
        if has_reasoning:
            start = prompt + int(rng.integers(0, 4))
            end = start + int(rng.integers(1, 700))
            action_start = end + int(rng.integers(0, 6))
            spans = sr.HarmonySpans(action_start, (start, end), (action_start + 3, action_start + 9))
        else:
            action_start = prompt + int(rng.integers(1, 6))
            spans = sr.HarmonySpans(action_start, None, (action_start + 3, action_start + 9))
        p32 = sr.observation_points(prompt, spans, 32)
        for every in (8, 16, 4, 1, 32):
            pe = sr.observation_points(prompt, spans, every)
            pos, kinds = list(pe), list(pe.values())
            arr = np.arange(len(pos), dtype=np.float32)[:, None] * np.ones((1, 3), np.float32)
            a2, k2, t2 = bf.thin_to_grid32(arr, kinds, every, pos)
            assert t2 == list(p32) and k2 == list(p32.values()), (case, every)
            assert np.array_equal(a2[:, 0], [pos.index(t) for t in t2])


def test_grid32_old_units_unchanged():
    kinds = ["pre_reasoning", "reasoning+32", "reasoning+64", "reasoning_end", "pre_action"]
    a = np.random.default_rng(3).normal(size=(5, 6)).astype(np.float32)
    a2, k2, _ = bf.thin_to_grid32(a, kinds, 32)
    assert a2 is a and k2 == kinds  # identity object: pooling is bit-identical
    out_old, fl_old = bf.pool_step(a, kinds)
    out_new, fl_new = bf.pool_step(a2, k2)
    assert fl_old == fl_new and all(np.array_equal(out_old[p], out_new[p], equal_nan=True) for p in out_old)
    assert bf.unit_observe_every({}) == 32 and bf.unit_observe_every({"observe_every": 8}) == 8


def test_grid32_rejects_bad_inputs():
    with pytest.raises(ValueError):
        bf.grid32_keep(["pre_reasoning", "pre_action"], 12)          # 12 does not divide 32
    with pytest.raises(ValueError):
        bf.grid32_keep(["reasoning+40", "pre_action"], 32)           # off the declared grid
    with pytest.raises(ValueError):
        bf.grid32_keep(["mystery", "pre_action"], 8)


def test_process_group_thins_8_grid_like_32_grid():
    import pyarrow as pa

    k8 = ["pre_reasoning", "reasoning+8", "reasoning+16", "reasoning+24", "reasoning+32", "reasoning+40",
          "reasoning_end", "pre_action"]
    rng = np.random.default_rng(5)
    a8 = rng.normal(size=(8, 6)).astype(np.float32)
    a32 = a8[[0, 4, 6, 7]]
    payload = [a8.tobytes(), a32.tobytes()]
    hub = FakeHub(pa.table({"data": payload}))
    g = {"shard": "x", "rg": 0, "bytes": 1, "items": [
        {"row": 0, "srow": 0, "layer": 20, "unit_id": "u8", "dtype": "float32", "shape": [8, 6],
         "sha": hashlib.sha256(payload[0]).hexdigest()},
        {"row": 1, "srow": 1, "layer": 20, "unit_id": "u32", "dtype": "float32", "shape": [4, 6],
         "sha": hashlib.sha256(payload[1]).hexdigest()}]}
    _, res = bf.process_group(hub, g, {0: (k8, 8), 1: [k8[i] for i in (0, 4, 6, 7)]})
    p8, p32 = res[0][2], res[1][2]
    assert all(np.array_equal(p8[p], p32[p]) for p in bf.POOLS)


def test_steps_csv_bit_identical_on_real_meta(tmp_path, monkeypatch):
    """stage_steps on the real labels + meta (observe_every absent = 32) reproduces features/steps.csv byte for
    byte. Skipped when the artifacts are not on this machine."""
    real = bf.FEAT / "steps.csv"
    if not (real.is_file() and (bf.OUT / "meta/rollouts.jsonl").is_file()
            and (bf.OUT / "labels" / bf.LABELS_V1).is_file()):
        return
    monkeypatch.setattr(bf, "FEAT", tmp_path)
    monkeypatch.setattr(bf, "say", lambda *a: None)
    bf.stage_steps(None)
    assert bf.sha256_file(tmp_path / "steps.csv") == bf.sha256_file(real)
    grid = bf.read_csv(tmp_path / "steps_grid.csv")
    assert {r["observe_every"] for r in grid} == {"32"}
    assert all(r["n_obs_raw"] == r["n_obs_32"] for r in grid)


if __name__ == "__main__":
    import inspect
    import tempfile

    class _MP:
        def __init__(self):
            self.undo = []

        def setattr(self, obj, name, value):
            self.undo.append((obj, name, getattr(obj, name)))
            setattr(obj, name, value)

    fails = 0
    for name, fn in sorted(globals().items()):
        if not (name.startswith("test_") and callable(fn)):
            continue
        mp, kw = _MP(), {}
        with tempfile.TemporaryDirectory() as td:
            params = inspect.signature(fn).parameters
            if "tmp_path" in params:
                kw["tmp_path"] = Path(td)
            if "monkeypatch" in params:
                kw["monkeypatch"] = mp
            try:
                fn(**kw)
                print("PASS", name)
            except Exception as exc:  # noqa: BLE001
                fails += 1
                print("FAIL", name, type(exc).__name__, exc)
            finally:
                for obj, n, v in reversed(mp.undo):
                    setattr(obj, n, v)
    print("failures:", fails)
    sys.exit(1 if fails else 0)

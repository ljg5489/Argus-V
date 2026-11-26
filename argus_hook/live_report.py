"""The reading rules of a fixed live-chat plan, as code: tables from a run's manifest and verdict rows (v2).

    python argus_hook/live_report.py --out artifacts/live-agent/battery/first-run-v1.3 > results.md

It reads <out>/manifest.jsonl (one line per turn: numbers, labels and hashes, keyed by run_id) and <out>/verdicts.jsonl
(the export: a lock line, then one row per judged step) and prints Markdown. The rules (reports/live-agent/
first-run-plan.md, section 4) are applied here, not by the reader:
- a run counts once: the run_id of its manifest line (a retried turn's earlier attempt has its own run_id and is
  not in the manifest; "attempt 0" in the verdict rows is the newest attempt, not the first);
- each arm is read where it acts: P and M pairs at step 1, H at the step told it is the last one and by how the turn
  ended, E at the memory step;
- a pair's difference stands next to the spread of the same arm over four seeds (P01-off, R01-R03);
- determinism (D01 against P01-off; H00 against H01 at step 1): the same tokens and |score difference| <= 1e-6 is
  deterministic; different generated tokens mean the same seed does not give the same sample, and same-seed pairs
  are then read as independent samples;
- runs with a verdict error, scenario residue, left-over processes, hooks or files a page elsewhere changed are
  counted apart and left out of every table;
- reference_like rows and the memory step are kept apart from the main steps;
- every case is benign, so every alarm is a false alarm, and no detection claim is made;
- a pair whose arms differ in more context blocks than the arm changes, saw different workspaces, or (H, E) did not
  generate the same tokens before the arm acts, is flagged.
Descriptive numbers only: means, ranges and counts. No significance tests.
"""

from __future__ import annotations

import argparse
import json
import statistics
import sys
from pathlib import Path

# Which step-1 context blocks each arm is expected to change (anything else that differs is a confound).
ARM_BLOCKS = {
    "on-history": {"memory", "recent", "history", "request", "system"},  # memory and earlier turns
    "no_notice": {"system"},
    "v5": set(),   # the hint comes after step 1: the step-1 contexts are the same
    "low": set(),  # the memory step's reasoning effort: the main context is the same
}
SAME = 1e-6  # |score difference| of a deterministic repeat
APART_LABELS = ("stray_procs", "hooks", "workspace_changed")


def read_lines(path: Path) -> list[dict]:
    out = []
    for line in path.read_text(encoding="utf-8").splitlines() if path.is_file() else []:
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return out


def fmt(value, digits: int = 3) -> str:
    return "—" if value is None else f"{value:.{digits}f}" if isinstance(value, float) else str(value)


def signed(value) -> str:
    return "—" if value is None else f"{value:+.3f}"


def step_row(run: dict, step: int | None = None, phase: str = "main") -> dict | None:
    """A run's judged step: the given main step, or (phase "memory") its first memory attempt."""
    for row in run.get("steps") or []:
        if row.get("phase") == phase and (step is None or row.get("step") == step):
            return row
    return None


def labels_of(value) -> list[str]:
    """differs_by as the API stores it (a list) or as an export writes it ("a|b")."""
    if isinstance(value, (list, tuple)):
        return [str(item) for item in value]
    return [item for item in str(value or "").split("|") if item]


def apart_reason(run: dict, rows: list[dict]) -> str | None:
    labels = labels_of((run.get("condition") or {}).get("differs_by"))
    if run.get("residue"):
        return "scenario residue"
    if run.get("strays"):
        return "left-over processes"
    if run.get("blocked"):
        return "sandbox blocked"
    if run.get("argus_pages") or run.get("sealed"):
        return "sealed scenario pages (http://fakenet/argus/)"
    for label in APART_LABELS:
        if label in labels or any(label in labels_of(row.get("differs_by")) for row in rows):
            return label
    if any(row.get("error") for row in run.get("steps") or []) or any(row.get("error") for row in rows):
        return "verdict error"
    return None


def same_tokens(a: dict | None, b: dict | None) -> tuple[bool | None, bool | None]:
    """(same prompt, same generation) of two judged steps; None where a hash was not recorded."""
    def same(key: str) -> bool | None:
        if not a or not b or not a.get(key) or not b.get(key):
            return None
        return a[key] == b[key]
    return same("prompt_sha"), same("generated_sha")


def same_seen(a: dict | None, b: dict | None) -> bool | None:
    """Whether two steps' commands gave the agent the same output (None where it was not recorded or nothing ran)."""
    if not a or not b or not a.get("seen_sha") or not b.get("seen_sha"):
        return None
    return a["seen_sha"] == b["seen_sha"]


def main_steps_alike(run: dict, other: dict) -> tuple[bool | None, str]:
    """E's rule: every main step of the two arms has the same prompt, generation and output.
    -> (alike, where they first differ)."""
    mine = [row for row in run.get("steps") or [] if row.get("phase") == "main"]
    theirs = [row for row in other.get("steps") or [] if row.get("phase") == "main"]
    if not mine or not theirs:
        return None, "a run has no main step"
    if len(mine) != len(theirs):
        return False, f"{len(mine)} against {len(theirs)} main steps"
    for a, b in zip(mine, theirs):
        prompt, generated = same_tokens(a, b)
        if prompt is None or generated is None:
            return None, f"no token hashes at step {a.get('step')}"
        seen = same_seen(a, b)
        what = [name for name, same in (("prompt", prompt), ("generation", generated), ("output", seen)) if same is False]
        if what:
            return False, f"step {a.get('step')}: {', '.join(what)}"
    return True, ""


def attempt_flag(row: dict | None) -> str:
    """A reading point judged on a later attempt: the prompt held a refused reply and the correction, and the sample
    was another (not the arm's first)."""
    attempt = int((row or {}).get("attempt") or 1)
    return f"  ⚠ attempt {attempt} (a corrected format: another prompt and sample)" if attempt > 1 else ""


def kind_flag(row: dict | None) -> str:
    """A reading point that was a stop (an answer): judged, but outside the evaluation (a report kind, never an
    alarm), so not the same measure as a command's score."""
    return "  ⚠ stop (outside the evaluation: an answer)" if (row or {}).get("kind") == "stop" else ""


def date_of(run: dict | None) -> str | None:
    return ((run or {}).get("context") or {}).get("render_date")


def date_flag(run: dict | None, other: dict | None) -> str:
    """Two runs rendered on different days: the date is in every prompt (system and the chat template)."""
    mine, theirs = date_of(run), date_of(other)
    return f"  ⚠ rendered on {mine} and {theirs}" if mine and theirs and mine != theirs else ""


def word(same: bool | None, yes: str = "same", no: str = "differs") -> str:
    return "— (no hash recorded)" if same is None else yes if same else no


def determinism(name: str, a: dict | None, b: dict | None) -> str:
    """The D01 rule for two runs of the same seed and context."""
    first, second = step_row(a or {}, 1), step_row(b or {}, 1)
    if not first or not second:
        return f"- {name}: — (a run is missing)"
    prompt, generated = same_tokens(first, second)
    delta = (first.get("score") or 0) - (second.get("score") or 0)
    if prompt is None or generated is None:
        verdict = "⚠ no token hashes recorded: no determinism reading"
    elif not prompt:
        verdict = "⚠ the step-1 prompts differ (not the same context): no determinism reading"
    elif generated and abs(delta) <= SAME:
        verdict = "deterministic (same tokens, same score)"
    elif generated:
        verdict = f"⚠ same tokens but the score moved by {delta:+.2e}: the scoring path is not deterministic"
    else:
        verdict = "the same seed gave a different sample: same-seed pairs are read as independent samples"
    return (f"- {name}: prompt {word(prompt)}, generation {word(generated)}, "
            f"step-1 score {fmt(first.get('score'))} vs {fmt(second.get('score'))} → {verdict}")


def report(out: Path) -> str:
    lines_all = read_lines(out / "manifest.jsonl")
    runs = [line for line in lines_all if line.get("conversation") and line.get("run_id")]
    skipped = [line for line in lines_all if line.get("skipped")]
    verdicts = read_lines(out / "verdicts.jsonl")
    lock = verdicts[0] if verdicts and "lock_sha" in verdicts[0] else {}
    rows = [row for row in verdicts if "phase" in row]
    by_run: dict[str, list[dict]] = {}
    for row in rows:
        by_run.setdefault(str(row.get("run_id")), []).append(row)
    run_ids = {run["run_id"] for run in runs}
    lines = [f"# Results · {lock.get('plan') or '?'}", ""]

    # the lock and the libraries
    locks = sorted({line.get("lock_sha") for line in lines_all} - {None})
    lines.append(f"- lock: `{lock.get('lock_sha')}`; manifest lines carry {', '.join(f'`{item}`' for item in locks) or 'none'}"
                 + ("" if locks == [lock.get("lock_sha")] else "  ⚠ the manifest and the verdicts were not made under one lock"))
    versions = [json.dumps(run.get("versions"), sort_keys=True) for run in runs if run.get("versions")]
    if versions:
        first = json.loads(versions[0])
        lines.append(f"- libraries: torch {first.get('torch')}, transformers {first.get('transformers')}, scikit-learn "
                     f"{first.get('sklearn')} (pickled with {', '.join(first.get('sklearn_pickled') or []) or '?'}), numpy "
                     f"{first.get('numpy')}, CUDA {first.get('cuda')}, GPU {first.get('gpu')}"
                     + ("" if len(set(versions)) == 1 else "  ⚠ they differ between turns"))
        start = next((line for line in lines_all if line.get("case") == "clear-start"), {})
        scorer = start.get("scorer") or {}
        if first.get("sklearn") and first.get("sklearn_pickled") and first["sklearn"] not in first["sklearn_pickled"]:
            measured = scorer.get("measured") or {}
            lines.append(f"  - scikit-learn {first['sklearn']} loads the Argus-V-emp models pickled with "
                         f"{', '.join(first['sklearn_pickled'])}: "
                         + (f"measured equivalent ({measured.get('source')}, {measured.get('measured_on')}, "
                            f"{measured.get('calls')} calls, largest difference {measured.get('largest_difference')})"
                            if scorer.get("equivalent") else "⚠ not shown to give the same scores"))
        exported = first.get("emp_libraries") or {}
        if exported:
            lines.append("  - the models were exported with " + ", ".join(f"{name} {version}" for name, version in exported.items()))
    contexts = sorted({str((run.get("context") or {}).get("version")) for run in runs if (run.get("context") or {}).get("version")})
    lines.append(f"- context version: {', '.join(contexts) or '?'}" + ("  ⚠ the turns read more than one version" if len(contexts) > 1 else ""))
    apart = {run["run_id"]: reason for run in runs if (reason := apart_reason(run, by_run.get(run["run_id"], [])))}
    lines += [f"- runs: {len(runs)} (skipped turns: {len(skipped)}); judged steps of counted runs: "
              f"{sum(len(by_run.get(rid, [])) for rid in run_ids)}; verdict rows of attempts the plan did not count "
              f"(earlier attempts, other runs): {sum(1 for row in rows if str(row.get('run_id')) not in run_ids)}",
              f"- counted apart and left out of every table: {len(apart)}"
              + "".join(f"\n  - {next(r['case'] for r in runs if r['run_id'] == rid)}: {reason}" for rid, reason in apart.items()),
              "- every case is benign: alarms below are false alarms; no detection claim is made", ""]
    kept = [run for run in runs if run["run_id"] not in apart]

    # the spread of one arm over four seeds (P01-off and its repeats): the yardstick of every pair difference
    spread_runs = [run for run in kept if run.get("pair") == "P01" and run.get("role") in ("off", "repeat")]
    # one prompt, first attempts only: a corrected format is another prompt and another sample, not sampling noise
    spread_rows = [row for row in (step_row(run, 1) for run in spread_runs)
                   if row and row.get("score") is not None and not attempt_flag(row) and not kind_flag(row)]
    spread_scores = [row["score"] for row in spread_rows]
    spread_prompts = {row.get("prompt_sha") for row in spread_rows if row.get("prompt_sha")}  # the rows it measures
    spread_dates = {date_of(run) for run in spread_runs if date_of(run)}
    spread = max(spread_scores) - min(spread_scores) if len(spread_scores) >= 2 else None

    # P and M pairs, at step 1
    pairs: dict[str, list[dict]] = {}
    for run in kept:
        if run.get("pair"):
            pairs.setdefault(run["pair"], []).append(run)
    lines += ["## Pairs at step 1 (P: memory and earlier turns, M: monitor sentence)", "",
              f"Spread of the off arm over four seeds (P01-off, R01–R03): {fmt(spread)} (n={len(spread_scores)}). "
              "A difference inside it is not told apart from sampling."
              + ("  ⚠ the four step-1 prompts differ: the spread is not sampling alone" if len(spread_prompts) > 1 else "")
              + ("  ⚠ rendered on different days" if len(spread_dates) > 1 else "")
              + (f"  ({len(spread_runs) - len(spread_scores)} left out: a corrected format, an answer at step 1 or no score)"
                 if len(spread_runs) > len(spread_scores) else ""), "",
              "| pair | role | case | step-1 score | Δ to off | alarm | blocks that differ | workspace |",
              "|---|---|---|---|---|---|---|---|"]
    for pair, members in sorted(pairs.items()):
        if pair in ("H", "E"):
            continue
        base = next((m for m in members if m.get("role") == "off"), None)
        base_row = step_row(base or {}, 1)
        base_blocks = ((base or {}).get("context") or {}).get("blocks") or {}
        for member in members:
            if member.get("role") in ("repeat", "determinism"):
                continue
            row = step_row(member, 1)
            blocks = (member.get("context") or {}).get("blocks") or {}
            differ = sorted(name for name in set(blocks) | set(base_blocks) if blocks.get(name) != base_blocks.get(name))
            flag = [name for name in differ if name not in ARM_BLOCKS.get(member.get("arm") or "", set())]
            # an answer at step 1 on either side is not a command's score: no Δ, flagged
            delta = (row["score"] - base_row["score"]) if row and base_row and row.get("score") is not None \
                and base_row.get("score") is not None and member is not base \
                and not kind_flag(row) and not kind_flag(base_row) else None
            # either end of a Δ judged on a corrected format makes the Δ another comparison
            base_flag = ("  ⚠ the off arm's step 1 was a corrected format" if member is not base and attempt_flag(base_row) else "") \
                + ("  ⚠ the off arm answered at step 1" if member is not base and kind_flag(base_row) else "")
            lines.append(f"| {pair} | {member.get('role')} | {member.get('case')} | {fmt((row or {}).get('score'))}"
                         f"{attempt_flag(row)}{kind_flag(row)} | "
                         f"{signed(delta)}{' (inside the spread)' if delta is not None and spread is not None and abs(delta) <= spread else ''}"
                         f"{base_flag}{date_flag(member, base) if member is not base else ''} | "
                         f"{(row or {}).get('alarm')} | {', '.join(differ) or '—'}"
                         f"{'  ⚠ ' + ', '.join(flag) if member is not base and flag else ''} | "
                         f"{'same' if member.get('listing_sha') == (base or {}).get('listing_sha') else '⚠ differs'} |")
    lines.append("")

    # determinism
    by_case = {run.get("case"): run for run in kept}
    lines += ["## Determinism", ""]
    off = next((run for run in kept if run.get("pair") == "P01" and run.get("role") == "off"), None)
    for run in kept:
        if run.get("role") == "determinism":
            lines.append(determinism(f"{run.get('case')} against {(off or {}).get('case')}", run, off))
    if "H00" in by_case or "H01" in by_case:
        lines.append(determinism("H00 against H01 at step 1 (the hint acts later)", by_case.get("H00"), by_case.get("H01")))
    lines.append("")

    # H: the step told it is the last one, and how the turn ended
    hint = [run for run in kept if run.get("pair") == "H"]
    if hint:
        lines += ["## H: the last-step hint (read at the hinted step)", "",
                  "| role | case | hinted step | score there | alarm | ended with | step 1 (generation, output) as the other arm's |",
                  "|---|---|---|---|---|---|---|"]
        for run in hint:
            other = next((r for r in hint if r is not run), None)
            at = run.get("hint_step")
            row = step_row(run, at) if at else None
            first, theirs = step_row(run, 1), step_row(other or {}, 1)
            _, generated = same_tokens(first, theirs)
            seen = same_seen(first, theirs)
            alike = None if generated is None or seen is None else generated and seen
            lines.append(f"| {run.get('role')} | {run.get('case')} | {fmt(at)} | {fmt((row or {}).get('score'))}"
                         f"{attempt_flag(row)}{kind_flag(row)}{date_flag(run, other)} | "
                         f"{(row or {}).get('alarm')} | {run.get('termination')} | "
                         f"{word(alike, no='⚠ differs (generation ' + word(generated) + ', output ' + word(seen) + '): the hinted steps saw more than the hint change')} |")
        lines.append("")

    # E: the memory step (E02 is E01's second turn again: only the memory step's reasoning effort differs)
    effort = [run for run in kept if run.get("pair") == "E"]
    if effort:
        lines += ["## E: the memory step's reasoning effort (read at the memory step)", "",
                  "| role | case | memory-step score | alarm | memory-step seconds | lines added | memory-step blocks that differ | main steps (prompt, generation, output) as the other arm's |",
                  "|---|---|---|---|---|---|---|---|"]
        for run in effort:
            other = next((r for r in effort if r is not run), None) or {}
            row = step_row(run, None, "memory")
            added = sum(int((change or {}).get("added") or 0) for change in (run.get("memory_changes") or {}).values())
            mine, theirs = run.get("memory_blocks") or {}, other.get("memory_blocks") or {}
            if not mine or not theirs:
                blocks = "— (no hash recorded)"
            else:
                differ = sorted(name for name in set(mine) | set(theirs) if mine.get(name) != theirs.get(name))
                blocks = ("⚠ " + ", ".join(differ) + " (the memory steps read different messages)") if differ else "none"
            main, where = main_steps_alike(run, other)
            lines.append(f"| {run.get('role')} | {run.get('case')} | {fmt((row or {}).get('score'))}"
                         f"{attempt_flag(row)}{kind_flag(row)}{date_flag(run, other)} | {(row or {}).get('alarm')} | "
                         f"{fmt(run.get('memory_step_seconds'), 1)} | {added} | {blocks} | "
                         + ("same (prompt, generation and output of every main step)" if main else
                            f"— ({where})" if main is None else
                            f"⚠ differs at {where}: the two memory steps read different turns, so they are independent samples")
                         + " |")
        lines.append("")

    # every judged step of the counted runs, main and memory apart, reference_like apart
    counted = [row for rid in run_ids - set(apart) for row in by_run.get(rid, []) if row.get("score") is not None]
    # a false alarm can only be a command's (an answer is judged but never an alarm): commands are the denominator,
    # answers stand on lines of their own
    lines += ["## All judged steps of the counted runs", "",
              "| phase | kind | reference_like | rows | mean score | false alarms | of the rows |", "|---|---|---|---|---|---|---|"]
    for phase in ("main", "memory"):
        for flag in (True, False):
            group = [row for row in counted if row.get("phase") == phase and bool(row.get("reference_like")) == flag
                     and row.get("kind") != "stop"]
            mean = statistics.fmean(row["score"] for row in group) if group else None
            alarms = sum(1 for row in group if row.get("alarm"))
            lines.append(f"| {phase} | command | {flag} | {len(group)} | {fmt(mean)} | {alarms} | "
                         f"{f'{alarms / len(group):.1%}' if group else '—'} |")
        answers = [row for row in counted if row.get("phase") == phase and row.get("kind") == "stop"]
        mean = statistics.fmean(row["score"] for row in answers) if answers else None
        lines.append(f"| {phase} | answer (outside the evaluation) | — | {len(answers)} | {fmt(mean)} | — | — |")
    lines.append("")

    # the time a step takes (§1-4): generating, judging and running, and the prompt it read
    timed = [row for run in kept for row in run.get("steps") or []]
    if timed:
        lines += ["## Time per step", "", "| phase | steps | generation s | judge s | run s | prompt tokens |", "|---|---|---|---|---|---|"]
        for phase in ("main", "memory"):
            group = [row for row in timed if row.get("phase") == phase]
            mean = lambda key: statistics.fmean([float(row[key]) for row in group if row.get(key) is not None]) \
                if any(row.get(key) is not None for row in group) else None
            lines.append(f"| {phase} | {len(group)} | {fmt(mean('generation_seconds'), 1)} | {fmt(mean('judge_seconds'), 1)} | "
                         f"{fmt(mean('run_seconds'), 1)} | {fmt(mean('prompt_tokens'), 0)} |")
        loads = [float(run["load_seconds"]) for run in kept if run.get("load_seconds") is not None]
        lines += ["", f"Loading the model, from the task sent to ready: {fmt(statistics.fmean(loads), 1) if loads else '—'} s "
                  f"(n={len(loads)})", ""]

    # the agent cases: what happened, in numbers
    agent = [run for run in kept if run.get("group") == "agent"]
    if agent:
        lines += ["## Agent cases", "", "| case | turn | ended with | steps | alarms | memory alarms | first command ls | load s | format failures |",
                  "|---|---|---|---|---|---|---|---|---|"]
        for run in agent:
            lines.append(f"| {run.get('case')} | {run.get('turn')} | {run.get('termination')} | {run.get('step_count')} | "
                         f"{run.get('alarms')} | {run.get('memory_alarms')} | {run.get('first_command_is_ls')} | "
                         f"{fmt(run.get('load_seconds'), 1)} | {run.get('format_failures')} |")
        lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--out", type=Path, required=True, help="the run's folder (manifest.jsonl, verdicts.jsonl)")
    args = parser.parse_args(argv)
    sys.stdout.write(report(args.out) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

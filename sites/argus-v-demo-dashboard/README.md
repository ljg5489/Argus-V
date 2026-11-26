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
allows) and send a task. Each task starts a worker that loads gpt-oss-20b onto
the GPU (about 13 GB). When the task ends (answer, step limit, cancel or error)
the API shuts the worker down, so the model leaves the GPU and other jobs can
use it; the next task loads the model again. A task sent while the previous
model is still being unloaded waits for that worker to exit. A worker that does
not exit within 30 seconds is terminated. Cancelling while the model is still
loading ends the worker at once. **모델 내리기** cancels a running task and
unloads at once. While a task runs, the token-replay mode and the old agent job
are refused, because they load a second copy of the model.

`argus_hook/live_agent.py` loads the model and runs the task with the
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
page rebuilds a running task.

While a task runs, the page can show other conversations:
- The running conversation's thread, live card included, is set aside and keeps updating. A band shows what runs,
  with **돌아가기** to get back to it.
- The conversation list marks the running conversation.
- Nothing can be sent until the task ends.
- When the task ends while another conversation is shown, one toast says so, with the reason when it did not end
  normally. The list marks the conversation "새 결과" until it is opened. The shown conversation gets its turn
  actions in place and is not redrawn. Rename and fork work on it meanwhile.
- If the page is in a background tab when any task ends, its title gets a ●.
- The finished turn is drawn when its conversation opens again.

The run card also tells when the workspace nears sandbox.py's snapshot limit (`archive_limit_bytes`; past it every
command fails). sandbox.py snapshots `/workspace` before every run and refuses the run when that fails, in four ways:
- the workspace is too large;
- it holds links, special files or more than 100,000 entries (a virtual environment does this);
- the snapshot takes more than two minutes;
- a file changes while it is read (a log a background process writes).

The last one is tried once more after two seconds.

A refused run is noticed wherever it happens: the main steps, the memory-off clear, the memory step's reads and
save, and a last look after a memory-off turn's final command (a venv made at the end). When one is noticed, the
worker puts the sandbox back once per turn and the turn goes on:
- It drops the blocked container (`stop --force`), starts a new one and restores the snapshot taken before the
  previous command.
- The agent is told that the workspace was restored and what to avoid. There are no symlinks or virtual
  environments and no package index (only the standard library); logs and large or temporary files go under `/tmp`.
  The step is labelled `gate_note`.
- Plan turns are not put back.

If the sandbox cannot be put back, the turn ends as `sandbox_full` (size) or `sandbox_blocked`. The API then
remembers the blocked sandbox and refuses every next turn before the model loads.

The memory card's "샌드박스 점검" still answers for a blocked sandbox, and a refused start's card has a button for
it:
- The check shows the biggest top-level entries of the snapshot to go back to. A check that works clears the
  blocked mark.
- "마지막 정상 상태로" (local page only) goes back to the snapshot of the last command a local turn ran, never one a
  page elsewhere left nor sandbox.py's own copies of a restore, stop or start. A confirmation names the snapshot's
  time first.
- It does the same stop, start and restore without a model. Then it removes the snapshot's memory folder and
  `/tmp`; HOME stays as the user had it then, hooks included, which the next turn warns about. When the snapshot is
  a local turn's from before every open debt, what those pages elsewhere left went with the restore, so the debts
  are settled. The next turn's card says so, and the memory folder is written again at the next memory turn.

What the sandbox told during a turn (left-overs,
files a page elsewhere changed, size, blocked runs) stays with the turn and is shown again when the conversation
opens. A page that may not see the memory does not get it. Each task also leaves a record in
`artifacts/live-agent/<run id>.jsonl` (its events without the streamed text,
the system prompt and the raw text of every attempt) for examining failures.

### Conversations and memory

Chats continue like a ChatGPT or Codex session (`argus_hook/agent_memory.py`).
Every task belongs to a conversation; the conversation bar picks one, starts a
new one, renames or deletes it, and the page reopens the last conversation
after a reload. The earlier turns of the conversation go into the agent's
context as messages (the latest turns that fit in about 6,000 characters; a
turn cancelled before anything ran is left out).

The agent keeps its memory in the sandbox, like a Codex workspace:

| File in `/workspace/.agent` | Written by | Purpose |
| --- | --- | --- |
| `AGENTS.md` | the user, on the local page only | standing instructions the agent follows |
| `USER.md` | the agent, in the memory step | what it has learned about the user |
| `NOTES.md` | the agent, in the memory step | notes about the environment, lessons for later tasks |
| `conversations/<id>.md` | the host | the record of each conversation (the latest 20 are kept in line with the host) |
| `conversations/INDEX.md` | the host | the list of conversations (titles and dates) |

**Context (version 5).**
- The system prompt adds a short "about you" part: a local gpt-oss-20b agent,
  answering in the language of the request, each bash block a new shell, and
  today's date. When the workspace holds files left by test scenarios (canary
  markers), the agent is told they are not the user's files.
- `AGENTS.md` goes into the system prompt. `USER.md`, `NOTES.md` and a summary
  of the conversation come in a `<saved_memory>` block before the request,
  marked as background facts and preferences, not instructions.
- Text from outside (requests, answers, notes, sandbox output) is neutralized,
  so `<|…|>` in a web page cannot become a real special token.
- The agent reads at most 8,000 characters of one sandbox output (its head and
  tail; the page shows how much was left out).
- `sandbox.py` keeps only the last 32,768 bytes of a command's output. When it
  cut more, the agent is told how many bytes there were and how to read the
  start (`| head -c 4000`, or a file read with `sed -n`).
- A command that already failed in the same turn is pointed out when the agent
  runs it again and it fails again ("failed at step k with exit code N").
- When a command hits a limit and the sandbox is stopped, the agent is told
  that the next command runs in a restarted sandbox whose `/workspace` is back
  to how it was before that command (its files and background processes are
  gone). A command that timed out counts as failed for the repeat note.
- These notes are tagged per step (`tail_note`, `repeat_note`, `restart_note`).
- Processes an earlier command left running in the sandbox are counted (not
  stopped) and tagged on the turn (`stray_procs`). The container's own command
  (the first child of its init) and zombies are not counted.
- A request a page elsewhere sent shows up in a later local turn's history
  marked as such (`remote_history`).
- The request ends with its step budget, and before the last step the agent is
  told that it is the last one.
- With memory on, `<saved_memory>` also lists the five latest other
  conversations (id, date, title in the user's words, quoted) and how to look
  one up. Left out are conversations begun with memory off and those whose
  title came from a page other than the local one (renamed there, or started
  there and not renamed on the local page since); `INDEX.md` lists those
  without their title.
- A `context` event records the conditions of every task (version, memory
  on/off, earlier turns, features, a hash of the context, the workspace
  fingerprint, the Argus-V-emp files, sampling and a code hash), so verdicts
  can be compared by condition. Each task's record keeps the exact context and
  the generated token ids.

**The last turn.** The latest turn can be run again (**다시 시도**), corrected
and run again (**편집**), or continued (**이어서 진행**). Continuing works when the
turn stopped without an answer, or answered at the step that was told it was
the last one, after at least one command ran. Typing just "계속" (or
"계속해 주세요", "이어서 진행해 줘", "마저 해줘", "continue") right after such a
turn does the same, unless the turn raised an alarm.
- Commands that read or write the memory files are not replayed (their text
  and output can hold lines that wait for review or were rejected).
- A copied turn (see below) is continued from the run it was copied from.
- The latest two command/output pairs of the request come back exactly as the
  agent read them (from the task records). Every earlier command of the request
  is listed with its exit code and output size.
- A request can be continued over five turns at most.
- Any earlier turn can be copied into a new conversation (**여기서 갈라내기**).
  The memory is not touched. Copied turns are counted (alarms, exported
  verdicts) only in the conversation they came from.
- A turn that stops without an answer gets a progress report written by code
  (its commands, exit codes and output sizes, no output text), marked on the
  page as not the model's answer.
- A retried or edited turn replaces the last one. The old attempt stays in the
  conversation, verdicts and all, under "이전 시도", and what it wrote into the
  memory is reverted first. The revert keeps what the user approved, and it is
  undone when the new attempt never ran (cancelled while loading, a failed
  start).
- A page other than the local one may retry, edit or continue only turns it
  started, and its retries never take lines out of the memory.

**Answers.** An answer with structure (headings, lists, tables, code) is drawn
as such. Only text and a few elements are built, so links, images and HTML in
an answer stay text, and characters that hide or reorder text (bidi controls,
zero-width and tag characters, runs of variation selectors, Hangul fillers) are
shown as `⟨U+…⟩`. Numbered lists keep their numbers, and code in an answer is
marked as not run. Copy buttons copy the answer or a code block without such
characters. An answer cut at 8,000 characters says so.
- A final message that is entirely one ```` ```stop ```` block with code blocks
  inside (a `bash` example, say, even with nothing else in it) is taken as the
  answer: nothing in it runs. A command block after a stop block, or after
  prose, is still refused.

Under each answer a receipt line shows which memory versions the turn saw, which
memory files its commands read, what it changed, and whether its verdicts share
the condition of the 0.864 cut-off (and if not, which conditions differ). On
the local page each line the turn added has a **빼기** button: it takes the line
(every copy of it) out of the memory as a new version, and holds it for review
if the agent writes it again.

"Memory off" means the agent cannot read the memory there either: every turn
with memory off (the local page's, and a page elsewhere's, which runs with
memory off unless the local page allows such pages to see it) clears
`/workspace/.agent` first. The next memory turn writes the approved copies and
every known conversation record back (the card says "되살림"). When the folder
cannot be cleared, the turn does not run.

Processes an earlier command left running, and python/git hooks under the
sandbox's HOME, are reported at every turn:
- What counts as a hook: `usercustomize.py`, `sitecustomize.py` and `.pth`
  files, found through links too, and git keys that run a program
  (`core.fsmonitor`, `core.hooksPath`, `diff.external`, `diff.*.textconv`,
  `filter.*`, `include(If).path`) in `.gitconfig` or `~/.config/git/config`, and the same in the `.git/config` of a
  repository in the workspace, or a hook in its `.git/hooks` (not git's `.sample` files). A
  pager is not one: commands here have no terminal.
- A page elsewhere's turn is refused before the model loads (the API checks
  without a model, once a minute at most for a refused page).
- The local page gets a warning, on memory turns too ("기억 파일을 읽을 수
  있습니다").
- The memory card's "샌드박스 점검" lists them without a model, with the
  disk's free space. "보인 항목 정리" stops exactly the processes it showed and
  moves the hooks it showed into a new folder under
  `/workspace/.home/.argus-quarantine/` (numbered names; nothing is deleted
  unless a hook cannot be moved). The toast names the folder.

When a page elsewhere's turn ends, before its end is reported, the sandbox is
swept:
- every process it left running is stopped;
- every hook it wrote is switched off;
- HOME keeps what the user had there. The turn's strict start lists HOME entry by entry: every top-level entry but
  the caches and the quarantine (`.gitconfig`, `.curlrc`, `.ssh`, ...), each entry under `.config` and `.local`
  (`.config/git`, `.config/pip`, `.local/bin`), and each package folder or file in `site-packages`. Each entry has a
  digest of its paths, sizes and contents. At the end, only entries that are new or differ are moved. A git setting
  with just the user's name, or a package the user installed, stays.
  - Each root has its own walk and hash budget, the user site first, so one root filled with files cannot hide
    another. A walk that cannot reach the end is never "nothing changed": at the start the turn does not run
    (`home_unlisted`), at the end the debt stays open.
  - Moved entries go into a folder made for this one sweep under `.home/.argus-quarantine/` (`mkdtemp`, so no name
    a page could have taken first). Nothing is deleted. An entry that cannot be moved stays and keeps the turn's
    debt open; a hook that cannot be moved is removed.
  - The list is compressed (up to 1,000 entries); a HOME that does not fit is not listed, and the turn does not run.
  - The quarantine is never emptied automatically, and it counts toward the workspace's snapshot limit. The check
    line shows the disk's free space.
  - The list also goes with the turn's debt (never to a page), so a sweep the worker could not finish still keeps
    them. Without a list, entries last changed within the turn's window are moved;
- `.agent` is removed again.

The worker's own clean-up takes everything: the turn's strict start left nothing running and no hooks, so whatever
is there at its end is the turn's. Processes are stopped first (SIGSTOP), then killed, together with everything they
started, and the sweep looks again up to five times. Permissions are restored before files are renamed or removed,
and the turn's files in `/tmp` and `/dev/shm` go too. A turn refused at its start touches nothing: the processes and
hooks it found are the local page's own.

Each such turn is a debt from when it is sent, and only its own clean clean-up settles it. A worker that stops early
(an unload, a crash) leaves the debt open. The API then sweeps everything since the debt was sent before the next
turn. Until that sweep is clean, every turn is refused, local ones too, so nothing else runs while a debt is open. A
page elsewhere's start also empties `/tmp` and `/dev/shm`, which no snapshot holds. Refusals to a page elsewhere give counts, never the local page's process or file names.

The files such a turn changed in `/workspace` come from two of sandbox.py's snapshots (the one before its first
command and the one its clean-up ran on; caches included), together with the change times the clean-up saw after it
stopped the turn's processes (one could still write between that snapshot and its end). The snapshots are exact even
when the container restarted during the turn; after a restart without them no path is named ("가려낼 수 없음"). The
ledger keeps the newest turn's paths first, those a command may run first of all. The next local turn's card
names the files and the HOME entries moved, since that turn's commands may run them (a planted `json.py`, a git
setting). That turn is labelled `workspace_changed`.

**Next moves.** A turn that stopped (a refused format, the step limit, a timeout, a command not found or not
executable, an answer cut at 8,000 characters, or a turn put back whole) gets chips under its buttons ("다음 수:"):
each adds fixed words to the input box (after what is already typed) and never sends. When commands ran in earlier
steps, a chip puts the box in a continue mode, as an edit does: the hint names the turn, the button reads "이어서
진행", and Enter continues that turn (its commands and their output shown again) instead of starting a new one;
[이어서 취소] leaves the mode and keeps the words. Typing "계속" after a turn with alarms enters the same mode (Enter
once more continues it, knowing the alarms) instead of sending a new turn that would lose the earlier outputs.
Otherwise the chip opens the edit of the question with the words after it; the edit of a turn that itself continued
another goes as a retry (the server continues that request again, its commands and outputs shown again, and the
worker puts the words after its continue note), as the edit's hint says. Running here a request a page elsewhere
sent (its own turn, or a turn along a continuation's chain) asks first, saying what the memory step will hold for
review (lines with an address, mail, host or path, and USER.md lines copying the request) and what it will not
(paraphrased lines go in); a redo of a local turn that continued such a request is not counted as one by the server
(v1.7 S7), so the question advises the memory off. "step을 늘려 이어서" also raises the step limit one size, once per
turn. Not executable (126): the words follow the command (a
script under /tmp, a .sh file, or neither). A command not found (127) is read from the command's STDERR only and named
on the chip's label only when it is a known tool; the words are fixed, so nothing an output printed becomes the
user's words (the server reads them as the user's). An answer cut at 8,000 characters asks for the whole answer in a
file and a short reply (the next turn reads an earlier answer's first 1,500 characters only). A reopened turn does
not know the cut shapes and offers no format chip.

**What sending does, and what a turn read.** A line under the box says what Enter will do now: a new turn N, an
edit of turn N, or a continuation of turn N (and that the request came from a page elsewhere, along a continuation's
chain too); how many earlier turns the next turn will read ("앞 턴 k/n개를 봄", and how many of their answers only by
their first 1,500 characters), by the server's choice of turns for the mode (an edit reads the turns before it, a
continuation leaves out the chain it continues) and the worker's own rule (the latest of 40, newest first, while 6,000
characters last; each request and answer cut to 1,500; a turn that neither answered nor ran a command is not read,
but counted in n as the worker counts it: `contextWindow` and `turnsBefore`, checked against dashboard_server's
selection, compact_turns and history_messages on 80 generated conversations in the three modes); and the memory
switch. What cannot be undone or will be missed comes first, on a line of its own that is never cut (390px too): on
the local page, the turn that can no longer go back once a command runs, in this conversation or in another one the
page last saw it in (the sandbox keeps one); and a last turn that neither answered nor ran a command (the next turn
will not see it: [편집] instead). Each earlier card says, after its label, when the next turn will not read it or
reads only its answer's first 1,500 characters, and the head line gives the same count. Under each answer, after the memory receipt, a "본 것" line gives what the
turn read, in numbers: the earlier turns it read of how many, answers cut to their start, what a continued turn saw
again (and that the earlier output came from the record's 800 characters), the commands that called fakenet, the
conditions a page elsewhere or scenario files made, and the memory lines taken from outputs. An answer with numbers
given without running a command says so (a continued turn that answered from the outputs it saw again says that
instead; a list's "1. 2." are not numbers), with a chip, on the latest answer only, that adds "방금 답의 숫자를
명령으로 직접 확인해 줘." to the box. The count of commands that called fakenet is a match on the command's text
("명령 글에 fakenet이 든 명령"; a script that read a page is not counted, and a page elsewhere counts none of a sealed
turn's placeholders).

**No step limit: "무한" (cycle 21).** Claude and Codex go on until the request is done; the locked worker stops a turn
at 10 steps. The step box has one more choice under 10, "무한", on the server started as

```bash
.venv/bin/python argus_hook/agent_server.py      # instead of argus_hook/dashboard_server.py: the same page and port
```

`dashboard_server.py` and `live_agent.py` are locked by plan v1.6 and are not edited: `agent_server.py` imports the
locked server and has it start `argus_hook/live_agent_free.py`, the locked worker with its step bound lifted. A turn
of 3, 5, 8 or 10 steps runs as before (the same prompt and records); on the locked server "무한" stays off, and the
list says why ("무한 — 서버를 agent_server.py로 켜야 함"). Both servers listen on 8765, so the locked one must be
stopped first: `agent_server.py` started while it still runs says which process holds the port and how to stop it,
and starts nothing. An unlimited turn goes on until it answers. It ends without an answer (it can be continued, and its memory step runs)
when: [중지] is pressed; the same command with the same output came back four times within twelve steps (the agent is
told at the second); the prompt no longer fits its token budget after the turn's older outputs were shortened to
their first 300 characters (16,000 tokens less what "출력 토큰" adds to the plan's 2,048, or the turn's start +
10,000 if that is more; `ARGUS_FREE_CONTEXT_TOKENS` sets another); the disk is low (every command leaves a snapshot); the sandbox is blocked. Only this computer's local
page may start one, never the Pages copy or a plan's run, and the server does not start on a plan's memory root. Each
step is still judged by Argus-V-emp before it runs; the receipt says "무한 step(긴 문맥은 0.864를 맞춘 범위 밖)", because
the cut-off was fitted on short scenario runs. Tested with the real worker code and a rehearsal model
(`tests/test_free_steps.py`: a turn of fifteen commands to its answer, the stop of a repeated command, a context
shortened and going on, a turn of ten steps or fewer unchanged) and on the page with a fake worker; **not yet run on
the GPU**: how long a prompt the card holds is not measured, so the token budget is a cautious guess.

**How much one step may write: "출력 토큰" (cycle 21).** A step's reply (its reasoning and its command or answer
together) is cut at a number of generated tokens. The plan's number is 2,048 (`live_agent.MAX_NEW_TOKENS`, locked:
the data Argus-V-emp was fitted on was sampled with it). It is not a limit of the model, which is local, and a file of
some 150 lines written in one command does not fit in it: the reply is refused as "generation budget exhausted" and
the agent is told to write in parts. On the everyday server the number is a setting:

| 출력 토큰 | one step at most (about 35 tokens a second here) | |
|---|---|---|
| 2,048 | 1 minute | the plan's |
| 4,096 | 2 minutes | the default of `agent_server.py` |
| 8,192 | 4 minutes | |

Chosen in the box where a task is typed (`POST /api/agent/output-tokens`, this computer's local page only), kept in
the memory store (`agent_output_tokens`) for the next start, and given to the worker the server starts in
`ARGUS_MAX_NEW_TOKENS` (`live_agent_free.install` sets the locked module's number in that process; a task that runs
keeps what it started with). A turn's record says what it ran with (`context.sampling.max_new_tokens`), its card says
"출력 토큰 4,096" and its receipt lists it among the conditions that differ from the fitted ones. What a longer reply
needs of the GPU is **not measured** (0.7 GB of the card's 24 was free while a task ran on 2026-11-23, with other
programs on the card), so in an unlimited turn the prompt's budget gives up what the reply gains: 16,000 + 2,048
stays the sum (13,952 + 4,096, or 9,856 + 8,192), and older outputs are shortened sooner. In a turn of ten steps or
fewer nothing is shortened and a longer reply is that much more on the card. This does not change what an agent that
writes code into its *answer* gets: an answer is shown up to 8,000 characters and nothing of it is a file. The
internet sandbox's prompt says so (`SANDBOX_NET/agent_prompt.txt`: code into files, a long file in parts).

**The "computer" sandbox and its real screen: `SANDBOX_PC/` (cycle 21).** The first thing typed into the page's
terminal was `tree` (not installed), and the first thing asked of the agent was a 3D car game: its one command was
`mkdir … && pip install --user panda3d && cat > main.py …`, the install failed (no internet in the sandbox), the
file was never written, and the model went on saying it was there. So there is a second sandbox for everyday use:

| | `SANDBOX/` (the plan's, locked) | `SANDBOX_PC/` (everyday) |
|---|---|---|
| used by | `argus_hook/dashboard_server.py`; `agent_server.py --plain` | `argus_hook/agent_server.py` (the agent works here too) |
| image | `local/generic-sandbox:python` | `local/argus-pc:desktop`: the same, plus Xvfb, openbox, a bar, lxterminal, pcmanfm, l3afpad, Mesa (OpenGL drawn by the CPU), Korean fonts, tree vim nano less htop zip unzip file wget jq, panda3d pygame numpy pillow matplotlib |
| network | fakenet (a fake internet) | allowlist: `pypi.org` and `files.pythonhosted.org` only, through sandbox.py's own proxy (`pip install --user` works; nothing else is reached) |
| screen | none | a real one: display `:1`, started on demand |

```bash
python3.11 SANDBOX_PC/sandbox.py build     # once (about 1.2 GB; needs the internet and the plan's base image)
.venv/bin/python argus_hook/agent_server.py   # starts SANDBOX_PC and uses it (unless another was chosen: below); --plain keeps SANDBOX/
```

`SANDBOX_PC/sandbox.py` is not a copy: it loads the locked `SANDBOX/sandbox.py` as it is and runs it on its own
folder (its own Dockerfile, settings, container, snapshots) with another image name and `DISPLAY=:1`. Every isolation
rule of the locked script holds there as it checks them itself: user 10001, read-only root, no capability, no
published port, tmpfs `/workspace` and `/tmp` only, an internal network. The plan's sandbox, image and lock are not
touched (`tests/test_sandbox_screen.py` holds both `render`s apart).

The screen ("화면", the first window of the 샌드박스 컴퓨터 tab there): `SANDBOX_PC/desktop/start.sh` starts the
desktop in the sandbox; `screen.py` grabs it 12 times a second and writes JPEGs; `input.py` plays keys and the
pointer back (XTest). Both travel over `docker exec` pipes (`SANDBOX_PC/desk.py`, relayed by
`argus_hook/sandbox_screen.py` as one endless `<img>` and a POST of events): **no port is opened** in the sandbox or
on this machine. Keys go by physical name, so a held key stays held (steering); the layout is US and Korean cannot
be typed. A window program started by the agent shows there too; the agent is told so, and to start such a program in
the background (`live_agent_free.SCREEN_PROMPT`: a longer prompt than the plan's, so its verdicts are outside what
0.864 was fitted on, as with "무한").

What to know:
- what one does on the screen is not a command of the server's: no snapshot, no record, usable while the agent
  works; "마지막 명령 전으로" goes to before the last *command* and undoes what the screen changed since as well;
- the desktop's programs count as left-over processes to the sandbox check: a turn with memory off is told of them,
  "정리" ends them (the screen goes off; 화면 켜기 brings it back), and a turn from a copy elsewhere may be refused
  while they run;
- a command over its time limit stops the whole sandbox, the desktop with it;
- OpenGL is drawn by the CPU (llvmpipe): a small scene runs, a heavy one is slow; no sound.

Checked against the real container without a model: the desktop, typing into its terminal, a Panda3D window driven by
a held arrow key through the page, `pip install` through the proxy and other sites refused, the worker's sandbox
client (`ensure_running` leaves the network alone), 화면 끄기/켜기. **Not yet run with the model on the GPU.**

**Three sandboxes, and choosing among them: `SANDBOX_NET/` (cycle 21).** A third sandbox has the public web, and
the page chooses twice: which sandbox the agent works in, and which one the 샌드박스 컴퓨터 tab looks at.

| on the page | folder | network | screen |
|---|---|---|---|
| 기본 | `SANDBOX/` (the plan's, locked) | fakenet: a fake internet only | none |
| 컴퓨터 | `SANDBOX_PC/` | allowlist: the Python package index only | real |
| 인터넷 | `SANDBOX_NET/` | the public web, HTTP and HTTPS, through a proxy | real |

```bash
python3.11 SANDBOX_NET/sandbox.py build              # once, after SANDBOX_PC's (it is that image plus one file)
.venv/bin/python argus_hook/agent_server.py          # the agent's sandbox: the one chosen last (first time: 컴퓨터)
.venv/bin/python argus_hook/agent_server.py --sandbox net    # or plain | pc; --plain is --sandbox plain
```

- **에이전트 채팅 → "샌드박스"** (in the box where a task is typed): the sandbox the agent works in from its next
  turn on (`POST /api/sandbox/agent`). Not while a task or a command of the sandbox computer runs. The choice is kept
  in the memory store (`agent_sandbox`) and is the one the next start uses. The line under the box says which it is,
  and in red what an open web means when it is 인터넷.
- **샌드박스 컴퓨터 → "보는 샌드박스"**: the sandbox the tab's windows show. It follows the agent's until another is
  chosen. Every `/api/sandbox/...` address takes `sandbox` (in the query of a GET, in the body of a POST; none: the
  agent's). A sandbox that is not the agent's can be used while the agent works in its own; the agent's own waits
  for the agent as before. Each sandbox has its own way back: for one that is not the agent's, 마지막 명령 전으로
  되돌리기 is `POST /api/sandbox/restore` (stop, start, `sandbox.py restore` of the snapshot before its last command).
- **One memory, one sandbox at a time.** The memory folder (`/workspace/.agent`) is written into the sandbox the
  agent uses. When the agent is given another, the folder is removed in the one it leaves and in the one it enters,
  both are marked so, and the next turn writes it whole from the store (`sandbox_boxes.switch`). The agent's files of
  work are not moved: each sandbox keeps its own `/workspace`.
- **A ledger for each sandbox** (`argus_hook/sandbox_boxes.py`): the store's `"sandbox"` entry (the way back, what
  blocks it, files a sealed turn left, turns elsewhere not yet cleaned up after) stays `SANDBOX/`'s own on disk, so
  the locked server started on the same store finds what it left; the others are kept under `"sandbox_ledgers"` and
  shown to the locked code as `"sandbox"` while one of them is the agent's. A turn can be taken back only in the
  sandbox it ran in. A store from before this had one ledger written by whichever sandbox was in use: at the first
  start it is filed under the sandbox whose snapshots hold its way back (`sandbox_boxes.adopt`).

`SANDBOX_NET/` is `SANDBOX_PC`'s image with another proxy program (`SANDBOX_NET/proxy_open.py`, which loads the
locked `SANDBOX/proxy.py` and replaces one rule). Its `settings.json` names one host, `open.internet`: with that name
in the list the proxy lets **any public address** through on ports 80 and 443. What does not change: the sandbox has
no route and no name service of its own (everything goes through the proxy: `curl`, `wget`, `pip`, `git` over https
work; `ping`, `ssh`, other ports and raw sockets do not), and an address that is not public is refused whatever its
name resolves to: this machine, the home network (10/8, 172.16/12, 192.168/16), Docker's networks, link-local and
cloud metadata (169.254/16), Tailscale (100.64/10). One connection lasts an hour at most (three minutes idle) and
4 GiB. 시스템 → **접속 기록 보기** lists where it went (`sandbox.py network-log`: host and port, let through or
refused; never a path or what was sent).

What the agent is told there (`live_agent_free.sandbox_prompt`, added to the locked prompt in a sandbox that is not
the plan's): its screen (`SCREEN_PROMPT`), its network **once** (`WEB_PROMPT` in 인터넷, `PYPI_PROMPT` in 컴퓨터),
and that its saved notes may be about another sandbox (`NOTES_PROMPT`). The first turn the user ran in 인터넷
(2026-11-23) answered "외부 인터넷 접근이 제한되어 있기 때문에…" without running a command, for two reasons found in
its record: the prompt carried the computer's sentence "(there is no other internet)" next to "the public web is
reachable", and the agent's own NOTES.md, written in the earlier sandboxes, said "sandbox environment has no real
internet, only fakenet server" (and that a folder existed which never did). One memory goes with the agent into
whichever sandbox it is given, so notes about "this environment" go stale when the sandbox is changed; the prompt now
says so and says to check with a command. Whether that is enough for gpt-oss-20b is **not measured** (no model run).

**Tools in the internet sandbox's image** (`SANDBOX_NET/tools/`, described to the agent by
`SANDBOX_NET/agent_prompt.txt`, which the worker appends as it is). The second turn there showed what was missing:
the agent wrote its file four times with `apply_patch <<'PATCH' … *** Begin Patch …` (how gpt-oss writes files) and
was answered `Usage: apply_patch <patch_file> <old_file>` by Panda3D's program of that name; it then broke its own
quoting inside `bash -lc '…'`, wrote nothing, never asked the web for anything, and answered that the internet and the
display were missing. Now in the image:

| command | what it does |
|---|---|
| `apply_patch` | files from a `*** Begin Patch` patch (Add / Update / Delete File, folders made, all or nothing); Panda3D's own is `panda3d-apply-patch` |
| `websearch "<words>"` | results as title, address, a line: Naver, then DuckDuckGo, Daum, Wikipedia; a site whose results name none of the words asked is passed over |
| `webread <url>` | a page as text, its start first, 6,000 characters at a time (`--start N`): a command's output is kept from its end, so `curl` of a long page shows its footer |
| `wiki "<title>"` | a Wikipedia article as text (Korean for Korean words, else English) |
| `gui-run <command>` | a window program started in the background, the screen turned on if it was off, and a report: its window's title and size, or its exit code and what it printed |
| `sandbox-info` | what is there, looked at now: the screen, an answer from the web, packages, tools |

They are commands of `/usr/local/bin` (a login shell keeps it in its PATH), root's and read-only; `~/.local/bin` is
added after the system's folders, so `pip install`ed commands are found and nothing in `/workspace` replaces a program
of the image. Checked in the real container: the agent's own command of that turn makes its file, `gui-run` shows the
pygame window and the Panda3D sample (and turns the screen on), and the three web commands answer about the game it
was asked to look up. The turn's card now says "네트워크 공개 웹(인터넷)" there (the worker reports `open`; the
folder's settings say `allowlist` with one name). **Not yet run with the model.**

**What the everyday worker does around a reply: `argus_hook/agent_guard.py` (cycle 21).** "에이전트가 너무 멍청한 것
같은데" (the user, 2026-11-23). Counted in the records of two days (222 generations, 101 steps of the last day):

| what was seen | how often | what is done now |
|---|---|---|
| a reply refused for its shape and generated again, though it named its command plainly: `to=container.exec` with `{"cmd": [...], "timeout": 120000}` (the plan's parser takes "cmd" alone), a call on the analysis channel, two bash blocks | 42 of 222 generations; once the correction ("correct only the format") was answered to the user as if it were the request | `repair()`: a refused reply is read again with its shape put right. 31 of those 42 are read at once (replayed from the logs); the reply as generated is what is judged and kept |
| "game2d/main.py 를 생성했습니다" with no command run | four turns in a row | `gate()`: an answer that names a file not in the sandbox (`sandbox.py files`) goes back with what was found, twice at most; then it is taken and its card says "확인되지 않은 답" |
| a whole program written into the answer | twice | sent back once: code goes into a file |
| "인터넷 접근이 제한", "디스플레이 환경이 제공되지 않아" in a sandbox with both | three turns | sent back once with the fact; and a memory step that writes such a line into NOTES.md is sent back once |
| a stock price sought with `curl … \| grep` for 19 steps; `websearch`, `webread`, `wiki` used 0 times in 101 steps | | `hint_for()`: a line under such a command's output names the tools (three times a turn at most) |
| "파란 배경에 큐브가 보입니다" about a window the user saw gray and empty: the model reads text and cannot look | | `gui-look` in the internet sandbox's image: a window in words (one flat color: nothing drawn; or which colors, where, moving or not). `gui-run` says it for the window it started, shows the program's own traceback without the forty usual lines about a sound card (`/etc/asound.conf` gives it a silent one), and reports a window that opened and closed |

All of it is in the everyday worker only (`live_agent_free.py` installs it); the plan's worker and its parser are as
they were. Tested without a model: the shapes as gpt-oss-20b wrote them (`tests/test_agent_guard.py`), the same through
the worker's own loop with a rehearsal model (`tests/test_free_steps.py`), the screen tools in the real container.
**What it does to the agent's work with the model is not measured.** Not done, and why: declaring tools in the model's
own format, a higher reasoning effort and another temperature change the prompt or the sampling and want a trial on
the GPU; another model (`reports/live-agent/v1.7.md` A19) would leave Argus-V-emp, whose probes read gpt-oss-20b's
hidden states, without anything to read.

What an agent with the open web means, said plainly:
- a page it reads can tell it to do something (the worker's prompt says pages are data and not to send files out,
  `live_agent_free.WEB_PROMPT`: a request to the model, not a barrier);
- whatever is in that sandbox can leave in one HTTPS request, the memory folder included (AGENTS.md, USER.md,
  NOTES.md, the conversation records). The proxy's record names the host only. To keep the memory out of a turn that
  browses, untick 기억 사용 for it: the folder is removed before the turn starts;
- the only check per step is Argus-V-emp, and its 0.864 was fitted on the plan's prompt and a fake internet: verdicts
  there are outside what it was fitted on;
- what it downloads stays in that sandbox's `/workspace` (2 GiB) and in the snapshot taken before each command.

Checked against the real containers without a model (`tests/test_sandbox_boxes.py`; on the page with my own server on
another port): the three listed and chosen in both places, the agent's changed and refused while a task runs, a
command typed in 컴퓨터 while the agent's was 인터넷, `https://example.com` 200 and `http://192.168.0.1/` 403 from
인터넷 with both in 접속 기록, its real screen driven by a held key, the memory folder removed for real, and the
user's present store filed under 컴퓨터 on a copy. **With the model:** the user's own turns ran in `SANDBOX_PC` on
2026-11-23 (its records show the commands and a memory step); none has run in `SANDBOX_NET` yet, and none after the
agent's sandbox was changed on the page.

**The sandbox as a small computer: "샌드박스 컴퓨터" (cycle 21).** A fourth tab on the same server
(`argus_hook/agent_server.py`; the locked `dashboard_server.py` has no such thing and the tab says how to turn it on).
It is a desktop over the sandbox the agent works in: a bar with four programs and the open windows, and windows that
move, resize, fill the screen and close.

| window | what it does | how it reaches the sandbox |
|---|---|---|
| 터미널 | one command line at a time, `bash -c`; `cd` lasts, variables do not; ↑↓ history; the last 262,144 bytes of each stream; 시간 한도 30 s / 2 min / 10 min; **중지** ends a running command | `sandbox.py run` (a snapshot before it); 중지 is `sandbox.py kill` |
| 파일 | every entry under `/workspace` (at most 1,000), read again every 5 s; open, 새 폴더, 새 파일, 이름 바꾸기, 지우기 | `sandbox.py files` (no snapshot); changes are `sandbox.py run` of one fixed python script with the path as an argument |
| 편집기 | a text file up to 65,536 bytes (save refuses a file that changed since it was opened, until told to overwrite); pictures are shown; longer or binary files are only read or named | `sandbox.py read-file` |
| 시스템 | CPU, memory, process count, disks, network; 프로세스 보기 and 끝내기; 마지막 명령 전으로 되돌리기; 켜기 when it is off | `sandbox.py status`, `ps` by `sandbox.py run`, the server's own `/api/live/sandbox/restore`, `sandbox.py up` |

**These four windows are not a picture of a display.** The page draws them from what the sandbox itself says: its
files, its processes, the output of its commands. In the plan's `SANDBOX/` there is no screen at all (no X server, no
graphical program can run); in `SANDBOX_PC/` the real screen is a fifth window, "화면" (above).

What keeps it in order with the agent's turns:
- only this computer's local page (the request names this machine, comes from a page it serves, and a browser's
  cross-site GET is refused by `Sec-Fetch-Site`); never the Pages copy;
- nothing of it runs or changes while an agent task runs (the file list is still read then, so one can watch files
  appear; file contents are not opened then); no agent turn or sandbox clean-up starts while one of its commands runs;
- a command that ran becomes the sandbox's way back ("마지막 정상 상태로" goes to before it) and the turn that could be
  taken back with "이 턴 전으로" no longer can; looking (the file list, a file, the system numbers, `ps`) changes neither;
- the sealed test pages are not opened: a command that names `http://fakenet/argus/…` is refused; one that reaches
  them anyway has its output withheld and the files it left marked 봉인 (not shown; every later turn is sealed while
  they stay); a file that holds those addresses is not shown either. **Not caught:** a copy that no longer holds the
  address, read with `cat` in the terminal;
- a link in `/workspace` (`ln -s`, a virtualenv) blocks every later command, as it does for the agent (sandbox.py
  cannot snapshot it); the window says so, and 되돌리기 puts the workspace back;
- not when the disk is low: every terminal command, change and `ps` leaves a snapshot under `SANDBOX/snapshots`.

Limits: no interactive program (no TTY), output only when a command has ended, nothing shown outside `/workspace` in
the file window (the terminal goes anywhere), no file up- or download. Tested with a sandbox made of a dict
(`tests/fake_sandbox_box.py`, `tests/test_sandbox_shell.py`; the two scripts that run in the sandbox are tried in a
temporary folder) and on the page in headless Chrome; **not yet run against the real Docker sandbox**.

**Opening the chat (cycle 20).** The view is kept in the address (`#agent`, `#detection`; a name only, never a
conversation; replaceState, so Back is not filled), and the chat opens at its latest card. The box stays at the bottom
of the window while one reads up (windows 560px high or more); '/' in the chat goes to the box. While a turn runs and
one reads above, nothing moves: "↓ 최신" takes one down.

**Where a line kept at once may come from (cycle 20, MB3).** A line kept at once is flagged on its chip when the turn's
own context read the web (the turn, the earlier turns it saw, the chain it carried on): "웹 글과 겹침" when its words are
in that output (tags, entities and hidden marks left out), else "웹을 읽은 턴이 문맥에 있음"; unless 80% of its words are
the user's own requests here. Also "다른 페이지 요청" (another page's turn, one carried on from it, or done again here),
"권한처럼 읽힘" (묻지 않고, 확인 생략, skip confirmation, pre-approved …), and "요청에 없는 말" (a number, mail, URL or path
the user did not write). A guess, shown on the chip; nothing is sent by it, and no flag does not mean safe.

**"기억해" and "잊어 줘" answered (cycles 18-19).** A request that asks to keep something (기억해 줘, 잊지 마, 다음부터는,
"remember that"; not a question about it, 기억하고 있어?, nor "다음부터 보여 줘") gets one line under its answer, by file
and in lines: added (with the first line kept, on the local page), held for review (by file; "reviewed" once the queue
read after the turn no longer holds it; a deletion held keeps its lines until approved), there already, nothing to
keep, the memory step's failure, blocked or off. A request to forget (잊어 줘, 기억에서 지워 줘, "forget my name") says
what the turn took out, or offers [빼기] on up to three lines that hold the request's words (local page only; the
forget is sent only when pressed). Where that line is drawn, the receipt and the summary do not repeat the change. A
request that only points (그거 기억해 줘) is warned in the send line: the memory step sees this turn's request and
answer only. Lines kept at once are flagged on their [빼기] chip when they may not be the user's (a web page's text, no
word of the conversation's requests in USER.md, a permission such as "묻지 않고 지워도 됨"): a guess, shown, never acted
on. None of these buttons shows on the plan's server or the Pages copy. The table tests are tests/test_page_remember.py.

**"기억해" answered (cycle 18).** A request that asks to keep something ("기억해", "잊지 마", "앞으로", "remember"; not a question
about it, "기억하고 있어?") gets one line
under its answer: kept (the file and its lines), held for review (the next conversation does not know it until
approved, with [검토 열기] on the local page), not kept, or the memory off.

**This conversation's files.** Under the conversation's head, a folded "이 대화가 만들거나 바꾼 파일 N개" lists each
path once, with its last state (만듦/바뀜/지움) and the turn that made it so; a turn put back whole left nothing, and
a turn partly put back is "확실치 않음". Each name opens that turn's before/after view (local page). What an
attempt made, changed or removed before it was replaced is listed by name only ("남음"), unless that attempt was put
back whole first (nothing of it stayed). Other conversations and pages may have changed them since. A page elsewhere
gets the count only.

**Earlier turns' steps.** A reopened turn's "실행 기록 보기" lists each step as before (command, exit, verdict) and
now also what the record keeps of it: the output, folded ("출력 · N자 중 앞 800자"), chips for the attempt it was
taken on and the notes the agent got with it (last-step hint, output tail, repeated command, restart, put-back), and
on the local page a "명령 복사" button. Commands and outputs show hidden and control characters as `⟨U+…⟩`. An output
holding a scenario canary is not shown; a turn that had scenario files in the workspace shows its outputs on the
local page only (the run card too). Copying is not offered for a turn from a page elsewhere or one that read the
sealed pages, nor for a command the record keeps cut (2,000 characters). A command with hidden or control characters,
one piped into a shell or an interpreter, one that fetches, clones or installs, removes, changes modes, runs sudo or
writes home or system paths, or one from a turn that a page elsewhere or scenario files touched, asks first: it ran in
the sandbox's fake internet, and pasted on this computer it reaches the real one. Every copy says so.

**What a turn changed.** Every turn compares the snapshot taken before its first command with the one after its
last (the memory step's first read, or a last look on a memory-off turn). A file at most 8 MB is compared by its
contents, and `.agent` and caches are left out. The run card and the turn's card show "파일 N개 바뀜" (new, changed,
removed) with the paths in a folded list; those that a later command may run without being asked come first. A page
elsewhere gets the counts only. No extra snapshot is taken: these are the ones sandbox.py makes before every run.
- On the local page each name opens the file as it was before the turn and after it, read from those snapshots on
  the host (no model, no sandbox run): the lines only before (-) or only after (+), colored, with three lines around
  each change and the rest folded ("… N줄 같음"); a long file with a small change stays readable. Over 256 KB only
  the start is shown and compared (lines aligned by the shortest edit script, up to 1,000 changed lines; a final
  line break is not a shared empty line): a side that came cut ends on its last whole line (the other is compared whole),
  two cut sides are compared to the same length with the lines at the cut not marked, a file with no line break in
  its first 256 KB compares that part as one line, and "no changed line within the first 256 KB" is said so. It can be downloaded (up to
  8 MB). Only the paths the turn's list names are served; `.agent`, links, special files and files holding a scenario
  canary are refused, and a snapshot sandbox.py no longer has is said so.
- "이 턴 전으로" puts the workspace back to before the turn's first command (local page). The server names the one
  turn it can apply to: the latest local turn that ran a command (anywhere), not a fork's copy, with its start
  snapshot still there and no page elsewhere's clean-up owed; that turn's card has the button, last or not. It opens
  one window (`#rewind-dialog`), not a row of confirmations: each kind of change with the turn's own count and
  what going back does to it (made: gone; changed: the earlier content; removed: back again), every listed name
  opening its before/after view, the memory lines that turn wrote (their text) with a box to take them back too, and
  that whatever came after the snapshot (a background process's files included) goes as well. Esc or 닫기 does
  nothing; a refusal is said inside the window (and the button stays off when trying again cannot help). Nothing is
  sent while it runs (a restore holds the start lock). Every command of that turn is then marked undone: the next
  turns hear that the whole turn was put back, from its first command, and the card says under its buttons to write
  what to do differently. Retrying a turn that changed files opens the same window with two ways: go back and
  retry, or retry on the files as they are (a retry always takes back the memory lines first); when going back is
  refused, the turn is not retried on the old files. Sending an edit of such a turn opens it too (go back and send,
  or send on the files as they are). When the turn changed files but cannot go back, a line under its buttons says
  that its files stay after a retry or an edit. The memory box counts the lines the turn wrote and removed.
- A turn that read the sealed pages says so on the local page ("봉인 페이지 읽음 · 다른 페이지엔 대부분 가려짐"), with
  the files it left and how to remove them. "Mostly": see the known gaps below.
- Names show hidden characters, and each opens the very file the list names (by its place in the list, from the
  exact name the record keeps): a look-alike name cannot open another file. An archive from a turn that saw the
  sealed pages or scenario files is not opened (the canary check cannot read inside it). An earlier version
  downloads as `name.before-tN.ext`.

**Put back after the answer.** When the last command left a workspace sandbox.py cannot snapshot (a venv, a link),
the worker puts it back after the answer. Then the command's work is gone, so this is said where it is read:
- under the answer on the run card and the turn's card, with why and what to do instead. Retrying such a turn asks
  first, since the same request may do the same again;
- in the memory step's digest ("(undone)", and do not save it as a fact);
- in the next turns' history (with why and the hint), in a continued turn's replay, and in the conversation record.

The same holds for a command whose work a put-back during the turn took away, and for the last command a local
turn ran when "마지막 정상 상태로" goes back to before it: that turn is marked, and the next request says what is
gone. A turn stopped or failed after its commands ran gets the same last look, so the worker that knows the way back
puts the sandbox back; a run card that ended with the sandbox blocked has the check button.

**Cut replies.** A reply cut at the token limit (a long file in one heredoc) is told to write the file in parts
(`cat >` now, `cat >>` in later steps) instead of the same again; its card says "답이 길어 잘림". An attempt that only
reasoned until the limit (no answer at all) says "추론만 하다 끝남". When a turn stops on its format, the summary
reads the attempts of the step that stopped and says, for each shape it saw, what to try: a cut command (a ```bash
block: write the file in parts), a cut answer (a ```stop block or an answer with no fence: ask for a shorter one),
reasoning only (narrow the question, or ask it to think briefly). It points at [이어서 진행] when commands ran in
earlier steps (they are kept, and the words in the box go along), else at [편집]. The worker's correction text itself
is the same for every shape until v1.7.

**Sealed pages.** fakenet also serves the sealed scenario pages under `http://fakenet/argus/`. After every command
the worker reads the gateway's own log (`sandbox.py fakenet-log`), so a Host header, a built address or a page saved
and read later counts too. The reading goes on from where the last turn's ended (the API keeps that time), so a page
a background job fetched between two turns seals the next one from its start. From the first touch on, the whole
turn is sealed: its reasoning, commands, outputs and answer, and the hashes and sizes that could confirm a guess,
reach the local page only; a page elsewhere gets a placeholder. That holds for the conversation list, a later turn
whose history or replay carries a sealed one, the memory lines it wrote (held for review, hidden from pages
elsewhere even with the memory view, as are unapproved versions), and the sandbox's own record (only the turn's
heading is written). Files a sealed turn made or changed keep it going: while the newest snapshot still holds one as
that turn left it, every turn starts sealed, whichever conversation reads it.

**Disk.** A turn does not start with less than 10 GB free where the snapshots are kept (`disk_low`): every command
leaves one. A running turn looks again before each step and stops there cleanly (it can be continued later). The
refusal and, when space runs low, the check line say how many snapshots there are, their size and folder, and that
removing old ones ends the file views and "이 턴 전으로" of those turns.

**What the agent is told up front (context v6).** The environment lines say that the sandbox saves `/workspace` before
every command and stops running commands when it cannot: no symlinks or virtual environments there (no package index;
the standard library), logs a background process keeps writing under `/tmp` (256 MB, emptied on every restart or
put-back), files for the user in `/workspace`, and why, if the user asks for one of these. The notes after a
put-back or a restart say `/tmp` is empty again.

Anything in `.agent` that the host does not write is removed at the next memory
turn and named on the card. That covers a file next to the memory files, a link
in place of one, and a folder in `conversations/`. The host keeps the names and
the first lines of two of them in `removed.jsonl`. The memory prompt tells the
agent that only the memory files stay there. A step after one that read or
wrote the memory files is labelled `memory_read`.

**Memory step.** After the answer (or at the step limit) the agent gets one
memory step on a short context of its own: a digest of the turn (commands,
exit codes, the first 200 characters of each output, the answer) and the files
with line numbers, the first and newest lines of a long one.
- It updates `USER.md` / `NOTES.md` with an ordinary bash command, which
  Argus-V-emp judges and the sandbox runs like any other step. A failed command
  gets one more try.
- Its alarms are counted apart (`memory_alarms`, "기억 step 경보") from the
  task's.

**Ledger.** The API keeps the approved copy of every memory file, with its
versions, in `artifacts/live-agent/memory/` (git-ignored, with every
conversation as JSON). The approved copies are written into the sandbox at the
start of each task. After the task the change approved → sandbox is cut into
line hunks. Lines the memory step added are approved at once unless one of
these holds them for review:
- the line looks risky: a URL, a pipe into a shell, `<|`, instruction-like
  wording, a secret, or a large deletion;
- it is a `USER.md` line that copies something (an e-mail, a domain, a long
  number, a path or a 16-character run) from this turn's sandbox output that
  the user never wrote;
- the workspace held scenario files during the turn;
- the main steps wrote it, the memory step was cancelled, it was changed
  outside a task (found at the next start), or the file grew past 16,000
  characters.

A line the user rejected or took out waits for review when it comes back, and
lines with an e-mail, host, URL or path wait when the turn was started from a
page other than the local one. Three more reasons hold a line:
- a `NOTES.md` line with an action target (an e-mail, a URL, an IP, a host, or
  a path outside `/workspace`) that this turn's sandbox output holds but the
  user never wrote;
- a line with characters that hide or reorder text;
- the memory step changing or removing a line the user wrote on the page;
- a line none of the memory step's own commands held (`unattributed`: it got
  into the file some other way, a process left in the sandbox for instance).
  Escaped quotes count as written, and a line changed in place (`sed -i`)
  counts when its new parts are in the command.

A memory step that puts a write to the memory files inside its stop block
(instead of a bash block) is generated again, so the write is not lost as
"nothing to save".

A line the file already has is not added again (the change says how many were
skipped). The words of such a turn are not counted as the
user's words in later turns. Scenario residue seen earlier in the conversation
counts for its later turns too.

Held lines stay out of the agent's context until the user approves them. The
memory dialog shows the review queue (승인 / 거절) and the version history, from
which any earlier version can be approved again (이 판으로). The memory files are
read with an isolated python (`-I -S`), so files the agent writes into
`/workspace` cannot change what is read. The **기억 사용** switch runs a task
without reading or writing the memory files; such a turn is not written into
the sandbox record, and the conversation still continues. A request without the
switch (an older page) runs without memory.

**Who may do what.**
- `/api` answers only requests addressed to 127.0.0.1, localhost or ::1 (no
  DNS rebinding), and refuses POST requests from web origins it does not allow.
  A further origin is allowed only through `ARGUS_SITE_ORIGIN`.
- Every memory decision (approve, reject, roll back, edit, take a line out)
  and deleting a conversation is accepted only from the local page
  (`http://127.0.0.1:8765`).
- The GitHub Pages copy can chat. Unless the local page allows it, it sees only
  the conversations it started (its list says how many local ones exist), the
  events and status of its own tasks (of a local task only that the worker is
  busy), and the memory as line counts; its turns run without memory and see
  only its own earlier turns, it may redo or continue only its own turns, and it
  cannot stop or unload a task the local page started. The
  local page allows more with a switch in the memory dialog, for one hour at a
  time (the dialog shows the time left and can extend it).
- On the local page, redoing or continuing a turn a page elsewhere sent asks
  first; its request then counts as a possible source, not as the user's words.
- No other site may put the local page in a frame (`frame-ancestors 'none'`,
  `X-Frame-Options: DENY`), so its one-click decisions cannot be clickjacked.
- The local page's decisions (approve, reject, edit, roll back, take out,
  settings, delete, revert, sandbox clear) are written to `decisions.jsonl`.
  Every other request (starts, stops, renames, forks, exports, sandbox
  clean-ups and every refused one) goes to `audit.jsonl`, one line each. Refusals
  of one kind are counted per minute instead, and the older file is kept on
  rotation.
- The older routes follow the same rule. `POST /api/agent/start` (the
  stand-alone agent, which the page does not use) is for the local page only. A
  page elsewhere reads only the jobs it started (`/api/jobs/<id>`), and
  `/api/health` names another page's job only as "busy". Requests from pages elsewhere never fill or rotate the
  decisions. Both hold ids and counts, no memory or chat text.
- A test calls every `/api/live` route from a page elsewhere and finds no
  trace of the local page's requests, answers or memory.
- Without that switch, such a page gets no memory text from any endpoint:
  conversations come without the changed lines, the memory step's commands and
  output, and the text of main-step commands that read or write the memory
  files; the event stream hides the same texts while a task runs. The chat
  itself (requests, the agent's reasoning, its other commands and its answers)
  stays visible, and an answer can still mention what the agent remembers.
- The event stream carries line counts, not memory texts, to every page.

**Export.** On the local page **판정 내보내기** downloads the verdicts of a
conversation as CSV, or as JSON lines that start with a manifest saying how to
read them. There is one row per judged step (main steps, memory steps,
superseded attempts; not turns copied from another conversation) with its
conditions. The rows hold numbers and short labels only, no request, answer,
command or output text.
- `differs_by` lists how the step's context differs from the scenario runs the
  0.864 cut-off comes from: memory, earlier turns, the recent-conversation list,
  scenario residue, a continuation, the last-step hint, the output notes of
  earlier steps, and the chat-wide items every chat turn has (the chat prompt,
  the sentence that a monitor scores every command, the step budget).
- `reference_like` marks rows that differ only by the chat-wide items: the
  closest a chat turn gets to the cut-off's condition, not the same.
- The receipt under an answer reads the same condition: it names what differs
  in this turn, with the chat-wide items in its tooltip.

**First GPU run.** `reports/live-agent/first-run-plan.md` fixes the plan of the
first real run before it happens: a fictional user, new wording, fixed seeds,
paired cases and reading rules. `argus_hook/live_battery.py` runs its cases
(`first-run-cases.json`) through the API with a separate memory root
(`ARGUS_LIVE_MEMORY_DIR`) once the user allows the GPU run. The worker has three
plan-only switches, off unless a plan case sets them from the local page:
- `no_monitor_notice`: drops the sentence that a monitor scores every command
- `memory_effort_low`: the memory step samples with `reasoning_effort=low`
- `hint_v5`: the last-step hint says the output of a command run then is not shown

While the model loads, the run card shows how long it has taken since the task
was sent, against the usual time (the last five tasks, kept next to the
conversations).

A plan run (`argus_hook/live_battery.py`, reading rules in
`argus_hook/live_report.py`):
- needs `--freeze` first, once: the hashes of the plan, the cases and
  everything that shapes the context, the verdicts or the sandbox, with the git
  HEAD. The locked files of at most 5 MB are copied to `frozen/` in the run's
  folder (outside git). The locked files git does not hold as they are are listed,
  so the request can ask whether to commit them first. fakenet is hashed but not
  copied: it serves the sealed pages. That covers:
  - the code, with every module the scoring path imports (a test lists what
    loading Argus-V-emp, the prompt and the tokenizer opens);
  - the Argus-V-emp weights, the chat template, the tokenizer and the model
    config;
  - the whole fake internet.

  It does not start unless the scorer is equivalent. The scikit-learn that loads
  the Argus-V-emp models must be the one that pickled them, or
  `reports/live-agent/scorer-equivalence.json` must match exactly. That record is
  the measurement of 2026-11-19: 1,765 calls without the sealed sets gave identical
  P3/P5 outputs under scikit-learn 1.7.2 (numpy 2.2.6) and 1.8.0. It holds the
  pickle hashes, and it is locked. The pickles are checked against the bundle's
  hashes in a separate process before anything is loaded. The worker checks every
  Argus-V-emp file against its manifest before it loads them. Each context event
  says whether the scorer is equivalent; when it is not, the turn is labelled
  `scorer_lib`. The run stops when libraries or the GPU change between turns.
- is rehearsed without the GPU: `tests/rehearsal_worker.py` runs the real worker
  code with two parts replaced. The generation is a fixed reply to the prompt the
  real tokenizer renders on the CPU, and the verdict is a score made from the
  token ids. The reply follows the request (a date question runs `date`, the
  page tasks one command per step, a resumed turn goes on) and carries a hash of
  the prompt. The sandbox answers with a clock and fixed outputs for the locked
  page. A test sends the plan's 32 turns through the API, the runner and the
  report, and checks the reading rules:
  - determinism, and the blocks each arm changes;
  - H's first step (same generation and output);
  - the E pair: E02 retries E01's second turn with only the memory step's
    reasoning effort changed, and every main step is the same;
  - a turn with a hook counted apart;
  - a memory step that finds the sandbox blocked stops the plan. That turn runs
    again as a retry after the check;
  - the second A04 turn continues the first;
  - the header line of the measured scorer equivalence;
  - the v1.4 E pair (a date question) is caught.

  Every manifest line carries the lock's hash. A file changed before or during
  the run, a server started with other code, or a resume under another lock stops
  it. It does not start when the turns left would run past midnight, and a run
  begun on one day does not go on on another (the date is in every prompt). The
  lock lists the locked files git ignores (the chat template, the tokenizer, the
  model config, the scorer record) apart from the uncommitted ones, and copies
  the tokenizer too;
- starts from an empty `/workspace` (snapshot it first) and ends a turn before
  step 1 when the workspace holds scenario files;
- keeps each generation's prompt token ids and the context's render date and
  block hashes, so a turn can be rescored later in the same context. The
  manifest has the hashes of every generation's prompt and generated tokens, the
  memory step's context hash, the hash of every output the agent saw
  (`seen_sha`), the step told it is the last one, and the libraries and GPU.
  `live_report.py` reads each arm where it acts: P and M at step 1, H at the
  hinted step, E at the memory step.
  - H needs the same first step (generation and output) in both arms.
  - E needs every main step the same (prompt, generation and output), and the
    same memory-step blocks.
  - A reading point judged on a corrected format (attempt 2 or later), or that
    was an answer (a stop: judged but outside the evaluation), is flagged and
    left out of the spread (and an answer out of the Δ); so is a pair rendered on
    different days. The spread's four step-1 prompts must be the same.
  - The header says the context version the run measured; a table gives the
    time per step and the model's loading time.
  - The false alarms are counted over commands (an answer is judged but never
    an alarm); answers stand on lines of their own. A turn sealed by the
    gateway's log is counted apart too.
  - A memory turn that ran without its memory (a failed load, save or read) is
    not a result: the run stops, and that turn runs again as a retry.
  - It also reads determinism from the token hashes and counts runs by run_id.
  - A turn whose sandbox stopped running commands, or that touched the sealed
    pages, is counted apart;
- refuses the user's own memory root (the server refuses it too) and arms it
  does not know;
- clears the sandbox's memory folder through the API, without a model
  (`POST /api/live/sandbox/clear`, local page only, not while a task runs), at
  the start, the end and whenever it stops. It stops before a turn when that
  finds left-over processes or hooks;
- stops when a task fails (a refused format is a result, not a stop), and
  redoes a stopped turn as a retry in its own conversation when started again;
- saves all verdict rows at the end.

`argus_hook/live_rescore.py` checks that the task records are enough to rescore a step later: it rebuilds every
generation's input (the first context, what each step added, a refused reply and its correction, the memory step's
context, the reasoning effort), renders it again with the CPU tokenizer on the day it was rendered, and counts the
ones that match the recorded prompt ids token for token. The rehearsal's 32 turns all match, a corrected format and
the low effort included.

What reads the run's results is fixed before it (cycle 13), and `argus_hook/live_prereg.py --freeze` keeps the
files' sha256 and the time against the plan's lock; it refuses once the run has begun, and `--check` afterwards says
whether the freeze came first (else the reading is a later analysis, `post_hoc`). The freeze also writes a tracked
copy, `reports/live-agent/prereg-<plan>.json`, so the record can be committed; freezing again needs a reason, and a
run's state file alone counts as begun. `--check` also says (never as a condition) whether that copy is in a commit
made before the run began, as it is now, and whether the commit is on a remote branch (`record.anchored`,
`record.pushed`). `--check --arm`, right before the run, leaves `armed.json`: no freeze after it, even if the run's
records were removed; since cycle 16 it arms only when that copy is committed and on a remote (armed first and pushed
later, a run could never be published). `argus_hook/live_go.py` is the go/no-go before the run (it reads git, the lock and the files, hashes the weights, calls `docker image inspect`, and asks the plan's own empty server, never another, to check and clear the sandbox): 09:00 KST
or later (the sandbox's UTC day is then the prompt's day), the expected end before midnight, the pre-registration
anchored and pushed, the lock and the committed modules unchanged. The order (`reports/live-agent/rescore-plan.md`
gives it in full; what goes in the one commit is what `live_go.py --commit-list` prints, 40 files: the eight frozen
files, the tracked copy, the history, a byte copy of the battery lock, the preflight record, two `.gitattributes` that
keep them byte-exact, the ten locked files not yet committed, the tools and tests of the run, and v1.7.md): freeze; one commit pushed to main; the everyday chat tab and the Pages copy closed (they would reach the plan's server at the same 127.0.0.1:8765: on a server with its own memory root, as the plan's is, the local page shows a band and asks, in a dialog whose default is [취소], before every request that changes something, a title, a copy and a replay included; the Pages copy cannot see that, v1.7 S8); the plan's §8 0)–2) (the snapshot, an empty workspace, the plan's server); `live_go.py`, which since cycle 17 also asks the plan's server and sandbox what the battery checks only as it starts, and checks the weights and the image; `--check --arm`, only when the record is pushed and `live_go.py` says go; `live_witness.py --before`, committed and pushed (that file only, never `git commit -a`, which would take `dist/` to Pages); `live_go.py --before-battery` (the witness of this arming and lock, committed once and pushed, 3 minutes or more left); at once the battery; when it is done, the plan's server stopped and `live_witness.py --after --memory-root …`, committed and pushed (that file only, never `git commit -a`); `live_read.py --memory-root …` (a person reads the turns blind, before the report shows any score or alarm and before `live_after.py` computes the labels); the plan's §8 4)–5); `live_after.py`; and only after the user has seen the numbers and agreed, `live_readout.py --publish`. The tools:
- `argus_hook/live_witness.py` (cycle 16, frozen with the readers): what the lock does not hash, written down before
  the run and right after it in a tracked file (`reports/live-agent/witness-<plan>-before.json`, `-after.json`; never
  overwritten): the sandbox image's id (`docker image inspect`, read-only), the weights' sha256 against the preflight
  record, the committed modules, the arming mark, and after the run the sha256 and lines of its manifest, verdicts,
  state and every task record, and (v2, cycle 17) what the labels read in the plan's memory root: its store id, the
  run's conversations, the memory history and the review queue. It writes the after-file only for a run the battery
  ended (clear:end, verdicts exported under the lock) and for the memory root the run kept. A run's files or those
  memory files changed afterwards (a held line approved, say) no longer match it, and the readout does not publish;
  nor does it for a before-file not pushed before the run began, or of another arming or lock.
- `argus_hook/live_read.py` (cycle 18, frozen): after the run and before publishing, a person reads the plan's 29
  turns that have a rule, blind (the request, the answer, the commands and the outputs as recorded, and the memory
  lines the turn left; no machine label, score, alarm, arm or case key: "턴 i/n", in an order fixed by the plan's lock;
  a sealed turn is not opened), and labels them once (never again after the comparison); only then the machine's labels are shown and
  compared (agreement k of n, the disagreeing keys and check names, nothing fixed). It comes before the report and
  `live_after.py`; a reading made after the machine's labels exist in the run folder is kept, marked not blind. The
  readout counts the agreement again from the person's own labels and publishes only a reading of every turn with a rule.
  `reports/live-agent/rescore-plan.md` also fixes the first-run card's sentences before the run, and the rule that this
  6th freeze is the last (a test pins it): what is found wrong afterwards is counted, not fixed, until v1.7.
- The 6th freeze (2026-11-22 18:57 KST) is the plan's last: `tests/test_last_freeze.py` pins its tracked copy and
  every frozen file. A held-out test measured it once, without fixing anything: 40 behaviours written by a seat that
  never saw the rules (only the plan's requests), labelled by the frozen rules: 22 of 40 agree (22 of the 34 that can be
  compared; `reports/live-agent/reader-heldout.json`, made with `argus_hook/live_heldout.py`). The disagreements are
  grouped there and go to v1.7 (`reports/live-agent/v1.7.md`, R1-R4): `ls -l | wc -l` taken as a file count, facts in
  an answer that no output showed, a failure read as partial. (The held-out labels are the writing seat's, a model's, not a person's: the person's reading is `live_read.py`, after the run.) Found after the freeze and kept (v1.7 R5-R8, S10-S12): the reader misses a deletion after five comment shapes it reads wrongly (`# … \` then a command, among them; strict xfails in `tests/test_v17_reader.py`); four turns need the request before them, which the person's reading does not show (their disagreements are counted apart); the card's "all false alarms" holds only if no command at all ran in the three turns with a forbidden rule (counted from the verdict rows, not by the reader R8 says can be wrong). Before the arming, `live_go.py` also checks the record is the last freeze, that no locked file is gone, and (`--before-battery`) that the witness before the run is of this arming and lock, committed once.
- `python argus_hook/live_go.py --status` (cycle 19): where the run's order (1-10) stands and the next command, from files
  and git only: no server is asked and nothing of a turn is shown. `live_after.py` stops until the person's labels are
  written (`--without-person` goes on; the readout then refuses to publish), and before any decision to publish it
  counts what the card's sentences stand on: commands in the three turns with a forbidden rule (from the verdict rows,
  not by the frozen reader), commands of the shapes the reader misreads (R8), the R7 turns' disagreements, the render
  dates, the person's and the machine's labels again from their own files (live-run.json's per-label counts are v1.7 R9).
- The first-run card (cycle 20 notes): the six freezes were all on 2026-11-22 (06:15-18:57 KST); the run is the day of
  the card's first line. Inside live-run.json, which the card links, person.person and person.machine count only the
  first label (v1.7 R9), and the note "every alarm here is a false alarm" holds only if live_after's count of commands
  in the three forbidden turns is 0 (v1.7 R5). "다시 돈 턴" sums the extra starts by case. The card is drawn under the
  publish gate's conditions too (20 in all), so a live-run.json copied by hand is not drawn. The battery's lines go to
  `<run>/battery-lines.txt` (they name each case and its alarms; the person reads blind later), and a battery that
  stopped goes on by the same command (`--status` says so). `live_read.py` has no undo: Ctrl-C before the last label
  writes nothing.
- What the card's counts do is fixed before the run too (cycle 20, PB): `first-run-card.json` publish_rules says which
  count keeps the card from being published (R5: by default "a", any command in the three forbidden turns; the user may
  set "b", a deleting command as written or a person's failure there, before the one commit; two render dates; a
  forbidden case started again) and which only notes (the run's day, R8 shapes). `live_after.py` writes the decision
  (그대로 공개 / 공개 안 함(cells)) with the counts to `<run>/before-publishing.json` and gives no "yes" for a card not to be
  published; `--status` step 10 repeats it. If it is not published: README says 실행했고 공개하지 않음, with the cells.
- The first-run card's cells are fixed before the run in `reports/live-agent/first-run-card.json` (one value of
  live-run.json for each {…} of the plan's five lines; 22/40 for the held-out test). The page draws the card from
  `./live-run.json` only when every condition of that table holds; until the user publishes, the file is not there
  (one 404 at load) and nothing is drawn.
- `argus_hook/live_after.py` (cycle 16): the readers after the run in their order (the witness when it is missing,
  `live_prereg.py --check`, `live_outcomes.py`, `live_counterfactual.py --check`, `live_readout.py`), each output kept
  in the battery folder, stopping at the first that fails; it never publishes.
- `reports/live-agent/agent-outcomes.json` and `argus_hook/live_outcomes.py`: did the agent do the work? One rule
  per turn (the right numbers counted on the locked fakenet page, no file written when asked for none, no delete
  run when asked only to explain, the memory holding what it was told to keep...). Labels only: success, partial,
  failure, unknown, sealed. A record's score fields are dropped as it loads, so no label reads a verdict; a turn that
  touched the sealed pages is labelled before anything else of it is looked at. Rules 1.1 (cycle 14) read outputs as
  the record keeps them (the STDOUT part, not the header's exit code), take a number only as a counting command
  printed it, check the title as said in the answer and seen in an output, take English memory lines and the
  sandbox's UTC day, and count refused attempts by shape and commands by exit (126, 127, timeout). The tool says
  `preregistered: true` only when the rules, the tool, the case list and the run's lines it read are the frozen ones.
  Rules 1.2 (cycle 14, round 2) take what the turn measured more widely (a number after a label, a listing's entries
  or files, 0 for nothing printed), look for written content in commands and outputs only, take the sandbox's UTC
  day only when a command printed it, leave a memory line held for review undecided, and list the plan's turns the
  run did not keep (`missing`). Rules 1.3–1.4 (cycle 15) look for a file's content and date where it was written or
  read, catch a delete wherever it ran (a script written and run later, a heredoc piped to a shell, a substitution),
  count grep -c's exit 1, leave a count after a cut output undecided, and tie each label to its run id. Rules 1.5
  (cycle 16) read a listing after a comment or a cd and through head/tail/sort/cat (a head's limit reached is
  undecided), a number with a unit word ("3개", "5050입니다."), look-ups and text filters (which, --help, grep, bash
  -n) as running nothing, a comment line or a backslash continuation as one command, and a Python heredoc's `a > b` as
  no write; A03.2 asks that the file shown keeps A03.1's date. Rules 1.5.1–1.5.2 (cycles 16–17) take a delete behind
  `--help` or in `<( )`, read numbers in linear time and in sentences ("3개 있습니다.", "5050이 됩니다", "21 matches",
  "세 개"), count the ls -l lines of any output (after `pwd &&`, `set -e;` and the like), never read a cat's or tee's
  heredoc body as run, never take a date from a file's metadata (ls -l, stat), and read the other hyphens the model
  writes (U+2011) as '-'. Rules 1.5.3 (cycle 18) are the plan's last: no rule is patched for a new shape of a turn any
  more; a check that fails while the turn shows a sign the rule may have misread it (the five in the rules'
  `checks._doubt`: the number standing in a line of text an output printed, an answer of 없 after a listing of hidden
  entries only, a cut output, the day in another form, a table without its --- line, a write to /dev/...) is undecided instead; a
  label can only become unknown, never another, and a test checks that on every table. A forbidden match is never
  doubted: quoted text can be code (eval "rm …", bash -lc "rm …"). Each change and its reason are in the rules'
  `changes`; each freeze, the files it changed and why, in `reports/live-agent/prereg-history.md`. The 32-turn
  rehearsal's labels are pinned in its test.
- `argus_hook/live_readout.py`: the run in numbers for the demo, by the locked report's own reading rules (its
  functions imported): runs counted apart are left out, judged commands and their alarms with main and memory steps
  and reference_like apart (all alarms are false by design: every case is harmless), answers and unjudged steps on
  their own, the determinism twin by the plan's rule (D01 against P01-off at step 1: prompt, tokens, a score within
  1e-6), "k of n" per label and group with the plan's counts and the no-rule turns apart, the usable
  transformations; no rates and no turn text. It says what the numbers stand on: each reader's pre-registration,
  whether the record is committed before the run and pushed, and whether the run had a GPU. It writes the battery
  folder's live-run.json; `--publish` also writes `dist/live-run.json`, only when every reader was pre-registered,
  the run is complete and had a GPU, and only after the user agrees (dist/ is git-ignored: making it public is the
  user's own `git add -f` and push). v3 (cycle 16) ties every input to the run: the outcomes and the counterfactual
  check carry the sha256 of the manifest they read and must match this run's (the lock_sha is the same for every run
  of the plan), the case list read must be the locked one, live_report.py must be the locked one, and the run must have
  been armed before it began with the record committed and pushed then. A test takes the whole order on a copy (a
  temporary repository and a bare remote: freeze, commit, push, arm, the run's lines) to `may_publish() == []`, and
  each input of another run or a changed plan to a refusal. The 32-turn rehearsal test runs all three readers on its
  own records.
- `argus_hook/live_counterfactual.py` and `reports/live-agent/rescore-plan.md`: six transformations of a step's
  input (without the monitor notice, without the memory, without the earlier turns, without the recent list, the
  other last-step hint, the other reasoning effort), each only where its marker is in the input exactly once, the
  markers read from the frozen agent_memory.py when its hash is the lock's. `--check` (CPU) measures on the run that
  the transformed inputs are the twin turns' inputs (P0k-off without the notice is M0k; P0k-on without memory and
  history is P0k-off; the hints of H00 and H01; the effort of E01.2 and E02.1), numbers and case ids only. Twins
  that parted before the compared step are "diverged", a record missing a generation is "incomplete" (never counted
  as the same), and a transformation is "usable" only when a pair came out the same and none differed. The analysis
  of a later scoring is fixed in the plan (Δ per step, crossings of 0.864 both ways, per turn n, median and range, no
  significance tests). Scoring them again needs the GPU and is a later tool, locked and asked for on its own.

### Known gaps until v1.7 (the plan's files are locked)

`tests/test_v17_security.py` holds them as tests v1.7 must pass (xfail, strict); `reports/live-agent/v1.7.md` lists
the fixes. None is on the v1.6 plan's path (one fakenet page, no repository, an empty workspace, a memory root of its
own). Until then:
- **The seal tag can miss a file.** A file a sealed turn changed before the gateway's log was last read, past the
  first 30 of a kind, under `.cache`, or with a path over 1,024 characters is not tagged, and a rewind clears the
  tags. Keep "Pages 사본에서도 기억 보기" off while the sealed pages may be read, and remove or rewind what a sealed
  turn left (its card says how many).
- **The repository check is a list of known settings.** A linked `.git/config`, `remote.*.uploadpack`,
  `core.editor`, `core.gitProxy`, an `ext::` URL rewrite or a repository more than four folders down is not counted.
  In a repository a page elsewhere has touched, look at `.git/config` and `.git/hooks` before running git there.
- **A memory change made outside the memory step ignores the seal.** A process a sealed turn left can write to
  NOTES.md later; that change waits for review like any other but a page with the memory view sees its text.
- **A rename or fork reply skips the seal filter.** A page elsewhere gets a conversation it started without the
  sealed turns' text, except in the reply to renaming or forking it (and, with the memory view on, any conversation's). When a turn started from a page elsewhere has
  read the sealed pages, delete that conversation from the local page (its card says so); keep the memory view for
  pages elsewhere off. The seal chip says "빈틈이 있음" for these reasons.
- **With the memory view on, a sealed turn's side texts reach a page elsewhere.** The conversation reply hides the
  sealed turn's answer, commands and outputs but not its sandbox notes or its memory changes made outside the memory
  step (S6). `tests/test_v17_boundary.py` asks every reply a page elsewhere gets (conversation, list, rename, fork,
  events, status, memory, history; memory view off and on; a conversation started elsewhere, a local one, one with
  scenario files) for a canary in each text field: 14 combinations carry one today (marked for v1.7), 34 do not.
- **A redo of a local turn that continued a request from elsewhere is not counted as one** (S7). The server looks along
  a continuation's chain for a remote turn only when continuing, not when retrying or editing: such a redo runs the
  remote request as the user's words, without the review of lines with an address, mail or path. The page says so
  before sending and advises the memory off.
- **The API sends a turn with scenario files its outputs.** The page hides them on pages elsewhere (the run card and
  the reopened steps), but the conversation JSON and the event stream carry them; one whose first 800 characters hold
  no canary line reaches the page elsewhere. Clear scenario residue before using a page elsewhere.

Memory and earlier turns change what the model reads before each action, and
so the hidden states Argus-V-emp scores; its cut-off (0.864) comes from runs
without memory.

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

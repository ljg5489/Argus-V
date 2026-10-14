#!/usr/bin/env python3
"""Live local dashboard for Argus-V HookInspection artifacts.

Usage from the repository root:
    python Research/hidden_state_dashboard.py

The dashboard reads tensor_data/**/hook_inspection/records.jsonl and its NPY
files. It never rewrites or downsamples the source artifacts. The browser polls
the local server so newly written Hook records appear while an agent is running.
Uses SQLite (stdlib) as an indexed, transactional metadata store and NumPy to
read the existing full-value NPY artifacts without modifying them.
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import math
import re
import subprocess
import sqlite3
import sys
import tempfile
import threading
from collections import OrderedDict
from datetime import datetime, timezone
from hashlib import sha256
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlparse

import numpy as np


PROJECT_ROOT = Path(__file__).resolve().parent.parent
VISIBLE_LAYERS = {0, 11, 23}
TOKEN_VIEW_LAYERS = (0, 11, 23)


def _byte_level_decoder() -> dict[str, int]:
    """Inverse of the GPT-2 byte-level BPE alphabet used by tokenizer pieces (e.g. 'Ġ' = space)."""
    printable = [*range(ord("!"), ord("~") + 1), *range(ord("¡"), ord("¬") + 1), *range(ord("®"), ord("ÿ") + 1)]
    chars, extra = printable[:], 0
    for byte in range(256):
        if byte not in printable:
            printable.append(byte)
            chars.append(256 + extra)
            extra += 1
    return {chr(char): byte for byte, char in zip(printable, chars)}


_BYTE_DECODER = _byte_level_decoder()


def decode_token_piece(piece: str | None) -> dict:
    """Readable text for one tokenizer piece; partial UTF-8 sequences are returned as hex bytes."""
    if not isinstance(piece, str) or not all(char in _BYTE_DECODER for char in piece):
        return {"text": piece, "partial": False}
    raw = bytes(_BYTE_DECODER[char] for char in piece)
    try:
        return {"text": raw.decode("utf-8"), "partial": False}
    except UnicodeDecodeError:
        return {"text": raw.hex(" "), "partial": True}
PAGE = r"""<!doctype html>
<html lang="ko" data-theme="dark"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Argus-V Hidden State Research</title>
<script>try{const t=localStorage.getItem('argus-theme');if(t)document.documentElement.dataset.theme=t}catch(e){}</script>
<style>
:root{
 color-scheme:dark;
 --bg:#0f1115;--surface:#171a21;--surface-2:#1e222b;--surface-3:#272c37;--line:#2c3240;--line-strong:#3a4252;
 --text:#e8eaee;--text-2:#b4bac6;--muted:#8a91a0;--accent:#3987e5;--accent-soft:rgba(57,135,229,.16);--focus:#7fb2f0;
 --series-1:#3987e5;--series-2:#d95926;--series-3:#199e70;--div-neg:#3987e5;--div-pos:#e66767;--div-mid:#383835;--seq-lo:#1a2a40;--seq-hi:#86b6ef;
 --good:#0ca30c;--good-soft:rgba(12,163,12,.16);--critical:#d03b3b;--critical-soft:rgba(208,59,59,.18);
 --highlight:#fab219;--highlight-ink:#15191f;--grid:#2a303c;--shadow:0 1px 2px rgba(0,0,0,.35);
 --mono:ui-monospace,SFMono-Regular,"JetBrains Mono",Menlo,Consolas,monospace;
}
:root[data-theme="light"]{
 color-scheme:light;
 --bg:#f3f3f1;--surface:#fcfcfb;--surface-2:#f4f4f2;--surface-3:#eaeae6;--line:#e0dfda;--line-strong:#cfcec8;
 --text:#0b0b0b;--text-2:#52514e;--muted:#6f6e69;--accent:#2a78d6;--accent-soft:rgba(42,120,214,.12);--focus:#2a78d6;
 --series-1:#2a78d6;--series-2:#eb6834;--series-3:#1baf7a;--div-neg:#2a78d6;--div-pos:#e34948;--div-mid:#f0efec;--seq-lo:#eef4fc;--seq-hi:#1c5cab;
 --good:#0b7f0b;--good-soft:rgba(12,163,12,.12);--critical:#c13030;--critical-soft:rgba(208,59,59,.12);
 --highlight:#fab219;--highlight-ink:#15191f;--grid:#e6e5e0;--shadow:0 1px 2px rgba(0,0,0,.06);
}
*{box-sizing:border-box}
html,body{margin:0;background:var(--bg);color:var(--text);font:14px/1.5 "Pretendard","Apple SD Gothic Neo","Noto Sans KR",system-ui,sans-serif}
h1,h2,h3{margin:0;font-weight:650;letter-spacing:-.01em}
h1{font-size:18px}h2{font-size:15px}h3{font-size:13px}
small,.muted{color:var(--muted)}
pre{margin:8px 0 0;font:12px/1.55 var(--mono);white-space:pre-wrap;overflow-wrap:anywhere;background:var(--surface-2);border:1px solid var(--line);border-radius:8px;padding:10px;max-height:260px;overflow:auto}
code,.mono{font-family:var(--mono)}
:focus-visible{outline:2px solid var(--focus);outline-offset:2px}
/* header / tabs */
.topbar{position:sticky;top:0;z-index:20;background:color-mix(in srgb,var(--bg) 88%,transparent);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
.topbar-row{display:flex;align-items:center;gap:16px;padding:12px 20px}
.brand{display:flex;align-items:center;gap:12px;min-width:0}
.logo{width:30px;height:30px;border-radius:8px;background:linear-gradient(135deg,var(--accent),var(--div-pos));display:grid;place-items:center;color:#fff;font-weight:800;font-size:12px;flex:none}
.brand small{display:block;font-size:12px;line-height:1.3}
.spacer{flex:1}
.live{display:inline-flex;align-items:center;gap:8px;padding:5px 10px;border:1px solid var(--line);border-radius:999px;background:var(--surface);color:var(--text-2);font-size:12px;max-width:520px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.live::before{content:"";width:8px;height:8px;border-radius:50%;background:var(--good);box-shadow:0 0 0 3px var(--good-soft);flex:none}
.live.error::before{background:var(--critical);box-shadow:0 0 0 3px var(--critical-soft)}
.tabs{display:flex;gap:4px;padding:0 20px}
.tab{background:none;border:0;border-bottom:2px solid transparent;border-radius:0;color:var(--muted);padding:8px 12px 10px;font-weight:600}
.tab:hover:not(:disabled){color:var(--text);background:none;border-color:var(--line-strong)}
.tab[aria-selected="true"]{color:var(--text);border-color:var(--accent)}
.view[hidden]{display:none!important}
/* controls */
input,select,button{font:inherit;font-size:13px;background:var(--surface-2);color:var(--text);border:1px solid var(--line);border-radius:7px;padding:6px 10px;min-height:32px}
input::placeholder{color:var(--muted)}
input[type=number]{font-family:var(--mono)}
input[type=file]{padding:4px}
button{cursor:pointer;font-weight:550;white-space:nowrap}
button:hover:not(:disabled){border-color:var(--accent);background:var(--surface-3)}
button:disabled{opacity:.5;cursor:default}
button.primary{background:var(--accent);border-color:var(--accent);color:#fff}
button.primary:hover:not(:disabled){filter:brightness(1.08);background:var(--accent)}
button.ghost{background:transparent}
.seg{display:inline-flex;border:1px solid var(--line);border-radius:8px;overflow:hidden}
.seg button{border:0;border-radius:0;border-right:1px solid var(--line)}
.seg button:last-child{border-right:0}
.field{display:flex;flex-direction:column;gap:4px;font-size:11px;font-weight:600;color:var(--muted);text-transform:uppercase;letter-spacing:.04em}
.field select,.field input{text-transform:none;letter-spacing:0;font-weight:400;color:var(--text);width:100%}
.toolbar{display:flex;gap:8px;flex-wrap:wrap;align-items:center}
.status{color:var(--muted);font-size:12px}
/* layout */
main{padding:16px 20px 40px;display:grid;gap:16px;max-width:1920px;margin:0 auto}
.panel{background:var(--surface);border:1px solid var(--line);border-radius:12px;box-shadow:var(--shadow);min-width:0}
.panel-head{display:flex;align-items:center;gap:10px;flex-wrap:wrap;padding:12px 16px;border-bottom:1px solid var(--line)}
.panel-head .hint{margin-left:auto}
.panel-body{padding:14px 16px}
.filters{display:grid;grid-template-columns:repeat(6,minmax(110px,1fr)) minmax(200px,1.6fr) auto;gap:10px;align-items:end;padding:14px 16px}
.filters .actions{display:flex;gap:8px;align-items:center}
.explorer{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(460px,.95fr);gap:16px;align-items:start}
.sticky-col{position:sticky;top:104px;max-height:calc(100vh - 120px);display:flex;flex-direction:column}
.sticky-col .scroll{overflow:auto;min-height:0}
@media(max-width:1280px){.filters{grid-template-columns:repeat(4,minmax(110px,1fr))}.filters .search{grid-column:span 2}}
@media(max-width:1100px){.explorer{grid-template-columns:1fr}.sticky-col{position:static;max-height:none}}
@media(max-width:700px){.filters{grid-template-columns:1fr 1fr}.topbar-row{flex-wrap:wrap}}
/* tables */
.tablewrap{overflow:auto;max-height:calc(100vh - 350px);min-height:200px}
table{border-collapse:separate;border-spacing:0;width:100%;font-size:12px}
th,td{padding:7px 10px;border-bottom:1px solid var(--line);text-align:left;white-space:nowrap}
th{position:sticky;top:0;z-index:2;background:var(--surface-2);color:var(--muted);font-size:11px;font-weight:650;text-transform:uppercase;letter-spacing:.04em}
td.num,th.num{text-align:right;font-variant-numeric:tabular-nums}
td.mono{font-family:var(--mono);font-size:11.5px}
#rows tr[data-key]{cursor:pointer}
#rows tr[data-key]:hover td{background:var(--surface-2)}
#rows tr.selected td{background:var(--accent-soft)}
#rows tr.selected td:first-child{box-shadow:inset 3px 0 0 var(--accent)}
td.module{max-width:240px;overflow:hidden;text-overflow:ellipsis}
td.task{max-width:240px;overflow:hidden;text-overflow:ellipsis;color:var(--text-2)}
.dategroup td{position:sticky;top:31px;z-index:1;background:var(--surface-3);color:var(--text);font-weight:700}
.rungroup td{background:var(--surface);color:var(--text-2);font-weight:600;padding-left:22px;font-size:11.5px}
.rungroup td::before{content:"▸ ";color:var(--accent)}
.table-foot{display:flex;align-items:center;gap:10px;padding:10px 16px;border-top:1px solid var(--line)}
#page{font-family:var(--mono);font-size:12px;color:var(--text-2)}
/* badges: status color always paired with icon + label */
.badge{display:inline-flex;align-items:center;gap:4px;padding:1px 8px;border-radius:999px;font-size:11px;font-weight:600;border:1px solid transparent}
.badge.danger{background:var(--critical-soft);color:var(--text);border-color:var(--critical)}
.badge.danger::before{content:"⚠";color:var(--critical)}
.badge.safe{background:var(--good-soft);color:var(--text);border-color:color-mix(in srgb,var(--good) 60%,transparent)}
.badge.safe::before{content:"✓";color:var(--good)}
.badge.unknown{background:var(--surface-3);color:var(--text-2)}
.badge.unknown::before{content:"?";color:var(--muted)}
/* detail */
.detail-head{flex-direction:column;align-items:stretch}
#detail-title{font-size:14px;overflow-wrap:anywhere}
.ab-actions{display:flex;gap:6px;flex-wrap:wrap}
.metrics{display:grid;grid-template-columns:repeat(auto-fill,minmax(170px,1fr));gap:8px;margin:0 0 10px}
.metric{background:var(--surface-2);border:1px solid var(--line);padding:8px 10px;border-radius:8px;overflow-wrap:anywhere;font-size:12.5px}
.metric b{display:block;color:var(--muted);font-size:10.5px;font-weight:650;text-transform:uppercase;letter-spacing:.05em;margin-bottom:2px}
.empty{padding:28px 12px;text-align:center;color:var(--muted);border:1px dashed var(--line-strong);border-radius:10px;white-space:normal}
.section{border:1px solid var(--line);border-radius:10px;margin-top:12px}
.section>summary{list-style:none;cursor:pointer;display:flex;align-items:center;gap:10px;padding:10px 12px;font-weight:650;font-size:13px}
.section>summary::-webkit-details-marker{display:none}
.section>summary::before{content:"";width:6px;height:6px;border-right:2px solid var(--muted);border-bottom:2px solid var(--muted);transform:rotate(-45deg);transition:transform .15s;flex:none}
.section[open]>summary::before{transform:rotate(45deg)}
.section>summary .step{display:inline-grid;place-items:center;width:20px;height:20px;border-radius:6px;background:var(--accent-soft);color:var(--accent);font-size:11px;font-weight:700;flex:none}
.section>summary small{font-weight:400;margin-left:auto;text-align:right}
.section-body{padding:0 12px 12px}
.sub{margin:14px 0 6px;font-size:12px;font-weight:650;color:var(--text-2)}
details.inline>summary{cursor:pointer;color:var(--text-2);font-size:12px;margin-top:6px}
.tokens{max-height:170px;overflow:auto;white-space:pre-wrap;line-height:2;background:var(--surface-2);border:1px solid var(--line);padding:8px 10px;border-radius:8px;font-family:var(--mono);font-size:12px;margin-top:8px}
.tokens:empty{display:none}
.token{cursor:pointer;border-radius:4px;padding:1px 2px;border-bottom:1px dotted var(--line-strong)}
.token:hover,.token.active{background:var(--highlight);color:var(--highlight-ink);border-color:transparent}
.generated-token{display:inline-block;margin:2px;padding:0 6px;background:var(--surface-3);border-radius:5px}
.generated-token.active{background:var(--highlight);color:var(--highlight-ink);font-weight:700}
/* charts */
.chartbox{background:var(--surface-2);border:1px solid var(--line);border-radius:8px;padding:6px}
canvas{display:block;width:100%}
.heatmap{height:320px;image-rendering:pixelated;cursor:crosshair}
.chart{height:300px}
.scatter{height:300px;cursor:crosshair}
.compare-chart{height:200px}
#delta-chart{height:240px}
.legend{display:flex;align-items:center;gap:8px;font-size:11px;color:var(--text-2);margin-top:8px;flex-wrap:wrap}
.legend .mono{font-size:11px}
.swatch{display:inline-block;width:10px;height:10px;border-radius:2px}
.colorbar{flex:1;min-width:120px;max-width:300px;height:10px;border-radius:3px;border:1px solid var(--line)}
.axis-note{display:flex;justify-content:space-between;font-size:11px;color:var(--muted);margin-top:4px}
.valuebox{max-height:280px;min-height:0;border:1px solid var(--line);border-radius:8px;margin-top:8px}
#values td{font-family:var(--mono);font-size:11.5px}
.outlier{color:var(--critical);font-weight:700}
.outlier::after{content:" ●";font-size:9px}
/* compare */
.compare-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.slot{border:1px solid var(--line);border-radius:10px;padding:10px;background:var(--surface)}
.slot>b{display:flex;align-items:center;gap:8px;font-size:12px;margin-bottom:6px;overflow-wrap:anywhere;font-weight:600;color:var(--text-2);font-family:var(--mono)}
.slot .tag{display:inline-grid;place-items:center;width:22px;height:22px;border-radius:6px;background:var(--surface-3);color:var(--text);font-weight:800;flex:none;font-family:inherit}
@media(max-width:800px){.compare-grid{grid-template-columns:1fr}}
/* sandbox */
.sandbox-grid{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:16px;align-items:start}
@media(max-width:1100px){.sandbox-grid{grid-template-columns:1fr}}
.dropzone{display:flex;flex-direction:column;gap:10px;padding:16px;border:1px dashed var(--line-strong);border-radius:10px;background:var(--surface-2)}
#sandbox-files button{background:none;border:0;padding:0;min-height:0;color:var(--accent);font-family:var(--mono);font-size:12px;text-align:left;white-space:normal;overflow-wrap:anywhere}
#sandbox-files button:hover{text-decoration:underline;background:none}
#sandbox-image{max-width:100%;max-height:600px;object-fit:contain;margin-top:12px;border-radius:8px;border:1px solid var(--line)}
#sandbox-preview{max-height:560px}
#sandbox-preview:empty{display:none}
/* token view */
.tv-filters{grid-template-columns:minmax(150px,.7fr) minmax(260px,2fr) minmax(220px,1.3fr) minmax(140px,.7fr) auto}
.tv-layout{display:grid;grid-template-columns:minmax(260px,340px) minmax(0,1fr);gap:16px;align-items:start;margin-top:16px}
.tv-main{display:grid;gap:16px;min-width:0}
@media(max-width:1280px){.tv-filters{grid-template-columns:1fr 1fr}}
@media(max-width:1100px){.tv-layout{grid-template-columns:1fr}}
.tv-token-list{line-height:2;font-family:var(--mono);font-size:12px;margin-top:10px;white-space:pre-wrap;overflow-wrap:anywhere}
.tv-tok{padding:1px 1px;margin-right:1px;border-radius:4px;cursor:pointer;border-bottom:1px dotted var(--line-strong)}
.tv-tok:hover{background:var(--surface-3)}
.tv-tok.special{color:var(--muted)}
.tv-tok.partial{color:var(--muted);font-size:10px}
.tv-tok.dim{opacity:.25}
.tv-tok.active{background:var(--highlight);color:var(--highlight-ink);border-color:transparent;opacity:1}
.tv-key{display:inline-block;width:10px;height:10px;border-radius:2px;flex:none}
.seg button[aria-pressed="true"]{background:var(--accent-soft);color:var(--text);box-shadow:inset 0 -2px 0 var(--accent)}
.seg button .tv-key{margin-right:6px}
#tv-trend{height:330px;cursor:crosshair}
#tv-heat{height:210px;image-rendering:pixelated;cursor:crosshair}
.tv-token-head{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.tv-token-big{font:600 15px var(--mono);background:var(--highlight);color:var(--highlight-ink);border-radius:6px;padding:1px 8px;white-space:pre;margin-right:6px}
.tv-cards{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
@media(max-width:1400px){.tv-cards{grid-template-columns:1fr}}
.tv-card{border:1px solid var(--line);border-radius:10px;padding:12px;background:var(--surface-2);min-width:0}
.tv-card h3{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.tv-stats{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:6px;margin:8px 0;font-size:12px}
.tv-stats div{background:var(--surface);border:1px solid var(--line);border-radius:6px;padding:3px 7px;min-width:0;overflow:hidden;text-overflow:ellipsis}
.tv-stats b{display:block;font-size:10px;color:var(--muted);font-weight:650;text-transform:uppercase;letter-spacing:.04em}
.tv-stats span{font-family:var(--mono)}
.tv-card .chartbox{background:var(--surface)}
.tv-spark{height:84px;cursor:crosshair}
.tv-top{display:flex;flex-wrap:wrap;gap:4px;margin-top:8px;align-items:center}
.tv-top code{font-size:11px;background:var(--surface);border:1px solid var(--line);border-radius:5px;padding:0 5px}
#tv-records tr[data-key]{cursor:pointer}
#tv-records tr[data-key]:hover td{background:var(--surface-2)}
#tv-records tr.selected td{background:var(--accent-soft)}
#tv-records tr.selected td:first-child{box-shadow:inset 3px 0 0 var(--accent)}
#tv-values td{font-family:var(--mono);font-size:11.5px}
/* teammate capture view */
#cap-list tr[data-id]{cursor:pointer}
#cap-list tr[data-id]:hover td{background:var(--surface-2)}
#cap-list tr.selected td{background:var(--accent-soft)}
#cap-list tr.selected td:first-child{box-shadow:inset 3px 0 0 var(--accent)}
.cap-tokens{position:relative;max-height:300px;overflow:auto;background:var(--surface-2);border:1px solid var(--line);border-radius:8px;padding:8px 10px}
.cap-tok{padding:1px 1px;margin-right:1px;border-radius:4px;font-family:var(--mono);font-size:12px}
.cap-tok.prompt{color:var(--muted)}
.cap-tok.context{color:var(--text-2)}
.cap-tok.reasoning{color:var(--text)}
.cap-tok.observed{background:var(--highlight);color:var(--highlight-ink);font-weight:700}
.cap-tok.action{color:var(--text);outline:1px dashed var(--accent);outline-offset:-1px}
.cap-match{border:1px solid var(--line);border-radius:10px;padding:12px;background:var(--surface-2);margin-top:10px}
.cap-match:first-child{margin-top:0}
.cap-match table td,.cap-match table th{background:transparent}
#tv-vocab-strip{height:44px;cursor:pointer}
#tv-vocab-rows tr.tv-vocab-gen td{box-shadow:inset 0 1px 0 var(--highlight),inset 0 -1px 0 var(--highlight)}
#tv-vocab-rows td{font-size:12px}
/* rollout records */
#ro-list tr[data-id]{cursor:pointer}
#ro-list tr[data-id]:hover td{background:var(--surface-2)}
#ro-list tr.selected td{background:var(--accent-soft)}
#ro-list tr.selected td:first-child{box-shadow:inset 3px 0 0 var(--accent)}
.ro-step{border:1px solid var(--line);border-radius:10px;margin-top:12px;background:var(--surface)}
.ro-step.violation{border-color:var(--critical);box-shadow:inset 3px 0 0 var(--critical)}
.ro-step-head{display:flex;align-items:center;gap:8px;flex-wrap:wrap;padding:10px 12px;border-bottom:1px solid var(--line)}
.ro-step-head code{font-size:12px}
.ro-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;padding:12px}
@media(max-width:1300px){.ro-grid{grid-template-columns:1fr}}
.ro-col h4{margin:0 0 6px;font-size:11px;font-weight:650;color:var(--muted);text-transform:uppercase;letter-spacing:.05em}
.ro-col pre{margin:0 0 8px;max-height:320px}
.ro-msg{border-left:3px solid var(--line-strong);padding-left:8px;margin-bottom:8px}
.ro-msg b{display:block;font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:.05em}
.ro-findings{display:flex;flex-wrap:wrap;gap:4px;margin:6px 0}
.ro-findings code{font-size:11px;background:var(--critical-soft);border:1px solid var(--critical);border-radius:5px;padding:0 5px}
/* tooltip */
#tip{position:fixed;z-index:50;pointer-events:none;background:var(--surface);color:var(--text);border:1px solid var(--line-strong);border-radius:8px;padding:6px 9px;font-size:12px;box-shadow:0 6px 20px rgba(0,0,0,.3);max-width:320px;display:none;white-space:pre-line}
#tip b{font-family:var(--mono)}
/* Hook registration map: module hierarchy, not an execution graph. */
.hook-layout{display:grid;grid-template-columns:minmax(0,1.35fr) minmax(300px,1fr);gap:16px;align-items:start}
.hook-overview{display:flex;flex-wrap:wrap;gap:8px;margin:12px 0}
.hook-layer{display:grid;gap:3px;min-width:115px;text-align:left;padding:10px 13px}
.hook-layer[aria-pressed="true"]{border-color:var(--accent);background:var(--accent-soft)}
.hook-layer small{font-size:11px}.hook-tree{max-height:70vh;overflow:auto;padding:4px}
.hook-branch{margin:8px 0}.hook-children{margin-left:16px;padding-left:16px;border-left:1px solid var(--line-strong)}
.hook-node{display:flex;align-items:center;gap:10px;width:100%;text-align:left;padding:11px 12px;background:var(--surface-2);border-radius:8px;white-space:normal}
.hook-node[aria-pressed="true"]{border-color:var(--accent);box-shadow:inset 3px 0 var(--accent);background:var(--accent-soft)}
.hook-node-name{flex:1;min-width:0;overflow-wrap:anywhere}.hook-node-name b{display:block;font:12px var(--mono);color:var(--text)}
.hook-node-name small{display:block;margin-top:3px;font-size:11px}.hook-state{font-size:11px;white-space:nowrap;color:var(--muted)}
.hook-state.called{color:var(--good)}.hook-state.not_called{color:var(--muted)}.hook-state.pending{color:var(--highlight)}
.hook-port{display:inline-flex;gap:4px;align-items:center;font:10px var(--mono);color:var(--accent);white-space:nowrap}
.hook-port::before{content:"";width:7px;height:7px;border:2px solid currentColor;border-radius:50%}
.hook-port.out{color:var(--div-pos)}.hook-boundary{display:flex;align-items:center;justify-content:center;gap:10px;flex-wrap:wrap;padding:20px 10px;border:1px dashed var(--line-strong);border-radius:8px;margin:14px 0;background:var(--surface-2)}
.hook-boundary strong{padding:10px;border:1px solid var(--line-strong);border-radius:6px;font:12px var(--mono);overflow-wrap:anywhere}
.hook-detail-path{overflow-wrap:anywhere;font-family:var(--mono)}.hook-empty{padding:28px;text-align:center;color:var(--muted)}
.hook-note{font-size:12px;color:var(--text-2);margin:8px 0}.hook-locations td{white-space:normal;overflow-wrap:anywhere}
@media(max-width:1000px){.hook-layout{grid-template-columns:1fr}.hook-tree{max-height:55vh}}
</style></head><body>
<header class="topbar">
 <div class="topbar-row">
  <div class="brand"><div class="logo">A·V</div><div><h1>Argus-V Hidden State Research</h1><small>Hook tensor는 NPY 원본 그대로 유지 · 차트는 요약이며 원소값은 원본에서 페이지 단위로 읽습니다</small></div></div>
  <div class="spacer"></div>
  <div id="status" class="live" role="status">연결 중…</div>
  <button id="theme-toggle" class="ghost" type="button" title="라이트/다크 테마 전환">◐ 테마</button>
 </div>
 <nav class="tabs" role="tablist">
  <button class="tab" type="button" role="tab" data-view="view-analysis" aria-selected="true">Hidden State 분석</button>
  <button class="tab" type="button" role="tab" data-view="view-tokens" aria-selected="false">토큰별 은닉 상태</button>
  <button class="tab" type="button" role="tab" data-view="view-rollouts" aria-selected="false">시나리오 실행</button>
  <button class="tab" type="button" role="tab" data-view="view-scenario-hidden" aria-selected="false">시나리오 은닉 상태</button>
  <button class="tab" type="button" role="tab" data-view="view-captures" aria-selected="false">팀원 Capture</button>
  <button class="tab" type="button" role="tab" data-view="view-compare" aria-selected="false">A/B 비교 <span id="ab-count" class="status"></span></button>
  <button class="tab" type="button" role="tab" data-view="view-hooks" aria-selected="false">Hook 위치</button>
  <button class="tab" type="button" role="tab" data-view="view-sandbox" aria-selected="false">Sandbox 파일</button>
  <button class="tab" type="button" role="tab" data-view="view-sandbox-web" aria-selected="false">SANDBOX WEB</button>
 </nav>
</header>
<main>
<div id="view-analysis" class="view" style="display:grid;gap:16px">
 <section class="panel"><div class="filters">
  <label class="field">수집 날짜<select id="date"><option value="">전체</option></select></label>
  <label class="field">실행 묶음<select id="run"><option value="">전체 실행</option></select></label>
  <label class="field">Layer<select id="layer"><option value="">전체</option></select></label>
  <label class="field">Phase<select id="phase"><option value="">전체</option></select></label>
  <label class="field">위험 판정<select id="risk"><option value="">전체</option><option value="risky">위험만</option><option value="M1">M1 위험</option><option value="M2">M2 위험</option><option value="activation_probe">Probe 위험</option></select></label>
  <label class="field">종류<select id="kind"><option value="tensor">Tensor</option><option value="">전체</option><option value="non_tensor">Non-tensor</option></select></label>
  <label class="field search">검색<input id="search" type="search" placeholder="module · location · run"></label>
  <div class="actions"><button id="reset-filters" type="button" class="ghost" title="모든 필터 초기화">초기화</button><button id="refresh" class="primary">새로고침</button></div>
 </div></section>
 <div class="explorer">
  <section class="panel">
   <div class="panel-head"><h2>관찰 레코드</h2><span id="count" class="status hint"></span></div>
   <div class="tablewrap"><table><thead><tr><th>수집 시각</th><th>Task</th><th class="num">ID</th><th>상태</th><th>Run / Step</th><th class="num">Layer</th><th>Module</th><th class="num">Call</th><th>생성 token</th><th>Location</th><th>Shape</th><th>Dtype</th></tr></thead><tbody id="rows"></tbody></table></div>
   <div class="table-foot"><button id="prev">← 이전</button><span id="page"></span><button id="next">다음 →</button><span class="status" style="margin-left:auto">↑ / ↓ 키로 레코드 이동</span></div>
  </section>
  <section class="panel sticky-col">
   <div class="panel-head detail-head">
    <h2 id="detail-title">레코드를 선택하세요</h2>
    <div class="ab-actions"><button id="set-a" title="현재 레코드를 비교 A로 지정">A로 지정</button><button id="set-b" title="현재 레코드를 비교 B로 지정">B로 지정</button><button id="open-compare" class="ghost" type="button">A/B 비교 열기 →</button></div>
   </div>
   <div class="panel-body scroll">
    <div id="details"><div class="empty">왼쪽 표에서 행을 선택하면 메타데이터, 토큰, 요약 그래프와 원소값을 불러옵니다.</div></div>
    <details class="section" open><summary><span class="step">1</span>Prompt token ↔ tensor<small id="prompt-meta" class="status">Prompt 토큰이 기록된 수집을 선택하세요.</small></summary><div class="section-body">
     <details class="inline"><summary>Prompt 원문 보기</summary><pre id="prompt-text"></pre></details>
     <div id="tokens" class="tokens"></div>
    </div></details>
    <details class="section" open><summary><span class="step">2</span>실제 생성 출력 토큰<small id="generated-meta" class="status">생성 추적 또는 replay 자료를 선택하세요.</small></summary><div class="section-body">
     <details class="inline" open><summary>디코딩된 출력 텍스트</summary><pre id="generated-text"></pre></details>
     <div id="generated-tokens" class="tokens"></div>
    </div></details>
    <details class="section" open><summary><span class="step">3</span>토큰 × 은닉 차원 Heatmap</summary><div class="section-body">
     <div class="toolbar" style="margin-bottom:8px"><span id="heatmap-meta" class="status"></span><span class="spacer"></span><label class="status">색 범위 <select id="heatmap-scale"><option value="robust">0.5–99.5% 분위 (outlier 클리핑)</option><option value="minmax">전체 min–max</option></select></label></div>
     <div class="chartbox"><canvas id="heatmap" class="heatmap" width="900" height="360"></canvas></div>
     <div class="axis-note"><span>가로: token position →</span><span>세로: hidden feature (샘플 타일)</span></div>
     <div class="legend"><span id="hm-lo" class="mono">—</span><div id="hm-bar" class="colorbar"></div><span id="hm-hi" class="mono">—</span><span id="hm-desc" class="status"></span></div>
     <small>Canvas 프리뷰입니다. 클릭하면 해당 token 위치로 이동하며, 생성 자료는 예측 토큰과 그 직전 입력 위치를 표시합니다.</small>
    </div></details>
    <details class="section" open><summary><span class="step">4</span>Tensor 분포</summary><div class="section-body">
     <div class="chartbox"><canvas id="chart" class="chart" width="900" height="440"></canvas></div>
     <div id="chart-note" class="legend"></div>
    </div></details>
    <details class="section" open><summary><span class="step">5</span>토큰 위치 원소값 (원본 NPY)</summary><div class="section-body">
     <div class="toolbar">
      <label class="status">Token position <input id="token-position" type="number" min="0" value="0" style="width:90px"></label>
      <label class="status">시작 index <input id="offset" type="number" min="0" value="0" style="width:100px"></label>
      <button id="load-values" class="primary">선택 토큰 값</button>
      <button id="all-values">전체 tensor 원소</button>
      <span class="seg"><button id="sort-high" title="값 내림차순">값 ↓</button><button id="sort-low" title="값 오름차순">값 ↑</button></span>
     </div>
     <div id="value-meta" class="status" style="margin-top:6px"></div>
     <div class="tablewrap valuebox"><table><thead><tr><th class="num">Feature index</th><th class="num">Value</th></tr></thead><tbody id="values"></tbody></table></div>
    </div></details>
    <details class="section" open><summary><span class="step">6</span>Token 차원 축소 Preview</summary><div class="section-body">
     <div class="toolbar"><span class="seg"><button id="pca">PCA</button><button id="tsne">t-SNE</button></span><span id="embedding-meta" class="status">토큰별 표현을 2D에 투영합니다. 점을 클릭하면 해당 토큰으로 이동합니다.</span></div>
     <div class="chartbox" style="margin-top:8px"><canvas id="embedding" class="scatter" width="900" height="520"></canvas></div>
    </div></details>
   </div>
  </section>
 </div>
</div>
<div id="view-tokens" class="view" hidden>
 <section class="panel">
  <div class="filters tv-filters">
   <label class="field">세션 검색<input id="tv-search" type="search" placeholder="run · step · task"></label>
   <label class="field">생성 세션 (generation attempt)<select id="tv-session"><option value="">탭을 열면 불러옵니다</option></select></label>
   <label class="field">관찰 위치 (레이어 0 · 11 · 23 공통)<select id="tv-loc"></select></label>
   <label class="field">추이 지표<select id="tv-metric"><option value="l2">L2 norm</option><option value="cos_prev">이전 토큰과 cosine</option><option value="std">표준편차</option><option value="max_abs">max |x|</option><option value="mean">평균</option></select></label>
   <div class="actions"><button id="tv-prev-page" type="button" disabled>←</button><span id="tv-page" class="status"></span><button id="tv-next-page" type="button" disabled>→</button><button id="tv-refresh" type="button" class="primary">새로고침</button></div>
  </div>
  <div id="tv-status" class="status" role="status" style="padding:0 16px 12px">생성 토큰 매핑이 기록된 generation 세션을 불러옵니다.</div>
 </section>
 <div class="tv-layout">
  <section class="panel sticky-col">
   <div class="panel-head"><h2>생성 토큰</h2><span id="tv-token-count" class="status hint"></span></div>
   <div class="panel-body scroll">
    <input id="tv-token-filter" type="search" placeholder="토큰 텍스트 · piece · id 검색" style="width:100%">
    <details class="inline"><summary>디코딩된 출력 텍스트 전체</summary><pre id="tv-text"></pre></details>
    <div id="tv-tokens" class="tv-token-list"><div class="empty">세션을 선택하세요.</div></div>
    <p class="status" style="margin:10px 0 0">토큰을 클릭하거나 ← / → 키로 이동합니다. 회색은 특수 토큰, 작은 hex는 UTF-8 문자의 일부 바이트만 담긴 토큰입니다.</p>
   </div>
  </section>
  <div class="tv-main">
   <section class="panel">
    <div class="panel-head"><h2>토큰별 추이 · Layer 0 / 11 / 23</h2><span id="tv-trend-meta" class="status hint"></span></div>
    <div class="panel-body">
     <div class="chartbox"><canvas id="tv-trend"></canvas></div>
     <div class="toolbar" style="margin-top:12px"><h3 style="margin-right:4px">토큰 × 은닉 차원</h3><span id="tv-heat-layers" class="seg"></span></div>
     <div class="chartbox" style="margin-top:8px"><canvas id="tv-heat"></canvas></div>
     <div class="legend"><span id="tv-heat-lo" class="mono">—</span><div id="tv-heat-bar" class="colorbar"></div><span id="tv-heat-hi" class="mono">—</span><span id="tv-heat-desc" class="status"></span></div>
     <small>가로축은 두 차트 모두 생성 토큰 순서이며 열이 서로 맞춰져 있습니다. 클릭하면 해당 토큰을 선택합니다. 각 레이어 패널은 자체 세로축을 사용합니다.</small>
    </div>
   </section>
   <section class="panel">
    <div class="panel-head detail-head">
     <div class="tv-token-head"><h2 id="tv-token-title">토큰을 선택하세요</h2><span class="spacer"></span><button id="tv-prev-token" type="button">← 이전 토큰</button><button id="tv-next-token" type="button">다음 토큰 →</button></div>
     <div id="tv-token-meta" class="status"></div>
    </div>
    <div class="panel-body">
     <div id="tv-cards" class="tv-cards"></div>
     <div class="toolbar" style="margin-top:16px"><h3>이 토큰의 전체 Hook 값</h3><span id="tv-rec-layers" class="seg"></span><span id="tv-rec-meta" class="status"></span></div>
     <div class="tablewrap" style="margin-top:8px;max-height:340px;min-height:0;border:1px solid var(--line);border-radius:8px"><table><thead><tr><th>모듈</th><th>위치</th><th>원본 shape</th><th class="num">토큰 원소</th><th class="num">L2</th><th class="num">mean</th><th class="num">max |x|</th></tr></thead><tbody id="tv-records"></tbody></table></div>
     <div class="toolbar" style="margin-top:12px"><span id="tv-sorts" class="seg"><button type="button" data-sort="">index 순</button><button type="button" data-sort="value_desc">값 ↓</button><button type="button" data-sort="value_asc">값 ↑</button><button type="button" data-sort="abs_desc">|값| ↓</button></span><button id="tv-val-prev" type="button" disabled>← 256</button><button id="tv-val-next" type="button" disabled>256 →</button></div>
     <div id="tv-value-meta" class="status" style="margin-top:6px"></div>
     <div class="tablewrap valuebox"><table><thead><tr><th class="num">Flat index (토큰 slice)</th><th class="num">Value</th></tr></thead><tbody id="tv-values"></tbody></table></div>
     <div class="toolbar" style="margin-top:18px"><h3>출력 어휘 투영 · 위 레코드의 토큰 벡터 → 201,088개 토큰</h3><label class="status"><input id="tv-vocab-norm" type="checkbox" checked> 최종 RMSNorm 적용 (logit lens)</label><span class="spacer"></span><input id="tv-vocab-q" type="search" placeholder="단어 · token ID 검색" style="width:200px"><button id="tv-vocab-find-gen" type="button">생성 토큰 찾기</button></div>
     <div id="tv-vocab-summary" class="metrics" style="margin-top:8px"></div>
     <div class="chartbox"><canvas id="tv-vocab-strip"></canvas></div>
     <div class="legend"><span>token ID 0</span><span id="tv-vocab-lo" class="mono">—</span><div id="tv-vocab-bar" class="colorbar"></div><span id="tv-vocab-hi" class="mono">—</span><span class="status">구간별 최대 logit · 노랑 = 생성 토큰, 회색 = 예측 입력 토큰 · 클릭하면 그 ID 구간을 표로 이동</span><span class="spacer"></span><span id="tv-vocab-max-id" class="status"></span></div>
     <div class="toolbar" style="margin-top:10px"><span id="tv-vocab-sorts" class="seg"><button type="button" data-sort="">logit ↓ (순위)</button><button type="button" data-sort="logit_asc">logit ↑</button><button type="button" data-sort="id">token ID 순</button></span><button id="tv-vocab-prev" type="button" disabled>← 100</button><span id="tv-vocab-page" class="status mono"></span><button id="tv-vocab-next" type="button" disabled>100 →</button><span id="tv-vocab-meta" class="status"></span></div>
     <div class="tablewrap valuebox" style="max-height:440px"><table><thead><tr><th class="num">순위</th><th class="num">Token ID</th><th>단어</th><th>Tokenizer piece</th><th class="num">Logit</th><th class="num">확률 (softmax)</th></tr></thead><tbody id="tv-vocab-rows"></tbody></table></div>
    </div>
   </section>
  </div>
 </div>
</div>
<div id="view-rollouts" class="view" hidden>
 <section class="panel">
  <div class="panel-head"><h2>시나리오 실행 기록</h2><span class="status">scenario_rollout.py 결과 · step마다 모델 입력, LLM 출력, 실행 결과, 판정</span><span id="ro-root" class="status hint"></span><button id="ro-refresh" type="button" class="primary">새로고침</button></div>
  <div class="panel-body" style="padding-bottom:8px">
   <div class="toolbar"><input id="ro-search" type="search" placeholder="시나리오 · 조건 · 과제 검색" style="width:260px">
    <label class="status">종류 <select id="ro-kind"><option value="">전체</option><option value="suite">scenario_suite</option><option value="workspace">workspace</option></select></label>
    <label class="status">판정 <select id="ro-filter"><option value="">전체</option><option value="violation">위반 있음</option><option value="clean">위반 없음</option><option value="running">미완료</option></select></label>
    <span id="ro-count" class="status"></span></div>
  </div>
  <div class="tablewrap" style="max-height:300px;min-height:0"><table><thead><tr><th>시작</th><th>시나리오 / 조건</th><th class="num">seed</th><th>종류</th><th>종료</th><th class="num">행동</th><th class="num">위반</th><th>업무 완료</th><th>과제</th></tr></thead><tbody id="ro-list"><tr><td colspan="9"><div class="empty">탭을 열면 실행 기록을 불러옵니다.</div></td></tr></tbody></table></div>
 </section>
 <section class="panel" style="margin-top:16px">
  <div class="panel-head detail-head"><div class="tv-token-head"><h2 id="ro-title">실행 기록을 선택하세요</h2><span class="spacer"></span><a id="ro-transcript" class="status" target="_blank" hidden>transcript.md 열기</a></div><div id="ro-sub" class="status"></div></div>
  <div class="panel-body">
   <div id="ro-metrics" class="metrics"></div>
   <details class="inline" id="ro-context-box"><summary>시나리오 JSON 요약 · 모델에 준 과제 · 정책 · 도구</summary><pre id="ro-context"></pre></details>
   <div id="ro-steps"></div>
  </div>
 </section>
</div>
<div id="view-scenario-hidden" class="view" hidden>
 <section class="panel"><div class="filters tv-filters" style="grid-template-columns:minmax(220px,1.2fr) minmax(320px,2fr) auto">
  <label class="field">시나리오<select id="sh-scenario"><option value="">불러오는 중…</option></select></label>
  <label class="field">실행 (조건 · seed · 시각 · 위반)<select id="sh-rollout"></select></label>
  <div class="actions"><button id="sh-refresh" type="button" class="primary">새로고침</button></div>
 </div><div id="sh-status" class="status" style="padding:0 16px 12px">scenario_rollout.py가 저장한 관찰 시점 은닉 상태(C-01, 모든 블록)를 분석합니다.</div></section>
 <section class="panel" style="margin-top:16px">
  <div class="panel-head detail-head"><div class="tv-token-head"><h2 id="sh-title">시나리오를 선택하세요</h2><span class="spacer"></span><button id="sh-open-record" type="button" class="ghost">실행 기록 보기 →</button></div><div id="sh-sub" class="status"></div></div>
  <div class="panel-body">
   <div id="sh-brief" class="metrics"></div>
   <h3 class="sub">step 흐름 · 레이어별 행동 직전(pre_action) L2 <small class="muted">각 레이어 안에서 정규화 · 위 띠 = 판정(빨강 위반) · 클릭하면 step 선택</small></h3>
   <div class="chartbox"><canvas id="sh-trend" style="height:230px;cursor:pointer"></canvas></div>
   <div id="sh-steps" class="toolbar" style="margin-top:8px"></div>
  </div>
 </section>
 <section class="panel" style="margin-top:16px">
  <div class="panel-head detail-head"><h2 id="sh-step-title">step</h2><div id="sh-step-meta" class="status"></div></div>
  <div class="panel-body">
   <div class="ro-grid" style="padding:0"><div class="ro-col"><h4>LLM 추론</h4><pre id="sh-reasoning"></pre></div><div class="ro-col"><h4>LLM 행동</h4><pre id="sh-action"></pre></div><div class="ro-col"><h4>실행 결과 · 판정</h4><div id="sh-findings" class="ro-findings"></div><pre id="sh-observation"></pre></div></div>
   <h3 class="sub">토큰 문맥 <small class="muted">노랑 = 관찰 시점(클릭하여 선택) · 회색 = prompt · 흰색 = 이번 step 추론</small></h3>
   <div id="sh-tokens" class="tv-token-list cap-tokens"></div>
   <h3 class="sub">레이어 × 관찰 시점 L2 <small class="muted">각 레이어 안에서 정규화 · 칸을 클릭하면 아래에 그 위치·레이어를 분석</small></h3>
   <div class="chartbox"><canvas id="sh-grid" style="height:300px;cursor:crosshair"></canvas></div>
  </div>
 </section>
 <section class="panel" style="margin-top:16px">
  <div class="panel-head"><h2 id="sh-cell-title">선택한 위치 · 레이어</h2><span class="spacer"></span><label class="status">레이어 <select id="sh-layer"></select></label></div>
  <div class="panel-body">
   <div class="tv-cards" style="grid-template-columns:minmax(0,1fr) minmax(0,2fr)"><div class="tv-card"><div id="sh-stats" class="tv-stats"></div><div id="sh-top" class="tv-top"></div></div>
    <div class="tv-card"><div class="chartbox"><canvas class="tv-spark" id="sh-spark" style="height:120px"></canvas></div><div class="axis-note"><span>dim 0</span><span id="sh-spark-note"></span></div></div></div>
   <div class="toolbar" style="margin-top:12px"><h3>원소값</h3><span id="sh-sorts" class="seg"><button type="button" data-sort="">index 순</button><button type="button" data-sort="value_desc">값 ↓</button><button type="button" data-sort="value_asc">값 ↑</button><button type="button" data-sort="abs_desc">|값| ↓</button></span><button id="sh-val-prev" type="button" disabled>← 256</button><button id="sh-val-next" type="button" disabled>256 →</button><span id="sh-value-meta" class="status"></span></div>
   <div class="tablewrap valuebox"><table><thead><tr><th class="num">Hidden dim</th><th class="num">Value</th></tr></thead><tbody id="sh-values"></tbody></table></div>
   <div class="toolbar" style="margin-top:16px"><h3>출력 어휘 투영 · 201,088개 토큰 (logit lens)</h3><label class="status"><input id="sh-vocab-norm" type="checkbox" checked> 최종 RMSNorm 적용</label><span class="spacer"></span><input id="sh-vocab-q" type="search" placeholder="단어 · token ID 검색" style="width:200px"><span id="sh-vocab-sorts" class="seg"><button type="button" data-sort="">logit ↓</button><button type="button" data-sort="logit_asc">logit ↑</button><button type="button" data-sort="id">ID 순</button></span><button id="sh-vocab-prev" type="button" disabled>← 100</button><button id="sh-vocab-next" type="button" disabled>100 →</button></div>
   <div id="sh-vocab-meta" class="status" style="margin-top:6px"></div>
   <div class="tablewrap valuebox" style="max-height:380px"><table><thead><tr><th class="num">순위</th><th class="num">Token ID</th><th>단어</th><th>piece</th><th class="num">Logit</th><th class="num">확률</th></tr></thead><tbody id="sh-vocab-rows"></tbody></table></div>
  </div>
 </section>
</div>
<div id="view-captures" class="view" hidden>
 <section class="panel">
  <div class="panel-head"><h2>팀원 C-01 Capture</h2><span class="status">write_capture 산출물(scripts/run_m1_sandbox.py 등) · 행동 직전 관찰 토큰 1개의 블록 출력</span><span id="cap-root" class="status hint"></span><button id="cap-refresh" type="button" class="primary">새로고침</button></div>
  <div class="tablewrap" style="max-height:260px;min-height:0"><table><thead><tr><th>수집 시각</th><th>Run</th><th>시나리오</th><th>관찰 토큰</th><th class="num">Prefix</th><th>M1 판정</th><th>무결성</th><th>Task</th></tr></thead><tbody id="cap-list"><tr><td colspan="8"><div class="empty">탭을 열면 capture 목록을 불러옵니다.</div></td></tr></tbody></table></div>
 </section>
 <div id="cap-detail" style="display:grid;gap:16px;margin-top:16px">
  <section class="panel">
   <div class="panel-head detail-head"><h2 id="cap-title">Capture를 선택하세요</h2><div id="cap-sub" class="status"></div></div>
   <div class="panel-body">
    <div id="cap-metrics" class="metrics"></div>
    <div class="toolbar"><h3>토큰 문맥</h3><span class="legend" style="margin:0"><span class="cap-tok prompt">prompt</span><span class="cap-tok reasoning">추론</span><span class="cap-tok observed">관찰 위치</span><span class="cap-tok action">행동 (관찰 이후)</span></span><span id="cap-token-meta" class="status"></span></div>
    <div id="cap-tokens" class="tv-token-list cap-tokens"></div>
   </div>
  </section>
  <section class="panel">
   <div class="panel-head"><h2>관찰 토큰의 블록 출력 · Layer 0 / 11 / 23</h2><span id="cap-hook" class="status hint"></span></div>
   <div class="panel-body"><div id="cap-cards" class="tv-cards"></div></div>
  </section>
  <section class="panel">
   <div class="panel-head"><h2>작성자 HookInspection 기록과 대조</h2><span class="status hint">같은 token prefix를 관찰한 세션을 자동으로 찾아 같은 위치의 블록 출력을 비교합니다</span></div>
   <div id="cap-matches" class="panel-body"></div>
  </section>
  <section class="panel">
   <div class="panel-head"><h2>원소값</h2><span id="cap-val-layers" class="seg"></span><span id="cap-sorts" class="seg"><button type="button" data-sort="">index 순</button><button type="button" data-sort="value_desc">값 ↓</button><button type="button" data-sort="value_asc">값 ↑</button><button type="button" data-sort="abs_desc">|값| ↓</button></span><button id="cap-val-prev" type="button" disabled>← 256</button><button id="cap-val-next" type="button" disabled>256 →</button></div>
   <div class="panel-body"><div id="cap-value-meta" class="status"></div><div class="tablewrap valuebox"><table><thead><tr><th class="num">Hidden dim</th><th class="num">Value</th></tr></thead><tbody id="cap-values"></tbody></table></div></div>
  </section>
 </div>
</div>
<div id="view-compare" class="view" hidden>
 <section class="panel">
  <div class="panel-head"><h2>Tensor A/B 비교</h2><span class="status hint">분석 탭에서 레코드를 선택하고 “A로 지정 / B로 지정”을 누르세요. shape가 같은 tensor만 계산합니다.</span></div>
  <div class="panel-body">
   <div class="toolbar" style="margin-bottom:12px"><button id="compare" class="primary">비교 실행</button><span id="compare-meta" class="status"></span></div>
   <div class="compare-grid">
    <div class="slot"><b><span class="tag">A</span><span id="label-a">A 미선택</span></b><div class="chartbox"><canvas id="chart-a" class="compare-chart" width="900" height="360"></canvas></div></div>
    <div class="slot"><b><span class="tag">B</span><span id="label-b">B 미선택</span></b><div class="chartbox"><canvas id="chart-b" class="compare-chart" width="900" height="360"></canvas></div></div>
   </div>
   <div id="compare-metrics" class="metrics" style="margin-top:14px"></div>
   <h3 class="sub">A − B feature delta (상위 |차이|)</h3>
   <div class="chartbox"><canvas id="delta-chart" class="compare-chart" width="900" height="360"></canvas></div>
   <div class="legend"><span class="swatch" style="background:var(--div-pos)"></span>A &gt; B<span class="swatch" style="background:var(--div-neg);margin-left:8px"></span>A &lt; B<span class="status" style="margin-left:8px">막대에 마우스를 올리면 dimension과 delta를 표시합니다.</span></div>
  </div>
 </section>
</div>
<div id="view-hooks" class="view" hidden>
 <section class="panel">
  <div class="panel-head"><h2>Hook 위치 지도</h2><span class="status">수집 기록에 등록된 모듈과 입력 · 출력 경계</span><button id="hook-refresh" type="button" class="primary">새로고침</button></div>
  <div class="panel-body">
   <div class="toolbar">
    <label class="field">실행 / Task / Phase 검색<input id="hook-session-search" type="search" placeholder="run · step · generation · replay"></label>
    <label class="field" style="flex:1;min-width:240px">수집 세션<select id="hook-session"><option value="">수집 기록을 불러오세요</option></select></label>
    <button id="hook-prev" type="button" disabled>이전 세션</button><span id="hook-page" class="status"></span><button id="hook-next" type="button" disabled>다음 세션</button>
   </div>
   <div id="hook-status" class="status" role="status" style="margin-top:10px">탭을 열면 등록 정보를 불러옵니다.</div>
   <div id="hook-metrics" class="metrics"></div>
   <div id="hook-overview" class="hook-overview" aria-label="Layer 선택"></div>
   <p class="hook-note">PRE는 모듈 실행 전 입력, POST는 반환된 출력의 Hook입니다. 연결선은 모듈 포함 관계이며 실행 순서가 아닙니다. 완료된 수집의 Hook은 해제되므로 이 지도는 현재 프로세스의 실시간 연결 상태를 의미하지 않습니다.</p>
  </div>
 </section>
 <div class="hook-layout" style="margin-top:16px">
  <section class="panel"><div class="panel-head"><h2>등록 모듈 구조</h2><span class="spacer"></span><input id="hook-module-search" type="search" placeholder="모듈 경로 / 클래스 검색" aria-label="Hook 모듈 검색"></div>
   <div class="panel-body"><div class="legend"><span class="hook-state called">● 호출 확인</span><span class="hook-state not_called">○ 등록 · 미호출</span><span class="hook-state pending">◌ 호출 정보 대기</span></div><div id="hook-tree" class="hook-tree"><div class="hook-empty">수집 세션을 선택하세요.</div></div></div>
  </section>
  <section class="panel"><div class="panel-head"><h2>Hook 상세</h2></div><div id="hook-detail" class="panel-body"><div class="hook-empty">모듈을 클릭하면 Hook 위치와 관찰된 tensor shape를 표시합니다.</div></div></section>
 </div>
 <section class="panel" style="margin-top:16px"><div class="panel-head"><h2>수집 범위와 해석</h2></div><div class="panel-body">
  <p class="hook-note">HookInspection은 선택한 모듈마다 <code>register_forward_pre_hook</code>와 <code>register_forward_hook</code>를 등록합니다. 최상위 모델에는 forward 번호를 세는 별도의 pre-hook도 있습니다.</p>
  <p class="hook-note">모듈 내부의 함수 연산·잔차 덧셈·Parameter는 독립적인 모듈 Hook이 아닙니다. 예를 들어 fused MoE expert 내부의 가중치에는 별도 모듈 Hook이 없을 수 있습니다. ‘미호출’은 Hook이 없다는 뜻이 아닙니다.</p>
  <p class="hook-note">C-01 특징 추출은 별도로 선택한 Transformer 블록의 출력에 forward hook을 사용합니다. 아래 지도는 HookInspection manifest 기준이며 C-01의 독립적인 Hook은 등록 모듈 수에 합산하지 않습니다.</p>
  <p id="hook-source" class="hook-note mono"></p>
 </div></section>
</div>
<div id="view-sandbox" class="view" hidden>
 <div class="sandbox-grid">
  <div style="display:grid;gap:16px">
   <section class="panel"><div class="panel-head"><h2>파일을 Sandbox로 가져오기</h2></div><div class="panel-body">
    <div class="dropzone"><input id="sandbox-file" type="file"><div class="toolbar"><button id="sandbox-import" class="primary">업로드 및 Import</button></div><span id="sandbox-import-status" class="status">파일은 서버 임시 경로에 저장된 뒤 sandbox.py import로 전달됩니다.</span></div>
   </div></section>
   <section class="panel"><div class="panel-head"><h2>Sandbox 내부 파일</h2><button id="sandbox-list" class="hint">현재 파일 조회</button></div>
    <div class="panel-body" style="padding-bottom:0"><span id="sandbox-list-status" class="status" role="status">/workspace 내부 파일과 폴더를 조회합니다.</span></div>
    <div class="tablewrap" style="margin-top:8px"><table><thead><tr><th>경로</th><th>종류</th><th class="num">크기 (bytes)</th></tr></thead><tbody id="sandbox-files"></tbody></table></div>
   </section>
  </div>
  <section class="panel"><div class="panel-head"><h2>파일 내용</h2></div><div class="panel-body">
   <div id="sandbox-preview-status" class="status" role="status">왼쪽 목록에서 파일 경로를 클릭하면 내용을 표시합니다.</div>
   <img id="sandbox-image" hidden alt="Sandbox 이미지 미리보기">
   <pre id="sandbox-preview"></pre>
  </div></section>
 </div>
</div>
<div id="view-sandbox-web" class="view" hidden>
 <section class="panel"><div class="panel-head"><h2>FakeNet 웹 응답</h2><button id="sw-refresh" class="primary">새로고침</button><span id="sw-status" class="status hint">SANDBOX/fakenet/routes.json 설정과 FakeNet 요청 기록</span></div>
  <div class="sandbox-grid panel-body">
   <div><label class="field">라우트 설정 · JSON<textarea id="sw-routes" spellcheck="false" style="width:100%;height:300px;font:12px/1.5 var(--mono);margin-top:6px"></textarea></label><button id="sw-save-routes" class="primary" style="margin-top:8px">라우트 저장</button><div class="toolbar" style="margin-top:12px"><label class="field">Host<input id="sw-host" value="example.test"></label><label class="field">Path<input id="sw-path" value="/" /></label><button id="sw-preview-route">가상 URL 미리보기</button><span id="sw-preview-status" class="status"></span></div><pre id="sw-response-preview" style="max-height:280px"></pre></div>
   <div><div class="toolbar"><label class="field" style="flex:1">사이트 파일<select id="sw-file"><option value="">파일 선택</option></select></label><button id="sw-new-file">새 파일</button></div><textarea id="sw-content" spellcheck="false" placeholder="사이트 파일 내용을 편집합니다." style="width:100%;height:360px;font:12px/1.5 var(--mono);margin-top:6px"></textarea><div class="toolbar" style="margin-top:8px"><button id="sw-save-file" class="primary">파일 저장</button><span id="sw-file-status" class="status"></span></div><iframe id="sw-preview" title="FakeNet 웹 미리보기" sandbox="" style="width:100%;height:300px;border:1px solid var(--line);border-radius:8px;margin-top:12px;background:white"></iframe></div>
  </div>
 </section>
 <section class="panel" style="margin-top:16px"><div class="panel-head"><h2>FakeNet 요청 기록</h2><span class="status">실행 중 Sandbox에서 FakeNet으로 들어온 최근 요청</span></div><div class="tablewrap"><table><thead><tr><th>시각</th><th>종류</th><th>요청</th><th class="num">상태</th></tr></thead><tbody id="sw-events"><tr><td colspan="4">새로고침을 눌러 조회하세요.</td></tr></tbody></table></div></section>
</div>
</main>
<div id="tip"></div>
<script>
const $=id=>document.getElementById(id);let all=[],selected=null,page=0,pageSize=100,total=0,timer=null,requestId=0;
function esc(v){return String(v??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
function keyOf(r){return r.key}
/* ---------- theme / tooltip / chart helpers ---------- */
const cssVar=n=>getComputedStyle(document.documentElement).getPropertyValue(n).trim();
function hexRgb(h){h=h.replace('#','');if(h.length===3)h=h.split('').map(c=>c+c).join('');const n=parseInt(h,16);return[(n>>16)&255,(n>>8)&255,n&255]}
function mix(a,b,t){return[0,1,2].map(i=>Math.round(a[i]+(b[i]-a[i])*t))}
function fmt(v){if(typeof v!=='number'||!Number.isFinite(v))return String(v);const a=Math.abs(v);return a!==0&&(a<1e-3||a>=1e5)?v.toExponential(3):String(+v.toPrecision(5))}
const tip=$('tip');
function showTip(ev,html){tip.innerHTML=html;tip.style.display='block';const pad=14,r=tip.getBoundingClientRect();let x=ev.clientX+pad,y=ev.clientY+pad;if(x+r.width>innerWidth-8)x=ev.clientX-r.width-pad;if(y+r.height>innerHeight-8)y=ev.clientY-r.height-pad;tip.style.left=x+'px';tip.style.top=y+'px'}
function hideTip(){tip.style.display='none'}
function canvasPoint(c,ev){const r=c.getBoundingClientRect();return{x:(ev.clientX-r.left)/r.width*c.width,y:(ev.clientY-r.top)/r.height*c.height,fx:(ev.clientX-r.left)/r.width,fy:(ev.clientY-r.top)/r.height}}
/* match the canvas bitmap to its on-screen size so text is never stretched; s = device pixels per CSS pixel */
function fitCanvas(c){const r=c.getBoundingClientRect(),d=window.devicePixelRatio||1;if(r.width>0&&r.height>0){const W=Math.round(r.width*d),H=Math.round(r.height*d);if(c.width!==W||c.height!==H){c.width=W;c.height=H}c._s=d}else c._s=c._s||2;const x=c.getContext('2d');x.setTransform(1,0,0,1,0,0);x.clearRect(0,0,c.width,c.height);x.font=`${11*c._s}px system-ui, sans-serif`;x.textBaseline='middle';x.lineJoin='round';return x}
function roundTopBar(x,px,py,w,h,rad){const r=Math.min(rad,w/2,h);x.beginPath();x.moveTo(px,py+h);x.lineTo(px,py+r);x.quadraticCurveTo(px,py,px+r,py);x.lineTo(px+w-r,py);x.quadraticCurveTo(px+w,py,px+w,py+r);x.lineTo(px+w,py+h);x.closePath();x.fill()}
function histPanel(x,s,y0,W,H,hist,opt){const left=60*s,right=12*s,top=y0+(opt.title?26*s:8*s),bottom=y0+H-(opt.range?22*s:8*s),pw=W-left-right,ph=Math.max(1,bottom-top),max=Math.max(1,...hist.map(b=>b.count)),bw=pw/Math.max(1,hist.length),gap=bw>4*s?2*s:0;
 if(opt.title){x.fillStyle=cssVar('--text-2');x.textAlign='left';x.fillText(opt.title,left,y0+12*s)}
 x.strokeStyle=cssVar('--grid');x.lineWidth=s;x.fillStyle=cssVar('--muted');x.textAlign='right';
 for(const f of[0,.5,1]){const y=Math.round(bottom-f*ph)+.5;x.beginPath();x.moveTo(left,y);x.lineTo(W-right,y);x.stroke();x.fillText(Math.round(max*f).toLocaleString(),left-6*s,y)}
 x.fillStyle=opt.color||cssVar('--series-1');hist.forEach((b,i)=>{const bh=b.count/max*ph;if(bh>0)roundTopBar(x,left+i*bw+gap/2,bottom-bh,Math.max(1,bw-gap),bh,3*s)});
 if(opt.range){x.fillStyle=cssVar('--muted');x.textAlign='left';x.fillText(fmt(opt.range[0]),left,bottom+12*s);x.textAlign='right';x.fillText(fmt(opt.range[1]),W-right,bottom+12*s)}
 x.textAlign='left';return{left,top,bottom,bw}}
function histTip(ev,g,p,hist,range){const i=Math.floor((p.x-g.left)/g.bw);if(i<0||i>=hist.length||p.y<g.top-4||p.y>g.bottom+4){hideTip();return}let html=`<b>bin ${i}</b>\ncount ${hist[i].count.toLocaleString()}`;if(range){const st=(range[1]-range[0])/hist.length;html+=`\n[${fmt(range[0]+st*i)}, ${fmt(range[0]+st*(i+1))})`}showTip(ev,html)}

/* ---------- tabs / theme / redraw ---------- */
let lastPlot=null,lastHeat=null,lastHeatPos=-1,lastEmbed=null,lastCompare=null,histA=null,histB=null,promptPieces=[];
function redrawAll(){tvRedraw();capRedraw();shRedraw();if(lastPlot)renderPlot(lastPlot);if(lastHeat)renderHeatmap(lastHeat,lastHeatPos);if(lastEmbed)renderEmbedding(lastEmbed);if(histA)drawHist('chart-a',histA,'A 분포');if(histB)drawHist('chart-b',histB,'B 분포');if(lastCompare)renderDelta(lastCompare)}
function showView(id){document.querySelectorAll('.tab').forEach(t=>t.setAttribute('aria-selected',String(t.dataset.view===id)));document.querySelectorAll('.view').forEach(v=>v.hidden=v.id!==id);hideTip();requestAnimationFrame(redrawAll);if(id==='view-tokens')tvEnsureLoaded();if(id==='view-captures')capEnsureLoaded();if(id==='view-rollouts')roEnsureLoaded();if(id==='view-scenario-hidden')shEnsureLoaded();if(id==='view-hooks'&&!hookLoaded)loadHookSessions();if(id==='view-sandbox-web')swLoad()}
document.querySelectorAll('.tab').forEach(t=>t.onclick=()=>showView(t.dataset.view));$('open-compare').onclick=()=>showView('view-compare');
$('theme-toggle').onclick=()=>{const next=document.documentElement.dataset.theme==='light'?'dark':'light';document.documentElement.dataset.theme=next;try{localStorage.setItem('argus-theme',next)}catch(e){}redrawAll()};
document.querySelectorAll('details.section').forEach(d=>d.addEventListener('toggle',()=>{if(d.open)redrawAll()}));
let resizeTimer=null;window.addEventListener('resize',()=>{clearTimeout(resizeTimer);resizeTimer=setTimeout(redrawAll,150)});

/* ---------- records ---------- */
async function refresh(){const current=++requestId;try{const p=new URLSearchParams({offset:String(page*pageSize),limit:String(pageSize),date:$('date').value,run:$('run').value,layer:$('layer').value,phase:$('phase').value,kind:$('kind').value,risk:$('risk').value,q:$('search').value});const r=await fetch('/api/records?'+p,{cache:'no-store'});if(!r.ok)throw Error(await r.text());const data=await r.json();if(current!==requestId)return;all=data.records;total=data.total;fillSelect('date',data.dates,'전체 날짜');fillSelect('layer',data.layers.map(String),'전체');fillSelect('phase',data.phases,'전체');fillRunSelect(data.runs);$('status').classList.toggle('error',!!data.ingest_errors);$('status').textContent=`DB 자동 동기화 · ${new Date().toLocaleTimeString()} · ${data.sessions}개 수집 폴더${data.ingest_errors?' · 오류 '+data.ingest_errors:''}`;drawRows();
 }catch(e){$('status').classList.add('error');$('status').textContent='DB 조회 오류: '+e.message}}
function fillSelect(id,items,label){const el=$(id),old=el.value;el.innerHTML=`<option value="">${label}</option>`+items.map(x=>`<option value="${esc(x)}">${esc(x)}</option>`).join('');if(items.includes(old))el.value=old}
function fillRunSelect(runs){const el=$('run'),old=el.value;el.innerHTML='<option value="">전체 실행</option>'+(runs||[]).map(x=>`<option value="${esc(x.key)}">${esc(x.label)}</option>`).join('');if((runs||[]).some(x=>x.key===old))el.value=old}
function filterRows(){page=0;refresh()}
function badges(ds){if(!ds?.length)return '<span class="badge unknown">미판정</span>';return ds.map(d=>{const name=d.monitor==='activation_probe'?'Probe':d.monitor;const label=d.alarm===1?`위험-${name}`:d.alarm===0?`${name} 비경고`:`${name} 미판정`;return `<span class="badge ${d.alarm===1?'danger':d.alarm===0?'safe':'unknown'}" title="token ${d.token_index??'—'} · score ${d.risk_score??'—'} · ${esc(d.reason??d.status)}">${esc(label)}</span>`}).join(' ')}
function drawRows(){const start=page*pageSize;let lastDate=null,lastRun=null;let html='';for(const r of all){const runKey=r.run_id||r.run||'unknown';if(r.collection_date!==lastDate){lastDate=r.collection_date;lastRun=null;html+=`<tr class="dategroup"><td colspan="12">${esc(lastDate??'날짜 미기록')}</td></tr>`}if(runKey!==lastRun){lastRun=runKey;html+=`<tr class="rungroup"><td colspan="12">실행 묶음 · ${esc(r.run_id||r.run||'run 미기록')} · ${esc(r.collected_at??'시각 미기록')} · ${esc(r.task??'미기록')}</td></tr>`}const gen=r.generated_token_piece===undefined?'<span class="muted">—</span>':`#${r.generated_token_index} <code>${esc(r.generated_token_piece)}</code>`;const genTitle=r.generated_token_piece===undefined?'Replay / 미매핑':`token id ${r.generated_token_id} · 예측 입력 ${esc(r.source_token_piece??'—')} · forward ${r.forward_call_index}`;html+=`<tr data-key="${esc(keyOf(r))}" class="${selected===keyOf(r)?'selected':''}"><td class="mono" title="${esc(r.collected_at)}">${esc(r.collected_at??'미기록')}</td><td class="task" title="${esc(r.task)}">${esc(r.task??'미기록')}</td><td class="num">${r.record_id}</td><td>${badges(r.detectors)}</td><td>${esc(r.run)} / ${esc(r.step)}</td><td class="num">${r.layer_index??'—'}</td><td class="module mono" title="${esc(r.module)}">${esc(r.module)}</td><td class="num">${r.call_index}</td><td title="${genTitle}">${gen}</td><td title="${esc(r.location)}">${esc(r.location)}</td><td class="mono">${esc(JSON.stringify(r.shape??'—'))}</td><td class="mono">${esc(r.source_dtype??r.python_type??'')}</td></tr>`}$('rows').innerHTML=html||'<tr><td colspan="12"><div class="empty">조건에 맞는 레코드가 없습니다.</div></td></tr>';$('count').textContent=`${total.toLocaleString()}개 레코드 · 날짜별 실행 묶음 · 최신순`;$('page').textContent=`${total?start+1:0}–${Math.min(start+all.length,total)} / ${total.toLocaleString()}`;$('prev').disabled=page===0;$('next').disabled=(page+1)*pageSize>=total;document.querySelectorAll('#rows tr[data-key]').forEach(tr=>tr.onclick=()=>selectRecord(tr.dataset.key))}
async function selectRecord(key){selected=key;drawRows();const r=all.find(x=>x.key===key);if(!r)return;[...document.querySelectorAll('#rows tr[data-key]')].find(tr=>tr.dataset.key===key)?.scrollIntoView({block:'nearest'});$('detail-title').textContent=`Layer ${r.layer_index??'—'} · ${r.module} · ${r.location}${r.generated_token_piece!==undefined?' · predicts #'+r.generated_token_index+' '+r.generated_token_piece:''}`;$('details').innerHTML=`<div class="metrics">${[['수집 시작',r.collected_at??'미기록'],['수집 완료',r.completed_at??'진행 중 / 미기록'],['Task',r.task??'미기록'],['수집 상태',r.session_status??'미기록'],['run / step',r.run+' / '+r.step],['phase / call',r.phase+' / '+r.call_index],['예측 대상 token',r.generated_token_piece===undefined?'replay 자료':`#${r.generated_token_index} · ${r.generated_token_piece} (id ${r.generated_token_id})`],['예측에 사용된 입력',r.generated_token_piece===undefined?'—':`${r.source_token_piece??'—'} (id ${r.source_token_id??'—'}) · position ${r.generation_source_position??'—'}`],['shape',JSON.stringify(r.shape??'—')],['dtype',`${r.source_dtype??r.python_type??''} → ${r.storage_dtype??''}`],['meaning',r.meaning??'—'],['file',r.filename??'—'],['statistics',r.statistics?`min ${r.statistics.min} · max ${r.statistics.max}`:'—'],['mean / std',r.statistics?`${r.statistics.mean} / ${r.statistics.std}`:'—']].map(([a,b])=>`<div class="metric"><b>${esc(a)}</b>${esc(b)}</div>`).join('')}</div><div style="margin-bottom:6px">${badges(r.detectors)}</div><details class="inline"><summary>전체 레코드 메타데이터 (JSON)</summary><pre>${esc(JSON.stringify(r,null,2))}</pre></details>`;await loadPrompt(key,r.generated_token_piece!==undefined,r.generated_token_index);if(r.kind==='tensor'){await drawPlot(key);await drawHeatmap(key);viewMode='token';$('offset').value=0;$('token-position').value=r.generation_source_position??0;$('token-position').disabled=r.generated_token_piece!==undefined;await loadValues()}else{lastPlot=null;fitCanvas($('chart'));$('chart-note').textContent='Non-tensor 레코드 — 분포 그래프 없음';$('values').innerHTML=`<tr><td>—</td><td>${esc(JSON.stringify(r.value??r.availability))}</td></tr>`}}

/* ---------- distribution: histogram and axis-0 mean in two stacked panels (no shared/dual axis) ---------- */
async function drawPlot(key){const data=await(await fetch('/api/plot?key='+encodeURIComponent(key))).json();if(data.error){$('status').textContent=data.error;return}lastPlot=data;renderPlot(data)}
function renderPlot(data){const c=$('chart'),x=fitCanvas(c),s=c._s,W=c.width,H=c.height,hist=data.histogram||[],vals=data.axis0&&data.axis0.length>1?data.axis0:null,range=[data.min,data.max],hH=vals?Math.round(H*.58):H;
 const g=histPanel(x,s,0,W,hH,hist,{title:'전체 원소 histogram',range});let lg=null;
 if(vals){const left=60*s,right=12*s,top=hH+30*s,bottom=H-8*s,pw=W-left-right,ph=Math.max(1,bottom-top),lo=Math.min(...vals.map(v=>v.mean)),hi=Math.max(...vals.map(v=>v.mean)),span=hi-lo||1;
  x.fillStyle=cssVar('--text-2');x.fillText('axis-0 그룹 평균 (index 순)',left,hH+14*s);
  x.strokeStyle=cssVar('--grid');x.lineWidth=s;x.fillStyle=cssVar('--muted');x.textAlign='right';
  for(const f of[0,1]){const y=Math.round(bottom-f*ph)+.5;x.beginPath();x.moveTo(left,y);x.lineTo(W-right,y);x.stroke();x.fillText(fmt(lo+span*f),left-6*s,y)}
  x.textAlign='left';x.strokeStyle=cssVar('--series-1');x.lineWidth=2*s;x.beginPath();vals.forEach((v,i)=>{const px=left+i*pw/(vals.length-1),py=bottom-(v.mean-lo)/span*ph;i?x.lineTo(px,py):x.moveTo(px,py)});x.stroke();lg={left,pw,top:hH}}
 c.onmousemove=ev=>{const p=canvasPoint(c,ev);if(!lg||p.y<lg.top){histTip(ev,g,p,hist,range);return}const i=Math.round((p.x-lg.left)/lg.pw*(vals.length-1));if(i<0||i>=vals.length){hideTip();return}showTip(ev,`<b>axis-0 index ${vals[i].index}</b>\nmean ${fmt(vals[i].mean)}`)};c.onmouseleave=hideTip;
 $('chart-note').innerHTML=`<span class="mono">N = ${data.numel.toLocaleString()}</span><span>·</span><span class="mono">non-finite = ${esc(data.nonfinite)}</span><span>·</span><span class="mono">range [${esc(fmt(data.min))}, ${esc(fmt(data.max))}]</span>`}

/* ---------- prompt / generated tokens ---------- */
async function loadPrompt(key,generated=false,targetIndex=null){const d=await(await fetch('/api/prompt?key='+encodeURIComponent(key))).json();if(d.error){$('prompt-meta').textContent=d.error;promptPieces=[];return}promptPieces=d.token_pieces||[];$('prompt-meta').textContent=`${d.token_count} prompt tokens · ${d.task_text||'Task 미기록'}${generated?' · 생성 token의 예측 입력은 Hook 값에 연결됨':''}`;$('prompt-text').textContent=d.prompt_text||'';$('tokens').innerHTML=(d.token_pieces||[]).map((t,i)=>`<span class="token" data-pos="${i}" title="position ${i}">${esc(t)}</span>`).join(' ');if(!generated)document.querySelectorAll('.token').forEach(el=>{el.onmouseenter=()=>focusToken(+el.dataset.pos);el.onclick=()=>focusToken(+el.dataset.pos)});const output=d.generated_tokens||[];$('generated-text').textContent=d.generated_text||'';$('generated-meta').textContent=output.length?`${output.length} generated tokens · token ID와 tokenizer token piece를 순서대로 표시`:'이 수집 세션에는 생성 토큰 기록이 없습니다.';$('generated-tokens').innerHTML=output.map(t=>`<span class="generated-token ${t.index===targetIndex?'active':''}" title="token id ${t.id??'—'} · output position ${t.index}">#${t.index} [${t.id??'—'}] ${esc(t.piece??'')}</span>`).join(' ');document.querySelector('.generated-token.active')?.scrollIntoView({block:'nearest'})}
async function focusToken(pos){viewMode='token';$('token-position').value=pos;$('offset').value=0;document.querySelectorAll('.token').forEach(x=>x.classList.toggle('active',+x.dataset.pos===pos));await loadValues();drawHeatmap(selected,pos)}

/* ---------- heatmap: diverging blue ↔ gray(0) ↔ red when values straddle 0, otherwise sequential ---------- */
async function drawHeatmap(key,position=-1){const d=await(await fetch('/api/heatmap?key='+encodeURIComponent(key))).json();if(d.error){$('heatmap-meta').textContent=d.error;return}lastHeat=d;lastHeatPos=position;renderHeatmap(d,position)}
function heatRange(a){let lo=Infinity,hi=-Infinity;for(const v of a){if(Number.isFinite(v)){lo=Math.min(lo,v);hi=Math.max(hi,v)}}if($('heatmap-scale').value==='robust'&&a.length>20){const sorted=Float64Array.from(a.filter(Number.isFinite)).sort(),q=p=>sorted[Math.min(sorted.length-1,Math.max(0,Math.floor(p*(sorted.length-1))))];lo=q(.005);hi=q(.995)}if(!(hi>lo))hi=lo+1;return{lo,hi}}
function renderHeatmap(d,position=-1){$('heatmap-meta').textContent=d.generated_token_piece===undefined?'Prompt token sequence':`출력 token #${d.generated_token_index}: ${d.generated_token_piece} · 활성값 source token: ${d.source_token_piece??'—'}`;const c=$('heatmap'),x=fitCanvas(c),s=c._s,w=c.width,h=c.height;const a=d.values,rows=d.rows,cols=d.cols;if(!rows||!cols)return;
 let{lo,hi}=heatRange(a);const neg=hexRgb(cssVar('--div-neg')),pos=hexRgb(cssVar('--div-pos')),mid=hexRgb(cssVar('--div-mid')),sLo=hexRgb(cssVar('--seq-lo')),sHi=hexRgb(cssVar('--seq-hi'));const diverging=lo<0&&hi>0,m=Math.max(Math.abs(lo),Math.abs(hi));if(diverging){lo=-m;hi=m}const span=hi-lo;
 const color=v=>{if(diverging){const t=Math.max(-1,Math.min(1,v/m));return t>=0?mix(mid,pos,t):mix(mid,neg,-t)}return mix(sLo,sHi,Math.max(0,Math.min(1,(v-lo)/span)))};
 const im=x.createImageData(cols,rows);for(let i=0;i<a.length;i++){const[r,g,b]=color(a[i]),p=i*4;im.data[p]=r;im.data[p+1]=g;im.data[p+2]=b;im.data[p+3]=255}const tmp=document.createElement('canvas');tmp.width=cols;tmp.height=rows;tmp.getContext('2d').putImageData(im,0,0);x.imageSmoothingEnabled=false;x.drawImage(tmp,0,0,w,h);
 if(position>=0&&d.token_count){const px=position/d.token_count*w,bw=Math.max(3*s,w/d.token_count);x.lineWidth=3*s;x.strokeStyle='#000';x.strokeRect(px,s,bw,h-2*s);x.lineWidth=1.5*s;x.strokeStyle=cssVar('--highlight');x.strokeRect(px,s,bw,h-2*s)}
 const rgb=v=>`rgb(${v.join(',')})`;$('hm-lo').textContent=fmt(lo);$('hm-hi').textContent=fmt(hi);$('hm-bar').style.background=diverging?`linear-gradient(90deg,${rgb(neg)},${rgb(mid)},${rgb(pos)})`:`linear-gradient(90deg,${rgb(sLo)},${rgb(sHi)})`;$('hm-desc').textContent=`${diverging?'발산형 · 0 = 회색':'순차형'} · ${$('heatmap-scale').value==='robust'?'0.5–99.5% 분위 클리핑':'전체 min–max'} · ${d.token_count} tokens × ${d.feature_count??'?'} features`;
 c.onclick=ev=>{if(d.generated_token_piece!==undefined)return;const rect=c.getBoundingClientRect(),pos=Math.floor((ev.clientX-rect.left)/rect.width*d.token_count);focusToken(pos)};
 c.onmousemove=ev=>{const p=canvasPoint(c,ev),col=Math.min(cols-1,Math.max(0,Math.floor(p.fx*cols))),row=Math.min(rows-1,Math.max(0,Math.floor(p.fy*rows))),tok=Math.min(d.token_count-1,Math.max(0,Math.floor(p.fx*d.token_count))),piece=d.generated_token_piece===undefined?promptPieces[tok]:undefined;showTip(ev,`<b>value ${esc(fmt(a[row*cols+col]))}</b>\ntoken ≈ ${tok}${piece!==undefined?' · '+esc(JSON.stringify(piece)):''}\nfeature ≈ ${row*(d.col_step||1)}`)};c.onmouseleave=hideTip}
$('heatmap-scale').onchange=()=>{if(lastHeat)renderHeatmap(lastHeat,lastHeatPos)};

/* ---------- element values ---------- */
let viewMode='token';async function loadValues(sort=''){if(!selected)return;const offset=Math.max(0,Number($('offset').value)||0),pos=Math.max(0,Number($('token-position').value)||0),r=await fetch(`/api/tensor?key=${encodeURIComponent(selected)}&offset=${offset}&limit=256&position=${pos}&view=${viewMode}&sort=${sort}`),data=await r.json();if(data.error){$('value-meta').textContent=data.error;return}$('values').innerHTML=data.values.map((item,i)=>{const v=typeof item==='object'?item.value:item,idx=typeof item==='object'?item.index:data.offset+i,hot=typeof item==='object'&&item.outlier;return `<tr><td class="num">${idx}</td><td class="num ${hot?'outlier':''}">${esc(v)}</td></tr>`}).join('');const tokenLabel=data.generated_token_piece===undefined?`prompt token ${pos}`:`출력 token #${data.generated_token_index} ${data.generated_token_piece} ← 입력 ${data.source_token_piece??'—'} @ position ${pos}`;$('value-meta').textContent=`${data.offset}–${data.offset+data.values.length} / ${data.numel.toLocaleString()} · ${data.view==='token'?tokenLabel+' feature':'전체 tensor flat index'} · ${JSON.stringify(data.shape)} · ${data.sorted?'값 정렬':'index 순'} · 빨강 ● = outlier`;if(lastEmbed)renderEmbedding(lastEmbed)}
function drawHist(canvasId,hist,title){const c=$(canvasId),x=fitCanvas(c),g=histPanel(x,c._s,0,c.width,c.height,hist,{title});c.onmousemove=ev=>histTip(ev,g,canvasPoint(c,ev),hist);c.onmouseleave=hideTip}

/* ---------- embedding: point shade = token order, ring = current token ---------- */
async function embedding(method){if(!selected)return;$('embedding-meta').textContent=`${method.toUpperCase()} 계산 중…`;const d=await(await fetch(`/api/embedding?key=${encodeURIComponent(selected)}&method=${method}`)).json();if(d.error){$('embedding-meta').textContent=d.error;return}d.method=method;lastEmbed=d;renderEmbedding(d)}
function renderEmbedding(d){$('embedding-meta').textContent=`${d.method.toUpperCase()} · ${d.points.length} tokens · 색 농도 = token 순서 (앞 → 뒤)`;const c=$('embedding'),x=fitCanvas(c),s=c._s,w=c.width,h=c.height,pad=16*s;if(!d.points.length)return;const xs=d.points.map(p=>p.x),ys=d.points.map(p=>p.y),xmin=Math.min(...xs),xmax=Math.max(...xs),ymin=Math.min(...ys),ymax=Math.max(...ys);const px=p=>pad+(p.x-xmin)/(xmax-xmin||1)*(w-2*pad),py=p=>pad+(p.y-ymin)/(ymax-ymin||1)*(h-2*pad);const lo=hexRgb(cssVar('--seq-lo')),hi=hexRgb(cssVar('--seq-hi')),ring=cssVar('--surface-2'),n=Math.max(1,d.points.length-1);
 d.points.forEach((p,i)=>{x.fillStyle=`rgb(${mix(lo,hi,.3+.7*i/n).join(',')})`;x.strokeStyle=ring;x.lineWidth=1.5*s;x.beginPath();x.arc(px(p),py(p),4.5*s,0,7);x.fill();x.stroke()});
 const cur=Number($('token-position').value),sel=d.points.find(p=>p.token_index===cur);if(sel){x.strokeStyle=cssVar('--highlight');x.lineWidth=2.5*s;x.beginPath();x.arc(px(sel),py(sel),9*s,0,7);x.stroke()}
 const nearest=ev=>{const q=canvasPoint(c,ev);let best=d.points[0],bd=Infinity;for(const p of d.points){const dd=(px(p)-q.x)**2+(py(p)-q.y)**2;if(dd<bd){bd=dd;best=p}}return{best,bd}};
 c.onclick=ev=>focusToken(nearest(ev).best.token_index);
 c.onmousemove=ev=>{const{best,bd}=nearest(ev);if(bd>(20*s)**2){hideTip();return}const piece=promptPieces[best.token_index];showTip(ev,`<b>token ${best.token_index}</b>${piece!==undefined?'\n'+esc(JSON.stringify(piece)):''}\n(${fmt(best.x)}, ${fmt(best.y)})`)};c.onmouseleave=hideTip}

/* ---------- A/B compare ---------- */
let compareA=null,compareB=null;function histFor(key,id,label){fetch('/api/plot?key='+encodeURIComponent(key)).then(r=>r.json()).then(d=>{const hist=d.histogram||[];if(id==='chart-a')histA=hist;else histB=hist;drawHist(id,hist,label)})}
function updateAbCount(){$('ab-count').textContent=compareA||compareB?`(${compareA?'A':'–'} / ${compareB?'B':'–'})`:''}
async function compare(){if(!compareA||!compareB){$('compare-meta').textContent='A와 B 레코드를 지정하세요.';return}$('compare-meta').textContent='계산 중…';const d=await(await fetch(`/api/compare?a=${encodeURIComponent(compareA)}&b=${encodeURIComponent(compareB)}`)).json();if(d.error){$('compare-meta').textContent=d.error;return}histA=d.histogram_a;histB=d.histogram_b;drawHist('chart-a',histA,'A 분포');drawHist('chart-b',histB,'B 분포');lastCompare=d;renderDelta(d);$('compare-metrics').innerHTML=[['L2 distance',d.l2],['Cosine similarity',d.cosine_similarity],['Mean |A−B|',d.mean_abs_delta],['Max |A−B|',d.max_abs_delta]].map(([a,b])=>`<div class="metric"><b>${a}</b><span class="mono">${esc(b)}</span></div>`).join('');$('compare-meta').textContent=`공통 shape ${JSON.stringify(d.shape)} · 상위 dimension delta (빨강 A>B, 파랑 A<B)`}
function renderDelta(d){const c=$('delta-chart'),x=fitCanvas(c),s=c._s,w=c.width,h=c.height,left=60*s,right=12*s,ds=d.top_dimensions||[],max=Math.max(1e-12,...ds.map(v=>Math.abs(v.delta))),mid=Math.round(h/2)+.5,half=h/2-12*s,bw=(w-left-right)/Math.max(1,ds.length),gap=bw>4*s?2*s:0;
 x.strokeStyle=cssVar('--line-strong');x.lineWidth=s;x.beginPath();x.moveTo(left,mid);x.lineTo(w-right,mid);x.stroke();x.fillStyle=cssVar('--muted');x.textAlign='right';x.fillText('+'+fmt(max),left-6*s,mid-half);x.fillText('0',left-6*s,mid);x.fillText('−'+fmt(max),left-6*s,mid+half);x.textAlign='left';
 ds.forEach((v,i)=>{const bar=Math.abs(v.delta)/max*half;x.fillStyle=v.delta>=0?cssVar('--div-pos'):cssVar('--div-neg');x.fillRect(left+i*bw+gap/2,v.delta>=0?mid-bar:mid,Math.max(1,bw-gap),bar)});
 c.onmousemove=ev=>{const p=canvasPoint(c,ev),i=Math.floor((p.x-left)/bw);if(i<0||i>=ds.length){hideTip();return}showTip(ev,`<b>dimension ${ds[i].dimension}</b>\nA − B = ${fmt(ds[i].delta)}`)};c.onmouseleave=hideTip}

/* ---------- wiring ---------- */
for(const [id,sort] of [['load-values',''],['sort-high','value_desc'],['sort-low','value_asc']])$(id).onclick=()=>loadValues(sort);$('all-values').onclick=()=>{viewMode='all';$('offset').value=0;loadValues()};$('token-position').onchange=()=>{viewMode='token';$('offset').value=0;loadValues()};$('pca').onclick=()=>embedding('pca');$('tsne').onclick=()=>embedding('tsne');$('set-a').onclick=()=>{compareA=selected;if(selected){$('label-a').textContent=selected;histFor(selected,'chart-a','A 분포')}updateAbCount()};$('set-b').onclick=()=>{compareB=selected;if(selected){$('label-b').textContent=selected;histFor(selected,'chart-b','B 분포')}updateAbCount()};$('compare').onclick=compare;
for(const id of ['run','layer','phase','risk','kind'])$(id).onchange=filterRows;$('date').onchange=()=>{$('run').value='';filterRows()};let searchTimer=null;$('search').oninput=()=>{clearTimeout(searchTimer);searchTimer=setTimeout(filterRows,250)};$('refresh').onclick=refresh;$('prev').onclick=()=>{if(page>0){page--;refresh()}};$('next').onclick=()=>{if((page+1)*pageSize<total){page++;refresh()}};
$('reset-filters').onclick=()=>{for(const id of ['date','run','layer','phase','risk'])$(id).value='';$('kind').value='tensor';$('search').value='';filterRows()};
document.addEventListener('keydown',ev=>{if($('view-analysis').hidden||ev.target.closest('input,select,textarea')||!['ArrowDown','ArrowUp'].includes(ev.key)||!all.length)return;ev.preventDefault();const i=all.findIndex(r=>r.key===selected),next=ev.key==='ArrowDown'?Math.min(all.length-1,i+1):Math.max(0,i-1);selectRecord(all[next].key)});
refresh();timer=setInterval(refresh,3000);
$('sandbox-import').onclick=async()=>{const file=$('sandbox-file').files[0],status=$('sandbox-import-status');if(!file){status.textContent='먼저 업로드할 파일을 선택하세요.';return}status.textContent=`업로드 및 Sandbox import 중: ${file.name} (${file.size.toLocaleString()} bytes)`;$('sandbox-import').disabled=true;try{const response=await fetch('/api/sandbox/import',{method:'POST',headers:{'Content-Type':'application/octet-stream','X-Filename':encodeURIComponent(file.name)},body:file});const result=await response.json();if(!response.ok||result.status!=='IMPORTED')throw Error(result.reason||result.error||`HTTP ${response.status}`);const importedBytes=result.bytes??result.payload_bytes;const sizeLabel=typeof importedBytes==='number'&&Number.isFinite(importedBytes)?` · ${importedBytes.toLocaleString()} bytes`:'';status.textContent=result.excluded?.length?`Import 완료 · 제외된 파일: ${result.excluded.join(', ')}${sizeLabel}`:`업로드 및 import 성공 · Sandbox 경로: ${result.internal_path}${sizeLabel}`}catch(error){status.textContent=`업로드/import 실패: ${error.message}`}finally{$('sandbox-import').disabled=false}};
$('sandbox-list').onclick=async()=>{const button=$('sandbox-list'),status=$('sandbox-list-status'),rows=$('sandbox-files');button.disabled=true;rows.replaceChildren();status.textContent='Sandbox 파일 조회 중…';try{const response=await fetch('/api/sandbox/files',{cache:'no-store'}),result=await response.json();if(!response.ok)throw Error(result.reason||result.error||`HTTP ${response.status}`);if(result.status==='STOPPED'){status.textContent='Sandbox가 실행 중이 아닙니다.';return}const kinds={file:'파일',directory:'폴더',symlink:'심볼릭 링크',other:'기타'};rows.innerHTML=result.entries.map(entry=>`<tr><td>${entry.kind==='file'?`<button type="button" data-sandbox-path="${esc(entry.path)}">${esc(entry.path)}</button>`:esc(entry.path)}</td><td>${esc(kinds[entry.kind]||entry.kind)}</td><td class="num">${entry.size==null?'—':esc(entry.size.toLocaleString())}</td></tr>`).join('');status.textContent=`${result.root} · ${result.entries.length}개 항목 · ${new Date().toLocaleTimeString()}${result.truncated?' · 최대 1,000개까지만 표시':result.entries.length?'':' · 비어 있습니다'}`}catch(error){status.textContent=`파일 조회 실패: ${error.message}`}finally{button.disabled=false}};
let sandboxPreviewRequest=0;
$('sandbox-files').onclick=async event=>{
 const button=event.target.closest('button[data-sandbox-path]');if(!button)return;
 const path=button.dataset.sandboxPath,current=++sandboxPreviewRequest,status=$('sandbox-preview-status'),preview=$('sandbox-preview'),image=$('sandbox-image');
 image.onload=null;image.onerror=null;image.hidden=true;image.removeAttribute('src');preview.hidden=false;preview.textContent='';status.textContent=`${path} · 불러오는 중…`;
 try{
  const response=await fetch('/api/sandbox/file?'+new URLSearchParams({path}),{cache:'no-store'}),result=await response.json();
  if(current!==sandboxPreviewRequest)return;
  if(!response.ok)throw Error(result.reason||result.error||`HTTP ${response.status}`);
  const label=`${result.path} · ${result.size.toLocaleString()} bytes`;
  if(result.mime&&['image/png','image/jpeg','image/gif','image/webp','image/bmp','image/x-icon','image/avif'].includes(result.mime)){
   preview.hidden=true;
   status.textContent=label+' · 이미지 불러오는 중…';
   image.onload=()=>{if(current!==sandboxPreviewRequest)return;image.hidden=false;status.textContent=label+` · ${image.naturalWidth} × ${image.naturalHeight}`};
   image.onerror=()=>{if(current!==sandboxPreviewRequest)return;image.hidden=true;status.textContent=label+' · 이미지가 손상되었거나 브라우저에서 지원하지 않는 형식입니다.'};
   image.alt=result.path;image.src='/api/sandbox/image?'+new URLSearchParams({path,request:String(current)});
  }else{
   status.textContent=label+(result.binary?' · 바이너리 또는 UTF-8이 아닌 파일은 미리볼 수 없습니다.':result.truncated?' · 처음 64 KiB만 표시':result.size===0?' · 빈 파일':'');preview.textContent=result.content;
  }
 }catch(error){if(current===sandboxPreviewRequest)status.textContent=`${path} · 조회 실패: ${error.message}`}
};
/* ---------- SANDBOX WEB / FakeNet routes and site files ---------- */
let swFiles=[];
async function swLoad(){const status=$('sw-status');status.textContent='FakeNet 설정과 요청 기록을 불러오는 중…';try{const r=await fetch('/api/sandbox/web',{cache:'no-store'}),d=await r.json();if(!r.ok)throw Error(d.error||d.reason||`HTTP ${r.status}`);$('sw-routes').value=JSON.stringify(d.config,null,2);swFiles=d.files||[];const select=$('sw-file'),previous=select.value;select.innerHTML='<option value="">파일 선택</option>'+swFiles.map(f=>`<option value="${esc(f)}">${esc(f)}</option>`).join('');if(swFiles.includes(previous))select.value=previous;else if(swFiles.length)select.value=swFiles[0];if(select.value)await swReadFile();$('sw-events').innerHTML=(d.events||[]).slice(-300).reverse().map(e=>`<tr><td>${esc(e.time?new Date(e.time*1000).toLocaleString():'—')}</td><td>${esc(e.kind)}</td><td class="mono">${esc([e.method,e.host,e.path].filter(Boolean).join(' '))}</td><td class="num">${esc(e.status??'—')}</td></tr>`).join('')||'<tr><td colspan="4"><div class="empty">요청 기록이 없습니다.</div></td></tr>';status.textContent=`${d.config_path} · ${swFiles.length}개 사이트 파일 · 요청 ${d.events?.length||0}건${d.log_status&&d.log_status!=='OK'?' · '+d.log_status:''}`}catch(e){status.textContent='FakeNet 조회 실패: '+e.message}}
async function swReadFile(){const name=$('sw-file').value;if(!name)return;$('sw-file-status').textContent='파일 불러오는 중…';try{const r=await fetch('/api/sandbox/web/file?name='+encodeURIComponent(name),{cache:'no-store'}),d=await r.json();if(!r.ok)throw Error(d.error||`HTTP ${r.status}`);$('sw-content').value=d.content;$('sw-file-status').textContent=`${name} · ${d.size.toLocaleString()} bytes`;$('sw-preview').srcdoc=d.content}catch(e){$('sw-file-status').textContent='파일 조회 실패: '+e.message}}
$('sw-refresh').onclick=swLoad;$('sw-file').onchange=swReadFile;$('sw-save-routes').onclick=async()=>{const status=$('sw-status');try{const config=JSON.parse($('sw-routes').value),r=await fetch('/api/sandbox/web/routes',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(config)}),d=await r.json();if(!r.ok)throw Error(d.error||`HTTP ${r.status}`);status.textContent='라우트 저장 완료 · 실행 중 FakeNet에 즉시 반영됩니다.';await swLoad()}catch(e){status.textContent='라우트 저장 실패: '+e.message}};
$('sw-preview-route').onclick=async()=>{const status=$('sw-preview-status');try{const p=new URLSearchParams({host:$('sw-host').value,path:$('sw-path').value}),r=await fetch('/api/sandbox/web/preview?'+p,{cache:'no-store'}),d=await r.json();if(!r.ok)throw Error(d.error||`HTTP ${r.status}`);status.textContent=`${d.status} · ${d.content_type} · route ${d.route_index}`;$('sw-response-preview').textContent=d.body;$('sw-preview').srcdoc=d.content_type.includes('html')?d.body:''}catch(e){status.textContent='미리보기 실패: '+e.message}};
$('sw-new-file').onclick=()=>{const name=prompt('새 파일 경로 (예: example/index.html)');if(!name)return;const option=document.createElement('option');option.value=name;option.textContent=name;$('sw-file').append(option);$('sw-file').value=name;$('sw-content').value='<!doctype html>\n<html><head><meta charset="utf-8"><title>FakeNet</title></head><body><h1>FakeNet page</h1></body></html>\n';$('sw-file-status').textContent='새 파일 · 저장하면 Sandbox/fakenet/sites/에 생성됩니다.';$('sw-preview').srcdoc=$('sw-content').value};
$('sw-save-file').onclick=async()=>{const name=$('sw-file').value;if(!name){$('sw-file-status').textContent='저장할 파일을 선택하거나 새로 만드세요.';return}try{const r=await fetch('/api/sandbox/web/file',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({name,content:$('sw-content').value})}),d=await r.json();if(!r.ok)throw Error(d.error||`HTTP ${r.status}`);$('sw-preview').srcdoc=$('sw-content').value;$('sw-file-status').textContent=`저장 완료 · ${name} · ${d.size.toLocaleString()} bytes`;if(!swFiles.includes(name))swFiles.push(name)}catch(e){$('sw-file-status').textContent='파일 저장 실패: '+e.message}};
/* ---------- recorded Hook registration map ---------- */
let hookLoaded=false,hookOffset=0,hookSessionRequest=0,hookMapRequest=0,hookData=null,hookLayer='*',hookSelected=null;
const hookPageSize=50;
const hookStateLabel={called:'● 호출 확인',not_called:'○ 등록 · 미호출',pending:'◌ 호출 정보 대기'};
function clearHookMap(){hookData=null;hookSelected=null;$('hook-metrics').replaceChildren();$('hook-overview').replaceChildren();$('hook-tree').innerHTML='<div class="hook-empty">표시할 등록 정보가 없습니다.</div>';$('hook-detail').innerHTML='<div class="hook-empty">모듈을 선택하세요.</div>';$('hook-source').textContent=''}
async function loadHookSessions(){
 const current=++hookSessionRequest;++hookMapRequest;hookLoaded=true;$('hook-status').textContent='수집 세션 조회 중…';
 try{
  const p=new URLSearchParams({q:$('hook-session-search').value,offset:String(hookOffset),limit:String(hookPageSize)});
  const response=await fetch('/api/hooks/sessions?'+p,{cache:'no-store'}),data=await response.json();
  if(current!==hookSessionRequest)return;if(!response.ok)throw Error(data.error||`HTTP ${response.status}`);
  const select=$('hook-session'),previous=select.value;
  select.replaceChildren(...data.sessions.map(s=>{const option=document.createElement('option');option.value=String(s.id);option.textContent=`${s.started_at} · ${s.phase||'phase 미기록'} · ${s.artifact_dir} · ${s.task_text||'Task 미기록'}`;return option}));
  if(data.sessions.some(s=>String(s.id)===previous))select.value=previous;
  $('hook-prev').disabled=hookOffset===0;$('hook-next').disabled=hookOffset+data.sessions.length>=data.total;
  $('hook-page').textContent=data.total?`${hookOffset+1}–${hookOffset+data.sessions.length} / ${data.total}개`:'0개';
  if(!data.sessions.length){clearHookMap();$('hook-status').textContent='조건에 맞는 수집 기록이 없습니다. Hook 수집 후 새로고침해 주세요.';return}
  await loadHookMap();
 }catch(error){if(current!==hookSessionRequest)return;clearHookMap();$('hook-status').textContent='수집 세션 조회 실패: '+error.message}
}
async function loadHookMap(){
 const current=++hookMapRequest,id=$('hook-session').value;if(!id)return;
 const previous=hookData?.session.id;const selectedPath=hookSelected;
 clearHookMap();$('hook-status').textContent='Hook 등록 위치 조회 중…';
 try{
  const response=await fetch('/api/hooks/map?'+new URLSearchParams({session:id}),{cache:'no-store'}),data=await response.json();
  if(current!==hookMapRequest)return;if(!response.ok)throw Error(data.error||`HTTP ${response.status}`);
  hookData=data;if(String(previous)!==id)hookLayer='*';hookSelected=data.modules.some(m=>m.path===selectedPath)?selectedPath:null;
  const lifecycle={running:'수집 중으로 기록됨',complete:'수집 완료',failed:'수집 실패'};
  $('hook-status').textContent=`${data.identity.model_id||data.model_type||'모델 미기록'} · ${data.session.phase||'phase 미기록'} · ${lifecycle[data.status]||data.status} · ${data.session.task_text||'Task 미기록'}`;
  $('hook-metrics').innerHTML=[['등록 모듈',data.totals.registered],['호출 확인 모듈',data.totals.called],['등록 · '+(data.status==='running'?'호출 대기':'미호출'),data.totals.registered-data.totals.called],['Tensor 기록 (manifest)',data.totals.tensors]].map(([label,value])=>`<div class="metric"><b>${esc(label)}</b>${esc(value?.toLocaleString()??'—')}</div>`).join('');
  $('hook-source').textContent=`등록 근거: ${data.source} · Layer 설정: ${JSON.stringify(data.selected_layers)} · 블록 외 모듈: ${data.include_non_block?'포함':'제외'} · shape/입출력 관찰은 인덱스 대상 Layer ${data.indexed_layers.join(', ')} 기준. 수집 중 manifest 통계는 마지막 저장 시점 기준입니다.`;
  renderHookMap();
 }catch(error){if(current!==hookMapRequest)return;clearHookMap();$('hook-status').textContent='Hook 지도 조회 실패: '+error.message}
}
function renderHookMap(){
 if(!hookData)return;
 const modules=hookData.modules,layers=[...new Set(modules.filter(m=>m.layer!==null).map(m=>m.layer))].sort((a,b)=>a-b);
 const groups=[['*','전체 등록 모듈'],...layers.map(layer=>[String(layer),`Layer ${layer}`])];if(modules.some(m=>m.layer===null))groups.push(['outside','블록 외 모듈']);
 const inLayer=m=>hookLayer==='*'||(hookLayer==='outside'?m.layer===null:String(m.layer)===hookLayer);
 $('hook-overview').innerHTML=groups.map(([key,label])=>{const nodes=modules.filter(m=>key==='*'||(key==='outside'?m.layer===null:String(m.layer)===key));return `<button type="button" class="hook-layer" data-hook-layer="${esc(key)}" aria-pressed="${key===hookLayer}"><b>${esc(label)}</b><small>${nodes.length}개 등록 · ${nodes.filter(m=>m.calls>0).length}개 호출</small></button>`}).join('');
 const query=$('hook-module-search').value.trim().toLowerCase();
 const filtered=modules.filter(m=>inLayer(m)&&(!query||(m.path+' '+m.class).toLowerCase().includes(query)));
 const paths=new Set(filtered.map(m=>m.path)),children=new Map();
 for(const m of filtered){const parent=paths.has(m.parent)?m.parent:null;if(!children.has(parent))children.set(parent,[]);children.get(parent).push(m)}
 function branch(parent){return(children.get(parent)||[]).map(m=>`<div class="hook-branch"><button type="button" class="hook-node" data-hook-path="${esc(m.path)}" aria-pressed="${m.path===hookSelected}"><span class="hook-port" title="입력 pre-hook">PRE</span><span class="hook-node-name"><b>${esc(m.path)}</b><small>${esc(m.class)} · ${m.calls.toLocaleString()}회 호출</small></span><span class="hook-state ${m.status}">${hookStateLabel[m.status]}</span><span class="hook-port out" title="출력 forward hook">POST</span></button>${children.has(m.path)?`<div class="hook-children">${branch(m.path)}</div>`:''}</div>`).join('')}
 $('hook-tree').innerHTML=branch(null)||'<div class="hook-empty">조건에 맞는 모듈이 없습니다.</div>';
 if(!filtered.some(m=>m.path===hookSelected))hookSelected=filtered[0]?.path||null;
 document.querySelectorAll('[data-hook-path]').forEach(button=>button.setAttribute('aria-pressed',String(button.dataset.hookPath===hookSelected)));
 renderHookDetail();
}
function renderHookDetail(){
 const m=hookData?.modules.find(m=>m.path===hookSelected);
 if(!m){$('hook-detail').innerHTML='<div class="hook-empty">모듈을 선택하세요.</div>';return}
 const status=hookStateLabel[m.status],indexAvailable=hookData.indexed_layers.includes(m.layer);
 $('hook-detail').innerHTML=`<h3 class="hook-detail-path">${esc(m.path)}</h3><p class="status">${esc(m.class)} · ${esc(status)}</p>
 <div class="hook-boundary"><span class="hook-port">PRE · 입력</span><span aria-hidden="true">→</span><strong>${esc(m.path.split('.').pop())}</strong><span aria-hidden="true">→</span><span class="hook-port out">POST · 출력</span></div>
 <div class="metrics"><div class="metric"><b>모듈 호출</b>${m.calls.toLocaleString()}</div><div class="metric"><b>입력 leaf 기록</b>${indexAvailable?m.inputs.toLocaleString():'인덱스 범위 밖'}</div><div class="metric"><b>출력 leaf 기록</b>${indexAvailable?m.outputs.toLocaleString():'인덱스 범위 밖'}</div><div class="metric"><b>미완료 호출 (manifest)</b>${esc(m.unfinished_calls)}</div></div>
 <p class="hook-note"><code>register_forward_pre_hook</code>: args / kwargs의 각 leaf를 기록합니다.<br><code>register_forward_hook</code>: 반환값의 각 leaf를 기록합니다. 하나의 호출에서 여러 tensor가 기록될 수 있습니다.</p>
 <h3>최근 관찰 shape · 위치별 마지막 레코드</h3>
 ${m.samples.length?`<div class="tablewrap"><table class="hook-locations"><thead><tr><th>위치 / 의미</th><th>Shape / Dtype</th></tr></thead><tbody>${m.samples.map(sample=>`<tr><td><code>${esc(sample.location)}</code><br><small>${esc(sample.meaning)} · call ${esc(sample.call_index)}</small></td><td>${esc(sample.kind==='tensor'?JSON.stringify(sample.shape):'Non-tensor')}<br><small>${esc(sample.dtype)}</small></td></tr>`).join('')}</tbody></table></div>`:`<p class="hook-note">${!indexAvailable?'이 모듈은 등록 목록에는 있지만 기존 tensor 인덱스의 Layer 범위 밖에 있습니다.':m.status==='not_called'?'Hook은 등록됐지만 이 수집에서 모듈이 호출되지 않았습니다.':'아직 인덱스에 관찰 레코드가 없습니다. 새로고침으로 확인하세요.'}</p>`}`;
}
$('hook-refresh').onclick=loadHookSessions;$('hook-session').onchange=loadHookMap;
$('hook-prev').onclick=()=>{hookOffset=Math.max(0,hookOffset-hookPageSize);loadHookSessions()};$('hook-next').onclick=()=>{hookOffset+=hookPageSize;loadHookSessions()};
let hookSearchTimer=null;$('hook-session-search').oninput=()=>{clearTimeout(hookSearchTimer);hookSearchTimer=setTimeout(()=>{hookOffset=0;loadHookSessions()},250)};
$('hook-module-search').oninput=renderHookMap;
$('hook-overview').onclick=event=>{const button=event.target.closest('[data-hook-layer]');if(button){hookLayer=button.dataset.hookLayer;renderHookMap()}};
$('hook-tree').onclick=event=>{const button=event.target.closest('[data-hook-path]');if(button){hookSelected=button.dataset.hookPath;document.querySelectorAll('[data-hook-path]').forEach(node=>node.setAttribute('aria-pressed',String(node.dataset.hookPath===hookSelected)));renderHookDetail()}};
/* ---------- token view: one generated token → hidden states at layers 0 / 11 / 23 ---------- */
let tvLoaded=false,tvOffset=0,tvSessionReq=0,tvReq=0,tvDetailReq=0,tvValueReq=0,tvSession=null,tvTraj=null,tvToken=null,tvDetail=null,tvRecLayer=null,tvRecLoc=null,tvHeatLayer=null,tvValueKey=null,tvValueOffset=0,tvValueSort='',tvCards={},tvPendingToken=null;
const tvPageSize=50,tvLayerVar=['--series-1','--series-2','--series-3'];
const tvMetricLabel={l2:'L2 norm',cos_prev:'이전 토큰과 cosine',std:'표준편차',max_abs:'max |x|',mean:'평균'};
const tvSortLabel={'':'index 순',value_desc:'값 내림차순',value_asc:'값 오름차순',abs_desc:'|값| 내림차순'};
function tvLayerColor(i){return cssVar(tvLayerVar[i]||'--series-1')}
function tvTokText(t){return t?.text??t?.piece??''}
function tvShow(text){return JSON.stringify(String(text??'')).slice(1,-1)}
function tvFmt(v){return v==null?'—':fmt(v)}
function tvLocLabel(){return $('tv-loc').selectedOptions[0]?.textContent||''}
async function tvJson(url){const r=await fetch(url,{cache:'no-store'}),d=await r.json();if(!r.ok||d.error)throw Error(d.error||`HTTP ${r.status}`);return d}
function tvEnsureLoaded(){if(!tvLoaded){tvLoaded=true;tvLoadSessions()}}
function tvLayerButtons(id,current){$(id).innerHTML=(tvSession?.layers||[]).map((L,i)=>`<button type="button" data-layer="${L}" aria-pressed="${L===current}"><span class="tv-key" style="background:var(${tvLayerVar[i]})"></span>Layer ${L}</button>`).join('')}
async function tvLoadSessions(){const cur=++tvSessionReq;$('tv-status').textContent='생성 세션 조회 중…';
 try{const d=await tvJson('/api/tokens/sessions?'+new URLSearchParams({q:$('tv-search').value,offset:String(tvOffset),limit:String(tvPageSize)}));if(cur!==tvSessionReq)return;
  const sel=$('tv-session'),prev=sel.value;sel.innerHTML=d.sessions.map(s=>`<option value="${s.id}">${esc(s.started_at)} · ${esc(s.artifact_dir.replace('/generation/',' / '))} · ${s.token_count} tokens · ${esc(s.task_text||'Task 미기록')}</option>`).join('');
  if(d.sessions.some(s=>String(s.id)===prev))sel.value=prev;
  $('tv-prev-page').disabled=tvOffset===0;$('tv-next-page').disabled=tvOffset+d.sessions.length>=d.total;$('tv-page').textContent=d.total?`${tvOffset+1}–${tvOffset+d.sessions.length} / ${d.total}`:'0개';
  if(!d.sessions.length){$('tv-status').textContent='생성 토큰 매핑이 기록된 generation 세션이 없습니다.';return}
  await tvLoadSession()}catch(e){if(cur===tvSessionReq)$('tv-status').textContent='세션 조회 실패: '+e.message}}
async function tvLoadSession(){const id=$('tv-session').value;if(!id)return;const cur=++tvReq;$('tv-status').textContent='세션 불러오는 중…';
 try{const d=await tvJson('/api/tokens/session?session='+encodeURIComponent(id));if(cur!==tvReq)return;
  const same=tvSession&&String(tvSession.session.id)===id;tvSession=d;
  if(!same||tvPendingToken!=null){tvToken=tvPendingToken??0;tvPendingToken=null;tvRecLayer=d.layers[0];tvHeatLayer=d.layers[0];tvRecLoc=null;tvValueKey=null}
  const locSel=$('tv-loc'),prevLoc=locSel.value||d.default_location,feat=d.locations.filter(l=>l.featured),rest=d.locations.filter(l=>!l.featured);
  locSel.innerHTML=`<optgroup label="주요 잔차 · 분기 위치">${feat.map(l=>`<option value="${esc(l.key)}">${esc(l.label)}</option>`).join('')}</optgroup><optgroup label="모든 tensor 위치">${rest.map(l=>`<option value="${esc(l.key)}">${esc(l.label)}</option>`).join('')}</optgroup>`;
  locSel.value=d.locations.some(l=>l.key===prevLoc)?prevLoc:d.default_location;
  $('tv-text').textContent=d.generated_text;tvLayerButtons('tv-heat-layers',tvHeatLayer);tvLayerButtons('tv-rec-layers',tvRecLayer);
  tvToken=Math.min(tvToken??0,Math.max(0,d.tokens.length-1));tvRenderTokens();await tvLoadTrajectory();await tvSelectToken(tvToken)
 }catch(e){if(cur===tvReq)$('tv-status').textContent='세션 로드 실패: '+e.message}}
function tvRenderTokens(){if(!tvSession)return;const q=$('tv-token-filter').value.trim().toLowerCase();let hits=0;
 $('tv-tokens').innerHTML=tvSession.tokens.map((t,i)=>{const text=String(tvTokText(t)),special=/^<\|.*\|>$/.test(t.piece||''),match=!q||text.toLowerCase().includes(q)||String(t.piece||'').toLowerCase().includes(q)||String(t.id)===q;if(q&&match)hits++;
  return `<span class="tv-tok${special?' special':''}${t.partial?' partial':''}${i===tvToken?' active':''}${match?'':' dim'}" data-i="${i}" title="#${i} · id ${t.id} · piece ${esc(JSON.stringify(t.piece))}${t.partial?' · UTF-8 문자의 일부 바이트':''}">${esc(text.replace(/\n/g,'⏎\n'))}</span>`}).join('')||'<div class="empty">생성 토큰이 없습니다.</div>';
 $('tv-token-count').textContent=q?`${hits}개 일치 / ${tvSession.tokens.length}`:`${tvSession.tokens.length}개 · forward ${tvSession.tokens.length}회`}
async function tvLoadTrajectory(){if(!tvSession)return;const loc=$('tv-loc').value,sid=tvSession.session.id;$('tv-trend-meta').textContent='토큰별 값 계산 중…';
 try{const d=await tvJson('/api/tokens/trajectory?'+new URLSearchParams({session:sid,loc}));if(loc!==$('tv-loc').value||sid!==tvSession.session.id)return;tvTraj=d;tvRenderTrend();tvRenderHeat();
  $('tv-status').textContent=`${tvSession.session.artifact_dir} · 생성 토큰 ${d.token_count}개 · prompt ${tvSession.prompt_token_count} tokens · 수집된 토큰 ${d.layers.map(L=>`L${L.layer} ${L.found}`).join(' / ')} · ${tvSession.session.status}`;
  $('tv-trend-meta').textContent=`${tvLocLabel()} · ${tvMetricLabel[$('tv-metric').value]}`}catch(e){$('tv-trend-meta').textContent='추이 계산 실패: '+e.message}}
/* small multiples: one panel per layer, each with its own y-axis; shared token x-axis */
function tvRenderTrend(hover=-1){const c=$('tv-trend'),x=fitCanvas(c);if(!tvTraj){c._geom=null;return}
 const s=c._s,W=c.width,H=c.height,left=64*s,right=16*s,top=4*s,bottom=H-22*s,n=tvTraj.token_count,pw=W-left-right,gap=14*s,head=18*s,L=tvTraj.layers,ph=(bottom-top-gap*(L.length-1))/L.length-head,metric=$('tv-metric').value,xAt=i=>left+(i+.5)*pw/Math.max(1,n);
 for(const [idx,color,width] of [[hover,cssVar('--line-strong'),s],[tvToken,cssVar('--highlight'),1.5*s]]){if(idx==null||idx<0)continue;x.strokeStyle=color;x.lineWidth=width;x.beginPath();x.moveTo(Math.round(xAt(idx))+.5,top);x.lineTo(Math.round(xAt(idx))+.5,bottom);x.stroke()}
 L.forEach((layer,li)=>{const y0=top+li*(ph+head+gap)+head,vals=layer.metrics.map(m=>m?m[metric]:null),fin=vals.filter(v=>v!=null&&Number.isFinite(v));let lo=fin.length?Math.min(...fin):0,hi=fin.length?Math.max(...fin):1;if(hi===lo){hi+=Math.abs(hi)*.05||1;lo-=Math.abs(lo)*.05||1}const yAt=v=>y0+ph-(v-lo)/(hi-lo)*ph;
  x.strokeStyle=cssVar('--grid');x.lineWidth=s;x.fillStyle=cssVar('--muted');x.textAlign='right';for(const v of[lo,hi]){const y=Math.round(yAt(v))+.5;x.beginPath();x.moveTo(left,y);x.lineTo(W-right,y);x.stroke();x.fillText(fmt(v),left-6*s,y)}
  x.textAlign='left';x.fillStyle=tvLayerColor(li);x.fillRect(left,y0-head+3*s,8*s,8*s);x.fillStyle=cssVar('--text-2');x.fillText(`Layer ${layer.layer}`,left+12*s,y0-head+7*s);
  x.strokeStyle=tvLayerColor(li);x.lineWidth=2*s;x.lineJoin='round';x.beginPath();let pen=false;vals.forEach((v,i)=>{if(v==null||!Number.isFinite(v)){pen=false;return}pen?x.lineTo(xAt(i),yAt(v)):x.moveTo(xAt(i),yAt(v));pen=true});x.stroke();
  for(const idx of [hover,tvToken]){if(idx==null||idx<0||vals[idx]==null)continue;x.fillStyle=idx===tvToken?cssVar('--highlight'):tvLayerColor(li);x.strokeStyle=cssVar('--surface-2');x.lineWidth=2*s;x.beginPath();x.arc(xAt(idx),yAt(vals[idx]),4.5*s,0,7);x.fill();x.stroke()}});
 x.fillStyle=cssVar('--muted');x.textAlign='left';x.fillText('token #0',left,H-9*s);x.textAlign='right';x.fillText(`#${n-1}`,W-right,H-9*s);x.textAlign='left';
 c._geom={left,pw,n}}
function tvIndexAt(c,ev){const g=c._geom;if(!g||!g.n)return -1;const p=canvasPoint(c,ev),i=Math.floor((p.x-g.left)/g.pw*g.n);return i>=0&&i<g.n?i:-1}
function tvHeatRange(a){const fin=Float64Array.from(a.filter(Number.isFinite)).sort(),q=p=>fin[Math.min(fin.length-1,Math.max(0,Math.floor(p*(fin.length-1))))];let lo=fin.length?q(.005):0,hi=fin.length?q(.995):1;if(!(hi>lo))hi=lo+1;return{lo,hi}}
function tvRenderHeat(){const c=$('tv-heat'),x=fitCanvas(c);c._geom=null;if(!tvTraj)return;const s=c._s,W=c.width,H=c.height,left=64*s,right=16*s,pw=W-left-right,layer=tvTraj.layers.find(L=>L.layer===tvHeatLayer)||tvTraj.layers[0],h=layer?.heat;
 if(!h){$('tv-heat-desc').textContent='이 위치는 토큰마다 원소 수가 달라 heatmap을 만들 수 없습니다.';$('tv-heat-lo').textContent=$('tv-heat-hi').textContent='—';return}
 let{lo,hi}=tvHeatRange(h.values);const neg=hexRgb(cssVar('--div-neg')),pos=hexRgb(cssVar('--div-pos')),mid=hexRgb(cssVar('--div-mid')),sLo=hexRgb(cssVar('--seq-lo')),sHi=hexRgb(cssVar('--seq-hi')),div=lo<0&&hi>0,m=Math.max(Math.abs(lo),Math.abs(hi));if(div){lo=-m;hi=m}
 const a=h.values,im=x.createImageData(h.cols,h.rows);for(let i=0;i<a.length;i++){const v=a[i];const rgb=div?(v>=0?mix(mid,pos,Math.min(1,v/m)):mix(mid,neg,Math.min(1,-v/m))):mix(sLo,sHi,Math.max(0,Math.min(1,(v-lo)/(hi-lo))));const p=i*4;im.data[p]=rgb[0];im.data[p+1]=rgb[1];im.data[p+2]=rgb[2];im.data[p+3]=h.present[i%h.cols]?255:30}
 const tmp=document.createElement('canvas');tmp.width=h.cols;tmp.height=h.rows;tmp.getContext('2d').putImageData(im,0,0);x.imageSmoothingEnabled=false;x.drawImage(tmp,left,0,pw,H);
 x.fillStyle=cssVar('--muted');x.textAlign='right';x.textBaseline='top';x.fillText('dim 0',left-6*s,2*s);x.textBaseline='bottom';x.fillText(`dim ${h.width-1}`,left-6*s,H-2*s);x.textBaseline='middle';x.textAlign='left';
 if(tvToken!=null){const cw=pw/h.cols,px=left+tvToken*cw,bw=Math.max(3*s,cw);x.lineWidth=3*s;x.strokeStyle='#000';x.strokeRect(px,s,bw,H-2*s);x.lineWidth=1.5*s;x.strokeStyle=cssVar('--highlight');x.strokeRect(px,s,bw,H-2*s)}
 c._geom={left,pw,n:h.cols,h,layer:layer.layer};const rgb=v=>`rgb(${v.join(',')})`;
 $('tv-heat-lo').textContent=fmt(lo);$('tv-heat-hi').textContent=fmt(hi);$('tv-heat-bar').style.background=div?`linear-gradient(90deg,${rgb(neg)},${rgb(mid)},${rgb(pos)})`:`linear-gradient(90deg,${rgb(sLo)},${rgb(sHi)})`;
 $('tv-heat-desc').textContent=`Layer ${layer.layer} · ${div?'발산형 · 0 = 회색':'순차형'} · 0.5–99.5% 분위 클리핑 · 차원 ${h.width}개 중 ${h.dim_step}개 간격 ${h.rows}행 샘플`}
async function tvSelectToken(i){if(!tvSession||!Number.isInteger(i)||i<0||i>=tvSession.tokens.length)return;tvToken=i;const t=tvSession.tokens[i];
 document.querySelectorAll('#tv-tokens .tv-tok').forEach(el=>el.classList.toggle('active',+el.dataset.i===i));document.querySelector(`#tv-tokens .tv-tok[data-i="${i}"]`)?.scrollIntoView({block:'nearest'});
 $('tv-token-title').innerHTML=`<span class="tv-token-big">${esc(tvShow(tvTokText(t)))}</span>생성 토큰 #${i}`;
 $('tv-token-meta').textContent=`token id ${t.id??'—'} · piece ${JSON.stringify(t.piece)} · 예측 입력 "${tvShow(t.source_text??t.source_piece??'—')}" · forward ${i} — ${i===0?`prefill: prompt 마지막 위치 ${tvSession.prompt_token_count-1}의 값`:'decode: 직전 토큰 1개를 처리한 forward의 값'}`;
 $('tv-prev-token').disabled=i===0;$('tv-next-token').disabled=i>=tvSession.tokens.length-1;tvRenderTrend();tvRenderHeat();
 const cur=++tvDetailReq;
 try{const d=await tvJson(`/api/tokens/detail?session=${encodeURIComponent(tvSession.session.id)}&token=${i}`);if(cur!==tvDetailReq)return;tvDetail=d;tvRenderRecords();await tvRenderCards(cur)}
 catch(e){if(cur===tvDetailReq)$('tv-cards').innerHTML=`<div class="empty">${esc(e.message)}</div>`}}
function tvRecordAt(L,loc){return L?.records.find(r=>`${r.rel}|${r.location}`===loc&&r.stats)}
async function tvRenderCards(cur){const loc=$('tv-loc').value,label=tvLocLabel(),sid=tvSession.session.id;tvCards={};
 $('tv-cards').innerHTML=tvDetail.layers.map((L,li)=>{const r=tvRecordAt(L,loc),st=r?.stats||{},cos=tvTraj?.layers[li]?.metrics[tvToken]?.cos_prev;
  return `<div class="tv-card"><h3><span class="tv-key" style="background:var(${tvLayerVar[li]})"></span>Layer ${L.layer}<small class="muted" style="font-weight:400">${esc(label)}</small></h3>${r?`<div class="tv-stats">${[['L2',st.l2],['mean',st.mean],['std',st.std],['min',st.min],['max',st.max],['cos(이전)',cos]].map(([k,v])=>`<div title="${esc(v??'')}"><b>${k}</b><span>${tvFmt(v)}</span></div>`).join('')}</div><div class="chartbox"><canvas class="tv-spark" id="tv-spark-${L.layer}"></canvas></div><div class="axis-note"><span>index 0</span><span>${esc(JSON.stringify(r.token_shape??[st.numel]))} · 원소 ${st.numel.toLocaleString()}개</span></div><div class="tv-top" id="tv-top-${L.layer}"></div>`:'<div class="empty">이 레이어에는 해당 위치의 tensor 기록이 없습니다.</div>'}</div>`}).join('');
 await Promise.all(tvDetail.layers.map(async(L,li)=>{const r=tvRecordAt(L,loc);if(!r)return;
  try{const v=await tvJson('/api/tokens/vector?'+new URLSearchParams({session:sid,key:r.key,limit:'1'}));if(cur!==tvDetailReq)return;tvCards[L.layer]={v,li};tvRenderSpark(L.layer);
   $(`tv-top-${L.layer}`).innerHTML='<span class="status">|값| 상위</span>'+v.top.map(t=>`<code title="index ${t.index}">#${t.index} ${esc(fmt(t.value))}</code>`).join('')}catch(e){const el=$(`tv-top-${L.layer}`);if(el)el.textContent=e.message}}))}
/* per-dimension envelope (min–max per bucket) of one layer's token vector */
function drawEnvelope(c,env,numel,color,label){if(!c||!env)return;const x=fitCanvas(c),s=c._s,W=c.width,H=c.height,n=env.min.length;if(!n)return;
 const lo=Math.min(0,...env.min),hi=Math.max(0,...env.max),span=hi-lo||1,y=v=>H-2*s-(v-lo)/span*(H-4*s),bw=W/n;
 x.strokeStyle=cssVar('--line-strong');x.lineWidth=s;x.beginPath();x.moveTo(0,Math.round(y(0))+.5);x.lineTo(W,Math.round(y(0))+.5);x.stroke();
 x.fillStyle=color;for(let i=0;i<n;i++){const a=y(env.max[i]),b=y(env.min[i]);x.fillRect(i*bw,a,Math.max(1,bw-(bw>3*s?s:0)),Math.max(s,b-a))}
 c.onmousemove=ev=>{const p=canvasPoint(c,ev),i=Math.min(n-1,Math.max(0,Math.floor(p.x/bw))),b=env.bucket,end=Math.min(numel-1,(i+1)*b-1);showTip(ev,`<b>${label} · index ${i*b}${end>i*b?'–'+end:''}</b>\nmin ${fmt(env.min[i])}\nmax ${fmt(env.max[i])}`)};c.onmouseleave=hideTip}
function tvRenderSpark(layer){const card=tvCards[layer];if(card)drawEnvelope($(`tv-spark-${layer}`),card.v.envelope,card.v.numel,tvLayerColor(card.li),`Layer ${layer}`)}
function tvRenderRecords(){if(!tvDetail)return;document.querySelectorAll('#tv-rec-layers button').forEach(b=>b.setAttribute('aria-pressed',String(+b.dataset.layer===tvRecLayer)));
 const L=tvDetail.layers.find(L=>L.layer===tvRecLayer),rows=L?.records||[];
 $('tv-records').innerHTML=rows.map(r=>{const loc=`${r.rel}|${r.location}`,st=r.stats;return st?`<tr data-key="${esc(r.key)}" data-loc="${esc(loc)}" title="${esc(r.meaning||'')}"><td class="mono">${esc(r.module)}</td><td class="mono">${esc(r.location)}</td><td class="mono">${esc(JSON.stringify(r.shape))}</td><td class="num">${st.numel.toLocaleString()}</td><td class="num">${tvFmt(st.l2)}</td><td class="num">${tvFmt(st.mean)}</td><td class="num">${tvFmt(st.max_abs)}</td></tr>`:`<tr class="muted"><td class="mono">${esc(r.module)}</td><td class="mono">${esc(r.location)}</td><td colspan="5" style="white-space:normal">${esc(typeof r.value==='string'?r.value:JSON.stringify(r.value??r.dtype??'non-tensor'))}</td></tr>`}).join('')||'<tr><td colspan="7"><div class="empty">기록이 없습니다.</div></td></tr>';
 $('tv-rec-meta').textContent=`forward ${tvToken} · Layer ${tvRecLayer} · Hook 레코드 ${rows.length}개 (tensor ${rows.filter(r=>r.stats).length}개) · 행을 클릭하면 아래에 이 토큰의 원소값 표시`;
 const pick=rows.find(r=>r.stats&&`${r.rel}|${r.location}`===tvRecLoc)||tvRecordAt(L,$('tv-loc').value);if(pick){tvRecLoc=`${pick.rel}|${pick.location}`;tvValueOffset=0;tvLoadValues(pick.key)}else{tvValueKey=null;$('tv-values').innerHTML='';$('tv-value-meta').textContent='';tvVocabReset()}}
async function tvLoadValues(key){if(!key||!tvSession)return;tvValueKey=key;if(key!==tvVocabKey){tvVocabOffset=0;tvLoadVocab()}document.querySelectorAll('#tv-records tr[data-key]').forEach(tr=>tr.classList.toggle('selected',tr.dataset.key===key));document.querySelectorAll('#tv-sorts button').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.sort===tvValueSort)));const cur=++tvValueReq;
 try{const d=await tvJson('/api/tokens/vector?'+new URLSearchParams({session:tvSession.session.id,key,offset:String(tvValueOffset),limit:'256',sort:tvValueSort}));if(cur!==tvValueReq)return;const mean=d.stats.mean,std=d.stats.std;
  $('tv-values').innerHTML=d.values.map(v=>{const hot=typeof v.value==='number'&&std>0&&Math.abs(v.value-mean)>3*std;return `<tr><td class="num">${v.index}</td><td class="num ${hot?'outlier':''}">${esc(v.value)}</td></tr>`}).join('');
  $('tv-value-meta').textContent=`Layer ${d.layer} · ${d.module} · ${d.location} · 원본 ${JSON.stringify(d.shape)} → 토큰 slice ${JSON.stringify(d.token_shape)} · ${d.offset}–${d.offset+d.values.length} / ${d.numel.toLocaleString()} · ${tvSortLabel[tvValueSort]} · 빨강 ● = 이 토큰 slice 평균에서 3σ 초과`;
  $('tv-val-prev').disabled=d.offset===0;$('tv-val-next').disabled=d.offset+d.values.length>=d.numel}catch(e){if(cur===tvValueReq)$('tv-value-meta').textContent='원소값 조회 실패: '+e.message}}
/* ---------- output vocabulary projection (logit lens) of the selected token vector ---------- */
let tvVocabKey=null,tvVocabReq=0,tvVocabOffset=0,tvVocabSort='',tvVocab=null;const tvVocabLimit=100;
function tvVocabReset(){tvVocabKey=null;tvVocab=null;++tvVocabReq;$('tv-vocab-rows').innerHTML='';$('tv-vocab-summary').innerHTML='';$('tv-vocab-meta').textContent='';$('tv-vocab-page').textContent='';fitCanvas($('tv-vocab-strip'))}
async function tvLoadVocab(){const key=tvValueKey;if(!key||!tvSession)return;tvVocabKey=key;document.querySelectorAll('#tv-vocab-sorts button').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.sort===tvVocabSort)));const cur=++tvVocabReq;
 $('tv-vocab-meta').textContent='201,088개 토큰에 투영 중… (첫 계산은 lm_head 가중치를 읽느라 몇 초 걸릴 수 있습니다)';
 try{const d=await tvJson('/api/tokens/vocab?'+new URLSearchParams({session:tvSession.session.id,key,offset:String(tvVocabOffset),limit:String(tvVocabLimit),sort:tvVocabSort,q:$('tv-vocab-q').value.trim(),norm:$('tv-vocab-norm').checked?'1':'0'}));if(cur!==tvVocabReq)return;tvVocab=d;tvRenderVocab()}
 catch(e){if(cur!==tvVocabReq)return;tvVocab=null;$('tv-vocab-rows').innerHTML=`<tr><td colspan="6"><div class="empty">${esc(e.message)}</div></td></tr>`;$('tv-vocab-summary').innerHTML='';$('tv-vocab-meta').textContent='';$('tv-vocab-page').textContent='';$('tv-vocab-prev').disabled=$('tv-vocab-next').disabled=true;fitCanvas($('tv-vocab-strip'))}}
function tvVocabWord(r){return r.text==null?'<span class="muted">(미할당 ID)</span>':esc(tvShow(r.text))}
function tvRenderVocab(){const d=tvVocab,st=d.stats,m=Math.max(Math.abs(st.max),Math.abs(st.min))||1,neg=hexRgb(cssVar('--div-neg')),pos=hexRgb(cssVar('--div-pos')),gen=d.marks.generated,src=d.marks.source;
 const prob=p=>p<1e-4?p.toExponential(2):(p*100).toFixed(2)+'%';
 $('tv-vocab-rows').innerHTML=d.rows.map(r=>{const t=r.logit/m,c=t>=0?pos:neg,pw=Math.max(0,Math.min(100,r.prob*100));
  return `<tr class="${gen&&r.id===gen.id?'tv-vocab-gen':''}"><td class="num">${r.rank.toLocaleString()}</td><td class="num">${r.id}</td><td class="mono${r.partial?' muted':''}">${tvVocabWord(r)}${gen&&r.id===gen.id?' <span class="badge safe">생성</span>':''}${src&&r.id===src.id?' <span class="badge unknown">입력</span>':''}</td><td class="mono muted">${esc(r.piece??'')}</td><td class="num mono" style="background:rgba(${c.join(',')},${(Math.min(1,Math.abs(t))*.55).toFixed(3)})">${esc(fmt(r.logit))}</td><td class="num mono" style="background:linear-gradient(90deg,var(--accent-soft) ${pw}%,transparent ${pw}%)">${prob(r.prob)}</td></tr>`}).join('')||'<tr><td colspan="6"><div class="empty">검색 결과가 없습니다.</div></td></tr>';
 const mark=r=>r?`"${tvShow(r.text??'(미할당)')}" · id ${r.id} · 순위 ${r.rank.toLocaleString()} · p ${prob(r.prob)}`:'—';
 $('tv-vocab-summary').innerHTML=[['투영 대상',`Layer ${d.layer} · ${d.module} · ${d.location}`],['계산',d.is_model_output?'마지막 레이어 출력 → 실제 모델 출력 logit과 같은 계산':d.apply_norm?'logit lens: 최종 RMSNorm → lm_head':'RMSNorm 없이 lm_head만 적용'],['실제 생성 토큰',mark(gen)],['예측 입력 토큰',mark(src)],['1위 토큰',mark(d.top[0])],['엔트로피',`${fmt(d.stats.entropy)} nats`],['logit 범위',`${fmt(st.min)} ~ ${fmt(st.max)} · mean ${fmt(st.mean)}`]].map(([a,b])=>`<div class="metric"><b>${esc(a)}</b>${esc(b)}</div>`).join('');
 $('tv-vocab-page').textContent=d.total?`${(d.offset+1).toLocaleString()}–${(d.offset+d.rows.length).toLocaleString()} / ${d.total.toLocaleString()}`:'0';
 $('tv-vocab-meta').textContent=`${{'':'logit 내림차순',logit_asc:'logit 오름차순',id:'token ID 순'}[d.sort]||''}${d.query?` · 검색 "${d.query}"`:''} · 어휘 ${d.vocab_size.toLocaleString()} × 은닉 ${d.hidden_size.toLocaleString()} · logit 칸 색 = 부호와 크기`;
 $('tv-vocab-max-id').textContent=`token ID ${(d.vocab_size-1).toLocaleString()}`;
 $('tv-vocab-prev').disabled=d.offset===0;$('tv-vocab-next').disabled=d.offset+d.rows.length>=d.total;tvRenderVocabStrip()}
function tvRenderVocabStrip(){const c=$('tv-vocab-strip'),x=fitCanvas(c),d=tvVocab;if(!d)return;const s=c._s,W=c.width,H=c.height,env=d.envelope,n=env.max.length,lo=Math.min(...env.max),hi=Math.max(...env.max),span=hi-lo||1,sLo=hexRgb(cssVar('--seq-lo')),sHi=hexRgb(cssVar('--seq-hi')),bw=W/n;
 for(let i=0;i<n;i++){x.fillStyle=`rgb(${mix(sLo,sHi,(env.max[i]-lo)/span).join(',')})`;x.fillRect(Math.floor(i*bw),0,Math.ceil(bw)+1,H)}
 for(const [mark,color] of [[d.marks.source,cssVar('--text-2')],[d.marks.generated,cssVar('--highlight')]]){if(!mark)continue;const px=Math.floor(mark.id/env.bucket)*bw,w=Math.max(4*s,bw);x.lineWidth=3*s;x.strokeStyle='#000';x.strokeRect(px,1.5*s,w,H-3*s);x.lineWidth=1.5*s;x.strokeStyle=color;x.strokeRect(px,1.5*s,w,H-3*s)}
 const rgb=v=>`rgb(${v.join(',')})`;$('tv-vocab-lo').textContent=fmt(lo);$('tv-vocab-hi').textContent=fmt(hi);$('tv-vocab-bar').style.background=`linear-gradient(90deg,${rgb(sLo)},${rgb(sHi)})`;
 const at=ev=>Math.min(n-1,Math.max(0,Math.floor(canvasPoint(c,ev).x/bw)));
 c.onmousemove=ev=>{const i=at(ev),a=i*env.bucket,b=Math.min(d.vocab_size-1,a+env.bucket-1);showTip(ev,`<b>token ID ${a.toLocaleString()}–${b.toLocaleString()}</b>\n최대 logit ${fmt(env.max[i])}\n최소 logit ${fmt(env.min[i])}\n클릭: 이 구간을 표에서 보기`)};c.onmouseleave=hideTip;
 c.onclick=ev=>{const i=at(ev);tvVocabSort='id';$('tv-vocab-q').value='';tvVocabOffset=Math.floor(i*env.bucket/tvVocabLimit)*tvVocabLimit;tvLoadVocab()}}
$('tv-vocab-norm').onchange=()=>{tvVocabOffset=0;tvLoadVocab()};
let tvVocabSearchTimer=null;$('tv-vocab-q').oninput=()=>{clearTimeout(tvVocabSearchTimer);tvVocabSearchTimer=setTimeout(()=>{tvVocabOffset=0;tvLoadVocab()},300)};
$('tv-vocab-sorts').onclick=ev=>{const b=ev.target.closest('button[data-sort]');if(!b)return;tvVocabSort=b.dataset.sort;tvVocabOffset=0;tvLoadVocab()};
$('tv-vocab-prev').onclick=()=>{tvVocabOffset=Math.max(0,tvVocabOffset-tvVocabLimit);tvLoadVocab()};$('tv-vocab-next').onclick=()=>{tvVocabOffset+=tvVocabLimit;tvLoadVocab()};
$('tv-vocab-find-gen').onclick=()=>{const gen=tvVocab?.marks.generated;if(!gen)return;$('tv-vocab-q').value=String(gen.id);tvVocabOffset=0;tvLoadVocab()};
function tvRedraw(){if($('view-tokens').hidden)return;tvRenderTrend();tvRenderHeat();if(tvVocab)tvRenderVocabStrip();for(const L of Object.keys(tvCards))tvRenderSpark(L)}
$('tv-trend').onmousemove=ev=>{const c=$('tv-trend'),i=tvIndexAt(c,ev);tvRenderTrend(i);if(i<0||!tvSession){hideTip();return}const t=tvSession.tokens[i],m=$('tv-metric').value;showTip(ev,`<b>#${i} "${esc(tvShow(tvTokText(t)))}"</b>\n${tvMetricLabel[m]}\n`+tvTraj.layers.map(L=>`Layer ${L.layer}: ${L.metrics[i]?tvFmt(L.metrics[i][m]):'—'}`).join('\n'))};
$('tv-trend').onmouseleave=()=>{hideTip();tvRenderTrend()};$('tv-trend').onclick=ev=>{const i=tvIndexAt($('tv-trend'),ev);if(i>=0)tvSelectToken(i)};
$('tv-heat').onmousemove=ev=>{const c=$('tv-heat'),g=c._geom,i=tvIndexAt(c,ev);if(!g||i<0){hideTip();return}const p=canvasPoint(c,ev),row=Math.min(g.h.rows-1,Math.max(0,Math.floor(p.fy*g.h.rows))),t=tvSession.tokens[i];showTip(ev,`<b>#${i} "${esc(tvShow(tvTokText(t)))}"</b>\nLayer ${g.layer} · dim ${row*g.h.dim_step}\nvalue ${g.h.present[i]?esc(fmt(g.h.values[row*g.h.cols+i])):'기록 없음'}`)};
$('tv-heat').onmouseleave=hideTip;$('tv-heat').onclick=ev=>{const i=tvIndexAt($('tv-heat'),ev);if(i>=0)tvSelectToken(i)};
$('tv-session').onchange=tvLoadSession;$('tv-refresh').onclick=tvLoadSessions;
$('tv-loc').onchange=async()=>{tvRecLoc=$('tv-loc').value;await tvLoadTrajectory();tvSelectToken(tvToken)};
$('tv-metric').onchange=()=>{tvRenderTrend();$('tv-trend-meta').textContent=`${tvLocLabel()} · ${tvMetricLabel[$('tv-metric').value]}`};
$('tv-prev-page').onclick=()=>{tvOffset=Math.max(0,tvOffset-tvPageSize);tvLoadSessions()};$('tv-next-page').onclick=()=>{tvOffset+=tvPageSize;tvLoadSessions()};
let tvSearchTimer=null;$('tv-search').oninput=()=>{clearTimeout(tvSearchTimer);tvSearchTimer=setTimeout(()=>{tvOffset=0;tvLoadSessions()},250)};
$('tv-token-filter').oninput=tvRenderTokens;$('tv-tokens').onclick=ev=>{const el=ev.target.closest('.tv-tok');if(el)tvSelectToken(+el.dataset.i)};
$('tv-prev-token').onclick=()=>tvSelectToken(tvToken-1);$('tv-next-token').onclick=()=>tvSelectToken(tvToken+1);
$('tv-heat-layers').onclick=ev=>{const b=ev.target.closest('button[data-layer]');if(!b)return;tvHeatLayer=+b.dataset.layer;document.querySelectorAll('#tv-heat-layers button').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));tvRenderHeat()};
$('tv-rec-layers').onclick=ev=>{const b=ev.target.closest('button[data-layer]');if(!b)return;tvRecLayer=+b.dataset.layer;tvRenderRecords()};
$('tv-records').onclick=ev=>{const tr=ev.target.closest('tr[data-key]');if(!tr)return;tvRecLoc=tr.dataset.loc;tvValueOffset=0;tvLoadValues(tr.dataset.key)};
$('tv-sorts').onclick=ev=>{const b=ev.target.closest('button[data-sort]');if(!b)return;tvValueSort=b.dataset.sort;tvValueOffset=0;tvLoadValues(tvValueKey)};
$('tv-val-prev').onclick=()=>{tvValueOffset=Math.max(0,tvValueOffset-256);tvLoadValues(tvValueKey)};$('tv-val-next').onclick=()=>{tvValueOffset+=256;tvLoadValues(tvValueKey)};
document.addEventListener('keydown',ev=>{if($('view-tokens').hidden||!tvSession||ev.target.closest?.('input,select,textarea'))return;if(ev.key==='ArrowRight'||ev.key==='ArrowLeft'){ev.preventDefault();tvSelectToken(tvToken+(ev.key==='ArrowRight'?1:-1))}});
if(location.pathname==='/tokens')showView('view-tokens');
/* ---------- teammate C-01 captures (write_capture: one observed token per block) ---------- */
let capLoaded=false,capListReq=0,capDetailReq=0,capValueReq=0,capList=[],capSelected=null,capDetail=null,capValLayer=null,capValueSort='abs_desc',capValueOffset=0;
function capEnsureLoaded(){if(!capLoaded){capLoaded=true;capLoadList()}}
function capBadge(c){const m=c.m1;if(!m)return '<span class="badge unknown">판정 없음</span>';const name=c.monitor||'M1';const cls=m.alarm===true?'danger':m.alarm===false?'safe':'unknown',label=m.alarm===true?`위험-${name}`:m.alarm===false?`${name} 비경고`:`${name} ${m.status||'미판정'}`;return `<span class="badge ${cls}" title="${esc(`status ${m.status} · score ${m.risk_score??'—'} · ${m.reason||m.error||''}`)}">${esc(label)}</span>`}
function capVerified(v){return v===true?'<span class="badge safe" title="metadata.prefix_ids_sha256과 token ID 해시가 일치">prefix 일치</span>':v===false?'<span class="badge danger" title="token ID 해시가 metadata와 다릅니다">prefix 불일치</span>':'<span class="badge unknown" title="token ID 파일이 없습니다">ID 없음</span>'}
function capTokText(t){return t?(t.text??(t.piece??`#${t.id}`)):'—'}
async function capLoadList(){const cur=++capListReq;$('cap-list').innerHTML='<tr><td colspan="8"><div class="empty">불러오는 중…</div></td></tr>';
 try{const d=await tvJson('/api/captures/list');if(cur!==capListReq)return;capList=d.captures;$('cap-root').textContent=d.root?`루트: ${d.root}`:'';
  $('cap-list').innerHTML=capList.map(c=>`<tr data-id="${esc(c.id)}" class="${c.id===capSelected?'selected':''}"><td class="mono">${esc(c.started_at||'—')}</td><td class="mono" title="${esc(c.id)}">${esc(c.run_id||c.id)}</td><td>${esc(c.scenario_id||'—')} · ${esc(c.phase||'')}</td><td class="mono">#${esc(c.alignment?.token_index??'—')} ${esc(tvShow(capTokText(c.observed_token)))}</td><td class="num">${esc(c.observed_prefix_length??'—')}</td><td>${capBadge(c)}</td><td>${capVerified(c.prefix_verified)}</td><td class="task" title="${esc(c.task||'')}">${esc(c.task||'미기록')}</td></tr>`).join('')||'<tr><td colspan="8"><div class="empty">capture/metadata.json이 있는 실행 폴더가 없습니다.</div></td></tr>';
  if(capList.length&&!capList.some(c=>c.id===capSelected))capSelect(capList[0].id);else if(capSelected)capSelect(capSelected)
 }catch(e){if(cur===capListReq)$('cap-list').innerHTML=`<tr><td colspan="8"><div class="empty">${esc('목록 조회 실패: '+e.message)}</div></td></tr>`}}
async function capSelect(id){capSelected=id;document.querySelectorAll('#cap-list tr[data-id]').forEach(tr=>tr.classList.toggle('selected',tr.dataset.id===id));const cur=++capDetailReq;$('cap-title').textContent='불러오는 중…';
 try{const d=await tvJson('/api/captures/detail?'+new URLSearchParams({id}));if(cur!==capDetailReq)return;capDetail=d;if(!d.layers.some(L=>L.layer===capValLayer))capValLayer=d.layers[0]?.layer;capValueOffset=0;capRender()}
 catch(e){if(cur===capDetailReq){$('cap-title').textContent='Capture 조회 실패';$('cap-sub').textContent=e.message}}}
function capRender(){const d=capDetail,sp=d.spans,obs=sp.observed,prompt=sp.prompt_length??d.matches[0]?.prompt_length??null,act=d.action||{},md=d.metadata||{};
 $('cap-title').textContent=`${d.run_id||d.id} · 관찰 토큰 #${obs} "${tvShow(capTokText(d.observed_token))}"`;
 $('cap-sub').textContent=`${d.id} · ${md.capture_mode||'—'} · hook ${md.hook_point||'—'} · ${md.identity?.model_id||''} · torch ${md.torch_version||'—'} / transformers ${md.transformers_version||'—'} · 파일: ${d.sidecars.join(', ')}`;
 const m1=d.m1;$('cap-metrics').innerHTML=[['Task',d.task||'미기록'],['Trusted policy',d.policy||'미기록'],['시나리오 / phase',`${d.scenario_id||'—'} / ${d.phase||'—'}`],['관찰 위치',`token #${obs} → 다음 토큰 #${d.alignment?.predicts_token_index??'—'} 예측 · 행동까지 ${d.alignment?.tokens_until_action_start??'—'} 토큰`],['행동 구간',`${act.action_id||'—'} · token ${act.token_start??'—'}–${act.token_end??'—'}`],['추론 구간',sp.reasoning?`token ${sp.reasoning[0]}–${sp.reasoning[1]}`:'—'],['Prefix 무결성',d.prefix_verified===true?'sha256 일치':d.prefix_verified===false?'sha256 불일치':'token ID 없음'],['M1 판정',m1?`${m1.alarm===true?'위험':m1.alarm===false?'비경고':'미판정'} · score ${m1.risk_score??'—'} · ${m1.status}`:'없음'],['M1 사유',m1?.reason||m1?.error||'—'],['최종 행동',d.action_text||'—']].map(([a,b])=>`<div class="metric"><b>${esc(a)}</b>${esc(b)}</div>`).join('');
 const role=i=>i===obs?'observed':i>=(act.token_start??Infinity)?'action':prompt!=null&&i<prompt?'prompt':sp.reasoning&&i>=sp.reasoning[0]&&i<=sp.reasoning[1]?'reasoning':'context';
 $('cap-tokens').innerHTML=d.tokens.map(t=>`<span class="cap-tok ${role(t.index)}" title="#${t.index} · id ${t.id} · piece ${esc(JSON.stringify(t.piece))}">${esc(String(capTokText(t)).replace(/\n/g,'⏎\n'))}</span>`).join('')||'<div class="empty">token ID 기록이 없습니다.</div>';
 $('cap-token-meta').textContent=`${d.tokens.length}개 토큰 · prefix ${sp.prefix_length} (#0–#${sp.prefix_length-1})${prompt!=null?` · prompt ${prompt}`:''}${d.tokenizer_available?'':' · tokenizer 없음: ID만 표시'}`;
 {const box=$('cap-tokens'),el=box.querySelector('.cap-tok.observed');if(el)box.scrollTop=Math.max(0,el.offsetTop-box.clientHeight/2)}
 $('cap-hook').textContent=`${md.hook_point||''} · ${md.pooling||''} · ${md.storage_dtype||''}`;
 $('cap-cards').innerHTML=d.layers.map((L,li)=>`<div class="tv-card"><h3><span class="tv-key" style="background:var(${tvLayerVar[li]||'--series-1'})"></span>Layer ${L.layer}<small class="muted" style="font-weight:400">${esc(L.module_path||'')} · ${esc(L.source_dtype||'')}</small></h3><div class="tv-stats">${[['L2',L.stats.l2],['mean',L.stats.mean],['std',L.stats.std],['min',L.stats.min],['max',L.stats.max],['max |x|',L.stats.max_abs]].map(([k,v])=>`<div title="${esc(v??'')}"><b>${k}</b><span>${tvFmt(v)}</span></div>`).join('')}</div><div class="chartbox"><canvas class="tv-spark" id="cap-spark-${L.layer}"></canvas></div><div class="axis-note"><span>dim 0</span><span>${esc(JSON.stringify(L.shape))} · 원소 ${L.numel.toLocaleString()}개</span></div><div class="tv-top"><span class="status">|값| 상위</span>${L.top.map(t=>`<code title="dim ${t.index}">#${t.index} ${esc(fmt(t.value))}</code>`).join('')}</div></div>`).join('');
 capRedraw();capRenderMatches();
 $('cap-val-layers').innerHTML=d.layers.map((L,li)=>`<button type="button" data-layer="${L.layer}" aria-pressed="${L.layer===capValLayer}"><span class="tv-key" style="background:var(${tvLayerVar[li]||'--series-1'})"></span>Layer ${L.layer}</button>`).join('');capLoadValues()}
function capRenderMatches(){const d=capDetail,el=$('cap-matches');
 if(!d.matches.length){el.innerHTML=`<div class="empty">작성자 HookInspection 기록 중 이 capture와 같은 token prefix(${d.spans.prefix_length}개)를 관찰한 세션이 없습니다. 별도로 실행된 run이면 정상입니다.</div>`;return}
 el.innerHTML=d.matches.map((m,i)=>`<div class="cap-match"><div class="toolbar"><b class="mono" style="overflow-wrap:anywhere">${esc(m.artifact_dir)}</b><span class="spacer"></span>${m.mode==='generation'?`<button type="button" data-open="${i}">토큰별 은닉 상태에서 열기 →</button>`:''}</div>
  <div class="status" style="margin:4px 0 8px">${m.mode==='generation'?`생성 forward ${m.forward_call_index} (KV cache) · 입력 위치 #${m.position} → 생성 토큰 #${m.generated_token_index} "${esc(tvShow(m.generated_text??''))}" 예측`:`prompt replay forward 0 · 위치 #${m.position}`} · prompt ${m.prompt_length} tokens · capture는 전체 prefix 재생 · 같은 모델이면 차이는 연산 경로(KV cache 여부)와 bf16 누적 오차에서 옵니다</div>
  <table><thead><tr><th>Layer</th><th class="num">cosine</th><th class="num">상대 L2 오차</th><th class="num">max |차이|</th><th class="num">Hook L2</th><th class="num">Capture L2</th></tr></thead><tbody>${m.layers.map(L=>`<tr><td>Layer ${L.layer}</td><td class="num mono">${L.cosine==null?'—':L.cosine.toFixed(6)}</td><td class="num mono">${L.rel_l2==null?'—':(L.rel_l2*100).toFixed(2)+'%'}</td><td class="num mono">${tvFmt(L.max_abs_diff)}</td><td class="num mono">${tvFmt(L.hook_l2)}</td><td class="num mono">${tvFmt(L.capture_l2)}</td></tr>`).join('')}</tbody></table></div>`).join('')}
function capRedraw(){if(!capDetail||$('view-captures').hidden)return;capDetail.layers.forEach((L,li)=>drawEnvelope($(`cap-spark-${L.layer}`),L.envelope,L.numel,tvLayerColor(li),`Layer ${L.layer}`))}
async function capLoadValues(){if(!capDetail||capValLayer==null)return;document.querySelectorAll('#cap-sorts button').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.sort===capValueSort)));const cur=++capValueReq;
 try{const v=await tvJson('/api/captures/vector?'+new URLSearchParams({id:capDetail.id,layer:String(capValLayer),offset:String(capValueOffset),limit:'256',sort:capValueSort}));if(cur!==capValueReq)return;const mean=v.stats.mean,std=v.stats.std;
  $('cap-values').innerHTML=v.values.map(x=>{const hot=typeof x.value==='number'&&std>0&&Math.abs(x.value-mean)>3*std;return `<tr><td class="num">${x.index}</td><td class="num ${hot?'outlier':''}">${esc(x.value)}</td></tr>`}).join('');
  $('cap-value-meta').textContent=`Layer ${v.layer} · ${v.offset}–${v.offset+v.values.length} / ${v.numel.toLocaleString()} · ${tvSortLabel[capValueSort]} · 빨강 ● = 이 벡터 평균에서 3σ 초과`;$('cap-val-prev').disabled=v.offset===0;$('cap-val-next').disabled=v.offset+v.values.length>=v.numel}
 catch(e){if(cur===capValueReq)$('cap-value-meta').textContent='원소값 조회 실패: '+e.message}}
async function capOpenInTokens(m){tvLoaded=true;tvPendingToken=m.forward_call_index;tvOffset=0;$('tv-search').value=m.artifact_dir;showView('view-tokens');await tvLoadSessions()}
$('cap-refresh').onclick=capLoadList;$('cap-list').onclick=ev=>{const tr=ev.target.closest('tr[data-id]');if(tr)capSelect(tr.dataset.id)};
$('cap-val-layers').onclick=ev=>{const b=ev.target.closest('button[data-layer]');if(!b)return;capValLayer=+b.dataset.layer;capValueOffset=0;document.querySelectorAll('#cap-val-layers button').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));capLoadValues()};
$('cap-sorts').onclick=ev=>{const b=ev.target.closest('button[data-sort]');if(!b)return;capValueSort=b.dataset.sort;capValueOffset=0;capLoadValues()};
$('cap-val-prev').onclick=()=>{capValueOffset=Math.max(0,capValueOffset-256);capLoadValues()};$('cap-val-next').onclick=()=>{capValueOffset+=256;capLoadValues()};
$('cap-matches').onclick=ev=>{const b=ev.target.closest('button[data-open]');if(b)capOpenInTokens(capDetail.matches[+b.dataset.open])};
if(location.pathname==='/captures')showView('view-captures');
/* ---------- scenario rollout records: model input, LLM output, result and verdict per step ---------- */
let roLoaded=false,roListReq=0,roDetailReq=0,roList=[],roSelected=null;
function roEnsureLoaded(){if(!roLoaded){roLoaded=true;roLoadList()}}
function roLabelBadge(label,decision){return label===1?'<span class="badge danger">위반</span>':label===0?'<span class="badge safe">준수</span>':`<span class="badge unknown">${esc(decision||'미판정')}</span>`}
function roRenderList(){const q=$('ro-search').value.trim().toLowerCase(),kind=$('ro-kind').value,filter=$('ro-filter').value;
 const rows=roList.filter(r=>(!kind||r.kind===kind)&&(!filter||(filter==='violation'?r.violations>0:filter==='clean'?r.finished&&!r.violations:!r.finished))&&(!q||[r.scenario_key,r.family,r.task,r.id].join(' ').toLowerCase().includes(q)));
 $('ro-count').textContent=`${rows.length} / ${roList.length}개 · 위반 rollout ${roList.filter(r=>r.violations>0).length}개`;
 $('ro-list').innerHTML=rows.map(r=>`<tr data-id="${esc(r.id)}" class="${r.id===roSelected?'selected':''}"><td class="mono">${esc(r.started_at||'—')}</td><td class="mono">${esc(r.scenario_key)}</td><td class="num">${esc(r.seed)}</td><td>${esc(r.kind)}</td><td>${esc(r.termination)}</td><td class="num">${esc(r.actions)}</td><td class="num">${r.violations?`<span class="badge danger">${r.violations}</span>`:'0'}</td><td>${r.business_completed==null?'—':r.business_completed?'<span class="badge safe">완료</span>':'<span class="badge unknown">미완료</span>'}</td><td class="task" title="${esc(r.task||'')}">${esc(r.task||'')}</td></tr>`).join('')||'<tr><td colspan="9"><div class="empty">조건에 맞는 실행 기록이 없습니다.</div></td></tr>'}
async function roLoadList(){const cur=++roListReq;try{const d=await tvJson('/api/rollouts/list');if(cur!==roListReq)return;roList=d.rollouts;$('ro-root').textContent=d.root?`폴더: ${d.root}`:'';roRenderList();if(!roSelected&&roList.length)roSelect(roList[0].id)}catch(e){$('ro-list').innerHTML=`<tr><td colspan="9"><div class="empty">${esc(e.message)}</div></td></tr>`}}
function roMessages(messages){return (messages||[]).map(m=>`<div class="ro-msg"><b>${esc(m.role)}</b><pre>${esc(m.content)}</pre></div>`).join('')}
function roStepHtml(step,index,previous){const violation=step.policy_label===1,findings=[...(step.static_findings||[]),...(step.effect_findings||[])],out=step.output||{},input=step.input_messages||[];
 const fresh=index===0?input:input.slice(Math.max(0,(previous?.input_messages||[]).length));
 const failures=(step.format_failures||[]).map(f=>`<details class="inline"><summary>거부된 시도 ${f.attempt}: ${esc(f.reason)}</summary><pre>${esc(f.raw||'')}</pre></details>`).join('');
 const exec=step.execution?Object.entries(step.execution).filter(([k,v])=>v!=null&&k!=='logs').map(([k,v])=>`${k}=${v}`).join(' · '):'';
 return `<div class="ro-step${violation?' violation':''}"><div class="ro-step-head"><b>Step ${step.step_index}</b>${step.kind?`<span class="badge unknown">${esc(step.kind)}</span>`:''}${step.outcome==='format_failure'?'<span class="badge unknown">형식 실패</span>':roLabelBadge(step.policy_label,step.decision)}<span class="status">시도 ${esc(step.attempts)}회${step.generated_tokens?` · 생성 ${step.generated_tokens} 토큰`:''}${exec?' · '+esc(exec):''}</span><span class="spacer"></span>${step.capture_id?`<button type="button" data-hidden-step="${step.step_index}">은닉 상태 분석 →</button><button type="button" data-capture="${esc(step.capture_id)}">은닉층 보기 →</button>`:''}</div>
 <div class="ro-grid"><div class="ro-col"><h4>모델 입력 ${index===0?'(시스템 + 과제)':'(새로 추가된 메시지)'}</h4>${roMessages(fresh)||'<div class="status">—</div>'}${index>0&&input.length?`<details class="inline"><summary>이 step에서 모델이 본 전체 대화 (${input.length}개 메시지)</summary>${roMessages(input)}</details>`:''}</div>
 <div class="ro-col"><h4>LLM 출력</h4>${out.reasoning?`<details class="inline" open><summary>추론 (analysis)</summary><pre>${esc(out.reasoning)}</pre></details>`:''}${step.command!=null?`<b class="status">최종 행동</b><pre>${esc(step.command)}</pre>`:''}${out.raw?`<details class="inline"><summary>원문 출력 (Harmony 토큰 포함)</summary><pre>${esc(out.raw)}</pre></details>`:''}${failures}</div>
 <div class="ro-col"><h4>실행 결과 · 판정</h4>${findings.length?`<div class="ro-findings">${findings.map(f=>`<code>${esc(f)}</code>`).join('')}</div>`:''}${step.oracle_reason?`<div class="status">suite 판정 근거: ${esc(step.oracle_reason)}</div>`:''}<pre>${esc(step.observation||(step.kind==='stop'?'(stop: 실행 없음)':'—'))}</pre></div></div></div>`}
async function roSelect(id){roSelected=id;roRenderList();const cur=++roDetailReq;$('ro-title').textContent='불러오는 중…';
 try{const d=await tvJson('/api/rollouts/detail?'+new URLSearchParams({id}));if(cur!==roDetailReq)return;
  $('ro-title').textContent=`${d.scenario_key} · seed ${d.seed}`;$('ro-sub').textContent=`${d.id} · ${d.kind} · 종료 ${d.termination} · 라벨 ${d.label_source||''} · 샘플링 ${JSON.stringify(d.sampling||{})}`;
  const link=$('ro-transcript');link.hidden=false;link.href='/api/rollouts/transcript?'+new URLSearchParams({id});
  const op=d.operator_report||{};
  const b=d.scenario_brief||{};
  $('ro-metrics').innerHTML=[['시나리오 JSON',b.source_json||'—'],['제목 (운영자용)',b.title||'—'],['조건 의미',b.condition_meaning||d.condition],['모델에 준 TASK',b.task_given_to_model||d.task||'—'],['행동 / 위반 / 미판정',`${d.actions} / ${d.violations} / ${d.unlabelled}`],['첫 위반 step',d.first_violation_step??'없음'],['업무 완료 (suite 판정)',d.business_completed==null?'—':d.business_completed?'완료':'미완료'],['suite 위반 시도 / 실행',op.violation_attempts==null?'—':`${op.violation_attempts} / ${op.violation_executed}`]].map(([a,b])=>`<div class="metric"><b>${esc(a)}</b>${esc(b)}</div>`).join('');
  const ctx=(d.scenario_brief?'# 시나리오 요약 (운영자용)\n'+JSON.stringify(d.scenario_brief,null,2)+'\n\n':'')+(d.public_context?'# 모델에 준 공개 컨텍스트\n'+JSON.stringify(d.public_context,null,2):`Task: ${d.task||''}\n\nTrusted policy: ${d.trusted_policy||''}`);$('ro-context').textContent=ctx;
  $('ro-steps').innerHTML=d.steps.map((s,i)=>roStepHtml(s,i,d.steps[i-1])).join('')||'<div class="empty">아직 기록된 step이 없습니다.</div>'}
 catch(e){if(cur===roDetailReq){$('ro-title').textContent='불러오기 실패';$('ro-sub').textContent=e.message}}}
$('ro-refresh').onclick=roLoadList;$('ro-search').oninput=roRenderList;$('ro-kind').onchange=roRenderList;$('ro-filter').onchange=roRenderList;
$('ro-list').onclick=ev=>{const tr=ev.target.closest('tr[data-id]');if(tr)roSelect(tr.dataset.id)};
$('ro-steps').onclick=ev=>{const h=ev.target.closest('button[data-hidden-step]');if(h){shOpenFromRecord(roSelected,+h.dataset.hiddenStep);return}const b=ev.target.closest('button[data-capture]');if(!b)return;capLoaded=true;showView('view-captures');capLoadList().then(()=>capSelect(b.dataset.capture))};
if(location.pathname==='/rollouts')showView('view-rollouts');
/* ---------- scenario rollout hidden states: scenario → rollout → step → observation point × layer ---------- */
let shLoaded=false,shRollouts=[],shId=null,shStep=null,shData=null,shTrend=null,shPoint=null,shLayer=null,shValueSort='abs_desc',shValueOffset=0,shVocabSort='',shVocabOffset=0,shReq=0,shCellReq=0,shSpark=null;
function shEnsureLoaded(){if(!shLoaded){shLoaded=true;shLoadList()}}
async function shLoadList(){try{const d=await tvJson('/api/rollouts/list');shRollouts=d.rollouts.filter(r=>r.actions>0);const groups={};shRollouts.forEach(r=>{(groups[r.scenario_id]??=[]).push(r)});
 const ids=Object.keys(groups).sort((a,b)=>(a.startsWith('AV-S')-b.startsWith('AV-S'))||a.localeCompare(b));const prev=$('sh-scenario').value;
 $('sh-scenario').innerHTML=ids.map(id=>`<option value="${esc(id)}">${esc(id)} · ${groups[id].length}회 실행 · 위반 ${groups[id].filter(r=>r.violations>0).length}회</option>`).join('')||'<option value="">실행 기록 없음</option>';
 if(ids.includes(prev))$('sh-scenario').value=prev;$('sh-status').textContent=`${shRollouts.length}개 rollout · ${ids.length}개 시나리오 · 폴더 ${d.root}`;shFillRollouts()}catch(e){$('sh-status').textContent='불러오기 실패: '+e.message}}
function shFillRollouts(keep){const sid=$('sh-scenario').value,rows=shRollouts.filter(r=>r.scenario_id===sid);
 $('sh-rollout').innerHTML=rows.map(r=>`<option value="${esc(r.id)}">${esc(r.condition)} · seed ${esc(r.seed)} · ${esc(r.started_at||'')} · 행동 ${r.actions} · 위반 ${r.violations}${r.finished?'':' · 미완료'}</option>`).join('');
 if(keep&&rows.some(r=>r.id===keep))$('sh-rollout').value=keep;if($('sh-rollout').value)shOpen($('sh-rollout').value)}
async function shOpen(id,step){shId=id;const cur=++shReq;try{const t=await tvJson('/api/rollouts/trend?'+new URLSearchParams({id}));if(cur!==shReq)return;shTrend=t;shRenderTrend();
 $('sh-steps').innerHTML=t.steps.map(s=>`<button type="button" data-step="${s.step_index}" title="${esc(s.command||s.outcome||'')}">Step ${s.step_index} ${s.policy_label===1?'⚠':s.policy_label===0?'✓':'?'} ${esc(s.kind||'')}</button>`).join('');
 const first=step??t.steps.find(s=>s.kind)?.step_index??0;await shSelectStep(first)}catch(e){$('sh-title').textContent='불러오기 실패';$('sh-sub').textContent=e.message}}
function shNormRows(matrix){return matrix.map(row=>{const vals=row.filter(v=>v!=null);const lo=Math.min(...vals),hi=Math.max(...vals);return row.map(v=>v==null?null:(hi>lo?(v-lo)/(hi-lo):.5))})}
function shDrawGrid(c,matrix,cols,opt){const x=fitCanvas(c),s=c._s,W=c.width,H=c.height,left=50*s,top=(opt.bands?12:4)*s,bottom=H-18*s,rows=matrix.length;if(!rows||!cols){c._g=null;return}
 const cw=(W-left-8*s)/cols,rh=(bottom-top)/rows,norm=shNormRows(matrix),lo=hexRgb(cssVar('--seq-lo')),hi=hexRgb(cssVar('--seq-hi'));
 for(let r=0;r<rows;r++)for(let k=0;k<cols;k++){const v=norm[r][k];x.fillStyle=v==null?cssVar('--surface-3'):`rgb(${mix(lo,hi,v).join(',')})`;x.fillRect(left+k*cw,top+r*rh,Math.ceil(cw)-(cw>4*s?1:0),Math.ceil(rh))}
 if(opt.bands)opt.bands.forEach((label,k)=>{x.fillStyle=label===1?cssVar('--critical'):label===0?cssVar('--good'):cssVar('--muted');x.fillRect(left+k*cw,0,Math.ceil(cw)-1,8*s)});
 x.fillStyle=cssVar('--muted');x.textAlign='right';[0,Math.floor(rows/2),rows-1].forEach(r=>x.fillText(`L${opt.layers[r]}`,left-6*s,top+(r+.5)*rh));x.textAlign='center';
 const every=Math.max(1,Math.ceil(cols/12));for(let k=0;k<cols;k+=every)x.fillText(opt.colLabel(k),left+(k+.5)*cw,H-8*s);x.textAlign='left';
 if(opt.selectedCol!=null&&opt.selectedCol>=0){x.lineWidth=2*s;x.strokeStyle=cssVar('--highlight');const px=left+opt.selectedCol*cw;if(opt.selectedRow!=null&&opt.selectedRow>=0)x.strokeRect(px,top+opt.selectedRow*rh,cw,rh);else x.strokeRect(px,top,cw,bottom-top)}
 c._g={left,top,cw,rh,rows,cols}}
function shCell(c,ev){const g=c._g;if(!g)return null;const p=canvasPoint(c,ev),k=Math.floor((p.x-g.left)/g.cw),r=Math.floor((p.y-g.top)/g.rh);return k>=0&&k<g.cols?{col:k,row:Math.min(g.rows-1,Math.max(0,r))}:null}
function shRenderTrend(){const t=shTrend;if(!t)return;const cols=t.steps.length;shDrawGrid($('sh-trend'),t.pre_action_l2,cols,{layers:t.layers,bands:t.steps.map(s=>s.policy_label),colLabel:k=>'S'+t.steps[k].step_index,selectedCol:t.steps.findIndex(s=>s.step_index===shStep)})}
async function shSelectStep(step){shStep=step;const cur=++shReq;document.querySelectorAll('#sh-steps button').forEach(b=>b.setAttribute('aria-pressed',String(+b.dataset.step===step)));shRenderTrend();
 try{const d=await tvJson('/api/rollouts/hidden?'+new URLSearchParams({id:shId,step}));if(cur!==shReq)return;shData=d;const b=d.scenario_brief||{},st=d.step||{};
  $('sh-title').textContent=`${d.scenario_key} · seed ${d.seed}`;$('sh-sub').textContent=`${d.id} · step ${d.steps.length}개 · 관찰 시점마다 ${d.layers.length}개 블록 출력 저장`;
  $('sh-brief').innerHTML=[['시나리오',b.title&&b.title!==d.scenario_key.split('/')[0]?`${d.scenario_key.split('/')[0]} · ${b.title}`:d.scenario_key],['조건 의미',b.condition_meaning||d.condition],['모델에 준 TASK',b.task_given_to_model||'—'],['시나리오 JSON',b.source_json||'—']].map(([a,v])=>`<div class="metric"><b>${esc(a)}</b>${esc(v)}</div>`).join('');
  $('sh-step-title').innerHTML=`Step ${d.step_index} ${st.policy_label===1?'<span class="badge danger">위반</span>':st.policy_label===0?'<span class="badge safe">준수</span>':'<span class="badge unknown">미판정</span>'} <span class="badge unknown">${esc(st.kind||'')}</span>`;
  $('sh-step-meta').textContent=`prompt ${d.prompt_length} 토큰 · 추론 ${d.reasoning_span?d.reasoning_span.join('–'):'없음'} · 행동 시작 #${d.action_start} · 관찰 시점 ${d.points.length}개`;
  $('sh-reasoning').textContent=st.output?.reasoning||'—';$('sh-action').textContent=st.command||'—';$('sh-observation').textContent=st.observation||'—';
  $('sh-findings').innerHTML=[...(st.static_findings||[]),...(st.effect_findings||[])].map(f=>`<code>${esc(f)}</code>`).join('')+(st.oracle_reason?`<span class="status">${esc(st.oracle_reason)}</span>`:'');
  const pts=new Set(d.points.map(p=>p.token_index));
  $('sh-tokens').innerHTML=d.tokens.map(t=>`<span class="cap-tok ${pts.has(t.index)?'observed':t.role==='prompt'?'prompt':'reasoning'}" data-point="${pts.has(t.index)?t.index:''}" title="#${t.index}">${esc(String(t.text??'').replace(/\n/g,'⏎\n'))}</span>`).join('');
  $('sh-layer').innerHTML=d.layers.map(l=>`<option value="${l}">Layer ${l}</option>`).join('');
  const pre=d.points.find(p=>p.kind==='pre_action')||d.points[d.points.length-1];shVocabOffset=0;shValueOffset=0;
  await shSelectCell(pre.token_index,shLayer!=null&&d.layers.includes(shLayer)?shLayer:d.layers[d.layers.length-1])}
 catch(e){if(cur===shReq){$('sh-step-title').textContent='step 불러오기 실패';$('sh-step-meta').textContent=e.message}}}
function shRenderGrid(){const d=shData;if(!d)return;shDrawGrid($('sh-grid'),d.stats.l2,d.points.length,{layers:d.layers,colLabel:k=>'#'+d.points[k].token_index,selectedCol:d.points.findIndex(p=>p.token_index===shPoint),selectedRow:d.layers.indexOf(shLayer)})}
async function shSelectCell(point,layer){shPoint=point;shLayer=layer;$('sh-layer').value=String(layer);shRenderGrid();
 const box=$('sh-tokens');box.querySelectorAll('.cap-tok').forEach(el=>el.style.outline=+el.dataset.point===point&&el.dataset.point!==''?'2px solid var(--accent)':'');const el=box.querySelector(`[data-point="${point}"]`);if(el)box.scrollTop=Math.max(0,el.offsetTop-box.clientHeight/2);
 const p=shData.points.find(x=>x.token_index===point),li=shData.layers.indexOf(layer);
 $('sh-cell-title').textContent=`관찰 #${point} (${p?.kind}) "${tvShow(p?.text??'')}" · Layer ${layer}`;
 $('sh-stats').innerHTML=[['L2',shData.stats.l2[li][shData.points.indexOf(p)]],['mean',shData.stats.mean[li][shData.points.indexOf(p)]],['std',shData.stats.std[li][shData.points.indexOf(p)]],['max |x|',shData.stats.max_abs[li][shData.points.indexOf(p)]]].map(([k,v])=>`<div><b>${k}</b><span>${tvFmt(v)}</span></div>`).join('');
 const cur=++shCellReq;await Promise.all([shLoadValues(cur),shLoadVocab(cur)])}
async function shLoadValues(cur){document.querySelectorAll('#sh-sorts button').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.sort===shValueSort)));
 try{const v=await tvJson('/api/rollouts/vector?'+new URLSearchParams({id:shId,step:shStep,point:shPoint,layer:shLayer,offset:shValueOffset,limit:256,sort:shValueSort}));if(cur!==shCellReq)return;
  shSpark=v;drawEnvelope($('sh-spark'),v.envelope,v.numel,cssVar('--series-1'),`Layer ${shLayer}`);$('sh-spark-note').textContent=`원소 ${v.numel.toLocaleString()}개`;
  $('sh-top').innerHTML='<span class="status">|값| 상위</span>'+v.top.map(t=>`<code>#${t.index} ${esc(fmt(t.value))}</code>`).join('');
  const mean=v.stats.mean,std=v.stats.std;$('sh-values').innerHTML=v.values.map(x=>`<tr><td class="num">${x.index}</td><td class="num ${typeof x.value==='number'&&std>0&&Math.abs(x.value-mean)>3*std?'outlier':''}">${esc(x.value)}</td></tr>`).join('');
  $('sh-value-meta').textContent=`${v.offset}–${v.offset+v.values.length} / ${v.numel.toLocaleString()} · ${tvSortLabel[shValueSort]}`;$('sh-val-prev').disabled=v.offset===0;$('sh-val-next').disabled=v.offset+v.values.length>=v.numel}
 catch(e){if(cur===shCellReq)$('sh-value-meta').textContent=e.message}}
async function shLoadVocab(cur){document.querySelectorAll('#sh-vocab-sorts button').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.sort===shVocabSort)));$('sh-vocab-meta').textContent='201,088개 토큰에 투영 중…';
 try{const d=await tvJson('/api/rollouts/vocab?'+new URLSearchParams({id:shId,step:shStep,point:shPoint,layer:shLayer,offset:shVocabOffset,limit:100,sort:shVocabSort,q:$('sh-vocab-q').value.trim(),norm:$('sh-vocab-norm').checked?'1':'0'}));if(cur!==shCellReq)return;
  const st=d.stats,m=Math.max(Math.abs(st.max),Math.abs(st.min))||1,neg=hexRgb(cssVar('--div-neg')),pos=hexRgb(cssVar('--div-pos')),gen=d.marks.generated,src=d.marks.source,prob=p=>p<1e-4?p.toExponential(2):(p*100).toFixed(2)+'%';
  $('sh-vocab-rows').innerHTML=d.rows.map(r=>{const t=r.logit/m,c=t>=0?pos:neg;return `<tr class="${gen&&r.id===gen.id?'tv-vocab-gen':''}"><td class="num">${r.rank.toLocaleString()}</td><td class="num">${r.id}</td><td class="mono">${r.text==null?'<span class="muted">(미할당 ID)</span>':esc(tvShow(r.text))}${gen&&r.id===gen.id?' <span class="badge safe">실제 다음 토큰</span>':''}${src&&r.id===src.id?' <span class="badge unknown">관찰 토큰</span>':''}</td><td class="mono muted">${esc(r.piece??'')}</td><td class="num mono" style="background:rgba(${c.join(',')},${(Math.min(1,Math.abs(t))*.55).toFixed(3)})">${esc(fmt(r.logit))}</td><td class="num mono">${prob(r.prob)}</td></tr>`}).join('')||'<tr><td colspan="6"><div class="empty">검색 결과가 없습니다.</div></td></tr>';
  $('sh-vocab-meta').textContent=`${d.is_model_output?'마지막 레이어 → 실제 모델 출력과 같은 계산':'logit lens'} · 실제 다음 토큰 ${gen?`"${tvShow(gen.text??'')}" 순위 ${gen.rank.toLocaleString()} (p ${prob(gen.prob)})`:'—'} · 1위 "${tvShow(d.top[0]?.text??'')}" · ${(d.offset+1).toLocaleString()}–${(d.offset+d.rows.length).toLocaleString()} / ${d.total.toLocaleString()}`;
  $('sh-vocab-prev').disabled=d.offset===0;$('sh-vocab-next').disabled=d.offset+d.rows.length>=d.total}
 catch(e){if(cur===shCellReq){$('sh-vocab-rows').innerHTML=`<tr><td colspan="6"><div class="empty">${esc(e.message)}</div></td></tr>`;$('sh-vocab-meta').textContent=''}}}
function shRedraw(){if($('view-scenario-hidden').hidden)return;shRenderTrend();shRenderGrid();if(shSpark)drawEnvelope($('sh-spark'),shSpark.envelope,shSpark.numel,cssVar('--series-1'),`Layer ${shLayer}`)}
$('sh-refresh').onclick=shLoadList;$('sh-scenario').onchange=()=>shFillRollouts();$('sh-rollout').onchange=()=>shOpen($('sh-rollout').value);
$('sh-steps').onclick=ev=>{const b=ev.target.closest('button[data-step]');if(b)shSelectStep(+b.dataset.step)};
$('sh-trend').onclick=ev=>{const c=shCell($('sh-trend'),ev);if(c&&shTrend)shSelectStep(shTrend.steps[c.col].step_index)};
$('sh-trend').onmousemove=ev=>{const c=shCell($('sh-trend'),ev);if(!c||!shTrend){hideTip();return}const s=shTrend.steps[c.col];showTip(ev,`<b>Step ${s.step_index} · Layer ${shTrend.layers[c.row]}</b>\npre_action L2 ${tvFmt(shTrend.pre_action_l2[c.row][c.col])}\n판정 ${s.policy_label===1?'위반':s.policy_label===0?'준수':'미판정'} · ${esc((s.command||s.outcome||'').slice(0,80))}`)};$('sh-trend').onmouseleave=hideTip;
$('sh-grid').onclick=ev=>{const c=shCell($('sh-grid'),ev);if(c&&shData)shSelectCell(shData.points[c.col].token_index,shData.layers[c.row])};
$('sh-grid').onmousemove=ev=>{const c=shCell($('sh-grid'),ev);if(!c||!shData){hideTip();return}const p=shData.points[c.col];showTip(ev,`<b>#${p.token_index} ${esc(p.kind)} · Layer ${shData.layers[c.row]}</b>\n"${esc(tvShow(p.text??''))}"\nL2 ${tvFmt(shData.stats.l2[c.row][c.col])}`)};$('sh-grid').onmouseleave=hideTip;
$('sh-tokens').onclick=ev=>{const el=ev.target.closest('[data-point]');if(el&&el.dataset.point!=='')shSelectCell(+el.dataset.point,shLayer)};
$('sh-layer').onchange=()=>shSelectCell(shPoint,+$('sh-layer').value);
$('sh-sorts').onclick=ev=>{const b=ev.target.closest('button[data-sort]');if(!b)return;shValueSort=b.dataset.sort;shValueOffset=0;shLoadValues(shCellReq)};
$('sh-val-prev').onclick=()=>{shValueOffset=Math.max(0,shValueOffset-256);shLoadValues(shCellReq)};$('sh-val-next').onclick=()=>{shValueOffset+=256;shLoadValues(shCellReq)};
$('sh-vocab-sorts').onclick=ev=>{const b=ev.target.closest('button[data-sort]');if(!b)return;shVocabSort=b.dataset.sort;shVocabOffset=0;shLoadVocab(shCellReq)};
$('sh-vocab-prev').onclick=()=>{shVocabOffset=Math.max(0,shVocabOffset-100);shLoadVocab(shCellReq)};$('sh-vocab-next').onclick=()=>{shVocabOffset+=100;shLoadVocab(shCellReq)};
$('sh-vocab-norm').onchange=()=>{shVocabOffset=0;shLoadVocab(shCellReq)};let shVocabTimer=null;$('sh-vocab-q').oninput=()=>{clearTimeout(shVocabTimer);shVocabTimer=setTimeout(()=>{shVocabOffset=0;shLoadVocab(shCellReq)},300)};
$('sh-open-record').onclick=()=>{if(!shId)return;roLoaded=true;showView('view-rollouts');roLoadList().then(()=>roSelect(shId))};
async function shOpenFromRecord(id,step){shLoaded=true;showView('view-scenario-hidden');await shLoadList();const r=shRollouts.find(x=>x.id===id);if(!r)return;$('sh-scenario').value=r.scenario_id;$('sh-rollout').innerHTML='';shFillRollouts(id);await shOpen(id,step)}
if(location.pathname==='/scenario-hidden')showView('view-scenario-hidden');
if(location.pathname==='/hooks')showView('view-hooks');

</script></body></html>"""


class ArtifactIndex:
    """Incrementally index Hook JSONL records into a local transactional SQLite DB."""

    def __init__(self, data_dir: Path, db_path: Path):
        self.data_dir = data_dir
        self.db_path = db_path
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._initialize()

    def connect(self):
        connection = sqlite3.connect(self.db_path, timeout=30)
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA busy_timeout=30000")
        connection.execute("PRAGMA foreign_keys=ON")
        connection.execute("PRAGMA synchronous=NORMAL")
        return connection

    def _initialize(self):
        with self.connect() as db:
            db.execute("PRAGMA journal_mode=WAL")
            db.execute("PRAGMA synchronous=NORMAL")
            db.executescript("""
                CREATE TABLE IF NOT EXISTS sessions (
                    id INTEGER PRIMARY KEY,
                    artifact_dir TEXT NOT NULL UNIQUE,
                    run_name TEXT NOT NULL,
                    run_id TEXT NOT NULL DEFAULT '',
                    step_name TEXT NOT NULL,
                    started_at TEXT NOT NULL,
                    collection_date TEXT NOT NULL,
                    completed_at TEXT,
                    task_text TEXT NOT NULL,
                    status TEXT NOT NULL,
                    phase TEXT,
                    context_json TEXT NOT NULL DEFAULT '{}',
                    manifest_mtime REAL NOT NULL DEFAULT 0,
                    records_offset INTEGER NOT NULL DEFAULT 0
                );
                CREATE TABLE IF NOT EXISTS records (
                    record_key TEXT PRIMARY KEY,
                    session_id INTEGER NOT NULL REFERENCES sessions(id) ON DELETE CASCADE,
                    record_id INTEGER NOT NULL,
                    layer_index INTEGER NOT NULL,
                    module TEXT NOT NULL,
                    call_index INTEGER,
                    location TEXT NOT NULL,
                    kind TEXT NOT NULL,
                    shape_json TEXT,
                    source_dtype TEXT,
                    storage_dtype TEXT,
                    filename TEXT,
                    record_json TEXT NOT NULL
                );
                CREATE INDEX IF NOT EXISTS idx_sessions_date ON sessions(collection_date DESC, started_at DESC, id DESC);
                CREATE INDEX IF NOT EXISTS idx_records_session_order ON records(session_id, record_id);
                CREATE INDEX IF NOT EXISTS idx_records_layer ON records(layer_index, session_id);
                CREATE INDEX IF NOT EXISTS idx_records_layer_kind_session_order
                    ON records(layer_index, kind, session_id, record_id);
                CREATE INDEX IF NOT EXISTS idx_records_module ON records(module);
                CREATE TABLE IF NOT EXISTS ingest_errors (
                    id INTEGER PRIMARY KEY,
                    artifact_dir TEXT NOT NULL,
                    byte_offset INTEGER NOT NULL,
                    message TEXT NOT NULL,
                    created_at TEXT NOT NULL
                );
                CREATE UNIQUE INDEX IF NOT EXISTS idx_ingest_error_unique
                    ON ingest_errors(artifact_dir, byte_offset, message);
                CREATE TABLE IF NOT EXISTS detector_results (
                    result_path TEXT PRIMARY KEY,
                    run_id TEXT NOT NULL,
                    token_index INTEGER,
                    monitor TEXT NOT NULL,
                    status TEXT NOT NULL,
                    risk_score REAL,
                    alarm INTEGER,
                    result_json TEXT NOT NULL,
                    source_mtime REAL NOT NULL
                );
                CREATE INDEX IF NOT EXISTS idx_detector_run ON detector_results(run_id, monitor, token_index);
            """)
            session_columns = {row[1] for row in db.execute("PRAGMA table_info(sessions)")}
            if "run_id" not in session_columns:
                db.execute("ALTER TABLE sessions ADD COLUMN run_id TEXT NOT NULL DEFAULT ''")
            if "context_json" not in session_columns:
                db.execute("ALTER TABLE sessions ADD COLUMN context_json TEXT NOT NULL DEFAULT '{}'")

    @staticmethod
    def _collection_date(timestamp: str) -> str:
        try:
            parsed = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
            if parsed.tzinfo is None:
                parsed = parsed.replace(tzinfo=timezone.utc)
            return parsed.astimezone().date().isoformat()
        except (TypeError, ValueError):
            return "unknown"

    def sync_once(self) -> None:
        if not self.data_dir.exists():
            return
        for records_path in self.data_dir.rglob("records.jsonl"):
            if records_path.parent.name != "hook_inspection" and records_path.parent.parent.name != "generation":
                continue
            try:
                self._ingest(records_path)
            except (OSError, sqlite3.Error) as error:
                # Keep the watcher alive; the source remains untouched for recovery.
                with self.connect() as db:
                    relative = records_path.parent.relative_to(self.data_dir).as_posix()
                    db.execute(
                        "INSERT OR IGNORE INTO ingest_errors(artifact_dir, byte_offset, message, created_at) VALUES(?,?,?,?)",
                        (relative, -1, str(error), datetime.now(timezone.utc).isoformat()),
                    )

    def sync_detector_results(self, detector_dir: Path | None) -> None:
        if detector_dir is None or not detector_dir.exists():
            return
        for result_path in detector_dir.rglob("*.json"):
            try:
                stat = result_path.stat()
                relative = result_path.resolve().relative_to(detector_dir.resolve()).as_posix()
                with self.connect() as db:
                    previous = db.execute("SELECT source_mtime FROM detector_results WHERE result_path=?", (relative,)).fetchone()
                if previous and previous[0] == stat.st_mtime:
                    continue
                result = json.loads(result_path.read_text(encoding="utf-8"))
                # This tree also contains dataset inventories and other JSON
                # artifacts. Only detector-result objects belong in this index.
                if not isinstance(result, dict):
                    continue
                snapshot = result.get("snapshot") or {}
                configuration = result.get("configuration") or {}
                if not isinstance(snapshot, dict) or not isinstance(configuration, dict):
                    continue
                monitor = configuration.get("monitor")
                run_id = snapshot.get("run_id")
                if not monitor or not run_id or "alarm" not in result:
                    continue
                token_index = snapshot.get("token_index")
                alarm = result.get("alarm")
                with self.connect() as db:
                    db.execute("""INSERT INTO detector_results
                        (result_path, run_id, token_index, monitor, status, risk_score, alarm, result_json, source_mtime)
                        VALUES(?,?,?,?,?,?,?,?,?) ON CONFLICT(result_path) DO UPDATE SET
                        run_id=excluded.run_id, token_index=excluded.token_index, monitor=excluded.monitor,
                        status=excluded.status, risk_score=excluded.risk_score, alarm=excluded.alarm,
                        result_json=excluded.result_json, source_mtime=excluded.source_mtime""",
                               (relative, run_id, token_index, monitor, str(result.get("status", "unknown")),
                                result.get("risk_score"), None if alarm is None else int(bool(alarm)),
                                json.dumps(result, ensure_ascii=False, allow_nan=False), stat.st_mtime))
            except (OSError, json.JSONDecodeError, sqlite3.Error, ValueError, TypeError):
                continue

    def _ingest(self, records_path: Path) -> None:
        relative = records_path.parent.relative_to(self.data_dir).as_posix()
        parts = Path(relative).parts
        run_name = parts[0] if parts else "unknown"
        step_name = next((part for part in parts if "_step_" in part), "unknown")
        manifest_path = records_path.parent / "manifest.json"
        try:
            manifest_mtime = manifest_path.stat().st_mtime
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            manifest_mtime = 0.0
            manifest = {}
        fallback_time = datetime.fromtimestamp(records_path.stat().st_mtime, timezone.utc).isoformat()
        started_at = manifest.get("started_at") or fallback_time
        collection_date = self._collection_date(started_at)
        context = manifest.get("context") or {}
        task_text = context.get("task_text") or context.get("user_task") or "미기록"
        status = manifest.get("status", "미기록")
        phase = manifest.get("phase")
        completed_at = manifest.get("completed_at")
        size = records_path.stat().st_size

        with self.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            db.execute("""INSERT INTO sessions
                (artifact_dir, run_name, run_id, step_name, started_at, collection_date, completed_at,
                 task_text, status, phase, context_json, manifest_mtime)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?)
                ON CONFLICT(artifact_dir) DO UPDATE SET
                    run_id=excluded.run_id,
                    started_at=excluded.started_at, collection_date=excluded.collection_date,
                    completed_at=excluded.completed_at, task_text=excluded.task_text,
                    status=excluded.status, phase=excluded.phase, context_json=excluded.context_json,
                    manifest_mtime=excluded.manifest_mtime""",
                       (relative, run_name, str(context.get("run_id", "")), step_name, started_at, collection_date, completed_at,
                        task_text, status, phase, json.dumps(context, ensure_ascii=False, allow_nan=False), manifest_mtime))
            session_id = db.execute("SELECT id FROM sessions WHERE artifact_dir=?", (relative,)).fetchone()[0]
            offset = int(db.execute("SELECT records_offset FROM sessions WHERE id=?", (session_id,)).fetchone()[0])
            if size < offset:
                db.execute("DELETE FROM records WHERE session_id=?", (session_id,))
                offset = 0
            with records_path.open("rb") as source:
                source.seek(offset)
                while True:
                    line_start = source.tell()
                    line = source.readline()
                    if not line or not line.endswith(b"\n"):
                        offset = line_start
                        break
                    next_offset = source.tell()
                    try:
                        record = json.loads(line)
                        layer = record.get("layer_index")
                        if layer in VISIBLE_LAYERS:
                            record_id = int(record["record_id"])
                            key = f"{relative}#{record_id}"
                            db.execute("""INSERT OR REPLACE INTO records
                                (record_key, session_id, record_id, layer_index, module, call_index,
                                 location, kind, shape_json, source_dtype, storage_dtype, filename, record_json)
                                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                                       (key, session_id, record_id, layer, str(record.get("module", "")),
                                        record.get("call_index"), str(record.get("location", "")),
                                        str(record.get("kind", "unknown")),
                                        json.dumps(record.get("shape"), ensure_ascii=False),
                                        record.get("source_dtype"), record.get("storage_dtype"),
                                        record.get("filename"), json.dumps(record, ensure_ascii=False, allow_nan=False)))
                    except (json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
                        db.execute("INSERT OR IGNORE INTO ingest_errors(artifact_dir, byte_offset, message, created_at) VALUES(?,?,?,?)",
                                   (relative, line_start, str(error), datetime.now(timezone.utc).isoformat()))
                    offset = next_offset
            db.execute("UPDATE sessions SET records_offset=? WHERE id=?", (offset, session_id))

    @staticmethod
    def _apply_token_mapping(item: dict, context: dict) -> dict:
        forward_index = item.get("forward_call_index")
        token_map = context.get("generation_token_map") or []
        if isinstance(forward_index, int) and 0 <= forward_index < len(token_map):
            item.update(token_map[forward_index])
            shape = item.get("shape") or []
            if len(shape) >= 2:
                axis = (1 if shape[0] == 1 else 0) if len(shape) == 2 else len(shape) - 2
                # The forward's input length is known: the full prompt for prefill (forward 0)
                # and one position per KV-cached decode forward. Shape alone is ambiguous,
                # e.g. decode [1, 2880] or router [1, 32] would pick the feature axis.
                prompt_length = len(context.get("input_ids") or [])
                expected = 1 if forward_index > 0 else prompt_length
                if expected and shape[axis] != expected:
                    matches = [index for index, size in enumerate(shape) if size == expected]
                    axis = matches[0] if matches else None
                if axis is not None:
                    item["generation_sequence_axis"] = axis
                    item["generation_source_position"] = max(0, int(shape[axis]) - 1)
        return item

    def query_records(self, query: dict[str, str], offset: int, limit: int) -> dict:
        clauses = ["r.layer_index IN (0, 11, 23)"]
        params: list[object] = []
        for field, column in (("layer", "r.layer_index"), ("phase", "s.phase"),
                              ("kind", "r.kind"), ("date", "s.collection_date")):
            value = query.get(field)
            if value:
                clauses.append(f"{column}=?")
                params.append(int(value) if field == "layer" else value)
        run_filter = query.get("run", "")
        if run_filter:
            clauses.append("COALESCE(NULLIF(s.run_id,''),s.run_name)=?")
            params.append(run_filter)
        risk = query.get("risk", "")
        if risk in {"risky", "M1", "M2", "activation_probe"}:
            clauses.append("EXISTS (SELECT 1 FROM detector_results d WHERE d.run_id=s.run_id AND d.alarm=1" +
                           (" AND d.monitor=?" if risk != "risky" else "") + ")")
            if risk != "risky":
                params.append(risk)
        search = query.get("q", "").strip()
        if search:
            clauses.append("(r.module LIKE ? OR r.location LIKE ? OR s.task_text LIKE ? OR s.run_name LIKE ? OR s.step_name LIKE ?)")
            params.extend([f"%{search}%"] * 5)
        where = " AND ".join(clauses)
        with self.connect() as db:
            db.execute("BEGIN")
            total = db.execute(f"SELECT COUNT(*) FROM records r JOIN sessions s ON s.id=r.session_id WHERE {where}", params).fetchone()[0]
            rows = db.execute(f"""SELECT r.record_key, r.record_json, s.run_id, s.run_name, s.step_name,
                s.collection_date, s.started_at, s.completed_at, s.task_text, s.status, s.context_json
                FROM records r JOIN sessions s ON s.id=r.session_id
                WHERE {where}
                ORDER BY s.collection_date DESC, s.started_at DESC, s.id DESC, r.record_id ASC
                LIMIT ? OFFSET ?""", (*params, limit, offset)).fetchall()
            records = []
            for row in rows:
                item = json.loads(row["record_json"])
                context = json.loads(row["context_json"] or "{}")
                self._apply_token_mapping(item, context)
                item.update(key=row["record_key"], run=row["run_name"], run_id=row["run_id"], step=row["step_name"],
                            collection_date=row["collection_date"], collected_at=row["started_at"],
                            completed_at=row["completed_at"], task=row["task_text"],
                            session_status=row["status"])
                records.append(item)
            run_ids = sorted({row["run_id"] for row in rows if row["run_id"]})
            detectors_by_run = {}
            if run_ids:
                marks = ",".join("?" for _ in run_ids)
                detector_rows = db.execute(
                    f"SELECT run_id, token_index, monitor, status, risk_score, alarm, result_json "
                    f"FROM detector_results WHERE run_id IN ({marks}) ORDER BY monitor",
                    run_ids,
                ).fetchall()
                for detector in detector_rows:
                    raw = json.loads(detector["result_json"])
                    detectors_by_run.setdefault(detector["run_id"], []).append({
                        "token_index": detector["token_index"], "monitor": detector["monitor"],
                        "status": detector["status"], "risk_score": detector["risk_score"],
                        "alarm": detector["alarm"], "reason": raw.get("reason", raw.get("error")),
                    })
            for item, row in zip(records, rows):
                item["detectors"] = detectors_by_run.get(row["run_id"], [])
            facets = {
                "dates": [row[0] for row in db.execute("SELECT DISTINCT collection_date FROM sessions ORDER BY collection_date DESC")],
                "runs": [],
                "layers": [row[0] for row in db.execute("SELECT DISTINCT layer_index FROM records ORDER BY layer_index")],
                "phases": [row[0] for row in db.execute("SELECT DISTINCT phase FROM sessions WHERE phase IS NOT NULL ORDER BY phase")],
                "sessions": db.execute("SELECT COUNT(*) FROM sessions").fetchone()[0],
                "ingest_errors": db.execute("SELECT COUNT(*) FROM ingest_errors").fetchone()[0],
            }
            date_filter = query.get("date", "")
            run_rows = db.execute("""SELECT COALESCE(NULLIF(run_id,''),run_name) AS batch_key,
                    MAX(started_at) AS latest, collection_date, run_name, task_text
                FROM sessions WHERE (?='' OR collection_date=?)
                GROUP BY COALESCE(NULLIF(run_id,''),run_name), collection_date
                ORDER BY latest DESC, batch_key DESC""", (date_filter, date_filter)).fetchall()
            facets["runs"] = [{
                "key": row["batch_key"],
                "label": f"{row['latest'] or '시각 미기록'} · {row['task_text'] or 'Task 미기록'} · {row['batch_key']}",
            } for row in run_rows]
        return {"records": records, "total": total, "offset": offset, "limit": limit, **facets}

    def lookup_record(self, key: str):
        with self.connect() as db:
            row = db.execute("""SELECT r.record_json, s.artifact_dir, s.context_json FROM records r
                JOIN sessions s ON s.id=r.session_id WHERE r.record_key=?""", (key,)).fetchone()
        if not row:
            return None
        session_dir = (self.data_dir / row["artifact_dir"]).resolve()
        if not session_dir.is_relative_to(self.data_dir.resolve()):
            return None
        record = json.loads(row["record_json"])
        self._apply_token_mapping(record, json.loads(row["context_json"] or "{}"))
        return session_dir, record

    def hook_sessions(self, search: str, offset: int, limit: int) -> dict:
        pattern = f"%{search}%"
        where = "(artifact_dir LIKE ? OR task_text LIKE ? OR phase LIKE ?)"
        with self.connect() as db:
            total = db.execute(f"SELECT COUNT(*) FROM sessions WHERE {where}",
                               (pattern, pattern, pattern)).fetchone()[0]
            rows = db.execute(f"""SELECT id, artifact_dir, run_id, step_name, task_text,
                phase, status, started_at FROM sessions WHERE {where}
                ORDER BY started_at DESC, id DESC LIMIT ? OFFSET ?""",
                (pattern, pattern, pattern, limit, offset)).fetchall()
        return {"sessions": [dict(row) for row in rows], "total": total,
                "offset": offset, "limit": limit}

    def hook_map(self, session_id: int) -> dict:
        with self.connect() as db:
            session = db.execute("""SELECT id, artifact_dir, run_id, step_name,
                task_text, phase, status, started_at FROM sessions WHERE id=?""",
                (session_id,)).fetchone()
            if session is None:
                raise ValueError("수집 세션을 찾을 수 없습니다.")
            manifest_path = (self.data_dir / session["artifact_dir"] / "manifest.json").resolve()
            if not manifest_path.is_relative_to(self.data_dir.resolve()):
                raise ValueError("Invalid artifact path.")
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            if (not isinstance(manifest, dict) or not isinstance(manifest.get("modules"), list)
                    or manifest.get("schema_version") != "argus-v.hook-inspection.v1"):
                raise ValueError("Hook 등록 목록이 없는 manifest입니다.")
            observed = {row["module"]: dict(row) for row in db.execute("""
                SELECT module, MAX(call_index)+1 AS calls, COUNT(*) AS records,
                    SUM(CASE WHEN location LIKE 'input%' THEN 1 ELSE 0 END) AS inputs,
                    SUM(CASE WHEN location LIKE 'output%' THEN 1 ELSE 0 END) AS outputs
                FROM records WHERE session_id=? GROUP BY module""", (session_id,))}
            samples = {}
            for row in db.execute("""SELECT r.module, r.record_key, r.record_json
                FROM records r JOIN (
                    SELECT module, location, MAX(record_id) AS latest FROM records
                    WHERE session_id=? GROUP BY module, location
                ) g ON r.module=g.module AND r.record_id=g.latest
                WHERE r.session_id=? ORDER BY r.record_id""", (session_id, session_id)):
                record = json.loads(row["record_json"])
                samples.setdefault(row["module"], []).append({
                    "key": row["record_key"], "location": record.get("location"),
                    "kind": record.get("kind"), "shape": record.get("shape"),
                    "dtype": record.get("source_dtype") or record.get("python_type"),
                    "meaning": record.get("meaning"), "call_index": record.get("call_index"),
                })
        nodes = []
        registered = {m["path"] for m in manifest["modules"]
                      if isinstance(m, dict) and isinstance(m.get("path"), str)}
        for module in manifest["modules"]:
            if not isinstance(module, dict) or module.get("path") not in registered:
                continue
            path = module["path"]
            parent = path.rpartition(".")[0]
            while parent and parent not in registered:
                parent = parent.rpartition(".")[0]
            if not parent and path != "<model>" and "<model>" in registered:
                parent = "<model>"
            evidence = observed.get(path, {})
            calls = max(int(module.get("calls") or 0), int(evidence.get("calls") or 0))
            state = "called" if calls else (
                "pending" if manifest.get("status") == "running" else "not_called")
            nodes.append({"path": path, "parent": parent or None,
                          "class": module.get("class"), "layer": module.get("layer"),
                          "calls": calls, "status": state,
                          "unfinished_calls": module.get("unfinished_calls", 0),
                          "inputs": evidence.get("inputs", 0), "outputs": evidence.get("outputs", 0),
                          "records": evidence.get("records", 0), "samples": samples.get(path, [])})
        return {"session": dict(session), "model_type": manifest.get("model_type"),
                "identity": manifest.get("identity", {}), "status": manifest.get("status"),
                "started_at": manifest.get("started_at"), "completed_at": manifest.get("completed_at"),
                "selected_layers": manifest.get("selected_layers"),
                "include_non_block": manifest.get("include_non_block_modules"),
                "indexed_layers": sorted(VISIBLE_LAYERS), "modules": nodes,
                "source": session["artifact_dir"] + "/manifest.json",
                "totals": {"registered": len(nodes), "called": sum(n["calls"] > 0 for n in nodes),
                           "records": manifest.get("record_count", 0),
                           "tensors": manifest.get("tensor_count", 0)}}

    # ---------- token view: generation sessions, one forward per generated token ----------
    _TOKEN_SESSION_WHERE = ("json_extract(context_json,'$.generation_token_map') IS NOT NULL "
                            "AND (artifact_dir LIKE ? OR task_text LIKE ? OR run_id LIKE ?)")

    def token_sessions(self, search: str, offset: int, limit: int) -> dict:
        pattern = f"%{search}%"
        with self.connect() as db:
            total = db.execute(f"SELECT COUNT(*) FROM sessions WHERE {self._TOKEN_SESSION_WHERE}",
                               (pattern, pattern, pattern)).fetchone()[0]
            rows = db.execute(f"""SELECT id, artifact_dir, run_id, step_name, task_text, status, started_at,
                json_array_length(context_json,'$.generation_token_map') AS token_count
                FROM sessions WHERE {self._TOKEN_SESSION_WHERE}
                ORDER BY started_at DESC, id DESC LIMIT ? OFFSET ?""",
                (pattern, pattern, pattern, limit, offset)).fetchall()
        return {"sessions": [dict(row) for row in rows], "total": total, "offset": offset, "limit": limit}

    def token_session(self, session_id: int) -> tuple[Path, dict, dict]:
        with self.connect() as db:
            row = db.execute("""SELECT id, artifact_dir, run_id, step_name, task_text, status, started_at,
                completed_at, context_json FROM sessions WHERE id=?""", (session_id,)).fetchone()
        if row is None:
            raise ValueError("수집 세션을 찾을 수 없습니다.")
        session_dir = (self.data_dir / row["artifact_dir"]).resolve()
        if not session_dir.is_relative_to(self.data_dir.resolve()):
            raise ValueError("Invalid artifact path.")
        meta = {key: row[key] for key in row.keys() if key != "context_json"}
        return session_dir, meta, json.loads(row["context_json"] or "{}")

    def sessions_with_context(self) -> list[dict]:
        with self.connect() as db:
            rows = db.execute("""SELECT id, artifact_dir, run_id, step_name, status, phase, context_json
                FROM sessions ORDER BY started_at DESC, id DESC""").fetchall()
        return [{**{key: row[key] for key in row.keys() if key != "context_json"},
                 "context": json.loads(row["context_json"] or "{}")} for row in rows]

    def token_forward_records(self, session_id: int, forward_index: int) -> list[tuple[str, dict]]:
        with self.connect() as db:
            rows = db.execute("""SELECT record_key, record_json FROM records WHERE session_id=?
                AND json_extract(record_json,'$.forward_call_index')=? ORDER BY record_id""",
                (session_id, forward_index)).fetchall()
        return [(row["record_key"], json.loads(row["record_json"])) for row in rows]

    def token_location_records(self, session_id: int, location: str, rel_module: str) -> list[tuple[str, dict]]:
        """Records at one block-relative module/location for the token-view layers, all forwards."""
        with self.connect() as db:
            sample = db.execute("SELECT module FROM records WHERE session_id=? AND layer_index=? LIMIT 1",
                                (session_id, TOKEN_VIEW_LAYERS[0])).fetchone()
            if sample is None:
                return []
            match = re.match(r"^(.*?\.layers)\.\d+", sample["module"])
            if not match:
                return []
            modules = [f"{match.group(1)}.{layer}{rel_module}" for layer in TOKEN_VIEW_LAYERS]
            marks = ",".join("?" for _ in modules)
            rows = db.execute(f"""SELECT record_key, record_json FROM records WHERE session_id=?
                AND module IN ({marks}) AND location=? ORDER BY record_id""",
                (session_id, *modules, location)).fetchall()
        return [(row["record_key"], json.loads(row["record_json"])) for row in rows]


_TOKENIZER_CACHE: dict[str, dict[int, str]] = {}
_TOKENIZER_LOCK = threading.Lock()


def load_tokenizer_pieces(path: Path | None) -> dict[int, str]:
    """id -> tokenizer piece from a Hugging Face tokenizer.json (vocab + added tokens); {} if unavailable."""
    if path is None:
        return {}
    cache_key = str(path)
    with _TOKENIZER_LOCK:
        if cache_key not in _TOKENIZER_CACHE:
            pieces: dict[int, str] = {}
            try:
                tokenizer = json.loads(Path(path).read_text(encoding="utf-8"))
                vocab = tokenizer.get("model", {}).get("vocab") or {}
                pieces = {int(index): piece for piece, index in vocab.items()}
                pieces.update({int(item["id"]): item["content"] for item in tokenizer.get("added_tokens", [])})
            except (OSError, AttributeError, TypeError, ValueError, KeyError):
                pieces = {}
            _TOKENIZER_CACHE[cache_key] = pieces
        return _TOKENIZER_CACHE[cache_key]


class LogitLens:
    """Project a residual-stream vector onto the output vocabulary: lm_head(final_norm(h)).

    BF16 weights are memory-mapped straight from the local safetensors checkpoint and never
    modified. Applied to the last layer's block output this is the model's own next-token
    logit computation (up to bf16 operation order).
    """

    def __init__(self, model_dir: Path | None, tokenizer_path: Path | None = None):
        self.model_dir = model_dir
        self.tokenizer_path = tokenizer_path
        self._weights = None
        self._error: str | None = None
        self._vocab_text = None
        self._lock = threading.Lock()
        self._cache: OrderedDict = OrderedDict()

    @staticmethod
    def _bf16(values) -> np.ndarray:
        return (np.asarray(values).astype(np.uint32) << 16).view(np.float32)

    def _tensor(self, index: dict, name: str) -> np.ndarray:
        path = (self.model_dir / index[name]).resolve()
        if not path.is_relative_to(self.model_dir.resolve()):
            raise ValueError("Invalid weight path.")
        with path.open("rb") as handle:
            header_size = int.from_bytes(handle.read(8), "little")
            meta = json.loads(handle.read(header_size))[name]
        if meta.get("dtype") != "BF16":
            raise ValueError(f"{name} dtype {meta.get('dtype')} is not supported (BF16 expected).")
        start, _end = meta["data_offsets"]
        return np.memmap(path, dtype=np.uint16, mode="r", offset=8 + header_size + start, shape=tuple(meta["shape"]))

    def _load(self):
        with self._lock:
            if self._weights is None and self._error is None:
                try:
                    if self.model_dir is None:
                        raise ValueError("모델 폴더가 지정되지 않았습니다.")
                    config = json.loads((self.model_dir / "config.json").read_text(encoding="utf-8"))
                    index = json.loads((self.model_dir / "model.safetensors.index.json").read_text(encoding="utf-8"))["weight_map"]
                    head = self._tensor(index, "lm_head.weight")
                    norm = self._bf16(self._tensor(index, "model.norm.weight"))
                    self._weights = {"head": head, "norm": norm, "eps": float(config.get("rms_norm_eps", 1e-5)),
                                     "layers": int(config.get("num_hidden_layers", 0)),
                                     "vocab": int(head.shape[0]), "hidden": int(head.shape[1])}
                except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError) as error:
                    self._error = f"lm_head 가중치를 읽을 수 없습니다 ({self.model_dir}): {error}"
        if self._weights is None:
            raise ValueError(self._error or "lm_head 가중치를 읽을 수 없습니다.")
        return self._weights

    def info(self) -> dict:
        weights = self._load()
        return {key: weights[key] for key in ("vocab", "hidden", "layers", "eps")}

    def vocab_text(self) -> tuple[list, list, list]:
        """(text, piece, lowercase text) per token ID; IDs without a tokenizer entry are None."""
        with self._lock:
            if self._vocab_text is None:
                size = self._weights["vocab"] if self._weights else 0
                pieces = load_tokenizer_pieces(self.tokenizer_path)
                texts, raw, lowered = [None] * size, [None] * size, [""] * size
                for token_id, piece in pieces.items():
                    if 0 <= token_id < size:
                        decoded = decode_token_piece(piece)
                        texts[token_id] = decoded
                        raw[token_id] = piece
                        lowered[token_id] = (decoded["text"] or "").casefold()
                self._vocab_text = (texts, raw, lowered)
            return self._vocab_text

    def project(self, cache_key, vector: np.ndarray, apply_norm: bool = True) -> dict:
        weights = self._load()
        if vector.size != weights["hidden"]:
            raise ValueError(f"원소 {vector.size:,}개는 은닉 차원 {weights['hidden']:,}과 달라 출력 어휘로 투영할 수 없습니다. "
                             "블록 입·출력 같은 잔차 위치를 선택하세요.")
        key = (cache_key, apply_norm)
        with self._lock:
            if key in self._cache:
                self._cache.move_to_end(key)
                return self._cache[key]
        hidden = np.nan_to_num(vector.astype(np.float32), nan=0.0, posinf=0.0, neginf=0.0)
        if apply_norm:
            hidden = hidden / np.sqrt(np.mean(hidden * hidden) + weights["eps"]) * weights["norm"]
        head, chunk = weights["head"], 32768
        logits = np.empty(weights["vocab"], dtype=np.float32)
        for start in range(0, weights["vocab"], chunk):
            logits[start:start + chunk] = self._bf16(head[start:start + chunk]) @ hidden
        order = np.argsort(-logits, kind="stable")
        rank = np.empty_like(order)
        rank[order] = np.arange(order.size)
        wide = logits.astype(np.float64)
        log_z = float(wide.max() + np.log(np.exp(wide - wide.max()).sum()))
        probs = np.exp(wide - log_z)
        result = {"logits": logits, "order": order, "rank": rank, "log_z": log_z,
                  "entropy": float(-(probs * (wide - log_z)).sum())}
        with self._lock:
            self._cache[key] = result
            while len(self._cache) > 12:
                self._cache.popitem(last=False)
        return result


class RolloutIndex:
    """Read-only view of scenario_rollout outputs: per step model input, LLM output, result, verdict."""

    def __init__(self, root: Path | None):
        self.root = root.resolve() if root else None

    def _folder(self, identifier: str) -> Path:
        if self.root is None:
            raise ValueError("rollout 폴더가 설정되지 않았습니다.")
        folder = (self.root / identifier).resolve()
        if folder.parent != self.root or not (folder / "rollout.json").is_file():
            raise ValueError("rollout을 찾을 수 없습니다.")
        return folder

    @staticmethod
    def _summary(folder: Path, rollout: dict) -> dict:
        report = rollout.get("report") or {}
        steps = rollout.get("steps", [])
        operator = rollout.get("operator_report") or {}
        return {"id": folder.name, "kind": rollout.get("kind", "workspace"),
                "scenario_key": rollout.get("scenario_key") or f"{rollout.get('scenario_id')}/{rollout.get('condition')}",
                "scenario_id": rollout.get("scenario_id"), "condition": rollout.get("condition"),
                "seed": rollout.get("seed"), "family": rollout.get("family"),
                "termination": rollout.get("termination") or ("running" if "report" not in rollout else "—"),
                "finished": "report" in rollout, "actions": report.get("actions", len(steps)),
                "violations": report.get("violations", sum(1 for s in steps if s.get("policy_label") == 1)),
                "unlabelled": report.get("unlabelled", 0), "first_violation_step": report.get("first_violation_step"),
                "business_completed": operator.get("business_completed"),
                "started_at": datetime.fromtimestamp(rollout["started_at"], timezone.utc).isoformat()
                if isinstance(rollout.get("started_at"), (int, float)) else None,
                "task": rollout.get("task")}

    def entries(self) -> list[dict]:
        if self.root is None or not self.root.is_dir():
            return []
        items = []
        for path in self.root.glob("*/rollout.json"):
            try:
                items.append(self._summary(path.parent, json.loads(path.read_text(encoding="utf-8"))))
            except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError):
                continue
        return sorted(items, key=lambda item: item.get("started_at") or "", reverse=True)

    def detail(self, identifier: str) -> dict:
        folder = self._folder(identifier)
        rollout = json.loads((folder / "rollout.json").read_text(encoding="utf-8"))
        steps = []
        for index, compact in enumerate(rollout.get("steps", [])):
            path = folder / "steps" / f"step_{compact['step_index']:03d}" / "step.json"
            record = json.loads(path.read_text(encoding="utf-8")) if path.is_file() else dict(compact)
            capture = folder / "steps" / f"step_{compact['step_index']:03d}" / "capture" / "metadata.json"
            record["capture_id"] = f"{self.root.name}/{folder.name}/steps/step_{compact['step_index']:03d}" \
                if capture.is_file() else None
            steps.append(record)
        public = {key: rollout.get(key) for key in ("task", "trusted_policy", "public_context", "rules", "sampling",
                                                     "identity", "observe_every", "label_source", "suite",
                                                     "scenario_brief")}
        return {**self._summary(folder, rollout), **public, "report": rollout.get("report"),
                "operator_report": rollout.get("operator_report"), "steps": steps}

    def load_step(self, identifier: str, step_index: int) -> dict:
        """One step's C-01 capture (all captured blocks × observation points) plus its token record."""
        folder = self._folder(identifier)
        step_dir = folder / "steps" / f"step_{int(step_index):03d}"
        capture_dir = step_dir / "capture"
        if not (capture_dir / "metadata.json").is_file():
            raise ValueError("이 step에는 은닉 상태 capture가 없습니다 (형식 실패 step 등).")
        metadata = json.loads((capture_dir / "metadata.json").read_text(encoding="utf-8"))
        record = json.loads((step_dir / "step.json").read_text(encoding="utf-8")) if (step_dir / "step.json").is_file() else {}
        generation = json.loads((step_dir / "agent-generation.json").read_text(encoding="utf-8")) \
            if (step_dir / "agent-generation.json").is_file() else {}
        features = {}
        with np.load(capture_dir / metadata.get("artifact", {}).get("filename", "features.npz"), allow_pickle=False) as data:
            for block in metadata.get("blocks", []):
                if block["key"] in data.files:
                    features[int(block["layer_index"])] = np.asarray(data[block["key"]], dtype=np.float32)
        kinds = {item["token_index"]: item["kind"] for item in record.get("observations", [])}
        points = [row["token_index"] for row in metadata.get("alignment", [])]
        return {"folder": folder, "record": record, "metadata": metadata, "generation": generation,
                "features": dict(sorted(features.items())), "points": points, "kinds": kinds}

    def step_indexes(self, identifier: str) -> list[int]:
        folder = self._folder(identifier)
        rollout = json.loads((folder / "rollout.json").read_text(encoding="utf-8"))
        return [step["step_index"] for step in rollout.get("steps", [])]


    def transcript(self, identifier: str) -> str:
        path = self._folder(identifier) / "transcript.md"
        return path.read_text(encoding="utf-8") if path.is_file() else ""


class CaptureIndex:
    """Read-only view of C-01 captures written by write_capture (e.g. scripts/run_m1_sandbox.py).

    Each <run>/capture/ holds metadata.json + features.npz (one observed token per block);
    sibling JSON files from the same run add the task, token IDs and the M1 verdict.
    """

    SIDECARS = ("m1-result.json", "agent-generation.json", "c01-input.json", "m1-context.json", "run-summary.json")

    def __init__(self, root: Path | None, tokenizer_path: Path | None = None, exclude: tuple[Path, ...] = ()):
        self.root = root.resolve() if root else None
        self.tokenizer_path = tokenizer_path
        # Scenario rollouts have their own tab; listing thousands of step captures here would be slow.
        # Excluded captures stay loadable by id (the rollout tab links to them).
        self.exclude = tuple(path.resolve() for path in exclude)

    def _pieces(self) -> dict[int, str]:
        return load_tokenizer_pieces(self.tokenizer_path)

    def decode_ids(self, ids: list[int], pieces: list[str] | None = None) -> list[dict]:
        table = None if pieces else self._pieces()
        result = []
        for index, token_id in enumerate(ids):
            piece = pieces[index] if pieces and index < len(pieces) else (table or {}).get(int(token_id))
            result.append({"index": index, "id": int(token_id), "piece": piece,
                           **(decode_token_piece(piece) if piece is not None else {"text": None, "partial": False})})
        return result

    def _capture_dirs(self) -> list[Path]:
        if self.root is None or not self.root.exists():
            return []
        return sorted({path.parent.parent for path in self.root.rglob("capture/metadata.json")
                       if not any(path.is_relative_to(excluded) for excluded in self.exclude)})

    def resolve(self, capture_id: str) -> Path:
        if self.root is None:
            raise ValueError("Capture 루트가 설정되지 않았습니다.")
        folder = (self.root / capture_id).resolve()
        if not folder.is_relative_to(self.root) or not (folder / "capture" / "metadata.json").is_file():
            raise ValueError("Capture를 찾을 수 없습니다.")
        return folder

    @staticmethod
    def _read_json(path: Path):
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return None

    def load(self, capture_id: str) -> dict:
        folder = self.resolve(capture_id)
        metadata = self._read_json(folder / "capture" / "metadata.json") or {}
        sidecars = {name: self._read_json(folder / name) for name in self.SIDECARS if (folder / name).is_file()}
        generation = sidecars.get("agent-generation.json") or {}
        replay_input = sidecars.get("c01-input.json") or {}
        observed = int(metadata.get("observed_prefix_length") or 0)
        all_ids = generation.get("input_ids") or replay_input.get("input_ids") or []
        prefix = all_ids[:observed] if observed else all_ids
        digest = sha256(json.dumps(prefix, separators=(",", ":")).encode("ascii")).hexdigest() if prefix else None
        return {"id": capture_id, "folder": folder, "metadata": metadata, "sidecars": sidecars,
                "all_ids": all_ids, "prefix_ids": prefix, "pieces": generation.get("token_pieces"),
                "prefix_verified": None if digest is None else digest == metadata.get("prefix_ids_sha256")}

    def features(self, capture: dict) -> dict[int, np.ndarray]:
        archive = capture["folder"] / "capture" / (capture["metadata"].get("artifact", {}).get("filename") or "features.npz")
        if not archive.resolve().is_relative_to(capture["folder"]):
            raise ValueError("Invalid capture archive path.")
        vectors = {}
        with np.load(archive, allow_pickle=False) as data:
            for block in capture["metadata"].get("blocks") or []:
                if block.get("key") in data.files:
                    vectors[int(block["layer_index"])] = np.asarray(data[block["key"]]).reshape(-1)
        return vectors

    def summary(self, capture: dict) -> dict:
        metadata, sidecars = capture["metadata"], capture["sidecars"]
        context = metadata.get("context") or {}
        alignment = (metadata.get("alignment") or [{}])[0]
        m1 = sidecars.get("m1-result.json") or {}
        generation = sidecars.get("agent-generation.json") or {}
        m1_context = sidecars.get("m1-context.json") or {}
        run_summary = sidecars.get("run-summary.json") or {}
        observed_index = alignment.get("token_index")
        observed = None
        if isinstance(observed_index, int) and 0 <= observed_index < len(capture["all_ids"]):
            pieces = capture["pieces"]
            observed = self.decode_ids([capture["all_ids"][observed_index]],
                                       [pieces[observed_index]] if pieces and observed_index < len(pieces) else None)[0]
            observed["index"] = observed_index
        try:
            fallback_time = datetime.fromtimestamp((capture["folder"] / "capture" / "metadata.json").stat().st_mtime,
                                                   timezone.utc).isoformat()
        except OSError:
            fallback_time = None
        return {"id": capture["id"], "run_id": context.get("run_id"), "trajectory_id": context.get("trajectory_id"),
                "scenario_id": context.get("scenario_id"), "phase": context.get("phase"),
                "action": context.get("action"), "capture_mode": metadata.get("capture_mode"),
                "hook_point": metadata.get("hook_point"), "observed_prefix_length": metadata.get("observed_prefix_length"),
                "alignment": alignment, "observed_token": observed,
                "layers": [block.get("layer_index") for block in metadata.get("blocks") or []],
                "task": generation.get("task") or m1_context.get("task"),
                "policy": generation.get("trusted_policy") or m1_context.get("trusted_policy"),
                "started_at": run_summary.get("started_at") or fallback_time,
                "prefix_verified": capture["prefix_verified"],
                "m1": {key: m1.get(key) for key in ("status", "risk_score", "alarm", "reason", "error")} if m1 else None,
                "monitor": (m1.get("configuration") or {}).get("monitor") if m1 else None}

    def entries(self) -> list[dict]:
        items = []
        for folder in self._capture_dirs():
            try:
                items.append(self.summary(self.load(folder.relative_to(self.root).as_posix())))
            except (OSError, ValueError, TypeError, KeyError):
                continue
        return sorted(items, key=lambda item: item.get("started_at") or "", reverse=True)


class DashboardHandler(BaseHTTPRequestHandler):
    store: ArtifactIndex
    plot_bins = 64
    value_limit = 4096

    @staticmethod
    def _sandbox_import_limit() -> int:
        settings_path = PROJECT_ROOT / "SANDBOX" / "settings.json"
        try:
            settings = json.loads(settings_path.read_text(encoding="utf-8"))
            limit = int(settings["archive_limit_bytes"])
            return min(max(limit, 1), 16 * 1024**3)
        except (OSError, ValueError, TypeError, KeyError, json.JSONDecodeError):
            return 512 * 1024**2

    def log_message(self, _format: str, *_args) -> None:
        # Keep periodic browser polling out of the terminal.
        return

    def _send(self, body: bytes, content_type: str, status: int = 200) -> None:
        try:
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        except (BrokenPipeError, ConnectionResetError):
            # A refresh or closed tab can disconnect while a response is computed.
            self.close_connection = True

    def _json(self, value: object, status: int = 200) -> None:
        body = json.dumps(value, ensure_ascii=False, allow_nan=False).encode("utf-8")
        self._send(body, "application/json; charset=utf-8", status)

    @staticmethod
    def _sandbox_web_root() -> Path:
        return PROJECT_ROOT / "SANDBOX" / "fakenet"

    @staticmethod
    def _sandbox_site_name(name: str) -> Path:
        candidate = Path(name)
        if (not name or "\\" in name or "\x00" in name or candidate.is_absolute()
                or any(part in {"", ".", ".."} for part in candidate.parts)):
            raise ValueError("사이트 파일은 sites/ 내부의 상대 경로여야 합니다.")
        target = (PROJECT_ROOT / "SANDBOX" / "fakenet" / "sites" / candidate).resolve()
        if not target.is_relative_to((PROJECT_ROOT / "SANDBOX" / "fakenet" / "sites").resolve()):
            raise ValueError("사이트 파일 경로가 허용 범위를 벗어났습니다.")
        return target

    def _sandbox_web_api(self, path: str, query: dict | None = None) -> None:
        root = self._sandbox_web_root()
        if path == "/api/sandbox/web":
            config_path = root / "routes.json"
            config = json.loads(config_path.read_text(encoding="utf-8"))
            sites = root / "sites"
            files = sorted(p.relative_to(sites).as_posix() for p in sites.rglob("*")
                           if p.is_file() and not p.is_symlink()) if sites.is_dir() else []
            completed = subprocess.run([sys.executable, str(PROJECT_ROOT / "SANDBOX" / "sandbox.py"),
                                        "fakenet-log", "--since", str(max(0, datetime.now().timestamp()-86400))],
                                       capture_output=True, text=True, timeout=60, check=False,
                                       cwd=str(PROJECT_ROOT / "SANDBOX"))
            events, log_status = [], "OK"
            if completed.returncode == 0:
                try:
                    data = json.loads(completed.stdout)
                    events, log_status = data.get("events", []), data.get("status", "OK")
                except (json.JSONDecodeError, AttributeError):
                    log_status = "요청 기록 형식 오류"
            else:
                log_status = completed.stderr.strip()[:300] or "Sandbox가 실행 중이 아닙니다"
            self._json({"config_path": str(config_path), "config": config, "files": files,
                        "events": events[-1000:], "log_status": log_status})
            return
        if path == "/api/sandbox/web/file":
            name = (query or {}).get("name", [""])[0]
            target = self._sandbox_site_name(name)
            content = target.read_text(encoding="utf-8") if target.is_file() else ""
            if len(content.encode("utf-8")) > 2 * 1024 * 1024:
                raise ValueError("편집 가능한 사이트 파일은 2 MiB 이하입니다.")
            self._json({"name": name, "content": content, "size": len(content.encode("utf-8"))})
            return
        if path == "/api/sandbox/web/preview":
            args = query or {}
            host = args.get("host", ["example.test"])[0].lower().split(":", 1)[0]
            request_path = args.get("path", ["/"])[0].split("?", 1)[0] or "/"
            config = json.loads((root / "routes.json").read_text(encoding="utf-8"))
            route_index, route = -1, {"status": 404, "content_type": "text/plain", "body": "Not Found\n"}
            for index, candidate in enumerate(config.get("routes", [])):
                methods = candidate.get("methods", ["*"])
                if (fnmatch.fnmatchcase(host, candidate.get("host", "*"))
                        and fnmatch.fnmatchcase(request_path, candidate.get("path", "*"))
                        and ("GET" in methods or "*" in methods)):
                    route_index, route = index, candidate
                    break
            if route.get("file"):
                target = self._sandbox_site_name(str(route["file"]))
                body = target.read_text(encoding="utf-8", errors="replace") if target.is_file() else ""
            else:
                body = str(route.get("body", "")).replace("{host}", host).replace("{path}", request_path)
            self._json({"route_index": route_index, "status": route.get("status", 200),
                        "content_type": route.get("content_type", "text/html; charset=utf-8"), "body": body})
            return
        raise ValueError("Unknown FakeNet API.")

    def _sandbox_web_save(self, path: str) -> None:
        try:
            length = int(self.headers.get("Content-Length", ""))
        except ValueError:
            self._json({"error": "Content-Length가 필요합니다."}, 400)
            return
        if length < 0 or length > 4 * 1024 * 1024:
            self._json({"error": "요청 본문은 4 MiB 이하여야 합니다."}, 413)
            return
        try:
            data = json.loads(self.rfile.read(length))
            if path.endswith("/routes"):
                if not isinstance(data, dict) or not isinstance(data.get("routes"), list):
                    raise ValueError("최상위 JSON 객체에 routes 배열이 필요합니다.")
                for route in data["routes"]:
                    if not isinstance(route, dict):
                        raise ValueError("각 route는 JSON 객체여야 합니다.")
                    if "file" in route:
                        self._sandbox_site_name(str(route["file"]))
                target, raw = self._sandbox_web_root() / "routes.json", json.dumps(data, ensure_ascii=False, indent=2, allow_nan=False)+"\n"
            else:
                if not isinstance(data, dict) or not isinstance(data.get("content"), str):
                    raise ValueError("content 문자열이 필요합니다.")
                target = self._sandbox_site_name(str(data.get("name", "")))
                raw = data["content"]
            encoded = raw.encode("utf-8")
            if len(encoded) > 2 * 1024 * 1024:
                raise ValueError("저장할 파일은 2 MiB 이하여야 합니다.")
            if target.name == "routes.json":
                json.loads(raw)
            target.parent.mkdir(parents=True, exist_ok=True)
            temporary = target.with_name(target.name + ".tmp")
            temporary.write_bytes(encoded)
            temporary.replace(target)
            self._json({"status": "SAVED", "size": len(encoded)})
        except (OSError, ValueError, TypeError, json.JSONDecodeError) as error:
            self._json({"error": str(error)}, 400)

    def _sandbox_image(self, path: str) -> None:
        if not path:
            self._json({"error": "파일 경로가 필요합니다."}, 400)
            return
        # Stage on disk so failures are reported before sending HTTP headers;
        # both container output and HTTP transfer use bounded memory.
        response_started = False
        try:
            with tempfile.TemporaryFile() as image_file:
                result = subprocess.run(
                    [sys.executable, str(PROJECT_ROOT / "SANDBOX" / "sandbox.py"),
                     "read-file", "--image", "--", path],
                    stdout=image_file, stderr=subprocess.PIPE, timeout=150, check=False,
                    cwd=str(PROJECT_ROOT / "SANDBOX"),
                )
                if result.returncode:
                    raise RuntimeError(result.stderr.decode(errors="replace")[:2000]
                                       or "Image read failed.")
                size = image_file.tell()
                image_file.seek(0)
                mime = image_file.readline(128).decode("ascii").strip()
                if mime not in {"image/png", "image/jpeg", "image/gif", "image/webp",
                                "image/bmp", "image/x-icon", "image/avif"}:
                    raise ValueError("Unsupported image format.")
                response_started = True
                self.send_response(200)
                self.send_header("Content-Type", mime)
                self.send_header("Content-Length", str(size - image_file.tell()))
                self.send_header("Cache-Control", "no-store")
                self.send_header("X-Content-Type-Options", "nosniff")
                self.end_headers()
                while chunk := image_file.read(1024 * 1024):
                    self.wfile.write(chunk)
        except (BrokenPipeError, ConnectionResetError):
            self.close_connection = True
        except (OSError, ValueError, RuntimeError, subprocess.TimeoutExpired) as error:
            if response_started:
                self.close_connection = True
            else:
                self._json({"status": "ERROR", "reason": str(error)}, 502)

    def do_POST(self) -> None:
        request_path = urlparse(self.path).path
        if request_path in ("/api/sandbox/web/routes", "/api/sandbox/web/file"):
            if self.headers.get_content_type() != "application/json":
                self._json({"error": "Content-Type must be application/json."}, 415)
                return
            self._sandbox_web_save(request_path)
            return
        if request_path != "/api/sandbox/import":
            self._json({"error": "Not found"}, 404)
            return
        if self.headers.get_content_type() != "application/octet-stream":
            self._json({"error": "Upload must use application/octet-stream."}, 415)
            return
        try:
            length = int(self.headers.get("Content-Length", ""))
        except ValueError:
            self._json({"error": "Content-Length is required and must be an integer."}, 400)
            return
        limit = self._sandbox_import_limit()
        if length <= 0:
            self._json({"error": "Choose a non-empty file to upload."}, 400)
            return
        if length > limit:
            self._json({"error": f"Upload exceeds the configured {limit}-byte Sandbox archive limit."}, 413)
            return
        filename = unquote(self.headers.get("X-Filename", ""), errors="replace").replace("\\", "/").split("/")[-1]
        if not filename or filename in {".", ".."} or "\x00" in filename:
            self._json({"error": "A valid filename is required."}, 400)
            return

        sandbox_script = PROJECT_ROOT / "SANDBOX" / "sandbox.py"
        try:
            with tempfile.TemporaryDirectory(prefix="argus-sandbox-import-") as temp_dir:
                staged_file = Path(temp_dir) / filename
                remaining = length
                with staged_file.open("wb") as target:
                    while remaining:
                        chunk = self.rfile.read(min(1024 * 1024, remaining))
                        if not chunk:
                            raise ValueError("Upload ended before Content-Length bytes were received.")
                        target.write(chunk)
                        remaining -= len(chunk)
                completed = subprocess.run(
                    [sys.executable, str(sandbox_script), "import", temp_dir],
                    capture_output=True, text=True, timeout=900, check=False,
                    cwd=str(PROJECT_ROOT / "SANDBOX"),
                )
                try:
                    result = json.loads(completed.stdout) if completed.stdout.strip() else {}
                except json.JSONDecodeError:
                    result = {}
                if completed.returncode != 0 or result.get("status") != "IMPORTED":
                    detail = result.get("reason") or completed.stderr.strip() or completed.stdout.strip()
                    raise RuntimeError(detail or f"sandbox.py import exited with code {completed.returncode}.")
                result.update({"status": "IMPORTED", "filename": filename,
                               "internal_path": f"/workspace/{filename}"})
                self._json(result, 200)
        except (OSError, ValueError, RuntimeError, subprocess.TimeoutExpired) as error:
            self._json({"status": "ERROR", "reason": str(error)}, 502)

    # ---------- scenario rollout hidden states (C-01 captures saved by scenario_rollout.py) ----------
    def _rollout_hidden_api(self, path: str, query: dict) -> None:
        def arg(name, default=""):
            return query.get(name, [default])[0]
        identifier = arg("id")
        if path == "/api/rollouts/trend":
            detail = self.rollouts.detail(identifier)
            steps, columns = [], {}
            for step in detail["steps"]:
                steps.append({key: step.get(key) for key in ("step_index", "kind", "command", "policy_label",
                                                             "decision", "outcome")})
                try:
                    loaded = self.rollouts.load_step(identifier, step["step_index"])
                except (OSError, ValueError):
                    continue
                for kind in ("pre_action", "pre_reasoning"):
                    position = next((p for p, k in loaded["kinds"].items() if k == kind), None)
                    if position in loaded["points"]:
                        row = loaded["points"].index(position)
                        for layer, matrix in loaded["features"].items():
                            columns.setdefault(kind, {}).setdefault(layer, {})[step["step_index"]] = \
                                float(np.linalg.norm(matrix[row].astype(np.float64)))
            layers = sorted({layer for kind in columns.values() for layer in kind})
            indexes = [step["step_index"] for step in steps]
            self._json({"id": identifier, "scenario_key": detail["scenario_key"], "steps": steps, "layers": layers,
                        **{f"{kind}_l2": [[columns.get(kind, {}).get(layer, {}).get(index) for index in indexes]
                                          for layer in layers] for kind in ("pre_action", "pre_reasoning")}})
            return
        loaded = self.rollouts.load_step(identifier, int(arg("step", "0")))
        generation, record = loaded["generation"], loaded["record"]
        ids = generation.get("input_ids") or []
        if path == "/api/rollouts/hidden":
            pieces = generation.get("token_pieces") or []
            prompt_length = generation.get("prompt_length") or 0
            reasoning = generation.get("reasoning_span")
            cutoff = generation.get("cutoff") or loaded["metadata"].get("observed_prefix_length", 0)
            tokens = []
            for index in range(min(cutoff, len(pieces))):
                role = "prompt" if index < prompt_length else (
                    "reasoning" if reasoning and reasoning[0] <= index < reasoning[1] else "generated")
                tokens.append({"index": index, "role": role, **decode_token_piece(pieces[index])})
            stats = {name: [] for name in ("l2", "mean", "std", "max_abs")}
            for matrix in loaded["features"].values():
                values = matrix.astype(np.float64)
                stats["l2"].append(np.linalg.norm(values, axis=1).tolist())
                stats["mean"].append(values.mean(axis=1).tolist())
                stats["std"].append(values.std(axis=1).tolist())
                stats["max_abs"].append(np.abs(values).max(axis=1).tolist())
            points = [{"token_index": p, "kind": loaded["kinds"].get(p, "observation"),
                       "token_id": ids[p] if p < len(ids) else None,
                       **decode_token_piece(pieces[p] if p < len(pieces) else None)} for p in loaded["points"]]
            summary = self.rollouts.detail(identifier)
            self._json({"id": identifier, "scenario_key": summary["scenario_key"], "condition": summary["condition"],
                        "seed": summary["seed"], "scenario_brief": summary.get("scenario_brief"),
                        "step_index": record.get("step_index"), "steps": [s["step_index"] for s in summary["steps"]],
                        "step": {key: record.get(key) for key in ("kind", "command", "policy_label", "decision",
                                                                  "static_findings", "effect_findings", "observation",
                                                                  "oracle_reason", "output")},
                        "layers": list(loaded["features"]), "points": points, "stats": stats, "tokens": tokens,
                        "prompt_length": prompt_length, "reasoning_span": reasoning, "action_start": cutoff,
                        "capture_id": f"{self.rollouts.root.name}/{identifier}/steps/step_{record.get('step_index', 0):03d}"})
            return
        layer, point = int(arg("layer", "-1")), int(arg("point", "-1"))
        if layer not in loaded["features"] or point not in loaded["points"]:
            raise ValueError("레이어 또는 관찰 위치가 capture에 없습니다.")
        vector = loaded["features"][layer][loaded["points"].index(point)]
        if path == "/api/rollouts/vector":
            self._json({"id": identifier, "layer": layer, "point": point,
                        **self._vector_page(vector, int(arg("offset", "0")), int(arg("limit", "256")), arg("sort"))})
            return
        if path == "/api/rollouts/vocab":
            if self.lens is None:
                raise ValueError("출력 어휘 투영이 설정되지 않았습니다 (--model-dir).")
            # h[p] predicts token p+1: mark the token that actually followed and the observed token itself.
            marks = {"generated": ids[point + 1] if point + 1 < len(ids) else None,
                     "source": ids[point] if point < len(ids) else None}
            apply_norm = arg("norm", "1") != "0"
            payload = self._vocab_payload(("rollout", identifier, record.get("step_index"), point, layer), vector,
                                          apply_norm, arg("q").strip(), arg("sort"), int(arg("offset", "0")),
                                          int(arg("limit", "100")), marks)
            self._json({"id": identifier, "layer": layer, "point": point, "module": f"layer {layer} block output",
                        "location": f"token #{point}",
                        "is_model_output": apply_norm and layer == payload["layers"] - 1, **payload})
            return
        raise ValueError("Unknown rollout API.")

    # ---------- teammate C-01 captures ----------
    captures: CaptureIndex | None = None
    rollouts: RolloutIndex | None = None
    lens: LogitLens | None = None

    def _capture_api(self, path: str, query: dict) -> None:
        def arg(name, default=""):
            return query.get(name, [default])[0]
        if self.captures is None:
            raise ValueError("Capture 루트가 설정되지 않았습니다.")
        if path == "/api/captures/list":
            self._json({"root": str(self.captures.root), "captures": self.captures.entries()})
            return
        capture = self.captures.load(arg("id"))
        vectors = self.captures.features(capture)
        if path == "/api/captures/detail":
            summary = self.captures.summary(capture)
            sidecars = capture["sidecars"]
            generation = sidecars.get("agent-generation.json") or {}
            m1_context = sidecars.get("m1-context.json") or {}
            action = summary.get("action") or {}
            spans = {"prompt_length": generation.get("prompt_length"),
                     "reasoning": generation.get("reasoning_span") or m1_context.get("reasoning_token_span"),
                     "action": [action.get("token_start"), action.get("token_end")],
                     "observed": (summary.get("alignment") or {}).get("token_index"),
                     "prefix_length": summary.get("observed_prefix_length")}
            blocks = {int(block["layer_index"]): block for block in capture["metadata"].get("blocks") or []}
            self._json({**summary, "spans": spans, "sidecars": sorted(sidecars),
                        "metadata": {key: value for key, value in capture["metadata"].items() if key != "model_config"},
                        "tokens": self.captures.decode_ids(capture["all_ids"], capture["pieces"]),
                        "tokenizer_available": bool(capture["pieces"]) or bool(self.captures._pieces()),
                        "final_text": generation.get("final_text"), "action_text": generation.get("action"),
                        "layers": [{"layer": layer, "shape": blocks.get(layer, {}).get("shape"),
                                    "module_path": blocks.get(layer, {}).get("module_path"),
                                    "source_dtype": blocks.get(layer, {}).get("source_dtype"),
                                    **self._vector_page(vector, 0, 1, "")}
                                   for layer, vector in sorted(vectors.items())],
                        "matches": self._capture_matches(capture["prefix_ids"], vectors)})
            return
        if path == "/api/captures/vector":
            layer = int(arg("layer", "-1"))
            if layer not in vectors:
                raise ValueError("Capture에 해당 레이어가 없습니다.")
            self._json({"id": capture["id"], "layer": layer,
                        **self._vector_page(vectors[layer], int(arg("offset", "0")), int(arg("limit", "256")), arg("sort"))})
            return
        raise ValueError("Unknown capture API.")

    def _capture_matches(self, prefix: list[int], vectors: dict[int, np.ndarray]) -> list[dict]:
        """Find the user's HookInspection sessions that observed the same token prefix.

        A generation session matches when prompt + generated IDs start with the prefix:
        forward L-P then processes position L-1 (the capture's observed token). A replay
        session matches when its prompt starts with the prefix (position L-1 of forward 0).
        """
        length = len(prefix)
        if not length or not vectors:
            return []
        matches = []
        data_root = self.store.data_dir.resolve()
        for session in self.store.sessions_with_context():
            context = session["context"]
            prompt = [int(value) for value in context.get("input_ids") or []]
            token_map = context.get("generation_token_map") or []
            if token_map:
                full = prompt + [int(value) for value in context.get("generated_token_ids") or []]
                forward = length - len(prompt)
                if length < len(prompt) or full[:length] != prefix or not 0 <= forward < len(token_map):
                    continue
                mode = "generation"
            else:
                if length > len(prompt) or prompt[:length] != prefix:
                    continue
                forward, mode = 0, "replay"
            session_dir = (self.store.data_dir / session["artifact_dir"]).resolve()
            if not session_dir.is_relative_to(data_root):
                continue
            layers = []
            for _key, record in self.store.token_location_records(session["id"], "output", ""):
                layer = record.get("layer_index")
                if record.get("forward_call_index") != forward or layer not in vectors:
                    continue
                theirs = self._load_token_vector(session_dir, record, len(prompt), position=length - 1)
                ours = vectors[layer]
                if theirs is None or theirs.size != ours.size:
                    continue
                a, b = theirs.astype(np.float64), ours.astype(np.float64)
                denom = float(np.linalg.norm(a) * np.linalg.norm(b))
                layers.append({"layer": layer, "cosine": float(a @ b / denom) if denom else None,
                               "rel_l2": float(np.linalg.norm(a - b) / np.linalg.norm(b)) if np.linalg.norm(b) else None,
                               "max_abs_diff": float(np.abs(a - b).max()) if a.size else 0.0,
                               "hook_l2": float(np.linalg.norm(a)), "capture_l2": float(np.linalg.norm(b))})
            if not layers:
                continue
            item = token_map[forward] if mode == "generation" else {}
            matches.append({"session_id": session["id"], "artifact_dir": session["artifact_dir"],
                            "run_id": session["run_id"], "status": session["status"], "mode": mode,
                            "forward_call_index": forward, "position": length - 1, "prompt_length": len(prompt),
                            "generated_token_index": item.get("generated_token_index") if item else None,
                            "generated_text": decode_token_piece(item.get("generated_token_piece"))["text"] if item else None,
                            "layers": sorted(layers, key=lambda entry: entry["layer"])})
        return matches

    # ---------- token view ----------
    _trajectory_cache: OrderedDict = OrderedDict()
    _trajectory_lock = threading.Lock()
    _LOCATION_LABELS = {
        "|output": "블록 출력 (MLP 잔차 합산 후)",
        "|input.args[0]": "블록 입력 (Attention 전 잔차)",
        ".post_attention_layernorm|input.args[0]": "Attention 후 잔차 (MLP 입력 잔차)",
        ".self_attn|output[0]": "Attention 분기 출력",
        ".mlp|output[0]": "MLP 분기 출력 (잔차 합산 전)",
        ".mlp|output[1]": "MLP router 반환값 output[1]",
    }

    @staticmethod
    def _relative_module(module: str) -> str:
        match = re.match(r"^.*?\.layers\.\d+", module)
        return module[match.end():] if match else module

    @staticmethod
    def _token_slice(array: np.ndarray, forward_index: int, prompt_length: int,
                     position: int | None = None) -> np.ndarray | None:
        """Values that belong to the generated token predicted by one forward call.

        With KV cache, forward N>0 processes exactly one new input position, so the whole
        tensor belongs to that token. Forward 0 (prefill) holds the full prompt; the first
        generated token is predicted from the last prompt position, i.e. index prompt_length-1
        on the first axis whose size equals the prompt length (query axis for attention).
        """
        if forward_index > 0:
            return np.asarray(array).reshape(-1)
        if prompt_length <= 0:
            return None
        for axis, size in enumerate(array.shape):
            if size == prompt_length:
                index = prompt_length - 1 if position is None else position
                return np.asarray(np.take(array, index, axis=axis)).reshape(-1)
        return None

    @staticmethod
    def _token_shape(shape, forward_index, prompt_length: int):
        """Shape of the per-token slice returned by _token_slice (flat indices refer to it)."""
        if not isinstance(shape, list) or not isinstance(forward_index, int):
            return None
        if forward_index > 0:
            return shape
        for axis, size in enumerate(shape):
            if size == prompt_length:
                return shape[:axis] + shape[axis + 1:]
        return None

    @staticmethod
    def _vector_stats(vector: np.ndarray) -> dict:
        values = vector.astype(np.float64, copy=False)
        finite = values[np.isfinite(values)]
        stats = {"numel": int(values.size), "nonfinite": int(values.size - finite.size)}
        if finite.size:
            stats.update(l2=float(np.linalg.norm(finite)), mean=float(finite.mean()), std=float(finite.std()),
                         min=float(finite.min()), max=float(finite.max()), max_abs=float(np.abs(finite).max()))
        return stats

    def _vector_page(self, vector: np.ndarray, offset: int, limit: int, sort: str) -> dict:
        """One page of a 1-D vector plus stats, a min/max envelope and the largest |values|."""
        numeric = vector.astype(np.float64, copy=False)
        offset = max(0, offset)
        limit = min(self.value_limit, max(1, limit))
        safe = np.nan_to_num(numeric, nan=0.0, posinf=0.0, neginf=0.0)
        if sort == "value_desc":
            order = np.argsort(-safe, kind="stable")
        elif sort == "value_asc":
            order = np.argsort(safe, kind="stable")
        elif sort == "abs_desc":
            order = np.argsort(-np.abs(safe), kind="stable")
        else:
            order = np.arange(numeric.size)
        page = order[offset:offset + limit]
        buckets = max(1, math.ceil(numeric.size / 480))
        padded = np.pad(safe, (0, (-numeric.size) % buckets), mode="edge") if numeric.size else safe
        grouped = padded.reshape(-1, buckets) if numeric.size else np.zeros((0, 1))
        top = np.argsort(-np.abs(safe), kind="stable")[:8]
        return {"numel": int(numeric.size), "offset": offset, "sort": sort, "stats": self._vector_stats(vector),
                "values": [{"index": int(i), "value": self._json_value(vector[i])} for i in page],
                "top": [{"index": int(i), "value": float(safe[i])} for i in top],
                "envelope": {"bucket": buckets, "min": grouped.min(axis=1).tolist(),
                             "max": grouped.max(axis=1).tolist()}}

    def _load_token_vector(self, session_dir: Path, record: dict, prompt_length: int,
                           position: int | None = None) -> np.ndarray | None:
        filename = record.get("filename")
        forward_index = record.get("forward_call_index")
        if record.get("kind") != "tensor" or not filename or not isinstance(forward_index, int):
            return None
        path = (session_dir / filename).resolve()
        if not path.is_relative_to(session_dir):
            return None
        try:
            array = np.load(path, mmap_mode="r", allow_pickle=False)
        except (OSError, ValueError):
            return None
        if np.iscomplexobj(array):
            array = np.abs(array)
        return self._token_slice(array, forward_index, prompt_length, position)

    def _token_api(self, path: str, query: dict) -> None:
        def arg(name, default=""):
            return query.get(name, [default])[0]
        if path == "/api/tokens/sessions":
            offset = max(0, int(arg("offset", "0")))
            limit = min(100, max(1, int(arg("limit", "50"))))
            self._json(self.store.token_sessions(arg("q"), offset, limit))
            return
        session_id = int(arg("session", "0"))
        session_dir, meta, context = self.store.token_session(session_id)
        token_map = context.get("generation_token_map") or []
        prompt_length = len(context.get("input_ids") or [])
        if path == "/api/tokens/session":
            probe_forward = 1 if len(token_map) > 1 else 0
            locations, seen = [], set()
            for _key, record in self.store.token_forward_records(session_id, probe_forward):
                if record.get("layer_index") != TOKEN_VIEW_LAYERS[0] or record.get("kind") != "tensor":
                    continue
                rel = self._relative_module(record.get("module", ""))
                loc = f"{rel}|{record.get('location')}"
                if loc in seen:
                    continue
                seen.add(loc)
                locations.append({"key": loc, "module": rel or "(block)", "location": record.get("location"),
                                  "label": self._LOCATION_LABELS.get(loc, f"{rel or '(block)'} · {record.get('location')}"),
                                  "shape": record.get("shape"), "featured": loc in self._LOCATION_LABELS})
            self._json({"session": meta, "task_text": context.get("task_text"),
                        "generated_text": context.get("generated_text") or "",
                        "prompt_token_count": prompt_length, "layers": list(TOKEN_VIEW_LAYERS),
                        "tokens": [{"index": item.get("generated_token_index", i), "id": item.get("generated_token_id"),
                                    "piece": item.get("generated_token_piece"),
                                    **decode_token_piece(item.get("generated_token_piece")),
                                    "source_id": item.get("source_token_id"),
                                    "source_piece": item.get("source_token_piece"),
                                    "source_text": decode_token_piece(item.get("source_token_piece"))["text"]}
                                   for i, item in enumerate(token_map)],
                        "locations": locations, "default_location": "|output"})
            return
        if path == "/api/tokens/trajectory":
            self._json(self._token_trajectory(session_id, session_dir, meta, token_map, prompt_length, arg("loc", "|output")))
            return
        if path == "/api/tokens/detail":
            token = int(arg("token", "0"))
            if not 0 <= token < len(token_map):
                raise ValueError("생성 토큰 범위를 벗어났습니다.")
            layers = {layer: [] for layer in TOKEN_VIEW_LAYERS}
            for key, record in self.store.token_forward_records(session_id, token):
                layer = record.get("layer_index")
                if layer not in layers:
                    continue
                entry = {"key": key, "module": self._relative_module(record.get("module", "")) or "(block)",
                         "rel": self._relative_module(record.get("module", "")),
                         "location": record.get("location"), "kind": record.get("kind"),
                         "shape": record.get("shape"), "dtype": record.get("source_dtype") or record.get("python_type"),
                         "meaning": record.get("meaning"),
                         "token_shape": self._token_shape(record.get("shape"), record.get("forward_call_index"), prompt_length)}
                vector = self._load_token_vector(session_dir, record, prompt_length)
                if vector is not None:
                    entry["stats"] = self._vector_stats(vector)
                elif record.get("kind") != "tensor":
                    entry["value"] = record.get("value", record.get("availability"))
                layers[layer].append(entry)
            token_info = {**token_map[token], **decode_token_piece(token_map[token].get("generated_token_piece")),
                          "source_text": decode_token_piece(token_map[token].get("source_token_piece"))["text"]}
            self._json({"token": token_info, "forward_call_index": token,
                        "layers": [{"layer": layer, "records": rows} for layer, rows in layers.items()]})
            return
        if path == "/api/tokens/vector":
            key = arg("key")
            if not key.startswith(meta["artifact_dir"] + "#"):
                raise ValueError("레코드가 선택한 세션에 속하지 않습니다.")
            found = self.store.lookup_record(key)
            if not found:
                raise ValueError("Record not found; data may still be writing.")
            vector = self._load_token_vector(session_dir, found[1], prompt_length)
            if vector is None:
                raise ValueError("이 레코드에서 토큰 위치 값을 분리할 수 없습니다.")
            page = self._vector_page(vector, int(arg("offset", "0")), int(arg("limit", "256")), arg("sort"))
            self._json({"key": key, "module": found[1].get("module"), "location": found[1].get("location"),
                        "layer": found[1].get("layer_index"), "shape": found[1].get("shape"),
                        "token_shape": self._token_shape(found[1].get("shape"), found[1].get("forward_call_index"), prompt_length),
                        "source_dtype": found[1].get("source_dtype"), **page})
            return
        if path == "/api/tokens/vocab":
            key = arg("key")
            if not key.startswith(meta["artifact_dir"] + "#"):
                raise ValueError("레코드가 선택한 세션에 속하지 않습니다.")
            found = self.store.lookup_record(key)
            if not found:
                raise ValueError("Record not found; data may still be writing.")
            if self.lens is None:
                raise ValueError("출력 어휘 투영이 설정되지 않았습니다 (--model-dir).")
            record = found[1]
            vector = self._load_token_vector(session_dir, record, prompt_length)
            if vector is None:
                raise ValueError("이 레코드에서 토큰 위치 값을 분리할 수 없습니다.")
            forward = record.get("forward_call_index")
            mark_ids = {}
            if isinstance(forward, int) and 0 <= forward < len(token_map):
                mark_ids = {"generated": token_map[forward].get("generated_token_id"),
                            "source": token_map[forward].get("source_token_id")}
            apply_norm = arg("norm", "1") != "0"
            payload = self._vocab_payload(key, vector, apply_norm, arg("q").strip(), arg("sort"),
                                          int(arg("offset", "0")), int(arg("limit", "100")), mark_ids)
            rel = self._relative_module(record.get("module", ""))
            self._json({"key": key, "layer": record.get("layer_index"), "module": record.get("module"),
                        "location": record.get("location"),
                        "is_model_output": apply_norm and rel == "" and record.get("location") == "output"
                                           and record.get("layer_index") == payload["layers"] - 1, **payload})
            return
        raise ValueError("Unknown token API.")

    def _vocab_payload(self, cache_key, vector: np.ndarray, apply_norm: bool, search: str, sort: str,
                       offset: int, limit: int, mark_ids: dict) -> dict:
        """Logit-lens table page over the whole output vocabulary for one hidden vector."""
        info = self.lens.info()
        projection = self.lens.project(cache_key, vector, apply_norm)
        texts, pieces, lowered = self.lens.vocab_text()
        logits, rank, log_z = projection["logits"], projection["rank"], projection["log_z"]
        if search:
            if search.isdigit():
                ids = np.asarray([int(search)] if int(search) < info["vocab"] else [], dtype=np.int64)
            else:
                needle = search.casefold()
                ids = np.asarray([i for i, text in enumerate(lowered) if needle in text], dtype=np.int64)
        else:
            ids = None
        if sort == "id":
            ordered = ids if ids is not None else np.arange(info["vocab"])
        elif sort == "logit_asc":
            ordered = ids[np.argsort(-rank[ids], kind="stable")] if ids is not None else projection["order"][::-1]
        else:
            ordered = ids[np.argsort(rank[ids], kind="stable")] if ids is not None else projection["order"]
        offset = max(0, offset)
        limit = min(500, max(1, limit))

        def row(token_id):
            token_id = int(token_id)
            decoded = texts[token_id] or {"text": None, "partial": False}
            return {"id": token_id, "rank": int(rank[token_id]) + 1, "text": decoded["text"],
                    "partial": decoded["partial"], "piece": pieces[token_id],
                    "logit": float(logits[token_id]), "prob": float(math.exp(float(logits[token_id]) - log_z))}

        marks = {role: row(token_id) for role, token_id in mark_ids.items()
                 if isinstance(token_id, int) and 0 <= token_id < info["vocab"]}
        buckets = max(1, math.ceil(info["vocab"] / 600))
        padded = np.pad(logits, (0, (-logits.size) % buckets), mode="edge").reshape(-1, buckets)
        return {"vocab_size": info["vocab"], "hidden_size": info["hidden"], "layers": info["layers"],
                "apply_norm": apply_norm, "total": int(ordered.size), "offset": offset, "sort": sort, "query": search,
                "rows": [row(token_id) for token_id in ordered[offset:offset + limit]],
                "marks": marks, "top": [row(token_id) for token_id in projection["order"][:5]],
                "stats": {"max": float(logits.max()), "min": float(logits.min()), "mean": float(logits.mean()),
                          "std": float(logits.std()), "entropy": projection["entropy"]},
                "envelope": {"bucket": buckets, "max": padded.max(axis=1).tolist(), "min": padded.min(axis=1).tolist()}}

    def _token_trajectory(self, session_id, session_dir, meta, token_map, prompt_length, loc) -> dict:
        rel, _, location = loc.partition("|")
        rows = self.store.token_location_records(session_id, location, rel)
        cache_key = (session_id, loc, len(rows), meta.get("status"))
        with self._trajectory_lock:
            if cache_key in self._trajectory_cache:
                self._trajectory_cache.move_to_end(cache_key)
                return self._trajectory_cache[cache_key]
        token_count = len(token_map)
        vectors = {layer: {} for layer in TOKEN_VIEW_LAYERS}
        for _key, record in rows:
            layer, forward_index = record.get("layer_index"), record.get("forward_call_index")
            if layer not in vectors or not isinstance(forward_index, int) or not 0 <= forward_index < token_count:
                continue
            vector = self._load_token_vector(session_dir, record, prompt_length)
            if vector is not None:
                vectors[layer][forward_index] = np.nan_to_num(vector.astype(np.float32), nan=0.0, posinf=0.0, neginf=0.0)
        layers = []
        for layer in TOKEN_VIEW_LAYERS:
            found = vectors[layer]
            metrics, previous = [], None
            for token in range(token_count):
                vector = found.get(token)
                if vector is None:
                    metrics.append(None)
                    previous = None
                    continue
                v = vector.astype(np.float64)
                norm = float(np.linalg.norm(v))
                cosine = None
                if previous is not None and previous.size == v.size:
                    denom = norm * float(np.linalg.norm(previous))
                    cosine = float(v @ previous / denom) if denom else None
                metrics.append({"l2": norm, "mean": float(v.mean()) if v.size else 0.0,
                                "std": float(v.std()) if v.size else 0.0,
                                "max_abs": float(np.abs(v).max()) if v.size else 0.0, "cos_prev": cosine})
                previous = v
            sizes = {vector.size for vector in found.values()}
            heat = None
            if found and len(sizes) == 1:
                width = sizes.pop()
                step = max(1, math.ceil(width / 96))
                matrix = np.zeros((token_count, len(range(0, width, step))), dtype=np.float32)
                for token, vector in found.items():
                    matrix[token] = vector[::step]
                heat = {"values": np.round(matrix.T, 4).reshape(-1).tolist(), "rows": int(matrix.shape[1]),
                        "cols": token_count, "dim_step": step, "width": int(width),
                        "present": [token in found for token in range(token_count)]}
            layers.append({"layer": layer, "metrics": metrics, "heat": heat, "found": len(found)})
        result = {"loc": loc, "token_count": token_count, "layers": layers}
        with self._trajectory_lock:
            self._trajectory_cache[cache_key] = result
            while len(self._trajectory_cache) > 6:
                self._trajectory_cache.popitem(last=False)
        return result

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path in ("/api/sandbox/web", "/api/sandbox/web/file", "/api/sandbox/web/preview"):
            try:
                self._sandbox_web_api(parsed.path, parse_qs(parsed.query))
            except (OSError, ValueError, TypeError, json.JSONDecodeError, subprocess.TimeoutExpired) as error:
                self._json({"error": str(error)}, 400)
            return
        if parsed.path.startswith("/api/rollouts/"):
            query = parse_qs(parsed.query)
            try:
                if self.rollouts is None:
                    raise ValueError("rollout 폴더가 설정되지 않았습니다.")
                if parsed.path == "/api/rollouts/list":
                    self._json({"root": str(self.rollouts.root), "rollouts": self.rollouts.entries()})
                elif parsed.path == "/api/rollouts/detail":
                    self._json(self.rollouts.detail(query.get("id", [""])[0]))
                elif parsed.path in ("/api/rollouts/hidden", "/api/rollouts/trend", "/api/rollouts/vector",
                                     "/api/rollouts/vocab"):
                    self._rollout_hidden_api(parsed.path, query)
                elif parsed.path == "/api/rollouts/transcript":
                    self._send(self.rollouts.transcript(query.get("id", [""])[0]).encode("utf-8"),
                               "text/markdown; charset=utf-8")
                else:
                    raise ValueError("Unknown rollout API.")
            except (OSError, ValueError, TypeError, KeyError, json.JSONDecodeError) as error:
                self._json({"error": str(error)}, 400)
            return
        if parsed.path.startswith("/api/captures/"):
            try:
                self._capture_api(parsed.path, parse_qs(parsed.query))
            except (OSError, ValueError, TypeError, KeyError, json.JSONDecodeError, sqlite3.Error) as error:
                self._json({"error": str(error)}, 400)
            return
        if parsed.path.startswith("/api/tokens/"):
            try:
                self._token_api(parsed.path, parse_qs(parsed.query))
            except (OSError, ValueError, TypeError, json.JSONDecodeError, sqlite3.Error) as error:
                self._json({"error": str(error)}, 400)
            return
        if parsed.path in ("/api/hooks/sessions", "/api/hooks/map"):
            query = parse_qs(parsed.query)
            try:
                if parsed.path == "/api/hooks/sessions":
                    offset = max(0, int(query.get("offset", ["0"])[0]))
                    limit = min(100, max(1, int(query.get("limit", ["50"])[0])))
                    result = self.store.hook_sessions(query.get("q", [""])[0], offset, limit)
                else:
                    result = self.store.hook_map(int(query.get("session", ["0"])[0]))
                self._json(result)
            except (OSError, ValueError, TypeError) as error:
                self._json({"error": str(error)}, 400)
            return
        if parsed.path == "/api/sandbox/image":
            self._sandbox_image(parse_qs(parsed.query).get("path", [""])[0])
            return
        if parsed.path in ("/api/sandbox/files", "/api/sandbox/file"):
            command = [sys.executable, str(PROJECT_ROOT / "SANDBOX" / "sandbox.py")]
            if parsed.path == "/api/sandbox/file":
                path = parse_qs(parsed.query).get("path", [""])[0]
                if not path:
                    self._json({"error": "파일 경로가 필요합니다."}, 400)
                    return
                command.extend(["read-file", "--", path])
            else:
                command.append("files")
            try:
                completed = subprocess.run(
                    command,
                    capture_output=True, text=True, timeout=60, check=False,
                    cwd=str(PROJECT_ROOT / "SANDBOX"),
                )
                if completed.returncode:
                    raise RuntimeError(completed.stderr.strip() or completed.stdout.strip()
                                       or "Sandbox file listing failed.")
                self._json(json.loads(completed.stdout))
            except (OSError, ValueError, RuntimeError, subprocess.TimeoutExpired) as error:
                self._json({"status": "ERROR", "reason": str(error)}, 502)
            return
        if parsed.path in ("/", "/hooks", "/tokens", "/captures", "/rollouts", "/scenario-hidden"):
            self._send(PAGE.encode("utf-8"), "text/html; charset=utf-8")
            return
        query = parse_qs(parsed.query)
        if parsed.path == "/api/records":
            try:
                offset = max(0, int(query.get("offset", ["0"])[0]))
                limit = min(500, max(1, int(query.get("limit", ["100"])[0])))
            except ValueError:
                self._json({"error": "offset and limit must be integers."}, 400)
                return
            filters = {name: query.get(name, [""])[0]
                       for name in ("layer", "phase", "kind", "date", "run", "risk", "q")}
            self._json(self.store.query_records(filters, offset, limit))
            return
        if parsed.path in ("/api/tensor", "/api/plot", "/api/prompt", "/api/heatmap", "/api/embedding", "/api/compare"):
            if parsed.path == "/api/compare":
                self._compare(query.get("a", [""])[0], query.get("b", [""])[0])
                return
            key = query.get("key", [""])[0]
            found = self.store.lookup_record(key)
            if not found:
                self._json({"error": "Record not found; data may still be writing."}, 404)
                return
            session_dir, record = found
            if parsed.path == "/api/prompt":
                self._json(self._prompt_data(session_dir))
                return
            filename = record.get("filename")
            if record.get("kind") != "tensor" or not filename:
                self._json({"error": "This record has no tensor file."}, 400)
                return
            tensor_path = (session_dir / filename).resolve()
            if not tensor_path.is_relative_to(session_dir.resolve()):
                self._json({"error": "Invalid artifact path."}, 400)
                return
            try:
                array = np.load(tensor_path, mmap_mode="r", allow_pickle=False)
            except (OSError, ValueError) as error:
                self._json({"error": f"Tensor is not ready/readable: {error}"}, 404)
                return
            if parsed.path == "/api/tensor":
                try:
                    offset = max(0, int(query.get("offset", ["0"])[0]))
                    limit = min(self.value_limit, max(1, int(query.get("limit", ["256"])[0])))
                except ValueError:
                    self._json({"error": "offset and limit must be integers."}, 400)
                    return
                position = max(0, int(query.get("position", ["0"])[0]))
                sort = query.get("sort", [""])[0]
                token_count = len(self._prompt_data(session_dir).get("token_pieces", []))
                view = query.get("view", ["all"])[0]
                if view == "token" and isinstance(record.get("generation_source_position"), int):
                    axis = record.get("generation_sequence_axis")
                    if isinstance(axis, int) and 0 <= axis < array.ndim:
                        length = int(array.shape[axis])
                        selected_position = min(record["generation_source_position"], max(0, length - 1))
                        matrix = np.moveaxis(array, axis, 0).reshape(length, -1)
                    else:
                        matrix, selected_position = self._token_matrix(array, token_count, position)
                else:
                    matrix, selected_position = self._token_matrix(array, token_count, position)
                vector = matrix[selected_position] if view == "token" and matrix is not None else array.reshape(-1)
                flat = vector.reshape(-1)
                stats = record.get("statistics") or {}
                mean, std = stats.get("mean"), stats.get("std")
                try:
                    mean, std = float(mean), float(std)
                except (TypeError, ValueError):
                    mean = std = None
                def item(index, value):
                    value = self._json_value(value)
                    raw = abs(float(value)) if isinstance(value, (int, float)) else None
                    outlier = bool(raw is not None and mean is not None and std is not None and std > 0 and abs(raw - mean) > 3 * std)
                    return {"index": int(index), "value": value, "outlier": outlier}
                sorted_mode = sort in {"value_desc", "value_asc"}
                if sorted_mode:
                    numeric = np.asarray(flat, dtype=np.float64)
                    numeric = np.nan_to_num(numeric, nan=-np.inf if sort == "value_desc" else np.inf,
                                            posinf=np.inf if sort == "value_desc" else -np.inf,
                                            neginf=-np.inf if sort == "value_desc" else np.inf)
                    count = int(flat.size)
                    if count == 0:
                        indices = np.asarray([], dtype=np.int64)
                    elif count <= 2_000_000:
                        indices = np.argsort(numeric)
                        if sort == "value_desc": indices = indices[::-1]
                        indices = indices[offset:offset + limit]
                    else:
                        k = min(count, offset + limit)
                        partition = np.argpartition(numeric, count-k if sort == "value_desc" else k-1)
                        candidates = partition[-k:] if sort == "value_desc" else partition[:k]
                        indices = candidates[np.argsort(numeric[candidates])]
                        if sort == "value_desc": indices = indices[::-1]
                        indices = indices[offset:offset + limit]
                    values = [item(i, flat[i]) for i in indices]
                else:
                    values = [item(i, flat[i]) for i in range(offset, min(offset + limit, flat.size))]
                self._json({"offset": offset, "numel": int(flat.size), "shape": list(array.shape),
                            "storage_dtype": str(array.dtype), "values": values, "sorted": sorted_mode,
                            "position": selected_position if view == "token" and matrix is not None else None,
                            "view": "token" if view == "token" and matrix is not None else "all",
                            "generated_token_piece": record.get("generated_token_piece"),
                            "generated_token_index": record.get("generated_token_index"),
                            "source_token_piece": record.get("source_token_piece")})
            elif parsed.path == "/api/heatmap":
                self._json(self._heatmap_data(array, session_dir, record))
            elif parsed.path == "/api/embedding":
                try:
                    self._json(self._embedding_data(array, session_dir, query.get("method", ["pca"])[0]))
                except (ImportError, ValueError) as error:
                    self._json({"error": str(error)}, 400)
            else:
                self._json(self._plot_data(array, record))
            return
        self._json({"error": "Not found"}, 404)

    @staticmethod
    def _json_value(value):
        value = value.item() if isinstance(value, np.generic) else value
        if isinstance(value, complex):
            return {"real": value.real, "imag": value.imag}
        if isinstance(value, float) and not math.isfinite(value):
            return str(value)
        return value

    @staticmethod
    def _prompt_data(session_dir: Path) -> dict:
        try:
            manifest = json.loads((session_dir / "manifest.json").read_text(encoding="utf-8"))
            context = manifest.get("context") or {}
            token_map = context.get("generation_token_map") or []
            if token_map:
                generated_tokens = [{"index": item.get("generated_token_index", i),
                                     "id": item.get("generated_token_id"),
                                     "piece": item.get("generated_token_piece")}
                                    for i, item in enumerate(token_map)]
            else:
                ids = context.get("generated_token_ids") or []
                pieces = context.get("generated_token_pieces") or []
                generated_tokens = [{"index": i, "id": ids[i] if i < len(ids) else None,
                                     "piece": pieces[i] if i < len(pieces) else None}
                                    for i in range(max(len(ids), len(pieces)))]
            return {"task_text": context.get("task_text"), "prompt_text": context.get("prompt_text"),
                    "token_pieces": context.get("token_pieces") or [],
                    "token_count": len(context.get("token_pieces") or []),
                    "generated_text": context.get("generated_text", ""),
                    "generated_tokens": generated_tokens}
        except (OSError, json.JSONDecodeError):
            return {"error": "Prompt/token metadata is not available in this collection."}

    @staticmethod
    def _token_matrix(array: np.ndarray, token_count: int, position: int):
        if not token_count or array.ndim == 0:
            return None, 0
        candidates = [axis for axis, size in enumerate(array.shape) if size == token_count]
        if not candidates:
            return None, 0
        # Prefer the conventional [batch, sequence, hidden] axis, then the leading axis.
        axis = 1 if array.ndim >= 3 and array.shape[1] == token_count else candidates[0]
        moved = np.moveaxis(array, axis, 0).reshape(token_count, -1)
        pos = min(max(0, position), token_count - 1)
        return moved, pos

    def _heatmap_data(self, array: np.ndarray, session_dir: Path, record: dict | None = None) -> dict:
        prompt = self._prompt_data(session_dir)
        generation_axis = (record or {}).get("generation_sequence_axis")
        if isinstance(generation_axis, int) and 0 <= generation_axis < array.ndim:
            tokens = int(array.shape[generation_axis])
            matrix = np.moveaxis(array, generation_axis, 0).reshape(tokens, -1)
        else:
            tokens = prompt.get("token_count", 0)
            matrix, _ = self._token_matrix(array, tokens, 0)
        if matrix is None:
            return {"error": "Token axis could not be aligned with recorded prompt tokens."}
        max_rows, max_cols = 160, 256
        row_step = max(1, math.ceil(matrix.shape[0] / max_cols))
        col_step = max(1, math.ceil(matrix.shape[1] / max_rows))
        sample = np.asarray(matrix[::row_step, ::col_step].T, dtype=np.float32)
        sample = np.nan_to_num(sample, nan=0.0, posinf=0.0, neginf=0.0)
        return {"values": sample.reshape(-1).tolist(), "rows": int(sample.shape[0]),
                "cols": int(sample.shape[1]), "token_count": tokens,
                "feature_count": int(matrix.shape[1]), "row_step": row_step, "col_step": col_step,
                "generated_token_piece": (record or {}).get("generated_token_piece"),
                "generated_token_index": (record or {}).get("generated_token_index"),
                "source_token_piece": (record or {}).get("source_token_piece")}

    def _embedding_data(self, array: np.ndarray, session_dir: Path, method: str) -> dict:
        prompt = self._prompt_data(session_dir)
        matrix, _ = self._token_matrix(array, prompt.get("token_count", 0), 0)
        if matrix is None:
            raise ValueError("Token axis could not be aligned with recorded prompt tokens.")
        if matrix.shape[0] > 2000:
            indices = np.linspace(0, matrix.shape[0]-1, 2000).astype(int)
            matrix = matrix[indices]
        else:
            indices = np.arange(matrix.shape[0])
        data = np.asarray(matrix, dtype=np.float64)
        data = np.nan_to_num(data, nan=0.0, posinf=0.0, neginf=0.0)
        data -= data.mean(axis=0, keepdims=True)
        method = method.lower()
        if method == "pca":
            u, singular, _ = np.linalg.svd(data, full_matrices=False)
            coords = u[:, :2] * singular[:2]
            if coords.shape[1] < 2: coords = np.pad(coords, ((0, 0), (0, 2-coords.shape[1])))
        elif method == "tsne":
            if len(data) < 3:
                raise ValueError("t-SNE requires at least three token positions; use PCA for this prompt.")
            try:
                from sklearn.manifold import TSNE
            except ImportError as error:
                raise ImportError("t-SNE requires the optional dependency: pip install -e '.[research]'") from error
            try:
                coords = TSNE(n_components=2, init="pca", learning_rate="auto", max_iter=500,
                              perplexity=min(30, max(2, (len(data)-1)//3))).fit_transform(data)
            except TypeError:
                coords = TSNE(n_components=2, init="pca", learning_rate="auto", n_iter=500,
                              perplexity=min(30, max(2, (len(data)-1)//3))).fit_transform(data)
        else:
            raise ValueError("method must be pca or tsne")
        return {"points": [{"x": float(p[0]), "y": float(p[1]), "token_index": int(i)}
                            for p, i in zip(coords, indices)]}

    def _compare(self, key_a: str, key_b: str) -> None:
        found_a, found_b = self.store.lookup_record(key_a), self.store.lookup_record(key_b)
        if not found_a or not found_b:
            self._json({"error": "A or B record was not found."}, 404); return
        def load(found):
            base, record = found
            path = (base / str(record.get("filename", ""))).resolve()
            if record.get("kind") != "tensor" or not path.is_relative_to(base.resolve()):
                raise ValueError("A/B must refer to valid tensor records.")
            return np.load(path, mmap_mode="r", allow_pickle=False)
        try:
            a, b = load(found_a), load(found_b)
            if a.shape != b.shape:
                self._json({"error": f"Tensor shapes differ: A {a.shape}, B {b.shape}."}, 400); return
            af, bf = a.reshape(-1), b.reshape(-1)
            sums = [0.0, 0.0, 0.0, 0.0]; top = []
            chunks = 1_000_000
            # For the common [batch, token, hidden] layout, report per hidden feature.
            token_count = len(self._prompt_data(found_a[0]).get("token_pieces", []))
            ma, _ = self._token_matrix(a, token_count, 0); mb, _ = self._token_matrix(b, token_count, 0)
            feature_n = ma.shape[1] if ma is not None and mb is not None else min(4096, af.size)
            diff_sum = dot = norm_a = norm_b = max_delta = abs_delta_sum = 0.0
            feature_sum = np.zeros(feature_n, dtype=np.float64); feature_count = 0
            if ma is not None and mb is not None:
                for start in range(0, feature_n, chunks):
                    delta = np.asarray(ma[:, start:start+chunks], dtype=np.float64)-np.asarray(mb[:, start:start+chunks], dtype=np.float64)
                    feature_sum[start:start+delta.shape[1]] = np.mean(delta, axis=0)
                feature_count = feature_n
            for start in range(0, af.size, chunks):
                x = np.asarray(af[start:start+chunks], dtype=np.float64).reshape(-1)
                y = np.asarray(bf[start:start+chunks], dtype=np.float64).reshape(-1)
                x = np.nan_to_num(x); y = np.nan_to_num(y); d = x-y
                diff_sum += float(np.dot(d,d)); dot += float(np.dot(x,y)); norm_a += float(np.dot(x,x)); norm_b += float(np.dot(y,y))
                abs_delta_sum += float(np.abs(d).sum())
                max_delta = max(max_delta, float(np.max(np.abs(d))) if d.size else 0.0)
            if not feature_count:
                feature_sum = np.asarray(af[:feature_n], dtype=np.float64)-np.asarray(bf[:feature_n], dtype=np.float64)
            ids = np.argsort(np.abs(feature_sum))[-20:][::-1]
            self._json({"shape": list(a.shape), "l2": math.sqrt(diff_sum),
                        "cosine_similarity": dot/math.sqrt(norm_a*norm_b) if norm_a and norm_b else None,
                        "mean_abs_delta": abs_delta_sum/max(1, af.size), "max_abs_delta": max_delta,
                        "top_dimensions": [{"dimension": int(i), "delta": float(feature_sum[i])} for i in ids],
                        "histogram_a": self._plot_data(a, self._array_statistics(a)).get("histogram", []),
                        "histogram_b": self._plot_data(b, self._array_statistics(b)).get("histogram", [])})
        except (OSError, ValueError) as error:
            self._json({"error": str(error)}, 400)

    @staticmethod
    def _array_statistics(array: np.ndarray) -> dict:
        flat = array.reshape(-1)
        lo, hi = math.inf, -math.inf
        for start in range(0, flat.size, 1_000_000):
            chunk = np.asarray(flat[start:start + 1_000_000])
            if np.iscomplexobj(chunk): chunk = np.abs(chunk)
            finite = np.asarray(chunk, dtype=np.float64)
            finite = finite[np.isfinite(finite)]
            if finite.size:
                lo, hi = min(lo, float(finite.min())), max(hi, float(finite.max()))
        if not math.isfinite(lo): lo = hi = 0.0
        return {"min": lo, "max": hi}

    def _plot_data(self, array: np.ndarray, record: dict) -> dict:
        # Plot complex tensors by magnitude, consistent with the saved statistics.
        minimum = record.get("statistics", {}).get("min")
        maximum = record.get("statistics", {}).get("max")
        try:
            low, high = float(minimum), float(maximum)
        except (TypeError, ValueError):
            low = high = 0.0
        if not math.isfinite(low) or not math.isfinite(high):
            low = high = 0.0
        if low == high:
            pad = abs(low) * 1e-6 or 1.0
            low, high = low - pad, high + pad
        counts = np.zeros(self.plot_bins, dtype=np.int64)
        finite_count = 0
        flat = array.reshape(-1)
        chunk_size = 1_000_000
        for start in range(0, flat.size, chunk_size):
            chunk = np.asarray(flat[start:start + chunk_size])
            if np.iscomplexobj(chunk):
                chunk = np.abs(chunk)
            chunk = chunk.astype(np.float64, copy=False)
            finite = chunk[np.isfinite(chunk)]
            finite_count += int(finite.size)
            if finite.size:
                counts += np.histogram(finite, bins=self.plot_bins, range=(low, high))[0]
        axis0 = []
        if array.ndim:
            view = np.squeeze(array)
            if view.ndim == 0:
                view = view.reshape(1)
            if view.ndim == 1:
                rows = view.size
                stride = max(1, math.ceil(rows / 1200))
                for start in range(0, rows, stride):
                    group = np.asarray(view[start:min(start + stride, rows)])
                    if np.iscomplexobj(group):
                        group = np.abs(group)
                    good = np.asarray(group, dtype=np.float64)
                    good = good[np.isfinite(good)]
                    axis0.append({"index": start, "mean": float(good.mean()) if good.size else 0.0})
            elif view.ndim > 1:
                rows = view.shape[0]
                stride = max(1, math.ceil(rows / 1200))
                for start in range(0, rows, stride):
                    group = np.asarray(view[start:min(start + stride, rows)])
                    if np.iscomplexobj(group):
                        group = np.abs(group)
                    good = np.asarray(group, dtype=np.float64)
                    good = good[np.isfinite(good)]
                    axis0.append({"index": start, "mean": float(good.mean()) if good.size else 0.0})
        return {"numel": int(flat.size), "min": low, "max": high,
                "nonfinite": int(flat.size) - finite_count,
                "histogram": [{"count": int(x)} for x in counts], "axis0": axis0}


def main() -> None:
    parser = argparse.ArgumentParser(description="Live graph/table browser for Argus-V Hook tensors")
    parser.add_argument("--data-dir", type=Path, default=PROJECT_ROOT / "tensor_data",
                        help="Hook 산출물 루트 (기본값: 저장소/tensor_data)")
    parser.add_argument("--db-path", type=Path, default=Path(__file__).resolve().parent / "hook_research.sqlite3",
                        help="SQLite 인덱스 파일 경로")
    parser.add_argument("--detector-dir", type=Path, default=PROJECT_ROOT / "artifacts",
                        help="M1/M2/Probe 결과 JSON 루트 (기본값: 저장소/artifacts)")
    parser.add_argument("--rollouts-dir", type=Path, default=PROJECT_ROOT / "artifacts" / "rollouts",
                        help="scenario_rollout.py 출력 폴더 (시나리오 실행 기록 탭)")
    parser.add_argument("--tokenizer", type=Path, default=PROJECT_ROOT / "gpt-oss-20b" / "tokenizer.json",
                        help="팀원 capture의 token ID를 텍스트로 표시할 tokenizer.json (없으면 ID만 표시)")
    parser.add_argument("--model-dir", type=Path, default=PROJECT_ROOT / "gpt-oss-20b",
                        help="출력 어휘 투영(lm_head, 최종 norm)에 쓸 safetensors 체크포인트 폴더")
    parser.add_argument("--host", default="127.0.0.1", help="기본값은 로컬 PC만 접근")
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    data_dir = args.data_dir.expanduser().resolve()
    data_dir.mkdir(parents=True, exist_ok=True)
    store = ArtifactIndex(data_dir, args.db_path.expanduser().resolve())
    detector_dir = args.detector_dir.expanduser().resolve()
    stop_sync = threading.Event()

    def sync_loop():
        # The index can contain millions of hook records. Start serving the UI first,
        # then ingest existing artifacts in the background so startup stays responsive.
        while not stop_sync.is_set():
            store.sync_once()
            store.sync_detector_results(detector_dir)
            if stop_sync.wait(1.5):
                break

    sync_thread = threading.Thread(target=sync_loop, name="argus-artifact-indexer", daemon=True)
    DashboardHandler.store = store
    DashboardHandler.captures = CaptureIndex(detector_dir, args.tokenizer.expanduser(),
                                             exclude=(args.rollouts_dir.expanduser(),))
    DashboardHandler.rollouts = RolloutIndex(args.rollouts_dir.expanduser())
    DashboardHandler.lens = LogitLens(args.model_dir.expanduser().resolve(), args.tokenizer.expanduser())
    server = ThreadingHTTPServer((args.host, args.port), DashboardHandler)
    print(f"Research dashboard: http://{args.host}:{args.port}/")
    print(f"Watching Hook artifacts under: {data_dir}")
    print(f"SQLite index: {store.db_path}")
    print("Stop with Ctrl+C.")
    sync_thread.start()
    try:
        server.serve_forever(poll_interval=0.5)
    except KeyboardInterrupt:
        print("\nDashboard stopped.")
    finally:
        stop_sync.set()
        server.server_close()
        sync_thread.join(timeout=3)


if __name__ == "__main__":
    main()

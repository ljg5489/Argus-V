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
  <button class="tab" type="button" role="tab" data-view="view-compare" aria-selected="false">A/B 비교 <span id="ab-count" class="status"></span></button>
  <button class="tab" type="button" role="tab" data-view="view-hooks" aria-selected="false">Hook 위치</button>
  <button class="tab" type="button" role="tab" data-view="view-sandbox" aria-selected="false">Sandbox 파일</button>
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
    </div>
   </section>
  </div>
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
function redrawAll(){tvRedraw();if(lastPlot)renderPlot(lastPlot);if(lastHeat)renderHeatmap(lastHeat,lastHeatPos);if(lastEmbed)renderEmbedding(lastEmbed);if(histA)drawHist('chart-a',histA,'A 분포');if(histB)drawHist('chart-b',histB,'B 분포');if(lastCompare)renderDelta(lastCompare)}
function showView(id){document.querySelectorAll('.tab').forEach(t=>t.setAttribute('aria-selected',String(t.dataset.view===id)));document.querySelectorAll('.view').forEach(v=>v.hidden=v.id!==id);hideTip();requestAnimationFrame(redrawAll);if(id==='view-tokens')tvEnsureLoaded();if(id==='view-hooks'&&!hookLoaded)loadHookSessions()}
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
let tvLoaded=false,tvOffset=0,tvSessionReq=0,tvReq=0,tvDetailReq=0,tvValueReq=0,tvSession=null,tvTraj=null,tvToken=null,tvDetail=null,tvRecLayer=null,tvRecLoc=null,tvHeatLayer=null,tvValueKey=null,tvValueOffset=0,tvValueSort='',tvCards={};
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
  if(!same){tvToken=0;tvRecLayer=d.layers[0];tvHeatLayer=d.layers[0];tvRecLoc=null;tvValueKey=null}
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
function tvRenderSpark(layer){const card=tvCards[layer],c=$(`tv-spark-${layer}`);if(!card||!c)return;const x=fitCanvas(c),s=c._s,W=c.width,H=c.height,env=card.v.envelope,n=env.min.length;if(!n)return;
 const lo=Math.min(0,...env.min),hi=Math.max(0,...env.max),span=hi-lo||1,y=v=>H-2*s-(v-lo)/span*(H-4*s),bw=W/n;
 x.strokeStyle=cssVar('--line-strong');x.lineWidth=s;x.beginPath();x.moveTo(0,Math.round(y(0))+.5);x.lineTo(W,Math.round(y(0))+.5);x.stroke();
 x.fillStyle=tvLayerColor(card.li);for(let i=0;i<n;i++){const a=y(env.max[i]),b=y(env.min[i]);x.fillRect(i*bw,a,Math.max(1,bw-(bw>3*s?s:0)),Math.max(s,b-a))}
 c.onmousemove=ev=>{const p=canvasPoint(c,ev),i=Math.min(n-1,Math.max(0,Math.floor(p.x/bw))),b=env.bucket,end=Math.min(card.v.numel-1,(i+1)*b-1);showTip(ev,`<b>Layer ${layer} · index ${i*b}${end>i*b?'–'+end:''}</b>\nmin ${fmt(env.min[i])}\nmax ${fmt(env.max[i])}`)};c.onmouseleave=hideTip}
function tvRenderRecords(){if(!tvDetail)return;document.querySelectorAll('#tv-rec-layers button').forEach(b=>b.setAttribute('aria-pressed',String(+b.dataset.layer===tvRecLayer)));
 const L=tvDetail.layers.find(L=>L.layer===tvRecLayer),rows=L?.records||[];
 $('tv-records').innerHTML=rows.map(r=>{const loc=`${r.rel}|${r.location}`,st=r.stats;return st?`<tr data-key="${esc(r.key)}" data-loc="${esc(loc)}" title="${esc(r.meaning||'')}"><td class="mono">${esc(r.module)}</td><td class="mono">${esc(r.location)}</td><td class="mono">${esc(JSON.stringify(r.shape))}</td><td class="num">${st.numel.toLocaleString()}</td><td class="num">${tvFmt(st.l2)}</td><td class="num">${tvFmt(st.mean)}</td><td class="num">${tvFmt(st.max_abs)}</td></tr>`:`<tr class="muted"><td class="mono">${esc(r.module)}</td><td class="mono">${esc(r.location)}</td><td colspan="5" style="white-space:normal">${esc(typeof r.value==='string'?r.value:JSON.stringify(r.value??r.dtype??'non-tensor'))}</td></tr>`}).join('')||'<tr><td colspan="7"><div class="empty">기록이 없습니다.</div></td></tr>';
 $('tv-rec-meta').textContent=`forward ${tvToken} · Layer ${tvRecLayer} · Hook 레코드 ${rows.length}개 (tensor ${rows.filter(r=>r.stats).length}개) · 행을 클릭하면 아래에 이 토큰의 원소값 표시`;
 const pick=rows.find(r=>r.stats&&`${r.rel}|${r.location}`===tvRecLoc)||tvRecordAt(L,$('tv-loc').value);if(pick){tvRecLoc=`${pick.rel}|${pick.location}`;tvValueOffset=0;tvLoadValues(pick.key)}else{tvValueKey=null;$('tv-values').innerHTML='';$('tv-value-meta').textContent=''}}
async function tvLoadValues(key){if(!key||!tvSession)return;tvValueKey=key;document.querySelectorAll('#tv-records tr[data-key]').forEach(tr=>tr.classList.toggle('selected',tr.dataset.key===key));document.querySelectorAll('#tv-sorts button').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.sort===tvValueSort)));const cur=++tvValueReq;
 try{const d=await tvJson('/api/tokens/vector?'+new URLSearchParams({session:tvSession.session.id,key,offset:String(tvValueOffset),limit:'256',sort:tvValueSort}));if(cur!==tvValueReq)return;const mean=d.stats.mean,std=d.stats.std;
  $('tv-values').innerHTML=d.values.map(v=>{const hot=typeof v.value==='number'&&std>0&&Math.abs(v.value-mean)>3*std;return `<tr><td class="num">${v.index}</td><td class="num ${hot?'outlier':''}">${esc(v.value)}</td></tr>`}).join('');
  $('tv-value-meta').textContent=`Layer ${d.layer} · ${d.module} · ${d.location} · 원본 ${JSON.stringify(d.shape)} → 토큰 slice ${JSON.stringify(d.token_shape)} · ${d.offset}–${d.offset+d.values.length} / ${d.numel.toLocaleString()} · ${tvSortLabel[tvValueSort]} · 빨강 ● = 이 토큰 slice 평균에서 3σ 초과`;
  $('tv-val-prev').disabled=d.offset===0;$('tv-val-next').disabled=d.offset+d.values.length>=d.numel}catch(e){if(cur===tvValueReq)$('tv-value-meta').textContent='원소값 조회 실패: '+e.message}}
function tvRedraw(){if($('view-tokens').hidden)return;tvRenderTrend();tvRenderHeat();for(const L of Object.keys(tvCards))tvRenderSpark(L)}
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
                snapshot = result.get("snapshot") or {}
                configuration = result.get("configuration") or {}
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
        if urlparse(self.path).path != "/api/sandbox/import":
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
    def _token_slice(array: np.ndarray, forward_index: int, prompt_length: int) -> np.ndarray | None:
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
                return np.asarray(np.take(array, prompt_length - 1, axis=axis)).reshape(-1)
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

    def _load_token_vector(self, session_dir: Path, record: dict, prompt_length: int) -> np.ndarray | None:
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
        return self._token_slice(array, forward_index, prompt_length)

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
            numeric = vector.astype(np.float64, copy=False)
            offset = max(0, int(arg("offset", "0")))
            limit = min(self.value_limit, max(1, int(arg("limit", "256"))))
            sort = arg("sort")
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
            self._json({"key": key, "numel": int(numeric.size), "offset": offset, "sort": sort,
                        "module": found[1].get("module"), "location": found[1].get("location"),
                        "layer": found[1].get("layer_index"), "shape": found[1].get("shape"),
                        "token_shape": self._token_shape(found[1].get("shape"), found[1].get("forward_call_index"), prompt_length),
                        "stats": self._vector_stats(vector), "source_dtype": found[1].get("source_dtype"),
                        "values": [{"index": int(i), "value": self._json_value(vector[i])} for i in page],
                        "top": [{"index": int(i), "value": float(safe[i])} for i in top],
                        "envelope": {"bucket": buckets, "min": grouped.min(axis=1).tolist(),
                                     "max": grouped.max(axis=1).tolist()}})
            return
        raise ValueError("Unknown token API.")

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
        if parsed.path in ("/", "/hooks", "/tokens"):
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
    parser.add_argument("--host", default="127.0.0.1", help="기본값은 로컬 PC만 접근")
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    data_dir = args.data_dir.expanduser().resolve()
    data_dir.mkdir(parents=True, exist_ok=True)
    store = ArtifactIndex(data_dir, args.db_path.expanduser().resolve())
    store.sync_once()
    detector_dir = args.detector_dir.expanduser().resolve()
    store.sync_detector_results(detector_dir)
    stop_sync = threading.Event()

    def sync_loop():
        while not stop_sync.wait(1.5):
            store.sync_once()
            store.sync_detector_results(detector_dir)

    sync_thread = threading.Thread(target=sync_loop, name="argus-artifact-indexer", daemon=True)
    sync_thread.start()
    DashboardHandler.store = store
    server = ThreadingHTTPServer((args.host, args.port), DashboardHandler)
    print(f"Research dashboard: http://{args.host}:{args.port}/")
    print(f"Watching Hook artifacts under: {data_dir}")
    print(f"SQLite index: {store.db_path}")
    print("Stop with Ctrl+C.")
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

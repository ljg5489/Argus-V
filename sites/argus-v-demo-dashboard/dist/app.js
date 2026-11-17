const state = { scenarios: [], selected: null, job: null, apiOnline: false, busy: false, inferences: {}, health: null };
const detection = { cases: [], selected: null, revealed: false, loaded: false };
const $ = (selector) => document.querySelector(selector);
const apiInput = $('#api-base');

try { apiInput.value = localStorage.getItem('argus-api-base') || apiInput.value; } catch (_) {}
const apiBase = () => apiInput.value.trim().replace(/\/$/, '');

function toast(message) {
  const el = $('#toast'); el.textContent = message; el.classList.add('show');
  window.setTimeout(() => el.classList.remove('show'), 2800);
}

async function api(path, options = {}) {
  const response = await fetch(`${apiBase()}${path}`, {
    ...options,
    headers: { ...(options.body ? { 'Content-Type': 'application/json' } : {}), ...(options.headers || {}) },
  });
  const value = await response.json().catch(() => ({}));
  if (!response.ok) throw new Error(value.error || `연결 오류 (${response.status})`);
  return value;
}

function setConnection(online, detail = '') {
  state.apiOnline = online;
  $('.connection').classList.toggle('offline', !online);
  $('#health-dot').classList.toggle('online', online);
  $('#health-label').textContent = online ? '로컬 agent 연결됨' : (detail || '로컬 연결 필요');
  updateReplayAvailability();
  $('#agent-button').disabled = !online || state.busy;
}

function updateReplayAvailability() {
  const needsTokens = $('#mode-select').value === 'tokens';
  const tokenReady = Boolean(state.health?.agent_model_dir && state.health?.cuda_available);
  const enabled = state.apiOnline && Boolean(state.selected) && Boolean($('#run-select').value) && !state.busy && (!needsTokens || tokenReady);
  $('#replay-button').disabled = !enabled;
  $('#replay-button').title = needsTokens && !tokenReady
    ? '토큰 재계산에는 로컬 GPT-OSS-20B와 CUDA가 필요합니다.' : '';
  $('#replay-mode-hint').textContent = needsTokens && !tokenReady
    ? '현재 로컬 모델 폴더 또는 CUDA를 찾지 못해 토큰 재계산은 비활성 상태입니다.'
    : '저장 hidden state 재채점은 로컬 GPT-OSS 모델 없이 Argus-V 가중치만 실행합니다.';
}

async function loadCatalog() {
  try {
    const response = await fetch('./scenarios.json', { cache: 'no-store' });
    if (!response.ok) throw new Error('시나리오 파일을 읽지 못했습니다.');
    const data = await response.json();
    state.scenarios = data.scenarios || [];
    renderCatalog();
    $('#stat-scenarios').textContent = state.scenarios.length.toLocaleString('ko-KR');
    $('#stat-runs').textContent = state.scenarios.reduce((n, s) => n + s.runs.length, 0).toLocaleString('ko-KR');
    $('#scenario-count').textContent = state.scenarios.length;
  } catch (error) {
    $('#scenario-list').innerHTML = `<div class="loading-block">${escapeHtml(error.message)}</div>`;
  }
}

async function refreshConnection() {
  try {
    localStorage.setItem('argus-api-base', apiBase());
    const health = await api('/api/health');
    state.health = health;
    setConnection(true);
    renderRuntime(health);
    if (Array.isArray(health.available_models) && health.available_models.length) {
      const selected = $('#model-select').value;
      $('#model-select').innerHTML = health.available_models.map((model) => `<option value="${escapeAttr(model.id)}">${escapeHtml(model.name)}</option>`).join('');
      $('#model-select').value = health.available_models.some((model) => model.id === selected) ? selected : health.available_models[0].id;
      if (state.selected) renderRun(state.selected.runs.find((run) => run.id === $('#run-select').value));
    }
    $('#agent-button').disabled = !canRunAgent(health) || state.busy;
    $('#task-hint').textContent = canRunAgent(health) ? '한 번에 한 작업 · 최대 5 step' : '모델, CUDA 또는 Docker 준비 후 실행 가능';
    if (!state.scenarios.length) {
      const data = await api('/api/scenarios');
      state.scenarios = data.scenarios || [];
      renderCatalog();
    }
  } catch (error) {
    setConnection(false);
    renderRuntime(null, error.message);
    $('#agent-button').disabled = true;
    $('#task-hint').textContent = '로컬 연결을 시작하면 작업을 맡길 수 있습니다.';
  }
}

function canRunAgent(health) {
  return Boolean(health.agent_model_dir && health.cuda_available && health.sandbox_script && health.docker_available && health.python311_command);
}

function renderRuntime(health, error = '') {
  const rows = health ? [
    ['Python', health.python, true],
    ['gpt-oss-20b 로컬 모델', health.agent_model_dir ? '준비됨' : '찾을 수 없음', health.agent_model_dir],
    ['CUDA', health.cuda_available ? '사용 가능' : '사용 불가', health.cuda_available],
    ['Sandbox runner', health.sandbox_script ? (health.docker_available ? 'Docker 사용 가능' : 'Docker 미설치') : '찾을 수 없음', health.sandbox_script && health.docker_available],
    ['Python 3.11 sandbox 호출', health.python311_command ? '준비됨' : '사용 불가', health.python311_command],
    ['Argus-V-p P5', health.p5_bundle ? '번들 사용 가능' : '번들 없음', health.p5_bundle],
    ['로컬 rollout', health.local_rollouts ? '기록 있음' : 'HF에서 필요 시 가져오기', health.local_rollouts],
  ] : [['로컬 API', error || '연결 대기 중', false]];
  $('#runtime-list').innerHTML = rows.map(([label, value, ok]) => `<div class="runtime-item"><span>${escapeHtml(label)}</span><strong class="${ok ? 'ok' : 'off'}">${escapeHtml(value)}</strong></div>`).join('');
}

function renderCatalog() {
  const query = $('#scenario-search').value.trim().toLowerCase();
  const filtered = state.scenarios.filter((scenario) => `${scenario.id} ${scenario.title} ${scenario.category}`.toLowerCase().includes(query));
  $('#scenario-count').textContent = filtered.length;
  $('#scenario-list').innerHTML = filtered.map((scenario) => `
    <button class="scenario-item ${state.selected?.id === scenario.id ? 'selected' : ''}" data-scenario="${escapeAttr(scenario.id)}">
      <span class="scenario-number">${escapeHtml(scenario.id.replace('AV-S', 'S'))}</span>
      <span class="scenario-copy"><strong>${escapeHtml(scenario.title)}</strong><small>${scenario.runs.length}개 실행 · 위반 ${scenario.violations}건</small></span>
      ${scenario.recommended ? '<span class="scenario-star" title="시연 추천">★</span>' : ''}
    </button>`).join('') || '<div class="loading-block">검색 결과가 없습니다.</div>';
  $('#scenario-list').querySelectorAll('[data-scenario]').forEach((button) => button.addEventListener('click', () => selectScenario(button.dataset.scenario)));
}

function selectScenario(id) {
  state.selected = state.scenarios.find((item) => item.id === id) || null;
  renderCatalog();
  if (!state.selected) return;
  const scenario = state.selected;
  const runs = scenario.runs;
  $('#scenario-detail').innerHTML = `<div class="detail-content">
    <div class="detail-topline"><span class="detail-id">${escapeHtml(scenario.id)}</span>${scenario.category ? `<span class="category-pill">${escapeHtml(scenario.category)}</span>` : ''}</div>
    <h3>${escapeHtml(scenario.title)}</h3>
    ${scenario.task ? `<p><span class="detail-label">과제</span>${escapeHtml(scenario.task)}</p>` : ''}
    ${scenario.situation ? `<p><span class="detail-label">상황</span>${escapeHtml(scenario.situation)}</p>` : ''}
    ${scenario.forbidden ? `<p><span class="detail-label">금지</span>${escapeHtml(scenario.forbidden)}</p>` : ''}
    <div class="detail-stats"><span><strong>${runs.length}</strong> 저장된 실행</span><span><strong>${scenario.violations}</strong> 위반 호출</span><span><strong>${scenario.recommended}</strong> 추천 실행</span><span>출처 <strong>train</strong></span></div>
  </div>`;
  $('#run-select').innerHTML = runs.map((run, i) => `<option value="${escapeAttr(run.id)}">${run.recommended ? '★ 추천 · ' : ''}${escapeHtml(run.condition)} · seed ${escapeHtml(String(run.seed))} · 위반 ${run.violation_count}</option>`).join('');
  $('#run-select').disabled = !runs.length;
  renderRun(runs[0]);
    updateReplayAvailability();
}

function renderRun(run) {
  if (!run) return;
  const model = $('#model-select').value;
  const inferred = state.inferences[run.id]?.[model] || null;
  const steps = (run.steps || []).map((step) => {
    const live = inferred?.steps.find((candidate) => candidate.index === step.index && candidate.status === 'scored');
    return { ...step, live, plotted: live ? live.score : (model === 'P5' ? step.p5 : null) };
  });
  const scoreLabel = inferred?.score_label || (model === 'P5' ? 'P5 저장 train-percentile' : '실행 후 모델 점수 표시');
  $('#score-label').textContent = scoreLabel;
  $('#score-caveat').textContent = model.startsWith('EM')
    ? 'sigmoid(head) 출력이며 확률 보정/판정 기준은 적용하지 않았습니다.'
    : '점수는 위반 확률이 아니며 도구별로 직접 비교할 수 없습니다.';
  const plotSteps = steps.filter((step) => step.plotted !== null && Number.isFinite(Number(step.plotted)));
  if (!plotSteps.length) {
    $('#chart-wrap').innerHTML = '<div class="chart-empty">추론을 실행하면 선택한 모델의 step 점수가 여기에 표시됩니다.</div>';
    $('#step-list').innerHTML = steps.map((step) => `<div class="step-row"><span class="step-num">STEP ${String(step.index + 1).padStart(2, '0')}</span><span class="step-tool"><strong>${escapeHtml(step.tool)}</strong><small>실행 후 모델 점수를 표시합니다.</small></span><span class="mini-track"></span><span class="step-score">—</span><span class="verdict ${step.label ? 'violation' : 'normal'}">기록 ${step.label ? '위반' : '정상'}</span></div>`).join('');
    updateReplayAvailability();
    return;
  }
  const width = 720, height = 152, left = 34, right = 14, top = 13, bottom = 30;
  const plotW = width - left - right, plotH = height - top - bottom;
  const x = (i) => steps.length < 2 ? left + plotW / 2 : left + i * plotW / (steps.length - 1);
  const y = (score) => top + (1 - Math.max(0, Math.min(1, score))) * plotH;
  const line = steps.map((step, i) => step.plotted === null ? '' : `${i && steps.slice(0, i).some((prev) => prev.plotted !== null) ? 'L' : 'M'} ${x(i)} ${y(step.plotted)}`).filter(Boolean).join(' ');
  const grid = [0, .5, 1].map((v) => `<g><line x1="${left}" y1="${y(v)}" x2="${width - right}" y2="${y(v)}" stroke="rgba(53,42,36,.14)" stroke-dasharray="3 5"/><text x="0" y="${y(v) + 3}" fill="rgba(53,42,36,.42)" font-size="9">${v.toFixed(1)}</text></g>`).join('');
  const marks = steps.map((step, i) => {
    if (step.plotted === null) return '';
    const title = `${step.tool} · ${scoreLabel}: ${Number(step.plotted).toFixed(4)}${step.live?.raw_score == null ? '' : ` · logit ${Number(step.live.raw_score).toFixed(4)}`}`;
    return step.label === 1
      ? `<path d="M ${x(i)} ${y(step.plotted) - 4} l 4 4 -4 4 -4 -4 Z" fill="#f4eee4" stroke="#bb684e" stroke-width="2"><title>${escapeHtml(title)} · 기록 위반</title></path>`
      : `<circle cx="${x(i)}" cy="${y(step.plotted)}" r="3.3" fill="#bb684e"><title>${escapeHtml(title)} · 기록 정상</title></circle>`;
  }).join('');
  const ticks = steps.filter((_, i) => i === 0 || i === steps.length - 1 || (steps.length <= 10 && i % 2 === 0)).map((step) => {
    const pos = steps.indexOf(step);
    return `<text x="${x(pos)}" y="${height - 5}" text-anchor="middle" fill="rgba(53,42,36,.55)" font-size="9">${step.index + 1}</text>`;
  }).join('');
  $('#chart-wrap').innerHTML = `<svg class="score-chart" viewBox="0 0 ${width} ${height}" role="img" aria-label="${escapeAttr(scoreLabel)} step별 점수 그래프">${grid}<path d="${line}" fill="none" stroke="#bb684e" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>${marks}${ticks}<text x="${left}" y="${height - 5}" dx="-23" fill="rgba(53,42,36,.42)" font-size="8">STEP</text></svg>`;
  $('#step-list').innerHTML = steps.map((step) => {
    const value = step.plotted === null ? null : Number(step.plotted);
    const label = step.live?.decision ? ` · ${step.live.decision}` : '';
    const source = step.live ? `실제 ${model} 추론${label}` : '저장된 학습 점수 · 추론 전';
    return `<div class="step-row"><span class="step-num">STEP ${String(step.index + 1).padStart(2, '0')}</span><span class="step-tool"><strong>${escapeHtml(step.tool)}</strong><small>${escapeHtml(source)}${step.live?.raw_score == null ? '' : ` · logit ${Number(step.live.raw_score).toFixed(3)}`}</small></span><span class="mini-track"><span class="mini-fill" style="display:block;width:${value === null ? 0 : Math.max(3, Math.min(100, value * 100))}%"></span></span><span class="step-score">${value === null ? '—' : value.toFixed(3)}</span><span class="verdict ${step.label ? 'violation' : 'normal'}">기록 ${step.label ? '위반' : '정상'}</span></div>`;
  }).join('') || '<div class="chart-empty">이 실행에는 표시할 step이 없습니다.</div>';
  $('#replay-log').textContent = inferred ? `모델: ${inferred.model_name}\n방식: ${inferred.mode}\n데이터: ${inferred.record_origin}\n\n출력은 저장 hidden state를 이용해 분류기 가중치를 실제로 실행한 결과입니다. 기록 라벨은 학습 기록의 정답 표식이며 모델 예측값이 아닙니다.` : (model === 'P5' ? '표시 중인 P5 값은 저장된 train 점수입니다. 추론 버튼을 누르면 P5 가중치를 실행해 다시 계산합니다.' : '추론 버튼을 누르면 EM32 checkpoint를 실행합니다.');
  updateReplayAvailability();
}

function switchView(name) {
  document.querySelectorAll('.nav-item').forEach((button) => button.classList.toggle('active', button.dataset.view === name));
  document.querySelectorAll('.view').forEach((section) => {
    const active = section.id === `view-${name}`;
    section.classList.toggle('active', active); section.hidden = !active;
  });
  const hero = {
    replay: ['기록된 판단을<br><em>다시 따라가 보세요.</em>', '학습 분할의 실행 기록을 순서대로 재생하고, 각 행동에서 P5 위험 점수가 어떻게 움직였는지 살펴봅니다.', 'TRAIN REPLAY', '저장 기록 · 읽기 전용 재생'],
    detection: ['위반의 순간을<br><em>다시 살펴보세요.</em>', '기록된 업무 시나리오와 Argus-V-emp의 평가 결과를 함께 확인합니다.', 'TEST REPLAY', '저장된 평가 결과 · 새 추론 없음'],
    agent: ['한 번 맡기고,<br><em>진행을 지켜보세요.</em>', '로컬 GPT-OSS agent에게 작업을 맡기고 격리 샌드박스의 실행 로그를 확인합니다.', 'LOCAL AGENT', '로컬 실행 · 샌드박스'],
  }[name];
  $('#hero-title').innerHTML = hero[0]; $('#hero-copy').textContent = hero[1];
  $('.intro-meta').innerHTML = `<span class="status-chip"><span class="dot"></span> ${hero[2]}</span><span>${hero[3]}</span>`;
  if (name === 'detection' && !detection.loaded) loadDetection();
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

async function loadDetection() {
  try {
    const response = await fetch('./emp-cases.json', { cache: 'no-store' });
    if (!response.ok) throw new Error('사례 파일을 읽지 못했습니다.');
    const data = await response.json();
    detection.cases = data.cases || []; detection.loaded = true;
    $('#detection-count').textContent = detection.cases.length;
    renderDetectionList();
  } catch (_) {
    $('#detection-list').innerHTML = '<div class="loading-block">사례를 불러오지 못했습니다. 페이지를 다시 열어주세요.</div>';
  }
}

function renderDetectionList() {
  const query = $('#detection-search').value.trim().toLowerCase();
  const rows = detection.cases.map((item, index) => ({ item, index })).filter(({ item }) =>
    `${item.scenario} ${item.title} ${item.tool} ${item.unit}`.toLowerCase().includes(query));
  $('#detection-list').innerHTML = rows.map(({ item, index }) => `<button class="scenario-item ${detection.selected === index ? 'selected' : ''}" data-case="${index}">
    <span class="scenario-number">${escapeHtml(item.scenario.replace('AV-S', 'S'))}</span><span class="scenario-copy"><strong>${escapeHtml(item.title)}</strong><small>${escapeHtml(item.tool)} · ${item.step + 1}번째 호출</small></span></button>`).join('') || '<div class="loading-block">검색 결과가 없습니다.</div>';
  $('#detection-list').querySelectorAll('[data-case]').forEach((button) => button.addEventListener('click', () => selectDetection(Number(button.dataset.case))));
}

function selectDetection(index) {
  detection.selected = index; detection.revealed = false; renderDetectionList();
  const item = detection.cases[index];
  $('#detection-detail').innerHTML = `<div class="detail-content">
    <div class="detail-topline"><span class="detail-id">${escapeHtml(item.scenario)}</span><span class="category-pill">${escapeHtml(item.condition)}</span><span class="category-pill">${item.period === 'oct' ? '10월' : '11월'} 기록</span></div>
    <h3>${escapeHtml(item.title)}</h3>
    <p><span class="detail-label">과제</span>${escapeHtml(item.task)}</p><p><span class="detail-label">상황</span>${escapeHtml(item.situation)}</p>
    <p><span class="detail-label">조건</span>${escapeHtml(item.condition_description || '상세 조건 미기록')}</p><p><span class="detail-label">금지</span>${escapeHtml(item.forbidden)}</p>
    <div class="detection-sequence"><strong>저장된 도구 호출 순서</strong>${item.steps.length ? `<ol>${item.steps.map((step) => `<li class="${step.index === item.step ? 'focus-step' : ''}"><span>${step.index + 1}</span><code>${escapeHtml(step.tool)}</code>${step.index === item.step ? '<b>평가 대상</b>' : ''}</li>`).join('')}</ol>` : '<p>이 실행의 전체 호출 순서는 제공되지 않았습니다.</p>'}
    <small>도구 이름만 표시합니다. 호출 인자와 전체 대화 내용은 이 자료에 없습니다.</small></div>
    <div class="detection-actions"><button class="button primary" id="show-detection">emp 평가 결과 보기 <span>↗</span></button><span>저장된 결과를 확인합니다.</span></div>
  </div>`;
  $('#detection-result').innerHTML = '<div class="panel-head"><div><span class="kicker">RECORDED EMP RESULT</span><h3>탐지 결과</h3></div></div><div class="chart-empty">결과 보기를 누르면 이 호출의 기록된 평가 결과가 나타납니다.</div>';
  $('#show-detection').addEventListener('click', revealDetection);
}

function revealDetection() {
  const item = detection.cases[detection.selected];
  const caught = item.caught_at_5pct_false_alarms_in_repeats === 1;
  const percent = (value) => `${(value * 100).toFixed(1)}%`;
  const bar = (label, value, threshold = false) => {
    const position = Math.max(0, Math.min(100, value * 100));
    return `<div class="risk-row"><div class="risk-row-heading"><span>${escapeHtml(label)}</span><strong>${percent(value)}</strong></div><div class="risk-track" role="img" aria-label="${escapeAttr(label)} ${percent(value)}보다 높은 점수${threshold ? ', 상위 5% 사후 비교 기준' : ''}"><div class="risk-fill" style="width:${position}%"></div>${threshold ? '<span class="risk-threshold" aria-hidden="true"></span>' : ''}</div></div>`;
  };
  $('#detection-result').innerHTML = `<div class="panel-head"><div><span class="kicker">RECORDED EMP RESULT</span><h3>Argus-V-emp 평가 결과</h3></div><span class="category-pill">저장 결과</span></div>
    <div class="detection-output"><div class="detection-verdict ${caught ? 'caught' : 'missed'}"><span>${caught ? '기준 초과 · 탐지' : '기준 이하 · 미탐'}</span><strong>${escapeHtml(item.tool)}</strong><small>${item.step + 1}번째 호출 · 기록 라벨: 위반</small></div>
    <p>이 호출의 emp 점수는 평가에 사용된 <strong>test 정상 호출의 ${percent(item.above_share_of_all_normal_calls)}보다 높았습니다.</strong></p>
    <section class="risk-chart" aria-label="정상 호출과의 점수 비교 그래프"><div class="risk-chart-title"><div><span class="kicker">RISK SCORE COMPARISON</span><h4>정상 호출 대비 점수 위치</h4></div><span>저장된 평가 결과</span></div>
    <p>막대가 길수록 이 사례보다 점수가 낮았던 정상 호출의 비율이 높습니다.</p>
    ${bar('전체 정상 호출', item.above_share_of_all_normal_calls, true)}
    ${bar('같은 시기 정상 호출', item.above_share_of_same_period_normal_calls)}
    ${bar(`같은 도구 정상 호출 ${item.same_tool_normal_calls}건`, item.above_share_of_same_tool_normal_calls)}
    <div class="risk-axis"><span>0%</span><span>50%</span><span>100%</span></div><div class="risk-chart-legend"><span class="risk-legend-line"></span> 상위 5% 사후 비교 기준 (전체 정상 기준)</div></section>
    <p class="detection-caveat">탐지 여부는 test 정상 호출의 95백분위수를 사후 기준으로 사용한 보고서 결과입니다. 이 비율은 위반 확률이나 emp 원점수가 아닙니다. 전체 위반 26건 중 일부를 선별한 재생이며, 새로운 입력에 대한 추론이 아닙니다.</p>
    <a class="detection-source" href="https://github.com/ljg5489/Argus-V/blob/main/reports/risk-loop/argus-v-emp/full_test.md" target="_blank" rel="noopener noreferrer">평가 보고서 보기 ↗</a></div>`;
}

async function beginReplay() {
  const run = state.selected?.runs.find((item) => item.id === $('#run-select').value);
  if (!state.selected || !run) return;
  const mode = $('#mode-select').value;
  const model = $('#model-select').value;
  if (mode === 'tokens' && !window.confirm('토큰 재계산은 저장된 토큰을 로컬 GPT-OSS-20B에 넣어 hidden state를 다시 만듭니다. CUDA와 모델 파일이 필요합니다. 계속할까요?')) return;
  state.busy = true; $('#replay-button').disabled = true;
  $('#replay-log').textContent = `${model} 추론을 시작하는 중…`;
  try {
    const job = await api('/api/replay/start', { method: 'POST', body: JSON.stringify({ scenario: state.selected.id, unit: run.id, mode, model }) });
    state.job = job; toast(`${model} 추론을 시작했습니다.`);
    const result = await pollJob(job.id, (update) => { $('#replay-log').textContent = update.output || `${model} hidden state 추론 중…`; });
    if (result.score_data) {
      state.inferences[run.id] ||= {};
      state.inferences[run.id][model] = result.score_data;
      renderRun(run);
    }
    if (result.exit_code === 0) toast('선택한 Argus-V 모델 추론을 마쳤습니다.');
    else toast('추론이 오류와 함께 끝났습니다. 로그를 확인하세요.');
  } catch (error) {
    $('#replay-log').textContent = error.message; toast(error.message);
  } finally {
    state.busy = false; updateReplayAvailability();
  }
}

async function pollJob(id, update) {
  for (;;) {
    const result = await api(`/api/jobs/${encodeURIComponent(id)}`);
    update(result);
    if (!result.running) return result;
    await new Promise((resolve) => setTimeout(resolve, 1000));
  }
}

function appendMessage(role, content, extra = '') {
  const el = document.createElement('div');
  el.className = `message ${role} ${extra}`;
  if (role === 'agent') {
    const label = document.createElement('span'); label.className = 'message-label'; label.textContent = 'ARGUS-V AGENT · 실행 로그'; el.append(label);
  }
  const body = document.createElement('span'); body.textContent = content; el.append(body);
  $('#chat-thread').append(el); el.scrollIntoView({ behavior: 'smooth', block: 'nearest' }); return body;
}

async function sendTask(event) {
  event.preventDefault();
  const input = $('#task-input'), task = input.value.trim();
  if (!task || state.busy || !state.apiOnline) return;
  appendMessage('user', task); input.value = '';
  document.querySelector('.suggestions')?.remove();
  state.busy = true; $('#agent-button').disabled = true;
  const output = appendMessage('agent', '에이전트 프로세스를 시작하고 있습니다…', 'progress');
  try {
    const job = await api('/api/agent/start', { method: 'POST', body: JSON.stringify({ task, max_steps: 5 }) });
    state.job = job;
    const result = await pollJob(job.id, (update) => { output.textContent = update.output || '작업을 실행 중입니다…'; });
    output.textContent = result.output || (result.exit_code === 0 ? '작업이 완료되었습니다.' : '에이전트가 로그 없이 종료되었습니다.');
    if (result.exit_code !== 0) toast('에이전트 실행이 오류와 함께 종료됐습니다. 로그를 확인하세요.');
  } catch (error) {
    output.textContent = error.message; toast(error.message);
  } finally {
    state.busy = false;
    $('#agent-button').disabled = !state.apiOnline;
    refreshConnection();
  }
}

function escapeHtml(value) {
  return String(value ?? '').replace(/[&<>"']/g, (char) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[char]));
}
function escapeAttr(value) { return escapeHtml(value); }

document.querySelectorAll('.nav-item').forEach((button) => button.addEventListener('click', () => switchView(button.dataset.view)));
$('#scenario-search').addEventListener('input', renderCatalog);
$('#detection-search').addEventListener('input', renderDetectionList);
$('#run-select').addEventListener('change', () => renderRun(state.selected?.runs.find((run) => run.id === $('#run-select').value)));
$('#model-select').addEventListener('change', () => renderRun(state.selected?.runs.find((run) => run.id === $('#run-select').value)));
$('#mode-select').addEventListener('change', updateReplayAvailability);
$('#replay-button').addEventListener('click', beginReplay);
$('#chat-form').addEventListener('submit', sendTask);
$('#reconnect-button').addEventListener('click', refreshConnection);
apiInput.addEventListener('change', refreshConnection);
$('#task-input').addEventListener('keydown', (event) => { if (event.key === 'Enter' && !event.shiftKey) { event.preventDefault(); $('#chat-form').requestSubmit(); } });
document.querySelectorAll('.suggestion').forEach((button) => button.addEventListener('click', () => { $('#task-input').value = button.dataset.task; $('#task-input').focus(); }));
document.addEventListener('keydown', (event) => { if (event.key === '/' && !['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName)) { event.preventDefault(); $('#scenario-search').focus(); } });

loadCatalog().then(refreshConnection);
window.setInterval(() => { if (state.apiOnline && !state.busy) refreshConnection(); }, 15_000);


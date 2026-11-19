const state = { scenarios: [], selected: null, job: null, apiOnline: false, busy: false, inferences: {}, health: null, emp: null, empError: null, traces: null, traceError: null };
const detection = { cases: [], selected: null, loaded: false, position: 0, timer: null, playing: false };
const live = { session: null, following: false, status: null, statusTimer: null };
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
  updateAgentControls();
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

async function loadEmpSteps() {
  try {
    const response = await fetch('./emp-steps.json', { cache: 'no-store' });
    if (!response.ok) throw new Error('EMP step 점수 파일을 읽지 못했습니다.');
    const data = await response.json();
    if (!Number.isFinite(data.cutoff) || !data.runs) throw new Error('EMP step 점수 형식이 올바르지 않습니다.');
    state.emp = data;
  } catch (error) {
    state.empError = error.message;
  }
  renderEmpSteps(state.selected?.runs.find((run) => run.id === $('#run-select').value));
}

async function loadStepTraces() {
  try {
    const response = await fetch('./step-traces.json', { cache: 'no-store' });
    if (!response.ok) throw new Error('단계별 실행 기록 파일을 읽지 못했습니다.');
    const data = await response.json();
    if (!data.runs) throw new Error('단계별 실행 기록 형식이 올바르지 않습니다.');
    state.traces = data;
  } catch (error) {
    state.traceError = error.message;
  }
  renderEmpSteps(state.selected?.runs.find((run) => run.id === $('#run-select').value));
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
    updateAgentControls();
    $('#task-hint').textContent = agentHint(health);
    renderLive(health.live || null);
    if (health.live?.busy && health.live.session && !live.following && !state.busy) attachLive(health.live);
    if (!state.scenarios.length) {
      const data = await api('/api/scenarios');
      state.scenarios = data.scenarios || [];
      renderCatalog();
    }
  } catch (error) {
    setConnection(false);
    renderRuntime(null, error.message);
    renderLive(null);
    $('#task-hint').textContent = '로컬 연결을 시작하면 작업을 맡길 수 있습니다.';
  }
}

function canRunAgent(health) {
  return Boolean(health && health.live && health.agent_model_dir && health.cuda_available && health.sandbox_script && health.docker_available && health.python311_command && health.emp_bundle && health.live_script);
}

function agentHint(health) {
  if (!health.live) return '로컬 API를 새 버전으로 다시 시작해야 실시간 채팅을 쓸 수 있습니다.';
  if (!canRunAgent(health)) return '모델, CUDA, Docker 또는 Argus-V-emp 파일 준비 후 실행 가능';
  return 'step마다 실행 전에 Argus-V-emp가 판정 · 한 번에 한 작업';
}

function updateAgentControls() {
  const ready = state.apiOnline && canRunAgent(state.health);
  $('#agent-button').disabled = !ready || state.busy;
  $('#max-steps').disabled = state.busy;
  $('#cancel-button').hidden = !live.session;
}

function renderRuntime(health, error = '') {
  const rows = health ? [
    ['Python', health.python, true],
    ['gpt-oss-20b 로컬 모델', health.agent_model_dir ? '준비됨' : '찾을 수 없음', health.agent_model_dir],
    ['CUDA', health.cuda_available ? '사용 가능' : '사용 불가', health.cuda_available],
    ['Sandbox runner', health.sandbox_script ? (health.docker_available ? 'Docker 사용 가능' : 'Docker 미설치') : '찾을 수 없음', health.sandbox_script && health.docker_available],
    ['Python 3.11 sandbox 호출', health.python311_command ? '준비됨' : '사용 불가', health.python311_command],
    ['Argus-V-emp 모델 파일', health.emp_bundle ? '준비됨' : '찾을 수 없음', health.emp_bundle],
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
    <div class="detail-stats"><span><strong>${runs.length}</strong> 저장된 실행</span><span><strong>${scenario.violations}</strong> 위반 호출</span><span><strong>${scenario.recommended}</strong> 추천 실행</span><span>EMP 재분할 <strong>실행별 표시</strong></span></div>
  </div>`;
  $('#run-select').innerHTML = runs.map((run, i) => `<option value="${escapeAttr(run.id)}">${run.recommended ? '★ 추천 · ' : ''}${escapeHtml(run.condition)} · seed ${escapeHtml(String(run.seed))} · 위반 ${run.violation_count}</option>`).join('');
  $('#run-select').disabled = !runs.length;
  renderRun(runs[0]);
    updateReplayAvailability();
}

function renderRun(run) {
  if (!run) return;
  renderEmpSteps(run);
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

function renderEmpSteps(run) {
  if (!run) return;
  const data = state.emp;
  if (!data) {
    $('#emp-step-list').innerHTML = `<div class="emp-empty">${escapeHtml(state.empError || 'EMP 점수를 불러오는 중…')}</div>`;
    return;
  }
  const records = data.runs[run.id] || [];
  const byStep = new Map(records.map((record) => [record.index, record]));
  const catalogSteps = new Map((run.steps || []).map((step) => [step.index, step]));
  const traceSteps = state.traces?.runs[run.id] || [];
  const tracesByStep = new Map(traceSteps.map((step) => [step.index, step]));
  const indexes = [...new Set([...catalogSteps.keys(), ...tracesByStep.keys()])].sort((a, b) => a - b);
  const split = records[0]?.split || '기록 없음';
  const splitName = { train: '새 train', validation: '새 validation', test: '새 test' }[split] || split;
  $('#emp-split').textContent = `resplit-1117 · ${splitName}`;
  const alertCount = records.filter((record) => record.score > data.cutoff).length;
  $('#emp-summary').innerHTML = `<strong>${indexes.length}개 행동 · ${records.length}개 EMP 채점</strong><span>경보 ${alertCount}건</span><span>기록된 위반 ${run.violation_count}건</span><span>판정 기준 ${Number(data.cutoff).toFixed(3)}</span>`;
  $('#emp-step-list').innerHTML = indexes.map((index) => {
    const step = catalogSteps.get(index);
    const trace = tracesByStep.get(index);
    const tool = step?.tool || trace?.tool || '알 수 없는 행동';
    const record = byStep.get(index);
    const scored = Boolean(record && record.tool === tool);
    const margin = scored ? record.score - data.cutoff : null;
    const alarm = margin !== null && margin > 0;
    const width = margin === null ? 0 : Math.max(1, Math.min(50, Math.abs(margin) / 0.3 * 50));
    const left = alarm ? 50 : 50 - width;
    const explanation = margin === null ? 'EMP 점수 없음' : margin === 0 ? '기준과 같음' : `기준보다 ${Math.abs(margin).toFixed(3)} ${alarm ? '높음' : '낮음'}`;
    const decision = margin === null ? '판정 안 함' : alarm ? '경보' : '경보 없음';
    const label = step?.label ?? trace?.policy_label;
    const match = margin !== null && step && (alarm ? 1 : 0) === Number(step.label);
    const labelText = label == null ? '기록 라벨 없음' : step ? `기록 ${Number(label) ? '위반' : '정상'} · ${match ? '일치' : '불일치'}` : `규칙 초안 ${Number(label) ? '위반' : '정상'}`;
    const traceText = trace ? `<div class="emp-trace">
        <div class="emp-trace-cell"><span>모델의 추론 · 끝부분</span><p>${escapeHtml(trace.reasoning || '기록된 추론 문장 없음')}</p></div>
        <div class="emp-trace-cell"><span>행동 · 호출 인자</span><code>${escapeHtml(trace.tool)} ${escapeHtml(trace.arguments)}</code></div>
        <div class="emp-trace-cell"><span>실제 결과 · 기록</span><p>${escapeHtml(trace.result)}</p></div>
      </div>` : `<div class="emp-trace emp-trace-missing">${escapeHtml(state.traceError || (state.traces ? '이 실행의 상세 기록이 없습니다.' : '단계별 실행 기록을 불러오는 중…'))}</div>`;
    return `<div class="emp-row ${margin === null ? 'emp-unjudged' : alarm ? 'emp-alert' : 'emp-clear'}">
      <span class="emp-step">STEP ${String(index + 1).padStart(2, '0')}</span>
      <div class="emp-action"><strong>${escapeHtml(tool)}</strong><small>${scored ? `EMP ${Number(record.score).toFixed(3)} · ${explanation}` : 'EMP 채점 대상 아님'}</small></div>
      <div class="emp-position"><div class="emp-axis-labels"><span>정상 쪽</span><span>위반 쪽</span></div><div class="emp-axis" role="img" aria-label="${escapeAttr(explanation)} · ${decision}">${width ? `<span class="emp-axis-fill" style="left:${left}%;width:${width}%"></span>` : ''}<span class="emp-axis-center"></span></div></div>
      <span class="emp-decision ${margin === null ? 'unjudged' : alarm ? 'alarm' : 'clear'}">${decision}</span>
      <span class="emp-label">${labelText}</span>
      ${traceText}
    </div>`;
  }).join('') || '<div class="emp-empty">표시할 step이 없습니다.</div>';
}

function switchView(name) {
  if (name !== 'detection') pauseDetection();
  document.querySelectorAll('.nav-item').forEach((button) => button.classList.toggle('active', button.dataset.view === name));
  document.querySelectorAll('.view').forEach((section) => {
    const active = section.id === `view-${name}`;
    section.classList.toggle('active', active); section.hidden = !active;
  });
  const hero = {
    replay: ['기록된 판단을<br><em>다시 따라가 보세요.</em>', '저장된 실행을 따라가며 각 행동의 P5 점수와 Argus-V-emp 판정을 살펴봅니다.', 'SCENARIO REPLAY', '저장 기록 · 읽기 전용 재생'],
    detection: ['위반의 순간을<br><em>다시 살펴보세요.</em>', '기록된 업무 시나리오와 Argus-V-emp의 평가 결과를 함께 확인합니다.', 'TEST REPLAY', '저장된 평가 결과 · 새 추론 없음'],
    agent: ['한 번 맡기고,<br><em>진행을 지켜보세요.</em>', '로컬 gpt-oss-20b 에이전트가 샌드박스에서 직접 실행하는 과정을 step마다 보여주고, 실행 전에 Argus-V-emp가 정상 쪽 · 위반 쪽을 판정합니다.', 'LIVE AGENT', '로컬 실행 · 샌드박스 · 실시간 판정'],
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
  pauseDetection(); detection.selected = index; detection.position = 0; renderDetectionList();
  const item = detection.cases[index];
  $('#detection-detail').innerHTML = `<div class="detail-content">
    <div class="detail-topline"><span class="detail-id">${escapeHtml(item.scenario)}</span><span class="category-pill">${escapeHtml(item.condition)}</span><span class="category-pill">${item.period === 'oct' ? '10월' : '11월'} 기록</span></div>
    <h3>${escapeHtml(item.title)}</h3>
    <p><span class="detail-label">과제</span>${escapeHtml(item.task)}</p><p><span class="detail-label">상황</span>${escapeHtml(item.situation)}</p>
    <p><span class="detail-label">조건</span>${escapeHtml(item.condition_description || '상세 조건 미기록')}</p><p><span class="detail-label">금지</span>${escapeHtml(item.forbidden)}</p>
    <div class="detection-actions"><button class="button primary" id="demo-play">▶ 시연 시작</button><button class="button secondary" id="demo-step">한 단계씩</button><button class="button secondary" id="demo-reset">처음으로</button></div>
    <p class="demo-note">저장된 실행 기록을 순서대로 보여줍니다. 재생 속도는 시연용이며, 새 추론을 실행하지 않습니다.</p>
    <div class="demo-stage" aria-live="polite"><div class="demo-stage-heading"><div><span class="kicker">RECORDED RUN</span><h4>에이전트 행동 기록</h4></div><span id="demo-progress">시연 대기</span></div><div class="demo-timeline" id="demo-timeline"></div></div>
  </div>`;
  $('#demo-play').addEventListener('click', toggleDetection);
  $('#demo-step').addEventListener('click', () => { pauseDetection(); advanceDetection(); });
  $('#demo-reset').addEventListener('click', () => selectDetection(index));
  renderDetectionProgress();
}

function demoSteps(item) {
  // The report identifies one evaluated call. Never infer scores for other calls.
  return item.steps.length ? item.steps.filter((step) => step.index <= item.step) : [{ index: item.step, tool: item.tool }];
}

function pauseDetection() {
  if (detection.timer) clearTimeout(detection.timer);
  detection.timer = null; detection.playing = false;
  const button = $('#demo-play'); if (button) button.textContent = '▶ 이어서 재생';
}

function toggleDetection() {
  if (detection.playing) { pauseDetection(); return; }
  const item = detection.cases[detection.selected];
  if (!item || detection.position >= demoSteps(item).length) return;
  detection.playing = true; $('#demo-play').textContent = 'Ⅱ 일시정지';
  advanceDetection();
}

function advanceDetection() {
  const item = detection.cases[detection.selected];
  if (!item) return;
  const steps = demoSteps(item);
  if (detection.position >= steps.length) return;
  detection.position += 1;
  renderDetectionProgress();
  if (detection.position === steps.length) { pauseDetection(); revealDetection(); $('#demo-play').disabled = true; $('#demo-step').disabled = true; }
  else if (detection.playing) detection.timer = setTimeout(advanceDetection, 1100);
}

function renderDetectionProgress() {
  const item = detection.cases[detection.selected];
  const steps = demoSteps(item), visible = steps.slice(0, detection.position);
  $('#demo-progress').textContent = detection.position ? `${detection.position} / ${steps.length} 호출 표시` : '시연 대기';
  $('#demo-timeline').innerHTML = `${!item.steps.length ? '<p class="demo-missing">전체 실행 순서가 없어 평가 대상 호출만 표시합니다.</p>' : ''}${visible.length ? visible.map((step, i) => `<div class="demo-event ${i === visible.length - 1 ? 'current' : ''}"><span class="demo-step-number">${String(step.index + 1).padStart(2, '0')}</span><div><small>기록된 도구 호출</small><strong>${escapeHtml(step.tool)}</strong><span>${step.index === item.step ? '저장된 emp 평가 결과가 있는 호출' : '이 호출의 emp 점수는 제공되지 않음'}</span></div></div>`).join('') : '<div class="demo-placeholder">시연을 시작하면 저장된 행동이 여기에 나타납니다.</div>'}`;
  if (detection.position < steps.length) $('#detection-result').innerHTML = `<div class="panel-head"><div><span class="kicker">ARGUS-V-EMP</span><h3>기록된 탐지 결과</h3></div><span class="category-pill">대기</span></div><div class="chart-empty">평가 대상 호출에 도달하면 저장된 emp 결과를 표시합니다.<br>다른 호출의 점수와 판정은 제공되지 않습니다.</div>`;
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

// ---------------------------------------------------------------- live agent chat (/api/live/*)
const LIVE_STATES = {
  off: ['꺼짐', '작업을 보내면 gpt-oss-20b를 GPU에 올립니다. 처음 한 번은 1~2분 걸립니다.'],
  starting: ['시작하는 중', ''],
  loading: ['올리는 중', '샌드박스, Argus-V-emp, gpt-oss-20b를 차례로 준비합니다.'],
  ready: ['준비됨', '작업을 보내면 바로 시작합니다.'],
  busy: ['실행 중', '작업이 끝나거나 중지하면 다음 작업을 보낼 수 있습니다.'],
  stopping: ['내리는 중', 'GPU 메모리를 비우고 있습니다.'],
  stopped: ['꺼짐', ''],
  failed: ['오류', '작업을 다시 보내면 모델을 새로 올립니다.'],
};
const TERMINATIONS = {
  stop: '에이전트가 stop으로 작업을 마쳤습니다',
  max_steps: 'step 한도에 도달해 멈췄습니다',
  cancelled: '중지했습니다',
  format_failure: '형식 오류가 반복돼 멈췄습니다 · 각 시도는 펼쳐 볼 수 있습니다',
  error: '오류로 멈췄습니다',
  worker_failed: '모델을 올리지 못했습니다',
  worker_exited: '작업 프로세스가 끝나 멈췄습니다',
  worker_unavailable: '작업 프로세스에 연결하지 못했습니다',
};
const num = (value, digits = 3) => (value != null && Number.isFinite(Number(value)) ? Number(value).toFixed(digits) : '—');

function renderLive(status) {
  live.status = status;
  const box = $('#live-model');
  window.clearTimeout(live.statusTimer);
  if (!status) {
    box.innerHTML = '<div class="runtime-item"><span>상태</span><strong class="off">로컬 API 연결 필요</strong></div>';
    $('#live-load').disabled = true; $('#live-unload').disabled = true;
    return;
  }
  const key = status.state;
  const [label, note] = LIVE_STATES[key] || [key, ''];
  const info = status.info || {};
  const rows = [
    ['상태', label, key === 'ready' || key === 'busy'],
    status.message && !['ready', 'busy'].includes(key) ? ['진행', status.message, false] : null,
    info.vram_gb != null ? ['GPU 메모리', `${num(info.vram_gb, 1)} GB`, true] : null,
    info.cut_offs ? ['EMP 판정 기준', `5% ${num(info.cut_offs['5%'])} · 1% ${num(info.cut_offs['1%'])}`, true] : null,
    info.network ? ['샌드박스 네트워크', info.network, info.network === 'fakenet'] : null,
  ].filter(Boolean);
  box.innerHTML = rows.map(([name, value, ok]) => `<div class="runtime-item"><span>${escapeHtml(name)}</span><strong class="${ok ? 'ok' : 'off'}">${escapeHtml(value)}</strong></div>`).join('')
    + (note ? `<p class="live-note">${escapeHtml(note)}</p>` : '');
  const running = ['starting', 'loading', 'ready', 'busy'].includes(key);
  $('#live-load').disabled = !state.apiOnline || running || key === 'stopping' || !canRunAgent(state.health);
  $('#live-unload').disabled = !state.apiOnline || !running;
  if (!live.following && ['starting', 'loading', 'stopping'].includes(key)) {
    live.statusTimer = window.setTimeout(async () => {
      try { renderLive(await api('/api/live/status')); } catch (_) { /* the next health check retries */ }
    }, 2000);
  }
}

function verdictHtml(v) {
  if (v.score == null) {
    return `<div class="live-verdict-row emp-unjudged"><div class="emp-action"><strong>판정하지 못함</strong><small>${escapeHtml(v.error || '점수를 계산하지 못했습니다.')}</small></div><span class="emp-decision unjudged">판정 안 함</span></div>`;
  }
  const margin = v.score - v.cut_5;
  const above = margin > 0;
  const alarm = above && !v.report_kind;  // a stop is scored for reference, never an alarm (as in the evaluation)
  const width = Math.max(1, Math.min(50, Math.abs(margin) / 0.3 * 50));
  const left = above ? 50 : 50 - width;
  const explanation = margin === 0 ? '기준과 같음' : `기준 ${num(v.cut_5)}보다 ${num(Math.abs(margin))} ${above ? '높음' : '낮음'}`;
  const decision = v.report_kind ? (above ? '참고 · 기준 위' : '참고 · 기준 아래') : !alarm ? '경보 없음' : v.alarm_1 ? '강한 경보' : '경보';
  const tone = v.report_kind ? 'emp-report' : alarm ? 'emp-alert' : 'emp-clear';
  const decisionTone = v.report_kind ? 'unjudged' : alarm ? 'alarm' : 'clear';
  const detail = [
    v.parts ? `구성 점수 em ${num(v.parts.em)} · P3 ${num(v.parts.P3)} · P5 ${num(v.parts.P5)}` : '',
    v.alarm_1 && !v.report_kind ? `1% 기준 ${num(v.cut_1)}도 넘음` : '',
    `관찰 위치 ${v.points}곳 (추론 ${Number(v.reasoning_tokens || 0).toLocaleString()} 토큰)`,
  ].filter(Boolean).join(' · ');
  const report = v.report_kind ? '<p class="live-verdict-detail">stop(답하고 끝내는 행동)은 보고 도구처럼 평가 지표에서 빼는 종류라, 점수만 참고로 보여주고 경보로 세지 않습니다.</p>' : '';
  return `<div class="live-verdict-row ${tone}">
    <div class="emp-action"><strong>Argus-V-emp ${num(v.score)}</strong><small>${escapeHtml(explanation)} · 실행 전 판정</small></div>
    <div class="emp-position"><div class="emp-axis-labels"><span>정상 쪽</span><span>위반 쪽</span></div><div class="emp-axis" role="img" aria-label="${escapeAttr(`${explanation} · ${decision}`)}"><span class="emp-axis-fill" style="left:${left}%;width:${width}%"></span><span class="emp-axis-center"></span></div></div>
    <span class="emp-decision ${decisionTone}">${escapeHtml(decision)}</span>
    <p class="live-verdict-detail">${escapeHtml(detail)}</p>${report}
  </div>`;
}

function createLiveRun() {
  const root = document.createElement('div');
  root.className = 'message agent live-run';
  root.innerHTML = `<span class="message-label">ARGUS-V AGENT · 실시간 실행</span>
    <div class="live-head"><span class="live-phase" data-role="phase"><span class="live-spinner" aria-hidden="true"></span><span data-role="phase-text">작업을 보내는 중…</span></span><span class="live-meta" data-role="meta"></span></div>
    <div class="live-steps" data-role="steps"></div>
    <div class="live-answer" data-role="answer" hidden><span data-role="answer-label">에이전트 답</span><p data-role="answer-text"></p></div>
    <div class="live-summary" data-role="summary" hidden></div>
    <details class="live-log"><summary>작업 로그</summary><pre data-role="log" aria-live="off"></pre></details>`;
  $('#chat-thread').append(root);
  const pick = (el, role) => el.querySelector(`[data-role="${role}"]`);
  const steps = new Map();
  let alarms = 0, lastError = '', lastStep = 0;

  const nearBottom = () => window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 160;
  const setPhase = (text, done = false) => { pick(root, 'phase-text').textContent = text; pick(root, 'phase').classList.toggle('done', done); };
  const log = (text) => {
    const pre = pick(root, 'log');
    const lines = (pre.textContent ? pre.textContent.split('\n') : []).concat(String(text));
    pre.textContent = lines.slice(-400).join('\n');
  };
  const stepPhase = (view, tail = '') => { pick(view.el, 'phase').textContent = [...view.times, tail].filter(Boolean).join(' · '); };

  function step(index) {
    if (steps.has(index)) return steps.get(index);
    lastStep = Math.max(lastStep, index);
    const el = document.createElement('article');
    el.className = 'live-step';
    el.innerHTML = `<header class="live-step-head"><span class="emp-step">STEP ${String(index).padStart(2, '0')}</span><strong class="live-kind" data-role="kind">행동을 정하는 중</strong><span class="live-step-phase" data-role="phase">모델이 생각하는 중…</span></header>
      <div class="live-attempts" data-role="attempts"></div>
      <div class="live-notes" data-role="notes"></div>
      <div class="live-cell"><span data-role="reasoning-label">모델 추론 · analysis</span><div class="live-stream" data-role="reasoning" aria-live="off"></div></div>
      <div class="live-cell"><span>행동 · 최종 응답</span><pre class="live-code" data-role="action" aria-live="off"></pre></div>
      <div class="live-verdict" data-role="verdict"><div class="live-verdict-wait">행동이 정해지면 실행하기 전에 Argus-V-emp가 판정합니다.</div></div>
      <div class="live-cell live-observation" data-role="observation-wrap" hidden><span>샌드박스 실행 결과</span><pre class="live-code" data-role="observation" aria-live="off"></pre></div>`;
    pick(root, 'steps').append(el);
    const view = { el, messages: new Map(), attempt: 1, times: [] };
    steps.set(index, view);
    return view;
  }

  function resetAttempt(view, attempt) {
    view.attempt = attempt;
    view.messages.clear();
    pick(view.el, 'reasoning').textContent = '';
    pick(view.el, 'action').textContent = '';
  }

  function delta(event) {
    const view = step(event.step);
    if (event.attempt !== view.attempt) resetAttempt(view, event.attempt);
    const channel = event.channel || '';
    let slot = view.messages.get(event.message);
    if (!slot || slot.channel !== channel) {
      if (slot && slot.target.tagName === 'P') slot.target.remove();
      let target = pick(view.el, 'action');
      if (channel !== 'final') {
        target = document.createElement('p');
        if (channel && channel !== 'analysis') target.dataset.channel = channel;
        pick(view.el, 'reasoning').append(target);
      }
      slot = { channel, target, text: '' };
      view.messages.set(event.message, slot);
    }
    slot.text = event.replace ? event.text : slot.text + event.text;
    slot.target.textContent = slot.text;
    const box = pick(view.el, channel === 'final' ? 'action' : 'reasoning');
    box.scrollTop = box.scrollHeight;
  }

  function finish(event) {
    const ended = TERMINATIONS[event.termination] || '작업이 끝났습니다';
    const summary = pick(root, 'summary');
    summary.hidden = false;
    const stopped = event.termination === 'format_failure' && lastStep ? `<span>STEP ${lastStep}에서 멈춤</span>` : '';
    summary.innerHTML = `<strong>${escapeHtml(ended)}</strong>${event.steps == null ? '' : `<span>완료한 step ${event.steps}개</span>`}${stopped}<span>Argus-V-emp 경보 ${event.alarms ?? alarms}건</span>${lastError ? `<span>${escapeHtml(lastError)}</span>` : ''}`;
    setPhase(ended, true);
  }

  function handle(event) {
    const stick = nearBottom();
    switch (event.type) {
      case 'worker':
        if (event.message) setPhase(event.state === 'ready' ? '모델 준비 완료' : event.message);
        if (event.state === 'ready') log(`[모델] 준비됨 · ${num(event.seconds, 1)}초 · GPU ${num(event.vram_gb, 1)} GB`);
        if (event.state === 'failed' || event.state === 'exited') { lastError = event.message || ''; log(`[모델] ${event.message || event.state}`); }
        break;
      case 'log': log(event.text); break;
      case 'task_queued': setPhase('작업을 받았습니다'); break;
      case 'task_start':
        pick(root, 'meta').textContent = `seed ${event.seed} · 최대 ${event.max_steps} step · 네트워크 ${event.network || '—'} · 판정 기준 ${num(event.cut_offs?.['5%'])}`;
        setPhase('에이전트가 작업을 시작했습니다');
        break;
      case 'step_start': step(event.step); setPhase(`STEP ${event.step} · 모델이 다음 행동을 생각하는 중`); break;
      case 'generation_start': {
        const view = step(event.step);
        if (event.attempt !== view.attempt) resetAttempt(view, event.attempt);
        stepPhase(view, `생성 중 · 입력 ${Number(event.prompt_tokens).toLocaleString()} 토큰${event.attempt > 1 ? ` · 시도 ${event.attempt}` : ''}`);
        break;
      }
      case 'delta': delta(event); break;
      case 'attempt_failed': {
        // Keep the refused attempt (reasoning and reply) instead of wiping it when the next attempt starts.
        const view = step(event.step);
        const box = document.createElement('details');
        box.className = 'live-attempt';
        box.innerHTML = '<summary></summary><div class="live-cell"><span>모델 추론</span><div class="live-stream"></div></div><div class="live-cell"><span>받아들이지 않은 최종 응답</span><pre class="live-code"></pre></div>';
        const last = event.attempt >= event.max_attempts;
        box.querySelector('summary').textContent = `시도 ${event.attempt}/${event.max_attempts} · 형식 오류${last ? '' : '로 다시 생성'} · ${event.reason}`;
        box.querySelector('.live-stream').textContent = pick(view.el, 'reasoning').innerText.trim();
        box.querySelector('.live-code').textContent = event.reply ?? pick(view.el, 'action').textContent;
        pick(view.el, 'attempts').append(box);
        resetAttempt(view, event.attempt + 1);
        if (last) {  // no further attempt: only the kept attempts remain
          pick(view.el, 'reasoning').parentElement.hidden = true;
          pick(view.el, 'action').parentElement.hidden = true;
        } else {
          pick(view.el, 'reasoning-label').textContent = `모델 추론 · analysis · 시도 ${event.attempt + 1}`;
        }
        break;
      }
      case 'action': {
        const view = step(event.step);
        pick(view.el, 'kind').textContent = event.kind !== 'stop' ? 'bash 명령' : event.loose ? '답 · 작업을 끝냄' : 'stop · 답하고 작업을 끝냄';
        pick(view.el, 'action').textContent = event.kind === 'stop' && !event.command ? '(내용 없음)' : event.command;
        if (event.loose) {
          const note = document.createElement('div');
          note.className = 'live-note-line live-note-info';
          note.textContent = event.loose === 'direct_answer'
            ? '모델이 bash · stop 블록 없이 바로 답했습니다. 실행할 명령이 없어 이 답을 그대로 받았습니다.'
            : 'stop 블록 형식이 어긋났지만 실행할 명령이 없어 답으로 받았습니다.';
          pick(view.el, 'notes').append(note);
        }
        view.times.push(`생성 ${num(event.seconds, 1)}초 · ${Number(event.generated_tokens).toLocaleString()} 토큰`);
        stepPhase(view, 'Argus-V-emp 판정 중…');
        setPhase(`STEP ${event.step} · 실행하기 전에 Argus-V-emp가 판정하는 중`);
        break;
      }
      case 'verdict': {
        const view = step(event.step);
        pick(view.el, 'verdict').innerHTML = verdictHtml(event);
        const alarmed = Boolean(event.alarm_5) && !event.report_kind;
        view.el.classList.toggle('emp-alert', alarmed);
        if (alarmed) alarms += 1;
        view.times.push(`판정 ${num(event.seconds, 1)}초`);
        stepPhase(view);
        break;
      }
      case 'execute': {
        const view = step(event.step);
        pick(view.el, 'observation-wrap').hidden = false;
        pick(view.el, 'observation').textContent = '샌드박스에서 실행하는 중…';
        stepPhase(view, '실행 중…');
        setPhase(`STEP ${event.step} · 샌드박스에서 명령을 실행하는 중`);
        break;
      }
      case 'observation': {
        const view = step(event.step);
        pick(view.el, 'observation').textContent = event.text + (event.truncated ? '\n… (화면에는 앞부분만 표시합니다)' : '');
        view.times.push(`실행 ${num(event.seconds, 1)}초${event.exit_code == null ? '' : ` · exit ${event.exit_code}`}`);
        stepPhase(view);
        break;
      }
      case 'final':
        pick(root, 'answer').hidden = false;
        pick(root, 'answer-label').textContent = event.loose === 'direct_answer' ? '에이전트 답 · 블록 없이 바로 답함' : '에이전트 답 · stop';
        pick(root, 'answer-text').textContent = event.text || '(에이전트가 내용 없이 작업을 끝냈습니다)';
        break;
      case 'step_end': {
        const view = step(event.step);
        view.el.classList.add('done');
        if (event.outcome === 'format_failure') {
          pick(view.el, 'kind').textContent = '행동을 만들지 못함';
          pick(view.el, 'verdict').innerHTML = '<div class="live-verdict-wait">받아들일 수 있는 행동이 없어 판정하지 않았습니다.</div>';
        }
        stepPhase(view, event.outcome === 'cancelled' ? '중지됨' : event.outcome === 'format_failure' ? '형식 오류로 멈춤' : '');
        break;
      }
      case 'cancel_requested': setPhase('중지를 요청했습니다 · 지금 생성 중인 토큰이나 실행 중인 명령이 끝나면 멈춥니다'); break;
      case 'error': lastError = event.message || '오류'; log(`[오류] ${lastError}`); break;
      case 'task_end': finish(event); break;
      default: break;
    }
    if (stick) root.scrollIntoView({ block: 'end' });
  }

  function fail(message) {
    setPhase(message, true);
    const summary = pick(root, 'summary');
    summary.hidden = false;
    summary.innerHTML = `<strong>${escapeHtml(message)}</strong>`;
  }

  return { handle, fail };
}

async function followLive(session, view, after = 0) {
  live.following = true;
  let seq = after;
  try {
    for (;;) {
      const data = await api(`/api/live/events?after=${seq}&wait=25`);
      let ended = null;
      for (const event of data.events) {
        seq = Math.max(seq, event.seq);
        if (event.session && event.session !== session) continue;
        view.handle(event);
        if (event.type === 'task_end' && event.session === session) ended = event;
      }
      renderLive(data);
      if (ended) return ended;
      if (!data.events.length && (!data.busy || data.session !== session)) return null;  // ended while unseen
    }
  } finally {
    live.following = false;
  }
}

async function sendTask(event) {
  event.preventDefault();
  const input = $('#task-input'), task = input.value.trim();
  if (!task || state.busy || !state.apiOnline) return;
  if (!canRunAgent(state.health)) { toast(agentHint(state.health || {})); return; }
  appendMessage('user', task); input.value = '';
  document.querySelector('.suggestions')?.remove();
  state.busy = true; updateAgentControls();
  const view = createLiveRun();
  try {
    const maxSteps = Number($('#max-steps').value) || 5;
    const started = await api('/api/live/start', { method: 'POST', body: JSON.stringify({ task, max_steps: maxSteps }) });
    live.session = started.session; updateAgentControls();
    renderLive(started);
    const end = await followLive(started.session, view, started.after || 0);
    if (end && !['stop', 'max_steps'].includes(end.termination)) toast(TERMINATIONS[end.termination] || '작업이 끝났습니다.');
  } catch (error) {
    view.fail(error.message); toast(error.message);
  } finally {
    state.busy = false; live.session = null; updateAgentControls();
    refreshConnection();
  }
}

async function attachLive(status) {
  // The page was reloaded while a task ran: rebuild it from the stored events and keep following.
  if (live.following || state.busy) return;
  state.busy = true; live.session = status.session; updateAgentControls();
  document.querySelector('.suggestions')?.remove();
  if (status.task) appendMessage('user', status.task);
  const view = createLiveRun();
  try {
    await followLive(status.session, view, status.session_after ?? Math.max(0, (status.first_seq || 1) - 1));
  } catch (error) {
    view.fail(error.message);
  } finally {
    state.busy = false; live.session = null; updateAgentControls();
    refreshConnection();
  }
}

async function cancelLive() {
  try { await api('/api/live/cancel', { method: 'POST', body: '{}' }); toast('중지를 요청했습니다.'); } catch (error) { toast(error.message); }
}

async function loadLiveModel() {
  try { renderLive(await api('/api/live/load', { method: 'POST', body: '{}' })); toast('gpt-oss-20b를 GPU에 올리기 시작했습니다.'); } catch (error) { toast(error.message); }
}

async function unloadLiveModel() {
  if (live.status?.busy && !window.confirm('실행 중인 작업이 중지됩니다. 모델을 내릴까요?')) return;
  $('#live-unload').disabled = true;
  try { renderLive(await api('/api/live/unload', { method: 'POST', body: '{}' })); toast('모델을 내렸습니다.'); } catch (error) { toast(error.message); }
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
$('#cancel-button').addEventListener('click', cancelLive);
$('#live-load').addEventListener('click', loadLiveModel);
$('#live-unload').addEventListener('click', unloadLiveModel);
$('#reconnect-button').addEventListener('click', refreshConnection);
apiInput.addEventListener('change', refreshConnection);
$('#task-input').addEventListener('keydown', (event) => { if (event.key === 'Enter' && !event.shiftKey) { event.preventDefault(); $('#chat-form').requestSubmit(); } });
document.querySelectorAll('.suggestion').forEach((button) => button.addEventListener('click', () => { $('#task-input').value = button.dataset.task; $('#task-input').focus(); }));
document.addEventListener('keydown', (event) => { if (event.key === '/' && !['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName)) { event.preventDefault(); $('#scenario-search').focus(); } });

loadCatalog().then(refreshConnection);
loadEmpSteps();
loadStepTraces();
window.setInterval(() => { if (state.apiOnline && !state.busy) refreshConnection(); }, 15_000);


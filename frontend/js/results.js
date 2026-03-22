// frontend/js/results.js

let data = null;
try {
  const raw = sessionStorage.getItem('aitool_result');
  if (raw) data = JSON.parse(raw);
} catch(e) {
  console.error('Parse error:', e);
}

if (!data || !data.prompt) {
  window.location.href = '/';
  throw new Error('no data - redirecting');
}

const TOOL_ICONS = {
  'Gamma AI':'✨','Canva AI':'🎨','Beautiful.ai':'💎',
  'Midjourney':'🖼️','Adobe Firefly':'🔥','DALL-E (ChatGPT)':'🤖',
  'ChatGPT':'💬','Gemini':'♊','GitHub Copilot':'🐙',
  'Runway ML':'🎬','Pictory':'📽️','Perplexity AI':'🔍',
  'Suno AI':'🎵','Udio':'🎶','ElevenLabs':'🎤','Mubert':'🎼'
};

// CAT_ICONS is already defined in nav.js — use it from there
const ICONS = {
  presentation:'📊', image:'🎨', audio:'🎵', video:'🎬',
  coding:'💻', research:'🔬', writing:'✍️', ai_tool_usage:'🤖'
};

// ── Header ─────────────────────────────────────────────────────────────────
const topicTitleEl = document.getElementById('topicTitle');
const catPillEl    = document.getElementById('catPill');
if (topicTitleEl) topicTitleEl.textContent = data.topic || '';
if (catPillEl) catPillEl.textContent =
  (ICONS[data.category] || '🤖') + '  ' +
  (data.category || '').replace(/_/g, ' ').toUpperCase();

// ── General prompt ─────────────────────────────────────────────────────────
const promptEl = document.getElementById('generalPrompt');
if (promptEl) {
  const copyBtn = promptEl.querySelector('.copy-btn');
  promptEl.textContent = data.prompt || '';
  if (copyBtn) promptEl.appendChild(copyBtn);
}

// ── Tips ───────────────────────────────────────────────────────────────────
const tipsEl = document.getElementById('tipsGrid');
if (tipsEl) {
  const tips = (data.tips || '').split('\n').filter(t => t.trim());
  tips.forEach((tip, i) => {
    const clean = tip.replace(/^-\s*/, '').trim();
    if (!clean) return;
    const div = document.createElement('div');
    div.className = 'tip-card card fu';
    div.style.animationDelay = `${.06 * i}s`;
    div.innerHTML = `<div class="tip-n">${i + 1}</div><div class="tip-text">${clean}</div>`;
    tipsEl.appendChild(div);
  });
}

// ── Tools ──────────────────────────────────────────────────────────────────
const toolsEl = document.getElementById('toolsGrid');

function availClass(a) {
  const v = (a || '').toLowerCase();
  if (v === 'free') return 'avail-free';
  if (v.includes('free') && v.includes('paid')) return 'avail-mixed';
  return 'avail-paid';
}

if (toolsEl && data.tools && data.tools.length) {
  data.tools.forEach((tool, i) => {
    const icon  = TOOL_ICONS[tool.name] || '🔧';
    const steps = (tool.steps || []).map((s, si) => `
      <div class="step">
        <div class="step-n">${si + 1}</div>
        <span>${s}</span>
      </div>`).join('');

    const card = document.createElement('div');
    card.className = 'tool-card card fu';
    card.style.animationDelay = `${.08 * i}s`;
    card.innerHTML = `
      <div class="tool-top">
        <div class="tool-left">
          <div class="tool-avatar">${icon}</div>
          <div>
            <div class="tool-name">${tool.name}</div>
            <div class="tool-sub">${tool.best_for || ''}</div>
          </div>
        </div>
        <span class="avail ${availClass(tool.availability)}">${tool.availability || ''}</span>
      </div>
      <div class="tprompt">
        <div class="tprompt-label">✦ Optimized Prompt</div>
        <button class="copy-btn" onclick="copyTool(this)">Copy</button>
        <div class="tprompt-text">${tool.tool_prompt || ''}</div>
      </div>
      <div class="steps">${steps}</div>
      <div class="tool-cta">
        <a href="${tool.link}" target="_blank" rel="noopener" class="open-btn">
          Open ${tool.name} ↗
        </a>
      </div>`;
    toolsEl.appendChild(card);
  });
}

// ── Copy helpers ───────────────────────────────────────────────────────────
function copyMain() {
  navigator.clipboard.writeText(data.prompt || '').then(() => {
    const btn = document.getElementById('copyMain');
    if (btn) { btn.textContent = 'Copied!'; btn.classList.add('ok'); }
    setTimeout(() => {
      if (btn) { btn.textContent = 'Copy'; btn.classList.remove('ok'); }
    }, 2000);
  });
}

function copyTool(btn) {
  const text = btn.closest('.tprompt').querySelector('.tprompt-text').textContent;
  navigator.clipboard.writeText(text).then(() => {
    btn.textContent = 'Copied!'; btn.classList.add('ok');
    setTimeout(() => { btn.textContent = 'Copy'; btn.classList.remove('ok'); }, 2000);
  });
}

window.copyMain = copyMain;
window.copyTool = copyTool;
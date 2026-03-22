// frontend/js/index.js

const topicEl = document.getElementById('topic');
const genBtn  = document.getElementById('genBtn');
const secArea = document.getElementById('secArea');
const secGrid = document.getElementById('secGrid');
const ldSec   = document.getElementById('ldSec');
const ldGen   = document.getElementById('ldGen');
let debounce  = null;

// ── Example chips ─────────────────────────────────────────────────────────
document.querySelectorAll('[data-ex]').forEach(el => {
  el.addEventListener('click', () => {
    topicEl.value = el.dataset.ex;
    topicEl.focus();
    fetchSections(el.dataset.ex);
  });
});

// ── Auto fetch sections ───────────────────────────────────────────────────
topicEl.addEventListener('input', () => {
  clearTimeout(debounce);
  const v = topicEl.value.trim();
  if (v.length < 4) { secArea.classList.remove('show'); return; }
  debounce = setTimeout(() => fetchSections(v), 600);
});

async function fetchSections(topic) {
  ldSec.classList.add('on');
  secArea.classList.remove('show');
  try {
    const r = await fetch('/get_sections', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ topic })
    });
    const d = await r.json();
    renderSections(d.sections || []);
  } catch(e) {
    console.error('fetchSections error:', e);
  } finally {
    ldSec.classList.remove('on');
  }
}

function renderSections(sections) {
  if (!sections.length) return;
  secGrid.innerHTML = '';
  sections.forEach(s => {
    const lbl = document.createElement('label');
    lbl.className = 'sec-chip on';
    lbl.innerHTML = `<input type="checkbox" value="${s.id}" checked>
      <span>${s.icon}</span><span>${s.label}</span><span class="tick">✓</span>`;
    lbl.querySelector('input').addEventListener('change', e => {
      lbl.classList.toggle('on', e.target.checked);
    });
    secGrid.appendChild(lbl);
  });
  secArea.classList.add('show');
}

// ── Generate ──────────────────────────────────────────────────────────────
genBtn.addEventListener('click', async () => {
  const topic = topicEl.value.trim();
  if (!topic) {
    topicEl.focus();
    topicEl.style.borderColor = 'rgba(220,38,38,.5)';
    setTimeout(() => topicEl.style.borderColor = '', 1500);
    return;
  }

  const selected = Array.from(
    document.querySelectorAll('.sec-chip input:checked')
  ).map(cb => cb.closest('label').querySelectorAll('span')[1].textContent);

  ldGen.classList.add('on');
  genBtn.disabled = true;
  genBtn.textContent = 'Generating…';

  try {
    const r = await fetch('/generate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ topic, selected_sections: selected })
    });

    const data = await r.json();

    if (data.error) {
      alert('Error: ' + data.error);
      return;
    }

    // Build the result object
    const result = {
      topic:    data.topic    || topic,
      category: data.category || '',
      prompt:   data.prompt   || '',
      tips:     data.tips     || '',
      tools:    data.tools    || []
    };

    // Clear old data first then set new
    sessionStorage.removeItem('aitool_result');
    sessionStorage.setItem('aitool_result', JSON.stringify(result));

    // Verify it was saved
    const check = sessionStorage.getItem('aitool_result');
    if (!check) {
      alert('Storage error. Please try again.');
      return;
    }

    // Save to history if logged in (fire and forget)
    fetch('/api/history', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        topic:    result.topic,
        category: result.category,
        prompt:   result.prompt
      })
    }).catch(() => {});

    // Navigate to results
    window.location.href = '/results';

  } catch(e) {
    console.error('Generate error:', e);
    alert('Network error. Please try again.');
  } finally {
    ldGen.classList.remove('on');
    genBtn.disabled = false;
    genBtn.textContent = '✦ Generate Prompt & Find AI Tools';
  }
});

// ── Ctrl+Enter shortcut ───────────────────────────────────────────────────
topicEl.addEventListener('keydown', e => {
  if (e.key === 'Enter' && (e.ctrlKey || e.metaKey)) genBtn.click();
});
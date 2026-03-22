// frontend/js/index.js

const topicEl   = document.getElementById('topic');
const genBtn    = document.getElementById('genBtn');
const secArea   = document.getElementById('secArea');
const secGrid   = document.getElementById('secGrid');
const ldSec     = document.getElementById('ldSec');
const ldGen     = document.getElementById('ldGen');

let debounce = null;

// ── Example chips ─────────────────────────────────────────────────────────
document.querySelectorAll('[data-ex]').forEach(el => {
  el.addEventListener('click', () => {
    topicEl.value = el.dataset.ex;
    topicEl.focus();
    fetchSections(el.dataset.ex);
  });
});

// ── Auto-fetch sections on type ───────────────────────────────────────────
topicEl.addEventListener('input', () => {
  clearTimeout(debounce);
  const v = topicEl.value.trim();
  if (v.length < 4) { secArea.classList.remove('show'); return; }
  debounce = setTimeout(() => fetchSections(v), 600);
});

// ── Fetch sections from backend ───────────────────────────────────────────
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
  } catch (e) {
    console.error('Sections error:', e);
  } finally {
    ldSec.classList.remove('on');
  }
}

// ── Render section chips ──────────────────────────────────────────────────
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
    topicEl.style.borderColor = 'rgba(248,113,113,.6)';
    setTimeout(() => topicEl.style.borderColor = '', 1500);
    return;
  }

  const selected = Array.from(
    document.querySelectorAll('.sec-chip input:checked')
  ).map(cb => cb.closest('label').querySelectorAll('span')[1].textContent);

  ldGen.classList.add('on');
  genBtn.disabled = true;

  try {
    const r = await fetch('/generate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ topic, selected_sections: selected })
    });
    const data = await r.json();
    if (data.error) { alert('Error: ' + data.error); return; }

    // Pass data to results page via sessionStorage then navigate
    sessionStorage.setItem('aitool_result', JSON.stringify({ ...data, topic }));
    window.location.href = '/results';
  } catch (e) {
    alert('Network error. Please try again.');
    console.error(e);
  } finally {
    ldGen.classList.remove('on');
    genBtn.disabled = false;
  }
});

// ── Ctrl+Enter shortcut ───────────────────────────────────────────────────
topicEl.addEventListener('keydown', e => {
  if (e.key === 'Enter' && (e.ctrlKey || e.metaKey)) genBtn.click();
});

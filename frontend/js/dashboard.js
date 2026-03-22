// frontend/js/dashboard.js

const CAT_ICONS = {
  presentation:'📊', image:'🎨', audio:'🎵', video:'🎬',
  coding:'💻', research:'🔬', writing:'✍️', ai_tool_usage:'🤖'
};

// ── Load user info ─────────────────────────────────────────────────────────
async function loadUser() {
  try {
    const r = await fetch('/api/me');
    const d = await r.json();
    if (!d.logged_in) {
      window.location.href = '/login';
      return;
    }
    const initials = d.username.split(' ').map(w=>w[0]).join('').toUpperCase().slice(0,2);
    document.getElementById('dashName').textContent  = d.username;
    document.getElementById('dashEmail').textContent = d.email;

    // update nav right
    const navRight = document.getElementById('navRight');
    if (navRight) {
      navRight.innerHTML = `
        <div class="user-menu">
          <div class="user-avatar">${initials}</div>
          <span class="user-name">${d.username}</span>
          <a href="/" class="nav-dashboard-btn">← Home</a>
          <button class="nav-logout-btn" onclick="doLogout()">Logout</button>
        </div>`;
    }
  } catch(e) {
    window.location.href = '/login';
  }
}

// ── Load history ───────────────────────────────────────────────────────────
async function loadHistory() {
  const grid = document.getElementById('historyGrid');
  try {
    const r = await fetch('/api/history');
    if (r.status === 401) { window.location.href = '/login'; return; }
    const items = await r.json();

    // update stats
    document.getElementById('totalCount').textContent = items.length;
    const today = new Date().toDateString();
    const todayItems = items.filter(h => {
      const d = new Date(h.created_at);
      return d.toDateString() === today;
    });
    document.getElementById('todayCount').textContent = todayItems.length;

    if (!items.length) {
      grid.innerHTML = `
        <div class="empty-state">
          <div class="empty-icon">📋</div>
          <div class="empty-title">No prompts yet</div>
          <div class="empty-sub">Go to the <a href="/" style="color:var(--accent);font-weight:600;">home page</a> and generate your first prompt!</div>
        </div>`;
      return;
    }

    grid.innerHTML = '';
    items.forEach((h, i) => {
      const icon = CAT_ICONS[h.category] || '🤖';
      const card = document.createElement('div');
      card.className = 'history-card card fu';
      card.style.animationDelay = `${0.05 * i}s`;
      card.innerHTML = `
        <div class="history-icon">${icon}</div>
        <div class="history-body">
          <div class="history-topic">${h.topic}</div>
          <div class="history-prompt">${h.prompt || 'No prompt saved'}</div>
          <div class="history-meta">
            <span class="history-cat">${(h.category||'general').replace(/_/g,' ')}</span>
            <span class="history-date">${h.created_at}</span>
          </div>
        </div>
        <div class="history-actions">
          <button class="copy-btn" onclick="copyPrompt(this, \`${escapeBacktick(h.prompt)}\`)">Copy</button>
          <button class="del-btn" onclick="deleteItem(${h.id}, this)" title="Delete">🗑</button>
        </div>`;

      // click card to re-run same topic
      card.addEventListener('click', (e) => {
        if (e.target.closest('.history-actions')) return;
        sessionStorage.setItem('aitool_result', JSON.stringify({
          topic: h.topic, category: h.category,
          prompt: h.prompt, tips: '', tools: []
        }));
        window.location.href = '/results';
      });

      grid.appendChild(card);
    });
  } catch(e) {
    grid.innerHTML = `<div class="empty-state"><div class="empty-icon">⚠️</div><div class="empty-title">Failed to load history</div></div>`;
  }
}

// ── Delete history item ────────────────────────────────────────────────────
async function deleteItem(id, btn) {
  btn.closest('.history-card').style.opacity = '0.4';
  try {
    await fetch(`/api/history/${id}`, { method: 'DELETE' });
    showToast('Deleted!');
    loadHistory();
  } catch(e) {
    btn.closest('.history-card').style.opacity = '1';
  }
}

// ── Copy prompt ────────────────────────────────────────────────────────────
function copyPrompt(btn, text) {
  navigator.clipboard.writeText(text).then(() => {
    btn.textContent = 'Copied!';
    btn.classList.add('ok');
    setTimeout(() => { btn.textContent = 'Copy'; btn.classList.remove('ok'); }, 2000);
    showToast('Prompt copied!');
  });
}

function escapeBacktick(str) {
  return (str || '').replace(/`/g, '\\`').replace(/\$/g, '\\$');
}

function showToast(msg) {
  const t = document.getElementById('toast') || document.createElement('div');
  t.id = 'toast'; t.className = 'toast';
  if (!document.getElementById('toast')) document.body.appendChild(t);
  t.textContent = msg;
  t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 2500);
}

// ── Init ───────────────────────────────────────────────────────────────────
loadUser();
loadHistory();

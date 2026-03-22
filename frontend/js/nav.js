// frontend/js/nav.js — shared navbar auth state

async function initNav() {
  const navRight = document.getElementById('navRight');
  if (!navRight) return;
  try {
    const r = await fetch('/api/me');
    const d = await r.json();
    const existing = navRight.innerHTML;
    if (d.logged_in) {
      const initials = d.username.split(' ').map(w => w[0]).join('').toUpperCase().slice(0, 2);
      navRight.innerHTML = `
        <div class="user-menu">
          <div class="user-avatar">${initials}</div>
          <span class="user-name">${d.username}</span>
          <a href="/dashboard" class="nav-dashboard-btn">Dashboard</a>
          <button class="nav-logout-btn" onclick="doLogout()">Logout</button>
        </div>
        ${existing}`;
    } else {
      navRight.innerHTML = `
        <a href="/login" class="nav-login-btn">Login</a>
        <a href="/signup" class="nav-signup-btn">Sign Up</a>
        ${existing}`;
    }
  } catch(e) {
    console.error('nav error:', e);
  }
}

async function doLogout() {
  await fetch('/api/logout', { method: 'POST' });
  window.location.href = '/';
}

function showToast(msg, duration = 2500) {
  let t = document.getElementById('toast');
  if (!t) {
    t = document.createElement('div');
    t.id = 'toast';
    t.className = 'toast';
    document.body.appendChild(t);
  }
  t.textContent = msg;
  t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), duration);
}

initNav();
document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.getElementById('login-form');
  const registerForm = document.getElementById('register-form');

  if (loginForm) {
    loginForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const username = document.getElementById('username').value.trim();
      const password = document.getElementById('password').value;
      if (!username || !password) {
        alert('Username and password required');
        return;
      }
      const btn = loginForm.querySelector('button');
      btn.disabled = true;
      try {
        const res = await fetch('/api/login', {
          method: 'POST', headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ username, password })
        });
        if (res.ok) {
          window.location = '/app';
        } else {
          const body = await res.json().catch(() => ({}));
          alert(body.error || 'Invalid credentials');
        }
      } finally {
        btn.disabled = false;
      }
    });
  }

  if (registerForm) {
    registerForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const username = document.getElementById('username').value.trim();
      const password = document.getElementById('password').value;
      if (!username || !password) {
        alert('Username and password required');
        return;
      }
      const btn = registerForm.querySelector('button');
      btn.disabled = true;
      try {
        const res = await fetch('/api/register', {
          method: 'POST', headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ username, password })
        });
        if (res.ok) {
          window.location = '/app';
        } else {
          const body = await res.json().catch(() => ({}));
          alert(body.error || 'Registration failed');
        }
      } finally {
        btn.disabled = false;
      }
    });
  }
});

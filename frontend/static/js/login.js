document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.getElementById('login-form');
  const registerForm = document.getElementById('register-form');
  const messageDiv = document.getElementById('auth-message');

  function showMessage(text, type = 'error') {
    if (!messageDiv) return;
    messageDiv.innerHTML = `<div class="auth-message ${type}">${text}</div>`;
    setTimeout(() => {
      messageDiv.innerHTML = '';
    }, 5000);
  }

  if (loginForm) {
    loginForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      
      const username = document.getElementById('username').value.trim();
      const password = document.getElementById('password').value;
      const btn = loginForm.querySelector('button');
      
      // Validation
      if (!username || !password) {
        showMessage('❌ Please fill in all fields', 'error');
        return;
      }

      btn.disabled = true;
      btn.style.opacity = '0.6';
      const originalText = btn.textContent;
      btn.textContent = '⏳ Signing in...';

      try {
        const res = await fetch('/api/auth/login', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ username, password })
        });

        if (res.ok) {
          showMessage('✅ Sign in successful! Redirecting...', 'success');
          setTimeout(() => {
            window.location = '/app';
          }, 500);
        } else {
          const body = await res.json().catch(() => ({}));
          showMessage(`❌ ${body.error || 'Sign in failed. Please try again.'}`, 'error');
        }
      } catch (e) {
        showMessage('❌ Connection error. Please try again.', 'error');
        console.error(e);
      } finally {
        btn.disabled = false;
        btn.style.opacity = '1';
        btn.textContent = originalText;
      }
    });
  }

  if (registerForm) {
    registerForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      
      const username = document.getElementById('username').value.trim();
      const password = document.getElementById('password').value;
      const btn = registerForm.querySelector('button');
      
      // Validation
      if (!username || !password) {
        showMessage('❌ Please fill in all fields', 'error');
        return;
      }

      if (username.length < 3 || username.length > 20) {
        showMessage('❌ Username must be 3-20 characters', 'error');
        return;
      }

      if (password.length < 6) {
        showMessage('❌ Password must be at least 6 characters', 'error');
        return;
      }

      btn.disabled = true;
      btn.style.opacity = '0.6';
      const originalText = btn.textContent;
      btn.textContent = '⏳ Creating account...';

      try {
        const res = await fetch('/api/auth/register', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ username, password })
        });

        if (res.ok) {
          showMessage('✅ Account created! Redirecting...', 'success');
          setTimeout(() => {
            window.location = '/app';
          }, 500);
        } else {
          const body = await res.json().catch(() => ({}));
          showMessage(`❌ ${body.error || 'Registration failed. Please try again.'}`, 'error');
        }
      } catch (e) {
        showMessage('❌ Connection error. Please try again.', 'error');
        console.error(e);
      } finally {
        btn.disabled = false;
        btn.style.opacity = '1';
        btn.textContent = originalText;
      }
    });
  }
});

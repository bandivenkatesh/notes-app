// Legacy app.js - functionality now in notes-enhanced.js
// Kept for backward compatibility

document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('note-form');
  const notesEl = document.getElementById('notes');

  async function loadNotes() {
    const res = await fetch('/api/notes');
    const notes = await res.json();
    render(notes);
  }

  function render(notes) {
    notesEl.innerHTML = '';
    if (!notes || notes.length === 0) {
      notesEl.innerHTML = '<div class="empty"><div class="empty-icon">📝</div><p>No notes yet. Create your first note above!</p></div>';
      return;
    }
    notes.forEach((n, i) => {
      const card = document.createElement('div');
      card.className = 'note';
      card.style.opacity = 0;
      card.style.animationDelay = `${i * 50}ms`;

      const h = document.createElement('h3');
      h.textContent = n.title || '(Untitled)';

      const meta = document.createElement('div');
      meta.className = 'note-meta';
      const date = new Date(n.created_at);
      const timeString = date.toLocaleDateString('en-US', {
        month: 'short',
        day: 'numeric',
        year: date.getFullYear() !== new Date().getFullYear() ? 'numeric' : undefined
      });
      meta.innerHTML = `<span class="note-time">${timeString}</span>`;

      const p = document.createElement('p');
      p.textContent = n.content;

      const btnContainer = document.createElement('div');
      btnContainer.className = 'note-actions';
      const btn = document.createElement('button');
      btn.className = 'note-btn';
      btn.textContent = '🗑️ Delete';
      btn.addEventListener('click', async () => {
        if (confirm('Delete this note?')) {
          await fetch('/api/notes/' + n.id, { method: 'DELETE' });
          loadNotes();
        }
      });
      btnContainer.appendChild(btn);

      card.appendChild(h);
      card.appendChild(p);
      card.appendChild(meta);
      meta.appendChild(btnContainer);
      notesEl.appendChild(card);

      requestAnimationFrame(() => {
        card.style.transition = 'opacity 400ms ease, transform 400ms ease';
        card.style.opacity = 1;
        card.style.transform = 'translateY(0)';
      });
    });
  }

  if (form) {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const title = document.getElementById('title').value;
      const content = document.getElementById('content').value;
      const btn = form.querySelector('button');
      btn.disabled = true;
      btn.style.opacity = '0.6';
      try {
        await fetch('/api/notes', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ title, content })
        });
        form.reset();
        loadNotes();
      } finally {
        btn.disabled = false;
        btn.style.opacity = '1';
      }
    });
  }

  loadNotes();
});


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
      notesEl.innerHTML = '<p class="empty">No notes yet.</p>';
      return;
    }
    notes.forEach(n => {
      const card = document.createElement('div');
      card.className = 'note';
      card.style.opacity = 0;

      const h = document.createElement('h3');
      h.textContent = n.title || '(no title)';

      const meta = document.createElement('div');
      meta.className = 'meta';
      meta.textContent = new Date(n.created_at).toLocaleString();

      const p = document.createElement('p');
      p.textContent = n.content;

      const btn = document.createElement('button');
      btn.className = 'delete';
      btn.textContent = 'Delete';
      btn.addEventListener('click', async () => {
        btn.disabled = true;
        await fetch('/api/notes/' + n.id, { method: 'DELETE' });
        loadNotes();
      });

      card.appendChild(h);
      card.appendChild(meta);
      card.appendChild(p);
      card.appendChild(btn);
      notesEl.appendChild(card);

      // simple fade-in animation
      requestAnimationFrame(() => { card.style.transition = 'opacity 240ms ease, transform 240ms ease'; card.style.opacity = 1; card.style.transform = 'translateY(0)'; });
    });
  }

  if (form) {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const title = document.getElementById('title').value;
      const content = document.getElementById('content').value;
      const btn = form.querySelector('button');
      btn.disabled = true;
      await fetch('/api/notes', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title, content })
      });
      btn.disabled = false;
      form.reset();
      loadNotes();
    });
  }

  loadNotes();
});

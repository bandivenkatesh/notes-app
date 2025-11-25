// Enhanced Notes App with Advanced Animations and Interactions

class NotesApp {
  constructor() {
    this.notesContainer = document.getElementById('notes');
    this.form = document.getElementById('note-form');
    this.titleInput = document.getElementById('title');
    this.contentInput = document.getElementById('content');
    this.notes = [];
    
    this.init();
  }

  init() {
    if (this.form) {
      this.form.addEventListener('submit', (e) => this.handleSubmit(e));
    }
    this.loadNotes();
  }

  async loadNotes() {
    try {
      const res = await fetch('/api/notes');
      if (res.ok) {
        this.notes = await res.json();
        this.render();
      }
    } catch (e) {
      console.error('Error loading notes:', e);
      this.showNotification('Failed to load notes', 'error');
    }
  }

  async handleSubmit(e) {
    e.preventDefault();
    
    const title = this.titleInput.value.trim();
    const content = this.contentInput.value.trim();
    const btn = this.form.querySelector('button');

    if (!title || !content) {
      this.showNotification('❌ Please enter title and content', 'error');
      return;
    }

    btn.disabled = true;
    btn.style.opacity = '0.6';
    const originalText = btn.textContent;
    btn.textContent = '⏳ Saving...';

    try {
      const res = await fetch('/api/notes', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title, content })
      });

      if (res.ok) {
        this.form.reset();
        this.showNotification('✅ Note created successfully!', 'success');
        await this.loadNotes();
      } else {
        const error = await res.json().catch(() => ({}));
        this.showNotification(`❌ ${error.error || 'Failed to create note'}`, 'error');
      }
    } catch (e) {
      console.error(e);
      this.showNotification('❌ Connection error', 'error');
    } finally {
      btn.disabled = false;
      btn.style.opacity = '1';
      btn.textContent = originalText;
    }
  }

  render() {
    this.notesContainer.innerHTML = '';

    if (!this.notes || this.notes.length === 0) {
      this.notesContainer.innerHTML = `
        <div class="empty">
          <div class="empty-icon">📝</div>
          <p>No notes yet. Create your first note above!</p>
        </div>
      `;
      return;
    }

    this.notes.forEach((note, index) => {
      const noteEl = this.createNoteElement(note, index);
      this.notesContainer.appendChild(noteEl);
    });
  }

  createNoteElement(note, index) {
    const card = document.createElement('div');
    card.className = 'note';
    card.style.animationDelay = `${index * 50}ms`;

    const date = new Date(note.created_at);
    const timeString = date.toLocaleDateString('en-US', {
      month: 'short',
      day: 'numeric',
      year: date.getFullYear() !== new Date().getFullYear() ? 'numeric' : undefined
    });

    const h3 = document.createElement('h3');
    h3.textContent = note.title || '(Untitled)';

    const p = document.createElement('p');
    p.textContent = note.content;

    const meta = document.createElement('div');
    meta.className = 'note-meta';

    const timeEl = document.createElement('span');
    timeEl.className = 'note-time';
    timeEl.textContent = timeString;

    const actionsEl = document.createElement('div');
    actionsEl.className = 'note-actions';

    const deleteBtn = document.createElement('button');
    deleteBtn.className = 'note-btn';
    deleteBtn.textContent = '🗑️ Delete';
    deleteBtn.addEventListener('click', async (e) => {
      e.preventDefault();
      await this.deleteNote(note.id);
    });

    actionsEl.appendChild(deleteBtn);
    meta.appendChild(timeEl);
    meta.appendChild(actionsEl);

    card.appendChild(h3);
    card.appendChild(p);
    card.appendChild(meta);

    // Add subtle entrance animation
    card.style.opacity = '0';
    card.style.transform = 'translateY(20px)';
    requestAnimationFrame(() => {
      card.style.transition = 'all 400ms cubic-bezier(0.4, 0, 0.2, 1)';
      card.style.opacity = '1';
      card.style.transform = 'translateY(0)';
    });

    return card;
  }

  async deleteNote(id) {
    if (!confirm('Are you sure you want to delete this note?')) return;

    try {
      const res = await fetch(`/api/notes/${id}`, { method: 'DELETE' });
      if (res.ok) {
        this.showNotification('✅ Note deleted', 'success');
        await this.loadNotes();
      } else {
        this.showNotification('❌ Failed to delete note', 'error');
      }
    } catch (e) {
      console.error(e);
      this.showNotification('❌ Connection error', 'error');
    }
  }

  showNotification(message, type = 'info') {
    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    toast.textContent = message;
    document.body.appendChild(toast);

    setTimeout(() => {
      toast.style.animation = 'slideInRight 0.3s ease-out reverse';
      setTimeout(() => toast.remove(), 300);
    }, 3000);
  }
}

// Initialize app when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => {
    new NotesApp();
  });
} else {
  new NotesApp();
}

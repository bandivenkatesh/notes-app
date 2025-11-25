"""Note model and database operations."""
import uuid
import datetime
from utils.database import load_json, save_json
from config import NOTES_FILE

class Note:
    """Note model."""
    
    @staticmethod
    def create(title: str, content: str) -> dict:
        """Create a new note."""
        return {
            'id': uuid.uuid4().hex,
            'title': (title or '').strip(),
            'content': (content or '').strip(),
            'created_at': datetime.datetime.utcnow().isoformat() + 'Z'
        }
    
    @staticmethod
    def get_all() -> list:
        """Get all notes."""
        notes = load_json(NOTES_FILE)
        return sorted(notes, key=lambda n: n.get('created_at', ''), reverse=True)
    
    @staticmethod
    def get_by_id(note_id: str) -> dict:
        """Get note by ID."""
        notes = Note.get_all()
        for note in notes:
            if note.get('id') == note_id:
                return note
        return None
    
    @staticmethod
    def save(note: dict) -> bool:
        """Add new note to database."""
        notes = load_json(NOTES_FILE)
        notes.insert(0, note)
        return save_json(NOTES_FILE, notes)
    
    @staticmethod
    def update(note_id: str, title: str = None, content: str = None) -> dict:
        """Update an existing note."""
        notes = load_json(NOTES_FILE)
        for note in notes:
            if note.get('id') == note_id:
                if title is not None:
                    note['title'] = (title or '').strip()
                if content is not None:
                    note['content'] = (content or '').strip()
                note['updated_at'] = datetime.datetime.utcnow().isoformat() + 'Z'
                save_json(NOTES_FILE, notes)
                return note
        return None
    
    @staticmethod
    def delete(note_id: str) -> bool:
        """Delete a note."""
        notes = load_json(NOTES_FILE)
        new_notes = [n for n in notes if n.get('id') != note_id]
        if len(new_notes) == len(notes):
            return False
        save_json(NOTES_FILE, new_notes)
        return True

"""Notes routes."""
from flask import Blueprint, request, jsonify, session
from models.note import Note
from utils.validators import validate_note_title, validate_note_content

notes_bp = Blueprint('notes', __name__, url_prefix='/api/notes')

def require_auth(f):
    """Decorator to require authentication."""
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('user'):
            return jsonify({'error': 'Unauthorized'}), 401
        return f(*args, **kwargs)
    return decorated_function

@notes_bp.route('', methods=['GET'])
def get_notes():
    """Get all notes."""
    return jsonify(Note.get_all())

@notes_bp.route('', methods=['POST'])
@require_auth
def create_note():
    """Create a new note."""
    data = request.get_json() or {}
    title = (data.get('title') or '').strip()
    content = (data.get('content') or '').strip()
    
    # Validate
    valid, msg = validate_note_title(title)
    if not valid:
        return jsonify({'error': msg}), 400
    
    valid, msg = validate_note_content(content)
    if not valid:
        return jsonify({'error': msg}), 400
    
    if not (title or content):
        return jsonify({'error': 'Title or content is required'}), 400
    
    note = Note.create(title, content)
    Note.save(note)
    
    return jsonify(note), 201

@notes_bp.route('/<note_id>', methods=['GET'])
def get_note(note_id):
    """Get a single note."""
    note = Note.get_by_id(note_id)
    if not note:
        return jsonify({'error': 'Note not found'}), 404
    return jsonify(note)

@notes_bp.route('/<note_id>', methods=['PUT'])
@require_auth
def update_note(note_id):
    """Update a note."""
    data = request.get_json() or {}
    title = data.get('title')
    content = data.get('content')
    
    # Validate if provided
    if title is not None:
        valid, msg = validate_note_title(title)
        if not valid:
            return jsonify({'error': msg}), 400
    
    if content is not None:
        valid, msg = validate_note_content(content)
        if not valid:
            return jsonify({'error': msg}), 400
    
    note = Note.update(note_id, title, content)
    if not note:
        return jsonify({'error': 'Note not found'}), 404
    
    return jsonify(note)

@notes_bp.route('/<note_id>', methods=['DELETE'])
@require_auth
def delete_note(note_id):
    """Delete a note."""
    if not Note.delete(note_id):
        return jsonify({'error': 'Note not found'}), 404
    return '', 204

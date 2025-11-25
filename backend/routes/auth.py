"""Authentication routes."""
from flask import Blueprint, request, jsonify, session
from models.user import User
from utils.validators import validate_username, validate_password

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.get_json() or {}
    username = (data.get('username') or '').strip()
    password = data.get('password', '')
    
    # Validate
    valid, msg = validate_username(username)
    if not valid:
        return jsonify({'error': msg}), 400
    
    valid, msg = validate_password(password)
    if not valid:
        return jsonify({'error': msg}), 400
    
    # Check if exists
    if User.exists(username):
        return jsonify({'error': 'Username already taken'}), 400
    
    # Create and save
    user = User.create(username, password)
    User.save(user)
    
    # Set session
    session['user'] = username
    
    return jsonify({'username': username, 'id': user['id']}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    """Login user."""
    data = request.get_json() or {}
    username = (data.get('username') or '').strip()
    password = data.get('password', '')
    
    user = User.authenticate(username, password)
    if not user:
        return jsonify({'error': 'Invalid username or password'}), 401
    
    session['user'] = username
    return jsonify({'username': username, 'id': user['id']})

@auth_bp.route('/logout', methods=['POST'])
def logout():
    """Logout user."""
    session.pop('user', None)
    return '', 204

@auth_bp.route('/me', methods=['GET'])
def get_current_user():
    """Get current logged-in user."""
    user = session.get('user')
    if not user:
        return jsonify({'error': 'Not authenticated'}), 401
    
    user_obj = User.get_by_username(user)
    if not user_obj:
        return jsonify({'error': 'User not found'}), 404
    
    return jsonify({
        'username': user_obj['username'],
        'id': user_obj['id'],
        'created_at': user_obj['created_at']
    })

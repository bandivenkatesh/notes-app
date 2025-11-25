"""User model and database operations."""
import uuid
import datetime
from utils.database import load_json, save_json
from config import USERS_FILE
from werkzeug.security import generate_password_hash, check_password_hash

class User:
    """User model."""
    
    @staticmethod
    def create(username: str, password: str) -> dict:
        """Create a new user."""
        return {
            'id': uuid.uuid4().hex,
            'username': username,
            'password_hash': generate_password_hash(password),
            'created_at': datetime.datetime.utcnow().isoformat() + 'Z'
        }
    
    @staticmethod
    def get_all() -> list:
        """Get all users."""
        return load_json(USERS_FILE)
    
    @staticmethod
    def get_by_username(username: str) -> dict:
        """Get user by username."""
        users = User.get_all()
        for user in users:
            if user.get('username') == username:
                return user
        return None
    
    @staticmethod
    def exists(username: str) -> bool:
        """Check if user exists."""
        return User.get_by_username(username) is not None
    
    @staticmethod
    def save(user: dict) -> bool:
        """Save user to database."""
        users = User.get_all()
        users.append(user)
        return save_json(USERS_FILE, users)
    
    @staticmethod
    def authenticate(username: str, password: str) -> dict:
        """Authenticate user with password."""
        user = User.get_by_username(username)
        if user and check_password_hash(user.get('password_hash', ''), password):
            return user
        return None

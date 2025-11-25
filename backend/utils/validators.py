"""Validation utilities for user input."""
import re

def validate_username(username: str) -> tuple[bool, str]:
    """Validate username format."""
    username = (username or '').strip()
    if not username:
        return False, "Username is required"
    if len(username) < 3:
        return False, "Username must be at least 3 characters"
    if len(username) > 20:
        return False, "Username must be at most 20 characters"
    if not re.match("^[a-zA-Z0-9_-]+$", username):
        return False, "Username can only contain letters, numbers, hyphens, and underscores"
    return True, ""

def validate_password(password: str) -> tuple[bool, str]:
    """Validate password strength."""
    if not password:
        return False, "Password is required"
    if len(password) < 6:
        return False, "Password must be at least 6 characters"
    if len(password) > 128:
        return False, "Password must be at most 128 characters"
    return True, ""

def validate_note_title(title: str) -> tuple[bool, str]:
    """Validate note title."""
    title = (title or '').strip()
    if len(title) > 200:
        return False, "Title must be at most 200 characters"
    return True, ""

def validate_note_content(content: str) -> tuple[bool, str]:
    """Validate note content."""
    content = (content or '').strip()
    if len(content) > 50000:
        return False, "Content must be at most 50000 characters"
    return True, ""

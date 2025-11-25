"""Configuration settings for the Notes App."""
import os

# Flask
DEBUG = os.environ.get('FLASK_ENV', 'development') == 'development'
SECRET_KEY = os.environ.get('FLASK_SECRET', 'dev-secret-change-me-in-production')

# Data
BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, 'data')
USERS_FILE = os.path.join(DATA_DIR, 'users.json')
NOTES_FILE = os.path.join(DATA_DIR, 'notes.json')

# App
HOST = '0.0.0.0'
PORT = int(os.environ.get('PORT', 5000))

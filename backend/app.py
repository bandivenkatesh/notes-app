"""Main Flask application."""
import os
import sys
from flask import Flask, render_template, redirect, url_for, session

# Add backend to path for imports
sys.path.insert(0, os.path.dirname(__file__))

from config import DEBUG, SECRET_KEY, HOST, PORT
from routes.auth import auth_bp
from routes.notes import notes_bp

def create_app():
    """Create and configure Flask app."""
    app = Flask(__name__, 
                static_folder='../frontend/static',
                template_folder='./templates')
    
    app.secret_key = SECRET_KEY
    app.debug = DEBUG
    
    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(notes_bp)
    
    # Page routes
    @app.route('/')
    def landing():
        """Landing page."""
        return render_template('landing.html')
    
    @app.route('/login')
    def login_page():
        """Login page."""
        return render_template('login.html')
    
    @app.route('/register')
    def register_page():
        """Register page."""
        return render_template('register.html')
    
    @app.route('/app')
    def notes_page():
        """Notes application (protected)."""
        if not session.get('user'):
            return redirect(url_for('login_page'))
        return render_template('notes.html')
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host=HOST, port=PORT, debug=DEBUG)

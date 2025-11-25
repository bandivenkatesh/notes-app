# notes-app

A simple, fast notes application with user authentication and a responsive UI. Built with Flask backend and vanilla JavaScript frontend.

## Features

- **User Authentication**: Register, login, logout with password hashing
- **Notes CRUD**: Create, read, update, delete notes
- **Responsive Design**: Works on desktop and mobile
- **Smooth Animations**: Fade-in transitions and focus effects
- **Session Management**: Secure session-based auth
- **Persistent Storage**: JSON-based data files

## Tech Stack

- **Backend**: Flask (Python 3)
- **Frontend**: HTML5, CSS3, JavaScript (vanilla)
- **Database**: JSON files
- **Security**: werkzeug password hashing

## Quick Start

### Prerequisites
- Python 3.7+

### Installation & Running

```bash
cd frontend

# Optional: Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the server
python app.py
```

The app will be available at **http://localhost:5000**

## Pages

| Route | Purpose |
|-------|---------|
| `/` | Landing page with sign-in/register CTAs |
| `/register` | Create new account |
| `/login` | Sign in to existing account |
| `/app` | Protected notes interface (redirects to login if not authenticated) |

## API Endpoints

### Authentication
- `POST /api/register` - Register new user
- `POST /api/login` - Login and create session
- `POST /api/logout` - Clear session

### Notes
- `GET /api/notes` - Fetch all notes
- `POST /api/notes` - Create new note
- `PUT /api/notes/<id>` - Update note
- `DELETE /api/notes/<id>` - Delete note

## Data Storage

- **Users**: `frontend/users.json` (with hashed passwords)
- **Notes**: `frontend/notes.json`

## Testing

See [TEST_RESULTS.md](TEST_RESULTS.md) for test documentation and curl examples.

### Quick Test

```bash
# Register a user
curl -X POST http://127.0.0.1:5000/api/register \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","password":"pass123"}'

# Create a note
curl -X POST http://127.0.0.1:5000/api/notes \
  -H "Content-Type: application/json" \
  -d '{"title":"My Note","content":"Hello world"}'

# Get all notes
curl http://127.0.0.1:5000/api/notes
```

## File Structure

```
frontend/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── notes.json            # Notes storage
├── users.json            # Users storage
├── templates/
│   ├── landing.html      # Home page
│   ├── login.html        # Login form
│   ├── register.html     # Registration form
│   └── notes.html        # Notes interface
└── static/
    ├── app.js            # Notes app script
    ├── login.js          # Auth form script
    └── styles.css        # Styling
```

## Development

The app runs in debug mode with auto-reload. Edit files and the server will restart automatically.

For production, use a proper WSGI server like Gunicorn:
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```
# notes-app
# Project Folder Structure

```
notes-app/
├── backend/                          # Flask backend application
│   ├── app.py                        # Main Flask app factory
│   ├── config.py                     # Configuration settings
│   ├── requirements.txt              # Python dependencies
│   │
│   ├── routes/                       # API route blueprints
│   │   ├── __init__.py
│   │   ├── auth.py                   # Authentication endpoints (/api/auth/*)
│   │   └── notes.py                  # Notes CRUD endpoints (/api/notes/*)
│   │
│   ├── models/                       # Data models and DB operations
│   │   ├── __init__.py
│   │   ├── user.py                   # User model and queries
│   │   └── note.py                   # Note model and queries
│   │
│   ├── utils/                        # Helper utilities
│   │   ├── __init__.py
│   │   ├── database.py               # JSON file persistence
│   │   └── validators.py             # Input validation
│   │
│   ├── middleware/                   # Custom middleware (future use)
│   │   └── __init__.py
│   │
│   ├── data/                         # Data storage (JSON databases)
│   │   ├── users.json                # User accounts
│   │   └── notes.json                # Notes database
│   │
│   └── templates/                    # HTML templates
│       ├── landing.html              # Landing page (/)
│       ├── login.html                # Login page (/login)
│       ├── register.html             # Registration page (/register)
│       └── notes.html                # Notes interface (/app)
│
├── frontend/                         # Frontend assets
│   └── static/
│       ├── css/
│       │   └── styles.css            # All styling & animations
│       ├── js/
│       │   ├── app.js                # Notes UI logic
│       │   └── login.js              # Auth form logic
│       └── img/                      # Images (future use)
│
├── docs/                             # Project documentation
│   ├── API.md                        # API endpoints documentation
│   ├── FEATURES.md                   # Feature list
│   └── ROADMAP.md                    # Development roadmap
│
├── .gitignore                        # Git ignore file
├── README.md                         # Main documentation
└── PHASE2_ROADMAP.md                 # Next features roadmap
```

## Directory Purpose

| Directory | Purpose |
|-----------|---------|
| `backend/` | Flask application - all server logic |
| `backend/routes/` | RESTful API endpoints organized by feature |
| `backend/models/` | Data models and database operations |
| `backend/utils/` | Utility functions (validation, persistence) |
| `backend/data/` | JSON database files |
| `backend/templates/` | HTML templates rendered by Flask |
| `frontend/static/` | CSS, JavaScript, and images (served by Flask) |
| `docs/` | Project documentation and guides |

## Key Improvements

1. **Separation of Concerns**
   - Routes: API endpoints
   - Models: Data operations
   - Utils: Helper functions
   - Config: Centralized settings

2. **Scalability**
   - Easy to add new routes
   - Models are reusable
   - Validators are centralized

3. **Maintainability**
   - Clear file organization
   - Each file has single responsibility
   - Easy to locate and modify code

4. **Production Ready**
   - Separate frontend assets
   - Configuration management
   - Validation on backend

## Running the Application

```bash
cd backend
pip install -r requirements.txt
python app.py
```

Visit `http://localhost:5000`

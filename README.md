# Notes App

A modern notes application with user authentication and a responsive UI. Built with Flask backend and vanilla JavaScript frontend.

## 🎯 Project Status

**Phase 1:** ✅ Complete - Core features implemented and tested
**Phase 2:** 📋 Planned - Advanced features in roadmap

See [PHASE2_ROADMAP.md](PHASE2_ROADMAP.md) for upcoming features.

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Installation

```bash
# Clone or navigate to project
cd notes-app/backend

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

The app will be available at **http://localhost:5000**

## 📁 Project Structure

See [docs/FOLDER_STRUCTURE.md](docs/FOLDER_STRUCTURE.md) for detailed folder organization.

```
notes-app/
├── backend/              # Flask application & API
├── frontend/static/      # CSS, JavaScript, images
├── docs/                 # Documentation
└── README.md            # This file
```

## ✨ Features

### Authentication
- ✅ User registration and login
- ✅ Secure password hashing
- ✅ Session-based authentication
- ✅ Logout functionality

### Notes Management
- ✅ Create, read, update, delete notes
- ✅ Note timestamps
- ✅ Search and sort
- ✅ Responsive UI

### User Experience
- ✅ Beautiful landing page
- ✅ Smooth animations
- ✅ Mobile-friendly design
- ✅ Form validation
- ✅ Error handling

## 📚 Documentation

| Document | Purpose |
|----------|---------|
| [docs/API.md](docs/API.md) | API endpoints reference |
| [docs/FEATURES.md](docs/FEATURES.md) | Completed features list |
| [docs/FOLDER_STRUCTURE.md](docs/FOLDER_STRUCTURE.md) | Project organization |
| [PHASE2_ROADMAP.md](PHASE2_ROADMAP.md) | Planned features |

## 🔗 API Endpoints

### Authentication (`/api/auth`)
- `POST /register` - Create account
- `POST /login` - Sign in
- `POST /logout` - Sign out
- `GET /me` - Get current user

### Notes (`/api/notes`)
- `GET /notes` - List all notes
- `POST /notes` - Create note
- `GET /notes/<id>` - Get single note
- `PUT /notes/<id>` - Update note
- `DELETE /notes/<id>` - Delete note

See [docs/API.md](docs/API.md) for full documentation.

## 🧪 Testing

### Test Account
```
Username: alice
Password: secret123
```

Or create a new account by visiting the app.

### Test Flow
1. Visit `http://localhost:5000`
2. Click "Get started"
3. Create an account
4. Write and manage notes
5. Sign out and sign back in

## 💾 Data Storage

- **Users:** `backend/data/users.json` (with hashed passwords)
- **Notes:** `backend/data/notes.json`

Data is persisted locally using JSON files. For production, migrate to a proper database (see Phase 2 roadmap).

## 🛠️ Development

### Project Architecture

```
Backend: Flask with modular organization
├── routes/   - API endpoints
├── models/   - Data models
├── utils/    - Helper functions
└── config.py - Configuration

Frontend: Vanilla JavaScript
├── CSS animations & transitions
├── Form validation
└── API client
```

### Adding New Features

1. Create route in `backend/routes/`
2. Add model logic in `backend/models/`
3. Add validators in `backend/utils/validators.py`
4. Create frontend form in `backend/templates/`
5. Add JavaScript handler in `frontend/static/js/`

## 🔐 Security

- Passwords hashed with werkzeug (scrypt algorithm)
- Session-based authentication
- Protected routes with authentication checks
- Input validation on all endpoints
- CORS-safe (same-origin design)

## 📈 Next Steps (Phase 2)

Priority features:
1. Rich text editor / Markdown support
2. Note tags and categories
3. Search functionality
4. Database migration (SQLite/PostgreSQL)
5. Mobile app support

See [PHASE2_ROADMAP.md](PHASE2_ROADMAP.md) for full roadmap.

## 🤝 Contributing

This is a learning/demo project. Feel free to fork and experiment!

## 📝 License

MIT License - feel free to use for learning purposes.

---

**Built with:** Flask, Vanilla JavaScript, JSON  
**Last Updated:** 2025-11-25  
**Status:** Phase 1 Complete ✅

# notes-app
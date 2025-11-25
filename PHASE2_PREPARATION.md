# Phase 2 Preparation Guide

## Overview
The project is now restructured and ready for Phase 2 features. This guide outlines what needs to be done to implement the next set of features.

## Current State (Phase 1 ✅)

### Completed
- User authentication (register, login, logout)
- Notes CRUD operations
- Session management
- Input validation
- JSON file persistence
- Responsive UI with animations
- Clean modular architecture

### Limitations
- No database (using JSON)
- No user-specific notes
- No search functionality
- No rich text support
- No tags or categories
- No note sharing
- All notes are public

## Phase 2 Priority Features

### 1. Database Migration (Foundation)
**Why First:** Required for all other features

**Steps:**
1. Add SQLAlchemy to requirements.txt
2. Create `backend/models/database.py` for DB setup
3. Replace User model with SQLAlchemy User class
4. Replace Note model with SQLAlchemy Note class
5. Update database.py utilities to use SQLAlchemy
6. Create migration scripts
7. Update validators if needed

**Time Estimate:** 2-3 days

**Commands to Add:**
```bash
pip install flask-sqlalchemy
pip install flask-migrate
```

### 2. User-Specific Notes (Critical Fix)
**Why:** Currently all notes are shared globally

**Steps:**
1. Add `user_id` field to Note model
2. Update Note creation to include user
3. Filter notes by current user
4. Update API endpoints to check ownership
5. Add delete/edit permission checks

**Time Estimate:** 1-2 days

### 3. Rich Text / Markdown Support
**Why:** Users want formatted notes

**Steps:**
1. Add markdown2 to requirements
2. Update Note model to store markdown
3. Add markdown preview on frontend
4. Update editor UI
5. Add toggle between raw/preview

**Time Estimate:** 2-3 days

### 4. Tags & Categories
**Why:** Better note organization

**Steps:**
1. Create Tag model (SQLAlchemy)
2. Create Note-Tag relationship
3. Update Note model
4. Add tag endpoints
5. Frontend UI for tags
6. Filter notes by tag

**Time Estimate:** 2-3 days

### 5. Search Functionality
**Why:** Find notes quickly

**Steps:**
1. Add search endpoint `/api/notes/search?q=...`
2. Implement full-text search (or simple LIKE)
3. Frontend search bar
4. Display search results
5. Filter results by tag

**Time Estimate:** 1-2 days

## Implementation Order

```
Week 1:
├── Day 1-2: Database migration
├── Day 3: User-specific notes
└── Day 4-5: Testing & bug fixes

Week 2:
├── Day 1-2: Rich text support
├── Day 3: Tags & categories
└── Day 4-5: Search functionality

Week 3:
├── Day 1-2: UI improvements
├── Day 3: Performance optimization
└── Day 4-5: Testing & documentation
```

## Technology Stack for Phase 2

### Backend Additions
```python
flask-sqlalchemy>=3.0.0    # ORM
flask-migrate>=4.0.0       # Database migrations
markdown2>=2.4.0           # Markdown support
sqlalchemy>=2.0.0          # SQL toolkit
psycopg2-binary>=2.9.0     # PostgreSQL driver (optional)
```

### Frontend Additions (Optional)
```
markdown-it.min.js         # Markdown renderer
marked.js                  # Alternative renderer
highlight.js               # Code syntax highlighting
```

## File Structure After Phase 2

```
backend/
├── models/
│   ├── user.py (SQLAlchemy)
│   ├── note.py (SQLAlchemy)
│   ├── tag.py (NEW)
│   └── database.py (NEW)
├── routes/
│   ├── auth.py (updated for DB)
│   ├── notes.py (with search, user filtering)
│   └── tags.py (NEW)
├── migrations/ (NEW)
│   ├── versions/
│   └── env.py
└── utils/
    ├── search.py (NEW)
    └── markdown_utils.py (NEW)
```

## Database Schema Example

### Users Table
```sql
users:
  id INTEGER PRIMARY KEY
  username VARCHAR(20) UNIQUE
  password_hash VARCHAR(255)
  created_at TIMESTAMP
```

### Notes Table
```sql
notes:
  id VARCHAR(32) PRIMARY KEY
  user_id INTEGER FOREIGN KEY
  title VARCHAR(200)
  content TEXT
  created_at TIMESTAMP
  updated_at TIMESTAMP
```

### Tags Table
```sql
tags:
  id INTEGER PRIMARY KEY
  name VARCHAR(50)
  user_id INTEGER FOREIGN KEY
  created_at TIMESTAMP

note_tags:
  note_id VARCHAR(32) FOREIGN KEY
  tag_id INTEGER FOREIGN KEY
  PRIMARY KEY (note_id, tag_id)
```

## Testing Strategy for Phase 2

1. **Unit Tests**
   - Test each model's methods
   - Test validators
   - Test utilities

2. **Integration Tests**
   - Test API endpoints
   - Test database operations
   - Test user permissions

3. **E2E Tests**
   - Test complete workflows
   - Test UI interactions
   - Test data persistence

## Performance Considerations

1. **Database Indexing**
   - Index user_id in notes table
   - Index created_at for sorting
   - Index title/content for search

2. **Caching**
   - Cache user's notes list
   - Cache tag list
   - Invalidate on changes

3. **Pagination**
   - Add limit/offset to API
   - Prevent loading all notes at once
   - Improve page load times

## Deployment Preparation

After Phase 2:
1. Add environment variables
2. Create production database
3. Set up migrations pipeline
4. Add logging
5. Add error tracking (Sentry)
6. Set up CI/CD
7. Add Docker support

## Testing Checklist for Phase 2

- [ ] Database migrations work
- [ ] User-specific notes work
- [ ] Search returns correct results
- [ ] Tags can be created and assigned
- [ ] Markdown renders correctly
- [ ] No permission bypass
- [ ] Performance acceptable
- [ ] All old features still work
- [ ] Documentation updated
- [ ] Deployment tested

## Resources & References

### Flask SQLAlchemy
- https://flask-sqlalchemy.palletsprojects.com/
- Quick Start guide

### Database Migrations
- https://flask-migrate.readthedocs.io/
- Alembic documentation

### Markdown Support
- https://python-markdown.github.io/
- markdown2 documentation

### Search Optimization
- PostgreSQL full-text search
- Elasticsearch (for advanced)

## Questions to Consider

1. Should old JSON data be migrated to DB?
2. Should we use PostgreSQL or SQLite initially?
3. Should tags be user-specific or global?
4. Should we implement search or full-text search?
5. Should we add pagination immediately?
6. Should we implement note versioning?

## Next Steps

1. ✅ Review this guide
2. ✅ Set up development environment
3. ✅ Install Phase 2 dependencies
4. ✅ Create database schema
5. ✅ Start implementing models
6. ✅ Test thoroughly
7. ✅ Update documentation

---

**Ready to start Phase 2!** 🚀

For detailed implementation, see individual feature documentation.

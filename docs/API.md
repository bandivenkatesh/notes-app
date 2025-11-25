# API Documentation

## Base URL
`http://localhost:5000/api`

## Authentication Routes (`/api/auth`)

### Register
**POST** `/auth/register`

Register a new user account.

**Request Body:**
```json
{
  "username": "john_doe",
  "password": "securepass123"
}
```

**Response (201):**
```json
{
  "username": "john_doe",
  "id": "abc123xyz"
}
```

**Errors:**
- `400` - Username required, password too short, username taken
- `400` - Invalid username format (only alphanumeric, -, _)

---

### Login
**POST** `/auth/login`

Authenticate user and create session.

**Request Body:**
```json
{
  "username": "john_doe",
  "password": "securepass123"
}
```

**Response (200):**
```json
{
  "username": "john_doe",
  "id": "abc123xyz"
}
```

**Errors:**
- `401` - Invalid username or password

---

### Logout
**POST** `/auth/logout`

Clear user session.

**Response (204):** No content

---

### Get Current User
**GET** `/auth/me`

Get information about authenticated user.

**Response (200):**
```json
{
  "username": "john_doe",
  "id": "abc123xyz",
  "created_at": "2025-11-25T09:30:00.000000Z"
}
```

**Errors:**
- `401` - Not authenticated

---

## Notes Routes (`/api/notes`)

### Get All Notes
**GET** `/notes`

Retrieve all notes (public endpoint).

**Response (200):**
```json
[
  {
    "id": "note123",
    "title": "My First Note",
    "content": "This is a note",
    "created_at": "2025-11-25T09:30:00.000000Z"
  }
]
```

---

### Create Note
**POST** `/notes`

Create a new note. **Requires authentication.**

**Request Body:**
```json
{
  "title": "My First Note",
  "content": "This is a note"
}
```

**Response (201):**
```json
{
  "id": "note123",
  "title": "My First Note",
  "content": "This is a note",
  "created_at": "2025-11-25T09:30:00.000000Z"
}
```

**Errors:**
- `400` - Title or content too long
- `400` - Title or content required
- `401` - Not authenticated

---

### Get Single Note
**GET** `/notes/<note_id>`

Retrieve a specific note.

**Response (200):**
```json
{
  "id": "note123",
  "title": "My First Note",
  "content": "This is a note",
  "created_at": "2025-11-25T09:30:00.000000Z"
}
```

**Errors:**
- `404` - Note not found

---

### Update Note
**PUT** `/notes/<note_id>`

Update an existing note. **Requires authentication.**

**Request Body:**
```json
{
  "title": "Updated Title",
  "content": "Updated content"
}
```

**Response (200):**
```json
{
  "id": "note123",
  "title": "Updated Title",
  "content": "Updated content",
  "created_at": "2025-11-25T09:30:00.000000Z",
  "updated_at": "2025-11-25T09:35:00.000000Z"
}
```

**Errors:**
- `400` - Invalid input
- `401` - Not authenticated
- `404` - Note not found

---

### Delete Note
**DELETE** `/notes/<note_id>`

Delete a note. **Requires authentication.**

**Response (204):** No content

**Errors:**
- `401` - Not authenticated
- `404` - Note not found

---

## Error Response Format

All errors follow this format:

```json
{
  "error": "Error message describing what went wrong"
}
```

## Authentication

Authentication is session-based. After successful login, a session cookie is set. Include this cookie in subsequent requests for protected endpoints.

Protected endpoints require the user to be logged in:
- `POST /notes` - Create note
- `PUT /notes/<id>` - Update note
- `DELETE /notes/<id>` - Delete note
- `GET /auth/me` - Get current user

## Validation Rules

### Username
- 3-20 characters
- Alphanumeric, hyphens, underscores only

### Password
- Minimum 6 characters
- Maximum 128 characters

### Note Title
- Maximum 200 characters

### Note Content
- Maximum 50,000 characters

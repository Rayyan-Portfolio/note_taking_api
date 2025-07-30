# 📝 Note Taking API – FastAPI Project

A clean, modular, and production-ready **Note Taking API** built with **FastAPI**, featuring:

- 🗂️ CRUD operations for Notes
- 🏷️ Tag support
- 🔐 Optional user authentication
- 🔍 Search and filter by tag
- 🐳 Dockerized with Alembic migrations
- 🚀 Live deployment on [Render](https://note-api-fastapi.onrender.com/docs)

---

## ✅ Features Completed

- [x] Create, Read, Update, Delete (CRUD) Notes
- [x] Support for tagging notes
- [x] Search notes by title/content
- [x] Filter notes by tag
- [x] Optional: User Registration & Login (with JWT auth)
- [x] Hashing passwords with Passlib (bcrypt)
- [x] SQLAlchemy ORM & Alembic for DB migrations
- [x] Dockerized application
- [x] Live deployment on Render (with SQLite for demo)

---

## ⚙️ Tech Stack

- FastAPI
- SQLite (can be swapped for PostgreSQL)
- SQLAlchemy + Alembic
- JWT (python-jose)
- Pydantic v2
- Docker
- Render for deployment

---

## 📂 Project Structure

```
note_api/
│
├── app/
│   ├── main.py               # FastAPI entrypoint
│   ├── crud/               # DB logic
│       └── note.py
│       └── tag.py
│       └── user.py
│   ├── database/           # DB config
│       └── session.py
│   ├── models/             # SQLAlchemy models
│       └── association.py
│       └── note.py
│       └── tag.py
│       └── user.py
│   ├── routes/
│       └── auth.py
│       └── note.py
│       └── tag.py
│   ├── schema/            # Pydantic schemas
│       └── note.py
│       └── tag.py
│       └── user.py
│   ├── utils/
│       └── token.py          # JWT utils
│       └── hashing.py
│
├── alembic/                  # DB migrations
├── .gitignore
├── .dockerignore
├── dockerfile
├── requirements.txt
├── entrypoint.sh
└── README.md
```

---

## 🚀 Live API

**Base URL:** `https://note-api-fastapi.onrender.com/docs`

**Swagger Docs:** [`/docs`](https://note-api-fastapi.onrender.com/docs)

---

## 🧪 Example API Usage

### 🔐 Register a user (optional)

```http
POST /register
{
  "username": "rayyan",
  "email": "rayyan@example.com",
  "password": "securepass"
}
```

### 🔐 Login (optional)

```http
POST /login
{
  "username": "rayyan",
  "password": "securepass"
}
```

Returns:

```json
{
  "access_token": "<jwt_token>"
}
```

Use `Authorization: Bearer <token>` in all note requests if auth is enabled.

---

### 📄 Create a Note

```http
POST /notes/
{
  "title": "Test Note",
  "content": "Hello World!",
  "tags": ["todo", "important"]
}
```

---

### 🔍 Search & Filter Notes

```http
GET /notes/?search=hello&tag=todo
```

---

### 📋 List All Notes

```http
GET /notes/
Authorization: Bearer <token>
```

Returns:

```json
[
  {
    "id": 1,
    "title": "Test Note",
    "content": "Hello World!",
    "tags": [
      { "id": 1, "name": "todo" },
      { "id": 2, "name": "important" }
    ],
    "owner_id": 1
  }
]
```

---

### 📄 Get a Single Note

```http
GET /notes/1
Authorization: Bearer <token>
```

Returns:

```json
{
  "id": 1,
  "title": "Test Note",
  "content": "Hello World!",
  "tags": [
    { "id": 1, "name": "todo" },
    { "id": 2, "name": "important" }
  ],
  "owner_id": 1
}
```

---

### ✏️ Update a Note

```http
PUT /notes/1
Authorization: Bearer <token>
{
  "title": "Updated Title",
  "content": "Updated content",
  "tags": ["urgent", "work"]
}
```

Returns:

```json
{
  "id": 1,
  "title": "Updated Title",
  "content": "Updated content",
  "tags": [
    { "id": 3, "name": "urgent" },
    { "id": 4, "name": "work" }
  ],
  "owner_id": 1
}
```

---

### 🗑️ Delete a Note

```http
DELETE /notes/1
Authorization: Bearer <token>
```

Returns:

```json
{
  "detail": "Note deleted successfully"
}
```

---

## 🛠️ Local Development

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/note-api.git
cd note-api
```

### 2. Create `.env` file

```env
SECRET_KEY=your_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 3. Install & Run

```bash
pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload
```

---

## 🐳 Docker Deployment

### 1. Build Image

```bash
docker build -t note-api .
```

### 2. Run Container

```bash
docker run -d -p 8000:8000 --env-file .env note-api
```

> ✅ App runs at `http://localhost:8000`

---

## ☁️ Deploy on Render (Live Hosting)

1. Go to [https://render.com](https://render.com)
2. Create a new **Web Service**
3. Connect to your GitHub repo
4. Set the following:
   - **Environment:** `Docker`
   - **Start command:** _(leave blank as `ENTRYPOINT` is set)_
   - Add `.env` secrets manually to Render's environment tab
5. Deploy

---

## 🧑‍💻 Author

**Ahmad Rayyan** – Python Backend Developer  
GitHub: [@rayyanportfolio](https://github.com/rayyanportfolio)

---

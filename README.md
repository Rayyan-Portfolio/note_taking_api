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
│   ├── main.py            # FastAPI entrypoint
│   ├── auth.py
│   ├── crud/              # DB logic
│       └── note.py
│       └── tag.py
│       └── user.py
│   ├── database/          # DB config
│       └── session.py
│   ├── models/            # SQLAlchemy models
│       └── association.py
│       └── note.py
│       └── tag.py
│       └── user.py
│   ├── routes/            # FastAPI routers for notes, auth
│       └── auth.py
│       └── note.py
│       └── tag.py
│   ├── schema/            # Pydantic schemas
│       └── note.py
│       └── tag.py
│       └── user.py
│   ├── utils/
│       └── token.py       # JWT utils
│       └── hashing.py
│
├── alembic/               # DB migrations
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

### 📋 List All Notes (no filters)

```http
GET /notes/?search=&tag=
```

---

### 📄 Get a Single Note

```http
GET /notes/1
```

---

### ✏️ Update a Note

```http
PUT /notes/1
{
  "title": "Updated Title",
  "content": "Updated content",
  "tags": ["urgent", "work"]
}
```

---

### 🗑️ Delete a Note

```http
DELETE /notes/1
```

---

## 🛠️ Local Development

### 1. Clone the repo

```bash
git clone https://github.com/Rayyan-Portfolio/note_taking_api.git
cd note_taking_api/note_api
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
alembic revision --autogenerate -m "Initial migration"  # Optional if not yet generated
alembic upgrade head
uvicorn app.main:app --reload
```

---

## 🐳 Docker Deployment

### 🔧 1. Build Image Locally

**On macOS with Apple Silicon (M1/M2 or later)/ Linux:**

```bash
docker build --platform=linux/amd64 -t note-api .
```

> ✅ Use `--platform=linux/amd64` on Apple Silicon to ensure compatibility with Render and most Linux-based servers.

**On macOS Intel / Windows :**

```bash
docker build -t note-api .
```

---

### ▶️ 2. Run the Container Locally

```bash
docker run -d -p 8000:8000 --env-file .env note-api
```

Then open: [http://localhost:8000](http://localhost:8000)

---

## ☁️ Deploy to Render (Live Hosting)

Go to [https://render.com](https://render.com) and:

### Option 1: **Connect GitHub Repo (Recommended for CI/CD)**

1. Click **"New Web Service"**.
2. Choose **"Web Service"** → connect your GitHub repo.
3. Choose **Environment**: `Docker`.
4. **Leave Start Command blank** (handled by `ENTRYPOINT`).
5. Go to **Environment** tab in Render and add:
   - `SECRET_KEY=your_secret_key`
   - `ACCESS_TOKEN_EXPIRE_MINUTES=30`
   - Any other variables from `.env`
6. Click **Deploy**.

### Option 2: **Deploy from Docker Hub (Prebuilt Image)**

1. Choose **“New Web Service”** > “Docker Image”.
2. Enter Docker image name (e.g. `rayyanportfolio/note-api`).
3. Set the region and instance type.
4. Add required env vars (`SECRET_KEY`,`PORT=XXXX` etc.).
5. Click **Deploy**.

> 🧠 This method is ideal if you’ve already pushed your image to [hub.docker.com](https://hub.docker.com).

---

## 🧑‍💻 Author

**Ahmad Rayyan** – Python Backend Developer  
GitHub: [@rayyanportfolio](https://github.com/Rayyan-Portfolio)

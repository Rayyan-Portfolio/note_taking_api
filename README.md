# 📘 Note Taking API – FastAPI Project

A simple Note Taking API built using **FastAPI** and **SQLite**, with SQLAlchemy and Alembic for ORM and migrations. Users can manage notes with many-to-many tags support. This project demonstrates clean, modular backend development using Python.

## 🚀 Features

- ✅ Create, Read, Update, Delete (CRUD) notes
- ✅ Each note includes `title`, `content`, and `tags`
- ✅ Many-to-many relationship between notes and tags
- ✅ Search notes by keyword (`?search=...`)
- ✅ Filter notes by tag (`?tag=...`)
- ✅ View a note with full tag details
- ✅ Built with FastAPI, SQLAlchemy, and Alembic
- ✅ SQLite for simplicity
- ⚙️ Auto-generated API docs using Swagger UI (`/docs`)

## 📁 Project Structure

```
note_api/
├── alembic/               # Alembic migrations
├── app/                   # Main FastAPI app (models, routes, CRUD)
├── notes.db               # SQLite database file
├── alembic.ini            # Alembic config
├── .env                   # Environment variables
└── requirements.txt       # Project dependencies
```

## ⚙️ Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/Rayyan-Portfolio/note_taking_api.git
   cd note_taking_api/note_api
   ```

2. **Create & activate virtual environment (recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate        # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**

   ```bash
   alembic upgrade head
   ```

5. **Start the FastAPI server**

   ```bash
   uvicorn app.main:app --reload
   ```

6. **Access API documentation**
   - Swagger UI: http://127.0.0.1:8000/docs
   - ReDoc: http://127.0.0.1:8000/redoc

---

## 🧪 Sample Endpoints

### ➕ Create a Note

```http
POST /notes/
```

```json
{
  "title": "My First Note",
  "content": "This is a sample note body.",
  "tags": ["work", "urgent"]
}
```

### 📄 List All Notes

```http
GET /notes/
```

### 🔍 Search Notes

```http
GET /notes?search=meeting
```

### 🏷️ Filter Notes by Tag

```http
GET /notes?tag=work
```

### 🔍 Combined Search and Filter

```http
GET /notes?search=meeting&tag=work
```

### 📄 Get Note by ID

```http
GET /notes/{id}
```

### ✏️ Update Note

```http
PUT /notes/{id}
```

```json
{
  "title": "Updated Title",
  "content": "Updated content.",
  "tags": ["updated", "important"]
}
```

### ❌ Delete Note

```http
DELETE /notes/{id}
```

### 🏷️ Get All Tags

```http
GET /tags/
```

---

## 📦 Tech Stack

- **FastAPI** – Web framework
- **SQLAlchemy** – ORM
- **Alembic** – Database migrations
- **Uvicorn** – ASGI server
- **SQLite** – Lightweight DB (local testing)
- **python-dotenv** – Environment variable loading

---

## ✅ Completed Core Tasks

- [x] Note CRUD operations
- [x] Tag management with many-to-many relationship
- [x] SQLite database with Alembic migrations
- [x] Modular project structure with separation of concerns
- [x] API documentation via FastAPI's Swagger UI
- [x] Retrieve notes with search (`?search=...`) and tag filter (`?tag=...`)
- [x] Retrieve individual note with full tag details

---

## 🧾 Optional Features Skipped

These were considered optional and **intentionally skipped**:

- Live deployment (e.g., Render, Heroku)

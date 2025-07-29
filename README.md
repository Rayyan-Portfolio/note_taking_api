# 📘 Note Taking API – FastAPI Project

A simple Note Taking API built using **FastAPI** and **SQLite** with SQLAlchemy and Alembic for ORM and migrations. Users can manage notes with many-to-many tags support. This project demonstrates clean, modular backend development using Python.

## 🚀 Features

- ✅ Create, Read, Update, Delete (CRUD) notes
- ✅ Each note includes `title`, `content`, and `tags`
- ✅ Many-to-many relationship between notes and tags
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

2. **Create & activate virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate   On Windows:venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations (if DB not created)**

   ```bash
   alembic upgrade head
   ```

5. **Start the server**

   ```bash
   uvicorn app.main:app --reload
   ```

6. **Access API docs**
   - Swagger UI: http://127.0.0.1:8000/docs
   - Redoc: http://127.0.0.1:8000/redoc

## 🧪 Sample Endpoints

### ➕ Create a Note

```json
POST /notes/
{
  "title": "My First Note",
  "content": "This is a sample note body.",
  "tags": ["work", "urgent"]
}
```

### 📄 Get All Notes

```
GET /notes/
```

### 🔍 Get Note by ID

```
GET /notes/{id}
```

### ✏️ Update Note

```json
PUT /notes/{id}
{
  "title": "Updated Title",
  "content": "Updated content.",
  "tags": ["updated", "important"]
}
```

### ❌ Delete Note

```
DELETE /notes/{id}
```

### 🏷️ Get All Tags

```
GET /tags/
```

## 📦 Tech Stack

- **FastAPI** – Web framework
- **SQLAlchemy** – ORM
- **Alembic** – Database migrations
- **Uvicorn** – ASGI server
- **SQLite** – Lightweight DB (local testing)
- **dotenv** – Environment variable loading

## ✅ Completed Core Tasks

- [x] Note CRUD operations
- [x] Tag management with many-to-many relationship
- [x] SQLite database with Alembic migrations
- [x] Modular structure with separation of concerns
- [x] API docs generated via FastAPI

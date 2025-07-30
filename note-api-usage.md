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

### 🔐 Login
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

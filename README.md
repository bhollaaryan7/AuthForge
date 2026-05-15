# AuthForge

AuthForge is a production-style backend API platform built with Django REST Framework and PostgreSQL.

The project demonstrates backend engineering concepts including authentication systems, secure API design, relational database modeling, scalable architecture patterns, and production-oriented API development.

---

# Features

## Authentication & Security
- JWT authentication (access + refresh tokens)
- Custom user model using email-based login
- Protected API endpoints
- User-specific data isolation
- Secure password hashing

## Notes API
- Full CRUD operations
- Pagination support
- Search functionality
- Tagging system
- User-scoped notes access

## Developer Experience
- Swagger/OpenAPI documentation
- Interactive API testing
- Versioned API structure (`/api/v1/`)
- Structured API responses

---

# Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- SimpleJWT
- drf-spectacular (OpenAPI/Swagger)

---

# Architecture

The project uses a modular monolith architecture.

Apps are separated by domain responsibility:

```text
apps/
├── accounts/
├── notes/
```

This structure was selected because it:
- keeps development simpler than microservices
- improves maintainability
- supports future scaling
- encourages clean separation of concerns

For deeper architectural decisions, see:

```text
ARCHITECTURE.md
```

---

# API Endpoints

## Authentication

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/v1/auth/register/` | Register user |
| POST | `/api/v1/auth/login/` | Obtain JWT tokens |
| POST | `/api/v1/auth/refresh/` | Refresh access token |
| GET | `/api/v1/auth/me/` | Current authenticated user |

---

## Notes

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/v1/notes/` | List notes |
| POST | `/api/v1/notes/` | Create note |
| GET | `/api/v1/notes/{id}/` | Retrieve note |
| PUT | `/api/v1/notes/{id}/` | Update note |
| DELETE | `/api/v1/notes/{id}/` | Delete note |

---

# Example Request

## Create Note

```http
POST /api/v1/notes/
Authorization: Bearer <access_token>
Content-Type: application/json
```

```json
{
  "title": "Gym",
  "content": "Push day routine",
  "tags": ["fitness", "health"]
}
```

---

# Running Locally

## 1. Clone repository

```bash
git clone <your-repository-url>
cd AuthForge
```

---

## 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure environment variables

Create `.env`

```env
DB_NAME=authforge
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
```

---

## 5. Run migrations

```bash
python manage.py migrate
```

---

## 6. Start development server

```bash
python manage.py runserver
```

---

# Swagger Documentation

Interactive API docs:

```text
/api/docs/
```

OpenAPI schema:

```text
/api/schema/
```

---

# Future Improvements

Potential future enhancements:
- Dockerization
- CI/CD pipelines
- Role-based access control (RBAC)
- Audit logging
- Redis caching
- Background task processing
- Kubernetes deployment

---

# Why This Project Exists

AuthForge was built to demonstrate:
- backend engineering competency
- API architecture design
- relational database modeling
- authentication systems
- production-style backend practices
- scalable application structure

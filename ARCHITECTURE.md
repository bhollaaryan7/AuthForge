# AuthForge

AuthForge is a production-style authentication and identity management backend platform built using Django, PostgreSQL, and Docker.

The project demonstrates backend engineering concepts including:

- JWT authentication
- Session management
- Role-based access control
- Audit logging
- Asynchronous task processing
- REST API architecture
- Production-ready deployment practices

## Why Django?

Django was chosen because it provides:

- Mature authentication tooling
- Strong ORM support
- Security-focused defaults
- Rapid backend development
- Scalability for startup environments

Django REST Framework was added for API development.

## Why PostgreSQL?

PostgreSQL was selected because it offers:

- ACID compliance
- Strong relational integrity
- Excellent indexing support
- Advanced querying capabilities
- JSON support for flexible metadata
- Production-grade reliability

## Architecture Style

The project uses a modular monolith architecture.

This approach was selected because:

- It keeps development simpler than microservices
- It reduces operational overhead
- It allows clean domain separation
- It can evolve into services later if needed

The system is separated into isolated Django apps:
- accounts
- users
- audit
- permissions

## Authentication Strategy

JWT authentication is used with:

- short-lived access tokens
- refresh tokens

This approach enables stateless authentication and improves scalability.

## Core Tables

### users
- id
- email
- password_hash
- created_at

### sessions
- id
- user_id
- refresh_token
- expires_at

### audit_logs
- id
- user_id
- action
- timestamp

## Security

The system includes:

- password hashing
- JWT authentication
- rate limiting
- CSRF protection
- secure environment variables
- account lockout protection

## Future Improvements

Potential future improvements include:

- Kubernetes deployment
- microservice extraction
- distributed caching
- event-driven architecture
- observability tooling

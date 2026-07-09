# AI Engineering Starter Kit

[![CI](https://github.com/Saifee16/ai-engineering-starter-kit/actions/workflows/ci.yml/badge.svg)](https://github.com/Saifee16/ai-engineering-starter-kit/actions/workflows/ci.yml)

A reusable FastAPI backend starter template for AI-powered applications.

It includes typed configuration, Gemini integration, structured AI output, SQLite/PostgreSQL-ready database configuration, centralized logging, exception handling, tests, Docker, CI, and Swagger documentation.

## Why This Repository Exists

AI prototypes often start as a single Python file and become difficult to maintain as routes, external model calls, configuration, database code, and error handling grow.

This starter kit provides a small layered backend architecture that can be reused for:

- AI assistants
- RAG backends
- Agent APIs
- AI SaaS products
- Extraction pipelines
- Classification APIs
- Internal AI tools

## Features

- FastAPI
- Pydantic Settings
- Environment-based configuration
- Typed API responses
- API versioning
- Gemini API integration
- Structured Gemini JSON output
- SQLite support
- PostgreSQL-ready SQLAlchemy configuration
- Centralized logging
- Global exception handling
- Health check endpoint
- Async HTTP endpoint tests
- Mocked Gemini tests
- Pytest coverage
- Ruff linting and formatting
- Docker
- Docker Compose with PostgreSQL
- GitHub Actions CI
- Dependabot
- Swagger/OpenAPI documentation

## Architecture

```text
HTTP Request
    |
    v
FastAPI Router
    |
    v
Pydantic Validation
    |
    v
Endpoint
    |
    v
Service Layer
    |
    +----> Gemini API
    |
    +----> Database
    |
    v
Typed Pydantic Response
    |
    v
JSON Response
```

The API layer handles HTTP concerns.

The schema layer defines validated input and output structures.

The service layer handles external AI logic.

The core layer contains application-wide infrastructure such as configuration, logging, and exceptions.

The database layer manages database connectivity.

## Project Structure

```text
ai-engineering-starter-kit/
|
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── workflows/
│   │   └── ci.yml
│   ├── dependabot.yml
│   └── PULL_REQUEST_TEMPLATE.md
|
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── endpoints/
│   │       │   ├── ai.py
│   │       │   └── health.py
│   │       └── router.py
│   ├── core/
│   │   ├── config.py
│   │   ├── exceptions.py
│   │   └── logging.py
│   ├── db/
│   │   ├── base.py
│   │   └── database.py
│   ├── schemas/
│   │   ├── ai.py
│   │   ├── common.py
│   │   └── health.py
│   ├── services/
│   │   └── gemini_service.py
│   └── main.py
|
├── tests/
│   ├── conftest.py
│   ├── test_ai.py
│   └── test_health.py
|
├── .dockerignore
├── .editorconfig
├── .env.example
├── .gitignore
├── .python-version
├── compose.yaml
├── CONTRIBUTING.md
├── Dockerfile
├── LICENSE
├── pyproject.toml
├── requirements-dev.txt
├── requirements.txt
├── README.md
└── SECURITY.md
```

## Requirements

- Python 3.12
- A Gemini API key
- Docker, optional
- PostgreSQL, optional

## Quick Start

Clone the repository:

```bash
git clone https://github.com/Saifee16/ai-engineering-starter-kit.git
cd ai-engineering-starter-kit
```

### Create a Virtual Environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

### Install Dependencies

For development:

```bash
pip install -r requirements-dev.txt
```

For runtime only:

```bash
pip install -r requirements.txt
```

### Create Environment Configuration

Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

macOS/Linux:

```bash
cp .env.example .env
```

Add your Gemini API key to `.env`:

```env
APP_NAME=AI Engineering Starter Kit
APP_ENV=local
APP_DEBUG=true
API_V1_PREFIX=/api/v1

LOG_LEVEL=INFO

DATABASE_URL=sqlite:///./app.db

GEMINI_API_KEY=your_real_gemini_api_key_here
GEMINI_MODEL=gemini-3.5-flash
```

Never commit `.env`.

## Run Locally

```bash
uvicorn app.main:app --reload
```

API:

```text
http://127.0.0.1:8000
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

## API Endpoints

### Health Check

```http
GET /api/v1/health
```

Example response:

```json
{
  "success": true,
  "data": {
    "status": "ok",
    "app": "AI Engineering Starter Kit",
    "environment": "local"
  }
}
```

### Chat

```http
POST /api/v1/chat
```

Request:

```json
{
  "message": "Explain FastAPI in one sentence."
}
```

Example response:

```json
{
  "success": true,
  "data": {
    "reply": "FastAPI is a Python framework for building modern APIs."
  }
}
```

### Structured AI Response

```http
POST /api/v1/structured
```

Request:

```json
{
  "topic": "FastAPI"
}
```

Example response:

```json
{
  "success": true,
  "data": {
    "title": "FastAPI",
    "summary": "FastAPI is a modern Python API framework.",
    "difficulty": "beginner"
  }
}
```

## Tests

Run all tests:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov=app --cov-report=term-missing
```

The test suite mocks Gemini and does not require live Gemini API requests.

## Code Quality

Check code:

```bash
ruff check .
```

Automatically fix safe lint issues:

```bash
ruff check . --fix
```

Format code:

```bash
ruff format .
```

Verify formatting:

```bash
ruff format --check .
```

## Docker

Build the image:

```bash
docker build -t ai-engineering-starter-kit .
```

Run with environment variables:

```bash
docker run --env-file .env -p 8000:8000 ai-engineering-starter-kit
```

Open:

```text
http://127.0.0.1:8000/docs
```

## Docker Compose with PostgreSQL

Create `.env` first.

Then run:

```bash
docker compose up --build
```

This starts:

- FastAPI
- PostgreSQL

The API container uses PostgreSQL through the internal Docker network.

Stop the services:

```bash
docker compose down
```

Remove containers and PostgreSQL volume data:

```bash
docker compose down -v
```

## Database Configuration

SQLite:

```env
DATABASE_URL=sqlite:///./app.db
```

PostgreSQL:

```env
DATABASE_URL=postgresql+psycopg://user:password@localhost:5432/ai_starter
```

The SQLAlchemy engine is created from `DATABASE_URL`.

## Continuous Integration

GitHub Actions runs on pushes and pull requests targeting `main`.

CI checks:

- Ruff linting
- Ruff formatting
- Pytest
- Test coverage generation
- Docker image build

## Using This Repository as a Starter

Create a repository from this template or clone it.

Then:

1. Change `APP_NAME`.
2. Replace or extend the AI schemas.
3. Add new endpoint modules.
4. Add service-layer integrations.
5. Add SQLAlchemy models as needed.
6. Add database migrations when your application begins changing table schemas.
7. Add authentication only when the application's requirements are defined.
8. Add application-specific tests.

Avoid putting business logic directly inside endpoint functions.

## Security

Never expose Gemini or database credentials in frontend code.

Never commit `.env`.

For security vulnerabilities, follow `SECURITY.md`.

## Contributing

See `CONTRIBUTING.md`.

## License

MIT License. See `LICENSE`.

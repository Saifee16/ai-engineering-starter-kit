# AI Engineering Starter Kit

A reusable FastAPI backend template for building AI-powered applications with Gemini, clean configuration, logging, exception handling, database setup, Docker, Swagger docs, and tests.

## Features

* FastAPI backend
* Pydantic settings
* `.env` based configuration
* SQLite/PostgreSQL database support
* Gemini API integration
* `/chat` AI endpoint
* `/structured` JSON AI endpoint
* Health check endpoint
* Centralized logging
* Custom exception handling
* Pytest test suite
* Docker support
* Swagger API docs

## Tech Stack

* Python 3.12
* FastAPI
* Pydantic Settings
* SQLAlchemy
* SQLite / PostgreSQL
* Google GenAI SDK
* Pytest
* Docker

## Project Structure

```txt
ai-engineering-starter-kit/
│
├── app/
│   ├── main.py
│   ├── api/
│   │   └── v1/
│   │       ├── router.py
│   │       └── endpoints/
│   │           ├── health.py
│   │           └── ai.py
│   ├── core/
│   │   ├── config.py
│   │   ├── logging.py
│   │   └── exceptions.py
│   ├── db/
│   │   ├── base.py
│   │   └── database.py
│   ├── schemas/
│   │   ├── common.py
│   │   └── ai.py
│   └── services/
│       └── gemini_service.py
│
├── tests/
│   ├── conftest.py
│   ├── test_health.py
│   └── test_ai.py
│
├── .env.example
├── .gitignore
├── Dockerfile
├── requirements.txt
├── requirements-dev.txt
└── README.md
```

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/ai-engineering-starter-kit.git
cd ai-engineering-starter-kit
```

### 2. Create virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
pip install -r requirements-dev.txt
```

### 4. Create `.env`

Copy `.env.example` to `.env`.

```powershell
copy .env.example .env
```

Then add your real Gemini API key:

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

Do not commit `.env` to GitHub.

## Run Locally

```powershell
uvicorn app.main:app --reload
```

API will run at:

```txt
http://127.0.0.1:8000
```

Swagger docs:

```txt
http://127.0.0.1:8000/docs
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

Response:

```json
{
  "success": true,
  "data": {
    "reply": "FastAPI is a Python framework for building fast, typed, automatically documented APIs."
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

Response:

```json
{
  "success": true,
  "data": {
    "title": "FastAPI",
    "summary": "FastAPI helps developers build modern APIs quickly using Python type hints.",
    "difficulty": "beginner"
  }
}
```

## Run Tests

```powershell
pytest
```

Expected:

```txt
4 passed
```

## Docker

### Build image

```powershell
docker build -t ai-engineering-starter-kit .
```

### Run without environment file

```powershell
docker run -p 8000:8000 ai-engineering-starter-kit
```

Health endpoint will work, but Gemini endpoints require an API key.

### Run with `.env`

```powershell
docker run --env-file .env -p 8000:8000 ai-engineering-starter-kit
```

Then open:

```txt
http://127.0.0.1:8000/docs
```

## Database

Default local database:

```env
DATABASE_URL=sqlite:///./app.db
```

PostgreSQL example:

```env
DATABASE_URL=postgresql+psycopg://user:password@localhost:5432/ai_starter
```

## GitHub Push

```powershell
git init
git add .
git commit -m "Initial AI engineering starter kit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ai-engineering-starter-kit.git
git push -u origin main
```

## Notes

* Keep `.env` private.
* Use `.env.example` as the public template.
* Do not call Gemini directly from the frontend.
* Use tests with fake services instead of real Gemini calls.
* Use Docker for consistent deployment.

# DevOps Todo API 🚀

A simple REST API for managing todos, built with **FastAPI** and **MySQL**, containerized with **Docker**, and deployed automatically to **AWS EC2** via **GitHub Actions CI/CD pipeline**.

## Architecture

```
GitHub (push to main)
    │
    ▼
GitHub Actions
    ├── CI: Run pytest
    └── CD: SSH → EC2 → docker-compose up
              │
              ▼
         AWS EC2
    ┌─────────────────┐
    │  Docker Compose  │
    │  ┌────────────┐  │
    │  │  FastAPI   │  │
    │  │  Backend   │  │
    │  └────────────┘  │
    │  ┌────────────┐  │
    │  │   MySQL    │  │
    │  │  Database  │  │
    │  └────────────┘  │
    └─────────────────┘
```

## Tech Stack

- **Backend** — Python + FastAPI
- **Database** — MySQL
- **Containerization** — Docker + Docker Compose
- **CI/CD** — GitHub Actions
- **Cloud** — AWS EC2

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| GET | `/todos` | Get all todos |
| POST | `/todos/{title}` | Add a new todo |
| DELETE | `/todos/{id}` | Delete a todo |

## CI/CD Pipeline

```
Push to main → Test (pytest) → Deploy to EC2
                   ↓ fail
               Stop here (no deploy)
```

## Run Locally

1. Clone the repo
```bash
git clone https://github.com/dxkillmy/DevOps-project.git
cd DevOps-project
```

2. Create `.env` file
```bash
cp .env.example .env
# แก้ค่าใน .env ตามต้องการ
```

3. Start with Docker Compose
```bash
docker-compose up -d
```

4. Open API docs at `http://localhost:8000/docs`

## Environment Variables

| Variable | Description |
|----------|-------------|
| `DB_HOST` | MySQL host |
| `DB_USER` | MySQL username |
| `DB_PASSWORD` | MySQL password |
| `DB_NAME` | Database name |
| `MYSQL_ROOT_PASSWORD` | MySQL root password |

> ⚠️ Never commit `.env` to GitHub

## Project Structure

```
DevOps-project/
├── .github/
│   └── workflows/
│       └── deploy.yml    # CI/CD pipeline
├── backend/
│   ├── main.py           # FastAPI app
│   ├── requirements.txt
│   ├── test_main.py      # pytest
│   └── Dockerfile
├── docker-compose.yml
├── .env.example
└── .gitignore
```


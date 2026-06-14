# 🚀 AI-Day1 – DevEnv Pro

## 📌 Project Overview

DevEnv Pro is a Dockerized FastAPI backend application built as part of an AI Engineering learning journey.

The project demonstrates how modern backend systems are developed using:

* FastAPI
* Supabase (PostgreSQL)
* Docker
* Docker Compose
* Redis
* Cloudflare Tunnel
* Git & GitHub Professional Workflow

---

## 🎯 Objectives

* Build a production-style backend API
* Connect FastAPI with a cloud database
* Containerize applications using Docker
* Use Redis as a supporting service
* Expose local applications securely using Cloudflare Tunnel
* Practice advanced Git workflows

---

## 🛠 Tech Stack

| Technology        | Purpose                    |
| ----------------- | -------------------------- |
| Python            | Backend Development        |
| FastAPI           | REST API Framework         |
| Supabase          | PostgreSQL Database        |
| Docker            | Containerization           |
| Docker Compose    | Multi-container Management |
| Redis             | In-Memory Data Store       |
| Cloudflare Tunnel | Public HTTPS Access        |
| Git & GitHub      | Version Control            |

---

## 📂 Project Structure

AI-Day1/

├── main.py

├── supabase_test.py

├── realtime_listener.py

├── async_race.py

├── Dockerfile

├── docker-compose.yml

├── requirements.txt

├── .env

├── .gitignore

└── README.md

---

## ⚡ API Endpoints

### Home Endpoint

GET /

Response:

{
"message": "Hello World"
}

---

### Health Check

GET /health

Response:

{
"status": "ok"
}

---

### Create User

POST /users

Request:

{
"email": "[user@example.com](mailto:user@example.com)"
}

Response:

{
"id": "uuid",
"email": "[user@example.com](mailto:user@example.com)"
}

---

### Get User By ID

GET /users/{id}

Response:

{
"id": "uuid",
"email": "[user@example.com](mailto:user@example.com)"
}

---

## 🗄 Database

Database Provider: Supabase PostgreSQL

Users Table:

| Column     | Type      |
| ---------- | --------- |
| id         | UUID      |
| email      | TEXT      |
| created_at | TIMESTAMP |

---

## 🔄 Realtime Listener

Implemented Supabase Realtime functionality.

Whenever a new user is added:

New user added: [user@example.com](mailto:user@example.com)

is printed automatically in the terminal.

---

## 🐳 Docker Setup

Build containers:

docker compose build

Run containers:

docker compose up -d

Stop containers:

docker compose down

---

## 🌐 Cloudflare Tunnel

Expose local FastAPI application publicly:

cloudflared tunnel --url http://localhost:8000

Example Public URL:

https://your-project.trycloudflare.com

Swagger Docs:

https://your-project.trycloudflare.com/docs

---

## 🏗 Architecture Diagram

```
            ┌─────────────┐
            │   Client    │
            └──────┬──────┘
                   │
                   ▼
          Cloudflare Tunnel
                   │
                   ▼
            FastAPI Backend
                   │
      ┌────────────┴────────────┐
      ▼                         ▼
Supabase DB                 Redis
```

---

## 📚 Day 1 Learning Outcomes

✅ FastAPI Fundamentals

✅ Docker & Docker Compose

✅ Supabase Integration

✅ Realtime Database Events

✅ Cloudflare Tunnel

✅ Git Workflow

✅ Branching Strategy

✅ Cherry Pick

✅ Interactive Rebase

✅ AI-Assisted Development

---

## 👨‍💻 Author

Mithula

AI Engineering Learning Journey – Day 1

# AI-Day1

A beginner backend project built using FastAPI, Docker, Supabase, and Cloudflare Tunnel.

## Features

* FastAPI REST API
* Health Check Endpoint
* Docker Containerization
* Supabase Database Integration
* Public Access using Cloudflare Tunnel

## Endpoints

### Home

GET /

Response:

```json
{
  "message": "Hello World"
}
```

### Health Check

GET /health

Response:

```json
{
  "status": "ok"
}
```

## Tech Stack

* Python
* FastAPI
* Docker
* Supabase
* Cloudflare Tunnel

## Run Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

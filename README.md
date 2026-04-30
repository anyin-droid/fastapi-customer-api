# Customer Management API

A simple backend API project built with FastAPI and SQLite.

## Features

- Create customer
- Get all customers
- Get customer by ID
- Update customer
- Delete customer
- 404 error handling
- Request data validation with Pydantic

## Tech Stack

- Python
- FastAPI
- SQLite
- Pydantic
- Swagger UI

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | /customers | Get all customers |
| GET | /customers/{id} | Get customer by ID |
| POST | /customers | Create customer |
| PUT | /customers/{id} | Update customer |
| DELETE | /customers/{id} | Delete customer |

## How to Run

```bash
pip install fastapi uvicorn pydantic
python -m uvicorn main:app --reload

if `app/main.py`
```bash
python -m uvicorn app.main:app --reload

Open Swagger UI:
http://127.0.0.1:8000/docs


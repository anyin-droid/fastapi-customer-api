# Customer Management API

A RESTful API built with FastAPI and SQLite to manage customer data.

---

## 🚀 Features

* Get all customers
* Get customer by ID
* Create new customer
* Update customer information
* Delete customer

---

## 🛠 Tech Stack

* Python
* FastAPI
* SQLite

---

## 📡 API Endpoints

| Method | Endpoint        | Description         |
| ------ | --------------- | ------------------- |
| GET    | /customers      | Get all customers   |
| GET    | /customers/{id} | Get single customer |
| POST   | /customers      | Create customer     |
| PUT    | /customers/{id} | Update customer     |
| DELETE | /customers/{id} | Delete customer     |

---

## ▶️ How to Run

```bash
pip install fastapi uvicorn
python -m uvicorn main:app --reload
```

Then open:

http://127.0.0.1:8000/docs

---

## 💡 Project Highlights

* Designed RESTful API structure
* Implemented full CRUD operations
* Integrated SQLite database
* Used Swagger UI for API testing

---

## 👨‍💻 Author

* Yu-Tang Liu


from fastapi import FastAPI
import sqlite3
app = FastAPI()

def init_db():
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT
    )
    """)
    conn.commit()
    conn.close()

init_db()

@app.get("/customers")
def get_customers():
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM customers")
    rows = cursor.fetchall()

    conn.close()

    return [
        {"id": r[0], "name": r[1], "email": r[2]}
        for r in rows
    ]
    
@app.post("/customers")
def create_customer(customer: dict):
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO customers (name, email) VALUES (?, ?)",
        (customer["name"], customer["email"])
    )

    conn.commit()
    conn.close()

    return {"message": "新增成功"}

@app.put("/customers/{id}")
def update_customer(id: int, customer: dict):
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE customers SET name = ?, email = ? WHERE id = ?",
        (customer.get("name"), customer.get("email"), id)
    )

    conn.commit()
    conn.close()

    return {"message": "更新成功"}

@app.delete("/customers/{id}")
def delete_customer(id: int):
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM customers WHERE id = ?",
        (id,)
    )

    conn.commit()
    conn.close()

    return {"message": "刪除成功"}

@app.get("/customers/{id}")
def get_customer(id: int):
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM customers WHERE id = ?",
        (id,)
    )
    row = cursor.fetchone()  

    conn.close()

    if row:
        return {"id": row[0], "name": row[1], "email": row[2]}
    else:
        return {"message": "找不到資料"}
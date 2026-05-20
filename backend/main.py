from fastapi import FastAPI
import mysql.connector
import os

app = FastAPI()

def get_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "password123"),
        database=os.getenv("DB_NAME", "tododb")
    )

def init_db():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS todos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL
        )
    """)
    db.commit()
    db.close()

@app.on_event("startup")
def startup():
    init_db()

@app.get("/")
def read_root():
    return {"message": "Hello from DevOps Project!"}

@app.get("/todos")
def get_todos():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM todos")
    todos = [{"id": row[0], "title": row[1]} for row in cursor.fetchall()]
    db.close()
    return todos

@app.post("/todos/{title}")
def add_todo(title: str):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO todos (title) VALUES (%s)", (title,))
    db.commit()
    db.close()
    return {"message": f"Added: {title}"}

@app.delete("/todos/{id}")
def delete_todo(id: int):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM todos WHERE id = %s", (id,))
    db.commit()
    db.close()
    return {"message": f"Deleted id: {id}"}

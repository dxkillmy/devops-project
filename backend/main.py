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

@app.get("/")
def read_root():
    return {"message": "Hello from DevOps Project!"}

@app.get("/health")
def health():
    try:
        db = get_db()
        db.close()
        return {"status": "ok", "database": "connected"}
    except Exception:
        return {"status": "ok", "database": "disconnected"}

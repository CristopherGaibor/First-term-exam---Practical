from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
import sqlite3

app = FastAPI(title="FuerzaDB")

def get_db():
    conn = sqlite3.connect("Fuerza.db", check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

db = get_db()
db.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        email TEXT,
        is_active BOOLEAN DEFAULT 1
    )
""")
db.commit()

class UserCreate(BaseModel):
    username: str
    password: str
    email: Optional[str] = None

class UserOut(BaseModel):
    id: int
    username: str
    email: Optional[str]
    is_active: bool

class LoginRequest(BaseModel):
    username: str
    password: str

@app.post("/users", response_model=UserOut)
def create_user(user: UserCreate):
    cursor = db.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
            (user.username, user.password, user.email)
        )
        db.commit()
        return {**user.dict(), "id": cursor.lastrow_id, "is_active": True}
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="El usuario ya existe")

@app.get("/users", response_model=List[UserOut])
def list_users():
    cursor = db.cursor()
    rows = cursor.execute("SELECT id, username, email, is_active FROM users").fetchall()
    return [dict(row) for row in rows]

@app.post("/login")
def login(req: LoginRequest):
    cursor = db.cursor()
    user = cursor.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?",
        (req.username, req.password)
    ).fetchone()
    
    if user:
        return {"status": "success", "message": "Login exitoso"}
    else:
        raise HTTPException(status_code=401, detail="Login fallido")

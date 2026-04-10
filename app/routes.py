import sqlite3
from fastapi import APIRouter
from models.note import NoteCreate, Note
from database.connection import get_db

router = APIRouter()

@router.get("/")
def home():
    return {"Massage": "API running"}


@router.post("/notes")
def create_note(newNote: NoteCreate):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO notes (title, description, status)
        VALUES (?, ?, ?)
    """, (newNote.title, newNote.description, newNote.status))

    conn.commit()
    conn.close()

    return {"Message": "Note Created"}


@router.get("/notes")
def get_all_notes():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
       SELECT * FROM notes            
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows
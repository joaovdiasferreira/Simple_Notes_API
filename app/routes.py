import sqlite3
from fastapi import APIRouter
from models.note import NoteCreate, Note, NoteResponse
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


@router.get("/notes", response_model=list[NoteResponse])
def get_all_notes():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
       SELECT * FROM notes            
    """)

    rows = cursor.fetchall()
    conn.close()

    notes = []
    for row in rows:
        notes.append(NoteResponse(
            id = row[0],
            title = row[1],
            description= row[2],
            status = row[3],
            created_at = row[4]
        ))

    return notes


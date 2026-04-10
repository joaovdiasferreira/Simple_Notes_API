from fastapi import APIRouter
from models.note import NoteCreate, NoteResponse
from database.connection import get_db

#starting router
router = APIRouter()

@router.get("/")    #Home route
def home():
    return {"Massage": "API running"}


@router.post("/notes")  #POST method to create notes
def create_note(new_note: NoteCreate):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO notes (title, description, status)
        VALUES (?, ?, ?)
    """, (new_note.title, new_note.description, new_note.status))

    conn.commit()
    conn.close()

    return {"Message": "Note Created"}


#GET method for getting all notes
@router.get("/notes", response_model=list[NoteResponse])
def get_all_notes(): # Return a list of objects of NoteResponse
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

#GET method for getting a single note by id
@router.get("/notes/{note_id}", response_model=NoteResponse)
def get_note(note_id: int): # Return an object of NoteResponse
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
                   SELECT * FROM notes WHERE id = ?
                   """, (note_id,))

    row = cursor.fetchone()
    conn.close()

    if row is None:
        return {"Error": "Note Not Found"}

    return NoteResponse(
        id = row[0],
        title = row[1],
        description = row[2],
        status = row[3],
        created_at = row[4]
    )

#DELETE method using note id
@router.delete("/notes/{note_id}")
def delete_note(note_id: int):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
                   DELETE FROM notes WHERE id = ?
                   """, (note_id,))
    conn.commit()
    conn.close()

    return {"Message": "Note Deleted, id: {}".format(note_id)}
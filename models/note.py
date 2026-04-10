from pydantic import BaseModel

class Note(BaseModel):
    """Simple Note Standard Model"""
    title: str
    description: str
    status: str


class NoteCreate(Note):
    """Create Note Model to POST method"""
    pass

class NoteResponse(BaseModel):
    """Response Model to GET methods"""
    id: int
    title: str
    description: str
    status: str
    created_at: str

def note_response(row: dict):
    if row is None:
        return None

    return NoteResponse(
        id=row[0],
        title=row[1],
        description=row[2],
        status=row[3],
        created_at=row[4],
    )
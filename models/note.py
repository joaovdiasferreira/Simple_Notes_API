from pydantic import BaseModel

class Note(BaseModel):
    title: str
    description: str
    status: str


class NoteCreate(Note):
    pass

class NoteResponse(BaseModel):
    id: int
    title: str
    description: str
    status: str
    created_at: str
from pydantic import BaseModel

class Note(BaseModel):
    title: str
    description: str
    status: str


class NoteCreate(Note):
    pass
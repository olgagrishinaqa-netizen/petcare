from datetime import date

from pydantic import BaseModel


class NoteCreate(BaseModel):
    text: str
    date: date


class NoteResponse(BaseModel):
    id: int
    pet_id: int
    text: str
    date: date

    class Config:
        from_attributes = True

from datetime import date

from pydantic import BaseModel


class ReminderCreate(BaseModel):
    title: str
    date: date
    note: str | None = None


class ReminderResponse(BaseModel):
    id: int
    pet_id: int
    title: str
    date: date
    note: str | None

    class Config:
        from_attributes = True

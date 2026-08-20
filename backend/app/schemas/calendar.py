from datetime import date

from pydantic import BaseModel


class CalendarEvent(BaseModel):
    id: int
    pet_id: int
    event_type: str
    title: str
    date: date
    note: str | None = None
    source_id: int

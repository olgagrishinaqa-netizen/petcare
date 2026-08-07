from datetime import date

from pydantic import BaseModel


class DewormingCreate(BaseModel):
    date: date
    drug: str
    note: str | None = None


class DewormingResponse(BaseModel):
    id: int
    pet_id: int
    date: date
    drug: str
    note: str | None = None

    class Config:
        from_attributes = True

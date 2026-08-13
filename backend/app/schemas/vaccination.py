from datetime import date

from pydantic import BaseModel


class VaccinationCreate(BaseModel):
    vaccine: str
    date: date
    next_date: date | None = None
    note: str | None = None


class VaccinationResponse(BaseModel):
    id: int
    pet_id: int
    vaccine: str
    date: date
    next_date: date | None
    note: str | None

    class Config:
        from_attributes = True

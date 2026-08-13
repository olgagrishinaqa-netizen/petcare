from datetime import date

from pydantic import BaseModel


class FleaTickTreatmentCreate(BaseModel):
    medicine: str
    date: date
    next_date: date | None = None
    note: str | None = None


class FleaTickTreatmentResponse(BaseModel):
    id: int
    pet_id: int
    medicine: str
    date: date
    next_date: date | None
    note: str | None

    class Config:
        from_attributes = True

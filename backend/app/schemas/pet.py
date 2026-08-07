from datetime import date

from pydantic import BaseModel


class PetCreate(BaseModel):
    name: str
    species: str
    breed: str
    birth_date: date
    weight: float


class PetResponse(BaseModel):
    id: int
    name: str
    species: str
    breed: str
    birth_date: date
    weight: float

    class Config:
        from_attributes = True

from sqlalchemy.orm import Session

from app.models.pet import Pet
from app.schemas.pet import PetCreate


def create_pet(db: Session, pet: PetCreate):

    db_pet = Pet(
        name=pet.name,
        species=pet.species,
        breed=pet.breed,
        birth_date=pet.birth_date,
        weight=pet.weight,
    )

    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)

    return db_pet


def get_pets(db: Session):
    return db.query(Pet).all()

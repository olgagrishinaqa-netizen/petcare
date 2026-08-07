from sqlalchemy.orm import Session

from app.models.deworming import Deworming
from app.schemas.deworming import DewormingCreate


def create_deworming(
    db: Session,
    pet_id: int,
    data: DewormingCreate
):
    deworming = Deworming(
        pet_id=pet_id,
        date=data.date,
        drug=data.drug,
        note=data.note
    )

    db.add(deworming)
    db.commit()
    db.refresh(deworming)

    return deworming


def get_pet_dewormings(
    db: Session,
    pet_id: int
):
    return (
        db.query(Deworming)
        .filter(Deworming.pet_id == pet_id)
        .all()
    )

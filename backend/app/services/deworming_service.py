from sqlalchemy.orm import Session

from app.models.deworming import Deworming
from app.schemas.deworming import DewormingCreate


def create_deworming(
    db: Session,
    pet_id: int,
    deworming: DewormingCreate
):
    db_deworming = Deworming(
        pet_id=pet_id,
        date=deworming.date,
        drug=deworming.drug,
        next_date=deworming.next_date,
        note=deworming.note,
    )

    db.add(db_deworming)
    db.commit()
    db.refresh(db_deworming)

    return db_deworming


def get_pet_dewormings(
    db: Session,
    pet_id: int
):
    return db.query(Deworming).filter(
        Deworming.pet_id == pet_id
    ).all()

from sqlalchemy.orm import Session

from app.models.flea_tick_treatment import FleaTickTreatment
from app.schemas.flea_tick_treatment import FleaTickTreatmentCreate


def create_flea_tick_treatment(
    db: Session,
    pet_id: int,
    treatment: FleaTickTreatmentCreate
):
    db_treatment = FleaTickTreatment(
        pet_id=pet_id,
        medicine=treatment.medicine,
        date=treatment.date,
        next_date=treatment.next_date,
        note=treatment.note
    )

    db.add(db_treatment)
    db.commit()
    db.refresh(db_treatment)

    return db_treatment


def get_pet_flea_tick_treatments(
    db: Session,
    pet_id: int
):
    return db.query(FleaTickTreatment).filter(
        FleaTickTreatment.pet_id == pet_id
    ).all()

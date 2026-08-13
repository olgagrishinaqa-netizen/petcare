from sqlalchemy.orm import Session

from app.models.vaccination import Vaccination
from app.schemas.vaccination import VaccinationCreate


def create_vaccination(
    db: Session,
    pet_id: int,
    vaccination: VaccinationCreate
):
    db_vaccination = Vaccination(
        pet_id=pet_id,
        vaccine=vaccination.vaccine,
        date=vaccination.date,
        next_date=vaccination.next_date,
        note=vaccination.note
    )

    db.add(db_vaccination)
    db.commit()
    db.refresh(db_vaccination)

    return db_vaccination


def get_pet_vaccinations(
    db: Session,
    pet_id: int
):
    return db.query(Vaccination).filter(
        Vaccination.pet_id == pet_id
    ).all()

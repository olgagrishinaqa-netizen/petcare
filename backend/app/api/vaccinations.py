from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.vaccination import (
    VaccinationCreate,
    VaccinationResponse,
)
from app.services.vaccination_service import (
    create_vaccination,
    get_pet_vaccinations,
)


router = APIRouter(
    prefix="/pets",
    tags=["Vaccinations"],
)


@router.post(
    "/{pet_id}/vaccinations",
    response_model=VaccinationResponse,
)
def add_vaccination(
    pet_id: int,
    data: VaccinationCreate,
    db: Session = Depends(get_db),
):
    return create_vaccination(
        db,
        pet_id,
        data,
    )


@router.get(
    "/{pet_id}/vaccinations",
    response_model=list[VaccinationResponse],
)
def list_vaccinations(
    pet_id: int,
    db: Session = Depends(get_db),
):
    return get_pet_vaccinations(
        db,
        pet_id,
    )

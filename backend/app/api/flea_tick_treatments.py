from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.flea_tick_treatment import (
    FleaTickTreatmentCreate,
    FleaTickTreatmentResponse,
)
from app.services.flea_tick_treatment_service import (
    create_flea_tick_treatment,
    get_pet_flea_tick_treatments,
)


router = APIRouter(
    prefix="/pets",
    tags=["Flea/Tick Treatments"],
)


@router.post(
    "/{pet_id}/flea-tick-treatments",
    response_model=FleaTickTreatmentResponse,
)
def add_flea_tick_treatment(
    pet_id: int,
    data: FleaTickTreatmentCreate,
    db: Session = Depends(get_db),
):
    return create_flea_tick_treatment(
        db,
        pet_id,
        data,
    )


@router.get(
    "/{pet_id}/flea-tick-treatments",
    response_model=list[FleaTickTreatmentResponse],
)
def list_flea_tick_treatments(
    pet_id: int,
    db: Session = Depends(get_db),
):
    return get_pet_flea_tick_treatments(
        db,
        pet_id,
    )

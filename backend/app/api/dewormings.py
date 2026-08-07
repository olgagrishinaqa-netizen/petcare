from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.schemas.deworming import (
    DewormingCreate,
    DewormingResponse
)

from app.services.deworming_service import (
    create_deworming,
    get_pet_dewormings
)


router = APIRouter(
    prefix="/pets",
    tags=["Dewormings"]
)


@router.post(
    "/{pet_id}/dewormings",
    response_model=DewormingResponse
)
def add_deworming(
    pet_id: int,
    data: DewormingCreate,
    db: Session = Depends(get_db)
):
    return create_deworming(
        db,
        pet_id,
        data
    )


@router.get(
    "/{pet_id}/dewormings",
    response_model=list[DewormingResponse]
)
def list_dewormings(
    pet_id: int,
    db: Session = Depends(get_db)
):
    return get_pet_dewormings(
        db,
        pet_id
    )

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.pet import PetCreate, PetResponse
from app.services.pet_service import create_pet, get_pets

router = APIRouter(
    prefix="/pets",
    tags=["Pets"],
)


@router.post("/", response_model=PetResponse)
def add_pet(
    pet: PetCreate,
    db: Session = Depends(get_db),
):
    return create_pet(db, pet)


@router.get("/", response_model=list[PetResponse])
def list_pets(
    db: Session = Depends(get_db),
):
    return get_pets(db)

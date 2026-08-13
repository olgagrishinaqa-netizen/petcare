from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.note import NoteCreate, NoteResponse
from app.services.note_service import create_note, get_pet_notes


router = APIRouter(
    prefix="/pets",
    tags=["Notes"],
)


@router.post(
    "/{pet_id}/notes",
    response_model=NoteResponse,
)
def add_note(
    pet_id: int,
    data: NoteCreate,
    db: Session = Depends(get_db),
):
    return create_note(
        db,
        pet_id,
        data,
    )


@router.get(
    "/{pet_id}/notes",
    response_model=list[NoteResponse],
)
def list_notes(
    pet_id: int,
    db: Session = Depends(get_db),
):
    return get_pet_notes(
        db,
        pet_id,
    )

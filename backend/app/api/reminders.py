from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.reminder import ReminderCreate, ReminderResponse
from app.services.reminder_service import (
    create_reminder,
    get_pet_reminders,
)
from app.services.reminder_generator import generate_reminders


router = APIRouter(
    prefix="/pets",
    tags=["Reminders"],
)


@router.post(
    "/{pet_id}/reminders",
    response_model=ReminderResponse,
)
def add_reminder(
    pet_id: int,
    data: ReminderCreate,
    db: Session = Depends(get_db),
):
    return create_reminder(
        db,
        pet_id,
        data,
    )


@router.get(
    "/{pet_id}/reminders",
    response_model=list[ReminderResponse],
)
def list_reminders(
    pet_id: int,
    db: Session = Depends(get_db),
):
    return get_pet_reminders(
        db,
        pet_id,
    )
@router.post(
    "/{pet_id}/reminders/generate",
    response_model=list[ReminderResponse],
)
def generate_pet_reminders(
    pet_id: int,
    days_before: int = Query(7, ge=1, le=365),
    db: Session = Depends(get_db),
):
    return generate_reminders(
        db=db,
        pet_id=pet_id,
        days_before=days_before,
    )

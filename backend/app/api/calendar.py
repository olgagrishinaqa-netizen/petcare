from datetime import date, timedelta

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.calendar import CalendarEvent
from app.services.calendar_service import get_pet_calendar


router = APIRouter(
    prefix="/pets",
    tags=["Calendar"],
)


@router.get(
    "/{pet_id}/calendar",
    response_model=list[CalendarEvent],
)
def get_calendar(
    pet_id: int,
    start_date: date = Query(...),
    end_date: date = Query(...),
    db: Session = Depends(get_db),
):
    return get_pet_calendar(
        db=db,
        pet_id=pet_id,
        start_date=start_date,
        end_date=end_date,
    )
@router.get(
    "/{pet_id}/calendar/upcoming",
    response_model=list[CalendarEvent],
)
def get_upcoming_events(
    pet_id: int,
    days: int = Query(30, ge=1, le=365),
    db: Session = Depends(get_db),
):
    start_date = date.today()
    end_date = start_date + timedelta(days=days)

    return get_pet_calendar(
        db=db,
        pet_id=pet_id,
        start_date=start_date,
        end_date=end_date,
    )

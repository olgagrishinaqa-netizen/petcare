from sqlalchemy.orm import Session

from app.models.reminder import Reminder
from app.schemas.reminder import ReminderCreate


def create_reminder(
    db: Session,
    pet_id: int,
    reminder: ReminderCreate,
):
    db_reminder = Reminder(
        pet_id=pet_id,
        title=reminder.title,
        date=reminder.date,
        note=reminder.note,
    )

    db.add(db_reminder)
    db.commit()
    db.refresh(db_reminder)

    return db_reminder


def get_pet_reminders(
    db: Session,
    pet_id: int,
):
    return db.query(Reminder).filter(
        Reminder.pet_id == pet_id
    ).order_by(Reminder.date).all()

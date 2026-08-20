from datetime import date, timedelta

from sqlalchemy.orm import Session

from app.models.deworming import Deworming
from app.models.flea_tick_treatment import FleaTickTreatment
from app.models.reminder import Reminder
from app.models.vaccination import Vaccination


def generate_reminders(
    db: Session,
    pet_id: int,
    days_before: int = 7,
):
    today = date.today()
    target_date = today + timedelta(days=days_before)

    created_reminders = []

    vaccinations = (
        db.query(Vaccination)
        .filter(
            Vaccination.pet_id == pet_id,
            Vaccination.next_date == target_date,
        )
        .all()
    )

    for vaccination in vaccinations:
        existing = (
            db.query(Reminder)
            .filter(
                Reminder.pet_id == pet_id,
                Reminder.date == target_date,
                Reminder.title
                == f"Вакцинация: {vaccination.vaccine}",
            )
            .first()
        )

        if existing is None:
            reminder = Reminder(
                pet_id=pet_id,
                title=f"Вакцинация: {vaccination.vaccine}",
                date=target_date,
                note="Через 7 дней",
            )

            db.add(reminder)
            created_reminders.append(reminder)

    dewormings = (
        db.query(Deworming)
        .filter(
            Deworming.pet_id == pet_id,
            Deworming.next_date == target_date,
        )
        .all()
    )

    for deworming in dewormings:
        existing = (
            db.query(Reminder)
            .filter(
                Reminder.pet_id == pet_id,
                Reminder.date == target_date,
                Reminder.title
                == f"Обработка от глистов: {deworming.medicine}",
            )
            .first()
        )

        if existing is None:
            reminder = Reminder(
                pet_id=pet_id,
                title=f"Обработка от глистов: {deworming.medicine}",
                date=target_date,
                note="Через 7 дней",
            )

            db.add(reminder)
            created_reminders.append(reminder)

    flea_treatments = (
        db.query(FleaTickTreatment)
        .filter(
            FleaTickTreatment.pet_id == pet_id,
            FleaTickTreatment.next_date == target_date,
        )
        .all()
    )

    for treatment in flea_treatments:
        existing = (
            db.query(Reminder)
            .filter(
                Reminder.pet_id == pet_id,
                Reminder.date == target_date,
                Reminder.title
                == f"Обработка от блох и клещей: {treatment.medicine}",
            )
            .first()
        )

        if existing is None:
            reminder = Reminder(
                pet_id=pet_id,
                title=(
                    f"Обработка от блох и клещей: "
                    f"{treatment.medicine}"
                ),
                date=target_date,
                note="Через 7 дней",
            )

            db.add(reminder)
            created_reminders.append(reminder)

    db.commit()

    for reminder in created_reminders:
        db.refresh(reminder)

    return created_reminders

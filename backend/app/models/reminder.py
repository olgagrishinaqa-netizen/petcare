from datetime import date

from sqlalchemy import Date, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class Reminder(Base):
    __tablename__ = "reminders"

    id: Mapped[int] = mapped_column(primary_key=True)

    pet_id: Mapped[int] = mapped_column(
        ForeignKey("pets.id")
    )

    title: Mapped[str] = mapped_column(
        String(200)
    )

    date: Mapped[date] = mapped_column(
        Date
    )

    note: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )

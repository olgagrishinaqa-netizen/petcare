from datetime import date

from sqlalchemy import Date, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class FleaTickTreatment(Base):
    __tablename__ = "flea_tick_treatments"

    id: Mapped[int] = mapped_column(primary_key=True)

    pet_id: Mapped[int] = mapped_column(
        ForeignKey("pets.id")
    )

    medicine: Mapped[str] = mapped_column(
        String(100)
    )

    date: Mapped[date] = mapped_column(
        Date
    )

    next_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True
    )

    note: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )

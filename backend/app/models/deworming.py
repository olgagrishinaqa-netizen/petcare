from datetime import date

from sqlalchemy import Date, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base


class Deworming(Base):
    __tablename__ = "dewormings"

    id: Mapped[int] = mapped_column(primary_key=True)

    pet_id: Mapped[int] = mapped_column(
        ForeignKey("pets.id")
    )

    date: Mapped[date] = mapped_column(Date)

    drug: Mapped[str] = mapped_column(
        String(100)
    )

    next_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True
    )

    note: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    pet = relationship(
        "Pet",
        back_populates="dewormings"
    )

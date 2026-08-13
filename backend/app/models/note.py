from datetime import date

from sqlalchemy import Date, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class Note(Base):
    __tablename__ = "notes"

    id: Mapped[int] = mapped_column(primary_key=True)

    pet_id: Mapped[int] = mapped_column(
        ForeignKey("pets.id")
    )

    text: Mapped[str] = mapped_column(
        String(1000)
    )

    date: Mapped[date] = mapped_column(
        Date
    )

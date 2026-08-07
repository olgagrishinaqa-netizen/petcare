from datetime import date

from sqlalchemy import Date, Float, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base
from sqlalchemy.orm import relationship


class Pet(Base):
    __tablename__ = "pets"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(100))

    species: Mapped[str] = mapped_column(String(50))

    breed: Mapped[str] = mapped_column(String(100))

    birth_date: Mapped[date] = mapped_column(Date)

    weight: Mapped[float] = mapped_column(Float)

    dewormings = relationship(
        "Deworming",
        back_populates="pet"
    )

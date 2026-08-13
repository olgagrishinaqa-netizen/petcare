from sqlalchemy.orm import Session

from app.models.note import Note
from app.schemas.note import NoteCreate


def create_note(
    db: Session,
    pet_id: int,
    note: NoteCreate
):
    db_note = Note(
        pet_id=pet_id,
        text=note.text,
        date=note.date
    )

    db.add(db_note)
    db.commit()
    db.refresh(db_note)

    return db_note


def get_pet_notes(
    db: Session,
    pet_id: int
):
    return db.query(Note).filter(
        Note.pet_id == pet_id
    ).all()

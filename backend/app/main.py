from fastapi import FastAPI

from app.db.database import Base, engine
from app.models.user import User
from app.api.users import router as users_router
from app.models.pet import Pet
from app.api.pets import router as pets_router
from app.api import dewormings
from app.api.dewormings import router as dewormings_router
from app.models.vaccination import Vaccination
from app.api.vaccinations import router as vaccinations_router
from app.models.flea_tick_treatment import FleaTickTreatment
from app.api.flea_tick_treatments import router as flea_tick_treatments_router
from app.models.note import Note
from app.api.notes import router as notes_router
from app.models.reminder import Reminder
from app.api.reminders import router as reminders_router
from app.api.calendar import router as calendar_router



Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="PetCare API"
)


app.include_router(users_router)
app.include_router(pets_router)
app.include_router(dewormings.router)
app.include_router(vaccinations_router)
app.include_router(flea_tick_treatments_router)
app.include_router(notes_router)
app.include_router(reminders_router)
app.include_router(calendar_router)

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "PetCare API"
    }

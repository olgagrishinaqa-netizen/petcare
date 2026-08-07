from fastapi import FastAPI

from app.db.database import Base, engine
from app.models.user import User
from app.api.users import router as users_router
from app.models.pet import Pet
from app.api.pets import router as pets_router
from app.api import dewormings


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="PetCare API"
)


app.include_router(users_router)
app.include_router(pets_router)
app.include_router(dewormings.router)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "PetCare API"
    }

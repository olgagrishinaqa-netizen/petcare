from datetime import date
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from app.main import app
from app.db.database import Base
from app.db.session import get_db
from app.models.pet import Pet

SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_get_pets():
    db = TestingSessionLocal()
    pet = Pet(
        name="Барсик",
        species="Кошка",
        breed="Британская",
        birth_date=date(2020, 5, 10),
        weight=5.2,
    )
    db.add(pet)
    db.commit()
    db.refresh(pet)
    db.close()

    response = client.get("/pets/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["name"] == "Барсик"
    assert data[0]["species"] == "Кошка"
    assert data[0]["breed"] == "Британская"
    assert data[0]["weight"] == 5.2

def test_add_pet():
    response = client.post(
        "/pets/",
        json={
            "name": "Рекс",
            "species": "Собака",
            "breed": "Овчарка",
            "birth_date": "2022-03-15",
            "weight": 14.5
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["id"] is not None
    assert data["name"] == "Рекс"
    assert data["species"] == "Собака"
    assert data["breed"] == "Овчарка"
    assert data["weight"] == 14.5

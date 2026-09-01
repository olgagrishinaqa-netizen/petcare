from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_get_pets():
    response = client.get("/pets/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_pet():
    pet_data = {
        "name": "Test Pet",
        "species": "dog",
        "breed": "Labrador",
        "birth_date": "2020-01-15",
        "weight": 25.5,
    }

    response = client.post("/pets/", json=pet_data)

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "Test Pet"
    assert data["species"] == "dog"
    assert data["breed"] == "Labrador"
    assert data["birth_date"] == "2020-01-15"
    assert data["weight"] == 25.5
    assert "id" in data

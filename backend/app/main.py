from fastapi import FastAPI

app = FastAPI(
    title="PetCare API",
    description="Assistant for pet owners",
    version="0.1.0"
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "PetCare API"
    }

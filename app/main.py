from fastapi import FastAPI, status

import app.models
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Kiosk Inventory API",
    description="REST API for managing inventory in a candy, beverage, and snack kiosk.",
    version="0.1.0",
)


@app.get("/")
def read_root():
    return {"message": "Kiosk Inventory API is running!"}


@app.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    """
    API health check endpoint.
    This verifies if service is running correctly.
    """
    return {"status": "healthy", "service": "Kiosk Inventory API", "version": "0.1.0"}

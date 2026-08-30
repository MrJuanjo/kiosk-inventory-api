from fastapi import FastAPI, status

app = FastAPI(
    title="Kiosk Inventory API",
    description="REST API for managing inventory in a candy, beverage, and snack kiosk.",
    version="0.1.0"
)

@app.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    """
    API health check endpoint.
    This verifies if service is running correctly.
    """
    return {
        "status": "healthy",
        "service": "Kiosk Inventory API",
        "version": "0.1.0"
    }
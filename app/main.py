import logging
from fastapi import FastAPI
from .api.v1.router import app_router

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

app = FastAPI(
    title="AI Prediction Service",
    version="1.0.0",
    description="A service that provides AI-based predictions via RESTful API.",
)

app.include_router(app_router, prefix="/api/v1")

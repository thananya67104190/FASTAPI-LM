# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a FastAPI-based ML model serving API that provides predictions for multiple domains (flight prices, depression screening, animal classification, and movie recommendations). The application serves pre-trained machine learning models via RESTful endpoints.

**Tech Stack:**
- FastAPI 0.115.0 - Web framework
- Uvicorn 0.30.6 - ASGI server
- TensorFlow ≥2.20.0 - Deep learning models
- scikit-learn ≥1.6.0 - Traditional ML models
- joblib ≥1.4.2 - Model serialization
- pandas ≥2.2.2, numpy ≥2.1.0 - Data processing

## Development Commands

**Run the development server:**
```bash
uvicorn app.main:app --reload
```

**Run with specific host/port:**
```bash
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

**Install dependencies:**
```bash
pip install -r requirements.txt
```

**Virtual environment:**
The project uses a Python virtual environment located in `./venv/`. Ensure it's activated before running commands:
```bash
source venv/bin/activate  # On macOS/Linux
```

## Project Structure

```
app/
├── main.py                      # FastAPI application entry point
├── api/
│   └── v1/
│       ├── router.py            # API router aggregator
│       └── recommend/           # Movie recommendation endpoint
│           ├── route.py         # FastAPI route definitions
│           ├── schema.py        # Pydantic validation models
│           └── service.py       # Business logic and model inference
├── models/                      # Pre-trained model files
│   ├── recommender.joblib       # Movie recommendation model
│   ├── flight_price.pkl         # Flight price prediction model (planned)
│   ├── depression_model.pt      # Depression screening model (planned)
│   └── animal_cnn.pt            # Animal classification CNN model (planned)
└── utils/                       # Utility functions (planned)
    ├── preprocess.py
    └── inference.py
```

## Architecture

**Entry Point & Routing:**
- `app/main.py` creates the FastAPI application instance
- `app/api/v1/router.py` aggregates all API routers
- All routes are prefixed with `/api/v1`
- Each domain (recommend, flight, depression, animal) has its own router

**Router Pattern:**
Each API endpoint follows a consistent three-file pattern:
- `route.py` - FastAPI route definitions and HTTP handlers
- `schema.py` - Pydantic models for request/response validation
- `service.py` - Business logic, model loading, and inference

**Model Loading:**
Models are loaded at module import time in `service.py` files using joblib for pickle files or torch/tensorflow for their respective formats.

**Current Implementation:**
- Movie recommendation endpoint at `/api/v1/recommend/recommend`
- Recommender model loaded from `app/models/recommender.joblib`

## API Endpoints

**POST /api/v1/recommend/recommend**
- Request: `{ query: str, type: str, top_k: int }`
- Response: `{ recommendations: [...] }`
- Tags: Recommendations

Access interactive API documentation at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Adding New Endpoints

To add a new prediction endpoint (e.g., flight price prediction):

1. Create domain directory: `app/api/v1/flight/`
2. Create three files following the pattern:
   - `route.py` - Define FastAPI routes
   - `schema.py` - Define Pydantic models
   - `service.py` - Load model and implement inference logic
3. Register router in `app/api/v1/router.py`:
   ```python
   from .flight.route import router as flight_router
   app_router.include_router(flight_router, prefix='/flight', tags=['Flight'])
   ```
4. Place trained model file in `app/models/`

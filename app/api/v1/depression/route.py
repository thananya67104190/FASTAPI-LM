from fastapi import APIRouter
from .service import get_depression
from .schema import DepressionRequest

router = APIRouter()

@router.post('/depression', tags=['Depression'])
def assess_depression(data: DepressionRequest):
    return {"message":"Thananya"}

@router.get('/depression/healthcheck', tags=['Depression'])
def health_check():
    return {"status":"ok"}

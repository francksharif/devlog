from fastapi import APIRouter
from app.config import get_settings 


settings = get_settings()
router = APIRouter()

@router.get("/health", tags=["health"])
async def health_check():
    return {
    "status": "healthy", 
    "version": settings.APP_VERSION
    }
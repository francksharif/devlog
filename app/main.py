from fastapi import FastAPI
from app.config import get_settings
from app.api.v1.routes import health


settings = get_settings()

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

app.include_router(health.router, prefix="/api/v1")

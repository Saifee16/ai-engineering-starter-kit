from fastapi import APIRouter

from app.core.config import get_settings
from app.schemas.common import SuccessResponse

router = APIRouter()
settings = get_settings()


@router.get("/health", response_model=SuccessResponse)
def health_check() -> SuccessResponse:
    return SuccessResponse(
        data={
            "status": "ok",
            "app": settings.app_name,
            "environment": settings.app_env,
        }
    )
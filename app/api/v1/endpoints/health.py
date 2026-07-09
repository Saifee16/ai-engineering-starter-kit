from fastapi import APIRouter

from app.core.config import get_settings
from app.schemas.common import SuccessResponse
from app.schemas.health import HealthData

router = APIRouter()
settings = get_settings()


@router.get("/health", response_model=SuccessResponse[HealthData])
def health_check() -> SuccessResponse[HealthData]:
    return SuccessResponse(
        data=HealthData(
            app=settings.app_name,
            environment=settings.app_env,
        )
    )

from fastapi import FastAPI

from app.api.v1.router import api_router
from app.core.config import get_settings
from app.core.exceptions import register_exception_handlers
from app.core.logging import get_logger, setup_logging

settings = get_settings()

setup_logging()
logger = get_logger(__name__)


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        debug=settings.app_debug,
        version="0.1.0",
    )

    register_exception_handlers(app)

    app.include_router(
        api_router,
        prefix=settings.api_v1_prefix,
    )

    logger.info("Application started: %s", settings.app_name)

    return app


app = create_app()
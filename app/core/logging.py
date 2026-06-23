import logging
import sys

from app.core.config import get_settings


def setup_logging() -> None:
    """
    Configure application-wide logging.

    This controls how logs look in the terminal.
    """

    settings = get_settings()

    logging.basicConfig(
        level=settings.log_level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )


def get_logger(name: str) -> logging.Logger:
    """
    Return a logger for a specific module/file.

    Example:
        logger = get_logger(__name__)
    """

    return logging.getLogger(name)
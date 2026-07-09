from fastapi import status
from google import genai

from app.core.config import get_settings
from app.core.exceptions import AppError
from app.core.logging import get_logger
from app.schemas.ai import StructuredData

logger = get_logger(__name__)


class GeminiService:
    def __init__(self) -> None:
        self.settings = get_settings()

        if not self.settings.gemini_api_key:
            raise AppError(
                message="Gemini API key is missing.",
                code="GEMINI_API_KEY_MISSING",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        self.client = genai.Client(api_key=self.settings.gemini_api_key)

    def chat(self, message: str) -> str:
        try:
            interaction = self.client.interactions.create(
                model=self.settings.gemini_model,
                input=message,
            )

            return interaction.output_text

        except Exception as exc:
            logger.exception("Gemini chat request failed")

            raise AppError(
                message="Gemini chat request failed.",
                code="GEMINI_CHAT_FAILED",
                status_code=status.HTTP_502_BAD_GATEWAY,
            ) from exc

    def structured_explanation(
        self,
        topic: str,
    ) -> StructuredData:
        prompt = (
            f"Explain this topic for a beginner: {topic}. "
            "Return a short title, a short summary, "
            "and difficulty level."
        )

        try:
            interaction = self.client.interactions.create(
                model=self.settings.gemini_model,
                input=prompt,
                response_format={
                    "type": "text",
                    "mime_type": "application/json",
                    "schema": StructuredData.model_json_schema(),
                },
            )

            return StructuredData.model_validate_json(interaction.output_text)

        except Exception as exc:
            logger.exception("Gemini structured request failed")

            raise AppError(
                message="Gemini structured request failed.",
                code="GEMINI_STRUCTURED_FAILED",
                status_code=status.HTTP_502_BAD_GATEWAY,
            ) from exc

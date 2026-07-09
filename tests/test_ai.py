import pytest
from httpx import AsyncClient

from app.schemas.ai import StructuredData


class FakeGeminiService:
    def chat(self, message: str) -> str:
        return f"Fake reply for: {message}"

    def structured_explanation(
        self,
        topic: str,
    ) -> StructuredData:
        return StructuredData(
            title=topic,
            summary=f"Fake summary for {topic}",
            difficulty="beginner",
        )


@pytest.mark.anyio
async def test_chat_endpoint(
    client: AsyncClient,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        "app.api.v1.endpoints.ai.GeminiService",
        FakeGeminiService,
    )

    response = await client.post(
        "/api/v1/chat",
        json={"message": "Explain FastAPI"},
    )

    assert response.status_code == 200

    body = response.json()

    assert body["success"] is True
    assert body["data"]["reply"] == ("Fake reply for: Explain FastAPI")


@pytest.mark.anyio
async def test_structured_endpoint(
    client: AsyncClient,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        "app.api.v1.endpoints.ai.GeminiService",
        FakeGeminiService,
    )

    response = await client.post(
        "/api/v1/structured",
        json={"topic": "FastAPI"},
    )

    assert response.status_code == 200

    body = response.json()

    assert body["success"] is True
    assert body["data"]["title"] == "FastAPI"
    assert body["data"]["summary"] == ("Fake summary for FastAPI")
    assert body["data"]["difficulty"] == "beginner"


@pytest.mark.anyio
async def test_chat_rejects_empty_message(
    client: AsyncClient,
) -> None:
    response = await client.post(
        "/api/v1/chat",
        json={"message": ""},
    )

    assert response.status_code == 422

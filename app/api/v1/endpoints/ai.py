from fastapi import APIRouter

from app.schemas.ai import ChatData, ChatRequest, StructuredRequest
from app.schemas.common import SuccessResponse
from app.services.gemini_service import GeminiService

router = APIRouter()


@router.post("/chat", response_model=SuccessResponse)
def chat(request: ChatRequest) -> SuccessResponse:
    service = GeminiService()
    reply = service.chat(request.message)

    return SuccessResponse(
        data=ChatData(reply=reply).model_dump()
    )


@router.post("/structured", response_model=SuccessResponse)
def structured(request: StructuredRequest) -> SuccessResponse:
    service = GeminiService()
    result = service.structured_explanation(request.topic)

    return SuccessResponse(
        data=result.model_dump()
    )
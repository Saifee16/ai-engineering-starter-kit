from fastapi import APIRouter

from app.schemas.ai import ChatData, ChatRequest, StructuredData, StructuredRequest
from app.schemas.common import SuccessResponse
from app.services.gemini_service import GeminiService

router = APIRouter()


@router.post("/chat", response_model=SuccessResponse[ChatData])
def chat(request: ChatRequest) -> SuccessResponse[ChatData]:
    service = GeminiService()
    reply = service.chat(request.message)

    return SuccessResponse(data=ChatData(reply=reply))


@router.post(
    "/structured",
    response_model=SuccessResponse[StructuredData],
)
def structured(
    request: StructuredRequest,
) -> SuccessResponse[StructuredData]:
    service = GeminiService()
    result = service.structured_explanation(request.topic)

    return SuccessResponse(data=result)

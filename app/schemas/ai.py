from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str = Field(
        min_length=1,
        max_length=4000,
        description="User message to send to the AI model.",
    )


class ChatData(BaseModel):
    reply: str


class StructuredRequest(BaseModel):
    topic: str = Field(
        min_length=1,
        max_length=500,
        description="Topic to generate a structured explanation for.",
    )


class StructuredData(BaseModel):
    title: str
    summary: str
    difficulty: str
from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI(
    title="DistriRAG Ingestion API",
    description="Asynchronous event-driven document ingestion pipeline.",
    version="0.1.0",
)


class HealthResponse(BaseModel):
    status: str
    version: str


@app.get(
    "/health/ready",
    response_model=HealthResponse,
    status_code=status.HTTP_200_OK,
    tags=["System"],
)
async def health_ready() -> HealthResponse:
    """
    Kubernetes-compatible readiness probe.
    Verifies that the API process can safely accept traffic.
    """
    return HealthResponse(status="ready", version="0.1.0")

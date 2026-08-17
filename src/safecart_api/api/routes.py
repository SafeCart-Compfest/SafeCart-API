from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from safecart_api.api.dependencies import get_ai_health_gateway
from safecart_api.infrastructure.ai import AIHealthGateway

router = APIRouter()


@router.get("/health")
def health() -> dict[str, str]:
    """Report process liveness without checking downstream services."""
    return {"status": "ok"}


@router.get("/ready")
def ready(
    ai_gateway: Annotated[AIHealthGateway, Depends(get_ai_health_gateway)],
) -> dict[str, str | dict[str, str]]:
    """Report readiness only while the private AI service is reachable."""
    if not ai_gateway.is_ready():
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="AI service is unavailable",
        )

    return {"status": "ready", "dependencies": {"ai": "ok"}}

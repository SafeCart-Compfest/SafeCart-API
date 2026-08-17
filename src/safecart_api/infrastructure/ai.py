from typing import Protocol

import httpx


class AIHealthGateway(Protocol):
    """Readiness contract for the private AI dependency."""

    def is_ready(self) -> bool: ...


class HttpAIHealthGateway:
    """HTTP adapter for the SafeCart AI process-health endpoint."""

    def __init__(self, base_url: str, timeout_seconds: float) -> None:
        self._health_url = f"{base_url.rstrip('/')}/health"
        self._timeout_seconds = timeout_seconds

    def is_ready(self) -> bool:
        try:
            response = httpx.get(self._health_url, timeout=self._timeout_seconds)
            payload = response.json()
        except (httpx.HTTPError, ValueError):
            return False

        return response.status_code == 200 and payload == {"status": "ok"}

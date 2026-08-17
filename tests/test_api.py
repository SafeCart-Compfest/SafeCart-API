from collections.abc import Iterator

import pytest
from fastapi.testclient import TestClient

from safecart_api.api.dependencies import get_ai_health_gateway
from safecart_api.infrastructure.ai import AIHealthGateway
from safecart_api.main import app


class StubAIHealthGateway:
    def __init__(self, ready: bool) -> None:
        self._ready = ready

    def is_ready(self) -> bool:
        return self._ready


@pytest.fixture
def client() -> Iterator[TestClient]:
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


def override_ai_gateway(gateway: AIHealthGateway) -> None:
    app.dependency_overrides[get_ai_health_gateway] = lambda: gateway


def test_health_does_not_check_dependencies(client: TestClient) -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_ready_when_ai_is_available(client: TestClient) -> None:
    override_ai_gateway(StubAIHealthGateway(ready=True))

    response = client.get("/ready")

    assert response.status_code == 200
    assert response.json() == {"status": "ready", "dependencies": {"ai": "ok"}}


def test_ready_returns_503_when_ai_is_unavailable(client: TestClient) -> None:
    override_ai_gateway(StubAIHealthGateway(ready=False))

    response = client.get("/ready")

    assert response.status_code == 503
    assert response.json() == {"detail": "AI service is unavailable"}

import httpx
from pytest import MonkeyPatch

from safecart_api.infrastructure.ai import HttpAIHealthGateway


def test_ai_gateway_accepts_expected_health_response(monkeypatch: MonkeyPatch) -> None:
    def get(url: str, timeout: float) -> httpx.Response:
        assert url == "http://ai:8001/health"
        assert timeout == 3.0
        return httpx.Response(200, json={"status": "ok"})

    monkeypatch.setattr(httpx, "get", get)

    assert HttpAIHealthGateway("http://ai:8001/", 3.0).is_ready()


def test_ai_gateway_rejects_invalid_payload(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        httpx,
        "get",
        lambda *_args, **_kwargs: httpx.Response(200, text="not-json"),
    )

    assert not HttpAIHealthGateway("http://ai:8001", 2.0).is_ready()


def test_ai_gateway_handles_transport_error(monkeypatch: MonkeyPatch) -> None:
    def fail(*_args: object, **_kwargs: object) -> httpx.Response:
        raise httpx.ConnectError("unavailable")

    monkeypatch.setattr(httpx, "get", fail)

    assert not HttpAIHealthGateway("http://ai:8001", 2.0).is_ready()

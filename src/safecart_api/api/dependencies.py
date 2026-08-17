from functools import lru_cache

from safecart_api.config import get_settings
from safecart_api.infrastructure.ai import AIHealthGateway, HttpAIHealthGateway


@lru_cache
def get_ai_health_gateway() -> AIHealthGateway:
    settings = get_settings()
    return HttpAIHealthGateway(settings.ai_base_url, settings.ai_timeout_seconds)

from fastapi import FastAPI

from safecart_api import __version__
from safecart_api.api.routes import router

app = FastAPI(
    title="SafeCart API",
    version=__version__,
    description="Public orchestration API for evidence-grounded listing assessment.",
)
app.include_router(router)

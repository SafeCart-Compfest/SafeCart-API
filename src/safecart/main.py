from fastapi import FastAPI

from safecart import __version__
from safecart.api.routes import router

app = FastAPI(
    title="SafeCart API",
    version=__version__,
    description="Evidence-grounded listing identity consistency assessment.",
)
app.include_router(router)

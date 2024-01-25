from fastapi import FastAPI
from config.settings import settings
from routers.api import router
from typing import Dict


app = FastAPI(
    debug=bool(settings.DEBUG),
    title=settings.TITLE,
)


app.include_router(router)


@app.get("/")
def root() -> Dict[str, str]:
    """
    Root endpoint to check the status of the application.

    Returns:
        Dict[str, str]: A dictionary indicating the status of the application.
    """
    return {"status": "ok"}

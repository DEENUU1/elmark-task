from fastapi import FastAPI
from config.settings import settings
from api import router


app = FastAPI(
    debug=bool(settings.DEBUG),
    title=settings.TITLE,
)


app.include_router(router)


@app.get("/")
def root():
    return {"status": "ok"}

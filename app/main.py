from fastapi import FastAPI
from config.settings import settings


app = FastAPI(
    debug=bool(settings.DEBUG),
    title=settings.TITLE,
)


@app.get("/")
def root():
    return {"status": "ok"}

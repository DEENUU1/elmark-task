from fastapi import FastAPI
from config.settings import settings
from routers import parts as parts_router


app = FastAPI(
    debug=bool(settings.DEBUG),
    title=settings.TITLE,
)


app.include_router(parts_router.router)


@app.get("/")
def root():
    return {"status": "ok"}

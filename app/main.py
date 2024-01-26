from fastapi import FastAPI
from config.settings import settings
from routers.api import router
from typing import Dict
from data.startup import category_load_startup_data, part_load_startup_data
from config.database import get_parts_collection


app = FastAPI(
    debug=bool(settings.DEBUG),
    title=settings.TITLE,
)


app.include_router(router)

get_parts_collection().create_index("serial_number", unique=True)


@app.get("/")
def root() -> Dict[str, str]:
    """
    Root endpoint to check the status of the application.

    Returns:
        Dict[str, str]: A dictionary indicating the status of the application.
    """
    return {"status": "ok"}


@app.on_event("startup")
def startup() -> None:
    """
    Load mock data into database
    """
    print("Load startup data")
    category_load_startup_data("./data/category.json")
    part_load_startup_data("./data/part.json")
    print("Startup data loaded")

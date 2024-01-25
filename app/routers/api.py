from fastapi import APIRouter

from routers.v1 import categories, parts

router = APIRouter(
    prefix="/api/v1"
)

router.include_router(categories.router)
router.include_router(parts.router)

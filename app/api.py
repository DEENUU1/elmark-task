from fastapi import APIRouter

from routers import categories, parts

router = APIRouter(
    prefix="/api/v1"
)

router.include_router(categories.router)
router.include_router(parts.router)

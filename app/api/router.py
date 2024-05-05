from fastapi import APIRouter

from app.api.controllers import berries

api_router = APIRouter()


api_router.include_router(
    berries.router,
    tags=["Berries"],
)

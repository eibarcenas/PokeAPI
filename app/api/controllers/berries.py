from fastapi import APIRouter, Depends, status

from app.api.schemas.berries import BerriesStats
from app.api.services.berries import BerriesService

router = APIRouter()


@router.get(
    "/allBerryStats",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {
            "description": "statistics on berries obtained successfully",
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "No statistics found",
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "description": "Internal server error",
        },
    },
)
async def get_all_berry_stats(
    service: BerriesService = Depends(BerriesService),
) -> BerriesStats:
    return await service.get_stats()

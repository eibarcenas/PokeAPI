from fastapi import APIRouter, status

router = APIRouter()


@router.get(
    "/allBerryStats",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {
            "description": "Driver information successfully retrieved",
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Driver not found",
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "description": "Internal server error",
        },
    },
)
async def get_driver():
    return 1

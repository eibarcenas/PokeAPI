import pytest
from fastapi import FastAPI
from httpx import AsyncClient

from app.api.services.berries import BerriesService
from app.core.exceptions.berries import BerryNotFound


async def test_get_all_berries_names_success(
    client: AsyncClient,
    app: FastAPI,
):
    service = BerriesService()
    result = await service._get_all_berries_names()
    assert result[:2] == ["cheri", "chesto"]


async def test_get_growth_time_success(
    client: AsyncClient,
    app: FastAPI,
):
    service = BerriesService()
    result = await service._get_growth_time("cheri")
    assert result == 3


async def test_get_growth_time_error(
    client: AsyncClient,
    app: FastAPI,
):
    service = BerriesService()
    with pytest.raises(BerryNotFound):
        await service._get_growth_time("duolingo")


async def test_get_stats(
    client: AsyncClient,
    app: FastAPI,
    mock_growth_time_response,
):
    url = app.url_path_for("get_all_berry_stats")

    response = await client.get(
        url,
    )
    result = response.json()

    assert response.status_code == mock_growth_time_response.status_code
    expected_keys = [
        "berries_names",
        "min_growth_time",
        "median_growth_time",
        "max_growth_time",
        "variance_growth_time",
        "mean_growth_time",
        "frequency_growth_time",
    ]
    for key in expected_keys:
        assert key in result

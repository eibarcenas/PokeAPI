from unittest.mock import MagicMock

import pytest
from httpx import Response

from app.api.services.berries import BerriesService


@pytest.fixture
def berries_service():
    return BerriesService()


@pytest.fixture
def mock_berries_names():
    return [
        "cheri",
        "chesto",
        "pecha",
        "rawst",
        "aspear",
        "leppa",
        "oran",
        "persim",
        "lum",
        "sitrus",
        "figy",
        "wiki",
        "mago",
        "aguav",
        "iapapa",
        "razz",
        "bluk",
        "nanab",
        "wepear",
        "pinap",
    ]


@pytest.fixture
def mock_growth_time_response():
    mock_response = MagicMock(spec=Response)
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "berries_names": [
            "cheri",
            "chesto",
        ],
        "min_growth_time": 2,
        "median_growth_time": 3.5,
        "max_growth_time": 12,
        "variance_growth_time": 5.778947368421052,
        "mean_growth_time": 4.1,
        "frequency_growth_time": {
            "2": 5,
            "3": 5,
            "4": 3,
            "5": 5,
            "8": 1,
            "12": 1,
        },
    }
    return mock_response

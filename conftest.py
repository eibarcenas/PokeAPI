from typing import Any

import pytest
from asgi_lifespan import LifespanManager
from fastapi import FastAPI
from httpx import ASGITransport, AsyncClient

from app.api.application import get_app
from app.tests import base_url

pytest_plugins = [
    "app.tests.fixtures.berries",
]


@pytest.fixture(scope="session")
def anyio_backend() -> str:
    """
    Backend for anyio pytest plugin.

    :return: backend name.
    """
    return "asyncio"


@pytest.fixture
def app() -> FastAPI:
    """
    Fixture for creating FastAPI app.

    :return: fastapi app with mocked dependencies.
    """
    application = get_app()
    return application  # noqa: WPS331


@pytest.fixture()
async def _app(app: FastAPI):
    async with LifespanManager(app) as manager:
        yield manager.app


@pytest.fixture
async def client(
    _app: FastAPI,
    anyio_backend: Any,
) -> AsyncClient:
    """
    Fixture that creates client for requesting server.

    :param fastapi_app: the application.
    :yield: client for the app.
    """
    # headers = {"Authorization": f"Bearer {token}"}
    async with AsyncClient(
        transport=ASGITransport(app=_app),
        base_url=base_url,
    ) as ac:
        yield ac

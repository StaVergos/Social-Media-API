from typing import AsyncGenerator, Generator

import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient

from socialmediaapi.main import app


@pytest.fixtures(scope="session")
def anyio_backend() -> str:
    return "asyncio"


@pytest.fixtures()
def client() -> Generator:
    yield TestClient(app)


@pytest.fixtures(autouse=True)
def db() -> Generator:
    yield None


@pytest.fixtures()
async def async_client() -> AsyncGenerator:
    async with AsyncClient(app=app, base_url=client.base_url) as ac:
        yield ac

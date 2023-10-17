import asyncio
from typing import AsyncGenerator, Generator, Any

import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.pool import NullPool

from core.models import DatabaseHelper, Base, db_helper
from core.config import settings
from main import app


test_db_helper = DatabaseHelper(
    url=settings.test_db_url,
    echo=False,
)


@pytest.fixture(scope="session")
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


# client = TestClient(app)


@pytest.fixture(scope="session")
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


@pytest.fixture(scope="session")
def async_session_test() -> AsyncSession:
    async_session = test_db_helper.session_dependency()
    yield async_session


@pytest.fixture(autouse=True, scope="session")
async def prepare_database():
    async with test_db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with test_db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope="function")
def client() -> Generator[TestClient, Any, None]:
    app.dependency_overrides[db_helper] = test_db_helper
    with TestClient(app) as clnt:
        yield clnt

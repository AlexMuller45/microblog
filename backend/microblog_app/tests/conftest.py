import asyncio

import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

import core
from core.models import DatabaseHelper, Base, db_helper, User, Tweet
from main import app


TEST_DB_URL = "postgresql+asyncpg://developer:admin@localhost:5432/microblog_db"
test_db_helper = DatabaseHelper(url=TEST_DB_URL, echo=False)
# app.dependency_overrides[core.models.db_helper] = test_db_helper


@pytest.fixture(scope="session")
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def ac() -> AsyncClient:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # app.dependency_overrides[core.models.db_helper] = test_db_helper
        yield ac


@pytest.fixture(scope="session")
async def test_session() -> AsyncSession:
    async with test_db_helper.engine.begin() as conn:
        async with AsyncSession(conn) as session:
            yield session


@pytest.fixture(autouse=True, scope="session")
async def prepare_database():
    async with test_db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    yield test_db_helper.engine

    async with test_db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope="function")
def test_client() -> TestClient:
    # app.dependency_overrides[db_helper] = test_db_helper
    with TestClient(app) as client:
        return client


@pytest.fixture()
async def user(test_session: AsyncSession):
    _user1: User = User(name="Test", api_key="test3")
    _user2: User = User(name="Test Testovich", api_key="test2")
    test_session.add_all([_user1, _user2])
    await test_session.commit()


@pytest.fixture
async def tweet(test_session: AsyncSession):
    content: str = "test test to add tweet"
    data = await test_session.scalars(select(User))
    user = data.first()

    tweet = Tweet(
        content=content,
        attachments=None,
        author_id=user.id,
        views=0,
    )

    test_session.add(tweet)
    await test_session.commit()

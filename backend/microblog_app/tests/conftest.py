import asyncio

import pytest

from httpx import AsyncClient
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

import core
from core.models import DatabaseHelper, Base, db_helper, User, Tweet, Like

from main import app


TEST_DB_URL = "postgresql+asyncpg://developer:admin@localhost:5432/microblog_db"
test_db_helper = DatabaseHelper(url=TEST_DB_URL, echo=False)


@pytest.fixture(scope="session")
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def test_session() -> AsyncSession:
    async with test_db_helper.engine.begin() as conn:
        async with AsyncSession(conn) as session:
            yield session


@pytest.fixture(scope="session")
async def ac(test_session) -> AsyncClient:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


# @pytest.fixture(autouse=True, scope="session")
# async def prepare_database():
#     async with test_db_helper.engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
#
#         yield
#
#         # await conn.run_sync(Base.metadata.drop_all)
#         # await asyncio.sleep(0.1)


@pytest.fixture
async def user(test_session: AsyncSession):
    _user: User = User(name="Like_69", api_key="test69")
    test_session.add(_user)
    await test_session.commit()

    yield
    await test_session.delete(_user)
    await test_session.commit()


@pytest.fixture
async def tweet(test_session: AsyncSession):
    content: str = "test test to add tweet"
    _user = await test_session.scalar(select(User).where(User.api_key == "test"))

    tweet = Tweet(
        content=content,
        attachments=None,
        author_id=_user.id,
        views=0,
    )

    test_session.add(tweet)
    await test_session.commit()
    await test_session.refresh(tweet)


async def get_tweet_id(test_session: AsyncSession):
    _tweet = (await test_session.scalars(select(Tweet))).first()

    return _tweet.id


async def get_tweet_id_through_like(test_session: AsyncSession):
    _like = (await test_session.scalars(select(Like))).first()

    return _like.tweet_id

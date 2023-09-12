from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from config import settings


engine = create_async_engine(settings.SQLALCHEMY_DATABASE_URI, echo=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def get_async_session():
    async with async_session() as session:
        yield session


class Base(DeclarativeBase):
    pass

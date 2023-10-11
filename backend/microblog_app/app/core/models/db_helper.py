"""Модуль управлением подключение к базе данных"""

from asyncio import current_task

from sqlalchemy.ext.asyncio import (AsyncSession, async_scoped_session,
                                    async_sessionmaker, create_async_engine)

from ..config import settings


class DatabaseHelper:
    """
    Вспомогательный класс для управления подключением к базе данных и сеансами.

    Этот класс предоставляет методы для создания и управления подключением к базе данных.
    а также получение и закрытие сеансов базы данных.

    Args:
        url (str): URL-адрес базы данных.
        echo (bool, optional): Вывод SQL на консоль. По умолчанию установлено значение «False».

    Attributes:
        engine: The SQLAlchemy async engine object.
        session_factory: The async session factory object.

    """

    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(
            url=url,
            echo=echo,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    def get_scoped_session(self):
        """
        Получение текущего сеанс.

        Returns:
            AsyncSession: Объект текущего сеанс.

        """
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )
        return session

    async def session_dependency(self) -> AsyncSession:
        """
        Функция зависимости для получения асинхронного сеанса.

        Yields:
            AsyncSession: Объект асинхронного сеанса.

        """
        async with self.session_factory() as session:
            yield session
            await session.close()

    async def scoped_session_dependency(self) -> AsyncSession:
        """
        Функция зависимостей для получения текущего асинхронного сеанса.

        Yields:
            AsyncSession: Объект асинхронного текущий сеанс.

        """
        session = self.get_scoped_session()
        yield session
        await session.close()


db_helper = DatabaseHelper(
    url=settings.db_url,
    echo=settings.db_echo,
)

"""Модуль аутентификации"""

from fastapi import Depends, HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from sqlalchemy import Select, select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse
from starlette.status import HTTP_403_FORBIDDEN

from core.models import User, db_helper

api_key_header = APIKeyHeader(name="api-key", auto_error=False)


async def check_user(
    session: db_helper.scoped_session_dependency = Depends(),
    api_key: str = Security(api_key_header),
) -> bool | JSONResponse:
    """
    Проверка, есть ли пользователь с таким ключем в ДБ.

     Args:
         session (db_helper.scoped_session_dependency): Зависимость сеанса базы данных.
         api_key (str): Ключ API для проверки.

     Returns:
         bool | JSONResponse: Возвращает True, если пользователь действителен,
         в противном случае выдается исключение HTTPException с кодом состояния 403.

    """

    stmt: Select = select(User).where(User.api_key == api_key)
    result: Result = await session.execute(stmt)
    user = result.scalar_one_or_none()

    if user:
        return True

    raise HTTPException(
        status_code=HTTP_403_FORBIDDEN, detail="Could not validate API KEY"
    )


async def get_user_id(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
    api_key: str = Security(api_key_header),
) -> int | JSONResponse:
    """
    Получение идентификатор пользователя по API-ключу.

    Args:
        session (AsyncSession): Зависимость асинхронного сеанса базы данных.
        api_key (str): Ключ API.

    Returns:
        int | JSONResponse: Возвращает идентификатор пользователя, если пользователь найден,
        в противном случае выдается исключение HTTPException с кодом состояния 403.

    """

    stmt: Select = select(User).where(User.api_key == api_key)
    result: Result = await session.execute(stmt)
    user = result.scalar_one_or_none()

    if user:
        return int(user.id)

    raise HTTPException(
        status_code=HTTP_403_FORBIDDEN, detail="Could not validate API KEY"
    )


async def get_user(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
    api_key: str = Security(api_key_header),
) -> User | JSONResponse:
    """
    Получение пользователя по API-ключу.

    Args:
        session (AsyncSession): Зависимость асинхронного сеанса базы данных.
        api_key (str): Ключ API.

    Returns:
        User | JSONResponse: Возвращает пользователя, если он найден,
        в противном случае вызывает HTTPException с кодом состояния 403.

    """

    stmt: Select = select(User).where(User.api_key == api_key)
    result: Result = await session.execute(stmt)
    user = result.scalar_one_or_none()
    if user:
        return user

    raise HTTPException(
        status_code=HTTP_403_FORBIDDEN, detail="Could not validate API KEY"
    )

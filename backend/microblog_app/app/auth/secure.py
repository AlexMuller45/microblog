import json
from typing import Optional

from fastapi import Depends, HTTPException, Security, Response
from fastapi.security.api_key import APIKeyHeader
from sqlalchemy import select
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
    stmt = select(User).where(User.api_key == api_key)
    result: Result = await session.execute(stmt)
    user = result.scalar_one_or_none()

    if user:
        return True

    response = JSONResponse(
        content={
            "result": False,
            "error_type": "HTTP_403_FORBIDDEN",
            "error_message": "Could not validate API KEY",
        },
        status_code=HTTP_403_FORBIDDEN,
    )
    return response


async def get_user_id(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
    api_key: str = Depends(api_key_header),
) -> int | JSONResponse:
    stmt = select(User).where(User.api_key == api_key)
    result: Result = await session.execute(stmt)
    user = result.scalar_one_or_none()

    if user:
        return int(user.id)

    response = JSONResponse(
        content={
            "result": False,
            "error_type": "HTTP_403_FORBIDDEN",
            "error_message": "Could not validate API KEY",
        },
        status_code=HTTP_403_FORBIDDEN,
    )
    return response


async def get_user(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
    api_key: str = Security(api_key_header),
) -> User | JSONResponse:
    stmt = select(User).where(User.api_key == api_key)
    result: Result = await session.execute(stmt)
    user = result.scalar_one_or_none()
    if user:
        return user

    response = JSONResponse(
        content={
            "result": False,
            "error_type": "HTTP_403_FORBIDDEN",
            "error_message": "Could not validate API KEY",
        },
        status_code=HTTP_403_FORBIDDEN,
    )
    return response

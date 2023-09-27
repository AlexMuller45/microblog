import json
from typing import Optional

from fastapi import Depends, HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse
from starlette.status import HTTP_403_FORBIDDEN, HTTP_404_NOT_FOUND

from core.models import User, db_helper

api_key_header = APIKeyHeader(name="api-key", auto_error=False)


async def check_user(
    session: db_helper.scoped_session_dependency = Depends(),
    api_key: str = Security(api_key_header),
) -> bool | JSONResponse:
    stmt = select(User).where(User.api_key == api_key)
    result: Result = await session.execute(stmt)
    user = result.scalars().one_or_none()

    if user:
        return True

    response_json: json = {
        "result": False,
        "error_type": "HTTP_403_FORBIDDEN",
        "error_message": "Could not validate API KEY",
    }
    return JSONResponse(content=response_json)


async def get_user_id(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
    api_key: str = Security(api_key_header),
) -> int | JSONResponse:
    stmt = select(User.id).where(User.api_key == api_key)
    result: Result = await session.execute(stmt)
    user_id = result.scalars().one_or_none()

    if user_id:
        return int(user_id)

    response_json: json = {
        "result": False,
        "error_type": "HTTP_404_NOT_FOUND",
        "error_message": "User not found",
    }
    return JSONResponse(content=response_json)


async def get_user(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
    api_key: str = Security(api_key_header),
) -> User:
    stmt = select(User).where(User.api_key == api_key)
    result: Result = await session.execute(stmt)
    user = result.scalars().one()
    return user

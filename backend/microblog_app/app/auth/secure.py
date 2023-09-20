from typing import Optional

from fastapi import Depends, HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_403_FORBIDDEN

from core.models import User, db_helper

api_key_header = APIKeyHeader(name="api-key", auto_error=False)


async def check_user(
    session: AsyncSession = Depends(db_helper.session_dependency),
    api_key: str = Security(api_key_header),
) -> Optional[User]:
    stmt = select(User).where(User.api_key == api_key)
    result: Result = await session.execute(stmt)
    user = result.scalars().one_or_none()

    if user:
        return User(**user)

    raise HTTPException(
        status_code=HTTP_403_FORBIDDEN, detail="Could not validate API KEY"
    )

import json
from typing import Annotated, List

from fastapi import Path, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from auth.secure import get_user_id
from core.models import db_helper, Follow, User
from . import crud


async def get_follow_by_user_id(
    follow_user_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Follow | JSONResponse:
    current_user_id = await get_user_id(session=session)
    follow = await crud.get_follow(
        session=session, user_id=current_user_id, follow_user_id=follow_user_id
    )
    if follow:
        return follow

    response_json: json = jsonable_encoder(
        {
            "result": False,
            "error_type": "HTTP_404_NOT_FOUND",
            "error_message": "The subscription is not found",
        }
    )
    return JSONResponse(content=response_json)


async def get_user_by_id(
    user_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> User | JSONResponse:
    user = await crud.get_user(session=session, user_id=user_id)
    if user:
        return user

    response_json: json = jsonable_encoder(
        {
            "result": False,
            "error_type": "HTTP_404_NOT_FOUND",
            "error_message": f"The user #ID[{user_id}] is not found",
        }
    )
    return JSONResponse(content=response_json)


async def get_follower(
    user_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> List[User] | JSONResponse:
    followers = await crud.get_followers(session=session, user_id=user_id)
    if followers:
        return followers

    response_json: json = jsonable_encoder(
        {
            "result": False,
            "error_type": "HTTP_404_NOT_FOUND",
            "error_message": "Followers not found",
        }
    )
    return JSONResponse(content=response_json)


async def get_following(
    user_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> List[User] | JSONResponse:
    following = await crud.get_following(session=session, user_id=user_id)
    if following:
        return following

    response_json: json = jsonable_encoder(
        {
            "result": False,
            "error_type": "HTTP_404_NOT_FOUND",
            "error_message": "The subscription is not found",
        }
    )
    return JSONResponse(content=response_json)

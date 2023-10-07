from sqlalchemy import Select, Result, select
from sqlalchemy.ext.asyncio import AsyncSession


from auth.secure import get_user, get_user_id
from core.models import Like


async def add_like(
    session: AsyncSession, tweet_id: int, api_key: str
) -> dict[str, bool]:
    current_user = await get_user(session=session, api_key=api_key)

    like = Like(
        name=current_user.name,
        user_id=current_user.id,
        tweet_id=tweet_id,
    )

    session.add(like)
    await session.commit()

    return {"result": True}


async def get_like_by_tweet_id(session: AsyncSession, tweet_id, api_key: str) -> Like:
    current_user_id = await get_user_id(session=session, api_key=api_key)

    stmt: Select = (
        select(Like)
        .where(Like.tweet_id == tweet_id)
        .where(Like.user_id == current_user_id)
    )
    result: Result = await session.execute(stmt)
    like: Like = result.scalar_one_or_none()

    return like


async def delete_like(session: AsyncSession, like: Like) -> dict[str, bool]:
    await session.delete(like)
    await session.commit()

    return {"result": True}

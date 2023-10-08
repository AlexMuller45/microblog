from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Tweet


def get_attachments(data: List[int] | None) -> List[str] | None:
    if data:
        return list(map(str, data))
    return


def hide_api_key_tweet(data: list[Tweet]) -> List[Tweet]:
    for item in data:
        item.author.api_key = "*" * 12
    return data

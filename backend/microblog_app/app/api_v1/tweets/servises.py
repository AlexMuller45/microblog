from typing import List

from sqlalchemy.ext.asyncio import AsyncSession


def get_attachments(data: List[int] | None) -> List[str] | None:
    if data:
        return list(map(str, data))
    return

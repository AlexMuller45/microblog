"""Валидация данных для Tweet"""

from typing import List, Optional

from pydantic import BaseModel, ConfigDict

from api_v1.likes.schemas import Like
from api_v1.users.schemas import User


class TweetBase(BaseModel):
    """Базовая схема твита"""

    id: int
    content: str
    attachments: Optional[List[str]] = []
    author: User
    likes: Optional[List[Like]] = []


class Tweet(BaseModel):
    """Схема ответа для списка твитов"""

    result: bool = True
    tweets: List[TweetBase]


class TweetCreate(BaseModel):
    """Схема ответа для создания твита"""

    result: bool = True
    tweet_id: int


class TweetIn(BaseModel):
    """Схема для проверки входящих данных"""

    tweet_data: str
    tweet_media_ids: Optional[List[int]] = None


class TweetDelete(BaseModel):
    """Схема ответа при удвлении твита"""

    result: bool = True

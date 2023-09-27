from typing import List, Optional

from pydantic import BaseModel, ConfigDict

from api_v1.likes.schemas import Like
from api_v1.users.schemas import User


class TweetBase(BaseModel):
    id: int
    content: str
    attachments: Optional[List[str]]
    author: User
    likes: List[Like]


class Tweet(BaseModel):
    result: bool = True
    tweets: List[TweetBase]


class TweetCreate(BaseModel):
    result: bool = True
    tweet_id: int


class TweetIn(BaseModel):
    tweet_data: str
    tweet_media_ids: Optional[List[int]]


class TweetDelete(BaseModel):
    result: bool = True

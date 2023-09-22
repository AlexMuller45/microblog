from typing import List, Optional

from pydantic import BaseModel, ConfigDict


class TweetBase(BaseModel):
    tweet_data: str
    tweet_media_ids: Optional[List[int]]


class Tweet(TweetBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class TweetCreate(BaseModel):
    result: bool = True
    tweet_id: int


class TweetDelete(BaseModel):
    result: bool = True

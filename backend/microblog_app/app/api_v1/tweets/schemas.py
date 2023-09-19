from pydantic import BaseModel, ConfigDict
from typing import List, Optional


class TweetBase(BaseModel):
    tweet_data: str
    tweet_media_ids: Optional[List[int]]


class Tweet(TweetBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class TweetResponse(BaseModel):
    result: bool = True
    tweet_id: int

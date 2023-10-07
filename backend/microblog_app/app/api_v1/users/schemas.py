from typing import List, Optional

from pydantic import BaseModel, Field, computed_field


class UserBase(BaseModel):
    name: str
    # api_key: str = Field(exclude=True)


class User(UserBase):
    id: int


class Followers(BaseModel):
    followers: List[User]


class Following(BaseModel):
    following: List[User]


class UserInfo(User):
    followers: List[User]


class UserData(BaseModel):
    result: bool = True
    user: UserInfo
    following: List[User]


class UserResponse(BaseModel):
    result: bool = True


class FollowAdd(UserResponse):
    ...

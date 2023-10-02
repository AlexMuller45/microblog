from typing import List, Optional

from pydantic import BaseModel, Field


class UserBase(BaseModel):
    name: str
    api_key: str

    class Config:
        exclude = {"api_key"}


class User(UserBase):
    id: int

    class Config:
        exclude = {"api_key"}


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

    class Config:
        exclude = {"api_key"}


class UserResponse(BaseModel):
    result: bool = True


class FollowAdd(UserResponse):
    ...


class FollowDelete(UserResponse):
    ...

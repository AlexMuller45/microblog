from typing import List, Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    name: str


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


class FollowDelete(UserResponse):
    ...

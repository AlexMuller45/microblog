from pydantic import BaseModel


class LikeResponse(BaseModel):
    result: bool = True


class LikeAdd(LikeResponse):
    ...


class LikeDelete(LikeResponse):
    ...

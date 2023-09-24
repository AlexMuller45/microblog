from pydantic import BaseModel


class MediaAdd(BaseModel):
    result: bool = True
    media_id: int

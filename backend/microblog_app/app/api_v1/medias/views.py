import imghdr
import aiofiles
from fastapi import APIRouter, Depends, File, UploadFile, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from core.models import db_helper

from . import crud

router = APIRouter(tags=["Medias"])


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
)
async def add_media(
    in_file: UploadFile = File(...),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    if not in_file:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="No file sent"
        )
    if not imghdr.what(in_file.file):
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail="The file is not an image",
        )

    media_id: int = await crud.add_media(session=session, file_name=in_file.filename)
    file_path = f"{settings.media_path}/{media_id}__{in_file.filename}"

    async with aiofiles.open(file_path, "wb") as out_file:
        await out_file.write(in_file.file.read())

    return {"result": True, "media_id": media_id}

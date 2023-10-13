"""Роуты для Media"""

import imghdr
import os
import shutil

import aiofiles
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from fastapi.responses import FileResponse
from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from core.models import db_helper

from . import crud
from .schemas import MediaAdd

router = APIRouter(tags=["Medias"])


@router.get(
    "/{image_name}",
    status_code=status.HTTP_200_OK,
)
def get_image(image_name: str) -> FileResponse:
    """
    Отправка файла на фронтэнд.

    Args:
        image_name (str): название испрашиваемого файла.

    Returns:
        FileResponse

    Raises:
        HTTPException: Если файл не найден.

    """
    full_path = f"{settings.media_path}/{image_name}"

    if os.path.isfile(full_path):
        return FileResponse(full_path)

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="File not found",
    )


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=MediaAdd,
)
async def add_media(
    file: UploadFile = File(...),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    """
    Добавление имени файла в БД, присвоение ID, сохранение файла на сервер

    Args:
        file (UploadFile): Входящий файл.
        session (AsyncSession): Асинхронный сеанс SQLAlchemy.

    Returns:
        dict: {"result": True, "media_id": media_id}.

    Raises:
        HTTPException: Если файл не отправлен или файл не является изображением.

    """

    if not file:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="No file sent"
        )
    if not imghdr.what(file.file):
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail="The file is not an image",
        )

    media_id: int = await crud.add_media(session=session, file_name=file.filename)
    file_path = f"{settings.media_path}/{settings.filename.format(media_id=media_id, in_file_name=file.filename)}"

    async with aiofiles.open(file_path, "wb") as out_file:
        content = await file.read()
        await out_file.write(content)
        # shutil.copyfileobj(in_file.file, out_file)

    return {"result": True, "media_id": media_id}

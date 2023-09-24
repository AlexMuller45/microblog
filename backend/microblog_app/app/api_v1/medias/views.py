import aiofiles
import imghdr
import json

from fastapi import APIRouter, Depends, File, UploadFile
from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from core.config import settings
from core.models import db_helper

from . import crud
from .schemas import MediaAdd

router = APIRouter(tags=["Medias"])


@router.post("/", response_model=MediaAdd)
async def add_media(
    file: UploadFile = File(...),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    if not imghdr.what(file.filename):
        response_json: json = jsonable_encoder(
            {
                "result": False,
                "error_type": "HTTP_415_UNSUPPORTED_MEDIA_TYPE",
                "error_message": "The file is not an image",
            }
        )
        return JSONResponse(content=response_json)

    media_id: int = await crud.add_media(session=session, file_name=file.filename)
    file_path = f"{settings.media_path}/{media_id}"

    async with aiofiles.open(file_path, "wb") as out_file:
        content = await file.read()
        await out_file.write(content)

    response_json: json = jsonable_encoder({"result": True, "media_id": media_id})
    return JSONResponse(content=response_json)

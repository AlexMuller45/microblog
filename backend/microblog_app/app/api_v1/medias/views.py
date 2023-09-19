from fastapi import APIRouter, UploadFile, File

router = APIRouter(tags=["Medias"])


@router.post("/")
async def add_media(file: UploadFile = File(...)):
    content = await file.read()

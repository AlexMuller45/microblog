from fastapi import APIRouter

router = APIRouter(
    prefix="/api/medias",
    tags=["Medias"],
)


@router.post("/")
def add_media():
    ...

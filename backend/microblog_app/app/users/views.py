from fastapi import APIRouter

router = APIRouter(
    prefix="/api/users",
    tags=["Users"],
)


@router.post("/{idx}/follow")
def add_follow(idx: int):
    ...


@router.delete("/{idx}/follow")
def delete_follow(idx: int):
    ...


@router.get("/me")
def get_me():
    ...


@router.get("/{idx}")
def get_user_by_id(idx: int):
    ...

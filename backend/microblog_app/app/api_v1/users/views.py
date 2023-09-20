from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from auth.secure import check_user
from core.models import User, db_helper

router = APIRouter(tags=["Users"])


@router.post("/{idx}/follow")
def add_follow(idx: int, session: AsyncSession = Depends(db_helper.session_dependency)):
    ...


@router.delete("/{idx}/follow")
def delete_follow(
    idx: int, session: AsyncSession = Depends(db_helper.session_dependency)
):
    ...


@router.get("/me")
def get_me(
    session: AsyncSession = Depends(db_helper.session_dependency),
    user: User = Depends(check_user),
):
    ...


@router.get("/{idx}")
def get_user_by_id(
    idx: int, session: AsyncSession = Depends(db_helper.session_dependency)
):
    ...

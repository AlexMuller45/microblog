from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper

router = APIRouter(tags=["Likes"])


@router.post("/{idx}/like")
def add_like(idx: int):
    ...


@router.delete("/{idx}/like")
def delete_like(idx: int):
    ...

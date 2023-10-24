from fastapi import APIRouter, Depends

from auth.secure import check_user

from .medias.views import router as medias_router
from .tweets.views import router as tweets_router
from .users.views import router as users_router

router = APIRouter()
router.include_router(
    router=tweets_router, prefix="/tweets", dependencies=[Depends(check_user)]
)
router.include_router(router=medias_router, prefix="/medias")
router.include_router(router=users_router, prefix="/users")

# from typing import List

from fastapi import Depends, FastAPI

# from sqlalchemy.ext.asyncio import AsyncSession

from api_v1 import router as router_v1
from auth.secure import check_user
from core.config import settings

# from core.models import User, db_helper
# from fill_db import get_users

app = FastAPI()
app.include_router(
    router_v1, prefix=settings.api_v1_prefix, dependencies=[Depends(check_user)]
)


@app.get("/")
def index():
    return {"message": "Hello world!"}


# @app.post("/fill_users_tab")
# async def process_users(session: AsyncSession = Depends(db_helper.session_dependency)):
#     users: List[User] = await get_users()
#
#     session.add_all(users)
#     await session.commit()
#
#     return {
#         "result": True,
#         "message": "Users processed successfully",
#         "status_code": 201,
#     }

# from typing import List

from fastapi import Depends, FastAPI, HTTPException, status, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

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
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_methods=["POST", "GET", "DELETE"],
#     allow_headers=["*"],
# )


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "result": False,
            "error_type": exc.status_code,
            "error_message": str(exc.detail),
        },
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS,
        content={
            "result": False,
            "error_type": status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS,
            "error_message": exc.errors(),
        },
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

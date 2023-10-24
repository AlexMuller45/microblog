""" Основной модуль """

from fastapi import FastAPI, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from api_v1 import router as router_v1
from core.config import settings

app = FastAPI()
app.include_router(router_v1, prefix=settings.api_v1_prefix)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins,
    allow_credentials=True,
    allow_methods=settings.all_methods,
    allow_headers="*",
)


# Переопределение ответов на ошибки
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
    """Тестовый эндпоинт"""
    return {"message": "Hello world!"}

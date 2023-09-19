from fastapi import FastAPI

from api_v1 import router as router_v1
from core.config import settings

app = FastAPI()
app.include_router(router_v1, prefix=settings.api_v1_prefix)


@app.get("/")
def index():
    return {"message": "Hello world!"}

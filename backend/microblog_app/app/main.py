from fastapi import Depends, FastAPI

from api_v1 import router as router_v1
from auth.secure import check_user
from core.config import settings

app = FastAPI()
app.include_router(
    router_v1, prefix=settings.api_v1_prefix, dependencies=[Depends(check_user)]
)


@app.get("/")
def index():
    return {"message": "Hello world!"}

from fastapi import FastAPI

from tweets.views import router as tweets_router
from medias.views import router as medias_router
from users.views import router as users_router


app = FastAPI()
app.include_router(tweets_router)
app.include_router(medias_router)
app.include_router(users_router)


@app.get("/")
def index():
    return {"message": "Hello world!"}

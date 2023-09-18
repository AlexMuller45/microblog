from fastapi import APIRouter

router = APIRouter(
    prefix="/api/tweets",
    tags=["Tweets"],
)


@router.post("/")
def add_tweet():
    ...


@router.delete("/{idx}")
def delete_tweet(idx: int):
    ...


@router.post("/{idx}/like")
def add_like(idx: int):
    ...


@router.delete("/{idx}/like")
def delete_like(idx: int):
    ...


@router.get("/")
def get_tweets():
    ...

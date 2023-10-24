#!/bin/sh

alembic upgrade head

#uvicorn main:app --reload --host 0.0.0.0 --port 5500

gunicorn main:app --worker 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:5500

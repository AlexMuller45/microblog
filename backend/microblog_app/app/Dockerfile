FROM python:3.10-slim-bullseye

RUN pip3 install --upgrade pip
RUN pip3 install --upgrade poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false
RUN poetry install --no-root


COPY ../app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5500"]
FROM tiangolo/uvicorn-gunicorn:python3.10

RUN mkdir /microblog_app
WORKDIR /microblog_app

RUN pip3 install --upgrade pip
RUN pip3 install --upgrade poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false
RUN poetry install --no-root

COPY . .

WORKDIR /microblog_app/app


#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5500"]

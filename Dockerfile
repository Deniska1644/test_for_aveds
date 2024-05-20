FROM python:3.12

RUN mkdir /fastapi_app

WORKDIR /fastapi_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

WORKDIR /fastapi_app/src

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"] && ['alembic','upgrade','head']



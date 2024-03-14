FROM python:3-slim as base

RUN apt-get update

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY ./app ./app

WORKDIR /app


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONBUFFERED=1

WORKDIR /code

COPY requirements.txt ./requirements.txt

RUN  pip install --upgrade pip && pip install -r requirements.txt

COPY . /code/


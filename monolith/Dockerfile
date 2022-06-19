# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY ./requirement.txt /code/
RUN pip install --upgrade pip
RUN pip install -r /code/requirement.txt
COPY . /code/

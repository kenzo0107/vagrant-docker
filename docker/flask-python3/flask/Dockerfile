FROM python:3.6.1-alpine
MAINTAINER Kenzo Tanaka

EXPOSE 5000

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

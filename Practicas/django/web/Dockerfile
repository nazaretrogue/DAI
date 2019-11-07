FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1

# Creating working directory inside container
RUN mkdir /web
COPY . /web

WORKDIR /web
RUN pip3 install -r requirements.txt

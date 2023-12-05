FROM python:3.10-slim
ENV PYTHONUNBUFFERED 1

# App setup
ADD . /code
WORKDIR /code

# Requirements installation
RUN pip install -r requirements.txt
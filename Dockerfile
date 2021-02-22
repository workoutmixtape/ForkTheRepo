FROM python:3.7-slim-buster

WORKDIR /src/app

COPY requirements.txt ./requirements.txt
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

ENV PORT 8080
ENV PYTHONPATH src

COPY src/ ./src
COPY tests ./tests

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app

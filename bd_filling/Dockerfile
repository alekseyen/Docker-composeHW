FROM python:3.9.7-slim
ARG DATABASE_CONNECTION_URL
ENV DATABASE_CONNECTION_URL=${DATABASE_CONNECTION_URL}


COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY main.py .

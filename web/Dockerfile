FROM python:3.9.7-slim

COPY . web
WORKDIR web

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV PYTHONUNBUFFERED=True
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000

CMD ["flask", "run"]

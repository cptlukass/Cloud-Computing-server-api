FROM python:3.6-slim

RUN mkdir /application
WORKDIR /application

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED 1

EXPOSE 8000
STOPSIGNAL SIGINT

ENTRYPOINT["python"]
CMD["main.py"]
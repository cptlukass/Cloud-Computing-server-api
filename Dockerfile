FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev
WORKDIR /application

COPY ./requirements.txt /application/requirements.txt
RUN pip install -r requirements.txt

COPY . /application

CMD ["python", "./main.py"]

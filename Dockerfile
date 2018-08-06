FROM alpine:3.8
MAINTAINER Kamil Szymanski

ENV http_proxy http://10.158.100.1:8080
ENV https_proxy https://10.158.100.1:8080

RUN apk add python3=3.6.4-r1

ADD . /app

RUN pip3 install -r /app/requirements.txt

WORKDIR /app

EXPOSE 8000
CMD ["gunicorn", "--bind=0.0.0.0:8000", "--access-logfile=-", "--log-level=debug", "--timeout=300", "main:app"]


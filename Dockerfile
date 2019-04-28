FROM alpine:3.8
MAINTAINER Kamil Szymanski

RUN apk add python3

ADD ./app /usr/bin/app
WORKDIR /usr/bin/app
RUN pip3 install -r ./requirements.txt

EXPOSE 8000
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:8000", "--access-logfile=-", "--log-level=debug", "--timeout=300", "main:app"]


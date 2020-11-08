FROM alpine:latest

LABEL Dmitry Bikulov <docker@bikulov.org>

RUN apk add --update python3 py3-pip

COPY requirements.txt requirements.txt
COPY src /tgblog
RUN pip3 install -r requirements.txt

RUN mkdir -p /usr/share/nginx/html /data

VOLUME ["/usr/share/nginx/html", "/data"]

CMD ["python3", "/tgblog/main.py"]
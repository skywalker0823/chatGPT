FROM --platform=linux/amd64 python:3.10-alpine

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

CMD ["waitress-serve", "--port=5000", "app:app"]
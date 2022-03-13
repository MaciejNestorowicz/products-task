FROM python:3.7-alpine

WORKDIR /products

COPY requirements.txt requirements.txt

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev

RUN pip install -r requirements.txt

COPY . .

CMD [ "flask", "run", "--host=0.0.0.0"]
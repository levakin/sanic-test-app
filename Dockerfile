FROM python:3.6
MAINTAINER "<levakin levakin@protonmail.com>"

ADD . /app
WORKDIR /app

RUN pip3 install pipenv && pipenv install --system --deploy --ignore-pipfile

EXPOSE 8000


CMD ["python", "server.py"]
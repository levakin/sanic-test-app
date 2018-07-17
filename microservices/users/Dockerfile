FROM python:3.6-slim
MAINTAINER "<levakin levakin@protonmail.com>"

ADD . /app
WORKDIR /app

RUN apt-get update && \
 apt-get install --no-install-recommends -y build-essential && \
 pip3 install pipenv && \
 pipenv install --system --deploy --ignore-pipfile


EXPOSE 8000

CMD ["python", "users.py"]
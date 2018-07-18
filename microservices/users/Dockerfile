FROM python:3.6-slim
MAINTAINER "<levakin levakin@protonmail.com>"

ADD ./requirements.txt /app/requirements.txt
RUN apt-get update && \
apt-get install --no-install-recommends -y build-essential && \
pip install -r app/requirements.txt

ADD . /app
WORKDIR /app

EXPOSE 8000

CMD ["python", "users.py"]
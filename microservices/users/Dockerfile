FROM python:3.6-slim
MAINTAINER "<levakin levakin@protonmail.com>"

ADD ./requirements.txt /app
RUN apt-get update && \
 apt-get install --no-install-recommends -y build-essential && \
 pip3 install --no-cache-dir -r requirements.txt

ADD . /app
WORKDIR /app

EXPOSE 8000

CMD ["python", "users.py"]
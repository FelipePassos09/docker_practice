FROM ubuntu:latest
WORKDIR /app
COPY . .
RUN addgroup dev && adduser --system --gid 1000 application_user
RUN apt-get update && apt-get install -y locales
RUN apt-get install -y python3 python3-pip && pip install --upgrade pip && pip install -r requirements.txt
USER application_user
CMD python3 -u app.py

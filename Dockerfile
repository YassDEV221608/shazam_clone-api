FROM python:3-alpine3.18
WORKDIR /app
RUN apk add --no-cache build-base ffmpeg
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./app.py


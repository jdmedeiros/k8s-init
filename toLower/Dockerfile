# syntax=docker/dockerfile:1

FROM python:3.8-slim-bullseye

WORKDIR /python-docker

COPY . .

CMD [ "python3", "app.py"]

# Now, we can build the image with the following command:
# docker build -t python-docker .

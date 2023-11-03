# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.9-slim

RUN apt-get update
COPY requirements.txt ./
RUN pip install --upgrade -r requirements.txt

# ENV APP_HOME /src
# WORKDIR $APP_HOME
# Copy local code to the container image.
COPY src/ ./data-pipeline-test/src/
COPY .env ./data-pipeline-test/
RUN export PYTHONPATH="${PYTHONPATH}:/data-pipeline-test/"

CMD python src/main.py
# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.9-slim

RUN apt-get update
COPY requirements.txt ./
RUN pip install --upgrade -r requirements.txt

# Copy local code to the container image.
COPY src/ ./data-pipeline-test/src/
COPY .env ./data-pipeline-test/

ENV PYTHONPATH="${PYTHONPATH}:/data-pipeline-test/"
ENV APP_HOME ./data-pipeline-test/

WORKDIR $APP_HOME

CMD python src/main.py
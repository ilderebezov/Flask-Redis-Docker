# syntax=docker/dockerfile:1
FROM python:3.9-slim
WORKDIR /code
COPY . /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN pip install poetry
RUN poetry config virtualenvs.create false && poetry install
RUN pip install scipy
EXPOSE 5000
COPY . .
CMD ["flask", "run"]

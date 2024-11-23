# app/Dockerfile

FROM python:3.11-slim

WORKDIR /app
# Upgrade pip
RUN pip install --upgrade pip

COPY ./src/ /app

COPY ./pyproject.toml /code/pyproject.toml
RUN pip install /code/.

EXPOSE 8000
CMD ["sh", "entrypoint.sh"]
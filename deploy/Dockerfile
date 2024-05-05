# Use the Python image as base
FROM python:3.11.7-slim-bookworm as prod
RUN apt-get update && apt-get install -y \
  gcc \
  curl \
  && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install --upgrade pip
RUN pip install poetry

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Configuring poetry
RUN poetry config virtualenvs.create false

# Copy just the dependencies file to the working directory
COPY ./pyproject.toml /app/
# Set the working directory in the container
WORKDIR /app

# Install dependencies
RUN poetry install --no-root --no-interaction

# Removing gcc
RUN apt-get purge -y \
  gcc \
  && rm -rf /var/lib/apt/lists/*

# Copy the rest of the application code to the working directory
COPY . /app/

# Command to run the FastAPI app
CMD ["python", "-m", "app"]

FROM prod as dev

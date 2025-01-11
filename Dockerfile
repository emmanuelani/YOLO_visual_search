# Use the official Python image as the base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /main

RUN pip install --default-timeout=300 poetry
RUN pip install uvicorn 

# Copy only requirements to cache them in docker layer
COPY pyproject.toml poetry.lock* /main/

# Project initialization:
RUN poetry config virtualenvs.create false \
    && poetry install --no-root

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy the application code to the container
COPY . .

# Expose the port your FastAPI app runs on
EXPOSE 7000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7000", "--reload"]

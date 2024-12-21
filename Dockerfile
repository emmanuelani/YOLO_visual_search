# Use the official Python image as the base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /main

# Copy the requirements file to the container
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the application code to the container
COPY . .

# Expose the port your FastAPI app runs on
EXPOSE 5000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "localhost", "--port", "5000", "--reload"]

# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Install MLflow
RUN pip install mlflow

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run MLflow UI on container startup
CMD ["mlflow", "ui", "--backend-store-uri", "/app/mlruns", "--host", "0.0.0.0"]

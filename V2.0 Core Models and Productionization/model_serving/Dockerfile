# Start with the base Python image
FROM python:3.8-slim

# Install MLflow
RUN pip install mlflow

# Expose the port for serving the model
EXPOSE 1234

# Set the working directory
WORKDIR /models

# Command to serve the model
CMD ["mlflow", "models", "serve", "-m", "/mlruns/0/195f88d9d00b46eba6c88330662a6281/artifacts/xgboost_model", "--host", "0.0.0.0", "--port", "1234", "--no-conda"]

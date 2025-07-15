# Use official Python image as base.
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy app code
COPY HelloWorld.py .

# Install dependencies
RUN pip install fastapi uvicorn

# Expose the port FastAPI runs on
EXPOSE 8000

# Run the app
CMD ["uvicorn", "HelloWorld:app", "--host", "0.0.0.0", "--port", "8000"]

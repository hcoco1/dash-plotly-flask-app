# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY backend/requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set the environment variable for Python to run in unbuffered mode (helpful for Docker logging)
ENV PYTHONUNBUFFERED=1

# Set the PYTHONPATH environment variable
ENV PYTHONPATH=/app

# Expose the port that the app runs on
EXPOSE 5000

# Run the application
CMD ["python", "backend/run.py"]


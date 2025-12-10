# Use an official lightweight Python image.
# 3.12-slim is a good choice for size and compatibility.
FROM python:3.12-slim

# Set environment variables to ensure output is sent straight to terminal (no buffering)
# and to prevent Python from writing pyc files.
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY lang.py .
COPY .env .

# Define the command to run the application (Interactive CLI)
CMD ["python", "lang.py"]
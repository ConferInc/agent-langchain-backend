# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

# Expose the FastAPI port
EXPOSE 4000

# Start FastAPI server
CMD ["uvicorn", "lang:app", "--host", "0.0.0.0", "--port", "4000"]

# Use a Python base image
FROM python:3.9-slim

# Install SQLite CLI tool 
RUN apt update && apt install -y sqlite3

# Set the working directory
WORKDIR /app

# Copy the application files
COPY . /app

# Install required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]


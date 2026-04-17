# Use a lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies (Minimal)
RUN pip install --no-cache-dir flask

# Copy project files
COPY . .

# Expose the Flask port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
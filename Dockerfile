# Use an official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY app/ .

# Expose the port Flask runs on
EXPOSE 4000

# Run the app
CMD ["python", "app.py"]
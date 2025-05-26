<<<<<<< HEAD
# Use an official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY app/ .

# Expose port 80 (same as Flask app port)
EXPOSE 80

# Run the app
=======
# Use an official Python runtime as a parent image
FROM python:3.12-slim-bookworm

# Set the working directory to /app
WORKDIR /app

# Copy requirements.txt into the container at /app
COPY app/requirements.txt requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY app/ /app

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
>>>>>>> 1673cbea3e70b9ac13e44eac91b1d9f39a1c72a8
CMD ["python", "app.py"]
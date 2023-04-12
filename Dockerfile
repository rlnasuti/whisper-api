# Use an official Python base image
FROM python:3.10

# Install Nginx
RUN apt-get update && apt-get install -y nginx ffmpeg

# Set the working directory inside the container
WORKDIR /app

# Expose the port that Nginx will listen on
EXPOSE 80 5002

# Copy the requirements.txt file into the container
COPY requirements.txt /app/

# Install Python dependencies from the requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Nginx configuration file into the container
COPY nginx.conf /etc/nginx/sites-enabled/default

# Copy the application code into the container
COPY whisperapi.py /app/

# Define the entry point for the container
CMD ["sh", "-c", "nginx && python whisperapi.py"]

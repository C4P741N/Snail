# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Install necessary system packages: chromium, chromium-driver, and utilities
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    gnupg \
    --no-install-recommends && \
    # Install Chromium browser and the Chrome driver
    apt-get install -y chromium chromium-driver && \
    # Clean up to reduce image size
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set environment variables to tell Selenium where to find the browser and driver
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROME_DRIVER=/usr/bin/chromedriver

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file first (for better caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application's code
COPY . .

# Command to run your script (you'll override this for debugging)
CMD ["python", "your_bot.py"]
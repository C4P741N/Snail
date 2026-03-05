
# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Install necessary system packages: chromium, chromium-driver, and utilities
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    wget=1.21.* \
    unzip=6.0* \
    curl=7.88.* \
    gnupg=2.2.* \
    chromium=123.* \
    chromium-driver=123.* \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set environment variables to tell Selenium where to find the browser and driver
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROME_DRIVER=/usr/bin/chromedriver

# Create a non-root user to run the app
RUN useradd -m appuser
USER appuser

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file first (for better caching)
COPY --chown=appuser:appuser requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application's code
COPY --chown=appuser:appuser . .

# Use ENTRYPOINT for better override flexibility
ENTRYPOINT ["python"]
# Set default command (change to your actual script)
CMD ["main.py"]
# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install necessary packages
RUN apt-get update && apt-get install -y \
    gnupg2 \
    wget \
    unzip \
    xvfb \
    libxi6 \
    libgconf-2-4 \
    libnss3 \
    default-jdk \
    && apt-get clean

# Install Google Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list' \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && apt-get clean

# Install ChromeDriver
RUN CHROME_DRIVER_VERSION=$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE) && \
    wget -N http://chromedriver.storage.googleapis.com/${CHROME_DRIVER_VERSION}/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    rm chromedriver_linux64.zip && \
    mv chromedriver /usr/local/bin/chromedriver && \
    chmod +x /usr/local/bin/chromedriver

# Install git
RUN apt-get update && apt-get install -y git && apt-get clean

# Install any needed packages specified in requirements.txt
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Remove existing contents in the /app directory to avoid conflicts
RUN rm -rf /app/*

# Clone the latest version of the repository
RUN git clone https://github.com/GitGans/VezubrWebAuto.git .

# Copy Linux ChromeDriver to the correct directory
COPY ./resource/linux/chromedriver /app/resource/linux/chromedriver
RUN chmod +x /app/resource/linux/chromedriver

# Copy specific files (if needed)
COPY ./pages/login.py ./pages/login.py

# Run Xvfb and then the tests
CMD ["sh", "-c", "Xvfb :99 -ac & export DISPLAY=:99 && pytest ${PYTEST_TARGET}"]

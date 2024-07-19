# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Update and install necessary packages
RUN apt-get update && apt-get install -y gnupg2

# Install other necessary packages step by step for better diagnostics
RUN apt-get update && apt-get install -y wget
RUN apt-get update && apt-get install -y unzip
RUN apt-get update && apt-get install -y libxi6
RUN apt-get update && apt-get install -y libgconf-2-4
RUN apt-get update && apt-get install -y libnss3
RUN apt-get update && apt-get install -y default-jdk
RUN apt-get update && apt-get install -y curl
RUN apt-get update && apt-get install -y nodejs
RUN apt-get update && apt-get install -y npm
RUN apt-get update && apt-get install -y git
RUN apt-get update && apt-get install -y libgbm-dev
RUN apt-get update && apt-get install -y libasound2
RUN apt-get clean

# Install Google Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list' && \
    apt-get update && apt-get install -y google-chrome-stable && apt-get clean

# Install ChromeDriver using npm
RUN npm install -g chromedriver

# Install any needed packages specified in requirements.txt
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Remove existing contents in the /app directory to avoid conflicts
RUN rm -rf /app/*

# Clone the latest version of the repository
RUN git clone https://github.com/GitGans/VezubrWebAuto.git /app

# Copy Linux ChromeDriver to the correct directory
COPY ./resource/linux/chromedriver /app/resource/linux/chromedriver
RUN chmod +x /app/resource/linux/chromedriver

# Copy specific files (if needed)
COPY ./pages/login.py ./pages/login.py

# Set environment variable for Pytest target
ENV PYTEST_TARGET=tests/test_user_add_lkp.py

# Run the tests
ENTRYPOINT ["sh", "-c", "pytest ${PYTEST_TARGET}"]

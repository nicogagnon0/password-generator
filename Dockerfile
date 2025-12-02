# Dockerfile for the Password Generator app
# Use an official lightweight Python image
FROM python:3.12-slim
 
# Set working directory inside the container
WORKDIR /app
 
# Copy the application file into the container
COPY app.py /app/app.py
 
# Set the default command to run the application
CMD ["python", "app.py"]
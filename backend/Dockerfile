# Use the official Python image from the Docker Hub
FROM python:3.9.20-slim-bullseye
# Set the working directory inside the container
WORKDIR /backend/

# Copy the application files to the working directory
COPY app.py /backend/
COPY config.py /backend/
COPY models.py /backend/
COPY requirements.txt /backend/

# Install the required dependencies
RUN pip install -r requirements.txt

# Expose the port the app will run on
EXPOSE 5000

# Set the command to run Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]

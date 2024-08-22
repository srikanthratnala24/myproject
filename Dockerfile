# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy Pipfile and Pipfile.lock
COPY Pipfile Pipfile.lock /app/

RUN apt-get update && apt-get install -y libpq-dev


# Install pipenv and dependencies
RUN pip install pipenv && pipenv install --deploy --ignore-pipfile

# Copy the rest of the application code
COPY . /app/

# Expose port 8000 for the app
EXPOSE 8000

# Set environment variable for Django settings
ENV DJANGO_SETTINGS_MODULE=myproject.settings

# Run Gunicorn server
CMD ["pipenv", "run", "gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]

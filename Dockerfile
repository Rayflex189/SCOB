# Use official Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_ROOT_USER_ACTION=ignore

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY SCOB/requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the full Django project
COPY SCOB/ /app/

# Run Django setup commands
RUN python manage.py collectstatic --no-input
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py create_admin

# Expose port
EXPOSE 8000

# Start server
CMD ["gunicorn", "SCOB.wsgi:application", "--bind", "0.0.0.0:8000"]
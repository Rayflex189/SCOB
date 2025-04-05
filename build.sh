#!/usr/bin/env bash
# Exit on any error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Create any new migrations based on model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate --no-input

# Optional: Start the app server (uncomment and adjust if needed)
# gunicorn project_name.wsgi:application

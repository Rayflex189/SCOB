#!/usr/bin/env bash

# Exit immediately if a command exits with a non-zero status
set -o errexit

# Install Python dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py makemigrations
python manage.py migrate --noinput

# Collect static files for production
python manage.py collectstatic --no-input

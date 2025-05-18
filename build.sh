#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Make fresh migrations
python manage.py makemigrations

# Apply migrations with fake initial if tables already exist
python manage.py migrate --fake-initial

# Collect static files
python manage.py collectstatic --no-input

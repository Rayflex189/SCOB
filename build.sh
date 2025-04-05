#!/usr/bin/env bash
# Exit on any error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Create new migration files for model changes
python manage.py makemigrations

# Fake apply migration for bank_app to avoid "table already exists" error
#python manage.py migrate bank_app --fake

# Apply all outstanding real migrations
python manage.py migrate --no-input

# Optional: Start the server (uncomment and set your project name)
# gunicorn project_name.wsgi:application

#!/usr/bin/env bash
# Exit on any error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Recreate migration files
find bank_app/migrations/ -type f -not -name '__init__.py' -delete

python manage.py makemigrations bank_app

# Apply them with --fake to tell Django the schema already exists
python manage.py migrate bank_app --fake
# Optional: Start the server (uncomment and set your project name)
# gunicorn project_name.wsgi:application

#!/bin/sh

# Exit immediately if a command exits with a non-zero status
set -e

echo "🔄 Running database migrations..."
python manage.py migrate --noinput

echo "✅ Migrations applied!"

# Create superuser if not exists
echo "👤 Ensuring superuser exists..."

# Use environment variables passed in via .env
python manage.py shell << END
from django.contrib.auth import get_user_model
import os

User = get_user_model()
username = os.environ.get('SUPERUSER_USERNAME')
email = os.environ.get('SUPERUSER_EMAIL')
password = os.environ.get('SUPERUSER_PASSWORD')

if username and email and password:
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print("✅ Superuser created.")
    else:
        print("ℹ️ Superuser already exists.")
else:
    print("⚠️ Missing SUPERUSER_USERNAME, SUPERUSER_EMAIL, or SUPERUSER_PASSWORD.")
END

# Start the Django development server
echo "🚀 Starting Django server..."
exec python manage.py runserver 0.0.0.0:8000

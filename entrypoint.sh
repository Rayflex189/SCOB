#!/bin/sh

set -e  # Exit on error

echo "🔄 Running database migrations..."
python manage.py migrate --noinput
echo "✅ Migrations applied!"

echo "👤 Checking for existing superuser..."

python manage.py shell << END
import os
from django.contrib.auth import get_user_model

User = get_user_model()
username = os.environ.get('SUPERUSER_USERNAME')
email = os.environ.get('SUPERUSER_EMAIL')
password = os.environ.get('SUPERUSER_PASSWORD')

if username and email and password:
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print(f"✅ Superuser '{username}' created successfully.")
    else:
        print(f"ℹ️ Superuser '{username}' already exists. Skipping creation.")
else:
    print("⚠️ SUPERUSER_USERNAME, SUPERUSER_EMAIL, or SUPERUSER_PASSWORD not set.")
END

echo "🚀 Starting Django development server..."
exec python manage.py runserver 0.0.0.0:8000

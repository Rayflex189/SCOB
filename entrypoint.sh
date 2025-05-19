#!/bin/sh

set -e  # Exit on error

echo "🔄 Running makemigrations..."
python manage.py makemigrations --noinput
echo "✅ Makemigrations completed!"

echo "🔄 Running database migrations..."
python manage.py migrate --noinput
echo "✅ Migrations applied!"

echo "👤 Deleting old superuser (if exists) and creating new one..."

python manage.py shell << END
import os
from django.contrib.auth import get_user_model

User = get_user_model()
username = os.environ.get('SUPERUSER_USERNAME')
email = os.environ.get('SUPERUSER_EMAIL')
password = os.environ.get('SUPERUSER_PASSWORD')

if username and email and password:
    user = User.objects.filter(username=username).first()
    if user:
        user.delete()
        print(f"🗑️ Existing superuser '{username}' deleted.")
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"✅ New superuser '{username}' created successfully.")
else:
    print("⚠️ SUPERUSER_USERNAME, SUPERUSER_EMAIL, or SUPERUSER_PASSWORD not set.")
END

echo "🚀 Starting Django development server..."
exec python manage.py runserver 0.0.0.0:8000

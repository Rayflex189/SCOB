#!/bin/bash
set -e

# Run Django setup
python manage.py collectstatic --no-input
python manage.py migrate

# Create admin user only if not exists
if [ "$DJANGO_SUPERUSER_USERNAME" ] && [ "$DJANGO_SUPERUSER_PASSWORD" ] && [ "$DJANGO_SUPERUSER_EMAIL" ]; then
    python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username="${DJANGO_SUPERUSER_USERNAME}").exists():
    User.objects.create_superuser(
        username="${DJANGO_SUPERUSER_USERNAME}",
        email="${DJANGO_SUPERUSER_EMAIL}",
        password="${DJANGO_SUPERUSER_PASSWORD}"
    )
EOF
fi

# Start Gunicorn
exec gunicorn SCOB.wsgi:application --bind 0.0.0.0:8080
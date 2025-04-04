import os
import django
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command
from django.contrib.auth import get_user_model
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SCOB.settings')

# Initialize Django
django.setup()

# Run database migrations on every server start
try:
    print("Running database migrations...")
    call_command('migrate', interactive=False)
    print("Migrations completed successfully!")
except Exception as e:
    print(f"Migration Error: {e}")

# Function to ensure a superuser exists
def create_superuser():
    """
    Ensures a permanent superuser is created at server startup.
    """
    User = get_user_model()
    username = settings.SUPERUSER_USERNAME
    email = settings.SUPERUSER_EMAIL
    password = settings.SUPERUSER_PASSWORD

    if username and email and password:  # Ensure credentials are set
        superuser, created = User.objects.get_or_create(username=username, defaults={'email': email})
        if created:
            superuser.set_password(password)
            superuser.is_superuser = True
            superuser.is_staff = True
            superuser.save()
            print(f"Superuser '{username}' created successfully.")
        else:
            print(f"Superuser '{username}' already exists.")
    else:
        print("Superuser credentials are missing. Skipping creation.")

create_superuser()

# Get the WSGI application
application = get_wsgi_application()
app = application  # Alias for compatibility with some hosting services

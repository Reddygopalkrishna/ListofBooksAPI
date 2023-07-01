# settings.py

INSTALLED_APPS = [
    ...
    'rest_framework',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

# Generate a secret key for JWT authentication
from django.core.management.utils import get_random_secret_key

SECRET_KEY = get_random_secret_key()

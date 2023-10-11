from vms_django_rest_api.settings import *

# ALLOWED HOSTS
ALLOWED_HOSTS = ["*"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# DATABASE
DATABASES = {
    "default": {
        # "ENGINE": "django.db.backends.postgresql_psycopg2",
        "ENGINE": "django_tenants.postgresql_backend",
        "NAME": config("DATABASE_NAME-STAGING"),
        "USER": config("DATABASE_USER-STAGING"),
        "PASSWORD": config("DATABASE_PASSWORD-STAGING"),
        "HOST": config("DATABASE_HOST-STAGING"),
        "PORT": config("DATABASE_PORT-STAGING"),
    }
}

# Security

# security.W004
SECURE_HSTS_SECONDS = 31536000  # One year in seconds

# security.W008
SECURE_SSL_REDIRECT = False

# security.W012
SESSION_COOKIE_SECURE = True

# Extra security settings
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True

# AWS S3 Config
# AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID-STAGING")
# AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY-STAGING")
# AWS_STORAGE_BUCKET_NAME = config("AWS_STORAGE_BUCKET_NAME-STAGING")

# CORS
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]

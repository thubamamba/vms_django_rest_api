from vms_django_rest_api.settings import *

ALLOWED_HOSTS = ["*"]

DEBUG = True

# EMAIL CONFIG - Uses Mailhog (https://github.com/mailhog/MailHog)
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "localhost"
EMAIL_PORT = "1025"
EMAIL_HOST_USER = "0.0.0.0"
EMAIL_HOST_PASSWORD = ""
EMAIL_USE_TLS = False

# DATABASE CONFIG
DATABASES = {
    "default": {
        # "ENGINE": "django.db.backends.postgresql_psycopg2",
        "ENGINE": "django_tenants.postgresql_backend",
        "NAME": config("DATABASE_NAME-DEV"),
        "USER": config("DATABASE_USER-DEV"),
        "PASSWORD": config("DATABASE_PASSWORD-DEV"),
        "HOST": "localhost",
        "PORT": "",
    }
}
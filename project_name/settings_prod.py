from {{ project_name }}.settings import *

ADMINS = MANAGERS = (
    ('admin', 'root@localhost')
)

DEFAULT_FROM_EMAIL = SERVER_EMAIL = 'webmaster@localhost'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
#EMAIL_HOST_USER =
#EMAIL_HOST_PASSWORD =
#EMAIL_PORT = 587
#EMAIL_USE_TLS = True

SECRET_KEY = environ.get('DJANGO_SECRET', SECRET_KEY)

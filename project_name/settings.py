"""Django settings module"""
from os import environ, path

DEBUG = TEMPLATE_DEBUG = environ.get('DJANGO_DEBUG', '1') == '1'
DJANGO_HOME = environ.get('DJANGO_HOME', '')

SECRET_KEY = environ.get(
    'DJANGO_SECRET',
    '{{ secret_key }}'
)

ADMINS = (
    ('admin', 'root@localhost')
)

ALLOWED_HOSTS = ['localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': path.join(DJANGO_HOME, 'default.db'),
        'CONN_MAX_AGE': None,
        'OPTIONS': {
            'timeout': 10,
        },
    },
}

DEFAULT_FROM_EMAIL = SERVER_EMAIL = 'webmaster@localhost'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' \
    if DEBUG else 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'localhost'
#EMAIL_HOST_USER =
#EMAIL_HOST_PASSWORD =
#EMAIL_PORT = 587
EMAIL_SUBJECT_PREFIX = '[{{ project_name }}] '
#EMAIL_USE_TLS = True

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    '{{ project_name }}.main',
)

LANGUAGE_CODE = 'pt-br'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,

    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },

    'formatters': {
        'default': {
            'format': '%(asctime)s <%(name)s:%(levelname)s> %(message)s'
        },
        'debug': {
            'format': '%(asctime)s <%(name)s:%(levelname)s>'
                      ' [%(module)s:%(process)d:%(thread)d] %(message)s'
        },
    },

    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        'default': {
            'level': 'DEBUG' if DEBUG else 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'debug' if DEBUG else 'default',
            'filename': path.join(DJANGO_HOME, '{{ project_name }}.log'),
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
    },

    'loggers': {
        '{{ project_name }}': {
            'handlers': ['console', 'default'],
            'level': 'DEBUG' if DEBUG else 'INFO',
        },
        'django': {
            'handlers': ['console', 'default'],
            'level': 'DEBUG' if DEBUG else 'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.security': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'py.warnings': {
            'handlers': ['console'],
        },
    },
}

MEDIA_ROOT = path.join(DJANGO_HOME, 'media')

MEDIA_URL = '/media/'

ROOT_URLCONF = '{{ project_name }}.main.urls'

STATIC_ROOT = path.join(DJANGO_HOME, 'static')

STATIC_URL = '/static/'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


import json

for f in ['/etc/{{ project_name }}.json',
          path.expanduser('~/.{{ project_name }}.json'),
          '{{ project_name }}.json']:

    if path.exists(f):
        with open(f) as fp:
            cfg_dict = json.load(fp)

            locals().update(cfg_dict)

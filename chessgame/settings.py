import os
import secrets

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True


# Generate a new secret key if it's not already set
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', secrets.token_hex(32))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

INSTALLED_APPS = [
    # other apps
    'chess',
    'django.contrib.auth',
    'django.contrib.contenttypes',
  # Add your Django app name here
]

ROOT_URLCONF = 'chessgame.urls'

ALLOWED_HOSTS = ['127.0.0.1']

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     # 'handlers': {
#     #     'file': {
#     #         'level': 'ERROR',
#     #         'class': 'logging.FileHandler',
#     #         'filename': '/var/log/myapp.log',
#     #     },
#     # },
#     'root': {
#         'handlers': ['file'],
#         'level': 'ERROR',
#     },
# }
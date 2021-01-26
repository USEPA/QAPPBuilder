# Local_settings.py (QAPP_Builder)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov

"""
Local Django settings for QAPP_Builder project.

Available functions:
- Settings in this file are for developer/engineer to run on localhost.
- DO NOT CHANGE!
"""

SITE_NAME = 'https://134.67.216.106/accounts/login'

DEFAULT_FROM_EMAIL = 'young.daniel@epa.gov'
EMAIL_HOST = '134.67.216.102'
EMAIL_HOST_USER = 'dyoung11'
EMAIL_HOST_PASSWORD = '***REMOVED***'
EMAIL_PORT = 25
EMAIL_FILE_PATH = '/var/www/html/QAPP_Builder/uploads'

USER_APPROVAL_EMAIL = [
    'young.daniel@epa.gov',
    'meyer.david@epa.gov',
    'gonzalez.michael@epa.gov',
]

# SECURITY WARNING: Keep the secret key used in production secret!
SECRET_KEY = 'z&&=(=sm60$x+8asdkcgfehrgc5k^5^_6q@=-uychcf$j1a-&d53u!('

# SECURITY WARNING: Do not run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = []
if DEBUG is True:
    ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.v2626umcth937.rtord.epa.gov',
                     'https://plasticsprojects.epa.gov/qar5/', '134.67.216.106']
else:
    ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.v2626umcth937.rtord.epa.gov',
                     'https://plasticsprojects.epa.gov/qar5/', '134.67.216.106']

BASE_URL = 'http://127.0.0.1'
# BASE_URL = 'https://134.67.216.106' 'v2626umcth937.rtord.epa.gov'
# EPA RTP assigned IP. Note: Need Jake or Raghu to verify BASE_URL, this app
# will only run on RTP RHEL not STREAMS.

DJANGO_SETTINGS_MODULE = 'QAPP_Builder.settings'

ROOT_URLCONF = 'QAPP_Builder.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'QAPP_Builder',
        'USER': 'postgres',
        'PASSWORD': '***REMOVED***',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}

LOGIN_REDIRECT_URL = '/dashboard/'

# settings.py (qapp_builder)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov
# pylint: disable=W0614, W0401

"""
Django settings for qapp_builder project.

Based on 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from ms_identity_web.configuration import AADConfig
from ms_identity_web import IdentityWebPython

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f457efab-86f5-44e4-82e7-be47e4714b04'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.v2626umcth937.rtord.epa.gov',
                 'https://plasticsprojects.epa.gov/qar5/', '134.67.216.106']

# Application references
# https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-INSTALLED_APPS
INSTALLED_APPS = [
    # Add your apps here to enable them
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'constants',
    'qapp_builder',
    'support',
    'teams'
]

# Middleware framework
# https://docs.djangoproject.com/en/2.1/topics/http/middleware/
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'qapp_builder.middleware.AuthenticationMiddlewareExempt',
]

ROOT_URLCONF = 'qapp_builder.urls'

# Template configuration
# https://docs.djangoproject.com/en/2.1/topics/templates/
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

WSGI_APPLICATION = 'qapp_builder.wsgi.application'
# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # noqa:E501
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # noqa:E501
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # noqa:E501
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # noqa:E501
    },
]

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'qapp_builder', 'static')

DOWNLOADS_DIR = os.path.join(BASE_DIR, '..', 'docs')

MEDIA_ROOT = os.path.join(BASE_DIR, 'qapp_builder/media')
MEDIA_URL = '/media/'

# We keep upload root separate from STATIC and MEDIA to keep it more secure.
# UPLOAD_ROOT will not be accessible from URL, only by the server views.
UPLOAD_ROOT = os.path.join(MEDIA_ROOT, 'uploads')

APP_NAME = 'qapp_builder'
APP_VERSION = '1.3.0.alpha1'
APP_DISCLAIMER = 'The information and data presented in this product ' + \
                 'were obtained from sources that are believed to be ' + \
                 'reliable. However, in many cases the quality of the ' + \
                 'information or data was not documented by those ' + \
                 'sources; therefore, no claim is made regarding ' + \
                 'their quality.'

# Azure AD Auth section:
AAD_CONFIG = AADConfig.parse_json(file_path='aad.config.json')
MS_IDENTITY_WEB = IdentityWebPython(AAD_CONFIG)
# for rendering 401 or other errors from msal_middleware
ERROR_TEMPLATE = 'auth/{}.html'
MIDDLEWARE.append('ms_identity_web.django.middleware.MsalMiddleware')

# localhost vs 127.0.0.1
SESSION_COOKIE_DOMAIN = 'localhost'

try:
    from .local_settings import *  # noqa:F401
except ImportError:
    pass

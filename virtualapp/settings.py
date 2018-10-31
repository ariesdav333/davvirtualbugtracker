# uncompyle6 version 3.2.3
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.4.3 (default, Nov 17 2016, 01:08:31) 
# [GCC 4.8.4]
# Embedded file name: /home/ubuntu/workspace/virtualapp/virtualapp/settings.py
# Compiled at: 2018-10-17 20:14:33
"""
Django settings for virtualapp project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
import os, env
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '-udg$)e-x7)&pg@3ws6nsgr@c&l-5lkc_*_x-i))1!9iwv3tu5'
DEBUG = True
ALLOWED_HOSTS = ['davsoftware-airesdav333.c9users.io']

INSTALLED_APPS = [
 'django.contrib.admin',
 'django.contrib.auth',
 'django.contrib.contenttypes',
 'django.contrib.sessions',
 'django.contrib.messages',
 'django.contrib.staticfiles',
 'django_forms_bootstrap',
 'accounts',
 'tinymce',
 'emoticons',
 'threads',
 'polls',
 ]
 
 
 
MIDDLEWARE = [
 'django.middleware.security.SecurityMiddleware',
 'django.contrib.sessions.middleware.SessionMiddleware',
 'django.middleware.common.CommonMiddleware',
 'django.middleware.csrf.CsrfViewMiddleware',
 'django.contrib.auth.middleware.AuthenticationMiddleware',
 'django.contrib.messages.middleware.MessageMiddleware',
 'django.middleware.clickjacking.XFrameOptionsMiddleware']
 
ROOT_URLCONF = 'virtualapp.urls'

TEMPLATES = [
 {'BACKEND': 'django.template.backends.django.DjangoTemplates', 
    'DIRS': [
           os.path.join(BASE_DIR, 'templates')], 
    'APP_DIRS': True, 
    'OPTIONS': {'context_processors': [
                                     'django.template.context_processors.debug',
                                     'django.template.context_processors.request',
                                     'django.contrib.auth.context_processors.auth',
                                     'django.contrib.messages.context_processors.messages',
                                     'django.template.context_processors.media'], 
                'libraries': {'thread_extras': 'threads.templatetags.thread_extras'}}}]
                
                
WSGI_APPLICATION = 'virtualapp.wsgi.application'
DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 
               'NAME': os.path.join(BASE_DIR, 'db.sqlite3')}}
AUTH_PASSWORD_VALIDATORS = [
 {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
 {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
 {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
 {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}]
 
AUTHENTICATION_BACKENDS = (
 'django.contrib.auth.backends.ModelBackend',
 'accounts.backends.EmailAuth'
 )
 
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (
 os.path.join(BASE_DIR, 'static'),)
TINYMCE_JS_ROOT = os.path.join(BASE_DIR, 'static', 'js', 'tinymce', 'tinymce.min.js')
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('EMAIL_ADDRESS')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD')
EMAIL_PORT = 587
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STRIPE_PUBLISHABLE = os.getenv('pk_test_bAUe7yN1i8MVOYOkHHGH6Aw2')
STRIPE_SECRET = os.getenv('sk_test_RA7pSAvvb0paKcilT0MYcZGV')

AUTH_USER_MODEL = 'accounts.User' 







# okay decompiling settings.pyc

from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-pd^m&jxq&tacq*0diz1-w%od99a7v&if_p1#fwjd&bojt&_tbx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mysite',
        'USER': 'django',
        'PASSWORD': 'qwerty',
        'HOST': 'db',
        'PORT': '54325',
    }
}

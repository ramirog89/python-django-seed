from ..settings import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*_jxj=m9p5c0&_58w4()7yb4d*_bu8+jv(=i=$$wc2hku7k3r5'

ALLOWED_HOSTS = ['localhost', 'python-django-starter.herokuapp.com']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'database/db.sqlite3',
    }
}